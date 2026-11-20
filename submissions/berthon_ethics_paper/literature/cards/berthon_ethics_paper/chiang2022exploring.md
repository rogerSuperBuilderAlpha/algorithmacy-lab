---
citekey: chiang2022exploring
title: Exploring the Effects of Machine Learning Literacy Interventions on Laypeople's Reliance on Machine Learning Models
authors: Chiang, Chun-Wei; Yin, Ming
year: 2022
type: chapter
doi: 10.1145/3490099.3511121
venue: Proceedings of the 27th International Conference on Intelligent User Interfaces (IUI '22), ACM, pp. 148-161
source_basis: full-text
pages_read: "pp. 148-161 (pdf pp. 1-14); appendix pages skimmed"
source_url: https://par.nsf.gov/servlets/purl/10320531
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N4/chiang2022/par10320531.pdf
sha256: dc31506750fa9a295257767b28bcce981b9359b0e83f180c3576441dade6484e
manuscript_lines: []
ledger_rows: [E16, N17]
premises: [A4, A8]
facet: N4
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Crossref confirms the paper (IUI '22, pp. 148-161). The ACM PDF returned HTTP 403 (Cloudflare); I read the NSF Public Access Repository copy, which carries the ACM pagination (p. 148 on the first page). The study is a randomised experiment with 498 MTurk workers in the US predicting house prices with an ML model's help, on in-distribution and out-of-distribution examples. Treatments varied whether a user tutorial (the "ML literacy intervention") was given, whether it was interactive, and whether it addressed ML in general or the specific model; one arm used a model card. The authors split subjects by their own unaided accuracy: 40.4 per cent were "low-performing". For high performers, an interactive, model-specific tutorial reduced over-reliance when they could outperform the model. For low performers, no intervention changed reliance: "none of our ML literacy interventions could impact the low-performing subjects' reliance on the ML model" (p. 159). The study is a single task, short-term, with crowd workers.

## Key facts it relies on
- p. 153: "In total, 498 unique subjects participated in our experiment".
- p. 148 (abstract): "for those individuals who have relatively high ability in solving the decision-making task themselves, receiving a user tutorial that is interactive and addresses the specific ML model to be used allows them to reduce their over-reliance on the ML model when they could outperform the model. In contrast, low-performing individuals' reliance on the ML model is not affected by the presence or the type of user tutorial."
- p. 157 (§5.4.2): "providing the ML literacy interventions to low-performing subjects did not have significant impacts on their reliance on the model on either out-of-distribution or in-distribution examples, as compared to those low-performing subjects who did not receive any ML literacy interventions."
- p. 159: "none of our ML literacy interventions could impact the low-performing subjects' reliance on the ML model."
- p. 159 (Limitations): "Our study was conducted with laypeople (i.e., subjects recruited from Amazon Mechanical Turk) on one specific type of prediction task. Therefore, cautions should be used when generalizing results".

## Critical notes from the literature
- Puppart and Aru (2025; `puppart2025brief`) find a brief text intervention did not reduce over-reliance among 36 Estonian students and raised under-reliance: a second null result for short literacy interventions, in a smaller sample.

## Where the argument uses it
- A8, M11, E16: supports. The one controlled test I found of literacy training for laypeople (the population nearest to "the people acted on") shows the benefit going to those already competent; those who most need help are unmoved. This is the literacy-myth pattern (Kamperman and Graff 2026, `kamperman2026ai`) in experimental form: a course beside the task helps the already able.
- Narrows: an interactive, model-specific tutorial did help some people. Support built around the specific system did better than general instruction, which fits the paper's duty D08 (scaffold inside the system) rather than refuting it.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
