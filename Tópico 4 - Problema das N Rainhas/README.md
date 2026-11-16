# ♛ Tópico 4 — Problema das N-Rainhas (N-Queens & Backtracking)

Módulo correspondente à seção **Problema das N Rainhas** no Moodle, aplicando a técnica de **Backtracking** em linguagem **C puro** (sem `<stdbool.h>`) e manipulação avançada de ponteiros triplos (`char ***`) para compatibilidade direta com o desafio **LeetCode #51**.

---

## 📌 Fundamentos e Estratégia de Solução

* **Abstração 1D:** Em vez de alocar uma matriz $\mathcal{O}(N^2)$ para representar o tabuleiro, utiliza-se um vetor unidimensional `int posicoes[N]`, onde o índice representa a linha e `posicoes[linha]` armazena a coluna da rainha. Isso elimina por construção conflitos na mesma linha.
* **Verificação de Segurança (`eh_seguro`):** Para cada linha anterior `i < linha`:
  * **Coluna:** `posicoes[i] == col`
  * **Diagonal:** `abs(i - linha) == abs(posicoes[i] - col)`
* **Backtracking (`backtrack`):** Testa recursivamente cada coluna `0 .. n - 1`. Quando `linha == n`, aloca e formata o tabuleiro em strings (`'.'` e `'Q'`).
* **Complexidade:**
  * **Tempo:** $\mathcal{O}(N!)$ no pior caso (com poda imediata de ramos inválidos).
  * **Espaço:** $\mathcal{O}(N)$ para o vetor de posições e pilha de chamadas recursivas (além da memória das soluções retornadas).

---

## 📂 Organização dos Arquivos do Módulo

```text
📁 Tópico 4 - Problema das N Rainhas/
│
├── 📄 README.md                                             # Este documento de referência técnica
│
├── 📁 Entregas/                                             # [ARQUIVO PRONTO PARA SUBMISSÃO NO MOODLE]
│   └── 💻 n_rainhas.c                                       # Implementação completa em C puro (LeetCode #51)
│
├── 📁 Exercícios e Laboratórios/
│   └── 💻 n_rainhas.c                                       # Código-fonte com suíte de testes (N = 1, 2, 3, 4, 8)
│
└── 📁 Material de Apoio/
    └── 📑 Roteiro de Laboratório_ N-Queens (C Puro).pdf     # Roteiro oficial da atividade prática
```

---

## 🛠️ Como Compilar e Executar a Entrega em C

```bash
gcc -Wall -Wextra -O2 "Exercícios e Laboratórios/n_rainhas.c" -o n_rainhas
./n_rainhas
```
