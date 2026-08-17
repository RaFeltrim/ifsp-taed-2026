---
tags: [grafos, representação, matriz-adjacência, lista-adjacência, fase-3, crítico]
tipo: conceito
status: lacuna-crítica
pré-requisito: [[99 - Complexidade Big-O/Guia de Complexidade Big-O]]
próximo: [[03 - Grafos/BFS - Busca em Largura]]
criado: 2026-07-27
---

# 🔴 Grafos - Representações (Matriz vs. Lista)

> **Representação ≠ Algoritmo.** Escolher errado aqui desperdiça memória ou torna operações lentas.

## O que é um Grafo?

```
G = (V, E)
V = conjunto de vértices (nós)
E = conjunto de arestas (conexões)
```

```
Exemplo: V = {A, B, C, D}
         E = {(A,B), (A,C), (B,D), (C,D)}

    A ─── B
    │     │
    C ─── D
```

---

## Representação 1 - Matriz de Adjacência

### Estrutura
```
Grafo: A─B, A─C, B─D, C─D
V = {A=0, B=1, C=2, D=3}

Matriz 4×4:
       A  B  C  D
  A  [ 0  1  1  0 ]
  B  [ 1  0  0  1 ]
  C  [ 1  0  0  1 ]
  D  [ 0  1  1  0 ]

matriz[i][j] = 1 se existe aresta entre i e j
```

### Complexidade

| Operação | Complexidade |
|---|---|
| Espaço total | **O(V²)** |
| Verificar se existe aresta (u,v) | **O(1)** |
| Listar todos os vizinhos de v | **O(V)** - percorre linha inteira |
| Adicionar aresta | **O(1)** |
| Remover aresta | **O(1)** |

### Quando Usar?
- Grafo **denso**: muitas arestas (E ≈ V²)
- Precisa verificar existência de arestas **rapidamente**
- V é pequeno (V² de memória é aceitável)

---

## Representação 2 - Lista de Adjacência

### Estrutura
```
Grafo: A─B, A─C, B─D, C─D

A → [B, C]
B → [A, D]
C → [A, D]
D → [B, C]
```

Implementado como: array de listas encadeadas, ou dicionário de listas.

### Complexidade

| Operação | Complexidade |
|---|---|
| Espaço total | **O(V + E)** |
| Verificar se existe aresta (u,v) | **O(grau(v))** |
| Listar todos os vizinhos de v | **O(grau(v))** |
| Adicionar aresta | **O(1)** |

### Quando Usar?
- Grafo **esparso**: poucas arestas (E << V²)
- Precisa percorrer vizinhos rapidamente
- V é grande (O(V²) de memória seria proibitivo)

---

## Comparação Direta

| | Matriz de Adjacência | Lista de Adjacência |
|---|---|---|
| **Espaço** | O(V²) | O(V + E) |
| **hasEdge(u,v)** | O(1) | O(grau(v)) |
| **neighbors(v)** | O(V) | O(grau(v)) |
| **Melhor para** | Grafos densos | Grafos esparsos |
| **Exemplo prático** | Rede de correlação completa | Mapa rodoviário |

---

## Exemplo de Trade-off Real

```
Rede social com V = 1.000.000 usuários (1 milhão):

Matriz de Adjacência:
  1.000.000² = 10^12 bits ≈ 125 GB de memória 💀

Lista de Adjacência (cada usuário tem ~300 amigos em média):
  1.000.000 × 300 = 300.000.000 entradas ≈ 2.4 GB ✅
```

> Redes sociais SEMPRE usam lista de adjacência.

---

## Tipos de Grafos

| Tipo | Descrição | Exemplo |
|---|---|---|
| **Não-dirigido** | Aresta (u,v) = (v,u) | Amizades |
| **Dirigido (Dígrafo)** | Aresta (u,v) ≠ (v,u) | Seguidores no Twitter |
| **Ponderado** | Arestas têm pesos | Distâncias em mapas |
| **DAG** | Dígrafo sem ciclos | Dependências de tarefas |
| **Árvore** | Grafo conexo sem ciclos | Hierarquia |

---

## Conexões no Vault

- [[03 - Grafos/BFS - Busca em Largura]] - percorre vizinhos (lista é mais eficiente)
- [[03 - Grafos/DFS - Busca em Profundidade]] - percorre vizinhos
- [[03 - Grafos/Algoritmo de Dijkstra]] - grafo ponderado
- [[03 - Grafos/Algoritmo de Kruskal]] - arestas ordenadas
- [[03 - Grafos/DAGs - Grafos Acíclicos Dirigidos]] - tipo especial de grafo
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - por que O(V²) vs O(V+E) importa
