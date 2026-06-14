# Q8 — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules/parameters), the measure, the controls, and the
decision rule fixed before the run. A reader should reproduce every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `org_frontier/classifier/classifier.py` (`classify`, `classify_rules`,
  `tpm_from_rules`, `cm_from_rules`), `org_frontier/probes/lib.py` (`verdict`, `major_complex`,
  `max_phi_float`).
- Information measures: `org_frontier/probes/_info.py` (entropy, mutual_information, transfer_entropy,
  o_information).
- Exact Φ / trajectories: `proxy_audit/exact_phi.py`.
- Python: `~/iit-playground/venv-4.0/bin/python`.
- The verdict is the binary structure (`dyadic` vs `triadic`) read off `Φ_MIP` over the most-integrated
  reachable state, with `PHI_EPS = 1e-9` the zero threshold. Φ magnitude is an ordinal hint, per the
  classifier docstring. The Q8 claims rest on the *shape* and *ordering* of the two hubs' Φ(p) curves and
  on the binary verdict, not on any single Φ value being a true scale.

## The two forms, the noise model, and the sizes (fixed for every test)
Node 0 is the hub `S`; nodes 1…n−1 are the parties. Each party reads the hub (`party' = S`). The two hub
forms differ only in the commit rule on node 0:

- **Parity (XOR) hub** — `S' = x[1] ⊕ x[2] ⊕ … ⊕ x[n−1]` (XOR of all parties).
  `parity_hub(n)` from `probe_parity_scaling.py` (#115). Clean Φ = `2^(2−n)` (0.5 at n=3, 0.25 at n=4),
  triadic, MIP the all-singletons cut.
- **Conjunctive (AND-all) hub** — `S' = x[1] ∧ x[2] ∧ … ∧ x[n−1]` (AND of all parties).
  `single_hub(n)` from `probe_distributed_mediators.py` (#116). Clean Φ = `n−1` (2.0 at n=3, 3.0 at n=4),
  triadic.

Both forms are run at **n=3 and n=4**. Labels are `tuple(f"n{i}" for i in range(n))`.
`CLEAN_TPM = tpm_from_rules(rules)` is the deterministic state-by-node TPM; `CM = cm_from_rules(rules)` is
the clean connectivity matrix, reused for every `p` (the noise rescales transition probabilities, it does
not add or remove a dependency).

Flip-noise of strength `p` is applied as **output noise on the hub column (node 0)**, exactly the Q6/Q7
model. With clean hub column `col_clean = CLEAN_TPM[:, 0] ∈ {0,1}` per row, the column is replaced by the
probability `P(S'=1) = (1−p)·col_clean + p·(1−col_clean)`, so the commit lands on its clean value with
reliability `1−p` and flips with probability `p`. The party columns stay deterministic. The flip rides in
the mechanism's TPM, not in the initial state (Aguilera 2019).

```python
def noisy_tpm(rules, p):
    t = tpm_from_rules(rules).copy()
    sc = t[:, 0]
    t[:, 0] = (1.0 - p) * sc + p * (1.0 - sc)   # hub commit is node 0
    return t
```

`Φ_MIP(p)` for either form at either size is `max_phi_float(noisy_tpm(rules, p))[0]` (max exact IIT-4.0 Φ
over reachable states, `cm` inferred numerically; it accepts a stochastic state-by-node TPM and reproduces
the deterministic `CM` at `p=0`). The binary verdict and MIP location at any `p` are
`classify(noisy_tpm(rules, p), CM, labels=LABELS)` (`structure ∈ {triadic, dyadic}`, `mip_partition`); the
major complex is `major_complex` machinery over the most-integrated reachable state.

**The grid (fixed before any run).** `p` runs on a uniform grid of 51 points, `p = 0.00, 0.01, …, 0.50`
(step 0.01) — the same grid as Q6/Q7, so the conjunctive curve here is directly comparable to #140–144.
Four sweeps (parity-n3, parity-n4, conjunctive-n3, conjunctive-n4) are each computed once and reused
across the tests that need them. The discrete first derivative is the centered difference
`dΦ/dp|_{p_k} = (Φ(p_{k+1}) − Φ(p_{k−1})) / (2·0.01)` on interior points, with one-sided forward/backward
differences at the two endpoints. Numerical tolerance throughout is `TOL = 1e-6` (the Φ-reporting precision
that fixes the clean values).

**Normalized curve (used by H2, H3).** `Φ̂_form,n(p) = Φ_form,n(p) / Φ_form,n(0)` rescales each sweep to its
own clean value, removing the starting-magnitude gap (0.5/0.25 vs 2.0/3.0). The *drop fraction* is
`f_form,n(p) = 1 − Φ̂_form,n(p)`.

## Instrument control (run first — shared by every test)
The two clean forms at `p = 0` are the established hubs from #115 and #116. Before any swept value is
trusted, the four clean endpoints must reproduce their known verdicts and Φ:

| form | n | required verdict | required Φ (to 1e-6) |
|------|---|------------------|---------------------|
| parity (XOR) | 3 | triadic | 0.5  |
| parity (XOR) | 4 | triadic | 0.25 |
| conjunctive (AND-all) | 3 | triadic | 2.0 |
| conjunctive (AND-all) | 4 | triadic | 3.0 |

Confirmed in pre-registration trial: `max_phi_float(noisy_tpm(rules, 0.0))[0]` returns 0.5, 0.25, 2.0, 3.0
respectively, all `triadic` (parity MIP all-singletons, conjunctive MIP `{n0n1,n2}` at n=3). The
conjunctive n=3 endpoint (Φ=2.0, triadic) is the same reference value Q6/Q7 used, tying this question's
instrument to those runs. If any form's `p=0` endpoint does not reproduce its tabled value and `triadic`,
halt and do not read that form's swept values.

## H1 test — parity verdict flips at an interior p; conjunctive holds to the endpoint
- **Form / ensemble:** All four sweeps. At each grid point read the binary verdict
  `classify(noisy_tpm(rules, p), CM, labels=LABELS).structure` and the major complex over the
  most-integrated reachable state.
- **Measure:** For each (form, n), the **strict verdict-flip point** `p_v` — the smallest grid `p` at which
  `structure` reads `dyadic` (`Φ_MIP ≤ PHI_EPS = 1e-9`). Record `p_v(parity, n)` and `p_v(conj, n)` at n=3
  and n=4, and whether the major complex stays the full hub-plus-parties set up to `p_v`.
- **Controls:** Instrument control above (all four `p=0` endpoints triadic). `PHI_EPS = 1e-9` is the
  classifier's standard zero cutoff (no per-test tuning), applied identically to both forms so the
  parity-vs-conjunctive comparison is symmetric. Negative control for "an interior dyadic reading is real,
  not a numerical artifact": at each grid point also record `max_phi_float`'s raw Φ; a `dyadic` reading
  must carry `Φ_MIP ≤ PHI_EPS` while its left neighbor carries `Φ_MIP > PHI_EPS`, so the flip is a genuine
  zero-crossing of the same statistic, not a one-point dropout.
- **Decision rule (fixed before run):** H1 is **confirmed** if, at both n=3 and n=4,
  `p_v(parity, n) < 0.5` strictly (the parity verdict flips at an interior `p`) **and** `p_v(conj, n) = 0.5`
  (the conjunctive verdict holds through every interior `p` and flips only at the degenerate endpoint). H1
  is **refuted** if the parity verdict also flips only at `p=0.5` at either size (`p_v(parity, n) = 0.5`),
  i.e. both forms cross dyadic only at the coin-flip maximum — the H0 outcome. Pre-registration trial
  (coarse 6-point grid `p ∈ {0,…,0.5}`) finding, stated honestly: at this resolution **both** forms carry
  `Φ_MIP > 0` at every interior `p` and read `dyadic` only at `p=0.5`, at both n=3 and n=4. On that
  evidence the strict register is expected to **refute** the H1 claim. The 51-point sweep is the
  pre-registered finer test; H1 stands only if a parity dyadic reading appears at some interior grid point
  the coarse sample stepped over.
- **Script:** `probe_q8_verdict_flip.py`

## H2 test — parity Φ decays faster than conjunctive Φ in flip fraction (normalized decay)
- **Form / ensemble:** All four sweeps, rescaled to the normalized curves `Φ̂_form,n(p)` and drop fractions
  `f_form,n(p)`. Compared at matched n: parity vs conjunctive at n=3, and parity vs conjunctive at n=4.
- **Measure:** Two quantities at matched n. (a) **Fraction lost at every interior p:** the count of interior
  grid points `p ∈ {0.01,…,0.49}` where `f_parity,n(p) > f_conj,n(p)` (parity has shed a larger fraction).
  (b) **Clean-limit log-slope:** `L_form,n = |Δ log Φ̂ / Δp|` at the first interior step, estimated as
  `|log Φ̂_form,n(0.01) − log Φ̂_form,n(0)| / 0.01 = |log Φ̂_form,n(0.01)| / 0.01` (since `Φ̂(0)=1`). H2's
  direction needs `L_parity,n > L_conj,n`.
- **Controls:** Instrument control above (all four `p=0` endpoints reproduce `Φ̂=1`). Self/identity control
  for "the fraction comparison reads coincidence as zero, not as a spurious lead": compare each normalized
  curve against itself, `f_form,n − f_form,n ≡ 0`, which must give 0 interior points won, confirming the
  point-count statistic is zero when two identical curves are fed and any nonzero count on the real pair is
  a genuine decay-rate difference.
- **Decision rule (fixed before run):** H2 is **confirmed** if, at **both** n=3 and n=4, the parity curve
  has lost a strictly larger fraction at every interior grid point (`f_parity,n(p) > f_conj,n(p)` for all 49
  interior `p`) **and** the clean-limit log-slope is steeper for parity (`L_parity,n > L_conj,n`). H2 is
  **refuted** if at either size the conjunctive curve has lost the larger fraction at any interior point
  (`f_conj,n(p) ≥ f_parity,n(p)`) or `L_conj,n ≥ L_parity,n` — the conjunctive form decays at least as fast
  in fraction, the H0 (or sign-reversed) outcome. Pre-registration trial finding, stated honestly: on the
  coarse grid the **conjunctive** form sheds the larger fraction at every interior `p` at both sizes
  (e.g. n=3 at p=0.1, `Φ̂_parity=0.763` vs `Φ̂_conj=0.594`; n=4 at p=0.1, `Φ̂_parity=0.763` vs
  `Φ̂_conj=0.407`), so the measured ordering runs **opposite** to H2's prediction. On that evidence H2 is
  expected to be **refuted**, and the parity normalized curve is observed n-independent (identical at n=3
  and n=4) rather than steeper. The decision rule above is fixed before the full-grid run and adjudicates it.
- **Script:** `probe_q8_normalized_decay.py`

## H3 test — the verdict-flip gap widens with n
- **Form / ensemble:** All four sweeps. Two registers, both fixed before the run.
  (a) **Strict verdict-flip point** `p_v(form, n)` from H1 (`Φ_MIP ≤ PHI_EPS`).
  (b) **Effective collapse point** `p_eff(form, n)`: the smallest grid `p` at which the *normalized* curve
  `Φ̂_form,n(p) < 0.01` (1/100 of the form's own clean Φ — a fixed near-zero-integration band declared here,
  identical for both forms and both sizes so the comparison is symmetric). The effective register stands in
  for "the hub has effectively factored" when both strict flips sit at the degenerate endpoint.
- **Measure:** The flip-gap `G_v(n) = p_v(conj, n) − p_v(parity, n)` on the strict register and
  `G_eff(n) = p_eff(conj, n) − p_eff(parity, n)` on the effective register, each at n=3 and n=4; and the
  difference across sizes `G(4) − G(3)`. Record whether parity's own flip point moves to lower `p` as n
  grows (`p_par*(4) < p_par*(3)` on whichever register governs).
- **Controls:** Instrument control above. `PHI_EPS = 1e-9` and the `0.01` effective band are the same fixed
  thresholds used for both forms at both sizes (no per-size tuning). H3 is read **jointly with H1**: which
  register governs is decided by H1 — if H1's strict parity flips are interior at both sizes, `G_v` governs;
  if the strict flips sit at 0.5 (the trial-expected outcome), the effective register `G_eff` governs and is
  reported as such.
- **Decision rule (fixed before run):** H3 is **confirmed** if, on the governing register, the gap is
  strictly larger at n=4 than n=3 (`G(4) > G(3)`) **and** parity's flip point moves to a lower `p` from n=3
  to n=4 (`p_par*(4) < p_par*(3)`), while the conjunctive flip stays at or near the endpoint (`p_v(conj, n)
  = 0.5` on the strict register, or `p_eff(conj, n)` not earlier than parity's on the effective one). H3 is
  **refuted** if `G(4) ≤ G(3)` (the gap does not widen) or parity's flip does not move earlier with size.
  Pre-registration trial finding, stated honestly: on the strict register both forms flip only at `p=0.5`
  at both sizes, so `G_v(3) = G_v(4) = 0` and the strict register **refutes** H3 outright. On the effective
  register the parity normalized curve is observed n-independent (the same `Φ̂(p)` at n=3 and n=4), so
  `p_eff(parity, 3) = p_eff(parity, 4)` is expected — parity's flip does *not* move earlier with size — and
  the conjunctive curve decays *faster* at n=4 than n=3, so `G_eff` is expected to **narrow or invert**, not
  widen. On that evidence H3 is expected to be **refuted** on both registers. The decision rule is fixed
  before the full-grid run.
- **Script:** `probe_q8_gap_scaling.py`

## H4 test — the parity collapse threshold tracks (1−2p)^n
- **Form / ensemble:** The two parity sweeps (n=3, n=4), read on the normalized curve `Φ̂_parity,n(p)`.
- **Measure:** Two quantities at each n. (a) The **measured collapse** `p_par*` — the smallest grid `p` at
  which `Φ̂_parity,n(p)` drops below the resolution floor `r_n` that the hypothesis names: `r_n = (Φ floor)
  / 2^(2−n)` with `Φ floor = PHI_EPS = 1e-9`, i.e. on the normalized curve the floor is `Φ̂ < PHI_EPS /
  Φ_parity,n(0)`; this collapses to the strict verdict-flip `p_v(parity, n)` from H1, so `p_par*` is read as
  that flip. (b) The **closed-form prediction** `p_pred(n)` solving `(1 − 2·p_pred)^n = r_n` for the same
  `r_n`, evaluated at n=3 and n=4. The contrast is `|p_par* − p_pred(n)|` versus the grid spacing 0.01.
  A weaker corroborant, recorded but not decisive: across the whole interior, the residual between the
  measured normalized parity curve and the `(1−2p)^n` curve, `max_p |Φ̂_parity,n(p) − (1−2p)^n|`.
- **Controls:** Instrument control above (parity `p=0` endpoints = 0.5 and 0.25, `Φ̂(0)=1 = (1−2·0)^n`, so
  the closed form and the measured curve start at the same point). Positive control for "the residual
  statistic can see a curve that does match": feed the analytic `(1−2p)^n` sampled on the grid against
  itself through the residual machinery — it must return `max residual = 0`, confirming the statistic reads
  zero for an exact match and any nonzero residual on the real parity curve is a genuine departure.
- **Decision rule (fixed before run):** H4 is **confirmed** if, at **both** n=3 and n=4, the measured parity
  collapse lands within one grid step of the closed form (`|p_par* − p_pred(n)| ≤ 0.01`). H4 is **refuted**
  if `|p_par* − p_pred(n)| > 0.01` at either size — the partition-minimization structure of Φ_MIP shifts the
  collapse off the Boolean-function prediction. Pre-registration trial finding, stated honestly: the
  measured normalized parity curve is n-**independent** (identical at n=3 and n=4: 0.880 at p=0.05, 0.763 at
  p=0.10, 0.542 at p=0.20), whereas `(1−2p)^n` is strongly n-dependent (0.729 vs 0.656 at p=0.05; 0.512 vs
  0.410 at p=0.10), so the parity curve does **not** track `(1−2p)^n` and the per-interior residual is large
  and grows with n. On that evidence H4 is expected to be **refuted**: the Boolean-function law gives the
  wrong shape for the IIT collapse, and the parity normalized decay follows a single n-independent law
  closer to `(1−2p)` than to `(1−2p)^n`. The decision rule above is fixed before the full-grid run and is
  the deliberately sharpest, most falsifiable Q8 claim.
- **Script:** `probe_q8_boolean_law.py`

## H5 test — parity collapses as a cliff, conjunctive as a glide (shape of dΦ/dp)
- **Form / ensemble:** All four sweeps. For each, the susceptibility `χ_form,n(p) = dΦ/dp` by centered
  difference on the interior grid points; read on the form's own (un-normalized) Φ(p) so the shape is the
  raw decay shape.
- **Measure:** For each (form, n): the location `p_χ = argmax_p |χ(p)|` over the interior grid and whether
  `|χ(p)|` has an **interior peak** (a grid point `0.01 < p_χ < 0.49` where `|χ|` exceeds both immediate
  neighbors and both endpoints) versus its maximum sitting at an endpoint (steepest at `p→0`). H5 needs the
  parity curve to show an interior susceptibility peak (a knee) that the conjunctive curve lacks. Weaker
  corroborant, recorded for both forms: any non-monotone excursion (a forward-difference rise
  `Φ(p_{k+1}) − Φ(p_k) > TOL` after an earlier fall — the Orio–Mediano–Rosas 2023 transient-rise caution),
  so monotonicity is not assumed before measurement.
- **Controls:** Instrument control above. Positive control for "an interior knee is detectable by this
  test": apply the same argmax/neighbor test to a synthetic piecewise-linear curve with a deliberate corner
  — `Φ_test(p) = Φ_parity,3(0)` for `p ≤ 0.25` then a steeper line to 0 at `p=0.5` — whose `|χ|` jumps at
  p=0.25; the test must locate `p_χ = 0.25` as an interior peak, confirming it can see a knee when one is
  present. H5 is read **jointly with H1**: the cliff/glide contrast is between two co-measured curves on the
  one grid.
- **Decision rule (fixed before run):** H5 is **confirmed** if, at **both** n=3 and n=4, the parity
  `|χ_parity,n(p)|` has an interior maximum (`0.01 < p_χ < 0.49`, exceeding both neighbors and both
  endpoints) **and** the conjunctive `|χ_conj,n(p)|` is monotone-decreasing from `p=0` with its maximum at
  the left endpoint (no interior peak). H5 is **refuted** if the parity susceptibility has no interior peak
  (its `|χ|` maximal at an endpoint, the parity curve a scaled glide) or the conjunctive susceptibility
  itself shows an interior peak (both forms have a knee, no distinguishing signature). Pre-registration
  trial finding, stated honestly: on the coarse grid **both** forms' Φ(p) fall fastest near `p=0` and
  flatten toward `p=0.5` (parity n=3: 0.50→0.38→0.27→0.17→0.08→0; conjunctive n=3: 2.0→1.19→0.68→0.35→0.14→0)
  — both look like monotone glides with the steepest slope at the left endpoint and no obvious interior
  knee. On that evidence H5 is expected to be **refuted**: the parity collapse is a scaled-down glide, not a
  phase-transition cliff. The 51-point susceptibility curve is the pre-registered finer test; the
  injected-corner control confirms an interior knee would register if present.
- **Script:** `probe_q8_cliff_vs_glide.py`
