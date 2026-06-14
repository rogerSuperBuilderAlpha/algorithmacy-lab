# Q66 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on where the irreducible core sits in an agent chain, and what closing the chain into a
loop does. Four rather than five: the question is a focused follow-up to Q65 with four distinct,
separable predictions. Parties: sender intent (E), agents (A1 … Ad), recipient (R). Written and committed
before any test runs.

## H1 — The open-chain core is the recipient-facing pair at every depth

- **Claim:** The maximal complex of the open chain E → A1 → … → Ad → R is the two-element recipient-facing
  pair {Ad, R} for d = 2, 3, 4.
- **H0:** Some depth has a maximal complex that is not {Ad, R}.
- **Predicted outcome:** core = {A2,R}, {A3,R}, {A4,R} at d = 2, 3, 4. H0 refuted.

## H2 — The core stays size two regardless of chain length

- **Claim:** The maximal complex of the open chain has exactly two elements at d = 2, 3, 4; the sender and
  all upstream agents are excluded.
- **H0:** The maximal complex has more than two elements at some depth.
- **Predicted outcome:** |core| = 2 at every depth. H0 refuted.

## H3 — Closing the chain into a loop binds the whole structure

- **Claim:** A conjunctive ring (each element commits the conjunction of its two cyclic neighbours, closing
  E → A1 → … → Ad → R → E) has a maximal complex equal to the full element set, at d = 2 and d = 3.
- **H0:** The ring's maximal complex is a proper subset of the elements.
- **Predicted outcome:** core = all elements for the ring at both sizes. H0 refuted.

## H4 — Closing the loop raises integration above the open-chain pair

- **Claim:** The open-chain maximal-complex Φ is 2.0 at every depth, while the closed ring's
  maximal-complex Φ exceeds 2.0.
- **H0:** The ring's maximal-complex Φ does not exceed the open chain's 2.0.
- **Predicted outcome:** open chain Φ = 2.0; ring Φ > 2.0. H0 refuted.
