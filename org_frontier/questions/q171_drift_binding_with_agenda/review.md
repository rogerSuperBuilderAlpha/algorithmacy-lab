# q171 — review

## Claims and support

The probe computes exact Φ at every cell of a drift x interest grid and tests two pre-registered
hypotheses against the numbers. H1 (super-additive destruction) is refuted; H2 (drift re-integrates an
interested mediator) is supported. Both verdicts read directly off the printed grid. The instrument
control reads the d = 0, k = 0 cell two ways (the verdict classifier and sphi) and halts unless both
report the faithful triad at Φ = 2.0.

## Reproducibility

sphi is exact and uses no RNG. A seed is fixed for any stochastic fallback. The output is byte-identical
across three runs. The reproduce check pins the CONTROL PASS line and both H verdict lines.

## Threats and limits

The drift target is a modelling choice. PP4 drifts W ∧ C toward W ∨ C; this bridge applies that same
flip to the faithful arm only, holding the agenda on the overridden states. A different drift target
(toward the agenda, or toward a random rule) could change the interaction sign, and that sensitivity is
not yet mapped. The grid is coarse (four d, five k). The H2 effect is confined to the deny agenda at
k = 1 in this grid; it is a region, not a pervasive phenomenon, and the wording reflects that.

The result is on synthetic data. "Drift", "agenda", "approve", "deny" are labels for the rule and its
output values, not measured intent. No worker is in the loop. The finding is about how two Boolean
opacities compose under exact Φ, the kind of structural question the binary verdict cannot answer alone.

## Verdict

The study runs clean and deterministic, reports its null and its refutation honestly, and states its
in-silico scope. The interaction it surfaces — sub-additive erosion, with a sign flip on the deny
agenda — is a determinate property of the construction worth carrying into the next study.
