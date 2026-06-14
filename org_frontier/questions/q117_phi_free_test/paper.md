# Q117 — Triadicity has a Φ-free test, and it reads the logic

## Question

The program reads the verdict with exact IIT-4.0 Φ. This asks whether a predicate computed without Φ, from
the form's truth tables alone, reproduces that verdict on the whole 256-form strict-mediation family, and
whether the feedback cycle suffices or more is needed.

## Method

The 256 strict-mediation forms (worker W, mediator S, counterpart C): each is eight bits, a 2-bit worker read,
a 2-bit counterpart read, and a 4-bit mediator table. The exact verdict (Φ over the MIP) is the ground truth.
Two Φ-free predicates are tested against it: the topology-only feedback cycle, and the cycle plus a logical
composition condition.

## Results

A Φ-free predicate matches the oracle on every form. The topology-only cycle is necessary but over-calls 16
forms; adding one logical condition closes the error to zero.

| predicate | TP | FP | FN | TN | errors |
|---|---|---|---|---|---|
| feedback cycle (topology only) | 24 | 16 | 0 | 216 | 16 |
| cycle + composition (Φ-free) | 24 | 0 | 0 | 232 | 0 |

Forty forms carry the full feedback cycle; 24 are triadic and 16 dyadic, on identical wiring.

| | result |
|---|---|
| H1 the feedback cycle is necessary | confirmed (0 false negatives) |
| H2 the feedback cycle is not sufficient | confirmed (16 false positives) |
| H3 the cycle-plus-logic predicate matches the oracle exactly | confirmed (0 errors) |
| H4 identical-wiring forms split on the verdict | confirmed (24 vs 16) |

## Interpretation

The feedback cycle is a real necessary condition. Every triadic form carries it: the mediator depends on both
outer parties, and both outer parties depend on the mediator. Break any of those four edges and the form is
dyadic, without exception across the family. The cycle is also cheap, read off which inputs each truth table
uses, so a necessary screen for triadicity needs no Φ.

The wiring leaves the verdict undecided. Of the 40 forms that carry the full cycle, 24 are triadic and 16 are
dyadic, and the two classes share the identical connectivity diagram: the same parties, the same edges, the
same directions of influence. A connectivity check would call all 40 triadic and miss on 16. Whatever
separates the triadic forms from the dyadic ones is not in the graph, because the graph is the same on both
sides.

It is in the logic of the determination. A predicate that adds one composition condition to the cycle matches
the oracle on all 256 forms with zero error. A parity mediator binds the cycle whenever it is present; a
non-parity mediator binds iff the outer reads' phase alignment composes coherently with the mediator's
symmetry. When the reads reinforce the mediator's joint dependence, the determination is irreducible; when
they cancel it, one outer party becomes redundant and the form factors along a party line. The deciding
property is the composition of the reads with the mediator's function, a logical fact, not a topological one.

The open question resolves to a qualified yes. A Φ-free necessary-and-sufficient test for triadicity exists on
this family, so the exact oracle is replaceable here by a closed-form predicate, and the classifier can be
made cheap and exact at once. The qualification is that the test reaches past the pure connectivity law one
might have wanted: topology gives only the necessary half, and the sufficient half must read the truth tables. The
result confirms IIT's own claim in passing, that integration is a property of the mechanisms, not of the
wiring they ride on, by exhibiting forty forms of one wiring that the mechanisms split in two.

## Limitations

In-silico; the exact IIT-4.0 verdict over the MIP is the ground truth. The 256 forms fix a single topology
(the mediator reads both outer parties; each outer party reads only the mediator); generalization to other
n=3 forms is Q118. The composition condition is validated against the oracle on the complete family, not
derived from the IIT axioms; a derivation would make it a theorem.
