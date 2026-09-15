# margin_cascade_tau — hypotheses (fixed before computing)

**Question.** For the margin cascade that calls exact IIT-4.0 Φ on uncertain forms, do a
**top-B% ranking** rule and a **threshold-τ** rule agree at matched budget, and which rule
transfers better n=4 → n=5?

**Background (cited, not reopened).** `margin_cascade_phi` WIN: top-B% at B=10%/20% cuts
n=4 FN|tri 10.1%→3.7%→0.7%; fragility adds nothing. Size series 4.8→7.5→9.0; F28;
FN-redesign null. Exact Φ = cached `triadic` on the called subset; cheap OOF elsewhere.

**Protocol.** Probe-125/131 RF(400, seed 0); gating probs from 5-fold `cross_val_predict`
(no leakage). Primary: n=4 unc (N=1000). Validate: n=5 unc (N=500).

**Rules.**
1. **Top-B%** — call exact on the `round(B·N)` forms with smallest `|p−0.5|`.
2. **Fixed τ** — call exact wherever `|p−0.5| < τ` (call rate data-dependent).
3. **τ-calibrated (nested)** — for each of 5 folds: set `τ_B` on the other folds so call
   rate ≈ B, apply to the held-out fold; pool predictions. Compare to top-B% on the same
   held-out folds.

**τ grid (fixed-τ curve):** `{0.02, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25, 0.30, 0.40}`.
**B grid:** `{0.05, 0.10, 0.15, 0.20, 0.25, 0.30}` for matched comparisons.
On-panel identity note: choosing τ as the B-quantile of `|p−0.5|` on the *same* full panel
reproduces top-B% exactly; nested calibration is the non-trivial matched-budget test.

## H1 — nested τ-calibrated ≈ top-B% at B=10% (n=4)

Pooled nested FN|tri for τ-calibrated @ B=0.10 and top-B% @ B=0.10 differ by ≤ **0.02**
(2 pp absolute).

Null: |Δ| > 2 pp.

## H2 — frozen τ from n=4 transfers to n=5 within band

Let `τ*` = B=10% quantile of `|p−0.5|` on n=4 OOF probs. Apply fixed `τ*` to n=5.
Require both:
- realized call rate on n=5 ∈ **[0.05, 0.15]**
- FN|tri within **3 pp** of n=5 top-B% at B=0.10

Null: call rate outside band **or** FN gap > 3 pp.

## H3 — recommend a lab default

If H1 holds and H2 holds (or top-B% clearly dominates transfer), recommend
**B=10% top-B%** as the budgeted default, with `τ*` reported as the equivalent on-panel
threshold for documentation. If H2 fails because frozen τ mis-scales call rate, recommend
**top-B% only** (recompute ranks per panel) as the lab default.

Null for H3: no stable recommendation (both rules disagree >2 pp nested **and** transfer
fails).
