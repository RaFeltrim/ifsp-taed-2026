---
tags: [árvores, AVL, balanceamento, rotação, fase-4]
tipo: conceito
status: atenção
pré-requisito: [[04 - Árvores/BST - Árvore Binária de Busca]]
próximo: [[04 - Árvores/B-Trees - Estrutura para Disco]]
criado: 2026-07-27
---

# 🟡 AVL Trees - Balanceamento Automático

> BST que se auto-balanceia. Garante O(log N) em TODAS as operações, sempre.

## O Problema que AVL Resolve

```
BST normal: O(log N) no caso médio, O(N) no pior caso (degenerada)
AVL Tree:   O(log N) GARANTIDO - sem degeneração possível
```

---

## Fator de Balanceamento (FB)

```
FB(nó) = altura(subárvore esquerda) - altura(subárvore direita)

Invariante AVL: |FB| ≤ 1 para TODO nó da árvore
  → FB pode ser -1, 0 ou +1
  → Se FB = ±2 → DESBALANCEADO → rotação necessária!
```

---

## Calculando Altura e FB

```
Árvore:
         8  (h=2, FB=0)
        / \
       3   10  (h=0, FB=0)
      / \
     1   6
    (h=0)(h=0)
  
Altura do nó 3 = 1 + max(h(1), h(6)) = 1 + max(0,0) = 1
FB do nó 3 = h(esq) - h(dir) = 0 - 0 = 0 ✅
FB do nó 8 = h(3) - h(10) = 1 - 0 = 1 ✅ (ainda balanceado)
```

---

## Os 4 Casos de Desbalanceamento e Rotações

### Caso LL (Left-Left) → Rotação Simples à Direita

```
Situação: FB = +2, filho esquerdo com FB = +1

    z (+2)          y (0)
   /                / \
  y (+1)    →      x   z
 /
x

Rotação à direita em z:
  y vira a nova raiz
  z vira filho direito de y
  filho direito de y vira filho esquerdo de z
```

### Caso RR (Right-Right) → Rotação Simples à Esquerda

```
Situação: FB = -2, filho direito com FB = -1

  z (-2)              y (0)
    \                 / \
     y (-1)    →     z   x
      \
       x

Rotação à esquerda em z (espelho do LL)
```

### Caso LR (Left-Right) → Rotação Dupla

```
Situação: FB = +2, filho esquerdo com FB = -1

    z (+2)
   /
  x (-1)
    \
     y

Passo 1: Rotação à esquerda em x → vira caso LL
Passo 2: Rotação à direita em z
```

### Caso RL (Right-Left) → Rotação Dupla

```
Situação: FB = -2, filho direito com FB = +1
(espelho do LR)

Passo 1: Rotação à direita no filho direito → vira caso RR
Passo 2: Rotação à esquerda em z
```

---

## Dry-Run - Inserindo e Balanceando

```
Inserindo: 30, 20, 10 numa AVL

Passo 1: Insert 30
    30 (FB=0) ✅

Passo 2: Insert 20
    30 (FB=+1)
   /
  20 ✅

Passo 3: Insert 10
    30 (FB=+2) ← DESBALANCEADO!
   /
  20 (FB=+1)
 /
10

→ Caso LL → Rotação simples à direita em 30:

  20 (FB=0)
 /  \
10   30  ✅ Balanceado!
```

---

## Complexidade

| Operação | Complexidade |
|---|---|
| **Busca** | **O(log N)** garantido |
| **Inserção** | **O(log N)** + O(1) rotações |
| **Remoção** | **O(log N)** + O(log N) rotações |
| **Rotação** | **O(1)** por rotação |

> A altura máxima de uma AVL com N nós ≈ 1.44 × log₂(N)

---

## AVL vs. Red-Black Tree

| | AVL | Red-Black |
|---|---|---|
| **Balanceamento** | Mais estrito | Mais relaxado |
| **Busca** | Ligeiramente mais rápida | Mais lenta |
| **Inserção/Remoção** | Mais rotações | Menos rotações |
| **Uso** | Muita busca, pouca modificação | Muita modificação |

---

## Conexões no Vault

- [[04 - Árvores/BST - Árvore Binária de Busca]] - base da AVL
- [[04 - Árvores/B-Trees - Estrutura para Disco]] - generalização diferente
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - por que O(log N) garantido
