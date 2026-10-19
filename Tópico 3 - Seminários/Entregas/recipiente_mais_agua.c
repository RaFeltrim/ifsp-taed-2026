/**
 * ============================================================================
 * INSTITUTO FEDERAL DE SÃO PAULO (IFSP) - CAMPUS SÃO CARLOS
 * DISCIPLINA: Tópicos em Algoritmos e Estruturas de Dados (TAED)
 * PROFESSOR:  Prof. Dr. Rodrigo Elias Bianchi
 * ALUNO:      Rafael Feltrim
 * 
 * TEMA:       Recipiente com Mais Água (Container With Most Water)
 * DESAFIO:    LeetCode #11
 * 
 * DESCRIÇÃO DO PROBLEMA:
 * Dado um array de alturas 'height' com n números inteiros positivos, cada elemento
 * representa uma linha vertical nas coordenadas (i, height[i]). Duas linhas
 * juntamente com o eixo x formam um recipiente que pode armazenar água.
 * O objetivo é encontrar duas linhas que maximizem a área retangular de água retida:
 * 
 *             Área = min(height[i], height[j]) * (j - i),  onde j > i
 * 
 * ABORDAGENS IMPLEMENTADAS:
 * 1. Força Bruta (Brute Force):
 *    - Testa todas as combinações de pares (i, j) com 2 loops aninhados.
 *    - Complexidade de Tempo: O(N^2)
 *    - Complexidade de Espaço: O(1)
 * 
 * 2. Dois Ponteiros (Two Pointers - Padrão Ouro de Entrevistas Big Tech):
 *    - Inicializa um ponteiro no início (left = 0) e outro no fim (right = n - 1).
 *    - A área é limitada pela menor das duas alturas.
 *    - Move sempre o ponteiro que aponta para a menor altura, pois manter a menor
 *      altura e diminuir a largura nunca resultará em ganho.
 *    - Complexidade de Tempo: O(N)
 *    - Complexidade de Espaço: O(1)
 * 
 * TESTES E VALIDAÇÕES:
 * - Casos de borda (vazio, tamanho < 2)
 * - Array estritamente crescente e estritamente decrescente
 * - Array com valores constantes/repetidos
 * - Casos canônicos de teste do LeetCode
 * - Benchmark comparativo de tempo e operações
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Função auxiliar para retornar o menor entre dois inteiros
static inline int min_val(int a, int b) {
    return (a < b) ? a : b;
}

// Função auxiliar para retornar o maior entre dois inteiros
static inline int max_val(int a, int b) {
    return (a > b) ? a : b;
}

// ============================================================================
// 1. SOLUÇÃO FORÇA BRUTA (BRUTE FORCE) - O(N^2)
// ============================================================================
long long max_area_forca_bruta(const int height[], int n, unsigned long long *ops) {
    if (ops) *ops = 0;
    if (n < 2) return 0;

    long long max_area = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (ops) (*ops)++;
            int h = min_val(height[i], height[j]);
            int w = j - i;
            long long area = (long long)h * w;
            if (area > max_area) {
                max_area = area;
            }
        }
    }

    return max_area;
}

// ============================================================================
// 2. SOLUÇÃO DOIS PONTEIROS (TWO POINTERS) - O(N)
// ============================================================================
long long max_area_two_pointers(const int height[], int n, unsigned long long *ops) {
    if (ops) *ops = 0;
    if (n < 2) return 0;

    int left = 0;
    int right = n - 1;
    long long max_area = 0;

    while (left < right) {
        if (ops) (*ops)++;
        int h = min_val(height[left], height[right]);
        int w = right - left;
        long long current_area = (long long)h * w;

        if (current_area > max_area) {
            max_area = current_area;
        }

        // Decisão gulosa ótima: avança o ponteiro de menor altura
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return max_area;
}

// ============================================================================
// FUNÇÃO UTILITÁRIA DE TESTES E RELATÓRIO
// ============================================================================
void executar_caso_teste(const char* descricao, const int height[], int n, long long esperado) {
    unsigned long long ops_fb = 0, ops_tp = 0;
    long long res_fb = max_area_forca_bruta(height, n, &ops_fb);
    long long res_tp = max_area_two_pointers(height, n, &ops_tp);

    printf("----------------------------------------------------------------------------\n");
    printf("Cenário: %s\n", descricao);
    printf("Entrada: [");
    for (int i = 0; i < n && i < 10; i++) {
        printf("%d%s", height[i], (i == n - 1 || i == 9) ? "" : ", ");
    }
    if (n > 10) printf("... (total %d itens)", n);
    printf("]\n");

    printf("  -> Força Bruta O(N^2):     Área = %lld (Comparações: %llu)\n", res_fb, ops_fb);
    printf("  -> Two Pointers O(N):      Área = %lld (Iterações:   %llu)\n", res_tp, ops_tp);
    
    if (esperado >= 0) {
        printf("  -> Esperado pelo LeetCode: Área = %lld [%s]\n", esperado, (res_tp == esperado) ? "SUCESSO" : "FALHA");
    }
}

// ============================================================================
// MAIN: SUÍTE DE TESTES E BENCHMARK EXPERIMENTAL
// ============================================================================
int main() {
    printf("============================================================================\n");
    printf("  IFSP SCL - TAED: RECIPIENTE COM MAIS ÁGUA (LEETCODE #11)\n");
    printf("============================================================================\n\n");

    // Caso 1: Teste clássico do LeetCode 11
    int t1[] = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    executar_caso_teste("Exemplo 1 do LeetCode (Padrão)", t1, 9, 49);

    // Caso 2: Dois elementos mínimos
    int t2[] = {1, 1};
    executar_caso_teste("Exemplo 2 do LeetCode (Mínimo)", t2, 2, 1);

    // Caso 3: Array estritamente crescente
    int t3[] = {1, 2, 3, 4, 5, 6, 7, 8};
    executar_caso_teste("Array Estritamente Crescente", t3, 8, 16);

    // Caso 4: Array estritamente decrescente
    int t4[] = {8, 7, 6, 5, 4, 3, 2, 1};
    executar_caso_teste("Array Estritamente Decrescente", t4, 8, 16);

    // Caso 5: Alturas constantes (todas iguais)
    int t5[] = {5, 5, 5, 5, 5, 5};
    executar_caso_teste("Alturas Constantes e Repetidas", t5, 6, 25);

    // Caso 6: Caso de borda - Entrada com menos de 2 elementos
    int t6[] = {10};
    executar_caso_teste("Caso Extremo (Apenas 1 elemento)", t6, 1, 0);

    // Benchmark de Desempenho com N = 10.000 elementos
    printf("\n============================================================================\n");
    printf("  BENCHMARK EXPERIMENTAL DE PERFORMANCE (N = 10.000 elementos aleatórios)\n");
    printf("============================================================================\n");

    int n_bench = 10000;
    int *large_array = (int*)malloc(n_bench * sizeof(int));
    srand(42);
    for (int i = 0; i < n_bench; i++) {
        large_array[i] = (rand() % 1000) + 1;
    }

    clock_t start, end;
    unsigned long long ops_fb_large = 0, ops_tp_large = 0;

    // Mede Força Bruta
    start = clock();
    long long area_fb_large = max_area_forca_bruta(large_array, n_bench, &ops_fb_large);
    end = clock();
    double time_fb = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;

    // Mede Two Pointers
    start = clock();
    long long area_tp_large = max_area_two_pointers(large_array, n_bench, &ops_tp_large);
    end = clock();
    double time_tp = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;

    printf("+--------------------------+---------------+-------------------+-----------------+\n");
    printf("| Algoritmo                | Maior Área    | Operações         | Tempo (ms)      |\n");
    printf("+--------------------------+---------------+-------------------+-----------------+\n");
    printf("| Força Bruta O(N^2)       | %-13lld | %-17llu | %10.3f ms   |\n", area_fb_large, ops_fb_large, time_fb);
    printf("| Dois Ponteiros O(N)      | %-13lld | %-17llu | %10.3f ms   |\n", area_tp_large, ops_tp_large, time_tp);
    printf("+--------------------------+---------------+-------------------+-----------------+\n");
    printf("-> Ganho de Desempenho: O algoritmo Two Pointers reduziu %.1f vezes o número de\n", (double)ops_fb_large / ops_tp_large);
    printf("   operações e executou de forma praticamente instantânea!\n\n");

    free(large_array);
    return 0;
}
