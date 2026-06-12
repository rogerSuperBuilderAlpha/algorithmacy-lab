# Q124 findings — the verdict survives every reasonable aggregation; only the strict every-state rule flips it

All four hypotheses confirmed. The triadic verdict is robust to the state-aggregation rule: all 24 triadic
forms remain triadic under the max, the uniform mean, and the long-run stationary weighting, and the
integrating state carries positive stationary weight in every case. Only the strict min rule, which demands
integration in every reachable state, flips the 16 forms that integrate at a single state. No aggregation ever
turns a dyadic form triadic. The charge that the verdict rests on one cherry-picked, unoccupied state does not
hold.

| aggregation of per-state Φ_MIP | triadic forms surviving (of 24) |
|---|---|
| max (classifier's rule) | 24 |
| mean (uniform over reachable states) | 24 |
| stationary (long-run occupancy) | 24 |
| min (strict every-state) | 8 |
| dyadic forms flipping to triadic (any rule) | 0 of 232 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | every triadic form survives mean aggregation | confirmed (24/24) |
| H2 | every triadic form survives stationary aggregation | confirmed (24/24) |
| H3 | the strict every-state rule flips some | confirmed (8/24 survive) |
| H4 | no dyadic form turns triadic under any aggregation | confirmed (0 flips) |

From `probe_aggregation_robustness.py`.

## What it says

The verdict survives the mean, so it is no artifact of the maximum. Every one of the 24 triadic forms has a
positive mean-over-reachable-states Φ_MIP (H1), so reading the verdict from the average state rather than the
best state keeps all of them triadic. The max-over-states rule the classifier uses is not load-bearing in the
way the objection supposed: the cheaper, less favorable uniform mean reaches the same verdict on every form.

The integrating state is genuinely occupied, which answers the sharpest form of the charge. The objection's
strongest version was that the integrating state is one the system barely visits, so a weighting by the
distribution the system actually occupies would wash the verdict out. It does not: all 24 triadic forms have a
positive stationary-weighted Φ_MIP (H2), with the integrating state carrying real long-run occupancy under the
deterministic dynamics. The verdict holds under the distribution the system spends its time in, so it is a
property of the form's behavior, not of a transient, cherry-picked state.

The verdict is a capacity reading, and the strict rule names a different construct. Under the min aggregation,
which requires the form to integrate in every reachable state, only 8 of the 24 survive: the 16 single-state
integrators read dyadic (H3). This is the honest scope of the verdict. The classifier asks whether a form can
support irreducible coordination in a state it occupies, a capacity claim, and the answer is robust across
max, mean, and stationary. The min rule asks whether the form integrates always, a strictly stronger claim,
and 16 forms that integrate at one occupied state fail it. The two are different questions, and the program's
verdict is the capacity one, which it should state.

The sensitivity is one-sided: aggregation never invents a verdict. No dyadic form gains a positive Φ_MIP under
any of the four rules (H4), because a dyadic form has Φ_MIP = 0 at every reachable state, so every aggregation
of zeros is zero. The aggregation choice can only cost a triadic form its verdict under the strict rule, never
manufacture a triadic verdict from a dyadic form. The dyadic class is stable under every aggregation, and the
boundary moves in only one direction.

The net for the defense agenda: the fatal-rated F1 objection is substantially answered. The verdict is robust
to the max, the mean, and the stationary weighting, and the integrating state is occupied long-run, so it is
not a property of one cherry-picked state. The honest residue is that the verdict is a capacity claim: under
the strict every-state rule, the single-state integrators read dyadic, a scope the program should state rather
than a flaw it should hide.

## Caveats

- **Confirmatory, and the risky claim was real.** H2 could have failed if the integrating states were
  transient; they were not. H3 could have come back 24 (full robustness) or near 0 (the charge vindicated); it
  came back 8, locating the verdict as a capacity claim.
- **One family.** The 256 strict-mediation forms. The aggregation robustness is established for these, not
  proven for every coordination form.
- **Deterministic dynamics.** The stationary occupancy is the attractor distribution of a deterministic map.
  For stochastic dynamics the stationary distribution would be computed differently, and the weighting could
  shift, though the mean result already shows the verdict does not depend on favoring the integrating state.
- **Exact Φ throughout.** The per-state profile is the exact IIT-4.0 Φ_MIP. In-silico.
