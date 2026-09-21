# topology_aware_imputer — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #15).** Under V2 #24’s role-gated
collapse (hide party kills MI screen; hide mediator does not), does a
**topology-aware imputer** (ring vs hub prior) restore AUC, or is party
absence a hard information cut no prior repairs?

**Already known (cited, not reopened).**
- V2 #24 `partial_observation_screen/` —
  **HIDDEN_COLLAPSE_INTERMITTENT_CLIFF**: family_n3 full MI AUC≈0.922;
  hide party C →≈0.547; hide mediator S →≈0.934; intermittent cliffs at
  δ=0.
- #122 / #23 FAST_WITHIN_FAMILY: mean pairwise MI ranks verdict under
  full observation.
- Estimation lane picture in `ESTIMATION_ARC.md`. Construct/omit/
  ladder/indeg closed. No reopen of #24’s intermittent grid.

**Universe.** Exact binary IIT-4.0 labels (`classify_rules`) on
`family_n3` (24 tri / 24 dya strict-mediation forms). Cheap screen =
mean pairwise MI. One nested noisy trajectory per form (T=2000;
noise=0.08). Ground-truth labels always use the full designed system —
observation / imputation affects the screen only.

**Observation / imputation regimes (party index C=2; mediator S=1).**
1. **full** — all nodes observed (baseline).
2. **hide_party** — C always masked; complete-case MI (no impute).
3. **hide_mediator** — S always masked; complete-case MI (role control).
4. **hub_prior** — C masked; fill C under conjunctive-hub prior, then
   mean MI on the completed trajectory.
5. **ring_prior** — C masked; fill C under cycle-copy ring prior, then
   mean MI on the completed trajectory.
6. **naive baselines** (honesty checks, not topology priors): copy-W,
   copy-S, constant-0, Bernoulli(0.5).

**Hub prior (party leaf of conjunctive hub).** Parties mirror the hub
and the hub is AND of parties: seed `C_t ← S_{t-1}`; then enforce
AND consistency from `S_t = W_{t-1} ∧ C_{t-1}` when decisive (S=1 ⇒
C=1; S=0 ∧ W=1 ⇒ C=0).

**Ring prior (3-cycle copy W←C←S←W).** Synchronous ring: `C' = S`,
`W' = C`. Impute `C_t ← W_{t+1}` when available, else `C_t ← S_{t-1}`.

**Primary metric.** Oriented ROC-AUC of mean-MI ranking triadic vs
dyadic. Restore bar: AUC ≥ **0.85** or within **0.10** of full-obs AUC.

## H1 — hide party collapses (reproduce #24 role gate)

On `family_n3`, full-obs MI AUC ≥ **0.90**, and hide-party (no impute)
AUC drops by ≥ **0.20** or falls below **0.70**. Null: drop < 0.20 and
AUC ≥ 0.70.

## H2 — hub prior restores

Under hide-party + hub prior, MI AUC ≥ **0.85** or within **0.10** of
full. Null: neither.

## H3 — ring prior restores

Under hide-party + ring prior, MI AUC ≥ **0.85** or within **0.10** of
full. Null: neither.

## H4 — topology-aware beats naive (optional sharpness)

`max(hub, ring)` exceeds the best naive baseline by ≥ **0.05** AUC.
Null: topo best − naive best < 0.05 (restoration, if any, is not
topology-specific).

## H5 — mediator hide stays healthy

Hide-mediator complete-case AUC ≥ **0.85**. Null: below.

## Reading keys

- **IMPUTER_RESTORES_AUC:** H1 ∧ (H2 ∨ H3) — at least one topology prior
  restores the MI screen.
- **PARTY_ABSENCE_HARD_CUT:** H1 ∧ ¬H2 ∧ ¬H3 — neither prior repairs
  the hide-party collapse.
- **CONTROLS_FAIL:** ¬H1 or ¬H5 (role gate or instrument broken).
