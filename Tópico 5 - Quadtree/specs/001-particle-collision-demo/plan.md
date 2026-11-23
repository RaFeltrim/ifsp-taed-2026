# Implementation Plan: Demo de Colisão de Partículas com Quadtree

**Branch**: `001-particle-collision-demo` | **Date**: 2026-11-09 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-particle-collision-demo/spec.md`

## Summary

Demo no navegador com partículas circulares de mesmo raio que se movem, quicam nas
bordas e ricocheteiam entre si. A detecção de colisão alterna entre força bruta
(todos os pares) e uma Quadtree implementada do zero, reconstruída a cada frame. Um
painel mostra FPS, partículas e testes de colisão por frame; controles permitem mudar
quantidade, raio (2–32 px, potências de 2), modo, exibir a grade e selecionar uma
região com o mouse (range query). A lógica pura (geometria, Quadtree, física,
detecção) fica separada do desenho e é testada com `node --test`.

## Technical Context

**Language/Version**: JavaScript (ES2020+) em scripts clássicos no navegador; Node 22
para os testes.

**Primary Dependencies**: nenhuma (Canvas 2D nativo do navegador; `node:test` e
`node:assert` nativos do Node).

**Storage**: N/A

**Testing**: `node --test` com `node:assert/strict`, só na lógica pura
(`quadtree.js`, `particle.js`, `simulation.js`).

**Target Platform**: navegador de desktop moderno (Chrome, Firefox, Edge), abrindo o
`index.html` direto do disco (`file://`).

**Project Type**: aplicação web estática de página única (demo didática).

**Performance Goals**: FPS no modo Quadtree ≥ 2× o da força bruta com 1000 partículas
(SC-003); modo Quadtree com ≥10× menos testes (SC-002).

**Constraints**: sem build, sem servidor, sem dependências; precisa funcionar em
`file://`, onde ES modules são bloqueados pelo navegador (ver research.md, R1).

**Scale/Scope**: 10–2000 partículas; 5 arquivos de código, 3 de teste.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Princípio / Regra | Status | Observação |
|---|---|---|
| I. Simplicidade | ✅ | 5 arquivos planos, sem classes base, padrões ou configurações; Quadtree reconstruída a cada frame em vez de atualização incremental. |
| II. Código didático | ✅ | Funções curtas e nomeadas por passo do algoritmo; comentários explicam o porquê. |
| III. Quadtree do zero | ✅ | `quadtree.js` próprio (Rect, insert, subdivide, query). |
| IV. Testes só na lógica pura | ✅ | Testes apenas para `quadtree.js`, `particle.js`, `simulation.js`; `renderer.js` e `main.js` verificados manualmente. |
| V. Zero dependências | ✅ | Sem `package.json`, sem npm; apenas APIs nativas. |
| Demo abre pelo `index.html` | ✅ | Scripts clássicos em vez de ES modules (decisão do usuário, R1). |
| Mesmo módulo no navegador e no Node | ✅ | `module.exports` condicional no fim de cada arquivo de lógica (R2). |

**Pós-design (Phase 1)**: reavaliado — nenhuma violação; Complexity Tracking vazio.

## Project Structure

### Documentation (this feature)

```text
specs/001-particle-collision-demo/
├── plan.md              # Este arquivo
├── research.md          # Phase 0
├── data-model.md        # Phase 1
├── quickstart.md        # Phase 1
├── contracts/
│   └── modules.md       # API pública de cada módulo + controles da UI
└── tasks.md             # Phase 2 (/speckit-tasks)
```

### Source Code (repository root)

```text
index.html               # canvas em tela cheia + painel de controles; carrega os scripts em ordem
style.css                # estilo mínimo do painel
src/
├── particle.js          # Particle, movimento, quique nas bordas, sobreposição e ricochete
├── quadtree.js          # Rect e Quadtree (insert, subdivide, query)
├── simulation.js        # estado da simulação, passo do frame, detecção (força bruta / quadtree), range query
├── renderer.js          # desenho no canvas: partículas, grade, retângulo de seleção
└── main.js              # DOM, controles, eventos de mouse/resize, loop e FPS
tests/
├── particle.test.js
├── quadtree.test.js
└── simulation.test.js
```

Ordem de carregamento no `index.html`: `particle.js` → `quadtree.js` →
`simulation.js` → `renderer.js` → `main.js`.

**Structure Decision**: projeto único e plano na raiz; `src/` para o código e
`tests/` para os testes da lógica pura. Os módulos são os pedidos pelo usuário; a
dependência é em uma só direção (`main` → `renderer`/`simulation` → `quadtree`/
`particle`).

## Complexity Tracking

Nenhuma violação a justificar.
