# Q115 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 Shapley value of subsystem-Φ (Q111), applied to the Q85 all-required market at N = 2, 3, 4.
Run on `~/iit-playground/venv-4.0/bin/python`. N = 4 (six nodes) takes ~21s; the full probe ~25s.

## Forms (`forms.py`)

The Q85 all-required market: a worker E and a counterpart C, both of whom require all N agents M1..MN
(E' = C' = M1 ∧ ... ∧ MN), and each agent commits when E and C agree (Mi' = E ∧ C). The two outer parties (E,
C) are unique; the N agents are interchangeable but all required. `market_shapley(N)` reuses Q111's
`shapley` with the coalition value the subsystem's Φ, and reads off one outer party's value (E) and one
agent's (M1); by symmetry the other outer party and the other agents match.

## Decision rules (`probe_market_value.py`)

- H1 confirmed if |Σ Shapley − Φ| < 0.01 at N = 2, 3, 4.
- H2 confirmed if the outer party's value exceeds the agent's at N = 3 and N = 4.
- H3 confirmed if the outer party's value is strictly increasing across N = 2, 3, 4.
- H4 confirmed if the agent's value at N = 4 does not exceed its value at N = 2.
