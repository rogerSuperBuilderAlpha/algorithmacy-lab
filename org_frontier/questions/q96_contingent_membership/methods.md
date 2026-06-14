# Q96 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict (`classifier`) and major complex (`probes.lib.major_complex`). Run on
`~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Worker E, mediator M, recipient R, gate T.
- **contingent** — M'=E∧(R∨¬T), T'=E, E'=M, R'=M. The mediator reads the recipient only when the gate is
  on, and the gate tracks the worker, so the recipient is in the determination contingently.
- **always** — M'=E∧R (gate always on; the read-recipient triad). Control.
- **never** — M'=E (gate always off; broadcast). Control.

## Decision rules (`probe_contingent_membership.py`)

- H1 confirmed if the contingent form is triadic.
- H2 confirmed if the contingent form's Φ is below 2.0.
- H3 confirmed if the recipient is in the contingent major complex.
- H4 confirmed if the gate is in the contingent major complex.
