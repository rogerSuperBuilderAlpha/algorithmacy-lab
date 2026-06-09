# Q93 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on a margin-to-dyadic fragility metric for triadic forms. The verdict is binary at
Φ_MIP = 0, with no measure of how close a triadic form sits to collapse. For each of the 24 triadic forms
in the 256-form strict-mediation family, the metric counts how many of the eight single-bit truth-table
flips turn it dyadic; the robustness fraction is the share of flips that preserve the verdict. Written and
committed before the metric and the noise-survival comparison are read.

## H1 — Triadic forms sit on a structural edge

- **Claim:** A majority of triadic forms have at least one single-bit flip that collapses them to dyadic
  (margin-to-dyadic of one).
- **H0:** Fewer than half do.
- **Predicted outcome:** majority fragile. H0 refuted. (The corpus's recurring result is that a single
  edge or read toggles the verdict.)

## H2 — The margin is informative

- **Claim:** The robustness fraction varies across triadic forms, with a range of at least 0.25 between
  the most and least robust.
- **H0:** The range is below 0.25 (the metric is near-constant and carries little information).
- **Predicted outcome:** range at least 0.25. H0 refuted.

## H3 — The structural margin predicts noise survival

- **Claim:** The robustness fraction rank-separates forms by their exact Φ under noise 0.1: the rank-AUC
  of robustness predicting above-median noise-Φ is at least 0.60.
- **H0:** rank-AUC below 0.60 (structural margin and noise survival are unrelated).
- **Predicted outcome:** at least 0.60 — a structural margin computed without any dynamics predicts the
  Q71 robustness. This is the study's central and genuinely uncertain claim.

## H4 — Parity mediators give the robust triads

- **Claim:** The mean robustness of triadic forms whose mediator is a parity function (XOR/XNOR) exceeds
  that of forms whose mediator is monotone (AND/OR/NAND/NOR).
- **H0:** Parity-mediator robustness does not exceed monotone-mediator robustness.
- **Predicted outcome:** parity exceeds monotone — extending Finding 4 (parity supports irreducibility
  most readily) from frequency to robustness.
