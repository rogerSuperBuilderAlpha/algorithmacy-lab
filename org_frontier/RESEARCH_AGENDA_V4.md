# Research agenda v4 — questions only

V3’s science cells are closed on `contrib` (#1–#16; last verdict
`ALTERNATION_RECREATES_CLIFF`; close-out `V3_LANE_CLOSE.md`). V2 stays
closed. This file lists **new** questions only — residuals V3 named but
did not run, and motifs V3’s Boolean+MI sandbox never reached. No
methods here. Numbered 1–12. Each cites the V3 finding it grows from.

## A. Joint-observation cliff under exact Φ / cross-topo

1. Does V3 #16’s joint-observation cliff
   (`ALTERNATION_RECREATES_CLIFF`) **transfer** under an **exact-Φ
   screen** (not MI-only) across a **multifamily / cross-topo** panel
   (hub / chain / pool / mediation), or is it MI- and family_n3-specific?
   **Answered — TRANSFER_PARTIAL_EXACT_PHI.** MI alt cliffs on
   family_n3 (0.967→0.585); exact-Φ alt is soft there (1.000→0.812)
   but cliffs on multifamily (1.000→0.660). See
   `studies/joint_obs_cliff_exact_phi/`.
2. If exact-Φ alternation cliffs (or fails to), does a **phase-locked**
   same-slot duty at δ=0.5 restore exact-Φ ranking the way it restored
   MI in V3 #16, or does exact Φ need a different joint condition?
   **Answered — PHASE_RESTORES_JOINT.** At matched δ=0.5, phase holds
   on multifamily (AUC 1.000) where alt cliffs (0.660); MI phase holds
   on family_n3 (0.913 vs alt 0.592). Joint observation, not mean duty.
   See `studies/phase_lock_exact_phi/`.
3. Under exact Φ, is **zero-duty** of one party still sufficient to cliff
   (V3 #16 H1), or can an induced party–mediator subsystem retain Φ
   rank when the absent party is frozen out?
   **Answered — RETAIN_FAILS_WITH_ZERO.** Zero-duty cliffs on
   multifamily (1.000→0.592) and family_n3 (→0.750); retain_MA fails
   with it (same AUCs); omit-mediator also cliffs (0.559). See
   `studies/zero_duty_retain_exact_phi/`.

## B. Estimation / imputation leftovers

4. Does V3 #15’s **ring-prior** (and naive copy-W) restoration of
   hide-party MI **transfer under exact-Φ scoring**, or does imputation
   only rescue the MI screen?
   **Answered — COPY_RESTORES_RING_FAILS.** MI restore holds
   (ring 0.944, copy-W 0.932); copy-W restores exact Φ (1.000→0.896)
   but ring does not (0.806). See `studies/imputer_exact_phi/`.
5. Across topologies, does a **topology-matched imputer** (ring on
   rings, hub on hubs) beat a mismatched prior under exact Φ, reversing
   V3 #15’s finding that hub priors fail on mediation family_n3?

## C. Validation / instrument bridge

6. Does V3 #14’s **W+n → landmark** rule survive when W is taken from a
   **fielded / survey-style instrument** on a designed Boolean form
   (not the CM echo alone), or does instrument noise erase landmark
   separation?
7. On logged collaboration graphs (or a public OSS role graph), does
   **anti-correlated party duty** predict failure of a cheap integration
   screen the way V3 #16 predicts in silico?

## D. Scale beyond n=7–8

8. Does V3 #8’s **band grammar** at n=7 (indeg (0,1,1,1,1,1,2)) hold at
   **n=8–9**, or does a new morph appear once more cycle types fit?
9. Does V3 #10’s **parity-hub law** Φ=2^(2−n) continue for **n>8**, or
   does the closed-form break when reachability / MIP sampling bites?
10. At n≥6, do V3 #4–#7’s **composed-topology** verdicts (necklace /
    ring-of-hubs / shared-mediator / hybrid seam) remain discrete
    landmarks under a denser random-coupling draw, or do new interstitial
    atoms dominate?

## E. Beyond the Boolean sandbox (only if A–D block)

11. Does the joint-observation cliff (V3 #16 / V4 #1) survive a
    **graded / continuous** party channel (soft duty, not hard mask), or
    is it an artifact of binary observation masks?
12. Optional tooling: does **M3 subset-Φ fidelity** on
    `third_party/pyphi_iit4_mv` change any V4 #1–#3 verdict, or is
    exact binary Φ already decisive?

---

**First cells on this agenda:** #1
(`studies/joint_obs_cliff_exact_phi/` → `TRANSFER_PARTIAL_EXACT_PHI`);
#2 (`studies/phase_lock_exact_phi/` → `PHASE_RESTORES_JOINT`);
#3 (`studies/zero_duty_retain_exact_phi/` → `RETAIN_FAILS_WITH_ZERO`);
#4 (`studies/imputer_exact_phi/` → `COPY_RESTORES_RING_FAILS`).
