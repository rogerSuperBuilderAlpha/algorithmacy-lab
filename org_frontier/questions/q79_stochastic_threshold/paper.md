# Stochastic emergence: the triad accumulates with the probability of reading the recipient

## Abstract

The program's outreach verdicts are computed on a deterministic commit. This study makes the agent's
commit probabilistic — it reads the recipient with probability p and ignores it with 1−p — and reads the
verdict with exact IIT-4.0 Φ as p is swept. Four pre-registered hypotheses are tested. At p=1 the form is
triadic at Φ=2.0 and at p=0 it is dyadic at Φ=0; Φ rises monotonically across the grid; an agent that
reads the recipient only a quarter of the time already has Φ>0; and the emergence is graded, with no
flat-zero region. All four hypotheses confirmed: irreducibility accumulates with the probability of
genuine reading rather than appearing at a threshold.

## Introduction

A real agent reads the recipient imperfectly. The deterministic verdicts of Q63 are the endpoints of a
probabilistic commit. This study sweeps the reading probability and asks how the triad emerges between
them.

## Related work

Integrated information is defined for stochastic systems and the exact-Φ machinery accepts a stochastic
transition matrix [oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi], as used in the noise
study Q71. The economics of spam frames the cheap fallback [rao2012economics] and costly signaling the
informative reading [spence1973job; zahavi1975mate]; the framing carries from Q63-Q75
[malone1994interdisciplinary; hancock2020aimc].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: the deterministic endpoints. H2: Φ monotone in p. H3:
partial reading yields Φ>0. H4: emergence is graded.

## Methods

Over the state-by-node TPM on (E, M, R), E'=M and R'=M are deterministic and P(M'=1)=p·(E∧R)+(1−p)·E. Exact
max-Φ is computed with `probes.lib.max_phi_float` at p in {0, 0.25, 0.5, 0.75, 1.0}. Decision rules are in
`methods.md`.

## Results

Φ is 0.0, 0.11, 0.28, 0.54, 2.0 at p = 0, 0.25, 0.5, 0.75, 1.0. H1 (endpoints 2.0 and 0), H2 (monotone),
H3 (interior Φ>0), and H4 (graded, Φ>0 at p=0.25) all confirmed.

## Discussion

The triadic verdict is the deterministic limit of a graded quantity. An agent that sometimes reads the
recipient produces a partially irreducible coordination, and the degree of irreducibility tracks how often
it reads. There is no threshold of reading below which the coordination is a clean broadcast and above
which it is a clean triad; irreducibility accumulates continuously. For the application this sharpens the
binary law: genuine reading is not all-or-nothing, and an agent that tailors half the time sits half-way
into algorithmacy. The deterministic conjunction at p=1 is the maximally-integrated special point, which is
why the last step in Φ is steep.

## Limitations

The study is confirmatory. Results are in-silico: a Boolean form with a probabilistic commit, evidence
about the model [axtell1996aligning]. Φ is read ordinally and the five-point grid does not exclude fine
structure between points. The mixture is between read-recipient and broadcast; other probabilistic commits
are untested. Hypotheses were fixed before computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
