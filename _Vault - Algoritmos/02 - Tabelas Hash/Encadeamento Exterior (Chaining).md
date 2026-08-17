---
tags: [hash-table, chaining, encadeamento, fase-2, crítico]
tipo: conceito
status: lacuna-crítica
pré-requisito: [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]]
próximo: [[02 - Tabelas Hash/Sondagem Linear (Linear Probing)]]
criado: 2026-07-27
---

# 🔴 Encadeamento Exterior (Chaining)

> Estratégia de resolução de colisão: cada slot da tabela vira uma **lista encadeada**.

## Como Funciona

```
Tabela com m = 5 slots:

slot 0: NULL
slot 1: [Ana|→] → [Marcos|→] → NULL    ← COLISÃO resolvida por lista
slot 2: [Carlos|→] → NULL
slot 3: [Rafael|→] → NULL
slot 4: NULL

hash("Ana")    % 5 = 1
hash("Marcos") % 5 = 1   ← colisão! vai para lista do slot 1
```

---

## Operações com Chaining

### Insert
```
1. Calcule: idx = hash(chave) % m
2. Insira na lista do slot idx
   - Inserção no início da lista → O(1)
```

### Search
```
1. Calcule: idx = hash(chave) % m
2. Percorra a lista do slot idx até encontrar a chave
   - Melhor caso: chave é a primeira → O(1)
   - Pior caso: percorre toda a lista → O(k) onde k = tamanho da lista
```

### Delete
```
1. Calcule: idx = hash(chave) % m
2. Encontre e remova da lista do slot idx → O(k)
```

---

## Análise de Complexidade

| Operação | Caso Médio | Pior Caso |
|---|---|---|
| insert | **O(1)** | O(1) - insere sempre no início |
| search | **O(1 + α)** | O(N) - todas as chaves no mesmo slot |
| delete | **O(1 + α)** | O(N) |

Onde **α = n/m** (Fator de Carga) → ver [[02 - Tabelas Hash/Fator de Carga e Rehashing]]

> O(1 + α) no caso médio: o "1" é o custo da função hash + acesso ao slot.
> O "α" é o comprimento médio das listas.

---

## Dry-Run - Inserindo com Colisões

```
Tabela m = 5. Inserindo: "Ana", "Bob", "Carlos", "Dan", "Eve", "Flo"

hash("Ana") % 5 = 0  → slot 0: [Ana]
hash("Bob") % 5 = 2  → slot 2: [Bob]
hash("Carlos") % 5 = 0  → COLISÃO! slot 0: [Carlos] → [Ana]
hash("Dan") % 5 = 3  → slot 3: [Dan]
hash("Eve") % 5 = 2  → COLISÃO! slot 2: [Eve] → [Bob]
hash("Flo") % 5 = 0  → COLISÃO! slot 0: [Flo] → [Carlos] → [Ana]

Estado final:
slot 0: [Flo] → [Carlos] → [Ana]
slot 1: NULL
slot 2: [Eve] → [Bob]
slot 3: [Dan]
slot 4: NULL

α = 6/5 = 1.2 → acima do ideal! Hora de rehashing.
```

---

## Chaining vs. Sondagem Linear

| | Chaining | Sondagem Linear |
|---|---|---|
| Estrutura por slot | Lista encadeada | Slot vazio no array |
| Memória extra | Sim (ponteiros) | Não |
| Degradação | Gradual | Clustering rápido |
| Cache friendly | Não | Sim |
| α tolerado | α > 1 possível | α < 1 obrigatório |

---

## Conexões no Vault

- [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]] - base da estrutura
- [[02 - Tabelas Hash/Sondagem Linear (Linear Probing)]] - abordagem alternativa
- [[02 - Tabelas Hash/Fator de Carga e Rehashing]] - quando fazer rehash
- [[01 - Estruturas Lineares/Listas Duplamente Encadeadas e Deque]] - estrutura da lista nos slots
