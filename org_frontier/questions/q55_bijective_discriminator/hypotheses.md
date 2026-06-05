# Q55 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on what separates the sixteen bijective parity-channel pairs below Φ=2.0 from the
thirty-two at the ceiling on matched-read implication forms. Written and committed before any test runs.
Grows from Q54 probes #170 and #171.

## H1 — Misaligned one-sided parity exhausts the below-ceiling set
- **Claim:** Every bijective below-ceiling pair is a one-sided parity topology (worker or counterpart XOR/XNOR)
  with commit-topology misalignment; no symmetric and no aligned one-sided pair appears in the below set.
- **H0:** At least one below-ceiling bijective pair is symmetric, aligned one-sided, or not misaligned under
  the XOR/XNOR alignment rule.
- **Predicted outcome:** Sixteen of sixteen below are misaligned one-sided; zero symmetric or aligned one-sided
  in below; thirty-two ceiling pairs are symmetric or aligned one-sided only. H0 refuted only if the partition
  is perfect.

## H2 — Uniform mid-rung Phi on the below-ceiling half
- **Claim:** All sixteen below-ceiling bijective pairs share max_phi=0.415037 (the Q52 C-centric mid rung); all
  thirty-two ceiling pairs reach max_phi=2.0 with zero overlap in magnitude.
- **H0:** At least one below-ceiling bijective pair has max_phi other than 0.415037, or at least one ceiling
  pair falls below 2.0 − 1e−9.
- **Predicted outcome:** Perfect phi separation: below spread 0, ceiling spread 0 at 2.0. H0 refuted on any
  exception.

## H3 — Seam conditional entropy is lower on below-ceiling bijective pairs
- **Claim:** Mean H(W,C|S) over the sixteen below-ceiling bijective pairs is strictly less than the mean over
  the thirty-two ceiling pairs.
- **H0:** Mean seam entropy for below-ceiling bijective pairs is not less than the ceiling mean (difference
  ≤ 0 + 1e−6 bits).
- **Predicted outcome:** Strict positive gap in mean H(W,C|S). H0 refuted if below mean exceeds ceiling mean.
  H0 partial if direction holds on a majority of pairs but mean gap is non-positive.

## H4 — MIP seam singleton {S,WC} marks the below-ceiling half
- **Claim:** Every below-ceiling bijective pair has MIP first line `2 parts: {S,WC}` (mediator S as singleton
  seam); no ceiling pair uses that partition.
- **H0:** At least one below-ceiling bijective pair has a different MIP partition, or at least one ceiling
  pair shows `{S,WC}`.
- **Predicted outcome:** Sixteen of sixteen below at `{S,WC}`; zero of thirty-two ceiling at `{S,WC}`. Ceiling
  pairs use `{WS,C}`, `{W,SC}`, or complete `{W,S,C}` only. H0 refuted on any violation.

## H5 — XNOR inverts one-sided alignment polarity relative to XOR
- **Claim:** One-sided Φ=2.0 under worker_xnor requires W-centric commits {2,13}; under counterpart_xnor
  requires C-centric {4,11} — the complement of the XOR alignment rule from Q54 #173.
- **H0:** At least one one-sided XNOR ceiling hit violates the inverted alignment rule, or at least one
  aligned XOR one-sided pair fails to reach Φ=2.0.
- **Predicted outcome:** Zero XNOR misalignments at ceiling; eight of eight worker_xnor ceiling hits W-centric;
  eight of eight counterpart_xnor ceiling hits C-centric. H0 refuted on any violation.
