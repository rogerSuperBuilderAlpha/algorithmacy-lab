---
citekey: gao-schulman-hilton-2023-reward-model-overoptimization
authors: Gao, L., Schulman, J., & Hilton, J.
year: 2023
title: "Scaling Laws for Reward Model Overoptimization"
venue: "Proceedings of the 40th ICML (PMLR 202)"
doi: unknown
url: unknown
verified: verified
found_in_runs: ["RLHF/feedback loops/model collapse"]
supports_sections: ["4.5"]
needs_full_copy: false
---

## Summary
Synthetic setup with a fixed "gold" reward model supervising a proxy; optimizing hard against the proxy degrades gold-standard performance (Goodhart's law, quantified with clean functional forms scaling smoothly with reward-model size).

## Relevance to draft.md
NEW SUPPORT — formal statement, from the other side, of §4.5's "what can be taught is what the operator wants learned": the reward model is an imperfect proxy for contributors' judgements, and harder optimization drifts further from what contributors actually meant.

## Key facts / candidate quotes
- None directly quoted.

## Verification notes
Confidence: verified (PMLR v202, gao23h).
