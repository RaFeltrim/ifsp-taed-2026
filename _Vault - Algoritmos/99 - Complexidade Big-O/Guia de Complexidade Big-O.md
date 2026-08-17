---
tags: [big-o, complexidade, fundamento, teoria]
tipo: referência
status: fundamento-obrigatório
pré-requisito-de: tudo
criado: 2026-07-27
---

# 📈 Guia de Complexidade Big-O

> **Pré-requisito de TUDO.** Sem isso, você não consegue comparar estruturas de dados.

## O que é Big-O?

Big-O descreve o **comportamento assintótico** de um algoritmo - como o tempo ou espaço
cresce em função do tamanho da entrada `N`, ignorando constantes.

> Não medimos segundos. Medimos **crescimento relativo**.

---

## Hierarquia de Complexidades

```
O(1) < O(log N) < O(N) < O(N log N) < O(N²) < O(2^N) < O(N!)
 ↑                                                              ↑
melhor                                                       pior
```

| Notação | Nome | Exemplo |
|---|---|---|
| O(1) | Constante | Acesso a array por índice |
| O(log N) | Logarítmica | Busca binária, operações em AVL |
| O(N) | Linear | Percorrer lista encadeada |
| O(N log N) | Linearítmica | Merge Sort, Heap Sort |
| O(N²) | Quadrática | Bubble Sort, busca em grafo denso ingênua |
| O(2^N) | Exponencial | Subconjuntos, força bruta combinatória |

---

## Regras de Simplificação

### 1. Descarte constantes
```
O(3N) → O(N)
O(500) → O(1)
```

### 2. Descarte termos menores
```
O(N² + N) → O(N²)
O(N log N + N) → O(N log N)
```

### 3. Soma vs. Multiplicação
```
# Loops sequenciais → SOMA
for i in range(N):   # O(N)
    ...
for j in range(M):   # O(M)
    ...
# Total: O(N + M)

# Loops aninhados → MULTIPLICAÇÃO
for i in range(N):
    for j in range(M):  # O(N × M)
        ...
# Total: O(N·M)
```

---

## Big-O por Estrutura de Dados

| Estrutura | Busca | Inserção | Remoção | Espaço |
|---|---|---|---|---|
| Array | O(N) | O(N) | O(N) | O(N) |
| Lista Encadeada | O(N) | O(1)* | O(1)* | O(N) |
| Pilha / Fila | O(N) | O(1) | O(1) | O(N) |
| Hash Table (avg) | O(1) | O(1) | O(1) | O(N) |
| Hash Table (pior) | O(N) | O(N) | O(N) | O(N) |
| BST (balanceada) | O(log N) | O(log N) | O(log N) | O(N) |
| BST (degenerada) | O(N) | O(N) | O(N) | O(N) |
| AVL Tree | O(log N) | O(log N) | O(log N) | O(N) |
| Heap Binário | O(N) | O(log N) | O(log N) | O(N) |
| Heap - peek | O(1) | - | - | - |

> *Com ponteiro de cauda/cabeça

---

## Análise de Caso

Sempre especifique **qual caso** você está analisando:

| Caso | Significado | Exemplo em Hash |
|---|---|---|
| **Melhor caso** | Entrada mais favorável | Chave no primeiro slot |
| **Caso médio** | Comportamento esperado | Distribuição uniforme |
| **Pior caso** | Entrada mais desfavorável | Todas as chaves colidem |

> Em entrevistas e disciplinas, o **pior caso** é o mais relevante.

---

## Complexidade de Espaço

Não é só o tempo que importa. Espaço também tem Big-O:

```
# O(1) espaço extra - variáveis simples
soma = 0
for i in range(N):
    soma += i

# O(N) espaço extra - estrutura proporcional à entrada
resultado = []
for i in range(N):
    resultado.append(i)

# O(V²) espaço - Matriz de Adjacência de grafo com V vértices
matriz = [[0]*V for _ in range(V)]
```

---

## Links Relacionados

- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]] - onde O(1) vs O(N) aparecem
- [[02 - Tabelas Hash/Fator de Carga e Rehashing]] - quando O(1) vira O(N)
- [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]] - O(V²) vs O(V+E)
- [[04 - Árvores/AVL Trees - Balanceamento Automático]] - garantia de O(log N)
