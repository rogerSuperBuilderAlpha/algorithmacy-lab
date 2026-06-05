# Q52 — phi-ladder mechanism

## Question

What structural feature of implication commit indices {2, 4, 11, 13} determines an n=3 form's rung on the
one-sided back-channel Φ ladder (0.830075 vs 0.415037 vs dyadic), and why does symmetric two-sided
coupling collapse the ladder to a single value?

## Background

Q51 probes #156 and #159 documented a commit-index ladder under one-sided worker back-channels and its
erasure under symmetric two-sided coupling. Six of eight matched-read implication forms bind triadically at
0.830075 or 0.415037; two (W1_S13_C1, W2_S2_C2) stay dyadic. Symmetric back-channels unify all eight at
0.830075. Q50 probe #154 supplied the implication commit set and party-read predicates. The open problem is
the structural predictor behind the three rungs.

Commit truth tables decode as: S2 = W∧¬C, S4 = ¬W∧C, S11 = C→W, S13 = W→C. Indices {2,13} are W-centric
(distinguishing output at W=1,C=0); {4,11} are C-centric (distinguishing output at W=0,C=1).

## Hypotheses

Five pre-registered hypotheses (committed before probe code):

- **H1:** W-centric matched forms split by S'(1,0) vs party-read index: high rung iff S'(1,0) ≠ (iw=2).
- **H2:** All C-centric matched forms plateau at Φ=0.415037.
- **H3:** All s∈{4,11} forms (matched and complementary) sit at 0.415037 under one-sided back-channel.
- **H4:** Symmetric coupling lifts the two one-sided dyadic W-centric forms to 0.830075.
- **H5:** Symmetric coupling makes all eight matched forms share 0.830075 with zero spread.

## Methods

Instrument: exact IIT-4.0 Φ via PyPhi on n=3 deterministic Boolean networks, synchronous update, labels
(W, S, C). Instrument control: canonical triad W'=S, S'=W∧C, C'=S — triadic, max_phi=2.0, MIP `2 parts:
{W,SC}`.

Ensemble: implication-commit strict-mediation forms (S-index ∈ {2, 4, 11, 13}) with Q51 back-channel
transforms. Party-read predicates from Q50. Commit outputs read from `_two_input_tables()` at fixed
(W,C) states.

## Results

**H1 — confirmed.** Four W-centric matched forms: zero mismatches between predicted and observed rung.
W1_S2_C1 and W2_S13_C2 high (0.830075); W1_S13_C1 and W2_S2_C2 dyadic. Rule: S'(1,0) ≠ (iw=2) → high.

**H2 — confirmed.** Four C-centric matched forms all triadic at 0.415037.

**H3 — confirmed.** Eight of eight forms with s∈{4,11} (four matched, four complementary) triadic at
0.415037 under one-sided worker back-channel.

**H4 — confirmed.** W1_S13_C1 and W2_S2_C2: one-sided dyadic (Φ=0) → symmetric triadic at 0.830075.

**H5 — confirmed.** Eight of eight matched symmetric forms triadic at uniform 0.830075; max_phi spread 0.

## Discussion

The ladder is a commit-class phenomenon, not a party-read phenomenon alone. W-centric commits {2,13} carry
the verdict split: party-read polarity must align with the commit's output at the W=1,C=0 distinguishing
state for the one-sided back-channel to reach the high rung. When polarity mismatches (identity read on a
zero output or negated read on a one output), integration fails entirely. C-centric commits {4,11} never
reach the high rung under one-sided wiring; they share a mid plateau invariant across matched and
complementary party reads.

Symmetric two-sided coupling explains collapse. It lifts the two dyadic W-centric mismatches to the high
rung and pulls the four C-centric mid forms up to the same 0.830075. The equilibrium value equals the
one-sided high rung and matches probe #77's symmetric-channel grade on the conjunctive triad. One-sided
back-channels add directional outer-party coupling that commit class and party-read alignment partially
exploit; symmetric back-channels restore bilateral outer-party coupling and erase within-panel heterogeneity.

## Validation gap

These are n=3 Boolean coordination forms under synchronous update with conjunctive back-channel gates.
Real channels may be graded, noisy, or scheduled differently. The mechanism is exact for this encoder and
wiring family only.
