# Q55 — findings

Probes #175–#179. Exact IIT-4.0 Φ via PyPhi, n=3 deterministic Boolean forms, implication commits
{2,4,11,13} with matched party reads and six bijective parity back-channel topologies. Grows from Q54
probes #170 and #171.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — misaligned one-sided partition | confirmed | 16/16 below misaligned one-sided; 0 below symmetric; 0 below aligned; 32 ceiling (16 one-sided + 16 symmetric). |
| H2 — uniform mid-rung Phi | confirmed | 16/16 below at 0.415037 (spread 0); 32/32 ceiling at 2.0 (spread 0). |
| H3 — seam entropy split | confirmed | Mean H below=1.494161 vs ceiling=1.630633; delta=0.136472 bits; 384/512 pair-wise below<ceiling. |
| H4 — MIP {S,WC} singleton | confirmed | 16/16 below at `2 parts: {S,WC}`; 0/32 ceiling at that partition. |
| H5 — XNOR alignment inversion | confirmed | 0 XNOR ceiling misalignments; worker_xnor 4/4 W-centric; counterpart_xnor 4/4 C-centric; XOR aligned 8/8 at ceiling. |

**Through-line.** Q54 left sixteen bijective parity pairs below Phi=2.0 without a complete partition rule.
The forty-eight bijective parity pairs split cleanly. Every below-ceiling pair is a one-sided topology with
commit misalignment; every ceiling pair is either symmetric or one-sided aligned (H1). Magnitude separates
perfectly: all sixteen below sit at the Q52 mid rung 0.415037; all thirty-two ceiling reach 2.0 (H2). Seam
conditional entropy H(W,C|S) is lower on the below half by 0.136472 bits on average (H3). MIP geometry
marks the split: below pairs sever the mediator as singleton seam `{S,WC}`; ceiling pairs use `{WS,C}`,
`{W,SC}`, or complete `{W,S,C}` only (H4). XNOR inverts the one-sided alignment polarity relative to XOR:
worker_xnor ceiling hits require W-centric commits, counterpart_xnor require C-centric — the complement of
the XOR rule from Q54 #173 (H5).

**Caveats.** n=3 deterministic Boolean; synchronous update; seam entropy uses reachable-state plug-in
estimates. Results describe coordination forms, not empirical organizations.

**Reproduce.**
```
python -m org_frontier.questions.q55_bijective_discriminator.probe_misaligned_partition
python -m org_frontier.questions.q55_bijective_discriminator.probe_mid_rung_uniform
python -m org_frontier.questions.q55_bijective_discriminator.probe_seam_entropy_split
python -m org_frontier.questions.q55_bijective_discriminator.probe_mip_singleton
python -m org_frontier.questions.q55_bijective_discriminator.probe_xnor_alignment_flip
```
