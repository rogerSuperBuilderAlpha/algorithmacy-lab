# Q74 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems, synchronous update. For each form the whole-system verdict and Φ_MIP come
from `classifier.classify_rules`; the maximal complex (label set, Φ) from `probes.lib.major_complex`; the
connectivity matrix from `classifier.cm_from_rules`. An element x outside the maximal complex C is
**read-only** if some core element feeds x but x feeds no core element, **emit-only** if x feeds some core
element but no core element feeds x, and **bidirectional** if both. Run on `~/iit-playground/venv-4.0/bin/python`.
Decision rules fixed here.

Forms (state tuple in label order):
- **disclosed** (E, M, R, D): E'=M, M'=E∧R, R'=M, D'=M.
- **delegated** (E, As, Ar, R): E'=E, As'=E∧Ar, Ar'=As∧R, R'=R.
- **monitoring** (E, M, R, T): E'=M, M'=E∧R, R'=M, T'=M.
- **chain** (E, A1, A2, R): E'=A1, A1'=E∧A2, A2'=A1∧R, R'=A2.

## Test (`probe_verdict_vs_complex.py`)

- **Measure:** per form, the whole-system verdict and Φ_MIP, the maximal complex and its Φ, and for each
  excluded element its coupling class (read-only / emit-only / bidirectional).
- **Decision rules:**
  - H1 confirmed if disclosed, delegated, monitoring are whole-system dyadic and triadic on the maximal complex.
  - H2 confirmed if every excluded element in those three forms is non-bidirectional.
  - H3 confirmed if the chain is whole-system triadic, its maximal complex is a proper subset, and an
    excluded element is bidirectional.
  - H4 confirmed if, across the four forms, an excluded element is bidirectional iff the form is
    whole-system triadic.
