# Contracts: API dos módulos e controles da UI

Assinaturas públicas que os testes e os outros módulos usam. Nomes de campos em
[data-model.md](../data-model.md). Arquivos de lógica exportam via `module.exports`
condicional (ver research R2); no navegador os nomes ficam globais.

## `src/particle.js` — exporta `{ Particle, particlesOverlap, resolveCollision }`

| Função | Contrato |
|---|---|
| `new Particle(id, x, y, vx, vy, r)` | Cria partícula com `colliding = selected = false`. |
| `particle.move(width, height)` | Soma a velocidade à posição; ao ultrapassar uma borda, reposiciona encostada nela e inverte a componente para dentro. |
| `particlesOverlap(a, b)` | `true` se `distância(a, b) < a.r + b.r`. |
| `resolveCollision(a, b)` | Separa as duas ao longo da normal até ficarem encostadas; se estão se aproximando, troca as componentes normais das velocidades (elástica, massas iguais). Centros iguais → normal (1, 0). |

## `src/quadtree.js` — exporta `{ Rect, Quadtree }`

| Função | Contrato |
|---|---|
| `new Rect(x, y, w, h)` | Retângulo alinhado aos eixos. |
| `rect.contains(px, py)` | Borda esquerda/superior inclusiva, direita/inferior exclusiva. |
| `rect.intersects(other)` | `true` se há sobreposição. |
| `new Quadtree(boundary, capacity = 4, depth = 0, maxDepth = 8)` | Nó raiz (ou filho). |
| `tree.insert(item)` | `item` tem `x`, `y`. Retorna `false` se fora do `boundary`, `true` caso contrário. Subdivide conforme data-model. |
| `tree.query(range, found = [])` | Retorna todos os itens com centro dentro de `range`; não desce em nós que não intersectam `range`. |
| `tree.boundary`, `tree.children` | Lidos pelo renderer para desenhar a grade. |

## `src/simulation.js` — exporta `{ Simulation, findPairsBruteForce, findPairsQuadtree }`

| Função | Contrato |
|---|---|
| `findPairsBruteForce(particles)` | Retorna `{ pairs, tests }`; testa cada par `i < j` uma vez; `tests = n(n−1)/2`. |
| `findPairsQuadtree(particles, tree)` | Retorna `{ pairs, tests }`; para cada `p`, consulta o quadrado de meia largura `2r` centrado em `p` e testa candidatas com `id > p.id`. O conjunto de pares é igual ao da força bruta. |
| `new Simulation(width, height)` | Simulação vazia, `mode = 'brute'`. |
| `sim.reset(count, radius, width, height)` | Ver data-model. |
| `sim.step()` | Avança um frame (ver data-model). |
| `sim.setSelection(rect \| null)` | Define ou limpa a região; aplicada no próximo `step`. |

## `src/renderer.js` — função global `draw` (só navegador, não testado)

`draw(ctx, sim, showGrid, dragRect)`: limpa o canvas; desenha a grade (se `showGrid`),
as partículas (vermelho se `colliding`, destaque se `selected`, cor normal caso
contrário) e o retângulo de seleção/arrasto.

## `src/main.js` (não testado) — controles da UI

| Controle | Comportamento |
|---|---|
| Slider de quantidade (10–2000, inicial 200) | Mostra o valor; ao mudar, `reset`. |
| Seletor de raio (2, 4, 8, 16, 32; inicial 4) | Ao mudar, `reset`. |
| Botão de modo | Alterna `'brute'` ↔ `'quadtree'`; rótulo mostra o modo atual. |
| Checkbox "Mostrar grade" | Liga/desliga a grade. |
| Arrastar no canvas | Desenha o retângulo e atualiza a seleção enquanto arrasta; ao soltar, a seleção fica. Clique sem arrastar → `setSelection(null)`. |
| Redimensionar janela | Ajusta canvas à janela e `reset`. |
| Painel | FPS, partículas, testes/frame, modo e encontrados na seleção. |
