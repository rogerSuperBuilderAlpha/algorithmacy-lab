# logged_alt_duty_exact_phi — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_V4 #7).** On logged collaboration graphs (or
the lab’s closest logged-structure panel), does **anti-correlated party
duty** recreate the exact-Φ joint-observation cliff seen on synthetic
multifamily (V4 #1 `TRANSFER_PARTIAL_EXACT_PHI`, phi_alt 1.000→0.660),
or does logged structure soften it?

**Already known (cited, not reopened).**
- V3 #16 `correlated_party_duty/` —
  **ALTERNATION_RECREATES_CLIFF**: MI alt ≈ chance; phase holds.
- V4 #1 `joint_obs_cliff_exact_phi/` —
  **TRANSFER_PARTIAL_EXACT_PHI**: exact-Φ alt cliffs on multifamily
  (1.000→0.660); soft on mediation family_n3.
- V4 #2 `PHASE_RESTORES_JOINT`; V4 #3 `RETAIN_FAILS_WITH_ZERO`.
- V3 #13 / V2 #45: public OSS role counts + institutional elicits +
  activity fits are the lab’s committed logged-structure renders.

**Universe.** Exact binary IIT-4.0 via `classify_rules`. Two panels:

1. **synthetic multifamily** — V4 #1 designed hub / chain / pool / ring /
   broadcast / broken forms at n∈{3,4} (cliff control).
2. **logged structure** — committed recurrence OSS Boolean renders:
   institutional elicits (PyPhi v9, sklearn v10, k8s v11), weekly
   activity fits (`real_series` core/recent), and role-count Boolean
   templates at public role cardinalities n∈{3,4} (identity, cycle-copy,
   k-of-n, conjunctive hub). Closest logged-structure panel the lab has;
   not a live graph crawl.

**Roles.** Parties A,B and mediator M. Mediation / n=3 activity: A=0,
M=1, B=2. Hub-like / role-count / n=4 activity: M=0, A=1, B=n−1.
Institutional v10 (W,R,S,C): A=0, M=2, B=3. v11 (R,B,C,W): A=3, M=0,
B=2.

**Screens (labels = full-form structure).**
1. **phi_full** — exact max Φ of the full form.
2. **phi_alt** — mean exact max Φ on induced pairs (M,A) and (M,B)
   (anti-correlated / never-joint party admission; same screen as V4 #1).
3. **phi_phase** — equals phi_full (joint design admits the full form).

**Bars.** Hold: AUC ≥ **0.85** or within **0.10** of phi_full. Cliff:
AUC < **0.70** or drop from phi_full ≥ **0.20**.

## H1 — synthetic multifamily alt cliffs (#1 control)

On multifamily, `phi_alt` meets the cliff bar vs `phi_full`. Null:
softens.

## H2 — synthetic multifamily full holds

On multifamily, `phi_full` holds (AUC ≥ 0.85). Null: fails.

## H3 — logged alt cliffs (recreates)

On the logged panel, `phi_alt` meets the cliff bar vs `phi_full`. Null:
softens (logged structure softens the cliff).

## H4 — logged full holds

On the logged panel, `phi_full` holds. Null: fails.

## H5 — phase equals full on both panels

`phi_phase` AUC equals `phi_full` on multifamily and logged (joint
admission). Null: any mismatch.

## Reading keys

- **CLIFF_RECREATES_ON_LOGGED:** H1 ∧ H2 ∧ H3 ∧ H4 — anti-correlated
  duty recreates the exact-Φ cliff on logged structure.
- **LOGGED_SOFTENS_CLIFF:** H1 ∧ H2 ∧ ¬H3 ∧ H4 — synthetic cliffs;
  logged softens.
- **CONTROLS_FAIL:** ¬H1 ∨ ¬H2.
- **LOGGED_PANEL_FAILS:** H1 ∧ H2 ∧ ¬H4.
