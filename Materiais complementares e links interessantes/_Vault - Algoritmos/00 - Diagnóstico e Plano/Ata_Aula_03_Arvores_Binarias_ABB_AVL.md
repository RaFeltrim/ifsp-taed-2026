---
tags: [ata-de-aula, aula-3, abb, bst, avl, arvores-balanceadas, rotacoes, c, ponteiros]
tipo: ata-de-aula
data: 2026-08-17
aula_numero: 3
professor: Prof. Dr. Rodrigo Elias Bianchi
disciplina: Tópicos em Algoritmos e Estruturas de Dados (IFSP - São Carlos)
---

# 📌 Ata da Aula 03: Árvores Binárias de Busca (ABB) e Árvores AVL

> **Data:** 17 / Agosto / 2026  
> **Professor:** Prof. Dr. Rodrigo Elias Bianchi  
> **Material Base:** 
> - Slides IFSP São Carlos (*Estruturas de Dados — Árvores AVL*)
> - Material Complementar UFAM (*Árvores AVL — Adelson-Velskii and Landis*)
> - Unidade 15 MC-202 Unicamp (*Árvores Binárias de Busca*)

---

## 🎯 1. Resumo Executivo da Aula

A aula aprofundou a transição crítica de **Estruturas Lineares ($O(N)$)** para **Estruturas Hierárquicas Balanceadas ($O(\log N)$)**:
1. **Árvores Binárias de Busca (ABB/BST):** Propriedade fundamental de ordenação, percursos, busca recursiva/iterativa, cálculo de mínimo/máximo, sucessor/antecessor e os 3 casos de remoção.
2. **O Problema da Degeneração:** Como a inserção ordenada degrada a ABB em uma lista linear ($O(N)$).
3. **Árvores AVL (Adelson-Velskii & Landis):** Fator de Balanceamento ($FB \in \{-1, 0, +1\}$), detecção de pivôs e restauração do equilíbrio via **Rotações Simples** (LL, RR) e **Rotações Duplas** (LR, RL) implementadas em C com ponteiro duplo.

---

## 🌳 2. Árvores Binárias de Busca (ABB / BST)

### A. Propriedade Fundamental
Para qualquer nó $r$:
$$\forall e \in T_e \implies e \le r \quad \text{e} \quad \forall d \in T_d \implies d \ge r$$

### B. O TAD em C (com e sem ponteiro para pai)
```c
typedef struct No {
    int chave;
    struct No *esq, *dir;
    struct No *pai; // Opcional, facilita sucessor/antecessor
} No;
```

### C. Mínimo, Máximo, Sucessor e Antecessor
* **Mínimo:** Desce para a esquerda até `esq == NULL`.
* **Máximo:** Desce para a direita até `dir == NULL`.
* **Sucessor de $X$ (Próximo na ordenação crescente):**
  - **Caso 1 (Tem filho direito):** É o `minimo(X->dir)`.
  - **Caso 2 (Não tem filho direito):** Sobe na árvore até encontrar o primeiro ancestral para o qual $X$ está na subárvore esquerda (`ancestral_a_direita`).

---

## ⚖️ 3. Árvores AVL (Árvores Auto-Balanceadas)

### A. Fator de Balanceamento ($FB$)
$$FB(n) = \text{altura}(sad) - \text{altura}(sae) \quad \text{ou} \quad FB(n) = \text{altura}(sae) - \text{altura}(sad)$$
* **Invariante AVL:** $|FB(n)| \le 1$ para todo nó da árvore.
* Se $|FB(n)| = 2$, o nó está desbalanceado e exige rotação imediata.

### B. Eficiência Comparativa
* Em uma ABB degenerada com $10.000$ nós $\rightarrow$ Média de **$5.000$ comparações** por busca ($O(N)$).
* Em uma AVL com os mesmos $10.000$ nós $\rightarrow$ Média de **apenas $14$ comparações** ($\approx 1.44 \log_2 N$).

---

## 🔄 4. Catálogo Completo de Rotações em C (com `No**`)

### 1. Rotação Simples à Esquerda (Caso RR)
Aplicada quando o filho direito está mais pesado ($FB(A) = +2$ e $FB(B) = +1$).
```c
void rotacao_simples_esquerda(No **A) {
    No *B = (*A)->dir;
    (*A)->dir = B->esq;
    B->esq = *A;
    *A = B; // Atualiza a raiz da subárvore
}
```

### 2. Rotação Simples à Direita (Caso LL)
Aplicada quando o filho esquerdo está mais pesado ($FB(A) = -2$ e $FB(B) = -1$).
```c
void rotacao_simples_direita(No **A) {
    No *B = (*A)->esq;
    (*A)->esq = B->dir;
    B->dir = *A;
    *A = B; // Atualiza a raiz da subárvore
}
```

### 3. Rotação Dupla à Direita (Caso LR)
Aplicada quando $FB(A) = -2$ e $FB(B) = +1$.
```c
void rotacao_dupla_direita(No **A) {
    rotacao_simples_esquerda(&((*A)->esq)); // 1ª fase em B
    rotacao_simples_direita(A);             // 2ª fase em A
}
```

### 4. Rotação Dupla à Esquerda (Caso RL)
Aplicada quando $FB(A) = +2$ e $FB(B) = -1$.
```c
void rotacao_dupla_esquerda(No **A) {
    rotacao_simples_direita(&((*A)->dir));  // 1ª fase em B
    rotacao_simples_esquerda(A);            // 2ª fase em A
}
```

---

## 💥 5. Diferença Fundamental: Inserção vs. Remoção em AVL
* **Inserção:** Requer **no máximo 1 rotação** (simples ou dupla) para restabelecer todo o balanceamento da árvore.
* **Remoção:** Pode causar desbalanceamento em cascata, exigindo **até $O(\log N)$ rotações** subindo até a raiz!

---

## 📝 6. Resolução dos Exercícios Propostos (Slide 129 / Unicamp)

1. **Impressão em Ordem Crescente:** Percurso em-ordem (*Inorder Traversal*): `esq -> raiz -> dir`.
2. **Número Máximo de Comparações na Busca:** Calculado recursivamente pela altura da árvore: `1 + max(altura(esq), altura(dir))`.
3. **Sucessor sem ponteiro `pai`:** Realiza busca a partir da raiz guardando o último nó visitado onde dobramos à esquerda.

---

## 🔗 Links Relacionados no Vault

- [[04 - Árvores/BST - Árvore Binária de Busca]]
- [[04 - Árvores/AVL Trees - Balanceamento Automático]]
- [[00 - Diagnóstico e Plano/Ata_Aula_02_Revisao_C_Memoria_Ponteiros_Listas]]
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]]
