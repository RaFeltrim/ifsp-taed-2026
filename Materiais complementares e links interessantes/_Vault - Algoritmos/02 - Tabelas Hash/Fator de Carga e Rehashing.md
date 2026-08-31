---
tags: [hash-table, load-factor, rehashing, fase-2, crítico]
tipo: conceito
status: lacuna-crítica
pré-requisito: [[02 - Tabelas Hash/Sondagem Linear (Linear Probing)]]
próximo: [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]]
criado: 2026-07-27
---

# 🔴 Fator de Carga e Rehashing

> O fator de carga é o termômetro da Hash Table. Quando está alto, a performance despenca.

## Definição

```
α (alpha) = n / m

onde:
  n = número de elementos inseridos
  m = número de slots na tabela (tamanho)
```

### Exemplos

```
m = 10 slots, n = 3 elementos → α = 3/10 = 0.3  (saudável)
m = 10 slots, n = 7 elementos → α = 7/10 = 0.7  (limite)
m = 10 slots, n = 9 elementos → α = 9/10 = 0.9  (perigoso)
m = 10 slots, n = 10 elementos → α = 1.0  (sondagem linear trava!)
```

---

## Impacto no Desempenho

### Chaining
```
α = 0.5 → listas de comprimento médio 0.5 → busca ≈ O(1)
α = 1.0 → listas de comprimento médio 1.0 → busca ≈ O(1) ainda ok
α = 5.0 → listas de comprimento médio 5.0 → busca ≈ O(5) = O(N/m)
```

> No chaining, α pode ultrapassar 1.0, mas a performance cai gradualmente.

### Sondagem Linear
```
α = 0.5 → busca média ≈ 1.5 comparações
α = 0.7 → busca média ≈ 2.5 comparações
α = 0.9 → busca média ≈ 10  comparações
α → 1.0 → busca → O(N)  ← colapso!
```

> Na sondagem, α **nunca pode atingir 1.0** (sem slots livres = loop infinito).

---

## Limiares Práticos

| Estratégia | Rehash quando... | Por quê |
|---|---|---|
| **Chaining** | α > 1.0 (ou 0.75 conservador) | Listas ficam longas |
| **Sondagem Linear** | α > 0.7 | Clustering acelera |

> Python dict e Java HashMap usam **0.75** como limiar padrão.

---

## Processo de Rehashing

```
Situação: tabela com m=10, α > 0.7 → precisa rehash

Passo 1: Criar nova tabela com m' = 2 × m = 20 slots
         (geralmente dobra e escolhe o próximo primo)

Passo 2: Para cada elemento existente:
         novo_idx = hash(chave) % 20  ← recalcula!
         insere na nova tabela

Passo 3: Substituir a tabela antiga pela nova

Custo do rehash: O(N) - percorre todos os N elementos
```

> Rehashing é O(N), mas acontece raramente.
> **Custo amortizado:** O(1) por inserção em média.

---

## Visualização do Rehashing

```
ANTES (m=5, n=4, α=0.8 → REHASH!):
slot 0: [Eve] → NULL
slot 1: [Ana] → [Carlos] → NULL
slot 2: [Bob] → NULL
slot 3: NULL
slot 4: [Dan] → NULL

DEPOIS (m=10, α=0.4 → saudável):
slot 0: [Eve]
slot 1: [Ana]
slot 3: [Carlos]
slot 7: [Bob]
slot 9: [Dan]
```

---

## Complexidade Amortizada

| Operação | Custo individual | Custo amortizado |
|---|---|---|
| insert (sem rehash) | O(1) | O(1) |
| insert (com rehash) | O(N) | O(1) |
| search | O(1) avg | O(1) avg |

> "Amortizado" = o custo total de N inserções é O(N), então cada uma custa O(1) em média.

---

## Conexões no Vault

- [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]] - contexto geral
- [[02 - Tabelas Hash/Encadeamento Exterior (Chaining)]] - como α afeta chaining
- [[02 - Tabelas Hash/Sondagem Linear (Linear Probing)]] - por que sondagem é mais sensível
- [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]] - próxima fase
