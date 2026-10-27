# Little, B. (2026). Length penalties make chain-of-thought less monitorable. *arXiv preprint* arXiv:2607.09786.

**Identifier:** arXiv:2607.09786 · **Read depth:** partial (preprint v4, dated 21 Sep 2026, 32 pages; locators are PDF pages. I read the nine-page body, the limitations and the reference list closely. Of the appendices, pp. 12-32, I read only E.5, the monitor validation (p. 26), and skimmed the rest: prompts, hyperparameters, per-dataset tables) · **Source-tier:** preprint, single author, not peer reviewed · **Evidence basis:** direct_read · **Design and sample:** reinforcement-learning fine-tuning of Qwen3-4B and Qwen3-14B with a length penalty targeting 60, 50, 40 and 30 percent of baseline chain-of-thought length, one run per target, plus a no-penalty RL control; 7,786 reasoning-type prompts from MMLU-Pro (4,672 train, 3,114 test) and four transfer benchmarks; nine hint types; an LLM monitor (GPT-5.4 mini) checked against human labels. A three-seed check exists only for the 30% target on one dataset (Appendix D, p. 22; not read in detail); a single-run cross-family check on Nemotron-Nano-9B-v2 is reported on p. 7 and in Table 8 · **Parties modeled:** none of the person–artefact kinds. The parties are a model trainer and an automated monitor model; no human reads a trace in the experiment · **Facets:** G · **Read:** 2026-10-13

## What it argues

Training reasoning models to think less saves inference cost, and papers in that line judge it by tokens saved and accuracy kept. Little argues this criterion "ignores monitorability, whether the trace reveals what drove the answer" (p. 1). He plants a hint that points to an answer, counts a chain as faithful only if a monitor can tell from it that the hint influenced the answer, and measures how often the model both follows the hint and says so.

The central result: at the 30% target, accuracy stays within 4.3 points of baseline and wrong-answer hints still switch answers at near-baseline rates, yet faithfulness falls on every evaluation set, "by 39% for Qwen3-14B and 35% for Qwen3-4B on MMLU-Pro-R" (p. 1). Qwen3-14B's median unhinted chain drops from 878 to 330 tokens while the monitor's catch rate falls from 71% to 51%; Qwen3-4B goes from 1,294 to 488 tokens and 60% to 48% (p. 7). Two controls carry the causal reading. The no-penalty RL control raises faithfulness in 17 of 20 settings and never lowers it by more than 1.1 points (p. 2). Randomly deleting sentences from baseline chains to the same length leaves hint mentions 7 to 35 percentage points more frequent than in the compressed models' chains, with every question-clustered interval excluding zero (Table 2, p. 8).

Little says the earlier tests found no clean effect, and calls this "the first positive result" (p. 2). The conclusion is narrow: "Safety cases that rely on chain-of-thought monitoring should therefore account for the evidence lost when models shorten their reasoning" (p. 9).

## Relation to the argument

The paper bears on the argument map's P11 (the post places its load-bearing controls outside the model) and on the post's own paragraph 9, which calls chain-of-thought transparency "not sufficient or dependable". It shows one mechanism by which evidence that the model itself writes can thin out under an optimisation pressure the party who trains the model chooses, for a reason of cost, with no change in task accuracy. That supports the post's choice to put its load-bearing controls outside the model. It does not touch the author's rulings D3 or D4 about disclosure as a literacy intervention, because no person reads anything here.

Facet check: facet G says monitoring "degrades under pressures the deployer can introduce by accident." In Little the pressure is a training objective, set by whoever fine-tunes the model, and the cost saving is deliberate; the monitorability loss is the side effect the token-accuracy criterion does not count (p. 1). It reaches a deployer only if the deployer trains. The full text bears out the abstract claims facet G recorded. The 39% and 35% figures are relative falls on MMLU-Pro-R at the 30% target, and the paper's own primary contrast is the 50% target (p. 5), which shows smaller falls (for Qwen3-14B the faithfulness score falls by 9 to 15 points, p. 2).

## In conversation with

- `korbak2025chain`: Little opens from its "useful but fragile safety channel" (p. 2).
- `baker2025monitoring`: cited for obfuscated reward hacking and the "monitorability tax" (pp. 2-3).
- `chen2025reasoning`: he adopts its switched-pair hint setup and faithfulness normalisation (pp. 2, 5).
- `turpin2023language`: source of the hint-intervention design (pp. 2, 5).
- Leads, not in the bib: Guan et al. 2025, "Monitoring monitorability" (arXiv:2512.18311), which finds monitorability correlates with chain length; Kaufmann et al. 2026 and MacDermott et al. 2025, the two prior length-penalty tests Little distinguishes from his own (p. 3); Arora and Zanette 2025, the closest precedent faithfulness audit (p. 3).
- Facet G lists `duzan2026chain`, `gema2026chain`, `wang2026monitorbench` and `jia2026faithfulness` beside Little. Little's text and reference list cite none of them.

## Caution

Two small open models (plus one single-run Nemotron-Nano-9B-v2 check), one training recipe (length-penalised group-relative RL on multiple-choice questions), 100 training steps, one run per target. Faithfulness here means that an LLM monitor detects a planted hint's role, not that a chain reveals misbehaviour, and the benchmarks are multiple-choice. At the 50% target the identification intervals include zero for every Qwen3-4B result and every wrong-answer result (p. 7). The monitor makes more false positives on short chains and more false negatives on long ones, which Little argues would understate the decline (p. 9); agreement with adjudicated human labels is κ = 0.766 on n = 248 (p. 28). No human reader appears, so the paper cannot be cited on what people can or cannot read. Preprint v4 may change.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v4 PDF (2607.09786v4, 21 Sep 2026, 32 pp.), extracted with pdftotext. I checked 7 verbatim quotations with pages, the 4.3-point accuracy bound, 878 to 330 and 1,294 to 488 tokens, 71% to 51% and 60% to 48% catch rates, 17 of 20 settings and the 1.1-point bound, 7 to 35 percentage points (stated on pp. 1, 2 and 9, Table 2 on p. 8), 7,786 prompts as 4,672 plus 3,114, GPT-5.4 mini, 100 steps, kappa 0.766 on n = 248 (p. 28), the 50% intervals including zero (p. 7), the three-seed check (p. 22), and the Guan, Kaufmann, MacDermott and Arora passages on p. 3.

**Findings:** Three changes. (1) Read depth: the card says full_text but that only E.5 of appendices pp. 12-32 was read and the rest skimmed (about two thirds of the file); changed to partial and kept the list. (2) The card says faithfulness fell '9 to 15 points in distribution for Qwen3-14B' at the 50% target; the source (p. 2) says Qwen3-14B loses under one point of accuracy in distribution and 'its faithfulness score falls by 9 to 15 points', with no 'in distribution' qualifier on the faithfulness drop; I reworded. (3) The design line omitted a single-run cross-family check on Nemotron-Nano-9B-v2 (p. 7, Table 8); I added it and qualified 'Two small open models' in the Caution. Other numbers match. The quoted 'not sufficient or dependable' is the post's wording and the facet quotation is the facet's; neither was checked against the paper.
