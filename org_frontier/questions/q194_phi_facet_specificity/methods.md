# q194 — Methods

## Machinery reused

- `org_frontier.probes.lib.verdict` — whole-system classifier verdict for the instrument control.
- `org_frontier.survey.cohort_algorithmacy.phi_bridge` — the shared bridge module from study 1 of
  this line. The study uses its exact-Φ readers and its facet cohort:
  - `phi_whole_and_wc(rules)` reads two numbers from a W-S-C Boolean form with exact IIT-4.0 Φ:
    whole-system Φ (max Φ_MIP over reachable states) and the W-C-restricted component Φ_WC.
  - `coordination_form(commit, coupled)` returns the W-S-C rules for two binary reported conditions.
  - `simulate_facet_cohort(n, rng)` builds the simulated cohort.
  - `pearson_ci`, `steiger_diff` carry the interval estimates.

## The partition-restricted Φ

Whole-system Φ reads how irreducible a form is overall. The W-C component reads how much of that
irreducibility runs through the worker-counterpart relation. At each reachable state, every system
partition that places W and C in different blocks is a cut that severs the worker-counterpart
relation. Φ_WC takes the least informative such cut at each state (the partition-restricted analogue
of the minimum-information partition) and the maximum over states. The cuts are enumerated with
PyPhi's `new_big_phi.system_partitions` and scored with `evaluate_partition`, so Φ_WC uses the same
exact apparatus as the whole-system reading.

For the faithful mediated triad the whole-system Φ is 2.0 and Φ_WC is 1.0: the counterpart relation
carries half the global integration.

## Coordination forms

Two binary reported conditions key the form a worker maps to:

- `commit` (TI/SA high, SU low): the system commits a joint determination rather than conveying one
  party's signal.
- `coupled` (counterpart coupling): the counterpart reads the worker directly, so the irreducibility
  runs through the W-C relation; otherwise the counterpart sits hidden behind the gate.

The four forms read:

| commit | coupled | Φ_whole | Φ_WC |
|-------:|--------:|--------:|-----:|
| 0 | 0 | 0.0 | 0.0 |
| 0 | 1 | 0.0 | 0.0 |
| 1 | 0 | 2.0 | 1.0 |
| 1 | 1 | 1.0 | 1.0 |

The coupled form holds Φ_WC at 1.0 while Φ_whole drops to 1.0, which decouples the W-C component from
the whole-system reading and makes the incremental test in H2 non-trivial.

## Cohort generation

A coordination latent drives the commit gate through TI, SA, and SU; an independent
counterpart-coupling latent drives the coupled flag. Each worker carries the exact (Φ_whole, Φ_WC)
of the form the two conditions map to. The facets and covariate follow the survey_bridge map:
ACS-CI loads on Φ_WC, ACS-SC and ACS-RT load on Φ_whole, and SE loads on a generic-competence latent
independent of the coordination structure. All draws use `numpy.random.default_rng(0)`.

## Tests

- H1: standardized OLS slopes of ACS-CI and SE on Φ_whole, and a 5000-sample bootstrap percentile CI
  (fixed seed) for the difference of the Φ-to-construct correlations.
- H2: nested OLS of ACS-CI on Φ_whole alone versus Φ_whole plus Φ_WC, with a 5000-sample bootstrap
  percentile CI (fixed seed) for the incremental ΔR².

## Determinism

All RNG is seeded (`default_rng(0)`, bootstrap seed 0). The probe re-runs byte-identical. The
instrument control asserts the faithful triad reads `triadic`, max Φ_MIP 2.0, Φ_WC 1.0 before any
cohort numbers are computed.

## Run

```
source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
python -m org_frontier.questions.q194_phi_facet_specificity.probe_phi_facet_specificity \
  | tee org_frontier/questions/q194_phi_facet_specificity/results/output.txt
```
