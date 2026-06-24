# Q131 — methods

## Model and value function

The Q126 interested mediator on the triad W, S, C: W' = S, C' = S, and S' an interested mediator of the
parties. At interestedness level k = 0..4 the mediator outputs its agenda a (approve = 1, deny = 0) on the k
input states where the parties least warrant it, and commits the faithful S' = W ∧ C elsewhere. k = 0 is the
faithful mediator; k = 4 ignores the parties.

The value of a coalition S is the integrated information of the subsystem on S — `pyphi.new_big_phi.sia` over
`Subsystem(net, state, nodes=S)` — reusing Q111's value function (`q111_shapley_value/forms.py`), at the
all-ones background state. A party's **Shapley value** is its average marginal contribution to coalition
value across all orderings; the Shapley values sum to the system's Φ. The **mediator share** is the
mediator's Shapley value divided by the total.

## Procedure

For each agenda and each level k, build the interested-mediator rules and compute the Shapley split and the
total Φ. The control is the faithful mediator (k = 0), which must reproduce Q111: total Φ = 2.0, mediator
Shapley 1.333 (two-thirds). Report the trajectory of the total and the mediator's share across the
interestedness axis.

## A known caveat

The value function uses the all-ones background, Q111's convention; the background-state dependence of the
subsystem-Φ value function is itself an open question (Q122). At the collapsed (dyadic) forms the value
function is no longer monotone, so a small negative Shapley value can appear where the total is already zero;
those rows carry no value to distribute and are read as zero. The Φ-to-economic-value bridge is the lab's
standing open question, so "value", "share", and "capture" name Shapley allocations of Φ, not money.

## Reproduce

```
python -m org_frontier.questions.q131_value_capture.probe_value_capture
```

Output is saved in [`results/output.txt`](results/output.txt).
