# Quadtree — Colisão de Partículas

![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=flat-square&logo=javascript&logoColor=000000)
![HTML5 Canvas](https://img.shields.io/badge/Canvas-2D%20API-E34F26?style=flat-square&logo=html5&logoColor=FFFFFF)
![Node Test](https://img.shields.io/badge/node%20--test-37%2F37%20passando-2EA44F?style=flat-square&logo=nodedotjs&logoColor=FFFFFF)
![Dependencies](https://img.shields.io/badge/Depend%C3%AAncias-Zero-4C1?style=flat-square)

Simulação interativa que compara a detecção de colisão entre partículas por **força bruta** ($O(N^2)$) e por uma **Quadtree** ($O(N \log N)$) implementada do zero em JavaScript puro, sem servidor, sem *bundler* e sem dependências externas.

---

## Como executar

Após clonar o repositório, não é necessário instalar dependências nem rodar *build*.

### 1. Abrir a simulação no navegador

Abra [`index.html`](./index.html) diretamente ou execute pelo terminal:

```bash
# Windows (PowerShell / CMD)
start index.html

# Linux
xdg-open index.html

# macOS
open index.html
```

*(Opcional, via servidor HTTP local)*:

```bash
python -m http.server 8080
# Acesse: http://localhost:8080
```

### 2. Rodar os testes unitários

```bash
node --test
```

### Controles

- **Minimizar painel (`−` / `+` ou tecla `H`)**: recolhe ou expande os controles para liberar a área total do canvas.
- **Benchmarks**: abre o painel interativo [`bench/benchmark.html`](./bench/benchmark.html) direto a partir do simulador.
- **Partículas (`10–2000`)**: ajuste pelo *slider* (reinicia ao soltar) ou diretamente pelo campo numérico ao lado (`Enter` ou sair do campo aplica o valor entre `10` e `2000` e reinicia).
- **Raio (`2, 4, 8, 16, 32 px`)**: altera o tamanho das partículas e reinicia a simulação.
- **Distribuição (`Uniforme`, `Aglomerado`, `Dois clusters`)**: define a posição inicial das partículas para comparar o caso médio (`Uniforme`) com cenários de degradação por alta densidade local (`Aglomerado` no centro ou `Dois clusters` separados).
- **FPS alvo (`5, 15, 30, 60, 120, Máx`)**: ajusta a taxa de passos simulados por segundo sem alterar as posições nem os cálculos de tempo por frame.
- **Modo (`Força bruta` / `Quadtree`)**: alterna o algoritmo de detecção (mantém as posições em `Uniforme` e reinicia automaticamente a distribuição em `Aglomerado` e `Dois clusters`).
- **Reiniciar simulação**: reinicia as posições das partículas com a distribuição selecionada.
- **Mostrar grade**: desenha as subdivisões recursivas da Quadtree no canvas.
- **Arrastar o mouse**: seleciona uma região retangular e destaca as partículas encontradas pela *range query*. Um clique simples limpa a seleção.

O painel superior exibe FPS, número de partículas, testes de colisão por frame, tempo de detecção e o algoritmo ativo:

- **Testes**: quantas comparações entre pares foram feitas no frame.
- **Detecção**: tempo médio (ms) para encontrar os pares que colidem.
- **Árvore** *(só no modo Quadtree)*: tempo médio (ms) para reconstruir a Quadtree a cada frame.
- **Total**: custo total por frame (em força bruta é igual a **Detecção**; em Quadtree é **Detecção + Árvore**), seguido da **média** acumulada por frame desde o último reinício ou troca de modo.
- **Gráfico de velocidade**: exibido abaixo das estatísticas com o tempo por frame (ms) e o pico máximo. Ao alternar o modo na mesma distribuição, a curva anterior permanece visível como referência para comparação direta com a nova linha.

O FPS é limitado pela taxa de atualização do monitor e por isso pode não diferenciar os algoritmos; o tempo em ms mostra a diferença real. Com `2000` partículas e raio `4`, a força bruta leva cerca de `4 ms` por frame e a Quadtree cerca de `1,5 ms` (detecção + árvore), com ordem de grandeza menor de testes (`~2 milhões` contra `~150`). O ganho cresce com o número de partículas.

---

## Modo didático

Permite acompanhar o algoritmo encontrando colisões iteração por iteração. Ative pelo botão **Modo didático** (disponível para até `200` partículas; valores próximos de `20` facilitam a visualização).

A animação executa normalmente até duas partículas colidirem. Nesse momento, a simulação pausa **antes do ricochete**, destaca em **verde** o par que colidiu e exibe o passo a passo da detecção daquele frame desde a primeira iteração:

| Atalho / Controle | Ação durante a apresentação |
| :--- | :--- |
| `→` / `←` | Avança ou retrocede um passo da detecção |
| `Shift + →` / `Shift + ←` | Pula para a próxima ou anterior partícula analisada |
| `Enter` | Vai direto ao teste da colisão que disparou a pausa |
| `Esc` *(ou `→` no último passo)* | Encerra o modo passo a passo, aplica os ricochetes e retoma a animação |
| **Botão de Modo** | Refaz os passos do mesmo frame com o outro algoritmo |

Após encerrar a apresentação, há um intervalo de `5 s` (`COOLDOWN_MS = 5000`) em que novas colisões não pausam a simulação (o painel exibe a contagem regressiva). Terminado o intervalo, a próxima colisão volta a pausar.

**Como ler o painel do modo didático:** `Passo N / M` conta todas as ações do algoritmo (analisar uma partícula, visitar um nó da árvore ou testar um par); a linha entre parênteses mostra a composição de `M` (por exemplo, `200 partículas + 2793 nós + 200 testes`). Já `Testes` e `Nós` (visitados) mostram o progresso sobre o total do frame. Por isso `M` é bem maior que o `Testes` do painel normal: este conta só as comparações entre pares.

**Representação no canvas:**
- Anel branco: partícula sob análise no passo atual.
- Quadrado tracejado (Quadtree): região da *range query*.
- Quadrantes em ciano / vermelho: nós intersectados (descida na árvore) vs. nós descartados inteiros (poda espacial).
- Linhas amarelas / vermelhas: testes sem colisão vs. com colisão (o par que disparou a pausa permanece em verde).
- Durante a apresentação, eventos de mouse sobre o canvas são ignorados.

---

## Testes

Execute a suíte unitária nativa com Node.js:

```bash
node --test
```

Os **37 testes** em [`tests/`](./tests) cobrem exclusivamente a lógica pura (`src/particle.js`, `src/quadtree.js`, `src/simulation.js`), sem dependências externas nem acoplamento ao DOM.

---

## Benchmark de escala

Compara força bruta e Quadtree para `N` de `100` a `10000` partículas e raios `4` e `16`, sem navegador e sem dependências:

```bash
node bench/benchmark.js                     # tabela em Markdown (~40 s)
node bench/benchmark.js --csv               # saída CSV, para gráficos
node bench/benchmark.js --sizes=500,2000    # só alguns tamanhos
node bench/benchmark.js --frames=100        # mais frames por cenário (mais estável)
node bench/benchmark.js --distribution=cluster # reproduz o pior caso (aglomeração)

# Abrir painel HTML interativo com os resultados gravados (e benchmark ao vivo no navegador):
start "bench/benchmark.html"
```

Os resultados gravados nas 3 distribuições (`uniform`, `cluster`, `clusters`) ficam salvos em [`bench/results.json`](./bench/results.json) e renderizados no painel offline [`bench/benchmark.html`](./bench/benchmark.html).

Para cada cenário, mede a **mediana** do tempo por frame (em ms) da força bruta, da construção da árvore e da busca na Quadtree. O ganho é `bruta / (árvore + busca)`. A cada frame o script também confere que os dois algoritmos encontram exatamente os mesmos pares e falha com `AssertionError` se divergirem. Os tempos variam conforme a máquina; o que importa é a tendência com o crescimento de `N`.

---

## Estrutura do repositório

```text
quadtree_ttec/
├── index.html                           # Ponto de entrada da aplicação web
├── style.css                            # Estilos do canvas e do painel de controles
├── src/
│   ├── particle.js                      # Entidade Particle, bordas e resolveCollision
│   ├── quadtree.js                      # Rect e Quadtree (insert, subdivide, query)
│   ├── simulation.js                    # Step do frame, força bruta, Quadtree e buildTrace
│   ├── renderer.js                      # Renderização no Canvas 2D
│   └── main.js                          # Controles de UI, loop e máquina de estados didática
├── bench/
│   ├── benchmark.js                     # Benchmark de escala (força bruta x Quadtree)
│   ├── benchmark.html                   # Painel HTML interativo offline (cenas, SVG e execução ao vivo)
│   └── results.json                     # Medições gravadas nas 3 distribuições (Node v24.22.1)
├── tests/
│   ├── particle.test.js                 # Testes unitários de física e colisão
│   ├── quadtree.test.js                 # Testes unitários de subdivisão e range query
│   └── simulation.test.js               # Testes de detecção, SC-002 e trace didático
├── docs/
│   ├── README.md                        # Índice da documentação técnica
│   ├── arquitetura.md                   # Arquitetura dos módulos e máquina de estados
│   └── algoritmos-e-complexidade.md     # Análise assintótica e funcionamento da Quadtree
├── specs/                               # Especificações funcionais (001, 002, 003)
└── graphify-out/                        # Mapeamento estrutural gerado via /graphify
```

---

## Documentação e especificações

- Índice técnico: [`docs/README.md`](./docs/README.md)
- Arquitetura e contratos: [`docs/arquitetura.md`](./docs/arquitetura.md)
- Algoritmos e complexidade: [`docs/algoritmos-e-complexidade.md`](./docs/algoritmos-e-complexidade.md)
- Relatório estrutural (`/graphify`): [`graphify-out/GRAPH_REPORT.md`](./graphify-out/GRAPH_REPORT.md)
- Especificações: [`001-particle-collision-demo`](./specs/001-particle-collision-demo/spec.md), [`002-didactic-step-mode`](./specs/002-didactic-step-mode/spec.md), [`003-collision-triggered-didactic`](./specs/003-collision-triggered-didactic/spec.md)

---

## Integrantes

- **Gustavo** — [@gcontiero11](https://github.com/gcontiero11)
- **Heitor** — [@heitorlemescaldas](https://github.com/heitorlemescaldas)
- **Ian** — [@Iofsoft](https://github.com/Iofsoft)
- **Rafael** — [@RaFeltrim](https://github.com/RaFeltrim)
