# Q97 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict (`classifier`) and major complex (`probes.lib.major_complex`). Run on
`~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

The read-recipient triad (E, M, R) with two external agents X1, X2, in four configurations:
- **two_read_only** — X1, X2 each read the mediator, read by none.
- **two_emit_only** — a broadcast base (M'=E) with X1, X2 as constant sources the core does not read.
- **external_loop** — X1 reads M, M reads X2 (M'=E∧R∧X2), X2 reads X1; the coalition bridges the core on
  both sides while each member is unidirectional with respect to the core directly.
- **single_bidir** — one bidirectional-pivotal agent (M'=E∧R∧X, X'=M); the Q84 control.

## Decision rules (`probe_coordinated_adversary.py`)

- H1 confirmed if two_read_only is triadic with core {E, M, R}.
- H2 confirmed if two_emit_only is dyadic.
- H3 confirmed if external_loop's core is {E, M, R} or contains X2 (no influence without membership).
- H4 confirmed if single_bidir is triadic with X in the core.
