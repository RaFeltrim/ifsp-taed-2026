---
tags: [c, memoria, stack, heap, malloc, segfault, memory-leak, chrome, aula-2, ponteiros]
tipo: anotaçoes-de-aula
status: ativo
criado: 2026-08-03
professor: Prof. Dr. Rodrigo Elias Bianchi
disciplina: Tópicos em Algoritmos e Estruturas de Dados (IFSP - São Carlos)
---

# 📝 Anotações da Aula 2: Gerenciamento de Memória, Ponteiros e Erros em C

> **Contexto:** Explicação detalhada em sala de aula sobre o comportamento da RAM, diferença Stack vs. Heap, alocação dinâmica, Memory Leak e limitações de vetores estáticos.

---

## 🧠 1. As Duas Faces do "Stack Overflow"

### A. O Significado Social vs. O Erro Computacional
- **Site de devs:** Comunidade famosa de perguntas e respostas.
- **Erro de Memória (Stack Overflow):** Ocorre quando a **Pilha de Chamadas (Call Stack)** estoura o limite de memória reservado pelo Sistema Operacional para a aplicação.

### B. Características da Memória Stack (Pilha)
- **Gerenciamento:** Automático pelo PC / Compilador.
- **Velocidade:** Extremamente rápida (alocação via deslocamento do *Stack Pointer*).
- **Escopo:** Variáveis locais de funções (nascem e morrem com o escopo).
- **Causa típica de estouro:** Recursão infinita sem caso-base ou declaração de vetores gigantes estáticos na pilha (ex: `int arr[10000000]`).

---

## 🏗️ 2. A Memória Heap (Monte) & O Papel do Desenvolvedor

Diferente da Stack, a **Heap** é a área de memória gerenciada **explicitamente por nós, desenvolvedores**.

- **Por que usar a Heap?** Para estruturas de tamanho dinâmico e flexível que crescem em tempo de execução (Listas Encadeadas, Árvores, Grafos, Hash Tables).
- **Como a Heap funciona:**
  1. O dev solicita $X$ bytes para o sistema (`malloc`).
  2. O gerenciador da Heap busca um bloco livre contíguo com pelo menos $X$ bytes.
  3. Ele marca aquele bloco como **ocupado** em sua tabela interna e retorna o **endereço inicial**.
  4. O dev utiliza e, obrigatoriamente, deve devolver o bloco com `free()`.

---

## 💧 3. Memory Leak (Vazamento de Memória) & Ciclo de Vida do Processo

> **Termo correto:** *Memory Leak* (vazamento de memória).

### Como Funciona o Ciclo de Vida:
1. Se você aloca na Heap via `malloc()` e **esquece de chamar `free()`**, aquela memória continua ocupada e indisponível para o sistema.
2. **Enquanto o processo estiver rodando**, a memória alocada vazada **continua consumida na RAM**.
3. O Sistema Operacional só consegue recuperar essa memória vazada no momento em que o **processo é encerrado/morto** (fechamento da aplicação ou *kill process* no Gerenciador de Tarefas).

### Analogia do Professor: As Versões Antigas do Google Chrome
- Nas versões mais antigas do Chrome, fechar uma aba às vezes não liberava a memória RAM devido a um *Memory Leak* na renderização.
- Mesmo com a aba fechada, o consumo de RAM permanecia alto e o navegador travava, exigindo que o usuário encerasse o **processo do Chrome** por completo para que o SO recuperasse a memória.

---

## 📐 4. Dilema do Vetor Estático vs. Estruturas Dinâmicas

### O Problema do Array Fixo (`int vet[1000]`)
- Se alocamos um vetor para até 1.000 elementos:
  - **Desperdício:** Se usarmos apenas 5 elementos, 995 posições ficam gastas sem uso.
  - **Inflexibilidade:** Se precisarmos inserir o 1.001º elemento, o bloco de memória contíguo reservado na compilação **não consegue crescer mais**.
- **Solução:**
  - **Listas Encadeadas:** Cada elemento é um nó alocado individualmente na Heap conforme a necessidade.
  - **Arrays Dinâmicos (`realloc`):** Aloca-se um tamanho inicial na Heap e, quando atinge a capacidade, realoca-se um bloco maior (geralmente dobrando de tamanho).

---

## 🔍 5. O Ponteiro para Void (`void*`) e Confirmação de Alocação

```c
// Assinatura do malloc na biblioteca <stdlib.h>:
void* malloc(size_t size);
```

### Por que `void*`?
`malloc` aloca **bytes brutos na RAM**. Ele não sabe se você vai guardar `int`, `float` ou `struct Node`. Por isso, retorna um **ponteiro genérico (`void*`)**, que é depois convertido (*cast*) para o tipo de ponteiro específico:

```c
struct Node* novo = (struct Node*) malloc(sizeof(struct Node));
```

### Confirmação de Recebimento de Memória (Null Check)
Sempre devemos validar se o sistema operacional conseguiu entregar a memória solicitada:

```c
if (novo == NULL) {
    printf("Erro: Memória Heap esgotada!\n");
    exit(1); // Interrompe a execução com segurança
}
```

---

## 💥 6. O Famoso *Segmentation Fault* (Segfault)

O **Segmentation Fault** (Falha de Segmentação) é uma violação de hardware/SO que ocorre quando o programa tenta **acessar ou modificar uma região de memória que ele não possui permissão ou que não existe**.

### Principais Causas em C:
1. **Dereferenciar ponteiro NULL ou não-inicializado:**
   ```c
   struct Node* p = NULL;
   p->data = 10; // 💀 SEGFAULT! Tentou acessar endereço 0x0.
   ```
2. **Acesso fora dos limites (Out of Bounds):**
   ```c
   int arr[5];
   arr[10000] = 42; // 💀 SEGFAULT! Invasão de segmento de memória alheio.
   ```
3. **Uso de memória após liberação (*Use-After-Free*):**
   ```c
   free(ptr);
   ptr->data = 5; // 💀 SEGFAULT! Bloco já foi devolvido à Heap.
   ```

---

## 🔗 Links Relacionados no Vault

- [[00 - Diagnóstico e Plano/Ata_Aula_02_Revisao_C_Memoria_Ponteiros_Listas]]
- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]] — memória contígua vs dispersa
- [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]] — comportamento LIFO na Stack de chamadas
