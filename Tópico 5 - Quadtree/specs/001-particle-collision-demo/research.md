# Research: Demo de Colisão de Partículas com Quadtree

## R1. Como carregar os módulos abrindo `index.html` direto do disco

- **Decision**: scripts clássicos (`<script src="...">`) carregados em ordem, com
  declarações no escopo global compartilhado da página.
- **Rationale**: Chrome, Edge e Firefox bloqueiam `<script type="module">` em
  `file://` (tratado como origem cruzada), o que violaria a constituição ("demo roda
  abrindo o index.html"). Scripts clássicos funcionam em `file://` sem servidor.
- **Alternatives considered**: ES modules + servidor local (exige emendar a
  constituição); arquivo único (perde a divisão em módulos e dificulta testes).

## R2. Mesmo código no navegador e nos testes do Node

- **Decision**: cada arquivo de lógica termina com
  `if (typeof module !== 'undefined') module.exports = { ... }`. Em `simulation.js`,
  que usa `particle.js` e `quadtree.js`, o topo faz, apenas no Node:
  `if (typeof require !== 'undefined') Object.assign(globalThis, require('./particle.js'), require('./quadtree.js'))`.
  Testes usam `require('../src/x.js')`.
- **Rationale**: sem `package.json`, o Node trata `.js` como CommonJS; no navegador
  `module`/`require` não existem e os blocos são ignorados. Não se pode usar
  `var { Quadtree } = require(...)` em `simulation.js`: no navegador o `var` seria
  içado e colidiria com a `class Quadtree` global já declarada (SyntaxError).
- **Alternatives considered**: bundler (proibido), duplicar código para testes
  (contraria simplicidade).

## R3. Reconstruir a Quadtree a cada frame vs. atualizar incrementalmente

- **Decision**: reconstruir do zero a cada frame (`new Quadtree` + inserir todas).
- **Rationale**: todas as partículas se movem em todo frame; atualização incremental
  exigiria remoção, reinserção e fusão de nós, com ganho pequeno ou nulo. Reconstruir
  é O(n log n) e muito mais didático. A árvore é construída em todo frame, inclusive no
  modo força bruta, pois a grade e a seleção a usam; esse custo é desprezível perto de
  O(n²).
- **Alternatives considered**: atualização incremental; loose quadtree; grade uniforme
  (spatial hash) — fora do foco do projeto.

## R4. Parâmetros da Quadtree

- **Decision**: capacidade 4 por nó, profundidade máxima 8. A árvore guarda o centro
  das partículas (pontos).
- **Rationale**: a profundidade máxima impede subdivisão infinita quando muitas
  partículas se acumulam (ex.: 2000 partículas de raio 32). Com tela ~2000 px, o nível 8
  tem nós de ~8 px, perto do diâmetro das menores bolinhas (4 px); dividir mais não
  ajuda. Nós no nível máximo simplesmente aceitam itens além da capacidade.
- **Alternatives considered**: profundidade calculada pelo raio (mais complexo, ganho
  pequeno).

## R5. Busca de candidatos e contagem de testes no modo Quadtree

- **Decision**: para cada partícula `p`, consultar o retângulo centrado em `p` com meia
  largura `2r` (todas as partículas que podem tocá-la têm o centro a ≤ 2r). Para cada
  candidata `q` com `q.id > p.id`, contar um teste e verificar `distância < 2r`.
- **Rationale**: como todos têm o mesmo raio, guardar só pontos e expandir a busca é o
  mais simples. A regra `q.id > p.id` garante que cada par é testado e contado uma vez
  (FR-006), igual à força bruta, que percorre `i < j`.
- **Alternatives considered**: guardar círculos/retângulos na árvore (inserção em
  múltiplos nós, mais complexo).

## R6. Detecção e resposta de colisão

- **Decision**: em cada frame: (1) mover partículas e quicar nas bordas; (2) construir
  a Quadtree; (3) **detectar** todos os pares em colisão (força bruta ou Quadtree) com as
  posições congeladas; (4) **resolver** os pares: separar metade da sobreposição para
  cada lado e, se estiverem se aproximando, trocar as componentes de velocidade ao longo
  da normal (colisão elástica com massas iguais); (5) marcar as partículas dos pares
  como `colliding`.
- **Rationale**: separar detecção e resolução garante que os dois modos encontrem
  exatamente o mesmo conjunto de pares (FR-004, SC-004), testável sem a UI. Massas
  iguais tornam a fórmula elástica uma simples troca de componentes normais.
  Caso de centros coincidentes: usar normal (1, 0).
- **Alternatives considered**: resolver durante a detecção (resultado dependeria da
  ordem e os modos divergiriam).

## R7. Tempo e FPS

- **Decision**: velocidades em px por frame (sem `dt`); FPS medido em `main.js` com
  `performance.now()` e média suavizada, atualizada no painel algumas vezes por segundo.
- **Rationale**: mais simples. Como efeito colateral, quando o FPS cai a simulação fica
  mais lenta, o que torna a diferença de desempenho entre os modos visível.
- **Alternatives considered**: integração com `dt` real (mais código, esconde a queda
  de desempenho).

## R8. Redimensionamento e reinício

- **Decision**: canvas ocupa a janela inteira; no evento `resize`, ajustar o canvas e
  chamar `reset` da simulação. Mudanças no slider de quantidade e no seletor de raio
  também chamam `reset`. Modo e grade são preservados; a seleção é sempre limpa no
  reset (mais simples e evita seleção fora da nova área).
- **Rationale**: um único caminho de reinício (decisão da clarificação).
- **Alternatives considered**: debounce do resize (desnecessário; reset é barato).
