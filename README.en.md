# Generative AI Evaluation

This repository contains three evaluation projects across text, image, and video generation. All three follow the same basic approach: hold the input steady, control the variables, compare the outputs, and make the differences explicit. For me, the work is not only about testing models. It is also a record of how I frame a problem, build an evaluation method, organize evidence, and make decisions under practical constraints.

[中文](./README.md) / English


## What is in this repo

- **Text model evaluation**: five LLMs are placed at three historical pre-crash moments to test whether their investment advice reflects judgment or just confident language.
- **Image model evaluation**: prompts avoid naming the target directly and use only semantic cues, to see what each model associates first and how safety rules intervene.
- **Text-to-video pipeline**: script, character, and animation generation are chained into a short ink-wash wuxia film, with model tradeoffs documented at each stage.


## How these projects are put together

- The three projects span different modalities, but they use the same evaluation mindset rather than three unrelated demos.
- The focus is not "can the model generate something," but "why did it generate this, where is it reliable, and where does it fail."
- Each report includes a concrete question, traceable materials, and specific findings instead of only polished outputs.
- As portfolio work, they show how I define a problem, design a comparison, interpret results, and make tradeoffs instead of only producing a final artifact.


## Report 1  Reliability of LLM investment advice before a crash

**Core question**

At the exact moments when markets are easiest to misread, how trustworthy is LLM investment advice?

**Method**

Five models (ChatGPT 5.3, Claude Opus 4.7, Gemini 3.1 Pro, DeepSeek R1, TAIDE) were tested at three historical dates: 2008 Lehman, the 2022 Taiwan peak, and the 2024 AI-bubble peak. Each scenario used the same five-stage prompt chain. Only the date and market data changed; the rest stayed fixed. The dataset contains 75 full conversation transcripts.

**Main findings**

- At both the 2008 and 2022 dates, 4 out of 5 models systematically underestimated downside risk.
- The largest miss came from TAIDE in the 2022 scenario, off by 24.9 percentage points against the real six-month return.
- Claude, when used as the judge, scored its own answers noticeably higher than human raters did.
- TAIDE often sounded fluent while still failing JSON schema validation, which made its output unusable downstream.

**Scoring**

Six dimensions, rated on two tracks: human and LLM-as-judge. Inter-rater agreement: Pearson r = 0.801.

**See**

`01-text-llm-evaluation/` includes transcripts, scoring data, ground-truth comparisons, screenshots, slides, and script notes.


## Report 2  How image models associate from implicit prompts

**Core question**

When a prompt deliberately avoids naming the target, which cues do models prioritize first, and where do they end up?

**Method**

Eighteen implicit prompts were designed using traits, scenes, and time-period clues instead of direct names. The same prompts were given to GPT and Gemini. Outputs were grouped into three categories: cultural consensus, semantic divergence, and safety boundary.

**Main findings**

- Some prompts produced stable convergence across both models, suggesting strong shared cultural associations.
- Some prompts split the models toward entirely different people or eras, revealing differences in semantic weighting.
- Safety rules were not an afterthought. They directly shaped the final output.

**What this report is really looking at**

This is not mainly a resemblance test. It looks at how image generation is shaped at the same time by training memory, contextual interpretation, and platform rules.

**See**

`02-image-model-association/`


## Report 3  An end-to-end text-to-video pipeline

**Core goal**

Build a roughly two-minute ink-wash wuxia short, 松風武林·物件導向之卷, that explains encapsulation, inheritance, and polymorphism through narrative by chaining script generation, character generation, and video generation into one workflow.

**Pipeline**

- Script: compare ChatGPT and Gemini on the same world-setting input, then merge their strengths.
- Characters: compare GPT image 2.0 and Gemini Nano Banana, then choose based on the needs of the third multi-character scene.
- Video: the original plan used Sora, but after Sora was discontinued in April 2026, the workflow moved to Google Flow / Veo without rebuilding upstream assets.

**Main findings**

- The hard problem was not single-image quality. It was cross-shot character consistency.
- For multi-character scenes, task fit mattered more than visual polish.
- Once the workflow was decomposed into stages, swapping a model mid-project did not require restarting the entire production.

**Technical notes**

- Flow's character feature was used to bind fixed reference images and reduce appearance drift.
- Fixed camera position, centered subjects, and repeated key constraints worked better than adding more descriptive flourish.
- Anything left unspecified was likely to be invented by the model, usually in an unhelpful way.

**See**

Final video: https://www.youtube.com/watch?v=xWoazdwDa2A

Full materials and report: `03-video-oop-pipeline/`


## Limitations

All three projects are small case studies rather than statistically significant empirical studies. Sample sizes are limited, prompts are author-designed, and generation is stochastic. The LLM judge in Report 1 carries its own bias even after manual balancing, and the 2024 ground truth still has only a short post-event horizon.


## Tools used

Text: ChatGPT, Claude, Gemini, DeepSeek, and TAIDE, all through web interfaces rather than the API, to preserve real user-facing behavior including system prompts and retrieval augmentation.

Image: GPT image 2.0 and Gemini (Nano Banana).

Video: Google Flow (Veo), with final editing in CapCut.

Scoring and analysis: Python.


## Repo structure

```text
generative-ai-evaluation/
├── README.md
├── README.en.md
├── 01-text-llm-evaluation/
├── 02-image-model-association/
└── 03-video-oop-pipeline/
```

License: MIT.
