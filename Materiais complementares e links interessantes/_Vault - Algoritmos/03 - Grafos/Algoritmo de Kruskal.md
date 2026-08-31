---
tags: [grafos, kruskal, union-find, MST, fase-3, crítico]
tipo: algoritmo
status: lacuna-crítica
pré-requisito: [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]]
próximo: [[03 - Grafos/DAGs - Grafos Acíclicos Dirigidos]]
criado: 2026-07-27
---

# 🔴 Algoritmo de Kruskal

> Encontra a **Árvore Geradora Mínima (MST)** - conecta todos os vértices com o menor peso total possível.

## Problema que Resolve

```
Dado um grafo ponderado e conexo, qual o subconjunto de arestas que:
1. Conecta todos os vértices?
2. Tem o menor peso total?
→ Árvore Geradora Mínima (Minimum Spanning Tree)
```

**Aplicações:** Redes de fibra óptica, cabos elétricos, tubulações - minimizar custo de conexão.

---

## Ideia Central

```
1. Ordene TODAS as arestas por peso (crescente)
2. Para cada aresta (em ordem):
   - Se conecta dois componentes DIFERENTES → adiciona à MST
   - Se cria um ciclo (mesma componente) → descarta
3. Repita até ter V-1 arestas na MST
```

A estrutura que detecta ciclos eficientemente: **Union-Find (DSU)**

---

## Union-Find (Estrutura Auxiliar)

```
Mantém conjuntos disjuntos de vértices:

find(v): retorna o "representante" do conjunto de v
union(u, v): une os conjuntos de u e v

Dois vértices estão no mesmo componente se find(u) == find(v)
```

---

## Pseudocódigo

```
Kruskal(grafo):
    arestas = ordenar todas as arestas por peso (crescente)
    uf = UnionFind(V)  ← inicializa cada vértice como componente própria
    mst = []

    para cada (peso, u, v) em arestas:
        se uf.find(u) ≠ uf.find(v):   ← componentes diferentes → sem ciclo
            mst.append((u, v, peso))
            uf.union(u, v)

        se len(mst) == V - 1:
            break  ← MST completa!

    retorna mst
```

---

## Dry-Run Completo

```
Grafo:
  A ──4── B
  │  ╲    │
  2   3   5
  │    ╲  │
  C ──1── D

Arestas ordenadas por peso:
  (1, C, D), (2, A, C), (3, A, D), (4, A, B), (5, B, D)

Passo 1: (1, C-D) → find(C)≠find(D) → adiciona! mst=[(C,D,1)]
  Componentes: {A} {B} {C,D}

Passo 2: (2, A-C) → find(A)≠find(C) → adiciona! mst=[(C,D,1),(A,C,2)]
  Componentes: {A,C,D} {B}

Passo 3: (3, A-D) → find(A)==find(D) → CICLO! descarta

Passo 4: (4, A-B) → find(A)≠find(B) → adiciona! mst=[(C,D,1),(A,C,2),(A,B,4)]
  Componentes: {A,B,C,D}

|mst| = 3 = V-1 = 4-1 → FIM!

MST: C─D(1), A─C(2), A─B(4)
Peso total: 1 + 2 + 4 = 7
```

---

## Complexidade

| Passo | Complexidade |
|---|---|
| Ordenar arestas | **O(E log E)** |
| Operações Union-Find (com otimizações) | **O(E α(V)) ≈ O(E)** |
| **Total** | **O(E log E)** |

> α(V) é a inversa da função de Ackermann - praticamente constante para qualquer V real.

---

## Kruskal vs. Prim (outro algoritmo de MST)

| | Kruskal | Prim |
|---|---|---|
| **Abordagem** | Arestas globais | Expande a partir de um vértice |
| **Estrutura** | Union-Find | Heap Mínimo |
| **Melhor para** | Grafos **esparsos** | Grafos **densos** |
| **Complexidade** | O(E log E) | O((V+E) log V) |

---

## Conexões no Vault

- [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]] - grafo como entrada
- [[03 - Grafos/Algoritmo de Dijkstra]] - outro algoritmo clássico de grafos
- [[04 - Árvores/Binary Heaps - Heap Binário]] - usado no algoritmo de Prim
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - análise O(E log E)
