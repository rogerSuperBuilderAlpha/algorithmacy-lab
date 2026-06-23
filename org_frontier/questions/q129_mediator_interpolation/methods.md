# Q129 — methods

## Model

Four nodes: worker W, system S, counterpart C, objective O. The mediator interpolates between faithful and
predatory by a mix level m = 0..4: on m of the four (W, C) input states it serves its objective (S' = O), and
on the rest it commits the faithful joint determination (S' = W ∧ C). The parties read the system (W' = S,
C' = S). The objective is either **frozen** (O' = O, a fixed stance) or **adaptive** (O' = W ∧ C, learned
from both parties). m = 0 is the faithful triad; m = 4 is the fully predatory mediator of Q128.

## Two readings of "the coordination survives"

The objective O can be a disconnected spectator at low mix, so a single whole-system number is not enough.
Two readings are taken at each m:

- **Parties bound in the core** — the major complex (the lab's convention for forms with spectator nodes) and
  whether both parties W and C are in it. The coordination-Φ is that core's Φ when both parties are bound,
  else 0.
- **Whole-system irreducible** — the whole-system verdict (Φ_MIP > PHI_EPS over all four nodes), the measure
  Q128 used.

Each reading is run for both objectives, along a fixed conversion order and averaged over every choice of
which m states serve the objective. The control is the faithful mediator at m = 0, whose major complex is
{W, S, C} at Φ = 2.0.

## Reproduce

```
python -m org_frontier.questions.q129_mediator_interpolation.probe_mediator_interpolation
```

Output is saved in [`results/output.txt`](results/output.txt). The run is a few seconds (four nodes).
