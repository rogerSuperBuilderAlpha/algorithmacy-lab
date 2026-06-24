# q182 — review

## What the probe does

It builds 200 synthetic coder panels over six defensible mediator readings, lets an adversary pick the
extreme opposite-kind reading present in each panel, and measures the forced-flip rate and the
agreement-weighted CI's containment of the forced point estimate. It reuses the q173 bridge
(`rule_to_phi`, `phi_ci_from_rules`); Φ is not reimplemented.

## Determinism

All randomness runs through `numpy.random.default_rng(0)`: the population draw and the per-account
bootstrap-t seed. Three consecutive runs produced byte-identical stdout.

## Controls

The instrument control reads the faithful triad as triadic at Φ_MIP = 2.0. Control A confirms a
unanimous panel gives the adversary no opposite-kind reading. Control B confirms a unique reading
yields a degenerate CI `[0,0]` and a powerless adversary. The controls bound the attack: the adversary
needs a contested pool to do anything.

## Threats to validity

- The verdict is categorical, so a forced-flip rate of 1.0 on attacked accounts is partly built into
  the dyadic/triadic dichotomy. The finding that matters is not the flip rate alone but its pairing
  with H2: the CI does not cover the flip.
- The reading library is small and the peripheral rules are fixed. A wider library or stochastic
  rules could change the Φ values, though not the categorical structure of the verdict.
- The CI is bootstrap-t over the panel mean. A different interval (e.g. one spanning the full min–max
  of defensible readings) would cover the adversary by construction. H2 tests the bridge's CI as
  built, not every conceivable interval.

## Honesty

H2 is reported as NOT SUPPORTED. The agreement-weighted CI does not defend against adversarial reading
selection in this design. The defenses that work are a determinate pool and a tied panel.

## Scope

Synthetic coder panels only. No worker is measured.
