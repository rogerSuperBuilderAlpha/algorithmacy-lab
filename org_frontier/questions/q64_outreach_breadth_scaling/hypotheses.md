# Q64 — Stage 3 hypotheses (fixed before computation)

Five hypotheses on how the outreach verdict scales with the number of recipients. Parties: sender intent
(E), agent/mediator (M), recipients (R1 … Rk). The agent's commit is M's rule. Written and committed
before any test runs.

## H1 — An all-required campaign stays triadic at Φ = n−1 at every breadth

- **Claim:** The all-required campaign (M'=E∧R1∧…∧Rk, each Ri'=M, E'=M) is triadic for k = 1, 2, 3, 4
  (n = 3, 4, 5, 6), with Φ_MIP = n − 1, matching the conjunctive-hub law.
- **H0:** Some all-required campaign is dyadic, or its Φ_MIP departs from n − 1.
- **Predicted outcome:** triadic at every k with Φ_MIP = 2.0, 3.0, 4.0, 5.0. H0 refuted.

## H2 — A substitutable campaign is dyadic at every breadth

- **Claim:** The substitutable campaign (M'=E∧(R1∨…∨Rk), each Ri'=M) is dyadic for k = 2, 3, 4.
- **H0:** Some substitutable campaign is triadic.
- **Predicted outcome:** dyadic (Φ_MIP = 0) at every k. H0 refuted.

## H3 — A pooled broadcast is dyadic at every breadth

- **Claim:** The pooled broadcast (M'=E, each Ri'=M; the agent ignores every recipient) is dyadic for
  k = 2, 3, 4.
- **H0:** Some pooled broadcast is triadic.
- **Predicted outcome:** dyadic (Φ_MIP = 0) at every k. H0 refuted.

## H4 — One substitutable recipient collapses an otherwise all-required campaign

- **Claim:** At k = 3, a mixed campaign with one substitutable pair (M'=E∧R1∧(R2∨R3)) is dyadic, while the
  fully all-required campaign (M'=E∧R1∧R2∧R3) is triadic.
- **H0:** The mixed campaign is triadic.
- **Predicted outcome:** mixed dyadic (Φ_MIP = 0); all-required triadic. H0 refuted.

## H5 — Every recipient sits in the core of an all-required campaign

- **Claim:** The major complex of the all-required campaign is the full party set {E, M, R1, …, Rk} at
  k = 2 and k = 3; no recipient is excluded.
- **H0:** At least one recipient is outside the major complex of an all-required campaign.
- **Predicted outcome:** core = {E, M, R1, R2} at k=2 and {E, M, R1, R2, R3} at k=3. H0 refuted.
