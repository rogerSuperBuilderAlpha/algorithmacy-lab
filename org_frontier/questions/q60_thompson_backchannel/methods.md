# Q60 — Stage 4 methods

## Ensemble and controls

- **Panel:** Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56 (`one_sided_ceiling()`),
  scanned as in Q56–Q59. All held at triadic Φ=2.0 by Q54 commit-alignment (#173).
- **Reuse:** Q59 `cut_edge_utils.py` (edge templates, `edge_detail_rows`); Q57 `direction_mip_utils.py`
  (recipient identification); Q43 `probe_thompson_primitives.py` (`has_feedback_cycle`).
- **Q60 extension:** `thompson_backchannel_utils.py` (return-path Thompson typing, template matching,
  panel enrichment).
- **Instrument control:** Canonical triad `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` must
  read triadic, max_phi=2.0, MIP first line `2 parts: {W,SC}`. Abort if control fails.

## Return-path Thompson typing (Q43 H3/H4 convention)

For each panel row, read `recipient` from Q57 `back_channel_recipient(topology)` and connectivity matrix
`cm = cm_from_rules(rules)`:

- **Sequential (propagating return):** recipient is W and the non-recipient party C depends on mediator S
  (`cm[1,2]=1`) but not on W directly (`cm[0,2]=0`). The far end retains the Q43 propagating-chain return
  path while W receives the back-channel cross-edge.
- **Reciprocal (direct cross return):** recipient is C and C depends on W directly (`cm[0,2]=1`) in addition
  to S. The recipient party reads the cross-party edge, matching Q43's reciprocal direct-coupling reading.

Any row failing both patterns is labeled `other` (expected count 0).

## Mediator-severance template (Q59)

From Q59 `expected_templates(topology)`: worker-recipient topologies match
`only_tied={S→W, W→C, W→S}`, `only_excl={C→S}`; counterpart-recipient topologies match
`only_tied={C→S, C→W, S→C}`, `only_excl={W→S}`. Template match requires frozenset equality on both sets
from Q59 `edge_detail_rows()`.

## H1 test — return-path typing tracks recipient

- **Measure:** `thompson_type = return_path_type(rules, recipient)`; compare to recipient party.
- **Decision rule:** Confirmed if 8/8 worker→sequential and 8/8 counterpart→reciprocal with 0 `other`;
  partial if 15/16 correct; refuted if any `other` or ≥2 recipient mismatches.

## H2 test — uniform triadic verdict

- **Measure:** `verdict(rules).structure` and `.max_phi` for each row.
- **Decision rule:** Confirmed if 16/16 triadic and max_phi=2.0 within PHI_TOL; partial if 15/16; refuted
  if any dyadic or Φ deviation.

## H3 test — feedback-cycle predicate collapse

- **Measure:** `has_feedback_cycle(rules)` from Q43; count cycle=True vs False.
- **Decision rule:** Confirmed if 16/16 cycle=True (all reciprocal by cycle predicate, none sequential);
  partial if 15/16; refuted if fewer than 16 cycle=True.

## H4 test — Thompson type tracks template

- **Measure:** for each row, compare `return_path_type` to `expected_templates` worker/counterpart classes.
- **Decision rule:** Confirmed if 16/16 sequential rows match worker template and reciprocal rows match
  counterpart template; partial if 15/16; refuted if ≥2 mismatches.

## H5 test — no Φ discrimination between subpanels

- **Measure:** max_phi and structure within sequential (8) and reciprocal (8) subpanels; spread across each
  subpanel and between subpanel means.
- **Decision rule:** Confirmed if both subpanels are uniformly triadic at max_phi=2.0 with spread 0; partial
  if spread >0 but all triadic; refuted if subpanels differ in structure or mean max_phi.
