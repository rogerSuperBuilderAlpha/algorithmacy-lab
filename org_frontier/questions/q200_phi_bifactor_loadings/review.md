# q200 — review

## What the probe shows

In a bifactor model of the ACS (general factor g plus three orthogonal facets CI, SC, RT), Φ_coord
loads on g (standardized β = +0.46, 95% CI [+0.37, +0.55]) and not on any specific facet (facet βs
near zero, every general-minus-facet Δ CI excludes 0). Routing Φ_coord to g reproduces the augmented
[9 items | Φ] covariance at CFI = 0.99 against CFI = 0.90 for routing it to the SC facet, ΔCFI = +0.09.
H1 and H2 hold on the synthetic W2 cohort. The instrument control passed at the canonical faithful triad.

## Stress tests a reader should apply

- **Built-in placement.** The cohort is simulated so the coordination latent loads on the general
  factor. Φ_coord loads on g because it was generated to. The contribution is that exact Φ recovers the
  planted placement through the Boolean-form bridge and that the bifactor scoring separates g from the
  facets cleanly enough to read it. A real wave could place Φ_coord differently.
- **Factor-score scoring, not full SEM.** The bifactor scores come from orthogonalized principal
  components (general factor from the full pool, specifics from partialled blocks), and the CFI is built
  on the model-implied vs observed covariance of the augmented block. This is a lightweight stand-in for
  a full bifactor CFA with a fitted measurement model. A confirmatory fit in lavaan or semopy on a real
  wave is the next step; the direction of the discriminant result should not depend on the estimator.
- **Two-valued Φ_coord.** Φ_coord takes one of two values (0 or 2), since the bridge maps each worker
  to one of two forms. The general-factor path is close to a point-biserial between commit-form
  membership and g. A graded Φ_coord from a richer form family would sharpen the loading; per the
  classifier's standing caveat the magnitude of Φ is at most an ordinal hint.
- **The competitor is the hard one.** SC (system coordination) is the facet a reader expects a
  coordination measure to load on, so it is the named competitor in H2. That the SC routing loses is the
  point: Φ_coord behaves as a general indicator even against the facet most aligned with its surface
  content.

## Validation gap

The cohort is simulated and no worker is measured; no W2 wave file exists. The study validates the
bridge module and the bifactor recovery pipeline, not a measured loading in a real cohort. It supplies
the discriminant placement (Φ_coord on the general factor, not the SC facet) that the later
sub-competence studies build on.
