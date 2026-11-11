# O13 results — hourly-bin run (30 Oct 2026)

Run of the pre-registration in `../HYPOTHESES.md` (committed dd64c48a before any data fetch).
Code: `analyze.py`, `fetch.sh`, `extract.py`. Full numbers: `results.json`, log `run.log`.

## Data
GH Archive hourly files, 90 days 2024-04-01 to 2024-06-29 (2,160 hours; every hour present). The files
were streamed and filtered to five repositories, and no raw archive was kept. 2024 was chosen because
2025–26 hours in the archive carry far fewer events per repository. Spot checks of kubernetes/kubernetes
found 55 events in one 2024 hour against 1 in 2026 hours. The filtered events are 175,115 lines (~52 MB),
kept on the box only and not committed.
- Bot-merged: kubernetes/kubernetes (730 merges, 100% bot), rust-lang/rust (1,965 merges, 100% bot).
- Human-merged comparison: django/django, facebook/react, microsoft/vscode (0% bot merges).
- Nodes: W = PR opened/synchronize/reopened by a non-bot; M = PR merged; C = non-bot approving review or
  `/lgtm`, `/approve`, `@bors r+` comment. Each node is 1 in a bin with ≥1 event. Lag 1. Beta(1,1) prior.
  K=500 posterior draws and 200 circular-shift surrogates (≥24 h shift).

## Instrument check (run first)
- Controls pass. Decoupled → single-node complex only (Φ=1.0, core C). Coupled cycle → Φ=2.0, core WMC.
- Blind recovery from simulated logs (T=2,160, ε=0.05, 100 replicates):
  - v11 Prow projection (cycle): 100% → pass.
  - **v9 human-merge (AND gate): 39% → FAIL** (rule: ≥80%).
- Under the pre-registered rule, failing the instrument check means real-data verdicts are not read as
  confirmatory. The real-data numbers below are reported as **exploratory**.

## Real data, 1-hour bins (primary)
| repo | merge | marginals W/M/C | states ≥30 | Φ median [90%] | P(multi-node core ⊇ M,C) | obs Φ (post-mean) | null 95th | rule label |
|---|---|---|---|---|---|---|---|---|
| kubernetes | bot | .34/.22/.28 | 8/8 | 0.167 [0.128, 0.211] | 0.000 | 0.152 (C) | 0.301 | dyadic |
| rust | bot | .63/.35/.56 | 8/8 | 0.501 [0.457, 0.557] | 0.000 | 0.497 (M) | 0.497 | dyadic |
| django | human | .11/.06/.08 | 6/8 | 0.245 [0.121, 0.483] | 0.000 | 0.224 (C) | 0.586 | dyadic |
| react | human | .21/.13/.13 | 8/8 | 0.175 [0.114, 0.252] | 0.002 | 0.162 (W) | 0.526 | dyadic |
| vscode | human | .48/.41/.44 | 7/8 | 0.167 [0.131, 0.225] | 0.086 | 0.157 (W) | 0.380 | dyadic |

Core frequencies (kubernetes): C 302, W 196, M 2 of 500. Rust: M 500/500. Vscode: W 374, M 56, WMC 43, MW 26.
Every repo's Φ is that of a **single-node self-loop complex** and sits at or below the surrogate null.
Sensitivity to the Beta(0.5) prior leaves the medians essentially unchanged (kubernetes 0.170).
Robustness: 15-min bins give the same reading (all single-node cores, Φ below the null). The exception is
django, which fails H1 at 15 min. 4-hour bins fail H1 for every repo.

## Hypotheses vs decision rules
- **H1 coverage: supported.** All five repos reach ≥6/8 states with ≥30 visits at 1 h (kubernetes and
  rust 8/8). Marginals are within [0.05, 0.95].
- **H2 structure: not supported** (null holds). P(multi-node core ⊇ M,C) = 0.000 for both bot-merged
  repos, against a required ≥0.8. The estimated arrangement does not recover the elicited v11 triadic core
  (CMW / RBC), so it disagrees with the elicited model.
- **H3 conduit: kubernetes −** collapsing M changes median Φ by +8.6% (<10%, formally "supported").
  Rust changes by −84%, so H3 fails there. Because the full-system core is a single node, H3 does not
  test the conduit claim it was written for.
- **H4 bot vs human contrast: not supported.** Every repo is single-node and dyadic-labelled, and the
  Φ>0 rate is identical. The only composition difference is that rust's core is M; that is not systematic
  across bot repos (kubernetes's core is C/W).
- **H5 CRQA C→M (O09): kubernetes supported.** The peak lag is +1 h (approval leads merge) with
  prominence 0.088, above the 0.05 floor. The estimated C→M effect is also positive in the posterior-mean
  TPM (see `results.json`). Rust has its peak at −5 h with low prominence, so H5 fails there.
- **Verdict: inconclusive overall.** The instrument check failed on v9, so no confirmatory verdict can be
  read. The exploratory reading on every repo is dyadic: there is no multi-party integration above
  surrogate level. Behavioural coupling C→M is visible in kubernetes, but it does not produce Φ>0 for a
  multi-node core.

## Caveats
- **Estimator weakness.** Blind recovery fails for AND-gate (v9) structures at this series length and
  noise. The posterior-mean TPM with ε-noise smooths a conjunctive rule toward independence. The
  pre-registered estimator is therefore underpowered for gate structures, which is a finding in itself.
- **Encoding issues.**
  - Activity-presence bits are not the elicited "state" bits. A PR approved and later merged spans many
    hours, and the elicited model's bits are standing states (approved / merged), not event pulses.
  - Hourly lag-1 also cuts across Prow's batching.
- **Unobserved parties and drivers.** Unobserved CI and Prow labels are missing. Time-of-day common
  drivers were not conditioned out (no clock node), and they push every node toward self-persistence.
- **Pre-registered steps not run.** The BIC structural alternative, the order-2 check, and the
  block-bootstrap variant were not run. The posterior-draw route was used, which the plan allows.

## Suggested next step (not pre-registered here; needs a new pre-registration)
- Encode standing states rather than event pulses: open-PR-awaiting-approval, approved-not-merged,
  merged-in-last-h.
- Add a clock node.
- Use a rule-based (BIC) estimator, which should recover AND gates better.
- Re-run the instrument check before any real data.
