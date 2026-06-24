# q196 — findings

The Φ_coord-to-ACS association strengthens under perceived system commitment. In the commit cohort,
Φ_coord predicts ACS-total only through its interaction with reported commit: the main Φ effect is
flat and the Φ_coord × SA-commit interaction is positive with a CI clear of zero. The convey-floored
control cohort holds Φ_coord at zero, so its Φ-ACS slope is exactly flat, and the slope difference
between cohorts excludes zero.

## Moderated OLS (commit cohort, N=600): ACS-total ~ 1 + Φ_coord + SA(z) + Φ_coord×SA

| term | coef | 95% CI |
|---|---|---|
| Φ_coord | +0.1002 | [-0.0889, +0.2892] |
| SA(z) | +0.2131 | [+0.1441, +0.2821] |
| Φ_coord×SA | +0.5006 | [+0.3646, +0.6365] |

## Φ-ACS slope by cohort

| cohort | Φ-ACS slope | Φ variance |
|---|---|---|
| commit | +0.9084 | 0.4816 |
| convey | +0.0000 | 0.0000 |

Slope difference (commit − convey) = +0.9084, bootstrap 95% CI [+0.7997, +1.0194].

## Verdicts

- H1 (Φ_coord × SA-commit interaction on ACS-total is positive, CI excludes 0): **SUPPORTED**.
  Interaction coef = +0.5006, CI [+0.3646, +0.6365]. The standalone Φ_coord term is not distinct
  from zero, so the association lives in the moderation, not a main effect.
- H2 (commit Φ-ACS slope positive, convey slope flat, slope-diff CI excludes 0): **CONFIRMED**.
  Commit slope +0.9084, convey slope +0.0000, difference CI [+0.7997, +1.0194].

## Reading

The moderation is built into the synthetic generator; the test shows the bridge and the exact-Φ
instrument recover it. The cohort is simulated and no worker is measured, so this is in-silico
evidence about the measurement chain, not a measured effect in a real panel.
