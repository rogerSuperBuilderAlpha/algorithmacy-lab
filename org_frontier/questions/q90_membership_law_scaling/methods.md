# Q90 — Stage 4 methods (fixed before computation)

Ground truth is the exact major complex (`probes.lib.major_complex`) of each sampled wiring, computed
with exact IIT-4.0 Φ. Run on `~/iit-playground/venv-4.0/bin/python`.

## The family (`forms.py`)

The full n-node family: each node reads all n-1 others through an arbitrary Boolean function, so a wiring
is n truth tables of 2^(n-1) bits each. This is probe #12's three-node construction lifted to larger n.
For each sampled wiring and each node, two quantities are computed:

- **bidirectional:** the node reads someone (its function is non-constant) and influences someone (its
  out-influence is positive).
- **out-influence:** the mean over the other nodes of the Boolean sensitivity of their updates to this
  node's input position.

and whether the node's label is in the major complex.

## Sampling (`probe_membership_law_scaling.py`)

Sample sizes fall with n because the major-complex cost rises steeply (~27s per wiring at n = 5):

- n = 3: 300 wirings (seed 31)
- n = 4: 150 wirings (seed 41)
- n = 5: 15 wirings (seed 51)

n = 6 is not sampled; one major-complex computation there is ~9 minutes.

## Measures and decision rules

Per size: the non-bidirectional in-core rate; the rank-AUC of out-influence predicting membership among
bidirectional nodes; and the membership probability for the bottom and top influence terciles.

- H1 confirmed if the non-bidirectional in-core rate is below 0.05 at n = 3, 4, 5.
- H2 confirmed if the rank-AUC is at least 0.75 at n = 3, 4, 5.
- H3 confirmed if, at n = 4, the top-tercile membership probability exceeds the bottom-tercile one.
- H4 confirmed if the n = 4 rank-AUC is within 0.15 of the n = 3 value.
