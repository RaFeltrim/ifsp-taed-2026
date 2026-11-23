---

description: "Task list for Modo Didático Passo a Passo"
---

# Tasks: Modo Didático Passo a Passo

**Input**: Design documents from `/specs/002-didactic-step-mode/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/modules.md, quickstart.md

**Tests**: Incluídos apenas para a lógica pura (`quadtree.js`, `simulation.js`), conforme
FR-014 e o Princípio IV da constituição. `renderer.js`, `main.js` e `index.html` são
verificados manualmente via [quickstart.md](./quickstart.md).

**Organization**: Tasks agrupadas por user story (US1–US3 da spec).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Pode rodar em paralelo (arquivos diferentes, sem dependência pendente)
- **[Story]**: User story da spec (US1–US3)

## Regras gerais (valem para todas as tasks)

- Continuar com scripts clássicos, sem `import`/`export`; arquivos de lógica terminam com
  `if (typeof module !== 'undefined') module.exports = { ... }` (feature 001, research R1/R2).
- Testes em CommonJS com `node:test` e `node:assert/strict`; rodar com `node --test`.
- Código simples e didático, no mesmo estilo dos arquivos existentes (comentários em
  português explicando o porquê).
- Commits feitos pelo Claude, mensagens curtas, **sem** linha `Co-Authored-By` nem
  qualquer atribuição no final; testes passando antes de cada commit.

---

## Phase 1: Setup

- [X] T001 Criar a branch `002-didactic-step-mode` a partir de `001-particle-collision-demo` (`git checkout -b 002-didactic-step-mode`) e commitar `specs/002-didactic-step-mode/` e `.specify/feature.json` com a mensagem "Especificação do modo didático"

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Pausar o frame entre "mover + montar árvore" e "detectar + resolver" (research R1), usado por todas as stories

- [X] T002 Adicionar teste em `tests/simulation.test.js`: duas simulações montadas à mão (partículas com velocidade, duas delas sobrepostas após o movimento); uma chama `step()`, a outra `moveAndBuildTree()` + `detectAndResolve()`; `x, y, vx, vy, colliding` de todas as partículas ficam iguais
- [X] T003 Em `src/simulation.js`: dividir `step()` em `moveAndBuildTree()` (passos 1–2: mover e reconstruir `this.tree`) e `detectAndResolve()` (passos 3–5: detectar conforme `mode`, `tests`, resolver, `colliding`, seleção); `step()` passa a chamar as duas, com comentário explicando que a divisão serve para o modo didático parar entre elas
- [X] T004 Rodar `node --test` (todos os testes antigos e o novo passam); commit "Divide o passo do frame em duas metades"

**Checkpoint**: Simulação pode ser pausada no instante da detecção

---

## Phase 3: User Story 1 - Percorrer a detecção iteração por iteração (Priority: P1) 🎯 MVP

**Goal**: Ligar o modo didático (até 200 partículas), pausar, e avançar/voltar com → / ← vendo cada teste de par em força bruta, com painel explicativo.

**Independent Test**: Cenários 1, 2, 3, 7, 10 e 11 do [quickstart.md](./quickstart.md) em força bruta; testes automatizados de `buildTrace` no modo `'brute'`.

- [X] T005 [US1] Adicionar testes em `tests/simulation.test.js` (importar `buildTrace`): para 300 partículas aleatórias (raio 8, área 800×600), `buildTrace(particles, tree, 'quadtree')` já tem número de passos `'test'` = `findPairsQuadtree(particles, tree).tests` e os mesmos pares com `overlap`; e `buildTrace(particles, tree, 'brute')` tem número de passos `'test'` = `findPairsBruteForce(particles).tests`, mesmos pares com `overlap = true` (comparar como conjunto de chaves `"menorId-maiorId"`), último passo com `tests` e `collisions` iguais ao total de testes e de pares, nenhum passo `'visit'`, um passo `'particle'` por partícula com `range = null`, o primeiro passo é `'particle'` e `tests`/`collisions` nunca diminuem ao longo da lista
- [X] T006 [US1] Em `src/simulation.js`: criar `buildTrace(particles, tree, mode)` com os dois ramos, para o modo didático nunca ficar sem passos: ramo `'brute'` — para cada `i`, passo `{ type: 'particle', p, range: null, tests, collisions }` e, para cada `j > i`, passo `{ type: 'test', p, q, overlap, tests, collisions }`; ramo `'quadtree'` (versão inicial, sem visitas) — para cada `p`, `range = new Rect(p.x − 2p.r, p.y − 2p.r, 4p.r, 4p.r)`, passo `'particle'` com `range` e depois passos `'test'` com cada candidata de `tree.query(range)` que tenha `q.id > p.id`; `tests`/`collisions` acumulados; comentário no topo descrevendo os três tipos de passo (data-model); não altera partículas nem árvore; adicionar `buildTrace` ao `module.exports`
- [X] T007 [P] [US1] Em `index.html`: depois de `#modeBtn`, adicionar `<button id="stepBtn">Modo didático: desligado</button>` e `<div id="notice"></div>` (aviso, vazio por padrão); em `style.css`, estilo de `#notice` em amarelo e fonte menor
- [X] T008 [P] [US1] Em `src/renderer.js`: função `drawTrace(ctx, sim, steps, index, showGrid)` — fundo; grade completa se `showGrid`; todas as partículas apagadas (cor clara semitransparente), exceto as que aparecem em algum passo `'test'` com `overlap` entre `0..index` (vermelhas); voltar de `index` até o passo `'particle'` mais próximo (`start`); desenhar em cinza fino as linhas dos testes de `start..index−1` e a do teste atual mais grossa (verde sem colisão, vermelha com colisão) com anel branco na partícula `q`; anel branco grosso na partícula analisada `p`
- [X] T009 [US1] Em `src/main.js`: constante `MAX_TRACE_PARTICLES = 200` e estado `let trace = null` (`{ steps, index }`); funções `rebuildTrace()` (`buildTrace(sim.particles, sim.tree, sim.mode)`, `index = 0`) e `startTraceFrame()` (`sim.moveAndBuildTree()` + `rebuildTrace()`); clique em `#stepBtn`: se ligado → `sim.detectAndResolve()`, `trace = null`; se desligado e `sim.particles.length > MAX_TRACE_PARTICLES` → não liga e `#notice` = "Modo didático: reduza para até 200 partículas"; senão `startTraceFrame()` e limpa `#notice`; atualizar rótulo do botão ("Modo didático: ligado/desligado") e `stepBtn.blur()`
- [X] T010 [US1] Em `src/main.js`: listener `keydown` na janela que, só com `trace` ligado, trata `ArrowRight` (`index + 1`, sem passar do último passo por enquanto) e `ArrowLeft` (`index − 1`, mínimo 0) e chama `e.preventDefault()` (para o slider em foco não mudar); função `describeStep(s)` com os textos de [contracts/modules.md](./contracts/modules.md) para `'particle'` (força bruta) e `'test'` (distância com 1 casa decimal e distância mínima `p.r + q.r`); função `updateTraceStats()` que escreve em `#stats`: "MODO DIDÁTICO (força bruta|Quadtree)", "Passo k / N", descrição, "Testes até aqui", "Colisões até aqui" e "→ ← passo   Shift+→ ← partícula"; no `loop`, com `trace` ligado chamar `drawTrace` + `updateTraceStats` em vez de `step` + `draw`
- [X] T011 [US1] Rodar `node --test`; validar cenários 1, 2, 3, 7, 10 e 11 do quickstart em força bruta (cobre também o cenário 4 da US2 da spec: linhas a cada teste na força bruta) e conferir que ligar o modo didático em Quadtree mostra partícula + testes sem erro; commit "Modo didático: passos da força bruta"

**Checkpoint**: MVP — percorrer a força bruta passo a passo

---

## Phase 4: User Story 2 - Ver o caminho da Quadtree até as candidatas (Priority: P1)

**Goal**: No modo Quadtree, mostrar a região de busca, cada nó visitado (tocou / descartado) e os testes intercalados logo após cada nó (FR-006a).

**Independent Test**: Cenário 5 do quickstart; testes automatizados de `query` com caminho e de `buildTrace` no modo `'quadtree'`.

- [X] T012 [P] [US2] Adicionar teste em `tests/quadtree.test.js`: com 300 pontos aleatórios em 1000×1000 e range `Rect(100, 100, 150, 150)`, `query(range, [], visited)` devolve o mesmo que `query(range)`; `visited[0].node` é a raiz com `hit = true`; a concatenação de todos os `visited[i].found` (na ordem) é igual ao retorno; todo registro com `hit = false` tem `found` vazio e nenhum descendente do nó aparece em `visited`
- [X] T013 [US2] Em `src/quadtree.js`: parâmetro opcional `visited = null` em `query(range, found = [], visited = null)`; calcular `hit = this.boundary.intersects(range)`; se `visited`, registrar `{ node: this, hit, found: [] }` e preencher esse `found` com os itens deste nó dentro do range (além de colocá-los no `found` geral); só descer nos filhos se `hit`, repassando `visited`; comentário explicando que o registro serve ao modo didático e que sem `visited` nada muda
- [X] T014 [US2] Adicionar testes em `tests/simulation.test.js`: para 300 partículas aleatórias, `buildTrace(particles, tree, 'quadtree')` tem número de passos `'test'` = `findPairsQuadtree(particles, tree).tests`, mesmos pares com `overlap` (como conjunto), totais do último passo corretos, um `'particle'` por partícula com `range` de lado `4r` centrado nela, existe ao menos um `'visit'` com `hit = true` e todo `'test'` está depois de um `'visit'` da mesma partícula (intercalação)
- [X] T015 [US2] Em `src/simulation.js`: completar o ramo `'quadtree'` de `buildTrace` (substitui a versão inicial do T006): para cada `p`, passo `'particle'` com `range`; `tree.query(range, [], visited)`; para cada registro de `visited`, passo `{ type: 'visit', p, range, node, hit, tests, collisions }` seguido imediatamente dos passos `'test'` com os `q` de `found` que têm `q.id > p.id` (research R5)
- [X] T016 [P] [US2] Em `src/renderer.js` (`drawTrace`): se o passo `'particle'` da partícula atual tem `range`, desenhá-lo tracejado em branco; desenhar os nós dos passos `'visit'` de `start..index` — verde se `hit`, vermelho se descartado, linha mais grossa no nó do passo atual
- [X] T017 [US2] Em `src/main.js` (`describeStep`): textos de `'particle'` em Quadtree ("Partícula #i: buscar vizinhas na região tracejada") e de `'visit'` ("Nó nível d toca a região → examina e desce" / "Nó nível d fora da região → descartado")
- [X] T018 [US2] Rodar `node --test`; validar cenários 4 e 5 do quickstart; commit "Modo didático: caminho na Quadtree"

**Checkpoint**: Os dois algoritmos podem ser percorridos passo a passo

---

## Phase 5: User Story 3 - Navegar rápido e seguir para o próximo frame (Priority: P2)

**Goal**: Shift + →/← entre partículas, → no último passo avança o frame, troca de modo refaz o trace, reinícios respeitam o limite.

**Independent Test**: Cenários 6, 8, 9 e 12 do quickstart.

- [X] T019 [US3] Em `src/main.js` (listener `keydown`): Shift + → avança até o próximo passo `'particle'`; Shift + ← faz `index − 1` e volta até o passo `'particle'` anterior (mínimo 0); → ou Shift + → além do último passo chama `nextTraceFrame()` = `sim.detectAndResolve()` + `startTraceFrame()`
- [X] T020 [US3] Em `src/main.js`: no clique de `#modeBtn` (troca do modo de detecção), se `trace` ligado, chamar `rebuildTrace()` (mesmo frame, outro algoritmo); em `restart()`, depois do `reset`: com até `MAX_TRACE_PARTICLES` partículas, limpar `#notice` e, se `trace` ligado, chamar `startTraceFrame()`; acima disso, se `trace` ligado, `trace = null`, rótulo do botão "Modo didático: desligado" e o aviso em `#notice`
- [X] T020a [US3] Em `src/main.js`: no handler de `mousedown` do canvas, sair sem fazer nada se `trace` estiver ligado (o mouse é ignorado no modo didático; arrastar não cria nem altera a seleção)
- [X] T021 [US3] Validar cenários 6, 8, 9, 12, 13 e 14 do quickstart; commit "Modo didático: navegação entre partículas e frames"

**Checkpoint**: Modo didático completo

---

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T022 [P] Atualizar `README.md`: seção "Modo didático" (como ligar, limite de 200 partículas, teclas → ← e Shift, o que significam as cores)
- [X] T023 Revisar `src/*.js` alterados quanto a simplicidade e didática (sem código morto, comentários explicando as duas metades do frame, o registro do caminho e a intercalação dos testes)
- [ ] T024 Executar todos os cenários de [quickstart.md](./quickstart.md); rodar `node --test`; commit "README do modo didático"

---

## Dependencies & Execution Order

- **Setup (T001)** → **Foundational (T002–T004)** → **US1 (T005–T011)** → **US2 (T012–T018)** → **US3 (T019–T021)** → **Polish (T022–T024)**
- US2 depende de US1 (estende `buildTrace`, `drawTrace` e `describeStep`); US3 depende de US1 (estado `trace` e teclado) e é mais útil depois de US2.
- Dentro de cada story: testes → lógica (`quadtree.js` / `simulation.js`) → desenho → `main.js` → commit.

## Parallel Opportunities

- US1: T007 (`index.html`/`style.css`) e T008 (`renderer.js`) em paralelo com T005/T006 (`simulation`).
- US2: T012 (`tests/quadtree.test.js`) em paralelo com T014; T016 (`renderer.js`) em paralelo com T015 (`simulation.js`).
- Polish: T022 em paralelo com T023.

```text
# US1 em paralelo:
T005/T006 tests/simulation.test.js + src/simulation.js
T007      index.html + style.css
T008      src/renderer.js
```

## Implementation Strategy

1. **MVP**: Setup + Foundational + US1 → força bruta passo a passo e Quadtree já
   funcionando (partícula, região e testes com as candidatas), com limite de 200.
2. **Incremento principal**: US2 → o caminho completo na Quadtree (nós visitados e
   descartados, testes intercalados) — o objetivo central do modo didático.
3. **Conforto**: US3 → atalhos e continuidade entre frames.
4. Commit ao fim de cada fase, com testes passando e sem linha de coautoria.
