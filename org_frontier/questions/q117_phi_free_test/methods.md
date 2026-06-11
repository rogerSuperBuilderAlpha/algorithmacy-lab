# Q117 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict as ground truth, against two Φ-free predicates, over the complete 256-form
strict-mediation family. Run on `~/iit-playground/venv-4.0/bin/python`; the full sweep computes in ~4s.

## The family (`q93.enumerate_family`)

Each strict-mediation form (outer worker W, mediator S, outer counterpart C) is eight bits: a 2-bit worker
read tW (W' = tW[S]), a 2-bit counterpart read tC (C' = tC[S]), and a 4-bit mediator table tS
(S' = tS[W | C<<1]). The 256 forms are all bit settings. The exact verdict is `q93.is_triadic`
(`classify_rules`, Φ over the MIP).

## Predicates (`forms.py`)

- **cycle_present** — topology only: tW and tC non-constant (both outer parties read the mediator), and tS
  depends on both its inputs (the mediator reads both outer parties). Read off which inputs each table uses.
- **phi_free_verdict** — the cycle plus a composition condition. A parity mediator (tS ∈ {XOR, XNOR}) binds
  whenever the cycle is present. A non-parity mediator binds iff `(tW identity == tC identity) != (tS
  asymmetric under input swap)`, where tW identity means W copies the mediator (0,1) rather than inverts it
  (1,0), and tS asymmetric means tS[1] ≠ tS[2].

## Decision rules (`probe_phi_free_test.py`)

- H1 confirmed if the cycle predicate has zero false negatives against the oracle.
- H2 confirmed if the cycle predicate has at least one false positive.
- H3 confirmed if `phi_free_verdict` has zero false positives and zero false negatives over all 256 forms.
- H4 confirmed if the full-cycle forms include both triadic and dyadic forms (a split within one wiring).
