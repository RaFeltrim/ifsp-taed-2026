# Data Model: Modo Didático Passo a Passo

Entidades da feature 001 (`Particle`, `Rect`, `Quadtree`, `Simulation`) continuam
iguais; ver `specs/001-particle-collision-demo/data-model.md`. Abaixo só o que muda ou é
novo.

## Registro de visita — preenchido por `query(range, found, visited)`

| Campo | Tipo | Descrição |
|---|---|---|
| `node` | Quadtree | Nó visitado. |
| `hit` | booleano | `true` se o nó toca o range (a busca examina seus itens e desce). |
| `found` | lista de itens | Itens *deste* nó com o ponto dentro do range; vazio se `hit = false`. |

Regras: o primeiro registro é a raiz; nós com `hit = false` não têm descendentes
registrados; a concatenação de todos os `found` (na ordem) é igual ao retorno da `query`.

## Passo (Step) — objeto devolvido por `buildTrace`

Campos comuns a todos os tipos:

| Campo | Tipo | Descrição |
|---|---|---|
| `type` | `'particle'` \| `'visit'` \| `'test'` | Tipo do passo. |
| `p` | Particle | Partícula sendo analisada. |
| `tests` | inteiro | Testes de par feitos até este passo, inclusive. |
| `collisions` | inteiro | Colisões encontradas até este passo, inclusive. |

Por tipo:

| Tipo | Campos extras | Significado |
|---|---|---|
| `particle` | `range`: Rect (Quadtree) ou `null` (força bruta) | Começa a análise de `p`; `range` é o quadrado de lado `4r` centrado em `p`. |
| `visit` | `range`: Rect, `node`: Quadtree, `hit`: booleano | A busca visitou `node`; `hit = false` = descartado. Só no modo Quadtree. |
| `test` | `q`: Particle, `overlap`: booleano | Testou o par `(p, q)`, sempre com `q.id > p.id`; `overlap` = colidem. |

Ordem (FR-006a):
- Força bruta: `particle(p0)`, `test(p0, p1)`, `test(p0, p2)`, …, `particle(p1)`, …
- Quadtree: `particle(p)`, depois para cada nó na ordem da busca: `visit(nó)` seguido
  dos `test(p, q)` com os `q` do `found` desse nó que têm `q.id > p.id`.

Regras:
- A sequência começa sempre com `particle` (para `p.id = 0`).
- Número de passos `test` = `tests` da detecção normal do mesmo modo; pares com
  `overlap = true` = pares da detecção normal (FR-010).
- `tests` e `collisions` são não decrescentes ao longo da lista.

## Estado do modo didático (em `main.js`)

| Campo | Tipo | Descrição |
|---|---|---|
| `trace` | `null` ou `{ steps, index }` | `null` = desligado. `steps` = passos do frame; `index` = passo exibido (0..steps.length−1). |
| `MAX_TRACE_PARTICLES` | constante = 200 | Limite para ligar o modo (FR-001a). |

Transições:

| Evento | Efeito |
|---|---|
| Ligar com > 200 partículas | Continua desligado; aviso "reduza para até 200 partículas". |
| Ligar com ≤ 200 | `moveAndBuildTree()`; `trace = { steps: buildTrace(...), index: 0 }`; limpa aviso. |
| → | `index + 1`; se passar do fim: `detectAndResolve()`, `moveAndBuildTree()`, novo trace. |
| ← | `index − 1`, mínimo 0. |
| Shift + → | Próximo passo `particle`; se não houver: como → no fim. |
| Shift + ← | `index − 1` e volta até o passo `particle` anterior (mínimo 0). |
| Trocar modo | Novo trace com o mesmo frame, `index = 0`. |
| `restart()` | `reset(...)`; se ≤ 200: limpa o aviso e, se o modo estiver ligado, `moveAndBuildTree()` e novo trace; se > 200 com o modo ligado: `trace = null` e aviso. |
| Desligar | `detectAndResolve()`; `trace = null`. |

## Mudança em `Simulation`

`step()` passa a ser `moveAndBuildTree()` seguido de `detectAndResolve()`; o resultado
de `step()` não muda.
