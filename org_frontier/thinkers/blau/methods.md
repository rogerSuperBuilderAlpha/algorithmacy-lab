# Blau — Stage 4 methods

## Shared infrastructure

- Expression specs and evaluation from `org_frontier.thinkers.coleman.forms`; a deleted variable reads 0. A
  constant supplier is the expression `OR()` of nothing negated — encoded as `NOT(AND())`, since `AND()` of
  nothing is 1 and `NOT` of it 0; the constant 1 is `AND()`.
- Verdict via `probes.lib.verdict`; major complex via `probes.lib.major_complex`; next state from the
  deterministic TPM.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}.

## Forms

| form | rules |
|---|---|
| independent | S' = 1; B' = S |
| contingent | S' = B; B' = S |
| single | S' = B; B' = S |
| alternatives | S1' = B; S2' = B; B' = S1 ∨ S2 |
| unorganized | S' = B1 ∨ B2; B1' = S; B2' = S |
| organized | S' = B1 ∨ B2; B1' = S ∧ B2; B2' = S ∧ B1 |
| power | S' = B1 ∧ B2; B1' = S; B2' = S |
| authority | S' = B1 ∧ B2; B1' = S ∨ B2; B2' = S ∨ B1 |
| opposition_isolated | S' = B1 ∧ B2; B1' = ¬S; B2' = ¬S |
| opposition_shared | S' = B1 ∧ B2; B1' = ¬S ∨ B2; B2' = ¬S ∨ B1 |

The two opposition forms are the Coleman paper's norm_open and norm_closed relabeled (A → S); their numbers
are re-derived here, not copied.

## Decision rules

- **H1** CONFIRMED iff core(contingent) = {S, B} with Φ > 0 and B ∉ core(independent). PARTIAL iff the first
  clause alone. REFUTED otherwise.
- **H2** CONFIRMED iff advantage(S1, alternatives) < advantage(S, single) − 1e-6 and V(S1, alternatives) <
  V(S, single) − 1e-6. PARTIAL iff one. REFUTED otherwise.
- **H3** CONFIRMED iff advantage(S, organized) < advantage(S, unorganized) − 1e-6 and V(B_i, organized) >
  V(B_i, unorganized) + 1e-6 for both. PARTIAL iff one. REFUTED otherwise.
- **H4** CONFIRMED iff next(authority, 011) has B1 = B2 = 1, next(power, 011) does not, and {B1, B2} ⊆
  core(authority). PARTIAL iff two of three. REFUTED otherwise.
- **H5** CONFIRMED iff |core(opposition_shared)| = |core(authority)| and |ΔcoreΦ| < 1e-6, and
  opposition_shared has a fixed point with S = B1 = B2 = 1 while opposition_isolated has no fixed point.
  PARTIAL iff one of the two clauses. REFUTED otherwise.

## Reporting

Each probe prints the control, one line per form, and one verdict. Results in `results/<probe>.json`.
