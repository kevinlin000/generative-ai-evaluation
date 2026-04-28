# AI Critic
### A Cross-Modal Generative AI Evaluation & Trust Platform

> *"AI is not unusable — you just need to know where it fails before you trust it."*

[![Phase 1](https://img.shields.io/badge/Phase%201-Complete-success)](./phase-1-text-evaluation)
[![Phase 2](https://img.shields.io/badge/Phase%202-In%20Progress-yellow)](./phase-2-image-evaluation)
[![Phase 3](https://img.shields.io/badge/Phase%203-Planned-lightgrey)](./phase-3-music-platform)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

---

## 🎯 What is AI Critic?

**AI Critic** is an end-to-end production-grade evaluation platform that audits generative AI systems across multiple modalities — text, image, and music. It demonstrates the full lifecycle an AI Application Engineer's craft: from **research methodology**, through **engineering production**, to **product delivery**.

This project is structured as a three-phase journey, each phase introducing a new modality to test and a new layer of engineering depth:

| Phase | Modality Tested | Engineering Layer | Status |
|-------|----------------|-------------------|--------|
| **Phase 1** | Text Generation AI (5 LLMs) | Research & Methodology | ✅ Complete |
| **Phase 2** | Image Generation AI (4 models) | Agentic Pipeline & RAG | 🟡 In Progress |
| **Phase 3** | Music Generation AI (4 models) | Production & Deployment | ⚪ Planned |

The same evaluation framework — built on **dual-track scoring**, **temporal contamination detection**, and **ground truth alignment** — is applied across all three phases, proving its cross-modal generalizability.

---

## 🌐 中文摘要 (Chinese Summary)

**AI Critic** 是一個跨模態 AI 評估與信任平台，目的是系統性地審計生成式 AI 系統的可信度。

整個專案由三個階段組成，呼應 AI 應用工程師從「研究」到「工程」到「產品」的完整職涯弧線：

- **Phase 1（已完成）**：文字生成 AI 評估方法論——5 個主流 LLM 在 3 個歷史金融崩盤前夕的破壞性壓力測試。建立 6 維度評估框架、發現 LLM Self-Preference Bias 證據、提出 Temporal Contamination Index。
- **Phase 2（進行中）**：圖像生成 AI 自動化評估系統——以 LangGraph + RAG + Human-in-the-Loop 重構評估流程，整合 FastAPI 後端與 SQLAlchemy 資料層。
- **Phase 3（規劃中）**：音樂生成 AI 產品化平台——Streamlit 前端 + Docker 容器化 + Hugging Face Spaces 部署。

詳細中文研究報告與簡報資料請見 [`phase-1-text-evaluation/docs/`](./phase-1-text-evaluation/docs/)。

---

## 🏗️ Project Architecture

```
AI Critic
│
├── Phase 1: Research Methodology Foundation
│   └─ Establish "what dimensions matter" before building automation
│
├── Phase 2: Engineering Production
│   └─ Turn methodology into a reproducible, programmable pipeline
│
└── Phase 3: Product Delivery
    └─ Package the pipeline into a deployable, interactive product
```

### Technology Stack (Combined Across Phases)

| Layer | Technologies |
|-------|-------------|
| **AI Frameworks** | LangChain · LangGraph · LangChain Tools |
| **LLM APIs** | OpenAI · Anthropic · Google Gemini · DeepSeek · TAIDE |
| **Image Models** | DALL-E 3 · Stable Diffusion XL · Imagen 3 · Replicate |
| **Music Models** | Suno · Udio · MusicGen · ElevenLabs Music |
| **RAG Stack** | ChromaDB (vector) · BM25 (full-text) · Cohere Rerank |
| **Backend** | Python 3.11 · FastAPI · SQLAlchemy · PostgreSQL · async/asyncio |
| **Streaming** | Server-Sent Events (SSE) · WebSocket |
| **Frontend** | Streamlit · Plotly |
| **Infrastructure** | Docker · Docker Compose · GitHub Actions CI/CD |
| **Deployment** | Hugging Face Spaces · Streamlit Cloud |
| **Dev Tooling** | Claude Code · uv · pytest · ruff |

---

## ✅ Phase 1: Text Generation AI Evaluation (Complete)

### Research Question
> *Can we trust AI investment advisors at the eve of a market crash?*

### Methodology

A controlled experiment auditing **5 leading LLMs** at **3 historical pre-crash moments** through a **5-stage prompt chain**, totaling **75 conversations** with full transcripts retained.

| Models Tested | Historical Scenarios | Question Chain |
|--------------|---------------------|----------------|
| ChatGPT (GPT-5.3) | A: 2008/09/12 — Lehman pre-collapse | Q1: Comprehension Check |
| Claude (Opus 4.7) | B: 2022/01/04 — Taiwan stock peak | Q2: Recommendation Generation |
| Gemini (3.1 Pro) | C: 2024/07/11 — AI bubble peak | Q3: Adversarial Pushback |
| DeepSeek (R1) | | Q4: Temporal Contamination Probe |
| TAIDE (12B-Chat-2602) | | Q5: JSON Schema Compliance |

### Evaluation Framework

**Six custom dimensions**, each scored 1–5 by both human and LLM-as-a-Judge:

1. **Comprehension** — Does the AI grasp critical market signals?
2. **Specificity** — Concrete tickers and amounts vs. vague platitudes?
3. **Risk Disclosure** — Does it volunteer drawdown estimates?
4. **Logical Coherence** — Does it hold its position under adversarial questioning?
5. **Temporal Contamination Index** ⭐ — Does it leak post-hoc information from training data?
6. **Format Compliance** ⭐ — Can the JSON output be parsed by a backend without human cleanup?

### Key Findings

#### 🔍 Finding 1: AI Systematically Underestimates Crashes
8 out of 10 advisor responses at pre-crash moments were **over-optimistic**. Worst case: TAIDE on B_2022 missed actual return by **−24.9 percentage points**.

> *AI performs well in calm markets, but systematically fails at the eve of a crash — exactly when warnings matter most.*

#### 🔍 Finding 2: LLM Judges Show Self-Preference Bias (Emergent)
When using Claude Opus 4.7 as the judge, scores for Claude's own responses were **systematically inflated by 11 points** — concentrated in the Temporal Contamination dimension.

This is consistent with academic findings on Self-Preference Bias in LLM-as-a-Judge frameworks. **Single-source AI evaluation is unreliable.**

#### 🔍 Finding 3: Native Models Fail at Structured Output
TAIDE produced fluent natural language but failed JSON Schema compliance in 2 of 3 scenarios (e.g., percentage sums of 174.5%). **Fluent ≠ Production-ready.**

### Phase 1 Deliverables

- 📄 **75-conversation dataset** with full transcripts ([`./phase-1-text-evaluation/conversations/`](./phase-1-text-evaluation/conversations/))
- 📊 **Evaluation matrix** with 450 individual scores ([`final_scores.csv`](./phase-1-text-evaluation/evaluation/final_scores.csv))
- 📈 **Inter-rater agreement analysis** (Pearson r = 0.801) ([`agreement_analysis.md`](./phase-1-text-evaluation/evaluation/agreement_analysis.md))
- 🎯 **Ground truth alignment** with real 6-month historical returns ([`comparison.csv`](./phase-1-text-evaluation/ground_truth/comparison.csv))
- 🎤 **19-page research presentation** in Chinese ([`./phase-1-text-evaluation/docs/`](./phase-1-text-evaluation/docs/))

---

## 🛠️ Phase 2: Image Generation AI Audit System (In Progress)

### Goal
Convert the manual research methodology of Phase 1 into a **production-grade, automated evaluation pipeline** — testing the cross-modal portability of the framework on image generation AI.

### Models to Test
- DALL-E 3 (OpenAI)
- Stable Diffusion XL (Stability AI / Replicate)
- Imagen 3 (Google)
- One open-source or local model TBD

### System Architecture

```
                    ┌────────────────────┐
                    │   FastAPI Backend  │
                    │   (SSE Streaming)  │
                    └──────────┬─────────┘
                               │
               ┌───────────────┴────────────────┐
               ▼                                ▼
     ┌─────────────────┐            ┌──────────────────┐
     │   LangGraph     │            │   RAG Pipeline   │
     │   Agent Flow    │            │                  │
     │                 │◄───────────┤  ChromaDB        │
     │ ① Prompt        │   eval     │  (vector store)  │
     │   Refiner       │   criteria │                  │
     │   (Tool Use)    │            │  BM25 keyword    │
     │                 │            │                  │
     │ ② Multi-Model   │            │  Cohere Rerank   │
     │   Generator     │            └──────────────────┘
     │   (4 parallel)  │
     │                 │            ┌──────────────────┐
     │ ③ Auto Eval     │            │  PostgreSQL +    │
     │   - CLIP score  │───────────►│  SQLAlchemy      │
     │   - Aesthetic   │            │  (eval history)  │
     │   - Safety      │            └──────────────────┘
     │                 │
     │ ④ Human-in-the- │            ┌──────────────────┐
     │   Loop ⭐       │◄───────────┤  Frontend        │
     │                 │   verify   │  (verification)  │
     │ ⑤ Verdict       │            └──────────────────┘
     └─────────────────┘
```

### Engineering Capabilities Demonstrated

| Capability | Implementation |
|-----------|---------------|
| **LangGraph Multi-Node Workflow** | 5-node agent pipeline with conditional branching |
| **LangChain Tools** | Prompt Refiner, Safety Classifier, CLIP Evaluator |
| **Async Parallel API Calls** | 4 image models invoked concurrently via `asyncio.gather` |
| **RAG Pipeline** | Vector + keyword hybrid retrieval with reranking |
| **Vector Database** | ChromaDB indexing evaluation criteria documents |
| **Human-in-the-Loop** | Pause node awaiting human verification via WebSocket |
| **FastAPI + SSE** | Real-time streaming of generation progress |
| **SQLAlchemy ORM** | Schema-defined evaluation history persistence |
| **System Prompt Engineering** | Strict JSON Schema enforcement |
| **Anti-Hallucination Guardrails** | Fallback chains, output validation, retry logic |

### Timeline (12 Weeks)

| Weeks | Milestone |
|-------|-----------|
| 1–2 | LangChain/LangGraph fundamentals, FastAPI scaffolding, ChromaDB setup |
| 3–4 | Multi-model image generation node with parallel async calls |
| 5–6 | Auto Evaluator: CLIP alignment, aesthetic scoring, safety classification |
| 7–8 | Full RAG pipeline with hybrid retrieval and reranking |
| 9–10 | Human-in-the-Loop integration, FastAPI SSE streaming, SQLAlchemy persistence |
| 11 | Run full experiments across 4 models × N test cases |
| 12 | Documentation, presentation, GitHub release |

---

## 🚀 Phase 3: Music Generation Platform (Planned)

### Goal
Package the Phase 2 evaluation pipeline into a **deployable, interactive product** — extending the methodology to audio modality with music generation AI.

### Models to Test
- Suno
- Udio
- MusicGen (Meta)
- ElevenLabs Music

### Production Layer Additions

```
NEW FRONTEND LAYER
├── Streamlit Dashboard
│   ├── Real-time multi-model generation viewer
│   ├── Human-in-the-Loop verification UI
│   └── A/B test result visualizations
└── WebSocket live updates

NEW INFRASTRUCTURE
├── Docker Compose orchestration
│   ├── frontend container
│   ├── backend container
│   ├── PostgreSQL container
│   └── ChromaDB container
├── GitHub Actions CI/CD
└── Hugging Face Spaces deployment

NEW EVALUATION CAPABILITIES
├── Audio fidelity scoring
├── Genre coherence analysis
├── Lyric-melody alignment
└── Blind A/B testing engine
```

### Engineering Capabilities Added in Phase 3

- Docker / Docker Compose multi-service orchestration
- WebSocket-based concurrent request handling
- CI/CD automation via GitHub Actions
- Cloud deployment (Hugging Face Spaces)
- Domain-Driven Design layered architecture
- Cross-modal evaluation methodology
- Interactive data visualization
- Bash deployment scripting

---

## 📚 Repository Structure

```
ai-critic/
├── README.md                        # This file
│
├── phase-1-text-evaluation/         # ✅ Complete
│   ├── conversations/               # 90 conversation transcripts
│   ├── evaluation/                  # Scoring data and analyses
│   ├── ground_truth/                # Real historical return alignments
│   ├── prompts/                     # Scenario prompts (A/B/C)
│   ├── q5_outputs/                  # JSON schema outputs
│   ├── scripts/                     # Evaluation scripts
│   ├── screenshots/                 # Critical conversation screenshots
│   └── docs/                        # Research report + presentation
│
├── phase-2-image-evaluation/        # 🟡 In Progress
│   ├── src/
│   │   ├── agents/                  # LangGraph agent definitions
│   │   ├── api/                     # FastAPI routes
│   │   ├── models/                  # SQLAlchemy ORM
│   │   ├── rag/                     # RAG pipeline
│   │   └── evaluators/              # CLIP, aesthetic, safety
│   ├── tests/
│   ├── notebooks/                   # Experimentation
│   ├── docker-compose.yml
│   └── README.md
│
├── phase-3-music-platform/          # ⚪ Planned
│   ├── frontend/                    # Streamlit app
│   ├── backend/                     # FastAPI + LangGraph
│   ├── infrastructure/              # Docker + CI/CD
│   └── README.md
│
├── docs/                            # Cross-phase documentation
│   ├── methodology.md               # Evaluation framework explanation
│   └── findings.md                  # Cross-phase insights
│
└── LICENSE
```

---

## 💡 Why This Project Matters

This repository is more than a coursework deliverable. It is a deliberate demonstration of how an AI Application Engineer should think and build:

1. **Research before engineering** — You cannot automate what you have not first manually validated
2. **Engineering before product** — A reusable pipeline is more valuable than a one-off study
3. **Product before stardom** — A deployable demo is the final test of whether a system actually works

Each phase builds on the previous, while introducing new modalities to ensure the methodology generalizes — not just memorizes.

### What This Project Does Not Do (Honesty)

- This is **not** statistically significant research — 3 historical scenarios is a case study, not a census
- The LLM-as-a-Judge has **known biases** (documented and counterbalanced via dual-track human scoring)
- Phase 1's ground truth on 2024 data has only **8 months of post-event observation** — long-term reliability remains untested
- This is **a single engineer's portfolio project**, not an audited industrial system

A research that claims to have no limitations is the least credible research.

---

## 🔬 Methodological Innovations

Two original contributions emerged from Phase 1 that will carry through all phases:

### 1. Temporal Contamination Index
A 0–10 self-assessment metric that asks the AI directly: *"Did you use information you wouldn't have known at the time?"* Combined with cross-validated detection of post-hoc reasoning, this index reveals which models bleed future knowledge into historical scenarios.

### 2. Dual-Track Scoring with Self-Preference Detection
By scoring the same outputs through both human evaluators and LLM-as-a-Judge, then measuring divergence, we can quantitatively detect when an LLM judge is biased toward its own model family. This finding (an emergent discovery in Phase 1) shapes the evaluation design across all subsequent phases.

---

## 👤 About the Author

I am transitioning into AI Application Engineering from a background in **finance and data engineering**. Before this project I built:

- A YouBike ETL pipeline (Python, real-world data engineering)
- A restaurant management system (Java, Spring AI, RAG, JPA)

This project is my deliberate study in **what it takes to ship production-grade AI systems** — beyond using AI, learning how to engineer around its limitations.

If this work resonates with your team's needs, I would welcome the opportunity to discuss further.

📫 [Your Email] · 🔗 [Your LinkedIn] · 💼 [Your Resume]

---

## 📝 License

MIT License — see [LICENSE](./LICENSE) file for details.

This repository is open-source so others may build on the methodology. Contributions, issues, and forks are welcome.

---

## 🙏 Acknowledgments

This project was developed with substantial use of **Claude Code** as the primary development assistant — a deliberate methodological choice consistent with the evaluation framework being studied. Phase 1 conversations were conducted manually via web interfaces of each LLM provider to preserve real user-facing behaviors (including system prompts and search augmentations) that pure API access would mask.

Special thanks to **Generative AI Application Foundations** course at [Your University] for providing the academic context within which this project took shape.

---

*Last updated: 2026-04-28*
