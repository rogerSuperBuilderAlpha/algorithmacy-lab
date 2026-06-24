# q171 — methods

## The two knobs

The mediator triad has nodes (W, S, C): the worker W, the system S, the counterpart C. The parties read
S faithfully, W' = S and C' = S. S's commit rule carries the two opacities.

Drift d comes from PP4 in `org_frontier/cognition/predictive_processing.py`. A faithful gate A = W ∧ C
drifts toward a flipped rule B = W ∨ C with probability d, the moving target of a retraining system. At
d the gate fires A with probability (1 − d) and B with probability d.

Interest k comes from Q126's `mediator(agenda, k)` in
`org_frontier/questions/q126_interested_mediator/probe_interested_mediator.py`. The mediator imposes its
agenda a on the k states where the parties least warrant it (approve a = 1 starting from the fewest
parties on, deny a = 0 from the most), and runs the faithful arm elsewhere. k = 0 is the faithful AND;
k = 4 is the predatory constant.

## The cross

The bridge function `drift_binding_phi(agenda, d, k)` in
`org_frontier/cognition/interested_mediator_forms.py` crosses the two. S commits the interested gate
`mediator(agenda, k)` with probability (1 − d) and the drifted gate (agenda on the overridden states,
W ∨ C on the rest) with probability d. The drift acts only on the faithful arm, the states the parties
still rule. Each cell's whole-system Φ is `sphi` over the stochastic 8×3 state-by-node TPM, the same
reader the margin-to-dyad thread uses.

The sweep runs d ∈ {0, 0.1, 0.25, 0.5} crossed with k ∈ {0, 1, 2, 3, 4}, for both agendas. The d = 0
column is the pure-interest Q126 ladder; the k = 0 row is the pure-drift PP4 ladder. These edges are the
controls.

## Reading the hypotheses

H1 compares each interior cell's Φ to the multiplicative null Φ(d, 0)·Φ(0, k)/Φ(0, 0). Super-additive
destruction means combined Φ strictly below the null. H2 checks whether any interior cell's Φ exceeds
the d = 0 baseline at the same k.

## Determinism and control

`sphi` is exact and uses no RNG; a seed `numpy.random.default_rng(0)` is fixed so any stochastic fallback
reproduces. The output is byte-identical across re-runs. The instrument control reads the d = 0, k = 0
cell two ways that must agree: the verdict classifier on the Boolean faithful triad
`[lambda x:x[1], lambda x:x[0]&x[2], lambda x:x[1]]` reports triadic with max Φ = 2.0, and `sphi` on the
same cell's TPM returns 2.0. The probe halts if they disagree.
