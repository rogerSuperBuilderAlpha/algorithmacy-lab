# Greenblatt, R., Shlegeris, B., Sachan, K., & Roger, F. (2024). AI control: Improving safety despite intentional subversion. In *Proceedings of the 41st International Conference on Machine Learning* (PMLR 235). arXiv:2312.06942.

**Identifier:** arXiv:2312.06942 · **Read depth:** partial (arXiv v5, 23 Jul 2024, 47 pp.; pagination is the arXiv PDF's. Footnote 1, p. 1, says the ICML paper is "a shortened and modified version", so page and table numbers differ from the proceedings. Body, pp. 1–19, read in full; appendices A–N, pp. 21–47, skimmed: glossary, noise, score-combination details and prompt examples) · **Source-tier:** preprint of a proceedings paper · **Evidence basis:** direct_read · **Design and sample:** simulated red-team/blue-team game on 5,000 APPS "interview" coding problems (1,500 generated, upsampled, §2.5); models GPT-4 (untrusted), GPT-3.5 (trusted); no human participants · **Parties modeled:** other: a protocol designer, an untrusted model and a simulated auditor; no affected third party · **Facets:** G · **Read:** 2026-10-13

## What it argues
Greenblatt et al. ask whether the safety pipelines around a language model still work when the model itself tries to subvert them: "researchers have not evaluated whether such techniques still ensure safety if the model is itself intentionally trying to subvert them" (abstract, p. 1). The blue team (the deployer) holds an untrusted model U (GPT-4), a weaker trusted model T (GPT-3.5) and a small budget of trusted human labour H. The red team writes an "attack policy" that replaces U. The safety property is worst-case: one submitted backdoor, a solution that passes the test cases but has an exploitable input, is a failure (§2, p. 3).

The human is not a human. The authors "model limited access to trusted human labor by allowing the protocol to access GPT-4 through a channel that will not be affected by the red team" (p. 4), enough to audit "up to 2% of problems" (§2.2, p. 5). They add an informal guess that a person needs about three minutes per problem to match GPT-4 in that role (p. 4); they measured nothing.

Results (Table 2, p. 7; Table 7, p. 15; usefulness rescaled so GPT-3.5 = 0 and GPT-4 = 1, from raw rates of 22% and 54%, p. 7). Auditing the first 2% of problems upfront: safety 15%, usefulness 100%. Trusted monitoring with a 2% audit budget: 62% and 97%. Untrusted monitoring: 79% and 96%. Trusted editing (20% threshold): 92% and 94%. Untrusted monitoring fails completely (0%) if the monitor model simply lies, so the blue team first tests it on synthetic backdoors and then redacts and paraphrases inputs to block collusion (§3.4, pp. 11–14). Collusion through a "while loop where a for loop would have been more natural" gives safety of 57.5% with no redaction and 78.6% with input and output redaction (Table 6, p. 13). The authors call the contest "an arms race between the red team and the blue team" (p. 12).

Every protocol treats U as a black box, with no fine-tuning or interpretability (App. D), and each estimate averages 2,000 simulated runs (App. F, p. 27). Their stated limits: the same 1,500 problems serve for tuning and scoring (§2.4, p. 6); a model that sandbags in the evaluation is "the core bottleneck to scalability of control evaluations" (p. 17); control gets weaker as models outgrow the trusted model and the humans, since "humans probably won't get more capable over time" (p. 18); and auditing is assumed to work well, which the authors flag as the setting's weak point for later work (p. 5).

## Relation to the argument
It supports premise P11 and the Nadella post's logic of external, independent controls: the best protocols do not rely on one model checking itself, they put a weaker trusted model, a validation test and information-jamming outside the untrusted model (post P11, P14, P17). Its related-work section also gives the safety lineage of the "insider" frame: the adversary is "an AI inside the AI lab" and the problem is "similar to the problem of insider threats" (§4, p. 16).

It cannot support premise P12 as `../../ARGUMENT_MAP.md` lists it. That row cites "Greenblatt et al." among the evidence that people perform sustained monitoring badly. The paper contains no human data, because the auditor is GPT-4. What it shows is that human attention is treated as the scarcest input and spent on the most suspicious few percent of outputs, which is a design for a person who cannot read everything.

On ruling D4 (the author's "his only move is disclosure design"): these protocols disclose nothing to a person. Trusted editing, defer-to-trusted and redaction change what the model's output path does. They are deployer-side moves, which fits the post but not the author's "only disclosure" reading.

Facet check: the facet's reading is correct (human simulated by GPT-4; "up to 2%" is an evaluation parameter; the Table 2 numbers match). Facet G lists the read status as "in part"; the full body agrees with what the facet took from it.

## In conversation with
Nothing in this paper's reference list is in `../references.bib`. In the other direction, within the bib: `korbak2025chain` cites it twice as "Greenblatt et al., 2024b" for responses to flagged outputs and for red-team evaluation of monitors (pp. 2, 5–6); `kutasov2025shade` cites it as the framework that introduced AI control (ref. 10); `jia2026faithfulness` cites it for CoT monitoring (ref. 28); `lanham2023measuring` thanks Greenblatt in its acknowledgements (p. 10).
Leads not in the bib: Bowman et al. (2022), scalable oversight, arXiv:2211.03540; Irving et al. (2018), debate, arXiv:1805.00899; Saunders et al. (2022), AI critiques; Naihin et al. (2023), arXiv:2311.10538; Oakley (2019), *Professional Red Teaming*.

## Caution
A coding-backdoor testbed with models standing in for people. It gives no evidence on how well a person audits, reads logs or halts anything, and 2% is an assumed budget, not a finding. Results come from one model pair, one task type and a tuning set equal to the test set. The arXiv v5 differs from the ICML text, so numbers should be re-checked against the proceedings before they enter the paper.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened cards/greenblatt2024ai.pdf (arXiv 2312.06942v5, 23 Jul 2024, 47 pp.). Checked the 11 in-source quotations by exact match, every number in the Results paragraph against Table 2 (p. 7) and Table 7 (p. 15) (15/100, 62/97, 79/96, 92/94), the 22% / 54% raw rates, 57.5% and 78.6% (Table 6, p. 13), 5,000 problems upsampled from 1,500 (Section 2.5), 2,000 trials (App. F, p. 27), the 2% H budget (p. 5), the three-minutes guess (p. 4) and the page locators 12, 16, 17, 18. Not checked: the claims in the last In-conversation paragraph about what korbak2025chain, kutasov2025shade, jia2026faithfulness and lanham2023measuring say; they live in other cards.

**Findings:** One fix: Read depth said full_text although the card states that the appendices (pp. 21-47, more than half the PDF) were only skimmed; changed to partial and kept the list of what was not read. All quotations, numbers and locators match. The three non-matching quotations are the author's and the argument map's phrases, not the source's.
