---
tags: [plano, mentoria, estratégia]
tipo: plano-de-ação
status: ativo
criado: 2026-07-27
fases: 4
---

# 📋 Plano de Mentoria Estratégico

> Documento vivo. Atualizado a cada sessão de mentoria.

## Filosofia

> "A estrutura de dados certa resolve o problema.
>  A análise de complexidade certa escolhe a estrutura."

**Regra de ouro:** Você constrói. O mentor orienta. O aprendizado acontece no processo.

---

## Sequência de Fases

```
Fase 1: Fundamentos Lineares
    └─ Pré-requisito de tudo
Fase 2: Tabelas Hash (Crítico)
    └─ Depende de: arrays, funções hash
Fase 3: Grafos (Crítico)
    └─ Depende de: Pilhas (DFS) + Filas (BFS) + Heaps (Dijkstra)
Fase 4: Árvores (Atenção)
    └─ Depende de: BST → AVL → B-Tree; Heap separado
```

---

## Fase 1 - Estruturas Lineares

**Objetivo:** Dominar as estruturas que são a base de todos os algoritmos.

| Tópico | Nota | Complexidade-chave |
|---|---|---|
| Arrays vs Listas | [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]] | O(1) acesso vs O(N) busca |
| Pilha (LIFO) | [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]] | O(1) push/pop |
| Fila (FIFO) | [[01 - Estruturas Lineares/Filas (Queue - FIFO)]] | O(1) enqueue/dequeue |
| Deque / Dupla | [[01 - Estruturas Lineares/Listas Duplamente Encadeadas e Deque]] | O(1) nas pontas |

**Critério de conclusão:** Implementar Pilha e Fila do zero, sem consulta.

---

## Fase 2 - Tabelas Hash

**Objetivo:** Entender colisão como comportamento esperado e gerenciável.

| Tópico | Nota |
|---|---|
| Arquitetura interna | [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]] |
| Encadeamento | [[02 - Tabelas Hash/Encadeamento Exterior (Chaining)]] |
| Sondagem Linear | [[02 - Tabelas Hash/Sondagem Linear (Linear Probing)]] |
| Load Factor | [[02 - Tabelas Hash/Fator de Carga e Rehashing]] |

**Projeto:** Hash Table com encadeamento + benchmark por load factor.

---

## Fase 3 - Grafos

**Objetivo:** Nunca mais confundir representação com algoritmo.

| Tópico | Nota |
|---|---|
| Representações | [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]] |
| BFS | [[03 - Grafos/BFS - Busca em Largura]] |
| DFS | [[03 - Grafos/DFS - Busca em Profundidade]] |
| Dijkstra | [[03 - Grafos/Algoritmo de Dijkstra]] |
| Kruskal | [[03 - Grafos/Algoritmo de Kruskal]] |
| DAGs | [[03 - Grafos/DAGs - Grafos Acíclicos Dirigidos]] |

**Projeto:** Modelar dependências de tarefas como DAG + ordenação topológica.

---

## Fase 4 - Árvores

| Tópico | Nota |
|---|---|
| BST | [[04 - Árvores/BST - Árvore Binária de Busca]] |
| AVL | [[04 - Árvores/AVL Trees - Balanceamento Automático]] |
| B-Tree | [[04 - Árvores/B-Trees - Estrutura para Disco]] |
| Heap | [[04 - Árvores/Binary Heaps - Heap Binário]] |

**Projeto:** AVL com balanceamento automático + MaxHeap.

---

## Protocolo por Sessão

1. **Dry-run** no papel / pseudocódigo
2. Você **implementa**
3. **Code review** conjunto
4. **Benchmark** experimental (quando aplicável)

Ver diagnóstico: [[00 - Diagnóstico e Plano/Diagnóstico Técnico]]
