# Q128 — methods

## Model

Four nodes: worker W, system S, counterpart C, objective O (state index 0, 1, 2, 3). The mediator is
predatory in the strongest sense — it commits exactly its own objective and never reads the parties
directly:

- W' = S, C' = S — the parties read the system.
- S' = O — the system commits its objective.
- O' = g(W, C) — the objective updates by an adaptation rule.

The adaptation rule g is swept from no adaptation to full:

| adaptation | O' | reads |
|---|---|---|
| frozen | O | neither party |
| reads worker | W | W only |
| reads counterpart | C | C only |
| joint AND | W ∧ C | both |
| either OR | W ∨ C | both |
| differ XOR | W ⊕ C | both |

## Measure

For each adaptation, exact IIT-4.0 Φ over the four-node system via the lab's classifier: the structure
(triadic when Φ_MIP > PHI_EPS in some reachable state, else dyadic), the major complex, whether the
objective O is in it, and how many of the parties W, C are in it. The control is the faithful three-party
triad (triadic, Φ = 2.0), confirming the instrument.

The refined finding is read off the sweep: the predatory mediator is triadic exactly on the adaptations
where the objective reads both parties, and the objective is in the core whenever the form re-integrates.

## Reproduce

```
python -m org_frontier.questions.q128_adaptive_mediator.probe_adaptive_mediator
```

Output is saved in [`results/output.txt`](results/output.txt). The run is a few seconds (four nodes).
