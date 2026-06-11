# Q121 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether a non-Φ criterion recovers the verdict, answering the first question of the
critical review's defense agenda (T1). The review found the construct's behavioral validation unmet: the
independent agent-difficulty checks failed or were weak (Probes 98, 107, 108), and the one supporting check
(18) is circular. This study tests the weak form of T1 (a non-circular *formal* criterion), with the strong
form (a behavioral or empirical-external criterion) left explicitly open. Written and committed before the
run; the instruments were prototyped for correctness.

Scope note, fixed in advance: "non-circular" here means computed by a formalism independent of IIT (statistical
multi-information; Boolean-network damage spreading), from the same dynamical system. It does not mean
behavioral or empirical-external. Two criteria are tested against the exact verdict over the 256-form family
and over the 40 full-cycle forms (the hard subset Q117 isolated, where topology and logic split 24/16).

## H1 — The full-family AUC bar is trivial

- **Claim:** On the full 256-form family the class imbalance (24 triadic, 232 dyadic) makes a high rank-AUC
  easy: the topology-only feedback cycle (Q117) alone scores above 0.9.
- **H0:** The cycle's full-family AUC is at or below 0.9.
- **Predicted outcome:** above 0.9. H0 refuted. "AUC well above 0.5 on the family" is therefore not a severe
  test, and the hard subset must carry the burden.

## H2 — An observational criterion fails on the hard cases

- **Claim:** The observational criterion (total correlation of the next-state joint) does not separate the
  verdict on the 40 full-cycle forms: rank-AUC at or below 0.6 (chance-level).
- **H0:** It separates them (AUC above 0.6).
- **Predicted outcome:** at or below 0.6. H0 refuted. Statistical dependence of the dynamics' output does not
  carry the verdict where connectivity cannot, consistent with Q117 and the prior dependence-measure nulls
  (Probes 45-47).

## H3 — An interventional criterion separates the hard cases

- **Claim:** The interventional criterion (Boolean-network damage spreading, horizon ≥ 2) separates the
  verdict on the 40 full-cycle forms at rank-AUC ≥ 0.9.
- **H0:** It does not (AUC below 0.9).
- **Predicted outcome:** ≥ 0.9. H0 refuted. A do-intervention probe recovers the verdict where observation
  fails. This is the study's genuinely uncertain claim — the interventional criterion could equally have
  failed like the observational one, leaving the verdict with no non-Φ correlate on the hard cases.

## H4 — The interventional criterion is not a standalone classifier

- **Claim:** Damage spreading alone does not perfectly classify the full family (full-family AUC below
  0.999): some acyclic dyadic forms spread a perturbation without being irreducible.
- **H0:** It perfectly classifies the full family.
- **Predicted outcome:** below 0.999. H0 refuted. The criterion is a sufficiency test within the
  cycle-screened candidates, not a replacement for the verdict, matching Q117's two-part structure (a
  necessary topological screen plus a sufficient condition).
