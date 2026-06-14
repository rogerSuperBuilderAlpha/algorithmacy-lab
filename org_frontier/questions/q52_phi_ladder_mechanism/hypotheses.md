# Q52 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on the structural mechanism behind the one-sided back-channel Φ ladder for
matched-read implication commits {2,4,11,13}. Written and committed before any test runs. Grows from
Q51 probes #156 and #159.

## H1 — W-centric commits split by party-read polarity at (W=1,C=0)
- **Claim:** Among matched-read forms with W-centric commits s∈{2,13} (distinguishing output at
  W=1,C=0), the high rung (Φ≈0.830075) occurs iff S'(1,0) ≠ (iw=2); the dyadic rung occurs iff they
  match. The four W-centric matched forms obey this with zero mismatches.
- **H0:** At least one W-centric matched form lands on the wrong rung relative to the (1,0) output vs
  party-read rule.
- **Predicted outcome:** Perfect 4/4 classification: W1_S2_C1 and W2_S13_C2 high; W1_S13_C1 and
  W2_S2_C2 dyadic. H0 is refuted.

## H2 — C-centric commits plateau at the mid rung
- **Claim:** All matched-read forms with C-centric commits s∈{4,11} (distinguishing output at W=0,C=1)
  read triadic at Φ≈0.415037 under one-sided worker back-channel, regardless of party-read index.
- **H0:** At least one C-centric matched form is dyadic or reaches Φ≈0.830075.
- **Predicted outcome:** Four of four C-centric matched forms triadic at 0.415037. H0 is refuted.

## H3 — Mid rung is invariant across party-read pairing
- **Claim:** The mid plateau Φ≈0.415037 is shared by all eight implication forms (matched and
  complementary) whose commit index is s∈{4,11}, under one-sided worker back-channel.
- **H0:** Any s∈{4,11} form with worker back-channel deviates from 0.415037 by more than 1e−6 or is
  dyadic.
- **Predicted outcome:** Eight of eight at 0.415037 triadic. H0 is refuted.

## H4 — Symmetric coupling lifts dyadic W-centric forms to the high rung
- **Claim:** The two one-sided dyadic W-centric matched forms (W1_S13_C1, W2_S2_C2) become triadic at
  Φ≈0.830075 when the symmetric two-sided back-channel replaces the one-sided edge.
- **H0:** At least one of the two remains dyadic or stays below 0.830075 under symmetric coupling.
- **Predicted outcome:** Both triadic at 0.830075. H0 is refuted.

## H5 — Symmetric equilibrium equals the one-sided high rung and erases within-panel spread
- **Claim:** Under symmetric two-sided back-channel, all eight matched-read implication forms share
  max_phi=0.830075 (the one-sided high-rung value), with zero within-panel variance — the mechanism of
  ladder collapse.
- **H0:** Fewer than eight triadic or max_phi differs across forms by more than 1e−6.
- **Predicted outcome:** Eight of eight triadic at identical 0.830075; spread 0. H0 is refuted.
