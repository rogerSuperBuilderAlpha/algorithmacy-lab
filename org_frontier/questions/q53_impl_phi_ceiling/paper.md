# Q53 — implication Phi ceiling

## Question

Can any back-channel topology or graded channel strength restore matched-read implication forms to the
strict-mediation complementary ceiling Φ=2.0, or is 0.830075 the absolute maximum once outer-party coupling
is added beyond the four-edge floor?

## Background

Q51 probes #155 and #159 showed matched-read implication commits {2,4,11,13} bind below Φ=2.0 under
worker-side and symmetric AND back-channels, with symmetric-AND unifying all eight forms at 0.830075. Q52
probe #164 confirmed zero spread at that equilibrium. The open problem is whether a different topology or
weaker/stronger Boolean gate can recover the four-edge ceiling or whether 0.830075 is an impossibility
bound.

## Hypotheses

Five pre-registered hypotheses (committed before probe code):

- **H1:** Counterpart-side AND (C'=old_C & W) restores Φ=2.0 for at least one matched form.
- **H2:** OR-graded worker-side coupling (W'=old_W | C) restores Φ=2.0 for at least one matched form.
- **H3:** XOR parity gates raise max_phi above 0.830075 for at least one matched form.
- **H4:** Zero of 64 (form, topology) pairs across AND/OR/cross topologies reach Φ=2.0.
- **H5:** Global supremum equals 0.830075; symmetric-AND saturates it on all eight forms.

## Methods

Instrument: exact IIT-4.0 Φ via PyPhi on n=3 deterministic Boolean networks, synchronous update, labels
(W, S, C). Instrument control: canonical triad W'=S, S'=W∧C, C'=S — triadic, max_phi=2.0, MIP `2 parts:
{W,SC}`.

Ensemble: eight matched-read implication strict-mediation forms (S-index ∈ {2,4,11,13}, W-index = C-index
∈ {1,2}). Back-channel topologies: worker/counterpart/symmetric AND and OR; cross (W-OR/C-AND) and
(W-AND/C-OR); worker/counterpart/symmetric XOR. Helpers in `ceiling_utils.py`; party-read predicates from
Q51 `backchannel_utils.py`.

## Results

**H1 — partial.** Counterpart-side AND: zero of eight at Φ=2.0; six of eight triadic below ceiling. Max
0.830075 on W1_S4_C1 and W2_S11_C2. The ladder mirrors worker-side AND with W-centric and C-centric roles
exchanged: C-centric commits reach the high rung under counterpart wiring where W-centric commits reached
it under worker wiring.

**H2 — partial.** Worker-side OR: zero of eight at Φ=2.0; six of eight triadic below ceiling. Max
0.830075 on W1_S11_C1 and W2_S4_C2. OR weakens the channel gate but does not recover the ceiling.

**H3 — confirmed.** Sixteen of twenty-four XOR (form, topology) pairs exceed 0.830075. Symmetric_xor
reaches Φ=2.0 on all eight matched forms. One-sided XOR reaches 2.0 on four of eight: worker_xor on
C-centric forms {4,11}; counterpart_xor on W-centric forms {2,13}.

**H4 — confirmed.** Zero of sixty-four pairs across the eight conjunctive-style topologies
{worker_and, counterpart_and, symmetric_and, worker_or, counterpart_or, symmetric_or, cross_wor_cand,
cross_wand_cor} reach Φ=2.0.

**H5 — refuted.** Global max_phi over eighty-eight pairs equals 2.0 (sixteen argmax pairs, all XOR).
Symmetric-AND remains uniform at 0.830075 on all eight forms (spread 0). The supremum for conjunctive-style
coupling is 0.830075; the overall supremum across all tested gates is 2.0.

## Discussion

The ceiling question has a gate-class answer. Conjunctive-style back-channels — AND, OR, and their mixed
cross combinations — cap matched-read implication integration at 0.830075 regardless of topology direction
or graded OR weakening. Symmetric-AND remains the conjunctive supremum, replicating Q51 #159 and Q52 #164.

XOR parity gates break the impossibility bound. Symmetric_xor restores Φ=2.0 on every matched form, matching
the strict-mediation complementary-read ceiling that matched reads cannot reach at the four-edge floor.
One-sided XOR restores 2.0 selectively by commit class: worker_xor on C-centric {4,11}, counterpart_xor on
W-centric {2,13}. The pattern inverts the one-sided AND ladder from Q52: parity coupling on the channel
side compensates for the commit-class asymmetry that conjunctive gates only partially bridge.

0.830075 is the absolute maximum for conjunctive-style outer-party coupling on matched implication forms.
It is not the absolute maximum across all deterministic n=3 Boolean back-channel gates tested here.

## Validation gap

These are n=3 Boolean coordination forms under synchronous update with a finite {AND, OR, XOR} gate panel.
Real channels may be graded continuously, noisy, or scheduled differently. The XOR restoration result is
exact for this encoder and gate family only.
