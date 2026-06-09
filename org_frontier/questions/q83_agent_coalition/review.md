# Q83 — Stage 1 review: a recipient-side gating coalition

## The question

A recipient may run several agents that jointly gate which messages reach it. This study asks whether two
recipient-side gating agents both join the irreducible core when delivery requires both of them, mirroring
the regulator-coalition result where two weak regulators enter the core only when both gate the commit.
Parties: sender E, message M, recipient R, gating agents T1, T2.

## What the lab already knows that bears on this

- **A single bidirectional triage agent joins the core and displaces the sender (Q68, probe 232).** The
  one-agent baseline.
- **A regulator coalition enters only under joint gating (probe 111).** Two observe-only regulators stay
  out; only when both regulators' approval gates the commit do they enter, growing the core to {W,S,C,R1,R2}
  at Φ=4.0. This study tests whether a recipient-side gating coalition behaves the same way.
- **Substitutability collapses participation (Finding 5, Q70).** A substitutable gate (either agent
  suffices) should leave the agents outside the core.

## The gap

The regulator coalition gates the mediator's commit; a recipient-side coalition gates the recipient's
input. Whether two required recipient-side agents both enter the core, as the regulators do, is uncomputed.
No prior probe builds the recipient-side gating coalition, so the question is open.
