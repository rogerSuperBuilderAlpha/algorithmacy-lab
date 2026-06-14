# Q58 — Stage 4 methods

## Ensemble and controls

- **Panel:** Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56 (`one_sided_ceiling()`).
- **Reuse:** Q56 `mip_geometry_utils.py` (ceiling panel, partition scan); Q57 `direction_mip_utils.py`
  (recipient/non-recipient cut identification, norm fields).
- **Q58 extension:** `norm_cut_utils.py` (min-norm partition detail: phi, normalized_phi,
  `normalization_factor`, `cut_ones` from `partition._cut_matrix`).
- **Instrument control:** Canonical triad `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` must
  read triadic, max_phi=2.0, MIP first line `2 parts: {W,SC}`. Abort if control fails.

## PyPhi normalization access

For each partition type at system Phi, scan all `system_partitions`, keep entries with
`abs(evaluate_partition(...).phi - sys_phi) < 1e-6`, and take the minimum `normalized_phi` row (matching
Q56–Q57 `min_norm`). On that row:

- `phi` — unnormalized integrated information
- `normalized_phi` — IIT-4.0 normalized value (`phi × normalization_factor`)
- `normalization_factor` — via `pyphi.new_big_phi.normalization_factor(partition)` (= `1 / sum(cut_matrix)`
  for `GeneralKCut`)
- `cut_ones` — `int(sum(partition._cut_matrix))`

Recipient (tied) and non-recipient (excluded) cuts follow Q57 `expected_tied_cut` /
`excluded_outer_cut`.

## H1 test — severed-connection count ratio

- **Measure:** `cut_ones_tied / cut_ones_excl` on min-norm at-system-Phi partitions.
- **Decision rule:** Confirmed if 16/16 pairs at ratio 2.0 within `PHI_TOL=1e-6` and spread 0; partial if
  all 16 at 2.0 but spread > 0; refuted otherwise.

## H2 test — normalization factor ratio

- **Measure:** `norm_factor_excl / norm_factor_tied` on the same min-norm rows.
- **Decision rule:** Confirmed if 16/16 at ratio 2.0 with spread 0; partial if all 16 at 2.0; refuted
  otherwise.

## H3 test — equal unnormalized phi

- **Measure:** `phi_tied / phi_excl` on min-norm at-system-Phi rows.
- **Decision rule:** Confirmed if 16/16 at ratio 1.0; partial if 15/16; refuted if any pair differs beyond
  tolerance.

## H4 test — complete shares recipient geometry

- **Measure:** compare `cut_ones` and `norm_factor` on complete min-norm vs recipient singleton min-norm.
- **Decision rule:** Confirmed if 16/16 pairs match both fields; partial if cut_ones match but norm_factor
  differs on ≤1 pair; refuted otherwise.

## H5 test — inverse cut-size law

- **Measure:** `norm_phi_excl / norm_phi_tied` vs `cut_ones_tied / cut_ones_excl`; require equality within
  `PHI_TOL`.
- **Decision rule:** Confirmed if 16/16 pairs satisfy the identity; partial if 15/16; refuted otherwise.
