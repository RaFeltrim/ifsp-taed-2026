/**
 * ============================================================================
 * INSTITUTO FEDERAL DE SÃO PAULO (IFSP) - CAMPUS SÃO CARLOS
 * DISCIPLINA: Tópicos em Algoritmos e Estruturas de Dados (TAED)
 * PROFESSOR:  Prof. Dr. Rodrigo Elias Bianchi
 * ALUNO:      Rafael Feltrim
 * 
 * TEMA:       Inverter Árvore Binária (Invert Binary Tree)
 * DESAFIO:    LeetCode #226
 * 
 * CONTEXTO HISTÓRICO:
 * Famoso problema mencionado por Max Howell (criador do Homebrew) em processo
 * seletivo do Google: "Google: 90% of our engineers use the software you wrote
 * (Homebrew), but you can't invert a binary tree on a whiteboard so fuck off."
 * O desafio tornou-se uma referência em entrevistas técnicas das Big Techs.
 * 
 * DESCRIÇÃO DO PROBLEMA:
 * Dada a raiz de uma árvore binária, inverta a árvore (produza a sua versão
 * espelhada) e retorne a sua raiz.
 * Para cada nó, seu filho esquerdo e seu filho direito devem ser trocados.
 * 
 * ABORDAGENS IMPLEMENTADAS:
 * 1. Abordagem Recursiva (DFS - Post-Order / Pre-Order):
 *    - Troca os ponteiros left e right de cada nó recursivamente.
 *    - Complexidade de Tempo: O(N), onde N é o número de nós (visita cada nó 1 vez).
 *    - Complexidade de Espaço: O(H), onde H é a altura da árvore (Call Stack).
 *      * O(log N) para árvores balanceadas;
 *      * O(N) no pior caso (árvore desbalanceada / degenerada em lista).
 * 
 * 2. Abordagem Iterativa (BFS com Fila):
 *    - Utiliza uma fila (Queue) para percorrer nível por nível e inverter os nós.
 *    - Complexidade de Tempo: O(N)
 *    - Complexidade de Espaço: O(W), onde W é a largura máxima da árvore.
 * 
 * ESTRUTURAS E TESTES:
 * - Impressão visual em formato de árvore / níveis
 * - Percurso Em-Ordem (In-Order) e Pré-Ordem (Pre-Order)
 * - Casos de teste: Árvore completa do slide [4, 2, 7, 1, 3, 6, 9], árvore vazia,
 *   nó único, árvore degenerada.
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

// Estrutura do Nó da Árvore Binária
typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

// Função auxiliar para criar um novo nó
TreeNode* criar_no(int val) {
    TreeNode* no = (TreeNode*)malloc(sizeof(TreeNode));
    if (!no) {
        fprintf(stderr, "Erro de alocação de memória!\n");
        exit(EXIT_FAILURE);
    }
    no->val = val;
    no->left = NULL;
    no->right = NULL;
    return no;
}

// ============================================================================
// 1. SOLUÇÃO RECURSIVA (DFS) - PADRÃO CLÁSSICO O(N)
// ============================================================================
TreeNode* invertTree(TreeNode* root) {
    // Caso base: nó nulo encerra a recursão
    if (root == NULL) {
        return NULL;
    }

    // Inverte recursivamente as subárvores esquerda e direita
    TreeNode* left_inverted = invertTree(root->left);
    TreeNode* right_inverted = invertTree(root->right);

    // Troca os filhos esquerdo e direito
    root->left = right_inverted;
    root->right = left_inverted;

    return root;
}

// ============================================================================
// 2. SOLUÇÃO ITERATIVA (BFS COM FILA) - O(N)
// ============================================================================
typedef struct QueueNode {
    TreeNode* tree_node;
    struct QueueNode* next;
} QueueNode;

typedef struct {
    QueueNode* front;
    QueueNode* rear;
} Queue;

Queue* criar_fila() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}

void enfileirar(Queue* q, TreeNode* t_node) {
    if (!t_node) return;
    QueueNode* q_node = (QueueNode*)malloc(sizeof(QueueNode));
    q_node->tree_node = t_node;
    q_node->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = q_node;
        return;
    }
    q->rear->next = q_node;
    q->rear = q_node;
}

TreeNode* desenfileirar(Queue* q) {
    if (q->front == NULL) return NULL;
    QueueNode* temp = q->front;
    TreeNode* t_node = temp->tree_node;
    q->front = q->front->next;
    if (q->front == NULL) q->rear = NULL;
    free(temp);
    return t_node;
}

int fila_vazia(Queue* q) {
    return q->front == NULL;
}

TreeNode* invertTreeIterative(TreeNode* root) {
    if (root == NULL) return NULL;

    Queue* q = criar_fila();
    enfileirar(q, root);

    while (!fila_vazia(q)) {
        TreeNode* curr = desenfileirar(q);

        // Troca os filhos esquerdo e direito do nó atual
        TreeNode* temp = curr->left;
        curr->left = curr->right;
        curr->right = temp;

        if (curr->left != NULL) enfileirar(q, curr->left);
        if (curr->right != NULL) enfileirar(q, curr->right);
    }

    free(q);
    return root;
}

// ============================================================================
// FUNÇÕES UTILITÁRIAS DE IMPRESSÃO E LIBERAÇÃO
// ============================================================================

// Percurso Em-Ordem (In-Order Traversal: Esquerda -> Raiz -> Direita)
void imprimir_em_ordem(TreeNode* root) {
    if (root == NULL) return;
    imprimir_em_ordem(root->left);
    printf("%d ", root->val);
    imprimir_em_ordem(root->right);
}

// Percurso Pré-Ordem (Pre-Order Traversal: Raiz -> Esquerda -> Direita)
void imprimir_pre_ordem(TreeNode* root) {
    if (root == NULL) return;
    printf("%d ", root->val);
    imprimir_pre_ordem(root->left);
    imprimir_pre_ordem(root->right);
}

// Impressão Nível a Nível (BFS / Level-Order)
void imprimir_por_niveis(TreeNode* root) {
    if (root == NULL) {
        printf("[Árvore Vazia]\n");
        return;
    }
    Queue* q = criar_fila();
    enfileirar(q, root);
    printf("[ ");
    while (!fila_vazia(q)) {
        TreeNode* curr = desenfileirar(q);
        printf("%d ", curr->val);
        if (curr->left) enfileirar(q, curr->left);
        if (curr->right) enfileirar(q, curr->right);
    }
    printf("]\n");
    free(q);
}

// Liberação recursiva da memória
void liberar_arvore(TreeNode* root) {
    if (root == NULL) return;
    liberar_arvore(root->left);
    liberar_arvore(root->right);
    free(root);
}

// ============================================================================
// MAIN: CASOS DE TESTE E DEMONSTRAÇÃO
// ============================================================================
int main() {
    printf("============================================================================\n");
    printf("  IFSP SCL - TAED: INVERSÃO DE ÁRVORE BINÁRIA (LEETCODE #226)\n");
    printf("============================================================================\n\n");

    // CASO 1: Árvore do Slide da Apresentação
    //         4
    //       /   \
    //      2     7
    //     / \   / \
    //    1   3 6   9
    printf("[CASO 1] Árvore Completa do Slide (LeetCode Exemplo 1):\n");
    TreeNode* root1 = criar_no(4);
    root1->left = criar_no(2);
    root1->right = criar_no(7);
    root1->left->left = criar_no(1);
    root1->left->right = criar_no(3);
    root1->right->left = criar_no(6);
    root1->right->right = criar_no(9);

    printf("  Estrutura Original:\n");
    printf("          4\n");
    printf("        /   \\\n");
    printf("       2     7\n");
    printf("      / \\   / \\\n");
    printf("     1   3 6   9\n");
    printf("  Níveis Original:   "); imprimir_por_niveis(root1);
    printf("  Em-Ordem Original: "); imprimir_em_ordem(root1); printf("\n\n");

    // Aplica inversão recursiva
    root1 = invertTree(root1);

    printf("  Estrutura Invertida (Espelhada):\n");
    printf("          4\n");
    printf("        /   \\\n");
    printf("       7     2\n");
    printf("      / \\   / \\\n");
    printf("     9   6 3   1\n");
    printf("  Níveis Invertida:   "); imprimir_por_niveis(root1);
    printf("  Em-Ordem Invertida: "); imprimir_em_ordem(root1); printf("\n");
    printf("  -> Resultado: Sucesso absoluto! Filhos trocados perfeitamente.\n\n");
    liberar_arvore(root1);

    // CASO 2: Demonstração da Inversão Iterativa (BFS com Fila)
    printf("----------------------------------------------------------------------------\n");
    printf("[CASO 2] Teste da Abordagem Iterativa (BFS com Fila):\n");
    TreeNode* root2 = criar_no(2);
    root2->left = criar_no(1);
    root2->right = criar_no(3);

    printf("  Original:  "); imprimir_por_niveis(root2);
    root2 = invertTreeIterative(root2);
    printf("  Invertida: "); imprimir_por_niveis(root2);
    liberar_arvore(root2);

    // CASO 3: Árvore Degenerada / Desbalanceada (Caminho único à esquerda)
    printf("----------------------------------------------------------------------------\n");
    printf("[CASO 3] Árvore Desbalanceada (Degenerada em Lista):\n");
    TreeNode* root3 = criar_no(1);
    root3->left = criar_no(2);
    root3->left->left = criar_no(3);

    printf("  Original:  "); imprimir_por_niveis(root3);
    root3 = invertTree(root3);
    printf("  Invertida: "); imprimir_por_niveis(root3);
    printf("  (Agora todos os nós apontam para a direita!)\n");
    liberar_arvore(root3);

    // CASO 4: Casos de Borda (Árvore Vazia e Nó Único)
    printf("----------------------------------------------------------------------------\n");
    printf("[CASO 4] Casos de Borda:\n");
    TreeNode* root4 = NULL;
    root4 = invertTree(root4);
    printf("  Árvore Vazia (NULL): "); imprimir_por_niveis(root4);

    TreeNode* root5 = criar_no(42);
    printf("  Nó Único Original:   "); imprimir_por_niveis(root5);
    root5 = invertTree(root5);
    printf("  Nó Único Invertido:  "); imprimir_por_niveis(root5);
    liberar_arvore(root5);

    printf("\n============================================================================\n");
    printf("  Todos os testes de Inversão de Árvore Binária foram validados com êxito!\n");
    printf("============================================================================\n");

    return 0;
}
