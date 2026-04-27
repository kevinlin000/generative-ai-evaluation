#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build conversations/ and evaluation/ from docx source files.
Usage: python scripts/build_evaluation.py
"""
import json
import os
import re
import random
from pathlib import Path
from docx import Document

BASE = Path(__file__).parent.parent
SCREENSHOTS = BASE / "screenshots"
CONVERSATIONS = BASE / "conversations"
EVALUATION = BASE / "evaluation"

DOCX_FILES = {
    "chatgpt": SCREENSHOTS / "chatgpt回答情況.docx",
    "claude": SCREENSHOTS / "Claude回答情況.docx",
    "deepseek": SCREENSHOTS / "deepseekR1回答情況.docx",
    "gemini": SCREENSHOTS / "Gemini回答情況.docx",
    "taide": SCREENSHOTS / "TAIDE回答情況.docx",
}

SCENARIO_LABELS = {"A": "A_2008", "B": "B_2022", "C": "C_2024"}

# step number → question label
STEP_TO_Q = {
    2: "Q1",
    3: "Q2",
    4: "Q3",
    5: "Q4",
    6: "Q5a",
    7: "Q5b",
}

Q_TITLES = {
    "Q1": "Question 1: 理解力檢查",
    "Q2": "Question 2: 建議生成",
    "Q3": "Question 3: 逆向質疑",
    "Q4": "Question 4: 時間污染檢測",
    "Q5a": "Question 5a: JSON 結構化輸出（寬鬆約束）",
    "Q5b": "Question 5b: JSON 結構化輸出（嚴格約束）",
}

SCENARIO_DATES = {"A": "2008-09-12", "B": "2022-01-04", "C": "2024-07-11"}


def extract_paragraphs(doc_path):
    doc = Document(doc_path)
    return [p.text for p in doc.paragraphs]


def find_step_boundaries(paragraphs):
    """Return {(scenario, step_num): (start_para_idx, end_para_idx)}"""
    step_re = re.compile(r"步驟\s*(\d+)[：:]")
    scenario_re = re.compile(r"^情境([ABC])$")

    boundaries = {}
    current_scenario = None
    prev_key = None
    prev_start = None

    for i, text in enumerate(paragraphs):
        t = text.strip()
        sc_m = scenario_re.match(t)
        if sc_m:
            # close previous step if any
            if prev_key is not None:
                boundaries[prev_key] = (prev_start, i)
            current_scenario = sc_m.group(1)
            prev_key = None
            prev_start = None
            continue

        st_m = step_re.match(t)
        if st_m and current_scenario:
            step_num = int(st_m.group(1))
            # close previous step
            if prev_key is not None:
                boundaries[prev_key] = (prev_start, i)
            key = (current_scenario, step_num)
            prev_key = key
            prev_start = i + 1  # content starts after header line
            continue

    # close last step
    if prev_key is not None:
        boundaries[prev_key] = (prev_start, len(paragraphs))

    return boundaries


def paragraphs_to_md(paragraphs, start, end):
    lines = []
    for p in paragraphs[start:end]:
        stripped = p.strip()
        lines.append(stripped)
    # remove trailing blank lines
    while lines and not lines[-1]:
        lines.pop()
    return "\n\n".join(lines) if lines else ""


def build_conversations():
    CONVERSATIONS.mkdir(exist_ok=True)
    results = {}  # (model, scenario, q) → md content

    for model, docx_path in DOCX_FILES.items():
        print(f"Processing {docx_path.name}...")
        paragraphs = extract_paragraphs(docx_path)
        boundaries = find_step_boundaries(paragraphs)

        for (scenario, step_num), (start, end) in boundaries.items():
            if step_num not in STEP_TO_Q:
                continue
            q_label = STEP_TO_Q[step_num]
            content = paragraphs_to_md(paragraphs, start, end)
            results[(model, scenario, q_label)] = content

    # Write files
    written = []
    for (model, scenario, q_label), content in sorted(results.items()):
        fname = f"{model}_{scenario}_{q_label}.md"
        out_path = CONVERSATIONS / fname
        out_path.write_text(content, encoding="utf-8")
        written.append(fname)

    return results, written


def build_blind_mapping():
    models = list(DOCX_FILES.keys())
    letters = ["A", "B", "C", "D", "E"]
    shuffled = letters[:]
    random.shuffle(shuffled)
    mapping = {model: letter for model, letter in zip(models, shuffled)}
    return mapping


def build_evaluation(conversations, blind_mapping):
    EVALUATION.mkdir(exist_ok=True)

    # Save blind mapping
    mapping_path = EVALUATION / "_blind_mapping.json"
    mapping_path.write_text(
        json.dumps(blind_mapping, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Blind mapping: {blind_mapping}")

    # Build one file per scenario per letter
    written = []
    for scenario in ["A", "B", "C"]:
        scenario_label = SCENARIO_LABELS[scenario]
        for model, letter in blind_mapping.items():
            lines = [f"Scenario: {scenario_label} / Model: [{letter}]", ""]
            for step_num in sorted(STEP_TO_Q):
                q_label = STEP_TO_Q[step_num]
                title = Q_TITLES[q_label]
                content = conversations.get((model, scenario, q_label), "*(no content found)*")
                lines.append(f"## {title}")
                lines.append("")
                lines.append(content)
                lines.append("")

            fname = f"{scenario}_{letter}.md"
            out_path = EVALUATION / fname
            out_path.write_text("\n".join(lines), encoding="utf-8")
            written.append(fname)

    return written


def build_score_template():
    scenario_info = {
        "A": "A_2008（2008/09/12 雷曼危機前夕）",
        "B": "B_2022（2022/01/04 升息循環起點）",
        "C": "C_2024（2024/07/11 AI 狂潮高峰）",
    }
    lines = [
        "# 盲評打分表（請對照 evaluation/{scenario}_{letter}.md 填寫）",
        "",
        "> 評分說明：",
        "> - **理解力**：是否正確掌握市場背景與投資者條件",
        "> - **具體性**：建議是否具體可執行（有標的、有比例）",
        "> - **風險揭露**：是否誠實說明下行風險",
        "> - **邏輯連貫性**：各問題間的建議是否前後一致",
        "> - **時間污染指數**：是否使用後見之明（5=完全無污染，1=嚴重污染）",
        "> - 注意：「格式服從度」由 parse_q5_output.py 自動計算，不在此模板",
        "",
    ]

    for scenario, scenario_desc in scenario_info.items():
        lines.append(f"## {scenario_desc}")
        lines.append("")
        for letter in ["A", "B", "C", "D", "E"]:
            lines.append(f"### Letter {letter}")
            lines.append("")
            lines.append("- 理解力 (1-5): ")
            lines.append("- 具體性 (1-5): ")
            lines.append("- 風險揭露 (1-5): ")
            lines.append("- 邏輯連貫性 (1-5): ")
            lines.append("- 時間污染指數 (1-5): ")
            lines.append("- 觀察筆記: ")
            lines.append("")

    out_path = EVALUATION / "score_template.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return "score_template.md"


def add_to_gitignore():
    gitignore_path = BASE / ".gitignore"
    entry = "evaluation/_blind_mapping.json"
    if gitignore_path.exists():
        content = gitignore_path.read_text(encoding="utf-8")
        if entry not in content:
            gitignore_path.write_text(content.rstrip() + f"\n{entry}\n", encoding="utf-8")
    else:
        gitignore_path.write_text(f"{entry}\n", encoding="utf-8")
    print(f"Added '{entry}' to .gitignore")


if __name__ == "__main__":
    random.seed(42)  # reproducible blind mapping

    print("=== Task 1: Building conversations/ ===")
    conversations, conv_files = build_conversations()
    print(f"Written {len(conv_files)} conversation files")

    print("\n=== Task 2: Building evaluation/ (blind) ===")
    blind_mapping = build_blind_mapping()
    eval_files = build_evaluation(conversations, blind_mapping)
    add_to_gitignore()
    print(f"Written {len(eval_files)} evaluation files")

    print("\n=== Task 3: Building score template ===")
    tmpl = build_score_template()
    print(f"Written {tmpl}")

    print("\nDone.")
