# Influence requires membership: an agent outside the core cannot flip the verdict

## Abstract

This study asks whether an adversarial agent can change a coordination's dyadic/triadic verdict from
outside its irreducible core, using exact IIT-4.0 Φ. Four pre-registered hypotheses are tested by adding
an agent X to the read-recipient triad in three couplings, with the verdict read on the maximal complex
per the Q74 rule. A read-only X and an emit-only X each leave the maximal complex {E, M, R} triadic at
Φ=2.0, unchanged. Only a bidirectional, pivotal X changes the coordination, joining the core to make it
{E, M, R, X} at Φ=3.0. All four hypotheses confirmed: influence over the irreducible coordination requires
membership in it.

## Introduction

The lab's core-membership conditions say which elements belong to the coordination. This study reads them
as an adversarial question: can a party that wants to change the coordination do so from outside, or must
it join the core, where it becomes detectable?

## Related work

Integrated information theory locates the coordination in the maximal complex [oizumi2014phenomenology;
albantakis2023iit4; mayner2018pyphi], and membership requires bidirectional coupling plus pivotality
(Finding 8). The economics of spam frames adversarial senders and resisting filters [rao2012economics];
AI-mediated communication places agents that may act against a party [hancock2020aimc; jakesch2019aimc].
The framing carries from Q63-Q83 [malone1994interdisciplinary].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: a read-only agent leaves the core unchanged. H2: an
emit-only agent leaves the core unchanged. H3: a bidirectional, pivotal agent changes the core. H4: no
non-core coupling flips the core verdict.

## Methods

The base triad is E'=M, M'=E∧R, R'=M. The agent X is added read-only (X'=M), emit-only (X'=X, constant),
and bidirectional-pivotal (M'=E∧R∧X, X'=M). The verdict is read on the maximal complex
(`probes.lib.major_complex`) with the whole-system verdict reported alongside. Decision rules are in
`methods.md`.

## Results

read-only and emit-only X: whole-system dyadic (Φ=0), maximal complex {E, M, R} at Φ=2.0, unchanged.
bidirectional-pivotal X: whole-system triadic (Φ=3.0), maximal complex {E, M, R, X} at Φ=3.0. H1 through
H4 all confirmed.

## Discussion

Influence over the irreducible coordination requires membership in it. An agent that only reads the message
or only emits without being read is a spectator: it leaves the core triadic and unchanged, and the
whole-system Φ=0 is the spectator signature the Q74 rule identifies, not a manipulation of the verdict. The
only way the added agent changes the coordination is to couple into it bidirectionally and pivotally, and
then it joins the core. For adversarial settings the reading is clean: a party positioned outside the core,
reading or feeding without being read, cannot flip the dyadic/triadic verdict; to change the coordination
it must become a member, where the instrument places it inside the core. There is no manipulation from the
outside that the verdict does not register as membership.

## Limitations

The study is confirmatory. Results are in-silico: Boolean models, evidence about the models
[axtell1996aligning]. Φ is read ordinally. The pivotal case uses a conjunctive read; other pivotal
couplings are untested, and a non-pivotal bidirectional agent would stay out (Finding 8). Hypotheses were
fixed before computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
