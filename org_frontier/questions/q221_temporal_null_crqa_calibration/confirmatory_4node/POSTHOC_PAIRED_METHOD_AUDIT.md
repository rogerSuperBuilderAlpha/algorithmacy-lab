# Independent follow-up receipts and paired-comparator audit (POST-HOC)

**Date:** 2026-10-15. **Status:** independent read-only record audit, completed after outcomes were available. It is not a new preregistered experiment, a superiority test, or a replacement for the frozen primary decision rules.

## Provenance and integrity

Sources: `results/followup_pairs.json`, all twelve `results/followup_part_*.json` files, `results/followup.json`, and the original `results/screen4.json`.

Independent checks established:

- 600 unique follow-up **orbit pairs**, with indices 0–599, and no overlap with the 40 parent-study orbit pairs.
- All 600 retained exact recurrence equality, distinct transition matrix, and 384-transformation non-isomorphism flags.
- Every combined row has a matching original selected pair and identical raw correct counts and exact-feature differences in the committed chunk files.
- 240,000 held-out classification decisions (600 orbit pairs × 400 trajectories), with correct-count sums: R = 120,184, joint recurrence = 182,514, SHREC = 169,669, transition likelihood = 240,000. The manipulation checks pass.
- Reapplying the frozen parent per-pair Wilson cutoff and the follow-up Bonferroni classifier-level cutoff reproduces 347/600 joint-recurrence and 363/600 SHREC separations and the published primary verdicts.
- Recomputing the exact-versus-finite secondary tables agrees with the committed JSON.

**Sampling-unit nuance:** orbit **pairs** are unique, but orbits themselves are reused across different pairs. The 600 pairs contain 782 distinct orbit IDs among 1,200 appearances. This is not a test on 1,200 independent systems. The primary estimand and sampling protocol explicitly use orbit pairs, so this observation does not change the preregistered rule; it limits claims about novel independent forms or model-level generalization.

## Paired comparison of joint recurrence and SHREC

Each method is evaluated on the *same* 600 orbit pairs. The paired outcomes are:

| | SHREC separates | SHREC does not separate | Total |
|---|---:|---:|---:|
| Joint recurrence separates | 231 | 116 | 347 |
| Joint recurrence does not separate | 132 | 121 | 253 |
| Total | 363 | 237 | 600 |

SHREC's separation proportion is 363/600 = 0.605 and joint recurrence's is 347/600 = 0.5783; the observed difference is **+2.67 percentage points**. Among 248 discordant pairs, SHREC wins 132 and joint recurrence wins 116. A *post-hoc*, two-sided, exact matched-pair binomial/McNemar calculation gives **p = 0.3409**. This is not evidence that SHREC outperforms joint recurrence at a conventional significance threshold. No multiplicity-adjusted or preregistered superiority claim is made.

The two **separately preregistered** findings remain valid under their specified criterion: each comparator's proportion of separated orbit pairs exceeds 0.5 by the Bonferroni-adjusted Wilson rule. That does not establish an ordering between the two.

## Unresolved scope

- No inferential claim about SHREC-versus-JR superiority.
- The primary results apply to the 1,832 held-out eligible orbit pairs and the specified 4-node affine family, 600-step trajectories, 8% noise, and these software implementations.
- Classification outcomes are conditional on one trained model per pair and a stochastic trajectory draw. Dependence across pairs sharing an orbit and the finite-population correction merit explicit consideration in any broader generalization analysis.
- No IIT or q161 bottleneck comparison is established by the 4-node results, and no new q220 classifier calibration result follows.
- These QA checks are reproducible without SHREC, PyPhi, or repeating the expensive simulation. Run `python -m org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node.audit_followup_receipts`.

**Disposition:** retain the precommitted JR and SHREC primary verdicts, separately from this post-hoc comparison; do not alter the original data, seeds, thresholds, preregistration, or verdicts.
