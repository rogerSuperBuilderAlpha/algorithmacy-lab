# Q114 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 Shapley value of subsystem-Φ (Q111). Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Worker E, mediator M, recipient R, principal P:
- **bidirectional** — M'=E∧R∧P, P'=M (P is read by the mediator and reads it; P is in the core, Finding 8).
- **monitor_only** — M'=E∧R, P'=M (P reads the mediator but is not read; P is outside the core).

The base triad (no principal) is the read-recipient triad. `shapley_for` computes each party's Shapley
value with the coalition value the subsystem's Φ.

## Decision rules (`probe_principal_rent.py`)

- H1 confirmed if the bidirectional principal's Shapley value is positive.
- H2 confirmed if the monitor-only principal's Shapley value is at most zero.
- H3 confirmed if no existing party's Shapley value falls below its base-triad value.
- H4 confirmed if the bidirectional principal's Φ exceeds 2.0.
