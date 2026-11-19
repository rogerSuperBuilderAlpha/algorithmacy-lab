# Auto-recurrence screen of four symmetry-filtered representatives

Independent eight-state Markov-chain calculation with node-flip probability 0.08, stationary law, and lag 0..20. Candidate truth tables regenerated from the committed `nsi` and `aff` code identifiers, not copied from the candidate's numerical outputs.

| Pair | Max absolute difference across three self-match profiles |
|---|---:|
| nsi(0,3,3) vs aff(6,9,5) | 0.35280000000000067 |
| nsi(0,3,12) vs aff(6,9,4) | 0.3528000000000019 |
| aff(9,0,10) vs aff(9,12,10) | 0.5619059712000016 |
| aff(9,0,10) vs aff(9,12,11) | 0.3528000000000018 |

All four pairs are in `identifiability/results/verify_candidates.json` and are recorded as having different eligible q161 bottleneck sets and equal cross-channel lag profiles. None matches **all within-channel recurrence profiles** in the tested lag range.

This is a screen of **four selected representatives**, not a screen of all 74 symmetry-unique classes or 6,480 filtered pairs. It does not prove that no fully profile-matched non-isomorphic pair exists. It also does not invalidate the narrower, legitimate cross-channel representation insufficiency claim.

## Decision

Stop promoting any of these four as full-observation or full-recurrence non-identifiability results. Retain them as restricted cross-channel summary counterexamples. A broader search for all-auto-and-cross equality requires a separately documented question, complete candidate enumeration, symmetry validation, and clear stopping rules; do not silently widen the current preregistration or exploratory claims.
