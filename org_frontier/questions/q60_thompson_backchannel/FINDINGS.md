# Q60 — findings

Thompson sequential/reciprocal interdependence against the Q59 back-channel mediator-severance templates.
Sixteen aligned one-sided ceiling pairs, all triadic at max_phi=2.0. Instrument control passed in every
probe: triadic, max_phi=2.000000, MIP `2 parts: {W,SC}`.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 return-path tracks recipient | confirmed | worker→sequential 8/8; counterpart→reciprocal 8/8; other 0/16; recipient match 16/16. |
| H2 uniform triadic verdict | confirmed | triadic 16/16; max_phi=2.0 on 16/16; spread 0. |
| H3 cycle predicate collapse | confirmed | feedback_cycle=True on 16/16; sequential by cycle 0/16. |
| H4 type tracks template | confirmed | template match 16/16; sequential 8/8 worker template; reciprocal 8/8 counterpart template. |
| H5 no Phi discrimination | confirmed | sequential subpanel triadic mean 2.0 spread 0; reciprocal subpanel triadic mean 2.0 spread 0. |

**Through-line.** Q43 return-path typing and Q59 recipient mediator-severance templates are the same
partition on the back-channel panel: worker-recipient halves read sequential with worker edge template;
counterpart-recipient halves read reciprocal with counterpart template. The IIT verdict offers no
sequential-vs-reciprocal discrimination — every form reads triadic at max_phi=2.0. Q43's feedback-cycle
predicate assigns all sixteen forms reciprocal, so cycle presence alone cannot track the recipient split
that return-path typing preserves. Interdependence typing survives at partition-template level after the
back-channel raises every form to the triadic ceiling; it does not survive at the verdict or cycle-predicate
level.

**Caveats.** n=3 deterministic Boolean models, AND/implication family with bijective parity back-channels;
return-path typing follows Q43 H3 conventions applied to back-channel connectivity. Real organizations
remain beyond reach.

**Reproduce.**

```bash
python -m org_frontier.questions.q60_thompson_backchannel.probe_return_path_tracks_recipient
python -m org_frontier.questions.q60_thompson_backchannel.probe_uniform_triadic_verdict
python -m org_frontier.questions.q60_thompson_backchannel.probe_cycle_collapse
python -m org_frontier.questions.q60_thompson_backchannel.probe_type_tracks_template
python -m org_frontier.questions.q60_thompson_backchannel.probe_no_phi_discrimination
```
