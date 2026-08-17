---
tags: [árvores, heap, priority-queue, fase-4]
tipo: conceito
status: atenção
pré-requisito: [[04 - Árvores/BST - Árvore Binária de Busca]]
usado-em: [[03 - Grafos/Algoritmo de Dijkstra]], [[03 - Grafos/Algoritmo de Kruskal]]
criado: 2026-07-27
---

# 🟡 Binary Heaps - Heap Binário

> Árvore binária completa com propriedade de ordem. A base da Priority Queue.

## Dois Tipos

```
MaxHeap: pai ≥ filhos (raiz = maior elemento)
MinHeap: pai ≤ filhos (raiz = menor elemento)
```

```
MaxHeap válido:        MinHeap válido:
       90                     1
      /  \                   / \
    75    80                3   2
   / \   /                 7   5
  60 50 65
```

---

## Propriedades Obrigatórias

1. **Propriedade de Heap:** pai ≥ (ou ≤) filhos em TODOS os nós
2. **Propriedade de Completude:** todos os níveis preenchidos, exceto o último (preenchido da esquerda)

---

## Implementação com Array (não usa ponteiros!)

```
Para nó no índice i:
  Filho esquerdo: 2i + 1
  Filho direito:  2i + 2
  Pai:            (i - 1) // 2

MaxHeap [90, 75, 80, 60, 50, 65]:
índice:   0   1   2   3   4   5

         90 (i=0)
        /        \
     75 (i=1)   80 (i=2)
    /    \      /
60(i=3) 50(i=4) 65(i=5)
```

---

## Operações e Complexidade

| Operação | Complexidade | Descrição |
|---|---|---|
| `peek()` | **O(1)** | Retorna a raiz sem remover |
| `insert(x)` | **O(log N)** | Insere e faz sift-up |
| `extractMax/Min()` | **O(log N)** | Remove raiz e faz sift-down |
| `buildHeap(array)` | **O(N)** ← surpresa! | Constrói heap a partir de array |

> **O ponto mais confuso:** Por que `buildHeap` é O(N) e não O(N log N)?
> Porque não chamamos N vezes o `insert`. Fazemos sift-down da metade dos elementos, e os níveis baixos têm muito menos trabalho. A somatória colapsa para O(N).

---

## Dry-Run - Insert com Sift-Up (MaxHeap)

```
Heap atual: [90, 75, 80, 60, 50, 65]
Insert 95:

Passo 1: Adiciona ao final
  [90, 75, 80, 60, 50, 65, 95]
  95 está no índice 6, pai = (6-1)//2 = 2 → valor 80

Passo 2: 95 > 80 → TROCA (sift-up)
  [90, 75, 95, 60, 50, 65, 80]
  95 está no índice 2, pai = (2-1)//2 = 0 → valor 90

Passo 3: 95 > 90 → TROCA (sift-up)
  [95, 75, 90, 60, 50, 65, 80]
  95 está no índice 0 → É A RAIZ → PARAR ✅

MaxHeap final:
         95
        /  \
       75   90
      / \  /  \
    60  50 65  80
```

---

## Dry-Run - ExtractMax com Sift-Down

```
Heap: [95, 75, 90, 60, 50, 65, 80]

Passo 1: Salva raiz (95), move último elemento para raiz
  [80, 75, 90, 60, 50, 65]

Passo 2: Sift-down do 80
  Filhos: 75 (esq) e 90 (dir) → maior filho = 90
  80 < 90 → TROCA com 90
  [90, 75, 80, 60, 50, 65]

Passo 3: 80 está no índice 2
  Filhos: 65 (índice 5) → 80 > 65 → para ✅

Retorna: 95
Heap resultante: [90, 75, 80, 60, 50, 65]
```

---

## Heap vs. BST

| | Heap Binário | BST (balanceada) |
|---|---|---|
| **Busca por qualquer valor** | O(N) | O(log N) |
| **Encontrar o máx/mín** | O(1) | O(log N) |
| **Inserção** | O(log N) | O(log N) |
| **Remoção do máx/mín** | O(log N) | O(log N) |
| **Uso** | Priority Queue | Dicionário ordenado |

> Heap é ideal quando você só precisa do **menor ou maior elemento rapidamente**.

---

## Heap Sort - Bônus

```
1. BuildHeap(array) → O(N)
2. Para i de N-1 até 0:
   - Extrai o máximo (raiz) → coloca no índice i
   - Faz sift-down → O(log N)
3. Total: O(N log N) - in-place, sem memória extra!
```

---

## Conexões no Vault

- [[03 - Grafos/Algoritmo de Dijkstra]] - usa MinHeap como Priority Queue
- [[03 - Grafos/Algoritmo de Kruskal]] - usa MinHeap para ordenar arestas
- [[04 - Árvores/BST - Árvore Binária de Busca]] - comparação estrutural
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - por que buildHeap é O(N)
