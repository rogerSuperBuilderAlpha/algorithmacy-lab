# O13 follow-up: results

Pre-registration: `HYPOTHESES.md` (commit 87d5217e, not edited). Code and logs are in `run/`, and the full output is in `results.json`.
Data: GH Archive 2024-04-01..2024-06-29 (2,160 hourly files), re-extracted with PR numbers, and the same five repositories. There are 1-hour bins, lag 1, and the first 168 h are dropped as burn-in (T = 1,992).

## Instrument check (run before any real data): PASS
- v11 Prow cycle: the recovered core equals the true core {W,M,C} in **100/100** replicates.
- v9 human-merge gate: **82/100** replicates (others: CM 9, MW 8, K 1). The threshold is ≥80%, so it passes, but the margin is small.
- Controls: the decoupled TPM gives a single-node complex (C), and the coupled cycle gives Φ=2.0 with core CMW. Both pass.
- So the verdicts below are **confirmatory**, not exploratory.

## Per-repository table
Marginals are [W, M, C, K]. "Rule Φ" is the probabilistic BIC TPM, which the verdict uses. "Denoised core" is the Boolean-rounded rule. The bootstrap has 200 moving-block replicates (24 h blocks). The null uses 100 circular-shift surrogates. "Table" is the Bayesian Beta(1,1) 16-row table, with 200 draws.

| repo | bot-merge share | marginals | states ≥20 (of 16) | rule Φ (core) | denoised core | boot Φ median [90%] | boot cores | P(core ⊇ {M,C}) | null 95th / Φ exceeds? | P(C ∈ pa(M)) | table Φ median, P(⊇MC) | lag check (H5) | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kubernetes/kubernetes | 1.0 | [0.916, 0.228, 0.78, 0.512] | 12 | 0.923 (C) | K | 0.949 [0.920, 0.974] | {'C': 138, 'W': 62} | 0.00 | 0.926 / no | 0.175 | 0.963, P=0.00 | misspecified | **dyadic** |
| rust-lang/rust | 1.0 | [0.87, 0.341, 0.83, 0.518] | 12 | 0.837 (W) | K | 0.859 [0.810, 0.914] | {'W': 130, 'C': 70} | 0.00 | 0.837 / no | 0.055 | 0.905, P=0.00 | ok | **dyadic** |
| django/django | 0.0 | [0.716, 0.061, 0.449, 0.676] | 12 | 0.923 (C) | K | 0.927 [0.907, 0.963] | {'C': 152, 'W': 48} | 0.00 | 0.929 / no | 0.245 | 0.875, P=0.00 | misspecified | **dyadic** |
| facebook/react | 0.0 | [0.692, 0.128, 0.585, 0.512] | 12 | 0.950 (C) | K | 0.957 [0.940, 0.978] | {'C': 133, 'W': 67} | 0.00 | 0.954 / no | 0.055 | 0.935, P=0.00 | misspecified | **dyadic** |
| microsoft/vscode | 0.0 | [0.861, 0.4, 0.92, 0.524] | 11 | 0.838 (C) | K | 0.922 [0.828, 0.969] | {'W': 167, 'C': 33} | 0.00 | 0.880 / no | 0.010 | 0.935, P=0.00 | misspecified | **no verdict (H1 failed)** |
Threshold changes required by the pre-registration: for vscode, C at the median had a marginal of 0.954 (>0.95), so C uses the trailing 60th percentile (resulting marginal 0.92). All other nodes use the median. All final marginals lie in [0.05, 0.95].

BIC parent sets (full series):
- kubernetes: W←W, M←K, C←C, K←{C,K}
- rust: W←W, M←M, C←{M,C}, K←K
- django: W←W, M←K, C←C, K←K
- react: W←W, M←{M,K}, C←C, K←K
- vscode: W←W, M←{M,K}, C←C, K←{M,K}

Sensitivity without K: the major complex is the same single node in every repository (Φ unchanged).

## Hypotheses vs decision rules
- **H1 coverage (≥12/16 states visited ≥20 times in every repository): NOT supported overall.** Kubernetes, rust, django and react have exactly 12. Vscode has 11, so vscode gives no verdict.
- **H2 structure (kubernetes, rust): NOT supported; null side holds.** P(multi-node core ⊇ {M,C}) is 0.00 in both (≤0.2 means dyadic), and the observed Φ does not exceed the 95th surrogate percentile in either.
- **H3 approval→merge edge (C ∈ pa(M) in ≥80% of replicates, all repositories): NOT supported.** The rates are 0.175 / 0.055 / 0.245 / 0.055 / 0.010.
- **H4 bot vs human contrast (difference ≥0.3): NOT supported.** The difference is 0.00 − 0.00 = 0.00.
- **H5 order adequacy: holds only for rust.** For kubernetes, django, react and vscode, order 2 is preferred for 2 of W, M, C (mostly W and C, which take a t−2 self-term; for kubernetes it is M and C). By the pre-registered rule, their lag-1 TPMs are misspecified, and Φ is read with that caveat.

## Verdicts (confirmatory, since the instrument passed)
- kubernetes: **dyadic**
- rust: **dyadic**
- django: **dyadic**
- react: **dyadic**
- vscode: **no verdict** (H1 failed)

The standing-state encoding with a clock party does not find the triadic arrangement in either bot-merged repository. In every repository, each party's state is driven mainly by its own past. Merges follow the clock (K) or their own past, not the approver's standing commitment. The major complex is always a single self-persistent node (C or W). The bootstrap, the Bayesian table and the surrogate null all agree.

## Caveats
- Single-node complexes with Φ≈0.84–0.95 come from self-loops (persistent backlog states). The surrogate null keeps self-persistence, so the Φ value means nothing beyond "one sticky node". When rust's observed Φ equals its null 95th percentile, that is a tie, not an exceedance.
- The denoised Boolean rule's core is K (the deterministic clock self-loop, Φ=1) everywhere. It is reported as required but is not the verdict input.
- The v9 instrument passed at 82%, close to the 80% threshold, so recovery of a gate-type triad is only modestly reliable at T≈2,000.
- For 4 of 5 repositories, the lag-1 model is misspecified (H5). Slower (multi-hour) dynamics in W and C are not captured.
- PRs opened before the window are unseen, and the 7-day burn-in only partly fixes this. Approval detection depends on reviews and commands that GH Archive records. Bot merges counted via the actor login give a share of 1.0 for kubernetes and rust and 0.0 for the others.
- Data integrity: the original fetch script had no `pipefail`, so 30 hours had been marked done with empty or partial output. They were re-fetched (`run/refetch_small.log`). For four hours (2024-06-19 21h and 22h, 2024-06-20 0h and 3h), the source gzip files on data.gharchive.org are truncated, so only the readable prefix was kept. Larger hours were not individually re-verified.
- vscode needed the pre-registered 60th-percentile fallback for C.
