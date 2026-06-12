# Q124 — Stage 4 methods (fixed before computation)

Exact IIT-4.0. The verdict recomputed under four aggregations of the per-state Φ_MIP profile, over the
256-form strict-mediation family. Run on `~/iit-playground/venv-4.0/bin/python`; the audit computes in ~3s.

## Aggregations (`forms.py`)

For each form, `phi_profile` gives Φ_MIP at every reachable state. `aggregations` returns:
- **max** — the maximum over reachable states (the classifier's rule).
- **mean** — the uniform mean over reachable states.
- **stationary** — the mean weighted by `stationary_occupancy`, each state's long-run occupancy under the
  deterministic dynamics from a uniform start (the attractor distribution).
- **min** — the minimum over reachable states (the strict every-state rule).

A form is triadic under an aggregation if that aggregation exceeds EPS = 1e-9.

## Checks (`probe_aggregation_robustness.py`)

`classify_family` splits the 256 forms into triadic and dyadic by the classifier's verdict. For each triadic
form the four aggregations are computed and counted as surviving (Φ > EPS); for each dyadic form the maximum
aggregation is checked for any triadic flip.

## Decision rules

- H1 confirmed if all triadic forms have mean Φ_MIP > EPS.
- H2 confirmed if all triadic forms have stationary Φ_MIP > EPS.
- H3 confirmed if fewer than all triadic forms have min Φ_MIP > EPS.
- H4 confirmed if no dyadic form has any aggregation above EPS.
