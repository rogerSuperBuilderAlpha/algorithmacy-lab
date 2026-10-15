# Q221 — Final exploratory technical report (2026-10-15)

**This report is exploratory and retrospective.** It is not a preregistered confirmatory study, an externally reproduced PyPhi result, a universal IIT theorem, or an assertion of novelty priority. It reflects repository records and independent exact-rational checks as identified below.

## 1. Executive conclusion

- **Verified mathematical result:** For the lead pair P=aff(9,6,10), Q=aff(9,15,10), the declared stationary categorical **auto- and cross-channel population match profiles** are exactly equal at every integer lag. An independent rational implementation checks the first sixteen lags and Cayley–Hamilton extends the result to all lags. The models differ and are not isomorphic under the stated 48-element node/value transformation group.
- **Reported pinned-PyPhi computational result:** In the lab's pinned historical IIT-4.0 implementation, the two models share the same major complex {X,H} and Phi=2 but have different **q161 leave-one-rule-out maximizing sets**: {X,H} vs {H}. The repository records a separate direct PyPhi implementation and clamp-to-0/1 checks.
- **Exact-set information limitation:** No decoder given only the identical population profile can recover both **complete target sets** exactly.
- **Not an impossibility of choosing a correct node:** H belongs to both target sets; selecting H is correct on both under q220 single-node tie-aware scoring. A hypothetical balanced **exact-set** prediction task has maximum accuracy 1/2, while the corresponding **correct-node** task admits accuracy 1.
- **Constructive sufficiency under a stronger observation regime:** Full-state one-step conditional per-node update probabilities identify every deterministic rule bit when update flips satisfy epsilon<1/2; the independent rational certificate reconstructs both rule tables exactly. This is sufficient, not proved minimal.
- **Empirical exploratory result:** Simple recurrence-summary classifiers were near chance on held-out trajectories for three survivor classes, while full-transition-based classifiers attained 1.000 recorded accuracy. This is not out-of-form generalization.
- **Separate temporal-null pilot:** Naive shuffled Pearson-correlation surrogates exhibit inflated false positives for persistent binary series, a known issue; this pilot does not validate or refute the q220 recurrence null.

## 2. Exact claim tested

Model: synchronous 3-node Boolean rules, independently flipped after each update at epsilon=2/25; state s=X+2Y+4H. Statistic: all nine ordered stationary categorical pair-match rates r_ij(k)=Pr(S_t^i=S_{t+k}^j), at every integer lag. Target: q161-defined set of nodes whose constant-rule clamping produces the maximal positive drop in major-complex Phi under the pinned historical formalism. Eligibility: major complex at least two nodes, nonempty proper bottleneck set, margin threshold and non-isomorphism filter. Full observed trajectory equivalence is **not claimed**.

## 3. Mathematical results

P update rules: X'=NOT H, Y'=X XOR Y, H'=X XOR H. Q rules: X'=NOT H, Y'=NOT(X XOR Y XOR H), H'=X XOR H.

The independent standard-library Fraction script reconstructs exact stochastic 8x8 kernels, proves uniform stationarity by column sums, checks 144 exact recurrence components at lags 0–15, excludes every one of 48 relabeling transformations, and reconstructs all 24 deterministic update-rule bits in **each** system from one-step conditional means. The proof uses Cayley–Hamilton: the difference of scalar profiles of two 8-state kernels obeys a monic order-16 recurrence; sixteen exact zeros force equality for every nonnegative lag. Stationarity gives negative-lag equality. See independent_audit/EXACT_ALL_LAGS_PROOF.md and exact_all_lags_certificate.py.

The conditional probability identity is Pr(S_next^j=1|S=s)=epsilon+(1−2epsilon) f_j(s); thresholding above 1/2 recovers f_j(s). With epsilon=2/25, every conditional mean is exactly 2/25 or 23/25.

The exact-set loss consequence is **not** an impossibility of a correct single-node selection: H is common to the two reported maximizing sets.

## 4. PyPhi and q220 reproduction

The pinned receipt in identifiability/results/rep_verify.txt reports historical PyPhi feature/iit-4.0 @ b78d0e34, IIT version 4.0 with GENERALIZED_INTRINSIC_DIFFERENCE, identical major complex {X,H} and Phi=2, but different leave-one-out drops [2,0,2] vs [1,0,2]. The q161 implementation and an independently written direct PyPhi loop reportedly agree, including both clamp values. This work independently checked the recurrence mathematics; **it did not run an external second PyPhi installation**.

The q220 pipeline receipt in identifiability/results/adjudicate.txt uses its actual trajectory, timestamp coupling, prominence, centrality, and tie-aware score. Its lead-pair scores are close to respective set-size chance. This does not establish population-wide q220 failure. Newer PyPhi 2.0 defaults (IIT_4_0_2026) can differ materially from the pinned 2023-era formalism. See literature/FORMALISM_VERSION_NOTE.md.

## 5. Temporal-null results

The separate exploratory Pearson-correlation pilot reports independent binary-series rejection rates (n=250 pairs per persistence, B=199 surrogates, nominal alpha=0.05):

| Stay probability | Independent time shuffle | Circular shift |
|---|---:|---:|
| 0.50 | 14/250 (5.6%) | 12/250 (4.8%) |
| 0.90 | 85/250 (34.0%) | 14/250 (5.6%) |
| 0.98 | 168/250 (67.2%) | 5/250 (2.0%) |

A constant-series convention assigns undefined Pearson correlations zero; four degenerate pairs occurred at 0.98. This limitation matters. Circular shifts are not generally valid absent suitable null, stationarity, and shift-invariance assumptions. These results **do not** quantify Type-I error for q220's CRQA bottleneck decoder.

## 6. Baseline and generalization results

The deterministic search sampled 8,192 forms and found 7,488 candidate pairs satisfying the initial target/profile requirements. Retrospective stricter screening retained 144 pair records in **three** 48-group-unique classes. This is not 144 independent discoveries.

Recorded held-out trajectory classification (400 test trajectories per pair) gave:

| Survivor | Marginals | Self profiles | Cross profiles | 8x8 transition counts | Fitted transition likelihood |
|---|---:|---:|---:|---:|---:|
| 1 | .4625 | .5250 | .4650 | 1.000 | 1.000 |
| 2 | .5025 | .4275 | .4400 | 1.000 | 1.000 |
| 3 | .5200 | .4550 | .4975 | 1.000 | 1.000 |

Training/test seeds were disjoint, but the systems were selected post hoc. Uncertainty across **independent new network forms** was not estimated. Near-chance values are not proof of equal finite-sample feature distributions.

## 7. Literature novelty matrix

| Prior work | Established topic | Q221 limitation or possible increment |
|---|---|---|
| Theiler et al. (1992); Schreiber & Schmitz (2000) | Surrogate time-series testing | Shuffle calibration is established, not novel |
| Yuan & Shou (2022, 2024) | Dependence-induced false positives and shift-based testing | Circular shifts not a new universal fix |
| Marwan et al. (2007, 2011); Wallot & Leonardi (2018) | Recurrence analysis and pitfalls | One categorical match summary is not the whole CRQA field |
| Gilpin (2025) | Shared-driver reconstruction using recurrence | A different representation and inference target |
| Albantakis et al. (2023); Mayner et al. (2018); PyPhi docs | IIT theory and implementation | q161 bottleneck is a **lab-specific derived target** under a pinned formalism |
| Prior observational integrated-information proxy work | Differences between empirical dependence and interventional targets | Broad pairwise insufficiency not original |
| Q221 computational construction | Specified Boolean family, recurrence observable, pinned q161 target | Concrete independently checked **representation example**; exhaustive novelty priority unresolved |

Sources and verification levels appear in literature/LITERATURE_REGISTER_DRAFT.md, IDENTIFIABILITY_CLOSEST_PRIOR_ART.md and FORMALISM_VERSION_NOTE.md.

## 8. Gate status with evidence links

| Gate | Status for exploratory scope | Evidence / limitation |
|---|---|---|
| A — exact candidate and recurrence | PASS | Exact Fraction script + all-lag proof + non-isomorphism test |
| B — pinned IIT target | PASS in the lab's reported pinned run; external second implementation NOT RUN | identifiability/results/rep_verify.txt |
| C — actual q220 pipeline | PASS in recorded lab run | identifiability/results/adjudicate.txt |
| D — adversarial evaluation | PASS on selected held-out trajectories; independent-form generalization NOT RUN | baselines_survivors.json |
| E — null calibration | PASS for exploratory Pearson pilot; q220-specific calibration NOT RUN | independent_audit/REPRODUCTION_STATUS.md |
| F — literature novelty | PARTIAL | Targeted source review; exhaustive certification not performed |
| G — separation of evidence | PASS | paper.md, FINDINGS.md, hypotheses.md, methods.md |
| H — tests, CI, repository integrity | PASS on an earlier post-certificate head with 7/7 checks; final head must be rechecked | ci/reproduce.json, workflow receipts, scope diff |

## 9. Files changed and tests executed

The project files are confined to Q221 plus generated README.md/MAP.md and the explicit q221 entry added to ci/reproduce.json. Independent local mathematical regression: five tests passed after adding rule-recovery assertions. GitHub's changed-study reproducibility workflow passed 7/7 on commit ba966a04, including the newly registered 0.1s Q221 exact-certificate command. **The latest head may be newer and requires another CI check.** No q161/q220 study outputs were rewritten.

The canonical lead candidate and evidence Git blob identifiers appear in LEAD_CANDIDATE_MANIFEST.json. The original degenerate XOR pair and the value-relabeling-isomorphic pair were explicitly rejected.

## 10. Remaining blockers

- Full prospective claim-specific novelty and independent-form generalization are **outside the present exploratory study** and cannot be retroactively established.
- The pinned IIT result has not been independently rerun under current PyPhi 2.0/2026; version robustness is **not claimed**.
- The upstream draft PR body remains stale; this connected GitHub integration returned HTTP 403 to both PR-update and issue-update actions. See PR_DESCRIPTION_READY.md for replacement prose.
- Maintainer scientific review and an explicit decision about the desired contribution category remain external requirements.
- The **final commit** requires successful CI, even though prior-head registered checks were green.

## 11. Recommended next scientific experiment

A **separate prospective study**, not a retroactive Q221 stage: draw eligible Boolean network forms independently of the exploratory search, freeze selection criteria and the q161 target formalism, preregister separate exact-set and correct-node prediction losses, compare pairwise recurrence summaries with state-conditioned one-step means and strong baselines, and evaluate on held-out **forms**. Fix the null-generating mechanism and FPR tolerance in a separate calibration arm. Choose sample size and computational budget from a pilot before exposing confirmatory outcomes. Report negative and inconclusive results without changing margins.

## 12. Draft PR review and merge recommendation

**Scientific review recommendation:** YES for a narrowly scoped exploratory computational methods submission; NO for describing it as a new IIT theorem, general observational non-identifiability, q220 failure, or a preregistered calibration result. **Merge recommendation:** Keep draft until the current-head CI and maintainer scientific review are complete. No merge authorization or maintainer approval is implied by this report.
