# Caplow — Stage 4 methods

## Shared infrastructure

- Whole-system verdict Φ_MIP: `org_frontier.probes.lib.verdict`; major complex: `major_complex` (max over
  reachable states). Boolean influence as in the Simmel paper (`forms.influence`) for the post hoc reading.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

Conjunctive triad A'=M, M'=A∧B, B'=M: Φ = 2.000000, core {A, M, B}. No comparison is read until it passes.

## Forms

Node order (A, B, C, O). Weights w = (wA, wB, wC) per type:

| type | w | Caplow predicts |
|---|---|---|
| 1 | (1, 1, 1) | AB, AC, BC |
| 2 | (3, 2, 2) | BC |
| 3 | (1, 2, 2) | AB, AC |
| 4 | (3, 1, 1) | none |
| 5 | (4, 3, 2) | AC, BC |
| 6 | (4, 2, 1) | none |
| 7 | (3, 2, 1) | AB, AC |
| 8 | (2, 1, 1) | AB, AC |

`coalition(w, pair)` for pair {X, Y}, isolate Z:

- `bloc = 1 if wX·X + wY·Y > (wX + wY)/2 else 0` — the stronger partner's stance when unequal; X∧Y when equal.
- `O' = 1 if (wX + wY)·bloc + wZ·Z > T/2; 0 if < T/2; O if = T/2`, with T = wA + wB + wC.
- `A' = B' = C' = O`.

`precoalition(w)`: `O' = 1 if wA·A + wB·B + wC·C > T/2; 0 if <; O if =`; `A' = B' = C' = O`.

Form names: `t<k>_<XY>` (e.g. `t2_BC`) and `t<k>_pre`. 24 coalition forms + 8 precoalition forms.

A coalition **binds** iff both partners are in the major complex. A coalition **wins** iff wX + wY > wZ.

## Decision rules

- **H1** CONFIRMED iff for every type the set of binding coalitions equals Caplow's predicted set. PARTIAL if
  it matches in at least four types. REFUTED otherwise. Report the per-type match table.
- **H2** CONFIRMED iff, counting membership over all binding coalitions across the eight types, count(A) <
  count(B) and count(A) < count(C). REFUTED otherwise.
- **H3** CONFIRMED iff in Types 4, 6, 7, 8 BC never binds and A is in the core of all four coalition forms
  and the precoalition form of each type. PARTIAL if BC never binds but A leaves a core. REFUTED if BC binds.
- **H4** CONFIRMED iff in Type 5 all three coalitions bind and A is out of the core under BC and in under AB
  and AC. PARTIAL if the A-membership pattern holds but a partner is out of the core. REFUTED otherwise.
- **H5** CONFIRMED iff every winning coalition (all types) binds. REFUTED if some winning coalitions bind and
  others do not; report whether binding coincides with equal partner weights.

## Reporting

Each probe prints the control line, one line per form (`form  Φ_MIP  core  wins  binds`), and one verdict
line `H<k> (...): CONFIRMED | PARTIAL | REFUTED`. Results in `results/<probe>.json`. The five probes share
`forms.evaluate_types()`; each recomputes the forms it needs.
