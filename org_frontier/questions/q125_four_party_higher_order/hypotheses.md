# Q125 — hypotheses (fixed before computing)

Q120 found that among three parties no pure higher-order bind exists: every irreducible form has all three
parties pivotal, so removing any one collapses it. The result was argued to be three-party-specific. With
four parties, redundancy becomes possible — two parties can jointly stand in for a third — so a form might
stay irreducible after the knockout of any single party, the binding carried by the group with no
individual lynchpin. Q125 tests whether that pure higher-order bind appears at four parties.

Definitions carry over from Q120. A four-party form is **irreducible** when its whole-system Φ over the MIP
exceeds PHI_EPS in some reachable state. Party P is **pivotal** when knocking it out (replacing its rule
with a non-interpreting pass-through) makes the form reducible. A **pure higher-order bind** is an
irreducible form with zero pivotal parties.

- **H1.** A pure higher-order bind exists at four parties: some irreducible form survives the knockout of
  every single party. Four-party redundancy breaks the Q120 three-party result.
- **Null (refutes H1).** No four-party form tested is a pure higher-order bind; every irreducible form has
  at least one pivotal party.

The search is targeted, not exhaustive. Exact Φ on four nodes is about a second per form, so the full
16^4 = 65536 four-party symmetric family cannot be swept. The hypothesis is tested where a no-pivot bind is
most likely — the symmetric forms, where interchangeability is greatest, plus hand-built redundant
constructions. A non-symmetric rule breaks interchangeability, which makes a no-pivot bind less likely, so
a null over the symmetric and redundant forms is strong evidence even though it is not a proof over all
four-party wirings. Two knockout definitions are run (spectator P' = x[P]; silenced P' = 0); a pure
higher-order bind must hold under both.
