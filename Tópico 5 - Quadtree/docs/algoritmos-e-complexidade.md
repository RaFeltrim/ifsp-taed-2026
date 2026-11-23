# Algoritmos e Complexidade

Comparativo entre a detecção por **Força Bruta** (`findPairsBruteForce`) e por **Quadtree** (`findPairsQuadtree`) implementadas em [`src/simulation.js`](../src/simulation.js) e [`src/quadtree.js`](../src/quadtree.js).

---

## Complexidade por frame

| Algoritmo | Pares testados / Custo | Complexidade de tempo | Espaço auxiliar |
| :--- | :---: | :---: | :---: |
| **Força bruta** | $\frac{N(N - 1)}{2}$ pares | $O(N^2)$ | $O(1)$ |
| **Quadtree** | Inserção + *range query* local | $O(N \log N)$ médio / $O(N^2)$ pior caso | $O(N)$ |

Nos testes unitários (`tests/simulation.test.js`), o critério **SC-002** verifica que, com **$N = 1.000$ partículas**, a Quadtree executa no máximo **$1/10$** dos testes de colisão realizados pela força bruta.

---

## Subdivisão espacial e poda (`src/quadtree.js`)

1. **Partição por `Rect`:** `contains(px, py)` considera inclusivas as bordas esquerda e superior (`>=`) e exclusivas as bordas direita e inferior (`<`), evitando ambiguidade quando um ponto cai exatamente na divisa entre quadrantes.
2. **Subdivisão sob demanda:** cada nó folha armazena até `capacity = 4` itens. Ao ultrapassar o limite (e enquanto `depth < maxDepth`, com `maxDepth = 8`), `subdivide()` cria quatro filhos (`NE`, `NW`, `SE`, `SW`) e redistribui os pontos.
3. **Consulta de vizinhança (`query`):** para cada partícula, busca-se apenas dentro do retângulo de alcance centrado na partícula. Quadrantes que não intersectam esse retângulo (`!this.boundary.intersects(range)`) são podados imediatamente sem percorrer seus filhos.
4. **Rastreamento didático (`visited`):** quando o parâmetro opcional `visited` é passado, `query()` registra cada nó avaliado e se houve entrada ou poda, permitindo a visualização no canvas sem alterar o conjunto de candidatos retornado.

---

## Geração de trace (`buildTrace`)

A função `buildTrace()` em `src/simulation.js` reproduz a mesma detecção de pares de `findPairsBruteForce()` e `findPairsQuadtree()`, registrando cada passo em `steps` para que o modo didático consiga avançar, retroceder e alternar entre os dois algoritmos no mesmo frame pausado.

---

## Pior caso e degradação

A eficiência da Quadtree depende de as partículas estarem distribuídas pelo espaço para que a poda espacial descarte a maioria dos quadrantes. A estrutura perde vantagem — e pode ficar mais lenta que a força bruta pelo custo extra de construir e percorrer a árvore — em três situações:

1. **Aglomeração espacial (`cluster` e `clusters`):** quando muitas partículas ocupam uma fração pequena da área (`8%` de largura e altura), a árvore subdivide até `maxDepth = 8` e acumula dezenas ou centenas de pontos nas mesmas folhas. Na consulta, quase toda partícula testa quase todas as vizinhas do cluster, levando o número de comparações para próximo de $O(N^2)$. Em `clusters`, a poda ainda separa um aglomerado do outro, mas degrada dentro de cada grupo.
2. **Raio grande em área densa:** a janela de busca tem lado $4r$, então raios maiores (como `32 px`) intersectam mais quadrantes e reduzem a poda.
3. **$N$ muito pequeno:** com poucas partículas, o custo fixo de alocar nós e executar `query()` supera o loop duplo direto da força bruta.
