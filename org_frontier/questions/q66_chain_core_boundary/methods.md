# Q66 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems, synchronous update, read on the maximal complex
(`probes.lib.major_complex`) and classified by exact IIT-4.0 Φ where needed (`classifier.classify_rules`).
The open chain reuses `multiparty.chains.chain_rules`. Every probe validates the instrument first: a
decoupled relay reads dyadic and a fully-coupled triad reads triadic at Φ = 2.0. Run on
`~/iit-playground/venv-4.0/bin/python`. Decision rules fixed here.

## H1 and H2 test — open-chain core across depth

- **Forms:** `chain_rules(d)` for d = 2, 3, 4 (n = 4, 5, 6), labels (E, A1, …, Ad, R).
- **Measure:** the maximal complex (`major_complex`): its label set and size.
- **Decision rule:** H1 confirmed if the core is exactly {Ad, R} at every depth. H2 confirmed if the core
  has exactly two elements at every depth. Either is refuted if any depth departs.

## H3 and H4 test — closed ring

- **Forms:** a conjunctive ring on the same elements for d = 2 (n = 4) and d = 3 (n = 5): index the n
  elements 0..n−1 in a cycle (E, A1, …, Ad, R), and set each element's next state to the conjunction of
  its two cyclic neighbours, x[(i−1) mod n] ∧ x[(i+1) mod n].
- **Measure:** the maximal complex (label set, size) and its Φ; the open chain's maximal-complex Φ for
  comparison.
- **Decision rule:** H3 confirmed if the ring's maximal complex is the full element set at both sizes.
  H4 confirmed if the open chain's maximal-complex Φ = 2.0 (within 1e-6) at every depth and the ring's
  maximal-complex Φ exceeds 2.0 at both sizes. Refuted if the ring core is a proper subset (H3) or the
  ring Φ does not exceed 2.0 (H4).
