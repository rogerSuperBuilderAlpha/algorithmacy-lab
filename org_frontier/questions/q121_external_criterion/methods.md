# Q121 — Stage 4 methods (fixed before computation)

Two non-Φ criteria against the exact verdict, over the 256-form strict-mediation family (Q93) and its 40
full-cycle forms (Q117 `cycle_present`). Run on `~/iit-playground/venv-4.0/bin/python`; the sweep computes in
~4s. The exact verdict (`q93.is_triadic`) is the ground truth; neither criterion calls Φ.

## Criteria (`forms.py`)

- **Observational — `total_correlation_next`.** The multi-information Σ H(Y_i) − H(Y) of the next-state joint
  Y = (W', S', C') under a uniform distribution over current states. Pure statistical dependence of the
  dynamics' output; an established information-theoretic quantity, computed without intervention or Φ.
- **Interventional — `damage_spreading`.** The Boolean-network damage-spreading measure (Kauffman 1969;
  Derrida & Pomeau 1986): from each reachable start state, flip one party, run the deterministic dynamics for
  the horizon, and average the Hamming divergence between the perturbed and unperturbed trajectories over all
  parties, starts, and steps. A do-intervention probe from dynamical-systems theory, computed without Φ.

The horizon is fixed at 4. The separation on the hard subset is stable for any horizon ≥ 2 (at horizon 1 the
single step is too short to reveal divergence; at horizon ≥ 2 the rank-AUC on the hard subset is 1.000, with
the triadic and dyadic score ranges disjoint).

## Evaluation (`probe_external_criterion.py`)

Rank-AUC (Mann-Whitney) of each criterion against the verdict, on the full family and on the hard full-cycle
subset, with the topology-only cycle indicator (Q117) reported for reference.

## Decision rules

- H1 confirmed if the cycle indicator's full-family AUC exceeds 0.9.
- H2 confirmed if the observational criterion's hard-subset AUC is at most 0.6.
- H3 confirmed if the interventional criterion's hard-subset AUC is at least 0.9.
- H4 confirmed if the interventional criterion's full-family AUC is below 0.999.

The thresholds (0.6 for "fails", 0.9 for "separates") are conventional rank-AUC bars fixed before the run, not
tuned to the observed values.
