# Q124 — Stage 1 review: robustness of the verdict to the state-aggregation rule

## The question

The critical review's sharpest IIT-methodological objection (rated fatal) holds that the verdict, read as
Φ_MIP at the single most-integrated reachable state, rests on one cherry-picked state: for many triadic forms
only the all-ones state integrates, so a min, mean, or stationary aggregation might call them dyadic. This
tests whether the triadic verdict survives a change of aggregation rule.

## What the lab already knows that bears on this

- **The classifier reads the verdict as max Φ_MIP over reachable states, and records n_states_irreducible.**
  The per-state profile is already exposed, so the aggregation can be varied without new machinery.
- **For the read-recipient triad, only the all-ones state integrates (Φ=2 there, 0 elsewhere).** This is the
  prime example the objection rests on, and the family holds many like it.
- **IIT is state-dependent by construction; there is no state-free Φ.** Any classifier must choose an
  aggregation, so the question is which choices the verdict survives, not whether a choice is made.

## The gap

The program fixed the max-over-states rule without testing its sensitivity. Whether the verdict survives the
mean, the stationary weighting, and the strict min, and whether any aggregation flips a dyadic form, is
untested.
