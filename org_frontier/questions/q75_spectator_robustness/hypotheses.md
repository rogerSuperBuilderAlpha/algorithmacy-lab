# Q75 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on the robustness of the triadic core {E, M, R} under added spectators. Written and
committed before any test runs.

## H1 — Uncoupled spectators leave the core fixed

- **Claim:** Adding k uncoupled frozen spectators (Si'=Si, no edges to the triad) leaves the maximal
  complex {E, M, R} at Φ=2.0 for k = 1, 2, 3.
- **H0:** Some uncoupled spectator joins the core or changes its Φ.
- **Predicted outcome:** core {E, M, R}, Φ=2.0 at every k. H0 refuted.

## H2 — A read-only spectator stays out

- **Claim:** A read-only spectator (reads M, read by none) leaves the maximal complex {E, M, R}.
- **H0:** The read-only spectator joins the core.
- **Predicted outcome:** core {E, M, R}. H0 refuted.

## H3 — An emit-only spectator stays out

- **Claim:** An emit-only spectator (a constant source the determination does not depend on) leaves the
  maximal complex {E, M, R}.
- **H0:** The emit-only spectator joins the core.
- **Predicted outcome:** core {E, M, R}. H0 refuted.

## H4 — The core Φ is invariant across all spectator additions

- **Claim:** The maximal-complex Φ stays at 2.0 across the uncoupled, read-only, and emit-only additions.
- **H0:** Some addition changes the core Φ.
- **Predicted outcome:** Φ=2.0 throughout. H0 refuted.
