---

description: "Task list for Modo Didático Disparado por Colisão"
---

# Tasks: Modo Didático Disparado por Colisão

**Input**: Design documents from `/specs/003-collision-triggered-didactic/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/modules.md, quickstart.md

**Tests**: Incluídos apenas para a lógica pura (`simulation.js`), conforme FR-009 e o
Princípio IV da constituição. `renderer.js` e `main.js` são verificados manualmente via
[quickstart.md](./quickstart.md).

**Organization**: Tasks agrupadas por user story (US1–US2 da spec).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Pode rodar em paralelo (arquivos diferentes, sem dependência pendente)
- **[Story]**: User story da spec (US1–US2)

## Regras gerais (valem para todas as tasks)

- Trabalhar na branch local `003-collision-triggered-didactic`; **não** fazer push de
  branches de feature (só a `main` vai para o remoto, e quem faz o push é o usuário).
- Scripts clássicos, sem `import`/`export`; arquivos de lógica terminam com o
  `module.exports` condicional (feature 001).
- Testes em CommonJS com `node:test` e `node:assert/strict`; rodar com `node --test`.
- Código simples e didático, no estilo dos arquivos existentes (comentários em português
  explicando o porquê).
- Commits feitos pelo Claude, mensagens curtas, **sem** linha `Co-Authored-By` nem
  qualquer atribuição no final; testes passando antes de cada commit.

---

## Phase 1: Setup

- [X] T001 Na branch `003-collision-triggered-didactic`, commitar `specs/003-collision-triggered-didactic/` com a mensagem "Especificação do modo didático disparado por colisão"

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Saber se houve colisão antes de resolver (research R1), usado pelas duas stories

- [X] T002 Adicionar testes em `tests/simulation.test.js`: (a) para 300 partículas aleatórias (`sim.reset(300, 8, 800, 600)` + `sim.moveAndBuildTree()`), `sim.detect()` devolve nos dois modos os mesmos `pairs` (mesma ordem) e `tests` que `findPairsBruteForce` / `findPairsQuadtree`, atualiza `sim.tests` e não altera `x, y, vx, vy, colliding` de nenhuma partícula; (b) duas simulações montadas à mão com partículas sobrepostas: uma chama `detectAndResolve()`, a outra `resolve(detect().pairs)`; `x, y, vx, vy, colliding` ficam iguais
- [X] T003 Em `src/simulation.js`: dividir `detectAndResolve()` em `detect()` (passo 3: detecta conforme `mode`, `this.tests = tests`, devolve `{ pairs, tests }`) e `resolve(pairs)` (passos 4–5: zera `colliding`, `resolveCollision` em cada par marcando `colliding`, seleção); `detectAndResolve()` passa a ser `this.resolve(this.detect().pairs)`, com comentário explicando que a separação permite pausar antes de resolver
- [X] T004 Rodar `node --test` (todos passam); commit "Separa detecção e resolução de colisões"

**Checkpoint**: É possível olhar os pares de um frame antes do ricochete

---

## Phase 3: User Story 1 - Pausar automaticamente quando uma colisão acontece (Priority: P1) 🎯 MVP

**Goal**: Com o modo ligado, a animação roda até a primeira colisão; pausa e apresenta o frame inteiro desde o passo 1, com o par em verde, Enter levando ao teste do par e o painel marcando esse passo.

**Independent Test**: Cenários 1–6 e 11–13 do [quickstart.md](./quickstart.md); testes automatizados de `findPairStepIndex` e de "par apresentado = primeiro par da detecção".

- [X] T005 [US1] Adicionar testes em `tests/simulation.test.js` (importar `findPairStepIndex`): para 300 partículas aleatórias (raio 8, 800×600) e nos dois modos, o primeiro passo `'test'` com `overlap` de `buildTrace` tem o mesmo par (em qualquer ordem) que `detect().pairs[0]`; `findPairStepIndex(steps, a, b)` devolve exatamente esse índice, também com `a` e `b` trocados; devolve `-1` para um par que não foi testado (ex.: duas partículas distantes no modo `'quadtree'`)
- [X] T006 [US1] Em `src/simulation.js`: função `findPairStepIndex(steps, a, b)` — índice do passo `{ type: 'test' }` com `(p, q)` igual a `(a, b)` ou `(b, a)`; `-1` se não houver; adicionar ao `module.exports`
- [X] T007 [P] [US1] Em `src/renderer.js`: `drawTrace(ctx, sim, steps, index, showGrid, pair)` — partículas de `pair` (`[a, b]` ou `null`) preenchidas em verde `#4f4` em todos os passos (por cima das regras de cor atuais); trocar as demais cores verdes do modo didático: linha do teste atual sem colisão → amarelo `#fd3`, nós com `hit` → ciano `#4cf`; a grade completa mantém o verde suave `COLOR_GRID` (distinto do verde vivo `#4f4` do par); vermelho continua para colisões encontradas e nós descartados (research R5)
- [X] T008 [US1] Em `src/main.js`: substituir o estado `trace` da feature 002 por `let didactic = 'off'` (`'off' | 'waiting' | 'presenting' | 'cooldown'`) e `trace = { steps, index, pair, pairs, pairIndex }` só em `'presenting'`; `#stepBtn`: de `'off'` com até `MAX_TRACE_PARTICLES` partículas → `'waiting'` e limpa aviso (acima → aviso, continua `'off'`); de qualquer outro estado → `'off'`, chamando `sim.resolve(trace.pairs)` se estava `'presenting'`; no `loop`: `'off'` → `step` + `draw` como hoje; `'waiting'` → `sim.moveAndBuildTree()`, `const { pairs } = sim.detect()`; se `pairs.length === 0` → `sim.resolve(pairs)` + `draw`; senão monta o trace (`pair = pairs[0]`, `steps = buildTrace(...)`, `index = 0`, `pairIndex = findPairStepIndex(steps, ...pair)`) e muda para `'presenting'`; `'presenting'` → `drawTrace(..., trace.pair)` + painel; remover `startTraceFrame`/`nextTraceFrame` que não forem mais usados
- [X] T009 [US1] Em `src/main.js` (teclado, só em `'presenting'`, com `preventDefault`): manter → / ← / Shift da feature 002; → além do último passo (temporariamente, até a US2) → `sim.resolve(trace.pairs)` e volta a `'waiting'`; **Enter** → `trace.index = trace.pairIndex`; troca do modo de detecção em `'presenting'` → refaz `steps` com o mesmo `pair`, `index = 0`, novo `pairIndex`; `restart()` com o modo ligado → `'waiting'` (descarta trace) ou `'off'` com aviso se > 200; mouse ignorado só com `didactic === 'presenting'` (em `'waiting'` e `'cooldown'` a seleção funciona; FR-003a)
- [X] T010 [US1] Em `src/main.js` (painel): `'waiting'` → estatísticas normais + linha "Modo didático: aguardando colisão"; `'presenting'` → "MODO DIDÁTICO (força bruta|Quadtree)", "Colisão apresentada: #a × #b", "Passo k / N", descrição do passo (acrescentar " ← colisão que disparou a pausa" quando `index === pairIndex`), testes e colisões até ali, e a dica "→ ← passo · Shift partícula · Enter colisão · Esc continuar"
- [X] T011 [US1] Rodar `node --test`; validar cenários 1–6 e 11–13 do quickstart (os cenários 1, 2 e 9 cobrem o SC-001: pausa só com colisão); commit "Modo didático pausa na primeira colisão"

**Checkpoint**: MVP — pausa na colisão com o par verde e Enter

---

## Phase 4: User Story 2 - Intervalo de 5 segundos entre apresentações (Priority: P1)

**Goal**: Esc ou → no último passo encerram a apresentação; a animação volta e por 5 s nenhuma colisão pausa, com contagem regressiva no painel.

**Independent Test**: Cenários 7–10 e 14 do quickstart.

- [X] T012 [US2] Em `src/main.js`: constante `COOLDOWN_MS = 5000` e variável `cooldownEnd`; função `endPresentation()` → `sim.resolve(trace.pairs)`, `trace = null`, `didactic = 'cooldown'`, `cooldownEnd = performance.now() + COOLDOWN_MS`; **Esc** em `'presenting'` e → além do último passo chamam `endPresentation()` (substitui o comportamento temporário do T009); no `loop`, `'cooldown'` → `step` + `draw` normais e, quando `now >= cooldownEnd`, `didactic = 'waiting'`; desligar ou `restart()` durante o intervalo descartam o intervalo (data-model)
- [X] T013 [US2] Em `src/main.js` (painel): em `'cooldown'`, estatísticas normais + "Modo didático: próxima pausa em N s" (`N = Math.ceil((cooldownEnd − now) / 1000)`)
- [X] T014 [US2] Rodar `node --test`; validar cenários 7–10, 14 e 15 do quickstart; commit "Modo didático: intervalo de 5 s entre colisões"

**Checkpoint**: Modo didático disparado por colisão completo

---

## Phase 5: Polish & Cross-Cutting Concerns

- [X] T015 [P] Atualizar a seção "Modo didático" do `README.md`: aguarda colisão, par em verde, Enter, Esc, intervalo de 5 s, novas cores (amarelo, ciano, cinza)
- [X] T016 Revisar `src/*.js` alterados (sem código morto da feature 002, comentários explicando os estados e a separação detect/resolve)
- [ ] T017 Executar todos os cenários de [quickstart.md](./quickstart.md); rodar `node --test`; commit "README do modo didático disparado por colisão"
- [X] T018 Fazer merge local da branch na `main` (`git checkout main && git merge --ff-only 003-collision-triggered-didactic`); **não** fazer push — avisar o usuário que a `main` está pronta para ele enviar

---

## Dependencies & Execution Order

- **Setup (T001)** → **Foundational (T002–T004)** → **US1 (T005–T011)** → **US2 (T012–T014)** → **Polish (T015–T018)**
- US2 depende de US1 (estado `didactic`, trace e teclado).
- Dentro de cada story: testes → lógica (`simulation.js`) → desenho → `main.js` → commit.

## Parallel Opportunities

- US1: T007 (`renderer.js`) em paralelo com T005/T006 (`simulation`).
- Polish: T015 (`README.md`) em paralelo com T016.

```text
# US1 em paralelo:
T005/T006 tests/simulation.test.js + src/simulation.js
T007      src/renderer.js
```

## Implementation Strategy

1. **MVP**: Setup + Foundational + US1 → pausa na primeira colisão, par verde, Enter.
2. **Completa**: US2 → Esc e intervalo de 5 s.
3. Commit ao fim de cada fase, testes passando, sem linha de coautoria; merge na `main`
   local no fim, push feito pelo usuário.
