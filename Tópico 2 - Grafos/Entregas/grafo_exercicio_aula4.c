#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

#define INF INT_MAX

// Estrutura do Grafo usando Matriz de Adjacência
typedef struct {
    int num_vertices;
    int **matriz;
} Grafo;

// 1. Função de criação do grafo, passando o número de vértices.
Grafo* criar_grafo(int num_vertices) {
    Grafo* g = (Grafo*)malloc(sizeof(Grafo));
    g->num_vertices = num_vertices;
    
    g->matriz = (int**)malloc(num_vertices * sizeof(int*));
    for (int i = 0; i < num_vertices; i++) {
        g->matriz[i] = (int*)malloc(num_vertices * sizeof(int));
        for (int j = 0; j < num_vertices; j++) {
            g->matriz[i][j] = 0; // 0 indica ausência de aresta
        }
    }
    return g;
}

// 2. Função de adicionar arestas a um grafo (não dirigido)
// e 6. Adicione pesos às arestas nessa representação.
void adicionar_aresta(Grafo* g, int origem, int destino, int peso) {
    if (origem >= 0 && origem < g->num_vertices && destino >= 0 && destino < g->num_vertices) {
        g->matriz[origem][destino] = peso;
        g->matriz[destino][origem] = peso; // Grafo não dirigido (simétrico)
    } else {
        printf("Vértices inválidos!\n");
    }
}

// 3. Função de verificar se existe uma aresta entre um par de vértices.
bool existe_aresta(Grafo* g, int origem, int destino) {
    if (origem >= 0 && origem < g->num_vertices && destino >= 0 && destino < g->num_vertices) {
        return g->matriz[origem][destino] != 0;
    }
    return false;
}

// Bônus: Encontrar a menor distância entre 2 vértices utilizando os pesos.
// Utiliza o Algoritmo de Dijkstra para calcular a menor rota.
void menor_distancia_dijkstra(Grafo* g, int origem, int destino) {
    int *dist = (int*)malloc(g->num_vertices * sizeof(int));
    bool *visitado = (bool*)malloc(g->num_vertices * sizeof(bool));
    int *anterior = (int*)malloc(g->num_vertices * sizeof(int));

    for (int i = 0; i < g->num_vertices; i++) {
        dist[i] = INF;
        visitado[i] = false;
        anterior[i] = -1;
    }

    dist[origem] = 0;

    for (int count = 0; count < g->num_vertices - 1; count++) {
        int min_dist = INF;
        int u = -1;
        
        // Encontra o vértice com a menor distância ainda não visitado
        for (int v = 0; v < g->num_vertices; v++) {
            if (!visitado[v] && dist[v] <= min_dist) {
                min_dist = dist[v];
                u = v;
            }
        }

        if (u == -1 || min_dist == INF) break;
        visitado[u] = true;
        if (u == destino) break; // Otimização: já alcançou o destino

        // Atualiza a distância dos vizinhos do vértice u
        for (int v = 0; v < g->num_vertices; v++) {
            if (!visitado[v] && g->matriz[u][v] != 0 && dist[u] != INF && 
                dist[u] + g->matriz[u][v] < dist[v]) {
                dist[v] = dist[u] + g->matriz[u][v];
                anterior[v] = u;
            }
        }
    }

    if (dist[destino] == INF) {
        printf("Nao existe caminho entre o vertice %d e o vertice %d.\n", origem, destino);
    } else {
        printf("A menor distancia entre o vertice %d e o vertice %d eh: %d\n", origem, destino, dist[destino]);
        
        printf("Caminho percorrido: ");
        int curr = destino;
        int caminho[1000];
        int idx = 0;
        while (curr != -1) {
            caminho[idx++] = curr;
            curr = anterior[curr];
        }
        for (int i = idx - 1; i >= 0; i--) {
            printf("%d", caminho[i]);
            if (i > 0) printf(" -> ");
        }
        printf("\n");
    }

    free(dist);
    free(visitado);
    free(anterior);
}

// Função utilitária para liberar a memória alocada
void liberar_grafo(Grafo* g) {
    for (int i = 0; i < g->num_vertices; i++) {
        free(g->matriz[i]);
    }
    free(g->matriz);
    free(g);
}

int main() {
    printf("--- TAD Grafo Nao Dirigido com Matriz de Adjacencias ---\n\n");
    
    // Criação de um grafo com 5 vértices (0 a 4), equivalentes a 1 a 5 no slide
    int num_vertices = 5;
    Grafo* g = criar_grafo(num_vertices);
    
    // Adição de arestas exatamente conforme a Matriz de Adjacências do Slide:
    // Pesos fictícios inseridos para atender ao requisito "Adicione pesos" e "Bônus de Dijkstra".
    adicionar_aresta(g, 0, 1, 10); // Aresta 1-2
    adicionar_aresta(g, 0, 4, 15); // Aresta 1-5
    adicionar_aresta(g, 1, 2, 10); // Aresta 2-3
    adicionar_aresta(g, 1, 3, 20); // Aresta 2-4
    adicionar_aresta(g, 2, 3, 30); // Aresta 3-4
    adicionar_aresta(g, 3, 4, 25); // Aresta 4-5

    // Verificação de existência de arestas
    printf("Existe aresta entre (0 e 1)? %s\n", existe_aresta(g, 0, 1) ? "Sim" : "Nao");
    printf("Existe aresta entre (0 e 2)? %s\n", existe_aresta(g, 0, 2) ? "Sim" : "Nao");

    // Cálculo da menor distância usando Dijkstra (Desafio Bônus)
    printf("\n--- Teste: Menor Distancia (Dijkstra) ---\n");
    menor_distancia_dijkstra(g, 0, 3);
    
    liberar_grafo(g);
    
    printf("\nExecucao finalizada com sucesso.\n");
    return 0;
}
