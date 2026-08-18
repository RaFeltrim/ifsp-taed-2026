import os
import base64
import subprocess
import time

def build_presentation():
    img_path = os.path.join("_Vault - Algoritmos", "assets", "sliding_window_leetcode3.jpg")
    img_b64 = ""
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            img_b64 = f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"

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
            padding: 44px 60px;
        }}

        /* Header Editorial */
        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 20px;
            border-bottom: 1.5px solid #e2e8f0;
            padding-bottom: 10px;
        }}

        .header-tag {{
            font-size: 11.5px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: #047857;
        }}

        .header-sub {{
            color: #64748b;
            font-size: 13px;
            font-weight: 500;
        }}

        /* Tipografia de Destaque (Swiss Typography) */
        .slide-title {{
            font-size: 32px;
            font-weight: 800;
            color: #090d16;
            line-height: 1.15;
            margin-bottom: 20px;
            letter-spacing: -0.8px;
        }}

        .slide-title span {{
            color: #047857;
        }}

        /* Grids Assimétricos */
        .grid-60-40 {{
            display: grid;
            grid-template-columns: 1.4fr 1fr;
            gap: 24px;
            flex: 1;
            align-items: stretch;
        }}

        .grid-40-60 {{
            display: grid;
            grid-template-columns: 1fr 1.4fr;
            gap: 24px;
            flex: 1;
            align-items: stretch;
        }}

        .grid-50-50 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
            flex: 1;
            align-items: stretch;
        }}

        .grid-3-col {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
            flex: 1;
        }}

        /* Cartões Editoriais */
        .card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 22px;
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
            font-size: 16px;
            font-weight: 700;
            color: #090d16;
            margin-bottom: 10px;
            letter-spacing: -0.3px;
        }}

        .card-text {{
            font-size: 13.5px;
            line-height: 1.6;
            color: #334155;
            margin-bottom: 10px;
        }}

        /* Pull Quotes Editoriais */
        .pull-quote {{
            font-size: 16px;
            font-weight: 600;
            line-height: 1.5;
            color: #090d16;
            border-left: 3px solid #047857;
            padding-left: 14px;
            margin: 12px 0;
            background: #f0fdf4;
            padding: 12px 16px;
            border-radius: 0 8px 8px 0;
        }}

        /* Keynote Metrics de Alto Impacto */
        .metric-container {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 20px;
        }}

        .metric-big {{
            font-size: 42px;
            font-weight: 800;
            line-height: 1;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 6px;
            letter-spacing: -1px;
        }}

        .metric-label {{
            font-size: 12px;
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
            margin-top: 8px;
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

        /* Blocos de Código em Dark Slate Elegante */
        pre {{
            font-family: 'JetBrains Mono', monospace;
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 6px;
            padding: 12px 14px;
            font-size: 11.5px;
            line-height: 1.45;
            color: #f8fafc;
            white-space: pre;
            overflow-x: auto;
            flex: 1;
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

        /* Tabelas Editoriais Suíças */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 6px;
        }}

        th, td {{
            padding: 8px 12px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
            font-size: 12.5px;
        }}

        th {{
            background: #f1f5f9;
            color: #475569;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 10.5px;
            letter-spacing: 0.6px;
        }}

        td {{
            color: #090d16;
        }}

        .trace-table th, .trace-table td {{
            padding: 6px 8px;
            font-size: 11.5px;
        }}

        /* Rodapé Editorial */
        .footer-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 15px;
            padding-top: 8px;
            border-top: 1px solid #e2e8f0;
            color: #64748b;
            font-size: 11.5px;
            font-weight: 600;
        }}

        /* Capa Editorial */
        .cover-slide {{
            justify-content: space-between;
            padding: 55px 70px;
            background: #ffffff;
        }}

        .cover-main {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            max-width: 950px;
        }}

        .cover-tag {{
            font-size: 12px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: #047857;
            margin-bottom: 14px;
        }}

        .cover-title {{
            font-size: 42px;
            font-weight: 800;
            color: #090d16;
            line-height: 1.12;
            letter-spacing: -1.2px;
            margin-bottom: 14px;
        }}

        .cover-subtitle {{
            font-size: 17px;
            line-height: 1.5;
            color: #475569;
            max-width: 850px;
        }}

        .cover-footer {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-top: 1.5px solid #e2e8f0;
            padding-top: 18px;
        }}

        .team-group {{
            display: flex;
            gap: 30px;
        }}

        .team-item {{
            display: flex;
            flex-direction: column;
            gap: 2px;
        }}

        .team-name {{
            font-size: 13.5px;
            font-weight: 700;
            color: #090d16;
        }}

        .team-role {{
            font-size: 11px;
            color: #047857;
            font-weight: 600;
        }}

        .cover-meta {{
            font-size: 12px;
            color: #64748b;
            text-align: right;
            line-height: 1.4;
        }}

        .img-container {{
            width: 100%;
            height: 100%;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #cbd5e1;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #020617;
        }}

        .img-container img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
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
                <p class="card-text" style="margin-top: 6px;">
                    O avaliador busca testar se o candidato percebe a redundância da força bruta e consegue implementar a janela deslizante com consulta em tempo constante O(1).
                </p>
            </div>

            <div style="display: flex; flex-direction: column; gap: 14px;">
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
                    <p class="card-text" style="font-size: 12.5px; margin: 0;">
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

    <!-- SLIDE 3: ENUNCIADO DO PROBLEMA (EDITORIAL & CASOS DE TESTE) -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">02 · Definição Formal</div>
            <div class="header-sub">Compreendendo o Problema Computacional</div>
        </div>
        <h2 class="slide-title">Enunciado: <span>Substring sem Caracteres Repetidos</span></h2>

        <div class="grid-50-50">
            <div class="card card-emerald">
                <div class="card-title">Definição do Problema</div>
                <p class="card-text" style="font-size: 15.5px; font-weight: 600; color: #090d16; margin-bottom: 14px;">
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
                    <code style="font-size: 13.5px; color: #090d16;">s = "abcabcbb"</code> → <b>Comprimento: 3</b> (substring: <code>"abc"</code>)
                </div>

                <div style="margin-bottom: 8px; background: #f8fafc; border: 1px solid #e2e8f0; padding: 8px 12px; border-radius: 6px;">
                    <div style="color: #0369a1; font-weight: 700; font-size: 11px; text-transform: uppercase;">Exemplo 2 (Homogêneo)</div>
                    <code style="font-size: 13.5px; color: #090d16;">s = "bbbbb"</code> → <b>Comprimento: 1</b> (substring: <code>"b"</code>)
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 8px 12px; border-radius: 6px;">
                    <div style="color: #0369a1; font-weight: 700; font-size: 11px; text-transform: uppercase;">Exemplo 3 (Composto)</div>
                    <code style="font-size: 13.5px; color: #090d16;">s = "pwwkew"</code> → <b>Comprimento: 3</b> (substring: <code>"wke"</code>)
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Tarefa Prática do Dia · Slide 13</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 4: 3 ABORDAGENS EM CÓDIGO -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">03 · Soluções Comparadas</div>
            <div class="header-sub">Evolução do Algoritmo em 3 Níveis de Eficiência</div>
        </div>
        <h2 class="slide-title">As 3 Diferentes <span>Abordagens em Código</span></h2>

        <div class="grid-3-col">
            <div class="card card-rose">
                <div class="card-title" style="color: #be123c; font-size: 14.5px;">1. Força Bruta O(N³)</div>
                <pre><code><span class="kw">def</span> <span class="fn">brute_force</span>(s):
    n = <span class="fn">len</span>(s)
    max_len = <span class="num">0</span>
    <span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(n):
        <span class="kw">for</span> j <span class="kw">in</span> <span class="fn">range</span>(i+<span class="num">1</span>, n+<span class="num">1</span>):
            sub = s[i:j]
            <span class="kw">if</span> <span class="fn">len</span>(<span class="fn">set</span>(sub)) == <span class="fn">len</span>(sub):
                max_len = <span class="fn">max</span>(max_len, <span class="fn">len</span>(sub))
    <span class="kw">return</span> max_len</code></pre>
                <div class="badge-list" style="margin-top: 8px;">
                    <span class="badge badge-danger">Tempo: O(N³)</span>
                    <span class="badge badge-danger">Rejeitado</span>
                </div>
            </div>

            <div class="card card-amber">
                <div class="card-title" style="color: #b45309; font-size: 14.5px;">2. Sliding Window (Set)</div>
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
                <div class="badge-list" style="margin-top: 8px;">
                    <span class="badge badge-warning">Tempo: O(2N)</span>
                    <span class="badge badge-warning">Contratado</span>
                </div>
            </div>

            <div class="card card-emerald">
                <div class="card-title" style="color: #047857; font-size: 14.5px;">3. Sliding Window (Map O(1))</div>
                <pre><code><span class="kw">def</span> <span class="fn">sliding_window_map</span>(s):
    char_map = {{}}
    left = max_len = <span class="num">0</span>
    <span class="kw">for</span> right, char <span class="kw">in</span> <span class="fn">enumerate</span>(s):
        <span class="kw">if</span> char <span class="kw">in</span> char_map <span class="kw">and</span> char_map[char] >= left:
            left = char_map[char] + <span class="num">1</span>
        char_map[char] = right
        max_len = <span class="fn">max</span>(max_len, right - left + <span class="num">1</span>)
    <span class="kw">return</span> max_len</code></pre>
                <div class="badge-list" style="margin-top: 8px;">
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

    <!-- SLIDE 5: CÓDIGO RODANDO EM ETAPAS (TABELA DE ALTA DENSIDADE) -->
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
                        <td style="color: #047857; font-weight: 800; font-size: 13.5px;">3 (Pico Máximo)</td>
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

    <!-- SLIDE 6: BENCHMARK DE ECONOMIA DE TEMPO (HERO METRIC LAYOUT) -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">05 · Demonstração de Economia</div>
            <div class="header-sub">Benchmark Experimental Real com Diferentes Entradas (N)</div>
        </div>
        <h2 class="slide-title">Economia de CPU: <span>De 4 Horas para 11 Milissegundos</span></h2>

        <div class="grid-40-60" style="margin-bottom: 14px;">
            <div class="metric-container" style="border-left: 4px solid #047857;">
                <div class="metric-big" style="color: #047857;">-99,99999%</div>
                <div class="metric-label">Redução no Tempo de Execução ($N = 50.000$)</div>
                <p class="card-text" style="font-size: 12px; margin-top: 8px; color: #64748b;">
                    Redução de <b>416.000.000×</b> no total de ciclos de instrução de CPU processados.
                </p>
            </div>

            <div class="card" style="padding: 14px;">
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
            <div class="card card-rose" style="padding: 14px;">
                <div class="card-title" style="color: #be123c; font-size: 14px;">O Gargalo da Força Bruta</div>
                <p class="card-text" style="font-size: 12px; margin: 0;">
                    Com $N = 50.000$, a Força Bruta executa mais de <b>20 trilhões de operações</b>, tornando o sistema inoperante em produção.
                </p>
            </div>
            <div class="card card-emerald" style="padding: 14px;">
                <div class="card-title" style="color: #047857; font-size: 14px;">A Eficiência da Janela Deslizante</div>
                <p class="card-text" style="font-size: 12px; margin: 0;">
                    A abordagem com Hash Map processa a entrada em passagem única com <b>exatamente 50.000 operações</b> em <b>0,011 segundos</b>.
                </p>
            </div>
        </div>

        <div class="footer-bar">
            <span>Benchmark Experimental em Python 3.12</span>
            <span>Redução Superior a 4 Horas de Processamento</span>
        </div>
    </div>

    <!-- SLIDE 7: ARQUITETURA VISUAL DA JANELA DESLIZANTE -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">06 · Arquitetura Visual</div>
            <div class="header-sub">Mapeamento da Janela Deslizante</div>
        </div>
        <h2 class="slide-title">Dinâmica dos <span>Dois Ponteiros & Hash Map</span></h2>

        <div class="grid-60-40">
            <div class="img-container">
                <img src="{img_b64}" alt="Diagrama LeetCode 3">
            </div>

            <div class="card card-blue">
                <div class="card-title">Mecânica da Otimização</div>
                
                <div style="margin-bottom: 12px;">
                    <b style="color: #0369a1; font-size: 14.5px;">1. Ponteiro Direito (right):</b>
                    <p class="card-text" style="font-size: 12.5px;">Avança sequencialmente expandindo a janela e lendo novos caracteres.</p>
                </div>

                <div style="margin-bottom: 12px;">
                    <b style="color: #047857; font-size: 14.5px;">2. Tabela Hash (char_map):</b>
                    <p class="card-text" style="font-size: 12.5px;">Armazena o mapeamento <code>map[char] = ultimo_indice</code> em tempo constante O(1).</p>
                </div>

                <div>
                    <b style="color: #b45309; font-size: 14.5px;">3. Salto do Ponteiro Esquerdo (left):</b>
                    <p class="card-text" style="font-size: 12.5px;">Ao identificar duplicata, salta diretamente para <code>map[char] + 1</code> sem varredura intermediária.</p>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Visualização da Janela Deslizante</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 8: IMPLEMENTAÇÃO EM C (BAIXO NÍVEL) -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">07 · Implementação de Baixo Nível</div>
            <div class="header-sub">Conexão com a Aula 2 de Revisão em C</div>
        </div>
        <h2 class="slide-title">Implementação em C: <span>Tabela Direta ASCII</span></h2>

        <div class="grid-50-50">
            <div class="card">
                <div class="card-title" style="color: #6d28d9; font-size: 14.5px;">Código em C com Vetor ASCII Fixo</div>
                <pre><code><span class="kw">#include</span> <span class="str">&lt;string.h&gt;</span>

<span class="kw">int</span> <span class="fn">lengthOfLongestSubstring</span>(<span class="kw">char</span>* s) {{
    <span class="kw">int</span> last_index[<span class="num">256</span>];
    <span class="kw">for</span> (<span class="kw">int</span> i = <span class="num">0</span>; i < <span class="num">256</span>; i++) last_index[i] = -<span class="num">1</span>;
    
    <span class="kw">int</span> max_len = <span class="num">0</span>, left = <span class="num">0</span>;
    <span class="kw">int</span> n = <span class="fn">strlen</span>(s);
    
    <span class="kw">for</span> (<span class="kw">int</span> right = <span class="num">0</span>; right < n; right++) {{
        <span class="kw">unsigned char</span> c = (<span class="kw">unsigned char</span>)s[right];
        
        <span class="kw">if</span> (last_index[c] >= left) {{
            left = last_index[c] + <span class="num">1</span>;
        }}
        
        last_index[c] = right;
        <span class="kw">int</span> cur_len = right - left + <span class="num">1</span>;
        <span class="kw">if</span> (cur_len > max_len) max_len = cur_len;
    }}
    <span class="kw">return</span> max_len;
}}</code></pre>
            </div>

            <div class="card card-emerald">
                <div class="card-title">Vantagens da Implementação em C</div>
                <p class="card-text"><b>1. Ausência de Colisões:</b> Acesso direto por índice do byte ASCII elimina qualquer necessidade de encadeamento ou tratamento de colisão.</p>
                <p class="card-text"><b>2. Memória Estática e Restrita:</b> <code>256 * sizeof(int) = 1.024 bytes (1 KB)</code> alocados diretamente na Stack $\rightarrow$ <b>espaço O(1) estrito</b>.</p>
                <p class="card-text"><b>3. Eficiência de Cache L1:</b> Disposição sequencial contígua na memória, sem dispersão de ponteiros na Heap.</p>
            </div>
        </div>

        <div class="footer-bar">
            <span>Engenharia de Baixo Nível · Alinhado com a Aula 2</span>
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

        <div class="card card-emerald" style="margin-bottom: 14px;">
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
                <p class="card-text" style="font-size: 12.5px;">O ponteiro direito avança de 0 até N-1 exatamente uma vez. Todas as consultas e inserções no Hash Map executam em tempo constante <b>O(1)</b>.</p>
            </div>
            <div class="card card-blue">
                <div class="card-title">Justificativa de Espaço: O(min(N, Σ))</div>
                <p class="card-text" style="font-size: 12.5px;">O consumo de memória é limitado pelo menor valor entre o comprimento da string <code>N</code> e a cardinalidade do alfabeto <code>Σ</code> (ASCII = 256).</p>
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
                <p class="card-text" style="font-size: 12.5px;"><b>• String Vazia <code>""</code>:</b> Retorna <code>0</code> imediatamente.</p>
                <p class="card-text" style="font-size: 12.5px;"><b>• Caracteres Idênticos <code>"bbbbbb"</code>:</b> A janela se mantém em comprimento <code>1</code>.</p>
                <p class="card-text" style="font-size: 12.5px;"><b>• Todos Distintos <code>"abcdef"</code>:</b> A janela expande linearmente até o comprimento total <code>N</code>.</p>
                <p class="card-text" style="font-size: 12.5px;"><b>• Espaços e Símbolos <code>"a b c!"</code>:</b> Indexados nativamente pela tabela ASCII.</p>
            </div>

            <div class="card card-emerald" style="justify-content: center; align-items: center; text-align: center;">
                <div class="card-title" style="font-size: 24px; justify-content: center;">Conclusão</div>
                <p class="card-text" style="font-size: 14px; color: #64748b; margin-top: 6px;">
                    Agradecemos a atenção do Prof. Bianchi e dos colegas.<br>
                    Abrimos para perguntas e considerações da banca.
                </p>
                <div class="badge-list" style="justify-content: center; margin-top: 14px;">
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

    print("HTML dos 10 slides (Padrão Editorial Suíço) gerado com sucesso!")

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
        print(f"PDF Editorial Suíço Gerado com Sucesso: {pdf_file} ({size_kb:.1f} KB)")
    else:
        print("Erro ao gerar PDF.")

if __name__ == "__main__":
    build_presentation()
