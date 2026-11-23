# Who hears back: a platform that reads some users and answers some users

Fixed before this study's computation.

## Gap

Topology studies so far mostly close every loop: each party feeds the mediator and copies it. Feedforward
pieces are known to drop out of cores (`mediator_hierarchy_census` hub chains; `spanning_mediator_multihub`
feedforward tops; `rival_platforms` spectator W). The two-sided series (`two_sided_platform`,
`asymmetric_sides`, `off_platform_deals`) found that a platform binds exactly the parties whose input can
change its verdict. Here we vary, on one hub, *which* parties the platform listens to and *which* it
answers, independently.

## Model

Platform P and four parties A1..A4 (n = 5). P' = AND of the parties it reads; with r read parties,
P reads A1..Ar. With t answered parties, A1..At copy P (A' = P); the others keep their own last state
(A' = A, a self-loop: they act without hearing back). So A1..min(r, t) are in a closed loop with P;
parties read but not answered are fixed inputs; parties answered but not read are followers.

Grid: r ∈ {1, 2, 3, 4} × t ∈ {0, 1, 2, 3, 4}: 20 forms, plus an OR version of (4, 4) and (2, 4).

Exact IIT 4.0 φ of every reachable subset in every reachable state. Whole Φ = largest full-group φ over
states; top = largest subset φ over states; top ties within 1e-9.

Controls: conjunctive triad Φ = 2.0; (r, t) = (4, 4) AND equals the 4-party AND hub of
`two_sided_platform` (whole Φ = 4.0).

## Outcomes (threshold 1e-9)

- H1: whole Φ > 1e-9 only at (r, t) = (4, 4) among the AND grid.
- H2: for every AND form with m = min(r, t) ≥ 1, top φ = m (within 1e-6), and the top tie set is exactly
  {P, A1..Am}.
- H3: for t = 0, no top tie contains P.
- H4: the OR version of (2, 4) has the same top φ as AND (2, 4).
