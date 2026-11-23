// Desenho no canvas. Só lê o estado da simulação, nunca o altera.

const COLOR_BACKGROUND = '#111';
const COLOR_PARTICLE = '#8cf';
const COLOR_COLLIDING = '#f44';
const COLOR_GRID = 'rgba(120, 255, 120, 0.35)';
const COLOR_SELECTED = '#fd3';

function draw(ctx, sim, showGrid, dragRect) {
  ctx.fillStyle = COLOR_BACKGROUND;
  ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);

  if (showGrid && sim.tree) {
    ctx.strokeStyle = COLOR_GRID;
    ctx.lineWidth = 1;
    drawTree(ctx, sim.tree);
  }

  for (const p of sim.particles) {
    ctx.fillStyle = p.colliding ? COLOR_COLLIDING : COLOR_PARTICLE;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, 2 * Math.PI);
    ctx.fill();

    // Selecionadas ganham um contorno, para não confundir com o vermelho da colisão.
    if (p.selected) {
      ctx.strokeStyle = COLOR_SELECTED;
      ctx.lineWidth = 2;
      ctx.stroke();
    }
  }

  const selection = dragRect || sim.selection;
  if (selection) {
    ctx.strokeStyle = COLOR_SELECTED;
    ctx.lineWidth = 1;
    ctx.setLineDash([6, 4]);
    ctx.strokeRect(selection.x, selection.y, selection.w, selection.h);
    ctx.setLineDash([]);
  }
}

// Desenha o retângulo de cada nó, descendo recursivamente pelos filhos.
function drawTree(ctx, node) {
  const b = node.boundary;
  ctx.strokeRect(b.x, b.y, b.w, b.h);
  if (node.children) {
    for (const child of node.children) drawTree(ctx, child);
  }
}

// ---------- Modo didático ----------

const COLOR_DIM = 'rgba(136, 204, 255, 0.35)';
const COLOR_FOCUS = '#fff';
// O verde vivo é só do par que disparou a pausa; o resto usa outras cores
// (a grade completa continua no verde suave COLOR_GRID).
const COLOR_PRESENTED = '#4f4';
const COLOR_NO_COLLISION = '#fd3';
const COLOR_OLD_TEST = 'rgba(200, 200, 200, 0.25)';
const COLOR_NODE_HIT = '#4cf';
const COLOR_NODE_PRUNED = 'rgba(255, 90, 90, 0.8)';

// Desenha o passo `index` do trace: o que o algoritmo está olhando agora
// e o caminho percorrido até ali para a partícula atual.
// `pair` ([a, b] ou null) é a colisão que disparou a pausa: fica verde o tempo todo.
function drawTrace(ctx, sim, steps, index, showGrid, pair) {
  ctx.fillStyle = COLOR_BACKGROUND;
  ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);

  if (showGrid && sim.tree) {
    ctx.strokeStyle = COLOR_GRID;
    ctx.lineWidth = 1;
    drawTree(ctx, sim.tree);
  }

  // O par apresentado fica verde; colisões já encontradas até este passo, vermelhas;
  // o resto, apagado.
  const found = new Set();
  for (let i = 0; i <= index; i++) {
    const s = steps[i];
    if (s.type === 'test' && s.overlap) {
      found.add(s.p);
      found.add(s.q);
    }
  }
  for (const p of sim.particles) {
    if (pair && (p === pair[0] || p === pair[1])) ctx.fillStyle = COLOR_PRESENTED;
    else ctx.fillStyle = found.has(p) ? COLOR_COLLIDING : COLOR_DIM;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, 2 * Math.PI);
    ctx.fill();
  }

  // Volta até o passo 'particle' para saber onde começou a partícula atual.
  let start = index;
  while (start > 0 && steps[start].type !== 'particle') start--;
  const current = steps[index];
  const p = steps[start].p;

  // Região de busca (só Quadtree): o quadrado onde podem estar as vizinhas.
  const range = steps[start].range;
  if (range) {
    ctx.strokeStyle = COLOR_FOCUS;
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);
    ctx.strokeRect(range.x, range.y, range.w, range.h);
    ctx.setLineDash([]);
  }

  // Nós visitados até agora: verde = tocou a região (a busca desce),
  // vermelho = descartado inteiro. O nó do passo atual fica mais grosso.
  for (let i = start; i <= index; i++) {
    const s = steps[i];
    if (s.type !== 'visit') continue;
    const b = s.node.boundary;
    ctx.strokeStyle = s.hit ? COLOR_NODE_HIT : COLOR_NODE_PRUNED;
    ctx.lineWidth = i === index ? 3 : 1;
    ctx.strokeRect(b.x, b.y, b.w, b.h);
  }

  // Testes já feitos por esta partícula (cinza) e o teste atual (verde = não colide, vermelho = colide).
  for (let i = start; i <= index; i++) {
    const s = steps[i];
    if (s.type !== 'test') continue;
    const isCurrent = i === index;
    ctx.strokeStyle = isCurrent ? (s.overlap ? COLOR_COLLIDING : COLOR_NO_COLLISION) : COLOR_OLD_TEST;
    ctx.lineWidth = isCurrent ? 2 : 1;
    ctx.beginPath();
    ctx.moveTo(s.p.x, s.p.y);
    ctx.lineTo(s.q.x, s.q.y);
    ctx.stroke();
  }
  if (current.type === 'test') {
    ctx.strokeStyle = COLOR_FOCUS;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(current.q.x, current.q.y, current.q.r + 3, 0, 2 * Math.PI);
    ctx.stroke();
  }

  // A partícula analisada ganha um anel branco.
  ctx.strokeStyle = COLOR_FOCUS;
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.arc(p.x, p.y, p.r + 3, 0, 2 * Math.PI);
  ctx.stroke();
}

// ---------- Gráfico de velocidade (painel) ----------

const COLOR_BRUTE = '#f87171';
const COLOR_BRUTE_REF = 'rgba(248, 113, 113, 0.55)';
const COLOR_QUAD = '#38bdf8';
const COLOR_QUAD_REF = 'rgba(56, 189, 248, 0.55)';

function drawSpeedChart(ctx, series, activeMode, maxSamples) {
  const { width, height } = ctx.canvas;
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = 'rgba(0, 0, 0, 0.35)';
  ctx.fillRect(0, 0, width, height);

  const padLeft = 48;
  const padRight = 6;
  const padTop = 46;
  const padBottom = 10;
  const plotW = Math.max(1, width - padLeft - padRight);
  const plotH = Math.max(1, height - padTop - padBottom);
  const maxVal = Math.max(...series.brute, ...series.quadtree, 0.1);
  const xAt = (i) => padLeft + (i / Math.max(1, maxSamples - 1)) * plotW;
  const yAt = (v) => padTop + plotH * (1 - v / maxVal);

  ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
  ctx.fillStyle = '#94a3b8';
  ctx.font = '13px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
  ctx.textBaseline = 'middle';
  ctx.textAlign = 'right';
  ctx.lineWidth = 1;
  for (const frac of [0, 0.5, 1]) {
    const y = padTop + plotH * (1 - frac);
    ctx.beginPath();
    ctx.moveTo(padLeft, y);
    ctx.lineTo(width - padRight, y);
    ctx.stroke();
    ctx.fillText(frac === 0 ? '0' : (maxVal * frac).toFixed(1), padLeft - 5, y);
  }

  const drawLine = (samples, color, isActive) => {
    if (samples.length === 0) return;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    if (samples.length > 1) {
      ctx.lineWidth = isActive ? 2 : 1.5;
      ctx.beginPath();
      ctx.moveTo(xAt(0), yAt(samples[0]));
      for (let i = 1; i < samples.length; i++) {
        ctx.lineTo(xAt(i), yAt(samples[i]));
      }
      ctx.stroke();
    }
    if (isActive) {
      const last = samples.length - 1;
      ctx.beginPath();
      ctx.arc(xAt(last), yAt(samples[last]), 2.5, 0, 2 * Math.PI);
      ctx.fill();
    }
  };

  const otherMode = activeMode === 'brute' ? 'quadtree' : 'brute';
  drawLine(series[otherMode], otherMode === 'brute' ? COLOR_BRUTE_REF : COLOR_QUAD_REF, false);
  drawLine(series[activeMode], activeMode === 'brute' ? COLOR_BRUTE : COLOR_QUAD, true);

  ctx.font = '14px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
  ctx.textBaseline = 'top';
  ctx.textAlign = 'left';
  let ly = 6;
  const rows = [
    ['brute', '● Bruta   ', COLOR_BRUTE],
    ['quadtree', '● Quadtree', COLOR_QUAD],
  ];
  for (const [mode, label, color] of rows) {
    const samples = series[mode];
    if (samples.length === 0) continue;
    const peak = Math.max(...samples);
    ctx.fillStyle = color;
    ctx.fillText(`${label} máx ${peak.toFixed(2)} ms`, 6, ly);
    ly += 18;
  }
}
