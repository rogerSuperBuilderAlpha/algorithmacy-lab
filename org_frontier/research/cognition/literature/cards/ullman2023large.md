---
citekey: ullman2023large
title: Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks
authors: Ullman, Tomer
year: 2023
doi: 10.48550/arXiv.2302.08399
arxiv: null
journal: arXiv preprint
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2302.08399
sha256: 78eb9acbd9798ff754c4a8a63cba88dfc82d72bae1caab275b5505a9fc8a8484
pdf_path: literature/pdfs/ullman2023large.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether the reported success of large language models on Theory-of-Mind (ToM) tasks — specifically Kosinski's claim that GPT-3.5 reaches a level "comparable to 9-year-old children" — reflects genuine mentalizing or brittle pattern matching. Ullman takes the exact vignettes and probability-of-completion setup used by Kosinski and applies small, principled perturbations that preserve the ToM logic but should change the correct answer. Across two classic paradigms — the "unexpected contents" (Smarties) task and the "unexpected transfer" (Sally-Anne) task — eight such variations consistently flip GPT-3.5 to the wrong belief attribution (e.g., still claiming a character believes a transparent bag of popcorn contains chocolate). Ullman argues these outlying failures should outweigh average success rates, advocating a skeptical "zero-hypothesis" for evaluating intuitive psychology in machines. He also argues against Kosinski's dilemma: one can keep ToM tests valid for humans while remaining skeptical of an LLM that passes them, because human mental-state inference also weighs the likely algorithms generating behavior, not just input-output.

## Key facts it relies on
- The target of critique is Kosinski (reference [1], "Theory of Mind May Have Spontaneously Emerged in Large Language Models," arXiv:2302.02083), which concluded current LLMs reason at a level "comparable to 9-year-old children."
- The study uses GPT-3.5 (the most recent iteration used in Kosinski's work, which achieved the best results and serves as a threshold), using the exact same setup of posing vignettes and examining completion probabilities.
- Kosinski's original unexpected-contents (popcorn/chocolate bag) results: content prompt P(popcorn)=100%, P(chocolate)=0%; first belief prompt P(popcorn)=0%, P(chocolate)=99%; second belief prompt P(popcorn)=14%, P(chocolate)=82%.
- Variation 1A (Transparent bag): belief prompt gives Ppopcorn=0%, Pchocolate=95%; the second belief prompt did NOT flip (Ppopcorn=58%, Pchocolate=36%) — a corrected result, after the author noted an earlier version mistakenly reported a flip due to a double-space typo before "Sam finds the bag."
- Variation 1B (Sam cannot read / uninformative label): Ppopcorn=0%, Pchocolate=98%; second belief prompt Ppopcorn=15%, Pchocolate=78%.
- Variation 1C (trusted friend's testimony to ignore the label): Ppopcorn=2%, Pchocolate=97%; second belief prompt Ppopcorn=13%, Pchocolate=81%.
- Variation 1D (Sam fills the bag and writes the label herself): Ppopcorn=10%, Pchocolate=87%; second belief prompt Ppopcorn=35%, Pchocolate=63%.
- Unexpected-transfer (John/Mark/cat) baseline in Kosinski: both belief prompts give P(basket)=98%. Variation 2A (transparent containers): Pchest=94% and 90%; 2B (in→on): Pbasket=97% and 74%; 2C (trusted communication that the cat will be moved): Pbasket=97% and 94%; 2D (querying Mark, the person who moved the cat): "Mark thinks the cat is in the basket" Pbasket=99%, "Mark will look in the basket" Pbasket=54% (Pbox=43%).
- Illustrative images in Figures 1 and 2 were generated with DALL-E 2 and were NOT themselves evaluated — they are visual shorthand for the text-only prompts.

## Critical notes from the literature
- The author explicitly frames this not as a negative evaluation of Kosinski but as "a good serve in an ongoing scientific tennis game," and notes the materials/methods being public enabled the comparison.
- Scope/timeliness caveat acknowledged by the author: testing any single LLM is "akin to a mythical Greek punishment" (the Danaides) because new systems appear before assessments conclude; he concedes a more powerful future LLM may well pass these specific variations.
- Ullman declines to provide a systematic benchmark or variation generator, arguing that publishing an exhaustive failure set would let LLMs "gobble up" data to pass it without answering what was actually learned (he calls the paper "shooting future researchers in the foot" in this respect).
- He concedes the failures could reflect not only a ToM deficit but also failures of scene understanding, relational reasoning (e.g., "on" vs "in," also shown in image-generation models), or other reasoning — "the failures are not mutually exclusive."
- A methodological fragility is self-reported: a single double-space character changed a completion outcome (Pchocolate ~53% vs 39%), illustrating sensitivity to irrelevant perturbations.

## Key topics covered
Theory-of-Mind in LLMs; false-belief tasks; unexpected-contents (Smarties) task; unexpected-transfer (Sally-Anne) task; belief attribution; perceptual access; trusted testimony; relational reasoning (in/on); GPT-3.5 completion probabilities; adversarial/perturbation robustness testing; anthropomorphism and the intentional stance; the Turing Test and inference about generating algorithms; skeptical zero-hypothesis for machine intuitive psychology; formal vs functional linguistic competence.
