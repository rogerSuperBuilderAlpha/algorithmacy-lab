# Q95 — Stage 4 methods (fixed before computation)

Ground truth is the exact IIT-4.0 verdict (`classifier`), major complex (`probes.lib.major_complex`), and
the disjoint-complex tiling (reusing Q94's `max_disjoint_complexes`). Run on
`~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

The read-recipient triad is E'=M, M'=E∧R, R'=M (Φ = 2, core {E, M, R}). The composition shares one node:
the recipient of triad 1 is the sender of triad 2. Five nodes E1, M1, S, M2, R2 with E1'=M1, M1'=E1∧S,
S'=M1, M2'=S∧R2, R2'=M2. A single triad and two disjoint triads (six nodes) are the references.

## Decision rules (`probe_composition_of_triads.py`)

- H1 confirmed if the composed form is whole-system triadic.
- H2 confirmed if the composed form has one disjoint complex whose core contains a node from {E1, M1} and
  a node from {M2, R2}.
- H3 confirmed if the composed major-complex Φ exceeds 2.0.
- H4 confirmed if the shared node S is in the composed major complex.
