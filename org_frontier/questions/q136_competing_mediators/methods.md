# Q136 — methods

Four nodes W, S1, S2, C. Each mediator commits the parties' joint determination, Si' = W ∧ C. Substitutes:
W' = C' = S1 ∨ S2 (the parties route through either). Complements: W' = C' = S1 ∧ S2 (both required). For
each form: the whole-system verdict (max-Φ over reachable states), the major complex (the lab convention for
forms with spectator/redundant nodes), the total Φ, and the Shapley value of subsystem Φ at the verdict's
integrating state, giving each mediator's share and the parties' collective share. Control: the single
faithful mediator (two-thirds, Q111).

Caveats from Q111/Q122: value-function background, unproven Φ-to-money bridge; "value/share/rent" name
Shapley allocations of Φ.

Reproduce: `python -m org_frontier.questions.q136_competing_mediators.probe_competing_mediators`
([`results/output.txt`](results/output.txt)).
