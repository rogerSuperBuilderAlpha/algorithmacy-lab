# partial_observation_screen — hypotheses (fixed before computing)

**Question (agenda #24).** How fast does estimability degrade under
partial observation — a hidden node, or a party observed only
intermittently?

**Already known (cited, not reopened).**
- #122 / #23 FAST_WITHIN_FAMILY: mean pairwise MI ranks the verdict at
  AUC≥0.97 by T=125 on the n=3 strict-mediation family under full
  observation; lab T=4000 is past the knee.
- #21 SPECTRAL_PARTIAL: transfer-operator spectral gap is a partial
  cross-family lever; not a closed invariant.
- #22 NO_STRUCTURE_GAIN; #25 AL_NO_GAIN; #134 coupling inversion across
  topology.
- Estimation lane picture in `ESTIMATION_ARC.md` (#21–#23, #25). Cascade
  selective exact Φ remains the practice default for uncertain screens.
- Construct/omit/ladder/indeg closed. No Hegel/Substack.

**Universe.** Exact binary IIT-4.0 labels (`classify_rules`) on designed
panels. Cheap screen = mean pairwise MI among *observed* node pairs
(complete-case MI under the observation mask). One nested noisy
trajectory per form (candid: one draw; T=2000; noise=0.08). Ground-truth
Φ and triadic/dyadic labels always use the full designed system —
partial observation affects the screen only.

**Observation regimes.**
1. **Full** — all nodes observed (baseline).
2. **Hidden node** — one column always masked (party vs mediator).
3. **Intermittent** — one column observed each step with duty cycle
   δ ∈ {1.0, 0.75, 0.5, 0.25, 0.1, 0.0}; other nodes always observed.
   Pairwise MI uses timesteps where both endpoints are observed.

**Panels (honest N).**
- Primary: `family_n3` — 48 forms (24 tri / 24 dya) from strict
  mediation (#122/#23 setting), where full-obs MI works.
- Secondary: designed multi-family panel at n∈{3,4} (hub / chain /
  pool / broadcast / broken / majority / two_hub) for family mediation.

**Primary metric.** Oriented ROC-AUC of mean-MI ranking triadic vs
dyadic. Secondary: ΔAUC vs full-obs baseline; per-family AUC under
hidden party.

## H1 — hidden party collapses cheap-screen AUC sharply

On `family_n3`, full-obs MI AUC ≥ **0.90**, and hiding one party drops
AUC by ≥ **0.20** (or to < **0.70**).

Null: drop < 0.20 and AUC under hidden party still ≥ 0.70.

## H2 — intermittent observation degrades smoothly with duty cycle

On `family_n3`, intermittent-party MI AUC is monotone non-decreasing in
δ (allowing ties), and the largest consecutive drop on the δ grid is
≤ **0.25** (no single cliff as large as H1’s hidden-party collapse).

Null: non-monotone by more than 0.05, or a consecutive drop > 0.25.

## H3 — topology / family mediates degradation

Either (a) ΔAUC under hidden party differs by ≥ **0.15** across families
on the multi-family panel, or (b) hiding the mediator vs a party differs
by ≥ **0.10** AUC on `family_n3`.

Null: family ΔAUC spread < 0.15 and mediator-vs-party |Δ| < 0.10.
