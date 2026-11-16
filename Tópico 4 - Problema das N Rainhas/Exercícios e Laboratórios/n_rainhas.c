/**
 * ============================================================================
 * INSTITUTO FEDERAL DE SÃO PAULO (IFSP) - CAMPUS SÃO CARLOS
 * DISCIPLINA: Tópicos em Algoritmos e Estruturas de Dados (TAED)
 * PROFESSOR:  Prof. Dr. Rodrigo Elias Bianchi
 * ALUNO:      Rafael Feltrim
 *
 * TEMA:       Problema das N-Rainhas (N-Queens) em C Puro
 * DESAFIO:    LeetCode #51 (Hard)
 *
 * DESCRIÇÃO DO PROBLEMA:
 * Posicionar N rainhas em um tabuleiro de xadrez N x N de forma que nenhuma
 * rainha ataque outra (sem compartilhar mesma linha, coluna ou diagonal).
 *
 * ESTRATÉGIA (CONFORME ROTEIRO DE LABORATÓRIO):
 * - Representação unidimensional: int posicoes[N], onde o índice representa
 *   a linha e o valor armazenado representa a coluna da rainha naquela linha.
 * - C Puro: sem uso de <stdbool.h> (retornos booleanos via int: 1 ou 0).
 * - Backtracking recursivo linha a linha, validando coluna e diagonais via abs().
 * - Alocação dinâmica tripla (char ***) compatível com a assinatura do LeetCode #51.
 *
 * COMPLEXIDADE:
 * - Tempo:  O(N!) no pior caso (poda significativa via backtracking).
 * - Espaço: O(N) para o vetor de posições e pilha de recursão (além do espaço
 *           de saída das soluções geradas).
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SOLUCOES 15000

// ============================================================================
// PASSO 2: VERIFICAÇÃO DE SEGURANÇA (COLUNA E DIAGONAIS)
// ============================================================================

/**
 * Verifica se é seguro posicionar uma rainha em (linha, col) dadas as rainhas
 * já posicionadas nas linhas 0 .. linha - 1.
 * Retorna 1 se seguro, 0 se houver conflito.
 */
int eh_seguro(int *posicoes, int linha, int col) {
    for (int i = 0; i < linha; i++) {
        // Mesma coluna
        if (posicoes[i] == col) {
            return 0;
        }
        // Mesma diagonal: |x1 - x2| == |y1 - y2|
        if (abs(i - linha) == abs(posicoes[i] - col)) {
            return 0;
        }
    }
    return 1;
}

// ============================================================================
// PASSO 3: LÓGICA RECURSIVA DE BACKTRACKING
// ============================================================================

/**
 * Constrói recursivamente todas as configurações válidas das N rainhas.
 */
void backtrack(int n, int linha, int *posicoes, char ***solucoes, int *total_solucoes) {
    // Caso Base: todas as N rainhas foram posicionadas com sucesso
    if (linha == n) {
        if (*total_solucoes >= MAX_SOLUCOES) {
            return;
        }

        char **tabuleiro = (char **)malloc((size_t)n * sizeof(char *));
        if (tabuleiro == NULL) {
            fprintf(stderr, "Erro de alocacao para o tabuleiro.\n");
            exit(EXIT_FAILURE);
        }

        for (int i = 0; i < n; i++) {
            tabuleiro[i] = (char *)malloc((size_t)(n + 1) * sizeof(char));
            if (tabuleiro[i] == NULL) {
                fprintf(stderr, "Erro de alocacao para linha do tabuleiro.\n");
                exit(EXIT_FAILURE);
            }
            for (int j = 0; j < n; j++) {
                tabuleiro[i][j] = '.';
            }
            tabuleiro[i][posicoes[i]] = 'Q';
            tabuleiro[i][n] = '\0';
        }

        solucoes[*total_solucoes] = tabuleiro;
        (*total_solucoes)++;
        return;
    }

    // Passo Recursivo: tenta posicionar a rainha em cada coluna da linha atual
    for (int col = 0; col < n; col++) {
        if (eh_seguro(posicoes, linha, col)) {
            posicoes[linha] = col;
            backtrack(n, linha + 1, posicoes, solucoes, total_solucoes);
        }
    }
}

// ============================================================================
// PASSO 4: ASSINATURA PRINCIPAL EXIGIDA PELO LEETCODE #51
// ============================================================================

/**
 * Resolve o problema das N-Rainhas e retorna um array de tabuleiros formatados.
 * O chamador é responsável por liberar a memória retornada.
 */
char ***solveNQueens(int n, int *returnSize, int **returnColumnSizes) {
    if (n <= 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    char ***solucoes = (char ***)malloc((size_t)MAX_SOLUCOES * sizeof(char **));
    int *posicoes = (int *)malloc((size_t)n * sizeof(int));
    if (solucoes == NULL || posicoes == NULL) {
        fprintf(stderr, "Erro de alocacao inicial.\n");
        free(solucoes);
        free(posicoes);
        exit(EXIT_FAILURE);
    }

    int total_solucoes = 0;
    backtrack(n, 0, posicoes, solucoes, &total_solucoes);

    *returnSize = total_solucoes;

    if (total_solucoes > 0) {
        char ***solucoes_ajustadas = (char ***)realloc(
            solucoes, (size_t)total_solucoes * sizeof(char **)
        );
        if (solucoes_ajustadas != NULL) {
            solucoes = solucoes_ajustadas;
        }

        *returnColumnSizes = (int *)malloc((size_t)total_solucoes * sizeof(int));
        if (*returnColumnSizes == NULL) {
            fprintf(stderr, "Erro de alocacao para returnColumnSizes.\n");
            free(posicoes);
            exit(EXIT_FAILURE);
        }
        for (int i = 0; i < total_solucoes; i++) {
            (*returnColumnSizes)[i] = n;
        }
    } else {
        free(solucoes);
        solucoes = NULL;
        *returnColumnSizes = NULL;
    }

    free(posicoes);
    return solucoes;
}

// ============================================================================
// FUNÇÕES AUXILIARES DE EXIBIÇÃO E LIBERAÇÃO DE MEMÓRIA
// ============================================================================

void liberar_solucoes(char ***solucoes, int total_solucoes, int *col_sizes) {
    if (solucoes != NULL) {
        for (int i = 0; i < total_solucoes; i++) {
            int n = (col_sizes != NULL) ? col_sizes[i] : 0;
            for (int r = 0; r < n; r++) {
                free(solucoes[i][r]);
            }
            free(solucoes[i]);
        }
        free(solucoes);
    }
    free(col_sizes);
}

void executar_e_exibir(int n, int max_imprimir) {
    int total_solucoes = 0;
    int *col_sizes = NULL;

    char ***solucoes = solveNQueens(n, &total_solucoes, &col_sizes);

    printf("----------------------------------------------------------------------------\n");
    printf("[N = %d] Total de solucoes encontradas: %d\n", n, total_solucoes);

    int limite = (total_solucoes < max_imprimir) ? total_solucoes : max_imprimir;
    for (int s = 0; s < limite; s++) {
        printf("\n  Solucao #%d:\n", s + 1);
        for (int r = 0; r < col_sizes[s]; r++) {
            printf("    %s\n", solucoes[s][r]);
        }
    }

    if (total_solucoes > max_imprimir) {
        printf("\n  (... exibindo apenas as %d primeiras de %d solucoes)\n",
               max_imprimir, total_solucoes);
    }

    liberar_solucoes(solucoes, total_solucoes, col_sizes);
}

// ============================================================================
// MAIN: SUÍTE DE TESTES
// ============================================================================
int main(void) {
    printf("============================================================================\n");
    printf("  IFSP SCL - TAED: PROBLEMA DAS N-RAINHAS (N-QUEENS - LEETCODE #51)\n");
    printf("============================================================================\n\n");

    // Casos conhecidos da literatura / LeetCode:
    // N = 1 -> 1 solucao
    // N = 2 -> 0 solucoes
    // N = 3 -> 0 solucoes
    // N = 4 -> 2 solucoes
    // N = 8 -> 92 solucoes (problema classico do tabuleiro de xadrez)
    executar_e_exibir(1, 5);
    executar_e_exibir(2, 5);
    executar_e_exibir(3, 5);
    executar_e_exibir(4, 5);
    executar_e_exibir(8, 2);

    printf("\n============================================================================\n");
    printf("  Todos os testes de N-Rainhas (C Puro + Backtracking) concluidos!\n");
    printf("============================================================================\n");

    return 0;
}
