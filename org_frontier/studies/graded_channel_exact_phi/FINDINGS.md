# Graded party channel under exact Φ — findings (V4 #11)

**Question.** Does the exact-Φ joint-observation cliff survive a graded party
channel? The mediating system reads each party through a lossy channel —
correct with probability q, the default 0 otherwise — while party duty stays
perfectly correlated. The screen is whole-form Φ on the V4 #1 multifamily
panel (24 forms) and the V4 #7 logged panel (15 forms). Hypotheses were fixed
in `hypotheses.md` and the script committed before this run.

**Method.** Party→mediator edges degrade by mixture: the mediator's next value
is computed on the true party reads with probability q and on reads set to the
default 0 with probability 1−q. Party outputs never degrade. Φ is exact binary
IIT-4.0 via `max_phi_float` (max Φ over reachable states), the same engine the
foundations arc uses for stochastic TPMs. Whole-form triadic labels come from
`classify_rules`. Panel AUC is oriented per V4 #1; hold is AUC ≥ 0.85 or within
0.10 of the q=1 reference, cliff is AUC < 0.70 or a drop ≥ 0.20.

## Controls

Instrument gate passes: the faithful triad is triadic at Φ=2.000 and the
sticky form is dyadic at Φ=0.000. The anchors replicate the arc:
multifamily full 1.000, alternation 0.660 (V4 #1: 0.660), phase 1.000; logged
full 1.000, alternation 0.591 (V4 #7: 0.591). The channel sweep reproduces
the deterministic forms at q=1.

## Results

Multifamily panel AUC against the triadic label:

| condition | AUC |
| --- | --- |
| q = 1.00 | 1.000 |
| q = 0.75 | 1.000 |
| q = 0.50 | 0.853 |
| q = 0.25 | 0.824 |
| alternation anchor | 0.660 |
| phase-lock anchor | 1.000 |

Logged panel: q = 1.00 at 1.000, q = 0.50 at 0.909, q = 0.25 at 0.864,
alternation 0.591.

All five hypotheses are supported. H2: the q=0.5 graded channel holds
(0.853 ≥ 0.85). H3: degradation is monotone with no interior cliff. H4: q=0.5
beats hard alternation by 0.193. H5: the logged panel shows the same signed
conclusions, softer (0.909 at q=0.5).

**Verdict: `GRADED_HOLDS`.** The cliff is a duty-correlation artifact. Half
the party information, delivered through a lossy channel at perfectly
correlated duty, keeps the screen within the hold band (0.853), while
anti-correlated half duty at full information cliffs it (0.660). Information
quality and joint observability are separable: the second carries the screen
in this family, the first degrades it smoothly.

## Per-form texture

Degradation is not uniform across forms, and the ranking survives the
non-uniformity. Some forms shed Φ sharply under the channel — the conjunctive
carriers (chain_and, pool_and, ring at n=4) fall from landmark Φ to 0.000
already at q=0.5, a mechanism-side consequence of the default-0 read removing
the last conjunctive support — while others decay geometrically (and_hub
2.000 → 1.000 → 0.500; parity hubs trace 2^(2−n) → 0.193 at q=0.25). Every
dyadic form stays at 0.000 throughout. The AUC holds because the degradation
never reorders the classes: no dyadic form rises and no triadic form falls to
the dyadic floor at any interior q.

## Scope

In-silico. Designed Boolean forms; a default-zero garbling channel on
party→mediator edges only. The result is evidence about these models, not
about real organizations, and the channel family is one of many possible
degradations. A stale-read or hold-default channel, and party-side (not only
mediator-side) degradation, remain untested.
