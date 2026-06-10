# Q92 findings — a tracking memory substitutes for a live read, and reorganizes the core

All four hypotheses confirmed. A mediator that reads a memory tracking the recipient keeps the triad, so
liveness is about the recipient being bound through some path, not read at the current step. A
memory that does not track the recipient, or a mediator reading only its own past, collapses the form.

| form | whole-system | Φ | major complex |
|---|---|---|---|
| live | triadic | 2.00 | {E, M, R} |
| tracking memory | triadic | 2.00 | {M, R, Mem} |
| frozen memory | dyadic | 0.00 | {E, M} |
| self memory | dyadic | 0.00 | {E, M} |

| H | Result | Verdict |
|---|--------|---------|
| H1 | a tracking memory preserves the triad | confirmed |
| H2 | a frozen memory collapses to dyadic | confirmed |
| H3 | self-memory alone is dyadic | confirmed |
| H4 | the tracking memory node is in the core | confirmed |

From `probe_stateful_mediator.py`.

## What it says

A memory that tracks the recipient substitutes for a live read of it. When the mediator reads a memory
holding the recipient's previous value, rather than the recipient directly, the form stays triadic at
Φ = 2.0 (H1). The one-step delay does not break the binding, so the relay-gap collapse of Q65 does not
apply here: a memory that faithfully tracks the recipient keeps it bound, where a relay that gates or
delays without tracking would not. Liveness, in the sense Finding 3 needs, is the recipient being bound
into the determination through some path, and a tracking memory is such a path.

The core reorganizes when the memory enters. The live triad's core is {E, M, R}; the tracking-memory
triad's core is {M, R, Mem}, with the memory in (H4) and the worker displaced. The memory becomes the
party that carries the recipient's constraint into the mediator, and in doing so it takes the worker's
place in the irreducible set. Adding memory does not merely preserve the triad; it changes which parties
are bound into it, the way recipient-side delegation reorganized the core in Q68.

The controls collapse as predicted. A frozen memory, which does not track the recipient, leaves the
recipient unbound and the form dyadic (H2): a stored value substitutes for a read only while it tracks. A
mediator reading the worker and its own past, with the recipient feeding nothing, is dyadic (H3): a
mediator's history does not manufacture a triad without the recipient. Memory binds a party only when it
carries that party's current information.

## Caveats

- **Confirmatory.** All four predictions held.
- **In-silico.** Boolean models, exact Φ and major complex. The memory is a single one-step buffer; deeper
  memories and memories with their own noise are untested.
- **Core displacement.** The worker leaving the core when the memory enters is read on the major complex; a
  fuller account would track why the memory displaces the worker instead of joining a larger core, which
  this study does not pursue.
