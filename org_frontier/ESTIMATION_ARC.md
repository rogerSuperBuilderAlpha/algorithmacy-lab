# Estimation lane (#21–#23, #25) — working picture

A short synthesis of the cheap-screen / surrogate estimation arm on
PR #739. Exact binary IIT-4.0 Φ; in-silico. Sibling arcs:
[`CONSTRUCT_LADDER_ARC.md`](CONSTRUCT_LADDER_ARC.md) (closed),
[`OMIT_ATOM_ARC.md`](OMIT_ATOM_ARC.md),
[`ROLE_TARGET_GRAIN.md`](ROLE_TARGET_GRAIN.md). No construct/omit/
ladder/indeg reopen.

## Verdict in one line

**The generalization bottleneck is topology, not sample length,
GNN-style structure, or label order.** Within-family MI is fast;
cross-family coupling inverts; structure-aware RF adds little under
holdout; transfer-operator spectral gap is a partial cross-family
lever; active acquisition does not beat random on this panel.

## Arc

| step | study | verdict | claim |
|---|---|---|---|
| 1 | [`structure_aware_surrogate/`](studies/structure_aware_surrogate/) | **NO_STRUCTURE_GAIN** (#22) | cm+function RF ≈ coupling under LOFO (lift +0.049) |
| 2 | [`sample_complexity_screen/`](studies/sample_complexity_screen/) | **FAST_WITHIN_FAMILY** (#23) | family n=3 MI AUC≥0.97 at T*=125; longer T ≠ cross-topo |
| 3 | [`spectral_invariant/`](studies/spectral_invariant/) | **SPECTRAL_PARTIAL** (#21) | `P_spectral_gap` AUC=0.893 vs inverted MI 0.775; lift +0.118 < 0.15 |

Cited priors (not reopened): #122 within-family MI; #123/#129 OOD
surrogate failure; #134 coupling inversion; cascade/residual arm in
[`foundations/RESIDUAL_AND_CASCADE.md`](../foundations/RESIDUAL_AND_CASCADE.md).

## Working picture

1. **Within family, estimation is cheap.** Mean pairwise MI ranks the
   verdict almost immediately (T*=125 on strict mediation). Lab default
   T=4000 is past the knee.

2. **Across topology, coupling fails.** The same MI feature inverts or
   stays near chance when families mix (#134; #23 cross-topo curves).
   More trajectory length does not fix that.

3. **Structure-aware input is not the missing lever.** Under
   leave-one-family-out, connectivity-plus-function RF does not
   materially beat coupling (#22). The failure mode is not “wrong
   architecture class” on this panel.

4. **Spectral gap is partial.** The noisy transfer-operator spectral
   gap ranks better than inverted coupling and correlates with Φ, but
   misses the pre-registered lift bar (#21). Useful baseline, not a
   closed topology-invariant instrument.

5. **Practice.** Use family-matched cheap screens (or cascade selective
   exact Φ). Do not expect one coupling or GNN-style surrogate to travel
   across topology without labels from that class.

## Active learning (#25)

[`active_label_acquisition/`](studies/active_label_acquisition/) —
**AL_NO_GAIN.** Uncertainty mean AUC 0.901 vs random 0.886 (Δ=+0.015);
topo_balance loses under LOFO mid-budget (0.518 vs uncertainty 0.690).
Label order is secondary; it does not repair the topology bottleneck.

## Best next

**Estimation lane closed.** #21–#25 fix the picture: within-family MI is
cheap and fast; cross-topo needs family-matched labels or selective exact
Φ; structure-aware, spectral, and active acquisition are partial or null
levers, not a closed invariant. **#24**
[`partial_observation_screen/`](studies/partial_observation_screen/)
(PR #749) → **HIDDEN_COLLAPSE_INTERMITTENT_CLIFF** (hide party collapses
MI AUC; intermittent cliffs at δ=0; hide mediator ≈ full).
Construct/omit/ladder stay closed. V3 estimation residual **#15**
[`topology_aware_imputer/`](studies/topology_aware_imputer/) →
**IMPUTER_RESTORES_AUC** (ring prior restores hide-party MI; hub does
not; naive copy-W also restores). Remaining V3 cell: **#16** correlated
party duty cycles vs the δ=0 cliff.
