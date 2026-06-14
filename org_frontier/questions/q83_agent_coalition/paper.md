# A recipient-side gating coalition keeps a size-three core; only one of two required agents enters

## Abstract

This study builds a coalition of two recipient-side gating agents over the outreach triad and reads the
maximal complex with exact IIT-4.0 Φ. Four pre-registered hypotheses are tested. When delivery requires
both agents, only one enters the maximal complex; the core stays {M, R, T2} at Φ=2.0, with the sender
displaced and the second required agent absorbed, refuting the prediction that both enter as in the
regulator coalition. A substitutable coalition, where either agent suffices, keeps both agents out and
leaves the base triad {E, M, R}. A single bidirectional gating agent enters, replicating Q68, and the
triadic core is present in every configuration. Three hypotheses confirmed, one refuted; the refutation
separates recipient-side gating from mediator-side regulation.

## Introduction

The regulator-coalition probe found that two weak regulators enter the irreducible core only when both
gate the mediator's commit. This study asks whether two recipient-side agents that jointly gate delivery
behave the same way.

## Related work

Coordination theory treats a gatekeeper as part of the structure when it constrains the flow
[malone1994interdisciplinary]; the economics of spam places filters on the receiving side
[rao2012economics]; AI-mediated communication places agents on both sides [hancock2020aimc]. Integrated
information theory decides membership by the major complex [oizumi2014phenomenology; albantakis2023iit4;
mayner2018pyphi], and the lab's regulator-coalition probe is the mediator-side comparison.

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: both required agents enter. H2: a substitutable coalition
keeps the agents out. H3: a single bidirectional agent enters. H4: the triadic core is present in every
configuration.

## Methods

Base triad E'=M, M'=E∧R, R'=M; gating agents read the message (Ti'=M) and gate delivery (R'=M∧…). Forms:
both_required (R'=M∧T1∧T2), either_suffices (R'=M∧(T1∨T2)), single_bidir (R'=M∧T, T'=M). The maximal
complex is read with `probes.lib.major_complex`. Decision rules are in `methods.md`.

## Results

**H1 (refuted).** both_required has maximal complex {M, R, T2} at Φ=2.0. Only one of the two required
agents enters; the core stays size three with the sender displaced.

**H2 (confirmed).** either_suffices has maximal complex {E, M, R}; neither substitutable agent enters.

**H3 (confirmed).** single_bidir has maximal complex {M, R, T}; the single bidirectional agent enters,
replicating Q68.

**H4 (confirmed).** The maximal complex is triadic at Φ=2.0 in every configuration.

## Discussion

A recipient-side gating coalition does not grow the core the way a mediator-side regulator coalition does.
Two agents that jointly gate the recipient's input are symmetric and redundant to each other once one is
in the core, so the maximal complex keeps a size-three structure {M, R, T2} with one agent standing in for
the pair, rather than expanding to include both. The contrast with the regulator coalition is the finding:
where two regulators gate the mediator's commit, both enter and the core grows; where two agents gate the
recipient's input, one suffices for the core. The location of the gate, not the number of gatekeepers,
decides whether a coalition enlarges the irreducible coordination. Substitutable gating leaves the agents
outside entirely, consistent with the substitutability law.

## Limitations

H1's refutation shows the regulator-coalition pattern does not transfer to recipient-side gating. Results
are in-silico: Boolean models, evidence about the models [axtell1996aligning]. Φ is read ordinally. The two
agents are symmetric; asymmetric gating agents are untested and might both enter. Hypotheses were fixed
before computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
