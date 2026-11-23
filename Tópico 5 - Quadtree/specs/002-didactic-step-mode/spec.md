# Feature Specification: Modo Didático Passo a Passo

**Feature Branch**: `002-didactic-step-mode`

**Created**: 2026-11-16

**Status**: Draft

**Input**: User description: "preciso que ele tenha algum modo didático que permita ele mostrar o \"caminho\" até a encontrar a colisão, deve ter algum jeito da gente passar para o lado, com a seta do teclado para passar as iterações manualmente, assim seria possível ver o algoritmo encontrando a colisão na prática"

**Contexto**: estende a demo da feature `001-particle-collision-demo` (partículas que
colidem, modos força bruta e Quadtree, painel, grade e seleção por região).

## Clarifications

### Session 2026-11-16

- Q: No modo Quadtree, os testes com as partículas de um nó aparecem quando a busca
  chega nele ou só depois de percorrer a árvore inteira? → A: Intercalado — ao visitar
  um nó que toca a região, testa ali mesmo as partículas daquele nó que estão dentro da
  região, e depois continua descendo.
- Q: O modo didático deve ter algum limite de quantidade de partículas? → A: Sim, só
  liga com até 200 partículas; acima disso o controle avisa que é preciso reduzir.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Percorrer a detecção iteração por iteração (Priority: P1)

O estudante liga o modo didático. A simulação congela no instante em que as colisões
do frame vão ser procuradas. Cada toque na seta → avança uma iteração do algoritmo e a
tela mostra o que ele está fazendo naquele momento: qual partícula está sendo
analisada e com qual outra ela está sendo comparada, e se as duas colidem. A seta ←
volta uma iteração.

**Why this priority**: é o núcleo do pedido — ver o algoritmo encontrando a colisão na
prática, no ritmo do estudante.

**Independent Test**: com poucas partículas, ligar o modo didático, avançar e voltar
com as setas e conferir que cada passo mostra a comparação atual e o resultado.

**Acceptance Scenarios**:

1. **Given** a simulação rodando, **When** o usuário liga o modo didático, **Then** o
   movimento para e o painel mostra o passo atual, o total de passos do frame e uma
   frase explicando o passo.
2. **Given** o modo didático ligado, **When** o usuário pressiona →, **Then** a demo
   avança exatamente uma iteração e a tela destaca a partícula analisada, a partícula
   com que ela está sendo comparada e o resultado (colisão ou não).
3. **Given** um passo qualquer depois do primeiro, **When** o usuário pressiona ←,
   **Then** a demo volta exatamente uma iteração e a tela mostra o estado daquele passo.
4. **Given** um passo qualquer, **When** colisões já foram encontradas em passos
   anteriores do mesmo frame, **Then** as partículas dessas colisões aparecem em
   vermelho e o painel mostra quantos testes e quantas colisões houve até ali.
5. **Given** o modo didático ligado, **When** o usuário o desliga, **Then** a simulação
   volta a rodar normalmente a partir de onde parou.
6. **Given** mais de 200 partículas, **When** o usuário tenta ligar o modo didático,
   **Then** o modo não liga e a tela avisa que é preciso reduzir para até 200.

---

### User Story 2 - Ver o caminho da Quadtree até as candidatas (Priority: P1)

No modo Quadtree, antes dos testes de cada partícula, o estudante vê o caminho da busca
na árvore: a região de busca ao redor da partícula e, passo a passo, cada nó
visitado — os que tocam a região (a busca desce por eles) e os que ficam de fora
(descartados inteiros, sem olhar o que há dentro).

**Why this priority**: é a parte que explica *por que* a Quadtree faz menos testes; sem
ela o estudante só vê menos comparações, sem entender de onde vêm.

**Independent Test**: no modo Quadtree, avançar pela análise de uma partícula e
conferir que os nós aparecem na ordem da busca, diferenciando visitados e descartados,
e que os testes com as candidatas de um nó aparecem logo após a visita a esse nó.

**Acceptance Scenarios**:

1. **Given** o modo didático em Quadtree, **When** começa a análise de uma partícula,
   **Then** a região de busca ao redor dela é desenhada.
2. **Given** a análise de uma partícula em Quadtree, **When** o usuário avança,
   **Then** cada passo mostra um nó da árvore sendo visitado, com destaque diferente
   para nós que tocam a região e nós descartados.
3. **Given** a visita a um nó que toca a região e contém partículas dentro dela,
   **When** o usuário avança, **Then** os passos seguintes são os testes da partícula
   analisada com essas partículas, e só depois a busca continua para o próximo nó.
4. **Given** o modo didático em força bruta, **When** o usuário avança, **Then** não há
   passos de árvore: cada passo é um teste com a próxima partícula, ligadas por uma
   linha, deixando visível que partículas distantes também são testadas.

---

### User Story 3 - Navegar rápido e seguir para o próximo frame (Priority: P2)

O estudante pula direto para a próxima (ou anterior) partícula com Shift + →/←, e ao
chegar ao fim das iterações do frame, → resolve as colisões encontradas, as partículas
se movem um frame e começa a detecção do frame seguinte.

**Why this priority**: com dezenas de partículas um frame tem muitos passos; sem atalho
e sem continuidade entre frames o modo fica cansativo.

**Independent Test**: usar Shift + → para pular partículas e chegar ao fim do frame;
pressionar → e ver as partículas se moverem e a contagem de passos reiniciar.

**Acceptance Scenarios**:

1. **Given** um passo da análise de uma partícula, **When** o usuário pressiona
   Shift + →, **Then** a demo vai para o primeiro passo da próxima partícula.
2. **Given** um passo da análise de uma partícula, **When** o usuário pressiona
   Shift + ←, **Then** a demo vai para o início da partícula anterior (ou da atual, se
   não estiver no início dela).
3. **Given** o último passo do frame, **When** o usuário pressiona →, **Then** as
   colisões encontradas são resolvidas (ricochete), as partículas avançam um frame e o
   modo didático recomeça no primeiro passo do novo frame.
4. **Given** o modo didático ligado, **When** o usuário troca o modo de detecção,
   **Then** as iterações do mesmo frame são refeitas com o outro algoritmo, a partir do
   primeiro passo.

---

### Edge Cases

- Mais de 200 partículas: o modo didático não liga e a tela avisa para reduzir. Se o
  modo estiver ligado e o usuário aumentar a quantidade acima de 200, a simulação
  recomeça com o modo didático desligado e o mesmo aviso aparece. O aviso some quando a
  simulação recomeça com até 200 partículas ou quando o modo liga.
- Setas pressionadas com o foco em um controle do painel (ex.: slider): no modo
  didático as setas controlam os passos e não alteram o controle.
- Segurar a seta: repete o avanço continuamente sem travar a demo.
- ← no primeiro passo do frame: permanece no primeiro passo (não volta a frames
  anteriores).
- Mudar quantidade, raio ou tamanho da janela com o modo ligado: a simulação recomeça
  e o modo didático continua ligado (se ainda houver até 200 partículas), no primeiro
  passo do novo frame.
- Partícula sem nenhuma candidata (Quadtree) ou a última partícula (força bruta):
  aparece o passo de início da análise, sem passos de teste.
- Desligar o modo no meio do frame: o frame é concluído (colisões resolvidas) e a
  animação continua.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Usuários MUST poder ligar e desligar o modo didático por um controle no
  painel; o estado (ligado/desligado) MUST ficar visível.
- **FR-001a**: O modo didático MUST ligar apenas com até 200 partículas; acima disso
  MUST permanecer desligado e exibir um aviso pedindo para reduzir a quantidade. Se a
  quantidade passar de 200 com o modo ligado, o modo MUST ser desligado com o mesmo
  aviso.
- **FR-002**: Com o modo ligado, a simulação MUST ficar pausada no instante da detecção
  de colisões do frame atual.
- **FR-003**: A tecla → MUST avançar exatamente um passo e ← MUST voltar exatamente um
  passo, sem passar do primeiro passo do frame.
- **FR-004**: Shift + → MUST ir para o início da próxima partícula; Shift + ← MUST ir
  para o início da partícula atual ou, se já estiver nele, da anterior.
- **FR-005**: Os passos MUST ser de três tipos: início da análise de uma partícula,
  visita a um nó da árvore (só no modo Quadtree) e teste de um par.
- **FR-006**: Cada passo de visita MUST indicar se o nó toca a região de busca (a busca
  desce) ou não (descartado).
- **FR-006a**: No modo Quadtree, os testes MUST aparecer intercalados com as visitas:
  logo após a visita a um nó que toca a região, vêm os testes da partícula analisada
  com as partículas daquele nó que estão dentro da região; só então a busca segue.
- **FR-007**: Cada passo de teste MUST mostrar as duas partículas comparadas e o
  resultado (colisão ou não), incluindo a distância entre elas e a distância mínima
  para colidir.
- **FR-008**: A tela MUST destacar a partícula analisada, a região de busca (Quadtree),
  os nós e testes já percorridos para a partícula atual e, em vermelho, as partículas
  das colisões já encontradas no frame até o passo atual.
- **FR-009**: O painel MUST mostrar o número do passo, o total de passos do frame, uma
  descrição em texto do passo, os testes e as colisões acumulados até ali e um lembrete
  das teclas.
- **FR-010**: A sequência de passos MUST corresponder exatamente à detecção normal do
  mesmo frame e modo: mesmo número de testes e mesmos pares em colisão.
- **FR-011**: Ao avançar além do último passo, a demo MUST resolver as colisões
  encontradas, avançar um frame e reiniciar os passos para o novo frame.
- **FR-012**: Trocar o modo de detecção com o modo didático ligado MUST refazer os
  passos do mesmo frame com o outro algoritmo, começando do primeiro passo.
- **FR-013**: Com o modo didático ligado, as setas MUST controlar apenas os passos,
  mesmo que algum controle do painel esteja com o foco.
- **FR-014**: A geração dos passos MUST ser verificável por testes automatizados
  independentes da interface.

### Key Entities

- **Passo**: uma iteração da detecção; tem tipo (início de partícula, visita a nó,
  teste de par), a partícula analisada e, conforme o tipo, a região de busca, o nó
  visitado e se ele toca a região, ou a outra partícula e se colidem; guarda também os
  totais acumulados de testes e colisões.
- **Sequência de passos do frame**: lista ordenada de passos de um frame, com a posição
  atual que o usuário está vendo; é refeita a cada novo frame ou troca de modo.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Em 100% dos frames verificados por teste, o número de passos de teste e os
  pares em colisão da sequência didática são iguais aos da detecção normal, nos dois
  modos.
- **SC-002**: Cada toque de tecla atualiza a tela e o painel imediatamente
  (perceptivelmente sem atraso) com até 200 partículas.
- **SC-003**: Com 20 partículas, um estudante consegue, em menos de 2 minutos, seguir no
  modo Quadtree a análise de uma partícula do início ao fim e apontar quais nós foram
  descartados e qual colisão foi encontrada.
- **SC-004**: Com o mesmo frame, o estudante consegue comparar o total de passos de teste
  dos dois modos trocando o modo, sem perder o frame.

## Assumptions

- Partículas analisadas em ordem de identificador; em Quadtree, nós na ordem da busca,
  com os testes intercalados (FR-006a) e só com candidatas de identificador maior (cada
  par aparece uma vez). A ordem pode diferir da detecção normal, mas o total de testes e
  os pares em colisão são os mesmos (FR-010).
- Uma "iteração" é o menor passo útil para entender o algoritmo: visitar um nó ou testar
  um par; o início de cada partícula é um passo próprio para mostrar a região de busca.
- O movimento e o ricochete só acontecem ao passar do último passo (ou ao desligar o
  modo); dentro do frame as posições ficam congeladas.
- A grade completa da Quadtree continua controlada pelo checkbox existente; os nós
  visitados pela partícula atual são sempre destacados.
- No modo didático o mouse é ignorado: arrastar não cria nem altera a seleção por
  região; uma seleção que já existia volta a aparecer ao desligar o modo.
- Uso em desktop com teclado; não há controles por toque.
