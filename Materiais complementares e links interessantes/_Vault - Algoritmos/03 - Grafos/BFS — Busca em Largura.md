---
tags: [grafos, BFS, fila, fase-3, crítico]
tipo: algoritmo
status: lacuna-crítica
pré-requisito: [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]], [[01 - Estruturas Lineares/Filas (Queue - FIFO)]]
próximo: [[03 - Grafos/DFS - Busca em Profundidade]]
criado: 2026-07-27
---

# 🔴 BFS - Busca em Largura (Breadth-First Search)

> **BFS = Fila disfarçada.** Se você entendeu Fila, você entende BFS.

## Ideia Central

```
Explore todos os vizinhos do nó atual ANTES de ir para os vizinhos dos vizinhos.
→ Nível por nível.
→ Usa uma FILA (FIFO).
```

## Pseudocódigo

```
BFS(grafo, início):
    fila = Fila()
    visitados = conjunto vazio

    fila.enqueue(início)
    visitados.add(início)

    enquanto fila não está vazia:
        atual = fila.dequeue()
        processar(atual)  ← faz algo com o nó

        para cada vizinho de atual:
            se vizinho não está em visitados:
                visitados.add(vizinho)
                fila.enqueue(vizinho)
```

---

## Dry-Run Completo

```
Grafo:
    1 ── 2 ── 5
    │    │
    3 ── 4

Lista de adjacência:
1: [2, 3]
2: [1, 4, 5]
3: [1, 4]
4: [2, 3]
5: [2]

BFS a partir do nó 1:

Passo 0: fila=[1], visitados={1}
Passo 1: dequeue(1) → processa 1
         vizinhos: 2, 3 → enqueue ambos
         fila=[2, 3], visitados={1,2,3}

Passo 2: dequeue(2) → processa 2
         vizinhos: 1(visitado), 4, 5 → enqueue 4, 5
         fila=[3, 4, 5], visitados={1,2,3,4,5}

Passo 3: dequeue(3) → processa 3
         vizinhos: 1(visitado), 4(visitado)
         fila=[4, 5]

Passo 4: dequeue(4) → processa 4
         vizinhos: todos visitados
         fila=[5]

Passo 5: dequeue(5) → processa 5
         vizinhos: todos visitados
         fila=[]  → FIM

Ordem de visita: 1 → 2 → 3 → 4 → 5
Nível 0: {1}
Nível 1: {2, 3}
Nível 2: {4, 5}
```

---

## Complexidade

| | Lista de Adjacência | Matriz de Adjacência |
|---|---|---|
| **Tempo** | **O(V + E)** | O(V²) |
| **Espaço** | **O(V)** - fila e visitados | O(V) |

> Com lista: visitamos cada vértice uma vez (V) e cada aresta duas vezes (E).

---

## Aplicações de BFS

| Problema | Por quê BFS? |
|---|---|
| **Menor caminho não-ponderado** | Explora por nível → primeiro caminho encontrado é o mais curto |
| **Detectar conectividade** | Verifica se todos os nós são alcançáveis |
| **Nível de separação** (6 graus) | Distância em número de arestas |
| **Crawlers web** | Explora links nível por nível |
| **GPS - menor número de ruas** | Ignora pesos, conta arestas |

---

## BFS vs. DFS - Quando Usar

| | BFS | DFS |
|---|---|---|
| **Estrutura** | Fila (FIFO) | Pilha (LIFO) / Recursão |
| **Menor caminho** | ✅ Sim (não-ponderado) | ❌ Não garante |
| **Detecção de ciclo** | ✅ | ✅ |
| **Topologia de grafo** | Por níveis | Por profundidade |
| **Uso de memória** | Pode ser alto (fila larga) | Menor (caminho atual) |

---

## Conexões no Vault

- [[01 - Estruturas Lineares/Filas (Queue - FIFO)]] - estrutura base do BFS
- [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]] - como acessar vizinhos
- [[03 - Grafos/DFS - Busca em Profundidade]] - alternativa ao BFS
- [[03 - Grafos/Algoritmo de Dijkstra]] - BFS ponderado com Heap
