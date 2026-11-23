# Data Model: Demo de Colisão de Partículas com Quadtree

## Particle (`particle.js`)

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | inteiro | Índice único na simulação (0..n−1); usado para contar cada par uma vez. |
| `x`, `y` | número | Centro, em px. |
| `vx`, `vy` | número | Velocidade, em px por frame. |
| `r` | número | Raio, em px; igual para todas (2, 4, 8, 16 ou 32). |
| `colliding` | booleano | `true` se sobrepôs alguma partícula neste frame (desenha em vermelho). |
| `selected` | booleano | `true` se o centro está na região selecionada (destaque). |

Regras:
- Após `move`, a partícula fica dentro de `[r, largura−r] × [r, altura−r]`; ao tocar
  uma borda, a componente de velocidade correspondente passa a apontar para dentro.
- Duas partículas colidem quando `distância(centros) < a.r + b.r`.
- `colliding` e `selected` são recalculados do zero a cada frame.

## Rect (`quadtree.js`)

| Campo | Tipo | Descrição |
|---|---|---|
| `x`, `y` | número | Canto superior esquerdo. |
| `w`, `h` | número | Largura e altura (≥ 0). |

Regras:
- `contains(px, py)`: `x ≤ px < x+w` e `y ≤ py < y+h` (borda direita/inferior
  exclusiva, para um ponto cair em exatamente um quadrante).
- `intersects(outro)`: os retângulos se sobrepõem.
- Retângulo de seleção é normalizado (largura/altura positivas) independentemente da
  direção do arrasto.

## Quadtree (`quadtree.js`)

| Campo | Tipo | Descrição |
|---|---|---|
| `boundary` | Rect | Região coberta pelo nó. |
| `capacity` | inteiro | Máximo de itens antes de subdividir (padrão 4). |
| `depth` | inteiro | Profundidade do nó (raiz = 0). |
| `maxDepth` | inteiro | Profundidade máxima (padrão 8). |
| `items` | lista de Particle | Itens guardados neste nó (só em folhas). |
| `children` | `null` ou 4 Quadtree | NE, NW, SE, SW após subdividir. |

Transições:
- Folha com `items.length < capacity` → insere no próprio nó.
- Folha cheia e `depth < maxDepth` → subdivide em 4 filhos, move os itens para os
  filhos e insere o novo item no filho que contém o ponto.
- Folha cheia e `depth == maxDepth` → aceita o item mesmo acima da capacidade.
- Itens fora do `boundary` são ignorados (`insert` retorna `false`).

## Simulation (`simulation.js`)

| Campo | Tipo | Descrição |
|---|---|---|
| `width`, `height` | número | Tamanho da área (canvas). |
| `radius` | número | Raio atual das partículas. |
| `particles` | lista de Particle | Partículas ativas. |
| `mode` | `'brute'` \| `'quadtree'` | Modo de detecção. |
| `tree` | Quadtree | Árvore do último frame (usada pela grade e pela seleção). |
| `tests` | inteiro | Testes de colisão realizados no último frame. |
| `selection` | `null` ou Rect | Região selecionada pelo mouse. |
| `selectedCount` | inteiro | Partículas encontradas pela range query no último frame. |

Transições:
- `reset(count, radius, width, height)` → recria `count` partículas em posições e
  direções aleatórias dentro da área; `tests = 0`; `selection = null`. Disparado por quantidade, raio ou
  redimensionamento.
- `step()` → move → constrói árvore → detecta pares (conforme `mode`) → resolve →
  marca `colliding` → aplica seleção (marca `selected`, atualiza `selectedCount`).
  A seleção usa a árvore do frame, ou seja, as posições anteriores à resolução das
  colisões; a diferença (no máximo meio raio) é aceitável e imperceptível.
- Trocar `mode` não reinicia nada.

## Estatísticas exibidas (calculadas em `main.js`)

FPS (média suavizada), `particles.length`, `tests`, `mode`, `selectedCount` (quando há
seleção).
