# holistic_residual_n4_unconstrained — hypotheses (fixed before computing)

**Question.** Once the n=4 sample is not dominated by a vanishing triadic base rate (the F26
strict-mediation asterisk: 2.4% triadic, RF never predicted triadic), does the cheap-feature
holistic residual shrink, hold, or grow relative to the n=3 Probe-131 baseline of 4.8%?

**Primary universe (Probe-131 analogue at n=4).** Unconstrained random Boolean networks with
in-degree k=2: each of 4 nodes independently chooses 2 distinct others and a random 2-input truth
table. This is the natural n=4 lift of the n=3 4096 panel (where each node necessarily reads the
other two). Full 3-input coupling was measured first and rejected for the primary panel: it is
~93% triadic and would only invert the base-rate asterisk. Fixed sample **N=1000**, seed **40**.

**Features / classifier.** Same Probe-125/131 ten-feature panel as `holistic_residual_n4`
(connectivity, synergy, dynamics), RF `n_estimators=400`, `random_state=0`, 5-fold
`cross_val_predict`. Exact IIT-4.0 Φ_MIP labels via `classify_rules`.

**Baselines.** n=3 miss rate = 4.8% (196/4096). F26 SM miss rate = 2.4% (71/3000). F27 not reopened.

**Hold band.** Same as F26: rate in **[3.3%, 6.3%]** counts as holding (±1.5 pp of 4.8%).

## H0 — residual holds near ~5%

Unconstrained n=4 RF miss rate ∈ [3.3%, 6.3%].

## H1 — residual shrinks

Miss rate < 3.3%.

## H2 — residual grows

Miss rate > 6.3%.

## H3 — RF predicts both classes (asterisk check)

The forest's cross-validated predictions include at least one triadic and one dyadic call (positive
predicted count ∈ (0, N)). If H3 fails, any shrink/grow verdict is again majority-floor dominated
and is reported as inconclusive for the base-rate-controlled question.

Secondary (not decisive): FP/FN, miss rate among triadic vs dyadic, near-boundary fraction among
misses, majority-class miss rate, comparison to F26's 2.4%.
