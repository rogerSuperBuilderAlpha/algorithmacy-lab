# q190 findings

The disagreement-Φ spread survives synthetic elicitation noise. Under bounded Bernoulli jitter on
each account's rule table (RATE = 0.10, DELTA = 0.10, 30 draws per pair), verdict_agreement moved
only on pairs sitting at the dyad/triad boundary. Pairs far from the boundary never flipped, and
the signed phi_gap never changed sign on any pair. For pairs that genuinely disagree, the gap
magnitude had signal-to-noise above two.

## Per-pair spread under elicitation noise (30 draws)

| pair | Φ_A0 | Φ_B0 | agree0 | boundary | agree_flip | sign_flip | gap_mean | gap_sd |
|---|---|---|---|---|---|---|---|---|
| anchor_triad_self | 2.000 | 2.000 | 1 | FAR | 0 | 0 | 0.663 | 0.483 |
| far_triad_triad | 2.000 | 2.000 | 1 | FAR | 0 | 0 | 0.680 | 0.518 |
| far_triad_ortriad | 2.000 | 2.000 | 1 | FAR | 0 | 0 | 0.541 | 0.477 |
| near_triad_dyad | 2.000 | 0.000 | 0 | NEAR | 2 | 0 | 1.318 | 0.558 |
| near_ortriad_indep | 2.000 | 0.000 | 0 | NEAR | 3 | 0 | 1.346 | 0.532 |
| near_dyad_dyad | 0.000 | 0.000 | 1 | NEAR | 4 | 0 | 0.004 | 0.011 |

All 9 agreement flips fell on NEAR-boundary pairs; FAR pairs accrued 0 flips of either kind.

## Verdicts

- H1 SUPPORTED. Flips occur only near the dyad/triad boundary, never far from it. NEAR-boundary
  pairs accrued 9 agree/sign flips; FAR pairs accrued 0. The spread is not an artifact of
  elicitation precision: a triad with Φ at or above ~0.65 under jitter never crosses to dyadic,
  and only a clean dyad at the boundary lifts across.
- H2 SUPPORTED. Pooled over the noiseless-disagreeing pairs, phi_gap mean = 1.332, sd = 0.545,
  signal-to-noise = 2.442 (n = 60). The gap magnitude is a measurable quantity for pairs that
  disagree.

## Scope

Synthetic accounts; exact IIT-4.0 Φ on small Boolean coordination forms. The rates are baselines
on synthetic data. The Φ-to-organization bridge is open.
