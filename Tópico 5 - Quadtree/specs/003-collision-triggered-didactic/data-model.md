# Data Model: Modo Didático Disparado por Colisão

Entidades das features 001 e 002 (`Particle`, `Rect`, `Quadtree`, `Simulation`, passos
do trace) continuam iguais. Abaixo o que muda ou é novo.

## Mudança em `Simulation`

| Método | Descrição |
|---|---|
| `detect()` | Detecta pares conforme `mode`, atualiza `tests`, devolve `{ pairs, tests }`. Não altera partículas. |
| `resolve(pairs)` | Zera e marca `colliding`, chama `resolveCollision` em cada par, aplica a seleção. |
| `detectAndResolve()` | `resolve(detect().pairs)` — mesmo resultado de antes. |

## Estado do modo didático (em `main.js`)

| Campo | Tipo | Descrição |
|---|---|---|
| `didactic` | `'off'` \| `'waiting'` \| `'presenting'` \| `'cooldown'` | Estado atual. |
| `trace` | `null` ou `{ steps, index, pair, pairs, pairIndex }` | Só em `'presenting'`. `pair` = `[a, b]` apresentado (verde); `pairs` = todos os pares do frame (para resolver ao encerrar); `pairIndex` = índice do passo `test` do par. |
| `cooldownEnd` | número (ms) | Só em `'cooldown'`: quando o intervalo termina. |
| `COOLDOWN_MS` | constante = 5000 | Duração do intervalo. |
| `MAX_TRACE_PARTICLES` | constante = 200 | Mantida da feature 002. |

## Transições

| De | Evento | Para | Efeito |
|---|---|---|---|
| `'off'` | Ligar, ≤ 200 partículas | `'waiting'` | Limpa aviso. |
| `'off'` | Ligar, > 200 | `'off'` | Aviso de limite. |
| `'waiting'` | Frame sem colisão | `'waiting'` | `moveAndBuildTree()`, `detect()`, `resolve([])`. |
| `'waiting'` | Frame com colisão | `'presenting'` | `moveAndBuildTree()`, `detect()`; `pair = pairs[0]`; `steps = buildTrace(...)`; `index = 0`; `pairIndex = findPairStepIndex(steps, ...pair)`. |
| `'presenting'` | →, ←, Shift | `'presenting'` | Navegação da feature 002 (→ no último passo encerra, ver abaixo). |
| `'presenting'` | Enter | `'presenting'` | `index = pairIndex`. |
| `'presenting'` | Esc ou → além do último | `'cooldown'` | `resolve(pairs)`; `cooldownEnd = now + COOLDOWN_MS`; `trace = null`. |
| `'presenting'` | Trocar modo de detecção | `'presenting'` | Novo `buildTrace` com o mesmo `pair`; `index = 0`; novo `pairIndex`. (`pairs` não muda: os dois modos acham os mesmos pares.) |
| `'cooldown'` | Frame com `now < cooldownEnd` | `'cooldown'` | `sim.step()` normal. |
| `'cooldown'` | Frame com `now ≥ cooldownEnd` | `'waiting'` | — |
| qualquer ≠ `'off'` | Desligar | `'off'` | Se `'presenting'`: `resolve(pairs)`. Descarta trace/intervalo. |
| qualquer ≠ `'off'` | `restart()`, ≤ 200 | `'waiting'` | Descarta trace/intervalo; limpa aviso. |
| qualquer ≠ `'off'` | `restart()`, > 200 | `'off'` | Aviso de limite. |

## Regras

- O par apresentado é sempre um par em colisão no frame pausado (SC-004) e é o
  primeiro passo `test` com `overlap` do trace (R2).
- `findPairStepIndex(steps, a, b)` devolve o índice do passo `test` com o par `{a, b}`
  em qualquer ordem, ou `-1`.
