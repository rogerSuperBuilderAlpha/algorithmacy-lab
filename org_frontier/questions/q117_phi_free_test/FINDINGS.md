# Q117 findings — triadicity has a Φ-free test, but it reads the logic, not the wiring

All four hypotheses confirmed. A predicate computed without Φ reproduces the exact IIT-4.0 verdict on all 256
strict-mediation forms with zero error. The feedback cycle is necessary but not sufficient: 40 forms share
the same full-cycle wiring, yet 24 are triadic and 16 dyadic, and only a logical condition on the truth
tables tells them apart. Topology screens the verdict; logic decides it.

| predicate | TP | FP | FN | TN | errors |
|---|---|---|---|---|---|
| feedback cycle (topology only) | 24 | 16 | 0 | 216 | 16 |
| cycle + composition (Φ-free) | 24 | 0 | 0 | 232 | 0 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | the feedback cycle is necessary (no triadic form lacks it) | confirmed (0 false negatives) |
| H2 | the feedback cycle is not sufficient (cyclic dyadic forms) | confirmed (16 forms) |
| H3 | the cycle-plus-logic predicate matches the oracle exactly | confirmed (0 errors / 256) |
| H4 | identical-wiring forms split on the verdict | confirmed (24 triadic vs 16 dyadic) |

From `probe_phi_free_test.py`. The 256 forms hold 24 triadic and 232 dyadic.

## What it says

The feedback cycle is a necessary screen. Every one of the 24 triadic forms carries the full effective cycle:
the mediator depends on both outer parties, and both outer parties depend on the mediator (H1). A form that
breaks any of those four edges is dyadic without exception. So the cycle is a real necessary condition, and a
cheap one, computable from which inputs each truth table uses, with no Φ.

The cycle falls short of sufficiency, and the gap is wide. Of the 40 forms that carry the full cycle, only 24
are triadic; the other 16 carry the identical wiring diagram and are dyadic (H2, H4). A connectivity check
would call all 40 triadic and be wrong on 16. The verdict floats free of the graph: forms with the same
parties, the same edges, and the same directions of influence land on opposite sides of the line. Whatever
decides the verdict lies outside the wiring.

It is in the logic. A Φ-free predicate that adds one composition condition to the cycle matches the oracle on
every form, with zero error across all 256 (H3). The condition reads the truth tables: a parity mediator
(XOR or XNOR) binds the cycle whenever it is present, and a non-parity mediator binds iff the outer reads'
phase alignment matches the mediator's symmetry under swapping its inputs. Where the two outer parties copy
the mediator with phases that compose coherently with its logic, the determination is irreducible; where the
phases cancel that logic, one party becomes redundant and the form factors. The deciding property is the
composition of the reads with the mediator's function, a logical fact about the determination.

This answers the open question with a qualified yes. A Φ-free necessary-and-sufficient test for triadicity
exists on the strict-mediation family, so the exact-Φ oracle is replaceable here by a closed-form predicate.
But the test reaches past the connectivity law one might have hoped for. Topology gives only the necessary
half; the sufficient half is logical, and reading it requires the truth tables beyond the graph. The classifier can
be made cheap on this family, and the structural law has a closed form, yet the form confirms IIT's deeper
claim: integration is a property of the mechanisms, not of the wiring they ride on.

## Caveats

- **Confirmatory.** All four predictions held; the genuinely uncertain claim, H3 (that a Φ-free predicate
  matches exactly), resolved to zero error. The composition condition was found by inspecting the family and
  could have failed on some form; it did not.
- **One family.** The 256 strict-mediation forms fix the topology to a single mediator reading both outer
  parties, with each outer party reading only the mediator. Whether the predicate generalizes to forms where
  the mediator reads one party, or to a broader n=3 sample, is Q118.
- **Discovered, not derived.** The composition condition is validated against the oracle on the complete
  family, short of a proof from the IIT axioms. A derivation would turn the test into a theorem.
- **Exact Φ throughout.** The ground truth is the exact IIT-4.0 verdict over the MIP. In-silico.
