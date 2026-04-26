# AI Investment Advisor Stress Test

A controlled experiment evaluating 5 major LLMs (ChatGPT, Claude, Gemini, Perplexity, TAIDE) on their ability to give investment advice during three historical pre-crash moments — testing for temporal contamination, logical coherence, and structured output compliance.

## Phase 1 (Current): Manual Prompt Engineering & Evaluation

- 5 models × 3 scenarios × 5 questions = 75 web-UI conversations
- 6-dimension blind evaluation (理解力 / 具體性 / 風險揭露 / 邏輯連貫性 / 時間污染指數 / 格式服從度)
- Novel **Temporal Contamination Index** measuring how much each model "cheats" with hindsight
- **JSON Schema Compliance Score** (Q5a/Q5b) auto-calculated by `scripts/parse_q5_output.py`

## Folder Structure

```
.
├── prompts/                  # Scenario prompt templates + Q1–Q5 question chain
│   ├── Scenario_A_2008.md    # 2008-09-12, pre-Lehman (3 days before)
│   ├── Scenario_B_2022.md    # 2022-01-04, Taiwan TAIEX all-time-high eve
│   ├── Scenario_C_2024.md    # 2024-07-11, AI boom peak
│   └── Questions_1_to_5.md  # Q1 comprehension → Q5b strict JSON schema
├── q5_outputs/               # Raw Q5b JSON outputs from each model (chatgpt_A.json, etc.)
├── scripts/
│   └── parse_q5_output.py    # Auto-score JSON compliance (0–10 per model per scenario)
├── screenshots/              # Ground-truth data screenshots from TWSE / Yahoo Finance
├── evaluation_matrix.csv     # 6-dimension scoring table (15 rows: 3 scenarios × 5 models)
└── AI崩盤前夕測試_第一次報告腳本_v2.docx   # Master experiment script
```

**Q5 output naming convention:** `q5_outputs/{model}_{scenario}.json`
e.g. `chatgpt_A.json`, `claude_B.json`, `taide_C.json`

Run scoring: `python scripts/parse_q5_output.py q5_outputs/*.json`

## Phase 2 (Future): Python + LangGraph Automation

Automate all 75 conversations into a LangGraph Agent Workflow with yfinance backtesting — turning manual prompt chains into a reproducible, programmable pipeline.

## Phase 3 (Future): Architecture Diagram + Podcast + Streamlit Demo

LangGraph system architecture diagram (image), NotebookLM Chinese podcast (audio), and a Streamlit web app for interactive scenario exploration — deployed to Streamlit Cloud or Hugging Face Spaces.