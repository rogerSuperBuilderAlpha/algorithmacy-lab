---
citekey: kulesza2015principles
title: "Principles of Explanatory Debugging to Personalize Interactive Machine Learning"
authors: Kulesza, Todd and Burnett, Margaret and Wong, Weng-Keen and Stumpf, Simone
year: 2015
type: article
doi: 10.1145/2678025.2701399
venue: Proceedings of the 20th International Conference on Intelligent User Interfaces (IUI '15), pp. 126-137
source_basis: full-text
pages_read: "all (accepted manuscript, 11 pp.; manuscript pagination)"
source_url: https://openaccess.city.ac.uk/id/eprint/13819/1/paper326.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/V5/kulesza2015.pdf
sha256: 92b1d18794b32380370650dfcfdf956ff02014bc0e8f4f35b172c5ce8e4916ca
manuscript_lines: []
ledger_rows: []
verified: corrected
written: 2026-10-14
---

## Summary
Kulesza and colleagues ask how end users can efficiently steer the predictions a machine-learning system makes on
their behalf. Their answer, Explanatory Debugging, is a two-way loop: the system explains why it made each
prediction, and the user explains corrections back, which the system honours (p. 1). Their earlier work had
"relied on human instructors to help participants build useful mental models" (p. 2); this paper builds that help
into the system. The principles are grouped under "Explainability" (be sound, be complete, but don't overwhelm)
and "Correctability" (be actionable, be reversible, always honour user feedback, incremental changes matter)
(pp. 2-3). A prototype, EluciDebug, is an email-style text classifier. In a between-subjects study, 77 people with
no more than introductory programming used either the full prototype or a black-box version that only accepted
labels, for 30 minutes on a hockey/baseball task (p. 7). Treatment participants scored 52% higher on a mental-model
test, their feedback was worth about two of the control group's, mental-model scores correlated with classifier
quality, and workload did not rise (pp. 8-10).

## Key facts it relies on
- "the system explains the reasons for its predictions to its end user, who in turn explains corrections back"
  (p. 1).
- The earlier study "relied on human instructors to help participants build useful mental models" (p. 2).
- Principles 1.1-1.3 (sound, complete, don't overwhelm) and 2.1-2.4 (actionable, reversible, honour feedback,
  incremental changes) (pp. 2-3).
- 77 participants (27 women, 50 men), 37 control and 40 treatment; no one with more than introductory programming
  (p. 7).
- Treatment "scored 52% higher on the mental model assessment than control participants (W = 259, p < .001)"
  (p. 9).
- Spearman's rho between mental-model score and classifier F1: .282, p = .013 (p. 10).
- No difference in NASA-TLX workload between conditions (p. 9).
- Conclusion: the loop "resulted in smarter users and smarter learning systems" (p. 10).

## Critical notes from the literature
- The user owns the classifier and its goal; no party with diverging interests is modelled (`V5_scaffolding.md`,
  Q2).
- Thirty minutes in a lab with a toy task; durability of the gain was not tested, so it cannot show fading or
  later independent competence in Belland's (2017) sense.
- The accepted manuscript may differ from the proceedings version; page numbers here are the manuscript's.

## Key topics covered
explanatory debugging, interactive machine learning, mental models, end-user personalisation, explanation soundness and completeness, correctability, user study

## Where the manuscript uses it
- v4 (not yet drafted): proposed use — a measured case in which a system replaces the human tutor and scaffolds
  novices' understanding through a two-way loop rather than a text to read (pp. 1-2, 9-10). narrower: the replacement of human instructors (p. 2) and the
  mental-model gain (p. 9) hold, but the explanations never fade and durability was not tested, so this is
  scaffolding only in a loose sense, not Belland's (2017, p. 18).
- v4 (not yet drafted): proposed use — the limit: the case assumes a system that serves only its user (p. 1);
  the insider post's systems act on people for a deploying firm. holds: the scenario is a user personalising her
  own email classifier (p. 1); the paper implies the assumption rather than stating it.

## Verifier notes
- 2026-10-14. sha256 matches. Re-extracted (no-layout mode; layout mode breaks the columns). All quotations exact.
- Corrected: every page reference was one too high. The eprint PDF has a City Research Online cover sheet, so
  manuscript page = PDF page - 1 (footers confirm: PDF p. 3 prints "2"). The card claimed manuscript pagination
  but gave PDF pages. Now: loop p. 1, "relied on human instructors" p. 2, principles pp. 2-3, participants p. 7,
  "52% higher ... (W = 259, p < .001)" and NASA-TLX p. 9, rho = .282 and "smarter users and smarter learning
  systems" p. 10.
- Participants: the source says "27 females, 50 males", 37 control and 40 treatment, nobody past an introductory
  course, 30 minutes (p. 7); the card paraphrases, which is fine. Feedback "twice as efficient" (p. 8).
- Verdicts added: use 1 narrower, use 2 holds. Crossref matches V5 bib (IUI '15, pp. 126-137).
