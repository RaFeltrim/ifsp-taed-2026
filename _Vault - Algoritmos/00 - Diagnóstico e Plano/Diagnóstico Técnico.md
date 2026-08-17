---
tags: [diagnóstico, plano, meta]
tipo: diagnóstico
status: referência
criado: 2026-07-27
pontuação: 11/40
---

# 📊 Diagnóstico Técnico - Jul/2026

> Documento de referência. Use para medir sua evolução ao longo das sessões.

## Resultado Geral

| Métrica | Valor |
|---|---|
| Pontuação | **11/40 (27,5%)** |
| Status | Revisão crítica de fundamentos |

---

## Mapeamento de Lacunas

### 🔴 Crítico - Tabelas Hash
- Confusão entre Sondagem Linear e Encadeamento Exterior
- Desconhecimento do Fator de Carga (Load Factor)
- Não domina a degradação para O(N) no pior caso

→ Plano de ação: [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]]

---

### 🔴 Crítico - Grafos e Matrizes
- Erros em representação espacial (Matriz vs Lista de Adjacência)
- Falha na identificação de aplicações de Kruskal, Dijkstra, BFS, DFS
- Não reconhece topologias como DAGs

→ Plano de ação: [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]]

---

### 🟡 Atenção - Árvores
- Falta de clareza nas regras de balanceamento AVL
- Propriedades estruturais de B-Trees confusas
- Aplicação equivocada de Heaps Binários

→ Plano de ação: [[04 - Árvores/AVL Trees - Balanceamento Automático]]

---

### 🟡 Atenção - Estruturas Lineares
- Confusão LIFO (Pilha) vs FIFO (Fila)
- Erros na complexidade de inserção em lista duplamente encadeada

→ Plano de ação: [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]]

---

## Causa Raiz Identificada

> Você aprendeu as **interfaces** antes de entender as **implementações**.
> Sabe o nome, não sabe o comportamento em memória.

**Estratégia de correção:** Ir de baixo para cima.
`Complexidade Big-O → Lineares → Hash → Grafos → Árvores`

Ver: [[MOC - Mapa do Conhecimento]]
