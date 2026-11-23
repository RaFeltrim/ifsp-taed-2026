const test = require('node:test');
const assert = require('node:assert/strict');
const { Particle, particlesOverlap, resolveCollision } = require('../src/particle.js');

test('move soma a velocidade à posição', () => {
  const p = new Particle(0, 50, 50, 2, -3, 5);
  p.move(100, 100);
  assert.equal(p.x, 52);
  assert.equal(p.y, 47);
});

test('move quica na borda esquerda e na direita', () => {
  const left = new Particle(0, 6, 50, -3, 0, 5);
  left.move(100, 100);
  assert.equal(left.x, 5);
  assert.ok(left.vx > 0);

  const right = new Particle(1, 94, 50, 3, 0, 5);
  right.move(100, 100);
  assert.equal(right.x, 95);
  assert.ok(right.vx < 0);
});

test('move quica na borda superior e na inferior', () => {
  const top = new Particle(0, 50, 6, 0, -3, 5);
  top.move(100, 100);
  assert.equal(top.y, 5);
  assert.ok(top.vy > 0);

  const bottom = new Particle(1, 50, 94, 0, 3, 5);
  bottom.move(100, 100);
  assert.equal(bottom.y, 95);
  assert.ok(bottom.vy < 0);
});

test('particlesOverlap: sobrepostas sim, apenas encostadas não', () => {
  const a = new Particle(0, 0, 0, 0, 0, 5);
  assert.equal(particlesOverlap(a, new Particle(1, 9, 0, 0, 0, 5)), true);
  assert.equal(particlesOverlap(a, new Particle(2, 10, 0, 0, 0, 5)), false);
  assert.equal(particlesOverlap(a, new Particle(3, 20, 0, 0, 0, 5)), false);
});

test('resolveCollision: colisão frontal troca as velocidades e separa', () => {
  const a = new Particle(0, 0, 0, 1, 0, 5);
  const b = new Particle(1, 8, 0, -2, 0, 5);
  resolveCollision(a, b);
  assert.equal(a.vx, -2);
  assert.equal(b.vx, 1);
  assert.ok(Math.abs(Math.hypot(b.x - a.x, b.y - a.y) - 10) < 1e-9);
});

test('resolveCollision: partículas se afastando mantêm a velocidade', () => {
  const a = new Particle(0, 0, 0, -1, 0, 5);
  const b = new Particle(1, 8, 0, 1, 0, 5);
  resolveCollision(a, b);
  assert.equal(a.vx, -1);
  assert.equal(b.vx, 1);
});

test('resolveCollision: centros coincidentes não geram NaN', () => {
  const a = new Particle(0, 10, 10, 1, 0, 5);
  const b = new Particle(1, 10, 10, -1, 0, 5);
  resolveCollision(a, b);
  for (const v of [a.x, a.y, a.vx, a.vy, b.x, b.y, b.vx, b.vy]) {
    assert.ok(Number.isFinite(v));
  }
  assert.ok(Math.abs(b.x - a.x - 10) < 1e-9);
});
