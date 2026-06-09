# Q98 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether core membership is a conjunctive gate on a node's two influences. Finding 8
ties membership to bidirectional coupling and pivotality together; this separates a node's reading
(in-influence: how much its own update depends on others) from its influence (out-influence: how much
others depend on it), over the full three-node family, and asks whether one can compensate the other.
Written and committed before the membership surface is read.

## H1 — Strong influence cannot compensate zero reading

- **Claim:** A node with maximal out-influence and zero in-influence is in the major complex with
  probability below 0.10.
- **H0:** Such nodes are in the core with probability ≥ 0.10.
- **Predicted outcome:** below 0.10. H0 refuted. (Reading is necessary and not bought by influence.)

## H2 — Strong reading cannot compensate zero influence

- **Claim:** A node with maximal in-influence and zero out-influence is in the major complex with
  probability below 0.10.
- **H0:** Such nodes are in the core with probability ≥ 0.10.
- **Predicted outcome:** below 0.10. H0 refuted. (Influence is necessary and not bought by reading.)

## H3 — Membership tracks the minimum, not the sum

- **Claim:** The rank-AUC of `min(in-influence, out-influence)` predicting membership exceeds the rank-AUC
  of their sum — the gate is conjunctive, both must be substantial, rather than additive.
- **H0:** The sum predicts membership at least as well as the minimum.
- **Predicted outcome:** the minimum predicts better. H0 refuted. This is the study's central and
  genuinely uncertain claim.

## H4 — Balanced-high membership is near-certain

- **Claim:** A node with both in- and out-influence at the top value is in the major complex with
  probability at least 0.85.
- **H0:** Such nodes are in the core with probability below 0.85.
- **Predicted outcome:** at least 0.85. H0 refuted.
