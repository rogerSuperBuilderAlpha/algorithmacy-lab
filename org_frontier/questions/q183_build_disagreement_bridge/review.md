# q183 — review

## What was built

A shared bridge module, `org_frontier/qualitative/disagreement_phi.py`, and study 1 of the
qualitative disagreement line. The module exposes `spread(A, B, labels)` and reuses
`verdict()` and `major_complex()` from `org_frontier.probes.lib`; Φ is not reimplemented.

## What holds

- Instrument control passes: the faithful triad reads triadic with max Φ_MIP = 2.0.
- H1 (zero anchor) supported: identical accounts return (1, 0.0, 1.0).
- H2 (symmetry) supported: swapping A and B leaves the spread unchanged on a pair that
  genuinely diverges (verdict split, phi_gap = 2.0).
- Output is byte-identical across three runs (deterministic, seeded).

## Limits and open points

- The accounts are synthetic. The module scores divergence between two coded rule sets, not a
  real coordination. The coded-account-to-observation gap is not addressed here.
- `core_jaccard` is read at each account's own max-Φ reachable state. When two accounts reach
  the same structure but at different states, the Jaccard is well defined but its interpretation
  as "core divergence" leans on the max-Φ state being the representative one. This is a modelling
  choice, fine for the binary-contrast controls used here; a later study that needs per-state
  alignment should compare cores state-by-state over the shared reachable set.
- H2 is shown on a single divergent pair. Symmetry is a structural property of the construction
  (the spread components are symmetric functions of the two accounts), so the single control is
  a check rather than a survey; a later study can widen the pair set.

## Verdict

The instrument is valid on its controls and ready for the rest of the line to apply across
settings.
