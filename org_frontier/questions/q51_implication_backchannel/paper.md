# Q51 — implication back-channel

## Question

Does adding a minimal worker–counterpart back-channel edge let implication-commit triads bind irreducibly
(Φ=2.0) with matched party reads, instead of the complementary reads that strict mediation requires?

## Background

Q50 probe #154 split monotone Φ=2.0 forms by commit symmetry. Symmetric commits (AND, OR, NOR, NAND) bind
only with matched party reads; implication commits bind only with complementary reads. All tests ran under
strict mediation with exactly four edges. A back-channel adds a fifth (or sixth) directed edge between the
outer parties. Probes #142 and #77 showed back-channels can preserve triadicity while grading Φ below the
ceiling.

## Hypotheses

Five pre-registered hypotheses (committed before probe code):

- **H1:** Worker-side back-channel W'=f_W(S)∧C lets at least one matched-read implication form reach Φ=2.0.
- **H2:** The same transform makes at least six of eight matched forms triadic (Φ>0).
- **H3:** Without back-channel, all eight matched-read implication forms stay dyadic.
- **H4:** Worker-side back-channel preserves Φ=2.0 on all eight complementary-read implication forms.
- **H5:** Symmetric two-sided back-channel makes all eight matched forms triadic at a single shared max_phi.

## Methods

Instrument: exact IIT-4.0 Φ via PyPhi on n=3 deterministic Boolean networks, synchronous update, labels
(W, S, C). Instrument control: canonical triad W'=S, S'=W∧C, C'=S — triadic, max_phi=2.0, MIP `2 parts:
{W,SC}`.

Ensemble: eight implication-commit strict-mediation forms (S-index ∈ {2, 4, 11, 13}) for each party-read
predicate. Matched reads: W-index = C-index ∈ {1, 2}. Complementary reads: {W-index, C-index} = {1, 2} with
W-index ≠ C-index. Back-channel transforms conjunctively extend party updates: worker-side adds C to W';
symmetric adds W to C' as well.

## Results

**H1 — partial.** Zero of eight matched-read implication forms with worker-side back-channel reach Φ=2.0.
Six are triadic below the ceiling; two (W1_S13_C1, W2_S2_C2) stay dyadic. Maximum observed max_phi is
0.830075.

**H2 — confirmed.** Six of eight matched forms are triadic with worker-side back-channel. Magnitudes split:
0.830075 on W1_S2_C1 and W2_S13_C2; 0.415037 on W1_S4_C1, W1_S11_C1, W2_S4_C2, W2_S11_C2.

**H3 — confirmed.** All eight matched-read implication forms are dyadic (Φ=0) under strict mediation,
replicating Q50.

**H4 — partial.** All eight complementary-read forms stay triadic with worker-side back-channel, but none
retain Φ=2.0. Strict-mediation baselines are all Φ=2.0; back-channel values are 0.830075 or 0.415037.

**H5 — confirmed.** Symmetric two-sided back-channel makes all eight matched forms triadic at uniform
max_phi=0.830075 with six directed edges each.

## Discussion

The main question receives a negative answer at the Φ=2.0 ceiling. A minimal worker-side back-channel
enables irreducible binding for matched-read implication forms but grades them below the four-edge ceiling.
The party-read rule from Q50 is not overturned at full integration strength; matched reads never reach the
same Φ as complementary reads under any back-channel tested here.

The symmetric two-sided back-channel is the sharper finding. It collapses commit-index heterogeneity: all
eight matched forms share Φ=0.830075, the same magnitude probe #77 reported for a symmetric W↔C channel on
the conjunctive triad. One-sided back-channels leave a commit-dependent ladder (0.830, 0.415, or dyadic);
two-sided coupling unifies the panel.

## Validation gap

These are n=3 Boolean coordination forms under synchronous update. The back-channel is one conjunctive wiring
pattern. Real organizations may carry richer channels, noise, and update schedules that move both verdict
and magnitude.
