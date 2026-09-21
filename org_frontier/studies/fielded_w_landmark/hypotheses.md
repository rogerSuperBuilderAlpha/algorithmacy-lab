# fielded_w_landmark — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #6).** Does V3 #14’s **W+n → landmark**
rule (`W_N_PREDICTS_LANDMARK`) still hold when W is taken from a
**fielded / noisier instrument** (rater noise on subscales, partial /
missing subscales) — or does landmark prediction collapse while
**verdict-class** hold survives?

**Already known (cited, not reopened).**
- V3 #14 `wageman_phi_landmark/` — **W_N_PREDICTS_LANDMARK**: clean CM
  echo W with n predicts HUB / RING4 / POOL; W alone fails cross-n;
  verdict AUC=1.
- V2 #44 `wageman_ti_verdict/` — **WAGEMAN_PREDICTS_VERDICT**.
- V4 #4–#5 exact-Φ imputer arc (separate lane).

**Universe.** Exact binary IIT-4.0 Φ via `major_complex` / `verdict`.
Landmark forms: hub / ring / pool at n∈{3..6} (ring/pool n≥4). Verdict
holdout: #14-style independent / feed / handoff / AND / XOR / OR
chains. Clean W = V2 #44 index `(reciprocity+input+affect)/3` from CM.

**Fielded instrument (query W).** Prototypes stay **clean CM W**.
Observed W is degraded:
1. **Rater noise** — Gaussian noise on the three subscales (σ fixed;
   clip to [0,1]; mean over trials).
2. **Missing subscale** — drop one subscale (mean of the other two).
3. **Partial (single subscale)** — reciprocity-only (stress case).

**Bars.** Landmark hold: (W,n) nearest-clean-prototype accuracy ≥
**0.85**. Landmark collapse: accuracy < **0.85**. Verdict hold: AUC(W→
triadic) ≥ **0.85**. N4 order: hub < ring < pool with gaps ≥ **0.05**.

## H1 — clean control replicates #14

Clean W: N4 order+gaps hold; (W,n) acc ≥ 0.85; W-alone cross-n acc <
0.85; verdict AUC ≥ 0.85. Null: any fails.

## H2 — rater noise collapses landmark

Under subscale rater noise (σ=0.20, trial-mean), (W,n) acc < 0.85.
Null: still ≥ 0.85.

## H3 — verdict hold survives the same rater noise

Under the same σ=0.20 regime, verdict AUC ≥ 0.85. Null: below.

## H4 — missing subscale does not by itself collapse landmark

Dropping any one subscale (same-instrument W) keeps (W,n) acc ≥ 0.85
on this symmetric landmark panel. Null: some drop collapses it.

## H5 — single-subscale stress still orders N4

Reciprocity-only W still yields N4 hub < ring < pool with gaps ≥ 0.05.
Null: order or gaps fail.

## Reading keys

- **LANDMARK_COLLAPSES_VERDICT_HOLDS:** H1 ∧ H2 ∧ H3 — fielded rater
  noise breaks landmark prediction; verdict class still separates.
- **BOTH_HOLD:** H1 ∧ ¬H2 ∧ H3 — landmark survives this fielded noise.
- **BOTH_COLLAPSE:** H1 ∧ H2 ∧ ¬H3 — noise breaks both.
- **MISSING_ALSO_COLLAPSES:** H1 ∧ ¬H4 — missing subscale alone is
  enough (panel not subscale-redundant).
- **CONTROLS_FAIL:** ¬H1.
