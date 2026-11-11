---
citekey: hatherley2025moving
title: "A Moving Target in AI-Assisted Decision-Making: Dataset Shift, Model Updating, and the Problem of Update Opacity"
authors: "Hatherley, Joshua"
year: 2025
doi: 10.1007/s10676-025-09829-2
venue: "Ethics and Information Technology"
cluster: ai-automation
status: cited
role: evidence
used_by_sections: [4, 6]
claims: [integrating-conditions, affordances-derived]
read_depth: full-text
verified: verified
verified_date: 2026-11-08
source_basis: "Full text read 2026-11-08 from the user-supplied PDF (sources/hatherley2025moving/user_pdf/fulltext.pdf): Springer version of record, open access, Ethics Inf Technol (2025) 27:20, accepted 20 Mar 2025, published online 4 Apr 2025; 15 PDF pages (14 article pages 'Page n of 14' plus a licence page). Title, author and DOI match the card and Crossref. Locators are the article's printed page numbers. Earlier record: Springer article-page abstract."
generated_run: 2026-08-11-p9
flags: []
hold_rationale: "Held for section 4 paragraph 2 and section 6 paragraph 3. Load-bearing: it supplies a name the argument has been describing without one."
---
## Summary

Argues that model updating, the usual remedy for performance decline under dataset shift,
introduces "update opacity": expert users cannot say why the current version of a model gives a
different output from a previous version for the same input. Updates disrupt the mental models
users build through repeated use, causing post-update performance drops. Standard black-box
remedies (explainability, model reporting, validation) are poorly equipped for it; bi-factual
explanations, dynamic model reporting and update compatibility each have limits. The setting is
clinical decision support.

## Key facts / verified quotes with loci

- Definition: "Update opacity occurs when expert humans cannot, upon inspection, say why, in general, the current version of a model predicts an output (y) as a result of an input (x), while a previous version of the model predicts a different output (z), as a result of x." (p. 7) [full-text]
- Distinct from static opacity: "inference opacity is static and atemporal ... In contrast, update opacity is dynamic and temporal" (p. 7) [full-text]
- Learned knowledge depreciates: "Human users learn when it is appropriate to rely on the outputs of ML systems by developing mental models of these systems through repeated interactions with them" ... "model updates have been found to disrupt users' mental models of ML systems, resulting in precipitous drops in the performance and accuracy of human-ML teams" (p. 5) [full-text]
- "Once the model is updated, however, these expectations may be undermined, and the user's mental model may become outdated." (p. 7) [full-text]
- Recalibration slowed: update opacity "may interfere with users' capacity to maintain reliable and up-to-date mental models of ML systems that undergo model updates" (p. 8) [full-text]
- Announcing changes is a weak fix: under dynamic model reporting "users are informed about changes that have occurred to the model after each update" (p. 10), but "The provision of such information may not reduce the epistemic or safety risks of update opacity since it does not appear to address this type of opacity directly." (p. 11) [full-text]
- Conclusion: standard strategies "are poorly equipped to address the problem of update opacity"; "Prioritising interpretable AI systems over their black box counterparts in high-stakes environments may often be the most optimal available solution at present." (p. 12) [full-text]

## Critical notes & threats

The full text supports the "moving target" image and the depreciation of learned skill, in a clinical setting with expert users. It does not support two things v4 attaches to it. One is the forecasting asymmetry. The other is the idea that the harm is *silence*. Hatherley's problem is that users cannot understand *how and why* the reasoning changed. He argues that simply informing users of changes (update cards) "may not reduce" the risk (p. 11). v4's third interface principle ("make significant rule changes visible") therefore cites a source that doubts visibility is enough. The principle can stand, since announced change is better than silent change, but it should not imply that Hatherley recommends it.

Support verdicts (v4):

- §5 (line 39): predictability "goes one-sided when the system can forecast the guest ever better while the rules they are subject to change without warning (Hatherley 2025)." **PARTLY.** Rules that change and leave users' models outdated: supported (pp. 5, 7–8). "Forecast the guest ever better": not in Hatherley. "Without warning": his concern is unintelligible change, not unannounced change (p. 11).
- §6 (line 59): "the skill the employee lends is a moving target: when a system quietly revises its rules or categories, the hard-won knowledge depreciates overnight, and no one tells the employee or the guest it has happened (Hatherley 2025)." **PARTLY.** Depreciation of hard-won mental models after updates: supported (pp. 5, 7, 8). "Overnight" is reasonable for "precipitous drops" (p. 5). "No one tells" is the authors' addition; Hatherley's users may well be told and still not understand (pp. 10–11). His users are clinicians, not front-desk staff.
- §7 (line 65): "make significant rule changes visible, because when rules move in silence the knowledge guests and staff have built becomes a moving target (Hatherley 2025)." **PARTLY.** The moving target is supported (pp. 5, 7). The remedy is not Hatherley's: he judges reporting changes insufficient (p. 11) and prefers interpretable systems (p. 12).
- Card's earlier note, "a system can be fully explained today and silently different tomorrow, and transparency does not catch the difference": **SUPPORTED** in substance (static vs temporal opacity, p. 7; black-box remedies "poorly equipped", p. 12).

## Where it enters the manuscript

v4 §5 (predictability), §6 (the lent skill as a moving target), §7 (third interface principle). Suggested wording fixes are in the report; drop "forecast the guest" from the citation's scope, and do not cite Hatherley as recommending visibility.

Upgraded to full text in rr-2026-11 (2026-11-08) from user-supplied PDF: update opacity defined (p. 7); mental-model depreciation supports the moving target (p. 5); all three v4 uses PARTLY, because Hatherley judges announcing updates insufficient (p. 11) and says nothing about forecasting users.

Fable-checked rr-2026-11 (2026-11-08): verifier_3 PASS accepted; p. 11 'may not reduce the epistemic or safety risks' and p. 12 'poorly equipped' confirmed against the full text in sources/; all three PARTLY verdicts stand; references.bib now carries issue 2 (27(2), art. 20); no card change.
