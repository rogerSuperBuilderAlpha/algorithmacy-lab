# Q221 — Pairwise recurrence summaries do not identify the transition law; proved for the affine class (exploratory draft, not confirmatory)

Draft PR #842. No merge requested. Gate status: [`GATES.md`](GATES.md). Detailed records:
`IDENTIFIABILITY_NOTE.md`, `identifiability/SEARCH_RECORD.md`, `independent_audit/` (Hassan's parallel work), and
`EXACT_PHI_DECISION_RULES.md` (fixed before the post-rules Φ runs).

**Defensible conclusion (Hassan, binding):**
- **Claimed:** pairwise *population* recurrence summaries may not identify the full multivariate transition law.
- **Not claimed:** finite-sample indistinguishability.
- **Not claimed:** that q220 fails.
- **Not claimed:** an IIT theorem.

## Targets A–D: which survived

| target | claim | status | evidence |
|---|---|---|---|
| **A** statistical identifiability | R(P) = R(Q) with P ≠ Q | **Survives. Proved** for invertible GF(2)-affine systems; 3 non-isomorphic classes found among 3-node systems | `THEORY.md`, `results/screen_exact.txt` |
| **B** structural target | q161 B(P) ≠ B(Q) | **Survives only under the q161 freeze convention.** Under an IIT background-condition reading, no survivor pair has two distinct eligible targets | `TARGET_AUDIT.md`, `results/target_variants.txt` |
| **C** IIT quantity | Φ or major complex differ | **Does not survive.** Same major complex {X,H}, same Φ = 2, same per-state φ | `results/rep_verify.txt` |
| **D** q220 decoder on held-out families | beats chance or baselines | **Not supported.** +0.04 [−0.05, +0.12] on `nsi` and +0.02 [−0.04, +0.08] on `aff`. A plug-in transition-law comparator scores 1.000 | `results/structural_baselines.txt` |

## Comparator study (prespecified, spec commit `311a6477`; exploratory)

- Results: `identifiability/results/comparators.{txt,json}`.
- Pairs: S1 = P/Q, S2 = aff(9,6,10)/aff(9,15,12), S3 = aff(9,6,11)/aff(9,14,10).
- Finite-sample test: 400 test trajectories per pair at T = 600, nearest-centroid classifier, decision by a
  Bonferroni-adjusted Wilson lower bound > 0.5 (15 tests).

| comparator | exact population separation | S1 accuracy | S2 accuracy | S3 accuracy |
|---|---|---|---|---|
| C1 transfer entropy (history 1) | **yes**, all 3 pairs (max diff 0.598 bits) | 1.000 | 1.000 | 1.000 |
| C2 joint recurrence, categorical, lags 1–10 | **yes**, all 3 (max diff 0.176); the (X,H) block is equal | 1.000 | 1.000 | 0.995 |
| C3 MdRQA full-vector recurrence rate, lags 1–10 | **no**: exactly equal = trace(P^k)/8 | 0.488 | 0.490 | 0.493 |
| C4 SHREC (`williamgilpin/shrec` @ `49c6d3e0`, defaults; 4 prespecified driver features) | not computable | 0.895 | 1.000 | 0.918 |
| C5 false-pair-calibrated q220 prominence | **no** (equal by the Corollary) | 0.583* | 0.483 | 0.505 |

\* For S1, C5's Bonferroni lower bound is 0.509, so it passes the prespecified rule, but only weakly. The
population means are equal, so this reflects a difference in the sampling distribution of the nonlinear
prominence statistic.

**False-pair rejection rates (p < 0.05).** For each channel pair, the fraction of test trajectories whose
coupling test rejects is 0.025–0.125 in both members. This is close to nominal.

**Reading.**
- The statistics that separate the pairs see joint multi-time structure of a channel pair or of the full
  state: TE, JRP, transition counts and SHREC's shared multi-channel embedding.
- The full-vector recurrence *rate* is a spectral invariant of the transition matrix, and it does not separate
  the pairs.
- This matches the exact law decision: the (X,Y) and (Y,H) laws differ, and the univariate and (X,H) laws
  are equal.

## The three equalities, for the lead pair P/Q

1. **The declared recurrence observable.**
   - Observable: r_ij(k) = P(x_i(t) = x_j(t+k)), for all ordered (i,j) with i = j included (auto-profiles),
     lags k = 0..40 in both directions (negative lags are the reversed pair). Marginals are included too.
   - Result: **exactly equal**, and equal at every lag by the linear-recurrence argument and Proposition 1.
   - Relation to q220: q220's implemented statistic is the *empirical* estimator of the cross part of this
     observable, followed by the nonlinear peak−median transform. q220's chain starts from the uniform law,
     which is stationary for invertible A, so the estimator's expectation equals r_ij(k) exactly. Equality of
     the expectations does **not** imply equality of the prominence distributions.
2. **The full observed process law L(X_{0:T}).**
   - **Not equal** (`results/process_law_equivalence.txt`; exact decision for all T by the
     Tzeng/Schützenberger span algorithm).
   - The univariate laws of X, Y and H are equal.
   - The bivariate laws of (X,H) are equal; those of (X,Y) and (Y,H) differ.
   - So the systems are **not** observationally indistinguishable, even from a single pair of channels.
3. **Identity under an explicit bijection.** **Not equal**: no node permutation × value relabelling maps P to Q
   (48-group check).

The evidence falls into four categories, kept strictly separate below.

## 0. Theory (proved; `THEORY.md`)

These results hold for invertible GF(2)-affine systems with i.i.d. flips, for any n.

- **Proposition 1** gives a closed form for every pairwise recurrence statistic: marginals, plus auto- and
  cross-profiles at every lag. These statistics depend on (A, c) only through the unit-vector paths of A^T,
  specifically their hitting lags, weight sums and sign parities.
- **Proposition 2.** One-step (|row| + 1)-point parity statistics identify (A, c) exactly.
- **Exact check:** all 1344 invertible three-node forms (`results/affine_theory.txt`).
- **Scope:** this is elementary Walsh–Fourier analysis. It explains *why* the survivors exist; no novelty in
  the mathematics is claimed.

## 1. Exploratory search (deterministic, population-level, exact)

| item | result | evidence |
|---|---|---|
| Original A/B pair (variants A, B, C) | All targets are ineligible for q161: empty B and a single-node core. Rejected as a bottleneck counterexample (rule 1). | `identifiability/results/phi_detail.txt`, `ab_hassan_code.txt` |
| A/B/C reconciliation | Every number traced to exact rules and the variant's own stationary law. B_xor's law is non-uniform; A and C are uniform. Cross-recurrence is 1/2 at all lags in all three. Hassan's finite-sample table is A vs C. | `identifiability/results/variants_abc.txt` |
| Bounded search (rule 3) | Completed 2823/2823 groups in 290 s of the 1800 s budget. 7488 candidate pairs, 74 unique up to perm × value flip. | `identifiability/SEARCH_RECORD.md` |
| Exact screen, all 7488 pairs | 7488 → 6816 (no constant node) → 6432 (+ equal marginals) → 180 (+ equal self-recurrence, lags 0..20) → 180 (+ exact cross-recurrence) → **144 raw / 24 node-perm-unique / 3 unique up to the 48-group, not isomorphic**. All GF(2)-affine; none in the R2 family. | `identifiability/results/screen_exact.txt` |
| Hassan's matched candidate aff(6,9,5) vs aff(11,9,5) | **Isomorphic**: swap Y and H, and flip the values of Y and H. Its B sets {H}/{Y} are the same target relabelled. Not a counterexample. | `identifiability/results/iso_check_hassan_pair.txt` |
| Lead survivor P = aff(9,6,10), Q = aff(9,15,10) (pinned PyPhi) | Major complex {X,H}, Φ = 2 in both, with identical per-state φ for every subset. q161 B: {X,H} vs {H}. Same under clamp 0 and clamp 1. **Equal ({X,H}) under the background-condition variant** (`TARGET_AUDIT.md`). Tie gap 1.0; B margin ≥ 1; both eligible. Marginals and self- and cross-recurrence exactly equal at lags 0..40, hence at every lag. Not 48-group isomorphic. | `identifiability/results/rep_verify.txt` |

The search is exploratory. Its 3 survivors are examples, not a characterisation. They have not been validated
under a locked protocol.

### Exact all-lag proof and task-level limitation

An independent Python-standard-library rational certificate reconstructs the lead pair's two stochastic transition matrices and verifies **144 exact fractions**: all nine ordered auto/cross-channel categorical match rates for lags 0–15. By the Cayley–Hamilton recurrence of two eight-state transition matrices, those sixteen initial matches imply equality of the specified population summaries at **every integer lag** under stationarity; negative lags follow by swapping ordered channels. No node permutation or per-node value flip in the 48-element symmetry group maps the pair. Evidence: independent_audit/exact_all_lags_certificate.py, test_exact_all_lags_certificate.py, and EXACT_ALL_LAGS_PROOF.md. The certificate is independent of PyPhi and does not recompute the IIT targets.

**Critical target distinction:** For the lead pair, B(P)={X,H} and B(Q)={H}. Different complete bottleneck sets cannot both be reconstructed exactly from a common population summary. **However, H belongs to both sets**: a decoder selecting node H would be correct on both under the q220 single-node membership/tie-aware score. Thus the mathematical counterexample is about **exact maximizer-set identification**, not universal failure to choose a correct bottleneck node, and not a difference in Phi or major complex. No general finite-sample q220 failure follows.

## 2. Finite-sample checks (exploratory, one form per system, seeded)

| item | result | evidence |
|---|---|---|
| q220's actual pipeline on P/Q: repo `crqa.trajectory`, then q220 `stage2.observe` `coupling` → `centrality` → `bottleneck_scores`; R = 400; seeds 43000+ | Pipeline outputs match within SE (max prominence 0.0607 / 0.0606). Tie-aware BN score 0.643 / 0.330, which equals set-size chance (0.667 / 0.333) for each system. | `identifiability/results/adjudicate.txt` |
| Hassan's `candidate_finite_sample.py` on P/Q (his own simulator, q220 `observe`), seeds 0..299 | Score 0.661 / 0.333, consistent with the row above. | `identifiability/results/pinned_env_runs/lead_pair_finite_sample.json` |
| Prespecified simple baselines on all 3 survivors (spec committed in `35313d47` before running) | Marginals, self-recurrence and cross-recurrence give 0.43 to 0.53 (near chance). **Transition counts and transition likelihood give 1.000 (Wilson 95% CI 0.99 to 1.0) on every pair.** | `identifiability/results/baselines_survivors.txt` |

**Structural prediction pilot on fresh, independently generated forms** (gate D, `results/structural_baselines.txt`;
spec committed in `ecd014dd`):
- 80 eligible forms per family, with held-out families; the unit is the form.
- The q220 rule beats chance by **+0.039 [−0.05, +0.12]** on `nsi` and **+0.017 [−0.04, +0.08]** on `aff`.
  Neither interval excludes zero.
- Node-prior, marginal and autocorrelation baselines are also near or below chance.
- A plug-in comparator (estimate the transition law, then compute the q161 target) scores 1.000 on both
  families.
- **Reading:** on this exploratory pilot, pairwise recurrence does not predict the target beyond chance, while
  the full transition law does.
- **Caveat:** this pilot is the *structural prediction* track. It is not confirmatory and not a test of q220's
  published corpus.

**Reading.**
- The systems are trivially separable from finite data through three-point and transition statistics. One
  example: P(Y_{t+1} = X_t⊕Y_t) is 0.92 in P and 0.5 in Q.
- The equivalence is population-level, and only for one- and two-point summaries.
- The q220 decoder scoring at chance on one designed pair is **not** evidence that q220 fails on its own corpus.
- Two of the near-chance baselines have Wilson intervals that exclude 0.5: 0.427 and 0.440. The Wilson interval
  treats the test trajectories as independent and ignores variability in the single fitted centroid. These
  excursions are read as classifier-fit noise, not signal. No tuning was done.
- Uncertainty across independently generated forms does not apply here. The 3 pairs are the complete survivor
  set of a deterministic search, not a sample of forms.

## 3. Pilot calibration (exploratory methods check)

- Hassan's null pilot is reproduced bit-identically in the pinned environment.
- **Its scope:** the zero-lag absolute **Pearson** correlation, for **independent binary Markov channels** only.
  It used 250 pairs per persistence level, 199 surrogates, and seed 2212026.
- Naive-shuffle FPR: 5.6% / 34.0% / 67.2% at persistence 0.5 / 0.9 / 0.98.
- Circular-shift FPR: 4.8% / 5.6% / 2.0%.
- **Extension (gate E, `results/null_extension.txt`; spec committed in `6ad206a3`):** a fresh seed, 250 pairs
  per cell, and four surrogate types, applied both to Pearson and to **q220's actual prominence statistic**.
  - Shuffle FPR for q220 prominence: 27.2% at p = 0.9 and 42.8% at p = 0.98.
  - Circular, block-16 and fitted-Markov surrogates for q220 prominence: 2.0% to 6.4%.
  - The block surrogate is inflated for Pearson at p = 0.98 (16.8%).
  - With n = 250 per cell, no interval fits inside the 0.025–0.075 band. Those cells are inconclusive by
    design, and **no improved-calibration claim is made.**
- **No calibration claim for the q220 decoder and no confirmatory claim.**
- Shuffle miscalibration under autocorrelation is already known (Yuan & Shou 2022). Circular shifts can also
  fail (Yuan & Shou 2024).
- Evidence: `independent_audit/null_pilot_results.json` and `REPRODUCTION_STATUS.md`.

## 4. Structural prediction and confirmatory evidence

- **None.** Track B (predicting the Φ bottleneck from recurrence on held-out forms) was not run.
- No preregistration exists.
- No confirmatory data were collected.

## What is (possibly) new

The general phenomenon is classical. Pairwise statistics miss XOR and other higher-order structure (Williams &
Beer 2010; James & Crutchfield 2017; Gilpin 2025). Dependence-aware testing is also established (Yuan & Shou
2022/2024; Theiler 1992; Politis & Romano 1994).

What may be new, and is still exploratory and unvalidated:
1. An exact construction inside the lab's own Boolean family (q220's generator) of non-isomorphic systems that
   are equal on every one- and two-point recurrence summary at every lag, and on major complex and Φ, yet have
   different q161 leave-one-out bottleneck targets.
2. The observation that the q161 target can change through a rule **outside** the major complex.

The comparison against the lab's recurrence review and against dependence-aware testing is in `literature/NOVELTY_ASSESSMENT.md`. That file also lists the open items: MdCRQA/joint recurrence, TE and CCM on the survivors, and a database search on IIT-target identifiability.

## Limitations

- Three nodes; synchronous; two families (`nsi`, GF(2)-affine).
- The q161 Φ convention is the one used throughout.
- Single search; single seeds per experiment.
- The literature review is retrospective and only partly full-text verified; a future confirmatory study would require a separately prospective review and protocol.
- The residual-Φ mechanism has been illustrated for selected pairs in `identifiability/SEARCH_RECORD.md`; it has not been characterized across all Boolean families.

## Reproduce

Use the pinned environment: Python 3.12.15, numpy 2.5.4, scipy 1.18.1, PyPhi `feature/iit-4.0` @ `b78d0e34`.
Run from the repo root.

```
M=org_frontier.questions.q221_temporal_null_crqa_calibration
python -m $M.identifiability.pair_search            # bounded search (~5 min, deterministic)
python -m $M.identifiability.verify_candidates      # 48-group check + independent recomputation
python -m $M.identifiability.screen_exact           # exact screen of all 7488 pairs
python -m $M.identifiability.iso_check_hassan_pair  # aff(6,9,5) vs aff(11,9,5) isomorphism
python -m $M.identifiability.rep_verify             # lead pair exact Φ (q161 + own clamp 0/1), profiles to lag 40
python -m $M.identifiability.adjudicate             # q220 actual pipeline on the lead pair (R=400)
python -m $M.identifiability.lead_pair_finite_sample
python -m $M.identifiability.baselines_survivors    # gate-3 baselines
python -m $M.identifiability.affine_theory          # THEORY.md exact check (1344 forms)
python -m $M.identifiability.structural_baselines   # gate D (held-out families)
python -m $M.identifiability.null_extension         # gate E
python -m $M.build_manifest                         # MANIFEST.json
python -m $M.identifiability.variants_abc
python -m pytest -q org_frontier/questions/q221_temporal_null_crqa_calibration/
```

## Future confirmatory work (not started)

Any confirmatory study needs:
- a preregistration committed and pushed before data collection;
- a fresh seed stream and form-level holdouts;
- the baselines in `BLUEPRINT_REQUIREMENTS.md` §5;
- for the identifiability claim, a symbolic or larger-family characterisation rather than examples.
