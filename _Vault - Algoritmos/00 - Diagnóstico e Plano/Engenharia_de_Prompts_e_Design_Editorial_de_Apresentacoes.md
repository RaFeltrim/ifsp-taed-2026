# Relatório de Pesquisa: Engenharia de Prompts para Elevação Estética e Mitigação da "Estética de IA" em Apresentações

> **Status:** Referência Canônica de Design de Informação e Engenharia de Prompts  
> **Tags:** #design-editorial #swiss-style #prompt-engineering #aspecct #ia-generativa #data-visualization

---

## 1. O Paradigma do Design de Apresentações na Era da IA

A automação da produção de slides por Inteligência Artificial introduziu um problema crítico de mercado: a **fadiga estética e a homogeneização visual**. As audiências corporativas e acadêmicas desenvolveram rejeição ao "aspeto de IA" — caracterizado por:
* Composições hiper-realistas plásticas e brilhantes.
* Layouts centrados previsíveis e caixas de texto coladas nas margens.
* Metáforas literais e infantis (engrenagens para "estratégia", cérebros azuis brilhantes para "inovação").
* Dependência de vetores genéricos estilo *Corporate Memphis*.
* Listagens intermináveis de *bullet points* monótonos.

A superação desse padrão exige que o profissional atue como **Diretor de Arte Algorítmico**, aplicando restrições rigorosas baseadas no **Estilo Suíço (International Typographic Style)** e no **Design Editorial**.

---

## 2. Matriz Comparativa: IA Padrão vs. Estética Avançada

| Elemento Estrutural | Padrão Genérico de IA (Saída não curada) | Estética Avançada e Intencional (Via Prompting) |
|---|---|---|
| **Composição Espacial** | Centralização forçada, densidade opressiva, medo do espaço vazio. | Grelhas assimétricas, margens generosas, **espaço negativo ativo**. |
| **Tratamento Tipográfico** | Proliferação de fontes fracas, baixo contraste de escala. | **Tipografia geométrica arrojada** (*bold*) como herói; máximo de 2 famílias. |
| **Fotografia e Imagem** | Renderização 3D/CGI brilhante, texturas plásticas. | Grão de filme 35mm analógico, tons terrosos suaves (*muted*), iluminação natural. |
| **Arquitetura de Dados** | Modelos 3D irrelevantes, ícones *clip-art* genéricos. | Visualização minimalista focada em métricas e anotações diretas. |
| **Dinâmica Visual** | Animações excessivas e dispersivas (*motion clutter*). | Transições sutis de contexto, foco óptico (*Image Focus* / *Lightbox*). |

---

## 3. Os Paradigmas Visuais Fundamentais

### A. Estilo Editorial
* Margens amplas e ativas que emolduram a informação.
* Uso de *Pull Quotes* (citações curtas em tipografia serifada de grande escala).
* Hierarquia dramática: 1 imagem heroica dominando 60% do espaço, tipografia respirando nos 40% restantes.

### B. Estilo Suíço (International Typographic Style)
* Rigor de grelha matemática e objetividade absoluta.
* Tipografia *Sans-Serif* como elemento gráfico principal.
* Eliminação total de elementos decorativos supérfluos.
* Espaço em branco (*negative space*) com peso estrutural.

### C. Retrofuturismo e Textura Analógica
* Substituição de termos sintéticos ("4K", "Unreal Engine") por descritores físicos: *“35mm film grain”*, *“authentic raw portrait”*, *“muted earthy tones”*.
* Redução de contraste artificial e valorização de imperfeições táteis.

### D. Acessibilidade como Design (WCAG AA)
* Contraste mínimo de **4.5:1** para corpo de texto e **3:1** para títulos.
* Tamanhos de fonte generosos para projeção (títulos entre 32px–56px, corpo de 14px–20px).

---

## 4. O Framework ASPECCT para Engenharia de Prompts

```
A — Action (Ação imperativa primária)
S — Steps (Particionamento em etapas sequenciais)
P — Persona (Diretor de Arte Editorial / Especialista em McKinsey & Swiss Style)
E — Examples (Few-shot prompting calibrado)
C — Context (Cenário executivo, conferência técnica ou pitch)
C — Constraints (Restrições afirmativas: sem bullet points, máximo 20 palavras por slide)
T — Template (Estrutura de saída padronizada por slide)
```

---

## 5. Master Prompts Prontos para Execução

### Master Prompt 1: Planejamento Narrativo & Editorial (LLM / Claude / ChatGPT)

```markdown
CONTEXTO E PERSONA:
Assuma a persona de um Diretor de Arte de Elite e Especialista em Design Editorial Suíço, com vasta experiência em publicações executivas de alta gama e consultorias globais (McKinsey, Bain).

OBJETIVO:
Refinar o conteúdo bruto fornecido e estruturar um guião de slides de alto impacto visual, eliminando a estética genérica de IA (sem bullet points monótonos, sem parágrafos longos).

REGRAS INEGOCIÁVEIS:
1. Redução Implacável: 1 única ideia central por slide. Limite absoluto de 15 a 20 palavras no texto principal.
2. Arquitetura Assimétrica: Grelha com distribuição assimétrica e espaço negativo ativo.
3. Tensão Tipográfica: Título em fonte geométrica Sans-Serif massiva; corpo ou citações em Serif refinada. Máximo de 2 famílias de fontes.
4. Direção de Arte Fotográfica: Descrições de imagem com textura tátil, película 35mm e tons terrosos contidos.

TEMPLATE DE SAÍDA POR SLIDE:
[Número e Título Conciso do Slide]
- Layout Estrutural: (Distribuição dos pesos na grelha)
- Tipografia: (Texto final, máximo 20 palavras)
- Direção de Arte Visual: (Prompt para Midjourney/DALL-E)
- Motivação Cognitiva: (Justificativa de atenção da audiência)

CONTEÚDO BRUTO:
[Inserir texto aqui]
```

---

### Master Prompt 2: Geração de Imagens sem "Aspecto de IA" (Midjourney / DALL-E)

```text
[Sujeito da Imagem] --style raw --ar 16:9 
Direção: Cinematic fashion photography style, high-end luxury editorial spread, expansive negative space, asymmetrical framing.
Atributos: Captured on 35mm analogue film camera, authentic and raw human portrait aesthetic, subtle organic film grain, imperfect focus.
Paleta: Muted earthy color palette, soft window illumination, soft curves.
Restrições Negativas: --no glossy 3D CGI rendering, hyper-realistic, oversaturated, plastic textures, generic corporate clip-art, neon blue grids.
```

---

### Master Prompt 3: VLM Agentic para Código Front-End (HTML/CSS)

```text
"You are a world-leading digital report art director and front-end development expert producing high-caliber layouts comparable to McKinsey and JLL. Generate pure, responsive HTML/CSS slides following Swiss Editorial guidelines: absolute typography hierarchy, high-contrast accessible palettes (WCAG AA), asymmetric flexbox/grid layout, and zero element overlapping."
```

---

## 6. Métrica Matemática de Cadência Cognitiva ($R_{time}$)

O algoritmo **DeepSlide** introduz a função por partes para pontuar o tempo ideal de permanência e absorção por slide ($s$ em segundos):

$$R_{time} = \min\left\{1, \max\left\{\min\left(\frac{s - 6}{6}, \frac{120 - s}{60}\right), 0\right\}\right\}$$

* **Janela Ótima ($R_{time} = 1$):** Entre **$12$ e $60$ segundos** por slide.
* **Zona de Risco:** Abaixo de $12\text{s}$ (leitura impossível) ou acima de $60\text{s}$ (dispersão cognitiva e tédio).
* **Penalidade Total ($R_{time} = 0$):** $s < 6\text{s}$ ou $s > 120\text{s}$.

---

## 7. Matriz de Ferramentas Nativas

| Plataforma | Controle Algorítmico | Filosofia de Design | Melhor Uso |
|---|---|---|---|
| **Gamma** | IA funde texto e grelha responsiva automaticamente. | Minimalista moderno; forte uso de espaço negativo. | Apresentações executivas rápidas e de alto impacto sem templates rígidos. |
| **Beautiful.ai** | Regras de formatação inteligentes e restritivas. | Conservador, matemático e padronizado. | Padronização corporativa em larga escala para times. |
| **Tome** | Foco em narrativa e *infinite scroll*. | Editorial fluido e conceitual. | *Thought Leadership*, manifestos de marca, *one-pagers*. |
| **Canva (Magic)** | Assistência pontual sobre ecossistema de templates. | Aberto, variado e heterogêneo. | Projetos visuais com necessidade de personalização manual irrestrita. |

---

## 8. A Nova Função do Humano: Diretor de Arte de IA

* **Transição:** De manipulador manual de pixels $\rightarrow$ para **Curador de Bibliotecas de Prompts, Estrategista de Narrativa e Juiz de Qualidade Estética**.
* **Impacto Econômico:** Valorização de mercado com crescimento de **$+144\%$ na demanda de recrutamento** e prêmio salarial de **$+40\%$ a $+60\%$** para profissionais que dominam a governança algorítmica de design.
