# Quickstart: Demo de Colisão de Partículas com Quadtree

## Pré-requisitos

- Navegador de desktop moderno (Chrome, Firefox ou Edge).
- Node 18+ apenas para rodar os testes (nada a instalar).

## Rodar a demo

Abrir `index.html` direto no navegador (duplo clique ou `xdg-open index.html`). Sem
servidor, sem build.

## Rodar os testes

```bash
node --test
```

Esperado: todos os testes de `particle`, `quadtree` e `simulation` passam.

## Validação manual (cenários da spec)

| # | Ação | Resultado esperado |
|---|---|---|
| 1 | Abrir a demo | 200 partículas de raio 4 se movem e quicam nas bordas; painel atualizando FPS, partículas e testes. |
| 2 | Observar encontros | Partículas que se tocam ficam vermelhas e ricocheteiam, sem grudar. |
| 3 | Modo força bruta com 200 partículas | Testes/frame = 19900 (200·199/2). |
| 4 | Slider em 1000, alternar modos | Quadtree mostra ≥10× menos testes e FPS ≥ 2× o da força bruta; simulação não reinicia ao trocar modo. |
| 5 | Marcar "Mostrar grade" | Retângulos da Quadtree aparecem, mais densos onde há aglomeração; desmarcar some. |
| 6 | Arrastar retângulo (inclusive para cima/esquerda) | Partículas com centro dentro ficam destacadas; painel mostra quantas. Clique simples limpa. |
| 7 | Mudar raio para 32 | Simulação recomeça com bolinhas grandes; modo e grade mantidos. |
| 8 | Redimensionar a janela | Canvas acompanha e a simulação recomeça na nova área. |
| 9 | 2000 partículas de raio 32 | Demo continua respondendo (profundidade máxima evita travamento). |

Detalhes das APIs em [contracts/modules.md](./contracts/modules.md); entidades em
[data-model.md](./data-model.md).
