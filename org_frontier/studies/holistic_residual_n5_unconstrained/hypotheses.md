# holistic_residual_n5_unconstrained — hypotheses (fixed before computing)

**Question.** Under the same unconstrained k=2 protocol as `holistic_residual_n4_unconstrained/`,
does the cheap-feature holistic residual at n=5 hold near the n=4 rate (7.5%), shrink toward the
n=3 rate (4.8%), or grow further?

**Universe.** Unconstrained random Boolean networks with in-degree k=2 on **n=5** nodes: each node
independently chooses 2 distinct others and a random 2-input truth table. Fixed sample **N=500**,
seed **50**. (Full 3-input coupling and strict-mediation are out of scope here; N=500 is the largest
honest size with expected exact-Φ runtime under ~10 minutes on this host — pilot mean ~0.55 s/form.)

**Features / classifier.** Same Probe-125/131 ten-feature panel as the n=4 unc study; RF
`n_estimators=400`, `random_state=0`, 5-fold `cross_val_predict`. Exact IIT-4.0 Φ_MIP via
`classify_rules`.

**Baselines.** n=3 miss = 4.8% (196/4096). n=4 unc k=2 miss = 7.5% (75/1000). F26 SM 2.4% is a
base-rate artifact and is **not** used as the size-trend reference. F27 not reopened.

**Hold band (relative to n=4 unc 7.5%).** Rate in **[5.5%, 9.5%]** (±2.0 pp) counts as holding.

## H0 — residual holds near the n=4 unc rate

n=5 RF miss rate ∈ [5.5%, 9.5%].

## H1 — residual shrinks toward n=3

Miss rate < 5.5%.

## H2 — residual grows further

Miss rate > 9.5%.

## H3 — RF predicts both classes

Cross-validated predictions include at least one triadic and one dyadic call. If H3 fails, the
band verdict is reported as inconclusive for the size trend (majority-floor risk, as in F26 SM).

Secondary: triadic rate, FP/FN, miss rate among triadic vs dyadic, near-boundary fraction among
misses, comparison table n=3 / n=4 unc / n=5.
