# Thread — conflict integrates like cooperation; only disengagement breaks it

A prior for the catalog. Does it matter whether the two parties agree or conflict in how they respond to the
mediator? It does not. A party that responds by agreeing and one that responds by doing the opposite bind
into the coordination identically — the same commitment rate, the same credit split. Only a party that does
not respond at all, that ignores the mediator, fails to bind. What binds a party is that it heeds the
mediator, not that it agrees with it. Reproduce with
`python org_frontier/threads/conflict/conflict.py`.

## Setup

The worker copies the mediator, and the counterpart's response is varied: it agrees with the mediator, it
conflicts by doing the opposite, or it ignores the mediator with a constant rule. For each, the mediator's
gate is ranged over all sixteen Boolean functions of the two parties. The measures are how many of those
gates commit and the mediator's credit share.

## The arc

**Agreement and conflict bind the same.** When the counterpart agrees with the mediator, six of the sixteen
gates commit and the mediator's share is 0.556. When the counterpart conflicts, doing the opposite of the
mediator, the figures are identical: six gates commit, share 0.556. An adversarial party that tracks the
mediator in order to oppose it is bound into the coordination exactly as a cooperative one that tracks it to
agree. The sign of the response carries no weight, because reversing a party's output is a relabeling the
integration does not see.

**Ignoring the mediator breaks the bind.** When the counterpart ignores the mediator with a constant rule,
none of the sixteen gates commit. A party that does not respond at all is coupled to nothing, and the triad
cannot form. The line is not between agreement and conflict but between responding and not responding.

## What the thread establishes

Conflict integrates like cooperation, and only disengagement breaks the coordination. A party that heeds the
mediator binds whether it agrees or opposes, with the same commitment and the same credit; a party that
ignores the mediator never binds. As a prior for reading real coordination: an adversarial relationship, so
long as the parties track one another, should read as irreducible exactly as a cooperative one does, and the
thing that takes a party out of the coordination is not opposition but indifference. Whether parties get
along is invisible to the integration; whether they respond to one another is everything.

## Limits, honestly

The agree-equals-conflict result is a symmetry — Φ is invariant to flipping a node's output convention — so
it is exact rather than a measured near-equality, and the substance is its pairing with the constant case,
which separates responding from not. The party responses are fixed simple rules and the mediator ranges over
its full gate space, so the gate axis is complete while the response axis is three chosen points. Everything
is in-silico, and a prior is to be tested against data.
