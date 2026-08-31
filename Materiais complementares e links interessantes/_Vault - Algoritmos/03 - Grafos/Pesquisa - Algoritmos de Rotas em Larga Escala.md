---
tags: [grafos, dijkstra, a-star, google-maps, uber, entrevista, big-tech, caso-real]
tipo: pesquisa-aprofundada
status: ativo
criado: 2026-07-27
empresa: [Google, Uber, Lyft, DoorDash]
---

# 🗺️ Pesquisa Aprofundada: Algoritmos de Roteamento em Larga Escala (Google Maps & Uber)

> **Contexto:** Trabalho prático e estudo de caso real de processo seletivo em Big Techs.
> **Tema:** Solução de Menor Caminho em Grafos (Shortest Path Problems) — do Dijkstra básico a Hierarquias de Contração.

---

## 🌐 1. Abstração Teórica & Modelagem de Domínio

No mundo real, o sistema de navegação precisa representar o tráfego global em uma estrutura computacional rápida e eficiente.

### O Grafo Espacial $G = (V, E, w)$

```
MUNDO REAL                                MODELAGEM EM COMPUTABILIDADE
Cruzamentos / Intersecções / Edifícios ──► Vértices (V) / Nós (com coordenadas lat, lon)
Trechos de Ruas / Avenidas / Vias      ──► Arestas Dirigidas (E)
Tempo estimado de viagem (ETA)        ──► Peso da Aresta w(u, v) (dinâmico)
```

- **Grafo Dirigido (Dígrafo):** Essencial porque vias urbanas possuem sentido (mão única vs. mão dupla).
- **Grafo Esparso:** O número de arestas $E$ é pequeno em relação a $V^2$. Na prática, um cruzamento conecta-se a 3 a 5 vias ($E \approx 3V$ a $4V$).
- **Pesos Dinâmicos:** $w(u, v) = \frac{\text{distância}}{\text{velocidade média atual}}$. O peso muda a cada segundo com telemetria de trânsito.

---

## ⚖️ 2. A Evolução Algorítmica: Do Teórico ao Sistema de Produção

### Por que o Dijkstra Puro Falha em Escala Global?

O Dijkstra explora vértices de forma **radial** (em forma de círculo concêntrico em todas as direções). 

```
Busca com Dijkstra (Círculo cego):           Busca com A* (Direcionada):
       ( Origem )                                 ( Origem )
     ↙     ↓     ↘                                   ↘
   ◯       ◯       ◯                                  ◯  →  →  ( Destino )
 ↙   ↓   ↘ │ ↙   ↓   ↘
◯    ◯    ◯ ◯   ◯    (Destino)
```

Para ir de São Paulo ao Rio de Janeiro, o Dijkstra puro avaliaria estradas na direção de Curitiba simplesmente porque a distância percorrida até lá é pequena. Em um grafo com centenas de milhões de nós, isso resulta em tempo de resposta inaceitável ($> 10$ segundos).

---

## 📊 Tabela Comparativa de Complexidade & Trade-offs

| Algoritmo | Estrutura de Dados Base | Complexidade de Tempo (Pior Caso) | Complexidade de Espaço | Uso Prático / Aplicação |
|---|---|---|---|---|
| **BFS (Busca em Largura)** | Fila (FIFO) | $O(V + E)$ | $O(V)$ | Grafos sem peso (menor número de conexões/trocas de ônibus). |
| **Dijkstra Clássico** | Array Simples | $O(V^2)$ | $O(V)$ | Grafos densos pequenos sem heap. |
| **Dijkstra Otimizado** | Heap Mínimo (Priority Queue) | $O((V + E) \log V)$ | $O(V + E)$ | Padrão acadêmico para menor caminho com pesos não-negativos. |
| **A* (A-Star)** | MinHeap + Função Heurística $h(n)$ | $O(E)$ (melhor) / $O((V+E) \log V)$ | $O(V)$ | Roteamento com coordenadas geográficas (linha reta/Haversine). |
| **Contraction Hierarchies (CH)** | Grafo Pré-processado + Dijkstra Bidirecional | $O(\log V)$ por consulta | $O(V + E')$ extra | **Produção real** (Google Maps, OSRM) em grafos continentais. |

---

## 🎯 3. Desafios Reais Utilizados em Entrevistas de Big Techs

Analisamos as questões mais frequentes cobradas em entrevistas de codificação e arquitetura no Google, Uber e Lyft:

---

### 🧩 Desafio 1: Network Delay Time (LeetCode 743 — Nível Médio)
> **Empresas:** Google, Amazon, Uber

#### Enunciado Sintético
Você recebe uma rede de $N$ nós rotulados de $1$ a $N$, e uma lista de tempos de transmissão `times[i] = (u, v, w)` representando o tempo $w$ para um sinal ir de $u$ até $v$. Dado o nó de origem $K$, determine quanto tempo levará para que **todos** os nós recebam o sinal. Se for impossível, retorne $-1$.

#### Modelo da Solução (Dijkstra)
```python
import heapq
from collections import defaultdict

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    # 1. Construir Lista de Adjacência: O(E)
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # 2. Min-Heap: armazena tuplas (tempo_acumulado, no)
    pq = [(0, k)]
    dist = {}
    
    while pq:
        time, u = heapq.heappop(pq)
        
        if u in dist:
            continue
        dist[u] = time
        
        for v, w in graph[u]:
            if v not in dist:
                heapq.heappush(pq, (time + w, v))
                
    # Se nem todos os nós foram alcançados, retorna -1
    return max(dist.values()) if len(dist) == n else -1
```

- **Complexidade de Tempo:** $O(E \log V)$ — cada aresta é processada e inserida na MinHeap.
- **Complexidade de Espaço:** $O(V + E)$ — armazenamento do grafo e distâncias.

---

### 🧩 Desafio 2: Bus Routes / Redes de Transbordo (LeetCode 815 — Nível Difícil)
> **Empresas:** Uber, DoorDash, Lyft

#### Enunciado Sintético
Você recebe um conjunto de rotas de ônibus `routes[i]` com as paradas de cada linha. Você quer ir da parada `source` até `target`. Qual o **menor número de ônibus** que você precisa pegar?

#### O Pulo do Gato (Transformação de Domínio)
Modelar as paradas como nós gera um grafo gigante. O segredo usado em entrevistas é inverter a abstração: **as rotas de ônibus são os Vértices**, e duas rotas têm uma Aresta se compartilham pelo menos uma parada em comum!

```text
Grafos de Paradas (Gigante) ──► Transformação ──► Grafo de Linhas de Ônibus (Pequeno)
Usa BFS no grafo de linhas para encontrar o menor número de trocas de ônibus em O(V_rotas + E_rotas).
```

---

### 🧩 Desafio 3: Cheapest Flights Within K Stops / Restrição de Estado (LeetCode 787 — Nível Difícil)
> **Empresas:** Google, Airbnb, Amazon

#### Enunciado Sintético
Encontrar o voo mais barato de `src` para `dst` com no máximo `K` escalas.

#### Por que o Dijkstra Puro Falha Aqui?
O Dijkstra ganancioso pode descartar um caminho que é mais caro inicialmente, mas que usaria menos escalas e chegaria ao destino dentro do limite $K$.

#### Solução Otimizada: Dijkstra com Estado Expandido $(u, \text{stops})$ ou Bellman-Ford
- **Estado:** Em vez de `dist[u]`, armazenamos `dist[u][stops]`.
- **Complexidade com Bellman-Ford (DP):** $O(K \cdot E)$ tempo e $O(V)$ espaço.

---

## 🏛️ 4. Arquitetura de Produção: Como o Google Maps Funciona em Larga Escala

Em uma pergunta de **System Design (Design de Sistemas)** em Big Techs, a resposta esperada não é "eu rodo o Dijkstra". A resposta sênior envolve **3 Pilares**:

1. **Particionamento Espacial (Indexing):**
   O planeta é particionado em células usando bibliotecas como **Google S2 Geometry** ou **H3 (Uber)** (indexação por hexágonos). As consultas ocorrem dentro da célula e células vizinhas.

2. **Hierarquias de Contração (Contraction Hierarchies - CH):**
   Nós insignificantes (ruas residenciais) são "contraídos" em fase de pré-processamento, criando **atalhos** (shortcut edges). Uma busca de longa distância avalia apenas a rede principal de rodovias.

3. **Cálculo de ETA em Tempo Real:**
   Fluxos de eventos via **Apache Kafka** atualizam os pesos das arestas dinamicamente com base no GPS dos celulares dos motoristas.

---

## 🔗 Links Relacionados no Vault

- [[03 - Grafos/Algoritmo de Dijkstra]] — base teórica e MinHeap
- [[03 - Grafos/BFS - Busca em Largura]] — menor caminho sem pesos
- [[03 - Grafos/Grafos - Representação (Matriz vs Lista)]] — análise espacial O(V+E)
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]] — análise assintótica
