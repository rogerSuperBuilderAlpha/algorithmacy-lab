# O13 follow-up — pre-registration (standing states, clock party, rule estimator)

Committed before any follow-up computation. The first run (`../RESULTS.md`) failed the v9 instrument check
(39% blind recovery) and read every repository as single-node/dyadic on event-pulse bits. This follow-up
fixes the encoding and the estimator, as that file proposed. The data is the same: GH Archive,
2024-04-01..2024-06-29, the same five repositories. The filtered events are re-extracted once to add PR
numbers, which standing states need; no new window or repository is added. Nothing below has been computed.

## Encoding (1-hour clock, lag 1)
Tracked units are PRs opened inside the window. PRs opened before the window are unseen, so the first
7 days are dropped as burn-in.
- **W (worker backlog)**: 1 when the count of open PRs awaiting approval (opened, not yet approved, not
  closed) exceeds its trailing 168-hour median, else 0.
- **C (approver standing commitment)**: 1 when the count of approved-not-merged open PRs exceeds its
  trailing 168-hour median, else 0. A PR is "approved" from its first non-bot approving review or
  `/lgtm`, `/approve`, `@bors r+` comment.
- **M (merger acts)**: 1 when ≥1 PR is merged in the hour.
- **K (clock party)**: 1 when the hour-of-week is among the repository's busiest 50% of hours-of-week for
  merge+approval events. This deseasonalises: time-of-day and weekday drivers enter as a node instead of
  inflating self-persistence. Sensitivity: the same analysis without K.
- Marginals must lie in [0.05, 0.95]. If not, the threshold changes from the median to the 60th/40th
  percentile before Φ is computed, and that change is reported.

## Estimators
1. **Rule estimator (primary).**
   - For each node, choose its parent set among all subsets of {W, M, C, K} by BIC, using a
     Bernoulli-per-parent-configuration likelihood.
   - Estimate the probabilities on that set (Laplace +1/+2), giving the implied 4-node state-by-node TPM.
   - Also compute a denoised Boolean rule (each probability rounded at 0.5), the lab's deterministic form.
   - Report Φ on both. The **verdict uses the probabilistic BIC TPM**.
2. **Bayesian table (secondary)**: full 16-row Beta(1,1) table, 200 posterior draws.
3. **Uncertainty**:
   - Moving-block bootstrap of the series (block = 24 h, 200 replicates), re-running BIC selection each time.
   - Report the median Φ, the 90% interval, the core frequencies, and P(multi-node core ⊇ {M, C}).
4. **Null**: 100 circular-shift surrogates (each node shifted ≥24 h independently; K is kept fixed),
   pushed through the same rule estimator.
5. **Two-step lag check**: per node, compare BIC of the best order-1 parent set against the best set drawn
   from lags 1 and 2 (parents at t-1 and t-2).

## Instrument check (before any real data)
- Simulate 3-node logs (T = 2,160, ε = 0.05) from two models:
  - the v11 Prow projection (W'=M, M'=C, C'=W);
  - the v9 human-merge gate (W'=S, S'=W∧C, C'=S, with S in the M slot).
- Add an independent clock node with period 24 and a 50% duty cycle, so the 4-node pipeline is identical.
- Run the rule estimator blind, 100 replicates each.
- **Pass = the recovered major complex equals the true core (excluding K) in ≥80% of replicates for BOTH
  v11 and v9.**
- Controls: a decoupled TPM gives no multi-node complex; the coupled cycle gives Φ>0 with the full core.
- If either check fails, real-data results are reported as **exploratory only** and no confirmatory
  verdict is read.

## Hypotheses (each with its null)
- **H1 coverage**: ≥12 of 16 joint states are visited ≥20 times in every repository.
  Null: fewer → that repository gives no verdict.
- **H2 structure (bot-merged: kubernetes, rust)**: the bootstrap gives P(multi-node core ⊇ {M, C}) ≥ 0.8,
  and the observed Φ exceeds the 95th surrogate percentile.
  Null: P ≤ 0.2 (dyadic) or Φ within the null.
- **H3 approval→merge edge**: C is in the BIC parent set of M in ≥80% of bootstrap replicates, in all
  five repositories. Null: <80% in any.
- **H4 bot vs human contrast**: P(multi-node core ⊇ {M, C}) is higher in the bot-merged repositories than
  in the human-merged ones by ≥0.3 (mean over repositories). Null: the difference is <0.3.
- **H5 order adequacy**: for each repository, order-2 BIC is not lower than order-1 for at least 2 of
  W, M, C. Null: order 2 is preferred for 2 or more, so the lag-1 TPM is misspecified and Φ is read with
  that caveat.

## Decision rules
- Per repository, the verdict is **triadic** if H2's conditions hold, **dyadic** if P ≤ 0.2, and
  **undetermined** otherwise. A core consisting only of K, or K plus one party, is not multi-party.
- If the instrument check fails, every verdict is labelled exploratory.
- If H1 fails, that repository gives no verdict.
- Results are reported as they fall. No re-encoding happens after results are seen, except via a new
  pre-registration.
