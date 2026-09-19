# matched_imputer_exact_phi — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #5).** Across topologies, does a
**topology-matched imputer** (hub prior on hub carriers, ring prior on
ring carriers) restore exact-Φ ranking under hide-party where the
mismatched ring prior failed in V4 #4 — or is **copy-W** still
uniquely effective?

**Already known (cited, not reopened).**
- V3 #15 `topology_aware_imputer/` — **IMPUTER_RESTORES_AUC**: ring
  restores hide-party MI on mediation; hub does not; copy-W also
  restores (not uniquely topo-specific for MI).
- V4 #4 `imputer_exact_phi/` — **COPY_RESTORES_RING_FAILS**: on
  mediation, copy-W restores exact Φ (0.896); ring (= `C'=S`) does
  not (0.806).
- V4 #1–#3 exact-Φ joint / phase / zero-duty–retain arc.

**Universe.** Exact binary IIT-4.0 via `classify_rules`. Hide party B;
structural completion of B’s update (exact-Φ analogue of imputation).

**Priors (structural next-state for B).**
- **hub** — `B' = M` (party mirrors mediator/hub).
- **ring** — neighbor-AND: `B' = x_{(B-1) mod n} ∧ x_{(B+1) mod n}`
  (canonical ring generative rule). Distinct from V4 #4’s ring, which
  was `C'=S` (≡ hub here on mediation).
- **copy_a** — `B' = A` (naive party-echo / copy-W).
- **const0** — `B' = 0` (fail control).

**Topo tags.**
- **hub-native** — single/or/parity/broadcast hubs + broken-hub
  controls (party-mirror generative).
- **ring-native** — `ring(n)` + broken-ring controls.
- **mediation** — family_n3 as in V4 #4 (SEED 15 panel).
- **matched** — hub prior on hub-native, ring prior on ring-native,
  copy_a elsewhere.
- **mismatched** — ring prior on hub-native, hub prior on ring-native,
  hub elsewhere.

**Bars.** Restore / hold: AUC ≥ **0.85** or within **0.10** of full.
Cliff: AUC < **0.70** or drop ≥ **0.20**. Exact retention on a
triadic form: `|Φ_imp − Φ_full| < 1e-9`.

## H1 — hub-matched retains on hub-native triadics

Exact-retention rate of hub prior on hub-native triadic forms ≥
**0.95**. Null: below.

## H2 — ring-matched retains on ring-native triadics

Exact-retention rate of ring prior on ring-native triadic forms ≥
**0.95**. Null: below.

## H3 — matched beats mismatched on retention

On both hub-native and ring-native triadics, matched exact rate exceeds
mismatched by ≥ **0.50**. Null: gap smaller on either.

## H4 — copy-A restores ranking on mediation

`phi_copy_a` meets the restore bar on mediation (replicate V4 #4
copy-W). Null: fails.

## H5 — matched does not restore ranking on hub∪ring natives

`phi_matched` fails the restore bar on the hub∪ring-native panel.
Null: matched restores ranking there.

## H6 — full holds on mediation and hub∪ring; const0 fails mediation

`phi_full` holds on mediation and on hub∪ring-native; `phi_const0`
fails restore on mediation. Null: any fails.

## Reading keys

- **MATCHED_RETAINS_COPY_RANKS:** H1 ∧ H2 ∧ H3 ∧ H4 ∧ H5 ∧ H6 —
  matched priors retain native Φ and beat mismatch on magnitude;
  copy-A uniquely restores ranking (matched does not).
- **MATCHED_RESTORES_RANK:** H1 ∧ H2 ∧ H3 ∧ ¬H5 ∧ H6 — matched also
  restores ranking on hub∪ring natives.
- **MATCHED_FAILS:** ¬(H1 ∧ H2) — matched retention fails.
- **COPY_FAILS:** ¬H4 ∧ H6 — copy no longer restores mediation.
- **CONTROLS_FAIL:** ¬H6.
