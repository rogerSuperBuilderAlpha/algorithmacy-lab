# Q6 — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules/parameters), the measure, the controls, and the
decision rule fixed before the run. A reader should reproduce every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `org_frontier/classifier/classifier.py` (`classify_rules`,
  `tpm_from_rules`, `cm_from_rules`), `org_frontier/probes/lib.py` (`verdict`, `major_complex`,
  `max_phi_float`).
- Information measures: `org_frontier/probes/_info.py` (entropy, mutual_information, transfer_entropy,
  o_information).
- Exact Φ / trajectories: `proxy_audit/exact_phi.py`.
- Python: `~/iit-playground/venv-4.0/bin/python`.
- The verdict is the binary structure (`dyadic` vs `triadic`) read off `Φ_MIP` over the most-integrated
  reachable state, with `PHI_EPS = 1e-9` the zero threshold. Φ magnitude is an ordinal hint, per the
  classifier docstring; the phase-transition claims below rest on the verdict and on the *shape* of the
  Φ(p) curve, not on any single Φ value being a true scale.

## The form and the noise model (fixed for every test)
The form is the triadic conjunctive mediated chain at n=3, labels `("W","S","C")`, clean rules
`[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` — `W' = S`, `S' = W & C`, `C' = S` (#26/#33/#27).
The commit is the mediator's next state `S'`. Commit noise of strength `p` is applied as output noise on
the mediator column of the state-by-node TPM: the clean column `tpm_from_rules(...)[:, 1]` (call it
`s_clean ∈ {0,1}` per row) is replaced by the probability `P(S'=1) = (1−p)·s_clean + p·(1−s_clean)`, so
the commit lands on its clean value with reliability `1−p` and flips with probability `p`. The W and C
columns stay deterministic. This makes the flip part of the mechanism's TPM, not an initial-state
injection, per Aguilera (2019). The connectivity matrix is the clean form's `cm_from_rules(...)` (the
noise rescales transition probabilities, it does not add or remove a dependency). `Φ_MIP(p)` is read with
`max_phi_float(noisy_tpm)` (max exact IIT-4.0 Φ over reachable states, inferring `cm` numerically), which
accepts a stochastic state-by-node TPM. The MIP location is read with `classify`'s `mip_partition` on the
same noisy TPM and `cm`.

**The grid (fixed before any run).** `p` runs on a uniform grid of 51 points, `p = 0.00, 0.01, …, 0.50`
(step 0.01). The discrete first derivative is the centered difference
`dΦ/dp|_{p_k} = (Φ(p_{k+1}) − Φ(p_{k−1})) / (2·0.01)` on interior points, forward/backward differences at
the two endpoints. The single 51-point sweep is computed once and reused by every test below. The coarse
6–7-point reliability sample whose blind spots this question probes is #27 at
`p ∈ {0.0, 0.1, 0.2, 0.3, 0.4, 0.5}` (its `r = 1−p`).

## Instrument control (run first)
The clean form at `p = 0` is the established triadic conjunctive chain (#26/#33/#27). It must reproduce
`triadic` with `max_phi = 2.0` (to 1e-6) and MIP `2 parts: {W,SC}` before any swept value in this question
is trusted. Confirmed in pre-registration trial: `verdict(rules, labels)` returns `triadic`,
`max_phi = 2.0`, MIP `2 parts: {W,SC}`; and `max_phi_float(noisy_tpm(0.0))` returns `2.0`. If the `p=0`
endpoint of the sweep does not reproduce `2.0` triadic with MIP `{W,SC}`, halt and do not read the swept
values. This same `p=0` point is the left endpoint of the grid every test uses, so the instrument control
and the sweeps share one reference value.

## H1 test — mean Φ decays smoothly, no kink, no interior discontinuity
- **Form / ensemble:** The noisy conjunctive chain on the full 51-point grid. Measure `Φ_MIP(p)` at every
  grid point via `max_phi_float(noisy_tpm(p))`.
- **Measure:** The Φ(p) curve and its fit residual. Fit two smooth low-order forms to the 51 points by
  least squares: an exponential decay `Φ = a·exp(−b·p) + c` and a quadratic `Φ = a·p² + b·p + c`, each fit
  on the open interior `p ∈ (0, 0.5)` (the 49 points `0.01 … 0.49`, excluding the two degenerate
  endpoints). Record, for the better-fitting form, the max absolute residual and the residual at each
  point; and the second difference `Δ²Φ|_{p_k} = Φ(p_{k+1}) − 2Φ(p_k) + Φ(p_{k−1})` at every interior
  point (a discontinuity or corner shows as a localized `Δ²Φ` spike).
- **Controls:** Instrument control above (left endpoint = 2.0 triadic). Positive control for "a kink is
  detectable by this residual test": the same 51 Φ values with an artificial corner injected — set
  `Φ_test(p) = Φ(p)` for `p ≤ 0.25` and `Φ_test(p) = Φ(0.25)·(0.5−p)/0.25` for `p > 0.25` (a piecewise
  line that kinks at p=0.25), fit and residual-test it the same way; the corner must register as a
  localized residual / `Δ²Φ` spike, confirming the test can see a kink when one is present.
- **Decision rule (fixed before run):** H1 is confirmed if the better smooth fit has max absolute residual
  ≤ 0.02 (1% of the clean Φ=2.0) with no interior point exceeding 3× the median absolute residual, and the
  largest interior `|Δ²Φ|` is below 5× the median interior `|Δ²Φ|` (no localized second-difference spike).
  H1 is refuted if the fit residual exceeds 0.02 at any interior point or a single interior point carries a
  `|Δ²Φ|` spike above 5× the median while its neighbors do not — a kink or jump the coarse #27 sample
  stepped over. Predicted: smooth exponential-like decay from 2.0 toward 0, residuals flat under 0.02, no
  spike; the injected-corner control does spike, proving the test discriminates. H0 refuted.
- **Script:** `probe_q6_smoothness.py`

## H2 test — the sharp feature lives in the susceptibility dΦ/dp, not in mean Φ
- **Form / ensemble:** The same 51-point Φ(p) sweep as H1. Compute the discrete susceptibility
  `χ(p) = dΦ/dp` by centered difference on the interior grid points.
- **Measure:** The location `p_χ = argmax_p |χ(p)|` and the shape of `|χ(p)|`. Record `|χ|` at every
  interior point; locate its maximum; check that `|χ|` rises to that maximum and falls on both sides (a
  single interior peak) versus being largest at an endpoint.
- **Controls:** Instrument control above. H2 is read jointly with H1: the test only counts as a
  "susceptibility-not-mean" result if H1 holds (mean Φ smooth) on the same sweep. Pre-registration trial
  shows the steep clean-limit drop (Φ: 2.0 at p=0 → 1.19 at p=0.1, matching #38's r_c 1.0→0.9 hint), so the
  peak is expected near small p; the decision rule below counts an interior peak as any peak with
  `0 < p_χ < 0.5` strictly, including a near-zero-p peak, but a maximum forced onto the very first interior
  grid point p=0.01 with `|χ|` monotone decreasing thereafter is scored as an endpoint peak (no interior
  maximum).
- **Decision rule (fixed before run):** H2 is confirmed if `|χ(p)|` has an interior maximum — there exists
  an interior grid point `p_χ` with `0.01 < p_χ < 0.49` where `|χ(p_χ)|` exceeds `|χ|` at both immediate
  neighbors and exceeds the value at each endpoint (p→0 and p→0.5) — while H1 holds. H2 is refuted if `|χ|`
  is monotone across the interval or attains its maximum at an endpoint (steepest descent at p→0 or
  p→0.5). Predicted: `|χ|` peaks at an interior `p_χ` biased toward small p and falls on either side,
  matching Niizato (2020) / Popiel (2020) χ_Φ-peaks-at-criticality. H0 refuted.
- **Script:** `probe_q6_susceptibility.py`

## H3 test — verdict flips only at the degenerate endpoint, no interior critical p*
- **Form / ensemble:** The noisy conjunctive chain at every grid point. At each `p` read the binary
  verdict via `classify(noisy_tpm(p), cm)` (`structure ∈ {triadic, dyadic}`, threshold PHI_EPS = 1e-9) and
  the major complex via the same most-integrated-state machinery.
- **Measure:** `structure(p)` across the 51 points and the smallest `p` at which `structure` reads
  `dyadic` (`Φ_MIP ≤ PHI_EPS`). Record whether that first dyadic reading is the random-commit endpoint
  p=0.5 or an interior point, and whether the major complex stays the full triad `{W,S,C}` up to it.
- **Controls:** Instrument control above (p=0 triadic). The PHI_EPS = 1e-9 threshold is the same zero
  cutoff the classifier uses everywhere; no per-test tuning.
- **Decision rule (fixed before run):** H3 is confirmed if `structure(p) = triadic` for every interior
  grid point `p ∈ {0.01, …, 0.49}` and reads `dyadic` only at p=0.5. H3 is refuted if any interior
  grid point reads `dyadic` — a finite interior critical p* where the triad factors below the degenerate
  maximum. Predicted: triadic at all 49 interior points with the major complex the full `{W,S,C}` triad
  throughout (#27/#34/#38/#79); the verdict crosses only at the coin-flip commit p=0.5. H0 refuted.
- **Script:** `probe_q6_verdict_interior.py`

## H4 test — the verdict transition is a step where mean Φ is a smooth ramp (verdict/Φ decoupling)
- **Form / ensemble:** The same sweep, read two ways at every grid point: the continuous `Φ_MIP(p)` (from
  H1) and the binary `structure(p)` (from H3), on the identical 51-point grid and identical noise model.
- **Measure:** Two step sizes across the single transition. For the verdict, the binary jump
  `Δstructure = 1` concentrated entirely in the one grid interval `[p_k, p_{k+1}]` where `structure`
  changes label (its width in `p`). For Φ, the largest single-interval drop `max_k |Φ(p_{k+1}) − Φ(p_k)|`
  and the fraction of the total fall `Φ(0) − Φ(0.5) = 2.0` carried by any one interval. The contrast is:
  the verdict's entire change is one all-or-nothing label flip localized to a single interval, while Φ's
  fall is spread smoothly across the grid (no single interval carries a dominant share).
- **Controls:** Instrument control above. H4 is read jointly with H1 and H3 on the same sweep: it requires
  H1 (Φ smooth: no single Φ interval dominant) and H3 (verdict a clean single flip) to both hold, so the
  step/ramp contrast is between two genuinely co-measured quantities, not an artifact of different grids.
- **Decision rule (fixed before run):** H4 is confirmed if the verdict's whole change is a single
  label flip confined to one grid interval (the verdict is constant `triadic` up to it and constant
  `dyadic` after) AND no single Φ interval carries more than 25% of the total `2.0` fall (Φ smooth, no
  step). H4 is refuted if Φ's fall is itself dominated by one interval carrying > 25% of the total (Φ has
  a step too, so verdict-sharpness and Φ-smoothness do not coexist) or if the verdict degrades through more
  than one interval (no clean step). Predicted: Φ fades smoothly with every interval under 25% of the
  total, while the triadic→dyadic label snaps in the single interval at the p=0.5 endpoint — a
  verdict-level discontinuity on a continuous Φ, matching Niizato (2020). H0 refuted.
- **Script:** `probe_q6_decoupling.py`

## H5 test — Φ_MIP is strictly monotone in commit noise (no interior Φ maximum)
- **Form / ensemble:** The same 51-point Φ(p) sweep. Examine monotonicity across every adjacent grid pair.
- **Measure:** The sequence of forward differences `δ_k = Φ(p_{k+1}) − Φ(p_k)` for `k = 0 … 49`. Count any
  `δ_k > tol` (a step where Φ rises) with `tol = 1e-6` (above PyPhi numerical noise); locate any interior
  local maximum (`δ_{k−1} > tol` and `δ_k < −tol`) other than the p=0 left endpoint.
- **Controls:** Instrument control above. The `tol = 1e-6` floor matches the Φ-reporting precision used to
  fix the instrument value (2.0 to 1e-6), so a "rise" must clear genuine numerical noise to count. Positive
  control for "a rebound would be caught": the same monotonicity test applied to the symmetric tracking-
  phase profile from #81 (Φ = 2.0 at both p=0 and p=1, 0 at p=0.5) — a U-shape that *does* rise on its
  right half — must register `δ_k > tol` on that half, confirming the test detects a non-monotone rise
  when one is present.
- **Decision rule (fixed before run):** H5 is confirmed if every forward difference `δ_k ≤ tol`
  (Φ non-increasing at every grid step) with no interior local maximum. H5 is refuted if any `δ_k > tol`
  on the commit-noise sweep (Φ rebounds) or an interior local Φ maximum exists — commit noise transiently
  raising integration, the Danilczuk (2026) caution. Predicted: Φ decreases at every step from 2.0 toward
  0, no interior peak, echoing the #81 trough-not-peak result; the #81 U-shape control does flag a rise on
  its rising half, proving the test would have caught a rebound. H0 refuted.
- **Script:** `probe_q6_monotonicity.py`
