---
tags: [grafos, dijkstra, heap, caminho-mínimo, fase-3, crítico]
tipo: algoritmo
status: lacuna-crítica
pré-requisito: [[03 - Grafos/BFS - Busca em Largura]], [[04 - Árvores/Binary Heaps - Heap Binário]]
próximo: [[03 - Grafos/Algoritmo de Kruskal]]
criado: 2026-07-27
---

# 🔴 Algoritmo de Dijkstra

> Encontra o **caminho mais curto** em grafos ponderados (pesos não-negativos).
> É um BFS evoluído - usa Heap em vez de Fila simples.

## Quando Usar

| Problema | Algoritmo |
|---|---|
| Menor caminho, **sem pesos** | BFS |
| Menor caminho, **com pesos não-negativos** | **Dijkstra** |
| Menor caminho, **com pesos negativos** | Bellman-Ford |
| Menor caminho, **entre todos os pares** | Floyd-Warshall |

---

## Ideia Central

```
Mantenha uma tabela de distâncias mínimas.
Sempre processe o vértice com MENOR distância conhecida (→ Heap Mínimo).
Atualize os vizinhos se encontrar caminho melhor (relaxamento).
```

## Pseudocódigo

```
Dijkstra(grafo, origem):
    distâncias = {v: ∞ para todo v}
    distâncias[origem] = 0
    heap_min = [(0, origem)]   ← (distância, vértice)

    enquanto heap_min não está vazio:
        (dist_atual, u) = heap_min.extrair_mínimo()

        se dist_atual > distâncias[u]:
            continue  ← entrada desatualizada, pula

        para cada (v, peso) em vizinhos de u:
            nova_dist = distâncias[u] + peso

            se nova_dist < distâncias[v]:
                distâncias[v] = nova_dist
                heap_min.inserir((nova_dist, v))

    retorna distâncias
```

---

## Dry-Run Completo

```
Grafo ponderado:
    A ──2── B ──1── D
    │               │
    4               3
    │               │
    C ──1── ────────┘

Arestas: A→B(2), A→C(4), B→D(1), C→D(3)
Origem: A

Passo 0: dist={A:0, B:∞, C:∞, D:∞}, heap=[(0,A)]

Passo 1: extrai (0,A)
  vizinho B: 0+2=2 < ∞ → dist[B]=2, heap insere (2,B)
  vizinho C: 0+4=4 < ∞ → dist[C]=4, heap insere (4,C)
  dist={A:0, B:2, C:4, D:∞}, heap=[(2,B),(4,C)]

Passo 2: extrai (2,B)
  vizinho A: 2+2=4 > 0 → não atualiza
  vizinho D: 2+1=3 < ∞ → dist[D]=3, heap insere (3,D)
  dist={A:0, B:2, C:4, D:3}, heap=[(3,D),(4,C)]

Passo 3: extrai (3,D)
  vizinho C: 3+3=6 > 4 → não atualiza
  dist não muda, heap=[(4,C)]

Passo 4: extrai (4,C)
  vizinho D: 4+3=7 > 3 → não atualiza
  heap=[]  → FIM

Distâncias mínimas a partir de A:
  A→A = 0
  A→B = 2
  A→C = 4
  A→D = 3  (via A→B→D, não A→C→D!)
```

---

## Complexidade

| Estrutura do Heap | Tempo | Espaço |
|---|---|---|
| **Heap Binário** | **O((V+E) log V)** | O(V) |
| Array simples | O(V²) | O(V) |
| Heap de Fibonacci | O(E + V log V) | O(V) |

> Para grafos esparsos, Heap Binário é a escolha padrão.

---

## Por que Dijkstra Não Funciona com Pesos Negativos?

```
A ──1── B
│       │
10    -15
│       │
└── C ──┘

Com Bellman-Ford: A→B→C = 1 + (-15) = -14 ← caminho correto
Com Dijkstra:     A→C = 10 ← "finaliza" C antes de descobrir o caminho melhor
                  BUG! ❌
```

---

## Conexões no Vault

- [[03 - Grafos/BFS - Busca em Largura]] - versão sem pesos (base conceitual)
- [[04 - Árvores/Binary Heaps - Heap Binário]] - estrutura central do Dijkstra
- [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]] - lista de adjacência com pesos
- [[03 - Grafos/Algoritmo de Kruskal]] - outro algoritmo clássico de grafos
