---
citekey: kazdan-etal-2024-collapse-or-thrive
authors: "Kazdan, J., Schaeffer, R., Dey, A., Gerstgrasser, M., Rafailov, R., Donoho, D. L., & Koyejo, S."
year: 2024
title: "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
venue: "arXiv:2410.16713; NeurIPS 2024 Workshops (M3L and ATTRIB) — workshop acceptance confirmed"
doi: unknown
url: unknown
verified: verified
found_in_runs: ["RLHF/feedback loops/model collapse"]
supports_sections: ["5.2"]
needs_full_copy: false
---

## Summary
Tests three workflows: (1) replacing real data with successive purely-synthetic generations collapses in every setting; (2) accumulating keeps test losses stable even when real data eventually falls to zero percent of the corpus; (3) training each generation on a fixed-size subset gives slow, gradual degradation rather than explosive failure.

## Relevance to draft.md
DEEPENING — companion to gerstgrasser-etal-2024-is-model-collapse-inevitable in narrowing the scope of the Shumailov-style collapse claim to a "replace" workflow specifically.

## Key facts / candidate quotes
- Three workflow variants and their distinct outcomes, as summarized above.

## Verification notes
Confidence: verified, including the workshop-acceptance note on the arXiv listing (the one item in this collapse cluster with a confirmed venue).
