# Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations can reduce overreliance on AI systems during decision-making. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW1), Article 129.

**Identifier:** doi:10.1145/3579605 · arXiv:2212.06823 · **Read depth:** full_text (arXiv v2 of 26 Jan 2023; the PDF carries the journal's article layout and page headers "129:1" to "129:38", and the locators below use those; the appendix with the model specification and survey items is not in this PDF's text and was not read) · **Source-tier:** peer-reviewed proceedings article · **Evidence basis:** direct_read · **Design and sample:** five online experiments with a simulated AI in a maze task (four possible exits, AI accuracy fixed at 80%); Prolific workers, N = 731 across studies (340, 340, 286, 114, 76; the studies share some participants, so the five figures do not sum to 731); Bayesian mixed-effects models; Studies 1, 2, 4 and 5 pre-registered, Study 3 exploratory · **Parties modeled:** person–system (one human, one AI aid) · **Facets:** X · **Read:** 2026-10-13

## What it argues
Earlier XAI studies found that explanations do not cut overreliance, defined as accepting an incorrect AI prediction (Section 1, p. 129:2). Vasconcelos and colleagues argue that people "strategically choose" whether to engage with an explanation, so the null results may come from a narrow band of task and explanation costs (Abstract; Section 3, p. 129:5–6). They set out a cost-benefit framework: people weigh the effort and payoff of engaging with the task (doing it alone, or verifying the AI) against the effortless strategy of relying on the AI. Five predictions follow (pp. 129:6–7).

Results, all in maze trials with exact designs on pp. 129:12–27:
- Study 1 (N = 340): in the prediction-only condition, overreliance rises from easy (10×10 maze) to medium (25×25) (estimate −3.97, 95% CI −5.48 to −2.53). A highlighted-path explanation changes nothing in the easy task (0.16, CI −1.68 to 2.17) or, unexpectedly, the medium task (0.92, CI −0.31 to 2.08). It lowers overreliance in the hard task, 50×50 (1.74, CI 0.89 to 2.76) (Table 1, p. 129:15). The authors do not state the units of these estimates; the PDF gives no percentages for them in text.
- Study 2 (N = 340): a written step list ("left, up, right...") is harder to check than the highlight and yields more overreliance in the medium task (−1.63) and hard task (−1.63) (Table 3, p. 129:18). Written explanations did not differ from prediction only (p. 129:18).
- Study 3 (exploratory, N = 286; 31 new participants): a "salient" explanation that colours the path blue after it crosses a wall averaged 0% overreliance, "people are unlikely to agree with an AI if they know it is incorrect" (Section 7.6, p. 129:21).
- Study 4 (N = 114): a $0.50 bonus per correct maze against $0.01 lowers overreliance (0.93, CI 0.41 to 1.46); the explanation effect replicates (Table 5, p. 129:23).
- Study 5 (N = 76, Cognitive Effort Discounting): people give up more reward to use an AI with explanations in a harder task (16.96, CI 5.22 to 28.7) and with highlight over written explanations (18.61, CI 9.51 to 27.79) (Table 6, p. 129:27).

Their conclusion: "overreliance is not merely an immutable inevitability of cognition but at least, in part, a strategic choice" (Section 11, p. 129:32).

## Relation to the argument
The paper bears on P9 and on the objection the facet file calls objection 8, that "take the work off the person" is not a general principle. It complicates P9 more than it rescues it. Cost-lowering works here only where the explanation re-represents the check: a highlighted path laid on the maze turns "solve the maze to see if the AI is right" into a glance. A written path, the same information in a form that costs more to parse, does nothing (Study 2). That matches P5 (the same content, a different form, carries the work) and gives the author a controlled case outside the history of writing. It cuts the other way on the "gives the person something to read" half of P9: the same paper shows that a read-this aid can reduce errors, but only when it is cheaper than the task and only in the hard condition. The medium task showed no effect (H1c not supported).

It also supports the paper's point that a remedy's form decides who benefits. But every design here keeps the person in the dyad as the checker; no condition removes the check. That fits Nadella's remedy (a person reading evidence, premise P11 of the argument map) as well as the author's. It is a person–AI dyad, with no counterpart party and no owner whose interest differs (P10).

Facet check: the facet file read the abstract only. Its gloss, that cost-lowering helps "when it makes verification cheaper than doing the task", is borne out by Study 1 and Study 2, with two additions the abstract lacks: the effect appeared only in the hard task, and a harder-to-check explanation did no better than no explanation.

## In conversation with
- `bucinca2021trust` (Buçinca et al. 2021, ref. 9): the forcing-function study. Vasconcelos reads forcing functions as a cost manipulation and suggests they raise the cost of relying on the AI (Section 2.1; Section 10.3).
- Bansal et al. 2021 (ref. 4, arXiv:2006.14779; not in the bib): the study whose null result the authors attribute to an easy task and a costly logical explanation (Section 10.2, p. 129:28). The bib's `bansal2019updates` is a different Bansal paper and is not cited here.
- Leads not in the bib: Kool & Botvinick 2018, "Mental labour"; Johnson & Payne 1985, effort and accuracy; Green & Chen 2019 on algorithm-in-the-loop decisions; Jacobs et al. 2021, clinicians lacking time for explanations.

## Caution
Maze task, crowdworkers, a simulated AI and "perfect" explanations; the authors say high-stakes, generative, uncertain and long-term settings are untested (Section 10.4, pp. 129:29–31). Tables give posterior means without stated units, so no effect should be quoted as a percentage-point change from this text. Study 3 added 31 participants and had no pre-registration. The medium-task hypothesis failed. The paper never measures a task re-representation in the author's sense; the reading of the highlight as a re-representation is the card's, not the authors'.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the arXiv v2 PDF with the journal layout (Article 129, 38 pages), extracted with pdftotext. Checked 3 verbatim quotations (all exact), the Table 1, 3, 5 and 6 values, all N figures (340, 340, 286 with 31 new, 114, 76, 731), pre-registration status, and the Bansal/Buçinca relations against Section 10.2-10.3 and the reference list.

**Findings:** One locator error fixed: the Study 3 'salient explanation averaged 0% overreliance' passage (Section 7.6) is on p. 129:21, not 129:20. Everything else matched. Card's read-depth statement about the unread appendix is honest (the PDF text ends with the references/pre-registration notes). Bansal et al. 2021 ref 4 appears in the text as [4].
