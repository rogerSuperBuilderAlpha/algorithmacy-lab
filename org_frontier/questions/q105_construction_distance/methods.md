# Q105 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict (`classifier.classify_rules`) on the 256-form strict-mediation family. Run on
`~/iit-playground/venv-4.0/bin/python`.

## Construction (`forms.py`)

Each form is eight bits: the worker's read (bits 0-1), the counterpart's read (bits 2-3), the mediator's
two-input function (bits 4-7). The family is classified into 232 dyadic and 24 triadic forms. The
construction distance of a dyadic form is its minimal Hamming distance to any triadic form; a distance-1
build is recorded with the bit position that achieves it.

## Decision rules (`probe_construction_distance.py`)

- H1 confirmed if the broadcast has construction distance 1 reached by a mediator bit (4-7).
- H2 confirmed if more than half the dyadic forms are within construction distance 2.
- H3 confirmed if the construction distance takes at least two distinct values.
- H4 confirmed if more than half the distance-1 dyadic forms are built by flipping a mediator bit.
