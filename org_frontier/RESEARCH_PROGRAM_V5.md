# Research program v5 — the holistic residual, and two v4 follow-ups

The standing open edge is the holistic 7% (#94, #106, #13): among the 4096 n=3 wirings, connectivity
decides ~93% of the verdict, and neither per-node influence (#13) nor per-function synergy (#106) closes
the rest. This round attacks the residual directly and follows two surprises from v4. Probes continue at
125. Runs on `worktree/org-frontier`.

## M. The holistic residual

- **M1 — residual-characterization** `[X]` — H: the connectivity-misclassified wirings share a dynamical
  signature (degenerate attractors or non-invertible maps). M: enumerate the 4096 wirings; build a panel
  of connectivity, synergy, and global-dynamics features plus the exact verdict; cache it; report the
  residual set's size and what the misclassified forms share. Builds on #94, #106. Out:
  `probe_residual_characterization.py` + cached panel.
- **M2 — residual-ceiling** `[R]` — H: no cheap feature panel reaches 100% — the residual is
  irreducibly holistic. M: from the cached panel, fit a random forest on the full feature set and report
  the ceiling accuracy and feature importances. Builds on #13, #106. Out: `probe_residual_ceiling.py`.
- **M3 — dynamics-ablation** `[R]` — H: global dynamics features do not help beyond connectivity and
  synergy. M: from the cached panel, compare decision-tree accuracy for connectivity, connectivity+synergy,
  and connectivity+synergy+dynamics. Builds on #94, #106. Out: `probe_dynamics_ablation.py`.

## N. Following v4's surprises

- **N1 — intermediate-hub-drop** `[X]` — H: intermediate hub counts drop members because the dropped
  nodes lose pivotality to the hub cluster (#119). M: at the m where the core is not full, identify which
  nodes drop and read their coupling to the rest. Builds on #119. Out: `probe_intermediate_hub.py`.
- **N2 — mixed-topology-surrogate** `[X]` — H: a surrogate trained on several topology families
  generalizes to a held-out family, fixing the family-specificity (#123). M: train on a mix of families,
  test on a held-out one; compare to the strict-mediation-only surrogate. Builds on #123, #99. Out:
  `probe_mixed_topology_surrogate.py`.

## Waves and status

| Wave | Projects | Lane | Status |
|------|----------|------|--------|
| Y1 | M1 M2 M3 | R/X | **done** (probes 125–127; residual all-FP, dynamics closes ~half, ~5% stays holistic) |
| Y2 | N1 N2 | X | pending |

Stop rule: all Lane-R/X projects done. Probe numbering continues from 124.
