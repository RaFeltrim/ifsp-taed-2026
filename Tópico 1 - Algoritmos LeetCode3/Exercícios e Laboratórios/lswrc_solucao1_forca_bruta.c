/*
 * LeetCode 3 - Longest Substring Without Repeating Characters
 * SOLUCAO 1: FORCA BRUTA (O(n^2))
 *
 * Objetivo didatico: mostrar dois ponteiros (inicio e fim) percorrendo
 * o vetor de caracteres, imprimindo indices, enderecos e o conteudo da
 * janela a cada passo. Pode pausar a execucao (ENTER) para explicar
 * cada movimento em sala de aula.
 *
 * Estrategia: para cada posicao "inicio", avanca-se o ponteiro "fim"
 * enquanto os caracteres nao se repetirem dentro da janela [inicio, fim].
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

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
  printf("=== SOLUCAO 1: FORCA BRUTA (O(n^2)) ===\n\n");

  printf("Digite a string: ");
  fflush(stdout);
  if (fgets(s, MAX, stdin) == NULL)
    return 1;
  s[strcspn(s, "\n")] = '\0'; /* remove o \n do fim */

  int n = (int)strlen(s);
  printf("\nString lida: \"%s\" (tamanho = %d)\n", s, n);
  printf("Endereco base do vetor s: %p\n", (void *)s);

  printf("\nDeseja executar passo a passo (pausando a cada comparacao)? (s/n): ");
  fflush(stdout);
  scanf(" %c", &resp);
  passo_a_passo = (resp == 's' || resp == 'S');
  getchar(); /* limpa o \n residual do buffer de entrada */

  int melhor_ini = 0, melhor_tam = 0;

  /* ponteiro "inicio" percorre cada posicao inicial possivel da substring */
  for (char *inicio = s; *inicio != '\0'; inicio++)
  {
    int idx_inicio = (int)(inicio - s); /* indice = aritmetica de ponteiros */
    printf("\n----------------------------------------------\n");
    printf(">> Ponteiro INICIO aponta para s[%d] = '%c' (endereco %p)\n",
           idx_inicio, *inicio, (void *)inicio);

    bool visto[256] = {false}; /* marca caracteres ja vistos na janela atual */
    char *fim = inicio;        /* ponteiro "fim" comeca igual a "inicio" */

    while (*fim != '\0' && !visto[(unsigned char)*fim])
    {
      int idx_fim = (int)(fim - s);
      printf("   -> Ponteiro FIM  aponta para s[%d] = '%c' (endereco %p) | ",
             idx_fim, *fim, (void *)fim);

      visto[(unsigned char)*fim] = true;
      int tam_atual = (int)(fim - inicio) + 1;
      printf("substring atual = \"%.*s\" (tamanho %d)\n",
             tam_atual, inicio, tam_atual);

      if (tam_atual > melhor_tam)
      {
        melhor_tam = tam_atual;
        melhor_ini = idx_inicio;
        printf("      *** Novo melhor resultado! tamanho = %d ***\n", melhor_tam);
      }

      pausar("avancando o ponteiro FIM");
      fim++;
    }

    if (*fim != '\0')
    {
      printf("   -> s[%d] = '%c' ja apareceu na janela! Parede de colisao.\n",
             (int)(fim - s), *fim);
    }
    else
    {
      printf("   -> Fim da string alcancado sem repeticoes.\n");
    }
    pausar("avancando o ponteiro INICIO para a proxima posicao");
  }

  printf("\n================================================\n");
  if (melhor_tam > 0)
    printf("RESULTADO: maior substring sem repeticao = \"%.*s\" | tamanho = %d\n",
           melhor_tam, s + melhor_ini, melhor_tam);
  else
    printf("RESULTADO: string vazia, tamanho = 0\n");

  return 0;
}
