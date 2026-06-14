# Q7 — Stage 4 methods

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
  classifier docstring. The Q7 claims rest on the *shape* and *ordering* of the Φ(p) curves and on the
  binary verdict, not on any single Φ value being a true scale.

## The form, the noise model, and the three sites (fixed for every test)
The form is the triadic conjunctive mediated chain at n=3, labels `("W","S","C")`, clean rules
`[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` — `W' = S`, `S' = W & C`, `C' = S` (#26/#33/#27).
`CLEAN_TPM = tpm_from_rules(RULES)` is the deterministic (8, 3) state-by-node TPM; `CM = cm_from_rules(RULES)`
is the clean connectivity matrix, reused for every `p` (the noise rescales transition probabilities, it does
not add or remove a dependency).

Flip-noise of strength `p` is applied as **output noise** on one or more node columns, exactly the Q6/#140–144
model. For a noised column `c` with clean values `col_clean = CLEAN_TPM[:, c] ∈ {0,1}` per row, the column is
replaced by the probability `P(out=1) = (1−p)·col_clean + p·(1−col_clean)`, so that output lands on its clean
value with reliability `1−p` and flips with probability `p`. The flip rides in the mechanism's TPM, not in the
initial state (Aguilera 2019). The three injection sites are:

- **Mediator site `S`** — noise on column 1 only (the commit `S' = W & C`). This is the Q6/#140–144 baseline
  curve, re-computed here on the Q7 grid so every comparison is against a same-run reference.
- **Party site `W`** — noise on column 0 only (`W' = S`).
- **Party site `C`** — noise on column 2 only (`C' = S`).
- **Joint-party site `WC`** — independent flip-noise on columns 0 and 2 together, same `p` on each.

```python
def noisy_tpm(p, cols):
    t = CLEAN_TPM.copy()
    for c in cols:
        sc = CLEAN_TPM[:, c]
        t[:, c] = (1.0 - p) * sc + p * (1.0 - sc)
    return t
# S: cols=(1,)   W: cols=(0,)   C: cols=(2,)   WC: cols=(0, 2)
```

`Φ_MIP(p)` for any site is `max_phi_float(noisy_tpm(p, cols))[0]` (max exact IIT-4.0 Φ over reachable states,
`cm` inferred numerically; it accepts a stochastic state-by-node TPM and reproduces the deterministic `CM` at
`p=0`). The binary verdict and MIP location at any `p` are `classify(noisy_tpm(p, cols), CM, labels=LABELS)`
(`structure ∈ {triadic, dyadic}`, `mip_partition`), and the major complex is `major_complex` machinery over
the most-integrated reachable state.

**The grid (fixed before any run).** `p` runs on a uniform grid of 51 points, `p = 0.00, 0.01, …, 0.50`
(step 0.01) — the same grid as Q6, so the mediator curve here is directly comparable to #140–144. Each
site's 51-point sweep is computed once and reused across the tests that need it. The discrete first
derivative is the centered difference `dΦ/dp|_{p_k} = (Φ(p_{k+1}) − Φ(p_{k−1})) / (2·0.01)` on interior
points, with one-sided forward/backward differences at the two endpoints. "Grid noise" / numerical
tolerance throughout is `TOL = 1e-6` (the Φ-reporting precision that fixes the instrument value to 2.0).

## Instrument control (run first — shared by every test)
The clean form at `p = 0` is the established triadic conjunctive chain (#26/#33/#27). Before any swept
value is trusted, `verdict(RULES, LABELS)` must return `structure = triadic`, `max_phi = 2.0` (to 1e-6),
MIP `2 parts: {W,SC}`; and `max_phi_float(noisy_tpm(0.0, cols))[0]` must return `2.0` (to 1e-6) for every
site (`S`, `W`, `C`, `WC`) — the four sweeps share the same `p=0` left endpoint, which must read the clean
triad regardless of which column would be noised. Confirmed in pre-registration trial: clean verdict
`triadic`, `max_phi = 2.0`, MIP `2 parts: {W,SC}`; `max_phi_float(noisy_tpm(0.0, ...))` = 2.0 for `S`, `W`,
`C`, `WC`. If any site's `p=0` endpoint does not reproduce `2.0` triadic with MIP `{W,SC}`, halt and do not
read the swept values for that site.

## H1 test — party noise and mediator noise trace different Φ(p) curves
- **Form / ensemble:** Two 51-point sweeps on the shared grid: the mediator curve `Φ_S(p)` (site `S`,
  cols=(1,)) and the party curve `Φ_W(p)` (site `W`, cols=(0,)). The party site is `W` alone; H2 establishes
  whether `W` may stand for "the party site" (see its instrument cross-check).
- **Measure:** The pointwise gap `g(p) = Φ_W(p) − Φ_S(p)` at every interior grid point `p ∈ {0.01, …, 0.49}`;
  its maximum absolute value `g_max = max_p |g(p)|` and the `p` achieving it.
- **Controls:** Instrument control above (both sweeps' `p=0` endpoint = 2.0). Negative/self control for "the
  comparison can read coincidence": the mediator curve compared against itself, `Φ_S(p) − Φ_S(p)`, which must
  be `0` at every grid point (`g_max = 0`), confirming the gap statistic is zero when two identical curves are
  fed in and any nonzero `g_max` on the real pair is a genuine site difference, not a measurement offset.
- **Decision rule (fixed before run):** H1 is **confirmed** if `g_max > 1e-3` (the two curves separate beyond
  grid noise `TOL = 1e-6` by a margin of at least three orders of magnitude) at one or more interior `p`. H1
  is **refuted** if `|g(p)| ≤ 1e-6` at every interior `p` (the party and mediator curves coincide pointwise
  within numerical tolerance). Predicted: the party curve sits strictly below the mediator curve at interior
  `p` (pre-registration: at `p=0.1`, `Φ_W ≈ 0.76` vs `Φ_S ≈ 1.19`, so `g ≈ −0.43`), `g_max ≈ 0.4`, well above
  `1e-3`; the self-control reads `g_max = 0`. H0 refuted: party noise and mediator noise are two curves.
- **Script:** `probe_q7_party_vs_mediator.py`

## H2 test — W-noise and C-noise give the same curve as each other
- **Form / ensemble:** Two 51-point sweeps: the `W`-only curve `Φ_W(p)` (cols=(0,)) and the `C`-only curve
  `Φ_C(p)` (cols=(2,)), on the shared grid.
- **Measure:** The pointwise difference `d(p) = Φ_W(p) − Φ_C(p)` at every grid point (all 51, endpoints
  included); the count of grid points with `|d(p)| > TOL`; the max `|d(p)|`; and the verdict-flip point of
  each site (smallest `p` at which `classify(noisy_tpm(p, cols), CM)` reads `dyadic`), which must match.
- **Controls:** Instrument control above. The `W↔C` swap is the form's clean verdict automorphism (#55): the
  swap maps cols `(0)↔(2)`, and since both clean columns equal `S` (`W' = S`, `C' = S`) the swap is exact, so
  the prediction is an exact (not approximate) overlay. Positive control for "the difference statistic can see
  a real gap": feed `Φ_W(p)` against the *mediator* curve `Φ_S(p)` through the same `d(p)` machinery — it must
  report many points with `|d| > TOL` and a nonzero max (it is the H1 gap), confirming `d(p)` is not
  identically zero by construction and would flag a real W/C difference if one existed.
- **Decision rule (fixed before run):** H2 is **confirmed** if `|d(p)| ≤ TOL = 1e-6` at every one of the 51
  grid points (zero W-vs-C difference) **and** the two sites' verdict-flip points are identical. H2 is
  **refuted** if any grid point shows `|d(p)| > 1e-6` or the two flip points differ. Predicted: exact overlay,
  0/51 flips, `max |d| ≈ 0`, identical flip point at `p=0.5` (pre-registration: `Φ_W` and `Φ_C` agree to
  display precision at every sampled `p`); the `W`-vs-`S` positive control flags many `|d|>TOL` points. H0
  refuted: the party site is one curve, and the H1 / H4 "party" contrast may use `W` as its representative.
- **Script:** `probe_q7_wc_symmetry.py`

## H3 test — the party verdict-collapse point relative to the degenerate endpoint
- **Form / ensemble:** The mediator sweep (site `S`) and the party sweep (site `W`) on the shared grid. At
  each grid point read the binary verdict `classify(noisy_tpm(p, cols), CM, labels=LABELS).structure` and the
  major complex over the most-integrated reachable state.
- **Measure:** For each site, two collapse points. (a) The **strict-verdict** collapse `p_v`: the smallest
  grid `p` at which `structure` reads `dyadic` (`Φ_MIP ≤ PHI_EPS = 1e-9`). (b) The **effective collapse**
  `p_eff`: the smallest grid `p` at which `Φ_MIP(p) < 0.01` (1/200 of the clean Φ=2.0), a fixed
  near-zero-integration threshold standing in for "the triad has effectively factored." Both thresholds are
  fixed here, before the run. Record `p_v` and `p_eff` for `S` and for `W`, and whether the major complex
  stays the full triad `{W,S,C}` up to each.
- **Controls:** Instrument control above (both sites `p=0` triadic). `PHI_EPS = 1e-9` is the classifier's
  standard zero cutoff (no per-test tuning); the `0.01` effective threshold is declared here and used
  identically for both sites, so the `S`-vs-`W` comparison is symmetric.
- **Decision rule (fixed before run):** H3 is read on two registers, both fixed before the run.
  - Strict verdict: H3 is **confirmed** if the party strict-collapse `p_v(W) < p_v(S)` (party verdict flips at
    an interior `p* < 0.5`, strictly before the mediator's). H3 is **refuted** if `p_v(W) = p_v(S) = 0.5`
    (both flip only at the degenerate endpoint) or `p_v(W) ≥ p_v(S)`.
  - Effective collapse (reported alongside, decisive when both strict flips sit at 0.5): the party site
    collapses earlier if `p_eff(W) < p_eff(S)` by at least one grid step.
  Predicted (pre-registration finding, stated honestly): on the strict verdict both sites flip only at
  `p=0.5`, so the strict register is expected to **refute** the H3 claim (`Φ_MIP > 0` for every interior `p`
  at both sites). The asymmetry the hypothesis is after shows up on the effective register — the party Φ
  reaches the near-zero band earlier (`p_eff(W) < p_eff(S)`), the order-parameter signature of party noise
  carrying a smaller integration budget. The two registers are reported separately and the strict one governs
  the H3 verdict.
- **Script:** `probe_q7_verdict_flip.py`

## H4 test — party noise decays Φ faster than mediator noise (asymmetry direction)
- **Form / ensemble:** The mediator sweep `Φ_S(p)` and the party sweep `Φ_W(p)` (cols=(1,) and cols=(0,)) on
  the shared grid.
- **Measure:** The clean-limit slope magnitude at each site, `|dΦ/dp|` evaluated at the first interior grid
  point `p=0.01` by the forward difference from `p=0` — `m_site = |Φ_site(0.01) − Φ_site(0.00)| / 0.01` — and
  the sign of the interior ordering `Φ_W(p) − Φ_S(p)` across `p ∈ {0.01, …, 0.49}` (the count of interior
  points where `Φ_W(p) < Φ_S(p)`).
- **Controls:** Instrument control above. H4 is read **jointly with H1**: the slope comparison only counts if
  H1 holds (the two curves are genuinely distinct on the same sweep), so a steeper party slope is a real
  ordering, not the two curves being the same. Self-control: `m_S` computed against itself is the same number
  on repeat (determinism check, `|Δ| ≤ TOL`).
- **Decision rule (fixed before run):** H4 is **confirmed** if `m_W > m_S` (steeper clean-limit drop for the
  party site) **and** `Φ_W(p) ≤ Φ_S(p)` at every interior `p` (the party curve sits at or below the mediator
  curve across the interior, with strict inequality at one or more points) — party noise destroys integration
  faster per unit `p`, in the direction the worker-on-the-weak-seam prior predicts. H4 is **refuted** if
  `m_W ≤ m_S` (mediator at least as steep, the core-versus-periphery direction) or the interior ordering
  reverses at any point (`Φ_W(p) > Φ_S(p)` for some interior `p`). Predicted: `m_W ≈ |0.76−2.0|/0.1 → ` steeper
  than `m_S ≈ |1.19−2.0|/0.1` at the first step (pre-registration: `Φ_W(0.1)=0.76 < Φ_S(0.1)=1.19`, so the
  party curve drops below immediately and stays below across the interior), `m_W > m_S`. H0 refuted: party
  noise is the steeper site.
- **Script:** `probe_q7_slope_asymmetry.py`

## H5 test — two simultaneously-noised parties interact, the joint collapse is non-additive
- **Form / ensemble:** Three 51-point sweeps: the single-party curve `Φ_W(p)` (cols=(0,)), the single-party
  curve `Φ_C(p)` (cols=(2,)), and the joint-party curve `Φ_WC(p)` (independent flip-noise on cols=(0,2)
  together, same `p` each).
- **Measure:** Two quantities. (a) **Non-additivity / non-separability:** at every interior grid point compare
  the joint curve to the separable prediction from the single-party curves. The fixed separable null is the
  independent-flip composition of the two single-party reliabilities — define the per-site *Φ-drop fraction*
  `f_site(p) = 1 − Φ_site(p)/2.0`, and the separable prediction `Φ_pred(p) = 2.0·(1 − f_W(p))·(1 − f_C(p))`
  (the integration that survives if the two party noises acted independently and multiplicatively on the
  surviving fraction). Record the residual `r(p) = Φ_WC(p) − Φ_pred(p)` at every interior `p`, its max
  absolute value `r_max`, and the `p` achieving it. (b) **Effective collapse shift:** the smallest grid `p` at
  which `Φ_WC(p) < 0.01` (`p_eff(WC)`, the same 0.01 effective threshold as H3) versus that of the single
  party `p_eff(W)`; and whether the joint curve has any interior local maximum (a forward-difference rise
  `Φ_WC(p_{k+1}) − Φ_WC(p_k) > TOL` after an earlier fall — the Danilczuk 2026 transient-rise corroborant).
- **Controls:** Instrument control above (all three sweeps `p=0` = 2.0). H5 reuses the H2 result: `Φ_W` and
  `Φ_C` are the same curve, so `f_W = f_C` and the separable null reduces to `Φ_pred = 2.0·(1−f_W)²`; the test
  is whether the conjunction couples the two flips beyond that square. Positive control for "the residual
  statistic reads non-additive when it should": feed the separable prediction `Φ_pred(p)` into the residual
  machinery against itself — `Φ_pred − Φ_pred ≡ 0` — confirming `r(p)` is zero for a truly separable curve, so
  any nonzero `r_max` on the real joint curve is genuine coupling.
- **Decision rule (fixed before run):** H5 is **confirmed** if `r_max > 1e-3` (the joint curve departs from
  the separable independent-flip prediction beyond grid noise) **and** the joint effective collapse precedes
  the single-party one, `p_eff(WC) < p_eff(W)` by at least one grid step (conjunction moves the effective
  collapse earlier than either party alone). H5 is **refuted** if `|r(p)| ≤ 1e-3` at every interior `p` (the
  joint curve is the separable composition of the single-party curves) **and** `p_eff(WC) = p_eff(W)`. A
  non-monotone interior excursion in `Φ_WC`, if present, is recorded as the weaker corroborant but is not
  required for confirmation. Predicted: `Φ_WC` departs from the squared-survival prediction (pre-registration:
  `Φ_WC(0.1)=1.37` vs single-party `Φ_W(0.1)=0.76`, so the joint curve is far above twice-the-single-drop and
  off the multiplicative null), `r_max` well above `1e-3`, and the joint near-zero band is reached before the
  single party's. The strict verdict still flips at `p=0.5` (pre-registration), so the "off 0.5" claim is
  carried by the effective-collapse register, reported as such. H0 refuted: conjunction couples the two party
  noises.
- **Script:** `probe_q7_joint_party.py`
