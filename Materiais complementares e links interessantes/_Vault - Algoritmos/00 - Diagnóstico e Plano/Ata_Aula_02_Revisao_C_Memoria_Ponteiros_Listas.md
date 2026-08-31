---
tags: [ata-de-aula, aula-2, c, ponteiros, malloc, stack, heap, listas, segfault, memory-leak, chrome]
tipo: ata-de-aula
data: 2026-08-03
aula_numero: 2
professor: Prof. Dr. Rodrigo Elias Bianchi
disciplina: Tópicos em Algoritmos e Estruturas de Dados (IFSP - São Carlos)
---

# 📌 Ata da Aula 02: Revisão de Estrutura de Dados em C, Memória & Ponteiros

> **Data:** 03 / Agosto / 2026  
> **Professor:** Prof. Dr. Rodrigo Elias Bianchi  
> **Material Base:** Slides 01 a 10 ("Revisão de Estrutura de Dados em C") + Anotações de Sala de Aula

---

## 🎯 1. Resumo Executivo da Aula

A aula revisou os fundamentos de programação em C baixo nível essenciais para a disciplina. Foram abordados ponteiros (`&` e `*`), a diferença arquitetural entre memória **Stack** e **Heap**, alocação dinâmica com `malloc`/`free`, pontes para `void*`, prevenção de **Memory Leak** e **Segmentation Fault**, o comportamento do SO durante a execução do processo (exemplo do Chrome antigo), limitações de vetores estáticos e a manipulação de **Listas Encadeadas Simples e Duplas**.

---

## 🧠 2. Síntese Teórica & Anotações de Sala de Aula

### A. Stack vs. Heap
- **Stack (Pilha de Chamadas):** Memória alocada automaticamente pelo compilador. Rápida, tamanho fixo, variáveis locais.
  - *Stack Overflow:* Ocorre quando a pilha estoura o limite do SO (ex: recursão infinita ou arrays locais gigantes).
- **Heap (Monte):** Memória dinâmica gerenciada **explicitamente pelo desenvolvedor**.
  - `malloc(bytes)`: Busca bloco contíguo na Heap, marca como ocupado e retorna endereço.
  - `free(ptr)`: Liberação obrigatória. Esquecer gera *Memory Leak*.

### B. Memory Leak & Ciclo de Vida do Processo
- **O que é:** Alocar na Heap via `malloc()` e esquecer de liberar via `free()`.
- **Ciclo de Vida:** Enquanto o processo do programa estiver rodando (*running*), a memória vazada continua presa pela Heap. O Sistema Operacional só consegue recuperar essa memória quando o **processo é finalizado/encerrado**.
- **Analogia do Professor (Google Chrome Antigo):** Em versões antigas do Chrome, abas fechadas não liberavam a memória devido a um *Memory Leak* no renderizador. O computador acumulava travamentos até que o processo do Chrome fosse totalmente encerrado pelo usuário.

### C. Dilema dos Vetores Estáticos vs. Estruturas Dinâmicas
- Um vetor estático `int vet[1000]` tem dois grandes problemas:
  1. **Desperdício:** Se usar apenas 5 posições, 995 ficam gastas sem uso.
  2. **Inflexibilidade:** Se precisar da posição 1.001, a memória contígua alocada estaticamente não consegue crescer.
- **Solução:** Usar **Listas Encadeadas** (alocação nó a nó na Heap) ou **Arrays Dinâmicos com `realloc()`**.

### D. Ponteiros, `void*` e Segmentation Fault
- **Operadores `&` e `*`:** Endereço de memória e dereferenciação.
- **Indireção Dupla (`Node** head_ref`):** Usada para alterar a cabeça (`head`) da lista por referência.
- **`void*`:** Ponteiro genérico retornado pelo `malloc`. Deve ser convertido para o tipo concreto.
- **Null Check:** Validar `if (ptr == NULL)` antes de usar a memória.
- **Segmentation Fault:** Erro de violação de acesso à memória (dereferenciar `NULL`, acessar índice fora dos limites ou usar bloco já desalocado).

---

## 💻 3. Exercícios Práticos Resolvidos na Aula

### 📌 Exercício 01: Busca e Contagem de Nós em Lista Simples
- **Enunciado:** Percorrer lista encadeada simples e retornar a frequência de um determinado inteiro.
- **Código C:**
  ```c
  int buscarEContar(struct Node* head, int valor_buscado) {
      int contador = 0;
      struct Node* atual = head;
      while (atual != NULL) {
          if (atual->data == valor_buscado) {
              contador++;
          }
          atual = atual->next;
      }
      return contador;
  }
  ```
- **Complexidade:** Tempo $O(n)$ | Espaço $O(1)$.

---

### 📌 Exercício 02: Inversão de Lista Duplamente Encadeada
- **Enunciado:** Inverter a ordem dos nós ajustando os ponteiros `next` e `prev`.
- **Código C:**
  ```c
  void inverterLista(struct Node** head_ref) {
      struct Node* temp = NULL;
      struct Node* atual = *head_ref;
      
      while (atual != NULL) {
          temp = atual->prev;
          atual->prev = atual->next;
          atual->next = temp;
          atual = atual->prev; // Avança para o antigo next (agora em prev)
      }
      
      if (temp != NULL) {
          *head_ref = temp->prev; // Atualiza novo head
      }
  }
  ```
- **Complexidade:** Tempo $O(n)$ | Espaço $O(1)$.

---

## 🔗 4. Links Relacionados no Vault

- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]]
- [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]]
- [[01 - Estruturas Lineares/Listas Duplamente Encadeadas e Deque]]
- [[01 - Estruturas Lineares/Anotacoes_Aula02_Ponteiros_Memoria_C]]
- [[00 - Diagnóstico e Plano/Ata_Aula_01_Introducao_e_Ementa]]
