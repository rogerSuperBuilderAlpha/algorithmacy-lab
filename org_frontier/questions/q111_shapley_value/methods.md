# Q111 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 integrated information of subsystems via PyPhi's `sia`. Run on
`~/iit-playground/venv-4.0/bin/python`.

## Construction (`forms.py`)

The value of a coalition S is the Φ of the subsystem on S, with the complement fixed at the all-ones state
(`pyphi.Subsystem(net, state, nodes=S)`). A party's Shapley value is the standard average marginal
contribution over all orderings. Two forms: the read-recipient triad, and the triad plus a read-only
spectator X that reads the mediator and is read by no one.

## Decision rules (`probe_shapley_value.py`)

- H1 confirmed if the mediator's Shapley value exceeds each outer party's.
- H2 confirmed if the Shapley values sum to the system Φ.
- H3 confirmed if the mediator's Shapley value exceeds Φ/n.
- H4 confirmed if the spectator's Shapley value is at most zero.
