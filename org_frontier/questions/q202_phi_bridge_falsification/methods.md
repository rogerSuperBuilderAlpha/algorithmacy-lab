# q202 — methods

## Machinery reused

- `org_frontier.survey.cohort_algorithmacy.phi_bridge` (study 1 of the survey line): the
  worker-to-form map, `simulate_cohort`, `simulate_facet_cohort`, `coordination_form`, and the
  per-worker exact Φ readings.
- `org_frontier.classifier.classifier.tpm_from_rules`, `cm_from_rules`.
- `org_frontier.probes.lib.max_phi_float`, `verdict`.

## Instrument control

The probe validates the Φ instrument on the canonical faithful mediated triad
`[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`: `verdict` reads `triadic` and
`max_phi_float` reads 2.0. The probe prints `CONTROL ... PASS` and asserts both before any cohort
runs.

## Cohorts

Two simulated cohorts the bridge already builds, N = 400 each, seed
`numpy.random.default_rng(0)`.

- **Whole-system** (`simulate_cohort`): every worker maps to one of two forms, the commit AND gate
  (Φ_coord = 2.0) or the convey pass-through (Φ_coord = 0). ACS-total loads on the coordination
  latent that drives the form.
- **Facet** (`simulate_facet_cohort`): workers map to four forms whose Φ_whole and edge density
  rank them differently. The counterpart-coupled form carries the highest edge density (0.556) yet
  a lower Φ (1.0) than the mediated form (density 0.444, Φ 2.0). The ACS target is the
  whole-system facet (`acs_sc`), which loads on Φ_whole.

## H1 — worker-form-shuffle null

Permute the per-worker Φ_coord vector against fixed ACS (1000 shuffles, seed 0), recompute the
Pearson r each time, and locate the real r in the null. The two-sided p is the add-one-smoothed
fraction of |null| at least as extreme as |real|. The null mean indexes whether shuffling centers
the effect on 0. H1 is supported when, in every cohort, p < .05 and the null mean is within 0.05
of 0.

## H2 — incremental validity over the edge-density proxy

The proxy is `edge_density(form) = cm.sum() / n²` from `cm_from_rules`, with no Φ. Per worker, take
the proxy for that worker's form. Hierarchical regression of ACS on the proxy alone, then on the
proxy plus Φ_coord; ΔR² is the increment. A nonparametric row bootstrap (2000 resamples, seed 0)
gives the 95% percentile CI on ΔR². H2 is supported when ΔR² > 0 and the CI excludes 0.

## Determinism

One cohort seed, one permutation seed (0), one bootstrap seed (0). Φ_coord depends only on which
form a worker maps to, so the sweep reproduces exactly. Output is byte-identical across runs.

## Validation gap

Exact Φ throughout. Both cohorts are simulated; the association is built into the synthetic data by
construction. The battery tests whether the bridge's reported relation is a labelling artifact (H1)
and whether exact Φ adds over a cheap proxy (H2) on that synthetic data. No worker is measured, and
the Φ-to-construct bridge to real response data stays open.
