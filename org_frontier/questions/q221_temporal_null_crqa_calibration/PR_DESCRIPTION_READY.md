# Suggested replacement description for draft PR #842

> **Historical fallback, superseded:** The upstream PR body was updated after this file was prepared. The text below predates the separate preregistered four-node study and C2/C4 follow-up and should **not** replace the current PR description. Read the live PR body, `FINDINGS.md`, and `confirmatory_4node/RESULTS.md` instead. Retained solely to document the earlier GitHub integration 403 and evidence chronology.


> **Historic, superseded PR description.** The live upstream PR body was subsequently updated by a separately authorized author workflow and now includes the preregistered four-node confirmatory target-A study and the q161 target-convention audit. This file is preserved only as a historical editorial artifact. Do not paste it over the current PR body.

**Draft exploratory methods study. No merge requested and no confirmatory hypothesis claim.**

Q221 asks whether stationary categorical pairwise recurrence summaries can uniquely identify a lab-defined leave-one-node-out IIT bottleneck **set** for three-node Boolean systems under 8% independent per-node flip noise.

## Evidence

- **Complete bounded search:** 8,192 forms; 7,488 initial eligible recurrence-equivalent pairs; 144 pairs after stricter constant-node, marginal, within-channel recurrence, cross-profile and 48-group symmetry filtering, representing **three symmetry-distinct classes**. These are exploratory search counts, not independent replicates.
- **Lead pair:** P=aff(9,6,10), Q=aff(9,15,10). Independent exact-rational certificate verifies all nine ordered auto/cross categorical match profiles at lags 0–15, then proves equality for **all integer lags** via Cayley–Hamilton. The systems are nonisomorphic under the 48-element node/value group.
- **Pinned IIT outcome:** Same reported major complex {X,H} and Phi=2 in both systems; different q161 leave-one-out bottleneck sets **{X,H} versus {H}** under the pinned historical PyPhi implementation. Clamp-to-0 and clamp-to-1 checks agree in the lab receipt.
- **Task-level limitation:** The common recurrence summary cannot reconstruct both **complete sets** exactly. It does **not** make single-node success impossible: choosing H is correct for both under q220 scoring.
- **Exact q220 population diagnostic:** At its original ±10 lag window, all three cross-channel peak-minus-median prominences are zero for the lead systems. With the 0.05 threshold and all-node tie, tie-aware scores equal their set-size chance levels, 2/3 (P) and 1/3 (Q). This says nothing about empirical finite-sample score distributions or broad q220 failure.
- **Constructive remedy:** In fully observed Boolean systems with independent update flips epsilon<1/2, state-conditioned one-step next-node probabilities recover every deterministic rule bit via thresholding at 1/2. This is sufficient, not proven minimal.
- **Finite-sample challenge:** Simple fixed recurrence-summary classifiers perform near chance on held-out trajectories for three representative pairs, but transition-aware baselines identify the generating systems in the recorded tests. This is **not** held-out form generalization.

## Scope and integrity

No new surrogate estimator, no difference in maximum Phi, no full-trajectory observational equivalence, no universal q220-decoder impossibility theorem, no prior-art priority claim, and **no prospective confirmatory result**. The earlier degenerate XOR example and a value-relabeling-isomorphic example are explicitly rejected. The independent Pearson-correlation null pilot is separate from q220's categorical recurrence calibration.

Read the evidence in Q221's paper.md, FINDINGS.md, PHASE0_AUDIT.md, GATES.md, LEAD_CANDIDATE_MANIFEST.json, independent_audit/EXACT_ALL_LAGS_PROOF.md and identifiability/results. An exact-rational certificate is registered in ci/reproduce.json for automated checks. The IIT target is defined relative to the **pinned historical** PyPhi IIT-4.0 version; newer formalism defaults may differ.

q161 and q220 historical files are unchanged. The PR modifies only Q221, generated index rows, and one justified reproducibility-manifest entry.

**Please review this as an exploratory computational methods contribution; keep draft until maintainer scientific review.**

---

**Administrative note:** The connected GitHub integration returned HTTP 403 when attempting to update the upstream PR body through both pull-request and issue update APIs. This file contains an accurate replacement description for an authorized maintainer or author UI edit.
