# Q221 — Maintainer review handoff (draft PR #842)

**Status:** Exploratory computational methods contribution; not preregistered, not confirmatory, no merge authorization.

## What is being contributed

A reproducible bounded search for small Boolean networks in which **restricted stationary categorical recurrence summaries** agree but the lab's **q161-defined leave-one-out bottleneck targets** differ. The strongest filtered results comprise **three symmetry-distinct classes**, not 144 independent discoveries. A pinned PyPhi IIT-4.0 representative check records the same maximum Φ and major complex for the lead pair but different leave-one-out bottleneck sets.

This is **not** a claim that the full multivariate observations are equivalent: transition-count and transition-likelihood baselines distinguish the three representative pairs with 100% accuracy in the recorded held-out trajectories. It is also not a new surrogate estimator or a prospective q220 null-calibration study.

## Critical scientific safeguards

- Original A/B XOR example **rejected** (degenerate target).
- aff(6,9,5) / aff(11,9,5) example **rejected** under node-permutation/value-flip isomorphism.
- Final survivor filtering requires no constant node, matched marginals and auto/cross profiles, and 48-group non-isomorphism.
- The q161 bottleneck is a derived perturbational target sensitive to the precise IIT/PyPhi and intervention conventions; do not generalize to all causal targets.
- Search and finite-sample evaluations are exploratory; finite-sample near-chance accuracy does not prove equality of feature distributions.
- Literature establishes the broad information-loss and dependence-calibration issues; novelty of the exact specific construction remains unverified.

## Evidence map

| Item | Source |
|---|---|
| Complete bounded search and accounting | `identifiability/SEARCH_RECORD.md`, `results/pair_search.json` |
| Stronger screen and three classes | `identifiability/results/screen_exact.json` |
| Pinned IIT representative and clamps | `identifiability/results/rep_verify.txt` |
| q220 finite-sample lead pair | `identifiability/results/adjudicate.txt` |
| Three survivor baselines | `identifiability/results/baselines_survivors.json` |
| Research narrative | `paper.md`, `FINDINGS.md`, `methods.md` |
| Targeted literature | `literature/LITERATURE_REGISTER_DRAFT.md`, `literature/IDENTIFIABILITY_CLOSEST_PRIOR_ART.md` |
| Independent adversarial audit | `independent_audit/` |

## GitHub and editorial status

- Current-head `reproduce-the-numbers` workflow passed at `d3c0a259` before this handoff file was added. **Recheck CI on the new head**.
- Root `README.md` and `MAP.md` are generated index entries; q161 and q220 source/history are not part of the PR diff.
- The upstream PR body still has stale progress text. The connected GitHub integration returned HTTP 403 on PR metadata update. The maintainer should use this handoff to replace that body; do not interpret the stale text as current status.
- No scientific novelty certification, maintainer approval, or merge has occurred.

## Review decision requested

Review this as a **bounded exploratory methods case study** with transparent negative controls. If the maintainer requires a prospective calibration study or external novelty certification, that is a distinct protocol and must not be retrofitted into these results. Keep the PR draft until the maintainer is satisfied with the scope and final CI.
