# Hegel — Stage 4 methods

## Shared infrastructure

- Rules → TPM via `classifier.tpm_from_rules`; whole-system verdict via `probes.lib.verdict`; major complex
  via `probes.lib.major_complex` (max over reachable states).
- Share: `Φ(core of whole) − Φ(core with the term and its edges deleted)`, deletion by dropping the node
  and every reference to it (a rule with no inputs left holds its state).
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}. The syllogism form is this triad under Hegel's
labels; the control and the H1 form are the same computation, and the paper says so.

## Forms

Little-endian; `∧` is AND. Specs are `label: (combinator, sources)`; `and` over an empty list holds.

| form | rules |
|---|---|
| judgment | A' = B; B' = A |
| syllogism | A' = M; M' = A ∧ B; B' = M |
| communication | A' = A; M' = A; B' = M |
| scent | A' = A; M' = A; B' = A |
| half_return | A' = M; M' = A ∧ B; B' = B |
| system | A' = B ∧ C; B' = A ∧ C; C' = A ∧ B |
| rotating | clock (k₁, k₂): 00 → 01 → 10 → 00 (11 → 00). Phase 0: A is middle — A' = B ∧ C, B' = A, C' = A. Phase 1: B is middle. Phase 2: C is middle. |

For `rotating`, whole-system Φ and the major complex are taken over the five nodes; the clock is expected
outside. Φ is reported as the max over reachable states, as everywhere in the lab.

## Decision rules

- **H1** CONFIRMED iff M in core, Φ(delete M) = 0, and Φ(syllogism) > Φ(judgment). PARTIAL iff (a) holds and
  Φ(syllogism) = Φ(judgment). REFUTED otherwise.
- **H2** CONFIRMED iff both relay forms have Φ_MIP = 0 and no complex containing M, with B reachable from A.
  REFUTED otherwise.
- **H3** CONFIRMED iff half_return core = {A, M} and syllogism core = {A, M, B}. REFUTED otherwise.
- **H4** CONFIRMED iff syllogism shares are (A 0, M 2, B 0) and system shares are equal and > 0. PARTIAL iff
  one of the two. REFUTED iff neither.
- **H5** CONFIRMED iff rotating core = {A, B, C} and |Φ(rotating) − Φ(system)| < 1e-6. PARTIAL iff core =
  {A, B, C} and Φ(rotating) < Φ(system). REFUTED iff core ≠ {A, B, C}.

## Reporting

Each probe prints the control line, one line per form (`form  Φ_MIP  core  coreΦ`), share lines where
computed, and a verdict. Results in `results/<probe>.json`.
