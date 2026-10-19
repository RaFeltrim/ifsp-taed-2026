#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// Função para verificar se os parênteses são válidos usando uma Pilha (Stack)
bool isValid(char * s) {
    int len = strlen(s);
    
    // Se o tamanho for ímpar, é impossível ser válido
    if (len % 2 != 0) return false;

    char* stack = (char*)malloc(len * sizeof(char));
    int top = -1;

    for (int i = 0; i < len; i++) {
        char c = s[i];
        
        // Empilha caracteres de abertura
        if (c == '(' || c == '{' || c == '[') {
            stack[++top] = c;
        } 
        // Verifica caracteres de fechamento
        else {
            // Se a pilha estiver vazia e vier um fechamento, é inválido
            if (top == -1) {
                free(stack);
                return false;
            }
            
            char pop = stack[top--];
            // Verifica se o par correspondente está correto
            if ((c == ')' && pop != '(') ||
                (c == '}' && pop != '{') ||
                (c == ']' && pop != '[')) {
                free(stack);
                return false;
            }
        }
    }
    
    // É válido se a pilha terminar vazia
    bool result = (top == -1);
    free(stack);
    return result;
}

int main() {
    printf("--- Testes do Algoritmo de Parênteses Balanceados ---\n\n");
    
    char s1[] = "()";
    char s2[] = "()[]{}";
    char s3[] = "(]";
    char s4[] = "([)]";
    char s5[] = "{[]}";
    char s6[] = "((({{{[[[]]]}}})))";

    printf("String: %-20s -> %s\n", s1, isValid(s1) ? "Válido" : "Inválido (Falso)");
    printf("String: %-20s -> %s\n", s2, isValid(s2) ? "Válido" : "Inválido (Falso)");
    printf("String: %-20s -> %s\n", s3, isValid(s3) ? "Válido" : "Inválido (Falso)");
    printf("String: %-20s -> %s\n", s4, isValid(s4) ? "Válido" : "Inválido (Falso)");
    printf("String: %-20s -> %s\n", s5, isValid(s5) ? "Válido" : "Inválido (Falso)");
    printf("String: %-20s -> %s\n", s6, isValid(s6) ? "Válido" : "Inválido (Falso)");

    return 0;
}
