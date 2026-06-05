# Q62 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses testing whether the excluded outer singleton cut carries independent return-path
signal after Q61 established tied-seam↔type co-extensiveness. Written and committed before any test runs.

## H1 — Excluded complement of tied singleton
- **Claim:** The excluded outer singleton party is always the complement of the tied singleton on every pair
  (tied W → excluded C; tied C → excluded W).
- **H0:** At least one pair where excluded singleton ≠ complement(tied singleton).
- **Predicted outcome:** 16/16 complement matches; 0 mismatches.

## H2 — Excluded inversely tracks return-path type
- **Claim:** Excluded singleton inversely mirrors return-path type: excluded C iff sequential, excluded W iff
  reciprocal — the inverse encoding of the tied-seam/type partition.
- **H0:** Excluded tracks type directly (same as tied: W+sequential, C+reciprocal) or mismatches on ≥2 pairs.
- **Predicted outcome:** 16/16 inverse matches; 0 direct matches with type.

## H3 — Excluded determined by tied seam
- **Claim:** Conditional on tied singleton, excluded is unique — no within-tied heterogeneity on excluded
  party.
- **H0:** At least one tied-singleton class contains both W and C excluded parties across different pairs.
- **Predicted outcome:** 0 within-tied excluded heterogeneity; W-tied rows all excluded C, C-tied rows all
  excluded W.

## H4 — No third independent joint label
- **Claim:** The triple (tied singleton, excluded singleton, return-path type) collapses to exactly two joint
  cells across the panel — no third independent partition dimension.
- **H0:** Three or more distinct joint signatures appear among the sixteen pairs.
- **Predicted outcome:** Exactly 2 joint cells: (W, sequential, C) on 8/8 and (C, reciprocal, W) on 8/8;
  distinct joint count 2.

## H5 — Excluded norm uniform, no Phi subpanel lift
- **Claim:** Excluded cut min normalized_phi is 1.0 on 16/16 and max_phi offers no discrimination between
  excluded-W and excluded-C subpanels despite the norm asymmetry.
- **H0:** Any excluded norm ≠ 1.0 or max_phi spread > PHI_TOL within excluded subpanels.
- **Predicted outcome:** 16/16 excluded norm 1.0; excluded-W subpanel mean max_phi 2.0 spread 0;
  excluded-C subpanel mean max_phi 2.0 spread 0.
