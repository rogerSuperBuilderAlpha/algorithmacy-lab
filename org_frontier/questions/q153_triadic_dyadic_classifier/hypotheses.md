# q153 — hypotheses

A coordination form carries two readings. The behavioral reading is a set of CRQA features from
a sampled run. The structural reading is the major-complex core size from exact IIT-4.0 Φ. The
question is whether the behavioral reading recovers the structural verdict triadic (a core of
three or more nodes) versus dyadic (a two-node core).

Features, fixed before computing:
- `det` — whole-system md_recurrence determinism.
- `rr` — whole-system recurrence rate.
- `lag_var` — variance of the prominent pairwise lead-lag lags.
- `spread` — prominence spread: count of pairwise links whose prominence clears the floor.

## H1 (classification beats the baseline)

A logistic classifier on the four features separates triadic from dyadic forms with held-out
accuracy above the majority-class baseline.

Null: held-out accuracy is at or below the majority-class baseline. A label-shuffled classifier
is the control and lands at the baseline.

## H2 (spread is the most predictive feature)

The prominence spread carries the largest-magnitude standardized coefficient: coupling breadth
drives the verdict.

Null: whole-system DET carries the largest coefficient, so behavioral richness rather than
coupling breadth drives the verdict.

## Scope

The forms are synthetic Boolean coordination models. The results are an in-silico reading of the
CRQA-to-Φ bridge. No field organization is measured here.
