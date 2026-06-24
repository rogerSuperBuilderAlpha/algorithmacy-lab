# q200 — findings

On the simulated W2 cohort, Φ_coord loads on the general algorithmacy factor, not on a specific facet.
The standardized path from Φ_coord to the bifactor general factor g is +0.4610 (95% CI [+0.3738,
+0.5481]); the paths to the three orthogonal specific facets are near zero (CI +0.0568, SC +0.0430,
RT −0.0966), and each general-minus-facet difference has a bootstrap CI excluding 0.

The instrument control passed: the faithful triad `[x1, x0&x2, x1]` reads triadic with max Φ_MIP = 2.0.

Routing matters for fit. The model that routes Φ_coord to the general factor reproduces the augmented
[9 items | Φ] covariance at CFI = 0.9917; routing Φ_coord to the SC specific facet drops to CFI =
0.9006, since Φ covaries with all three item blocks and a SC-only path cannot reproduce its CI and RT
covariances. ΔCFI = +0.0911 favours the general path, above the .01 threshold.

| Φ_coord path target | β (std) | 95% CI               | Δ vs g (β_g − β)        |
|---------------------|---------|----------------------|-------------------------|
| GENERAL g           | +0.4610 | [+0.3738, +0.5481]   | —                       |
| specific CI         | +0.0568 | [−0.0413, +0.1549]   | +0.4029 [+0.2874, +0.5146] |
| specific SC         | +0.0430 | [−0.0551, +0.1412]   | +0.4167 [+0.2987, +0.5301] |
| specific RT         | −0.0966 | [−0.1943, +0.0012]   | +0.5565 [+0.4364, +0.6743] |

| model        | routing            | CFI    |
|--------------|--------------------|--------|
| Φ→g          | general factor     | 0.9917 |
| Φ→SC         | SC specific facet  | 0.9006 |

N = 400; 51 irreducible (commit) forms, 349 factorizable (convey); 9 ACS items, 3 per facet.

- **H1: SUPPORTED.** β_g = +0.4610, 95% CI [+0.3738, +0.5481]: positive, interval excludes 0; the
  general path exceeds each specific-facet path (all Δ CIs exclude 0).
- **H2: SUPPORTED.** ΔCFI = +0.0911 ≥ .01: the Φ→general model fits the augmented covariance better
  than the Φ→SC-specific model.

Scope: the cohort is simulated. No worker is measured and no W2 wave file exists. The bifactor
structure and the Φ-to-g coupling are synthetic; the result is evidence about the bridge and the
bifactor pipeline on synthetic data. It places Φ_coord on the general algorithmacy dimension rather
than the system-coordination facet a reader might expect, which is the discriminant claim the later
sub-competence studies build on.
