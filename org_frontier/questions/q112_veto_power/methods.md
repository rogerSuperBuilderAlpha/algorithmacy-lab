# Q112 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict and major complex, with the Shapley value from Q111. Run on
`~/iit-playground/venv-4.0/bin/python`.

## Construction (`forms.py`)

A party defects by replacing its rule with a constant — it stops participating. `core_vetoes` records
whether each core party's defection makes the read-recipient triad dyadic. `spectator_veto` checks whether
a read-only spectator's defection changes the major complex {E, M, R}. `subcoalition_values` reads the
Q111 value function on the two-party coalitions.

## Decision rules (`probe_veto_power.py`)

- H1 confirmed if every core party's defection collapses the triad.
- H2 confirmed if the spectator's defection leaves the major complex unchanged.
- H3 confirmed if all three core parties veto while their Shapley values are unequal.
- H4 confirmed if the recipient pair's value is below both mediator pairs' values.
