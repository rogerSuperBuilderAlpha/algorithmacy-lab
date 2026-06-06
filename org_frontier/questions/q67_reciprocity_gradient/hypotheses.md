# Q67 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on the reciprocity gradient of a four-element agent exchange (E, A1, A2, R), from a
feed-forward relay (L0) through a single reciprocal end-loop (L1) and the open chain (L2) to a closed ring
(L3). Four, not five: the gradient admits four distinct, separable predictions. Written and committed
before any test runs.

## H1 — A feed-forward relay is dyadic

- **Claim:** L0 (E constant, A1'=E, A2'=A1, R'=A2; no feedback) is dyadic.
- **H0:** L0 is triadic.
- **Predicted outcome:** dyadic (Φ_MIP = 0). H0 refuted.

## H2 — A single reciprocal end-loop makes the exchange triadic

- **Claim:** L1 (a reciprocal loop only at the recipient end: A2'=A1∧R, R'=A2, upstream feed-forward) is
  triadic with a two-element core.
- **H0:** L1 is dyadic, or its core is not two elements.
- **Predicted outcome:** triadic with core {A2, R}. H0 refuted.

## H3 — The core jumps sharply at loop closure

- **Claim:** The core is two elements for the open chain (L2) and jumps to the full set (size four) for the
  closed ring (L3); the closing edge produces a sharp transition.
- **H0:** The core size at L3 is not four, or equals the L2 size.
- **Predicted outcome:** |core| = 2 at L2, = 4 at L3. H0 refuted.

## H4 — Integration rises monotonically with reciprocity

- **Claim:** Φ_MIP increases along L0 → L2 → L3: 0 < 2.0 < 4.0.
- **H0:** Φ_MIP is not monotone increasing along the gradient.
- **Predicted outcome:** L0 = 0, L2 = 2.0, L3 = 4.0. H0 refuted.
