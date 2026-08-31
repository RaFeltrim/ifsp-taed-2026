---
tags: [estruturas-lineares, hash-map, array, O(1), entrevista, big-tech, meta, twitter]
tipo: estudo-de-caso
status: ativo
criado: 2026-07-27
empresa: [Meta, Twitter/X, Netflix, Amazon]
---

# 🚀 RandomizedSet: Operações em Tempo Constante O(1)

> **Desafio LeetCode 380 (Nível Médio / Pergunta Favorita da Meta e Netflix)**
> **Objetivo:** Projetar uma estrutura de dados onde `insert(val)`, `remove(val)` e `getRandom()` rodem TODOS em tempo constante **$O(1)$**.

---

## 💡 O Conflito Teórico das Estruturas Simples

Para entender a genialidade do **RandomizedSet**, precisamos entender por que nenhuma estrutura individual consegue resolver o problema sozinha:

| Estrutura de Dados | `insert(x)` | `remove(x)` | `getRandom()` em $O(1)$ | Onde falha? |
|---|---|---|---|---|
| **Array Dinâmico** | $O(1)$ amortizado | $O(N)$ | **$O(1)$** (`array[rand()]`) | Deleção no meio requer deslocar todos os elementos para a esquerda ($O(N)$). |
| **Lista Encadeada** | $O(1)$ nas pontas | $O(N)$ para buscar | **$O(N)$** | Não possui acesso aleatório direto por índice em memória contígua. |
| **Hash Table** | **$O(1)$** | **$O(1)$** | **$O(N)$** | Os slots não são contíguos. Não dá para sortear um número de 0 a $N-1$ e pegar uma chave em $O(1)$. |
| **Árvore Balanceada (AVL/BST)** | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | Operações são logarítmicas, não constantes. |

---

## 🔑 A Solução Híbrida: Hash Map + Array Dinâmico

A sacada de engenharia consiste em unir **Array Dinâmico** (que dá acesso aleatório por índice $O(1)$) com uma **Tabela Hash** (que rastreia a posição de cada elemento no array em $O(1)$).

```text
HASH MAP:                   ARRAY DINÂMICO:
{"FilmeA": 0}              índice:    0         1         2         3
{"FilmeB": 1}   ────────►  valor:  ["FilmeA", "FilmeB", "FilmeC", "FilmeD"]
{"FilmeC": 2}
{"FilmeD": 3}
```

---

## ⚡ O Efeito Mágico: Deleção em $O(1)$ sem Deslocar Nada

Para deletar "FilmeB" (índice 1) em $O(1)$:

1. Localizamos o índice de "FilmeB" no Hash Map $\rightarrow$ `1`.
2. Pegamos o **último elemento do array** ("FilmeD", no índice `3`).
3. **Substituímos** "FilmeB" por "FilmeD" no índice 1 do array ($O(1)$).
4. Atualizamos o Hash Map: `{"FilmeD": 1}` ($O(1)$).
5. Executamos `.pop()` no final do array ($O(1)$)!

```text
PASSO 1: Troca com a ponta    → Array: ["FilmeA", "FilmeD", "FilmeC", "FilmeB"]
PASSO 2: Pop no final         → Array: ["FilmeA", "FilmeD", "FilmeC"]  (tamanho 3)
PASSO 3: Atualiza Hash Map    → {"FilmeA":0, "FilmeD":1, "FilmeC":2}
```

---

## 💻 Implementação Limpa em Python

```python
import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # HashMap: valor -> indice no array
        self.vals = []          # Dynamic Array: armazena os valores contíguos

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        # Insere no final do array (O(1))
        self.val_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        # 1. Localiza o índice do elemento a remover e o último elemento
        idx_to_remove = self.val_to_index[val]
        last_val = self.vals[-1]
        
        # 2. Move o último elemento para a posição do elemento removido
        self.vals[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove
        
        # 3. Remove o último elemento da lista e do mapa (O(1))
        self.vals.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # Sorteio uniforme instantâneo em O(1)
        return random.choice(self.vals)
```

---

## ⚖️ Análise de Complexidade

- **`insert(val)`:** Tempo $O(1)$ amortizado / Espaço $O(1)$.
- **`remove(val)`:** Tempo $O(1)$ / Espaço $O(1)$.
- **`getRandom()`:** Tempo $O(1)$ / Espaço $O(1)$.
- **Espaço Total:** $O(N)$ onde $N$ é o número de elementos únicos armazenados.

---

## 🔗 Links Relacionados no Vault

- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]] — acesso direto por índice
- [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]] — mapeamento rápido em O(1)
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] — tempo constante vs linear
