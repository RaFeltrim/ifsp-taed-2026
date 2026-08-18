/*
 * LeetCode 3 - Longest Substring Without Repeating Characters
 * SOLUCAO 2: JANELA DESLIZANTE / SLIDING WINDOW (O(n))
 *
 * Objetivo didatico: mostrar dois ponteiros (esquerda e direita) que
 * caminham SEMPRE PARA FRENTE sobre o vetor, formando uma "janela".
 * Um vetor auxiliar guarda a ultima posicao em que cada caractere foi
 * visto, permitindo saber instantaneamente se ha colisao dentro da
 * janela atual e para onde o ponteiro esquerdo deve pular.
 */

#include <stdio.h>
#include <string.h>

#define MAX 1000

int passo_a_passo = 1;

void pausar(const char *msg)
{
  if (!passo_a_passo)
    return;
  printf("      [PAUSA] %s\n", msg);
  printf("      Pressione ENTER para continuar...");
  fflush(stdout);
  getchar();
}

int main(void)
{
  char s[MAX];
  char resp;

  printf("=== Longest Substring Without Repeating Characters ===\n");
  printf("=== SOLUCAO 2: JANELA DESLIZANTE (Sliding Window) O(n) ===\n\n");

  printf("Digite a string: ");
  fflush(stdout);
  if (fgets(s, MAX, stdin) == NULL)
    return 1;
  s[strcspn(s, "\n")] = '\0';

  int n = (int)strlen(s);
  printf("\nString lida: \"%s\" (tamanho = %d)\n", s, n);
  printf("Endereco base do vetor s: %p\n", (void *)s);

  printf("\nDeseja executar passo a passo (pausando a cada movimento de ponteiro)? (s/n): ");
  fflush(stdout);
  scanf(" %c", &resp);
  passo_a_passo = (resp == 's' || resp == 'S');
  getchar();

  int ultima_pos[256];
  for (int k = 0; k < 256; k++)
    ultima_pos[k] = -1; /* -1 = nunca visto */

  char *esquerda = s; /* ponteiro esquerdo da janela, so anda para frente */
  int melhor_ini = 0, melhor_tam = 0;

  for (char *direita = s; *direita != '\0'; direita++)
  {
    int idx_dir = (int)(direita - s);
    unsigned char c = (unsigned char)*direita;

    printf("\n----------------------------------------------\n");
    printf(">> Ponteiro DIREITA em s[%d] = '%c' (endereco %p)\n",
           idx_dir, *direita, (void *)direita);

    /* colisao so importa se a ultima ocorrencia estiver DENTRO da janela atual */
    if (ultima_pos[c] != -1 && ultima_pos[c] >= (int)(esquerda - s))
    {
      char *nova_esquerda = s + ultima_pos[c] + 1;
      printf("   '%c' ja apareceu em s[%d], que esta DENTRO da janela atual.\n",
             *direita, ultima_pos[c]);
      printf("   Ponteiro ESQUERDA pula de s[%d] para s[%d]\n",
             (int)(esquerda - s), (int)(nova_esquerda - s));
      esquerda = nova_esquerda;
    }
    else
    {
      printf("   '%c' nao esta na janela atual, nenhuma colisao.\n", *direita);
    }

    ultima_pos[c] = idx_dir;

    int tam_atual = (int)(direita - esquerda) + 1;
    printf("   Janela atual: [%d .. %d] = \"%.*s\" (tamanho %d)\n",
           (int)(esquerda - s), (int)(direita - s), tam_atual, esquerda, tam_atual);

    if (tam_atual > melhor_tam)
    {
      melhor_tam = tam_atual;
      melhor_ini = (int)(esquerda - s);
      printf("   *** Novo melhor resultado! tamanho = %d ***\n", melhor_tam);
    }

    pausar("avancando o ponteiro DIREITA");
  }

  printf("\n================================================\n");
  if (melhor_tam > 0)
    printf("RESULTADO: maior substring sem repeticao = \"%.*s\" | tamanho = %d\n",
           melhor_tam, s + melhor_ini, melhor_tam);
  else
    printf("RESULTADO: string vazia, tamanho = 0\n");

  return 0;
}
