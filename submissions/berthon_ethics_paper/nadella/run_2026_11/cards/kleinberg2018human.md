---
citekey: kleinberg2018human
title: Human Decisions and Machine Predictions
authors: Kleinberg, Jon; Lakkaraju, Himabindu; Leskovec, Jure; Ludwig, Jens; Mullainathan, Sendhil
year: 2018
doi: 10.1093/qje/qjx032
source_basis: partial-text
pages_read: NBER WP 23180 (Feb 2017) cover and abstract (pdf pp. 1-2), introduction pp. 3-9 and conclusion pp. 40-41; the QJE version of record was not opened
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B5/kleinberg2018human/kleinberg2018human.pdf
sha256: 7246f61d266c5228eb98a7fd84a7e08c2250c5819d9c0316a5322cf22d82a21e
verified: corrected
structure_sections: 6-automation; 4.4-stop; counter
type: article
venue: Quarterly Journal of Economics 133(1), 237-293
source_url: https://www.nber.org/system/files/working_papers/w23180/w23180.pdf
record_check: crossref https://api.crossref.org/works/10.1093/qje/qjx032
facet: B5
supersedes: none
written: 2026-11-18
---

## Summary

Read: the cover, abstract, introduction (pp. 3-9) and conclusion (pp. 40-41) of the NBER working paper of February 2017, not the QJE version of
record (issued online 26 Aug 2017, vol. 133(1), 2018); figures may differ in the final version, and the working paper
is not peer-reviewed. Using New York City pretrial release data, the authors train a machine-learning model to predict
flight risk and compare simulated release rules with judges' actual decisions. In the New York data "crime" means
failure to appear in court (p. 3 n. 4). At the judges' release rate the
algorithm could cut crime by about a quarter; at the judges' crime rate it could jail about two-fifths fewer people,
while also reducing racial disparities in jail and cutting all crime categories. A "predicted judge" model outperforms
the actual judges, which they read as judges responding to noise rather than private information. A national dataset
gives a qualitatively similar but smaller gain. The authors stress the limits: selection on observables, the narrow
payoff function that makes bail (not sentencing) suitable, and that the numbers do not propose algorithms making the
decisions.

## Key facts it relies on

- p. 6: "at the same release rate as what the judges currently choose, the algorithm could produce 24.7% fewer crimes. Second, to produce the same crime rate as judges currently do, the algorithm could jail 41.8% fewer people." [quote] The working paper's own abstract (pdf p. 2) gives "up to 24.8%" and "42.0%", and its conclusion (p. 40) gives 25% and "over 40%"; the pages read do not say why the abstract's figures differ from p. 6. [paraphrase]
- p. 3 n. 4: under New York law judges at bail hearings are to consider flight risk only, and the authors use the term crime "to refer to failure to appear in the New York data, and to either failure to appear or re-arrest in the national data." [quote]
- p. 6: "An appropriately done re-ranking policy can reduce crime and jail populations while simultaneously reducing racial disparities. In this case, the algorithm is a force for racial equity." [quote]
- p. 6: "these calculations rely on a strong ‘selection on observables’ assumption; unobservable variables seen by judges could bias our results." [quote]
- p. 6 n. 9: "These numbers are not meant to suggest a policy in which algorithms actually make these decisions. Surely in practice they would be used instead as decision aids". [quote]
- p. 7: on the predicted-judge test, the unobserved variables "are not a source of private information so much as a source of mis-prediction. The unobservables create noise, not signal." [quote]
- pp. 7-8: national data (151,461 felony defendants, 40 urban counties, 1990-2009): crime down 18.8% at constant release, or 24.5% fewer jailed at constant crime. [paraphrase]
- p. 8: "It would be foolish to conclude that we can improve on sentencing decisions simply because we predicted recidivism." The authors "chose bail explicitly because these omitted payoff biases are specific and narrow in scope." [quote]

## Critical notes

- Contested: no critic was opened in this run. The authors themselves name the selective-labels problem (outcomes observed only for those released, p. 9) and address it with quasi-random judge assignment (abstract, pdf p. 2; pp. 4-6, 9). Critics of pretrial risk tools are not carded here; none was opened in this run.
- Limits for the paper's use: a prediction task with a narrow payoff and an outcome that can be observed; nothing on customer-service, refund or LLM agents. The comparison is algorithm versus judge; it says nothing about who holds the record or the brake.
- Strongest use against the paper (the card's inference; the authors write of judges and bail, and of algorithms as "decision aids", p. 6 n. 9): where an agent replaces a human who decides noisily and unequally, the person acted on may get a less arbitrary and less discriminatory decision, so the "gate" held by an agent may be better for her than the gate held by an official (STRUCTURE 6, automation objection).
- Person acted on gets: record — no (not addressed); brake — no (not addressed); envelope — no; standing — no; loss cover — no. What she may get is a less noisy decision (p. 7), which is outside the five goods.
- Corrected by V-B-1: locator for the quasi-random judge assignment changed from "p. 6, n. 10" to "abstract, pdf p. 2; p. 6"; n. 10 lists other confounds (capacity, timing, money bail) and does not mention quasi-random assignment.
- Corrected by the Fable read (V-B-1): `pages_read` and the basis sentence now name the pages opened (pp. 1-9, 40-41); the introduction begins on p. 3, not p. 6. Added p. 3 n. 4, because the headline "24.7% fewer crimes" counts failures to appear in the New York data. "An internal inconsistency in this copy" reworded to report the three sets of figures without judging them (the abstract says "up to"). "The standard objection" rested on no source opened and now reports the authors' own statement of the selective-labels problem. The "strongest use" note is marked as the card's inference.
