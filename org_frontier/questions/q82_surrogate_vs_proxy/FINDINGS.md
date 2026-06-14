# Q82 findings — the surrogate beats every single proxy, and one structural proxy is stronger than expected

Three hypotheses confirmed, one refuted. On the n=3 outreach family the learned surrogate separates the
verdict perfectly and beats every single cheap proxy. The refutation is informative: total edge count is a
strong single proxy on this family, stronger than the pre-registration expected, though still unable to
separate the verdict cleanly.

| Proxy | rank-AUC | best-threshold accuracy |
|---|---|---|
| mediator in-degree | 0.707 | 0.906 |
| total edges | **0.966** | 0.938 |
| Φ_R (ΦID) | 0.621 | 0.922 |
| Φ_WMS (whole-minus-sum) | 0.547 | 0.922 |
| **learned surrogate (5-fold CV)** | **1.000** | **1.000** |

Modal mediator in-degree = 2: 160 forms (24 triadic, 136 dyadic), surrogate out-of-fold accuracy 1.000.

| H | Result | Verdict |
|---|--------|---------|
| H1 | every single proxy rank-AUC < 0.85 | refuted (edges 0.966) |
| H2 | surrogate AUC ≥ 0.95 and beats every proxy | confirmed (1.000) |
| H3 | surrogate accuracy > best single-proxy threshold | confirmed (1.000 vs 0.938) |
| H4 | surrogate OOF accuracy ≥ 0.90 on the modal-in-degree subset | confirmed (1.000) |

From `probe_surrogate_vs_proxy.py`.

## What it says

The learned surrogate separates the verdict where single proxies cannot. Its CV ROC-AUC and accuracy are
both 1.000, above every single proxy. On the modal-in-degree subset — the 160 forms where the mediator
reads both parties, so in-degree is constant at 2 and carries no information, the regime of the Q72
read_recipient/one_shot collision — the surrogate's out-of-fold accuracy is still 1.000. Where the
structural proxy is flat, the combination of cheap features reads the difference.

One single proxy is stronger than the pre-registration expected. Total edge count ranks the verdict at
AUC 0.966: triadic forms on the strict-mediation family carry more active edges, and that leaks into a
simple count. This refutes H1, which predicted every single proxy below 0.85. The refutation does not
overturn the comparison. Edge count still cannot separate the verdict cleanly — its best-threshold
accuracy is 0.938, capped by the same collisions Q72 found, where a triadic and a dyadic form share an
edge count (read_recipient and one_shot both have four). The surrogate clears that cap to 1.000.

This reconciles with Q72. Q72 showed edge count collides on specific pairs;
that collision persists here and is exactly why edge count stops at 0.938. Across the whole family, edge
count still ranks triadic above dyadic well, which Q72's two-pair view did not measure. Both readings are
correct: a strong rank, an imperfect separator.

## What it does not say

Nothing here extends past n = 3. Q81 established that the surrogate does not generalize to larger forms, so
its perfect in-distribution separation is a within-size result. The comparison says the surrogate is the
best available reader of the verdict at a fixed size, not that it replaces the exact computation.

## Caveats

- **In-distribution only.** Per Q81, the surrogate fails to cross sizes; this study is fixed-size.
- **In-silico.** Boolean models, exact labels, cheap-statistic inputs.
- **Class imbalance.** 9.4% triadic; rank-AUC and the constant-in-degree subset carry the comparison, not
  raw accuracy, which a majority guess already pushes to 0.906.
- **One structural proxy's strength is family-specific.** Edge count's AUC 0.966 is a fact about the
  strict-mediation family, where triadic forms are edge-rich; it need not hold on other form populations.
