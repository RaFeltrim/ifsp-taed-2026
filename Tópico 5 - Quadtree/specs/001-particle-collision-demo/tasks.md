---

description: "Task list for Demo de Colisão de Partículas com Quadtree"
---

# Tasks: Demo de Colisão de Partículas com Quadtree

**Input**: Design documents from `/specs/001-particle-collision-demo/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/modules.md, quickstart.md

**Tests**: Incluídos apenas para a lógica pura (`particle.js`, `quadtree.js`,
`simulation.js`), conforme FR-012 e o Princípio IV da constituição. `renderer.js` e
`main.js` são verificados manualmente via [quickstart.md](./quickstart.md).

**Organization**: Tasks agrupadas por user story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Pode rodar em paralelo (arquivos diferentes, sem dependência pendente)
- **[Story]**: User story da spec (US1–US4)

## Regras gerais (valem para todas as tasks)

- Scripts clássicos, **sem** `import`/`export` nem `type="module"` (research R1).
- Arquivos de lógica terminam com `if (typeof module !== 'undefined') module.exports = { ... }`
  (research R2). Nunca usar `var/let/const { X } = require(...)` em `src/`.
- Testes em CommonJS: `const test = require('node:test'); const assert = require('node:assert/strict');`
  e `require('../src/<arquivo>.js')`. Rodar com `node --test`.
- Código simples e didático: funções curtas, comentários explicando o porquê, sem
  abstrações extras (constituição, Princípios I e II).
- Commits feitos pelo Claude, mensagens curtas, **sem** linha `Co-Authored-By` nem
  qualquer atribuição no final.

---

## Phase 1: Setup

**Purpose**: Estrutura do projeto e repositório

- [X] T001 Inicializar repositório git na raiz (`git init`), criar `.gitignore` com `.DS_Store` e `node_modules/`, e remover o comentário "Sync Impact Report" do topo de `.specify/memory/constitution.md`
- [X] T002 Criar `index.html` na raiz: `<canvas id="canvas">` ocupando a janela inteira e um `<div id="panel">` sobreposto no canto superior esquerdo contendo: slider `#count` (min 10, max 2000, value 200) com `<span id="countValue">`, `<select id="radius">` com opções 2, 4, 8, 16, 32 (selecionado 4), `<button id="modeBtn">`, checkbox `#showGrid` com rótulo "Mostrar grade", e `<pre id="stats">`; carregar no fim do `<body>`, nesta ordem e sem `type="module"`: `src/particle.js`, `src/quadtree.js`, `src/simulation.js`, `src/renderer.js`, `src/main.js`
- [X] T003 [P] Criar `style.css` mínimo: `body` sem margem e `overflow: hidden`, canvas `display: block`, painel com fundo semitransparente escuro, texto claro, padding pequeno e fonte monoespaçada em `#stats`
- [X] T004 [P] Criar diretórios `src/` e `tests/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Partícula e Quadtree, usadas por todas as stories (a árvore é construída em todo frame — research R3)

**⚠️ CRITICAL**: Nenhuma story começa antes desta fase

- [X] T005 [P] Escrever testes em `tests/particle.test.js`: `move` soma velocidade; ao passar da borda esquerda/direita/superior/inferior a partícula fica encostada (`x = r`, `x = width − r`, etc.) e a componente da velocidade aponta para dentro; `particlesOverlap` é `true` com distância < `a.r + b.r` e `false` quando exatamente encostadas; `resolveCollision` de duas partículas frontais se aproximando troca as velocidades normais e as deixa a distância `a.r + b.r`; se estão se afastando, velocidades não mudam; centros coincidentes usam normal (1, 0) sem gerar `NaN`
- [X] T006 [P] Escrever testes em `tests/quadtree.test.js`: `Rect.contains` com borda esquerda/superior inclusiva e direita/inferior exclusiva; `Rect.intersects` para retângulos sobrepostos, encostados e separados; `insert` retorna `false` fora do `boundary`; após inserir `capacity + 1` pontos espalhados, `children` tem 4 nós e `items` da raiz está vazio; inserir 50 pontos idênticos não estoura a pilha e nenhum nó tem `depth > maxDepth`; `query` retorna exatamente os pontos dentro do range (comparar com filtro linear sobre 500 pontos aleatórios)
- [X] T007 [P] Implementar `src/particle.js`: `class Particle` com `constructor(id, x, y, vx, vy, r)` e campos `id, x, y, vx, vy, r, colliding = false, selected = false`; método `move(width, height)` conforme contrato ("ao ultrapassar uma borda, reposiciona encostada nela e inverte a componente para dentro"); função `particlesOverlap(a, b)` ("`true` se `distância(a, b) < a.r + b.r`", comparar distâncias ao quadrado); função `resolveCollision(a, b)`: normal `n = (b − a)/dist` (centros iguais → `(1, 0)`), separar cada uma por metade da sobreposição ao longo de `n`, e se `(a.v − b.v)·n > 0` subtrair essa componente de `a.v` e somar em `b.v`; exportar `{ Particle, particlesOverlap, resolveCollision }`
- [X] T008 [P] Implementar `src/quadtree.js`: `class Rect` (`x, y, w, h`, `contains(px, py)`, `intersects(other)`) e `class Quadtree` com `constructor(boundary, capacity = 4, depth = 0, maxDepth = 8)`, campos `items = []` e `children = null`; `insert(item)` (fora do boundary → `false`; folha com espaço ou `depth == maxDepth` → guarda em `items`; folha cheia → `subdivide()` move os itens para os 4 filhos e insere o novo no filho certo); `subdivide()` cria NE, NW, SE, SW com `depth + 1`; `query(range, found = [])` não desce em nós que não intersectam `range` e adiciona itens com `range.contains(item.x, item.y)`; exportar `{ Rect, Quadtree }`
- [X] T009 Rodar `node --test` e garantir que T005–T006 passam; commit "Partícula e Quadtree com testes"

**Checkpoint**: Lógica base pronta e testada

---

## Phase 3: User Story 1 - Partículas quicando e colidindo (Priority: P1) 🎯 MVP

**Goal**: Partículas se movem, quicam nas bordas, ricocheteiam entre si e ficam vermelhas ao colidir; painel com FPS, partículas, testes; raio selecionável e resize reiniciam a simulação. Detecção por força bruta.

**Independent Test**: Abrir `index.html` e verificar os cenários 1, 2, 3, 7 e 8 de [quickstart.md](./quickstart.md).

- [X] T010 [US1] Escrever testes em `tests/simulation.test.js`: `findPairsBruteForce` retorna `tests = n(n−1)/2` (ex.: 200 → 19900), com 1 partícula `tests = 0` e nenhum par, e encontra exatamente os pares sobrepostos de um cenário montado à mão; `reset(count, radius, w, h)` cria `count` partículas com `r = radius`, ids 0..count−1, todas dentro de `[r, w−r] × [r, h−r]`; após `step()` em um cenário montado à mão (`sim.width/height` definidos e `sim.particles` com duas partículas sobrepostas e uma isolada, todas com `vx = vy = 0`), as duas sobrepostas têm `colliding = true` e a isolada `colliding = false`
- [X] T011 [US1] Implementar em `src/simulation.js`: no topo, `if (typeof require !== 'undefined') Object.assign(globalThis, require('./particle.js'), require('./quadtree.js'));` (com comentário explicando research R2); função `findPairsBruteForce(particles)` → `{ pairs, tests }` testando cada `i < j`; `class Simulation` com `constructor(width, height)` (campos `width, height, radius = 4, particles = [], mode = 'brute', tree = null, tests = 0, selection = null, selectedCount = 0`); `reset(count, radius, width, height)` cria partículas em posição aleatória dentro da área e velocidade aleatória (módulo entre 0.5 e 2 px/frame), zera `tests` e faz `selection = null`; `step()`: mover todas, construir `this.tree` (`new Quadtree(new Rect(0, 0, width, height))` + inserir todas), zerar `colliding`, detectar pares (por enquanto sempre força bruta), guardar `tests`, chamar `resolveCollision` em cada par e marcar `colliding = true` nos dois; exportar `{ Simulation, findPairsBruteForce }`
- [X] T012 [P] [US1] Implementar `src/renderer.js`: função global `draw(ctx, sim, showGrid, dragRect)` que limpa o canvas (fundo escuro) e desenha cada partícula como círculo preenchido — vermelho se `colliding`, cor clara padrão caso contrário (parâmetros `showGrid` e `dragRect` serão usados em US3/US4)
- [X] T013 [US1] Implementar `src/main.js`: obter canvas/contexto e elementos do painel; função `resizeCanvas()` ajusta `canvas.width/height` a `innerWidth/innerHeight`; função `restart()` chama `sim.reset(Number(count.value), Number(radius.value), canvas.width, canvas.height)`; eventos: `resize` → `resizeCanvas(); restart()`, `change` no `#radius` → `restart()`; loop com `requestAnimationFrame`: `sim.step()`, `draw(...)`, FPS com `performance.now()` em média suavizada; atualizar `#stats` ~4×/s com FPS, partículas, testes/frame e modo (research R7, R8)
- [X] T014 [US1] Rodar `node --test`; validar manualmente cenários 1, 2, 3, 7 e 8 do quickstart; commit "Simulação com força bruta, ricochete e painel"

**Checkpoint**: MVP funcional em força bruta

---

## Phase 4: User Story 2 - Comparar força bruta e Quadtree (Priority: P1)

**Goal**: Modo Quadtree com contagem correta de testes, botão de alternar e slider de quantidade.

**Independent Test**: Cenário 4 do quickstart (1000 partículas: Quadtree ≥10× menos testes, mesmos pares) e testes automatizados de equivalência.

- [X] T015 [US2] Adicionar testes em `tests/simulation.test.js`: para 500 partículas aleatórias (raio 8, área 800×600) e uma árvore construída com elas, `findPairsQuadtree` retorna o mesmo conjunto de pares que `findPairsBruteForce` (comparar como conjunto de chaves `"menorId-maiorId"`), sem pares duplicados, e com `tests` menor; com 1000 partículas de raio 4 em 1600×900, `tests` da Quadtree ≤ 1/10 da força bruta (SC-002)
- [X] T016 [US2] Implementar `findPairsQuadtree(particles, tree)` em `src/simulation.js`: para cada `p`, `tree.query(new Rect(p.x − 2p.r, p.y − 2p.r, 4p.r, 4p.r))`, e para cada candidata `q` com `q.id > p.id` contar um teste e, se `particlesOverlap`, adicionar o par (research R5); em `step()`, escolher a função conforme `this.mode` (`'brute'` | `'quadtree'`); adicionar `findPairsQuadtree` ao export
- [X] T017 [US2] Em `src/main.js`: `#modeBtn` alterna `sim.mode` entre `'brute'` e `'quadtree'` sem reiniciar e mostra o modo atual no rótulo; slider `#count` atualiza `#countValue` no `input` e chama `restart()` no `change`
- [X] T018 [US2] Rodar `node --test`; validar cenários 3 e 4 do quickstart; commit "Modo Quadtree e controles de modo e quantidade"

**Checkpoint**: Comparação entre modos funcionando

---

## Phase 5: User Story 3 - Visualizar a grade da Quadtree (Priority: P2)

**Goal**: Checkbox mostra/oculta os limites dos nós da Quadtree.

**Independent Test**: Cenário 5 do quickstart.

- [X] T019 [US3] Em `src/renderer.js`: função `drawTree(ctx, node)` recursiva que faz `strokeRect` de `node.boundary` com linha fina e cor discreta e percorre `node.children`; em `draw`, chamá-la com `sim.tree` quando `showGrid` for verdadeiro
- [X] T020 [US3] Em `src/main.js`: passar `showGrid.checked` para `draw`; validar cenário 5 do quickstart; commit "Exibição da grade da Quadtree"

**Checkpoint**: Grade visível sob demanda

---

## Phase 6: User Story 4 - Seleção por região (range query) (Priority: P3)

**Goal**: Arrastar o mouse define uma região; partículas encontradas pela range query ficam destacadas e o painel mostra a quantidade.

**Independent Test**: Cenário 6 do quickstart e teste automatizado da seleção.

- [X] T021 [US4] Adicionar testes em `tests/simulation.test.js`, montando `sim.particles` manualmente com partículas paradas (`vx = vy = 0`) e sem sobreposição: após `setSelection(rect)` e `step()`, `selected` é `true` exatamente para partículas com centro dentro do rect e `selectedCount` bate com essa contagem; `setSelection(null)` + `step()` zera `selected` e `selectedCount`; `reset` limpa a seleção
- [X] T022 [US4] Em `src/simulation.js`: método `setSelection(rect)` (aceita `Rect` ou `null`); ao fim de `step()`, zerar `selected` de todas e, se houver seleção, `this.tree.query(this.selection)` marca `selected = true` e define `selectedCount` (0 sem seleção)
- [X] T023 [US4] Em `src/renderer.js`: partículas com `selected` desenhadas com destaque distinto do vermelho (ex.: contorno amarelo); desenhar `dragRect` (se não nulo) ou `sim.selection` como retângulo tracejado
- [X] T024 [US4] Em `src/main.js`: `mousedown` guarda o ponto inicial; `mousemove` com botão pressionado atualiza `dragRect` normalizado (largura e altura positivas em qualquer direção) e chama `sim.setSelection(dragRect)`, para o destaque aparecer durante o arrasto; `mouseup` mantém a seleção se arrastou mais de 3 px, senão chama `sim.setSelection(null)`; limpar `dragRect`; mostrar "encontradas: N" em `#stats` quando há seleção
- [X] T025 [US4] Rodar `node --test`; validar cenário 6 do quickstart; commit "Seleção por região com range query"

**Checkpoint**: Todas as stories funcionando

---

## Phase 7: Polish & Cross-Cutting Concerns

- [X] T026 Revisar `src/*.js` quanto a simplicidade e didática: remover código morto, conferir comentários explicando subdivisão, consulta, busca de candidatas e ricochete
- [X] T027 [P] Criar `README.md` curto: o que é a demo, como abrir (`index.html`) e como testar (`node --test`)
- [ ] T028 Executar todos os cenários de [quickstart.md](./quickstart.md), incluindo o 1 (anima em < 2 s, SC-001) e o 9 (2000 partículas de raio 32); commit "Revisão final e README"

---

## Dependencies & Execution Order

- **Setup (T001–T004)** → **Foundational (T005–T009)** → **US1 (T010–T014)**
- **US2, US3, US4** dependem de US1 (usam `Simulation`, `draw` e o loop de `main.js`);
  entre si são independentes, mas tocam os mesmos arquivos — executar em sequência
  US2 → US3 → US4.
- **Polish** depois das stories desejadas.
- Dentro de cada story: testes → lógica (`simulation.js`) → desenho → `main.js` → commit.

## Parallel Opportunities

- Setup: T003 e T004 em paralelo após T002.
- Foundational: T005, T006, T007 e T008 em paralelo (quatro arquivos distintos).
- US1: T012 (`renderer.js`) em paralelo com T010/T011 (`simulation`).
- Polish: T027 em paralelo com T026.

```text
# Foundational em paralelo:
T005 tests/particle.test.js   T006 tests/quadtree.test.js
T007 src/particle.js          T008 src/quadtree.js
```

## Implementation Strategy

1. **MVP**: Setup + Foundational + US1 → demo em força bruta com ricochete e painel.
2. **Incremento principal**: US2 → comparação entre modos (objetivo didático central).
3. **Extras**: US3 (grade) e US4 (range query).
4. Commit ao fim de cada fase, com os testes passando e sem linha de coautoria.
