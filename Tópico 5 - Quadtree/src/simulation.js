// Estado da simulação e o passo de cada frame: mover, detectar colisões e resolvê-las.

// No navegador, Particle, Quadtree etc. já são globais (scripts carregados antes).
// No Node (testes) precisamos carregá-los e torná-los globais do mesmo jeito.
// Não dá para usar `var { Quadtree } = require(...)`: no navegador esse `var`
// colidiria com a classe global já declarada.
if (typeof require !== 'undefined') {
  Object.assign(globalThis, require('./particle.js'), require('./quadtree.js'));
}

// Força bruta: compara cada par (i, j) com i < j uma única vez.
// Sempre faz n(n-1)/2 testes, por isso cresce com o quadrado de n.
function findPairsBruteForce(particles) {
  const pairs = [];
  let tests = 0;
  for (let i = 0; i < particles.length; i++) {
    for (let j = i + 1; j < particles.length; j++) {
      tests++;
      if (particlesOverlap(particles[i], particles[j])) {
        pairs.push([particles[i], particles[j]]);
      }
    }
  }
  return { pairs, tests };
}

// Quadtree: cada partícula só é comparada com as vizinhas.
// Como todas têm o mesmo raio r, quem pode tocar `p` tem o centro a no máximo 2r
// de distância, ou seja, dentro de um quadrado de lado 4r centrado em `p`.
function findPairsQuadtree(particles, tree) {
  const pairs = [];
  let tests = 0;
  for (const p of particles) {
    const range = new Rect(p.x - 2 * p.r, p.y - 2 * p.r, 4 * p.r, 4 * p.r);
    for (const q of tree.query(range)) {
      // q.id > p.id: cada par é testado (e contado) uma só vez, como na força bruta.
      if (q.id <= p.id) continue;
      tests++;
      if (particlesOverlap(p, q)) pairs.push([p, q]);
    }
  }
  return { pairs, tests };
}

// Média móvel: um frame isolado é muito ruidoso para ler no painel.
function smooth(average, sample) {
  return average === 0 ? sample : average * 0.9 + sample * 0.1;
}

const CLUSTER_FRACTION = 0.08;

function spawnInBox(cx, cy, bw, bh, r, width, height) {
  const minX = Math.max(r, cx - bw / 2);
  const maxX = Math.min(width - r, cx + bw / 2);
  const minY = Math.max(r, cy - bh / 2);
  const maxY = Math.min(height - r, cy + bh / 2);
  return {
    x: minX + Math.random() * Math.max(0, maxX - minX),
    y: minY + Math.random() * Math.max(0, maxY - minY),
  };
}

class Simulation {
  constructor(width, height) {
    this.width = width;
    this.height = height;
    this.radius = 4;
    this.distribution = 'uniform';
    this.particles = [];
    this.mode = 'brute'; // 'brute' | 'quadtree'
    this.tree = null; // Quadtree do último frame (usada pela grade e pela seleção)
    this.tests = 0; // testes de colisão do último frame
    this.detectMs = 0; // tempo médio (ms) para achar os pares colidindo
    this.buildMs = 0; // tempo médio (ms) para reconstruir a Quadtree
    this.lastBuildMs = 0; // último frame (sem suavização), para medir a média
    this.lastTotalMs = 0; // tempo bruto total do último frame (ms)
    this.avgMs = 0; // média aritmética do tempo total por frame (ms)
    this.frameCount = 0; // frames contados em avgMs
    this.selection = null;
    this.selectedCount = 0;
  }

  // Recomeça do zero: posições e direções aleatórias conforme a distribuição escolhida.
  reset(count, radius, width, height, distribution = 'uniform') {
    this.width = width;
    this.height = height;
    this.radius = radius;
    this.distribution = distribution;
    this.particles = [];
    const bw = width * CLUSTER_FRACTION;
    const bh = height * CLUSTER_FRACTION;
    for (let i = 0; i < count; i++) {
      let pos;
      if (distribution === 'cluster') {
        pos = spawnInBox(width / 2, height / 2, bw, bh, radius, width, height);
      } else if (distribution === 'clusters') {
        const cx = i % 2 === 0 ? width * 0.25 : width * 0.75;
        pos = spawnInBox(cx, height / 2, bw, bh, radius, width, height);
      } else {
        pos = spawnInBox(width / 2, height / 2, width, height, radius, width, height);
      }
      const angle = Math.random() * 2 * Math.PI;
      const speed = 0.5 + Math.random() * 1.5; // entre 0.5 e 2 px por frame
      this.particles.push(new Particle(i, pos.x, pos.y, Math.cos(angle) * speed, Math.sin(angle) * speed, radius));
    }
    this.tests = 0;
    this.detectMs = 0;
    this.buildMs = 0;
    this.lastBuildMs = 0;
    this.lastTotalMs = 0;
    this.avgMs = 0;
    this.frameCount = 0;
    this.selection = null;
    this.selectedCount = 0;
  }

  // Define (Rect) ou limpa (null) a região de seleção; aplicada no próximo step().
  setSelection(rect) {
    this.selection = rect;
  }

  // Avança um frame. Dividido em duas metades para o modo didático poder
  // parar entre elas e mostrar a detecção passo a passo.
  step() {
    this.moveAndBuildTree();
    this.detectAndResolve();
  }

  moveAndBuildTree() {
    // 1) Mover e quicar nas bordas.
    for (const p of this.particles) p.move(this.width, this.height);

    // 2) Reconstruir a Quadtree do zero (mais simples que atualizá-la).
    const start = performance.now();
    this.tree = new Quadtree(new Rect(0, 0, this.width, this.height));
    for (const p of this.particles) this.tree.insert(p);
    this.lastBuildMs = performance.now() - start;
    this.buildMs = smooth(this.buildMs, this.lastBuildMs);
  }

  // Detectar e resolver também ficam separados: assim o modo didático pode olhar
  // se houve colisão neste frame e pausar antes do ricochete.
  detectAndResolve() {
    this.resolve(this.detect().pairs);
  }

  // 3) Detectar todos os pares com as posições congeladas (não altera as partículas).
  detect() {
    const start = performance.now();
    const result = this.mode === 'brute'
      ? findPairsBruteForce(this.particles)
      : findPairsQuadtree(this.particles, this.tree);
    const elapsed = performance.now() - start;
    this.detectMs = smooth(this.detectMs, elapsed);
    const frameTotal = elapsed + (this.mode === 'quadtree' ? this.lastBuildMs : 0);
    this.lastTotalMs = frameTotal;
    this.frameCount++;
    this.avgMs += (frameTotal - this.avgMs) / this.frameCount;
    this.tests = result.tests;
    return result;
  }

  resolve(pairs) {
    // 4) Só depois resolver: separar, ricochetear e pintar de vermelho.
    for (const p of this.particles) p.colliding = false;
    for (const [a, b] of pairs) {
      resolveCollision(a, b);
      a.colliding = true;
      b.colliding = true;
    }

    // 5) Range query: marcar as partículas dentro da região selecionada.
    // Usa a árvore deste frame (posições de antes do ricochete; diferença imperceptível).
    for (const p of this.particles) p.selected = false;
    this.selectedCount = 0;
    if (this.selection) {
      const found = this.tree.query(this.selection);
      for (const p of found) p.selected = true;
      this.selectedCount = found.length;
    }
  }
}

// Modo didático: refaz a detecção do frame anotando cada iteração como um "passo",
// para a tela poder mostrar o algoritmo trabalhando. Faz exatamente os mesmos testes
// que findPairsBruteForce / findPairsQuadtree; a diferença é que guarda o que aconteceu.
//   { type: 'particle', p, range }           começa a analisar a partícula p
//   { type: 'visit', p, range, node, hit }   (Quadtree) visitou um nó; hit = tocou a região?
//   { type: 'test', p, q, overlap }          testou o par (p, q); overlap = colidem?
// Cada passo também leva os totais acumulados `tests`, `collisions` e `visits`
// (nós visitados; sempre 0 na força bruta, que não usa árvore).
function buildTrace(particles, tree, mode) {
  const steps = [];
  let tests = 0;
  let collisions = 0;
  let visits = 0;

  function addTest(p, q) {
    tests++;
    const overlap = particlesOverlap(p, q);
    if (overlap) collisions++;
    steps.push({ type: 'test', p, q, overlap, tests, collisions, visits });
  }

  if (mode === 'brute') {
    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];
      steps.push({ type: 'particle', p, range: null, tests, collisions, visits });
      for (let j = i + 1; j < particles.length; j++) addTest(p, particles[j]);
    }
    return steps;
  }

  for (const p of particles) {
    const range = new Rect(p.x - 2 * p.r, p.y - 2 * p.r, 4 * p.r, 4 * p.r);
    steps.push({ type: 'particle', p, range, tests, collisions, visits });

    // Percorre o caminho da busca: cada nó visitado e, logo em seguida,
    // os testes com as partículas que a busca encontrou nele.
    const visited = [];
    tree.query(range, [], visited);
    for (const { node, hit, found } of visited) {
      visits++;
      steps.push({ type: 'visit', p, range, node, hit, tests, collisions, visits });
      for (const q of found) {
        if (q.id > p.id) addTest(p, q);
      }
    }
  }
  return steps;
}

// Índice do passo em que o par (a, b) é testado, em qualquer ordem; -1 se não foi testado.
// O modo didático usa para pular direto à colisão que disparou a pausa (tecla Enter).
function findPairStepIndex(steps, a, b) {
  return steps.findIndex((s) =>
    s.type === 'test' && ((s.p === a && s.q === b) || (s.p === b && s.q === a)));
}

if (typeof module !== 'undefined') module.exports = { Simulation, findPairsBruteForce, findPairsQuadtree, buildTrace, findPairStepIndex };
