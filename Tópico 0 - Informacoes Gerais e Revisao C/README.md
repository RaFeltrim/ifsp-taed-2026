# 📌 Tópico 0 — Informações Gerais, Ementa & Revisão de C

Repositório e guia de estudos do módulo inicial da disciplina **Tópicos em Algoritmos e Estruturas de Dados (TAED - SCLTAED / 400267)** do Bacharelado em Engenharia de Software (BES) no Instituto Federal de São Paulo (IFSP) — Campus São Carlos.

---

## 👨‍🏫 Corpo Docente e Informações da Disciplina

* **Instituição:** Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) — Campus São Carlos
* **Curso:** Bacharelado em Engenharia de Software (BES)
* **Disciplina:** Tópicos em Algoritmos e Estruturas de Dados (TAED)
* **Código:** SCLTAED / 400267
* **Ano / Semestre:** 2026.2
* **Docente Responsável:** Prof. Dr. Rodrigo Elias Bianchi
* **E-mail Institucional:** [bianchi@ifsp.edu.br](mailto:bianchi@ifsp.edu.br) / [cti.scl@ifsp.edu.br](mailto:cti.scl@ifsp.edu.br)
* **Ambiente Virtual:** [Moodle IFSP São Carlos (Curso ID 5193)](https://moodle.scl.ifsp.edu.br/course/view.php?id=5193)

---

## 🎯 Ementa e Objetivos do Módulo

1. **Apresentação e Metodologia:** Dinâmica das aulas expositivas, laboratórios práticos e seminários de algoritmos avançados das Big Techs (LeetCode Medium e Hard).
2. **Revisão Aprofundada em Linguagem C:**
   * Domínio de Ponteiros, Ponteiros para Ponteiros e Aritmética de Endereços.
   * Gerenciamento Dinâmico de Memória no Heap (`malloc`, `calloc`, `realloc`, `free`) e prevenção contra *Memory Leaks* e *Dangling Pointers*.
   * Definição e manipulação de tipos abstratos de dados (TADs) com `struct` e `typedef`.
   * Implementação fundamental de Listas Simplesmente e Duplamente Encadeadas.
3. **Avaliação Diagnóstica e Fixação:** Nivelamento sobre conversão de bases numéricas (Binário/Decimal) e representação de dados na arquitetura de computadores.

---

## 📂 Organização dos Arquivos do Módulo

```text
📁 Tópico 0 - Informacoes Gerais e Revisao C/
│
├── 📄 README.md                                             # Este documento de referência
│
├── 📁 Material de Apoio/
│   ├── 📑 Aula 1 - Tópicos em Algoritmos e Estruturas de Dados.pdf # Slides de abertura, objetivos e ementa
│   └── 📑 Aula 2 - Revisão de Estrutura de Dados em C.pdf          # Guia prático de ponteiros, heap e listas
│
└── 📁 Entregas/
    └── 📑 Exercícios de Fixação - Rafael F.pdf              # Resolução individual de fixação e conversão
```

---

## 📖 Resumo Conceitual: Ponteiros e Gestão de Memória em C

### 1. Declaração e Desreferenciação
```c
int x = 42;
int *p = &x;     // 'p' armazena o endereço físico de 'x' no Stack
*p = 100;        // Altera o valor de 'x' indiretamente para 100
```

### 2. Alocação no Heap vs. Stack
| Segmento | Características | Gerenciamento |
| :--- | :--- | :--- |
| **Stack (Pilha)** | Variáveis locais, passagem por valor, escopo léxico rápido | Automático |
| **Heap (Monte)** | Estruturas dinâmicas (árvores, listas, grafos), persistência flexível | Manual (`malloc` / `free`) |

```c
// Alocação segura com checagem de ponteiro nulo
int *vetor = (int*)malloc(n * sizeof(int));
if (vetor == NULL) {
    fprintf(stderr, "Erro crítico: Memória insuficiente!\n");
    exit(EXIT_FAILURE);
}

// Liberação obrigatória para evitar vazamentos (Memory Leaks)
free(vetor);
vetor = NULL;
```
