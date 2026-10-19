#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_CHARS 26

// Variáveis Globais para representar o Grafo Direcionado e o In-Degree
bool adj[MAX_CHARS][MAX_CHARS];
int in_degree[MAX_CHARS];
bool present[MAX_CHARS];

// Função para inicializar/limpar o grafo
void init_graph() {
    for (int i = 0; i < MAX_CHARS; i++) {
        for (int j = 0; j < MAX_CHARS; j++) {
            adj[i][j] = false;
        }
        in_degree[i] = 0;
        present[i] = false;
    }
}

// Extrai as arestas (dependências) comparando palavras adjacentes
bool build_graph(char** words, int numWords) {
    // 1. Marca todos os caracteres que aparecem no dicionário
    for (int i = 0; i < numWords; i++) {
        for (int j = 0; words[i][j] != '\0'; j++) {
            present[words[i][j] - 'a'] = true;
        }
    }

    // 2. Compara pares de palavras adjacentes para encontrar a primeira diferença
    for (int i = 0; i < numWords - 1; i++) {
        char* w1 = words[i];
        char* w2 = words[i + 1];
        int len1 = strlen(w1);
        int len2 = strlen(w2);
        int minLen = len1 < len2 ? len1 : len2;
        bool found = false;

        for (int j = 0; j < minLen; j++) {
            if (w1[j] != w2[j]) {
                int u = w1[j] - 'a';
                int v = w2[j] - 'a';
                // Adiciona uma aresta do caractere u para o v
                if (!adj[u][v]) {
                    adj[u][v] = true;
                    in_degree[v]++;
                }
                found = true;
                break;
            }
        }
        // Caso de erro: Prefixo maior vindo antes de um menor (ex: "abc" antes de "ab")
        // Isso é uma inconsistência no dicionário
        if (!found && len1 > len2) {
            return false;
        }
    }
    return true;
}

// Algoritmo de Ordenação Topológica (Kahn's Algorithm)
char* alien_order(char** words, int numWords) {
    init_graph();
    
    if (!build_graph(words, numWords)) {
        return strdup(""); // Dicionário inválido
    }

    // Fila para o BFS
    int queue[MAX_CHARS];
    int front = 0, rear = 0;
    
    int count = 0; // Quantidade de letras únicas que existem no grafo
    for (int i = 0; i < MAX_CHARS; i++) {
        if (present[i]) {
            count++;
            // Vértices sem nenhuma dependência (in-degree == 0) entram na fila
            if (in_degree[i] == 0) {
                queue[rear++] = i;
            }
        }
    }

    // String que armazenará o resultado
    char* result = (char*)malloc((count + 1) * sizeof(char));
    int resIdx = 0;

    // Processa a fila (BFS)
    while (front < rear) {
        int u = queue[front++];
        result[resIdx++] = u + 'a';

        // Reduz o in-degree dos vizinhos
        for (int v = 0; v < MAX_CHARS; v++) {
            if (adj[u][v]) {
                in_degree[v]--;
                // Se zerar o in-degree, adiciona na fila
                if (in_degree[v] == 0) {
                    queue[rear++] = v;
                }
            }
        }
    }

    result[resIdx] = '\0';

    // Se o resultado não contém todas as letras únicas, há um ciclo (ordem inválida)
    if (resIdx < count) {
        free(result);
        return strdup("");
    }

    return result;
}

int main() {
    printf("--- Alien Dictionary (Topological Sort) ---\n\n");

    // Exemplo clássico do LeetCode 269
    char* words[] = {"wrt", "wrf", "er", "ett", "rftt"};
    int numWords = 5;

    printf("Dicionario Alienigena ordenado:\n");
    for (int i = 0; i < numWords; i++) {
        printf("  %s\n", words[i]);
    }

    char* order = alien_order(words, numWords);
    
    if (strlen(order) > 0) {
        printf("\nOrdem deduzida das letras: \"%s\"\n", order);
    } else {
        printf("\nOrdem invalida (ciclo detectado ou inconsistencia no dicionario).\n");
    }

    free(order);
    printf("\nExecucao finalizada com sucesso.\n");
    return 0;
}
