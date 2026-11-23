const test = require('node:test');
const assert = require('node:assert/strict');
const { Rect, Quadtree } = require('../src/quadtree.js');

test('Rect.contains: borda esquerda/superior inclusiva, direita/inferior exclusiva', () => {
  const r = new Rect(0, 0, 10, 10);
  assert.equal(r.contains(0, 0), true);
  assert.equal(r.contains(5, 5), true);
  assert.equal(r.contains(10, 5), false);
  assert.equal(r.contains(5, 10), false);
  assert.equal(r.contains(-1, 5), false);
});

test('Rect.intersects: sobrepostos, encostados e separados', () => {
  const r = new Rect(0, 0, 10, 10);
  assert.equal(r.intersects(new Rect(5, 5, 10, 10)), true);
  assert.equal(r.intersects(new Rect(10, 0, 10, 10)), false);
  assert.equal(r.intersects(new Rect(20, 20, 5, 5)), false);
});

test('insert recusa pontos fora do boundary', () => {
  const tree = new Quadtree(new Rect(0, 0, 100, 100));
  assert.equal(tree.insert({ x: 150, y: 50 }), false);
  assert.equal(tree.insert({ x: 50, y: 50 }), true);
});

test('insert subdivide quando passa da capacidade', () => {
  const tree = new Quadtree(new Rect(0, 0, 100, 100), 4);
  const points = [
    { x: 10, y: 10 }, { x: 90, y: 10 }, { x: 10, y: 90 },
    { x: 90, y: 90 }, { x: 50, y: 50 },
  ];
  for (const p of points) tree.insert(p);
  assert.equal(tree.children.length, 4);
  assert.equal(tree.items.length, 0);
});

test('profundidade máxima impede subdivisão infinita com pontos idênticos', () => {
  const tree = new Quadtree(new Rect(0, 0, 100, 100), 4, 0, 8);
  for (let i = 0; i < 50; i++) tree.insert({ x: 30, y: 30 });

  let maxDepthFound = 0;
  (function walk(node) {
    maxDepthFound = Math.max(maxDepthFound, node.depth);
    if (node.children) node.children.forEach(walk);
  })(tree);
  assert.ok(maxDepthFound <= 8);
  assert.equal(tree.query(new Rect(0, 0, 100, 100)).length, 50);
});

test('query retorna exatamente os pontos dentro do range', () => {
  const tree = new Quadtree(new Rect(0, 0, 1000, 1000));
  const points = [];
  for (let i = 0; i < 500; i++) {
    const p = { x: Math.random() * 1000, y: Math.random() * 1000 };
    points.push(p);
    tree.insert(p);
  }
  const range = new Rect(200, 300, 250, 400);
  const expected = points.filter((p) => range.contains(p.x, p.y));
  const found = tree.query(range);
  assert.equal(found.length, expected.length);
  for (const p of expected) assert.ok(found.includes(p));
});

test('query com visited registra o caminho sem mudar o resultado', () => {
  const tree = new Quadtree(new Rect(0, 0, 1000, 1000));
  for (let i = 0; i < 300; i++) tree.insert({ x: Math.random() * 1000, y: Math.random() * 1000 });
  const range = new Rect(100, 100, 150, 150);

  const visited = [];
  const found = tree.query(range, [], visited);
  assert.deepEqual(found, tree.query(range));
  assert.equal(visited[0].node, tree);
  assert.equal(visited[0].hit, true);

  // Juntando o que cada nó achou, na ordem, temos exatamente o resultado da busca.
  assert.deepEqual(visited.flatMap((v) => v.found), found);

  // Nó descartado: não achou nada e nenhum descendente dele foi visitado.
  const visitedNodes = new Set(visited.map((v) => v.node));
  const hasVisitedDescendant = (node) =>
    node.children !== null && node.children.some((c) => visitedNodes.has(c) || hasVisitedDescendant(c));
  for (const v of visited) {
    if (!v.hit) {
      assert.equal(v.found.length, 0);
      assert.equal(hasVisitedDescendant(v.node), false);
    }
  }
  assert.ok(visited.some((v) => !v.hit), 'algum nó deve ter sido descartado');
});
