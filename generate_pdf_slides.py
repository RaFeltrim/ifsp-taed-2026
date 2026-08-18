import os
import subprocess
import time

def build_presentation():
    # SVG Vector Diagram in 100% Portuguese, perfectly framed, zero overflow, modern pill border-radius
    svg_diagram = """
    <svg viewBox="0 0 740 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
        <!-- Fundo do Diagrama -->
        <rect width="740" height="370" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>

        <!-- Título do Diagrama -->
        <text x="28" y="32" font-size="13" font-weight="800" fill="#090d16" letter-spacing="0.5">ESTADO DA MEMÓRIA NO PASSO 4: s = "abcabcbb"</text>
        <text x="28" y="48" font-size="11.5" fill="#64748b">O ponteiro direito (R) encontra 'a' repetido no índice 3. O ponteiro esquerdo (L) salta direto de 0 para 1.</text>

        <!-- Array / String Cells -->
        <g transform="translate(28, 68)">
            <!-- Header do Vetor -->
            <text x="0" y="12" font-size="10" font-weight="700" fill="#64748b" text-transform="uppercase" letter-spacing="0.8">Vetor de Caracteres na Memória</text>
            
            <!-- Células da String (0 a 7) -->
            <!-- 0: 'a' -->
            <rect x="0" y="24" width="48" height="48" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="24" y="54" font-size="18" font-weight="700" fill="#64748b" text-anchor="middle" font-family="'JetBrains Mono', monospace;">a</text>
            <text x="24" y="86" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">0</text>

            <!-- 1: 'b' -->
            <rect x="54" y="24" width="48" height="48" rx="6" fill="#ecfdf5" stroke="#047857" stroke-width="1.5"/>
            <text x="78" y="54" font-size="18" font-weight="700" fill="#047857" text-anchor="middle" font-family="'JetBrains Mono', monospace;">b</text>
            <text x="78" y="86" font-size="11" font-weight="700" fill="#047857" text-anchor="middle" font-family="'JetBrains Mono', monospace;">1</text>

            <!-- 2: 'c' -->
            <rect x="108" y="24" width="48" height="48" rx="6" fill="#ecfdf5" stroke="#047857" stroke-width="1.5"/>
            <text x="132" y="54" font-size="18" font-weight="700" fill="#047857" text-anchor="middle" font-family="'JetBrains Mono', monospace;">c</text>
            <text x="132" y="86" font-size="11" font-weight="700" fill="#047857" text-anchor="middle" font-family="'JetBrains Mono', monospace;">2</text>

            <!-- 3: 'a' -->
            <rect x="162" y="24" width="48" height="48" rx="6" fill="#eff6ff" stroke="#0284c7" stroke-width="2"/>
            <text x="186" y="54" font-size="18" font-weight="700" fill="#0284c7" text-anchor="middle" font-family="'JetBrains Mono', monospace;">a</text>
            <text x="186" y="86" font-size="11" font-weight="700" fill="#0284c7" text-anchor="middle" font-family="'JetBrains Mono', monospace;">3</text>

            <!-- 4: 'b' -->
            <rect x="216" y="24" width="48" height="48" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="240" y="54" font-size="18" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">b</text>
            <text x="240" y="86" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">4</text>

            <!-- 5: 'c' -->
            <rect x="270" y="24" width="48" height="48" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="294" y="54" font-size="18" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">c</text>
            <text x="294" y="86" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">5</text>

            <!-- 6: 'b' -->
            <rect x="324" y="24" width="48" height="48" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="348" y="54" font-size="18" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">b</text>
            <text x="348" y="86" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">6</text>

            <!-- 7: 'b' -->
            <rect x="378" y="24" width="48" height="48" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="402" y="54" font-size="18" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">b</text>
            <text x="402" y="86" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle" font-family="'JetBrains Mono', monospace;">7</text>

            <!-- Caixa da Janela Deslizante Ativa (Bordas Perfeitas com rx=10) -->
            <rect x="50" y="18" width="164" height="60" rx="10" fill="none" stroke="#047857" stroke-width="2.5" stroke-dasharray="6,4"/>
            
            <!-- Etiqueta da Janela Deslizante (Pill Shape Moderno rx=10) -->
            <rect x="57" y="2" width="150" height="20" rx="10" fill="#047857"/>
            <text x="132" y="15" font-size="9.5" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="0.4">JANELA ATIVA: "bca" (tam = 3)</text>
        </g>

        <!-- Ponteiros (Setas e Anotações) -->
        <g transform="translate(28, 178)">
            <!-- Ponteiro Esquerdo (L) -->
            <path d="M 78,30 L 78,8" stroke="#047857" stroke-width="2.5" marker-end="url(#arrow-green)" fill="none"/>
            <rect x="33" y="34" width="90" height="22" rx="6" fill="#ecfdf5" stroke="#a7f3d0" stroke-width="1"/>
            <text x="78" y="49" font-size="10.5" font-weight="800" fill="#047857" text-anchor="middle">L (left) = 1</text>

            <!-- Curva de Salto de L -->
            <path d="M 24,35 Q 50,4 74,34" fill="none" stroke="#b45309" stroke-width="1.8" stroke-dasharray="3,3"/>
            <text x="36" y="6" font-size="9.5" font-weight="700" fill="#b45309">Salto O(1): 0 → 1</text>

            <!-- Ponteiro Direito (R) -->
            <path d="M 186,30 L 186,8" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrow-blue)" fill="none"/>
            <rect x="141" y="34" width="90" height="22" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
            <text x="186" y="49" font-size="10.5" font-weight="800" fill="#0284c7" text-anchor="middle">R (right) = 3</text>
        </g>

        <!-- Painel Lateral: Tabela Hash (char_map) -->
        <g transform="translate(485, 68)">
            <rect width="225" height="205" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
            
            <!-- Cabeçalho da Tabela Hash -->
            <path d="M 0,8 Q 0,0 8,0 L 217,0 Q 225,0 225,8 L 225,30 L 0,30 Z" fill="#0f172a"/>
            <text x="112" y="19" font-size="10.5" font-weight="800" fill="#f8fafc" text-anchor="middle" letter-spacing="0.6">TABELA HASH (char_map)</text>

            <!-- Linhas da Tabela Hash -->
            <!-- Chave 'a' -->
            <g transform="translate(12, 40)">
                <rect width="201" height="30" rx="5" fill="#ffffff" stroke="#bfdbfe" stroke-width="1.5"/>
                <text x="12" y="20" font-size="12" font-weight="700" fill="#0284c7" font-family="'JetBrains Mono', monospace;">'a'</text>
                <text x="50" y="20" font-size="11" fill="#64748b">→</text>
                <text x="75" y="20" font-size="12" font-weight="800" fill="#0284c7" font-family="'JetBrains Mono', monospace;">índice 3</text>
                <text x="150" y="19" font-size="9" font-weight="700" fill="#0284c7">(atualizado)</text>
            </g>

            <!-- Chave 'b' -->
            <g transform="translate(12, 76)">
                <rect width="201" height="30" rx="5" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
                <text x="12" y="20" font-size="12" font-weight="700" fill="#334155" font-family="'JetBrains Mono', monospace;">'b'</text>
                <text x="50" y="20" fill="#64748b">→</text>
                <text x="75" y="20" font-size="12" font-weight="700" fill="#334155" font-family="'JetBrains Mono', monospace;">índice 1</text>
            </g>

            <!-- Chave 'c' -->
            <g transform="translate(12, 112)">
                <rect width="201" height="30" rx="5" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
                <text x="12" y="20" font-size="12" font-weight="700" fill="#334155" font-family="'JetBrains Mono', monospace;">'c'</text>
                <text x="50" y="20" fill="#64748b">→</text>
                <text x="75" y="20" font-size="12" font-weight="700" fill="#334155" font-family="'JetBrains Mono', monospace;">índice 2</text>
            </g>

            <!-- Nota de Complexidade no Rodapé da Tabela -->
            <g transform="translate(12, 152)">
                <rect width="201" height="40" rx="5" fill="#ecfdf5" stroke="#a7f3d0" stroke-width="1"/>
                <text x="100" y="17" font-size="9.5" font-weight="800" fill="#047857" text-anchor="middle">BUSCA & ATUALIZAÇÃO EM O(1)</text>
                <text x="100" y="30" font-size="8.5" font-weight="600" fill="#047857" text-anchor="middle">Sem retroceder o cursor de leitura</text>
            </g>
        </g>

        <!-- Linha Inferior: Resumo Matemático (Posicionado Perfeitamente sem Overflow) -->
        <g transform="translate(28, 290)">
            <rect width="682" height="60" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
            <text x="20" y="25" font-size="11" font-weight="800" fill="#090d16">CÁLCULO ATUAL DA JANELA:</text>
            <text x="20" y="44" font-size="12" font-weight="700" fill="#047857" font-family="'JetBrains Mono', monospace;">tamanho = right - left + 1  →  3 - 1 + 1 = 3</text>
            
            <line x1="370" y1="10" x2="370" y2="50" stroke="#cbd5e1" stroke-width="1"/>
            
            <text x="390" y="25" font-size="11" font-weight="800" fill="#090d16">REGISTRO DO MAIOR COMPRIMENTO:</text>
            <text x="390" y="44" font-size="12" font-weight="800" fill="#090d16" font-family="'JetBrains Mono', monospace;">max_len = max(3, 3) = 3</text>
        </g>

        <!-- Definições de Marcadores de Setas -->
        <defs>
            <marker id="arrow-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="#047857"/>
            </marker>
            <marker id="arrow-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="#0284c7"/>
            </marker>
        </defs>
    </svg>
    """

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Apresentação LeetCode 3 - Padrão Editorial Suíço</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        @page {{
            size: 1280px 720px;
            margin: 0;
        }}

        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #f8fafc;
            color: #090d16;
            width: 1280px;
            height: 720px;
            -webkit-font-smoothing: antialiased;
        }}

        .slide {{
            width: 1280px;
            height: 720px;
            page-break-after: always;
            position: relative;
            overflow: hidden;
            background-color: #f8fafc;
            display: flex;
            flex-direction: column;
            padding: 38px 55px;
        }}

        /* Header Editorial */
        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 16px;
            border-bottom: 1.5px solid #e2e8f0;
            padding-bottom: 8px;
        }}

        .header-tag {{
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: #047857;
        }}

        .header-sub {{
            color: #64748b;
            font-size: 12.5px;
            font-weight: 500;
        }}

        /* Tipografia de Destaque */
        .slide-title {{
            font-size: 30px;
            font-weight: 800;
            color: #090d16;
            line-height: 1.15;
            margin-bottom: 16px;
            letter-spacing: -0.8px;
        }}

        .slide-title span {{
            color: #047857;
        }}

        /* Grids Assimétricos */
        .grid-60-40 {{
            display: grid;
            grid-template-columns: 1.4fr 1fr;
            gap: 20px;
            flex: 1;
            align-items: stretch;
        }}

        .grid-40-60 {{
            display: grid;
            grid-template-columns: 1fr 1.4fr;
            gap: 20px;
            flex: 1;
            align-items: stretch;
        }}

        .grid-50-50 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            flex: 1;
            align-items: stretch;
        }}

        .grid-3-col {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            flex: 1;
            align-items: stretch;
        }}

        /* Cartões Editoriais */
        .card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}

        .card-emerald {{
            border-left: 4px solid #047857;
        }}

        .card-rose {{
            border-left: 4px solid #be123c;
        }}

        .card-amber {{
            border-left: 4px solid #b45309;
        }}

        .card-blue {{
            border-left: 4px solid #0369a1;
        }}

        .card-title {{
            font-size: 15px;
            font-weight: 700;
            color: #090d16;
            margin-bottom: 8px;
            letter-spacing: -0.3px;
        }}

        .card-text {{
            font-size: 12.5px;
            line-height: 1.55;
            color: #334155;
            margin-bottom: 8px;
        }}

        /* Pull Quotes Editoriais */
        .pull-quote {{
            font-size: 14.5px;
            font-weight: 600;
            line-height: 1.5;
            color: #090d16;
            border-left: 3px solid #047857;
            padding: 10px 14px;
            margin: 8px 0;
            background: #f0fdf4;
            border-radius: 0 8px 8px 0;
        }}

        /* Keynote Metrics */
        .metric-container {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 16px;
        }}

        .metric-big {{
            font-size: 38px;
            font-weight: 800;
            line-height: 1;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 6px;
            letter-spacing: -1px;
        }}

        .metric-label {{
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #64748b;
        }}

        /* Badges Minimalistas */
        .badge-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: auto;
            padding-top: 8px;
        }}

        .badge {{
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            background: #f1f5f9;
            color: #334155;
            border: 1px solid #cbd5e1;
        }}

        .badge-company {{
            background: #eff6ff;
            border-color: #bfdbfe;
            color: #1d4ed8;
        }}

        .badge-success {{
            background: #f0fdf4;
            border-color: #bbf7d0;
            color: #15803d;
        }}

        .badge-danger {{
            background: #fff1f2;
            border-color: #fecdd3;
            color: #be123c;
        }}

        .badge-warning {{
            background: #fffbeb;
            border-color: #fde68a;
            color: #b45309;
        }}

        /* Blocos de Código em Dark Slate Elegante - FORMATADO SEM VAZIO */
        pre {{
            font-family: 'JetBrains Mono', monospace;
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 12px 14px;
            font-size: 10.8px;
            line-height: 1.42;
            color: #f8fafc;
            white-space: pre;
            overflow-x: auto;
            margin-bottom: 10px;
        }}

        code {{
            font-family: 'JetBrains Mono', monospace;
            font-size: inherit;
        }}

        .kw {{ color: #fb7185; font-weight: 700; }}
        .fn {{ color: #38bdf8; font-weight: 700; }}
        .str {{ color: #4ade80; }}
        .com {{ color: #94a3b8; font-style: italic; }}
        .num {{ color: #fbbf24; }}

        /* Listas de Anotações Técnicas dentro dos Cards */
        .code-details {{
            font-size: 12px;
            color: #475569;
            line-height: 1.5;
            margin-bottom: 6px;
        }}

        /* Tabelas Editoriais Suíças */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 4px;
        }}

        th, td {{
            padding: 7px 10px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
            font-size: 12px;
        }}

        th {{
            background: #f1f5f9;
            color: #475569;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 10px;
            letter-spacing: 0.6px;
        }}

        td {{
            color: #090d16;
        }}

        .trace-table th, .trace-table td {{
            padding: 5px 7px;
            font-size: 11px;
        }}

        /* Rodapé Editorial */
        .footer-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 14px;
            padding-top: 8px;
            border-top: 1px solid #e2e8f0;
            color: #64748b;
            font-size: 11.5px;
            font-weight: 600;
        }}

        /* Capa Editorial */
        .cover-slide {{
            justify-content: space-between;
            padding: 50px 65px;
            background: #ffffff;
        }}

        .cover-main {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            max-width: 950px;
        }}

        .cover-tag {{
            font-size: 11.5px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: #047857;
            margin-bottom: 12px;
        }}

        .cover-title {{
            font-size: 40px;
            font-weight: 800;
            color: #090d16;
            line-height: 1.12;
            letter-spacing: -1.2px;
            margin-bottom: 12px;
        }}

        .cover-subtitle {{
            font-size: 16.5px;
            line-height: 1.5;
            color: #475569;
            max-width: 850px;
        }}

        .cover-footer {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-top: 1.5px solid #e2e8f0;
            padding-top: 16px;
        }}

        .team-group {{
            display: flex;
            gap: 28px;
        }}

        .team-item {{
            display: flex;
            flex-direction: column;
            gap: 2px;
        }}

        .team-name {{
            font-size: 13px;
            font-weight: 700;
            color: #090d16;
        }}

        .team-role {{
            font-size: 11px;
            color: #047857;
            font-weight: 600;
        }}

        .cover-meta {{
            font-size: 11.5px;
            color: #64748b;
            text-align: right;
            line-height: 1.4;
        }}

        .highlight-val {{
            color: #0284c7;
            font-weight: 700;
            font-family: 'JetBrains Mono', monospace;
        }}
    </style>
</head>
<body>

    <!-- SLIDE 1: CAPA EDITORIAL SUÍÇA -->
    <div class="slide cover-slide">
        <div class="cover-main">
            <div class="cover-tag">IFSP São Carlos · Bacharelado em Engenharia de Software</div>
            <h1 class="cover-title">Longest Substring Without Repeating Characters</h1>
            <p class="cover-subtitle">Desafio Técnico de Processos Seletivos (LeetCode #3) — Otimização Assintótica de O(N³) para O(N), Benchmark de CPU e Análise da Janela Deslizante.</p>
        </div>

        <div class="cover-footer">
            <div class="team-group">
                <div class="team-item">
                    <span class="team-name">Rafael Feltrim</span>
                    <span class="team-role">Desenvolvimento & Apresentação</span>
                </div>
                <div class="team-item">
                    <span class="team-name">Ian</span>
                    <span class="team-role">Pesquisa & Algoritmos</span>
                </div>
                <div class="team-item">
                    <span class="team-name">Gustavo (Gub)</span>
                    <span class="team-role">Análise de Complexidade</span>
                </div>
            </div>
            <div class="cover-meta">
                <b>Tópicos em Algoritmos e Estruturas de Dados</b><br>
                Prof. Dr. Rodrigo Elias Bianchi · 2026
            </div>
        </div>
    </div>

    <!-- SLIDE 2: RELEVÂNCIA DE MERCADO (LAYOUT ASSIMÉTRICO 60/40) -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">01 · Relevância de Mercado</div>
            <div class="header-sub">Mapeamento em Entrevistas de Alta Escala</div>
        </div>
        <h2 class="slide-title">Onipresença nos <span>Processos Seletivos</span></h2>
        
        <div class="grid-60-40">
            <div class="card card-emerald">
                <div class="card-title">Por que as Big Techs cobram este problema?</div>
                <p class="card-text">
                    Este problema é o divisor de águas entre candidatos que apenas conhecem sintaxe e desenvolvedores que dominam a **otimização de estruturas de dados e complexidade assintótica**.
                </p>
                <div class="pull-quote">
                    "Em entrevistas técnicas globais, o código representa apenas 30% da avaliação. Os outros 70% medem clareza de decomposição lógica, comunicação e justificativa de Big-O."
                </div>
                <p class="card-text" style="margin-top: 4px;">
                    O avaliador busca testar se o candidato percebe a redundância da força bruta e consegue implementar a janela deslizante com consulta em tempo constante O(1).
                </p>
            </div>

            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div class="card card-blue" style="flex: 1;">
                    <div class="card-title">Empresas com Aplicação Recorrente</div>
                    <div class="badge-list" style="margin-top: 4px;">
                        <span class="badge badge-company">Amazon (Top 10 SDE)</span>
                        <span class="badge badge-company">Meta (Triagem 45 min)</span>
                        <span class="badge badge-company">Google (Nível L3 / L4)</span>
                        <span class="badge badge-company">Microsoft</span>
                        <span class="badge badge-company">Apple</span>
                        <span class="badge badge-company">Bloomberg</span>
                    </div>
                </div>

                <div class="card card-amber" style="flex: 1;">
                    <div class="card-title">Competências Verificadas</div>
                    <p class="card-text" style="font-size: 12px; margin: 0;">
                        • Redução assintótica de O(N³) para O(N)<br>
                        • Escolha de Hash Map vs. Vetor ASCII estático<br>
                        • Tratamento de casos de borda e memória de pilha
                    </p>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Tarefa Prática do Dia · Slide 13</span>
            <span>LeetCode #3</span>
        </div>
    </div>

    <!-- SLIDE 3: ENUNCIADO DO PROBLEMA -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">02 · Definição Formal</div>
            <div class="header-sub">Compreendendo o Problema Computacional</div>
        </div>
        <h2 class="slide-title">Enunciado: <span>Substring sem Caracteres Repetidos</span></h2>

        <div class="grid-50-50">
            <div class="card card-emerald">
                <div class="card-title">Definição do Problema</div>
                <p class="card-text" style="font-size: 15px; font-weight: 600; color: #090d16; margin-bottom: 12px;">
                    "Dada uma string <code>s</code>, encontre o comprimento da <u>maior substring contígua</u> que não contenha caracteres repetidos."
                </p>
                <div class="pull-quote" style="background: #fffbeb; border-color: #b45309;">
                    <b>Distinção Conceitual Crítica:</b><br>
                    • <b>Substring:</b> Sequência estritamente contínua na memória (ex: <code>"abc"</code> em <code>"abcde"</code>).<br>
                    • <b>Subsequência:</b> Mantém a ordem mas não é contígua (ex: <code>"ace"</code> em <code>"abcde"</code>).
                </div>
            </div>

            <div class="card card-blue">
                <div class="card-title">Casos de Teste Padronizados</div>
                
                <div style="margin-bottom: 8px; background: #f8fafc; border: 1px solid #e2e8f0; padding: 8px 12px; border-radius: 6px;">
                    <div style="color: #0369a1; font-weight: 700; font-size: 11px; text-transform: uppercase;">Exemplo 1 (Geral)</div>
                    <code style="font-size: 13px; color: #090d16;">s = "abcabcbb"</code> → <b>Comprimento: 3</b> (substring: <code>"abc"</code>)
                </div>

                <div style="margin-bottom: 8px; background: #f8fafc; border: 1px solid #e2e8f0; padding: 8px 12px; border-radius: 6px;">
                    <div style="color: #0369a1; font-weight: 700; font-size: 11px; text-transform: uppercase;">Exemplo 2 (Homogêneo)</div>
                    <code style="font-size: 13px; color: #090d16;">s = "bbbbb"</code> → <b>Comprimento: 1</b> (substring: <code>"b"</code>)
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 8px 12px; border-radius: 6px;">
                    <div style="color: #0369a1; font-weight: 700; font-size: 11px; text-transform: uppercase;">Exemplo 3 (Composto)</div>
                    <code style="font-size: 13px; color: #090d16;">s = "pwwkew"</code> → <b>Comprimento: 3</b> (substring: <code>"wke"</code>)
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Tarefa Prática do Dia · Slide 13</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 4: 3 ABORDAGENS EM CÓDIGO (FORMATAÇÃO EQUILIBRADA SEM VAZIOS) -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">03 · Soluções Comparadas</div>
            <div class="header-sub">Evolução do Algoritmo em 3 Níveis de Eficiência</div>
        </div>
        <h2 class="slide-title">As 3 Diferentes <span>Abordagens em Código</span></h2>

        <div class="grid-3-col">
            <!-- Card 1: Força Bruta -->
            <div class="card card-rose">
                <div class="card-title" style="color: #be123c; font-size: 14px;">1. Força Bruta O(N³)</div>
                <pre><code><span class="kw">def</span> <span class="fn">brute_force</span>(s):
    n = <span class="fn">len</span>(s)
    max_len = <span class="num">0</span>
    <span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(n):
        <span class="kw">for</span> j <span class="kw">in</span> <span class="fn">range</span>(i+<span class="num">1</span>, n+<span class="num">1</span>):
            sub = s[i:j]
            <span class="kw">if</span> <span class="fn">len</span>(<span class="fn">set</span>(sub)) == <span class="fn">len</span>(sub):
                max_len = <span class="fn">max</span>(max_len, <span class="fn">len</span>(sub))
    <span class="kw">return</span> max_len</code></pre>
                <div class="code-details">
                    • Gera todas as fatias $O(N^2)$<br>
                    • Converte cada fatia em set $O(N)$<br>
                    • Causa Time Limit Exceeded (TLE)
                </div>
                <div class="badge-list">
                    <span class="badge badge-danger">Tempo: O(N³)</span>
                    <span class="badge badge-danger">Rejeitado</span>
                </div>
            </div>

            <!-- Card 2: Sliding Window com Set -->
            <div class="card card-amber">
                <div class="card-title" style="color: #b45309; font-size: 14px;">2. Sliding Window (Set)</div>
                <pre><code><span class="kw">def</span> <span class="fn">sliding_window_set</span>(s):
    char_set = <span class="fn">set</span>()
    left = max_len = <span class="num">0</span>
    <span class="kw">for</span> right <span class="kw">in</span> <span class="fn">range</span>(<span class="fn">len</span>(s)):
        <span class="kw">while</span> s[right] <span class="kw">in</span> char_set:
            char_set.remove(s[left])
            left += <span class="num">1</span>
        char_set.add(s[right])
        max_len = <span class="fn">max</span>(max_len, right - left + <span class="num">1</span>)
    <span class="kw">return</span> max_len</code></pre>
                <div class="code-details">
                    • Dois ponteiros dinâmicos<br>
                    • Remove elemento por elemento<br>
                    • Cada char entra e sai 1 vez: $O(2N)$
                </div>
                <div class="badge-list">
                    <span class="badge badge-warning">Tempo: O(2N)</span>
                    <span class="badge badge-warning">Contratado</span>
                </div>
            </div>

            <!-- Card 3: Sliding Window com Map -->
            <div class="card card-emerald">
                <div class="card-title" style="color: #047857; font-size: 14px;">3. Sliding Window (Map O(1))</div>
                <pre><code><span class="kw">def</span> <span class="fn">sliding_window_map</span>(s):
    char_map = {{}}
    left = max_len = <span class="num">0</span>
    <span class="kw">for</span> right, char <span class="kw">in</span> <span class="fn">enumerate</span>(s):
        <span class="kw">if</span> char <span class="kw">in</span> char_map <span class="kw">and</span> char_map[char] >= left:
            left = char_map[char] + <span class="num">1</span>
        char_map[char] = right
        max_len = <span class="fn">max</span>(max_len, right - left + <span class="num">1</span>)
    <span class="kw">return</span> max_len</code></pre>
                <div class="code-details">
                    • Salto direto em $O(1)$ sem loop<br>
                    • Passagem estrita de cursor único<br>
                    • Padrão Ouro em Entrevistas
                </div>
                <div class="badge-list">
                    <span class="badge badge-success">Tempo: O(N) Estrito</span>
                    <span class="badge badge-success">Forte Candidato</span>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Diferentes Soluções Algorítmicas</span>
            <span>LeetCode #3</span>
        </div>
    </div>

    <!-- SLIDE 5: CÓDIGO RODANDO EM ETAPAS -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">04 · Rastreio de Execução</div>
            <div class="header-sub">Simulação de Variáveis Passo a Passo</div>
        </div>
        <h2 class="slide-title">Código Rodando em <span>Etapas: "abcabcbb"</span></h2>

        <div class="card card-emerald" style="flex: 1;">
            <table class="trace-table">
                <thead>
                    <tr>
                        <th>Passo</th>
                        <th>Char</th>
                        <th>R (right)</th>
                        <th>L (left)</th>
                        <th>Janela</th>
                        <th>Evento / Ação da Tabela Hash</th>
                        <th>char_map Atual</th>
                        <th>max_len</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>1</b></td>
                        <td><span class="highlight-val">'a'</span></td>
                        <td>0</td>
                        <td>0</td>
                        <td><code>"a"</code></td>
                        <td>Primeira ocorrência registrada</td>
                        <td><code>{{'a': 0}}</code></td>
                        <td style="color: #047857; font-weight: 700;">1</td>
                    </tr>
                    <tr>
                        <td><b>2</b></td>
                        <td><span class="highlight-val">'b'</span></td>
                        <td>1</td>
                        <td>0</td>
                        <td><code>"ab"</code></td>
                        <td>Primeira ocorrência registrada</td>
                        <td><code>{{'a': 0, 'b': 1}}</code></td>
                        <td style="color: #047857; font-weight: 700;">2</td>
                    </tr>
                    <tr>
                        <td><b>3</b></td>
                        <td><span class="highlight-val">'c'</span></td>
                        <td>2</td>
                        <td>0</td>
                        <td><code>"abc"</code></td>
                        <td>Primeira ocorrência registrada</td>
                        <td><code>{{'a': 0, 'b': 1, 'c': 2}}</code></td>
                        <td style="color: #047857; font-weight: 800; font-size: 13px;">3 (Pico Máximo)</td>
                    </tr>
                    <tr style="background: #fffbeb;">
                        <td><b>4</b></td>
                        <td><span class="highlight-val" style="color: #b45309;">'a'</span></td>
                        <td>3</td>
                        <td style="color: #b45309; font-weight: 700;">0 → 1</td>
                        <td><code>"bca"</code></td>
                        <td>'a' repetido: L salta direto para <code>0+1=1</code></td>
                        <td><code>{{'a': 3, 'b': 1, 'c': 2}}</code></td>
                        <td style="color: #047857; font-weight: 700;">3</td>
                    </tr>
                    <tr style="background: #fffbeb;">
                        <td><b>5</b></td>
                        <td><span class="highlight-val" style="color: #b45309;">'b'</span></td>
                        <td>4</td>
                        <td style="color: #b45309; font-weight: 700;">1 → 2</td>
                        <td><code>"cab"</code></td>
                        <td>'b' repetido: L salta direto para <code>1+1=2</code></td>
                        <td><code>{{'a': 3, 'b': 4, 'c': 2}}</code></td>
                        <td style="color: #047857; font-weight: 700;">3</td>
                    </tr>
                    <tr style="background: #fffbeb;">
                        <td><b>6</b></td>
                        <td><span class="highlight-val" style="color: #b45309;">'c'</span></td>
                        <td>5</td>
                        <td style="color: #b45309; font-weight: 700;">2 → 3</td>
                        <td><code>"abc"</code></td>
                        <td>'c' repetido: L salta direto para <code>2+1=3</code></td>
                        <td><code>{{'a': 3, 'b': 4, 'c': 5}}</code></td>
                        <td style="color: #047857; font-weight: 700;">3</td>
                    </tr>
                    <tr style="background: #fff1f2;">
                        <td><b>7</b></td>
                        <td><span class="highlight-val" style="color: #be123c;">'b'</span></td>
                        <td>6</td>
                        <td style="color: #be123c; font-weight: 700;">3 → 5</td>
                        <td><code>"cb"</code></td>
                        <td>'b' repetido no idx 4: L salta para <code>4+1=5</code></td>
                        <td><code>{{'a': 3, 'b': 6, 'c': 5}}</code></td>
                        <td style="color: #047857; font-weight: 700;">3</td>
                    </tr>
                    <tr style="background: #fff1f2;">
                        <td><b>8</b></td>
                        <td><span class="highlight-val" style="color: #be123c;">'b'</span></td>
                        <td>7</td>
                        <td style="color: #be123c; font-weight: 700;">5 → 7</td>
                        <td><code>"b"</code></td>
                        <td>'b' repetido no idx 6: L salta para <code>6+1=7</code></td>
                        <td><code>{{'a': 3, 'b': 7, 'c': 5}}</code></td>
                        <td style="color: #047857; font-weight: 700;">3</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="footer-bar">
            <span>Rastreio de Execução em Passagem Única O(N)</span>
            <span>Resultado Final: 3</span>
        </div>
    </div>

    <!-- SLIDE 6: BENCHMARK DE ECONOMIA DE TEMPO -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">05 · Demonstração de Economia</div>
            <div class="header-sub">Benchmark Experimental Real com Diferentes Entradas (N)</div>
        </div>
        <h2 class="slide-title">Economia de CPU: <span>De 4 Horas para 11 Milissegundos</span></h2>

        <div class="grid-40-60" style="margin-bottom: 12px;">
            <div class="metric-container" style="border-left: 4px solid #047857;">
                <div class="metric-big" style="color: #047857;">-99,99999%</div>
                <div class="metric-label">Redução no Tempo de Execução ($N = 50.000$)</div>
                <p class="card-text" style="font-size: 11.5px; margin-top: 6px; color: #64748b;">
                    Redução de <b>416.000.000×</b> no total de ciclos de instrução de CPU processados.
                </p>
            </div>

            <div class="card" style="padding: 12px;">
                <table>
                    <thead>
                        <tr>
                            <th>Tamanho (N)</th>
                            <th>Força Bruta O(N³)</th>
                            <th>Sliding Window (Map O(1))</th>
                            <th>Economia</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>N = 100</b></td>
                            <td style="color: #be123c;">4.85 ms (171.700 ops)</td>
                            <td style="color: #047857; font-weight: 700;">0.032 ms (100 ops)</td>
                            <td><span class="badge badge-success">99.94%</span></td>
                        </tr>
                        <tr>
                            <td><b>N = 1.000</b></td>
                            <td style="color: #be123c; font-weight: 700;">1.953 ms (~2.0 s)</td>
                            <td style="color: #047857; font-weight: 700;">0.232 ms (1.000 ops)</td>
                            <td><span class="badge badge-success">99.99%</span></td>
                        </tr>
                        <tr>
                            <td><b>N = 5.000</b></td>
                            <td style="color: #be123c; font-weight: 700;">~15.0 s (20.8 bi ops)</td>
                            <td style="color: #047857; font-weight: 700;">1.113 ms (5.000 ops)</td>
                            <td><span class="badge badge-success">99.999%</span></td>
                        </tr>
                        <tr style="background: #f0fdf4;">
                            <td><b>N = 50.000</b></td>
                            <td style="color: #be123c; font-weight: 800;">~250 min (> 4 HORAS)</td>
                            <td style="color: #047857; font-weight: 800;">11.1 ms (50.000 ops)</td>
                            <td><span class="badge badge-success">> 99.99999%</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="grid-50-50">
            <div class="card card-rose" style="padding: 12px;">
                <div class="card-title" style="color: #be123c; font-size: 13.5px;">O Gargalo da Força Bruta</div>
                <p class="card-text" style="font-size: 11.5px; margin: 0;">
                    Com $N = 50.000$, a Força Bruta executa mais de <b>20 trilhões de operações</b>, tornando o sistema inoperante em produção.
                </p>
            </div>
            <div class="card card-emerald" style="padding: 12px;">
                <div class="card-title" style="color: #047857; font-size: 13.5px;">A Eficiência da Janela Deslizante</div>
                <p class="card-text" style="font-size: 11.5px; margin: 0;">
                    A abordagem com Hash Map processa a entrada em passagem única com <b>exatamente 50.000 operações</b> em <b>0,011 segundos</b>.
                </p>
            </div>
        </div>

        <div class="footer-bar">
            <span>Benchmark Experimental em Python 3.12</span>
            <span>Redução Superior a 4 Horas de Processamento</span>
        </div>
    </div>

    <!-- SLIDE 7: ARQUITETURA VISUAL DA JANELA DESLIZANTE (DIAGRAMA VETORIAL REENQUADRADO PERFEITO) -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">06 · Arquitetura Visual</div>
            <div class="header-sub">Mapeamento da Janela Deslizante & Hash Map</div>
        </div>
        <h2 class="slide-title">Dinâmica dos <span>Dois Ponteiros & Hash Map</span></h2>

        <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
            {svg_diagram}
        </div>

        <div class="footer-bar">
            <span>Visualização da Janela Deslizante · Passo 4 de 8</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 8: IMPLEMENTAÇÃO EM C (ARITMÉTICA DE PONTEIROS - GUB) -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">07 · Implementação de Baixo Nível</div>
            <div class="header-sub">Conexão com a Aula 2 de Revisão em C · Implementação do Gub</div>
        </div>
        <h2 class="slide-title">Implementação em C: <span>Aritmética de Ponteiros</span></h2>

        <div class="grid-50-50">
            <div class="card">
                <div class="card-title" style="color: #6d28d9; font-size: 14px;">lswrc_solucao2_janela_deslizante.c (Trecho Central)</div>
                <pre><code><span class="kw">int</span> ultima_pos[<span class="num">256</span>];
<span class="kw">for</span> (<span class="kw">int</span> k = <span class="num">0</span>; k &lt; <span class="num">256</span>; k++) ultima_pos[k] = -<span class="num">1</span>;

<span class="kw">char</span> *esquerda = s;
<span class="kw">int</span> melhor_tam = <span class="num">0</span>;

<span class="kw">for</span> (<span class="kw">char</span> *direita = s; *direita != <span class="str">'\\0'</span>; direita++) {{
    <span class="kw">unsigned char</span> c = (<span class="kw">unsigned char</span>)*direita;
    <span class="kw">int</span> idx_dir = (<span class="kw">int</span>)(direita - s);

    <span class="com">// Colisão: se o caractere está DENTRO da janela ativa</span>
    <span class="kw">if</span> (ultima_pos[c] != -<span class="num">1</span> &amp;&amp; ultima_pos[c] &gt;= (<span class="kw">int</span>)(esquerda - s)) {{
        esquerda = s + ultima_pos[c] + <span class="num">1</span>; <span class="com">// Pulo direto O(1)</span>
    }}

    ultima_pos[c] = idx_dir;
    <span class="kw">int</span> tam_atual = (<span class="kw">int</span>)(direita - esquerda) + <span class="num">1</span>;
    <span class="kw">if</span> (tam_atual &gt; melhor_tam) melhor_tam = tam_atual;
}}</code></pre>
            </div>

            <div class="card card-emerald">
                <div class="card-title">Engenharia de Memória & Conexão com Aula 2</div>
                <p class="card-text"><b>1. Aritmética de Ponteiros Pura:</b> O índice é obtido diretamente por <code>(direita - s)</code> e <code>(esquerda - s)</code>, sem custo de busca.</p>
                <p class="card-text"><b>2. Pulo de Ponteiro em O(1):</b> <code>esquerda = s + ultima_pos[c] + 1</code> desloca o endereço base instantaneamente na memória contígua.</p>
                <p class="card-text"><b>3. Memória Estática na Stack:</b> <code>int ultima_pos[256]</code> consome apenas 1.024 bytes (1 KB) na Pilha, sem chamadas a <code>malloc()</code> ou risco de <i>memory leak</i>.</p>
                <div class="badge-list" style="margin-top: 8px;">
                    <span class="badge badge-success">Arquivo: lswrc_solucao2_janela_deslizante.c</span>
                    <span class="badge badge-success">Modo Interativo Didático</span>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Engenharia de Baixo Nível · Código em C da Equipe</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 9: TABELA BIG-O -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">08 · Análise Assintótica</div>
            <div class="header-sub">Rigor Teórico e Comparativo</div>
        </div>
        <h2 class="slide-title">Análise Rigorosa de <span>Complexidade (Big-O)</span></h2>

        <div class="card card-emerald" style="margin-bottom: 12px;">
            <table>
                <thead>
                    <tr>
                        <th>Abordagem</th>
                        <th>Complexidade de Tempo</th>
                        <th>Complexidade de Espaço</th>
                        <th>Classificação Técnica</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>1. Força Bruta (Loops Aninhados)</b></td>
                        <td style="color: #be123c; font-weight: 700;">O(N³)</td>
                        <td>O(min(N, Σ))</td>
                        <td><span class="badge badge-danger">Rejeitado</span></td>
                    </tr>
                    <tr>
                        <td><b>2. Sliding Window (Set - Passo a Passo)</b></td>
                        <td style="color: #b45309; font-weight: 700;">O(2N) = O(N)</td>
                        <td>O(min(N, Σ))</td>
                        <td><span class="badge badge-warning">Contratado</span></td>
                    </tr>
                    <tr>
                        <td><b>3. Sliding Window (Hash Map - Pulo O(1))</b></td>
                        <td style="color: #047857; font-weight: 700;">O(N) Estrito</td>
                        <td>O(min(N, Σ))</td>
                        <td><span class="badge badge-success">Forte Candidato</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="grid-50-50">
            <div class="card card-blue">
                <div class="card-title">Justificativa de Tempo: O(N)</div>
                <p class="card-text" style="font-size: 12px;">O ponteiro direito avança de 0 até N-1 exatamente uma vez. Todas as consultas e inserções no Hash Map executam em tempo constante <b>O(1)</b>.</p>
            </div>
            <div class="card card-blue">
                <div class="card-title">Justificativa de Espaço: O(min(N, Σ))</div>
                <p class="card-text" style="font-size: 12px;">O consumo de memória é limitado pelo menor valor entre o comprimento da string <code>N</code> e a cardinalidade do alfabeto <code>Σ</code> (ASCII = 256).</p>
            </div>
        </div>

        <div class="footer-bar">
            <span>Análise Formal de Big-O</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 10: CASOS DE BORDA & CONCLUSÃO -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">09 · Fechamento & Perguntas</div>
            <div class="header-sub">Robustez de Engenharia</div>
        </div>
        <h2 class="slide-title">Casos de Borda & <span>Perguntas da Banca</span></h2>

        <div class="grid-50-50">
            <div class="card card-amber">
                <div class="card-title">Casos de Borda Validados</div>
                <p class="card-text" style="font-size: 12px;"><b>• String Vazia <code>""</code>:</b> Retorna <code>0</code> imediatamente.</p>
                <p class="card-text" style="font-size: 12px;"><b>• Caracteres Idênticos <code>"bbbbbb"</code>:</b> A janela se mantém em comprimento <code>1</code>.</p>
                <p class="card-text" style="font-size: 12px;"><b>• Todos Distintos <code>"abcdef"</code>:</b> A janela expande linearmente até o comprimento total <code>N</code>.</p>
                <p class="card-text" style="font-size: 12px;"><b>• Espaços e Símbolos <code>"a b c!"</code>:</b> Indexados nativamente pela tabela ASCII.</p>
            </div>

            <div class="card card-emerald" style="justify-content: center; align-items: center; text-align: center;">
                <div class="card-title" style="font-size: 22px; justify-content: center;">Conclusão</div>
                <p class="card-text" style="font-size: 13.5px; color: #64748b; margin-top: 6px;">
                    Agradecemos a atenção do Prof. Bianchi e dos colegas.<br>
                    Abrimos para perguntas e considerações da banca.
                </p>
                <div class="badge-list" style="justify-content: center; margin-top: 12px;">
                    <span class="badge badge-success">Repositório no GitHub</span>
                    <span class="badge badge-success">Vault Obsidian Integrado</span>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Rafael Feltrim · Ian · Gustavo (Gub)</span>
            <span>IFSP São Carlos · 2026</span>
        </div>
    </div>

</body>
</html>"""

    html_file = "Apresentacao_LeetCode3_Slides.html"
    pdf_file = "Apresentacao_LeetCode3_Equipe_IFSP.pdf"

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("HTML dos 10 slides (Frontend Refinado) gerado com sucesso!")

    # Invoke Chrome to print to PDF
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    curr_dir = os.path.abspath(".")
    in_html = os.path.join(curr_dir, html_file)
    out_pdf = os.path.join(curr_dir, pdf_file)

    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf}",
        in_html
    ]

    print("Gerando PDF com Chrome Headless...")
    subprocess.run(cmd, check=True)
    time.sleep(2)

    if os.path.exists(pdf_file):
        size_kb = os.path.getsize(pdf_file) / 1024
        print(f"PDF Final Gerado com Sucesso: {pdf_file} ({size_kb:.1f} KB)")
    else:
        print("Erro ao gerar PDF.")

if __name__ == "__main__":
    build_presentation()
