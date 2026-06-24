# q198 — findings

On the simulated panel, a worker's baseline (W1) Φ_coord predicts the individual latent ACS-growth slope.
Workers whose W1 reported conditions map to the irreducible commit form (Φ_coord = 2.0) gain algorithmacy
competence faster than workers whose conditions map to the factorizable convey form (Φ_coord = 0.0): the
recovered mean LGC slope is +0.5232 for commit forms versus +0.1953 for convey forms.

The instrument control passed: the faithful triad `[x1, x0&x2, x1]` reads triadic with max Φ_MIP = 2.0.

The effect survives controlling baseline competence. Regressing the slope on W1 Φ_coord with the W1 ACS
intercept added as a covariate leaves the Φ_coord coefficient positive with a CI excluding 0, so Φ_coord
is incremental over baseline level. A shuffled-Φ placebo predictor gives a coefficient whose CI includes
0, and the forced-dyadic control cohort holds Φ_coord at 0 for every worker (no predictor variance), so
the association rides on the form's irreducibility rather than on a scale shared between Φ_coord and the
slope.

| model                          | β(W1 Φ_coord) | 95% CI               |
|--------------------------------|---------------|----------------------|
| H1: slope ~ Φ                  | +0.1639       | [+0.1173, +0.2106]   |
| placebo: slope ~ shuffled-Φ    | +0.0033       | [-0.0469, +0.0536]   |
| H2: slope ~ Φ + W1-intercept   | +0.1894       | [+0.1388, +0.2400]   |

N = 300; 49 commit (irreducible) W1 forms, 251 convey (factorizable) W1 forms. β is per unit of Φ_coord
(0-2), so the commit-vs-convey slope gap (~0.33) is about twice the per-unit β.

- **H1: SUPPORTED.** β(Φ) = +0.1639, 95% CI [+0.1173, +0.2106]: positive, interval excludes 0; the
  shuffled-Φ placebo CI includes 0.
- **H2: SUPPORTED.** Partial β(Φ | W1-intercept) = +0.1894, 95% CI [+0.1388, +0.2400]: Φ_coord predicts
  the slope above and beyond baseline competence.

Scope: the panel is simulated. No worker is measured and no wave file exists. The growth structure and the
Φ-to-slope coupling are synthetic; the result is evidence about the bridge and the growth pipeline on
synthetic data. It extends the shared bridge (q193) from a cross-sectional association to a longitudinal
slope, and is the growth scaffold the later survey studies build on.
