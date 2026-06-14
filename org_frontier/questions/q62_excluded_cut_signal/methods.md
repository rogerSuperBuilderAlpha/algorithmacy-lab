# Q62 — Stage 4 methods

## Ensemble and controls

- **Panel:** Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56 (`one_sided_ceiling()`),
  scanned as in Q56–Q59. All held at triadic max_phi=2.0 by Q54 commit-alignment (#173).
- **Reuse:** Q57 `direction_mip_utils.py` (`enriched_rows`, `tied_outer_cut`, `excluded_outer_cut`,
  `norm_fields`, `EXCLUDED_NORM`); Q60 `thompson_backchannel_utils.py` (`return_path_type`); Q61
  `seam_return_utils.py` (`official_singleton`, `seam_type_match`); Q56 `mip_geometry_utils.py`
  (`OUTER_W`, `OUTER_C`, `PHI_TOL`, `instrument_control`).
- **Q62 extension:** `excluded_cut_utils.py` (excluded singleton extraction, complement/inverse cross-tabs,
  joint-label counting).
- **Instrument control:** Canonical triad `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` must
  read triadic, max_phi=2.0, MIP first line `2 parts: {W,SC}`. Abort if control fails.

## Excluded singleton extraction

For each panel row, read `tied_cut = tied_outer_cut(row)` from Q57 partition scan and
`excl_cut = excluded_outer_cut(tied_cut)`. Map partition string to singleton party: `OUTER_W` → `W`;
`OUTER_C` → `C`. Cross-check: `excluded_singleton` must equal complement of `tied_singleton` from Q61
`official_singleton(row)`.

## Return-path typing (Q43 / Q60)

`thompson_type = return_path_type(rules, recipient)` with `recipient = back_channel_recipient(topology)` as
in Q60.

## H1 test — excluded complement of tied

- **Measure:** `complement_match = (tied=='W' and excluded=='C') or (tied=='C' and excluded=='W')`.
- **Decision rule:** Confirmed if 16/16 complement matches; partial if 15/16; refuted if ≤14/16.

## H2 test — excluded inversely tracks type

- **Measure:** `inverse_match = (excluded=='C' and thompson_type=='sequential') or (excluded=='W' and
  thompson_type=='reciprocal')`; `direct_match` counts rows where excluded tracks type like tied.
- **Decision rule:** Confirmed if 16/16 inverse matches and 0 direct matches; partial if 15/16 inverse;
  refuted if ≤14/16 inverse or any direct match.

## H3 test — excluded determined by tied

- **Measure:** within-tied excluded heterogeneity — count W-tied rows with excluded W plus C-tied rows with
  excluded C.
- **Decision rule:** Confirmed if heterogeneity count 0; partial if 1; refuted if ≥2.

## H4 test — no third independent joint label

- **Measure:** distinct joint signatures `(tied, thompson_type, excluded)` across panel; count rows per cell.
- **Decision rule:** Confirmed if exactly 2 distinct joints with 8+8 split matching (W,seq,C) and
  (C,rec,W); partial if 2 joints but 7+9 split; refuted if ≥3 distinct joints or cell counts diverge from
  8+8.

## H5 test — excluded norm uniform, no Phi subpanel lift

- **Measure:** `excl_norm` from `norm_fields(row)`; max_phi spread across panel and within excluded-W and
  excluded-C subpanels.
- **Decision rule:** Confirmed if 16/16 excluded norm 1.0 and both excluded subpanels max_phi spread 0;
  partial if 15/16 norm match; refuted if ≤14/16 norm match or any subpanel max_phi spread > PHI_TOL.
