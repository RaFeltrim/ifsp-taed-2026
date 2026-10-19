# 🚀 Tópico 1 — Desafio LeetCode #3: Longest Substring Without Repeating Characters

Módulo dedicado ao estudo, implementação em linguagem C, documentação editorial e benchmark experimental do desafio **LeetCode #3** (*Longest Substring Without Repeating Characters* / Blind 75), apresentado pela equipe de **Rafael Feltrim, Ian e Gustavo (Gub)**.

---

## 📌 Visão Geral do Problema

* **Enunciado:** Dada uma string `s`, encontrar o comprimento da maior substring contígua que não possua caracteres repetidos.
* **Complexidade Assintótica:**
  * **Solução 1 (Força Bruta):** $\mathcal{O}(N^2)$ ou $\mathcal{O}(N^3)$ de tempo, $\mathcal{O}(\min(N, \Sigma))$ de espaço.
  * **Solução 2 (Janela Deslizante / Sliding Window):** $\mathcal{O}(N)$ de tempo estrito (passada linear única), $\mathcal{O}(\min(N, \Sigma))$ de espaço auxiliar com vetor de lookup direto ASCII.

---

## 📂 Organização dos Arquivos do Módulo

```text
📁 Tópico 1 - Algoritmos LeetCode3/
│
├── 📄 README.md                                             # Este documento de referência técnica
│
├── 📁 Entregas/                                             # [ARQUIVOS FINAIS DO SEMINÁRIO]
│   ├── 📑 Apresentacao_LeetCode3_Equipe_IFSP.pdf            # Slides oficiais da apresentação da equipe
│   ├── 📝 Apresentacao_LeetCode3_Editavel.docx              # Relatório textual completo e editável
│   ├── 🖥️ Apresentacao_LeetCode3_Slides.html                # Apresentação interativa web em HTML5/CSS3
│   └── 📑 Longest-Substring-Without-Repeating-Characters.pdf # Slide do seminário consolidado
│
├── 📁 Exercícios e Laboratórios/
│   ├── 💻 lswrc_solucao1_forca_bruta.c                      # Solução 1 em C: Força Bruta O(N^2)
│   ├── 💻 lswrc_solucao2_janela_deslizante.c                # Solução 2 em C: Janela Deslizante O(N) Padrão Ouro
│   ├── 🐍 benchmark_solutions.py                            # Benchmark experimental de operações e CPU
│   ├── ⚙️ generate_pdf_slides.py                            # Gerador headless de slides
│   ├── ⚙️ generate_docx_presentation.py                     # Compilador do relatório Word
│   └── ⚙️ export_slides_to_png.py                           # Exportador de lâminas em alta resolução
│
└── 📁 Material de Apoio/
    ├── 📑 Longest-Substring-Without-Repeating-Characters.pdf
    ├── 📑 Longest-Substring-Without-Repeating-Characters_1.pdf
    ├── 📐 diagrama_janela_deslizante_editavel.svg            # Diagrama vetorial ilustrando o avanço dos ponteiros
    ├── 📝 Roteiro_Apresentacao_Equipe.md                    # Script de fala de cada membro da equipe
    └── ⚡ Prompt_Gamma_Apresentacao_LeetCode3.md             # Engenharia de prompts editoriais
```

---

## 📊 Tabela Resumo do Benchmark Experimental

| Tamanho da String ($N$) | Força Bruta $\mathcal{O}(N^2)$ | Janela Deslizante $\mathcal{O}(N)$ | Redução de Operações / Tempo |
| :--- | :--- | :--- | :---: |
| **$N = 100$** | $4.85\text{ ms}$ ($171.700$ ops) | **$0.032\text{ ms}$** ($100$ ops) | **$99.94\%$ menor** |
| **$N = 1.000$** | $1.953\text{ ms}$ ($\approx 2.0\text{ s}$) | **$0.232\text{ ms}$** ($1.000$ ops) | **$99.99\%$ menor** |
| **$N = 5.000$** | $\approx 15.0\text{ s}$ ($20.8$ bi ops) | **$1.113\text{ ms}$** ($5.000$ ops) | **$99.999\%$ menor** |
| **$N = 50.000$ (LeetCode)** | **$\approx 250\text{ min}$ ($> 4\text{ HORAS}$)** | **$11.1\text{ ms}$** ($50.000$ ops) | **⚡ $> 99.99999\%$ de redução** |

---

## 🛠️ Como Compilar e Executar as Soluções em C

```bash
# Solução 1: Força Bruta
gcc -O2 "Exercícios e Laboratórios/lswrc_solucao1_forca_bruta.c" -o solucao1
./solucao1

# Solução 2: Janela Deslizante (Padrão Ouro)
gcc -O2 "Exercícios e Laboratórios/lswrc_solucao2_janela_deslizante.c" -o solucao2
./solucao2
```
