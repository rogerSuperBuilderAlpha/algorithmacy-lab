# Q58 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses spanning the normalization mechanism behind Q57's fixed two-to-one ratio. Written
and committed before any test runs.

## H1 — Severed-connection count ratio
- **Claim:** On min-norm at-system-Phi partitions, the recipient singleton severs exactly twice as many
  cut-matrix ones as the non-recipient singleton (`cut_ones_tied / cut_ones_excl = 2.0`).
- **H0:** The severed-connection ratio differs from 2.0 on at least one pair.
- **Predicted outcome:** 16/16 pairs at ratio 2.0 with spread 0.

## H2 — Normalization factor ratio
- **Claim:** PyPhi's `normalization_factor` on the excluded min-norm partition is exactly twice that on
  the tied partition (`norm_factor_excl / norm_factor_tied = 2.0`), because
  `normalized_phi = phi × normalization_factor` and `normalization_factor = 1 / cut_ones`.
- **H0:** The normalization-factor ratio differs from 2.0 on at least one pair.
- **Predicted outcome:** 16/16 pairs at ratio 2.0 with spread 0.

## H3 — Equal unnormalized phi baseline
- **Claim:** Both outer cuts reach identical unnormalized phi at system level on every pair
  (`phi_tied / phi_excl = 1.0`); the 2.0 normalized_phi ratio is not driven by phi asymmetry.
- **H0:** Unnormalized phi differs between tied and excluded outer cuts on at least one pair.
- **Predicted outcome:** 16/16 pairs with phi ratio 1.0.

## H4 — Complete shares recipient cut geometry
- **Claim:** The complete partition's min-norm at-system-Phi entry shares the recipient singleton's
  `cut_ones` count and `normalization_factor` on all sixteen pairs.
- **H0:** Complete min-norm cut geometry differs from the recipient singleton on at least one pair.
- **Predicted outcome:** 16/16 pairs with matching `cut_ones` and `norm_factor`.

## H5 — Inverse cut-size law for normalized_phi
- **Claim:** The normalized_phi ratio equals the inverse severed-connection ratio
  (`norm_phi_excl / norm_phi_tied = cut_ones_tied / cut_ones_excl`), confirming the IIT-4.0
  `NUM_CONNECTIONS_CUT` rule as the sole source of the fixed 2.0 split.
- **H0:** The normalized_phi ratio deviates from the inverse cut-ones ratio on at least one pair.
- **Predicted outcome:** 16/16 pairs with `norm_phi_ratio = cut_ones_ratio` within tolerance.
