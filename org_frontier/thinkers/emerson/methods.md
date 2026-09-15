# Emerson — Stage 4 methods

## Shared infrastructure

- Expression specs and evaluation from `org_frontier.thinkers.coleman.forms`; a deleted variable reads 0.
- Verdict via `probes.lib.verdict`; major complex via `probes.lib.major_complex`.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}.

## Forms

| form | rules |
|---|---|
| network | A' = B ∨ C; B' = A; C' = A |
| withdrawal | A' = B ∨ C; B' = B; C' = A |
| extension | A' = B ∨ C; B' = A ∨ C; C' = A ∨ B |
| status | A' = B; B' = A; C' = A |
| coalition | A' = B ∧ C; B' = A ∧ C; C' = A ∧ B |

## Decision rules

- **H1** CONFIRMED iff advantage(A) > 1e-6, |V(A) − coreΦ| < 1e-6, and V(B) = V(C) = 0. PARTIAL iff the
  first clause alone. REFUTED otherwise.
- **H2** CONFIRMED iff B ∉ core(withdrawal) and |advantage(A)| < 1e-6. PARTIAL iff one. REFUTED otherwise.
- **H3** CONFIRMED iff |advantage(A)| < 1e-6, A ∈ core, core = {A, B, C}, and all V equal. PARTIAL iff the
  advantage clause and one other. REFUTED otherwise.
- **H4** CONFIRMED iff |V(A) − V(B)| < 1e-6, {A, B} ⊆ core, and V(C) = 0. PARTIAL iff two of three. REFUTED
  otherwise.
- **H5** CONFIRMED iff advantage(A) is 0 in both, V(A, extension) < V(A, network) − 1e-6, and V(B, coalition)
  > V(B, network) + 1e-6 (likewise C). PARTIAL iff the advantage clause and one direction. REFUTED iff either
  operation leaves A an advantage.

## Reporting

Each probe prints the control, one line per form, and one verdict. Results in `results/<probe>.json`.
