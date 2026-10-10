# ergodic_cycle_ordering — hypotheses (fixed before computing)

**Question (Strand G / T8 residual).** On a deterministic cycle the finite-T
remainder of a party-bit time average depends on the order in which the bit
changes, not only on how often it changes. The basin-mode Equality-of-Averages
gap on the frozen 42-form panel still ranks whole-form triadic above dyadic
(AUC 0.729; `studies/ergodic_gap_decomposition/`), the gap magnitude scales
as ∼1/T, and `party_osc_frac` does not mediate that ranking (β ratio 0.985).
Does the ordering of party-bit flips around the attractor drive the leftover
gap–Φ link?

**Already known (cited, not reopened).**
- Basin fix (`ergodic_eoa_basin`): continuous basin-mode gap ranks triadic
  status (AUC 0.729). Verdict `EOA_BASIN_INCONCLUSIVE`.
- Settling residual (`ergodic_settling_time`): mean transient does not
  absorb the link. Verdict `SETTLING_NULL`.
- Gap decomposition (`ergodic_gap_decomposition`): verdict
  `GAP_UNEXPLAINED`. Phase artifact, within-basin heterogeneity,
  party-oscillation mediation, and panel composition were REFUTED. Secondary
  facts this study takes as given: mean log-log slope −0.976; mean CV of
  `gap·T` ≈ 0.0049; party-gap AUC 0.729 versus mediator-gap AUC 0.498;
  `party_osc_frac` β ratio 0.985.

**Null stated plainly.** Ordering may not explain the association either.
An amplitude or flip-rate covariate may fail as well. The original AUC may
be a small-panel fluke. Each of those is a legitimate result.

**Derived on a deterministic cycle (no panel numbers).** Let a party bit
take values \(x_0,\ldots,x_{p-1}\) on a cycle of period \(p\), with mean
\(\mu\). For horizon \(T = qp + r\), \(r = T \bmod p\), the time average
from phase \(\varphi\) is \(\mu\) when \(r = 0\), and otherwise

\[
\bar A_T(\varphi) - \mu = \frac{1}{T}\left(\sum_{k=0}^{r-1} x_{(\varphi+k)\bmod p} - r\mu\right).
\]

The right-hand side depends on the circular order once the window is long
enough to see runs (\(r \notin \{0\}\); at \(r = 1\) and \(r = p-1\) it
collapses to a function of the multiset alone). `gap·T` is therefore a
phase remainder. Whether that remainder, and the order features that set
it, track \(\Phi_{\mathrm{MIP}}\) is the conjecture under test.

**Instrument (committed before this study's numbers).** Reuses
`org_frontier.ergodicity.eoa` (basin reference, `trajectory_time_average`)
and `org_frontier.ergodicity.settling` (attractor partition).
Backward-compatible extension (f), unit-tested in
`org_frontier/ergodicity/test_cycle_order.py` on control maps and on
abstract binary cycles, adds the covariates below. Prior call sites are
unchanged. No \(\Phi\) is computed inside the extension. Whole-form
\(\Phi\) and the triadic label are read from the committed basin CSV.

**Panel (identical freeze).** G2 core (9) + classifier (5) + ejection (2)
+ random n=3 seed `20260930` (20) + n=4 tractable (6) = **42** forms
(17 triadic, 25 dyadic). CI subset: G2 + classifier + ejection via
`--ci` (no random n=3, no n=4). Full-panel hypotheses are
`NOT_TESTABLE` under `--ci`. H5 is scored on whichever panel is evaluated.

**Primary residual gap.** Basin-mode pooled party-bit `gap_mean` at
`T=64`, `noise=0`, matching `ergodic_eoa_basin`. Party bits are every
coordinate whose label is not `S`. The gap is recomputed and must match
the committed CSV (H5).

**Statistics (frozen).**
- Logistic of triadic on standardized predictors (divide by \(n\), not
  \(n-1\)); report the slope on the gap and its two-sided normal p.
  Shrink rule: \(|\beta_{\mathrm{partial}}| / |\beta_{\mathrm{uni}}| \le 0.50\).
- Spearman \(\rho\) of a score vs \(\Phi\); partial Spearman controlling
  for one covariate; two-sided permutation p (2000 shuffles, seed
  `20260930`).
- Rank-AUC vs triadic. Bootstrap CI: 2000 stratified resamples, seed
  `20260930`, 2.5th and 97.5th percentiles of the sorted replicates
  (index \(\lfloor 0.025(N-1)\rfloor\) and \(\lfloor 0.975(N-1)\rfloor\)).
  Label-permutation p is two-sided against chance 0.5 (2000 shuffles,
  same seed).
- A covariate with sample variance below \(10^{-15}\) cannot absorb:
  its mediation hypothesis is REFUTED.
- T-grid for the scaling clause: \(T \in \{16, 32, 64, 128, 256, 512\}\),
  basin mode, noise 0, pooled party bits. Per form, OLS slope of
  \(\log(\mathrm{gap}+10^{-12})\) on \(\log T\). Coefficient of variation
  of \(\mathrm{gap}\cdot T\) across the grid; forms with mean
  \(\mathrm{gap}\cdot T = 0\) are omitted from the panel mean of that CV
  (a panel of exact zeros passes the CV clause vacuously).

**Absorption rule (one covariate).** The covariate absorbs the gap–triadic
link when either

1. **Shrink.** \(|\beta_{\mathrm{partial}}| / |\beta_{\mathrm{uni}}| \le 0.50\)
   and \(|\rho(\mathrm{gap}, \Phi \mid \mathrm{covariate})| < |\rho(\mathrm{gap}, \Phi)|\),
   both Spearman values finite, or
2. **Identity, remainder covariates only.** The covariate is
   `pred_gap_cycle` or `remainder_allstarts`, its Pearson correlation
   with the basin gap is at least 0.99, and the mean absolute difference
   is at most \(10^{-3}\).

Clause 2 does not apply to sequence features. A remainder covariate that
fires clause 2 is SUPPORTED and is **excluded from the ranking**: it
restates the gap, so the ranking asks which sequence feature accounts for
the association.

**Primary ranking rule.** Among covariates that pass the absorption rule
and are not identity-excluded, the winner is the smallest
\(|\beta_{\mathrm{partial}}| / |\beta_{\mathrm{uni}}|\). Tie: the larger
drop \(|\rho_{\mathrm{uni}}| - |\rho_{\mathrm{partial}}|\). If none pass,
there is no winner. The descriptive minimum ratio is still reported.

---

## Covariates

All summaries use the zero-noise attractor partition. Basin-mass weights
are ensemble counts (the full state space). Within a cycle, phases are
uniform on the cycle states. Party bits are averaged with equal weight.
Constant bits contribute 0 to `order_index`, `order_excess`, and
`lag1_autocorr`.

| id | mechanism | covariate |
|---|---|---|
| (a) | Phase-remainder identity | `pred_gap_cycle` — basin-mass-weighted mean, over cycles and party bits, of the mean over phases of \(\|\bar A_T - \mu\|\) at \(T=64\). Cycle states only. |
| (a′) | All-start remainder vs cycle mean | `remainder_allstarts` — mean over starts and party bits of \(\|\bar A_T - \mu_{\mathrm{cycle}}\|\), transients included, reference = cycle mean (not the basin mean of time averages) |
| (b) | Ordering beyond amplitude | `order_index` — for each party bit, \((R_{\mathrm{obs}} - R_{\mathrm{spread}}) / (R_{\mathrm{clump}} - R_{\mathrm{spread}})\) at the same \(T\), or 0 if the denominator is below \(10^{-15}\). \(R_{\mathrm{spread}}\) is the mean absolute remainder of the most even placement of the same weight (the \(k\)-th one at \((k p)/w\)); \(R_{\mathrm{clump}}\) puts all ones first. |
| (b′) | Same contrast in gap units | `order_excess` = \(R_{\mathrm{obs}} - R_{\mathrm{spread}}\), basin-mass-weighted |
| (b″) | Co-flip synchrony | `cofilip_sync` — among cycle steps where at least one party bit flips, the fraction where at least two flip. No flip steps ⇒ 0. Independent of \(T\). |
| (b‴) | Phase lag | `phase_lag` — mean over non-constant party-bit pairs of \(\min(\ell^\star, p-\ell^\star)/(p/2)\), where \(\ell^\star\) is the smallest lag maximizing the circular cross-covariance. No eligible pair ⇒ 0. Independent of \(T\). |
| (b⁗) | Lag-1 dependence | `lag1_autocorr` — circular lag-1 autocorrelation of each party bit (0 if constant), basin-mass-weighted. Independent of \(T\). |
| (c) | Predicted gap | `pred_gap_cycle` again: the exhaustive on-cycle average above. No Monte Carlo. |
| (d) | Flip rate (frequency control) | `hamming_party_rate` — mean per-step party-bit Hamming distance divided by the number of party bits. Independent of \(T\). |
| (e) | Coarse oscillation (prior control) | `party_osc_frac` — fraction of (party bit × cycle) cells that are non-constant. Same definition as `ergodic_gap_decomposition`. |
| (f) | Amplitude control | `mean_cycle_var` — mean Bernoulli variance \(p(1-p)\) of party bits on cycles, as in `summarize_oscillation`. |

The canonical flip-mask signature (lexicographically minimal rotation of
the per-step party-bit change mask) is written per cycle for audit. It
is not a regressor.

`exact_basin_gap` is the closed-form mean \(\|\bar A_T - \mathrm{mean}_{\mathrm{basin}} \bar A_T\|\). It is the instrument identity in H5, not a covariate.

---

## H0 — the gap–triadic association is not a small-panel fluke

On the full 42-form panel, basin `gap_mean` at \(T=64\) versus triadic:

1. Bootstrap 95% CI for AUC has lower bound \(> 0.5\), **and**
2. Label-permutation two-sided p \(< 0.05\).

Null: the CI covers 0.5 **or** the permutation p is at least 0.05.

Continuity report, not a pass gate: the same CI and permutation p for
AUC(`pred_gap_cycle`).

## H1 — phase-remainder identity

Pass if **all** of the following hold on the full panel:

1. Panel-mean OLS slope of \(\log(\mathrm{gap}+10^{-12})\) on \(\log T\)
   lies in **[−1.25, −0.75]**.
2. Panel-mean CV of `gap·T`, over forms with positive mean `gap·T`, is
   **≤ 0.02** (vacuous pass if every form has mean `gap·T` = 0).
3. For every form, \(|\texttt{pred\_gap\_cycle} - \texttt{gap\_mean}| \le 10^{-3}\).
4. Spearman \(\rho(\texttt{pred\_gap\_cycle}, \texttt{gap\_mean}) \ge 0.90\).
   If both series have sample variance 0, this clause passes whenever
   clause 3 passes.

Null: any clause fails. A failure here means the on-cycle phase remainder
does not reproduce the empirical basin gap (transients or the basin
reference can still carry the number).

## H2 — the cycle-only prediction tracks triadic status as the empirical gap does

Pass if **all** of:

1. \(|\mathrm{AUC}(\texttt{pred\_gap\_cycle}) - \mathrm{AUC}(\texttt{gap\_mean})| \le 0.05\).
2. \(|\rho(\texttt{pred\_gap\_cycle}, \Phi) - \rho(\texttt{gap\_mean}, \Phi)| \le 0.10\).
3. The two Spearman correlations with \(\Phi\) have the same strict sign,
   or both have absolute value \(< 0.05\).

Null: the predicted remainder does not track \(\Phi\) / triadic status
within those tolerances.

## H3 — residualizing the empirical gap on the predicted remainder kills the association

`pred_gap_cycle` absorbs `gap_mean` under the absorption rule above
(shrink or identity).

Null: the partial association survives (ratio \(> 0.50\), or the partial
Spearman does not drop) and the identity clause does not fire.

## H4 — sequence features and controls

Each row uses the absorption rule. Identity clause applies only to H4i.
Pass means that covariate absorbs. The null for each row is that it does
not.

| id | covariate | role |
|---|---|---|
| H4a | `order_index` | pure ordering at \(T=64\) |
| H4b | `order_excess` | ordering in gap units |
| H4c | `cofilip_sync` | co-flip synchrony |
| H4d | `phase_lag` | folded phase lag |
| H4e | `lag1_autocorr` | lag-1 dependence |
| H4f | `hamming_party_rate` | flip-rate control |
| H4g | `party_osc_frac` | coarse-oscillation control (prior null) |
| H4h | `mean_cycle_var` | amplitude control |
| H4i | `remainder_allstarts` | all-start remainder vs cycle mean |

Pure-ordering set for the verdict: H4a–H4e.
Amplitude / frequency set: H4f–H4h.
Remainder set: `pred_gap_cycle` (H3) and H4i.

## H5 — closed form matches the instrument and the committed CSV

For every form on the evaluated panel, at \(T=64\), noise 0, pooled
parties:

1. Max over starts and party bits of
   \(|\texttt{finite\_T\_time\_average} - \texttt{trajectory\_time\_average}| \le 10^{-8}\).
2. \(|\texttt{exact\_basin\_gap} - \texttt{run\_eoa\_parties gap\_mean}| \le 10^{-6}\).
3. \(|\texttt{recomputed gap\_mean} - \texttt{committed gap\_mean}| \le 10^{-6}\).

Null: any form exceeds a tolerance. Then H0–H4 are `NOT_TESTABLE` and the
verdict is `ORDERING_NOT_TESTABLE` (the script exits non-zero).

**Primary verdict word** (full panel, H5 passed). The passing set is the
set of covariates that pass the absorption rule and are not
identity-excluded. A winner exists only when that set is non-empty.

- H0 fails → `ORDERING_ASSOC_FLUKE`
- H0 holds and the ranking winner is in the pure-ordering set →
  `ORDERING_DRIVES_GAP`
- H0 holds and the winner is `pred_gap_cycle` → `CYCLE_REMAINDER_ABSORBS`
- H0 holds and the winner is `remainder_allstarts` →
  `ALLSTART_REMAINDER_ABSORBS`
- H0 holds and the winner is in the amplitude / frequency set →
  `AMPLITUDE_NOT_ORDER`
- H0 holds, the passing set is empty, and both H1 and H3 pass →
  `REMAINDER_NOT_ORDER`
- H0 holds and the passing set is empty → `ORDERING_NULL`
- otherwise → `ORDERING_INCONCLUSIVE`

Under `--ci`, H0–H4 are `NOT_TESTABLE`. If H5 passes, the verdict word is
`ORDERING_INCONCLUSIVE`.

**Scope.** In-silico Boolean forms only. A cycle statistic that tracks a
residual gap is evidence about these models. It does not demote
\(\Phi\): exact \(\Phi_{\mathrm{MIP}}\) remains the literacy / algorithmacy
cut, and irreducibility is not established as necessary for any real
organization. No panel numbers until `analyze_ordering.py` runs after
this commit.
