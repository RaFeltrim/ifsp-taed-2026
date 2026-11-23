# 

---

### **1. Caso médio — onde a Quadtree ganha com folga**

- **Configure:** `Partículas = 2000`, `Raio = 4`, `Distribuição = Uniforme`, `Modo: força bruta`.

- **O que apontar:**

  - `Testes` fica cravado em **`1999000`** e `Total (média)` estabiliza por volta de **`4–5 ms`**.

- **Clique em `Modo: Quadtree`** *(e ligue `Mostrar grade`)*:

  - `Testes` despenca para a casa de **centenas** (~99,99% menos comparações).
  - Mesmo somando `Detecção + Árvore`, o **`Total (média)`** cai para menos da metade (~`1,5 ms`).

---

### **2. Quando `N` é pequeno — o custo fixo da árvore não se paga**

- **Configure:** `Partículas = 50` (ou `100`), `Raio = 4`, `Uniforme`.
- **O que apontar:** alternando entre `Força bruta` e `Quadtree`, o **`Total (média)`** empata ou a força bruta vence — com poucas partículas, o tempo gasto em **`Árvore`** (alocar e subdividir nós) supera o loop simples da força bruta.

---

### **3. Pior caso — degradação por aglomeração e raio grande**

- **Configure:** `Partículas = 1000`, `Raio = 16` *(ou `32`)*, `Distribuição = Aglomerado`, `Mostrar grade` **ligado**.

- **Comece em `Força bruta`:** anote o **`Total`** e observe que `Testes` continua fixo em `499500`.

- **Clique em `Modo: Quadtree`** *(como o reinício automático está ativo, o aglomerado recomeça do zero na hora)*:

  - **Na tela:** mostre a grade subdividindo densamente só no centro até bater no limite `maxDepth = 8`.
  - **No painel:** nos primeiros segundos, `Testes` dispara e **`Total` (`Detecção + Árvore`) ultrapassa o tempo da força bruta** — a Quadtree perde em tempo real. Conforme as partículas se espalham, a árvore "desafoga" e o `Total` volta a cair.
  - Se o professor quiser ver o pico de novo, basta clicar em **`Reiniciar simulação`**.

---

### **4. Poda parcial — `Dois clusters`**

- **Configure:** `Partículas = 1000`, `Raio = 16`, `Distribuição = Dois clusters`, `Mostrar grade` **ligado**, `Modo: Quadtree`.
- **O que apontar:** a grade mostra o meio vazio sendo descartado inteiro (um cluster nunca testa partículas do outro, então faz menos `Testes` que no `Aglomerado`), mas a degradação ainda acontece dentro de cada aglomerado.
