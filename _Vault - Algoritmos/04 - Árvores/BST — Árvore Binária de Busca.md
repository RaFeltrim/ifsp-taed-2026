---
tags: [árvores, BST, busca-binária, fase-4]
tipo: conceito
status: atenção
pré-requisito: [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]]
próximo: [[04 - Árvores/AVL Trees - Balanceamento Automático]]
criado: 2026-07-27
---

# 🟡 BST - Árvore Binária de Busca

> Base de todas as árvores balanceadas. Entender a BST é pré-requisito para AVL e B-Tree.

## Propriedade Fundamental

```
Para todo nó N:
  - Todos os valores na subárvore ESQUERDA < N.valor
  - Todos os valores na subárvore DIREITA > N.valor
```

```
Exemplo de BST válida:
         8
        / \
       3   10
      / \    \
     1   6    14
        / \
       4   7
```

---

## Operações e Complexidade

| Operação | Caso Médio | Pior Caso |
|---|---|---|
| **Search** | O(log N) | **O(N)** |
| **Insert** | O(log N) | **O(N)** |
| **Delete** | O(log N) | **O(N)** |

> **Pior caso O(N):** Quando a árvore se degenera em lista encadeada!

---

## Degeneração da BST

```
Inserindo: 1, 2, 3, 4, 5 (em ordem crescente)

  1
   \
    2
     \
      3
       \
        4
         \
          5

Virou uma lista encadeada! Busca = O(N) → BST inútil.
```

> Por isso existem as **árvores balanceadas**: AVL, Red-Black, B-Tree.
> Ver: [[04 - Árvores/AVL Trees - Balanceamento Automático]]

---

## Operações Principais

### Busca
```
search(raiz, alvo):
    se raiz == NULL: retorna NULL (não encontrado)
    se alvo == raiz.valor: retorna raiz
    se alvo < raiz.valor: retorna search(raiz.esq, alvo)
    senão: retorna search(raiz.dir, alvo)
```

### Inserção
```
insert(raiz, valor):
    se raiz == NULL: cria novo nó com valor
    se valor < raiz.valor: raiz.esq = insert(raiz.esq, valor)
    senão: raiz.dir = insert(raiz.dir, valor)
    retorna raiz
```


### Remoção (Delete) - Os 3 Casos

```
Caso 1 - Nó folha (sem filhos):
  Simplesmente remove o nó.
  
        8                   8
       / \       del(1)    / \
      3   10    ------→   3   10
     /                     
    1  ← remove            

Caso 2 - Nó com 1 filho:
  Substitui o nó pelo seu único filho.
  
        8                   8
       / \       del(10)   / \
      3   10    ------→   3   14
           \
           14 ← sobe

Caso 3 - Nó com 2 filhos:
  Substitui pelo SUCESSOR INORDER (menor da subárvore direita)
  ou pelo PREDECESSOR INORDER (maior da subárvore esquerda).
  
        8                   9
       / \       del(8)    / \
      3   10    ------→   3   10
     / \                 / \
    1   6               1   6
       / \                 / \
      4   7               4   7
           \
            9 ← menor da subárvore direita (sucessor inorder)
```

```
delete(raiz, alvo):
    se raiz == NULL: retorna NULL
    se alvo < raiz.valor: raiz.esq = delete(raiz.esq, alvo)
    se alvo > raiz.valor: raiz.dir = delete(raiz.dir, alvo)
    senão:  // encontrou o nó!
        se raiz sem filhos: retorna NULL        // Caso 1
        se raiz sem filho esq: retorna raiz.dir // Caso 2
        se raiz sem filho dir: retorna raiz.esq // Caso 2
        // Caso 3: encontra o sucessor inorder
        sucessor = menor_valor(raiz.dir)
        raiz.valor = sucessor.valor
        raiz.dir = delete(raiz.dir, sucessor.valor)
    retorna raiz
```

### Percursos (Traversals)
```
Em-ordem (inorder) → valores em ordem crescente!
  inorder(nó): inorder(esq) → visita(nó) → inorder(dir)

Pré-ordem (preorder): visita(nó) → preorder(esq) → preorder(dir)
Pós-ordem (postorder): postorder(esq) → postorder(dir) → visita(nó)
```

---

## Dry-Run - Busca

```
BST:
         8
        / \
       3   10

Busca por 3:
  raiz=8, 3 < 8 → vai para esquerda
  raiz=3, 3 == 3 → ENCONTRADO! ✅

Busca por 5:
  raiz=8, 5 < 8 → esquerda
  raiz=3, 5 > 3 → direita
  raiz=NULL → NÃO ENCONTRADO ❌
```

---

## Por que BST Importa?

É a estrutura conceitual de:
- [[04 - Árvores/AVL Trees - Balanceamento Automático]] - BST + balanceamento garantido
- [[04 - Árvores/B-Trees - Estrutura para Disco]] - BST generalizada para múltiplas chaves
- Sets e Maps em linguagens de programação (TreeMap em Java)

---

## Conexões no Vault

- [[04 - Árvores/AVL Trees - Balanceamento Automático]] - resolve o problema de O(N)
- [[04 - Árvores/B-Trees - Estrutura para Disco]] - versão para múltiplas chaves
- [[04 - Árvores/Binary Heaps - Heap Binário]] - árvore binária com propriedade diferente
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - por que O(log N) é bom
