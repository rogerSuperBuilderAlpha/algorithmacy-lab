# fn_tail_feature_redesign — hypotheses (fixed before computing)

**Question.** Can cheap features motivated by the triadic false-negative (FN) tail and by F28 local
instability reduce FN among triads on the unconstrained k=2 panels, versus the Probe-125/131
ten-feature baseline?

**Characterization (fixed before the redesign comparison; from the n=4 unc panel).** Baseline RF
FNs (n=30) vs TPs (n=267): FNs sit nearer the decision boundary (mean \|p−0.5\| 0.23 vs 0.42), carry
lower exact Φ (0.69 vs 0.97), are fully bidirectional (n_bidir=4), and show higher one-bit
*structural* fragility (graph features change on 0.75 vs 0.64 of Hamming-1 neighbours). Parity
tables are *less* common among FNs than TPs (30% vs 64%) — the FN tail is not the parity blind
spot.

**Baseline.** Probe-125/131 ten features + RF(400, seed 0), 5-fold CV on the committed n=4 unc
panel (N=1000, seed 40). Same protocol on n=5 (N=500, seed 50) for transfer.

**Redesign feature block (cheap; no exact Φ):**
- `struct_fragility` — fraction of one-bit table neighbours that change (n_edges, n_bidir,
  strongly_connected)
- `dyn_fragility` — fraction that change (n_fixed, n_reachable, invertible, max_period)
- `syn_fragility` — mean \|Δ syn_sum\| over those neighbours
- `n_parity` — count of XOR/XNOR node tables
- `n_affine` — count of GF(2)-affine node tables
- `n_both_dep` — count of nodes whose table depends on both inputs
- `mean_balance` — mean \|2·ones/4 − 1\| over node tables (0 = balanced)

**Primary metrics.** Overall miss rate; FN rate among triads; FP rate among dyads; ROC-AUC.
Primary comparison universe: **n=4 unc**. Secondary: **n=5 unc** in-distribution and
train-n4→test-n5 transfer.

Size series 4.8→7.5→9.0 and F27/F28 conclusions are cited, not reopened. Exact Φ remains the label.

## H1 — redesign cuts n=4 triadic FN rate

Redesign FN-among-triads ≤ baseline FN-among-triads − **0.05** (5 pp absolute).

Null: reduction < 5 pp (including any increase).

## H2 — redesign cuts n=4 overall miss rate

Redesign miss rate ≤ baseline miss rate − **0.01** (1 pp).

Null: reduction < 1 pp.

## H3 — redesign helps on n=5 (in-distribution)

Same 5 pp FN-among-triads improvement on the n=5 unc panel under the same CV protocol.

Null: reduction < 5 pp on n=5.

## H4 — n=4→n=5 transfer

A redesign RF fit on all n=4 rows, evaluated on n=5, has FN-among-triads at least 5 pp below a
baseline RF fit the same way.

Null: transfer FN improvement < 5 pp.
