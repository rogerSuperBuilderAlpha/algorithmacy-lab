# Q124 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether the verdict survives a change of state-aggregation rule, answering the sharpest
IIT-methodological objection (rated fatal): the verdict reads Φ_MIP at the single most-integrated reachable
state, a max over states, and for many triadic forms only the all-ones state integrates, so a min, a mean, or
a stationary weighting might call the form dyadic and reveal the verdict as a property of one cherry-picked
state. Written and committed before the run; the instrument is the classifier's own per-state Φ profile.

Each triadic form's verdict is recomputed under four aggregations of the per-state Φ_MIP profile: max (the
classifier's rule), mean (uniform over reachable states), stationary (weighted by the deterministic dynamics'
long-run occupancy), and min (the strict every-state rule).

## H1 — Every triadic form survives mean aggregation

- **Claim:** All 24 triadic forms have a positive mean-over-reachable-states Φ_MIP, so they remain triadic
  under a uniform aggregation, not just under the max.
- **H0:** Some triadic form has mean Φ_MIP = 0.
- **Predicted outcome:** all 24 survive. H0 refuted. The verdict is not an artifact of taking the maximum.

## H2 — Every triadic form survives stationary aggregation

- **Claim:** All 24 triadic forms have a positive stationary-weighted Φ_MIP, so the integrating state is
  actually occupied in the long run, and the form remains triadic under the distribution the system spends its
  time in.
- **H0:** Some triadic form's integrating state is unoccupied long-run, giving stationary Φ = 0.
- **Predicted outcome:** all 24 survive. H0 refuted. The objection that the verdict rests on an unoccupied,
  cherry-picked state does not hold; the integrating state carries long-run weight.

## H3 — The strict every-state rule flips some forms

- **Claim:** Under the min aggregation (the form integrates in every reachable state), fewer than 24 triadic
  forms survive: the single-state integrators read dyadic.
- **H0:** All 24 survive the min rule too.
- **Predicted outcome:** fewer than 24. H0 refuted. The verdict is a capacity reading (the form supports
  irreducible coordination in an occupied state), not an every-state reading, and the strict rule is a
  different, stronger construct. This is the study's genuinely uncertain claim and its honest scoping: the
  result could have been 24 (full robustness) or near 0 (the charge vindicated).

## H4 — No dyadic form turns triadic under any aggregation

- **Claim:** No dyadic form gains a positive Φ_MIP under any of the four aggregations.
- **H0:** Some dyadic form becomes triadic under some aggregation.
- **Predicted outcome:** zero flips. H0 refuted. The aggregation choice can only cost a triadic form its
  verdict, never invent one, so the sensitivity is one-sided and the dyadic class is stable.
