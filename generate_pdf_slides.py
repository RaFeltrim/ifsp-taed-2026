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
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

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
            background: radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.08), transparent 40%),
                        radial-gradient(circle at 20% 80%, rgba(6, 182, 212, 0.08), transparent 40%),
                        #080b12;
            display: flex;
            flex-direction: column;
            padding: 80px 100px;
        }}

        .header-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 20px;
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
            font-size: 16px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .header-sub {{
            color: #94a3b8;
            font-size: 18px;
            font-weight: 600;
        }}

        .slide-title {{
            font-size: 50px;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.15;
            margin-bottom: 30px;
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
            gap: 40px;
            flex: 1;
            align-items: stretch;
        }}

        .content-grid-3 {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            flex: 1;
        }}

        .card {{
            background: rgba(17, 24, 39, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 35px;
            display: flex;
            flex-direction: column;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
        }}

        .card-emerald {{
            border-color: rgba(16, 185, 129, 0.3);
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.05), rgba(17, 24, 39, 0.8));
        }}

        .card-cyan {{
            border-color: rgba(6, 182, 212, 0.3);
            background: linear-gradient(135deg, rgba(6, 182, 212, 0.05), rgba(17, 24, 39, 0.8));
        }}

        .card-amber {{
            border-color: rgba(245, 158, 11, 0.3);
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.05), rgba(17, 24, 39, 0.8));
        }}

        .card-title {{
            font-size: 26px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .card-text {{
            font-size: 20px;
            line-height: 1.6;
            color: #cbd5e1;
            margin-bottom: 15px;
        }}

        .badge-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 15px;
        }}

        .badge {{
            padding: 8px 18px;
            border-radius: 12px;
            font-size: 17px;
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
            border-radius: 18px;
            padding: 25px;
            font-size: 19px;
            line-height: 1.5;
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
            margin-top: 15px;
        }}

        th, td {{
            padding: 16px 20px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            font-size: 20px;
        }}

        th {{
            background: rgba(255, 255, 255, 0.03);
            color: #94a3b8;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 16px;
            letter-spacing: 1px;
        }}

        td {{
            color: #f1f5f9;
        }}

        .footer-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 30px;
            padding-top: 15px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            color: #64748b;
            font-size: 16px;
            font-weight: 600;
        }}

        /* Slide 1 - Cover */
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
            margin-bottom: 30px;
            box-shadow: 0 0 40px rgba(16, 185, 129, 0.4);
        }}

        .cover-title {{
            font-size: 64px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 20px;
            line-height: 1.15;
        }}

        .cover-subtitle {{
            font-size: 28px;
            color: #94a3b8;
            max-width: 1000px;
            line-height: 1.5;
            margin-bottom: 50px;
        }}

        .team-box {{
            display: flex;
            gap: 25px;
            background: rgba(17, 24, 39, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 20px 40px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
        }}

        .team-member {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        }}

        .team-name {{
            font-size: 22px;
            font-weight: 700;
            color: #f1f5f9;
        }}

        .team-role {{
            font-size: 16px;
            color: #34d399;
            font-weight: 600;
        }}

        .img-container {{
            width: 100%;
            height: 100%;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            background: #020617;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        }}

        .img-container img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}
    </style>
</head>
<body>

    <!-- SLIDE 1: CAPA -->
    <div class="slide cover-slide">
        <div class="cover-logo">⚡</div>
        <div class="header-tag" style="margin-bottom: 20px;">IFSP São Carlos · Engenharia de Software</div>
        <h1 class="cover-title">Longest Substring Without Repeating Characters</h1>
        <p class="cover-subtitle">Desafio Real de Processo Seletivo em Big Techs (LeetCode #3) — Otimização Assintótica via Janela Deslizante (Sliding Window)</p>
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
        <div class="footer-bar" style="width: 100%; justify-content: center; margin-top: 50px;">
            Prof. Dr. Rodrigo Elias Bianchi · Tópicos em Algoritmos e Estruturas de Dados · 2026
        </div>
    </div>

    <!-- SLIDE 2: CONTEXTO DE MERCADO -->
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
                <p class="card-text" style="font-size: 24px; font-weight: 600; color: #ffffff; margin-bottom: 25px;">
                    "Dada uma string <code>s</code>, encontre o comprimento da <u>maior substring contígua</u> que não contenha caracteres repetidos."
                </p>
                <div class="card" style="background: rgba(0,0,0,0.4); padding: 20px; border-radius: 16px;">
                    <div style="color: #fbbf24; font-weight: 700; font-size: 20px; margin-bottom: 10px;">⚠️ Distinção Crítica de Conceito:</div>
                    <p class="card-text" style="font-size: 18px; margin: 0;">
                        <b>Substring:</b> Sequência contínua de caracteres (ex: <code>"abc"</code> em <code>"abcde"</code>).<br>
                        <b>Subsequência:</b> Mantém a ordem mas não é contínua (ex: <code>"ace"</code> em <code>"abcde"</code>).
                    </p>
                </div>
            </div>

            <div class="card card-cyan">
                <div class="card-title">🧪 Exemplos de Teste</div>
                
                <div style="margin-bottom: 20px; background: rgba(0,0,0,0.3); padding: 15px 20px; border-radius: 14px;">
                    <div style="color: #38bdf8; font-weight: 700;">Exemplo 1:</div>
                    <code style="font-size: 22px;">s = "abcabcbb"</code> → <b>Resposta: 3</b> (substring: <code>"abc"</code>)
                </div>

                <div style="margin-bottom: 20px; background: rgba(0,0,0,0.3); padding: 15px 20px; border-radius: 14px;">
                    <div style="color: #38bdf8; font-weight: 700;">Exemplo 2:</div>
                    <code style="font-size: 22px;">s = "bbbbb"</code> → <b>Resposta: 1</b> (substring: <code>"b"</code>)
                </div>

                <div style="background: rgba(0,0,0,0.3); padding: 15px 20px; border-radius: 14px;">
                    <div style="color: #38bdf8; font-weight: 700;">Exemplo 3:</div>
                    <code style="font-size: 22px;">s = "pwwkew"</code> → <b>Resposta: 3</b> (substring: <code>"wke"</code>)
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Tarefa Prática do Dia · Slide 13</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 4: FORÇA BRUTA VS SLIDING WINDOW -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">03 · Comparação de Abordagens</div>
            <div class="header-sub">O Abismo de Desempenho</div>
        </div>
        <h2 class="slide-title">A Armadilha da <span>Força Bruta O(N³)</span></h2>

        <div class="content-grid-2">
            <div class="card" style="border-color: rgba(239, 68, 68, 0.4); background: rgba(239, 68, 68, 0.05);">
                <div class="card-title" style="color: #f87171;">❌ Abordagem 1: Força Bruta</div>
                <p class="card-text">1. Gera todos os pares de início e fim <code>(i, j)</code> possíveis: <b>O(N²) substrings</b>.</p>
                <p class="card-text">2. Para cada substring, executa um loop interno para verificar se há duplicatas: <b>O(N)</b>.</p>
                <div class="badge-list" style="margin-top: 25px;">
                    <span class="badge badge-danger">Tempo: O(N³)</span>
                    <span class="badge badge-danger">Espaço: O(min(N, Σ))</span>
                </div>
                <div style="margin-top: 30px; background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.3); padding: 20px; border-radius: 16px; color: #fca5a5; font-size: 19px;">
                    💀 <b>Resultado sob carga:</b> Para uma string de 50.000 caracteres, exige ~125 trilhões de operações → <b>Time Limit Exceeded (TLE)</b>.
                </div>
            </div>

            <div class="card card-emerald">
                <div class="card-title" style="color: #34d399;">🟢 Abordagem 2: Janela Deslizante (Sliding Window)</div>
                <p class="card-text">1. Mantém uma janela dinâmica delimitada por dois ponteiros: <code>[left, right]</code>.</p>
                <p class="card-text">2. O ponteiro <code>right</code> expande a janela caractere por caractere.</p>
                <p class="card-text">3. Ao detectar duplicata, contrai a janela pela esquerda com um salto instantâneo!</p>
                <div class="badge-list" style="margin-top: 25px;">
                    <span class="badge badge-success">Tempo: O(N) Linear</span>
                    <span class="badge badge-success">Espaço: O(min(N, Σ))</span>
                </div>
                <div style="margin-top: 30px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); padding: 20px; border-radius: 16px; color: #86efac; font-size: 19px;">
                    🚀 <b>Resultado:</b> Executa em passagem única em menos de <b>5 milissegundos</b>!
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Tarefa Prática do Dia · Slide 13</span>
            <span>Trade-offs & Análise Assintótica</span>
        </div>
    </div>

    <!-- SLIDE 5: DIAGRAMA VISUAL -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">04 · Arquitetura Visual</div>
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

    <!-- SLIDE 6: CÓDIGO FONTE -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">05 · Implementação</div>
            <div class="header-sub">Solução Limpa em Python & C Baixo Nível</div>
        </div>
        <h2 class="slide-title">Implementação <span>Otimizada em O(N)</span></h2>

        <div class="content-grid-2">
            <div class="card">
                <div class="card-title" style="color: #38bdf8;">🐍 Python (Legibilidade e Expressividade)</div>
                <div class="code-box">
<span class="kw">def</span> <span class="fn">lengthOfLongestSubstring</span>(s: <span class="kw">str</span>) -> <span class="kw">int</span>:
    char_map = {{}}  <span class="com"># char -> último índice</span>
    esquerda = <span class="num">0</span>
    maior = <span class="num">0</span>
    
    <span class="kw">for</span> direita, char <span class="kw">in</span> <span class="fn">enumerate</span>(s):
        <span class="com"># Se o caractere já está na janela ativa:</span>
        <span class="kw">if</span> char <span class="kw">in</span> char_map <span class="kw">and</span> char_map[char] >= esquerda:
            esquerda = char_map[char] + <span class="num">1</span>  <span class="com"># Pulo O(1)</span>
            
        char_map[char] = direita
        maior = <span class="fn">max</span>(maior, direita - esquerda + <span class="num">1</span>)
        
    <span class="kw">return</span> maior
                </div>
            </div>

            <div class="card">
                <div class="card-title" style="color: #a855f7;">⚡ C Baixo Nível (Array Direto ASCII)</div>
                <div class="code-box">
<span class="kw">int</span> <span class="fn">lengthOfLongestSubstring</span>(<span class="kw">char</span>* s) {{
    <span class="kw">int</span> last_index[<span class="num">256</span>]; <span class="com">// Tabela direta O(1)</span>
    <span class="kw">for</span> (<span class="kw">int</span> i = <span class="num">0</span>; i < <span class="num">256</span>; i++) last_index[i] = -<span class="num">1</span>;
    
    <span class="kw">int</span> max_len = <span class="num">0</span>, left = <span class="num">0</span>, n = <span class="fn">strlen</span>(s);
    <span class="kw">for</span> (<span class="kw">int</span> right = <span class="num">0</span>; right < n; right++) {{
        <span class="kw">unsigned char</span> c = (<span class="kw">unsigned char</span>)s[right];
        <span class="kw">if</span> (last_index[c] >= left) {{
            left = last_index[c] + <span class="num">1</span>; <span class="com">// Salto em O(1)</span>
        }}
        last_index[c] = right;
        <span class="kw">int</span> cur = right - left + <span class="num">1</span>;
        <span class="kw">if</span> (cur > max_len) max_len = cur;
    }}
    <span class="kw">return</span> max_len;
}}
                </div>
            </div>
        </div>

        <div class="footer-bar">
            <span>Código de Produção · LeetCode #3</span>
            <span>IFSP São Carlos</span>
        </div>
    </div>

    <!-- SLIDE 7: TABELA BIG-O -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">06 · Análise Assintótica</div>
            <div class="header-sub">Rigor Teórico e Comparativo</div>
        </div>
        <h2 class="slide-title">Análise Rigorosa de <span>Complexidade (Big-O)</span></h2>

        <div class="card card-emerald" style="margin-bottom: 30px;">
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
                        <td><span class="badge badge-company">Contratado (Hire)</span></td>
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

    <!-- SLIDE 8: CASOS DE BORDA & CONCLUSÃO -->
    <div class="slide">
        <div class="header-bar">
            <div class="header-tag">07 · Fechamento & Perguntas</div>
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
                <p class="card-text" style="font-size: 24px; color: #94a3b8; margin-top: 10px;">
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

    print("HTML dos slides gerado com sucesso!")

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
        print(f"PDF Gerado com Sucesso: {pdf_file} ({size_kb:.1f} KB)")
    else:
        print("Erro ao gerar PDF.")

if __name__ == "__main__":
    build_presentation()
