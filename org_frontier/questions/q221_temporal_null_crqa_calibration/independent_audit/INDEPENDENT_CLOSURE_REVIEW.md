# Independent closure review — 2026-10-15

**Scope:** read-only audit of currently committed q221 receipts; this note is retrospective and does not claim to have executed pinned PyPhi. The PR should remain draft until maintainer review and the readiness gates below are resolved.

## Evidence verified from committed records

- `PROGRESS.md` says the parallel run **stopped at the agreed feasibility finish line**, with phase-0 audit, full literature review, prospective null-statistic pilot specification and its results **deferred**. Do not misrepresent these as still-running tasks or as completed.
- `identifiability/results/screen_exact.json`: 7,488 candidate pairs, 180 with matched marginal/self/cross profiles before full symmetry exclusion, **144** surviving non-isomorphic pair records, collapsing to **three** 48-group classes.
- `identifiability/results/rep_verify.txt`: pinned-PyPhi representative P/Q verification, clamp-to-0 and clamp-to-1 agreement, exact auto/cross recurrence profiles to lag 40, 48-group non-isomorphism, clean process exit (rc=0). This is a substantive pinned-environment receipt **for the representative shown**, not necessarily independent verification of all three classes.
- `identifiability/results/baselines_survivors.json`: all three surviving pairs have restricted-feature classification near chance in the recorded held-out trajectories, but full transition-count and likelihood baselines achieve 100%. This refutes any claim of full-observation indistinguishability.
- Earlier original XOR A/B pair is ineligible for an IIT-bottleneck claim; preserve that rejection.
- Independent audit scripts and notes are exploratory; do not present their numbers as prospective confirmatory results.

## Adversarial findings

1. The strongest supported conclusion is **insufficiency of a restricted population categorical recurrence summary** for unique recovery of q161-defined leave-one-out bottleneck sets in selected synthetic Boolean systems. It is **not** a theorem about arbitrary finite-sample recurrence algorithms or the complete observed trajectory.
2. A matched pair can have the same maximum Φ and major complex while differing only in the **set-valued bottleneck**. Define tie-aware loss and chance adjustment clearly.
3. Clamp-to-zero and clamp-to-one sensitivity is an important intervention-convention check; where both agree in pinned receipts, report that explicitly without claiming formalism-independent causality.
4. The 144 pair records are not 144 independent experiments; three symmetry classes are the correct nonredundant summary of the filtered set.
5. Near-chance finite-sample classifier accuracy is not evidence of equality of feature distributions or proof of impossibility.
6. Literature novelty is **not established** by computational screening. Surrogate data, recurrence, and identifiability have extensive prior art.

## Scientific decision

**GO** to maintain this draft as an exploratory methods/feasibility contribution with complete search receipts, explicit negative controls, and narrow claims.

**NO-GO** for marking it confirmatory, claiming full observational equivalence, claiming a general IIT theorem, or merging on the basis of these receipts alone.

### Closure choices

- **Minimal scientific review submission:** reconcile README, FINDINGS, paper, and PR body with the completed search, the three classes, the verified P/Q representative, and the deferred pilot/literature work. Keep draft or request maintainer feedback explicitly as an exploratory methods contribution.
- **Full confirmatory study:** separate future protocol with independent-form generalization, source-verified literature novelty matrix, defined null estimand and valid surrogates, and prospectively fixed inference. Do **not** retrofit those claims into this draft.

### Verification still needed before calling this draft technically ready

- Run repository tests and reproducibility scripts at the **current final head**, recording exact commands and commit SHA.
- Check CI and the full diff for unrelated changes and documentation contradictions.
- Verify whether exact-Φ receipts cover all three classes; if not, state coverage precisely.
- Obtain source-level literature verification and maintainer scientific judgment before claims of novelty.

This note intentionally does not assert any unobserved CI success or mergeability.
