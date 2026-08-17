---
tags: [sliding-window, hash-map, two-pointers, leetcode-3, meta, amazon, google, trabalho-moodle]
tipo: estudo-de-caso-oficial
status: ativo
criado: 2026-08-17
problema: Longest Substring Without Repeating Characters (LeetCode 3)
empresas: [Meta, Amazon, Google, Microsoft, Apple, Bloomberg]
---

# 🏆 Longest Substring Without Repeating Characters (LeetCode #3)
> **Tema Oficial Escolhido pelo Grupo para a Atividade do Moodle (Slide 13 / Aula 1)**
> **Disciplina:** Tópicos em Algoritmos e Estruturas de Dados (Prof. Dr. Rodrigo Elias Bianchi — IFSP São Carlos)

---

## 📌 1. Identificação & Enunciado do Problema

* **Nome do Problema:** Substring Mais Longa Sem Caracteres Repetidos (*Longest Substring Without Repeating Characters*).
* **Classificação:** LeetCode #3 (Nível Médio) / Blind 75 / NeetCode 150.
* **Empresas Recorrentes:** **Amazon, Meta (Facebook), Google, Microsoft, Apple, Uber, Bloomberg**.

### Enunciado Formal:
> Dada uma string `s`, encontre o comprimento da **substring mais longa** que não contenha caracteres repetidos.

#### Exemplos:
* **Exemplo 1:** `s = "abcabcbb"` $\rightarrow$ **Saída:** `3` (a substring é `"abc"`).
* **Exemplo 2:** `s = "bbbbb"` $\rightarrow$ **Saída:** `1` (a substring é `"b"`).
* **Exemplo 3:** `s = "pwwkew"` $\rightarrow$ **Saída:** `3` (a substring é `"wke"`. Note que `"pwke"` é uma subsequência, não uma substring contígua).

---

## ⚖️ 2. Análise de Trade-offs: Da Força Bruta à Solução Ótima

### ❌ Abordagem 1: Força Bruta (Brute Force)
1. Gera todos os pares de início e fim $(i, j)$ possíveis: $O(N^2)$ substrings.
2. Para cada substring, verifica se todos os caracteres são únicos usando um conjunto: $O(N)$.
* **Complexidade de Tempo:** $O(N^3)$ $\rightarrow$ **Inválido / Time Limit Exceeded (TLE)** para $N = 50.000$.
* **Complexidade de Espaço:** $O(\min(N, \Sigma))$ onde $\Sigma$ é o tamanho do alfabeto.

---

### 🟡 Abordagem 2: Janela Deslizante Básica (Dois Ponteiros + Set)
* Mantém uma janela `[left, right]`.
* Avança `right` e adiciona ao conjunto.
* Se encontrar duplicata, avança `left` **passo a passo** removendo do conjunto até que a duplicata saia.
* **Complexidade de Tempo:** $O(2N) = O(N)$ (cada caractere é visitado no máximo duas vezes: por `left` e `right`).
* **Complexidade de Espaço:** $O(\min(N, \Sigma))$.

---

### 🟢 Abordagem 3: Janela Deslizante Otimizada com Hash Map (Pulo Direto do `left`)
* Em vez de avançar `left` de 1 em 1, armazenamos no **Hash Map** o **último índice visto de cada caractere** (`map[char] = indice`).
* Quando encontramos um caractere repetido em `right`, saltamos o `left` **diretamente para `max(left, map[char] + 1)`** em $O(1)$!

```text
String: " a  b  c  a  b  c  b  b "
         ↑        ↑
        left    right (ao ver 'a' repetido, left salta para índice 1 em O(1))
```

* **Complexidade de Tempo:** **$O(N)$ estrito** (varredura em passagem única).
* **Complexidade de Espaço:** **$O(\min(N, \Sigma))$** (no máximo 128 posições para tabela ASCII).

---

## 💻 3. Implementação Limpa da Solução Ótima

### Em Python:
```python
def lengthOfLongestSubstring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # Se o caractere já foi visto e está dentro da janela atual
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
            
        char_index_map[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len
```

### Em C (Alinhado com a Aula 2):
```c
#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int last_index[256]; // Tabela direta para caracteres ASCII
    for (int i = 0; i < 256; i++) last_index[i] = -1;
    
    int max_len = 0;
    int left = 0;
    int n = strlen(s);
    
    for (int right = 0; right < n; right++) {
        unsigned char c = (unsigned char)s[right];
        
        if (last_index[c] >= left) {
            left = last_index[c] + 1; // Salto direto em O(1)
        }
        
        last_index[c] = right;
        int current_len = right - left + 1;
        if (current_len > max_len) {
            max_len = current_len;
        }
    }
    
    return max_len;
}
```

---

## 🔗 Links Relacionados no Vault

- [[00 - Diagnóstico e Plano/Ata_Aula_01_Introducao_e_Ementa]]
- [[01 - Estruturas Lineares/Arrays vs Listas Encadeadas]]
- [[02 - Tabelas Hash/Tabelas Hash - Arquitetura Interna]]
- [[99 - Complexidade Big-O/Guia de Complexidade Big-O]]
