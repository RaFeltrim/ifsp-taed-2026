---
tags: [estruturas-lineares, fila, queue, FIFO, fase-1]
tipo: conceito
status: revisando
pré-requisito: [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]]
próximo: [[01 - Estruturas Lineares/Listas Duplamente Encadeadas e Deque]]
usada-em: [[03 - Grafos/BFS - Busca em Largura]]
criado: 2026-07-27
---

# 🔵 Filas (Queue - FIFO)

> **First In, First Out** - O primeiro a entrar é o primeiro a sair.
> Pense numa fila de banco: quem chegou primeiro, sai primeiro.

## ⚠️ A Confusão Clássica

| | Pilha (Stack) | Fila (Queue) |
|---|---|---|
| **Ordem** | LIFO - último entra, primeiro sai | FIFO - primeiro entra, primeiro sai |
| **Insere em** | Topo | Cauda (rear) |
| **Remove de** | Topo | Cabeça (front) |
| **Algoritmo** | DFS | BFS |

> **Regra mental:** Pilha = mesma ponta. Fila = pontas opostas.

---

## Interface da Fila

| Operação | O quê faz | Complexidade |
|---|---|---|
| `enqueue(x)` | Insere `x` na cauda | **O(1)** |
| `dequeue()` | Remove e retorna da cabeça | **O(1)** |
| `peek()` | Retorna o front sem remover | **O(1)** |
| `isEmpty()` | Verifica se está vazia | **O(1)** |

> Todas **O(1)** - desde que implementada corretamente com ponteiro de cauda!

---

## Visualização FIFO

```
enqueue(10):   enqueue(20):   enqueue(30):   dequeue():
                                              retorna 10
front→[10]←tail  [10]→[20]←tail  [10]→[20]→[30]←tail  front→[20]→[30]←tail
```

---

## Implementação Correta

### Por que o ponteiro de cauda importa?

```
# SEM ponteiro de cauda (ERRADO - O(N) no enqueue):
class FilaErrada:
    lista = []
    def enqueue(x): lista.append(x)    # O(1) ✅ neste caso
    def dequeue():  return lista.pop(0) # O(N) ❌ - desloca tudo!

# COM lista duplamente encadeada + head + tail (CORRETO - O(1)):
class FilaCorreta:
    head → [10] ↔ [20] ↔ [30] ← tail
    def enqueue(x): adiciona após tail → O(1)
    def dequeue():  remove de head     → O(1)
```

> **Essa foi uma das lacunas identificadas no diagnóstico!**
> Ver: [[00 - Diagnóstico e Plano/Diagnóstico Técnico]]

---

## Onde Filas Aparecem na Prática?

| Aplicação | Como a Fila é usada |
|---|---|
| **BFS** em grafos | Vértices a visitar ficam na fila |
| **Escalonador de CPU** | Processos aguardam na fila |
| **Buffer de impressão** | Documentos em ordem de chegada |
| **Streaming** | Frames de vídeo processados em ordem |
| **Cache LRU** | Fila de uso recente |

---

## Dry-Run - BFS simplificado

```
Grafo: A → B, A → C, B → D

Fila: [A]
Visita A → processa → enfileira B, C → Fila: [B, C]
Visita B → processa → enfileira D   → Fila: [C, D]
Visita C → processa → sem filhos    → Fila: [D]
Visita D → processa → sem filhos    → Fila: []
Fim ✅

Ordem de visita: A → B → C → D  (nível por nível)
```

---

## Conexões no Vault

- [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]] - estrutura oposta
- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]] - implementação interna
- [[03 - Grafos/BFS - Busca em Largura]] - BFS **é** uma fila
- [[01 - Estruturas Lineares/Listas Duplamente Encadeadas e Deque]] - base da fila eficiente
