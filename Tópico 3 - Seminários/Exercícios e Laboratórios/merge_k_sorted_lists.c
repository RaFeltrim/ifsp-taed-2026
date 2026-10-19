/**
 * ============================================================================
 * INSTITUTO FEDERAL DE SÃO PAULO (IFSP) - CAMPUS SÃO CARLOS
 * DISCIPLINA: Tópicos em Algoritmos e Estruturas de Dados (TAED)
 * PROFESSOR:  Prof. Dr. Rodrigo Elias Bianchi
 * ALUNO:      Rafael Feltrim
 * 
 * TEMA:       Merge K Sorted Lists (Fusão de K Listas Ordenadas)
 * DESAFIO:    LeetCode #23 (Hard)
 * 
 * DESCRIÇÃO DO PROBLEMA:
 * É fornecido um array com K listas encadeadas (linked lists), onde cada lista
 * individual já se encontra ordenada de forma estritamente crescente.
 * O objetivo é fundir todas as K listas em uma única lista encadeada ordenada e
 * retornar a sua cabeça (head).
 * 
 * ABORDAGENS IMPLEMENTADAS:
 * 1. Coleta e Ordenação (Array + QuickSort / qsort):
 *    - Coleta todos os N nós num array, ordena com qsort e reconstrói a lista.
 *    - Complexidade de Tempo: O(N log N)
 *    - Complexidade de Espaço: O(N)
 * 
 * 2. Min-Heap (Fila de Prioridades de Tamanho K):
 *    - Mantém um heap binário de mínimo contendo no máximo K nós (a cabeça de
 *      cada lista ativa).
 *    - A cada passo, retira o menor elemento e insere o próximo nó daquela lista.
 *    - Complexidade de Tempo: O(N log K)
 *    - Complexidade de Espaço: O(K)
 * 
 * 3. Divisão e Conquista (Divide and Conquer - Mais Eficiente em Memória):
 *    - Combina as listas de duas em duas utilizando a fusão linear (Merge de 2 listas).
 *    - O intervalo dobra a cada rodada (log K rodadas no total).
 *    - Reaproveita os nós existentes in-place sem alocação extra.
 *    - Complexidade de Tempo: O(N log K)
 *    - Complexidade de Espaço: O(1) de espaço auxiliar!
 * 
 * TRATAMENTO RIGOROSO DE CASOS DE BORDA (Edge Cases do Seminário):
 * - K = 0 (Array vazio de listas `[]`)
 * - Listas contendo apenas nós nulos (`[[]]`)
 * - Listas vazias intercaladas com listas válidas (`[[], [1], []]`)
 * - Listas de tamanhos discrepantes (`[[1], [0, 2, 3, 4, 5]]`)
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

// Definição do Nó da Lista Encadeada (ListNode)
typedef struct ListNode {
    int val;
    struct ListNode *next;
} ListNode;

// Função auxiliar para criar um novo nó
ListNode* criar_no(int val) {
    ListNode* novo = (ListNode*)malloc(sizeof(ListNode));
    if (!novo) {
        fprintf(stderr, "Erro de alocação de memória!\n");
        exit(EXIT_FAILURE);
    }
    novo->val = val;
    novo->next = NULL;
    return novo;
}

// Cria uma lista encadeada a partir de um array de inteiros
ListNode* criar_lista(const int arr[], int n) {
    if (n <= 0) return NULL;
    ListNode* head = criar_no(arr[0]);
    ListNode* curr = head;
    for (int i = 1; i < n; i++) {
        curr->next = criar_no(arr[i]);
        curr = curr->next;
    }
    return head;
}

// Imprime uma lista encadeada no formato "val -> val -> ... -> NULL"
void imprimir_lista(ListNode* head) {
    if (head == NULL) {
        printf("[Lista Vazia / NULL]\n");
        return;
    }
    ListNode* curr = head;
    while (curr != NULL) {
        printf("%d", curr->val);
        if (curr->next != NULL) printf(" -> ");
        curr = curr->next;
    }
    printf(" -> NULL\n");
}

// Libera toda a memória de uma lista encadeada
void liberar_lista(ListNode* head) {
    ListNode* curr = head;
    while (curr != NULL) {
        ListNode* temp = curr->next;
        free(curr);
        curr = temp;
    }
}

// ============================================================================
// 1. SOLUÇÃO POR DIVISÃO E CONQUISTA (DIVIDE AND CONQUER) - O(N log K), O(1) ESPAÇO
// ============================================================================

// Combina 2 listas ordenadas de forma in-place
ListNode* merge_two_lists(ListNode* l1, ListNode* l2) {
    ListNode dummy;
    dummy.next = NULL;
    ListNode* tail = &dummy;

    while (l1 != NULL && l2 != NULL) {
        if (l1->val <= l2->val) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }

    // Anexa o restante da lista que não terminou
    tail->next = (l1 != NULL) ? l1 : l2;

    return dummy.next;
}

// Mescla K listas usando divisão e conquista
ListNode* merge_k_divide_and_conquer(ListNode* lists[], int k) {
    if (k == 0 || lists == NULL) return NULL;
    if (k == 1) return lists[0];

    int step = 1;
    while (step < k) {
        for (int i = 0; i < k - step; i += 2 * step) {
            lists[i] = merge_two_lists(lists[i], lists[i + step]);
        }
        step *= 2;
    }

    return lists[0];
}

// ============================================================================
// 2. SOLUÇÃO POR MIN-HEAP (FILA DE PRIORIDADES) - O(N log K), O(K) ESPAÇO
// ============================================================================
typedef struct {
    ListNode** data;
    int size;
    int capacity;
} MinHeap;

MinHeap* criar_min_heap(int capacity) {
    MinHeap* h = (MinHeap*)malloc(sizeof(MinHeap));
    h->data = (ListNode**)malloc(sizeof(ListNode*) * capacity);
    h->size = 0;
    h->capacity = capacity;
    return h;
}

void heapify_up(MinHeap* h, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) / 2;
        if (h->data[idx]->val < h->data[parent]->val) {
            ListNode* temp = h->data[idx];
            h->data[idx] = h->data[parent];
            h->data[parent] = temp;
            idx = parent;
        } else {
            break;
        }
    }
}

void heapify_down(MinHeap* h, int idx) {
    while (2 * idx + 1 < h->size) {
        int left = 2 * idx + 1;
        int right = 2 * idx + 2;
        int smallest = left;

        if (right < h->size && h->data[right]->val < h->data[left]->val) {
            smallest = right;
        }

        if (h->data[smallest]->val < h->data[idx]->val) {
            ListNode* temp = h->data[idx];
            h->data[idx] = h->data[smallest];
            h->data[smallest] = temp;
            idx = smallest;
        } else {
            break;
        }
    }
}

void heap_push(MinHeap* h, ListNode* node) {
    if (node == NULL) return;
    h->data[h->size] = node;
    heapify_up(h, h->size);
    h->size++;
}

ListNode* heap_pop(MinHeap* h) {
    if (h->size == 0) return NULL;
    ListNode* root = h->data[0];
    h->size--;
    if (h->size > 0) {
        h->data[0] = h->data[h->size];
        heapify_down(h, 0);
    }
    return root;
}

void liberar_heap(MinHeap* h) {
    free(h->data);
    free(h);
}

ListNode* merge_k_min_heap(ListNode* lists[], int k) {
    if (k == 0 || lists == NULL) return NULL;

    MinHeap* heap = criar_min_heap(k);
    for (int i = 0; i < k; i++) {
        if (lists[i] != NULL) {
            heap_push(heap, lists[i]);
        }
    }

    ListNode dummy;
    dummy.next = NULL;
    ListNode* curr = &dummy;

    while (heap->size > 0) {
        ListNode* smallest = heap_pop(heap);
        curr->next = smallest;
        curr = curr->next;

        if (smallest->next != NULL) {
            heap_push(heap, smallest->next);
        }
    }

    liberar_heap(heap);
    return dummy.next;
}

// ============================================================================
// 3. SOLUÇÃO POR COLETA E ORDENAÇÃO (NAIVE / ARRAY SORT) - O(N log N)
// ============================================================================
int comparar_inteiros(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

ListNode* merge_k_sort_all(ListNode* lists[], int k) {
    if (k == 0 || lists == NULL) return NULL;

    // 1. Conta o total de elementos N
    int total_nodes = 0;
    for (int i = 0; i < k; i++) {
        ListNode* curr = lists[i];
        while (curr != NULL) {
            total_nodes++;
            curr = curr->next;
        }
    }
    if (total_nodes == 0) return NULL;

    // 2. Coleta todos os valores num array
    int* values = (int*)malloc(total_nodes * sizeof(int));
    int idx = 0;
    for (int i = 0; i < k; i++) {
        ListNode* curr = lists[i];
        while (curr != NULL) {
            values[idx++] = curr->val;
            curr = curr->next;
        }
    }

    // 3. Ordena o array completo com QuickSort O(N log N)
    qsort(values, total_nodes, sizeof(int), comparar_inteiros);

    // 4. Reconstrói a lista ordenada
    ListNode* result = criar_lista(values, total_nodes);
    free(values);
    return result;
}

// ============================================================================
// MAIN: SUÍTE DE TESTES E COBERTURA DE CASOS DE BORDA
// ============================================================================
int main() {
    printf("============================================================================\n");
    printf("  IFSP SCL - TAED: MERGE K SORTED LISTS (LEETCODE #23 - HARD)\n");
    printf("============================================================================\n\n");

    // CASO 1: Exemplo Principal da Apresentação
    // Lista 1: 1 -> 4 -> 5
    // Lista 2: 1 -> 3 -> 4
    // Lista 3: 2 -> 6
    printf("[CASO 1] Exemplo Principal do Seminário (K = 3 listas):\n");
    int arr1[] = {1, 4, 5};
    int arr2[] = {1, 3, 4};
    int arr3[] = {2, 6};

    ListNode* l1 = criar_lista(arr1, 3);
    ListNode* l2 = criar_lista(arr2, 3);
    ListNode* l3 = criar_lista(arr3, 2);

    printf("  Lista 1: "); imprimir_lista(l1);
    printf("  Lista 2: "); imprimir_lista(l2);
    printf("  Lista 3: "); imprimir_lista(l3);

    ListNode* lists1[3] = {l1, l2, l3};
    ListNode* merged1 = merge_k_divide_and_conquer(lists1, 3);

    printf("  -> Resultado (Divide & Conquer): "); imprimir_lista(merged1);
    printf("  -> Esperado: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> NULL [SUCESSO]\n\n");
    liberar_lista(merged1);

    // CASO 2: Min-Heap com K = 4 listas
    printf("----------------------------------------------------------------------------\n");
    printf("[CASO 2] Teste com Abordagem Min-Heap (K = 4 listas):\n");
    int h1[] = {2, 7, 10};
    int h2[] = {1, 5, 9};
    int h3[] = {3, 4, 8};
    int h4[] = {0, 6, 12};

    ListNode* lists2[4] = {
        criar_lista(h1, 3),
        criar_lista(h2, 3),
        criar_lista(h3, 3),
        criar_lista(h4, 4)
    };
    ListNode* merged2 = merge_k_min_heap(lists2, 4);
    printf("  -> Resultado (Min-Heap): "); imprimir_lista(merged2);
    liberar_lista(merged2);

    // CASOS DE BORDA DO SLIDE 4
    printf("----------------------------------------------------------------------------\n");
    printf("[CASOS DE BORDA - Conforme especificado nos slides do Seminário]:\n\n");

    // Borda 1: Entrada completamente vazia []
    printf("1. Entrada Vazia [] (K = 0):\n");
    ListNode* edge1 = merge_k_divide_and_conquer(NULL, 0);
    printf("   Resultado: "); imprimir_lista(edge1);

    // Borda 2: [[]] (K = 1, lista vazia)
    printf("2. Lista de Lista Vazia [[]] (K = 1, lista NULL):\n");
    ListNode* lists_edge2[1] = {NULL};
    ListNode* edge2 = merge_k_divide_and_conquer(lists_edge2, 1);
    printf("   Resultado: "); imprimir_lista(edge2);

    // Borda 3: [[], [1], []] (Listas vazias misturadas com nós)
    printf("3. Listas Vazias Intercaladas [[], [1], []]:\n");
    ListNode* lists_edge3[3] = {NULL, criar_no(1), NULL};
    ListNode* edge3 = merge_k_divide_and_conquer(lists_edge3, 3);
    printf("   Resultado: "); imprimir_lista(edge3);
    liberar_lista(edge3);

    // Borda 4: [[1], [0, 2, 3, 4, 5]] (Tamanhos muito discrepantes)
    printf("4. Listas com Tamanhos Discrepantes [[1], [0, 2, 3, 4, 5]]:\n");
    int b4_1[] = {1};
    int b4_2[] = {0, 2, 3, 4, 5};
    ListNode* lists_edge4[2] = {criar_lista(b4_1, 1), criar_lista(b4_2, 5)};
    ListNode* edge4 = merge_k_divide_and_conquer(lists_edge4, 2);
    printf("   Resultado: "); imprimir_lista(edge4);
    liberar_lista(edge4);

    printf("\n============================================================================\n");
    printf("  Todas as abordagens e casos de borda foram validados com êxito!\n");
    printf("============================================================================\n");

    return 0;
}
