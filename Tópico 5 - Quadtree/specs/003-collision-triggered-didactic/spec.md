# Feature Specification: Modo Didático Disparado por Colisão

**Feature Branch**: `003-collision-triggered-didactic`

**Created**: 2026-11-17

**Status**: Draft

**Input**: User description: "então o modo didático deveria mostrar este processo né? inclusive seria legal marcar em verde, as bolas que colidiram, no modo didático, portanto o modo didático espera uma colisão acontecer, para começar, e ao acabar em um delay de 5 segundos até outra colisão ativalos novamente (isso quando estiver com o modo ativo)"

**Contexto**: altera o modo didático da feature `002-didactic-step-mode`. Hoje, ao ligar,
ele pausa imediatamente qualquer frame (mesmo sem colisão). "Este processo" é o caminho
da detecção explicado ao usuário: a partícula analisada, a região de busca, os nós da
Quadtree descartados ou visitados e os testes com as candidatas até achar a colisão.

## Clarifications

### Session 2026-11-17

- Q: A apresentação cobre só a análise da partícula envolvida ou o frame inteiro? → A:
  O frame inteiro, começando do primeiro passo, com a tecla Enter levando direto ao
  passo em que a colisão apresentada é encontrada.
- Q: As partículas da colisão ficam verdes desde o início da apresentação ou só a
  partir do passo em que a colisão é encontrada? → A: Durante toda a apresentação.
- Q: A grade da Quadtree pode continuar verde durante a apresentação? → A: Sim, num
  verde levemente diferente (mais suave) do verde das partículas apresentadas.
- Q: O mouse fica ignorado durante todo o modo ou só durante a apresentação? → A: Só
  durante a apresentação.
- Q: Deve existir uma tecla para encerrar a apresentação na hora, sem ir até o último
  passo? → A: Sim, Esc encerra a qualquer momento (resolve as colisões, retoma a
  animação e inicia o intervalo de 5 s); → no último passo continua funcionando.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Pausar automaticamente quando uma colisão acontece (Priority: P1)

O estudante liga o modo didático e a animação continua rodando normalmente. Assim que
duas partículas colidem, a animação pausa e o modo didático mostra o processo que
encontrou essa colisão, passo a passo com as setas. As duas partículas que colidiram
ficam marcadas em verde.

**Why this priority**: é o núcleo do pedido — o modo didático passa a mostrar
justamente o momento interessante (uma colisão sendo encontrada), em vez de um frame
qualquer.

**Independent Test**: ligar o modo didático com poucas partículas, esperar a primeira
colisão e conferir que a animação pausa, as duas partículas ficam verdes e as setas
percorrem o processo que levou a essa colisão.

**Acceptance Scenarios**:

1. **Given** o modo didático ligado e nenhuma colisão no frame, **When** o tempo passa,
   **Then** a animação continua normalmente e o painel indica que o modo está
   aguardando uma colisão.
2. **Given** o modo didático ligado e aguardando, **When** duas partículas colidem,
   **Then** a animação pausa no instante da detecção e começa a apresentação passo a
   passo dessa colisão.
3. **Given** a apresentação de uma colisão, **When** a tela é desenhada, **Then** as
   duas partículas dessa colisão aparecem em verde durante toda a apresentação.
4. **Given** a apresentação de uma colisão, **When** ela começa, **Then** o passo
   exibido é o primeiro do frame (início da análise da primeira partícula).
5. **Given** a apresentação de uma colisão, **When** o usuário usa → / ← (e Shift),
   **Then** a navegação funciona como no modo didático atual.
6. **Given** qualquer passo da apresentação, **When** o usuário pressiona Enter,
   **Then** a demo vai direto ao passo em que a colisão apresentada é encontrada, e as
   setas continuam funcionando a partir dali.
7. **Given** a apresentação, **When** o usuário chega ao passo em que a colisão é
   encontrada, **Then** o painel destaca que aquela é a colisão que disparou a pausa.

---

### User Story 2 - Intervalo de 5 segundos entre apresentações (Priority: P1)

Depois que o estudante termina de ver uma colisão, a animação volta a rodar e, por 5
segundos, novas colisões acontecem normalmente sem pausar. Passado esse intervalo, a
próxima colisão pausa de novo.

**Why this priority**: sem o intervalo, com partículas colidindo o tempo todo, a demo
pausaria a cada frame e o estudante nunca veria o movimento.

**Independent Test**: terminar uma apresentação e cronometrar: colisões nos primeiros
5 segundos não pausam; a primeira colisão depois disso pausa.

**Acceptance Scenarios**:

1. **Given** o último passo da apresentação, **When** o usuário pressiona →, **Then** a
   colisão é resolvida (ricochete), a animação volta a rodar e começa um intervalo de 5
   segundos.
2. **Given** qualquer passo da apresentação, **When** o usuário pressiona Esc, **Then**
   acontece o mesmo que ao passar do último passo: colisões resolvidas, animação
   retomada e intervalo de 5 segundos iniciado.
3. **Given** o intervalo em andamento, **When** partículas colidem, **Then** elas
   ricocheteiam normalmente e a animação não pausa.
4. **Given** o intervalo em andamento, **When** o tempo passa, **Then** o painel mostra
   quantos segundos faltam para o modo voltar a aguardar colisões.
5. **Given** o intervalo terminado, **When** ocorre uma colisão, **Then** a animação
   pausa e uma nova apresentação começa.
6. **Given** o modo didático desligado, **When** ocorrem colisões, **Then** nada pausa
   (comportamento normal da demo).

---

### Edge Cases

- Várias colisões no mesmo frame: apenas uma é apresentada (a primeira encontrada pela
  ordem da detecção); as demais são resolvidas normalmente ao fim da apresentação.
- Ligar o modo didático com partículas já sobrepostas: a primeira detecção já encontra
  colisão e a apresentação começa no frame seguinte ao ligar.
- Desligar o modo durante a apresentação: o frame é concluído e a animação continua;
  desligar durante o intervalo cancela o intervalo.
- Trocar o modo de detecção durante a apresentação: a apresentação da mesma colisão é
  refeita com o outro algoritmo, mantendo as mesmas partículas em verde.
- Mudar quantidade, raio ou tamanho da janela com o modo ligado: a simulação recomeça e
  o modo volta a aguardar uma colisão (sem intervalo pendente).
- Mais de 200 partículas: mantém a regra da feature 002 (o modo não liga e avisa).
- Nenhuma colisão por muito tempo (poucas partículas pequenas): o modo continua
  aguardando indefinidamente, com a animação rodando.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Com o modo didático ligado, a animação MUST rodar normalmente até que a
  detecção de um frame encontre ao menos uma colisão; só então MUST pausar no instante
  da detecção, antes da resolução.
- **FR-002**: A apresentação MUST cobrir a detecção do frame inteiro, começando no
  primeiro passo, com os mesmos tipos de passo e a mesma navegação do modo didático
  atual (→ / ←, Shift + → / ←).
- **FR-002a**: A tecla Enter MUST levar, de qualquer passo da apresentação, direto ao
  passo em que a colisão apresentada é encontrada.
- **FR-003**: As duas partículas da colisão apresentada MUST aparecer em verde vivo
  durante toda a apresentação. Nenhum outro elemento MUST usar esse mesmo verde; a
  grade da Quadtree pode continuar verde, desde que num tom claramente mais suave.
- **FR-003a**: O mouse MUST ser ignorado durante a apresentação; nos estados
  "aguardando colisão" e "intervalo" a seleção por região funciona normalmente.
- **FR-004**: O passo em que a colisão apresentada é encontrada MUST ser identificado
  no painel como a colisão que disparou a pausa.
- **FR-005**: Ao avançar além do último passo, ou ao pressionar Esc em qualquer passo,
  a demo MUST encerrar a apresentação: resolver as colisões do frame, retomar a
  animação e iniciar um intervalo de 5 segundos.
- **FR-006**: Durante o intervalo, colisões MUST ser resolvidas normalmente sem pausar;
  ao fim do intervalo, o modo MUST voltar a aguardar a próxima colisão.
- **FR-007**: O painel MUST indicar o estado do modo didático: aguardando colisão,
  apresentando (passo k / N) ou em intervalo (segundos restantes).
- **FR-008**: Desligar o modo, recomeçar a simulação ou trocar o modo de detecção MUST
  seguir os casos de borda acima.
- **FR-009**: A escolha da colisão apresentada e a geração dos passos MUST ser
  verificáveis por testes automatizados independentes da interface.

### Key Entities

- **Estado do modo didático**: desligado, aguardando colisão, apresentando uma colisão
  ou em intervalo; no intervalo, guarda quando ele termina.
- **Colisão apresentada**: o par de partículas que disparou a pausa; define quais
  partículas ficam verdes e qual passo é destacado no painel.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Com o modo ligado, em 100% das vezes a pausa acontece no primeiro frame
  com colisão fora do intervalo, e nunca em um frame sem colisão.
- **SC-002**: O intervalo entre o fim de uma apresentação e a próxima pausa possível é
  de 5 segundos (±0,5 s), medido pelo painel ou por cronômetro.
- **SC-003**: Com 20 partículas, um estudante consegue, em menos de 1 minuto após uma
  pausa, apontar quais partículas colidiram e em qual passo a colisão foi encontrada
  (um toque em Enter leva a esse passo).
- **SC-004**: Em 100% das apresentações verificadas por teste, as partículas marcadas
  em verde são de fato um par em colisão no frame pausado.

## Assumptions

- "Ao acabar" significa o usuário passar do último passo com → ou pressionar Esc; não
  há avanço automático.
- O intervalo de 5 segundos conta tempo real a partir da retomada da animação.
- A colisão apresentada é a primeira encontrada pela ordem da detecção do modo atual
  (partícula de menor identificador e, entre os pares dela, o primeiro testado).
- Outras colisões do mesmo frame continuam aparecendo em vermelho quando encontradas
  nos passos; só o par apresentado fica verde.
- As cores atuais do modo didático que usam verde vivo (linha de teste sem colisão e
  nós que tocam a região) passam a usar outras cores; a grade mantém seu verde suave,
  diferente do verde vivo do par apresentado.
- O limite de 200 partículas e as teclas da feature 002 são mantidos.
- Fora do modo didático nada muda.
