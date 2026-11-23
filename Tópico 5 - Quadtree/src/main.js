// Liga a simulação à página: controles, eventos e o loop de animação.

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const panel = document.getElementById('panel');
const togglePanelBtn = document.getElementById('togglePanelBtn');
const countInput = document.getElementById('count');
const countValue = document.getElementById('countValue');
const radiusSelect = document.getElementById('radius');
const distributionSelect = document.getElementById('distribution');
const fpsSelect = document.getElementById('fps');
const modeBtn = document.getElementById('modeBtn');
const resetBtn = document.getElementById('resetBtn');
const stepBtn = document.getElementById('stepBtn');
const notice = document.getElementById('notice');
const showGridInput = document.getElementById('showGrid');
const stats = document.getElementById('stats');
const speedChart = document.getElementById('speedChart');
const speedCtx = speedChart.getContext('2d');

const MAX_SPEED_SAMPLES = 180;
const speedSeries = { brute: [], quadtree: [] };

function recordSpeed() {
  const arr = speedSeries[sim.mode];
  arr.push(sim.lastTotalMs);
  if (arr.length > MAX_SPEED_SAMPLES) arr.shift();
}

const sim = new Simulation(innerWidth, innerHeight);

function resizeCanvas() {
  canvas.width = innerWidth;
  canvas.height = innerHeight;
}

// Mudar quantidade, raio ou tamanho da janela sempre recomeça a simulação.
// Com o modo didático ligado, ele volta a aguardar uma colisão (se couber no limite).
function restart(keepOtherSeries = false) {
  sim.reset(Number(countInput.value), Number(radiusSelect.value), canvas.width, canvas.height, distributionSelect.value);
  trace = null;
  stepAccumulator = 0;
  if (keepOtherSeries === true) {
    speedSeries[sim.mode] = [];
  } else {
    speedSeries.brute = [];
    speedSeries.quadtree = [];
  }
  if (sim.particles.length <= MAX_TRACE_PARTICLES) {
    notice.textContent = '';
    if (didactic !== 'off') didactic = 'waiting';
  } else if (didactic !== 'off') {
    didactic = 'off';
    updateStepBtn();
    notice.textContent = LIMIT_NOTICE;
  }
}

window.addEventListener('resize', () => {
  resizeCanvas();
  restart();
});
radiusSelect.addEventListener('change', restart);
distributionSelect.addEventListener('change', restart);
fpsSelect.addEventListener('change', () => { stepAccumulator = 0; });
resetBtn.addEventListener('click', restart);

function togglePanel() {
  const collapsed = panel.classList.toggle('collapsed');
  togglePanelBtn.textContent = collapsed ? '+' : '−';
  togglePanelBtn.setAttribute('aria-expanded', String(!collapsed));
  togglePanelBtn.blur();
}
togglePanelBtn.addEventListener('click', togglePanel);

window.addEventListener('keydown', (e) => {
  if (e.ctrlKey || e.metaKey || e.altKey) return;
  const tag = document.activeElement ? document.activeElement.tagName : '';
  if (tag === 'INPUT' || tag === 'SELECT' || tag === 'TEXTAREA') return;
  if (e.key === 'h' || e.key === 'H') {
    e.preventDefault();
    togglePanel();
  }
});

// O slider mostra o valor enquanto arrasta e só recomeça ao soltar.
countInput.addEventListener('input', () => {
  countValue.value = countInput.value;
});
countInput.addEventListener('change', restart);

// O campo numérico sincroniza com o slider (limitado entre min e max) e reinicia ao confirmar.
function applyCountNumber() {
  const min = Number(countInput.min);
  const max = Number(countInput.max);
  const parsed = parseInt(countValue.value, 10);
  const clamped = Number.isNaN(parsed)
    ? Number(countInput.value)
    : Math.min(max, Math.max(min, parsed));
  countValue.value = String(clamped);
  countInput.value = String(clamped);
  restart();
}

countValue.addEventListener('change', applyCountNumber);
countValue.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    applyCountNumber();
    countValue.blur();
  }
});

// Em uniforme, mantém as posições; em Aglomerado / Dois clusters, reinicia ao trocar de modo.
modeBtn.addEventListener('click', () => {
  sim.mode = sim.mode === 'brute' ? 'quadtree' : 'brute';
  sim.avgMs = sim.frameCount = 0;
  modeBtn.textContent = sim.mode === 'brute' ? 'Modo: força bruta' : 'Modo: Quadtree';
  if (didactic === 'presenting') rebuildTrace(); // mesmo frame e mesmo par, outro algoritmo
  else if (sim.distribution !== 'uniform') restart(true);
  else speedSeries[sim.mode] = [];
});

// Modo didático: a animação roda até a detecção encontrar uma colisão. Aí pausa antes
// do ricochete e o usuário percorre, passo a passo, a detecção daquele frame.
//   'off'        desligado
//   'waiting'    animação rodando, aguardando a próxima colisão
//   'presenting' pausado, mostrando os passos da detecção
//   'cooldown'   animação rodando por alguns segundos sem pausar, depois volta a 'waiting'
const MAX_TRACE_PARTICLES = 200; // acima disso há passos demais para seguir à mão
const COOLDOWN_MS = 5000; // intervalo entre uma apresentação e a próxima pausa possível
const LIMIT_NOTICE = `Modo didático: reduza para até ${MAX_TRACE_PARTICLES} partículas`;
let didactic = 'off';
// Só em 'presenting': passos do frame, passo atual, par que disparou a pausa (fica verde),
// todos os pares do frame (resolvidos ao encerrar) e o passo em que o par é testado.
let trace = null; // { steps, index, pair, pairs, pairIndex }
let cooldownEnd = 0; // só em 'cooldown': quando o intervalo termina (ms)

// Um frame em 'waiting': move, detecta e só resolve se não houver colisão.
function waitForCollision() {
  sim.moveAndBuildTree();
  const { pairs } = sim.detect();
  recordSpeed();
  if (pairs.length === 0) {
    sim.resolve(pairs);
    return;
  }
  trace = { pairs, pair: pairs[0] }; // apresenta a primeira colisão encontrada
  rebuildTrace();
  didactic = 'presenting';
}

// (Re)gera os passos do frame pausado com o modo de detecção atual, mantendo o par.
function rebuildTrace() {
  trace.steps = buildTrace(sim.particles, sim.tree, sim.mode);
  trace.index = 0;
  trace.pairIndex = findPairStepIndex(trace.steps, trace.pair[0], trace.pair[1]);
}

// Encerra a apresentação: resolve as colisões do frame, retoma a animação e
// começa o intervalo em que novas colisões não pausam.
function endPresentation() {
  sim.resolve(trace.pairs);
  trace = null;
  didactic = 'cooldown';
  cooldownEnd = performance.now() + COOLDOWN_MS;
}

function updateStepBtn() {
  stepBtn.textContent = didactic !== 'off' ? 'Modo didático: ligado' : 'Modo didático: desligado';
}

stepBtn.addEventListener('click', () => {
  if (didactic !== 'off') {
    if (didactic === 'presenting') sim.resolve(trace.pairs); // conclui o frame pausado
    trace = null;
    didactic = 'off';
  } else if (sim.particles.length > MAX_TRACE_PARTICLES) {
    notice.textContent = LIMIT_NOTICE;
  } else {
    didactic = 'waiting';
    notice.textContent = '';
  }
  updateStepBtn();
  stepBtn.blur();
});

// Teclas da apresentação:
//   → / ←             próximo / anterior passo (→ no último passo encerra)
//   Shift + → / ←     próxima / anterior partícula
//   Enter             vai direto ao teste da colisão que disparou a pausa
//   Esc               encerra a apresentação na hora
window.addEventListener('keydown', (e) => {
  if (didactic !== 'presenting') return;
  if (document.activeElement === countValue) return;
  if (!['ArrowRight', 'ArrowLeft', 'Enter', 'Escape'].includes(e.key)) return;
  e.preventDefault(); // a tecla não deve mexer no controle em foco nem rolar a página
  const { steps } = trace;

  if (e.key === 'Escape') {
    endPresentation();
  } else if (e.key === 'Enter') {
    trace.index = trace.pairIndex;
  } else if (e.key === 'ArrowRight') {
    let next = trace.index + 1;
    if (e.shiftKey) {
      while (next < steps.length && steps[next].type !== 'particle') next++;
    }
    if (next >= steps.length) endPresentation();
    else trace.index = next;
  } else {
    let prev = Math.max(trace.index - 1, 0);
    if (e.shiftKey) {
      while (prev > 0 && steps[prev].type !== 'particle') prev--;
    }
    trace.index = prev;
  }
});

// Frase que explica o passo atual no painel.
function describeStep(s) {
  if (s.type === 'particle') {
    return sim.mode === 'brute'
      ? `Partícula #${s.p.id}: comparar com todas as de id maior`
      : `Partícula #${s.p.id}: buscar vizinhas na região tracejada`;
  }
  if (s.type === 'visit') {
    return s.hit
      ? `Nó nível ${s.node.depth} toca a região → examina e desce`
      : `Nó nível ${s.node.depth} fora da região → descartado`;
  }
  const dist = Math.hypot(s.q.x - s.p.x, s.q.y - s.p.y);
  const minDist = s.p.r + s.q.r;
  return s.overlap
    ? `Teste #${s.p.id} × #${s.q.id}: ${dist.toFixed(1)} < ${minDist} → COLISÃO`
    : `Teste #${s.p.id} × #${s.q.id}: ${dist.toFixed(1)} ≥ ${minDist} → sem colisão`;
}

function updateTraceStats() {
  const s = trace.steps[trace.index];
  const [a, b] = trace.pair;
  const marker = trace.index === trace.pairIndex ? '  ← colisão que disparou a pausa' : '';
  const total = trace.steps[trace.steps.length - 1];
  const isQuadtree = sim.mode === 'quadtree';
  // Passo = uma ação do algoritmo (analisar partícula, visitar nó ou testar par);
  // "Testes" conta só as comparações entre pares, por isso é bem menor que o total de passos.
  const composition = isQuadtree
    ? `${sim.particles.length} part. + ${total.visits} nós + ${total.tests} testes`
    : `${sim.particles.length} part. + ${total.tests} testes`;
  stats.textContent =
    `MODO DIDÁTICO (${sim.mode === 'brute' ? 'força bruta' : 'Quadtree'})\n` +
    `Colisão apresentada: #${a.id} × #${b.id}\n` +
    `Passo ${trace.index + 1} / ${trace.steps.length}\n` +
    `(${composition})\n` +
    `${describeStep(s)}${marker}\n` +
    `Testes:    ${s.tests}/${total.tests}\n` +
    (isQuadtree ? `Nós:       ${s.visits}/${total.visits}\n` : '') +
    `Colisões:  ${s.collisions}\n` +
    `→ ← passo · Shift partícula · Enter colisão · Esc continuar`;
}

// Seleção com o mouse: arrastar desenha um retângulo e atualiza a range query na hora.
let dragStart = null;
let dragRect = null;

// Retângulo com largura e altura positivas, em qualquer direção de arrasto.
function rectFromPoints(x1, y1, x2, y2) {
  return new Rect(Math.min(x1, x2), Math.min(y1, y2), Math.abs(x2 - x1), Math.abs(y2 - y1));
}

canvas.addEventListener('mousedown', (e) => {
  if (didactic === 'presenting') return; // durante a apresentação o mouse é ignorado
  dragStart = { x: e.offsetX, y: e.offsetY };
});

canvas.addEventListener('mousemove', (e) => {
  if (!dragStart) return;
  dragRect = rectFromPoints(dragStart.x, dragStart.y, e.offsetX, e.offsetY);
  sim.setSelection(dragRect);
});

window.addEventListener('mouseup', () => {
  if (!dragStart) return;
  // Clique sem arrastar (menos de 3 px) limpa a seleção.
  if (!dragRect || (dragRect.w < 3 && dragRect.h < 3)) sim.setSelection(null);
  dragStart = null;
  dragRect = null;
});

// FPS: taxa real de passos simulados; o painel é atualizado ~4 vezes por segundo.
let lastTime = performance.now();
let fps = 60;
let lastStatsUpdate = 0;
let stepAccumulator = 0;
let stepsSinceStats = 0;

function stepOnce() {
  if (didactic === 'waiting') waitForCollision(); // pode passar para 'presenting'
  else {
    sim.step();
    recordSpeed();
  }
}

function updateStats(now) {
  const dt = now - lastStatsUpdate;
  if (dt < 250) return;
  if (lastStatsUpdate > 0) fps = fps * 0.7 + ((stepsSinceStats * 1000) / dt) * 0.3;
  lastStatsUpdate = now;
  stepsSinceStats = 0;
  const totalMs = sim.detectMs + (sim.mode === 'quadtree' ? sim.buildMs : 0);
  stats.textContent =
    `FPS:        ${fps.toFixed(0)}\n` +
    `Partículas: ${sim.particles.length}\n` +
    `Testes:     ${sim.tests}\n` +
    `Detecção:   ${sim.detectMs.toFixed(3)} ms\n` +
    (sim.mode === 'quadtree' ? `Árvore:     ${sim.buildMs.toFixed(3)} ms\n` : '') +
    `Total:      ${totalMs.toFixed(3)} ms (média ${sim.avgMs.toFixed(3)})\n` +
    `Modo:       ${sim.mode === 'brute' ? 'força bruta' : 'Quadtree'}` +
    (sim.selection ? `\nEncontradas: ${sim.selectedCount}` : '') +
    (didactic === 'waiting' ? '\nModo didático: aguardando colisão' : '') +
    (didactic === 'cooldown'
      ? `\nModo didático: próxima pausa em ${Math.ceil((cooldownEnd - now) / 1000)} s`
      : '');
}

function loop(now) {
  const elapsed = Math.min(Math.max(now - lastTime, 0), 250);
  lastTime = now;

  if (didactic === 'cooldown' && now >= cooldownEnd) didactic = 'waiting';

  if (didactic !== 'presenting') {
    const targetFps = Number(fpsSelect.value);
    if (targetFps === 0) {
      stepOnce();
      stepsSinceStats++;
    } else {
      const interval = 1000 / targetFps;
      stepAccumulator = Math.min(stepAccumulator + elapsed, interval * 4);
      while (stepAccumulator >= interval && didactic !== 'presenting') {
        stepOnce();
        stepAccumulator -= interval;
        stepsSinceStats++;
      }
    }
  } else {
    stepAccumulator = 0;
  }

  if (didactic === 'presenting') {
    drawTrace(ctx, sim, trace.steps, trace.index, showGridInput.checked, trace.pair);
    updateTraceStats();
  } else {
    draw(ctx, sim, showGridInput.checked, dragRect);
    updateStats(now);
  }
  drawSpeedChart(speedCtx, speedSeries, sim.mode, MAX_SPEED_SAMPLES);
  requestAnimationFrame(loop);
}

resizeCanvas();
restart();
requestAnimationFrame(loop);
