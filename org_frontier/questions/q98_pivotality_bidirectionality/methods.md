# Q98 — Stage 4 methods (fixed before computation)

Ground truth is the exact major complex (`probes.lib.major_complex`). Run on
`~/iit-playground/venv-4.0/bin/python`.

## Construction (`forms.py`)

The full three-node family (each node reads the other two through an arbitrary Boolean function), reusing
Q90's `sample_wiring` and sensitivity measure. For each node: in-influence is the mean Boolean sensitivity
of the node's own update to its inputs; out-influence is the mean sensitivity of the other nodes to it
(Q90's measure). Membership is whether the node's label is in the major complex.

## Sampling and test (`probe_pivotality_bidirectionality.py`)

1,200 wirings, seed 98 (3,600 node observations). Both influences fall on a discrete grid; the top value
is the grid maximum. Cells:

- strong influence, zero reading: out-influence at the maximum, in-influence zero.
- strong reading, zero influence: in-influence at the maximum, out-influence zero.
- strong both: both at the maximum.

## Decision rules

- H1 confirmed if P(core | strong influence, zero reading) < 0.10.
- H2 confirmed if P(core | strong reading, zero influence) < 0.10.
- H3 confirmed if rank-AUC(min(in, out) → core) > rank-AUC(in + out → core).
- H4 confirmed if P(core | strong both) ≥ 0.85.
