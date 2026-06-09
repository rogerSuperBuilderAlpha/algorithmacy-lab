# Q81 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on a learned surrogate for the dyadic/triadic outreach verdict. The surrogate is a
random forest over ten size-invariant cheap features (intensive trajectory statistics), trained on the
256-form strict-mediation outreach family (n=3) labelled by exact IIT-4.0 Φ. Written and committed
before any surrogate result is read. Probe #21 already showed that a forest over the raw per-node
feature panel recovers the verdict in-distribution on this family; this study fixes a size-invariant
feature panel so the surrogate can be tested at sizes it never trained on.

## H1 — The surrogate recovers the verdict in-distribution

- **Claim:** On the n=3 outreach family, 5-fold cross-validated ROC-AUC is at least 0.85.
- **H0:** CV ROC-AUC < 0.85.
- **Predicted outcome:** ROC-AUC ≥ 0.85. H0 refuted. (Grounded in probe #21, which reached high AUC on
  this family with the raw panel; the intensive panel is a coarser summary, so the margin may be smaller.)

## H2 — The surrogate beats the class prior

- **Claim:** 5-fold CV accuracy is at least the majority-class baseline plus 0.10.
- **H0:** CV accuracy < baseline + 0.10.
- **Predicted outcome:** accuracy ≥ baseline + 0.10. H0 refuted.

## H3 — The surrogate generalizes past the size it trained on

- **Claim:** A surrogate trained on the full n=3 family classifies held-out outreach forms at n = 4, 5, 6
  (the breadth, chain/ring, and market forms, both classes) with mean accuracy ≥ 0.75 across three
  trajectory seeds. The held-out forms are larger than anything in training.
- **H0:** mean generalization accuracy < 0.75 (no better than the held-out majority, ~0.65).
- **Predicted outcome:** accuracy ≥ 0.75 — the size-invariant fingerprint carries across sizes. This is
  the study's central and genuinely uncertain claim; the verdict could equally fail to transfer if the
  trajectory statistics of larger forms drift outside the n=3 training range.

## H4 — Generalization is not just predicting the majority class

- **Claim:** On the held-out larger forms the surrogate's dyadic recall (mean across seeds) is at least
  0.50 — it identifies dyadic forms, not only the more common triadic ones.
- **H0:** dyadic recall < 0.50 (the apparent generalization is mostly the triadic prior).
- **Predicted outcome:** dyadic recall ≥ 0.50. H0 refuted.
