---
tags: [MOC, índice, hub]
tipo: mapa-de-conteudo
status: ativo
criado: 2026-07-27
---
# 🧠 Mapa do Conhecimento - Algoritmos & Estruturas de Dados

> Este é o **hub central** do vault. Todas as notas se conectam aqui.
> A rede de links forma a sua **curva de evolução técnica**.

---

## 🗺️ Grafo de Dependências de Aprendizado

```
[Complexidade Big-O]
        │
        ▼
[Estruturas Lineares] ──────────────────────┐
  Arrays, Listas, Pilhas, Filas             │
        │                                   │
        ▼                                   ▼
[Tabelas Hash]                        [Grafos]
  Hash Function                         BFS (usa Fila)
  Colisão / Load Factor                 DFS (usa Pilha)
        │                               Dijkstra, Kruskal
        ▼                                   │
[Árvores]  ◄──────────────────────────────┘
  BST, AVL, B-Tree, Heap
```

> **Regra:** Nunca pule um nível. Cada seta é um pré-requisito real.

---

## 📅 Diário de Atas de Aulas (Documentação Contínua)

> Registro cronológico de todas as aulas da disciplina (Slides + Anotações do Professor + Código em C).

| Aula              | Data        | Tema Principal                                      | Atas & Anotações |
| ----------------- | ----------- | --------------------------------------------------- | ------------------ |
| **Aula 01** | Jul/2026    | Ementa, Big Techs & Pensamento Computacional        | [[00 - Diagnóstico e Plano/Ata_Aula_01_Introducao_e_Ementa]]                   |
| **Aula 02** | 03/Ago/2026 | Revisão em C (Ponteiros, Memória, malloc, Listas) | [[00 - Diagnóstico e Plano/Ata_Aula_02_Revisao_C_Memoria_Ponteiros_Listas]]                   |
| **Aula 03** | 17/Ago/2026 | Árvores Binárias de Busca (ABB) e Árvores AVL    | [[00 - Diagnóstico e Plano/Ata_Aula_03_Arvores_Binarias_ABB_AVL]]                   |

---

## 📚 Módulos do Vault

### 🗺️ Diagnóstico, Planejamento & Design de Apresentações
* [[00 - Diagnóstico e Plano/Ata_Aula_01_Introducao_e_Ementa|Ata da Aula 01 - Introdução e Ementa]]
* [[00 - Diagnóstico e Plano/Ata_Aula_02_Revisao_C_Memoria_Ponteiros_Listas|Ata da Aula 02 - Revisão de C, Memória e Listas]]
* [[00 - Diagnóstico e Plano/Ata_Aula_03_Arvores_Binarias_ABB_AVL|Ata da Aula 03 - Árvores Binárias (ABB e AVL)]]
* [[00 - Diagnóstico e Plano/Guia_Apresentacao_Equipe_LeetCode3|Guia de Apresentação da Equipe - LeetCode #3]]
* [[00 - Diagnóstico e Plano/Engenharia_de_Prompts_e_Design_Editorial_de_Apresentacoes|Relatório: Engenharia de Prompts & Design Editorial Anti-IA]]
* [[00 - Diagnóstico e Plano/Avaliacao_Diagnostica_Gabarito_Comentado|Gabarito Comentado da Avaliação Diagnóstica]]

### 📈 Base Teórica

- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]]

### 🔵 Fase 1 - Estruturas Lineares

- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]]
- [[01 - Estruturas Lineares/Pilhas (Stack - LIFO)]]
- [[01 - Estruturas Lineares/Filas (Queue - FIFO)]]
- [[01 - Estruturas Lineares/Listas Duplamente Encadeadas e Deque]]
- [[01 - Estruturas Lineares/Anotacoes_Aula02_Ponteiros_Memoria_C]]
- [[01 - Estruturas Lineares/Longest Substring Without Repeating Characters - LeetCode 3]]
- [[01 - Estruturas Lineares/RandomizedSet - Operações O(1)]]
- [[01 - Estruturas Lineares/Estudo - Spotify Shuffle e Algoritmos de Anti-Repeticao]]

### 🔴 Fase 2 - Tabelas Hash *(Crítico)*

- [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]]
- [[02 - Tabelas Hash/Encadeamento Exterior (Chaining)]]
- [[02 - Tabelas Hash/Sondagem Linear (Linear Probing)]]
- [[02 - Tabelas Hash/Fator de Carga e Rehashing]]

### 🔴 Fase 3 - Grafos *(Crítico)*

- [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]]
- [[03 - Grafos/BFS - Busca em Largura]]
- [[03 - Grafos/DFS - Busca em Profundidade]]
- [[03 - Grafos/Algoritmo de Dijkstra]]
- [[03 - Grafos/Algoritmo de Kruskal]]
- [[03 - Grafos/DAGs - Grafos Acíclicos Dirigidos]]
- [[03 - Grafos/Pesquisa - Algoritmos de Rotas em Larga Escala]]

### 🟡 Fase 4 - Árvores *(Atenção)*

- [[04 - Árvores/BST - Árvore Binária de Busca]]
- [[04 - Árvores/AVL Trees - Balanceamento Automático]]
- [[04 - Árvores/B-Trees - Estrutura para Disco]]
- [[04 - Árvores/Binary Heaps - Heap Binário]]

---

## 📊 Dashboard de Evolução

| Módulo             | Status       | Confiança | Projeto Prático           |
| ------------------- | ------------ | ---------- | -------------------------- |
| Big-O               | 🔄 Revisando | 🟩🟩⬜⬜⬜ | -                          |
| Estruturas Lineares | 🔄 Revisando | 🟩🟩🟩⬜⬜ | LeetCode 3 + Revisão em C |
| Tabelas Hash        | ❌ Crítico  | ⬜⬜⬜⬜⬜ | Hash Table + Benchmark     |
| Grafos              | ❌ Crítico  | ⬜⬜⬜⬜⬜ | Sistema de Dependências   |
| Árvores            | 🔄 Em Curso  | 🟩🟩🟩⬜⬜ | ABB / AVL (Aula 3)         |

---

## 🔗 Links Rápidos por Algoritmo

| Algoritmo      | Estrutura Base    | Complexidade | Nota |
| -------------- | ----------------- | ------------ | ---- |
| BFS            | Fila (Queue)      | O(V+E)       | [[03 - Grafos/BFS - Busca em Largura]]     |
| DFS            | Pilha (Stack)     | O(V+E)       | [[03 - Grafos/DFS - Busca em Profundidade]]     |
| Dijkstra       | Heap Mínimo      | O((V+E)logV) | [[03 - Grafos/Algoritmo de Dijkstra]]     |
| Kruskal        | Union-Find + Sort | O(E log E)   | [[03 - Grafos/Algoritmo de Kruskal]]     |
| Inserção AVL | AVL Tree          | O(log N)     | [[04 - Árvores/AVL Trees - Balanceamento Automático]]     |
| Busca em Hash  | Hash Table        | O(1) avg     | [[02 - Tabelas Hash/Fator de Carga e Rehashing]]     |
