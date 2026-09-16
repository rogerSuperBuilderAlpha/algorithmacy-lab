# ladder_gate_panel — hypotheses (fixed before computing)

**Question.** Does MONO_EXTREMAL_VS_AFFINE still predict regimes A/B/C on
a larger stratified panel of 4-input Boolean gates (not just the designed
16)?

**Rule under test** (`ladder_gate_properties`, 16/16):
```
if alldep ∧ affine:                 → B  (triadic, n_core=5, Φ≪n−1)
elif alldep ∧ monotone ∧ wt∈{1,15}: → A  (triadic, n_core=5, Φ=n−1)
else:                               → C  (no full 5-core flip)
```

**Universe.** Binary exact IIT-4.0. Labels `("W1","S","W2","W3","C")`
(n=5). Full joint bind only (all outers in S, all read S). Assist not
per-gate (budget). Stratified panel of 4-input truth tables:
- exhaust predicted-A (4) and predicted-B (2);
- exhaust all monotone (inc or dec);
- exhaust all extremal-weight wt∈{1,15};
- exhaust all affine;
- random sample from the residual cube (fixed seed).

Observed regime: A / B as above; **C = anything else** (dyadic or
partial triadic / incomplete core) — the algorithmacy flip requires
n_core=5.

## H1 — rule holds on the panel

Predicted regime matches observed regime for every panel gate.
Null: at least one mismatch.

## H2 — counterexamples appear

Some gate is misclassified (e.g. predicted C but observed A or B, or
predicted A/B but not). Null: no mismatches.

## H3 — refinement needed

Some gate lands in an ambiguous observed class (triadic n_core=5 with
Φ neither ≈n−1 nor ≪n−1), or mismatches cluster on a missing Boolean
property. Null: all gates land cleanly in A/B/C under the rule.
