# 🎤 Guia Completo de Apresentação em Equipe — Tarefa Prática (Slide 13)

> **Disciplina:** Tópicos em Algoritmos e Estruturas de Dados  
> **Docente:** Prof. Dr. Rodrigo Elias Bianchi (IFSP - Campus São Carlos)  
> **Tema:** Desafio Real de Processo Seletivo Big Tech — *Longest Substring Without Repeating Characters* (LeetCode #3)  
> **Integrantes da Equipe:** Rafael Feltrim, Ian, Gustavo (Gub)

---

## 🎯 1. Ficha Técnica do Problema
* **Nome:** Substring Mais Longa Sem Caracteres Repetidos (*Longest Substring Without Repeating Characters*)
* **Plataforma:** LeetCode #3 / Blind 75 / NeetCode 150
* **Empresas Recorrentes:** **Amazon, Meta (Facebook), Google, Microsoft, Apple, Uber, Bloomberg**
* **Classificação:** Médio (Fundamental para entrevistas de Engenharia de Software)
* **Paradigma Central:** **Janela Deslizante (Sliding Window)** com **Tabela Hash / Direct Access Table**

---

## 👥 2. Divisão de Fala da Equipe (Roteiro Slide por Slide)

### 🎙️ Bloco 1: Contexto de Mercado & Enunciado do Problema (Membro 1 — ~2 min)
* **Abertura:** "Boa noite professor, boa noite turma. Nosso grupo escolheu o problema *Longest Substring Without Repeating Characters*, um dos desafios mais frequentes em entrevistas técnicas de empresas como Amazon, Meta e Google."
* **O Enunciado:** Dada uma string $s$, encontrar o tamanho da maior substring contígua sem caracteres repetidos.
* **Exemplos Rápidos na Lousa:**
  - `s = "abcabcbb"` $\rightarrow$ Resposta: **3** (substring `"abc"`).
  - `s = "bbbbb"` $\rightarrow$ Resposta: **1** (substring `"b"`).
  - `s = "pwwkew"` $\rightarrow$ Resposta: **3** (substring `"wke"`. *Atenção:* `"pwke"` é subsequência, não substring contígua!).

---

### 🎙️ Bloco 2: O Desastre da Força Bruta vs. Janela Deslizante (Membro 2 — ~2 min)
* **A Solução Ingênua (Força Bruta):**
  - Gerar todos os pares de início e fim $(i, j)$ possíveis: $O(N^2)$ substrings.
  - Para cada substring, verificar se há duplicatas com um laço extra: $O(N)$.
  - **Custo Total:** **$O(N^3)$** $\rightarrow$ Trava o sistema (*Time Limit Exceeded*) para strings com mais de 10.000 caracteres.
* **A Intuição da Janela Deslizante:**
  - Em vez de recomeçar do zero a cada tentativa, mantemos uma "janela" com dois ponteiros: `left` e `right`.
  - O ponteiro `right` expande a janela para a direita.
  - Quando encontramos um caractere repetido, em vez de voltar o `right`, nós apenas encolhemos a janela pela esquerda (`left`).

---

### 🎙️ Bloco 3: O "Pulo do Gato" com Hash Map & Demonstração de Código (Membro 3 — ~3 min)
* **A Otimização com Tabela Hash:**
  - Se usarmos apenas um conjunto (`set`), temos que andar com o `left` de 1 em 1 até remover a duplicata ($2N$ passos).
  - **A Sacada de Engenharia:** Guardamos no Hash Map o **último índice onde cada caractere apareceu** (`map[char] = indice`).
  - Ao encontrar um caractere repetido, o `left` **salta diretamente** para `map[char] + 1` em tempo constante $O(1)$!

```python
def lengthOfLongestSubstring(s: str) -> int:
    last_seen = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # Se o caractere já foi visto e está dentro da janela atual
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1  # Pulo direto em O(1)
            
        last_seen[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len
```

---

### 🎙️ Bloco 4: Análise Big-O, Casos de Borda & Perguntas (Membro 4 / Todos — ~2 min)

#### Tabela Comparativa de Complexidade:
| Abordagem | Complexidade de Tempo | Complexidade de Espaço | Veredicto |
|---|---|---|---|
| **1. Força Bruta** | $O(N^3)$ | $O(\min(N, \Sigma))$ | Inviável ($N > 1.000$) |
| **2. Sliding Window com Set** | $O(2N) = O(N)$ | $O(\min(N, \Sigma))$ | Boa, mas faz passos extras |
| **3. Sliding Window com Hash Map (Nossa)** | **$O(N)$ estrito** | **$O(\min(N, \Sigma))$** | **Ótima (Padrão Big Tech)** |

* $\Sigma$: Tamanho do alfabeto (para tabela ASCII padrão, $\Sigma = 128$ ou $256$, o que torna o espaço $O(1)$ na prática).

#### Casos de Borda (Edge Cases) Cobertos:
1. **String vazia `""`:** Retorna `0` imediatamente.
2. **String com todos os caracteres iguais `"aaaaaa"`:** A janela se mantém em tamanho `1`.
3. **String com todos os caracteres distintos `"abcdef"`:** A janela expande até o tamanho total $N$.
4. **Caracteres especiais, espaços e símbolos:** Totalmente suportados pela tabela ASCII.

---

## ❓ Possíveis Perguntas do Professor e Como Responder

1. **Pergunta:** *"Por que usamos `last_seen[char] >= left` na condição do `if`?"*
   - **Resposta:** Porque o Hash Map armazena índices de toda a string. Se um caractere repetido apareceu antes da janela atual (`< left`), ele não é uma duplicata da janela ativa e deve ser ignorado.

2. **Pergunta:** *"Como vocês implementariam isso em C baixo nível sem biblioteca de Hash Map?"*
   - **Resposta:** Criamos um vetor estático `int last_index[256]` inicializado com `-1`. O próprio valor ASCII do caractere `(unsigned char)s[right]` vira o índice do vetor, garantindo acesso em $O(1)$ sem overhead de colisão!
