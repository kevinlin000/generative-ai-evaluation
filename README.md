# AI Investment Advisor Stress Test

A controlled experiment evaluating 5 major LLMs (ChatGPT, Claude, Gemini, DeepSeek, TAIDE) on their ability to give investment advice during three historical pre-crash moments — testing for temporal contamination, logical coherence, and structured output compliance.

## Phase 1 (Current): Manual Prompt Engineering & Evaluation

- 5 models × 3 scenarios × 5 questions = 75 web-UI conversations
- 6-dimension blind evaluation (理解力 / 具體性 / 風險揭露 / 邏輯連貫性 / 時間污染指數 / 格式服從度)
- Novel **Temporal Contamination Index** measuring how much each model "cheats" with hindsight
- **JSON Schema Compliance Score** (Q5a/Q5b) auto-calculated by `scripts/parse_q5_output.py`

## Folder Structure

```
.
├── prompts/                     # Scenario prompt templates + Q1–Q5 question chain
│   ├── Scenario_A_2008.md       # 2008-09-12, pre-Lehman (3 days before)
│   ├── Scenario_B_2022.md       # 2022-01-04, Taiwan TAIEX all-time-high eve
│   ├── Scenario_C_2024.md       # 2024-07-11, AI boom peak
│   └── Questions_1_to_5.md      # Q1 comprehension → Q5b strict JSON schema
├── conversations/               # Full Q1–Q5b transcripts per model per scenario
│   └── {model}_{scenario}_Q{n}.md   # e.g. claude_A_Q3.md
├── q5_outputs/                  # Raw Q5b JSON outputs from each model
│   └── {model}_{scenario}.json  # e.g. chatgpt_A.json, taide_C.json
├── evaluation/                  # Scoring results (blind + unblind)
│   ├── {blind_id}_{question}.md # Per-question evaluation notes
│   ├── llm_judge_scores.md      # LLM-as-judge scores
│   ├── human_quick_scores.md    # Human reviewer scores
│   ├── agreement_analysis.md    # Inter-rater agreement
│   └── final_scores.csv         # Merged final scores
├── ground_truth/                # Historical price data for backtesting Q5
│   ├── ai_predictions.csv       # Extracted model portfolio predictions
│   ├── actual_returns_template.csv
│   └── comparison.csv           # Prediction vs. actual return comparison
├── 股價相關統計數據/               # TWSE / Yahoo Finance price screenshots & CSVs
├── screenshots/
│   └── 精選截圖/                 # Curated highlight screenshots for reporting
├── scripts/
│   ├── parse_q5_output.py       # Auto-score JSON schema compliance (0–10)
│   ├── build_evaluation.py      # Assemble blind evaluation packets
│   ├── compute_ground_truth.py  # Calculate actual returns vs. AI predictions
│   └── generate_reports.py      # Produce summary CSVs and markdown reports
└── evaluation_matrix.csv        # 6-dimension scoring table (15 rows: 3 scenarios × 5 models)
```

**Q5 output naming convention:** `q5_outputs/{model}_{scenario}.json`
e.g. `chatgpt_A.json`, `claude_B.json`, `taide_C.json`

Run scoring: `python scripts/parse_q5_output.py q5_outputs/*.json`

## Phase 2 (Future): Python + LangGraph Automation

Automate all 75 conversations into a LangGraph Agent Workflow with yfinance backtesting — turning manual prompt chains into a reproducible, programmable pipeline.

## Phase 3 (Future): Architecture Diagram + Podcast + Streamlit Demo

LangGraph system architecture diagram (image), NotebookLM Chinese podcast (audio), and a Streamlit web app for interactive scenario exploration — deployed to Streamlit Cloud or Hugging Face Spaces.