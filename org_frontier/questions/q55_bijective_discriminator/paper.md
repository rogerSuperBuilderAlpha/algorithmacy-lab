# Q55 — bijective parity below-vs-ceiling discriminator

## Question

What distinguishes the sixteen bijective parity-channel pairs that remain below Phi=2.0 from the thirty-two
that reach the ceiling on matched-read implication forms?

## Grounding

Q54 probes #170 and #171 showed channel-gate bijectivity is necessary but insufficient for Phi=2.0: thirty-two
bijective pairs reach the ceiling and sixteen stay below. The present study tests five structural discriminators
on the forty-eight bijective parity pairs.

## Instrument

Exact IIT-4.0 Phi via PyPhi on n=3 deterministic Boolean coordination forms with labels (W, S, C). The
canonical triad W'=S, S'=W AND C, C'=S reads triadic at max_phi=2.0 with MIP `2 parts: {W,SC}`. Every
probe asserts this control before comparison.

## Ensemble

Eight matched-read strict-mediation implication forms with S-index in {2,4,11,13}. Six bijective parity
topologies: worker_xor, counterpart_xor, symmetric_xor, worker_xnor, counterpart_xnor, symmetric_xnor.
Forty-eight pairs total; sixteen below ceiling, thirty-two at ceiling per Q54 #170.

## Results

### H1 — Misaligned one-sided partition

All sixteen below-ceiling pairs are one-sided topologies with commit-topology misalignment. Zero below pairs
are symmetric or aligned one-sided. The thirty-two ceiling pairs comprise sixteen one-sided aligned and
sixteen symmetric. **Verdict: confirmed.**

### H2 — Uniform mid-rung Phi

Every below-ceiling pair has max_phi=0.415037 with spread 0.000000. Every ceiling pair has max_phi=2.0 with
spread 0.000000. **Verdict: confirmed.**

### H3 — Seam entropy split

Mean H(W,C|S) over the below half is 1.494161 bits; over the ceiling half 1.630633 bits. Mean delta
0.136472 bits. Three hundred eighty-four of five hundred twelve pair-wise comparisons show below below
ceiling. **Verdict: confirmed.**

### H4 — MIP {S,WC} singleton

Sixteen of sixteen below-ceiling pairs have MIP first line `2 parts: {S,WC}`. Zero of thirty-two ceiling
pairs use that partition. Ceiling distribution: sixteen complete `{W,S,C}`, eight `{WS,C}`, eight
`{W,SC}`. **Verdict: confirmed.**

### H5 — XNOR alignment inversion

Zero XNOR ceiling hits violate the inverted alignment rule. Worker_xnor reaches Phi=2.0 on four of four
W-centric forms; counterpart_xnor on four of four C-centric forms. All eight XOR aligned one-sided pairs
reach Phi=2.0 with zero misses. **Verdict: confirmed.**

## Synthesis

The forty-eight bijective parity pairs partition into two disjoint structural classes. The sixteen below-
ceiling pairs share misaligned one-sided wiring, uniform mid-rung Phi, lower seam entropy, and mediator-
singleton MIP `{S,WC}`. The thirty-two ceiling pairs share symmetric or aligned one-sided wiring, Phi=2.0,
higher seam entropy, and outer-party or complete MIP cuts. XNOR inverts the one-sided alignment polarity
relative to XOR without breaking the partition.

## Validation gap

These results hold for n=3 deterministic Boolean models at synchronous update. Seam entropy uses plug-in
estimates on enumerated trajectories. No claim extends to empirical organizations or coarser update schedules.

## Reproduce

```
python -m org_frontier.questions.q55_bijective_discriminator.probe_misaligned_partition
python -m org_frontier.questions.q55_bijective_discriminator.probe_mid_rung_uniform
python -m org_frontier.questions.q55_bijective_discriminator.probe_seam_entropy_split
python -m org_frontier.questions.q55_bijective_discriminator.probe_mip_singleton
python -m org_frontier.questions.q55_bijective_discriminator.probe_xnor_alignment_flip
```
