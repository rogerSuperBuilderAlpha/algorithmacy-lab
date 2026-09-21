# wageman_phi_landmark — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V3 #14).** Can a survey / Wageman-style
instrument (V2 #44) be paired with an in-silico form so measured W
predicts not only verdict class but the **Φ landmark** (ring-4 vs
hub-(n−1) vs pool)?

**Already known (cited, not reopened).**
- V2 #44 `wageman_ti_verdict/` — **WAGEMAN_PREDICTS_VERDICT**: CM-only
  `W=(reciprocity+input+affect)/3` separates dyadic/triadic (AUC=1);
  does **not** grade Φ within a CM (XOR vs AND share W).
- Landmarks: conjunctive hub Φ=n−1; ring Φ=4 (n≥4); all-required pool
  Φ=n(n−1) (`probe_topology_map.pool`).
- V3 #13 ROLE_COUNTS_HUB_WEAKEST: pointer only.

**Instrument.** Exact binary IIT-4.0. Same Wageman CM index as #44.
In-silico designed forms (no new survey fielding). Pairing = attach
survey-style W (and size n) to a Boolean form and ask whether landmark
class is recoverable.

**Landmark labels (form family + Φ signature).**
- **HUB:** conjunctive `single_hub(n)` with Φ=n−1, full core.
- **RING4:** `ring(n)` with Φ=4, full core (the ring landmark).
- **POOL:** all-required pool with Φ=n(n−1), full core.
- **OTHER:** else (including #44 XOR/AND chains used for verdict check).

**Panels.**
1. **N4 triad** — hub4, ring4, pool4 (the question’s named comparison).
2. **Cross-n landmarks** — hubs n=3..6, rings n=4..6, pools n=4..6.
3. **Verdict holdout** — #44-style low/high W forms for dyadic/triadic.

**Predictors.**
- W alone: nearest prototype among {HUB,RING4,POOL} W values at n=4.
- (W, n): nearest prototype among landmarks that exist at that n.

## H1 — at n=4, W separates the three landmarks

On the N4 triad, W(hub) < W(ring) < W(pool) with gaps ≥0.05, and
nearest-prototype accuracy = 1. Null: any tie/inversion or miss.

## H2 — W alone fails across sizes

On the cross-n landmark panel, W-alone prototype accuracy < 0.85
(expected collisions, e.g. hub3 W = ring4 W). Null: accuracy ≥ 0.85.

## H3 — (W, n) recovers landmark across sizes

On the cross-n landmark panel, (W, n) prototype accuracy ≥ 0.85.
Null: below 0.85.

## H4 — W still predicts verdict class (#44 hold)

On the verdict holdout, AUC(W→triadic) ≥ 0.85. Null: below.

## Reading keys

- **W_N_PREDICTS_LANDMARK:** H1 ∧ H2 ∧ H3 ∧ H4 — W alone enough at the
  ring-4 comparison size; across sizes the pairing needs n; verdict hold
  intact.
- **W_ALONE_PREDICTS_LANDMARK:** H1 ∧ ¬H2 ∧ H4 — W alone works even
  cross-n.
- **W_VERDICT_NOT_LANDMARK:** ¬H1 ∧ H4 — verdict only (extends #44).
- **W_NULL:** ¬H4.
- **CONTROLS_FAIL:** instrument or landmark signatures break.
