# SCLTAED — Tópicos em Algoritmos e Estruturas de Dados (2026)

[![IFSP - Campus São Carlos](https://img.shields.io/badge/IFSP-São%20Carlos-red.svg)](https://scl.ifsp.edu.br/)
[![Curso](https://img.shields.io/badge/Curso-Engenharia%20de%20Software-informational.svg)](https://scl.ifsp.edu.br/index.php/cursos/superiores/bacharelado-em-engenharia-de-software.html)
[![Disciplina](https://img.shields.io/badge/Disciplina-SCLTAED%20(400267)-blue.svg)](https://moodle.scl.ifsp.edu.br/course/view.php?id=5193)
[![Status](https://img.shields.io/badge/Status-Repositório%20de%20Consulta%20%7C%20Privado-success.svg)]()

Repositório central de estudos, anotações, trabalhos práticos, implementações em linguagem C, relatórios teóricos, suítes de benchmark e materiais de apoio da disciplina **SCLTAED — Tópicos em Algoritmos e Estruturas de Dados**, ministrada no Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (**IFSP — Campus São Carlos**).

---

## 📌 Informações Gerais

- **Instituição:** Instituto Federal de São Paulo (IFSP) — Campus São Carlos
- **Curso:** Bacharelado em Engenharia de Software (BES)
- **Código da Disciplina:** SCLTAED / 400267
- **Semestre:** 2026.2
- **Docente Responsável:** Prof. Dr. Rodrigo Elias Bianchi ([bianchi@ifsp.edu.br](mailto:bianchi@ifsp.edu.br))
- **Ambiente Virtual:** [Moodle IFSP São Carlos (Curso ID 5193)](https://moodle.scl.ifsp.edu.br/course/view.php?id=5193)
- **Finalidade:** Base de conhecimento técnico e acervo privado de consulta pessoal para avaliações, provas e entrevistas de engenharia de software (Big Techs).

---

## 🗂️ Estrutura Oficial do Repositório por Módulos & Semanas

```text
TAED - IFSP/
│
├── 📁 Tópico 0 - Informacoes Gerais e Revisao C/              # (Semanas Iniciais / Aulas 1 e 2)
│   ├── README.md                                             # Apresentação da disciplina, ementa e revisão de C (ponteiros/memória)
│   ├── 📁 Entregas/
│   │   └── Exercícios de Fixação - Rafael F.pdf              # [PROVA / FIXAÇÃO] Resolução de fixação e conversão de bases
│   └── 📁 Material de Apoio/
│       ├── Aula 1 - Tópicos em Algoritmos e Estruturas de Dados.pdf # Slides de introdução e ementa do Prof. Dr. Rodrigo Bianchi
│       └── Aula 2 - Revisão de Estrutura de Dados em C.pdf          # Guia prático de ponteiros, heap e listas encadeadas
│
├── 📁 Tópico 1 - Algoritmos LeetCode3/                        # (Seminário Principal / Sliding Window)
│   ├── README.md                                             # Estudo de Caso LeetCode #3, Sliding Window O(N) e Big-O
│   ├── 📁 Entregas/
│   │   ├── Apresentacao_LeetCode3_Equipe_IFSP.pdf            # [ENTREGA OFICIAL] Slides finais para projeção
│   │   ├── Apresentacao_LeetCode3_Editavel.docx              # Documento da apresentação editável
│   │   ├── Apresentacao_LeetCode3_Slides.html                # Slides interativos web em HTML5/CSS3
│   │   └── Longest-Substring-Without-Repeating-Characters.pdf # Slide do seminário consolidado
│   ├── 📁 Exercícios e Laboratórios/
│   │   ├── lswrc_solucao1_forca_bruta.c                      # Solução 1 em C: Força Bruta O(N^2)
│   │   ├── lswrc_solucao2_janela_deslizante.c                # Solução 2 em C: Janela Deslizante O(N) Padrão Ouro
│   │   ├── benchmark_solutions.py                            # Script experimental de benchmark de CPU
│   │   ├── generate_pdf_slides.py                            # Gerador headless de slides
│   │   └── generate_docx_presentation.py                     # Compilador do relatório Word
│   └── 📁 Material de Apoio/
│       ├── Longest-Substring-Without-Repeating-Characters.pdf
│       ├── Longest-Substring-Without-Repeating-Characters_1.pdf
│       ├── diagrama_janela_deslizante_editavel.svg            # Diagrama vetorial da técnica Sliding Window
│       └── Roteiro_Apresentacao_Equipe.md                    # Script de fala de cada membro da equipe
│
├── 📁 Tópico 2 - Grafos/                                      # (Aula 4)
│   ├── README.md                                             # Teoria dos Grafos, Matriz/Lista de Adjacência, BFS/DFS
│   ├── 📁 Entregas/
│   │   └── grafo_exercicio_aula4.c                           # [ENTREGA MOODLE] Implementação do grafo do slide da aula 4
│   ├── 📁 Exercícios e Laboratórios/
│   │   └── grafo_exercicio_aula4.c                           # Código C de construção e percursos do grafo
│   └── 📁 Material de Apoio/
│       └── TAED - Grafos.pdf                                 # Slides teóricos e exercícios de Grafos
│
├── 📁 Tópico 3 - Seminários/                                 # (Seminários dos Grupos & Árvores AVL)
│   ├── README.md                                             # Panorama e análise assintótica dos desafios dos seminários
│   ├── 📁 Entregas/                                          # [CENTRAL DE ENVIOS DO MOODLE - ARQUIVOS PRONTOS]
│   │   ├── alien_dictionary.c                                # [ENTREGA] Ordem de símbolos alienígenas (Grafo / TopoSort)
│   │   ├── flatten_binary_tree.c                             # [ENTREGA] Achatamento de árvore binária in-place (LeetCode 114)
│   │   ├── inverter_arvore_binaria.c                         # [ENTREGA] Inversão de árvore binária (LeetCode 226)
│   │   ├── lucro_venda_vinhos.c                              # [ENTREGA] Venda de vinhos: FB, Guloso, DP e Benchmark 32 vinhos
│   │   ├── merge_k_sorted_lists.c                            # [ENTREGA] Fusão de K listas ordenadas (LeetCode 23)
│   │   ├── parenteses_balanceados.c                          # [ENTREGA] Validação de parênteses com pilha (LeetCode 20)
│   │   ├── recipiente_mais_agua.c                            # [ENTREGA] Recipiente com mais água (LeetCode 11)
│   │   └── subarray_soma_maxima.c                            # [ENTREGA] Algoritmo de Kadane - Subarray máx (LeetCode 53)
│   ├── 📁 Exercícios e Laboratórios/
│   │   ├── alien_dictionary.c
│   │   ├── flatten_binary_tree.c
│   │   ├── inverter_arvore_binaria.c
│   │   ├── lucro_venda_vinhos.c
│   │   ├── merge_k_sorted_lists.c
│   │   ├── parenteses_balanceados.c
│   │   ├── recipiente_mais_agua.c
│   │   ├── subarray_soma_maxima.c
│   │   └── 📁 ArvoreAVL/                                     # Código completo da Árvore AVL em C (Moodle Aula 3)
│   │       ├── ArvoreAVL.c
│   │       ├── ArvoreAVL.h
│   │       └── main.c
│   └── 📁 Material de Apoio/
│       ├── Alien Dictionary.pptx.pdf
│       ├── Apresentação - Flatten Binary Tree.pdf
│       ├── ArvoreAVL.zip
│       ├── arvores-avl.pdf
│       ├── ESD Árvores AVL 2025.pdf
│       ├── Inverter Árvore Binária (LeetCode 226).pdf
│       ├── LRU Cache.pdf
│       ├── Lucro máximo com a venda de vinhos.pdf
│       ├── merge_k_sorted_lists.pdf
│       ├── Parênteses Balanceados.pdf
│       ├── recipiente com mais água.pdf
│       ├── reverse-linked-list-1.pptx.pdf
│       ├── subarray-soma-maxima (2).pdf
│       ├── unidade15-abbs.pdf
│       └── unidade17-arvores-binarias.pdf
│
├── 📁 _Vault - Algoritmos/                                   # Second Brain no Obsidian (Atas, Mapas Mentais e MOC)
├── .gitignore                                                # Filtro de dependências e arquivos de ambiente (.env)
└── README.md                                                 # Portal central de navegação no padrão Gold
```

---

## 📚 Mapa Geral de Atividades & Entregas da Disciplina

| Atividade / Desafio | Módulo / Tópico | Prazo Moodle | Status | Arquivo Final de Entrega |
| :--- | :--- | :---: | :---: | :--- |
| **Exercícios de Fixação (Bases / Redes)** | Tópico 0 — Geral & Revisão C | Semanas Iniciais | ✅ **Concluído** | [`Exercícios de Fixação - Rafael F.pdf`](./Tópico%200%20-%20Informacoes%20Gerais%20e%20Revisao%20C/Entregas/Exercícios%20de%20Fixação%20-%20Rafael%20F.pdf) |
| **Seminário Oficial: LeetCode #3 (LSWRC)** | Tópico 1 — Algoritmos LeetCode 3 | Semana 4 | ✅ **Entregue** | [`Apresentacao_LeetCode3_Equipe_IFSP.pdf`](./Tópico%201%20-%20Algoritmos%20LeetCode3/Entregas/Apresentacao_LeetCode3_Equipe_IFSP.pdf) |
| **Código da Janela Deslizante (LeetCode 3)** | Tópico 1 — Algoritmos LeetCode 3 | Semana 4 | ✅ **Pronto** | [`lswrc_solucao2_janela_deslizante.c`](./Tópico%201%20-%20Algoritmos%20LeetCode3/Exercícios%20e%20Laboratórios/lswrc_solucao2_janela_deslizante.c) |
| **Código do Grafo do Exercício (Aula 4)** | Tópico 2 — Grafos | Semana 5 | ✅ **Pronto** | [`grafo_exercicio_aula4.c`](./Tópico%202%20-%20Grafos/Entregas/grafo_exercicio_aula4.c) |
| **Código do Flatten Binary Tree** | Tópico 3 — Seminários | 21/09/2026 | ✅ **Pronto** | [`flatten_binary_tree.c`](./Tópico%203%20-%20Seminários/Entregas/flatten_binary_tree.c) |
| **Código do Alien Dictionary** | Tópico 3 — Seminários | 28/09/2026 | ✅ **Pronto** | [`alien_dictionary.c`](./Tópico%203%20-%20Seminários/Entregas/alien_dictionary.c) |
| **Código de Parênteses Balanceados** | Tópico 3 — Seminários | 28/09/2026 | ✅ **Pronto** | [`parenteses_balanceados.c`](./Tópico%203%20-%20Seminários/Entregas/parenteses_balanceados.c) |
| **Lucro Máximo com a Venda de Vinhos** | Tópico 3 — Seminários | 05/10/2026 | ✅ **Entregue** | [`lucro_venda_vinhos.c`](./Tópico%203%20-%20Seminários/Entregas/lucro_venda_vinhos.c) |
| **Recipiente com Mais Água** | Tópico 3 — Seminários | 12/10/2026 | ✅ **Entregue** | [`recipiente_mais_agua.c`](./Tópico%203%20-%20Seminários/Entregas/recipiente_mais_agua.c) |
| **Inverter Árvore Binária (LeetCode 226)** | Tópico 3 — Seminários | 12/10/2026 | ✅ **Entregue** | [`inverter_arvore_binaria.c`](./Tópico%203%20-%20Seminários/Entregas/inverter_arvore_binaria.c) |
| **Merge K Sorted Lists (LeetCode 23)** | Tópico 3 — Seminários | 12/10/2026 | ✅ **Entregue** | [`merge_k_sorted_lists.c`](./Tópico%203%20-%20Seminários/Entregas/merge_k_sorted_lists.c) |
| **Subarray Contíguo de Soma Máxima (Kadane)** | Tópico 3 — Seminários | 12/10/2026 | ✅ **Entregue** | [`subarray_soma_maxima.c`](./Tópico%203%20-%20Seminários/Entregas/subarray_soma_maxima.c) |

---

## 🛠️ Guia Rápido de Compilação das Soluções em C

Todas as soluções foram desenvolvidas segundo os padrões **C99 / C11**, são autocontidas e incluem funções `main()` para testes automáticos no terminal:

```bash
# Compilar qualquer exercício individual da pasta de entregas:
gcc -Wall -Wextra -O2 "Tópico 3 - Seminários/Entregas/lucro_venda_vinhos.c" -o vinhos
./vinhos

# Compilar com g++ ou clang (compatível):
clang -O2 "Tópico 3 - Seminários/Entregas/subarray_soma_maxima.c" -o kadane
./kadane
```

---

## 👥 Autoria & Equipe

* **Rafael Feltrim** ([GitHub](https://github.com/RaFeltrim)) — *Bacharelado em Engenharia de Software (BES - IFSP São Carlos)*
* **Ian** — *Pesquisa Teórica & Análise de Algoritmos*
* **Gustavo (Gub)** — *Implementações em C & Complexidade Assintótica*
