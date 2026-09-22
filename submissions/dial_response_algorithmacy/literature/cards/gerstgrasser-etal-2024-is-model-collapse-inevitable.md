---
citekey: gerstgrasser-etal-2024-is-model-collapse-inevitable
authors: "Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., Pai, D., Gromov, A., Roberts, D. A., Yang, D., Donoho, D. L., & Koyejo, S."
year: 2024
title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
venue: "arXiv:2404.01413 (venue disputed: one source lists COLM 2024, another an ICML 2024 workshop — check before citing a venue)"
doi: unknown
url: unknown
verified: probably-real-check
found_in_runs: ["RLHF/feedback loops/model collapse"]
supports_sections: ["5.2"]
needs_full_copy: false
---

## Summary
Central rebuttal to model-collapse results including Shumailov et al. Prior collapse results assume each generation's data REPLACES the last; if synthetic data instead ACCUMULATES alongside real data, test error has a finite upper bound independent of iteration count, and collapse does not occur — demonstrated across LLMs, diffusion models, and VAEs.

## Relevance to draft.md
CAUTION/COMPLICATION — this is central to the fix needed for §5.2's Shumailov citation. Narrows the scope of "the loop can degrade the model for everyone": collapse is an artefact of a specific (replace) workflow, not inevitable. See Verification notes for the recommended handling.

## Key facts / candidate quotes
- None directly quoted.

## Verification notes
Confidence: paper/authors/result verified; VENUE DISPUTED (COLM 2024 vs. ICML 2024 workshop) — citing the arXiv preprint directly is safe, do not assert a specific venue without checking.
