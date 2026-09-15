# Peirce — Stage 4 methods

## Shared infrastructure

- Cause-effect structure: `pyphi.new_big_phi.phi_structure(pyphi.Subsystem(net, state))`. Each distinction
  `d` has `d.mechanism`, `d.cause.purview`, `d.effect.purview`, `d.phi`. Only irreducible distinctions
  (φ > 0) are returned.
- **Adicity** of a distinction: `max(|mechanism ∪ cause.purview|, |mechanism ∪ effect.purview|)`.
- **Genuine adicity** of a form: the maximum adicity over all distinctions, over all reachable states (plus
  the all-ones state). Implemented in `forms.py: genuine_adicity`.
- Whole-system verdict and major complex: `org_frontier.probes.lib.verdict`, `major_complex`.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad A'=M, M'=A∧B, B'=M must read irreducible at Φ = 2.000000, core {A, M, B}, and genuine
adicity 3 with the adicity-3 distinction being M's over {A, B}. No comparison is read until it does.

## Forms

### H1 — one-input wirings
`one_input_wirings(n)`: every assignment in which node i reads exactly one node j ≠ i, rule = copy
(node_i' = node_j). n = 3 gives 2³ = 8 wirings; n = 4 gives 3⁴ = 81. For each: genuine adicity, whole Φ,
major complex.

Decision rule. H1 confirmed iff max genuine adicity over all 89 wirings ≤ 2 and the control reads 3.
Report how many wirings are whole-irreducible (Φ > 0) despite adicity ≤ 2.

### H2 — grades of degeneracy
| form | rules | Peirce's example |
|---|---|---|
| `monadic_degenerate` | A'=A, B'=B, C'=C | three things each red |
| `dyadic_degenerate` | A'=A, B'=A, C'=B | A father of B, B father of C |
| `genuine` | control | — |

Decision rule. H2 confirmed iff genuine adicity is strictly ordered monadic < dyadic < genuine with values
≤ 1, 2, 3, and neither degenerate form has a three-member complex.

### H3 — giving
Nodes G (giver's act), T (the thing, available/put away), R (receiver's possession). The giver rule is the
same in both forms: G'=¬R (the giver acts while the receiver lacks).
| form | rules |
|---|---|
| `giving_genuine` | G'=¬R, T'=¬R, R'=G∧T — possession made "according to Law," jointly by act and thing |
| `giving_degenerate` | G'=¬R, T'=G, R'=T — "A's putting B away … C's subsequently taking B up" |

Decision rule. H3 confirmed iff `giving_genuine` has genuine adicity 3 with core ⊇ {G, T, R}, and
`giving_degenerate` has genuine adicity ≤ 2. Report Φ and core for both.

### H4 — the sign relation
Nodes O (object), S (sign), I (interpretant).
| form | rules |
|---|---|
| `sign_exogenous` | O'=O, S'=O, I'=(S↔O) — the dynamical object determines and is not determined |
| `sign_pragmatic` | O'=I, S'=O, I'=(S↔O) — interpretation alters conduct toward the object |

Decision rule. H4 confirmed iff `sign_exogenous` has genuine adicity 3 and major complex {O, S, I}. PARTIAL
if `sign_exogenous` has adicity 3 but O is outside the complex (or there is none), while `sign_pragmatic`
binds all three at adicity 3. REFUTED if neither form has an adicity-3 distinction.

### H5 — polyadic reducibility
`two_input_sample(n_forms, seed=0)`: four-element forms in which each node reads exactly two distinct other
nodes (a random choice of the 3 pairs) with a rule drawn uniformly from {AND, OR, XOR, NAND, NOR, XNOR}.
Default sample 60, seed 0. For each: genuine adicity, whole Φ, major complex. The q211 channel form was
considered as a named exemplar and is not used: its mediator rule S1' = W1∧C1∧S2 is three-input, so it is not
a compound of triads in Peirce's sense.

Decision rule. H5 confirmed iff at least one sampled two-input form has genuine adicity 4 and (from H1) no
one-input four-element form has genuine adicity ≥ 3. Report the fraction of the sample at adicity 4, 3, and
≤ 2.

## Reporting

Each probe prints the control line, one line per form (`form  Φ_MIP  core  genuine_adicity  n_distinctions`),
and one verdict line `H<k> (...): CONFIRMED | PARTIAL | REFUTED`. Results in `results/<probe>.json`.
