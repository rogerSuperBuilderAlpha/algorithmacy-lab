# Asynchronous update: the verdict survives, the magnitude falls

## Abstract

The program computes every verdict under synchronous update. This study recomputes the keystone outreach
forms under asynchronous update, modelled as a stochastic transition where one element acts each step and
the others hold, with exact IIT-4.0 Φ. Four pre-registered hypotheses are tested. The read-recipient triad
stays triadic (Φ falls from 2.0 to 0.25), the broadcast stays dyadic (Φ=0), and the all-required campaign
stays triadic (Φ falls from 3.0 to 0.20). The verdict is preserved for every keystone. All four hypotheses
confirmed: synchronicity is not load-bearing for the dyadic/triadic verdict.

## Introduction

Real coordination is asynchronous. The program's verdicts assume simultaneous action, and a result that
held only under that assumption would be an artifact. This study varies the update scheme and reads the
verdict.

## Related work

Integrated information is computed from a transition matrix [oizumi2014phenomenology; albantakis2023iit4;
mayner2018pyphi]; asynchronous update is a different, stochastic matrix on the same elements. Coordination
unfolds in time [malone1994interdisciplinary]; the framing carries from Q63-Q79 [rao2012economics;
hancock2020aimc].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: read_recipient stays triadic. H2: broadcast stays dyadic.
H3: all_required stays triadic. H4: the verdict is preserved for every keystone.

## Methods

Asynchronous update is the stochastic TPM P(j'=1) = (1/n)·f_j(state) + (1−1/n)·current_j. Synchronous
verdicts from `classifier.classify_rules`; asynchronous max-Φ from `probes.lib.max_phi_float`. Keystones:
read_recipient, broadcast, all_required. Decision rules are in `methods.md`.

## Results

read_recipient: synchronous triadic Φ=2.0, asynchronous triadic Φ=0.25. broadcast: dyadic at Φ=0 in both.
all_required: synchronous triadic Φ=3.0, asynchronous triadic Φ=0.20. Every keystone's verdict is
preserved. H1 through H4 confirmed.

## Discussion

The dyadic/triadic verdict is a property of the coordination structure, not of synchronous timing. Under
asynchronous update the triadic forms stay triadic and the broadcast stays dyadic; only the magnitude of Φ
falls, because acting one element at a time integrates less than acting all at once. This removes a
modelling worry: the outreach law does not depend on sender, agent, and recipient acting simultaneously,
which they never do. The fall in magnitude reinforces that Φ is read ordinally; under a realistic update
scheme the absolute numbers shrink while the line between dyadic and triadic holds.

## Limitations

The study is confirmatory. Results are in-silico under one asynchronous model, uniform one-element-per-step
[axtell1996aligning]; block or ordered schedules are untested. Only the binary verdict is robust; the
magnitude is not. Hypotheses were fixed before computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
