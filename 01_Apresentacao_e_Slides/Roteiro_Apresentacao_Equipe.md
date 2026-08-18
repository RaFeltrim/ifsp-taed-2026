# 🎙️ Roteiro Oficial de Apresentação — LeetCode #3
## *Longest Substring Without Repeating Characters*

> **Disciplina:** Tópicos em Algoritmos e Estruturas de Dados — IFSP São Carlos  
> **Professor:** Prof. Dr. Rodrigo Elias Bianchi · 2026  
> **Tempo Total Sugerido:** 10 a 12 minutos (~3,5 a 4 minutos por integrante)

---

```
                                  MAPA DE FALA DA EQUIPE
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ RAFAEL FELTRIM (Slides 1 a 3)  → Abertura, Mercado Big Tech & Definição do Problema    │
│ IAN FERNANDES  (Slides 4 a 6)  → 3 Soluções em Código, Rastreio Passo a Passo & Benchmark│
│ GUSTAVO CONTIERO (Slides 7 a 10)→ Arquitetura Visual, Código em C, Big-O & Casos de Borda│
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 👤 PARTE 1: RAFAEL FELTRIM (Slides 1, 2 e 3)
**Foco:** Contextualização, Relevância Estratégica e Definição Formal do Problema.  
**Tempo Estimado:** ~3 minutos.

---

### 🟢 Slide 1 — Capa Oficial
> **O que está na tela:** Título da apresentação, disciplina, professor e nomes da equipe.

**Fala do Rafael:**
> *"Boa noite, Professor Bianchi, boa noite colegas.*  
> *Hoje, o nosso grupo — composto por mim, pelo Ian Fernandes e pelo Gustavo Contiero — vai apresentar a resolução completa e aprofundada do problema **LeetCode #3: Longest Substring Without Repeating Characters**.*  
> *Este desafio foi proposto na Aula 1 como nossa tarefa prática de algoritmos e estruturas de dados lineares. Vamos demonstrar desde a formulação matemática e o mapeamento de mercado nas Big Techs até a otimização assintótica de $O(N^3)$ para $O(N)$ estrito, trazendo benchmarks reais de CPU e a implementação em linguagem C com gestão de memória e aritmética de ponteiros alinhada à nossa Aula 2."*

---

### 🟢 Slide 2 — Relevância de Mercado (Big Techs)
> **O que está na tela:** Painel com empresas (Amazon, Meta, Google, Apple), Regra dos 70/30 e competências técnicas.

**Fala do Rafael:**
> *"Para começar: por que este problema é tão famoso e recorrente em entrevistas da Amazon, Meta, Google e Microsoft?*  
> *Nas entrevistas globais de engenharia de software, vigora a chamada **Regra dos 70/30**: o código funcional representa apenas 30% da nota do candidato. Os outros 70% avaliam a clareza na decomposição lógica, a comunicação técnica e a capacidade de justificar a complexidade assintótica (Big-O).*  
> *O avaliador usa este problema para checar se o desenvolvedor reconhece o desperdício computacional de uma solução cúbica de força bruta e se domina o uso de tabelas hash ou vetores estáticos para processar dados em passagem única."*

---

### 🟢 Slide 3 — Compreendendo o Problema Computacional
> **O que está na tela:** Enunciado oficial, distinção entre Substring vs Subsequência e 3 casos de teste.

**Fala do Rafael:**
> *"Vamos à definição formal:*  
> *Dada uma string $s$, o objetivo é encontrar o comprimento da **maior substring contígua** que não contenha caracteres repetidos.*  
> *Aqui existe uma distinção conceitual que elimina muitos candidatos desatentos: **Substring vs. Subsequência**.*  
> *• A **Substring** exige contiguidade física na memória. Na palavra 'abcde', 'abc' é uma substring.*  
> *• A **Subsequência** mantém a ordem, mas permite saltos, como 'ace'. Nosso foco estrito é em substrings.*  
> *Temos três casos fundamentais de teste:*  
> *1. No caso geral `abcabcbb`, a maior substring sem repetição é `abc`, com tamanho 3.*  
> *2. No caso homogêneo `bbbbb`, a repetição imediata limita o tamanho a 1.*  
> *3. No caso composto `pwwkew`, a resposta é 3 (`wke`), provando que a resposta não precisa começar no início da palavra.*  
>  
> *Agora, passo a palavra ao **Ian**, que vai explicar as três abordagens em código, o rastreio da memória e o benchmark de economia de CPU."*

---

## 👤 PARTE 2: IAN FERNANDES (Slides 4, 5 e 6)
**Foco:** Comparação de Algoritmos, Rastreamento Passo a Passo e Demonstração de Economia de Tempo.  
**Tempo Estimado:** ~4 minutos.

---

### 🔵 Slide 4 — Evolução Algorítmica em 3 Níveis de Eficiência
> **O que está na tela:** Três colunas: 1. Força Bruta $O(N^3)$, 2. Sliding Window com Set $O(2N)$, 3. Sliding Window com Map $O(N)$ Estrito.

**Fala do Ian:**
> *"Obrigado, Rafael. Boa noite a todos.*  
> *Nós analisamos a evolução dessa solução em três patamares de maturidade algorítmica:*  
> *1. **Força Bruta $O(N^3)$:** Gera todas as substrings possíveis com dois loops aninhados $O(N^2)$ e, para cada uma, varre os caracteres verificando repetições com um conjunto $O(N)$. Essa solução é sumariamente **rejeitada** em processos seletivos por estourar o tempo limite de execução (Time Limit Exceeded).*  
> *2. **Sliding Window com Set $O(2N)$:** Usamos dois ponteiros (início e fim da janela). Quando encontramos um caractere repetido, avançamos o ponteiro esquerdo removendo elemento por elemento até eliminar a duplicata. Cada caractere entra e sai do conjunto no máximo uma vez, resultando em $O(2N)$, que assintoticamente é $O(N)$.*  
> *3. **Sliding Window com Hash Map $O(N)$ Estrito (Padrão Ouro):** Em vez de remover de um em um com um loop interno, usamos um Hash Map que guarda o último índice onde cada caractere foi visto. Ao detectar uma duplicata, o ponteiro esquerdo **salta instantaneamente** para a posição seguinte à duplicata em tempo constante $O(1)$. É uma passagem estritamente linear."*

---

### 🔵 Slide 5 — Simulação da Memória: `s = "abcabcbb"`
> **O que está na tela:** Tabela de rastreio de variáveis passo a passo em 8 etapas.

**Fala do Ian:**
> *"Para enxergarmos exatamente o que acontece nas variáveis durante a execução, montamos a tabela de rastreio na string de teste `abcabcbb`:*  
> *• Nos **Passos 1, 2 e 3**, lemos 'a', 'b' e 'c'. A janela expande normalmente: `'a'`, `'ab'`, `'abc'`, atingindo o comprimento **3** (nosso pico máximo).*  
> *• No **Passo 4**, o ponteiro direito $R$ chega no índice 3 e encontra o caractere `'a'`, que já está no mapa no índice 0. Em vez de retroceder, o algoritmo faz o ponteiro esquerdo $L$ saltar direto de 0 para $0 + 1 = 1$. A janela ativa se torna `'bca'`, mantendo tamanho 3.*  
> *• Nos **Passos 5 e 6**, o mesmo acontece com `'b'` e `'c'`, fazendo $L$ saltar progressivamente sem perder o registro do tamanho máximo.*  
> *• Nos **Passos 7 e 8**, as repetições consecutivas de `'b'` encolhem a janela para tamanho 1, mas o algoritmo preserva a variável global `max_len = 3` intacta até o final."*

---

### 🔵 Slide 6 — Economia de Tempo de CPU (Benchmark Experimental)
> **O que está na tela:** Gráfico de benchmark e métricas de alto impacto (-99,99999%, 416 bilhões de ciclos a menos, de 4h para 11ms).

**Fala do Ian:**
> *"Para comprovar esse ganho na prática, desenvolvemos um script de benchmark experimental em Python medindo o tempo real de CPU e o volume de operações para diferentes tamanhos de entrada $N$:*  
> *• Para entradas pequenas como $N = 100$, a força bruta leva $4.85\text{ ms}$, enquanto a janela deslizante leva $0.03\text{ ms}$.*  
> *• Mas quando escalamos para o limite padrão de plataformas como o LeetCode ($N = 50.000$ caracteres), a Força Bruta executaria mais de **20 trilhões de operações**, levando **mais de 4 HORAS** de processamento contínuo!*  
> *• Já a nossa solução otimizada com Janela Deslizante e Hash Map processou os mesmos 50.000 caracteres em apenas **11 milissegundos (0,011 segundos)**.*  
> *Isso representa uma **redução empírica de mais de 99,99999% no tempo de máquina**, poupando mais de 416 bilhões de ciclos de CPU.*  
>  
> *Agora, o **Gustavo** vai detalhar a arquitetura visual desse processo, a implementação em C com ponteiros e a análise formal de Big-O."*

---

## 👤 PARTE 3: GUSTAVO CONTIERO / GUB (Slides 7, 8, 9 e 10)
**Foco:** Arquitetura Visual, Código em C de Baixo Nível, Rigor de Big-O e Casos de Borda.  
**Tempo Estimado:** ~4 minutos.

---

### 🟣 Slide 7 — Mecânica dos Dois Ponteiros (Passo 4)
> **O que está na tela:** Diagrama visual com os ponteiros L=1 e R=3, a janela ativa "bca", a tabela hash e o cálculo $R - L + 1$.

**Fala do Gustavo:**
> *"Obrigado, Ian. Olá, Professor Bianchi, olá a todos.*  
> *Aqui no Slide 7 nós visualizamos a arquitetura geométrica da janela deslizante no momento mais importante da execução: o **Passo 4**.*  
> *Observem o vetor na memória: o ponteiro direito $R$ está no índice 3 apontando para `'a'`. Ao consultar a tabela hash em $O(1)$, identificamos que `'a'` já existia no índice 0.*  
> *Como esse índice está dentro da nossa janela ativa, o ponteiro esquerdo $L$ salta para $0 + 1 = 1$.*  
> *A janela ativa passa a ser exatamente o intervalo contíguo entre os índices 1 e 3 (`'b'`, `'c'`, `'a'`).*  
> *O tamanho da janela é calculado instantaneamente pela fórmula:*  
> $$\text{tamanho} = R - L + 1 \rightarrow 3 - 1 + 1 = 3$$  
> *E o valor de `'a'` no `char_map` é atualizado para o índice 3, tudo em tempo constante."*

---

### 🟣 Slide 8 — Implementação em C & Gestão de Memória na Stack
> **O que está na tela:** Código em C do grupo (`lswrc_solucao2_janela_deslizante.c`), aritmética de ponteiros e vantagens de engenharia.

**Fala do Gustavo:**
> *"Como conexão direta com a nossa **Aula 2 de Revisão em C**, implementamos esse algoritmo em C explorando manipulação explícita de memória e aritmética de ponteiros:*  
> *1. **Aritmética de Ponteiros Pura:** Em vez de indexação por colchetes, utilizamos dois ponteiros de caracteres: `char *esquerda` e `char *direita`. O índice numérico é obtido diretamente pelo deslocamento de memória contígua `(direita - s)` e `(esquerda - s)`.*  
> *2. **Pulo em O(1):** Quando ocorre colisão, fazemos o deslocamento base: `esquerda = s + ultima_pos[c] + 1`.*  
> *3. **Memória Estática na Stack:** Em vez de alocar estruturas complexas na Heap com `malloc()`, declaramos um vetor direto `int ultima_pos[256]`. Isso consome rigorosamente **1.024 bytes (1 KB) na Pilha (Stack)**, com zero sobrecarga de ponteiros, sem risco de memory leak e com máximo aproveitamento do Cache L1 do processador."*

---

### 🟣 Slide 9 — Fundamentação Teórica Assintótica (Big-O)
> **O que está na tela:** Tabela formal de complexidade de Tempo e Espaço, e as justificativas matemáticas.

**Fala do Gustavo:**
> *"Consolidando a análise teórica de complexidade:*  
> *• **Tempo $O(N)$ Estrito:** O ponteiro direito percorre a string do índice $0$ até $N-1$ exatamente uma vez. Todas as operações internas — lookup na tabela, comparação e atualização de ponteiro — executam em tempo constante $O(1)$.*  
> *• **Espaço $O(\min(N, \Sigma))$:** A memória auxiliar necessária depende do menor valor entre o comprimento da string $N$ e o tamanho do alfabeto $\Sigma$. Como o conjunto ASCII padrão possui 256 símbolos possíveis, o consumo de espaço torna-se constante $O(1)$ na prática.*  
> *Por isso, essa abordagem é classificada como **Strong Hire** nas avaliações técnicas."*

---

### 🟣 Slide 10 — Casos de Borda & Conclusão
> **O que está na tela:** Cenários extremos validados (string vazia, caracteres repetidos, distintos, símbolos) e encerramento.

**Fala do Gustavo:**
> *"Para garantir a robustez de nível de produção da nossa engenharia, validamos todos os casos de borda:*  
> *• String vazia `""`: retorna 0 imediatamente.*  
> *• Strings homogêneas como `"bbbbbb"`: a janela detecta colisões contínuas e mantém o tamanho em 1.*  
> *• Strings sem repetição como `"abcdef"`: a janela expande linearmente até o tamanho total $N$.*  
> *• Caracteres especiais e espaços como `"a b c!"`: indexados perfeitamente pelo valor ordinal do byte ASCII.*  
>  
> *Em síntese: transformamos um problema de mais de 4 horas em uma solução elegante de 11 milissegundos, com implementação em C e análise formal.*  
> *Todos os arquivos, códigos, testes e notas Obsidian estão disponíveis no nosso repositório no GitHub.*  
> *Agradecemos a atenção do Professor Bianchi e dos colegas, e estamos abertos para perguntas e considerações da banca!"*

---
