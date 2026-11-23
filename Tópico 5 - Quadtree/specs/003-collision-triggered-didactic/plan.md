# Implementation Plan: Modo Didático Disparado por Colisão

**Branch**: `003-collision-triggered-didactic` | **Date**: 2026-11-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/003-collision-triggered-didactic/spec.md`

## Summary

O modo didático da feature 002 deixa de pausar qualquer frame: com ele ligado, a
animação roda e, no primeiro frame em que a detecção encontra uma colisão, pausa e
apresenta a detecção daquele frame inteiro (como hoje), com o par que disparou a pausa
em verde, Enter para ir ao teste desse par e Esc para encerrar. Ao encerrar, as colisões
são resolvidas e começa um intervalo de 5 s sem pausas. Abordagem: separar a detecção
da resolução na `Simulation` (`detect()` / `resolve(pairs)`), para olhar o resultado da
detecção antes de resolver; uma função pura localiza o passo do par no trace; o resto é
uma pequena máquina de estados em `main.js` e ajustes de cor em `renderer.js`.

## Technical Context

**Language/Version**: JavaScript (ES2020+) em scripts clássicos; Node 22 para testes.

**Primary Dependencies**: nenhuma.

**Storage**: N/A

**Testing**: `node --test`, só na lógica pura (`simulation.js`).

**Target Platform**: navegador de desktop com teclado, abrindo `index.html` em `file://`.

**Project Type**: aplicação web estática (alteração do modo didático existente).

**Performance Goals**: aguardar colisão não pode custar mais que a animação normal (a
detecção já roda em todo frame); o trace só é gerado quando há colisão.

**Constraints**: mantém limite de 200 partículas e as teclas da 002; intervalo de 5 s
(±0,5 s) em tempo real.

**Scale/Scope**: alterações em `simulation.js`, `renderer.js`, `main.js`, testes e README;
nenhum arquivo novo de código.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Princípio / Regra | Status | Observação |
|---|---|---|
| I. Simplicidade | ✅ | Estado do modo é uma string (`'off' \| 'waiting' \| 'presenting' \| 'cooldown'`) + um horário de fim do intervalo; nenhuma abstração nova. |
| II. Código didático | ✅ | `detect()` e `resolve()` deixam o frame em fases ainda mais explícitas. |
| III. Quadtree do zero | ✅ | Sem mudança na Quadtree. |
| IV. Testes só na lógica pura | ✅ | Testes para `detect`/`resolve` e para localizar o par no trace; estados e cores verificados manualmente. |
| V. Zero dependências | ✅ | Nada novo. |
| Demo abre pelo `index.html` | ✅ | Sem mudança. |
| Commits sem coautoria, testes passando | ✅ | Mantido nas tasks. |

**Pós-design (Phase 1)**: reavaliado — nenhuma violação; Complexity Tracking vazio.

## Project Structure

### Documentation (this feature)

```text
specs/003-collision-triggered-didactic/
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
src/
├── simulation.js        # detect() + resolve(pairs); detectAndResolve() = resolve(detect()); findPairStepIndex()
├── renderer.js          # drawTrace recebe o par apresentado (verde); cores sem verde para o resto
└── main.js              # estados off/waiting/presenting/cooldown, Enter, Esc, intervalo de 5 s, painel
tests/
└── simulation.test.js   # + detect/resolve, par apresentado = primeiro par da detecção, findPairStepIndex
README.md                # atualiza a seção do modo didático
```

**Structure Decision**: mesma estrutura das features 001/002; só extensões.
`index.html`, `style.css`, `particle.js` e `quadtree.js` não mudam.

## Complexity Tracking

Nenhuma violação a justificar.
