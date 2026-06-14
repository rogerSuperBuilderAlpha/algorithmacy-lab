# Q82 — Stage 3 hypotheses (fixed before computation)

Four hypotheses comparing the learned surrogate of Q81 to the single cheap proxies that failed to
recover the outreach verdict in Q72 and `proxy_bridge`. All on the same labelled n=3 outreach family
(256 forms, exact-Φ labels). Written and committed before any comparison result is read. Scope is
in-distribution only: Q81 already established that the surrogate does not generalize past the size it
trains on, so Q82 asks the narrower question of whether, within a fixed size, combining features beats
every single proxy.

The single proxies under test: mediator in-degree and total edges (the structural proxies of Q72), and
ΦID Φ_R and whole-minus-sum Φ_WMS (the time-series proxies of `proxy_bridge`).

## H1 — Every single proxy fails on this family

- **Claim:** Each of the four single proxies has rank-AUC < 0.85 on the n=3 family — none separates the
  verdict cleanly on its own.
- **H0:** Some single proxy has rank-AUC ≥ 0.85.
- **Predicted outcome:** all four below 0.85. H0 refuted. (Q72 and `proxy_bridge` found ≈ 0.56–0.63.)

## H2 — The surrogate's separation far exceeds every single proxy

- **Claim:** The surrogate's 5-fold CV ROC-AUC is ≥ 0.95 and strictly exceeds every single proxy's
  rank-AUC.
- **H0:** The surrogate's AUC is < 0.95, or some single proxy matches or beats it.
- **Predicted outcome:** surrogate ≥ 0.95 and highest. H0 refuted.

## H3 — The surrogate's accuracy exceeds the best single proxy's best threshold

- **Claim:** The surrogate's CV accuracy exceeds the best single proxy's best-threshold accuracy on the
  same set.
- **H0:** Some single proxy's best-threshold accuracy matches or exceeds the surrogate's CV accuracy.
- **Predicted outcome:** surrogate higher. H0 refuted.

## H4 — The surrogate separates where the structural proxy is constant

- **Claim:** On the subset of forms sharing the modal mediator in-degree — where the structural proxy is
  constant and cannot separate, the regime of the Q72 read_recipient/one_shot collision — the surrogate's
  out-of-fold CV accuracy is ≥ 0.90.
- **H0:** out-of-fold accuracy on that subset < 0.90.
- **Predicted outcome:** ≥ 0.90. H0 refuted — the combination reads what a constant structural proxy
  cannot.
