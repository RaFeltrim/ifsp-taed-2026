---
tags: [hash-table, fase-2, crítico, arquitetura]
tipo: conceito
status: lacuna-crítica
pré-requisito: [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]]
próximo: [[02 - Tabelas Hash/Encadeamento Exterior (Chaining)]]
criado: 2026-07-27
---

# 🔴 Tabelas Hash - Arquitetura Interna

> **Módulo Crítico.** A ideia central: transformar uma chave qualquer em um índice de array.

## O Problema que Hash Tables Resolvem

Queremos buscar um valor por chave em **O(1)** - sem percorrer toda a estrutura.

```
Problema:  dado "Rafael", encontre a nota dele.
Solução ingênua:  percorrer lista até achar "Rafael" → O(N)
Solução com Hash: calcular onde "Rafael" está armazenado → O(1)
```

---

## Arquitetura em 3 Camadas

```
      CHAVE          FUNÇÃO HASH          ÍNDICE        ARRAY INTERNO
   "Rafael"    →    hash("Rafael")   →      3       →   [slot 3: valor]
   "Carlos"    →    hash("Carlos")   →      7       →   [slot 7: valor]
   "Ana"       →    hash("Ana")      →      1       →   [slot 1: valor]
```

### 1. Função Hash

Transforma a chave em um número inteiro e depois em um índice válido:

```
índice = hash(chave) % tamanho_da_tabela

Exemplo:
  hash("Rafael") = 1234567
  1234567 % 10 = 7   → armazena no slot 7
```

**Propriedades de uma boa função hash:**
- Determinística: mesma chave → sempre mesmo índice
- Uniforme: distribui bem entre todos os slots
- Rápida: deve ser O(1) de calcular

---

### 2. O Array Interno

```
Tabela com m = 10 slots:

índice: [ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ]
         NULL  "Ana" NULL  "Raf" NULL  NULL  NULL  "Car" NULL  NULL
```

---

### 3. Tratamento de Colisão

> **Colisão:** duas chaves diferentes geram o mesmo índice.

```
hash("Rafael") % 10 = 3
hash("Marcos") % 10 = 3   ← COLISÃO!
```

Não é uma falha - é um comportamento **matematicamente inevitável** (Princípio da Gaiola de Pombo).

Estratégias:
- [[02 - Tabelas Hash/Encadeamento Exterior (Chaining)]] - cada slot vira uma lista
- [[02 - Tabelas Hash/Sondagem Linear (Linear Probing)]] - busca o próximo slot livre

---

## Complexidade Geral

| Operação | Caso Médio | Pior Caso |
|---|---|---|
| `insert(key, val)` | **O(1)** | O(N) |
| `search(key)` | **O(1)** | O(N) |
| `delete(key)` | **O(1)** | O(N) |

> O pior caso **O(N)** acontece quando todas as chaves colidem no mesmo slot.
> Ver: [[02 - Tabelas Hash/Fator de Carga e Rehashing]]

---

## Analogia

> Imagine um arquivo físico com 10 gavetas (0-9).
> Cada documento tem um código. Você pega os últimos dois dígitos do código e abre aquela gaveta diretamente.
> Se dois documentos caem na mesma gaveta → é uma colisão. Você precisa de uma estratégia.

---

## Conexões no Vault

- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]] - array interno + lista no chaining
- [[02 - Tabelas Hash/Encadeamento Exterior (Chaining)]] - estratégia 1 de colisão
- [[02 - Tabelas Hash/Sondagem Linear (Linear Probing)]] - estratégia 2 de colisão
- [[02 - Tabelas Hash/Fator de Carga e Rehashing]] - quando O(1) vira O(N)
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] - referência de complexidade
