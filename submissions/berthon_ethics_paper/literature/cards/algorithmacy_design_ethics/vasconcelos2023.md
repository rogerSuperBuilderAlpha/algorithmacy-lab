# Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations can reduce overreliance on AI systems during decision-making. *Proceedings of the ACM on Human-Computer Interaction*, 7(CSCW1), Article 129, 38 pages.

**Identifier:** doi:10.1145/3579605 · arXiv:2212.06823v2 (26 Jan 2023) · **Read depth:** full_text (arXiv v2, which carries the PACM HCI running header and "129:n" pagination, so quotes below use the version-of-record page numbers) · **Source-tier:** peer-reviewed, top CSCW venue; five pre-registered crowdsourced studies · **Evidence basis:** direct_read · **Parties modeled:** human–technology (one Prolific worker and a simulated AI that names a maze exit) · **Relation last checked:** 2026-09-18

## What it argues

Overreliance is a choice, not a ceiling. The authors reframe the null results of Bansal et al. and Buçinca et al. with a cost–benefit account: a person weighs the cognitive cost of doing the task, of verifying the AI, and of simply deferring, and defers when verification is not cheaper than the task. They test it with mazes of 10 × 10, 25 × 25 and 50 × 50 cells, a simulated AI held at exactly 80% accuracy (humans 83.5% in pilots), and explanations that trace the AI's path (a highlight overlay, or the same path in words). Study 1 (N = 340): explanations left overreliance unchanged on easy and medium mazes and cut it on hard ones (Table 1; H1d confirmed, H1c not). Study 2 (N = 340 incl. 170 new): written explanations, costlier to check, did not reduce overreliance where highlights did. Study 3 (N = 286): explanations that make the wall-crossing error salient reduce it further. Study 4 (N = 114): a larger bonus for accuracy lowers overreliance. Study 5 (N = 76) adapts Cognitive Effort Discounting to show people forgo money for easier explanations and for explanations on harder tasks. "Overreliance is not an inevitability of cognition but a strategic decision where people are responsive to the costs and benefits" (129:3). The design deliberately strips trust cues — no anthropomorphism, no accuracy disclosure, no feedback during the test phase — so that only cost and benefit move.

## Relation to the argument

RQ4, structural axis. This is the most disciplined account in the cluster of *when* a person will check what an intermediary commits: only when checking is cheaper than deferring and the stakes justify the effort. That maps onto the essay's tactical limb of algorithmacy — contesting a determination has a price, and the design of the mediator sets it — and it gives the essay a lever (make verification cheap, make stakes visible) that does not depend on trust. But the intermediary here serves no one but the worker; the AI's objective is the worker's own exit, and no second human sits behind the maze. Confirmed absence of a second served party, and no purchase on the objective axis. Note also that the explanations were generated to be perfect when the AI was right and to expose the error when it was wrong (129:11), which is the opposite of a coopted mediator's explanation; the paper shows what honest seams can do, not what happens when the seam is engineered.

## Caution

Mazes on Prolific, $4 for 20 minutes, a simulated AI with scripted errors, a four-way answer to make chance-agreement 25%. The authors list the gaps: no high-stakes task, no generative or uncertain task, no practitioners, no long-term use, no imperfect explanations, and interface choices (progress bar, naming the AI, showing accuracy) that moved pilot results. They explicitly set trust aside. The result is a proof that explanations *can* work under the right cost structure, not that they do in deployed systems.

---

## S2 adversarial verification (2026-09-18)

**Verdict:** confirmed

**What I checked:** Re-downloaded arXiv 2212.06823v2 and checked the quoted sentence, all sample sizes, the 80%/83.5% accuracies, the $4/20-minute payment and the 129:11 explanation design.

**Findings:** All verbatim. The 129:11 characterisation is accurate: explanations are "accurate" when the AI is correct and trace a wall-crossing path when it is wrong. Relation section supported.
