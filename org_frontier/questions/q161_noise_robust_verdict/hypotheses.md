# q161 — Hypotheses

Both hypotheses were fixed before any number was computed.

## H1

The triadic/dyadic verdict stays correct across flip in {0.02 .. 0.30} for more than 80% of
forms, while bottleneck-node recovery degrades by more than 20 points between its best and worst
flip rate.

Null: all three verdicts (triadic/dyadic, membership, bottleneck) show the same flip-rate
sensitivity, measured as the spread in corpus-mean agreement across the swept flip rates.

Decision rule: SUPPORTED if the fraction of forms whose triadic/dyadic call is correct at every
swept flip exceeds 0.80 and the bottleneck recovery rate drops by more than 0.20 between its best
and worst flip; REFUTED otherwise.

## H2

Each form has a flip rate that maximizes verdict agreement, and that optimum is not constant
across forms: the per-form optimum tracks the form's intrinsic update entropy, a flip-independent
property of its truth table.

Null: a single flip rate is optimal for all forms, so the per-form optima are constant and there
is nothing for entropy to track.

Decision rule: SUPPORTED if the per-form optimal flip varies across forms and its Spearman rank
correlation with intrinsic update entropy exceeds 0.30 in the positive (predicted) direction;
NOT SUPPORTED otherwise.

## Scope

The corpus is synthetic Boolean coordination forms. Ground truth is exact IIT-4.0 Φ on their
transition matrices. The CRQA readings come from sampled stochastic trajectories. Every agreement
rate is a baseline on synthetic data. The Φ-to-organization bridge is open; no field organization
is measured.
