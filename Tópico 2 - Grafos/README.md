# 🌐 Tópico 2 — Teoria dos Grafos & Algoritmos de Percurso

Módulo correspondente à **Aula 4** da disciplina de Tópicos em Algoritmos e Estruturas de Dados, focando na modelagem formal de redes, estruturas de dados para representação de grafos em C e algoritmos de travessia.

---

## 📌 Fundamentos Teóricos

Um grafo $G = (V, E)$ é composto por um conjunto não-vazio de vértices $V$ e um conjunto de arestas $E \subseteq V \times V$.

### Formas de Representação Computacional em C
1. **Matriz de Adjacência:**
   * Matriz $V \times V$ onde $M[u][v]$ indica a presença (ou peso) da aresta entre $u$ e $v$.
   * Vantagem: Verificação de adjacência em tempo constante $\mathcal{O}(1)$.
   * Desvantagem: Consumo de memória quadrático $\mathcal{O}(V^2)$, ineficiente para grafos esparsos ($|E| \ll |V|^2$).
2. **Lista de Adjacência:**
   * Vetor de listas encadeadas onde cada vértice $u$ aponta para os seus vizinhos diretos.
   * Vantagem: Consumo de memória linear $\mathcal{O}(|V| + |E|)$, padrão ouro para grafos reais e esparsos.

### Algoritmos Fundamentais de Busca
* **Busca em Largura (BFS - Breadth-First Search):** Explora nível por nível utilizando uma **Fila (Queue - FIFO)**. Fundamental para cálculo de menores distâncias em grafos não-ponderados.
* **Busca em Profundidade (DFS - Depth-First Search):** Explora os ramos até a profundidade máxima utilizando uma **Pilha (Stack - LIFO)** ou recursão. Base para detecção de ciclos, componentes fortemente conexos e ordenação topológica.

---

## 📂 Organização dos Arquivos do Módulo

```text
📁 Tópico 2 - Grafos/
│
├── 📄 README.md                                             # Este documento de referência teórica
│
├── 📁 Entregas/                                             # [ARQUIVO PRONTO PARA SUBMISSÃO]
│   └── 💻 grafo_exercicio_aula4.c                           # Implementação completa do grafo da Aula 4
│
├── 📁 Exercícios e Laboratórios/
│   └── 💻 grafo_exercicio_aula4.c                           # Código-fonte em C com testes e percursos
│
└── 📁 Material de Apoio/
    └── 📑 TAED - Grafos.pdf                                 # Slides oficiais da Aula 4 do Prof. Bianchi
```

---

## 🛠️ Como Compilar e Executar a Entrega em C

```bash
gcc -Wall -Wextra -O2 "Exercícios e Laboratórios/grafo_exercicio_aula4.c" -o grafo
./grafo
```
