---
tags: [estruturas-lineares, pilha, stack, LIFO, fase-1]
tipo: conceito
status: revisando
pré-requisito: [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]]
próximo: [[01 - Estruturas Lineares/Filas (Queue - FIFO)]]
usada-em: [[03 - Grafos/DFS - Busca em Profundidade]]
criado: 2026-07-27
---

# 🔵 Pilhas (Stack - LIFO)

> **Last In, First Out** - O último a entrar é o primeiro a sair.
> Pense numa pilha de pratos: você só tira do topo.

## Interface da Pilha

| Operação | O quê faz | Complexidade |
|---|---|---|
| `push(x)` | Insere `x` no topo | **O(1)** |
| `pop()` | Remove e retorna o topo | **O(1)** |
| `peek()` | Retorna o topo sem remover | **O(1)** |
| `isEmpty()` | Verifica se está vazia | **O(1)** |
| `size()` | Retorna número de elementos | **O(1)** |

> Todas as operações são **O(1)**. Não existe operação lenta em uma pilha bem implementada.

---

## Visualização LIFO

```
Estado inicial:    push(10):     push(20):     pop():
                                               retorna 20
    [ vazio ]       [  10  ]      [  20  ] ←    [  10  ]
                    ← topo        ← topo         ← topo
```

---

## Implementações Possíveis

### Usando Array (mais comum)
```
Pilha baseada em array:
  dados = [10, 20, 30]
  topo = 2  (índice do último elemento)

  push(40) → dados = [10, 20, 30, 40], topo = 3
  pop()    → retorna dados[3]=40, topo = 2
```

**Trade-off:** Tamanho máximo fixo (ou custo de realocação O(N) amortizado).

### Usando Lista Encadeada
```
  topo → [30|→] → [20|→] → [10|→] → NULL

  push(40) → [40|→] → [30|→] → [20|→] → [10|→] → NULL
  pop()    → remove o primeiro nó, retorna 40
```

**Trade-off:** Sem limite de tamanho, mas usa mais memória por nó (ponteiro extra).

---

## Onde Pilhas Aparecem na Prática?

| Aplicação | Como a Pilha é usada |
|---|---|
| **DFS** em grafos | Vértices a visitar ficam na pilha |
| **Recursão** | Cada chamada de função é empilhada |
| **Undo/Redo** em editores | Ações são empilhadas |
| **Validação de parênteses** | Abre → push; fecha → pop e verifica |
| **Avaliação de expressões** | Operadores e operandos na pilha |

---

## Dry-Run - Validação de Parênteses

```
Entrada: "({[]})"

Passo 1: '(' → push → pilha: ['(']
Passo 2: '{' → push → pilha: ['(', '{']
Passo 3: '[' → push → pilha: ['(', '{', '[']
Passo 4: ']' → pop → retira '[' → match! pilha: ['(', '{']
Passo 5: '}' → pop → retira '{' → match! pilha: ['(']
Passo 6: ')' → pop → retira '(' → match! pilha: []

Resultado: VÁLIDO ✅
```

---

## Conexões no Vault

- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]] - escolha de implementação
- [[01 - Estruturas Lineares/Filas (Queue - FIFO)]] - estrutura oposta (FIFO)
- [[03 - Grafos/DFS - Busca em Profundidade]] - DFS **é** uma pilha
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - por que tudo é O(1)
