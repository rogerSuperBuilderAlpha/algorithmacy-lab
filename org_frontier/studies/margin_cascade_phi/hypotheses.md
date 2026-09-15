# margin_cascade_phi — hypotheses (fixed before computing)

**Question.** Can a margin-cascade — Probe-131 cheap RF as screen, exact IIT-4.0 Φ only on
out-of-fold uncertain forms — cut FN-among-triads on unc k=2 panels at a fixed exact-Φ budget,
relative to always-cheap?

**Background (cited, not reopened).** Size series miss 4.8% → 7.5% → 9.0%. F28: residual
misses sit on a phase boundary (mean flip ~0.37). `fn_tail_feature_redesign`: hand-feature
expansion honest null (H1–H4 REFUTED). Exact Φ remains ground truth on the called subset.

**Protocol.** Same Probe-125/131 ten features + RF(400, seed 0). Gating probabilities from
**5-fold `cross_val_predict`** (out-of-fold; no leakage). Primary panel: n=4 unc (N=1000,
seed 40). Secondary: n=5 unc (N=500, seed 50). Labels already cached (`triadic`); calling
exact Φ = substituting the true label for the cheap prediction on the selected subset.

**Gating scores (higher score → call exact first):**
- **margin:** `1 − 2|p − 0.5|` (uncertainty)
- **fragility:** `struct_fragility` from the committed FN-redesign enriched panels
- **combined:** rank-average of margin and fragility (higher combined rank → call first)
- **random:** uniform draw of the same count (20 seeds; mean ± reporting)

**Budgets.** Cost–error curve at exact-call fractions
`B ∈ {0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 1.0}`.
Pre-registered operating points: **B = 10%** and **B = 20%**.

**Primary metrics.** FN rate among triads; overall miss rate; FP among dyads. Always-cheap =
B=0; always-exact = B=1 (FN=0, miss=0).

## H1 — B=10% margin cascade beats always-cheap on FN|tri (n=4)

At B=0.10, margin-gated cascade FN-among-triads ≤ always-cheap FN-among-triads − **0.05**
(5 pp absolute).

Null: reduction < 5 pp.

## H2 — B=20% recovers most of the FN gap to always-exact (n=4)

At B=0.20, margin cascade recovers ≥ **60%** of the always-cheap → always-exact FN|tri gap
(i.e. FN_cascade ≤ 0.40 × FN_cheap).

Null: recovery < 60%.

## H3 — margin gating beats matched-budget random (n=4, B=10%)

At B=0.10, margin FN|tri ≤ mean(random FN|tri) − **0.03** (3 pp).

Null: advantage < 3 pp.

## H4 — fragility adds gating value over margin alone (n=4, B=10%)

At B=0.10, combined (rank-average) FN|tri ≤ margin-only FN|tri − **0.02** (2 pp).

Null: combined does not improve by ≥ 2 pp (fragility adds little beyond |p−0.5|).

## H5 — n=5 validation at B=10%

Same 5 pp FN|tri drop vs always-cheap on n=5 unc under margin gating at B=0.10.

Null: reduction < 5 pp on n=5.
