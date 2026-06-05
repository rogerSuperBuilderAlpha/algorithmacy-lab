# Q57 — Stage 4 methods

For each hypothesis: the form or ensemble, the measure, the controls, and the decision rule fixed before
the run.

## Shared infrastructure
- Reuse Q56: `mip_geometry_utils.py` (ceiling panel, partition scan, min normalized_phi, official ties).
- Reuse Q55: `discriminator_utils.py` (aligned one-sided ceiling subset).
- Reuse Q54: `mechanism_utils.py` (topology application, instrument control).
- Q57 extensions: `direction_mip_utils.py` (back-channel recipient, expected tied cut, norm ratio helpers).
- Verdict / Phi: `org_frontier/classifier/classifier.py`, PyPhi `evaluate_partition`.
- Python: repo `venv`, PyPhi IIT-4.0, n=3 deterministic Boolean, synchronous update, labels `("W","S","C")`.

## Instrument control (run first)
Canonical triad `W'=S`, `S'=W∧C`, `C'=S` — rules `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]`.
Must read **triadic**, max_phi = 2.0, MIP `2 parts: {W,SC}`. Abort if it fails.

## Test ensemble
- Sixteen aligned one-sided bijective parity ceiling pairs from Q56 (#181): worker_xor, counterpart_xor,
  worker_xnor, counterpart_xnor on eight matched implication forms at Phi=2.0.
- Back-channel recipient: under worker topologies the recipient is W (W' gains input from C); under
  counterpart topologies the recipient is C (C' gains input from W).
- Expected tied cut: recipient W → `2 parts: {W,SC}`; recipient C → `2 parts: {WS,C}`.

## Partition-type vocabulary
- Outer-party two-part: `2 parts: {W,SC}` (W singleton), `2 parts: {WS,C}` (C singleton).
- Complete: `3 parts: {W,S,C}`.
- Official tie set: `sia.ties` at max-Phi state via `mip_ties`.
- Minimum normalized_phi: minimum `normalized_phi` from `evaluate_partition` per partition type at system Phi.

## H1 test — back-channel recipient seam rule
- **Ensemble:** sixteen aligned one-sided ceiling pairs.
- **Measure:** back-channel recipient party; official tied outer cut; match flag.
- **Controls:** instrument control.
- **Decision rule:** H1 confirmed if all sixteen pairs tie the cut isolating the recipient outer party.
  H1 refuted if any pair ties the non-recipient singleton. H1 partial if fifteen of sixteen match.
- **Script:** `probe_recipient_seam_rule.py`

## H2 test — dual at-system Phi with norm split
- **Ensemble:** sixteen aligned one-sided ceiling pairs.
- **Measure:** at-system-Phi flags for both outer cuts; min normalized_phi on tied vs excluded outer cuts
  and complete.
- **Controls:** instrument control.
- **Decision rule:** H2 confirmed if all sixteen have both outer cuts at system Phi, tied outer norm 0.5,
  excluded outer norm 1.0. H2 refuted on any missing dual at-system or norm deviation. H2 partial if
  fifteen of sixteen match all three conditions.
- **Script:** `probe_dual_norm_split.py`

## H3 test — two-to-one normalized_phi ratio
- **Ensemble:** sixteen aligned one-sided ceiling pairs.
- **Measure:** ratio excluded_norm / tied_norm on the two outer-party cuts at system Phi.
- **Controls:** instrument control.
- **Decision rule:** H3 confirmed if all sixteen pairs have ratio 2.0 within 1e−6. H3 refuted if any pair
  deviates. H3 partial if fifteen of sixteen at ratio 2.0.
- **Script:** `probe_norm_ratio.py`

## H4 test — complete shares tied outer minimum
- **Ensemble:** sixteen aligned one-sided ceiling pairs.
- **Measure:** complete min normalized_phi vs tied outer min normalized_phi.
- **Controls:** instrument control.
- **Decision rule:** H4 confirmed if complete norm equals tied outer norm on all sixteen within 1e−6. H4
  refuted on any mismatch. H4 partial if fifteen of sixteen equal.
- **Script:** `probe_complete_norm_equal.py`

## H5 test — gate-invariant direction rule
- **Ensemble:** sixteen aligned one-sided ceiling pairs split by topology prefix (eight worker, eight
  counterpart).
- **Measure:** official tied outer cut by topology class.
- **Controls:** instrument control; Q55 #179 XNOR alignment flip as gate baseline.
- **Decision rule:** H5 confirmed if eight of eight worker topologies tie `{W,SC}` and eight of eight
  counterpart tie `{WS,C}`. H5 refuted if any worker ties `{WS,C}` or any counterpart ties `{W,SC}`. H5
  partial if one violation across sixteen.
- **Script:** `probe_gate_invariant_direction.py`
