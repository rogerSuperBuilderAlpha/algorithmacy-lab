# Q132 — methods

## Model

The Q127 interested mediator on the triad W, S, C: at interestedness level k the mediator imposes its agenda
(approve) on the k input states where the parties least warrant it, committing the faithful baseline
elsewhere; W' = S, C' = S. Four faithful baselines: AND, OR, XNOR, XOR.

## Value function and the background-state correction

The value of a coalition is the integrated information of the subsystem on it (`pyphi.new_big_phi.sia`), and
a party's Shapley value is its average marginal contribution; the Shapley values sum to the subsystem Φ of
the whole. The value depends on the background state the subsystem is conditioned on. Q111 uses all-ones,
which is where the AND mediator integrates. For the other baselines the integrating state differs, so the
value is read at the **verdict's max-Φ state** — the reachable state at which the form's whole-system Φ is
maximal, the state the verdict itself reads. The all-ones reading is computed alongside for comparison.

The **mediator share** is the mediator's Shapley value over the total at the verdict state. The control is
the faithful AND mediator, which must reproduce Q111/Q131 at its integrating state: total Φ = 2.0, mediator
1.333, share two-thirds.

## Procedure

For each baseline and level k: compute the verdict and its integrating state, the Shapley split at that
state, and the total at the all-ones state. Record the verdict-Φ trajectory, the mediator's verdict-aligned
share, and where the all-ones reading diverges. A baseline shows **extraction** when some interested level
raises the verdict Φ above the faithful value and the mediator's share there exceeds 0.6.

## A standing caveat

The Φ-to-economic-value bridge is the lab's open question (Q122), and the background-state dependence of the
value function is part of it; Q132 reads at the verdict-aligned state and says so. "Value", "share", and
"rent" name Shapley allocations of Φ, not money.

## Reproduce

```
python -m org_frontier.questions.q132_value_baselines.probe_value_baselines
```

Output is saved in [`results/output.txt`](results/output.txt).
