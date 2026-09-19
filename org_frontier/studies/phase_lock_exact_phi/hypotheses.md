# phase_lock_exact_phi — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #2).** Under **phase-locked same-slot
duty** (parties observed together at the same duty fraction δ=0.5),
does exact Φ recover / stay above the cliff where alternating duty
failed — i.e. is **joint observation** the causal factor, not mean
duty?

**Already known (cited, not reopened).**
- V4 #1 `joint_obs_cliff_exact_phi/` —
  **TRANSFER_PARTIAL_EXACT_PHI**: MI alt cliffs on family_n3
  (0.967→0.585); exact-Φ alt soft there (1.000→0.812) but cliffs on
  multifamily (1.000→0.660).
- V3 #16 `ALTERNATION_RECREATES_CLIFF`: MI phase-lock at δ=0.5 holds;
  alternation cliffs. Screen was MI.
- V2 #24 intermittent cliff. Construct/omit/ladder closed.

**Universe.** Exact binary IIT-4.0 via `classify_rules`. Panels from
V4 #1: family_n3 (24 tri / 24 dya) and multifamily (hub/chain/pool/…).
Primary restoration target: **multifamily**, where exact-Φ alt cliffed.

**Matched mean duty δ=0.5 — two correlation structures.**
1. **alt** — parties anti-correlated (never jointly admitted). Exact-Φ
   score = mean Φ on induced pairs (M,A) and (M,B). MI score = mean
   pairwise MI under alternating masks.
2. **phase** — parties co-present on the same half of slots (joint when
   on). Exact-Φ score = Φ(full) (joint design admits the full form).
   MI score = mean MI under same-slot δ=0.5 masks (mediator always on).
3. **full** — δ=1 baseline (exact Φ and MI).

Mean party duty is **0.5 for both alt and phase**; only jointness
differs.

**Bars.** Hold: AUC ≥ **0.85** or within **0.10** of full. Cliff: AUC
< **0.70** or drop from full ≥ **0.20**.

## H1 — exact-Φ alt cliffs on multifamily (#1 replicate)

`phi_alt` meets the cliff bar on multifamily. Null: softens.

## H2 — exact-Φ phase holds on multifamily (restore)

`phi_phase` meets the hold bar on multifamily. Null: fails.

## H3 — exact-Φ phase holds on family_n3

`phi_phase` meets the hold bar on family_n3. Null: fails.

## H4 — MI phase holds and MI alt cliffs on family_n3 (#16 echo)

`mi_phase` holds; `mi_alt` cliffs. Null: either fails.

## H5 — duty matched (design check)

Mean party duty is 0.5 under both alt and phase masks (within 0.01).
Null: |duty−0.5| > 0.01 for either.

## Reading keys

- **PHASE_RESTORES_JOINT:** H1 ∧ H2 ∧ H5 — at matched δ=0.5, phase
  holds where alt cliffs; joint observation (not mean duty) is the
  factor. H3/H4 sharpen.
- **PHASE_FAILS_EXACT_PHI:** H1 ∧ ¬H2 — phase does not restore exact Φ.
- **NO_ALT_CLIFF:** ¬H1 — cannot test restore.
- **CONTROLS_FAIL:** ¬H4 or ¬H5.
