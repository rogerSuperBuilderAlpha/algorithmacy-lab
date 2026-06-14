# Q61 — MIP seam vs return-path typing

## Question

On aligned one-sided back-channel forms held at uniform triadic max_phi=2.0, does the official MIP singleton
seam ({W,SC} vs {WS,C}) track return-path sequential/reciprocal typing even though max_phi offers no subpanel
discrimination?

## Panel

Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56. Instrument control: canonical triad
reads triadic, max_phi=2.0, MIP `2 parts: {W,SC}`.

## Methods

Official singleton seam from Q57 `tied_outer_cut` (W for `{W,SC}`, C for `{WS,C}`). Return-path typing from
Q60 `return_path_type` following Q43 connectivity conventions. Cross-tabulation and partition-equality metrics
in `seam_return_utils.py`.

## Results

### H1 — Seam tracks type bijection

W seam with sequential typing on 8/8. C seam with reciprocal typing on 8/8. Seam–type matches 16/16.
Mismatches 0/16.

### H2 — Co-extensive partitions

Sequential cells 8/8. Reciprocal cells 8/8. W singleton cells 8/8. C singleton cells 8/8. Partition equality
16/16.

### H3 — Seam not finer than type

Within-type seam heterogeneity 0/16. No sequential row carries C seam; no reciprocal row carries W seam.

### H4 — Seam not coarser than type

Within-seam type heterogeneity 0/16. No W-seam row reads reciprocal; no C-seam row reads sequential.

### H5 — Seam recovers verdict-lost discrimination

Panel max_phi spread 0.000000. W-seam subpanel equals sequential subpanel on 8/8. C-seam subpanel equals
reciprocal subpanel on 8/8. Subpanel match total 16/16.

## Synthesis

Q57 recipient→seam and Q60 recipient→type transitively yield perfect seam↔type co-extensiveness. The
singleton seam recovers the sequential/reciprocal partition that uniform max_phi=2.0 collapses. Seam and type
are equal partitions on the panel; the seam adds no information beyond return-path typing once recipient is
known.

## Validation gap

Deterministic n=3 Boolean models at finest grain with synchronous update. Results hold about the Boolean
models; real organizations remain beyond reach.

## Reproduce

```bash
python -m org_frontier.questions.q61_seam_return_typing.probe_seam_tracks_type
python -m org_frontier.questions.q61_seam_return_typing.probe_coextensive_partitions
python -m org_frontier.questions.q61_seam_return_typing.probe_seam_not_finer
python -m org_frontier.questions.q61_seam_return_typing.probe_seam_not_coarser
python -m org_frontier.questions.q61_seam_return_typing.probe_seam_recover_discrimination
```
