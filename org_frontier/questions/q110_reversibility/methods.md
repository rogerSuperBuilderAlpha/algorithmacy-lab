# Q110 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict over the 256-form family. Run on `~/iit-playground/venv-4.0/bin/python`.

## Construction (`forms.py`)

The family is classified into 24 triadic and 232 dyadic forms (Q105). The fragility margin of a triadic
form is its minimal Hamming distance to any dyadic form; the construction distance of a dyadic form is its
minimal Hamming distance to any triadic form (Q105). The two distributions are compared.

## Decision rules (`probe_reversibility.py`)

- H1 confirmed if every triadic form has fragility margin 1.
- H2 confirmed if the maximal construction distance exceeds 1.
- H3 confirmed if the two distance distributions differ.
- H4 confirmed if the mean construction distance exceeds the mean fragility margin.
