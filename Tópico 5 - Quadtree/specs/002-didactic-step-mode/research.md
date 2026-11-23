# Research: Modo Didático Passo a Passo

## R1. Onde pausar o frame

- **Decision**: dividir `Simulation.step()` em `moveAndBuildTree()` (mover, quicar,
  reconstruir a árvore) e `detectAndResolve()` (detectar, resolver, aplicar seleção);
  `step()` chama as duas. O modo didático para entre elas.
- **Rationale**: a detecção precisa ver as posições *antes* do ricochete; depois da
  resolução os pares ficam só encostados e nenhuma colisão apareceria. A divisão também
  deixa explícitas as fases do frame (bom para o objetivo didático).
- **Alternatives considered**: guardar uma cópia das posições antes da resolução
  (duplica estado); gerar o trace dentro de `step()` sempre (custo em todo frame).

## R2. Como representar as iterações

- **Decision**: função pura `buildTrace(particles, tree, mode)` que refaz a detecção e
  devolve uma lista de passos `{ type: 'particle' | 'visit' | 'test', ... }`, cada um com
  totais acumulados `tests` e `collisions`. A navegação é só um índice nessa lista.
- **Rationale**: voltar (←) fica trivial (índice − 1); a lista é testável no Node e pode
  ser comparada com `findPairsBruteForce`/`findPairsQuadtree` (FR-010, SC-001).
- **Alternatives considered**: gerador (`function*`) avançando a detecção sob demanda —
  não permite voltar sem refazer; estado de máquina manual — mais código.

## R3. Custo da lista e limite de partículas

- **Decision**: gerar a lista inteira de uma vez (ao começar cada frame ou trocar de
  modo) e só permitir o modo didático com até 200 partículas (clarificação, FR-001a).
- **Rationale**: medido no Node: força bruta com 2000 partículas = ~2 milhões de passos,
  ~0,7 s e ~190 MB. Com o limite de 200, o pior caso é força bruta com 19.900 testes +
  200 passos de partícula ≈ 20 mil passos — instantâneo. O limite elimina a necessidade
  de geração sob demanda.
- **Alternatives considered**: sem limite, aceitando a pausa (rejeitado na
  clarificação); reduzir a quantidade automaticamente (muda o cenário sem o usuário
  pedir).

## R4. Registrar o caminho da Quadtree

- **Decision**: parâmetro opcional `visited` em `query(range, found = [], visited = null)`;
  cada nó visitado faz `visited.push({ node, hit, found })`: `hit` = o nó toca o range;
  `found` = itens *deste* nó que estão dentro do range (vazio se `hit = false` ou se o
  nó não é folha). Nós com `hit = false` não descem.
- **Rationale**: o caminho mostrado é o da busca real, não uma reimplementação; guardar
  `found` por nó permite intercalar os testes (R5) sem uma segunda busca. Sem
  `visited`, comportamento e custo são os de antes.
- **Alternatives considered**: callback por nó (mais abstrato para um projeto didático);
  função `queryTraced` separada (duplica a busca).

## R5. Ordem e conteúdo dos passos

- **Decision**: partículas em ordem de `id`. Força bruta: `particle` e depois `test` com
  cada `j > i`. Quadtree: `particle` (com a região de busca de lado 4r) e, para cada
  registro de `visited` na ordem da busca, um passo `visit` seguido imediatamente dos
  `test` com os itens daquele nó (`found`) de `id` maior (clarificação, FR-006a).
- **Rationale**: mostra a colisão sendo encontrada no meio do caminho pela árvore. Como
  a concatenação dos `found` de todos os nós é exatamente o resultado da `query`, o
  conjunto de testes e de pares é igual ao de `findPairsQuadtree` (FR-010); só a
  intercalação com as visitas é nova.
- **Alternatives considered**: todas as visitas primeiro e os testes depois (mesma ordem
  do código de detecção, mas menos ilustrativo — rejeitado na clarificação).

## R6. Teclado e navegação

- **Decision**: um listener `keydown` na janela, ativo só com o modo ligado; trata
  `ArrowRight`/`ArrowLeft` com e sem `shiftKey` e chama `preventDefault()` (evita mexer
  no slider em foco ou rolar a página — FR-013). → além do último passo chama
  `detectAndResolve()` + `moveAndBuildTree()` + novo trace. Shift+→ procura o próximo
  passo `particle`; Shift+← faz `index − 1` e volta até um passo `particle`.
- **Rationale**: o `preventDefault` no listener da janela (fase de bolha) ainda impede a
  ação padrão do controle em foco. Segurar a tecla gera repetições do evento, o que já
  dá o avanço contínuo.
- **Alternatives considered**: botões na tela para avançar/voltar (o usuário pediu
  setas).

## R7. Ligar, desligar, limite e reinícios

- **Decision**: ligar → se houver mais de 200 partículas, não liga e mostra o aviso em
  um elemento `#notice` do painel; senão `moveAndBuildTree()` + trace e limpa o aviso.
  Desligar → `detectAndResolve()` (conclui o frame). Trocar modo → refaz o trace do mesmo
  frame (sem mover). `restart()` (quantidade/raio/resize) → `reset` e, se ligado: com até
  200, novo frame didático; acima de 200, desliga o modo e mostra o aviso.
- **Rationale**: cumpre FR-001a, FR-011, FR-012 e os casos de borda com um único estado
  (`trace`) e uma constante (`MAX_TRACE_PARTICLES = 200`).
- **Alternatives considered**: desabilitar o botão enquanto houver mais de 200
  (exigiria atualizar o botão a cada mudança do slider; o aviso no clique é mais
  simples).
