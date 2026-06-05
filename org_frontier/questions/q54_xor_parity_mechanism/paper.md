# Q54 — XOR parity back-channel mechanism

## Question

What structural feature of XOR parity back-channels enables Phi=2.0 restoration on matched-read implication
forms when conjunctive AND/OR gates cap at 0.830075?

## Grounding

Q53 probes #167 and #169 established that symmetric_xor reaches Phi=2.0 on all eight matched implication
forms while the conjunctive supremum stays at 0.830075. The present study tests five structural predictors
drawn from Boolean gate theory and seam information geometry.

## Instrument

Exact IIT-4.0 Phi via PyPhi on n=3 deterministic Boolean coordination forms with labels (W, S, C). The
canonical triad W'=S, S'=W AND C, C'=S reads triadic at max_phi=2.0 with MIP `2 parts: {W,SC}`. Every
probe asserts this control before comparison.

## Ensemble

Eight matched-read strict-mediation implication forms with S-index in {2,4,11,13} and matched live party
reads (iw=ic in {1,2}). Back-channel topologies extend the Q53 panel with XNOR variants. Commit classes:
W-centric {2,13}, C-centric {4,11}.

## Results

### H1 — Channel-gate bijectivity

Across 112 (topology, form) pairs, thirty-two reach Phi=2.0. All thirty-two use bijective channel gates
(XOR or XNOR in the coupled bit). Zero pairs with non-bijective AND/OR gates reach the ceiling. Sixteen
bijective pairs remain below 2.0 under one-sided parity wiring. Gate truth tables: AND and OR non-bijective;
XOR and XNOR bijective. **Verdict: confirmed.**

### H2 — Global TPM permutation

Twenty-four Phi=2.0 pairs under symmetric_xor, worker_xor, counterpart_xor, and symmetric_xnor were
checked for eight-state TPM permutation. Zero are permutations. Symmetric-AND on all eight forms also yields
non-permutation TPMs (0/8). **Verdict: refuted.** Phi=2.0 restoration does not require global bijective
dynamics.

### H3 — Seam conditional entropy

H(W,C|S) was computed over reachable-state trajectories. Symmetric_xor averages 1.811497 bits; symmetric-AND
averages 0.902747 bits. Mean delta 0.908749 bits; all eight forms show xor above and. **Verdict: confirmed.**

Per-form deltas range from 0.791380 to 1.026119 bits. The seam distinguishability gap is uniform in direction
and large in magnitude.

### H4 — Commit-topology alignment

Worker_xor reaches Phi=2.0 on four of eight forms, all C-centric commits {4,11}. Counterpart_xor reaches
Phi=2.0 on four of eight, all W-centric {2,13}. Zero misaligned one-sided ceiling hits. Symmetric_xor
reaches Phi=2.0 on eight of eight. **Verdict: confirmed.**

### H5 — Parity-class necessity

Across sixty-four monotone-gated pairs (eight topologies times eight forms), zero reach Phi=2.0. Symmetric_xnor
reaches Phi=2.0 on eight of eight, matching symmetric_xor. **Verdict: confirmed.** The ceiling requires
parity-class gates; monotone gates never suffice.

## Synthesis

Three features load-bear on Phi=2.0 restoration. Parity-class bijective channel gates are necessary (H1, H5).
Elevated seam conditional entropy H(W,C|S) accompanies the XOR panel (H3). Commit-topology alignment governs
one-sided restoration (H4). Global TPM permutation is not part of the story (H2 refuted): local gate
bijectivity and seam distinguishability matter; whole-system permutation does not.

The sixteen bijective-below-ceiling pairs are the residual puzzle. They share invertible channel maps with
the thirty-two ceiling pairs but lack either bilateral coupling or commit-aligned one-sided wiring.

## Validation gap

These results hold for n=3 deterministic Boolean models at synchronous update. Seam entropy uses plug-in
estimates on enumerated trajectories. No claim extends to empirical organizations or coarser update schedules.

## Reproduce

```
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_gate_bijectivity
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_tpm_permutation
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_seam_entropy
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_commit_alignment
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_parity_necessity
```
