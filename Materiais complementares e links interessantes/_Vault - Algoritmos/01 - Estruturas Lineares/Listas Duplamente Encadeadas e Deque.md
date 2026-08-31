---
tags: [estruturas-lineares, deque, lista-dupla, fase-1]
tipo: conceito
status: revisando
pré-requisito: [[01 - Estruturas Lineares/Filas (Queue - FIFO)]]
próximo: [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]]
criado: 2026-07-27
---

# 🔵 Listas Duplamente Encadeadas e Deque

> Extensão natural das listas simples - permite navegação e inserção em **ambas as direções**.

## Lista Duplamente Encadeada

```
NULL ← [prev|10|next] ↔ [prev|20|next] ↔ [prev|30|next] → NULL
           head                                  tail
```

Cada nó tem **três campos:**
- `prev` → ponteiro para o nó anterior
- `data` → valor armazenado
- `next` → ponteiro para o próximo nó

### Complexidades

| Operação | Complexidade | Por quê |
|---|---|---|
| Inserção no início (head) | **O(1)** | Atualiza head e prev do antigo head |
| Inserção no fim (tail) | **O(1)** | Atualiza tail e next do antigo tail |
| Inserção no meio | **O(N)** | Precisa encontrar a posição primeiro |
| Remoção de qualquer nó (se tiver ponteiro) | **O(1)** | Reconecta prev e next diretamente |
| Busca por valor | **O(N)** | Percorre a lista |

---

## Deque (Double-Ended Queue)

> Fila de duas pontas - insere e remove dos **dois lados** em O(1).

```
front → [A] ↔ [B] ↔ [C] ↔ [D] ← rear

addFront(Z): front → [Z] ↔ [A] ↔ [B] ↔ [C] ↔ [D] ← rear
addRear(E):  front → [Z] ↔ [A] ↔ [B] ↔ [C] ↔ [D] ↔ [E] ← rear
removeFront(): retorna Z → front → [A] ↔ [B] ↔ ...
removeRear():  retorna E → ... ↔ [D] ← rear
```

### Interface do Deque

| Operação | Complexidade |
|---|---|
| `addFront(x)` | **O(1)** |
| `addRear(x)` | **O(1)** |
| `removeFront()` | **O(1)** |
| `removeRear()` | **O(1)** |

---

## Por que Isso Resolve a Lacuna do Diagnóstico?

> *"Erros na análise de complexidade temporal para inserção O(1) em listas encadeadas duplas com ponteiro de cabeçalho"* - Diagnóstico

A inserção **só é O(1)** quando:
1. Você está inserindo **nas pontas** (head ou tail)
2. Você tem **ponteiros diretos** para head e tail
3. Você **não precisa encontrar a posição** primeiro

Se você busca uma posição no meio antes de inserir, a operação total vira **O(N)**.

---

## Aplicações

| Aplicação | Uso do Deque |
|---|---|
| **Implementação de Fila** | Deque com addRear + removeFront |
| **Implementação de Pilha** | Deque com addFront + removeFront |
| **Cache LRU** | Lista dupla + Hash Table |
| **Sliding Window** | Algoritmos de janela deslizante |
| **Histórico de navegação** | ← e → usam pontas do deque |

---

## Conexões no Vault

- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]] - base da estrutura
- [[01 - Estruturas Lineares/Filas (Queue - FIFO)]] - Deque generaliza a Fila
- [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]] - Deque generaliza a Pilha
- [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]] - próxima fase
