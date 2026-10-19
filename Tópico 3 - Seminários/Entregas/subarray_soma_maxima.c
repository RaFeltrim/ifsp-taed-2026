/**
 * ============================================================================
 * INSTITUTO FEDERAL DE SÃO PAULO (IFSP) - CAMPUS SÃO CARLOS
 * DISCIPLINA: Tópicos em Algoritmos e Estruturas de Dados (TAED)
 * PROFESSOR:  Prof. Dr. Rodrigo Elias Bianchi
 * ALUNO:      Rafael Feltrim
 * 
 * TEMA:       Subarray Contíguo de Soma Máxima (Maximum Subarray)
 * ALGORITMO:  Algoritmo de Kadane
 * DESAFIO:    LeetCode #53
 * 
 * DESCRIÇÃO DO PROBLEMA:
 * Dado um array de números inteiros (contendo números positivos, negativos e zero),
 * encontrar o subvetor contíguo, não vazio, que possua a maior soma possível de seus
 * elementos e retornar essa soma, juntamente com os índices inicial e final do trecho.
 * 
 * ABORDAGENS IMPLEMENTADAS:
 * 1. Força Bruta Ingênua (Brute Force O(N^3)):
 *    - Testa todos os pares de índices (i, j) e recalcula a soma do zero a cada vez.
 *    - Complexidade de Tempo: O(N^3)
 *    - Complexidade de Espaço: O(1)
 * 
 * 2. Força Bruta com Soma Acumulada / Prefix Sum (O(N^2)):
 *    - Mantém a soma acumulada enquanto expande o índice j a partir de i.
 *    - Complexidade de Tempo: O(N^2)
 *    - Complexidade de Espaço: O(1)
 * 
 * 3. Algoritmo de Kadane (Programação Dinâmica Ótima):
 *    - Percorre o vetor uma única vez (Single Pass).
 *    - A cada elemento, decide localmente: "Vale a pena estender o subvetor anterior
 *      ou é melhor recomeçar um novo subvetor a partir do elemento atual?"
 *      max_atual = max(nums[i], max_atual + nums[i])
 *    - Rastreia os índices de início e fim da janela de lucro máximo.
 *    - Complexidade de Tempo: O(N)
 *    - Complexidade de Espaço: O(1)
 * 
 * CASOS DE TESTE COBERTOS:
 * - Exemplo do seminário: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> Soma 6 (Trecho [4, -1, 2, 1])
 * - Vetor estritamente negativo: [-5, -2, -8, -1, -4] -> Soma -1 (Não vazio!)
 * - Vetor estritamente positivo: [1, 2, 3, 4, 5] -> Soma 15
 * - Elemento único: [42] -> Soma 42
 * - Benchmark comparativo de CPU e número de operações
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

// Estrutura para encapsular o resultado completo da busca
typedef struct {
    long long max_sum;
    int start_index;
    int end_index;
    unsigned long long operations;
} SubarrayResult;

// ============================================================================
// 1. FORÇA BRUTA INGÊNUA - O(N^3)
// ============================================================================
SubarrayResult max_subarray_brute_force_n3(const int nums[], int n) {
    SubarrayResult res = {LLONG_MIN, 0, 0, 0};
    if (n <= 0) return res;

    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            long long current_sum = 0;
            // Soma todos os elementos entre i e j do zero
            for (int k = i; k <= j; k++) {
                res.operations++;
                current_sum += nums[k];
            }
            if (current_sum > res.max_sum) {
                res.max_sum = current_sum;
                res.start_index = i;
                res.end_index = j;
            }
        }
    }
    return res;
}

// ============================================================================
// 2. FORÇA BRUTA COM SOMA ACUMULADA - O(N^2)
// ============================================================================
SubarrayResult max_subarray_prefix_sum_n2(const int nums[], int n) {
    SubarrayResult res = {LLONG_MIN, 0, 0, 0};
    if (n <= 0) return res;

    for (int i = 0; i < n; i++) {
        long long current_sum = 0;
        for (int j = i; j < n; j++) {
            res.operations++;
            current_sum += nums[j];
            if (current_sum > res.max_sum) {
                res.max_sum = current_sum;
                res.start_index = i;
                res.end_index = j;
            }
        }
    }
    return res;
}

// ============================================================================
// 3. ALGORITMO DE KADANE (ÓTIMO) - O(N) TEMPO, O(1) ESPAÇO
// ============================================================================
SubarrayResult max_subarray_kadane(const int nums[], int n) {
    SubarrayResult res = {LLONG_MIN, 0, 0, 0};
    if (n <= 0) return res;

    long long max_atual = nums[0];
    long long max_global = nums[0];
    int start = 0;
    int end = 0;
    int temp_start = 0;

    res.operations = 1;

    for (int i = 1; i < n; i++) {
        res.operations++;
        // Se o elemento atual sozinho for maior que a soma acumulada + elemento atual,
        // reiniciamos o subarray na posição i
        if (nums[i] > max_atual + nums[i]) {
            max_atual = nums[i];
            temp_start = i;
        } else {
            max_atual += nums[i];
        }

        // Atualiza o recorde global
        if (max_atual > max_global) {
            max_global = max_atual;
            start = temp_start;
            end = i;
        }
    }

    res.max_sum = max_global;
    res.start_index = start;
    res.end_index = end;
    return res;
}

// ============================================================================
// FUNÇÃO UTILITÁRIA DE TESTE E EXIBIÇÃO
// ============================================================================
void executar_teste(const char* titulo, const int nums[], int n, long long esperado) {
    printf("----------------------------------------------------------------------------\n");
    printf("Cenário: %s\n", titulo);
    printf("Array:   [");
    for (int i = 0; i < n && i < 15; i++) {
        printf("%d%s", nums[i], (i == n - 1 || i == 14) ? "" : ", ");
    }
    if (n > 15) printf("... (total %d itens)", n);
    printf("]\n");

    SubarrayResult res_kadane = max_subarray_kadane(nums, n);
    SubarrayResult res_n2 = max_subarray_prefix_sum_n2(nums, n);

    printf("  -> Algoritmo de Kadane O(N): Soma = %lld | Intervalo: [%d .. %d]\n", 
           res_kadane.max_sum, res_kadane.start_index, res_kadane.end_index);
    printf("     Subvetor ótimo: [");
    for (int i = res_kadane.start_index; i <= res_kadane.end_index; i++) {
        printf("%d%s", nums[i], (i == res_kadane.end_index) ? "" : ", ");
    }
    printf("]\n");

    printf("  -> Comparação de Operações: Kadane = %llu ops | Força Bruta O(N^2) = %llu ops\n",
           res_kadane.operations, res_n2.operations);

    if (esperado != LLONG_MIN) {
        printf("  -> Validação: Esperado = %lld | Obtido = %lld [%s]\n", 
               esperado, res_kadane.max_sum, (res_kadane.max_sum == esperado) ? "SUCESSO" : "FALHA");
    }
}

// ============================================================================
// MAIN: SUÍTE DE TESTES E BENCHMARK EXPERIMENTAL
// ============================================================================
int main() {
    printf("============================================================================\n");
    printf("  IFSP SCL - TAED: SUBARRAY DE SOMA MÁXIMA (ALGORITMO DE KADANE)\n");
    printf("============================================================================\n\n");

    // CASO 1: Exemplo canônico do seminário (LeetCode Exemplo 1)
    int c1[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    executar_teste("Exemplo 1 do Seminário (Misto)", c1, 9, 6);

    // CASO 2: Todos os elementos negativos (Desafio clássico)
    int c2[] = {-5, -2, -8, -1, -4};
    executar_teste("Todos os Elementos Negativos (Deve retornar o menor negativo)", c2, 5, -1);

    // CASO 3: Todos os elementos positivos
    int c3[] = {1, 2, 3, 4, 5};
    executar_teste("Todos os Elementos Positivos (Soma total)", c3, 5, 15);

    // CASO 4: Elemento único
    int c4[] = {42};
    executar_teste("Array com Elemento Único", c4, 1, 42);

    // CASO 5: Alternados com ganho intermediário
    int c5[] = {5, 4, -1, 7, 8};
    executar_teste("Exemplo 2 do LeetCode (Majoritariamente positivo)", c5, 5, 23);

    // BENCHMARK EXPERIMENTAL COMPARANDO O(N^3), O(N^2) e O(N)
    printf("\n============================================================================\n");
    printf("  BENCHMARK EXPERIMENTAL DE PERFORMANCE (N = 2.000 elementos)\n");
    printf("============================================================================\n");

    int n_bench = 2000;
    int* bench_array = (int*)malloc(n_bench * sizeof(int));
    srand(123);
    for (int i = 0; i < n_bench; i++) {
        bench_array[i] = (rand() % 201) - 100; // Valores entre -100 e +100
    }

    clock_t start, end;

    // Kadane O(N)
    start = clock();
    SubarrayResult r_kadane = max_subarray_kadane(bench_array, n_bench);
    end = clock();
    double t_kadane = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;

    // Força Bruta O(N^2)
    start = clock();
    SubarrayResult r_n2 = max_subarray_prefix_sum_n2(bench_array, n_bench);
    end = clock();
    double t_n2 = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;

    // Força Bruta O(N^3) (amostra menor para não travar a máquina: n = 400)
    int n_bench_n3 = 400;
    start = clock();
    SubarrayResult r_n3 = max_subarray_brute_force_n3(bench_array, n_bench_n3);
    end = clock();
    double t_n3 = ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;

    printf("+-----------------------------------+---------------+-------------------+-----------------+\n");
    printf("| Algoritmo / Estratégia            | Soma Máxima   | Operações         | Tempo (ms)      |\n");
    printf("+-----------------------------------+---------------+-------------------+-----------------+\n");
    printf("| Kadane O(N)                       | %-13lld | %-17llu | %10.4f ms   |\n", r_kadane.max_sum, r_kadane.operations, t_kadane);
    printf("| Força Bruta c/ Prefix Sum O(N^2)  | %-13lld | %-17llu | %10.4f ms   |\n", r_n2.max_sum, r_n2.operations, t_n2);
    printf("| Força Bruta Ingênua O(N^3) (N=400)| %-13lld | %-17llu | %10.4f ms   |\n", r_n3.max_sum, r_n3.operations, t_n3);
    printf("+-----------------------------------+---------------+-------------------+-----------------+\n");
    printf("-> Ganho do Algoritmo de Kadane: O(N) executou com apenas %llu operações,\n", r_kadane.operations);
    printf("   enquanto O(N^2) exigiu %llu operações no mesmo vetor!\n\n", r_n2.operations);

    free(bench_array);

    printf("============================================================================\n");
    printf("  Todos os testes do Algoritmo de Kadane foram executados com sucesso!\n");
    printf("============================================================================\n");

    return 0;
}
