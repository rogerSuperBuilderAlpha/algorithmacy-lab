# Q210 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses, each with its null and predicted outcome, committed before any test runs.

Two conjunctive triads share one counterpart C. Node order (n=5): W1, S1, W2, S2, C. Mediator one reads
worker one and the shared counterpart (`S1'=W1∧C`); mediator two reads worker two and the same counterpart
(`S2'=W2∧C`); each worker reads its mediator (`W1'=S1`, `W2'=S2`). The shared counterpart reads the two
mediators through a **bridge**, swept three ways: **none** `C'=S1` (C updates from mediator one only),
**AND** `C'=S1∧S2` (C commits only when both mediators fire), **OR** `C'=S1∨S2` (C commits when either
fires). The reference single triad F0 is `W'=S, S'=W∧C, C'=S`, triadic at Φ_MIP=2.0.

## H1 — Instrument control
- **Claim:** F0 reads triadic with Φ_MIP = 2.0.
- **H0:** —
- **Predicted outcome:** triadic, max_phi = 2.000000. No comparison number is trusted unless this passes.

## H2 — A shared counterpart merges the two triads into one core
- **Claim:** Under the AND bridge, the major complex spans both triads: it contains both mediators S1 and
  S2, not a single-triad subset.
- **H0:** The major complex is a single triad ({W1,S1,C} or {W2,S2,C}); the two stay separate.
- **Predicted outcome:** {S1, S2} ⊆ `major_complex(AND).core`.

## H3 — The shared counterpart is the bridge member
- **Claim:** C is in the merged core under the AND bridge.
- **H0:** C is excluded from the core.
- **Predicted outcome:** "C" ∈ `major_complex(AND).core`.

## H4 — Merging two triads is super-additive in Φ
- **Claim:** The merged core under the AND bridge carries more integration than a single triad: core Φ > 2.0.
- **H0:** The merged core carries Φ ≤ 2.0, no more than one triad.
- **Predicted outcome:** `major_complex(AND).core_phi` > 2.0 + PHI_EPS.

## H5 — The bridge rule changes the merge
- **Claim:** How the counterpart combines the two mediators changes the merged core's integration: the AND
  bridge yields a higher core Φ than the OR bridge, because AND requires both mediators and couples them
  more tightly.
- **H0:** The AND and OR bridges give the same core Φ; the combination rule does not matter.
- **Predicted outcome:** `major_complex(AND).core_phi` > `major_complex(OR).core_phi` + PHI_EPS.
