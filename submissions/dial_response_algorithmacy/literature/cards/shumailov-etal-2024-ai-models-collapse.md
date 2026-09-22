---
citekey: shumailov-etal-2024-ai-models-collapse
authors: Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y.
year: 2024
title: "AI models collapse when trained on recursively generated data"
venue: Nature, 631, 755–759
doi: 10.1038/s41586-024-07566-y
url: unknown
verified: verified
found_in_runs: ["RLHF/feedback loops/model collapse"]
supports_sections: ["5.2"]
needs_full_copy: false
---

## Summary
Already cited in draft.md §5.2. The original "model collapse" Nature paper: training a model recursively on its own (or prior generations') synthetic outputs degrades it over successive generations. Mechanism: model → synthetic data → model, in a replace (not accumulate) workflow.

## Relevance to draft.md
⚠️ MECHANISM MISMATCH FLAGGED. The paper's overall finding has NOT been retracted or refuted — alemohammad-etal-2024-self-consuming-models-mad reached the same conclusion independently in images, and dohmatob-etal-2024-strong-model-collapse sharpened it (1% contamination suffices). BUT the follow-up literature (gerstgrasser-etal-2024-is-model-collapse-inevitable, kazdan-etal-2024-collapse-or-thrive) showed the collapse is specific to a REPLACE workflow, and schaeffer-etal-2025-model-collapse-position found 8 incompatible definitions of "collapse" circulating. More importantly: Shumailov's mechanism is model→synthetic-data→model — NOT the draft's actual mechanism of user-feedback→model→user. A reviewer who knows this literature will notice the elision. RECOMMENDED FIX (per the research agent): keep Shumailov as an ANALOGY, not the load-bearing citation; put the actual weight on sharma-etal-2024-sycophancy (degradation running through human preference judgement) and milli-etal-2025-engagement-divisive-content (an engagement loop that measurably produces a feed no contributor prefers), whose mechanisms match the paper's claim.

## Key facts / candidate quotes
- Shumailov's own response to the accumulate-workflow rebuttal, reported by the research agent: it "does not really invalidate anything we showed" — fair, but concedes the scope-narrowing.

## Verification notes
Confidence: verified, established citation. The finding stands; its FIT to §5.2's specific claim is what needs revision — see Relevance note.
