# Implementation Plan: Modo Didático Passo a Passo

**Branch**: `002-didactic-step-mode` | **Date**: 2026-11-16 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-didactic-step-mode/spec.md`

## Summary

Adicionar à demo da feature 001 um modo didático que pausa o frame no instante da
detecção e permite percorrer, com as setas do teclado, cada iteração do algoritmo
(início de partícula, visita a nó da Quadtree, teste de par). A abordagem: dividir o
`step()` da simulação em duas metades (mover + montar árvore / detectar + resolver) e,
entre elas, gerar com uma função pura `buildTrace` a lista de passos que a detecção
faria. A busca da Quadtree ganha um parâmetro opcional para registrar o caminho
percorrido, incluindo as partículas encontradas em cada nó, o que permite intercalar os
testes logo após a visita a cada nó (clarificação). O modo só liga com até 200
partículas. O desenho e o teclado ficam em `renderer.js` e `main.js`.

## Technical Context

**Language/Version**: JavaScript (ES2020+) em scripts clássicos no navegador; Node 22
para os testes (mesmo da feature 001).

**Primary Dependencies**: nenhuma (Canvas 2D, eventos de teclado nativos; `node:test`).

**Storage**: N/A

**Testing**: `node --test`, só na lógica pura (`quadtree.js`, `simulation.js`).

**Target Platform**: navegador de desktop com teclado, abrindo `index.html` em `file://`.

**Project Type**: aplicação web estática (extensão da demo existente).

**Performance Goals**: resposta imediata a cada tecla com até 200 partículas (SC-002).

**Constraints**: sem dependências, sem build; a sequência didática deve fazer
exatamente os mesmos testes da detecção normal (FR-010); modo didático limitado a 200
partículas (FR-001a), o que mantém o trace em no máximo ~20 mil passos.

**Scale/Scope**: alterações em 5 arquivos existentes + testes; nenhum arquivo novo de
código.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Princípio / Regra | Status | Observação |
|---|---|---|
| I. Simplicidade | ✅ | Sem novos módulos; trace é uma lista de objetos simples; reaproveita `query` e `particlesOverlap`. Lista gerada inteira, viável pelo limite de 200 partículas — R3. |
| II. Código didático | ✅ | O próprio recurso é didático; `step()` explicitamente dividido em duas metades nomeadas. |
| III. Quadtree do zero | ✅ | Caminho da busca registrado pela própria `query`. |
| IV. Testes só na lógica pura | ✅ | Testes para `query` com caminho e `buildTrace`; desenho e teclado verificados manualmente. |
| V. Zero dependências | ✅ | Nada novo. |
| Demo abre pelo `index.html` | ✅ | Continua com scripts clássicos. |
| Commits sem coautoria, testes passando | ✅ | Mantido nas tasks. |

**Pós-design (Phase 1)**: reavaliado — nenhuma violação; Complexity Tracking vazio.

## Project Structure

### Documentation (this feature)

```text
specs/002-didactic-step-mode/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── modules.md
└── tasks.md             # /speckit-tasks
```

### Source Code (repository root)

```text
index.html               # + botão #stepBtn "Modo didático" e aviso #notice
src/
├── quadtree.js          # query(range, found, visited) registra o caminho e o que cada nó achou
├── simulation.js        # step() = moveAndBuildTree() + detectAndResolve(); buildTrace()
├── renderer.js          # drawTrace()
└── main.js              # estado do trace, botão, teclado, painel do modo didático
tests/
├── quadtree.test.js     # + teste da query com caminho
└── simulation.test.js   # + testes de buildTrace e da divisão do step
README.md                # + seção do modo didático
```

**Structure Decision**: mesma estrutura da feature 001; só extensões nos arquivos
existentes. `particle.js` e `style.css` não mudam.

## Complexity Tracking

Nenhuma violação a justificar.
