# 🎓 Tópicos em Algoritmos e Estruturas de Dados (IFSP - São Carlos)

> **Instituição:** Instituto Federal de São Paulo (IFSP) — Campus São Carlos  
> **Curso:** Bacharelado em Engenharia de Software (BES)  
> **Disciplina:** Tópicos em Algoritmos e Estruturas de Dados  
> **Docente:** Prof. Dr. Rodrigo Elias Bianchi  
> **Ano Letivo:** 2026

---

## 👥 Integrantes da Equipe
* **Rafael Feltrim** — *Desenvolvimento, Engenharia Frontend & Apresentação*
* **Ian** — *Pesquisa Teórica & Análise de Algoritmos*
* **Gustavo (Gub)** — *Análise de Complexidade & Implementações em C*

---

## 🚀 Central de Entrega: LeetCode #3 (Slide 13 / Moodle)

### 📌 Sobre o Desafio
* **Problema:** *Longest Substring Without Repeating Characters* (LeetCode #3 / Blind 75)
* **Paradigma de Resolução:** Janela Deslizante (*Sliding Window*) com Tabela Hash e Aritmética de Ponteiros em C.
* **Complexidade Ótima:** **$O(N)$ Tempo Estrito** | **$O(\min(N, \Sigma))$ Espaço**.
* **Impacto Experimental de Performance:** Redução de **$> 99,99999\%$** no tempo de CPU e eliminação de mais de $20$ trilhões de operações ($N = 50.000$) em relação à força bruta.

---

## 📂 Organização do Repositório

```text
📦 ifsp-taed-2026/
├── 📁 01_Apresentacao_e_Slides/               <- Arquivos da Apresentação Oficial
│   ├── 📄 Apresentacao_LeetCode3_Equipe_IFSP.pdf  <- PDF Final Otimizado para Projetor (10 Slides)
│   ├── 📝 Apresentacao_LeetCode3_Editavel.docx    <- Documento Editável (Google Docs / Word)
│   ├── 🖥️ Apresentacao_LeetCode3_Slides.html      <- Slides em HTML5 / CSS (Padrão Suíço)
│   ├── ⚡ Prompt_Gamma_Apresentacao_LeetCode3.md  <- Prompt Mestre para o Gamma App
│   └── 📐 diagrama_janela_deslizante_editavel.svg <- Diagrama Vetorial em Português
│
├── 📁 02_Codigos_e_Implementacoes/           <- Implementações Executáveis em C e Python
│   ├── 💻 lswrc_solucao1_forca_bruta.c            <- Solução 1 em C: Força Bruta O(N²) Interativo
│   ├── 💻 lswrc_solucao2_janela_deslizante.c      <- Solução 2 em C: Janela Deslizante O(N) Padrão Ouro
│   └── 🐍 benchmark_solutions.py                 <- Script de Benchmark Real de CPU e Operações
│
├── 📁 03_Scripts_de_Build/                   <- Automação e Geradores
│   ├── ⚙️ generate_pdf_slides.py                  <- Compilador Headless do Deck em PDF
│   └── ⚙️ generate_docx_presentation.py           <- Compilador do Documento DOCX
│
└── 📁 _Vault - Algoritmos/                   <- Cofre do Obsidian (Second Brain de Aulas)
    ├── 🏠 MOC - Mapa do Conhecimento.md           <- Índice Geral e Diário de Atas
    ├── 📊 00 - Diagnóstico e Plano/              <- Atas de Aula e Relatório de Prompts
    ├── 🔵 01 - Estruturas Lineares/              <- Notas de Arrays, Listas e LeetCode #3
    ├── 🔴 02 - Tabelas Hash/                     <- Arquitetura, Colisões e Fator de Carga
    ├── 🔴 03 - Grafos/                           <- BFS, DFS, Dijkstra, Kruskal
    ├── 🟡 04 - Árvores/                          <- BST, AVL Trees e Heaps
    └── 📈 99 - Complexidade Big-O/               <- Guia Assintótico
```

---

## 🔗 Links Rápidos para Acesso Direto:

### 1. Apresentação & Slides
* 📄 **[PDF Oficial da Apresentação](01_Apresentacao_e_Slides/Apresentacao_LeetCode3_Equipe_IFSP.pdf)**
* 📝 **[Documento Editável (.docx)](01_Apresentacao_e_Slides/Apresentacao_LeetCode3_Editavel.docx)**
* ⚡ **[Prompt Mestre para o Gamma App](01_Apresentacao_e_Slides/Prompt_Gamma_Apresentacao_LeetCode3.md)**
* 🖥️ **[Versão Web dos Slides (.html)](01_Apresentacao_e_Slides/Apresentacao_LeetCode3_Slides.html)**
* 📐 **[Diagrama Vetorial Editável (.svg)](01_Apresentacao_e_Slides/diagrama_janela_deslizante_editavel.svg)**

### 2. Códigos em C & Benchmark
* 💻 **[Solução 1 em C: Força Bruta O(N²)](02_Codigos_e_Implementacoes/lswrc_solucao1_forca_bruta.c)**
* 💻 **[Solução 2 em C: Janela Deslizante O(N) com Ponteiros](02_Codigos_e_Implementacoes/lswrc_solucao2_janela_deslizante.c)**
* 🐍 **[Script de Benchmark Experimental (Python)](02_Codigos_e_Implementacoes/benchmark_solutions.py)**

### 3. Notas do Vault Obsidian
* 🏠 **[MOC — Mapa do Conhecimento](_Vault%20-%20Algoritmos/MOC%20-%20Mapa%20do%20Conhecimento.md)**
* 📝 **[Nota Completa do Estudo LeetCode #3](_Vault%20-%20Algoritmos/01%20-%20Estruturas%20Lineares/Longest%20Substring%20Without%20Repeating%20Characters%20-%20LeetCode%203.md)**
* 📑 **[Relatório de Engenharia de Prompts & Design Editorial](_Vault%20-%20Algoritmos/00%20-%20Diagn%C3%B3stico%20e%20Plano/Engenharia_de_Prompts_e_Design_Editorial_de_Apresentacoes.md)**

---

## 📊 Tabela Resumo do Benchmark de Performance

| Tamanho da String ($N$) | Força Bruta $O(N^3)$ | Janela Deslizante ($O(N)$) | Redução de Operações / Tempo |
| :--- | :--- | :--- | :---: |
| **$N = 100$** | $4.85\text{ ms}$ ($171.700$ ops) | **$0.032\text{ ms}$** ($100$ ops) | **$99.94\%$ menor** |
| **$N = 1.000$** | $1.953\text{ ms}$ ($\approx 2.0\text{ s}$) | **$0.232\text{ ms}$** ($1.000$ ops) | **$99.99\%$ menor** |
| **$N = 5.000$** | $\approx 15.0\text{ s}$ ($20.8$ bi ops) | **$1.113\text{ ms}$** ($5.000$ ops) | **$99.999\%$ menor** |
| **$N = 50.000$ (LeetCode)** | **$\approx 250\text{ min}$ ($> 4\text{ HORAS}$)** | **$11.1\text{ ms}$** ($50.000$ ops) | **⚡ $> 99.99999\%$ de redução** |

---

## 🛠️ Como Executar os Códigos

### Compilando as Soluções em C:
```bash
# Solução 1: Força Bruta
gcc -O2 02_Codigos_e_Implementacoes/lswrc_solucao1_forca_bruta.c -o solucao1
./solucao1

# Solução 2: Janela Deslizante (Recomendada)
gcc -O2 02_Codigos_e_Implementacoes/lswrc_solucao2_janela_deslizante.c -o solucao2
./solucao2
```

### Executando o Benchmark Experimental:
```bash
python 02_Codigos_e_Implementacoes/benchmark_solutions.py
```

---

## 📚 Como Usar o Cofre no Obsidian
1. Abra o **Obsidian**.
2. Selecione **"Open folder as vault"** (Abrir pasta como cofre).
3. Aponte para a pasta `_Vault - Algoritmos`.
4. Abra o arquivo `MOC - Mapa do Conhecimento.md` para navegar pelo grafo de atas, árvores, grafos e estruturas lineares.
