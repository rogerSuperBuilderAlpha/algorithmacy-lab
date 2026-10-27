---
citekey: vasconcelos2023explanations
title: "Explanations Can Reduce Overreliance on AI Systems During Decision-Making"
authors: Vasconcelos, Helena and Jörke, Matthew and Grunde-McLaughlin, Madeleine and Gerstenberg, Tobias and Bernstein, Michael S. and Krishna, Ranjay
year: 2023
type: article
doi: 10.1145/3579605
venue: Proceedings of the ACM on Human-Computer Interaction 7(CSCW1), Article 129, 1-38
source_basis: full-text
pages_read: "pp. 129:1, 129:11, 129:15, 129:17-129:21, 129:27, 129:32 located this session; full read recorded on the S2-verified sister card"
source_url: https://arxiv.org/abs/2212.06823
local_path: /Users/ludwitt/iit-playground/dxd_foundation_local/pdfs/cards/vasconcelos2023explanations.pdf
sha256: a3e3e19b701043b86ab407ec0b279d9a1f303a874f38458580ba41013be0c15d
manuscript_lines: []
ledger_rows: []
verified: corrected
written: 2026-10-14
---

## Summary
Earlier studies found that explanations do not reduce overreliance on AI, defined as accepting an incorrect AI prediction (p. 129:12). Vasconcelos and colleagues argue that "people strategically choose whether or not to engage with an AI explanation" (p. 129:1), weighing the cost of checking against the cost of doing the task, and test this in five online experiments (Prolific, N = 731 in all) with a simulated AI of fixed 80% accuracy solving mazes. A highlighted-path explanation lowered overreliance only in the hard maze (posterior estimate 1.74, 95% CI 0.889 to 2.76; easy and medium not supported, p. 129:15). A written step-list ("left, up, right, up...") carrying the same path, which costs more to check, showed "no difference between the prediction only case and the hard-to-understand, written explanation case" across difficulties (p. 129:18). A "salient" explanation that marked where the AI's path crossed a wall averaged 0% overreliance (exploratory Study 3, p. 129:21). Larger bonuses lowered overreliance (Study 4), and people valued explanations more in harder tasks (Study 5). Conclusion: "overreliance is not merely an immutable inevitability of cognition but at least, in part, a strategic choice" (p. 129:32). Read as the arXiv v2 with the journal's article layout.

## Key facts it relies on
- p. 129:1: "people strategically choose whether or not to engage with an AI explanation, demonstrating empirically that there are scenarios where AI explanations reduce overreliance."
- p. 129:11: written explanations translate the path into words ("left, up, right, up..."), which increases the cost of engaging.
- p. 129:12: overreliance is "the percentage of decisions when a human decision maker accepts an AI's incorrect prediction".
- p. 129:15: hard task, prediction vs explanation, 1.74 (95% CI 0.889 to 2.76), hypothesis supported; medium task not supported.
- p. 129:18: across all difficulties, "no difference between the prediction only case and the hard-to-understand, written explanation case."
- p. 129:21: the salient explanation condition "has an average overreliance rate of 0%"; "people are unlikely to agree with an AI if they know it is incorrect."
- p. 129:32: "overreliance is not merely an immutable inevitability of cognition but at least, in part, a strategic choice."

## Critical notes from the literature
- The sister card (`wt-dxd-foundation/submissions/dxd_foundation/literature/library/vasconcelos2023explanations.md`, S2: corrected) notes the tables give posterior estimates without stated units, so no effect should be quoted as a percentage-point change; Study 3 was exploratory and not pre-registered; the medium-task hypothesis failed.
- Maze task with crowdworkers and "perfect" explanations; the authors say high-stakes and long-term settings are untested (§10.4, per the sister card).
- Buçinca et al. (2021) and Bansal et al. (2021) report the null or adverse results this paper responds to (sister cards).

## Key topics covered
Explainable AI, overreliance, cost-benefit framework, verification cost, task difficulty, written versus visual explanations, monetary incentives, cognitive effort discounting

## Where the manuscript uses it
- v4 (not yet drafted): proposed use against an overstated thesis — some explanations reduce overreliance (pp. 129:15, 129:21), so the paper should not say disclosure never helps. Holds; note the highlight explanation helped only in the hard maze (p. 129:15) and the 0% salient result is exploratory (p. 129:21).
- v4 (not yet drafted): proposed use for wrong (b) — the same path written as text did nothing while a visual highlight helped (pp. 129:15, 129:18): the form of the disclosure, not its content, decided the effect. Narrower: the highlight helped only in the hard maze (p. 129:15); the written-versus-prediction "no difference" result comes from exploratory analyses (p. 129:18); the authors explain it as the cost of engaging with the explanation, not form as such.

## Verifier notes
- 2026-10-14. sha256 matches (arXiv v2, 38 pp., with 129:n running heads). Crossref 10.1145/3579605 confirms PACM HCI 7(CSCW1), pp. 1-38, 2023, and the six authors.
- Exact-checked every Key-facts quotation and number (129:1, 129:11, 129:12, 129:15 = 1.74 [0.889, 2.76], 129:18, 129:21, 129:32; N = 731; 80% accuracy). All pass.
- Corrected use 2 to narrower. The highlight helped only in the hard maze, and the written-versus-prediction "no difference" result is exploratory. Use 1 holds, with those limits noted.
- Bib: agrees with the V4 facet .bib.
