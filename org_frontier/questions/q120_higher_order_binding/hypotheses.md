# Q120 — hypotheses (fixed before computing)

The standing law in [`STRUCTURAL_FINDINGS.md`](../../STRUCTURAL_FINDINGS.md) holds that a form demands
algorithmacy when every party is bound into one irreducible joint determination, and that substitutability
of any party collapses it. That phrasing asserts every party is pivotal. Q120 tests the exception: a
triadic form whose binding is purely higher-order, irreducible as a trio but with no single party whose
removal collapses it.

A party P is **pivotal** in a triadic form when knocking it out flips the whole-system verdict from
triadic to dyadic. Knockout replaces P's update rule with a non-interpreting pass-through (P is still read
by the others, but no longer reads them). A **pure higher-order bind** is a triadic form with zero pivotal
parties.

- **H1.** No triadic form is a pure higher-order bind: every triadic form has at least one pivotal party.
- **Null (refutes H1).** A triadic form exists whose verdict survives the knockout of every single party.

The test runs two families and two knockout definitions, fixed here before computing:

- Families: the 256 strict-mediation forms (the mediator S is the only path between W and C, so S is a
  topological cut vertex) and the 4096 fully-coupled forms (every party reads the other two, so no party
  is a cut vertex and redundancy could in principle carry the bind).
- Knockout definitions: "spectator" (P' = x[P], P freezes at its current value) and "silenced" (P' = 0,
  P is forced to a constant). H1 stands only if it holds under both.
