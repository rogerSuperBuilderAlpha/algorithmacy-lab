# Multi-homing across interchangeable agents collapses the coordination

## Abstract

This study applies the substitutability finding to the agent role with exact IIT-4.0 Φ. Four
pre-registered hypotheses are tested over a worker (E), agent(s) (M), and counterpart (C). Outreach
through a single agent is triadic at Φ_MIP = 2.0. When the worker and counterpart coordinate through
either of two interchangeable agents (M1∨M2), the form is dyadic. Requiring both agents (M1∧M2) keeps it
triadic at Φ_MIP = 4.0, with both agents in the irreducible core. All four hypotheses confirmed:
interchangeability of the agent collapses the coordination, the same way substitutability of a counterpart
or a platform does.

## Introduction

Q69 found that when both sides delegate, the two agents form the irreducible core. That result assumed a
specific agent on each side. Workers increasingly multi-home across interchangeable agent providers,
routing through whichever is cheapest or available. This study asks whether interchangeability of the
agent collapses the coordination, as the lab's substitutability finding predicts for other roles.

## Related work

Platform research treats multi-homing as weakening any single provider's hold
[malone1994interdisciplinary]. Costly-signaling theory notes that an interchangeable channel carries
little [spence1973job; zahavi1975mate], and the economics of spam turns on cheap interchangeable sending
[rao2012economics]. The lab's Finding 5 states that substitutability of any role collapses the triad, read
by exact integrated information [oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: the single-agent triad is triadic. H2: multi-homing across
interchangeable agents collapses the triad. H3: requiring both agents keeps it. H4: both required agents
are in the core.

## Methods

Forms over worker E, agents M (one or two), counterpart C: single (E'=M, M'=E∧C, C'=M), substitutable
(E and C read M1∨M2), required_both (E and C read M1∧M2). Each is classified by exact IIT-4.0 Φ over the
minimum-information partition (`classifier.classify_rules`) and, for H4, read on the major complex
(`probes.lib.major_complex`). The instrument is validated on a decoupled relay and a fully-coupled triad
first. Exact forms and decision rules are in `methods.md`.

## Results

The control passed (relay Φ = 0.000; triad Φ = 0.830).

**H1 (confirmed).** The single-agent form is triadic at Φ_MIP = 2.0.

**H2 (confirmed).** The substitutable form, where either of two agents suffices, is dyadic at Φ_MIP = 0.

**H3 (confirmed).** The required-both form is triadic at Φ_MIP = 4.0.

**H4 (confirmed).** The required-both major complex is {E, M1, M2, C}; both agents are in the core.

## Discussion

Interchangeability of the agent collapses the coordination. When either of two agents can carry the
outreach, no single agent is bound into the joint determination, and the form factors to dyadic, the same
structure as a broadcast. Requiring both agents keeps the coordination irreducible and puts both agents in
the core. The result completes the substitutability picture: counterpart, platform, and now agent all
collapse the triad when made interchangeable. For agent-mediated outreach it sharpens Q69's finding that
the agents can be the core: they are the core only when they are specific and required, not when they are
swappable commodities. A worker who treats agents as interchangeable has a dyadic coordination, and
algorithmacy is demanded only when a particular agent is bound into the joint determination.

## Limitations

The study is confirmatory; the predictions followed from Finding 5. Results are in-silico: Boolean models,
evidence about the models [axtell1996aligning]. Φ is read ordinally. Two interchangeable agents are
tested; larger pools follow the same disjunction structure but are untested. Hypotheses were fixed before
computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
