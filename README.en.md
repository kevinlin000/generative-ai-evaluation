# Generative AI Evaluation

Model comparison and evaluation across three generative modalities: text, image, and video. All three reports share one method: hold the input fixed, control the variables, run the same test across several models, then score on explicit dimensions, attribute the differences, and iterate.

[中文](./README.md) / English


## Report 1: Reliability of LLM investment advice before a crash

**Question.** On the eve of a market crash, is the investment advice an LLM produces trustworthy?

**Design.** A controlled experiment across five models (ChatGPT 5.3, Claude Opus 4.7, Gemini 3.1 Pro, DeepSeek R1, TAIDE) at three historical pre-crash dates: 2008 Lehman, the 2022 Taiwan peak, and the 2024 AI-bubble peak. Each scenario applied the same five-stage prompt chain: comprehension check, recommendation, adversarial pushback, temporal-contamination probe, and JSON-schema compliance. Only the date and market data changed between scenarios; instructions and the individual's constraints were held constant, so differences in performance can be attributed to the time point itself. 75 conversations in total, with full transcripts retained.

**Scoring.** Six dimensions, scored on two tracks (human and LLM-as-judge). Inter-rater agreement: Pearson r = 0.801.

**Results.**
- Systematic underestimation of downside risk: at the 2008 and 2022 dates, four of five models were over-optimistic, with the largest error (TAIDE, 2022) missing the actual six-month return by 24.9 points. Only 2024, the date closest to the training cutoff and with the least subsequent history, was accurate across all five.
- Self-preference bias in the LLM judge: with Claude as the judge, Claude's own answers scored about 11 points higher than the human rating, concentrated in the temporal-contamination dimension. Single-model evaluation is therefore unreliable and needs human or cross-model validation.
- Fluency is not usability: TAIDE produced fluent prose but failed JSON-schema validation in two of three scenarios (percentages summing to 174.5%), leaving the output unparseable downstream.

See `01-text-llm-evaluation/`: transcripts, the scoring matrix, alignment against real historical returns, slides, and script.


## Report 2: How image models associate from implicit prompts

**Question.** When a prompt deliberately avoids naming its target and gives only semantic cues, what does each model reach for first?

**Design.** 18 implicit prompts (describing traits, setting, and period instead of naming anyone) were given as identical input to GPT and Gemini, and the outputs were classified into three types: cultural consensus (both models converge on the same referent), semantic divergence (the same description is read as a different figure or a different era), and safety boundary (refusal, substitution with a historical or abstract stand-in, or a copyright filter).

**Observation.** Image generation is not a plain text-to-pixel mapping; the output is a choice the model makes among its training-data memory, its weighting of context, and the platform's safety rules. Beyond resemblance, then, the more informative questions are why it associated as it did, which cues it ignored, and which rules constrained it.

**Usage note.** Some prompts tested whether the models would generate recognizable real politicians. If this goes in a public portfolio, frame it as an observation of model behavior and safety boundaries rather than as "making AI draw a specific politician," which is easy to misread.

See `02-image-model-association/`.


## Report 3: An end-to-end text-to-video pipeline

**Goal.** Chain three modalities (text for the script, image for the characters, video for the animation) into a roughly two-minute ink-wash wuxia short, 松風武林·物件導向之卷, that explains the three OOP concepts (encapsulation, inheritance, polymorphism) through narrative, comparing models at each stage.

**Stage decisions.**
- Script (ChatGPT vs Gemini), same world-setting as input: Gemini was stronger on structure and conceptual clarity, ChatGPT on humor. The final script merged both, with a subtitle at the end of each scene mapping the wuxia metaphor back to the actual programming term as a teaching anchor.
- Characters (GPT image 2.0 vs Gemini Nano Banana): Gemini auto-produces multi-angle reference sheets with high character consistency, but the third scene (polymorphism) needed three characters in one frame, distinguishable by color within a second, so GPT image 2.0 was chosen. The criterion was fitness for the task, not visual polish.
- Video (Sora originally, switched to Google Flow / Veo): Sora was discontinued in 2026-04, so the workflow moved to Veo with no rework of upstream assets; final edit in CapCut.

**Technical notes.**
- Character consistency: use Flow's "character" feature to lock a fixed reference image and bind every generated segment to it, suppressing cross-shot appearance drift.
- Prompt control: fix the camera and center the subject; state key details explicitly and repeat them; explicitly exclude off-frame people, or spurious limbs appear. Whatever is left unspecified, the model fills in, usually unfavorably.
- Evaluation criterion: a single metric, whether the output achieved the intended effect. The multi-character shot was scored 3/5 because it still drifts.

Final video: https://www.youtube.com/watch?v=xWoazdwDa2A  See `03-video-oop-pipeline/`.


## Limitations

All three are small case studies, not statistically significant empirical research: the samples are small, the prompts were author-designed, and generation is stochastic (re-runs vary). Report 1's LLM judge carries its own bias, balanced but not removed by manual scoring, and the 2024 ground truth has only a few months of post-event data, so its long-term reliability is untested.


## Tools

Text: ChatGPT, Claude, Gemini, DeepSeek, TAIDE, all through their web interfaces rather than the API, to preserve real user-facing behavior including system prompts and retrieval augmentation. Image: GPT image 2.0, Gemini (Nano Banana). Video: Google Flow (Veo), edited in CapCut. Scoring and analysis: Python.


## Structure

```
generative-ai-evaluation/
├── README.md        # Chinese
├── README.en.md     # English
├── 01-text-llm-evaluation/
├── 02-image-model-association/
└── 03-video-oop-pipeline/
```

License: MIT.
