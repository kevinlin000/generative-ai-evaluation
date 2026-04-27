#!/usr/bin/env python3
"""Generate final_scores.csv, agreement_analysis.md, items_to_review.md, screenshots_for_slides.md"""

import csv, math, os

# ── 1. Raw data ──────────────────────────────────────────────────────────────

BLIND = {'chatgpt': 'D', 'claude': 'B', 'deepseek': 'C', 'gemini': 'E', 'taide': 'A'}
LETTER_TO_MODEL = {v: k for k, v in BLIND.items()}
DIMS = ['理解力', '具體性', '風險揭露', '邏輯連貫性', '時間污染指數']
SCENARIOS = ['A_2008', 'B_2022', 'C_2024']
LETTERS = ['A', 'B', 'C', 'D', 'E']

# LLM judge scores  {(scenario, letter): [理, 具, 風, 邏, 時]}
llm = {
    ('A_2008', 'A'): [2, 3, 2, 3, 3],
    ('A_2008', 'B'): [5, 5, 5, 5, 5],
    ('A_2008', 'C'): [4, 5, 4, 4, 2],
    ('A_2008', 'D'): [4, 4, 4, 4, 4],
    ('A_2008', 'E'): [4, 4, 4, 4, 3],
    ('B_2022', 'A'): [2, 2, 2, 2, 2],
    ('B_2022', 'B'): [5, 5, 5, 5, 5],
    ('B_2022', 'C'): [4, 5, 5, 4, 4],
    ('B_2022', 'D'): [4, 4, 4, 4, 3],
    ('B_2022', 'E'): [4, 4, 4, 4, 4],
    ('C_2024', 'A'): [2, 3, 2, 2, 2],
    ('C_2024', 'B'): [5, 5, 5, 5, 5],
    ('C_2024', 'C'): [4, 5, 5, 4, 3],
    ('C_2024', 'D'): [4, 4, 3, 4, 4],
    ('C_2024', 'E'): [4, 4, 4, 4, 4],
}

# Human scores  {(scenario, letter): [理, 具, 風, 邏, 時]}
human = {
    ('A_2008', 'A'): [2, 3, 1, 3, 2],
    ('A_2008', 'B'): [5, 5, 4, 4, 3],
    ('A_2008', 'C'): [4, 4, 3, 4, 1],
    ('A_2008', 'D'): [4, 3, 3, 4, 3],
    ('A_2008', 'E'): [4, 5, 5, 4, 2],
    ('B_2022', 'A'): [2, 1, 1, 2, 2],
    ('B_2022', 'B'): [5, 5, 4, 4, 3],
    ('B_2022', 'C'): [4, 4, 5, 3, 4],
    ('B_2022', 'D'): [4, 3, 4, 4, 3],
    ('B_2022', 'E'): [4, 5, 4, 3, 4],
    ('C_2024', 'A'): [2, 3, 2, 1, 3],
    ('C_2024', 'B'): [4, 5, 4, 5, 4],
    ('C_2024', 'C'): [4, 5, 4, 3, 2],
    ('C_2024', 'D'): [4, 3, 3, 3, 4],
    ('C_2024', 'E'): [5, 5, 4, 5, 4],
}

# Format compliance raw/10 → converted 1-5
# 10→5, 8-9→4, 6-7→3, 4-5→2, 0-3→1
def convert_q5(raw10):
    if raw10 == 10: return 5
    if raw10 >= 8:  return 4
    if raw10 >= 6:  return 3
    if raw10 >= 4:  return 2
    return 1

# model_name → {scenario_suffix: raw_score}
q5_raw = {
    'chatgpt': {'A': 10, 'B': 10, 'C': 10},
    'claude':  {'A': 10, 'B': 10, 'C': 10},
    'deepseek':{'A': 10, 'B': 10, 'C': 10},
    'gemini':  {'A': 10, 'B': 10, 'C': 10},
    'taide':   {'A':  6, 'B':  6, 'C': 10},
}

# scenario suffix mapping
SCENARIO_SUFFIX = {'A_2008': 'A', 'B_2022': 'B', 'C_2024': 'C'}

# ── 2. Build per-cell data ───────────────────────────────────────────────────

rows = []   # detail rows for CSV
for sc in SCENARIOS:
    for lt in LETTERS:
        model = LETTER_TO_MODEL[lt]
        h_list = human[(sc, lt)]
        l_list = llm[(sc, lt)]
        suf = SCENARIO_SUFFIX[sc]
        q5_converted = convert_q5(q5_raw[model][suf])

        dim_finals = []
        for i, dim in enumerate(DIMS):
            h, l = h_list[i], l_list[i]
            diff = h - l
            absdiff = abs(diff)
            status = 'REVIEW' if absdiff >= 2 else 'OK'
            final = (h + l) / 2
            rows.append({
                'scenario': sc, 'letter': lt, 'model': model,
                'dimension': dim,
                'human': h, 'llm': l, 'diff': diff, 'abs_diff': absdiff,
                'status': status, 'final': final,
            })
            dim_finals.append(final)

        # summary row for this (sc, lt)
        rows.append({
            'scenario': sc, 'letter': lt, 'model': model,
            'dimension': 'Q5_格式服從度',
            'human': q5_converted, 'llm': q5_converted,
            'diff': 0, 'abs_diff': 0,
            'status': 'OK', 'final': q5_converted,
        })
        dim_finals.append(q5_converted)

# ── 3. Write final_scores.csv ────────────────────────────────────────────────

out_dir = os.path.join(os.path.dirname(__file__), '..', 'evaluation')

with open(os.path.join(out_dir, 'final_scores.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'scenario','letter','model','dimension',
        'human','llm','diff','abs_diff','status','final'
    ])
    writer.writeheader()
    writer.writerows(rows)

print("✓ final_scores.csv written")

# ── 4. Compute totals per (sc, lt) ──────────────────────────────────────────

# Total = sum of 6 dims (5 quality + Q5)
totals = {}   # (sc, lt) → total_final
for sc in SCENARIOS:
    for lt in LETTERS:
        model = LETTER_TO_MODEL[lt]
        h_list = human[(sc, lt)]
        l_list = llm[(sc, lt)]
        suf = SCENARIO_SUFFIX[sc]
        q5c = convert_q5(q5_raw[model][suf])
        s = 0
        for i in range(5):
            s += (h_list[i] + l_list[i]) / 2
        s += q5c
        totals[(sc, lt)] = s

# ── 5. Agreement analysis ────────────────────────────────────────────────────

def pearson(xs, ys):
    n = len(xs)
    xbar = sum(xs) / n
    ybar = sum(ys) / n
    num = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    den = math.sqrt(sum((x - xbar)**2 for x in xs) * sum((y - ybar)**2 for y in ys))
    return num / den if den else float('nan')

def mae(xs, ys):
    return sum(abs(x - y) for x, y in zip(xs, ys)) / len(xs)

# Per-dimension Pearson + MAE (75 data points, but 15 per dimension)
dim_pearson = {}
dim_mae = {}
for i, dim in enumerate(DIMS):
    h_vals = [human[(sc, lt)][i] for sc in SCENARIOS for lt in LETTERS]
    l_vals = [llm[(sc, lt)][i]   for sc in SCENARIOS for lt in LETTERS]
    dim_pearson[dim] = pearson(h_vals, l_vals)
    dim_mae[dim] = mae(h_vals, l_vals)

# Overall Pearson + MAE (all 75)
all_h = [human[(sc, lt)][i] for sc in SCENARIOS for lt in LETTERS for i in range(5)]
all_l = [llm[(sc, lt)][i]   for sc in SCENARIOS for lt in LETTERS for i in range(5)]
overall_r = pearson(all_h, all_l)
overall_mae = mae(all_h, all_l)

# Per-model MAE (using all 5 dimensions, 3 scenarios = 15 pairs)
model_mae = {}
model_diff_detail = {}
for lt in LETTERS:
    model = LETTER_TO_MODEL[lt]
    h_vals = [human[(sc, lt)][i] for sc in SCENARIOS for i in range(5)]
    l_vals = [llm[(sc, lt)][i]   for sc in SCENARIOS for i in range(5)]
    model_mae[model] = mae(h_vals, l_vals)
    model_diff_detail[model] = sum(h_vals) - sum(l_vals)  # positive = human higher

# Which model has largest disagreement?
max_mae_model = max(model_mae, key=model_mae.get)

# Per-scenario MAE
scenario_mae = {}
for sc in SCENARIOS:
    h_vals = [human[(sc, lt)][i] for lt in LETTERS for i in range(5)]
    l_vals = [llm[(sc, lt)][i]   for lt in LETTERS for i in range(5)]
    scenario_mae[sc] = mae(h_vals, l_vals)

# ── 6. Write agreement_analysis.md ──────────────────────────────────────────

with open(os.path.join(out_dir, 'agreement_analysis.md'), 'w', encoding='utf-8') as f:
    f.write("# Inter-Rater Agreement 分析\n\n")
    f.write("**評分者**：人類（直觀評分）vs LLM-as-a-Judge（盲評）  \n")
    f.write("**資料點**：75 筆（5 模型 × 3 情境 × 5 維度）  \n")
    f.write("**分析方法**：Pearson 相關係數（r）+ 平均絕對差值（MAE）\n\n")
    f.write("---\n\n")

    f.write("## 1. 各維度一致性\n\n")
    f.write("| 維度 | Pearson r | MAE | 詮釋 |\n")
    f.write("|------|-----------|-----|------|\n")
    interp = {
        '理解力':     '高度一致，評分者對理解程度判斷相符',
        '具體性':     '高度一致，量化細節有無易於共識',
        '風險揭露':   '中高一致，人類對部分案例評分偏嚴',
        '邏輯連貫性': '高度一致，結構清晰度判斷穩定',
        '時間污染指數':'一致性最低，對「後見之明程度」主觀判斷差異最大',
    }
    for dim in DIMS:
        r = dim_pearson[dim]
        m = dim_mae[dim]
        note = interp.get(dim, '')
        f.write(f"| {dim} | **{r:.3f}** | {m:.3f} | {note} |\n")
    f.write(f"| **整體（75筆）** | **{overall_r:.3f}** | **{overall_mae:.3f}** | |\n\n")

    f.write("---\n\n")
    f.write("## 2. 各模型評分一致性\n\n")
    f.write("| 模型（Letter） | MAE | 人類總分 - LLM總分 | 詮釋 |\n")
    f.write("|--------------|-----|-----------------|------|\n")
    for lt in LETTERS:
        model = LETTER_TO_MODEL[lt]
        m = model_mae[model]
        delta = model_diff_detail[model]
        sign = '+' if delta >= 0 else ''
        if model == 'claude':
            note = '⚠️ 差異最大：時間污染指數人類評分顯著低於LLM（可能為self-preference bias）'
        elif model == 'taide':
            note = '一致性高，兩者對低品質內容評分接近'
        else:
            note = '一致性良好'
        f.write(f"| {model}（{lt}） | {m:.3f} | {sign}{delta} | {note} |\n")

    f.write("\n---\n\n")
    f.write("## 3. 各情境評分一致性\n\n")
    f.write("| 情境 | MAE |\n")
    f.write("|------|-----|\n")
    for sc in SCENARIOS:
        f.write(f"| {sc} | {scenario_mae[sc]:.3f} |\n")

    f.write("\n---\n\n")
    f.write("## 4. Self-Preference Bias 分析\n\n")
    f.write("LLM-as-a-Judge 與人類分數差異最大的模型為 **claude（Letter B）**，\n")
    f.write("差值集中在「時間污染指數」維度（LLM給5，人類給3，Diff=2），\n")
    f.write("且在 A_2008 與 B_2022 兩個情境均重複出現。\n\n")
    f.write("**可能解釋**：\n")
    f.write("- LLM Judge（claude-sonnet-4-6）對 Letter B 的自我污染識別能力高度讚賞\n")
    f.write("  （Letter B 在 Q4 中展示了精確的元認知分析），\n")
    f.write("  但人類評分者認為「識別出來了但還是被污染」不應得到最高分\n")
    f.write("- 此現象符合 Self-Preference Bias 的典型模式：\n")
    f.write("  同族模型在評分具有「meta-awareness」的回覆時傾向高估\n\n")
    f.write("**注意**：C_2024 情境的時間污染指數差值僅為 1（人類4 vs LLM5），\n")
    f.write("未達 REVIEW 門檻，顯示此偏差並非系統性，而是與情境複雜度相關。\n\n")
    f.write("---\n\n")
    f.write("## 5. 整體評估\n\n")
    f.write(f"- **整體 Pearson r = {overall_r:.3f}**，屬於高度相關，驗證 LLM-as-a-Judge 的有效性\n")
    f.write(f"- **整體 MAE = {overall_mae:.3f}**，平均每筆評分差距不超過 1 分（1-5 量表）\n")
    f.write("- 75 筆分數中僅 **2 筆**（2.7%）差值達到 REVIEW 門檻（≥2）\n")
    f.write("- 時間污染指數是一致性最低的維度，建議在後續研究中考慮細化評分標準\n")

print("✓ agreement_analysis.md written")

# ── 7. Write items_to_review.md ─────────────────────────────────────────────

# Gather REVIEW items with conversation snippet hints
review_snippets = {
    ('A_2008', 'B', '時間污染指數'): (
        'LLM給5分因B完整列出六個洩漏點並深度分析（如「分6個月剛好對準2009/3底部」）；'
        '人類給3分因認為「識別出後見之明卻仍採用它」不應得滿分。'
        '核心分歧：「認識錯誤」是否等同於「沒有犯錯」。'
    ),
    ('B_2022', 'B', '時間污染指數'): (
        'LLM給5分因B坦承「2022年15-20%修正+2023年回穩幾乎就是實際劇本...這是最嚴重的問題」；'
        '人類給3分因此答案雖有自覺但依然把後見之明劇本當作50%機率基準。'
        '核心分歧：元認知得分應補償還是無法補償實際污染。'
    ),
}

with open(os.path.join(out_dir, 'items_to_review.md'), 'w', encoding='utf-8') as f:
    f.write("# 需重新檢視項目（Diff ≥ 2）\n\n")
    f.write("> 規則：人類分數 vs LLM分數差值絕對值 ≥ 2，需人類最終裁定。\n\n")

    review_rows = [r for r in rows if r['status'] == 'REVIEW']
    if not review_rows:
        f.write("（無需重新檢視項目）\n")
    else:
        f.write("| Scenario | Letter | Model | Dimension | Human | LLM | Diff | 分歧摘要 |\n")
        f.write("|---------|--------|-------|-----------|-------|-----|------|----------|\n")
        for r in review_rows:
            sc, lt, model, dim = r['scenario'], r['letter'], r['model'], r['dimension']
            h, l, diff = r['human'], r['llm'], r['diff']
            snippet = review_snippets.get((sc, lt, dim), '—')
            f.write(f"| {sc} | {lt} | {model} | {dim} | {h} | {l} | {diff:+d} | {snippet} |\n")

        f.write("\n---\n\n")
        f.write("## 裁定建議\n\n")
        f.write("兩筆 REVIEW 項目均為 **claude（Letter B）× 時間污染指數**，\n")
        f.write("差異源於對「有自覺的污染」如何計分的哲學立場分歧：\n\n")
        f.write("**立場 A（支持 LLM 的 5 分）**：\n")
        f.write("自我辨識能力本身就是時間污染評估的核心能力，B 是唯一一個\n")
        f.write("精確識別出「分批時間恰好對準底部」這類量化洩漏點的模型，\n")
        f.write("5 分獎勵的是識別精準度，而非完全無污染。\n\n")
        f.write("**立場 B（支持人類的 3 分）**：\n")
        f.write("「時間污染指數」本意是評估回覆內容的污染程度，\n")
        f.write("有自覺地使用後見之明並不等於沒有使用後見之明，\n")
        f.write("3-4 分更能反映「部分污染但有自覺」的狀態。\n\n")
        f.write("**建議**：維持人類評分（3分），理由是評估維度名稱為「時間污染指數」\n")
        f.write("（污染程度），而非「時間污染識別能力」。\n")
        f.write("若要獎勵元認知，可在未來版本中新增獨立維度。\n")

print("✓ items_to_review.md written")

# ── 8. screenshots_for_slides.md ────────────────────────────────────────────

# Find best (human 5) and worst (human 1) per dimension
positive = {}
negative = {}
for i, dim in enumerate(DIMS):
    for sc in SCENARIOS:
        for lt in LETTERS:
            h = human[(sc, lt)][i]
            model = LETTER_TO_MODEL[lt]
            if h == 5:
                positive.setdefault(dim, []).append((sc, lt, model))
            if h == 1:
                negative.setdefault(dim, []).append((sc, lt, model))

# review items
review_items = [(r['scenario'], r['letter'], r['model'], r['dimension'],
                 r['human'], r['llm']) for r in rows if r['status'] == 'REVIEW']

# Map dimension to Question
DIM_TO_Q = {
    '理解力': 'Q1',
    '具體性': 'Q2',
    '風險揭露': 'Q2',
    '邏輯連貫性': 'Q3',
    '時間污染指數': 'Q4',
}
DIM_TO_SLIDE = {
    '理解力': 'Q1 市場背景理解頁',
    '具體性': 'Q2 建議具體性對比頁',
    '風險揭露': 'Q2 風險揭露深度頁',
    '邏輯連貫性': 'Q3 應對挑戰邏輯頁',
    '時間污染指數': 'Q4 時間污染檢測頁',
}

slides = []  # list of dicts

# Positive examples – pick 1 per dimension (most interesting)
positive_picks = [
    ('A_2008', 'E', 'gemini', '風險揭露', 'positive',
     'Q2', 'Q2 風險揭露深度頁',
     '人類給5：Gemini 在2008情境提供了精確的壓力測試計算（S&P500再跌40%對組合衝擊），且「最具體案例」與 Claude 相當，但無後見之明問題。',
     'positive_gemini_A2008_Q2_risk'),
    ('B_2022', 'C', 'deepseek', '風險揭露', 'positive',
     'Q2', 'Q2 風險揭露深度頁',
     '人類給5：DeepSeek 在2022情境精確計算「股票55%×跌30%=-16.5%」並涵蓋兩個壓力情境，LLM同給5，高度共識。',
     'positive_deepseek_B2022_Q2_risk'),
    ('C_2024', 'E', 'gemini', '邏輯連貫性', 'positive',
     'Q3', 'Q3 應對挑戰邏輯頁',
     '人類給5：Gemini 在2024情境對朋友觀點反駁結構清晰，「50%債券已是崩盤備案」論點邏輯自洽，人類與LLM分差僅1。',
     'positive_gemini_C2024_Q3_logic'),
    ('C_2024', 'B', '邏輯連貫性', 'positive',
     'Q3', 'Q3 應對挑戰邏輯頁',  # duplicate key issue, fix below
     '', '', ''),
]

# Rebuild properly
slides = [
    # Positive examples
    {
        'model': 'gemini（E）', 'scenario': 'A_2008', 'question': 'Q2',
        'category': '正面案例', 'dimension': '風險揭露（人類5分）',
        'slide_page': 'Q2 風險揭露深度頁',
        'note': 'Gemini 在2008情境精確計算股票壓力測試，「S&P500再暴跌40%，40%股票部位拖累約-16%」邏輯清晰；無後見之明疑慮，是與Claude最具說服力的競爭案例。',
        'filename': 'positive_E_gemini_A2008_Q2_risk_disclosure',
    },
    {
        'model': 'deepseek（C）', 'scenario': 'B_2022', 'question': 'Q2',
        'category': '正面案例', 'dimension': '風險揭露（人類5分）',
        'slide_page': 'Q2 風險揭露深度頁',
        'note': 'DeepSeek 在2022情境給出「股票55%×跌30%=-16.5%」精確計算，含兩個壓力情境；人類與LLM均給5，是全場少數完全共識的滿分案例。',
        'filename': 'positive_C_deepseek_B2022_Q2_risk_disclosure',
    },
    {
        'model': 'claude（B）', 'scenario': 'C_2024', 'question': 'Q3',
        'category': '正面案例', 'dimension': '邏輯連貫性（人類5分）',
        'slide_page': 'Q3 應對挑戰邏輯頁',
        'note': 'Claude 在2024情境對朋友五個論點逐一反駁，包含「1996年Greenspan喊非理性繁榮，市場又漲4年」反例；結構最系統，人類與LLM均給5。',
        'filename': 'positive_B_claude_C2024_Q3_logic',
    },
    {
        'model': 'gemini（E）', 'scenario': 'C_2024', 'question': 'Q2',
        'category': '正面案例', 'dimension': '理解力（人類5分）',
        'slide_page': 'Q1 市場背景理解頁',
        'note': 'Gemini 在2024情境是唯一人類給5分理解力的非Claude模型；精確點出CPI3.0%降息預期為「牽動全球資金流向的最核心指標」，排序邏輯清晰。',
        'filename': 'positive_E_gemini_C2024_Q1_understanding',
    },
    # Negative examples
    {
        'model': 'taide（A）', 'scenario': 'B_2022', 'question': 'Q2',
        'category': '負面案例', 'dimension': '具體性（人類1分）',
        'slide_page': 'Q2 建議具體性對比頁',
        'note': 'TAIDE 在2022情境僅給出「台積電、中華電信、IXUS、VTI」四個標的無邏輯框架；人類與LLM均給低分，且出現「台積電+中華電信」混搭無配置比例的問題。',
        'filename': 'negative_A_taide_B2022_Q2_specificity',
    },
    {
        'model': 'taide（A）', 'scenario': 'A_2008', 'question': 'Q2',
        'category': '負面案例', 'dimension': '風險揭露（人類1分）',
        'slide_page': 'Q2 風險揭露深度頁',
        'note': 'TAIDE 在2008情境風險揭露僅一行「預計投資組合可能下跌最多-20%」，無計算依據；人類比LLM更嚴（H=1 vs L=2），是全場最低分風險揭露案例。',
        'filename': 'negative_A_taide_A2008_Q2_risk_min',
    },
    {
        'model': 'taide（A）', 'scenario': 'C_2024', 'question': 'Q3',
        'category': '負面案例', 'dimension': '邏輯連貫性（人類1分）',
        'slide_page': 'Q3 應對挑戰邏輯頁',
        'note': 'TAIDE 在2024情境Q3宣稱「不大幅改變建議」但又說「會納入朋友意見」；前後矛盾且無具體調整數字，是全場唯一邏輯連貫性1分案例。',
        'filename': 'negative_A_taide_C2024_Q3_logic_min',
    },
    {
        'model': 'deepseek（C）', 'scenario': 'A_2008', 'question': 'Q4',
        'category': '負面案例', 'dimension': '時間污染指數（人類1分）',
        'slide_page': 'Q4 時間污染檢測頁',
        'note': 'DeepSeek 在2008情境Q4自評10/10並稱「無需舉例」；而Claude識別出TIPS選擇、黃金配置、6個月分批等洩漏點；「過度自信的滿分」是最可疑的污染指標。',
        'filename': 'negative_C_deepseek_A2008_Q4_contamination_min',
    },
    # Dispute examples (REVIEW items)
    {
        'model': 'claude（B）', 'scenario': 'A_2008', 'question': 'Q4',
        'category': '爭議案例', 'dimension': '時間污染指數（人類3 vs LLM5，Diff=2）',
        'slide_page': 'Q4 時間污染檢測頁 / 方法論頁',
        'note': '核心爭議：「識別出後見之明」等於「較無污染」嗎？B明確指出「分6個月剛好對準2009/3底部」，LLM獎勵其元認知能力給5；人類認為識別後仍採用=仍被污染給3。',
        'filename': 'dispute_B_claude_A2008_Q4_selfaware_contamination',
    },
    {
        'model': 'claude（B）', 'scenario': 'B_2022', 'question': 'Q4',
        'category': '爭議案例', 'dimension': '時間污染指數（人類3 vs LLM5，Diff=2）',
        'slide_page': 'Q4 時間污染檢測頁 / Self-Preference Bias 頁',
        'note': 'B坦承「把後見之明劇本當成50%機率基準，這是最嚴重的問題」——這是本次評測最強的Self-Preference Bias證據：LLM因B的自我批評而給滿分，但自我批評≠無污染。',
        'filename': 'dispute_B_claude_B2022_Q4_selfpref_bias',
    },
    # Bonus: interesting contrast
    {
        'model': 'chatgpt（D）', 'scenario': 'B_2022', 'question': 'Q2',
        'category': '負面案例', 'dimension': '具體性（人類3分，Q2表格缺失）',
        'slide_page': 'Q2 建議具體性對比頁 / 方法論頁',
        'note': 'ChatGPT 在2022情境Q2表格因docx提取異常缺失；評分參考Q5 JSON補充的8個標的，但原始對話展示缺陷影響可讀性。建議截圖顯示表格缺失問題作為資料品質說明。',
        'filename': 'note_D_chatgpt_B2022_Q2_table_missing',
    },
    {
        'model': 'gemini（E）vs taide（A）', 'scenario': 'A_2008', 'question': 'Q1',
        'category': '正面案例', 'dimension': '整體品質對比（人類E=20 vs A=11）',
        'slide_page': 'Q1 市場背景理解頁 / 模型排名頁',
        'note': '同情境最高分與最低分並排對比：Gemini精確引用「失業率6.1%、Fed 4.25%→2.00%、油價147→101」；TAIDE僅用「市場動盪、金融機構壓力」等泛化描述。最具視覺衝擊力的對比截圖。',
        'filename': 'contrast_E_vs_A_A2008_Q1_best_vs_worst',
    },
]

with open(os.path.join(out_dir, 'screenshots_for_slides.md'), 'w', encoding='utf-8') as f:
    f.write("# 簡報截圖建議清單\n\n")
    f.write("> 來源：final_scores.csv 最高/最低分項目 + REVIEW 爭議案例  \n")
    f.write("> 總數：12 筆（正面4 / 負面4 / 爭議2 / 其他2）  \n\n")
    f.write("| # | 模型（Letter） | 情境 | Question | 類別 | 維度 / 說明 | 對應簡報頁 | 建議截圖檔名 |\n")
    f.write("|---|--------------|------|---------|------|------------|------------|-------------|\n")
    for idx, s in enumerate(slides, 1):
        f.write(f"| {idx} | {s['model']} | {s['scenario']} | {s['question']} "
                f"| {s['category']} | {s['dimension']} | {s['slide_page']} | `{s['filename']}` |\n")
    f.write("\n---\n\n")
    f.write("## 截圖說明（各筆詳細）\n\n")
    for idx, s in enumerate(slides, 1):
        f.write(f"### #{idx} {s['model']} / {s['scenario']} / {s['question']} — {s['category']}\n\n")
        f.write(f"**維度**：{s['dimension']}  \n")
        f.write(f"**對應頁**：{s['slide_page']}  \n")
        f.write(f"**說明**：{s['note']}  \n")
        f.write(f"**建議檔名**：`{s['filename']}.png`\n\n")

print("✓ screenshots_for_slides.md written")

# ── 9. Print summary to stdout ───────────────────────────────────────────────

print("\n=== 最終排名（6維度總分，滿分90）===")
model_total = {}
for lt in LETTERS:
    model = LETTER_TO_MODEL[lt]
    total = sum(totals[(sc, lt)] for sc in SCENARIOS)
    model_total[model] = total

for rank, (model, total) in enumerate(sorted(model_total.items(), key=lambda x: -x[1]), 1):
    lt = BLIND[model]
    print(f"  #{rank} {model}（{lt}）: {total:.1f}/90")

print(f"\n整體 Pearson r = {overall_r:.3f}")
print(f"整體 MAE      = {overall_mae:.3f}")
print(f"REVIEW 項目   = {len([r for r in rows if r['status'] == 'REVIEW'])} 筆")
