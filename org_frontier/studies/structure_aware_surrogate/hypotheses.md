# structure_aware_surrogate — hypotheses (fixed before computing)

**Question (agenda #22).** Does a structure-aware surrogate
(connectivity-plus-function input) generalize across topology where
coupling features fail (#129, #134)?

**Already known (cited, not reopened).**
- #123 / #129: trajectory-coupling surrogates fail or only partly lift
  on held-out topology archetypes.
- #134: pairwise coupling AUCs invert across topology (pools low-MI
  yet high-Φ).
- Cascade / residual arc: cheap verdict screens leave a holistic
  residual; margin cascade is selective exact Φ — orthogonal here.
- Construct/omit/ladder arc closed (`CONSTRUCT_LADDER_ARC.md`).

**Universe.** Exact binary IIT-4.0 Φ labels (`classify_rules`). Designed
multi-topology panel at n∈{3,4,5}. Honest N; candid about compute
(trajectory coupling is the costly arm).

**Models.**
- **Coupling-only:** Probe-99 eight aggregate trajectory features
  (entropy / MI / TE / O-info) → RF.
- **Structure-aware:** connectivity matrix graph stats + per-node
  Boolean function properties (same *input class* as a GNN on
  connectivity-plus-function; no torch GNN in this environment) → RF.

**Protocol.** Leave-one-topology-family-out (not random form split).
Primary: detection AUC / accuracy for triadic vs dyadic. Secondary:
Spearman ρ(pred, Φ) for magnitude.

## H1 — structure-aware beats coupling on held-out topologies

Mean LOFO detection AUC for structure-aware ≥ mean LOFO AUC for
coupling-only + **0.15**, and structure-aware mean AUC ≥ **0.70**.

Null: lift < 0.15 or structure AUC < 0.70.

## H2 — no gain

|mean AUC_structure − mean AUC_coupling| < **0.05**.

Null: absolute gap ≥ 0.05.

## H3 — gains detection but not magnitude (or vice versa)

Detection meets H1 lift, but magnitude mean LOFO Spearman gain
(structure − coupling) < **0.10**; **or** magnitude gain ≥ 0.10 while
detection lift fails H1.

Null: both detection and magnitude clear the gain bars, or neither.
