# Q79 — Stage 2 deep research: probabilistic determination

This study makes the commit probabilistic and draws on the same literatures (shared `references.bib`).

## Stochastic integrated information

Integrated information is defined for stochastic systems, and the exact-Φ machinery accepts a state-by-node
transition probability matrix [oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi]. A deterministic
commit is the p∈{0,1} limit. A commit that reads the recipient with probability p is a mixture of the
read-recipient and broadcast determinations, and its Φ can be computed exactly at small size, as in Q71.

## Why a probabilistic reader matters

A real agent reads the recipient imperfectly: sometimes it tailors, sometimes it falls back to a template.
The economics of spam frames the fallback as the cheap default [rao2012economics]; costly signaling frames
genuine reading as the informative act [spence1973job]. The structural question is whether the irreducibility
that marks genuine coordination appears only under perfect reading or accumulates with the probability of it.
The framing carries from Q63-Q75 [malone1994interdisciplinary; hancock2020aimc].

## The open gap

The deterministic endpoints are known; the interpolation is uncomputed. The gap is open: sweep the reading
probability and read Φ. In-silico, with the validation gap [axtell1996aligning]; hypotheses fixed before
computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].
