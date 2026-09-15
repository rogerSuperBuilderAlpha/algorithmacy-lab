# Latour — Stage 4 methods

## Shared infrastructure

- Whole-system verdict Φ_MIP: `org_frontier.probes.lib.verdict`; major complex: `major_complex` (max over
  reachable states). Difference-making: Boolean influence of each node on each rule over all inputs (> 0 =
  makes a difference).
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

Conjunctive triad A'=M, M'=A∧B, B'=M: Φ = 2.000000, core {A, M, B}. No comparison is read until it passes.

## Forms

**H1 — intermediary chain** `chain(k)`, k = 0..3, nodes (A, I₁..I_k, B):
A' = B; I₁' = A; I_j' = I_{j−1}; B' = I_k (k = 0: A' = B, B' = A).

**H2 — the third between A and B**, nodes (A, M, B), A' = B, B' = M, and:
- `intermediary`: M' = A.
- `mediator_joint`: M' = A ∧ B.
- `mediator_specific`: M' = A ⊕ M.

**H3 — difference-making**, nodes (S, M, A):
- `source`: S' = S; M' = S ∧ A; A' = M. S makes a difference to M and is determined by nothing but itself.
- `spectator`: S' = M; M' = A; A' = M. S reads and makes no difference.
- `control` (the conjunctive triad) as the case where all three make a difference and all are in.

**H4 — citizen-gun**, nodes (C, G, X):
- `neutral_tool`: G' = C; X' = G; C' = X.
- `autonomous`: G' = G; X' = G; C' = X.
- `translation`: X' = C ∧ G; C' = X; G' = X.

**H5 — the star**, nodes (A, M₁, M₂, M₃), A' = M₁ ∧ M₂ ∧ M₃, and:
- `star_mediators`: M_i' = A ∧ M_{i+1} (indices mod 3).
- `star_intermediaries`: M_i' = A.

## Decision rules

- **H1** CONFIRMED iff Φ_MIP(chain(k)) = Φ_MIP(chain(0)) for k = 1..3 and no I_j is in any core. REFUTED iff
  some I_j is in a core. PARTIAL iff Φ changes but no I_j is in a core.
- **H2** CONFIRMED iff M ∈ core in both mediator forms and M ∉ core in the intermediary form. PARTIAL iff M is
  in the mediator cores but also in the intermediary core. REFUTED iff M is out of a mediator core.
- **H3** CONFIRMED iff, across the three forms, the set of nodes with influence > 0 on some other node equals
  the core. REFUTED iff a node makes a difference and is out of the core (report which). Report separately
  whether every core member makes a difference (necessity).
- **H4** CONFIRMED iff translation core = {C, G, X}, neutral-tool core excludes G, autonomous core excludes C.
  PARTIAL iff translation binds all three and exactly one myth sorts as predicted. REFUTED otherwise.
- **H5** CONFIRMED iff star_mediators core = {A, M₁, M₂, M₃} and Φ_MIP(star_mediators) >
  Φ_MIP(star_intermediaries). PARTIAL iff the mediator star binds all four but the Φ inequality fails, or the
  inequality holds but a mediator is out. REFUTED otherwise. Report the intermediary star's core.

## Reporting

Each probe prints the control line, one line per form (`form  Φ_MIP  core  coreΦ  [influence sets]`), and one
verdict line `H<k> (...): CONFIRMED | PARTIAL | REFUTED`. Results in `results/<probe>.json`.
