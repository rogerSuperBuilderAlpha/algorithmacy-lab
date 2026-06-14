# Q122 — Stage 4 methods (fixed before computation)

Exact IIT-4.0. The value wave's own value function, recomputed with the clamp and background as parameters,
audited over the full subset lattice of each form. Run on `~/iit-playground/venv-4.0/bin/python`; the audit
computes in ~3s.

## The value function (`forms.py`)

`value_fn(rules, labels, background, clamp)` returns v(S) = the subsystem-Φ of node-set S
(`pyphi.new_big_phi.sia(pyphi.Subsystem(net, state, nodes=S)).phi`), with the complement frozen at the
background state (all-ones or all-zeros). With `clamp=True` it floors at zero (the wave's convention); with
`clamp=False` it returns the raw signed Φ. `shapley(...)` is the wave's Shapley value over this v.

## Forms

- **Productive** (`productive_forms`): the read-recipient triad (Q111), the bidirectional principal (Q114),
  and the all-required markets at N = 2 and N = 3 (Q115). These are the forms whose value distribution the
  wave reported as surplus.
- **Degenerate** (`degenerate_form`): the monitor-only principal (Q114), a read-only owner whose value the
  wave reported as −0.833.

## Checks (`probe_game_validity.py`)

- `monotone_superadditive` counts, over the full subset lattice (clamp on, background all-ones): subset/superset
  pairs where v falls when a party is added (monotonicity violations), and disjoint pairs where
  v(S∪T) < v(S)+v(T) (superadditivity violations).
- The headline Shapley vectors are recomputed with the clamp off, and at the all-zeros background, to test the
  clamp-artifact and background-dependence charges.

## Decision rules

- H1 confirmed if every productive form has zero monotonicity violations.
- H2 confirmed if every productive form has zero superadditivity violations.
- H3 confirmed if the monitor-only form has at least one monotonicity violation.
- H4 confirmed if the clamped and unclamped vectors are identical on every form tested, and every form's
  vector is all-zero at the all-zeros background.
