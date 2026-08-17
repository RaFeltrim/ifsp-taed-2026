---
tags: [hash-table, sondagem-linear, open-addressing, fase-2, crítico]
tipo: conceito
status: lacuna-crítica
pré-requisito: [[02 - Tabelas Hash/Encadeamento Exterior (Chaining)]]
próximo: [[02 - Tabelas Hash/Fator de Carga e Rehashing]]
criado: 2026-07-27
---

# 🔴 Sondagem Linear (Linear Probing)

> Estratégia de endereçamento aberto: sem listas. Quando há colisão, **procura o próximo slot livre no próprio array**.

## Como Funciona

```
Se slot[hash(chave) % m] está ocupado:
    Tente slot[(hash(chave) + 1) % m]
    Tente slot[(hash(chave) + 2) % m]
    Tente slot[(hash(chave) + 3) % m]
    ...
```

---

## Dry-Run - Sondagem Linear Passo a Passo

```
Tabela m = 7. Inserindo: "Ana", "Bob", "Carlos" (todos com hash % 7 = 2)

Passo 1 - Insert "Ana":
  hash("Ana") % 7 = 2
  slot 2 livre → insere
  [ ][ ][Ana][ ][ ][ ][ ]

Passo 2 - Insert "Bob":
  hash("Bob") % 7 = 2
  slot 2 OCUPADO → sonda slot 3
  slot 3 livre → insere
  [ ][ ][Ana][Bob][ ][ ][ ]

Passo 3 - Insert "Carlos":
  hash("Carlos") % 7 = 2
  slot 2 OCUPADO → sonda slot 3
  slot 3 OCUPADO → sonda slot 4
  slot 4 livre → insere
  [ ][ ][Ana][Bob][Carlos][ ][ ]

Clustering! Chaves em slots consecutivos → degradação crescente.
```

---

## O Problema do Clustering Primário

```
Antes:  [ ][ ][X][ ][ ][ ][ ]
Após 4 inserções colisoras:  [ ][ ][X][X][X][X][ ]

Agora, qualquer nova chave com hash = 2, 3, 4 ou 5
precisa sondar até 5 slots → O(N) no pior caso!
```

> Quanto maior o cluster, maior a probabilidade de novos elementos aterrissarem nele.
> É uma **degradação acelerada** - não linear.

---

## Busca com Sondagem Linear

```
Search("Bob"):
  idx = hash("Bob") % 7 = 2
  slot 2 → "Ana" ≠ "Bob" → sonda slot 3
  slot 3 → "Bob" ✅ → retorna
```

```
Search("Pedro") (não existe):
  idx = hash("Pedro") % 7 = 2
  slot 2 → "Ana" ≠ "Pedro"
  slot 3 → "Bob" ≠ "Pedro"
  slot 4 → "Carlos" ≠ "Pedro"
  slot 5 → VAZIO → não existe na tabela ✅
```

> **Atenção:** A busca para no primeiro slot **vazio**, não em qualquer slot diferente.
> Isso cria um bug clássico na deleção!

---

## O Bug da Deleção

```
Estado: [ ][ ][Ana][Bob][Carlos][ ][ ]

Delete "Bob" (slot 3):
  Solução errada: marcar slot 3 como vazio
  Estado errado: [ ][ ][Ana][ ][Carlos][ ][ ]

Search("Carlos"):
  hash % 7 = 2
  slot 2 → Ana ≠ Carlos
  slot 3 → VAZIO → retorna "não encontrado" ❌ ERRADO!
```

**Solução:** Usar um marcador especial "DELETED" (tombstone) em vez de vazio.

---

## Variações de Probing

| Estratégia | Fórmula | Problema |
|---|---|---|
| **Linear** | `(h + i) % m` | Clustering primário |
| **Quadrática** | `(h + i²) % m` | Clustering secundário |
| **Double Hashing** | `(h1 + i × h2) % m` | Melhor distribuição |

---

## Complexidade com Clustering

| Estado | Busca (média) |
|---|---|
| α = 0.5 (50% cheio) | ≈ 1.5 comparações |
| α = 0.9 (90% cheio) | ≈ 10 comparações |
| α → 1.0 (quase cheio) | → O(N) |

> Por isso o rehashing é **obrigatório** antes de α atingir valores críticos.

---

## Conexões no Vault

- [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]] - contexto geral
- [[02 - Tabelas Hash/Encadeamento Exterior (Chaining)]] - abordagem alternativa
- [[02 - Tabelas Hash/Fator de Carga e Rehashing]] - quando agir para evitar O(N)
