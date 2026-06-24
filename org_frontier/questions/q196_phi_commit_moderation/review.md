# q196 — review

## What the probe shows

The Φ_coord × commit interaction on ACS-total is positive with a CI clear of zero, and the
convey-floored control cohort flattens the Φ-ACS slope to exactly zero. The bridge and the exact-Φ
instrument recover a commit-gated association when one is present in the synthetic generator.

## Threats and answers

- Built-in structure. The moderation is hard-coded into the cohort generator, so the test cannot
  fail to find a positive interaction when the data carry one. The probe is a recovery check on the
  measurement chain, not a discovery. The convey arm guards against a slope that appears regardless
  of structure: it floors commit, drives Φ_coord to a constant, and the slope collapses to zero.

- Φ_coord is binary at the worker level. Each form is one of two types, so Φ_coord takes values 0 or
  2.0. The moderation rides on the cohort mixture of the two forms crossed with reported commit, not
  on a graded Φ within a single worker. A graded-Φ extension would need forms with intermediate
  irreducibility.

- The interaction term shares the Φ_coord factor with the main effect. Standardizing commit and
  centering keep the interaction interpretable; the null main effect plus the clear interaction CI
  show the lift is located in the product term.

- Determinism. One seed for the cohort, one for the bootstrap. The captured stdout is byte-identical
  across re-runs.

## Standing limitation

The cohort is simulated and no worker is measured. The commit lever is demonstrated in silico. The
result is evidence about the bridge and instrument under a known generator, and it carries to a real
panel only when real waves replace the simulation.
