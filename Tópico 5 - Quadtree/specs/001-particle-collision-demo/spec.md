# Feature Specification: Demo de Colisão de Partículas com Quadtree

**Feature Branch**: `001-particle-collision-demo`

**Created**: 2026-11-09

**Status**: Draft

**Input**: User description: "Demo visual de colisão entre partículas circulares que quicam na tela. Dois modos alternáveis: força bruta (todos contra todos) e Quadtree. Mostrar na tela: FPS, número de testes de colisão por frame, número de partículas. Controles: slider de quantidade de partículas, botão de alternar modo, checkbox para exibir a grade da Quadtree. Partículas em colisão ficam vermelhas. Extra: arrastar o mouse para selecionar uma região e destacar as partículas encontradas pela range query."

## Clarifications

### Session 2026-11-09

- Q: As partículas devem ricochetear umas nas outras ou só mudar de cor? → A: Devem
  ricochetear (colisão física), além de ficarem vermelhas — aumenta a carga e evidencia
  a diferença de desempenho entre os modos.
- Q: A área de desenho acompanha o redimensionamento da janela? → A: Sim, a área se
  ajusta ao tamanho da janela e a simulação recomeça.
- Q: Como funciona o tamanho das bolinhas? → A: Todas sempre com o mesmo raio,
  escolhido pelo usuário entre as potências de 2 de 2 a 32 px (2, 4, 8, 16, 32);
  mudar o raio recomeça a simulação (não muda em tempo real).
- Q: Mudar a quantidade de partículas no slider também recomeça a simulação? → A: Sim,
  recomeça com a nova quantidade (mesmo comportamento do raio e da janela).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ver partículas quicando e colidindo (Priority: P1)

O estudante abre a demo e vê várias partículas circulares se movendo e quicando nas
bordas da área de desenho. Quando duas partículas se sobrepõem, ambas ficam vermelhas
enquanto estiverem sobrepostas. Um painel mostra FPS, número de partículas e número
de testes de colisão realizados no frame.

**Why this priority**: é a base da demo; sem a simulação e a detecção visível não há
nada a comparar.

**Independent Test**: abrir a demo e observar partículas em movimento, quicando nas
bordas, mudando para vermelho ao se tocarem e o painel atualizando os números.

**Acceptance Scenarios**:

1. **Given** a demo aberta, **When** ela carrega, **Then** uma quantidade padrão de
   partículas aparece em posições e direções aleatórias e começa a se mover.
2. **Given** uma partícula chegando à borda, **When** ela toca a borda, **Then** ela
   inverte a direção e permanece dentro da área.
3. **Given** duas partículas sobrepostas, **When** o frame é desenhado, **Then** ambas
   aparecem em vermelho; partículas sem sobreposição aparecem na cor normal.
4. **Given** duas partículas que se tocam aproximando-se, **When** a colisão é
   resolvida, **Then** elas ricocheteiam (trocam velocidade na direção do contato) e
   são separadas para não ficarem grudadas.
5. **Given** a simulação rodando, **When** o usuário redimensiona a janela, **Then** a
   área de desenho acompanha o novo tamanho e a simulação recomeça com as partículas
   redistribuídas na nova área.
6. **Given** a simulação rodando, **When** o usuário escolhe outro raio (2, 4, 8, 16 ou
   32 px),
   **Then** a simulação recomeça com todas as partículas no novo raio.
7. **Given** a simulação rodando, **When** o tempo passa, **Then** o painel mostra FPS,
   número de partículas e testes de colisão do frame atual, atualizados continuamente.

---

### User Story 2 - Comparar força bruta e Quadtree (Priority: P1)

O estudante alterna entre o modo força bruta (cada partícula testada contra todas as
outras) e o modo Quadtree, e ajusta a quantidade de partículas com um slider, vendo
como o número de testes e o FPS mudam em cada modo.

**Why this priority**: é o objetivo didático central — mostrar o ganho da Quadtree.

**Independent Test**: com muitas partículas, alternar o modo e verificar que o número
de testes no modo Quadtree é bem menor que no modo força bruta, com as mesmas
partículas ficando vermelhas nos dois modos.

**Acceptance Scenarios**:

1. **Given** a demo em força bruta com N partículas, **When** o frame é processado,
   **Then** o número de testes exibido é N×(N−1)/2.
2. **Given** a demo em qualquer modo, **When** o usuário clica no botão de alternar,
   **Then** o modo muda, o modo atual fica indicado na tela e a simulação continua sem
   reiniciar.
3. **Given** o mesmo estado de partículas, **When** comparados os dois modos, **Then**
   o conjunto de partículas em colisão é idêntico.
4. **Given** o slider de quantidade, **When** o usuário o move, **Then** a simulação
   recomeça com a quantidade de partículas indicada no slider.

---

### User Story 3 - Visualizar a grade da Quadtree (Priority: P2)

O estudante marca um checkbox para desenhar as subdivisões da Quadtree sobre as
partículas, vendo como a árvore se refina onde há mais partículas.

**Why this priority**: ajuda a entender a estrutura, mas a comparação já funciona sem
ela.

**Independent Test**: marcar o checkbox e ver retângulos das subdivisões, mais densos
onde há aglomeração; desmarcar e vê-los sumir.

**Acceptance Scenarios**:

1. **Given** o checkbox marcado, **When** o frame é desenhado, **Then** os limites de
   todos os nós da Quadtree do frame aparecem sobre a área.
2. **Given** o checkbox desmarcado, **When** o frame é desenhado, **Then** nenhuma
   grade aparece.

---

### User Story 4 - Selecionar região com o mouse (range query) (Priority: P3)

O estudante clica e arrasta o mouse para desenhar um retângulo de seleção; as
partículas encontradas pela consulta por região da Quadtree ficam destacadas.

**Why this priority**: recurso extra que demonstra outra operação da Quadtree.

**Independent Test**: arrastar um retângulo sobre um grupo de partículas e verificar
que exatamente as que estão dentro dele ficam destacadas.

**Acceptance Scenarios**:

1. **Given** a demo rodando, **When** o usuário arrasta o mouse, **Then** um retângulo
   de seleção é desenhado do ponto inicial até a posição atual do cursor.
2. **Given** um retângulo de seleção (durante o arrasto ou após soltar o mouse),
   **When** o frame é desenhado, **Then** as
   partículas cujo centro está dentro dele aparecem com um destaque distinto do
   vermelho de colisão, e a quantidade encontrada é exibida.
3. **Given** uma seleção ativa, **When** o usuário clica sem arrastar, **Then** a
   seleção é removida.

---

### Edge Cases

- Slider no mínimo (10 partículas): a demo funciona normalmente; com poucas partículas
  pode não haver nenhuma colisão.
- Muitas partículas no mesmo ponto: a Quadtree não pode subdividir indefinidamente
  (há profundidade máxima) e a demo continua funcionando.
- Partícula que cruza a fronteira entre quadrantes: colisões com partículas do
  quadrante vizinho continuam sendo detectadas.
- Retângulo de seleção arrastado em qualquer direção (para cima/esquerda): funciona
  igual.
- Seleção ativa enquanto as partículas se movem: o destaque acompanha quem está
  dentro da região a cada frame.
- Mudança de quantidade, raio ou tamanho da janela: a simulação sempre recomeça do
  zero com os novos parâmetros (o modo e a grade escolhidos são mantidos).
- Muitas partículas grandes (ex.: 2000 de raio 32 px) podem não caber sem sobreposição:
  a simulação começa mesmo assim e as colisões as separam.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A demo MUST simular partículas circulares com posição, velocidade e
  raio, movendo-se a cada frame e quicando nas bordas da área de desenho.
- **FR-002**: A demo MUST detectar, a cada frame, quais partículas se sobrepõem a
  pelo menos uma outra e desenhá-las em vermelho.
- **FR-002a**: Partículas em colisão MUST ricochetear entre si (resposta elástica) e
  ser separadas quando sobrepostas, nos dois modos.
- **FR-002b**: A área de desenho MUST se ajustar ao redimensionamento da janela, e a
  simulação MUST recomeçar com as partículas distribuídas na nova área.
- **FR-002c**: Todas as partículas MUST ter o mesmo raio; usuários MUST poder escolher
  o raio apenas entre os valores 2, 4, 8, 16 e 32 px (potências de 2), e a mudança
  MUST recomeçar a simulação.
- **FR-003**: A demo MUST oferecer dois modos de detecção: força bruta (todos os pares)
  e Quadtree (cada partícula testada apenas contra as candidatas próximas).
- **FR-004**: Os dois modos MUST produzir o mesmo conjunto de partículas em colisão.
- **FR-005**: A demo MUST exibir continuamente FPS, número de partículas, número de
  testes de colisão no frame e o modo atual.
- **FR-006**: Um teste de colisão MUST ser contado cada vez que um par de partículas é
  comparado; no modo Quadtree cada par é contado no máximo uma vez por frame.
- **FR-007**: Usuários MUST poder ajustar a quantidade de partículas por um slider,
  com o valor atual visível; a mudança MUST recomeçar a simulação com a nova
  quantidade.
- **FR-008**: Usuários MUST poder alternar o modo por um botão, sem reiniciar a
  simulação.
- **FR-009**: Usuários MUST poder exibir/ocultar a grade da Quadtree por um checkbox.
- **FR-010**: Usuários MUST poder arrastar o mouse para definir uma região retangular;
  as partículas encontradas pela consulta por região da Quadtree MUST ser destacadas
  e sua quantidade exibida.
- **FR-011**: A Quadtree MUST ter capacidade por nó e profundidade máxima definidas,
  evitando subdivisão infinita.
- **FR-012**: A lógica de detecção (Quadtree, geometria, força bruta) MUST ser
  verificável por testes automatizados independentes da interface.

### Key Entities

- **Partícula**: círculo com posição, velocidade, raio e estado "em colisão" /
  "selecionada".
- **Retângulo**: região alinhada aos eixos usada como limite de nós e como seleção.
- **Quadtree**: árvore reconstruída a cada frame; cada nó tem um retângulo, uma
  capacidade, os itens que guarda e até quatro filhos.
- **Estatísticas do frame**: FPS, número de partículas, testes de colisão, itens
  encontrados na seleção.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A demo abre e começa a animar em menos de 2 segundos após abrir o
  arquivo, sem nenhuma instalação.
- **SC-002**: Com 1000 partículas, o modo Quadtree realiza pelo menos 10× menos
  testes de colisão por frame que o modo força bruta.
- **SC-003**: Com 1000 partículas, o FPS no modo Quadtree é pelo menos 2× o FPS do modo
  força bruta em um computador comum (verificação manual pelo painel).
- **SC-004**: Em 100% dos frames verificados por teste, os dois modos marcam o mesmo
  conjunto de partículas em colisão.
- **SC-005**: Um estudante consegue, em menos de 1 minuto e sem instruções extras,
  alternar o modo, mudar a quantidade e ver a diferença no número de testes.

## Assumptions

- Slider de 10 a 2000 partículas, valor inicial 200; raio inicial 4 px; velocidades
  aleatórias; todas as partículas têm a mesma massa.
- Profundidade máxima da Quadtree pequena (ordem de 6–8 níveis): impede subdivisão
  infinita quando muitas partículas se acumulam no mesmo ponto, sem criar nós menores
  que uma partícula.
- A Quadtree é reconstruída do zero a cada frame (abordagem mais simples).
- A seleção considera o centro da partícula dentro do retângulo.
- A grade e a seleção usam a Quadtree mesmo quando o modo força bruta está ativo.
- Uso em navegador de desktop com mouse; toque/celular fora do escopo.
