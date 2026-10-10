# Q219 — Stage 3 hypotheses (fixed before computation)

Five hypotheses on which claims-routing design makes the claim decision triadic. Parties: claimant (C),
auto-adjudication engine (E), human adjuster (A), labels in the order (C, E, A). Rules follow the
`probes/lib.py` `verdict()` convention: `rules[j](x)` returns node j's next bit from the current state
tuple x. Written before any test runs; the exact forms and decision rules are in `methods.md`.

**Shared decision rule.** A form is **triadic** iff `verdict(rules, ("C","E","A")).structure == "triadic"`
(max Φ_MIP over reachable states > PHI_EPS = 1e-9) **and** `major_complex(rules, ("C","E","A"))` returns all
three labels. A form is **dyadic** iff `structure == "dyadic"` (max Φ_MIP ≤ PHI_EPS). A form that is
triadic as a whole with fewer than three labels in the major complex counts as **partial**, which fails
any hypothesis that predicts "triadic". Instrument controls must pass first (`methods.md`).

## H1 — A pass-through pipe is triadic through closure alone

- **Claim:** The pipe, in which the engine only forwards the claim, the adjuster's decision copies what
  arrives, and the claimant reads the decision (C'=A, E'=C, A'=E), is triadic with all three in the major
  complex. No node jointly determines from two sources, yet the three copies close a directed loop, so
  every party is read by another and no cut separates a part for free. The pipe is exactly the n=3
  rotating ring `rot_ring(3)` of Q11 (`questions/q11_oscillatory_scaling/`, x_i' = x_{i−1}, with
  C, E, A = x0, x1, x2), which Q11 reports triadic at Φ_MIP = 2.0 with the full node set as its core.
  An engine that only routes the claim therefore does not make the arrangement dyadic once the decision
  returns to the claimant.
- **H0:** The pipe is dyadic (max Φ_MIP ≤ PHI_EPS), or triadic with fewer than three labels in the major
  complex. STRUCTURAL_FINDINGS 3 (0% triadic without a mediator that reads all parties, in the
  strict-mediation family) is the structurally-expected basis for this null.
- **Predicted outcome:** `pipe` triadic, core {C, E, A}, Φ_MIP = 2.0 as in Q11. H0 refuted.
- **Risk.** The prediction rests on Q11 reproducing in this environment under the claims labels. The
  test is a replication on a relabeled form, so a dyadic reading would signal an instrument or labeling
  fault before it would signal a new finding. Its substantive content is the contrast with the lab's
  dyadic relays, which leave one party unread: closure, without joint determination, binds the three.

## H2 — Threshold auto-approval is triadic only through flagged claims

- **Claim:** In the threshold design (C'=E∧¬A, E'=C, A'=E∧C), where the engine flags large or contested
  claims, small claims close by auto-approval, and the adjuster acts only on flagged claims, the form is
  triadic with all three in the major complex, and every reachable state with Φ_MIP > PHI_EPS has the flag
  set (E=1). The adjuster both co-determines the claimant-facing outcome and reads the flag, the
  COMMIT_READ condition of study #39, but only on the flagged path.
- **H0:** The form is dyadic or partial, or some state with E=0 has Φ_MIP > PHI_EPS.
- **Predicted outcome:** `gated` triadic, core {C, E, A}; every irreducible state in the `phi_profile` has
  E=1; every E=0 state has Φ_MIP = 0. H0 refuted.
- **Risk.** The state-split clause is untested in the record. STRUCTURAL_FINDINGS 5 also warns that a
  substitutable route (auto-approve **or** adjuster) can collapse a triad, and `ats_feedback_factors`
  shows that a fully wired three-node form can still factor on its read functions.

## H3 — A fraud-flag loop with override learning is triadic

- **Claim:** The bidirectional design (C'=A, E'=C∧A, A'=E∧C), where the adjuster upholds the engine's
  fraud flag only when the flag and the claim file agree, the engine's next flag learns from the
  adjuster's last call, and the claimant reads the adjuster's call, is triadic with all three in the major
  complex. Two conjunctive commits that each read the other two parties meet the conjunctive law and the
  bidirectional-participation rule (STRUCTURAL_FINDINGS 8; #76).
- **H0:** The form is dyadic or partial, or the major complex contracts to a pair such as {E, A}
  (a private engine–adjuster dyad, as the override form in #39 produced {H, S}).
- **Predicted outcome:** `loop` triadic, core {C, E, A}. H0 refuted.

## H4 — The loop's triad survives removing override learning

- **Claim:** Removing the learning edge, so the engine flags from the claim alone (C'=A, E'=C, A'=E∧C),
  leaves the form triadic with all three in the major complex. The adjuster still jointly determines from
  engine and claimant, and the claimant stays live by reading the adjuster, the same structure as the
  strict-mediation triad `ats_triad_mediator` with the engine's read moved from the adjuster to the
  claimant.
- **H0:** `loop_nolearn` is dyadic or partial.
- **Predicted outcome:** `loop_nolearn` triadic, core {C, E, A}. H0 refuted. The irreducibility of the
  loop rests on the adjuster's joint read, and the engine's learning is not needed for it.

## H5 — Freezing the claimant collapses the loop

- **Claim:** If the claimant no longer reads the decision, so the claimant's state holds (C'=C) while
  engine and adjuster keep their H3 rules (E'=C∧A, A'=E∧C), the form is dyadic. A party read but frozen
  has no live link to the commit, the condition q63 H5 found sufficient to factor.
- **H0:** `loop_frozen_claimant` is triadic, so engine and adjuster reading the claimant suffices without
  the claimant reading the outcome.
- **Predicted outcome:** `loop_frozen_claimant` dyadic, max Φ_MIP = 0. H0 refuted. A claimant who cannot
  see or respond to the decision is outside the coordination that decides the claim.
