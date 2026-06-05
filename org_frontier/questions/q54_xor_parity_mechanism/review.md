# Q54 — XOR parity back-channel mechanism · Stage 1 review

**Question.** What structural feature of XOR parity back-channels enables Φ=2.0 restoration on matched-read
implication forms when conjunctive AND/OR gates cap at 0.830075?

**Agenda id.** Grows from Q53 probes #167 and #169. No dedicated agenda slot; the open thread is the
mechanism behind parity coupling restoring the strict-mediation ceiling that monotone gates cannot reach.

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #167 (Q53 H3) | XOR gates exceed 0.830075; symmetric_xor reaches Φ=2.0 on all eight matched forms. | Establishes that parity coupling restores the ceiling; mechanism untested. |
| #168 (Q53 H4) | Zero of 64 AND/OR/cross pairs reach Φ=2.0. | Monotone conjunctive channels cap below ceiling. |
| #169 (Q53 H5) | Global supremum is 2.0 via XOR; conjunctive supremum 0.830075. | Separates parity from monotone gate classes at the matched implication panel. |
| #155–#159 (Q51) | Worker-side AND yields triadic binding below ceiling; symmetric AND unifies at 0.830075. | Monotone back-channel baseline for comparison. |
| #160–#164 (Q52) | Commit-class ladder under one-sided AND; symmetric collapse to 0.830075. | W-centric {2,13} vs C-centric {4,11} split may align with one-sided XOR hits. |
| #146 (Q45 H2) | Sixteen monotone forms reach Φ=2.0 at four edges; parity forms cap at 0.5. | Parity vs monotone class membership is load-bearing at the floor. |
| #154 (Q50 H5) | Implication commits at Φ=2.0 under strict mediation require complementary reads. | Matched reads need a channel to bind; XOR is the only tested gate that restores ceiling. |

## The gap

Q53 documented that XOR parity gates restore Φ=2.0 while AND/OR gates cap at 0.830075, but named no
structural predictor for why. Bijectivity of the channel gate, global TPM permutation, seam conditional
entropy, commit-topology alignment, and parity-class membership are concrete candidates drawn from Boolean
function theory and information geometry. No probe has tested whether Φ=2.0 pairs correlate with invertible
channel maps, higher outer-party distinguishability at the mediator seam, or commit-class-aligned one-sided
XOR wiring. The impossibility of monotone restoration (#168) requires a positive mechanism account, not only
a supremum table.
