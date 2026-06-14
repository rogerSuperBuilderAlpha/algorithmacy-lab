# Q59 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses closing the cut-geometry thread from Q58. Written and committed before any test
runs.

## H1 — Cross-edge shared severance
- **Claim:** The back-channel cross-edge (W→C on worker topologies, C→W on counterpart topologies) appears
  in the severed-edge set of **both** the tied (recipient) and excluded (non-recipient) min-norm cuts on
  every pair.
- **H0:** The cross-edge is severed in only one of the two cuts on at least one pair.
- **Predicted outcome:** 16/16 pairs with cross-edge in both severed sets; 0/16 exclusive to one cut.

## H2 — Fixed symmetric-difference size
- **Claim:** The symmetric difference between tied and excluded severed-edge sets is exactly four directed
  edges on every pair: three edges only in the recipient cut, one edge only in the non-recipient cut.
- **H0:** The symmetric-difference size differs from four on at least one pair.
- **Predicted outcome:** 16/16 pairs at |only_tied|=3 and |only_excl|=1.

## H3 — Cross-edge subtraction equalizes counts
- **Claim:** Removing the back-channel cross-edge from each cut's `cut_ones` count equalizes tied and
  excluded severed-connection totals (the cross-edge alone accounts for the 4-versus-2 split).
- **H0:** Adjusted cut_ones remain unequal on at least one pair after cross-edge subtraction.
- **Predicted outcome:** 16/16 pairs with equal adjusted counts (predicted refutation based on Q58
  mechanistic thread leaving mediator edges unexplored).

## H4 — Mediator edges in recipient-only difference
- **Claim:** Exactly two mediator-incident directed edges (edges with S as source or target) appear in the
  only-tied symmetric-difference set on every pair, and these edges account for the residual 3-versus-1
  asymmetry after the shared cross-edge is counted.
- **H0:** The mediator-edge count in only_tied differs from two on at least one pair.
- **Predicted outcome:** 16/16 pairs with exactly two mediator edges in only_tied; adjusted ratio
  (cut_ones minus cross-edge) stays 3.0 on all pairs.

## H5 — Recipient-template gate invariance
- **Claim:** Worker-recipient topologies (worker_xor, worker_xnor) share one fixed only-tied template
  `{S→W, W→C, W→S}` and only-excl template `{C→S}`; counterpart-recipient topologies share
  `{C→S, C→W, S→C}` vs `{W→S}`; XOR and XNOR gate polarity preserve these templates.
- **H0:** At least one pair violates its recipient-class edge template or gate polarity swaps templates.
- **Predicted outcome:** 8/8 worker pairs match worker template; 8/8 counterpart pairs match counterpart
  template; 0 mismatches.
