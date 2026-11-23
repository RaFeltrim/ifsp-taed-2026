# Research: Modo Didático Disparado por Colisão

## R1. Saber se houve colisão antes de resolver

- **Decision**: dividir `detectAndResolve()` em `detect()` (detecta conforme `mode`,
  atualiza `tests`, devolve `{ pairs, tests }`, não altera partículas) e
  `resolve(pairs)` (ricochete, `colliding`, seleção). `detectAndResolve()` passa a ser
  `this.resolve(this.detect().pairs)`, então `step()` não muda.
- **Rationale**: no estado "aguardando", cada frame faz `moveAndBuildTree()` e `detect()`;
  se `pairs` estiver vazio, chama `resolve([])` e segue; se não, pausa *antes* do
  `resolve`, com as posições do instante da colisão (FR-001). Nenhuma detecção extra.
- **Alternatives considered**: gerar o trace em todo frame e procurar colisões nele
  (muito mais caro); detectar duas vezes (desperdício).

## R2. Qual colisão é apresentada

- **Decision**: o par apresentado é `pairs[0]` da detecção do modo atual.
- **Rationale**: é a primeira colisão encontrada pela ordem da detecção (spec,
  Assumptions). O `buildTrace` percorre na mesma ordem que `findPairsBruteForce` e
  `findPairsQuadtree` (na Quadtree, a concatenação dos `found` por nó é igual ao retorno
  da `query`), então o primeiro passo `test` com `overlap` do trace é esse mesmo par —
  verificável por teste (SC-004).
- **Alternatives considered**: escolher aleatoriamente (pior para teste e explicação).

## R3. Encontrar o passo do par (tecla Enter, destaque no painel)

- **Decision**: função pura `findPairStepIndex(steps, a, b)` em `simulation.js`: índice
  do passo `test` cujo par é `{a, b}` (em qualquer ordem); `-1` se não existir.
- **Rationale**: Enter = `index = findPairStepIndex(...)`; o painel marca o passo atual
  quando `index` é esse. Ao trocar o modo de detecção, o mesmo par é procurado no novo
  trace (edge case "trocar modo mantém as partículas verdes").
- **Alternatives considered**: guardar o índice no `buildTrace` (acopla o trace ao modo
  disparado por colisão).

## R4. Estados e intervalo

- **Decision**: `didactic` em `main.js` com valores `'off' | 'waiting' | 'presenting' |
  'cooldown'`, `trace` (`{ steps, index, pair, pairIndex }`) só durante `'presenting'` e
  `cooldownEnd` (horário em ms) durante `'cooldown'`. O tempo vem do `now` do
  `requestAnimationFrame` (`performance.now()`), em tempo real.
- **Rationale**: uma variável de estado + dois dados auxiliares cobre todos os fluxos da
  spec; o `now` do loop já existe para o FPS.
- **Alternatives considered**: `setTimeout` para o intervalo (mais um lugar com estado,
  precisa ser cancelado ao desligar/recomeçar).

## R5. Cores: verde só para o par apresentado

- **Decision**: no `drawTrace`, o par apresentado é preenchido em verde (`#4f4`). As
  demais cores verdes do modo didático mudam: linha de teste sem colisão → amarelo
  (`#fd3`), nó que toca a região → ciano (`#4cf`). A grade completa mantém o verde
  suave e semitransparente da feature 001 (`rgba(120, 255, 120, 0.35)`), que se
  distingue do verde vivo do par. Vermelho continua para colisões encontradas e nós
  descartados.
- **Rationale**: FR-003 exige que o verde vivo seja exclusivo do par; o usuário aceitou a
  grade num verde mais suave. A seleção (amarela) não aparece durante a apresentação,
  então o amarelo fica livre.
- **Alternatives considered**: manter o verde nos nós e usar outra cor para o par (o
  usuário pediu verde para o par).

## R6. Teclas e mouse

- **Decision**: as teclas do modo (→, ←, Shift, Enter, Esc) só são tratadas em
  `'presenting'` (com `preventDefault`); nos estados `'waiting'` e `'cooldown'` o teclado
  fica livre. O mouse é ignorado só em `'presenting'`; em `'waiting'` e `'cooldown'` a
  seleção por região funciona normalmente (FR-003a).
- **Rationale**: fora da apresentação não há passos para navegar e a animação está
  rodando, então a seleção continua útil.

## R7. Ligar, desligar, recomeçar, trocar modo

- **Decision**:
  - Ligar (≤ 200 partículas) → `'waiting'`; > 200 → continua `'off'` com aviso.
  - Desligar em `'presenting'` → `resolve(pairs)` e `'off'`; em `'waiting'`/`'cooldown'` →
    `'off'`.
  - `restart()` com o modo ligado → `'waiting'` (descarta trace e intervalo); > 200 →
    `'off'` com aviso.
  - Trocar modo em `'presenting'` → refaz `buildTrace`, mantém o mesmo par, `index = 0`,
    `pairIndex` recalculado.
  - → além do último passo ou Esc → `resolve(pairs)`, `'cooldown'`, `cooldownEnd =
    now + 5000`.
- **Rationale**: cobre FR-005 a FR-008 e todos os casos de borda da spec.
