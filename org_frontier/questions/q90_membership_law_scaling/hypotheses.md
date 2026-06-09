# Q90 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether the core-membership law generalizes past the three-node family it was
established on. The law (probe #12): a party is in the major complex only if it is bidirectionally
coupled, and among coupled parties the probability of membership rises with pivotality (out-influence),
at rank-AUC 0.89 on the n=3 family. This study replicates the test at n = 4 and n = 5. Written and
committed before any larger-n result is read. n = 6 is out of reach (~9 minutes per major-complex
computation), and that ceiling is reported rather than crossed.

## H1 — Coupling stays necessary at every size

- **Claim:** The fraction of non-bidirectional nodes in the major complex is below 0.05 at n = 3, 4, 5.
- **H0:** Some size has a non-bidirectional in-core rate ≥ 0.05.
- **Predicted outcome:** below 0.05 at every n. H0 refuted. (Coupling-necessary is the stronger half of
  the law and is expected to hold.)

## H2 — Pivotality keeps predicting membership at every size

- **Claim:** Among bidirectional nodes, the rank-AUC of out-influence predicting major-complex membership
  is at least 0.75 at n = 3, 4, and 5.
- **H0:** The rank-AUC falls below 0.75 at some size.
- **Predicted outcome:** at least 0.75 at every n — the law generalizes. This is the study's central and
  genuinely uncertain claim: more parties open more higher-order ways into the core, and the predictor
  could degrade.

## H3 — The membership gradient persists at n = 4

- **Claim:** At n = 4, the probability of membership for high-influence nodes (top tercile) exceeds that
  for low-influence nodes (bottom tercile).
- **H0:** The high-influence membership probability does not exceed the low-influence one at n = 4.
- **Predicted outcome:** high exceeds low. H0 refuted.

## H4 — The law does not collapse with one added party

- **Claim:** The rank-AUC at n = 4 is within 0.15 of the n = 3 value (no sharp degradation from the
  best-sampled step up in size).
- **H0:** The n = 4 rank-AUC is more than 0.15 below the n = 3 value.
- **Predicted outcome:** within 0.15. H0 refuted.
