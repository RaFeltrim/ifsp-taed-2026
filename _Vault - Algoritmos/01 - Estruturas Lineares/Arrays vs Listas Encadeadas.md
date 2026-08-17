---
tags: [estruturas-lineares, array, lista-encadeada, fase-1]
tipo: conceito
status: revisando
pré-requisito: [[99 - Complexidade Big-O/Guia de Complexidade Big-O]]
próximo: [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]]
criado: 2026-07-27
---

# 🔵 Arrays vs. Listas Encadeadas

> **Fase 1 - Fundamentos Lineares**
> Entender essa diferença é entender por que algumas operações são O(1) e outras O(N).

## A Diferença Fundamental

| | Array | Lista Encadeada |
|---|---|---|
| **Memória** | Contígua (bloco único) | Dispersa (nós com ponteiros) |
| **Acesso por índice** | O(1) - direto | O(N) - precisa percorrer |
| **Inserção no início** | O(N) - desloca tudo | O(1) - muda ponteiro |
| **Inserção no fim** | O(1) amortizado | O(1) com ponteiro de cauda |
| **Busca por valor** | O(N) | O(N) |
| **Espaço extra** | O(1) | O(N) - ponteiros custam memória |

---

## Memória Visual

### Array
```
índice:  [0]  [1]  [2]  [3]  [4]
valor:   [10] [20] [30] [40] [50]
         └─── endereços contíguos ───┘
```
Acesso: `arr[2]` → vai direto ao endereço base + 2 × tamanho. **O(1).**

### Lista Encadeada Simples
```
[10 | →] → [20 | →] → [30 | →] → [40 | →] → [50 | NULL]
  nó0          nó1         nó2         nó3         nó4
```
Para chegar ao nó2, precisa percorrer nó0 → nó1 → nó2. **O(N).**

### Lista Duplamente Encadeada
```
NULL ← [10 | ←→] ↔ [20 | ←→] ↔ [30 | ←→] ↔ [40 | ←→] ↔ [50 | →] → NULL
         head                                               tail
```
Com `head` e `tail`: inserção nas pontas em **O(1).**

---

## Quando Usar Cada Um?

**Use Array quando:**
- Precisa de acesso aleatório rápido por índice
- Tamanho é conhecido e fixo
- Cache performance importa (memória contígua = menos cache miss)

**Use Lista Encadeada quando:**
- Muitas inserções/remoções no início
- Tamanho varia muito (sem realocação)
- Vai implementar Pilha ou Fila internamente

---

## Conexões no Vault

- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - por que O(1) vs O(N)
- [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]] - usa array ou lista
- [[01 - Estruturas Lineares/Filas (Queue - FIFO)]] - lista com ponteiro de cauda
- [[01 - Estruturas Lineares/Listas Duplamente Encadeadas e Deque]] - extensão natural
