---
tags: [árvores, AVL, balanceamento, rotação, fase-4, c, ponteiros]
tipo: conceito
status: atenção
pré-requisito: [[04 - Árvores/BST - Árvore Binária de Busca]]
próximo: [[04 - Árvores/B-Trees - Estrutura para Disco]]
criado: 2026-07-27
atualizado: 2026-08-17
---

# 🟡 AVL Trees - Balanceamento Automático

> **Árvore de Adelson-Velskii e Landis (AVL)**: BST auto-balanceada que garante complexidade assintótica $O(\log N)$ em TODAS as operações de busca, inserção e remoção.

---

## 🎯 O Problema que a AVL Resolve

Em uma Árvore Binária de Busca comum (ABB), a inserção de elementos em ordem crescente (ex: 5, 10, 15, ..., 95) gera uma **árvore degenerada** (uma lista encadeada inclinada).

```text
BUSCA EM ÁRVORE DEGENERADA (10.000 nós):  Média de 5.000 comparações -> O(N)
BUSCA EM ÁRVORE AVL BALANCEADA (10.000 nós): Média de apenas 14 comparações -> O(log N)
```

---

## ⚖️ Fator de Balanceamento (FB)

O balanceamento é medido pela diferença de altura entre as subárvores de cada nó:

$$FB(n) = \text{altura}(sad) - \text{altura}(sae)$$

* **$FB(n) = 0$:** As subárvores esquerda e direita possuem exatamente a mesma altura.
* **$FB(n) = -1$:** A subárvore esquerda é $1$ nível mais alta que a direita.
* **$FB(n) = +1$:** A subárvore direita é $1$ nível mais alta que a esquerda.
* **$|FB(n)| \ge 2$:** **DESBALANCEADO!** Exige aplicação imediata de rotação.

---

## 🔄 Catálogo Oficial de Rotações em C (com Ponteiro Duplo `No**`)

Nas aulas do Prof. Dr. Rodrigo Bianchi, as rotações operam sobre ponteiros duplos `No** A` para atualizar a raiz da subárvore diretamente na memória:

### 1. Rotação Simples à Esquerda (Caso RR)
Aplicada quando o desbalanceamento ocorre na subárvore direita do filho direito ($FB(A) = +2, FB(B) = +1$).

```c
void rotacao_simples_esquerda(No **A) {
    No *B = (*A)->dir;
    (*A)->dir = B->esq;
    B->esq = *A;
    *A = B; // O nó B se torna a nova raiz da subárvore
}
```

```text
    A (+2)                  B (0)
      \                    /   \
       B (+1)    ───►     A(0)  C(0)
        \
         C (0)
```

---

### 2. Rotação Simples à Direita (Caso LL)
Aplicada quando o desbalanceamento ocorre na subárvore esquerda do filho esquerdo ($FB(A) = -2, FB(B) = -1$).

```c
void rotacao_simples_direita(No **A) {
    No *B = (*A)->esq;
    (*A)->esq = B->dir;
    B->dir = *A;
    *A = B; // O nó B se torna a nova raiz da subárvore
}
```

```text
        A (-2)              B (0)
       /                   /   \
      B (-1)     ───►    C(0)  A(0)
     /
    C (0)
```

---

### 3. Rotação Dupla à Direita (Caso LR)
Aplicada quando $FB(A) = -2$ e $FB(B) = +1$ (formato em "joelho"/zigue-zague).
- **1ª Fase:** Rotação simples à esquerda no filho $B$ (`&((*A)->esq)`).
- **2ª Fase:** Rotação simples à direita no pai $A$ (`A`).

```c
void rotacao_dupla_direita(No **A) {
    rotacao_simples_esquerda(&((*A)->esq)); // Alinha em formato LL
    rotacao_simples_direita(A);             // Balanceia
}
```

---

### 4. Rotação Dupla à Esquerda (Caso RL)
Aplicada quando $FB(A) = +2$ e $FB(B) = -1$ (formato em "joelho"/zigue-zague).
- **1ª Fase:** Rotação simples à direita no filho $B$ (`&((*A)->dir)`).
- **2ª Fase:** Rotação simples à esquerda no pai $A$ (`A`).

```c
void rotacao_dupla_esquerda(No **A) {
    rotacao_simples_direita(&((*A)->dir));  // Alinha em formato RR
    rotacao_simples_esquerda(A);            // Balanceia
}
```

---

## 💥 Inserção vs. Remoção: O Custo Oculto

| Operação | No Máximo Quantas Rotações? | Complexidade de Tempo |
|---|---|---|
| **Inserção** | **No máximo 1 rotação** (simples ou dupla) | $O(\log N)$ |
| **Remoção** | **Até $O(\log N)$ rotações** em cascata até a raiz | $O(\log N)$ |

> **Atenção:** Na remoção de um nó, o rebalanceamento de uma subárvore pode diminuir sua altura e propagar um novo desbalanceamento para o ancestral acima, exigindo múltiplas rotações sucessivas até a raiz.

---

## 🧪 Exercício Clássico Resolvido: Inserção de `[3, 2, 1, 4, 5, 6, 7]`

1. Insere 3, 2: Árvore OK ($FB(3)=-1, FB(2)=0$).
2. Insere 1: $FB(3)=-2, FB(2)=-1 \implies$ **Rotação Simples à Direita em 3**. Raiz vira 2.
3. Insere 4, 5: $FB(3)=+2, FB(4)=+1 \implies$ **Rotação Simples à Esquerda em 3**.
4. Insere 6: $FB(2)=+2, FB(4)=+1 \implies$ **Rotação Simples à Esquerda na Raiz 2**. Raiz vira 4.
5. Insere 7: $FB(5)=+2, FB(6)=+1 \implies$ **Rotação Simples à Esquerda em 5**.
* **Resultado:** Árvore perfeitamente cheia e balanceada com raiz `4` e altura `3`!

---

## 🔗 Links Relacionados no Vault

- [[04 - Árvores/BST - Árvore Binária de Busca]] — base sem balanceamento
- [[04 - Árvores/B-Trees - Estrutura para Disco]] — versão multi-chave para banco de dados
- [[00 - Diagnóstico e Plano/Ata_Aula_03_Arvores_Binarias_ABB_AVL]] — ata oficial da aula
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] — análise logarítmica
