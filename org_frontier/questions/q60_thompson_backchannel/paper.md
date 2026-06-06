# Q60 — Thompson back-channel typing

## Question

Among aligned one-sided back-channel forms held at triadic Φ=2.0, does Thompson's sequential/reciprocal
interdependence label track the recipient party's mediator-severance template, or does the uniform triadic
verdict collapse interdependence typing once the back-channel is present?

## Panel

Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56. Instrument control: canonical triad
reads triadic, max_phi=2.0, MIP `2 parts: {W,SC}`.

## Methods

Return-path Thompson typing follows Q43 H3: sequential when worker is back-channel recipient and counterpart
reads mediator S but not W directly; reciprocal when counterpart is recipient and reads W directly.
Mediator-severance templates from Q59 `edge_detail_rows()`. Feedback-cycle predicate from Q43
`has_feedback_cycle()`.

## Results

### H1 — Return-path typing tracks recipient

Worker-recipient pairs read sequential on 8/8; counterpart-recipient pairs read reciprocal on 8/8. Other
typing 0/16. Recipient match 16/16.

### H2 — Uniform triadic verdict

Triadic structure on 16/16. max_phi=2.0 on 16/16. Spread 0. Thompson Φ-ordering between sequential and
reciprocal collapses at the verdict level.

### H3 — Feedback-cycle predicate collapse

feedback_cycle=True on 16/16. Sequential by cycle predicate 0/16. The cycle predicate assigns every form
reciprocal and cannot split worker vs counterpart halves.

### H4 — Thompson type tracks mediator-severance template

Template match 16/16. Sequential subpanel matches worker template {S→W, W→C, W→S} vs {C→S} on 8/8.
Reciprocal subpanel matches counterpart template {C→S, C→W, S→C} vs {W→S} on 8/8.

### H5 — No Φ discrimination between subpanels

Sequential subpanel: triadic, mean max_phi=2.0, spread 0. Reciprocal subpanel: triadic, mean max_phi=2.0,
spread 0.

## Synthesis

The back-channel panel reconnects Q43 interdependence typing to Q59 cut geometry. Return-path
sequential/reciprocal and recipient mediator-severance templates are co-extensive on sixteen pairs. The
uniform triadic verdict and the feedback-cycle predicate both collapse typing discrimination; return-path
typing preserves the recipient partition the verdict loses.

## Validation gap

Deterministic n=3 Boolean models at finest grain with synchronous update. Results hold about the Boolean
models; real organizations remain beyond reach.

## Reproduce

```bash
python -m org_frontier.questions.q60_thompson_backchannel.probe_return_path_tracks_recipient
python -m org_frontier.questions.q60_thompson_backchannel.probe_uniform_triadic_verdict
python -m org_frontier.questions.q60_thompson_backchannel.probe_cycle_collapse
python -m org_frontier.questions.q60_thompson_backchannel.probe_type_tracks_template
python -m org_frontier.questions.q60_thompson_backchannel.probe_no_phi_discrimination
```
