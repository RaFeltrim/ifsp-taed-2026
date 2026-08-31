---
tags: [árvores, b-tree, disco, banco-de-dados, fase-4]
tipo: conceito
status: atenção
pré-requisito: [[04 - Árvores/BST - Árvore Binária de Busca]]
próximo: [[04 - Árvores/Binary Heaps - Heap Binário]]
criado: 2026-07-27
---

# 🟡 B-Trees - Estrutura para Disco

> BST generalizada projetada para minimizar acessos a disco. Usada em **todo banco de dados**.

## Por que B-Trees Existem?

```
Problema com BST/AVL em banco de dados:
  - Dados em disco
  - Cada acesso a um nó = 1 I/O de disco
  - BST com N=1.000.000 registros → altura ≈ 20 → 20 acessos a disco

Solução B-Tree:
  - Cada nó armazena MÚLTIPLAS chaves
  - Árvore muito mais "larga" que "alta"
  - N=1.000.000 registros → altura ≈ 3-4 → 3-4 acessos a disco ✅
```

---

## Propriedades (B-Tree de ordem t)

```
Cada nó (exceto raiz) tem:
  - Mínimo: t-1 chaves  (e t filhos)
  - Máximo: 2t-1 chaves (e 2t filhos)

A raiz tem:
  - Mínimo: 1 chave
  - Máximo: 2t-1 chaves

Todas as folhas estão no MESMO nível.
```

---

## Estrutura Visual (t=2, B-Tree 2-3-4)

```
         [10 | 20 | 30]              ← nó raiz com 3 chaves
        /    |    |    \
    [5|8]  [13] [25] [35|40|45]     ← nós internos e folhas
```

Cada nó folha carrega um "bloco de disco" com múltiplos registros.

---

## Operações e Complexidade

| Operação | Complexidade |
|---|---|
| **Busca** | **O(log N)** - mas com fator constante menor que BST |
| **Inserção** | **O(log N)** |
| **Remoção** | **O(log N)** |
| **Altura máxima** | **O(log_t N)** ← muito menor que O(log₂ N) |

> Com t=1000: log₁₀₀₀(1.000.000) = 2! Apenas 2 acessos a disco.

---

## B-Tree vs B+Tree

| | B-Tree | B+Tree |
|---|---|---|
| **Dados em** | Todos os nós | Apenas nas folhas |
| **Folhas** | Não encadeadas | Encadeadas (lista) |
| **Busca por intervalo** | Lenta | Rápida (percorre folhas) |
| **Uso** | Geral | Índices de BD (MySQL, PostgreSQL) |

> Bancos de dados usam **B+Tree** para índices. B-Tree é a teoria base.

---

## Inserção com Split

```
B-Tree de ordem t=2 (máx 3 chaves por nó):

Inserindo: 1, 2, 3, 4

Estado: [1 | 2 | 3]  ← nó cheio!

Insert 4 → SPLIT!
  Chave do meio (2) sobe para o pai (ou vira nova raiz)
  
        [2]
       /   \
     [1]   [3 | 4]

Árvore cresceu para cima, não para baixo!
```

---

## Por que B-Trees em Bancos de Dados?

```
MySQL InnoDB, PostgreSQL, SQLite:
  - Índice = B+Tree
  - Cada página de disco = um nó da árvore (tipicamente 4KB ou 16KB)
  - Com t grande, a árvore é quase plana
  
Regra prática:
  100 milhões de registros → altura da B+Tree ≈ 3-4
  → No máximo 4 acessos ao disco para qualquer busca!
```

---

## Conexões no Vault

- [[04 - Árvores/BST - Árvore Binária de Busca]] - base conceitual
- [[04 - Árvores/AVL Trees - Balanceamento Automático]] - alternativa para memória RAM
- [[04 - Árvores/Binary Heaps - Heap Binário]] - próxima estrutura
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - O(log_t N) vs O(log₂ N)
