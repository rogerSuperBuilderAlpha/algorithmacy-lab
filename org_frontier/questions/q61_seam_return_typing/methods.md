# Q61 — Stage 4 methods

## Ensemble and controls

- **Panel:** Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56 (`one_sided_ceiling()`),
  scanned as in Q56–Q59. All held at triadic max_phi=2.0 by Q54 commit-alignment (#173).
- **Reuse:** Q57 `direction_mip_utils.py` (recipient, `enriched_rows`, `tied_outer_cut`, `expected_tied_cut`);
  Q49 `seam.py` (MIP tie reading); Q60 `thompson_backchannel_utils.py` (`return_path_type`); Q56
  `mip_geometry_utils.py` (`OUTER_W`, `OUTER_C`, `instrument_control`).
- **Q61 extension:** `seam_return_utils.py` (singleton seam extraction, seam–type cross-tab, partition
  equality metrics).
- **Instrument control:** Canonical triad `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` must
  read triadic, max_phi=2.0, MIP first line `2 parts: {W,SC}`. Abort if control fails.

## Official singleton seam

For each panel row, read `tied_cut = tied_outer_cut(row)` from Q57 partition scan. Map partition string to
singleton party: `OUTER_W` (`2 parts: {W,SC}`) → `W`; `OUTER_C` (`2 parts: {WS,C}`) → `C`. Cross-check with
Q49 `seam_set(rules)`: the singleton set must be `{W}` or `{C}` on every triadic row (expected 16/16).

## Return-path typing (Q43 / Q60)

`thompson_type = return_path_type(rules, recipient)` with `recipient = back_channel_recipient(topology)` as
in Q60. Sequential when recipient W and cm[1,2]∧¬cm[0,2]; reciprocal when recipient C and cm[0,2].

## H1 test — seam tracks type bijection

- **Measure:** `seam_match = (singleton=='W' and thompson_type=='sequential') or (singleton=='C' and
  thompson_type=='reciprocal')`.
- **Decision rule:** Confirmed if 16/16 matches; partial if 15/16; refuted if ≤14/16 or any `other` typing.

## H2 test — co-extensive partitions

- **Measure:** partition equality — for each row, compare `(singleton, thompson_type)` assignment; count rows
  where both labels agree on subpanel membership.
- **Decision rule:** Confirmed if 16/16 partition equality and both labels yield 8+8; partial if 15/16;
  refuted if ≤14/16 or cell counts differ from 8+8.

## H3 test — seam not finer than type

- **Measure:** within-type seam heterogeneity — count sequential rows with C seam plus reciprocal rows with
  W seam.
- **Decision rule:** Confirmed (null: seam not finer) if heterogeneity count 0; partial if 1; refuted if ≥2.

## H4 test — seam not coarser than type

- **Measure:** within-seam type heterogeneity — count W-seam rows typed reciprocal plus C-seam rows typed
  sequential.
- **Decision rule:** Confirmed (null: seam not coarser) if heterogeneity count 0; partial if 1; refuted if
  ≥2.

## H5 test — seam recovers verdict-lost discrimination

- **Measure:** compare W-seam subpanel to sequential subpanel and C-seam subpanel to reciprocal subpanel;
  max_phi spread across all rows and within each subpanel.
- **Decision rule:** Confirmed if W-seam = sequential (8/8), C-seam = reciprocal (8/8), and max_phi spread
  0; partial if subpanel match 15/16 total; refuted if any subpanel mismatch or max_phi spread > PHI_TOL.
