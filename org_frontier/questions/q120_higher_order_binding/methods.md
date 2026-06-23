# Q120 — methods

## The instrument

Exact IIT-4.0 Φ via PyPhi, through the lab's classifier. A form is read as **triadic** when its
whole-system Φ over the minimum-information partition exceeds `PHI_EPS` (1e-9) in at least one reachable
state, and **dyadic** otherwise. `verdict(rules, labels)` returns the structure; `major_complex(rules,
labels)` returns the irreducible core and its Φ. Both are validated on the canonical strict-mediation
triad (W'=S, S'=W∧C, C'=S) as the control: triadic, Φ_MIP = 2.0, core {W, S, C}, all three parties
pivotal.

## Knockout and pivotality

Each coordination form is three Boolean update rules over the state (W, S, C). Knocking out party P
replaces P's rule with a non-interpreting pass-through, so P no longer reads the others while the others
still read P. Two definitions are run:

- **spectator** — `P' = x[P]`: P freezes at its current value (the lab's spectator construct);
- **silenced** — `P' = 0`: P is forced to a constant.

P is **pivotal** in a triadic form when the knockout flips the verdict to dyadic. A form's pivot count is
the number of its parties that are pivotal. A **pure higher-order bind** has pivot count zero.

## The two families

- **Strict mediation (256 forms):** `W' = f_W(S)`, `S' = f_S(W, C)`, `C' = f_C(S)`, with f_W, f_C ranging
  over the 4 one-input Boolean functions and f_S over the 16 two-input functions. The mediator S is a cut
  vertex: it is the only path between W and C.
- **Fully coupled (4096 forms):** `W' = f_W(S, C)`, `S' = f_S(W, C)`, `C' = f_C(W, S)`, each over the 16
  two-input functions. No party is a cut vertex; the redundancy across direct edges could carry an
  irreducible bind that no single party holds.

## Procedure

For every form in each family, compute the verdict. For each triadic form, knock out each party under each
definition and record whether the verdict flips. Report the distribution of pivot counts, the per-party
pivotal rate, and the count of pure higher-order binds.

## Reproduce

```
python -m org_frontier.questions.q120_higher_order_binding.probe_higher_order_binding          # both families (~4 min)
python -m org_frontier.questions.q120_higher_order_binding.probe_higher_order_binding --quick  # strict-mediation only (~1s; the CI gate)
```

The `--quick` run covers the 256 strict-mediation forms and is the registered CI check. The full run adds
the 4096 fully-coupled forms; its output is saved in [`results/full_output.txt`](results/full_output.txt).
