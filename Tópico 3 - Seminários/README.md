# 🏛️ Tópico 3 — Seminários & Desafios Avançados de Algoritmos (LeetCode)

Módulo centralizador dos seminários apresentados pelos grupos de estudantes e implementações em linguagem C dos problemas clássicos cobrados em entrevistas técnicas das Big Techs (Google, Meta, Amazon, Microsoft, Apple, Bloomberg).

---

## 📌 Catálogo Geral dos Desafios Implementados em C

| # | Problema / Seminário | Desafio LeetCode | Paradigma / Estrutura Central | Complexidade Ótima | Arquivo C |
| :-: | :--- | :--- | :--- | :---: | :--- |
| **1** | **Flatten Binary Tree** | LeetCode #114 | Árvore Binária / Manipulação de Ponteiros | $\mathcal{O}(N)$ tempo · $\mathcal{O}(1)$ espaço | `flatten_binary_tree.c` |
| **2** | **Alien Dictionary** | LeetCode #269 | Grafos Direcionados / Kahn's Topological Sort | $\mathcal{O}(C)$ tempo · $\mathcal{O}(V + E)$ espaço | `alien_dictionary.c` |
| **3** | **Parênteses Balanceados** | LeetCode #20 | Pilha Dinâmica (Stack LIFO) | $\mathcal{O}(N)$ tempo · $\mathcal{O}(N)$ espaço | `parenteses_balanceados.c` |
| **4** | **Lucro com Venda de Vinhos** | DP Clássico | Programação Dinâmica Memoization vs. Guloso | $\mathcal{O}(N^2)$ tempo · $\mathcal{O}(N^2)$ espaço | `lucro_venda_vinhos.c` |
| **5** | **Recipiente com Mais Água** | LeetCode #11 | Dois Ponteiros (Two Pointers) | $\mathcal{O}(N)$ tempo · $\mathcal{O}(1)$ espaço | `recipiente_mais_agua.c` |
| **6** | **Inverter Árvore Binária** | LeetCode #226 | Recursão DFS & Iterativo BFS com Fila | $\mathcal{O}(N)$ tempo · $\mathcal{O}(H)$ espaço | `inverter_arvore_binaria.c` |
| **7** | **Merge K Sorted Lists** | LeetCode #23 | Divisão e Conquista / Min-Heap Priority Queue | $\mathcal{O}(N \log K)$ tempo · $\mathcal{O}(1)$ espaço extra | `merge_k_sorted_lists.c` |
| **8** | **Subarray de Soma Máxima** | LeetCode #53 | Algoritmo de Kadane (Programação Dinâmica) | $\mathcal{O}(N)$ tempo · $\mathcal{O}(1)$ espaço | `subarray_soma_maxima.c` |
| **Bonus** | **Árvore AVL Completa** | Estrutura Canônica | Árvore Auto-Balanceável com Rotações em C | $\mathcal{O}(\log N)$ busca/inserção | `ArvoreAVL/` |

---

## 📂 Organização dos Arquivos do Módulo

```text
📁 Tópico 3 - Seminários/
│
├── 📄 README.md                                             # Este documento de referência e catálogo técnico
│
├── 📁 Entregas/                                             # [CENTRAL DE ENVIOS DO MOODLE - ARQUIVOS PRONTOS]
│   ├── 💻 alien_dictionary.c                                # [ENTREGA] Ordem do alfabeto alienígena
│   ├── 💻 flatten_binary_tree.c                             # [ENTREGA] Achatamento de árvore binária
│   ├── 💻 inverter_arvore_binaria.c                         # [ENTREGA] Inversão de árvore binária
│   ├── 💻 lucro_venda_vinhos.c                              # [ENTREGA] Vinhos: Força Bruta, Guloso, DP & Benchmark 32
│   ├── 💻 merge_k_sorted_lists.c                            # [ENTREGA] Fusão de K listas ordenadas
│   ├── 💻 parenteses_balanceados.c                          # [ENTREGA] Verificador de parênteses com pilha
│   ├── 💻 recipiente_mais_agua.c                            # [ENTREGA] Container with most water
│   └── 💻 subarray_soma_maxima.c                            # [ENTREGA] Kadane - Subarray contíguo máximo
│
├── 📁 Exercícios e Laboratórios/                             # [CÓDIGOS-FONTE & SUÍTES DE TESTES]
│   ├── 💻 alien_dictionary.c
│   ├── 💻 flatten_binary_tree.c
│   ├── 💻 inverter_arvore_binaria.c
│   ├── 💻 lucro_venda_vinhos.c
│   ├── 💻 merge_k_sorted_lists.c
│   ├── 💻 parenteses_balanceados.c
│   ├── 💻 recipiente_mais_agua.c
│   ├── 💻 subarray_soma_maxima.c
│   └── 📁 ArvoreAVL/                                        # Implementação canônica de Árvore AVL
│       ├── 💻 ArvoreAVL.c
│       ├── 📄 ArvoreAVL.h
│       └── 💻 main.c
│
└── 📁 Material de Apoio/                                    # [SLIDES & APRESENTAÇÕES OFICIAIS DOS GRUPOS]
    ├── 📑 Alien Dictionary.pptx.pdf
    ├── 📑 Apresentação - Flatten Binary Tree.pdf
    ├── 📦 ArvoreAVL.zip
    ├── 📑 arvores-avl.pdf
    ├── 📑 ESD Árvores AVL 2025.pdf
    ├── 📑 Inverter Árvore Binária (LeetCode 226).pdf
    ├── 📑 LRU Cache.pdf
    ├── 📑 Lucro máximo com a venda de vinhos.pdf
    ├── 📑 merge_k_sorted_lists.pdf
    ├── 📑 Parênteses Balanceados.pdf
    ├── 📑 recipiente com mais água.pdf
    ├── 📑 reverse-linked-list-1.pptx.pdf
    ├── 📑 subarray-soma-maxima (2).pdf
    ├── 📑 unidade15-abbs.pdf
    └── 📑 unidade17-arvores-binarias.pdf
```

---

## 🛠️ Como Compilar e Executar Qualquer Solução em C

Todos os programas foram escritos em C ANSI/C99 padrão, sendo 100% autocontidos com funções `main()` que realizam testes unitários automatizados e benchmarks.

```bash
# Compilando qualquer uma das entregas:
gcc -Wall -Wextra -O2 "Exercícios e Laboratórios/lucro_venda_vinhos.c" -o vinhos
./vinhos

gcc -Wall -Wextra -O2 "Exercícios e Laboratórios/recipiente_mais_agua.c" -o recipiente
./recipiente

gcc -Wall -Wextra -O2 "Exercícios e Laboratórios/subarray_soma_maxima.c" -o kadane
./kadane

gcc -Wall -Wextra -O2 "Exercícios e Laboratórios/merge_k_sorted_lists.c" -o merge_k
./merge_k

gcc -Wall -Wextra -O2 "Exercícios e Laboratórios/inverter_arvore_binaria.c" -o inverter
./inverter

# Compilando o pacote modular da Árvore AVL:
gcc -Wall -Wextra -O2 "Exercícios e Laboratórios/ArvoreAVL/ArvoreAVL.c" "Exercícios e Laboratórios/ArvoreAVL/main.c" -o arvore_avl
./arvore_avl
```
