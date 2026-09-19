# correlated_party_duty — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #16).** Does the intermittent-observation
**cliff at δ=0** soften under **correlated party duty cycles** (two
parties observed on alternating slots), or does any zero-duty party
recreate the cliff?

**Already known (cited, not reopened).**
- V2 #24 `partial_observation_screen/` —
  **HIDDEN_COLLAPSE_INTERMITTENT_CLIFF**: family_n3 full MI AUC≈0.922;
  hide party →≈0.547; intermittent party holds for every δ≥0.10 then
  cliffs at δ=0; hide mediator ≈ full. Cheap screen rides party–party
  coupling.
- V3 #15 `topology_aware_imputer/` — **IMPUTER_RESTORES_AUC** (pointer
  only; imputation not reopened here).
- Estimation lane picture in `ESTIMATION_ARC.md`. Construct/omit/
  ladder/indeg closed. No reopen of #24’s full δ grid beyond the
  controls needed here.

**Universe.** Exact binary IIT-4.0 labels (`classify_rules`) on
`family_n3` (24 tri / 24 dya strict-mediation forms). Cheap screen =
mean pairwise MI under complete-case observation masks. One nested
noisy trajectory per form (T=2000; noise=0.08). Ground-truth labels
always use the full designed system.

**Observation regimes (roles W=0, S=1, C=2; mediator S always on
unless noted).**
1. **full** — all nodes observed (baseline).
2. **zero_duty_C** — C never observed (δ_C=0); recreate #24 cliff.
3. **zero_duty_W** — W never observed (δ_W=0); any-zero-duty check.
4. **sparse_C_d0.10** — independent intermittent C at δ=0.10 (#24 hold
   control).
5. **alt_WC** — correlated / anti-correlated party duty: W on even
   slots, C on odd slots (each δ≈0.5; **never jointly observed**).
6. **phase_WC_d0.50** — both parties on the **same** half of slots
   (δ=0.5 each, joint WC available on those slots) — correlated-same
   control vs alternation.
7. **hide_mediator** — S always masked (role control; should stay high).

**Primary metric.** Oriented ROC-AUC of mean-MI ranking triadic vs
dyadic. Soften bar: AUC ≥ **0.85** or within **0.10** of full.
Cliff bar: AUC < **0.70** or drop from full ≥ **0.20**.

## H1 — zero-duty party recreates the cliff

`zero_duty_C` (and `zero_duty_W`) meet the cliff bar. Null: either
zero-duty party AUC stays ≥ 0.70 and drop < 0.20.

## H2 — alternating party duty softens the cliff

`alt_WC` meets the soften bar. Null: alt AUC < 0.85 and more than
0.10 below full.

## H3 — phase-locked same-slot duty also holds

`phase_WC_d0.50` meets the soften bar (joint WC preserved). Null:
fails soften bar.

## H4 — sparse independent δ=0.10 still holds (#24 control)

`sparse_C_d0.10` meets the soften bar. Null: fails.

## H5 — hide mediator stays healthy

`hide_mediator` AUC ≥ **0.85**. Null: below.

## Reading keys

- **CORRELATED_SOFTENS_CLIFF:** H1 ∧ H2 — alternation softens; any
  zero-duty party recreates the cliff.
- **ALTERNATION_RECREATES_CLIFF:** H1 ∧ ¬H2 — even with both parties at
  δ≈0.5, losing joint WC observation cliffs the screen.
- **CLIFF_UNRELATED:** ¬H1 — zero-duty does not cliff (controls break).
- **CONTROLS_FAIL:** ¬H4 or ¬H5 (instrument / #24 hold broken).
