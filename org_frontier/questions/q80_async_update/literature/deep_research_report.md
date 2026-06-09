# Q80 — Stage 2 deep research: update scheme and the verdict

This study varies the update scheme and draws on the same literatures (shared `references.bib`).

## Synchronous and asynchronous dynamics

Integrated information is computed from a transition probability matrix
[oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi]. A synchronous deterministic update gives
one matrix; an asynchronous update, where one element acts per step and the others hold, gives a different,
stochastic matrix on the same elements. The asynchronous matrix is a mixture: with probability 1/n the
chosen element applies its rule and the rest hold. Its Φ is computed exactly at small size with the same
machinery used for the noise and stochastic-commit studies.

## Why the update scheme matters

A result that held only under simultaneous action would be an artifact of the modelling convention, since
real coordination unfolds in time [malone1994interdisciplinary]. The framing carries from Q63-Q79
[rao2012economics; hancock2020aimc].

## The open gap

The synchronous verdicts are known; their robustness to asynchronous update is uncomputed. The gap is open:
recompute the keystones under asynchronous update and read the verdict. In-silico, with the validation gap
[axtell1996aligning]; hypotheses fixed before computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].
