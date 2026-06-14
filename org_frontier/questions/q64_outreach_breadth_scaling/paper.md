# Outreach breadth scaling: an all-binding campaign stays triadic at Φ = n−1

## Abstract

Q63 found single-recipient agent-mediated outreach triadic when the agent binds sender intent and a live
recipient into one joint determination. This study scales the recipient count. Five pre-registered
hypotheses are tested with exact IIT-4.0 Φ. An all-required campaign, where the agent's commit conjoins
the sender and every recipient, stays triadic as recipients grow from one to four (n = 3 to 6), with
Φ_MIP = n − 1 (2.0, 3.0, 4.0, 5.0), reproducing the conjunctive-hub law in the outreach frame, and every
recipient sits in the irreducible core. A pooled broadcast that ignores recipients and a substitutable
campaign where any recipient can be swapped are both dyadic at every breadth, and a single substitutable
recipient inside an otherwise all-binding campaign collapses the whole form. All five hypotheses were
confirmed. Breadth carries no verdict on its own; the joint determination does.

## Introduction

Outreach scales by adding recipients. Practice ranges from a pooled broadcast, sent to everyone at near
zero marginal cost [rao2012economics], through audience segmentation, to a message determined per
recipient. The structural question is which of these stays an irreducible three-party coordination as the
audience grows, and which factor into a sender broadcasting through a channel. Q63 established the
single-recipient verdict; this study reads the verdict from one recipient to four. The lab's
conjunctive-hub law predicts the answer for an all-binding campaign: a mediator that commits the
conjunction of all parties stays triadic at Φ = n − 1.

## Related work

The economics of spam explains pooled broadcast: free sending makes undifferentiated mass outreach
rational [rao2012economics]. Costly-signaling theory says the cost of a genuinely tailored message rises
with the audience while a broadcast's does not [spence1973job; zahavi1975mate; grafen1990biological].
AI-mediated communication studies the agent that generates messages on a person's behalf
[hancock2020aimc; jakesch2019aimc], and coordination theory treats the mediator as part of the structure
[malone1994interdisciplinary]. The structural reading uses exact integrated information
[albantakis2023iit4; oizumi2014phenomenology; mayner2018pyphi].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: an all-required campaign is triadic at Φ = n − 1 for
k = 1..4. H2: a substitutable campaign is dyadic at every breadth. H3: a pooled broadcast is dyadic at
every breadth. H4: one substitutable recipient collapses an otherwise all-required campaign. H5: every
recipient sits in the core of an all-required campaign.

## Methods

Parties are Boolean elements: sender intent (E), agent/mediator (M), recipients (R1..Rk). The agent's
commit is M's rule; each recipient reads the agent (Ri'=M) so it stays live. Forms are classified by
exact IIT-4.0 Φ over the minimum-information partition (`classifier.classify_rules`) and read on the
maximal complex (`probes.lib.major_complex`) for H5. Every probe validates the instrument on a decoupled
relay (dyadic, Φ = 0) and a fully-coupled triad (triadic, Φ = 0.83) first. Exact forms and decision rules
are in `methods.md`.

## Results

The control passed in all five probes (relay Φ = 0.000; triad Φ = 0.830).

**H1 (confirmed).** The all-required campaign (M'=E∧R1∧…∧Rk) is triadic for k = 1, 2, 3, 4, with
Φ_MIP = 2.0, 3.0, 4.0, 5.0, exactly n − 1. The conjunctive-hub law holds in the outreach frame, and
breadth does not dilute an all-binding campaign.

**H2 (confirmed).** The substitutable campaign (M'=E∧(R1∨…∨Rk)) is dyadic (Φ_MIP = 0) at k = 2, 3, 4.

**H3 (confirmed).** The pooled broadcast (M'=E) is dyadic (Φ_MIP = 0) at k = 2, 3, 4.

**H4 (confirmed).** At k = 3, the mixed campaign with one substitutable pair (M'=E∧R1∧(R2∨R3)) is dyadic,
while the fully all-required campaign is triadic at Φ_MIP = 4.0. One swappable recipient collapses the
whole form.

**H5 (confirmed).** The major complex of the all-required campaign is the full party set: {E, M, R1, R2}
at k = 2 (Φ = 3.0) and {E, M, R1, R2, R3} at k = 3 (Φ = 4.0). No recipient is excluded.

## Discussion

Breadth is not the variable. An all-binding campaign stays triadic at every breadth tested, with Φ = n − 1
and every recipient in the core, while a pooled broadcast and a substitutable campaign factor at every
breadth. The result sharpens the Q63 law for the multi-recipient case: outreach to many demands
algorithmacy exactly when the agent binds the sender and all recipients into one irreducible joint
determination, and the moment any recipient becomes swappable the form collapses to dyadic. The cost
intuition carries over: an all-binding campaign's per-recipient determination is the work whose cost
scales with the audience, while the pooled and substitutable forms that cost little also factor.

## Limitations

The study is confirmatory; all five predictions followed from the conjunctive-hub law and the
substitutability finding, and none was refuted, so the contribution is the explicit breadth verdicts.
Results are in-silico: Boolean models, evidence about the models, not real campaigns [axtell1996aligning].
Φ magnitude is encoding-dependent, so the n − 1 pattern is a structural signature rather than a difficulty
scale. The study scales the all-binding campaign, which escapes breadth dilution by construction; whether
randomly-wired multi-recipient outreach dilutes with breadth as the random mediation family does is left
open. Hypotheses were fixed before computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
