# q201 — findings

Substitutability degrades Φ_coord, and the degraded Φ_coord captures the substitutability-to-
algorithmacy association. In the bridge cohort, higher reported substitutability drives Φ_coord down:
a substitutable worker's form factors to the convey pass-through. The lower Φ_coord predicts lower
ACS-total. The path SU → ACS runs predominantly through Φ_coord: the bootstrapped indirect effect
clears zero and outweighs the direct effect. The pivotal-W control holds the form irreducible
throughout, so Φ_coord is constant and its SU slope is flat.

## H1 — Φ_coord ~ 1 + SU(z) (structural leg) and ACS ~ 1 + Φ_coord (construct leg)

| arm | SU → Φ_coord slope | 95% CI |
|---|---|---|
| bridge | −0.6720 | [−0.7206, −0.6234] |
| control (pivotal-W) | flat (Φ constant at 2.0) | n/a — no Φ variance |

Φ_coord → ACS slope (bridge) = +0.6569, 95% CI [+0.5857, +0.7281].

## H2 — mediation SU → Φ_coord → ACS (bridge arm, 5000-boot)

| path | estimate | 95% CI |
|---|---|---|
| a (SU → Φ_coord) | −0.7424 | [−0.7701, −0.7107] |
| b (Φ_coord → ACS \| SU) | +0.4894 | [+0.3971, +0.5804] |
| indirect (a·b) | −0.3634 | [−0.4335, −0.2939] |
| direct (c′, SU → ACS \| Φ) | −0.1416 | [−0.2342, −0.0465] |

|indirect| = 0.3634 exceeds |direct| = 0.1416.

## Verdicts

- H1 (SU lowers Φ_coord, CI < 0; lower Φ_coord predicts lower ACS, CI > 0): **SUPPORTED**.
  SU → Φ_coord = −0.6720 [−0.7206, −0.6234]; Φ_coord → ACS = +0.6569 [+0.5857, +0.7281]. The
  pivotal-W control holds Φ_coord constant, so its SU slope is flat: the degradation rides on
  substitutability factoring the form.
- H2 (indirect SU → Φ_coord → ACS nonzero and exceeds direct SU → ACS): **CONFIRMED**.
  Indirect = −0.3634 [−0.4335, −0.2939]; direct = −0.1416 [−0.2342, −0.0465]; |indirect| > |direct|.

## Reading

The capture structure is built into the synthetic generator; the test shows the bridge and the
exact-Φ instrument recover it. The cohort is simulated and no worker is measured, so this is in-silico
evidence about the measurement chain, not a measured effect in a real panel.
