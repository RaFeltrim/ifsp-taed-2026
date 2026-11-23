# Contracts: mudanças nas APIs e controles

Complementa os contratos das features 001 e 002. Estados em
[data-model.md](../data-model.md).

## `src/simulation.js` — exporta também `findPairStepIndex`

| Função | Contrato |
|---|---|
| `sim.detect()` | Devolve `{ pairs, tests }` da detecção do modo atual e atualiza `sim.tests`. Não move, não resolve, não altera `colliding`/`selected`. Mesmos pares que `findPairsBruteForce` / `findPairsQuadtree`, na mesma ordem. |
| `sim.resolve(pairs)` | Zera `colliding`, resolve cada par (ricochete) marcando os dois como `colliding`, aplica a seleção. |
| `sim.detectAndResolve()` | `resolve(detect().pairs)`; resultado idêntico ao da feature 002. |
| `findPairStepIndex(steps, a, b)` | Índice do passo `{ type: 'test' }` cujo par é `{a, b}` (em qualquer ordem); `-1` se não houver. |

## `src/renderer.js` (não testado)

`drawTrace(ctx, sim, steps, index, showGrid, pair)`: igual à feature 002, com:
- `pair` (`[a, b]` ou `null`): essas duas partículas preenchidas em **verde** em todos os
  passos;
- linha do teste atual sem colisão em **amarelo**; nós que tocam a região em **ciano**;
  grade completa no verde suave da feature 001 (distinto do verde vivo do par); vermelho mantido para colisões encontradas e nós
  descartados. Nenhum outro elemento usa o verde vivo do par.

## Controles e painel (`src/main.js`, não testado)

| Estado | Comportamento | Painel |
|---|---|---|
| `'off'` | Como sempre. | Estatísticas normais. |
| `'waiting'` | Animação normal; pausa no primeiro frame com colisão. | Estatísticas normais + "Modo didático: aguardando colisão". |
| `'presenting'` | Apresentação passo a passo (setas, Shift da 002); **Enter** vai ao teste do par; **Esc** encerra; → no último passo encerra. | "MODO DIDÁTICO (modo)", "Colisão apresentada: #a × #b", "Passo k / N", descrição, testes e colisões até ali; no passo do par, "← colisão que disparou a pausa"; dica: "→ ← passo · Shift partícula · Enter colisão · Esc continuar". |
| `'cooldown'` | Animação normal, sem pausas. | Estatísticas normais + "Modo didático: próxima pausa em N s". |

Outros controles:

| Controle | Comportamento |
|---|---|
| Botão `#stepBtn` | Liga (→ `'waiting'`) / desliga (→ `'off'`, resolvendo o frame se estiver apresentando). Rótulo mostra ligado/desligado. Limite de 200 com aviso, como na 002. |
| Botão de modo de detecção | Em `'presenting'`: refaz os passos do mesmo frame com o outro algoritmo, mesmo par em verde, volta ao passo 1. |
| Quantidade / raio / janela | Recomeça; com o modo ligado vai para `'waiting'` (ou `'off'` com aviso se > 200). |
| Mouse no canvas | Ignorado só em `'presenting'`; em `'waiting'` e `'cooldown'` a seleção funciona normalmente. |
