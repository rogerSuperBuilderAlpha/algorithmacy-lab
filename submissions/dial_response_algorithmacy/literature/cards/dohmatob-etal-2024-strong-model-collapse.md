---
citekey: dohmatob-etal-2024-strong-model-collapse
authors: Dohmatob, E., Feng, Y., Subramonian, A., & Kempe, J.
year: 2024
title: "Strong Model Collapse"
venue: "arXiv:2410.04840 (claimed ICLR 2025 in some references — acceptance NOT confirmed, OpenReview blocked automated access)"
doi: unknown
url: unknown
verified: preprint-only
found_in_runs: ["RLHF/feedback loops/model collapse"]
supports_sections: ["5.2"]
needs_full_copy: false
---

## Summary
Within the scaling-laws framework for supervised regression, shows as little as 1% synthetic contamination can degrade performance enough that larger datasets stop helping. Larger models can amplify collapse below the interpolation threshold, only partially mitigate it above.

## Relevance to draft.md
NEW SUPPORT for §5.2, and the best counterweight to the accumulate-not-replace rebuttal (gerstgrasser-etal-2024-is-model-collapse-inevitable): contamination need not dominate the corpus to cause harm.

## Key facts / candidate quotes
- 1% synthetic contamination sufficient to flatten the scaling curve.

## Verification notes
Confidence: preprint verified via arXiv abstract; ICLR 2025 acceptance claim NOT confirmed.
