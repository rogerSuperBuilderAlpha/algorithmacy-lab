# Q50 — findings

Probes #150–#154. Exact IIT-4.0 Φ via PyPhi, n=3 deterministic Boolean forms, strict-mediation family
(256 forms). Grows from Q45 probe #148.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — matched non-constant reads bind OR | confirmed | 2/16 OR forms triadic; both are W1_S7_C1 and W2_S7_C2 (iw=ic ∈ {1,2}); 0 false positives or negatives on the matched-live predicate. |
| H2 — constant reads exclude OR binding | confirmed | 12/16 OR forms have a constant party read (iw or ic ∈ {0,3}); 0 triadic among them. |
| H3 — asymmetric reads collapse OR | confirmed | 12/16 OR forms have iw ≠ ic; 0 triadic among asymmetric forms. |
| H4 — binding OR forms share the canonical seam tie | confirmed | W1_S7_C1 and W2_S7_C2 both triadic at max_phi=2.0; seam set {W,C}, matching the instrument control. |
| H5 — commit symmetry splits the party-read rule | confirmed | 16 monotone Phi=2.0 forms: 8 symmetric commits (AND/OR/NOR/NAND) all use matched reads (iw=ic ∈ {1,2}); 8 implication commits all use complementary reads ({iw,ic}={1,2}); 0 cross-rule violations. |

**Through-line.** OR-labelled strict-mediation forms share the same mediator commit (S'=W∨C) and the same
four-edge floor (#145), yet only two of sixteen bind triadically at Φ=2.0 (#148). The separating structure
is party-read wiring, not the OR commit itself. Both binding forms use matched non-constant reads of S:
W1_S7_C1 has W'=S and C'=S; W2_S7_C2 has W'=¬S and C'=¬S (H1). Constant party reads (emit-only or
sink-like) block binding in all twelve affected OR forms (H2), and every mismatched read pair (identity
on one side, NOT on the other) stays dyadic (H3). The two binding OR forms reach the same Φ magnitude and
{W,C} seam tie as the canonical conjunctive triad (H4). The rule generalizes across all sixteen monotone
Φ=2.0 forms: symmetric mediator commits require matched party reads; asymmetric implication commits
require complementary reads (H5).

**Caveats.** n=3 strict mediation only; synchronous update; party-read indices from one-input truth tables.
Results describe Boolean coordination forms, not empirical organizations.

**Reproduce.**
```
python -m org_frontier.questions.q50_or_triadic_seam.probe_or_matched
python -m org_frontier.questions.q50_or_triadic_seam.probe_or_constant
python -m org_frontier.questions.q50_or_triadic_seam.probe_or_asymmetric
python -m org_frontier.questions.q50_or_triadic_seam.probe_or_seam
python -m org_frontier.questions.q50_or_triadic_seam.probe_commit_symmetry
```
