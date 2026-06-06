# Q65 — Stage 3 hypotheses (fixed before computation)

Five hypotheses on agent-to-agent outreach. Parties: sender intent (E), agents (A1 … Ad) in series,
recipient (R). Each agent commits jointly from its two neighbours; the ends track their adjacent agent.
Written and committed before any test runs.

## H1 — The agent chain stays triadic at every depth

- **Claim:** The chain E → A1 → … → Ad → R (Aj' = A_{j-1} ∧ A_{j+1}, ends track the adjacent agent) is
  triadic for d = 1, 2, 3, 4 (n = 3, 4, 5, 6).
- **H0:** Some agent-chain depth is dyadic.
- **Predicted outcome:** triadic at every depth. H0 refuted.

## H2 — Depth holds Φ constant, unlike breadth

- **Claim:** Φ_MIP of the agent chain is constant at 2.0 across d = 1..4, in contrast to Q64's all-binding
  breadth campaign where Φ = n − 1.
- **H0:** Φ_MIP of the chain varies with depth, or departs from 2.0.
- **Predicted outcome:** Φ_MIP = 2.0 at every depth. H0 refuted.

## H3 — A relay-gap agent collapses the chain

- **Claim:** At d = 2, a chain where one agent relays only its upstream neighbour (A1' = E, ignoring A2)
  is dyadic, while the intact chain (A1' = E ∧ A2) is triadic.
- **H0:** The relay-gap chain is triadic.
- **Predicted outcome:** relay-gap dyadic (Φ_MIP = 0); intact chain triadic. H0 refuted.

## H4 — The whole chain is the irreducible core

- **Claim:** The major complex of the intact agent chain at d = 2 (n = 4) is the full set
  {E, A1, A2, R}; no agent or end is excluded.
- **H0:** At least one element of the chain is outside the major complex.
- **Predicted outcome:** core = {E, A1, A2, R}. H0 refuted.

## H5 — Depth does not undo breadth

- **Claim:** Inserting an agent before an all-binding two-recipient commit
  (E → A1 → M, M' = A1 ∧ R1 ∧ R2, each Ri' = M, A1' = E ∧ M) leaves the form triadic.
- **H0:** The depth-plus-breadth form is dyadic.
- **Predicted outcome:** triadic (Φ_MIP > 0). H0 refuted.
