# Documentação Técnica — Quadtree: Colisão de Partículas

Índice dos documentos de arquitetura, complexidade algorítmica e mapeamento estrutural do projeto.

---

## Documentos

| Arquivo | Conteúdo |
| :--- | :--- |
| [`arquitetura.md`](./arquitetura.md) | Separação em 5 módulos planos, contratos entre camadas e máquina de estados do modo didático |
| [`algoritmos-e-complexidade.md`](./algoritmos-e-complexidade.md) | Comparação entre força bruta ($O(N^2)$) e Quadtree ($O(N \log N)$), subdivisão espacial e `buildTrace()` |
| [`../graphify-out/GRAPH_REPORT.md`](../graphify-out/GRAPH_REPORT.md) | Relatório de dependências, comunidades e nós centrais gerado pelo `/graphify` (294 nós, 417 arestas) |
| [`../graphify-out/graph.html`](../graphify-out/graph.html) | Visualização interativa do grafo de conhecimento |

---

## Especificações por funcionalidade

- [`specs/001-particle-collision-demo/spec.md`](../specs/001-particle-collision-demo/spec.md) — Simulação base, Quadtree de pontos e seleção por arrasto.
- [`specs/002-didactic-step-mode/spec.md`](../specs/002-didactic-step-mode/spec.md) — Modo didático passo a passo e atalhos de navegação.
- [`specs/003-collision-triggered-didactic/spec.md`](../specs/003-collision-triggered-didactic/spec.md) — Pausa automática por colisão e intervalo de cooldown de 5 segundos.
