// Benchmark de escala: compara força bruta e Quadtree para vários N e raios.
// Uso:  node bench/benchmark.js [--csv] [--frames=50] [--sizes=100,1000,5000] [--distribution=uniform|cluster|clusters]
// Mede o tempo por frame (mediana, em ms) e confere que os dois algoritmos
// encontram exatamente os mesmos pares de partículas.

const assert = require('node:assert');
const { Simulation, findPairsBruteForce, findPairsQuadtree } = require('../src/simulation.js');
// simulation.js já tornou Quadtree e Rect globais.

const RADII = [4, 16];
const WIDTH = 1280;
const HEIGHT = 720;
const WARMUP_FRAMES = 10; // deixa o JIT aquecer antes de medir

const args = process.argv.slice(2);
const csv = args.includes('--csv');
const framesArg = args.find((a) => a.startsWith('--frames='));
const FRAMES = framesArg ? Number(framesArg.split('=')[1]) : 50;
const sizesArg = args.find((a) => a.startsWith('--sizes='));
const SIZES = sizesArg ? sizesArg.split('=')[1].split(',').map(Number) : [100, 200, 500, 1000, 2000, 5000, 10000];
const distArg = args.find((a) => a.startsWith('--distribution='));
const DISTRIBUTION = distArg ? distArg.split('=')[1] : 'uniform';

function median(values) {
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.floor(sorted.length / 2)];
}

// Mesmo critério de comparação de pares, independente da ordem.
function pairKeys(pairs) {
  return pairs.map(([a, b]) => `${Math.min(a.id, b.id)}-${Math.max(a.id, b.id)}`).sort();
}

function measure(count, radius) {
  const sim = new Simulation(WIDTH, HEIGHT);
  sim.reset(count, radius, WIDTH, HEIGHT, DISTRIBUTION);

  const brute = [];
  const buildTree = [];
  const quadDetect = [];
  let bruteTests = 0;
  let quadTests = 0;

  for (let frame = 0; frame < WARMUP_FRAMES + FRAMES; frame++) {
    // Mover as partículas (não entra na medição).
    for (const p of sim.particles) p.move(sim.width, sim.height);

    // Construir a árvore (medido).
    let t = performance.now();
    const tree = new Quadtree(new Rect(0, 0, WIDTH, HEIGHT));
    for (const p of sim.particles) tree.insert(p);
    const treeMs = performance.now() - t;

    // Força bruta (medido).
    t = performance.now();
    const bruteResult = findPairsBruteForce(sim.particles);
    const bruteMs = performance.now() - t;

    // Quadtree (medido).
    t = performance.now();
    const quadResult = findPairsQuadtree(sim.particles, tree);
    const quadMs = performance.now() - t;

    // Os dois algoritmos precisam concordar em quem colidiu.
    assert.deepStrictEqual(pairKeys(quadResult.pairs), pairKeys(bruteResult.pairs),
      `pares diferentes (N=${count}, r=${radius}, frame ${frame})`);

    if (frame >= WARMUP_FRAMES) {
      brute.push(bruteMs);
      buildTree.push(treeMs);
      quadDetect.push(quadMs);
      bruteTests = bruteResult.tests;
      quadTests = quadResult.tests;
    }

    // Resolver as colisões mantém a simulação evoluindo como na demo.
    sim.resolve(bruteResult.pairs);
  }

  const bruteMs = median(brute);
  const quadTotalMs = median(buildTree) + median(quadDetect);
  return {
    count, radius, bruteMs, treeMs: median(buildTree), quadDetectMs: median(quadDetect),
    quadTotalMs, speedup: bruteMs / quadTotalMs, bruteTests, quadTests,
  };
}

const rows = [];
for (const radius of RADII) {
  for (const count of SIZES) {
    rows.push(measure(count, radius));
    process.stderr.write(`N=${count} r=${radius} ok\n`);
  }
}

const header = ['N', 'raio', 'bruta_ms', 'arvore_ms', 'quad_busca_ms', 'quad_total_ms', 'ganho', 'testes_bruta', 'testes_quad'];
const cells = rows.map((r) => [
  r.count, r.radius, r.bruteMs.toFixed(3), r.treeMs.toFixed(3), r.quadDetectMs.toFixed(3),
  r.quadTotalMs.toFixed(3), `${r.speedup.toFixed(1)}x`, r.bruteTests, r.quadTests,
]);

if (csv) {
  console.log(header.join(','));
  for (const row of cells) console.log(row.join(','));
} else {
  console.log(`| ${header.join(' | ')} |`);
  console.log(`|${header.map(() => '---').join('|')}|`);
  for (const row of cells) console.log(`| ${row.join(' | ')} |`);
  console.log(`\n${FRAMES} frames por cenário (mediana), distribuição ${DISTRIBUTION}, área ${WIDTH}x${HEIGHT}, Node ${process.version}.`);
}
