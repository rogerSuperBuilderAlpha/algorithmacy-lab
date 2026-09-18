# construct_gates_n5 — hypotheses (fixed before computing)

**Question.** Do GATE_SPLITS regimes B (XOR: flip, Φ≪n−1) and C
(MAJ: no flip) transfer from HMC anchors to CMC and AI-MC full-bind
at n=5?

**Already known.**
- HMC gate arm (`encoding_ladder_gates` GATE_SPLITS_LADDER;
  `ladder_gate_properties` MONO_EXTREMAL_VS_AFFINE): AND→A (Φ=n−1);
  XOR→B (flip Φ=0.125); MAJ→C (no flip).
- Construct arm (`construct_ladders_n5` BOUNDARY_TRANSFERS): CMC/AI-MC
  match HMC on monotone AND/OR full-bind.
- Synthesis: `CONSTRUCT_LADDER_ARC.md` — non-monotone transfer is the
  open cell.

**Universe.** Binary exact IIT-4.0. n=5. Full-bind only (cheapest):
AND control + XOR + MAJ (≥3/4) on CMC `("W","S","C","D","E")` and
AI-MC `("W","A","C","D","E")`. HMC numbers cited from
`encoding_ladder_gates` (not re-laddered).

## H1 — XOR transfers Regime B

On CMC and AI-MC full XOR: whole triadic, n_core=5, Φ ≪ n−1 (≪1).
Null: some family stays Φ≈4 or fails to flip.

## H2 — MAJ transfers Regime C

On CMC and AI-MC full MAJ: no algorithmacy flip (not whole-triadic
n_core=5). Null: some family flips.

## H3 — some family morphs

At least one of H1/H2 fails on a family (construct-dependent gate
regime). Null: both families match HMC B/C.
