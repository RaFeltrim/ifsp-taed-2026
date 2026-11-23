# Quickstart: Modo Didático Passo a Passo

## Pré-requisitos

Os mesmos da feature 001: navegador de desktop com teclado; Node 18+ só para testes.

## Rodar os testes

```bash
node --test
```

Esperado: testes antigos continuam passando, mais os novos de `query` com caminho e de
`buildTrace` (mesmos testes e pares da detecção normal nos dois modos).

## Validação manual

Abrir `index.html`, colocar o slider em ~20 partículas e o raio em 16 (mais colisões).

| # | Ação | Resultado esperado |
|---|---|---|
| 1 | Clicar "Modo didático" | Movimento para; painel mostra "Passo 1 / N" e a descrição. |
| 2 | Em força bruta, pressionar → várias vezes | Cada passo liga a partícula analisada a outra com uma linha; pares que colidem ficam vermelhos; contadores sobem. |
| 3 | Pressionar ← | Volta exatamente um passo; em "Passo 1" permanece nele. |
| 4 | Trocar o modo de detecção para Quadtree (botão de modo) | Volta ao passo 1 do mesmo frame; N bem menor que em força bruta. |
| 5 | Avançar em Quadtree | Região tracejada ao redor da partícula; nós visitados aparecem verdes, descartados vermelhos; logo após um nó com partículas na região vêm os testes com elas, e só então a busca segue. |
| 6 | Shift + → / Shift + ← | Pula para o início da próxima / anterior partícula. |
| 7 | Com o slider em foco, pressionar → | Avança o passo; o slider não muda. |
| 8 | Chegar ao último passo e pressionar → | Partículas se movem um frame (as que colidiram ricocheteiam) e volta ao passo 1. |
| 9 | Mudar o raio com o modo ligado | Simulação recomeça e o modo didático continua no passo 1. |
| 10 | Clicar "Modo didático" de novo | Animação volta ao normal. |
| 11 | Com 500 partículas, clicar "Modo didático" | Modo não liga; aviso pede para reduzir para até 200. |
| 12 | Com o modo ligado (20 partículas), mover o slider para 500 | Simulação recomeça com o modo desligado e o aviso aparece; voltar o slider para 20 faz o aviso sumir. |
| 13 | 200 partículas, força bruta, modo didático ligado, segurar → por alguns segundos | Tela e painel acompanham cada passo sem travar (SC-002). |
| 14 | Com o modo ligado, arrastar o mouse no canvas | Nada acontece (nenhum retângulo de seleção). |

APIs em [contracts/modules.md](./contracts/modules.md); passos em
[data-model.md](./data-model.md).
