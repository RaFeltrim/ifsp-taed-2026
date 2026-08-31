# 🎵 Apresentação: O Algoritmo de Shuffle do Spotify

> **Disciplina:** Tópicos em Algoritmos e Estruturas de Dados (IFSP - Campus São Carlos)
> **Professor:** Prof. Dr. Rodrigo Elias Bianchi
> **Tema:** Desafio Prático de Processo Seletivo em Big Tech (Slide 13)

---

## 📄 SLIDE 1: Capa & Contexto do Problema

### **"Como Fazer o Aleatório Parecer Humano?"**

* **Objetivo:** Entender a evolução histórica do algoritmo de reprodução aleatória do Spotify.
* **O Desafio de Engenharia:** Como distribuir centenas de milhões de reproduções sem criar aglomerações (*clusters*) de faixas do mesmo artista, mantendo alta performance e baixa latência.

---

## 📄 SLIDE 2: A Abordagem Inicial — Fisher-Yates (Aleatoriedade Pura)

### **O Algoritmo Clássico**

* Utilizava uma variação do **Fisher-Yates Shuffle** (via Mersenne Twister).
* **Complexidade:** $O(N)$ em tempo, $O(1)$ espaço extra.

```python
# Fisher-Yates Shuffle - O(N)
def fisher_yates(playlist):
    for i in range(len(playlist) - 1, 0, -1):
        j = random.randint(0, i)
        playlist[i], playlist[j] = playlist[j], playlist[i]
```

### **O Problema da Percepção Humana**

* A aleatoriedade matemática pura produz **agrupamentos naturais**.
* Em uma lista com 4 faixas de um mesmo artista em 20 músicas, é comum 3 tocarem seguidas.
* Para a mente humana, que busca padrões, a sequência parecia **"viciada ou não-aleatória"**.

---

## 📄 SLIDE 3: A Virada de Chave — Dithering & Anti-Clustering

### **Inspiração no Processamento de Imagens**

* A engenharia do Spotify adaptou algoritmos de **Dithering** (como Floyd-Steinberg).
* Em vez de sorteio cego, o algoritmo calcula a **proporção de cada artista/gênero** e distribui as faixas homogeneamente ao longo da lista.

```text
[Aleatório Puro (Fisher-Yates)] ──►  [ArtistaA] [ArtistaA] [ArtistaA] [ArtistaB] [ArtistaC]
                                      └─ (Cluster indesejado)

[Dithering (Anti-Clustering)]   ──►  [ArtistaA] [ArtistaB] [ArtistaC] [ArtistaA] [ArtistaD]
                                      └─ (Espaçamento balanceado ~K posições)
```

### **Arquitetura de Dados:**

1. **Hash Map:** Conta frequências de cada artista.
2. **Max-Heap (Priority Queue):** Mantém os artistas com mais faixas pendentes no topo.
3. **Queue / Sliding Window:** Garante um tempo de espera (*cooldown*) antes de repetir o mesmo artista.

---

## 📄 SLIDE 4: Modos de Produção & API Oficial

### **Divisão em Modos (Experiência do Usuário)**

* **Fewer Repeats (Padrão Premium):** Calcula uma pontuação de "frescor" (*freshness score*) baseada no histórico recente do ouvinte.
* **Standard Shuffle:** Aleatoriedade matemática tradicional (Fisher-Yates).
* **Smart Shuffle:** Intercala recomendações de IA (1 recomendação a cada 3 faixas).

### **Integração com a Spotify Web API**

* **Endpoint:** `PUT https://api.spotify.com/v1/me/player/shuffle?state=true`
* O aplicativo envia a requisição HTTP e o *backend* da nuvem processa a reordenação em tempo real.

---

## 📄 SLIDE 5: Desafios Correlatos em Entrevistas de Big Techs (LeetCode)

As maiores empresas de tecnologia cobram essa mesma lógica em testes de código:

| Desafio LeetCode                            | Conceito Avaliado                                         | Estrutura de Dados                         | Complexidade       |
| ------------------------------------------- | --------------------------------------------------------- | ------------------------------------------ | ------------------ |
| **358. Rearrange String k Distance**  | Separar elementos iguais por$K$ posições              | Hash Map + Max-Heap + Cooldown Queue       | $O(N \log A)$    |
| **621. Task Scheduler**               | Tempo de espera (*cooldown*) antes de repetir categoria | Frequência + Algoritmo Guloso             | $O(N)$           |
| **380. Insert Delete GetRandom O(1)** | Sorteio aleatório instantâneo em catálogo              | Hash Map + Array Dinâmico (Swap na ponta) | **$O(1)$** |
| **384. Shuffle an Array**             | Permutação*in-place* sem viés                        | Array Swaps (Fisher-Yates)                 | $O(N)$           |

---

## 📄 SLIDE 6: Análise de Complexidade Assintótica (Big-O)

| Etapa do Algoritmo                              | Complexidade de Tempo | Complexidade de Espaço                     |
| ----------------------------------------------- | --------------------- | ------------------------------------------- |
| **Fisher-Yates Padrão**                  | $O(N)$              | $O(1)$                                    |
| **Anti-Clustering (Max-Heap + Cooldown)** | $O(N \log A)$       | $O(A)$ ($A = \text{artistas únicos}$)  |
| **Consulta da Janela Deslizante**         | $O(1)$ amortizado   | $O(K)$ ($K = \text{tamanho da janela}$) |

---

## 📄 SLIDE 7: Conclusão & Perguntas

* A verdadeira aleatoriedade computacional nem sempre atende às expectativas dos usuários.
* A solução combinou **Teoria dos Grafos / Janelas Deslizantes** com **Dithering de Imagem**.
* **Perguntas da Turma?**
