---
tags: [sliding-window, hash-map, two-pointers, leetcode-3, meta, amazon, google, trabalho-moodle, entrevista-simulada]
tipo: estudo-de-caso-oficial
status: ativo
criado: 2026-08-17
atualizado: 2026-08-17
problema: Longest Substring Without Repeating Characters (LeetCode 3)
empresas: [Amazon, Meta, Google, Microsoft, Apple, Uber, Bloomberg]
---

# 🏆 Longest Substring Without Repeating Characters (LeetCode #3)

> **Documento Oficial de Apresentação & Estudo de Caso de Processo Seletivo (Slide 13)**
> **Disciplina:** Tópicos em Algoritmos e Estruturas de Dados (Prof. Dr. Rodrigo Elias Bianchi — IFSP São Carlos)  
> **Integrantes da Equipe:** Rafael Feltrim, Ian, Gustavo (Gub)

---

## 📌 1. Visão Geral & Relevância de Mercado

* **Classificação:** LeetCode #3 (Nível Médio) / Blind 75 / NeetCode 150.
* **Empresas Recorrentes:**
  - **Amazon:** Frequentemente no *Top 10* de perguntas para cargos de SDE I e II.
  - **Meta (Facebook):** Questão favorita para triagem técnica inicial de 45 minutos.
  - **Google:** Usada para estágios e posições L3/L4 (foco em variações e *streams*).
  - **Microsoft & Bloomberg:** Presença constante em rodadas de algoritmos.

---

## 🎭 2. O "Ritual" da Entrevista Real em Big Techs (3 Fases)

Em uma entrevista técnica de Big Tech, **o código representa apenas ~30% da nota**. Os outros **70% avaliam a comunicação, decomposição e análise de trade-offs**.

```text
┌──────────────────────────┬──────────────────────────┬──────────────────────────┐
│ FASE A: A ARMADILHA     │ FASE B: A OTIMIZAÇÃO     │ FASE C: OS FOLLOW-UPS    │
├──────────────────────────┼──────────────────────────┼──────────────────────────┤
│ O candidato escreve      │ O candidato reconhece    │ O entrevistador adiciona │
│ Força Bruta O(N³).       │ a Janela Deslizante.     │ restrições de memória    │
│ Se não sugerir melhoria: │ Pulo direto em O(1)      │ (ASCII fixo 128/256 bytes│
│ ❌ Red Flag / Rejeitado. │ usando Hash Map:         │ ou stream infinito de    │
│                          │ 🟩 Strong Hire!          │ dados).                  │
└──────────────────────────┴──────────────────────────┴──────────────────────────┘
```

---

## 📈 3. Dinâmica Visual da Janela Deslizante (`s = "abcabcbb"`)

```text
Passo 1: [a]b c a b c b b       -> Janela: "a"   | max_len = 1 (L=0, R=0)
Passo 2: [a b]c a b c b b       -> Janela: "ab"  | max_len = 2 (L=0, R=1)
Passo 3: [a b c]a b c b b       -> Janela: "abc" | max_len = 3 (L=0, R=2)
Passo 4: 'a' repete (antigo=0)! -> Left pula para 0+1=1.
         a [b c a]b c b b       -> Janela: "bca" | max_len = 3 (L=1, R=3)
Passo 5: 'b' repete (antigo=1)! -> Left pula para 1+1=2.
         a b [c a b]c b b       -> Janela: "cab" | max_len = 3 (L=2, R=4)
Passo 6: 'c' repete (antigo=2)! -> Left pula para 2+1=3.
         a b c [a b c]b b       -> Janela: "abc" | max_len = 3 (L=3, R=5)
Passo 7: 'b' repete (antigo=4)! -> Left pula para 4+1=5.
         a b c a b [c b]b       -> Janela: "cb"  | max_len = 3 (L=5, R=6)
Passo 8: 'b' repete (antigo=6)! -> Left pula para 6+1=7.
         a b c a b c b [b]      -> Janela: "b"   | max_len = 3 (L=7, R=7)

Resultado Final: max_len = 3 ("abc")
```

---

## 💻 4. Implementações

### Python (Alta Legibilidade para Slides):
```python
def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}  # Mapeia: caractere -> último índice visto
    esquerda = 0
    maior_comprimento = 0
    
    for direita, char in enumerate(s):
        # Se o caractere já foi visto e está dentro da janela ativa
        if char in char_map and char_map[char] >= esquerda:
            esquerda = char_map[char] + 1  # Pulo direto em O(1)
            
        char_map[char] = direita
        maior_comprimento = max(maior_comprimento, direita - esquerda + 1)
        
    return maior_comprimento
```

### C Baixo Nível (Otimização para Espaço $O(1)$ Estrito):
```c
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int last_index[256]; // Tabela direta ASCII para O(1) de espaço
    for (int i = 0; i < 256; i++) last_index[i] = -1;
    
    int max_len = 0, left = 0;
    int n = strlen(s);
    
    for (int right = 0; right < n; right++) {
        unsigned char c = (unsigned char)s[right];
        if (last_index[c] >= left) {
            left = last_index[c] + 1; // Salto em O(1)
        }
        last_index[c] = right;
        int cur_len = right - left + 1;
        if (cur_len > max_len) max_len = cur_len;
    }
    return max_len;
}
```

---

## ⚖️ 5. Análise de Complexidade Assintótica (Big-O)

* **Complexidade de Tempo:** $O(N)$
  - O ponteiro `direita` percorre a string exatamente uma vez ($N$ passos).
  - Cada operação de consulta/atualização na tabela hash leva tempo constante $O(1)$.
* **Complexidade de Espaço:** $O(\min(N, \Sigma))$
  - $N$: Tamanho da string.
  - $\Sigma$: Tamanho do alfabeto. No pior caso, guarda os caracteres distintos. Se o conjunto for ASCII padrão, o espaço é limitado a $256$ inteiros ($O(1)$ estrito).

---

## 📋 6. Checklist de Avaliação do Entrevistador (Rubrica Big Tech)

Use esta tabela para ensaiar com a equipe:

| Critério de Avaliação | Peso | O que o entrevistador busca |
|---|---|---|
| **1. Decomposição do Problema** | 20% | Explicou a diferença entre substring (contígua) e subsequência? |
| **2. Identificação do Padrão** | 25% | Identificou Janela Deslizante (Two Pointers) sem dicas? |
| **3. Otimização de Estrutura** | 25% | Usou Hash Map para pular o `left` em $O(1)$ em vez de $O(2N)$ do Set? |
| **4. Rigor em Big-O** | 15% | Justificou corretamente $O(N)$ tempo e $O(\min(N, \Sigma))$ espaço? |
| **5. Tratamento de Edge Cases** | 15% | Testou string vazia `""`, caractere único `"a"` e repetidos `"bbbb"`? |

---

## 🔗 Links Relacionados no Vault

- [[00 - Diagnóstico e Plano/Ata_Aula_01_Introducao_e_Ementa]]
- [[00 - Diagnóstico e Plano/Guia_Apresentacao_Equipe_LeetCode3]]
- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]]
- [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]]
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]]
