# mixed_algebra_seats — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #3).** Do **mixed-algebra seats** (one seat
parity, one conjunctive) on a **single** mediator produce a hybrid
signature, or does the parity blind-spot (V2 #4 `BLINDSPOT_SURVIVES_RADIX`)
dominate the whole form?

**Already known (cited, not reopened).**
- **#113 / V2 #4:** parity (XOR/XNOR) commits are the cheap-measure blind
  spot; full-system Φ ≈ 0.5 vs conjunctive Φ = 2.0. Sum-mod-k keeps the
  low flat band — `BLINDSPOT_SURVIVES_RADIX`.
- **V2 #16 / V3 #6:** shared-mediator AND–AND merges at Φ = 2k.
- **V3 #1–#2:** five templates closed; majority collapses to redundancy.
- Faithful AND triad Φ=2.0; XOR triad Φ=0.5.

**Gap.** Pure seats are characterized. A single mediator with **one
conjunctive seat and one parity seat** (two party-pairs feeding one S)
was not asked whether the form hybrids or the parity blind-spot swallows
the whole-system signature.

**Universe.** Binary exact IIT-4.0. n≤5.

**Construction.** Labels (W1,C1,W2,C2,S); parties copy S.
- Conjunctive seat: a1 = W1 ∧ C1.
- Parity seat: a2 = W2 ⊕ C2 (or XNOR).
- Combine ⊙ ∈ {AND, OR, XOR}: S' = a1 ⊙ a2.

**Blind-spot dominates.** Every mixed cell has whole-system Φ in the
parity band (≤ 0.5+eps) or factors (dyadic / no full conjunctive
landmark Φ ∈ {2,3,4}). The conjunctive seat does not restore a
conjunctive whole-form Φ.

**Hybrid.** Some mixed cell is whole-system triadic with Φ strictly
between the parity band and the conjunctive landmark (0.5 < Φ < 2), or
full core spanning both seats at a novel Φ atom.

## H1 — pure anchors

AND triad: triadic, core Φ=2.0. XOR triad: triadic, core Φ=0.5.

## H2 — pure shared seats

Shared AND–AND: full-core triadic, Φ=4.0. Shared XOR–XOR (OR-combine):
whole Φ in parity band (≈0.5).

## H3 — mixed seats: no conjunctive whole landmark

On each mixed cell (AND⊙XOR for ⊙∈{AND,OR,XOR}; AND∧XNOR), whole-system
Φ is **not** in {2,3,4}. Either factors or sits in the parity band
(≤0.5+eps).

## H4 — panel verdict

H1–H3 hold and no mixed cell meets the hybrid criterion →
`BLINDSPOT_DOMINATES`.
Some mixed cell is hybrid → `HYBRID_SIGNATURE`.
H1 or H2 fails → `CONTROLS_FAIL`.
