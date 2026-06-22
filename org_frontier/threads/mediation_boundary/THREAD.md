# The mediation boundary: when a committing mediator binds, and the co-monotonicity law

A deep dive into the structure of the irreducibility boundary, derived from the
[mediated-or-irreducible paper](../../essays/mediated_or_irreducible.md). It develops ten research
questions, ranks them, and takes the top one twenty steps deep, each step's question drawn from the
previous step's result. The headline finding is a sharp rule for the mediator's determination: a system
binds a coordination into a strong irreducible whole exactly when it depends on every party in the same
monotone direction, and a single party read against the grain factors the whole and drops that party from
the core.

## Contents

- [`QUESTIONS.md`](QUESTIONS.md) — ten research questions from the paper, scored on centrality,
  tractability, depth, and novelty, with the top one chosen for the deep dive.
- [`DEEP_DIVE.md`](DEEP_DIVE.md) — the twenty-step chain on Q3, the structure of the boundary, with the
  boundary map and the connections to the lab's findings.
- [`chain.py`](chain.py) — every computation in the chain, reproducible.

## The law, in one statement

The mediator's determination decides the verdict in the configuration that matters, where the parties
faithfully read the mediator. A determination that depends on every party in the same monotone direction
(all-increasing or all-decreasing) binds them into a bipartition-irreducible whole, Φ = 2 at three nodes
and 3 at four. A mixed-direction dependence factors the whole and excludes the against-the-grain party. A
parity dependence binds only weakly, against the full atomization. The split is invisible to connectivity
and reachable states; it lives in the cause-effect structure exact Φ computes.

Three things qualify the law. Substitutability overrides it: a co-monotone but pooled gate (OR, or
majority) still factors, so all-required AND binds while any-of-many factors. The strong co-monotone value
is fragile to perturbation while the weak parity verdict is robust, two different measures of distance to
the boundary. And the law depends on liveness: it holds when the parties track the mediator and dissolves
under arbitrary downstream reads, which ties the mediator's contribution to the downstream condition the
eight structural findings already named.

## A testable prediction

A real merge gate of positive, all-required conditions (opened and approved and merged) is co-monotone,
which is why [v9](../../recurrence/event_series/)'s elicited merge triad measured Φ = 2. A governance gate
built on a veto, a negative blocking condition, is mixed and leaves the blocker outside the core. The
[field protocol](../../field/PROTOCOL.md) could check this on a real organization: approval-by-positive
constitutes a triad, block-by-veto leaves the blocker out.
