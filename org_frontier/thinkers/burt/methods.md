# Burt — Stage 4 methods

## Shared infrastructure

- Whole-system verdict Φ_MIP: `org_frontier.probes.lib.verdict`; major complex: `major_complex` (max over
  reachable states). Contingency classes (H1 only): `org_frontier.classifier.contingency.contingency_test`.
- Forms are written as a spec: node → (combinator, sources), combinator ∈ {and, or}. A node with no sources
  is the constant 0. Deleting a party removes its node and drops it from every source list.
- **Value added** V(P) = Φ(major complex of the whole) − Φ(major complex with P deleted).
- **Constraint** C_E = Σ_j (p_Ej + Σ_{q≠E,j} p_Eq p_qj)², p_ij = 1/degree(i) on the undirected tie graph
  (Burt 1992: 54–55). **Effective size** = n − Σ_j Σ_{q≠E,j} p_Eq m_jq, m_jq = 1 if j–q tied.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

Conjunctive triad A'=M, M'=A∧B, B'=M: Φ = 2.000000, core {A, M, B}. No comparison is read until it passes.

## Forms

**H1 — closure by cohesion**, nodes (E, X, Y). Information broker E = and(X, Y); control broker E = or(X, Y).
Open: X = or(E), Y = or(E). Closed: X = or(E, Y), Y = or(E, X). Also reported: the q214 one-sided replace
bypass (Y reads X instead of E) via `contingency_test`.

**H2 — structural equivalence**, information broker E = and(X, Y), contacts X = or(Z…), Y = or(Z…), sources
read E back: Z = or(E).
- `equivalent`: nodes (E, X, Y, Z); X = or(Z), Y = or(Z).
- `nonredundant`: nodes (E, X, Y, Z1, Z2); X = or(Z1), Y = or(Z2).
- `single`: nodes (E, X, Z); E = and(X) (= X), X = or(Z), Z = or(E) — the one-contact reference.

**H3 — constraint sweep**, nodes (E, X, Y, Z), E = and(X, Y, Z), contacts or(E, tied contacts):
k = 0 (no ties), 1 (X–Y), 2 (X–Y, Y–Z), 3 (triangle). C_E = 0.333, 0.611, 0.840, 0.926.

**H4 — the rival**, nodes (E, X, Y) and (E, R, X, Y): E = and(X, Y), R = and(X, Y), X = or(E, R), Y = or(E, R).

**H5 — closure within / beyond**, nodes (E, A1, A2, O), E = and(A1, A2, O):
- `open`: A1 = or(E), A2 = or(E), O = or(E).
- `within`: A1 = or(E, A2), A2 = or(E, A1), O = or(E).
- `across`: A1 = or(E, O), A2 = or(E), O = or(E, A1).
- `everywhere`: A1 = or(E, A2, O), A2 = or(E, A1, O), O = or(E, A1, A2).

## Decision rules

- **H1** CONFIRMED iff under symmetric closure both brokers leave the core or have V(E) = 0. PARTIAL iff
  exactly one does. REFUTED iff neither does.
- **H2** CONFIRMED iff in `equivalent` at most one of X, Y is in the core and V(E) ≤ V(E in `single`) + 1e−6,
  and in `nonredundant` both X and Y are in the core. PARTIAL iff the eviction holds but V(E) exceeds the
  single-contact value, or both hold in `equivalent` but V(E) is at the single value. REFUTED otherwise.
- **H3** CONFIRMED iff V(E) is strictly decreasing over k = 0..3. PARTIAL iff non-increasing with a tie.
  REFUTED iff any increase.
- **H4** CONFIRMED iff V(E | rival) < V(E) and not both E and R in the core. PARTIAL iff one condition holds.
  REFUTED otherwise.
- **H5** CONFIRMED iff V(E) in `within` strictly exceeds the other three. PARTIAL iff `within` is tied for the
  maximum. REFUTED otherwise.

## Reporting

Each probe prints the control line, one line per form (`form  Φ_MIP  core  coreΦ  V(E)`), and one verdict line
`H<k> (...): CONFIRMED | PARTIAL | REFUTED`. Results in `results/<probe>.json`.
