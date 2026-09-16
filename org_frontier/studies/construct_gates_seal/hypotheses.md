# construct_gates_seal — hypotheses (fixed before computing)

**Question.** Do XNOR (Regime B) and mixed-polarity extremal
(AND_negE / AND_negC-style, Regime C) transfer on a CMC full-bind at
n=5, sealing GATE_REGIMES_TRANSFER?

**Already known.**
- `construct_gates_n5` GATE_REGIMES_TRANSFER: CMC/AI-MC XOR→B, MAJ→C,
  AND→A.
- HMC: XNOR→B Φ=0.125 (`encoding_ladder_gates`); AND_negC→C
  (`ladder_gate_properties`).
- Open cell in `CONSTRUCT_LADDER_ARC.md`: optional XNOR / mixed-polarity
  seal.

**Universe.** Binary exact IIT-4.0. n=5. Minimal cells: CMC
`("W","S","C","D","E")` full-bind XNOR and AND_negE
(`S=W∧C∧D∧¬E`). AI-MC same two cells if cheap. HMC cited, not re-run.

## H1 — XNOR → Regime B

CMC (and AI-MC if run) full XNOR: whole triadic, n_core=5, Φ ≪ 1.
Null: Φ≈n−1 or no flip.

## H2 — mixed-polarity → Regime C

CMC (and AI-MC if run) full AND_negE: no algorithmacy flip (not
whole-triadic n_core=5 with Φ≈n−1). Null: Regime A or B.

## H3 — surprise flip

Either cell morphs relative to HMC anchors. Null: both match B/C.
