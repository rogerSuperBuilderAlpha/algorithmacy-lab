# Q124 — The verdict is a robust capacity reading, not an artifact of the maximum

## Question

The sharpest IIT-methodological objection holds that the verdict, read as Φ_MIP at the single most-integrated
reachable state, rests on one cherry-picked state, since many triadic forms integrate only at the all-ones
state; a min, mean, or stationary aggregation might call them dyadic. This tests that charge.

## Method

For each of the 24 triadic strict-mediation forms, the verdict is recomputed under four aggregations of the
per-state Φ_MIP profile: max (the classifier's rule), mean (uniform over reachable states), stationary
(weighted by the deterministic dynamics' long-run occupancy), and min (the strict every-state rule). The 232
dyadic forms are checked for any aggregation that turns them triadic.

## Results

The verdict survives max, mean, and stationary aggregation on every triadic form; only the strict min flips
some; no dyadic form ever flips.

| aggregation | triadic forms surviving (of 24) |
|---|---|
| max | 24 |
| mean | 24 |
| stationary | 24 |
| min | 8 |
| dyadic forms turning triadic (any rule) | 0 of 232 |

| | result |
|---|---|
| H1 every triadic form survives mean aggregation | confirmed |
| H2 every triadic form survives stationary aggregation | confirmed |
| H3 the strict every-state rule flips some | confirmed |
| H4 no dyadic form turns triadic under any aggregation | confirmed |

## Interpretation

The verdict is no artifact of the maximum. Every triadic form has a positive mean-over-states Φ_MIP, so
reading the verdict from the average reachable state rather than the best one keeps all 24 triadic. The
max-over-states rule is convenient, and the less favorable uniform mean reaches the same verdict on every
form, so the objection's premise that the maximum carries the verdict alone is wrong.

The integrating state is occupied, which answers the strongest form of the charge. The objection's sharpest
version was that the integrating state is barely visited, so a weighting by the distribution the system
occupies would wash the verdict out. It does not: all 24 triadic forms have a positive stationary-weighted
Φ_MIP, the integrating state carrying real long-run occupancy under the deterministic dynamics. The verdict
holds under the distribution the system spends its time in, a property of the form's behavior over time.

The verdict is a capacity reading, and the strict rule is a different construct. Under the min aggregation,
which requires integration in every reachable state, 8 of 24 survive and the 16 single-state integrators read
dyadic. This is the verdict's honest scope: the classifier asks whether a form can support irreducible
coordination in a state it occupies, robust across max, mean, and stationary; the min rule asks whether it
integrates always, a stronger claim the single-state integrators fail. The program's verdict is the capacity
one, which it should state.

The sensitivity is one-sided. No dyadic form gains a positive Φ_MIP under any aggregation, because a dyadic
form is zero at every reachable state, so every aggregation of zeros is zero. The aggregation choice can cost
a triadic form its verdict under the strict rule, never invent a triadic verdict, so the dyadic class is
stable and the boundary moves one way.

The fatal-rated objection is substantially answered. The verdict is robust to the max, the mean, and the
stationary weighting, and the integrating state is occupied long-run, so it is a property of the form rather
than of one cherry-picked state. The honest residue is the capacity scope: under the strict every-state rule
the single-state integrators read dyadic, a thing to state plainly.

## Limitations

In-silico; exact IIT-4.0 Φ_MIP per state. The robustness is established on the 256 strict-mediation forms, not
proven for every coordination form. The stationary occupancy is the attractor distribution of a deterministic
map; a stochastic dynamics would weight states differently, though the uniform-mean result already shows the
verdict does not depend on favoring the integrating state.
