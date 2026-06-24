# Q141 — methods

Two forms. **Immediate** (Q128, four nodes W, S, C, O): W' = S, S' = O, C' = S, O' = W ∧ C — the objective
reads the parties directly. **Lagged** (five nodes, memory M added): M' = W ∧ C (the memory captures the
parties' joint state), O' = M (the objective reads the memory), with S' = O, W' = S, C' = S — the objective
tracks the joint determination with a one-step delay. For each form: the whole-system verdict (max Φ over
reachable states), the major complex, whether the worker is in it, and the Φ. Control: the canonical
three-party triad (triadic, Φ = 2.0).

The lagged form has one more node than the immediate one, so the comparison spans a size change — named in the
limitations; the point is that the lag mechanism (the memory) changes the structure. Exact Φ on five nodes is
slow (~15 s). Φ-to-money bridge open (Q122).

Reproduce: `python -m org_frontier.questions.q141_lagging_objective.probe_lagging_objective`
([`results/output.txt`](results/output.txt)).
