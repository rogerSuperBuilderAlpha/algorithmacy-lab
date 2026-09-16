# sample_complexity_screen — hypotheses (fixed before computing)

**Question (agenda #23).** What trajectory length is needed to estimate
the dyadic/triadic verdict at a fixed confidence — the sample complexity
of the cheap screen (#122 lineage)?

**Already known (cited, not reopened).**
- #122: mean pairwise MI ranks the verdict at AUC ~0.94–0.96 at T=4000
  across n∈{3,4,5} (strict-mediation / sample_form).
- Probe-99: eight-feature RF transfers across size at T=4000.
- Probe 86: longer trajectories do **not** rescue Φ_R (structural fail).
- q159: CRQA behavioral verdict settles by ~600 steps (different feature).
- #22 NO_STRUCTURE_GAIN (`structure_aware_surrogate/`) — pointer only.
- Construct/omit/ladder/indeg closed.

**Universe.** Exact binary IIT-4.0 labels (`classify_rules`). Cheap
screen = mean pairwise MI (primary, #122) and eight-feature RF
(secondary). Nested prefixes of one long noisy trajectory per form
(candid: one draw; T_max=4000). Noise 0.08 (lab) and 0.16 (stress).

**Panel (honest N).**
- n=3 family: 48 forms (24 tri / 24 dya) from strict-mediation — primary
  #122 setting.
- Within-hub size series at n∈{3,4,5}: single_hub / or_hub / broken /
  broadcast / thresh-k1 / maj (same mediation class; mixed labels).
- Cross-topo designed panel at n=4,5 (secondary): shows whether longer T
  rescues MI when topology mixes (#134).

**Confidence target.** T* = smallest T with mean-MI AUC ≥ **0.90**.
Also report T*_RF for the eight-feature RF (Probe-99).

**Grid.** T ∈ {125, 250, 500, 1000, 2000, 4000}.

## H1 — n=3 family screen is reliable by T=1000

At noise=0.08, T*(n=3 family) ≤ 1000.

Null: AUC at T=1000 < 0.90.

## H2 — within-hub T* grows with n

On the within-hub series, T*(n=5) ≥ 2 × T*(n=3), or T*(n=5) undefined
while T*(n=3) is defined.

Null: T* flat/shrinks when both defined (T*(n=5) < 2× T*(n=3)).

## H3 — higher noise raises sample need

At n=3 family, T*(noise=0.16) ≥ 1.5 × T*(noise=0.08), or undefined at
0.16 while defined at 0.08.

Null: T* unchanged or lower at higher noise.
