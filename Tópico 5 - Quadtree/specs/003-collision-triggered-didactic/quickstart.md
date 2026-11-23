# Quickstart: Modo Didático Disparado por Colisão

## Pré-requisitos

Os mesmos das features anteriores: navegador de desktop com teclado; Node 18+ só para
testes.

## Rodar os testes

```bash
node --test
```

Esperado: testes antigos passando, mais os novos de `detect`/`resolve`, do par
apresentado (primeiro par da detecção) e de `findPairStepIndex`.

## Validação manual

Abrir `index.html`, colocar ~20 partículas e raio 16.

| # | Ação | Resultado esperado |
|---|---|---|
| 1 | Ligar o modo didático | Animação continua; painel mostra "aguardando colisão". |
| 2 | Esperar a primeira colisão | Animação pausa; duas partículas verdes; painel mostra "Colisão apresentada: #a × #b" e "Passo 1 / N". |
| 3 | Pressionar → / ← / Shift | Navegação como na feature 002; o par continua verde em todos os passos. |
| 4 | Pressionar Enter | Vai direto ao teste do par; painel marca "colisão que disparou a pausa". |
| 5 | Conferir as cores | Só o par em verde vivo: teste sem colisão amarelo, nós que tocam a região ciano, descartados vermelhos, grade (se ligada) em verde suave. |
| 6 | Trocar o modo de detecção durante a apresentação | Volta ao passo 1 com o outro algoritmo; o mesmo par segue verde; Enter acha o par de novo. |
| 7 | Pressionar Esc | Animação volta; painel mostra "próxima pausa em 5 s" contando para baixo. |
| 8 | Durante o intervalo | Colisões ricocheteiam sem pausar. |
| 9 | Fim do intervalo | Painel volta a "aguardando colisão"; a próxima colisão pausa. |
| 10 | Numa apresentação, ir até o último passo e pressionar → | Mesmo efeito do Esc. |
| 11 | Desligar durante a apresentação e durante o intervalo | Animação normal; nada mais pausa. |
| 12 | Mudar o raio com o modo ligado | Simulação recomeça e o modo volta a aguardar colisão. |
| 13 | Com 500 partículas, ligar o modo | Não liga; aviso de limite (como na 002). |
| 14 | Cronometrar do Esc até a próxima pausa possível | ~5 s (SC-002). |
| 15 | Arrastar o mouse durante a apresentação e depois durante o intervalo | Na apresentação nada acontece; no intervalo a seleção funciona normalmente. |

APIs em [contracts/modules.md](./contracts/modules.md); estados em
[data-model.md](./data-model.md).
