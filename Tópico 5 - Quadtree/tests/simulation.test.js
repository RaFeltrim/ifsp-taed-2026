const test = require('node:test');
const assert = require('node:assert/strict');
const { Particle } = require('../src/particle.js');
const { Rect, Quadtree } = require('../src/quadtree.js');
const { Simulation, findPairsBruteForce, findPairsQuadtree, buildTrace, findPairStepIndex } = require('../src/simulation.js');

// Cria `count` partículas aleatórias e uma Quadtree com elas.
function randomScene(count, radius, width, height) {
  const sim = new Simulation(width, height);
  sim.reset(count, radius, width, height);
  const tree = new Quadtree(new Rect(0, 0, width, height));
  for (const p of sim.particles) tree.insert(p);
  return { particles: sim.particles, tree };
}

// Chave de par independente da ordem, para comparar conjuntos de pares.
const pairKey = ([a, b]) => `${Math.min(a.id, b.id)}-${Math.max(a.id, b.id)}`;

test('findPairsBruteForce testa n(n-1)/2 pares', () => {
  const sim = new Simulation(800, 600);
  sim.reset(200, 4, 800, 600);
  assert.equal(findPairsBruteForce(sim.particles).tests, 19900);

  const one = findPairsBruteForce([new Particle(0, 10, 10, 0, 0, 4)]);
  assert.equal(one.tests, 0);
  assert.equal(one.pairs.length, 0);
});

test('findPairsBruteForce encontra exatamente os pares sobrepostos', () => {
  const particles = [
    new Particle(0, 10, 10, 0, 0, 5),
    new Particle(1, 15, 10, 0, 0, 5), // sobrepõe 0
    new Particle(2, 100, 100, 0, 0, 5),
    new Particle(3, 104, 100, 0, 0, 5), // sobrepõe 2
    new Particle(4, 300, 300, 0, 0, 5), // isolada
  ];
  const { pairs } = findPairsBruteForce(particles);
  assert.deepEqual(pairs.map(pairKey).sort(), ['0-1', '2-3']);
});

test('reset cria partículas com o raio pedido dentro da área', () => {
  const sim = new Simulation(800, 600);
  sim.reset(300, 16, 800, 600);
  assert.equal(sim.particles.length, 300);
  sim.particles.forEach((p, i) => {
    assert.equal(p.id, i);
    assert.equal(p.r, 16);
    assert.ok(p.x >= 16 && p.x <= 800 - 16);
    assert.ok(p.y >= 16 && p.y <= 600 - 16);
  });
});

test('step marca como colidindo só as partículas sobrepostas', () => {
  const sim = new Simulation(400, 400);
  sim.particles = [
    new Particle(0, 100, 100, 0, 0, 5),
    new Particle(1, 106, 100, 0, 0, 5),
    new Particle(2, 300, 300, 0, 0, 5),
  ];
  sim.step();
  assert.equal(sim.particles[0].colliding, true);
  assert.equal(sim.particles[1].colliding, true);
  assert.equal(sim.particles[2].colliding, false);
  assert.equal(sim.tests, 3);
});

test('findPairsQuadtree encontra os mesmos pares que a força bruta', () => {
  const { particles, tree } = randomScene(500, 8, 800, 600);
  const brute = findPairsBruteForce(particles);
  const quad = findPairsQuadtree(particles, tree);

  const quadKeys = quad.pairs.map(pairKey);
  assert.equal(new Set(quadKeys).size, quadKeys.length, 'sem pares duplicados');
  assert.deepEqual(quadKeys.sort(), brute.pairs.map(pairKey).sort());
  assert.ok(quad.tests < brute.tests);
});

test('com 1000 partículas a Quadtree faz no máximo 1/10 dos testes (SC-002)', () => {
  const { particles, tree } = randomScene(1000, 4, 1600, 900);
  const brute = findPairsBruteForce(particles);
  const quad = findPairsQuadtree(particles, tree);
  assert.ok(quad.tests <= brute.tests / 10, `${quad.tests} vs ${brute.tests}`);
});

test('step usa o modo escolhido', () => {
  const sim = new Simulation(1600, 900);
  sim.reset(1000, 4, 1600, 900);
  sim.mode = 'brute';
  sim.step();
  assert.equal(sim.tests, 499500);
  sim.mode = 'quadtree';
  sim.step();
  assert.ok(sim.tests < 49950);
});

test('seleção marca exatamente as partículas com centro dentro da região', () => {
  const sim = new Simulation(400, 400);
  sim.particles = [
    new Particle(0, 50, 50, 0, 0, 4),
    new Particle(1, 80, 60, 0, 0, 4),
    new Particle(2, 200, 200, 0, 0, 4),
    new Particle(3, 350, 30, 0, 0, 4),
  ];
  sim.setSelection(new Rect(40, 40, 100, 100));
  sim.step();
  assert.deepEqual(sim.particles.map((p) => p.selected), [true, true, false, false]);
  assert.equal(sim.selectedCount, 2);

  sim.setSelection(null);
  sim.step();
  assert.ok(sim.particles.every((p) => !p.selected));
  assert.equal(sim.selectedCount, 0);
});

test('reset limpa a seleção', () => {
  const sim = new Simulation(400, 400);
  sim.setSelection(new Rect(0, 0, 100, 100));
  sim.reset(10, 4, 400, 400);
  assert.equal(sim.selection, null);
});

test('step equivale a moveAndBuildTree + detectAndResolve', () => {
  const make = () => {
    const sim = new Simulation(400, 400);
    sim.particles = [
      new Particle(0, 100, 100, 1, 0, 8),
      new Particle(1, 112, 100, -1, 0, 8), // sobrepõe a 0 depois de mover
      new Particle(2, 300, 300, 0, 1, 8),
    ];
    return sim;
  };
  const a = make();
  a.step();
  const b = make();
  b.moveAndBuildTree();
  b.detectAndResolve();
  const state = (sim) => sim.particles.map((p) => [p.x, p.y, p.vx, p.vy, p.colliding]);
  assert.deepEqual(state(a), state(b));
  assert.equal(a.particles[0].colliding, true);
});

// Pares com colisão registrados no trace, como chaves "menor-maior".
const tracePairKeys = (steps) =>
  steps.filter((s) => s.type === 'test' && s.overlap).map((s) => pairKey([s.p, s.q])).sort();

// Confere que o trace faz os mesmos testes e acha os mesmos pares que `expected`.
function assertTraceMatches(steps, expected) {
  const last = steps[steps.length - 1];
  assert.equal(steps.filter((s) => s.type === 'test').length, expected.tests);
  assert.equal(last.tests, expected.tests);
  assert.equal(last.collisions, expected.pairs.length);
  assert.deepEqual(tracePairKeys(steps), expected.pairs.map(pairKey).sort());
}

test('buildTrace em força bruta: mesmos testes e pares, um passo por partícula', () => {
  const { particles, tree } = randomScene(300, 8, 800, 600);
  const steps = buildTrace(particles, tree, 'brute');
  assertTraceMatches(steps, findPairsBruteForce(particles));

  assert.equal(steps[0].type, 'particle');
  assert.equal(steps.some((s) => s.type === 'visit'), false);
  const particleSteps = steps.filter((s) => s.type === 'particle');
  assert.equal(particleSteps.length, 300);
  assert.ok(particleSteps.every((s) => s.range === null));
  for (let i = 1; i < steps.length; i++) {
    assert.ok(steps[i].tests >= steps[i - 1].tests);
    assert.ok(steps[i].collisions >= steps[i - 1].collisions);
  }
});

test('buildTrace em Quadtree: mesmos testes e pares da detecção normal', () => {
  const { particles, tree } = randomScene(300, 8, 800, 600);
  assertTraceMatches(buildTrace(particles, tree, 'quadtree'), findPairsQuadtree(particles, tree));
});

test('buildTrace em Quadtree mostra o caminho com os testes intercalados', () => {
  const { particles, tree } = randomScene(300, 8, 800, 600);
  const steps = buildTrace(particles, tree, 'quadtree');
  assertTraceMatches(steps, findPairsQuadtree(particles, tree));

  const particleSteps = steps.filter((s) => s.type === 'particle');
  assert.equal(particleSteps.length, 300);
  for (const s of particleSteps) {
    assert.equal(s.range.w, 4 * s.p.r);
    assert.equal(s.range.x + s.range.w / 2, s.p.x);
    assert.equal(s.range.y + s.range.h / 2, s.p.y);
  }
  assert.ok(steps.some((s) => s.type === 'visit' && s.hit));

  // Cada teste vem logo depois da visita ao nó que contém a candidata.
  let lastVisit = null;
  for (const s of steps) {
    if (s.type === 'particle') lastVisit = null;
    if (s.type === 'visit') lastVisit = s;
    if (s.type === 'test') {
      assert.ok(lastVisit && lastVisit.p === s.p && lastVisit.hit, 'teste sem visita antes');
      assert.ok(lastVisit.node.items.includes(s.q), 'candidata não está no nó visitado');
    }
  }
});

test('detect devolve os pares da detecção sem alterar as partículas', () => {
  const sim = new Simulation(800, 600);
  sim.reset(300, 8, 800, 600);
  sim.moveAndBuildTree();
  const snapshot = () => sim.particles.map((p) => [p.x, p.y, p.vx, p.vy, p.colliding]);
  const before = snapshot();
  for (const [mode, expected] of [
    ['brute', findPairsBruteForce(sim.particles)],
    ['quadtree', findPairsQuadtree(sim.particles, sim.tree)],
  ]) {
    sim.mode = mode;
    const result = sim.detect();
    assert.deepEqual(result.pairs.map(pairKey), expected.pairs.map(pairKey), mode);
    assert.equal(result.tests, expected.tests, mode);
    assert.equal(sim.tests, expected.tests, mode);
  }
  assert.deepEqual(snapshot(), before);
});

test('detectAndResolve equivale a resolve(detect().pairs)', () => {
  const make = () => {
    const sim = new Simulation(400, 400);
    sim.particles = [
      new Particle(0, 100, 100, 1, 0, 8),
      new Particle(1, 110, 100, -1, 0, 8),
      new Particle(2, 300, 300, 0, 1, 8),
    ];
    sim.moveAndBuildTree();
    return sim;
  };
  const a = make();
  a.detectAndResolve();
  const b = make();
  b.resolve(b.detect().pairs);
  const state = (sim) => sim.particles.map((p) => [p.x, p.y, p.vx, p.vy, p.colliding]);
  assert.deepEqual(state(a), state(b));
  assert.equal(a.particles[0].colliding, true);
});

test('a colisão apresentada é a primeira colisão do trace, e findPairStepIndex a encontra', () => {
  const sim = new Simulation(800, 600);
  sim.reset(300, 8, 800, 600);
  sim.moveAndBuildTree();
  for (const mode of ['brute', 'quadtree']) {
    sim.mode = mode;
    const { pairs } = sim.detect();
    assert.ok(pairs.length > 0, 'cenário precisa ter colisão');
    const [a, b] = pairs[0];
    const steps = buildTrace(sim.particles, sim.tree, mode);

    const firstHit = steps.findIndex((s) => s.type === 'test' && s.overlap);
    assert.equal(pairKey([steps[firstHit].p, steps[firstHit].q]), pairKey([a, b]), mode);
    assert.equal(findPairStepIndex(steps, a, b), firstHit, mode);
    assert.equal(findPairStepIndex(steps, b, a), firstHit, mode);
  }
});

test('findPairStepIndex devolve -1 para um par que não foi testado', () => {
  const particles = [
    new Particle(0, 50, 50, 0, 0, 8),
    new Particle(1, 750, 550, 0, 0, 8),
  ];
  const tree = new Quadtree(new Rect(0, 0, 800, 600));
  for (const p of particles) tree.insert(p);
  const steps = buildTrace(particles, tree, 'quadtree');
  assert.equal(findPairStepIndex(steps, particles[0], particles[1]), -1);
});

test('step registra o tempo de detecção e de construção da árvore', () => {
  const sim = new Simulation(800, 600);
  sim.reset(200, 4, 800, 600);
  assert.equal(sim.detectMs, 0);
  sim.step();
  assert.ok(sim.detectMs > 0);
  assert.ok(sim.buildMs > 0);
});

test('avgMs registra a média acumulada por frame em cada modo e zera no reset', () => {
  const sim = new Simulation(800, 600);
  sim.reset(200, 4, 800, 600);
  assert.equal(sim.avgMs, 0);
  assert.equal(sim.frameCount, 0);

  // Primeiro frame após reset: média móvel == amostra bruta, permitindo conferir a fórmula exata.
  sim.mode = 'brute';
  sim.step();
  assert.equal(sim.avgMs, sim.detectMs);
  assert.equal(sim.lastTotalMs, sim.detectMs);
  assert.equal(sim.frameCount, 1);

  sim.reset(200, 4, 800, 600);
  sim.mode = 'quadtree';
  sim.step();
  assert.equal(sim.avgMs, sim.detectMs + sim.buildMs);
  assert.equal(sim.lastTotalMs, sim.detectMs + sim.buildMs);
  assert.equal(sim.frameCount, 1);

  sim.step();
  assert.equal(sim.frameCount, 2);
  assert.ok(sim.avgMs > 0);

  sim.reset(200, 4, 800, 600);
  assert.equal(sim.avgMs, 0);
  assert.equal(sim.lastTotalMs, 0);
  assert.equal(sim.frameCount, 0);
});

test('buildTrace acumula nós visitados e o total de passos = partículas + nós + testes', () => {
  const { particles, tree } = randomScene(100, 8, 400, 300);
  const brute = buildTrace(particles, tree, 'brute');
  assert.equal(brute[brute.length - 1].visits, 0);

  const quad = buildTrace(particles, tree, 'quadtree');
  const last = quad[quad.length - 1];
  assert.equal(last.visits, quad.filter((s) => s.type === 'visit').length);
  assert.equal(quad.length, particles.length + last.visits + last.tests);
});

test('reset com distribuição cluster concentra partículas no centro e respeita bordas', () => {
  const sim = new Simulation(800, 600);
  sim.reset(200, 4, 800, 600, 'cluster');
  assert.equal(sim.distribution, 'cluster');
  for (const p of sim.particles) {
    assert.ok(p.x >= 400 - 32 && p.x <= 400 + 32, `x fora do cluster: ${p.x}`);
    assert.ok(p.y >= 300 - 24 && p.y <= 300 + 24, `y fora do cluster: ${p.y}`);
    assert.ok(p.x >= p.r && p.x <= 800 - p.r);
    assert.ok(p.y >= p.r && p.y <= 600 - p.r);
  }
});

test('reset com distribuição clusters divide partículas em dois aglomerados', () => {
  const sim = new Simulation(800, 600);
  sim.reset(200, 4, 800, 600, 'clusters');
  assert.equal(sim.distribution, 'clusters');
  const left = sim.particles.filter((p) => p.x < 400);
  const right = sim.particles.filter((p) => p.x > 400);
  assert.equal(left.length, 100);
  assert.equal(right.length, 100);
  for (const p of left) assert.ok(p.x >= 200 - 32 && p.x <= 200 + 32);
  for (const p of right) assert.ok(p.x >= 600 - 32 && p.x <= 600 + 32);
});

test('findPairsQuadtree concorda com força bruta em cluster e faz muito mais testes que no uniforme', () => {
  const makeAndDetect = (distribution) => {
    const sim = new Simulation(800, 600);
    sim.reset(500, 4, 800, 600, distribution);
    const tree = new Quadtree(new Rect(0, 0, 800, 600));
    for (const p of sim.particles) tree.insert(p);
    return {
      brute: findPairsBruteForce(sim.particles),
      quad: findPairsQuadtree(sim.particles, tree),
    };
  };

  const uniform = makeAndDetect('uniform');
  const cluster = makeAndDetect('cluster');
  assert.deepEqual(
    cluster.quad.pairs.map(pairKey).sort(),
    cluster.brute.pairs.map(pairKey).sort(),
  );
  assert.ok(cluster.quad.tests > uniform.quad.tests * 5, `${cluster.quad.tests} vs ${uniform.quad.tests}`);
});
