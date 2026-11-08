---
citekey: vaccaro2020contesting
title: "'At the End of the Day Facebook Does What It Wants': How Users Experience Contesting Algorithmic Content Moderation"
authors: "Vaccaro, Kristen and Sandvig, Christian and Karahalios, Karrie"
year: 2020
doi: 10.1145/3415238
venue: "Proceedings of the ACM on Human-Computer Interaction"
cluster: mediation-sovereignty
status: cited
role: null
used_by_sections: [5, 6]
claims: [accountability-is-a-relation, published-nulls]
read_depth: full-text
verified: crossref-verified
verified_date: 2026-08-07
source_basis: "Read in full (rr-2026-11, 2026-11-08) from the user-supplied PDF at manuscript/revision_2026-11/research/sources/vaccaro2020contesting/user_pdf/fulltext.pdf: ACM version of record, PACM HCI 4(CSCW2), Article 167, October 2020, 22 PDF pages (pp. 167:1-167:22). Identity confirmed against title, authors and DOI. Earlier basis: Crossref-verified; abstract read."
generated_run: 2026-08-08-library-build
flags: []
---

## Summary

A between-subjects online survey experiment (US sample recruited by Qualtrics to be
representative; n = 182 after cleaning) put participants in a hypothetical, incorrect Facebook
account suspension and offered no appeal or one of three appeals: written and reviewed by a
person, written and reviewed by an algorithm, or "behavioral" (change behaviour for a week, then
algorithmic re-review). Every appeal was denied, so the outcome was held unfavourable. No appeal
design improved perceived fairness, accountability, trustworthiness or control (FACT); the
no-appeal baseline scored numerically highest on all four, though not significantly. Open-ended
answers (449 participants including a validation sample) contested the goals of moderation, the
automation itself, opacity and inconsistency, not only the decision.

## Key facts / verified quotes with loci

- Design: "The between-subjects experiment compares the effects of no appeal to three types of appeals: a written appeal evaluated by a person, a written appeal evaluated by an algorithm, and one 'behavioral' appeal" (p. 167:2) [full-text]
- Outcome held constant: "our experiment tests the effect of appeals specifically when the outcome remains unfavorable; that is, the appeal does not correct the error" (p. 167:3); "In all cases users are told that their appeal was denied" (p. 167:6) [full-text]
- Result: "adding appeals (of any kind) does not significantly improve user perceptions of fairness compared to a no appeal baseline condition. In fact, while the differences are not significant, the no appeal condition performs better than all appeal types for all dependent measures" (pp. 167:10-11); Accountable M = 4.76 (no appeal) vs 4.23-4.51, F(3,163) = 2.305, p = 0.07 (Table 2, p. 167:11) [full-text]
- Human vs algorithmic reviewer made no difference: "Whether the appeal is evaluated by a person or by another algorithm does not significantly effect perceptions of FACT" (p. 167:11) [full-text]
- What users contested: the goal of moderating (n = 48), the automation of the decision (n = 125), opacity (n = 113), inconsistency (n = 84) (pp. 167:12-13); requests for human review (n = 51) and for an appeal (n = 33) (p. 167:13) [full-text]
- Fatalism: "many participants report that at the end of the day Facebook does what it wants [P106] (n=27), often suggesting that users don't influence its decisions" (p. 167:15) [full-text]
- The authors' own reading of the null: "While we believe most of the lack of effect should be attributed to poor appeal design, stronger effects might be found among communities that have experienced marginalization" (p. 167:15) [full-text]
- A structural alternative they float: "in the face of broad social criticism of social media platforms as a whole, that appeals on these platforms can never provide users the voice they need" (p. 167:16) [full-text]
- Skill matters inside appeals: they propose systems that, "Instead of prioritizing users who understand the systems better or make more experienced arguments", allow synchronous conversation or professional agents (p. 167:17) [full-text]
- *PACM HCI* 4(CSCW2), Article 167, 22 pp.; hypothetical scenario, Facebook only (pp. 167:15-16) [metadata]

## Critical notes & threats

- (rr-2026-11) The null is real but narrower than the card claimed. It is a hypothetical, single-platform survey experiment in which every appeal was denied; it shows that adding an appeal did not raise perceived accountability, not that "a grievance channel internal to the party that writes the rules absorbs the contest." All three appeals went back to Facebook, so the study cannot separate internal routing from poor design, and the authors attribute the null mainly to poor design (p. 167:15). The internal-routing reading is ours; at most it echoes their "perceived illegitimacy" explanation (p. 167:16).
- (rr-2026-11) The study does not vary competence and does not show that skill cannot create standing. Its design section implies the opposite tendency inside appeals: current systems favour "users who understand the systems better" (p. 167:17).
- (rr-2026-11) It does not test transparency. Every condition carried the same explanation of the misinformation system (§3.3.2, p. 167:7), and opacity was one of the commonest objections (n = 113, p. 167:13). It cannot support a claim about "a perfectly transparent algorithm."
- It is still the paper's best published null for appeal-as-remedy, and Martin and Waldman (2023) remains the positive counter-result the manuscript now cites.

## Support verdicts against v4 and the revision plan (rr-2026-11)

- v4 §5 (line 41): "A perfectly transparent algorithm can still replace hospitality, if no one is obliged to answer for it and no one has the power to change it (Ananny and Crawford 2018; Vaccaro et al. 2020)." PARTLY. Vaccaro shows an appeal channel without effect on the outcome did not lift perceived accountability (p. 167:11). It held explanation constant and did not test a transparent system (p. 167:7); participants called the system opaque (p. 167:13). The transparency half rests on Ananny and Crawford.
- v4 §6 (line 60): "Knowing how to file an appeal is not the same as having a right to an answer (Vaccaro et al. 2020; Are 2025)." PARTLY. Supported in spirit by the denied-appeal design and the fatalism quote (p. 167:15). Not tested: the study measures no appeal skill and no right; the authors blame design (p. 167:15).
- v4 §8 (line 86): "individual skill cannot create institutional rights, authority, or responsibility (Vaccaro et al. 2020; Are 2025)." PARTLY, weak. Vaccaro does not vary skill, and p. 167:17 says current appeals reward users who understand the system better.
- WS_B (line 81) gloss "An appeal routed back to the rule's author does not confer it" with Vaccaro [abstract: no lift]: PARTLY. True that all appeals went back to Facebook and none lifted accountability; no external-review arm exists, so the study cannot attribute the null to routing.

## Where it enters the manuscript

Sections 5 and 6. In section 5 it supports the claim that accountability is a relation no
competence reaches; in section 6 it sets the bar for the contestability affordance — an appeal
routing back to the rule's author does not confer standing.

Upgraded to full text in rr-2026-11 (2026-11-08) from user-supplied PDF: confirmed the no-lift null (Table 2, p. 167:11) but recorded that the authors blame poor appeal design (p. 167:15), that transparency and skill were never varied, and downgraded the three v4 uses to PARTLY.
