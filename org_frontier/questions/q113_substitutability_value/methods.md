# Q113 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 Shapley value of subsystem-Φ (Q111). Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

The Q85 agent market at N = 2: the all-required market (every agent needed; triadic, Φ = 4) and the
substitutable market (agents interchangeable; dyadic, Φ = 0). For each, `shapley_for` computes the Shapley
value of each party with the coalition value the subsystem's Φ.

## Decision rules (`probe_substitutability_value.py`)

- H1 confirmed if the all-required market's Shapley total is positive.
- H2 confirmed if the substitutable market's Shapley total is zero.
- H3 confirmed if the all-required market's Shapley values are equal across parties.
- H4 confirmed if the value lost (all-required total minus substitutable total) equals the all-required Φ.
