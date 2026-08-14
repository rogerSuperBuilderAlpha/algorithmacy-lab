# Analysis plan — cohort algorithmacy panel

Committed before fielding. It fixes the models and the decision rules so the analysis tests what the
design set out to test. All analyses run after Wave 3 closes; no test runs on partial data.

## Small-sample stance

The cohort is small, self-selected, and technical. The study is powered for measurement development and
within-person description, not for well-powered between-person inference. The confirmatory core is the
measurement model (H1) and the within-person growth in algorithmacy (H2). Every between-person relation
in RQ3 is exploratory: estimated, reported with its interval, and read as a lead for a larger sample, not
as a confirmed effect. The report states observed power or precision rather than claiming adequacy.

## Data preparation

- Reverse-score items marked (R) in the codebook.
- Compute scale means with the 75%-complete rule.
- Screen for careless responding: completion time floor, long-string runs, and an instructed-response
  check; flagged cases are reported and analyses run with and without them.
- Link waves by `pid` (one-way hash). Build a person-period long file and a wide file.

## Measurement model (RQ1)

1. **Structure.** Exploratory factor analysis of the twelve ACS items at W1 (oblique rotation, parallel
   analysis to fix the number of factors). Confirmatory factor analysis of the three-factor model at W2
   and W3, fit by maximum likelihood with robust corrections. Fit thresholds: CFI ≥ .90, RMSEA ≤ .08,
   SRMR ≤ .08. Compare against a one-factor model by Δχ² and ΔCFI.
2. **Reliability.** McDonald's ω per facet and total per wave, with bootstrap confidence intervals; α
   reported alongside for comparability.
3. **Invariance.** Longitudinal CFA across the three waves: configural, then metric, then scalar, with
   residual correlations for repeated items. A step holds if ΔCFI ≤ .01 and ΔRMSEA ≤ .015. If a step
   fails, partial invariance is established by freeing the fewest parameters, identified by modification
   indices, and reported.

Mean comparisons across waves proceed only after at least metric invariance holds.

## Growth model (RQ2)

- **Primary.** Latent growth curve model of ACS total across the three waves: intercept and linear slope,
  with the slope mean and variance estimated. H2 is supported if the slope mean is positive with a 95% CI
  excluding zero (one-tailed). A latent basis (freely estimated middle loading) model is fit as a
  sensitivity check on the shape.
- **Equivalent multilevel form.** With small N, a multilevel model (waves nested in persons, random
  intercept and slope, FIML) is the primary estimator and the latent-growth model the confirmatory
  parallel where it converges; if the latent model does not converge, the multilevel estimate stands and
  this is reported.
- **Facets.** Slopes for the three ACS facets are estimated and reported alongside the total.

## Nomological relations (RQ3)

- Person-mean-centered predictors separate within-person from between-person association in the
  multilevel models. H3a–H3e are tested as the relevant fixed effects; directional nulls per the
  pre-registration.
- **Discriminant validity — generic.** A CFA with ACS and general self-efficacy estimates their latent
  correlation; a value below .85 supports distinctness. RQ3 relations are re-estimated controlling for
  self-efficacy to show incremental association.
- **Discriminant validity — the published rival (H4), W2 only.** A second-order CFA with two factors,
  ACS and adapted algorithmic competency (ZAC; Zhou et al. 2025), against a single-factor alternative:
  distinctness needs the two-factor model to win on Δχ²/ΔCFI **and** the latent correlation to fall
  below .85. Fornell–Larcker is reported alongside (each AVE above their shared variance). RQ3 relations
  are then re-estimated with ZAC controlled, the same way self-efficacy is handled, so the incremental
  claim is made against the rival and not only against generic confidence. The registered facet-level
  predictions — ZAC-Understanding with counterpart inference, ZAC-Leveraging with signal compression,
  ZAC-Embracing with none — are examined as a pattern check, not as separate tests, and no facet-level
  p-values are interpreted. With one wave and a cohort-sized N this analysis is **exploratory in
  precision but confirmatory in direction**: the .85 threshold and the model comparison were fixed
  before fielding, and a failure is reported as a failure. `analysis.py` prints an observed-score
  preview of this block; the CFA needs a SEM package.
- Psychological-ownership and TMS change (W2→W3) are tested as latent change or multilevel slopes.

## Missing data and attrition

- FIML under missing-at-random for all model-based estimates.
- Attrition described per wave; a logistic regression predicts wave completion from W1 variables to
  characterize who drops out.
- Sensitivity: key results re-estimated under a pattern-mixture or selection-model alternative to probe
  the MAR assumption.

## Common-method and inference safeguards

- Procedural: scales separated and ordered to reduce priming, reverse-coded items within scales, anonymity
  assured to lower evaluation apprehension (Podsakoff et al., 2003).
- Statistical: a marker-variable or unmeasured-latent-method-factor check on the cross-sectional
  relations, reported as a robustness column.
- Multiplicity: the confirmatory tests (H1, H2) carry the inferential weight; RQ3 reports unadjusted and
  Benjamini–Hochberg-adjusted p-values, with the exploratory framing primary.

## Reproducibility

When the dataset is in hand, the analysis is a single committed script (R or Python) that reads the
de-identified data and writes every reported number and figure. It registers in
[`../../ci/reproduce.json`](../../ci/reproduce.json) with the commands and the expected output strings, so
each number re-derives under CI. Raw identifiable data is never committed; only de-identified, aggregated,
or board-approved material enters the public repository.

## Outputs

A `FINDINGS.md` reporting, in order: sample and attrition; the measurement model and invariance; the
growth result; the nomological relations; the falsification checklist from the pre-registration answered
one by one; and the limits. The paper draft follows the lab's house style.

## References

Bollen, K. A., & Curran, P. J. (2006). *Latent curve models*. Wiley. · Enders, C. K. (2010). *Applied
missing data analysis*. Guilford. · Meredith, W. (1993). Measurement invariance. *Psychometrika, 58*,
525–543. · Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method
biases. *Journal of Applied Psychology, 88*, 879–903. · Vandenberg, R. J., & Lance, C. E. (2000).
Measurement invariance. *Organizational Research Methods, 3*, 4–70. Full citations in
[`STUDY.md`](STUDY.md).
