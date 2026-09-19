# imputer_exact_phi — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #4).** Do V3 #15’s **ring-prior** and
**naive copy-W** imputers that restored hide-party MI also restore
**exact-Φ ranking**, or do they only rescue the MI screen?

**Already known (cited, not reopened).**
- V3 #15 `topology_aware_imputer/` — **IMPUTER_RESTORES_AUC**: hide
  party MI 1.000→0.550; ring 0.944 and copy-W 0.932 restore; hub
  does not.
- V4 #1–#3: exact-Φ joint / phase / zero-duty–retain arc; retain fails
  with zero-duty.
- V2 #24 role-gated collapse. Construct/omit closed.

**Universe.** Exact binary IIT-4.0 via `classify_rules`. Panel =
`family_n3` as in V3 #15 (SEED 15; 24 tri / 24 dya). Ground-truth
labels = full-form triadic.

**Two screens (same hide-party C).**
1. **MI** — trajectory regimes from V3 #15: full, hide_party (no
   impute), ring_prior, naive_copy_w. Replicate the MI restore control.
2. **Exact Φ** — structural completion of the hidden party’s update
   rule (the exact-Φ analogue of imputation):
   - **phi_full** — Φ(full designed rules).
   - **phi_omit_C** — Φ(V∖{C}) with C frozen out (no impute).
   - **phi_copy_w** — replace C′ with copy-W: `C' = W`.
   - **phi_ring** — replace C′ with ring prior: `C' = S` (3-cycle
     generative rule).
   - **phi_const0** — replace C′ with constant 0 (naive fail control).

**Bars.** Restore / hold: AUC ≥ **0.85** or within **0.10** of full.
Cliff: AUC < **0.70** or drop from full ≥ **0.20**.

## H1 — MI restore replicates (#15 control)

Hide-party MI cliffs, and at least one of ring / copy-W restores MI.
Null: MI control fails.

## H2 — copy-W restores exact Φ

`phi_copy_w` meets the restore bar vs `phi_full`. Null: fails hold.

## H3 — ring prior restores exact Φ

`phi_ring` meets the restore bar vs `phi_full`. Null: fails hold.

## H4 — omit / const0 do not restore

`phi_omit_C` meets the cliff bar, and `phi_const0` fails the restore
bar. Null: either escapes.

## H5 — full Φ holds

`phi_full` AUC ≥ **0.85**. Null: fails.

## Reading keys

- **IMPUTER_RESTORES_EXACT_PHI:** H1 ∧ H2 ∧ H3 — both MI-restoring
  imputers also restore exact-Φ ranking.
- **COPY_RESTORES_RING_FAILS:** H1 ∧ H2 ∧ ¬H3 — copy-W transfers; ring
  does not (partial transfer).
- **RING_RESTORES_COPY_FAILS:** H1 ∧ ¬H2 ∧ H3 — ring transfers; copy
  does not.
- **MI_ONLY_IMPUTER:** H1 ∧ ¬H2 ∧ ¬H3 — MI restores, exact Φ does not.
- **CONTROLS_FAIL:** ¬H1 or ¬H5.
