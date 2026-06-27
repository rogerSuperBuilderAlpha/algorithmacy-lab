# Q208 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses, each with its null and predicted outcome, committed before any test runs.

The depth-k form **F_k** is the conjunctive triad with k buffer nodes in series on the mediator's feedback
path: the mediator commits `S'=W∧C` every step, and the parties read the mediator's value k steps late
through a delay line B1→B2→…→Bk. F_0 is the synchronous triad `W'=S, S'=W∧C, C'=S` (triadic, Φ_MIP=2.0).
F_1 is q205's single-buffer form (n=4). The sweep runs k = 0, 1, 2, 3 (n = 3, 4, 5, 6).

## H1 — Instrument control
- **Claim:** F_0 reads triadic with Φ_MIP = 2.0.
- **H0:** —
- **Predicted outcome:** triadic, max_phi = 2.000000. No comparison number is trusted unless this passes.

## H2 — Represented latency never factors the triad
- **Claim:** F_k is triadic at every tested depth k = 1, 2, 3: a represented delay, however deep, leaves
  the coordination irreducible.
- **H0:** There is a depth k ≤ 3 at which F_k reads dyadic.
- **Predicted outcome:** all of F_1, F_2, F_3 read triadic.

## H3 — Whole-system Φ_MIP decays monotonically with depth
- **Claim:** Each added buffer lowers the whole-system Φ_MIP: the sequence over k = 0, 1, 2, 3 is strictly
  decreasing (q205 already showed 2.0 → 1.0 from k=0 to k=1).
- **H0:** Φ_MIP is flat or non-monotone in k.
- **Predicted outcome:** max_phi(F_0) > max_phi(F_1) > max_phi(F_2) > max_phi(F_3).

## H4 — Every buffer is load-bearing
- **Claim:** At each depth, all k buffer nodes are members of the major complex — the whole delay line
  carries the integration.
- **H0:** At some depth a buffer is excluded from the core.
- **Predicted outcome:** for each k ≥ 1, {B1, …, Bk} ⊆ `major_complex(F_k).core`.

## H5 — The worker stays excluded
- **Claim:** For every depth k ≥ 1 the worker W is not in the major complex, as at k=1, where the buffered
  loop displaced it.
- **H0:** The worker rejoins the core at some depth.
- **Predicted outcome:** "W" ∉ `major_complex(F_k).core` for all k ≥ 1.
