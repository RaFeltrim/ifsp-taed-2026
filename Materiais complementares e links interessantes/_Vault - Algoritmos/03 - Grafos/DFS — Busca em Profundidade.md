---
tags: [grafos, DFS, pilha, recursão, fase-3, crítico]
tipo: algoritmo
status: lacuna-crítica
pré-requisito: [[03 - Grafos/BFS - Busca em Largura]], [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]]
próximo: [[03 - Grafos/Algoritmo de Dijkstra]]
criado: 2026-07-27
---

# 🔴 DFS - Busca em Profundidade (Depth-First Search)

> **DFS = Pilha disfarçada.** Vai fundo antes de voltar.

## Ideia Central

```
Explore o máximo possível em uma direção ANTES de voltar (backtrack).
→ Desce fundo num caminho até o fim, depois retrocede.
→ Usa uma PILHA (LIFO) - implícita via recursão ou explícita.
```

## Pseudocódigo - Versão Recursiva

```
DFS(grafo, atual, visitados):
    visitados.add(atual)
    processar(atual)

    para cada vizinho de atual:
        se vizinho não está em visitados:
            DFS(grafo, vizinho, visitados)

# Chamada inicial:
visitados = conjunto vazio
DFS(grafo, início, visitados)
```

## Pseudocódigo - Versão Iterativa (com Pilha Explícita)

```
DFS_iterativo(grafo, início):
    pilha = Pilha()
    visitados = conjunto vazio

    pilha.push(início)

    enquanto pilha não está vazia:
        atual = pilha.pop()

        se atual não está em visitados:
            visitados.add(atual)
            processar(atual)

            para cada vizinho de atual:
                se vizinho não visitado:
                    pilha.push(vizinho)
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

DFS a partir do nó 1 (recursivo):

DFS(1): visitados={1}, processa 1
  vizinho 2 → não visitado
  DFS(2): visitados={1,2}, processa 2
    vizinho 1 → visitado
    vizinho 4 → não visitado
    DFS(4): visitados={1,2,4}, processa 4
      vizinho 2 → visitado
      vizinho 3 → não visitado
      DFS(3): visitados={1,2,4,3}, processa 3
        vizinho 1 → visitado
        vizinho 4 → visitado
        retorna ←
      retorna ←
    vizinho 5 → não visitado
    DFS(5): visitados={1,2,4,3,5}, processa 5
      vizinho 2 → visitado
      retorna ←
    retorna ←
  vizinho 3 → visitado
  retorna ←

Ordem de visita: 1 → 2 → 4 → 3 → 5
(vai fundo antes de voltar!)
```

---

## Comparação com BFS

```
Mesmo grafo, resultado diferente:

BFS ordem: 1 → 2 → 3 → 4 → 5  (nível por nível)
DFS ordem: 1 → 2 → 4 → 3 → 5  (profundidade primeiro)
```

---

## Complexidade

| | Lista de Adjacência | Matriz de Adjacência |
|---|---|---|
| **Tempo** | **O(V + E)** | O(V²) |
| **Espaço** | **O(V)** - pilha de recursão | O(V) |

> Mesma complexidade que BFS, mas comportamento diferente.

---

## Aplicações de DFS

| Problema | Como DFS resolve |
|---|---|
| **Detecção de ciclos** | Ciclo encontrado se revisitar nó no mesmo caminho |
| **Ordenação Topológica** | Pós-ordem do DFS em DAG |
| **Componentes conexas** | Cada DFS completa = uma componente |
| **Labirintos** | DFS com backtracking encontra saída |
| **Parsing de expressões** | Percurso em árvore de expressão |

---

## DFS e Ordenação Topológica

```
DAG: A → B → D
     A → C → D

DFS pós-ordem (empilha ao terminar):
DFS(A) → DFS(B) → DFS(D) → empilha D
       → volta  → empilha B
       → DFS(C) → DFS(D) → já visitado
       → empilha C
       → empilha A

Pilha ao final: [A, C, B, D]  ← lida de cima para baixo → ordem topológica!
```

Ver detalhes em: [[03 - Grafos/DAGs - Grafos Acíclicos Dirigidos]]

---

## Conexões no Vault

- [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]] - DFS **é** uma pilha
- [[03 - Grafos/BFS - Busca em Largura]] - alternativa; comparação direta
- [[03 - Grafos/DAGs - Grafos Acíclicos Dirigidos]] - DFS gera ordenação topológica
- [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]] - impacta complexidade do DFS
