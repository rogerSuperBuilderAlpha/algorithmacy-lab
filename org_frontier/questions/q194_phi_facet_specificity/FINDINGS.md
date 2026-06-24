# q194 — Findings

The exact-Φ coordination measure predicts the three ACS facets differentially, and a
partition-restricted component aimed at the worker-counterpart relation carries the counterpart facet
above and beyond whole-system Φ. Both results are on a simulated cohort built to the survey_bridge
facet map.

## Φ-to-facet correlations (n = 300, seed 0)

| construct | r(Φ_whole) | r(Φ_WC) |
|-----------|-----------:|--------:|
| ACS-CI    | +0.802 | +0.868 |
| ACS-SC    | +0.833 | +0.780 |
| ACS-RT    | +0.828 | +0.774 |
| SE        | −0.166 | −0.129 |

ACS-CI is the one facet whose correlation with the W-C component exceeds its correlation with
whole-system Φ. The two whole-system facets run the other way. The discriminant covariate SE tracks
neither Φ reading.

## Hypothesis verdicts

| Hypothesis | Key number | Verdict |
|-----------|-----------|---------|
| H1: Φ predicts CI more than SE | Δr = +0.967, 95% CI [+0.859, +1.083] | SUPPORTED |
| H2: W-C component adds variance over whole Φ | ΔR² = +0.1124, 95% CI [+0.0762, +0.1519] | SUPPORTED |

H1: the standardized ACS-CI slope on Φ is +0.802 against an SE slope of −0.166, and the difference in
the Φ-to-construct correlation excludes 0.

H2: adding Φ_WC to a model already holding Φ_whole raises the ACS-CI R² from 0.643 to 0.755, an
increment whose bootstrap CI excludes 0.

## Scope

The cohort is simulated and the facet-to-structure loadings are built into the data generator. The
study shows the partition-restricted instrument recovers the differential the survey_bridge map
predicts when that map holds. Whether the map holds is a question for fielded data; no worker is
measured here.
