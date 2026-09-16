# spectral_invariant — hypotheses (fixed before computing)

**Question (agenda #21).** Is there any topology-invariant feature —
spectral, not coupling-based — that ranks the dyadic/triadic verdict
across families, given that pairwise coupling inverts across topology
(#134)?

**Already known (cited, not reopened).**
- #134: mean MI / TC / O-info AUC ~0.10–0.20 across archetype topologies.
- #22 NO_STRUCTURE_GAIN: cm+function RF ≈ coupling under LOFO.
- #23 FAST_WITHIN_FAMILY: MI is fast within family; longer T ≠ cross-topo.
- Construct/omit/ladder/indeg closed.

**Universe.** Exact binary IIT-4.0 labels (`classify_rules`). Designed
multi-family panel at n∈{3,4,5} (hub / chain / pool / broadcast /
broken / majority / two_hub). Honest N.

**Features.**
- Coupling baselines (traj, T=2000, noise=0.08): mean MI, TC/node, |O-info|.
- Spectral of connectivity (cm): spectral radius; undirected Laplacian
  λ2 (algebraic connectivity), λ_max; spectral gap λ_max−λ2; graph
  energy; von Neumann entropy of normalized Laplacian.
- Spectral of transfer operator: second-largest |eigenvalue| and
  spectral gap of the noisy state-transition matrix P.

**Primary metric.** Pooled cross-family AUC for triadic vs dyadic
(same protocol spirit as #134). Secondary: Spearman ρ with max Φ
among all forms; per-family AUC spread (invariance check).

## H1 — some spectral feature ranks across families

Best spectral AUC ≥ **0.70** and ≥ coupling-best AUC + **0.15**.

Null: no spectral feature clears both bars.

## H2 — all tested spectral features fail or invert like coupling

Every spectral AUC ≤ **0.55** (near/below chance after orientation)
or ≤ coupling-best + 0.05.

Null: at least one spectral feature has AUC > 0.55 and beats coupling
by >0.05.

## H3 — ranks detection but not magnitude

H1 holds for detection, but best spectral Spearman ρ(Φ) < **0.30**.

Null: H1 fails, or ρ ≥ 0.30 when H1 holds.
