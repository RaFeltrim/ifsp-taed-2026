---
tags: [grafos, DAG, topológico, fase-3, crítico]
tipo: conceito
status: lacuna-crítica
pré-requisito: [[03 - Grafos/DFS - Busca em Profundidade]]
próximo: [[04 - Árvores/BST - Árvore Binária de Busca]]
criado: 2026-07-27
---

# 🔴 DAGs - Grafos Acíclicos Dirigidos

> **Directed Acyclic Graph** - Dígrafo sem ciclos.
> A estrutura por trás de compiladores, pipelines, e sistemas de dependência.

## Definição

```
DAG = Grafo Dirigido + Sem Ciclos

Dirigido: arestas têm direção (A → B ≠ B → A)
Acíclico: não existe caminho que volta ao ponto de origem
```

```
DAG válido:         NÃO é DAG (tem ciclo):
A → B → D           A → B
↓       ↑           ↑   ↓
C ──────┘           └── C
```

---

## Por que DAGs São Especiais?

1. **Sempre têm ordenação topológica** (ao contrário de grafos com ciclos)
2. **Têm pelo menos um nó fonte** (sem arestas de entrada)
3. **Têm pelo menos um nó sorvedouro** (sem arestas de saída)
4. **Permitem programação dinâmica** em problemas sobre caminhos

---

## Ordenação Topológica

> Ordena os vértices de forma que para toda aresta (u → v), u aparece antes de v.

**Aplicação direta:** Se B depende de A, A deve ser processado antes de B.

### Algoritmo via DFS (Pós-ordem)

```
ordenação_topológica(grafo):
    visitados = conjunto vazio
    pilha_resultado = Pilha()

    para cada vértice v não visitado:
        DFS_topológico(v, visitados, pilha_resultado)

    retorna pilha_resultado (do topo para baixo)

DFS_topológico(v, visitados, pilha):
    visitados.add(v)
    para cada vizinho w de v:
        se w não visitado:
            DFS_topológico(w, visitados, pilha)
    pilha.push(v)  ← empilha APÓS processar todos os descendentes
```

---

## Dry-Run - Sistema de Dependências

```
Tarefas: instalar pacotes
  numpy depende de: nada
  pandas depende de: numpy
  matplotlib depende de: numpy
  sklearn depende de: numpy, scipy
  scipy depende de: numpy

DAG:
  numpy → pandas
  numpy → matplotlib
  numpy → scipy → sklearn
  numpy → sklearn

DFS a partir de numpy:
  processa numpy → todos dependentes → empilha numpy por último? 
  
  Não! Vamos de sklearn para numpy:
  
  DFS(sklearn):
    vizinhos: numpy, scipy (não visitados)
    DFS(numpy): sem vizinhos não visitados → empilha numpy
    DFS(scipy): vizinho numpy (visitado) → empilha scipy
    empilha sklearn

  DFS(pandas):
    vizinho numpy (visitado) → empilha pandas

  DFS(matplotlib):
    vizinho numpy (visitado) → empilha matplotlib

Pilha (topo→base): [matplotlib, pandas, sklearn, scipy, numpy]
Ordem de instalação: numpy → scipy → sklearn → pandas → matplotlib ✅
```

---

## Detecção de Ciclo em Grafo Dirigido

```
Durante DFS, mantemos três estados:
  BRANCO = não visitado
  CINZA  = visitado, ainda na pilha de recursão (em progresso)
  PRETO  = visitado, recursão completa

Se durante DFS encontramos um nó CINZA → CICLO DETECTADO!
(Voltamos a um ancestral na pilha atual)
```

---

## Aplicações de DAGs

| Domínio | Aplicação |
|---|---|
| **Compiladores** | Ordem de compilação de módulos |
| **Gerenciadores de pacotes** | npm, pip, apt resolvem DAGs |
| **Makefiles** | Dependências de build |
| **Workflows** | Pipelines de dados (Airflow, Luigi) |
| **Spreadsheets** | Células dependentes de outras células |
| **Git** | Histórico de commits é um DAG |

---

## Conexões no Vault

- [[03 - Grafos/DFS - Busca em Profundidade]] - base da ordenação topológica
- [[03 - Grafos/Grafos - Representações (Matriz vs Lista)]] - como representar o DAG
- [[03 - Grafos/BFS - Busca em Largura]] - algoritmo de Kahn usa BFS para topologia
- [[04 - Árvores/BST - Árvore Binária de Busca]] - próxima fase
