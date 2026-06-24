# q202 — findings

The Φ-bridge survives the worker-form-shuffle null in both simulated cohorts, and exact Φ adds
large incremental variance over the cheap edge-density proxy once the form space is rich enough to
separate irreducibility from edge density.

## Battery (N = 400 per cohort, seed 0)

| cohort | r(Φ,ACS) real | shuffle null mean | p (two-sided) | ΔR² over proxy | ΔR² 95% CI | r(Φ,proxy) |
|---|---|---|---|---|---|---|
| whole-system (2 forms) | +0.3825 | -0.0031 | 0.0010 | +0.0000 | [-0.0000, +0.0000] | +1.0000 |
| facet (4 forms) | +0.8283 | -0.0019 | 0.0010 | +0.3772 | [+0.3179, +0.4390] | +0.6636 |

## Verdicts

- **H1 SUPPORTED.** Shuffling the worker-to-form mapping centers the Φ_coord-to-ACS correlation on
  0 (null means -0.003 and -0.002) and the real effect falls outside the null at p = .001 in both
  cohorts. The relation is not a labelling artifact.
- **H2 SUPPORTED.** On the facet cohort, where the four forms order differently under edge density
  and under Φ, Φ_coord adds ΔR² = +0.377 over the proxy with a CI that excludes 0. The cheap proxy
  does not subsume the irreducibility content.

## The boundary case, reported honestly

With only two whole-system forms, Φ_coord and edge density are perfectly collinear (r = 1.000), so
ΔR² is exactly 0 and the cheap proxy ties Φ. A two-level structure cannot separate the two
measures; any monotone relabelling of the form indicator matches Φ there. The proxy subsumes
Φ_coord wherever the form space has at most two forms. The separation appears once a third and
fourth form make edge density and irreducibility disagree: the counterpart-coupled form has the
most edges yet less Φ than the mediated form, and that is where Φ carries variance edge density
misses.

## Scope

Both cohorts are simulated; the association is built into the synthetic data. The result is
evidence about the instrument and the proxy on synthetic data. No worker is measured, and the
bridge to real response data stays open.
