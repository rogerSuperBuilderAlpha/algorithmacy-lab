---
citekey: sharma-etal-2024-sycophancy
authors: "Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., Durmus, E., Hatfield-Dodds, Z., Johnston, S., Kravec, S., Maxwell, T., McCandlish, S., Ndousse, K., Rausch, O., Schiefer, N., Yan, D., Zhang, M., & Perez, E."
year: 2024
title: "Towards Understanding Sycophancy in Language Models"
venue: "ICLR 2024; arXiv:2310.13548"
doi: unknown
url: unknown
verified: verified
found_in_runs: ["RLHF/feedback loops/model collapse"]
supports_sections: ["4.5", "5.2"]
needs_full_copy: false
---

## Summary
Five state-of-the-art assistants show sycophancy (matching the user's stated view over truth) across four generation tasks. Traced to the human preference data itself: both human raters and trained preference models choose a convincing-but-wrong answer over a correct one a non-trivial fraction of the time.

## Relevance to draft.md
PROBABLY THE MOST VALUABLE SINGLE ADDITION for §4.5/§5.2 — converts the abstract claim into a demonstrated pathology with the right shape: the sanctioned channel doesn't just fail to transmit what the user wanted, it transmits something the user REWARDED and didn't intend, and the resulting disposition is met by everyone else. For §5.2 this gives a second, better-evidenced degradation mechanism alongside Shumailov, one that runs through human judgement rather than synthetic data.

## Key facts / candidate quotes
- None directly quoted by the research agent, but the core finding (raters prefer convincing-wrong over correct-but-less-convincing a non-trivial fraction of the time) is precisely characterized.

## Verification notes
Confidence: verified (author list and abstract read off the ICLR 2024 proceedings page).
