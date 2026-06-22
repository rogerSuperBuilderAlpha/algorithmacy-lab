# Core membership: who is in the irreducible whole, and who drops out

The fourth deep dive from the [mediated-or-irreducible paper](../../essays/mediated_or_irreducible.md),
taking Q8 from the [mediation-boundary thread](../mediation_boundary/QUESTIONS.md) twenty steps deep. The
first three dives asked whether a coordination is irreducible; this one reads the major complex as the
measure of which parties are in the irreducible whole, and maps the rules of membership. They reduce to one
principle: the core is the tightest-coupled subset, and parties compete for a place in it.

## Contents

- [`DEEP_DIVE.md`](DEEP_DIVE.md) — the twenty-step chain, each step's question drawn from the previous
  result, with the rules of membership.
- [`chain.py`](chain.py) — every computation, reproducible.

## The rules of membership

A party is in the irreducible core when it is bound both ways, reading and read, into the tightest mutual
coupling. It is shed when it is decoupled, half-coupled (an in-only observer or an out-only emitter, both
excluded), read against the grain by the mediator (the negatively-read party leaves), substitutable (pooled
parties all leave at once), a pure feedforward relay (even the mediator can be excluded, leaving the source),
or out-coupled by a more tightly bound rival. The core is one connected cycle, can shrink to a single node,
and localizes to a single link in a deep chain instead of spanning it. Mutual two-cycle coupling predicts
membership at AUC 0.72, with the determination carrying the rest, so membership sits in the cause-effect
structure like the verdict.

The whole-system commit-or-convey verdict is the special case where every party is in the core: a party
dropping out factors the whole. Membership is the finer reading beneath the verdict, naming which parties are
bound, where the verdict gives only whether the form binds.

## Why it matters

A system can contract its irreducible core to itself and its owner, and a heavy review process can push the
proposer out: the parties a coordination exists to bind can sit outside the whole it runs. The light merge
gate of [v9](../../recurrence/event_series/) holds all three parties in the core; the heavy review of
[v10](../../recurrence/review_heavy/) excludes the author. This is the membership reading of disintermediation
and capture, and it connects to the [observer](../observer/THREAD.md),
[substitutability](../substitutability/THREAD.md), and [principal](../../principal/) lines.
