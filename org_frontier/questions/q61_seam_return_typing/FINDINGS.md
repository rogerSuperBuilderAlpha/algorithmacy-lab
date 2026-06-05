# Q61 — findings

Official MIP singleton seam against Q43 return-path sequential/reciprocal typing on the back-channel panel.
Sixteen aligned one-sided ceiling pairs, all triadic at max_phi=2.0. Instrument control passed in every
probe: triadic, max_phi=2.000000, MIP `2 parts: {W,SC}`.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 seam tracks type bijection | confirmed | W seam+sequential 8/8; C seam+reciprocal 8/8; matches 16/16; mismatches 0/16. |
| H2 co-extensive partitions | confirmed | sequential 8/8; reciprocal 8/8; W singleton 8/8; C singleton 8/8; partition equality 16/16. |
| H3 seam not finer than type | confirmed | within-type seam heterogeneity 0/16; sequential with C seam 0/8; reciprocal with W seam 0/8. |
| H4 seam not coarser than type | confirmed | within-seam type heterogeneity 0/16; W seam+reciprocal 0/8; C seam+sequential 0/8. |
| H5 seam recovers verdict-lost discrimination | confirmed | max_phi spread 0.000000; W-seam=sequential 8/8; C-seam=reciprocal 8/8; subpanel match 16/16. |

**Through-line.** Q57 recipient→singleton seam and Q60 recipient→return-path type compose into perfect
seam↔type co-extensiveness on the identical panel. The official MIP singleton seam ({W,SC} vs {WS,C}) tracks
return-path sequential/reciprocal typing on 16/16 pairs even though max_phi offers no subpanel discrimination.
Seam and type are equal partitions — neither strictly finer nor coarser — so the singleton seam recovers at
the verdict level the typing magnitude loses without adding information beyond return-path typing.

**Caveats.** n=3 deterministic Boolean models, AND/implication family with bijective parity back-channels;
seam read from Q57 official tied outer cut cross-checked with Q49 seam_set. Real organizations remain beyond
reach.

**Reproduce.**

```bash
python -m org_frontier.questions.q61_seam_return_typing.probe_seam_tracks_type
python -m org_frontier.questions.q61_seam_return_typing.probe_coextensive_partitions
python -m org_frontier.questions.q61_seam_return_typing.probe_seam_not_finer
python -m org_frontier.questions.q61_seam_return_typing.probe_seam_not_coarser
python -m org_frontier.questions.q61_seam_return_typing.probe_seam_recover_discrimination
```
