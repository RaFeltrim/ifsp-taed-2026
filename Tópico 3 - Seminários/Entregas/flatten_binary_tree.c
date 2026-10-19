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
    no->val = val;
    no->left = NULL;
    no->right = NULL;
    return no;
}

// Função principal: Achatar a Árvore Binária (In-place, O(1) de espaço extra)
// Desafio correspondente: LeetCode 114 - Flatten Binary Tree to Linked List
void flatten(TreeNode* root) {
    TreeNode* curr = root;
    while (curr != NULL) {
        if (curr->left != NULL) {
            // Encontra o nó mais à direita na subárvore esquerda
            TreeNode* pre = curr->left;
            while (pre->right != NULL) {
                pre = pre->right;
            }
            
            // Conecta a subárvore direita original ao nó mais à direita da subárvore esquerda
            pre->right = curr->right;
            
            // Move a subárvore esquerda para a direita e anula a esquerda
            curr->right = curr->left;
            curr->left = NULL;
        }
        // Avança para o próximo nó à direita
        curr = curr->right;
    }
}

// Função utilitária para imprimir a árvore já transformada em "Linked List"
void imprimir_flattened(TreeNode* root) {
    TreeNode* curr = root;
    while (curr != NULL) {
        printf("%d", curr->val);
        if (curr->right != NULL) {
            printf(" -> ");
        }
        curr = curr->right;
    }
    printf(" -> NULL\n");
}

// Função para testar
int main() {
    printf("--- Flatten Binary Tree to Linked List ---\n\n");
    
    // Criando a árvore de teste: [1,2,5,3,4,null,6]
    // Representação visual:
    //      1
    //     / \
    //    2   5
    //   / \   \
    //  3   4   6
    
    TreeNode* root = criar_no(1);
    root->left = criar_no(2);
    root->right = criar_no(5);
    
    root->left->left = criar_no(3);
    root->left->right = criar_no(4);
    
    root->right->right = criar_no(6);

    printf("Achatando a arvore...\n");
    flatten(root);
    
    printf("Resultado apos achatamento:\n");
    imprimir_flattened(root);
    
    // Liberação de memória (clean up)
    TreeNode* curr = root;
    while(curr != NULL) {
        TreeNode* temp = curr;
        curr = curr->right;
        free(temp);
    }
    
    printf("\nExecucao finalizada com sucesso.\n");
    return 0;
}
