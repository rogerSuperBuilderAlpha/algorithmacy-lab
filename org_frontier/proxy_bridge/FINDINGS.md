# Findings — the proxy bridge does not hold for the verdict

From `results/bridge.csv`: 8 coordination forms × 3 noise levels (0.05, 0.1, 0.2) × 3 seeds,
trajectory length 8000, on the IIT-4.0 venv. Two cheap time-series proxies (ΦID Φ_R with CCS
redundancy, and uncorrected whole-minus-sum Φ_WMS) estimated from simulated noisy trajectories,
against the exact structural verdict computed on the deterministic form.

## The question

The survey found that on real systems exact Φ is intractable, so researchers estimate a cheap
proxy from time series and report a lower bound. Organizational coordination also produces time
series. So: **can a cheap proxy estimated from a coordination form's trajectory recover the
literacy/algorithmacy verdict that exact Φ gives on its structure?**

## The answer: no, not reliably

| Proxy | triadic mean | dyadic mean | rank-AUC | best single-threshold accuracy |
|---|---|---|---|---|
| Φ_R (CCS) | +0.139 | +0.091 | 0.563 | 0.736 |
| Φ_WMS (whole-minus-sum) | +0.122 | +0.043 | **0.629** | **0.778** |

Rank-AUC of 0.5 is chance. Φ_WMS separates the two classes better than Φ_R (consistent with this
repo's `candidate_audit`, where whole-minus-sum tracked exact Φ best), but neither proxy cleanly
preserves the binary verdict. The class distributions overlap heavily.

## The failure mode: the proxy confuses dependence with integration

The clearest case is `hierarchy_backchannel`. It is **dyadic** (exact Φ = 0; it factors along the
MIP), yet it draws the **highest** Φ_R among all dyadic forms (+0.205) — higher than two of the
three genuinely triadic forms. The reason: it has a direct worker↔counterpart back-channel, which
produces strong statistical dependence in the trajectory. The cheap proxy reads that dependence as
integration. Exact Φ correctly discounts it, because the system still factors along the
minimum-information partition. `pure_relay` (dyadic, +0.136) fails the same way.

This is the repo's recurring result landing in the coordination domain: cheap proxies track
statistical dependence, not irreducibility, and the two come apart. The population-scale version of
this gap is already documented on random networks in `phiid_vs_phi/` (Φ_R detection AUC ≈ 0.56);
here the same gap appears on curated coordination forms, with the back-channel as a concrete cause.

## What this means for the size ceiling

The proxy bridge was the survey's candidate route past the ~10-12-element exact ceiling. For the
literacy/algorithmacy verdict, that route does not hold: a cheap proxy estimated from interaction
time-series will assign spurious "integration" to forms that structurally factor (e.g. any form
with a real back-channel). The verdict needs the exact structural computation. That is not a
practical problem here, because coordination units are small — the exact classifier runs well under
the ceiling. The proxy bridge is the wrong tool for *this* job, and the result strengthens the case
for the exact classifier rather than weakening it.

## Caveats

- Eight curated forms are an illustration, not a population. The population-level proxy gap is
  `phiid_vs_phi/`'s result; this experiment shows the mechanism on recognizable forms.
- Ground truth is the deterministic structural verdict; noise (0.05-0.2) is added only to make
  trajectories explore states. Exact Φ on the noisy TPM degrades from the deterministic value
  (e.g. gig_false_dyad 2.0 → ~1.16 at noise 0.1), as expected.
- Longer trajectories would tighten the proxy estimates but cannot fix a measure that tracks the
  wrong quantity; the `phiid_vs_phi` population study already establishes the asymptotic gap.
