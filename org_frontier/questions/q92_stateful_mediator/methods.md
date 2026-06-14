# Q92 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict (`classifier`) and major complex (`probes.lib.major_complex`). Run on
`~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Worker E, mediator M, recipient R, memory Mem.
- **live** — M'=E∧R, E'=M, R'=M (the read-recipient triad, Φ = 2).
- **tracking_memory** — M'=E∧Mem, Mem'=R, E'=M, R'=M (M reads a memory that holds R's previous value).
- **frozen_memory** — as tracking, but Mem'=Mem (the memory does not track R).
- **self_memory** — M'=E∧M, E'=M, R'=M (M reads the worker and its own previous state; R feeds nothing).

## Decision rules (`probe_stateful_mediator.py`)

- H1 confirmed if tracking_memory is triadic.
- H2 confirmed if frozen_memory is dyadic.
- H3 confirmed if self_memory is dyadic.
- H4 confirmed if the memory node is in the tracking_memory major complex.
