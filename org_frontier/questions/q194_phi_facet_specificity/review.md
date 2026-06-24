# q194 — Review

## What the study claims

Whole-system Φ predicts counterpart inference (ACS-CI) more than it predicts general self-efficacy
(H1), and a partition-restricted worker-counterpart component predicts ACS-CI beyond whole-system Φ
(H2). Both verdicts are SUPPORTED on simulated data.

## Strengths

- The worker-counterpart component is a genuine restriction of the same exact-Φ apparatus, scored
  with PyPhi's own partition enumeration, not a side heuristic. The control check pins the faithful
  triad at Φ_whole 2.0 and Φ_WC 1.0 before any cohort numbers are read.
- The four coordination forms decouple Φ_WC from Φ_whole (the coupled form holds Φ_WC at 1.0 while
  Φ_whole drops to 1.0), so the H2 increment is not collinear by construction.
- The facet-differential is visible directly in the correlation table: ACS-CI is the one facet that
  tracks Φ_WC above Φ_whole, while the two whole-system facets run the other way.
- The run is byte-identical across repeats; all RNG is seeded.

## Limits and threats

- The result is recovery, not confirmation. The facet loadings are written into the data generator
  from the survey_bridge map. A reader could object that the study only shows the instrument reads
  back what was put in. The defense is that the read-back is not automatic: the partition-restricted
  Φ had to be computable, non-redundant with the whole measure, and aligned with the right facet, and
  it is. None of that is guaranteed by the data generator.
- Φ_WC and Φ_whole correlate +0.91 across the full cohort. The decoupling lives among committers. A
  fielded cohort with a different commit rate would shift the increment.
- Only two facets are mapped to whole-system Φ and one to the partition. The study does not separate
  signal compression from rule-change tracking; they share a generator. A finer map would need
  distinct partition-restricted components for those facets.
- The discriminant covariate is one construct (SE). A stronger H1 would partial several nuisance
  competences at once.

## Verdict

The study does what it sets out to do on synthetic data: it builds a partition-restricted Φ, shows
it is not redundant with the whole-system measure, and shows it lines up with the facet the
survey_bridge map assigns. The contribution is the instrument and its facet-level reading. The
empirical claim waits on fielded waves.
