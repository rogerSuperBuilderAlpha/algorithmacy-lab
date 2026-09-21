# joint_obs_cliff_exact_phi — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #1).** Does V3 #16’s joint-observation
cliff (`ALTERNATION_RECREATES_CLIFF`) **transfer** under an **exact-Φ
screen** (not MI-only) across a **multifamily / cross-topo** panel, or
is it MI- and family_n3-specific?

**Already known (cited, not reopened).**
- V3 #16 `correlated_party_duty/` —
  **ALTERNATION_RECREATES_CLIFF**: alt W/C (δ≈0.5, never jointly
  observed) keeps MI near chance (≈0.57); zero-duty cliffs; phase-locked
  δ=0.5 holds. Screen was mean pairwise MI.
- V2 #24 `HIDDEN_COLLAPSE_INTERMITTENT_CLIFF`: hide party collapses MI;
  δ≥0.10 holds.
- V3 #15 imputation pointer only. Construct/omit/ladder closed. No
  reopen of the full δ grid.

**Universe.** Exact binary IIT-4.0 labels and exact-Φ scores via
`classify_rules` (max Φ_MIP). Two panels:
1. **family_n3** — 24 tri / 24 dya strict-mediation (V3 #16 universe).
2. **multifamily** — designed hub / chain / pool / ring / broadcast /
   broken forms at n∈{3,4} with both structure classes where available.

**Roles.** Two parties (A,B) and one mediator (M). family_n3: A=W=0,
M=S=1, B=C=2. Hub-like forms: M=0, A=1, B=n−1.

**Screens (scores; labels always full-form structure).**
1. **phi_full** — exact max Φ of the full form.
2. **phi_zero_duty_B** — exact max Φ of the induced subsystem on
   nodes excluding party B (freeze omitted bits at 0).
3. **phi_alt** — mean of exact max Φ on induced pairs (M,A) and (M,B)
   — both parties never jointly admitted.
4. **phi_phase** — same as phi_full (joint design admits the full
   form for exact Φ).
5. **mi_full / mi_alt** — mean pairwise MI under full vs alternating
   A/B masks (family_n3 only; V3 #16 replication control). T=2000,
   noise=0.08.

**Primary metric.** Oriented ROC-AUC of screen ranking triadic vs
dyadic. Soften/hold: AUC ≥ **0.85** or within **0.10** of phi_full.
Cliff: AUC < **0.70** or drop from phi_full ≥ **0.20** (or non-finite
when phi_full held).

## H1 — MI alt cliffs on family_n3 (#16 replicate)

`mi_alt` meets the cliff bar; `mi_full` holds. Null: either fails.

## H2 — exact-Φ alt cliffs on family_n3

`phi_alt` meets the cliff bar relative to `phi_full`. Null: softens.

## H3 — exact-Φ alt cliffs on multifamily (transfer)

`phi_alt` meets the cliff bar on the multifamily panel. Null: softens
or undefined.

## H4 — exact-Φ full / phase hold on both panels

`phi_full` (hence phase) holds on family_n3 and multifamily. Null:
either fails.

## H5 — exact-Φ zero-duty cliffs on family_n3

`phi_zero_duty_B` meets the cliff bar on family_n3. Null: softens.

## Reading keys

- **TRANSFER_HOLDS_EXACT_PHI:** H1 ∧ H2 ∧ H3 ∧ H4 — cliff transfers to
  exact Φ and cross-topo.
- **TRANSFER_PARTIAL_EXACT_PHI:** H1 ∧ ¬H2 ∧ H3 ∧ H4 — MI cliffs;
  exact-Φ alt does not meet the cliff bar on family_n3 but does cliff
  on the multifamily panel (cross-topo transfer without mediation-family
  exact-Φ cliff).
- **EXACT_PHI_ROBUST_MI_ONLY:** H1 ∧ ¬H2 ∧ ¬H3 ∧ H4 — MI cliffs; exact
  Φ alt softens on both panels (MI-specific).
- **FAMILY_N3_ONLY:** H1 ∧ H2 ∧ ¬H3 ∧ H4 — exact Φ cliffs on mediation
  family only.
- **CONTROLS_FAIL:** ¬H1 or ¬H4.
