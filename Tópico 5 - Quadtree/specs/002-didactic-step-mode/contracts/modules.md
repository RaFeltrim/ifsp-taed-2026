# Contracts: mudanças nas APIs e controles

Complementa `specs/001-particle-collision-demo/contracts/modules.md`. Campos dos passos
em [data-model.md](../data-model.md).

## `src/quadtree.js`

| Função | Contrato |
|---|---|
| `tree.query(range, found = [], visited = null)` | Igual à feature 001. Se `visited` for um array, cada nó visitado faz `visited.push({ node, hit, found })` na ordem da busca: `hit = false` significa que o nó não toca `range` e seus filhos não são visitados; `found` = itens deste nó dentro de `range`. O primeiro registro é a raiz; a concatenação dos `found` é igual ao retorno. Sem `visited`, nada muda. |

## `src/simulation.js` — exporta também `buildTrace`

| Função | Contrato |
|---|---|
| `sim.moveAndBuildTree()` | Move todas as partículas (com quique) e reconstrói `sim.tree`. |
| `sim.detectAndResolve()` | Detecta pares conforme `sim.mode`, atualiza `sim.tests`, resolve colisões, marca `colliding` e aplica a seleção. |
| `sim.step()` | `moveAndBuildTree()` + `detectAndResolve()`; mesmo resultado da feature 001. |
| `buildTrace(particles, tree, mode)` | Devolve a lista de passos do frame (ver data-model). Não altera partículas nem árvore. Em Quadtree, cada `visit` é seguido dos `test` com os itens daquele nó. Passos `test` e pares com `overlap` iguais (como conjunto) aos de `findPairsBruteForce` (`mode = 'brute'`) ou `findPairsQuadtree` (`mode = 'quadtree'`). |

## `src/renderer.js` (não testado)

`drawTrace(ctx, sim, steps, index, showGrid)`: fundo; grade completa se `showGrid`;
partículas apagadas, exceto as de colisões já encontradas até `index` (vermelhas); para a
partícula do passo atual: anel branco, região de busca tracejada (Quadtree), nós
visitados até `index` (verde = toca, vermelho = descartado, o atual mais grosso), linhas
dos testes já feitos (cinza) e do teste atual (verde sem colisão, vermelho com colisão),
com anel na outra partícula.

## Controles (`index.html` + `src/main.js`, não testado)

| Controle | Comportamento |
|---|---|
| Botão `#stepBtn` | Liga/desliga o modo didático; rótulo mostra o estado. Com mais de 200 partículas não liga e mostra o aviso. |
| Aviso `#notice` | Texto no painel: "Modo didático: reduza para até 200 partículas". Some ao recomeçar com até 200 partículas ou ao ligar o modo. |
| Arrastar no canvas com o modo ligado | Ignorado: não cria nem altera a seleção. |
| Mudar quantidade/raio/janela com o modo ligado | Recomeça; se passar de 200 partículas, desliga o modo e mostra o aviso. |
| → / ← | Próximo / anterior passo (só com o modo ligado; `preventDefault`). |
| Shift + → / ← | Próxima / anterior partícula. |
| → no último passo | Resolve, avança um frame e recomeça os passos. |
| Botão de modo | Com o modo didático ligado, refaz os passos do mesmo frame. |
| Painel (modo ligado) | Modo de detecção, "Passo k / N", descrição do passo, testes e colisões até ali, dica das teclas. |

Descrições do painel por tipo de passo:

- `particle`: "Partícula #i: comparar com todas as de id maior" (força bruta) /
  "Partícula #i: buscar vizinhas na região tracejada" (Quadtree)
- `visit`: "Nó nível d toca a região → examina e desce" / "Nó nível d fora da região → descartado"
- `test`: "Teste #i × #j: distância < mínima → COLISÃO" / "… ≥ mínima → sem colisão"
  (com os valores numéricos)
