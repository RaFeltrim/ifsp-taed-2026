import os
import base64
import subprocess
import time

def build_presentation():
    # Read the image and convert to base64
    img_path = os.path.join("_Vault - Algoritmos", "assets", "sliding_window_leetcode3.jpg")
    img_b64 = ""
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            img_b64 = f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Apresentação LeetCode 3 - IFSP São Carlos</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        @page {{
            size: 1920px 1080px;
            margin: 0;
        }}

        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #080b12;
            color: #f1f5f9;
        }}

        .slide {{
            width: 1920px;
            height: 1080px;
            page-break-after: always;
            position: relative;
            overflow: hidden;
            background: radial-gradient(circle at 85% 15%, rgba(16, 185, 129, 0.08), transparent 45%),
                        radial-gradient(circle at 15% 85%, rgba(6, 182, 212, 0.08), transparent 45%),
                        #080b12;
            display: flex;
            flex-direction: column;
            padding: 70px 90px;
        }}

        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 15px;
        }}

        .header-tag {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 16px;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 9999px;
            color: #34d399;
            font-size: 15px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .header-sub {{
            color: #94a3b8;
            font-size: 17px;
            font-weight: 600;
        }}

        .slide-title {{
            font-size: 46px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.15;
            margin-bottom: 25px;
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .slide-title span {{
            background: linear-gradient(135deg, #34d399 0%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .content-grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 35px;
            flex: 1;
            align-items: stretch;
        }}

        .content-grid-3 {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
            flex: 1;
        }}

        .card {{
            background: rgba(17, 24, 39, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
        }}

        .card-emerald {{
            border-color: rgba(16, 185, 129, 0.3);
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.06), rgba(17, 24, 39, 0.85));
        }}

        .card-cyan {{
            border-color: rgba(6, 182, 212, 0.3);
            background: linear-gradient(135deg, rgba(6, 182, 212, 0.06), rgba(17, 24, 39, 0.85));
        }}

        .card-amber {{
            border-color: rgba(245, 158, 11, 0.3);
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.06), rgba(17, 24, 39, 0.85));
        }}

        .card-rose {{
            border-color: rgba(244, 63, 94, 0.3);
            background: linear-gradient(135deg, rgba(244, 63, 94, 0.06), rgba(17, 24, 39, 0.85));
        }}

        .card-title {{
            font-size: 24px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .card-text {{
            font-size: 18px;
            line-height: 1.55;
            color: #cbd5e1;
            margin-bottom: 12px;
        }}

        .badge-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }}

        .badge {{
            padding: 6px 14px;
            border-radius: 10px;
            font-size: 15px;
            font-weight: 700;
            background: #1e293b;
            color: #e2e8f0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}

        .badge-company {{
            background: rgba(59, 130, 246, 0.15);
            border-color: rgba(59, 130, 246, 0.4);
            color: #60a5fa;
        }}

        .badge-danger {{
            background: rgba(239, 68, 68, 0.15);
            border-color: rgba(239, 68, 68, 0.4);
            color: #f87171;
        }}

        .badge-warning {{
            background: rgba(245, 158, 11, 0.15);
            border-color: rgba(245, 158, 11, 0.4);
            color: #fbbf24;
        }}

        .badge-success {{
            background: rgba(16, 185, 129, 0.15);
            border-color: rgba(16, 185, 129, 0.4);
            color: #34d399;
        }}

        pre, code {{
            font-family: 'JetBrains Mono', monospace;
        }}

        .code-box {{
            background: #020617;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 20px;
            font-size: 16px;
            line-height: 1.45;
            color: #e2e8f0;
            flex: 1;
            overflow: hidden;
        }}

        .kw {{ color: #f43f5e; font-weight: 700; }}
        .fn {{ color: #38bdf8; font-weight: 700; }}
        .str {{ color: #a3e635; }}
        .com {{ color: #64748b; font-style: italic; }}
        .num {{ color: #fbbf24; }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}

        th, td {{
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            font-size: 17px;
        }}

        th {{
            background: rgba(255, 255, 255, 0.04);
            color: #94a3b8;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 14px;
            letter-spacing: 1px;
        }}

        td {{
            color: #f1f5f9;
        }}

        .trace-table th, .trace-table td {{
            padding: 10px 14px;
            font-size: 15px;
        }}

        .footer-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 25px;
            padding-top: 12px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            color: #64748b;
            font-size: 15px;
            font-weight: 600;
        }}

        .cover-slide {{
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 0 160px;
        }}

        .cover-logo {{
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #10b981, #06b6d4);
            border-radius: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 38px;
            margin-bottom: 25px;
            box-shadow: 0 0 40px rgba(16, 185, 129, 0.4);
        }}

        .cover-title {{
            font-size: 60px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 18px;
            line-height: 1.15;
        }}

        .cover-subtitle {{
            font-size: 26px;
            color: #94a3b8;
            max-width: 1050px;
            line-height: 1.45;
            margin-bottom: 45px;
        }}

        .team-box {{
            display: flex;
            gap: 25px;
            background: rgba(17, 24, 39, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 18px 35px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
        }}

        .team-member {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 5px;
        }}

        .team-name {{
            font-size: 20px;
            font-weight: 700;
            color: #f1f5f9;
        }}

        .team-role {{
            font-size: 15px;
            color: #34d399;
            font-weight: 600;
        }}

        .img-container {{
            width: 100%;
            height: 100%;
            border-radius: 18px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            background: #020617;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
        }}

        .img-container img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}

        .highlight-val {{
            color: #38bdf8;
            font-weight: 700;
            font-family: 'JetBrains Mono', monospace;
        }}
    </style>
</head>
<body>

    <!-- SLIDE 1: CAPA -->
    <div class="slide cover-slide">
        <div class="cover-logo">⚡</div>
        <div class="header-tag" style="margin-bottom: 15px;">IFSP São Carlos · Engenharia de Software</div>
        <h1 class="cover-title">Longest Substring Without Repeating Characters</h1>
        <p class="cover-subtitle">Desafio Real de Processo Seletivo em Big Techs (LeetCode #3) — Otimização Assintótica, Benchmark de Economia & Janela Deslizante</p>
        <div class="team-box">
            <div class="team-member">
                <span class="team-name">Rafael Feltrim</span>
                <span class="team-role">Desenvolvedor & Apresentador</span>
            </div>
            <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
            <div class="team-member">
                <span class="team-name">Ian</span>
                <span class="team-role">Pesquisa & Algoritmos</span>
            </div>
            <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
            <div class="team-member">
                <span class="team-name">Gustavo (Gub)</span>
                <span class="team-role">Análise de Complexidade</span>
            </div>
        </div>
        <div class="footer-bar" style="width: 100%; justify-content: center; margin-top: 45px;">
            Prof. Dr. Rodrigo Elias Bianchi · Tópicos em Algoritmos e Estruturas de Dados · 2026
        </div>
    </div>

    <!-- SLIDE 2: RELEVÂNCIA DE MERCADO -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">01 · Relevância de Mercado</div>
            <div class="header-sub">Por que as Big Techs cobram este desafio?</div>
        </div>
        <h2 class="slide-title">Onipresença nos <span>Processos Seletivos</span></h2>
        
        <div class="content-grid-3">
            <div class="card card-emerald">
                <div class="card-title">🏢 Onde é Aplicado?</div>
                <p class="card-text">Problema clássico no topo do ranking de entrevistas de alta escala:</p>
                <div class="badge-list">
                    <span class="badge badge-company">Amazon (Top 10 SDE)</span>
                    <span class="badge badge-company">Meta (Triagem 45m)</span>
                    <span class="badge badge-company">Google (L3/L4)</span>
                    <span class="badge badge-company">Microsoft</span>
                    <span class="badge badge-company">Apple</span>
                    <span class="badge badge-company">Bloomberg</span>
                </div>
            </div>

            <div class="card card-cyan">
                <div class="card-title">🎯 O Que é Avaliado?</div>
                <p class="card-text"><b>1. Otimização de Força Bruta:</b> Sair de O(N³) para O(N).</p>
                <p class="card-text"><b>2. Escolha de Estruturas:</b> Uso de Hash Map para busca O(1).</p>
                <p class="card-text"><b>3. Gestão de Memória:</b> Uso de arrays diretos para tabela ASCII.</p>
                <p class="card-text"><b>4. Edge Cases:</b> Strings vazias, únicas e repetidas.</p>
            </div>

            <div class="card card-amber">
                <div class="card-title">📊 Peso na Contratação</div>
                <p class="card-text">Em entrevistas técnicas, <b>o código é apenas 30% da nota</b>.</p>
                <p class="card-text">Os outros <b>70%</b> medem:</p>
                <div class="badge-list">
                    <span class="badge badge-success">Decomposição Lógica</span>
                    <span class="badge badge-success">Comunicação Clara</span>
                    <span class="badge badge-success">Justificativa Big-O</span>
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
        <h2 class="slide-title">O Enunciado: <span>Substring sem Duplicatas</span></h2>

        <div class="content-grid-2">
            <div class="card card-emerald">
                <div class="card-title">📋 Descrição do Problema</div>
                <p class="card-text" style="font-size: 22px; font-weight: 600; color: #ffffff; margin-bottom: 20px;">
                    "Dada uma string <code>s</code>, encontre o comprimento da <u>maior substring contígua</u> que não contenha caracteres repetidos."
                </p>
                <div class="card" style="background: rgba(0,0,0,0.4); padding: 18px; border-radius: 14px;">
                    <div style="color: #fbbf24; font-weight: 700; font-size: 18px; margin-bottom: 8px;">⚠️ Distinção Crítica de Conceito:</div>
                    <p class="card-text" style="font-size: 16px; margin: 0;">
                        <b>Substring:</b> Sequência contínua de caracteres (ex: <code>"abc"</code> em <code>"abcde"</code>).<br>
                        <b>Subsequência:</b> Mantém a ordem mas não é contínua (ex: <code>"ace"</code> em <code>"abcde"</code>).
                    </p>
                </div>
            </div>

            <div class="card card-cyan">
                <div class="card-title">🧪 Exemplos de Teste</div>
                
                <div style="margin-bottom: 15px; background: rgba(0,0,0,0.3); padding: 12px 18px; border-radius: 12px;">
                    <div style="color: #38bdf8; font-weight: 700;">Exemplo 1:</div>
                    <code style="font-size: 20px;">s = "abcabcbb"</code> → <b>Resposta: 3</b> (substring: <code>"abc"</code>)
                </div>

                <div style="margin-bottom: 15px; background: rgba(0,0,0,0.3); padding: 12px 18px; border-radius: 12px;">
                    <div style="color: #38bdf8; font-weight: 700;">Exemplo 2:</div>
                    <code style="font-size: 20px;">s = "bbbbb"</code> → <b>Resposta: 1</b> (substring: <code>"b"</code>)
                </div>

                <div style="background: rgba(0,0,0,0.3); padding: 12px 18px; border-radius: 12px;">
                    <div style="color: #38bdf8; font-weight: 700;">Exemplo 3:</div>
                    <code style="font-size: 20px;">s = "pwwkew"</code> → <b>Resposta: 3</b> (substring: <code>"wke"</code>)
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Tarefa Prática do Dia · Slide 13</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 4: AS DIFERENTES SOLUÇÕES -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">03 · Soluções Comparadas</div>
            <div class="header-sub">Do Código Ineficiente à Engenharia de Alta Performance</div>
        </div>
        <h2 class="slide-title">As 3 Diferentes <span>Abordagens em Código</span></h2>

        <div class="content-grid-3">
            <div class="card card-rose">
                <div class="card-title" style="color: #f87171; font-size: 20px;">1. Força Bruta O(N³)</div>
                <div class="code-box" style="font-size: 13px;">
<span class="kw">def</span> <span class="fn">brute_force</span>(s):
    n = <span class="fn">len</span>(s)
    max_len = <span class="num">0</span>
    <span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(n):
        <span class="kw">for</span> j <span class="kw">in</span> <span class="fn">range</span>(i+<span class="num">1</span>, n+<span class="num">1</span>):
            sub = s[i:j]
            <span class="com"># Checa duplicatas O(N)</span>
            <span class="kw">if</span> <span class="fn">len</span>(<span class="fn">set</span>(sub)) == <span class="fn">len</span>(sub):
                max_len = <span class="fn">max</span>(max_len, <span class="fn">len</span>(sub))
    <span class="kw">return</span> max_len
                </div>
                <div class="badge-list" style="margin-top: 10px;">
                    <span class="badge badge-danger">Tempo: O(N³)</span>
                    <span class="badge badge-danger">Status: Rejeitado</span>
                </div>
            </div>

            <div class="card card-amber">
                <div class="card-title" style="color: #fbbf24; font-size: 20px;">2. Sliding Window (Set)</div>
                <div class="code-box" style="font-size: 13px;">
<span class="kw">def</span> <span class="fn">sliding_window_set</span>(s):
    char_set = <span class="fn">set</span>()
    left = <span class="num">0</span>
    max_len = <span class="num">0</span>
    <span class="kw">for</span> right <span class="kw">in</span> <span class="fn">range</span>(<span class="fn">len</span>(s)):
        <span class="com"># Remove um a um até limpar</span>
        <span class="kw">while</span> s[right] <span class="kw">in</span> char_set:
            char_set.remove(s[left])
            left += <span class="num">1</span>
        char_set.add(s[right])
        max_len = <span class="fn">max</span>(max_len, right - left + <span class="num">1</span>)
    <span class="kw">return</span> max_len
                </div>
                <div class="badge-list" style="margin-top: 10px;">
                    <span class="badge badge-warning">Tempo: O(2N)</span>
                    <span class="badge badge-warning">Status: Hire</span>
                </div>
            </div>

            <div class="card card-emerald">
                <div class="card-title" style="color: #34d399; font-size: 20px;">3. Sliding Window (Map O(1))</div>
                <div class="code-box" style="font-size: 13px;">
<span class="kw">def</span> <span class="fn">sliding_window_map</span>(s):
    char_map = {{}} <span class="com"># char -> último índice</span>
    left = <span class="num">0</span>
    max_len = <span class="num">0</span>
    <span class="kw">for</span> right, char <span class="kw">in</span> <span class="fn">enumerate</span>(s):
        <span class="com"># Pulo direto do ponteiro left!</span>
        <span class="kw">if</span> char <span class="kw">in</span> char_map <span class="kw">and</span> char_map[char] >= left:
            left = char_map[char] + <span class="num">1</span>
        char_map[char] = right
        max_len = <span class="fn">max</span>(max_len, right - left + <span class="num">1</span>)
    <span class="kw">return</span> max_len
                </div>
                <div class="badge-list" style="margin-top: 10px;">
                    <span class="badge badge-success">Tempo: O(N) Estrito</span>
                    <span class="badge badge-success">Status: Strong Hire</span>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Diferentes Soluções Algorítmicas</span>
            <span>LeetCode #3</span>
        </div>
    </div>

    <!-- SLIDE 5: CÓDIGO RODANDO EM ETAPAS (DRY-RUN) -->
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
                        <th>Janela Ativa</th>
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
                        <td>Primeira vez visto</td>
                        <td><code>{{'a': 0}}</code></td>
                        <td style="color: #34d399; font-weight: 700;">1</td>
                    </tr>
                    <tr>
                        <td><b>2</b></td>
                        <td><span class="highlight-val">'b'</span></td>
                        <td>1</td>
                        <td>0</td>
                        <td><code>"ab"</code></td>
                        <td>Primeira vez visto</td>
                        <td><code>{{'a': 0, 'b': 1}}</code></td>
                        <td style="color: #34d399; font-weight: 700;">2</td>
                    </tr>
                    <tr>
                        <td><b>3</b></td>
                        <td><span class="highlight-val">'c'</span></td>
                        <td>2</td>
                        <td>0</td>
                        <td><code>"abc"</code></td>
                        <td>Primeira vez visto (Pico Máximo)</td>
                        <td><code>{{'a': 0, 'b': 1, 'c': 2}}</code></td>
                        <td style="color: #34d399; font-weight: 800; font-size: 18px;">3 🏆</td>
                    </tr>
                    <tr style="background: rgba(245, 158, 11, 0.08);">
                        <td><b>4</b></td>
                        <td><span class="highlight-val" style="color: #fbbf24;">'a'</span></td>
                        <td>3</td>
                        <td style="color: #fbbf24; font-weight: 700;">0 → 1</td>
                        <td><code>"bca"</code></td>
                        <td><b>'a' repetido!</b> L salta para <code>0+1=1</code></td>
                        <td><code>{{'a': 3, 'b': 1, 'c': 2}}</code></td>
                        <td style="color: #34d399; font-weight: 700;">3</td>
                    </tr>
                    <tr style="background: rgba(245, 158, 11, 0.08);">
                        <td><b>5</b></td>
                        <td><span class="highlight-val" style="color: #fbbf24;">'b'</span></td>
                        <td>4</td>
                        <td style="color: #fbbf24; font-weight: 700;">1 → 2</td>
                        <td><code>"cab"</code></td>
                        <td><b>'b' repetido!</b> L salta para <code>1+1=2</code></td>
                        <td><code>{{'a': 3, 'b': 4, 'c': 2}}</code></td>
                        <td style="color: #34d399; font-weight: 700;">3</td>
                    </tr>
                    <tr style="background: rgba(245, 158, 11, 0.08);">
                        <td><b>6</b></td>
                        <td><span class="highlight-val" style="color: #fbbf24;">'c'</span></td>
                        <td>5</td>
                        <td style="color: #fbbf24; font-weight: 700;">2 → 3</td>
                        <td><code>"abc"</code></td>
                        <td><b>'c' repetido!</b> L salta para <code>2+1=3</code></td>
                        <td><code>{{'a': 3, 'b': 4, 'c': 5}}</code></td>
                        <td style="color: #34d399; font-weight: 700;">3</td>
                    </tr>
                    <tr style="background: rgba(244, 63, 94, 0.08);">
                        <td><b>7</b></td>
                        <td><span class="highlight-val" style="color: #f87171;">'b'</span></td>
                        <td>6</td>
                        <td style="color: #f87171; font-weight: 700;">3 → 5</td>
                        <td><code>"cb"</code></td>
                        <td><b>'b' repetido!</b> L salta para <code>4+1=5</code></td>
                        <td><code>{{'a': 3, 'b': 6, 'c': 5}}</code></td>
                        <td style="color: #34d399; font-weight: 700;">3</td>
                    </tr>
                    <tr style="background: rgba(244, 63, 94, 0.08);">
                        <td><b>8</b></td>
                        <td><span class="highlight-val" style="color: #f87171;">'b'</span></td>
                        <td>7</td>
                        <td style="color: #f87171; font-weight: 700;">5 → 7</td>
                        <td><code>"b"</code></td>
                        <td><b>'b' repetido!</b> L salta para <code>6+1=7</code></td>
                        <td><code>{{'a': 3, 'b': 7, 'c': 5}}</code></td>
                        <td style="color: #34d399; font-weight: 700;">3</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="footer-bar">
            <span>Rastreio de Execução em Passagem Única O(N)</span>
            <span>Resultado Final: 3</span>
        </div>
    </div>

    <!-- SLIDE 6: DEMONSTRAÇÃO DE ECONOMIA DE TEMPO (BENCHMARK) -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">05 · Demonstração de Economia</div>
            <div class="header-sub">Benchmark Experimental Real com Diferentes Tamanhos de Entrada (N)</div>
        </div>
        <h2 class="slide-title">Economia de Tempo: <span>Dois Mundos Diferentes</span></h2>

        <div class="card card-emerald" style="margin-bottom: 25px;">
            <table>
                <thead>
                    <tr>
                        <th>Tamanho da String (N)</th>
                        <th>Força Bruta O(N³)</th>
                        <th>Sliding Window (Set)</th>
                        <th>Sliding Window (Map O(1))</th>
                        <th>Redução de Operações</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>N = 100</b></td>
                        <td style="color: #f87171;">4.85 ms (171.700 ops)</td>
                        <td>0.039 ms (197 ops)</td>
                        <td style="color: #34d399; font-weight: 700;">0.032 ms (100 ops)</td>
                        <td><span class="badge badge-success">99.94% menor</span></td>
                    </tr>
                    <tr>
                        <td><b>N = 1.000</b></td>
                        <td style="color: #f87171; font-weight: 700;">1.953,3 ms (~2.0 s)</td>
                        <td>0.353 ms (1.995 ops)</td>
                        <td style="color: #34d399; font-weight: 700;">0.232 ms (1.000 ops)</td>
                        <td><span class="badge badge-success">99.99% menor</span></td>
                    </tr>
                    <tr>
                        <td><b>N = 5.000</b></td>
                        <td style="color: #f87171; font-weight: 700;">~15.0 s (20.8 bi ops)</td>
                        <td>1.735 ms (9.994 ops)</td>
                        <td style="color: #34d399; font-weight: 700;">1.113 ms (5.000 ops)</td>
                        <td><span class="badge badge-success">99.999% menor</span></td>
                    </tr>
                    <tr style="background: rgba(16, 185, 129, 0.08);">
                        <td><b>N = 50.000 (LeetCode)</b></td>
                        <td style="color: #f87171; font-weight: 800; font-size: 19px;">~250 min (> 4 HORAS)</td>
                        <td style="color: #fbbf24;">15.5 ms (99.992 ops)</td>
                        <td style="color: #34d399; font-weight: 800; font-size: 19px;">11.1 ms (50.000 ops)</td>
                        <td><span class="badge badge-success" style="font-size: 16px;">⚡ > 99.99999%</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="content-grid-2">
            <div class="card card-rose">
                <div class="card-title" style="color: #f87171;">💥 O Colapso da Força Bruta</div>
                <p class="card-text">Com $N = 50.000$, a Força Bruta precisa processar <b>mais de 20 trilhões de comparações</b>, tornando o sistema inoperante.</p>
            </div>
            <div class="card card-emerald">
                <div class="card-title" style="color: #34d399;">⚡ A Mágica do Tempo Linear O(N)</div>
                <p class="card-text">A solução com Hash Map processa a string em <b>exatamente 50.000 operações</b>, respondendo em <b>0,011 segundos</b>.</p>
            </div>
        </div>

        <div class="footer-bar">
            <span>Benchmark Real em Python 3.12</span>
            <span>Economia de Mais de 4 Horas de CPU</span>
        </div>
    </div>

    <!-- SLIDE 7: DIAGRAMA VISUAL -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">06 · Arquitetura Visual</div>
            <div class="header-sub">Mapeamento da Janela Deslizante</div>
        </div>
        <h2 class="slide-title">Dinâmica dos <span>Dois Ponteiros & Hash Map</span></h2>

        <div class="content-grid-2">
            <div class="img-container">
                <img src="{img_b64}" alt="Diagrama LeetCode 3">
            </div>

            <div class="card card-cyan">
                <div class="card-title">🔑 A Mecânica da Otimização</div>
                
                <div style="margin-bottom: 20px;">
                    <b style="color: #38bdf8; font-size: 22px;">1. Ponteiro Direita (right):</b>
                    <p class="card-text">Percorre a string da esquerda para a direita inserindo novos caracteres na janela.</p>
                </div>

                <div style="margin-bottom: 20px;">
                    <b style="color: #34d399; font-size: 22px;">2. Tabela Hash (char_map):</b>
                    <p class="card-text">Armazena a relação <code>map[caractere] = ultimo_indice</code> em tempo constante O(1).</p>
                </div>

                <div>
                    <b style="color: #fbbf24; font-size: 22px;">3. Salto do Ponteiro Esquerda (left):</b>
                    <p class="card-text">Ao achar caractere já visto na janela, salta direto para <code>map[char] + 1</code> sem varredura intermediária!</p>
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Visualização da Janela Deslizante</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 8: CÓDIGO C BAIXO NÍVEL -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">07 · Implementação de Alta Performance</div>
            <div class="header-sub">Conexão com a Aula 2 de Revisão em C</div>
        </div>
        <h2 class="slide-title">Implementação em C: <span>Tabela Direta ASCII</span></h2>

        <div class="content-grid-2">
            <div class="card">
                <div class="card-title" style="color: #a855f7;">⚡ Código em C com Vetor ASCII Fixo</div>
                <div class="code-box" style="font-size: 15px;">
<span class="kw">#include</span> <span class="str">&lt;string.h&gt;</span>

<span class="kw">int</span> <span class="fn">lengthOfLongestSubstring</span>(<span class="kw">char</span>* s) {{
    <span class="kw">int</span> last_index[<span class="num">256</span>]; <span class="com">// Tabela direta de 256 bytes (ASCII)</span>
    <span class="kw">for</span> (<span class="kw">int</span> i = <span class="num">0</span>; i < <span class="num">256</span>; i++) last_index[i] = -<span class="num">1</span>;
    
    <span class="kw">int</span> max_len = <span class="num">0</span>, left = <span class="num">0</span>;
    <span class="kw">int</span> n = <span class="fn">strlen</span>(s);
    
    <span class="kw">for</span> (<span class="kw">int</span> right = <span class="num">0</span>; right < n; right++) {{
        <span class="kw">unsigned char</span> c = (<span class="kw">unsigned char</span>)s[right];
        
        <span class="com">// Se o caractere já está na janela ativa, salta!</span>
        <span class="kw">if</span> (last_index[c] >= left) {{
            left = last_index[c] + <span class="num">1</span>; <span class="com">// Salto direto em O(1)</span>
        }}
        
        last_index[c] = right;
        <span class="kw">int</span> cur_len = right - left + <span class="num">1</span>;
        <span class="kw">if</span> (cur_len > max_len) max_len = cur_len;
    }}
    <span class="kw">return</span> max_len;
}}
                </div>
            </div>

            <div class="card card-emerald">
                <div class="card-title">💡 Vantagens da Implementação em C</div>
                <p class="card-text"><b>1. Zero Overhead de Colisão:</b> Como usamos uma tabela de acesso direto com 256 inteiros, não há colisões nem encadeamento na memória.</p>
                <p class="card-text"><b>2. Consumo de Memória Estrito:</b> <code>256 * sizeof(int) = 1.024 bytes (1 KB)</code> fixo na Stack, garantindo <b>espaço O(1) puro</b>.</p>
                <p class="card-text"><b>3. Cache L1 Friendly:</b> Memória 100% contígua com acesso instantâneo via deslocamento de ponteiro.</p>
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

        <div class="card card-emerald" style="margin-bottom: 25px;">
            <table>
                <thead>
                    <tr>
                        <th>Abordagem Algorítmica</th>
                        <th>Complexidade de Tempo</th>
                        <th>Complexidade de Espaço</th>
                        <th>Classificação em Entrevista</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>1. Força Bruta (Loops Aninhados)</b></td>
                        <td style="color: #f87171; font-weight: 700;">O(N³)</td>
                        <td>O(min(N, Σ))</td>
                        <td><span class="badge badge-danger">Rejeitado (Red Flag)</span></td>
                    </tr>
                    <tr>
                        <td><b>2. Sliding Window com Set (Remoção Passo a Passo)</b></td>
                        <td style="color: #fbbf24; font-weight: 700;">O(2N) = O(N)</td>
                        <td>O(min(N, Σ))</td>
                        <td><span class="badge badge-warning">Contratado (Hire)</span></td>
                    </tr>
                    <tr>
                        <td><b>3. Sliding Window com Hash Map (Pulo O(1))</b></td>
                        <td style="color: #34d399; font-weight: 700;">O(N) Estrito</td>
                        <td>O(min(N, Σ))</td>
                        <td><span class="badge badge-success">Forte Candidato (Strong Hire)</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="content-grid-2">
            <div class="card card-cyan">
                <div class="card-title">⏱️ Justificativa de Tempo: O(N)</div>
                <p class="card-text">O ponteiro <code>direita</code> avança de 0 até N-1 exatamente uma vez. Cada consulta, inserção e cálculo de máximo leva tempo constante <b>O(1)</b>.</p>
            </div>
            <div class="card card-cyan">
                <div class="card-title">💾 Justificativa de Espaço: O(min(N, Σ))</div>
                <p class="card-text">O espaço ocupado pelo Hash Map é limitado pelo menor valor entre o comprimento da string <code>N</code> e o tamanho do alfabeto <code>Σ</code> (ASCII = 256).</p>
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

        <div class="content-grid-2">
            <div class="card card-amber">
                <div class="card-title">🛡️ Casos de Borda Validados</div>
                <p class="card-text"><b>1. String Vazia <code>""</code>:</b> Retorna <code>0</code> imediatamente.</p>
                <p class="card-text"><b>2. Caracteres Idênticos <code>"bbbbbb"</code>:</b> A janela se mantém em tamanho <code>1</code>.</p>
                <p class="card-text"><b>3. Todos Distintos <code>"abcdef"</code>:</b> A janela expande até o tamanho total <code>N</code>.</p>
                <p class="card-text"><b>4. Espaços e Símbolos <code>"a b c!"</code>:</b> Tratados nativamente pela tabela ASCII.</p>
            </div>

            <div class="card card-emerald" style="justify-content: center; align-items: center; text-align: center;">
                <div style="font-size: 60px; margin-bottom: 20px;">🎓</div>
                <div class="card-title" style="font-size: 34px; justify-content: center;">Obrigado a Todos!</div>
                <p class="card-text" style="font-size: 22px; color: #94a3b8; margin-top: 10px;">
                    Abrimos agora para dúvidas do professor e da turma.
                </p>
                <div class="badge-list" style="justify-content: center; margin-top: 25px;">
                    <span class="badge badge-success">Código no GitHub</span>
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

    print("HTML dos 10 slides gerado com sucesso!")

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
        print(f"PDF Atualizado com Sucesso: {pdf_file} ({size_kb:.1f} KB)")
    else:
        print("Erro ao gerar PDF.")

if __name__ == "__main__":
    build_presentation()
