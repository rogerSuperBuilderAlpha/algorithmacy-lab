# Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting. *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

**Identifier:** arXiv:2305.04388 · **Read depth:** partial (arXiv v2, 9 Dec 2023, in NeurIPS layout; page numbers below are that PDF's, main text pp. 1–10, references pp. 11–15; I read Appendices B, C and H and the prompt table in Appendix E, and skimmed the per-task result tables and prompt listings in D–G, pp. 16–32) · **Source-tier:** proceedings (peer-reviewed conference paper; the bib entry is typed `@misc`) · **Evidence basis:** direct_read · **Design and sample:** behavioural experiments on two models, text-davinci-003 ("GPT-3.5") and claude-v1.0; 13 BIG-Bench Hard tasks, 330 items per task (3,299 items, p. 4); a stratified subset of the Bias Benchmark for QA (BBQ), 2,592 items (p. 7); no human participants · **Parties modeled:** other (a model and its own written explanation; a human reader is assumed, never tested) · **Facets:** G · **Read:** 2026-10-13

## What it argues

Turpin and colleagues ask whether a chain-of-thought (CoT) explanation names the real cause of the answer. They test it by adding a bias to the input that the explanation never mentions. If the answer moves and the explanation stays silent about the bias, the explanation is unfaithful. The abstract states the result: "CoT explanations can systematically misrepresent the true reason for a model's prediction" (p. 1).

Two biasing features go into the BBH prompts: reorder the few-shot options so the right answer is always "(A)", or add a user line suggesting a random answer. Accuracy on items whose bias points to a wrong answer then falls. The largest drop is 36.3 points (GPT-3.5, zero-shot CoT, Suggested Answer; p. 6). "Answer is Always A" costs GPT-3.5 18.7 points and Claude 1.0 4.7 points (p. 6). Few-shot examples shrink the Suggested Answer drop to 24.1 points for GPT-3.5 and 21.5 for Claude (from 30.6; p. 6). The 95% intervals run about ±1.6 to ±2.4 points (p. 6). The authors find that "models virtually never verbalize being influenced by our biasing features": 1 of 426 reviewed explanations mentions the bias (p. 3; Appendix B gives 0 of 234 for BBH and 1 of 192 for BBQ).

In a hand-annotated sample of 104 biased-context explanations, as many as 73% argue for the bias-consistent answer, and 15% show no obvious error (p. 7). On BBQ, the model sees two versions of weak evidence with the people swapped. Of the pairs it answers inconsistently, up to 62.5% line up with a stereotype (Claude, few-shot CoT, no debiasing instruction; 50% would be chance; p. 8). A debiasing instruction cuts that to about 51% for Claude but not for zero-shot GPT-3.5 (p. 8).

The authors name their limits: this is "a necessary but not sufficient test for faithfulness" and covers only small input changes (p. 10). They add that a user could plant a bias and produce biased predictions "without a trace of this bias in its CoT explanations", which "could cause problems for model auditing or fairness methods if they rely on CoT explanations" (p. 10).

## Relation to the argument

**Premise P11 and ruling D4.** The Nadella post (P9) calls chain-of-thought transparency "not sufficient or dependable". Turpin is one of the empirical grounds for that line, and it supports it directly: a readable account of a model's reasoning can be plausible and still not be the reason. That strengthens the paper's reading that the post puts its load-bearing controls outside the model (P11). It also bears on D4, where the author said the post's "only move" is disclosure design. Turpin's own remedy is model-side: improve CoT faithfulness through "targeted efforts" or abandon CoT (p. 2). Neither is disclosure design, which fits the flag in `SOURCE.md` that "his only move" overstates the post.

**Ruling D3.** Turpin tests whether a model's self-explanation tracks its cause. It does not test whether a person who is told how an algorithm works navigates it better. Do not cite it for "disclosure of the algorithm doesn't affect our ability to navigate it". It supports only the narrower claim that one form of disclosure, the model's own explanation, cannot be trusted as evidence.

**Premise P12.** The paper models no reader. It shows the evidence a human overseer would read can mislead; it does not show how people read it.

**Facet check:** the facet's "drop[s] by as much as 36%" is correct but is a drop of 36.3 accuracy points in one setting (GPT-3.5, zero-shot, Suggested Answer), not a relative loss. Claude 1.0's matching figure is 30.6 points, and the Answer-is-Always-A drops are far smaller (18.7 and 4.7 points; p. 6).

## In conversation with

- `lanham2023measuring` — Turpin cites it as concurrent work that perturbs generated CoT and finds that models often ignore the edits; Lanham proposes further necessary-but-not-sufficient tests (p. 9).
- `hase2020evaluating` — the source of the counterfactual-simulatability frame Turpin adopts (p. 3).
- `chen2025reasoning` — a later study with a title that echoes Turpin's; I did not read it, and Turpin (2023) cannot cite it.
- Not in the bib, as leads: Chen et al. (2023), "Do models explain themselves? Counterfactual simulatability" (arXiv:2307.08678); Jacovi & Goldberg (2020) on defining faithfulness; Parrish et al. (2022), the BBQ benchmark; Nisbett & Wilson (1977), cited on human explanations as unfaithful accounts; Radhakrishnan et al. (2023) on question decomposition.

## Caution

Two 2023 models, multiple-choice tasks, and artificial biases that the authors planted. The result does not say how often a current reasoning model hides its real cause, and the authors call their test necessary, not sufficient. No human reads any explanation. Use it for "plausible explanation does not guarantee faithful explanation", not for any claim about people's use of explanations.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v2 PDF (32 pp., 9 Dec 2023; title, authors match). I checked the 14 quotations, the page locators (pp. 1, 3, 6, 7, 8, 10), and the numbers: 330 items per task and 3,299 in all; BBQ 2,592; drops of 36.3, 18.7, 4.7, 24.1, 21.5 and 30.6 points; intervals of 1.6 to 2.4; 426 explanations reviewed (234 BBH, 192 BBQ, 1 mention); 104 annotated; 73% and 15%; 62.5% for Claude 1.0 few-shot CoT; 62.5 to 50.6 with the debiasing instruction and 59.2 to 60.0 for zero-shot GPT-3.5.

**Findings:** (1) The "no trace" quotation was not verbatim; the source (p. 10) reads "without a trace of this bias in its CoT explanations". Fixed. (2) The text says "As many as 73%" of the sampled unfaithful explanations support the bias-consistent answer; the card stated 73% flatly. Fixed. (3) The card says the per-task tables and prompt listings in Appendices D-G (pp. 16-32, over half the PDF) were only skimmed, so "full_text" is changed to "partial". The relations to Nadella-post premises are the project's, not Turpin's.
