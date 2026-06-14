# Q81 — Stage 1 review: a learned surrogate for the outreach verdict

## The question

The exact-Φ classifier runs only on small forms. The agenda's estimation frontier asks whether a learned
surrogate, fit on small forms an exact computation can label, predicts the verdict on forms too large to
label exactly. The test that matters is generalization: trained at one size, does the surrogate hold at a
larger one?

## What the lab already knows that bears on this

- **No single cheap proxy recovers the verdict (Q72, Finding 7; `proxy_bridge`).** Structural proxies
  collide; time-series proxies separate the classes only near chance (rank-AUC ≈ 0.56–0.63). Cheap signals
  track dependence, not irreducibility.
- **A forest over many cheap features recovers the verdict in-distribution (probe #21).** On the 256-form
  family, combining features succeeds where each fails. That probe's feature panel grows with n, so it
  cannot be applied across sizes.
- **The exact ceiling is ~10–12 elements.** Past it, only an estimate is available, which is the entire
  motivation for a surrogate.

## The gap

Probe #21 left the generalization question open because its features are not size-invariant. Whether a
surrogate built on intensive features crosses the size ceiling is uncomputed. This study fixes a
size-invariant panel and tests training at n = 3 against held-out forms at n = 4, 5, 6.
