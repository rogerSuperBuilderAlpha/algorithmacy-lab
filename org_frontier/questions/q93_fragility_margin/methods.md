# Q93 — Stage 4 methods (fixed before computation)

Ground truth is the exact IIT-4.0 verdict (`classifier.classify_rules`) and exact Φ
(`probes.lib.max_phi_float`). Run on `~/iit-playground/venv-4.0/bin/python`.

## The family and the perturbation (`forms.py`)

The 256 strict-mediation three-node forms, each parametrized by eight truth-table bits: a 2-bit read for
each outer party off the mediator, and a 4-bit mediator function of the two outer parties. The 24 triadic
forms are the subject. For each, the structural margin flips one of the eight bits at a time, rebuilds the
form, and reclassifies; the number of flips that turn the form dyadic is its collapse count, and the
robustness fraction is `(8 − collapses) / 8`. The mediator function is labelled parity (XOR/XNOR),
monotone (AND/OR/NAND/NOR), or other. Noise survival is the exact Φ of the deterministic TPM mixed toward
its flipped output by noise 0.1.

## Measures and decision rules

- H1 confirmed if more than half of the triadic forms have at least one collapsing single-bit flip.
- H2 confirmed if the robustness fraction's range across triadic forms is at least 0.25.
- H3 confirmed if the rank-AUC of robustness predicting above-median noise-Φ is at least 0.60.
- H4 confirmed if the mean robustness of parity-mediator triadic forms exceeds that of monotone-mediator
  ones.
