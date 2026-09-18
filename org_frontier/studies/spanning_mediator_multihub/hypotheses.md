# spanning_mediator_multihub — hypotheses (fixed before computing)

**Question (agenda #20 / extends q145).** Does an extra top mediator that spans
the hubs of a symmetric multi-hub raise Φ beyond the pool ceiling (#119), or
recreate the shared-mediator merge pattern from `two_triad_shared_member`?

**Already known (cited, not reopened).**
- **q145:** a fully spanning single mediator holds the whole set; Φ = n−1 at
  full span; partial span caps at span+1.
- **#119 / `sym_multihub`:** Φ rises with hub count toward the all-required
  **pool** ceiling (pool Φ = 12 at n=4, 20 at n=5).
- **`two_triad_shared_member`:** shared-mediator AND merges two triads into one
  five-node major complex at **Φ = 4.0**; shared leaves do not.
- **`mediator_hierarchy_census`:** recurrent closure spans levels; feedforward
  hub chains stay top-local. Ternary TOOLING_GAP / residual-cascade noted only.

**Gap.** q145 spans parties under a single hub. #119 approaches the pool by
adding *peer* hubs. Neither tests a **hierarchy-of-hubs** move: one top mediator
that reads the multi-hub layer. Shared-mediator merge is a flat shared-S, not a
spanning top atop hubs.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n ≤ 5 (exact-Φ feasible).
Primary base: `sym_multihub` with m=2 hubs. Primary add-on: one top T.

## Architectures

| cell | construction |
|---|---|
| pool(n) | each node = AND of all others (ceiling) |
| mh(n,m) | `sym_multihub` — hubs AND parties+other hubs; parties AND hubs |
| span_recurrent | T' = AND(hubs); each hub also reads T; parties AND hubs |
| span_ff | T' = AND(hubs); hubs/parties unchanged (feedforward top) |
| span_full | T' = AND(hubs+parties); hubs and parties also read T |
| shared_S_AND | two-triad shared-mediator AND (merge reference) |

**Primary contrast cell:** span_recurrent 2 hubs + 2 parties (n=5) vs pool(5)
vs mh(5,2) vs shared_S_AND.

## H1 — instrument + known ceilings

Faithful triad control. pool(4) core Φ = 12; pool(5) core Φ = 20.
shared_S_AND: full five-node core at Φ = 4.0 (replicates merge reference).

## H2 — multi-hub sits below the pool

At n=4, mh(4,2) core Φ < pool(4). At n=5, mh(5,2) core Φ < pool(5).

## H3 — spanning top does not beat the pool

On every spanning cell at total size n ∈ {4,5}, core Φ ≤ pool(n). Null: any
spanning cell exceeds the same-n pool.

## H4 — recurrent hub-span merges membership (merge analogy)

On span_recurrent 2h2p (n=5), the major complex includes T, both hubs, and at
least one party (hubs+leaves enter with the top). Null: T excluded, or no
party in the core.

## H5 — feedforward top does not enter the complex

On span_ff 2h2p (n=5), T is absent from the major complex (top fails to bind
under feedforward-only read). Null: T ∈ core.

## H6 — full span can reach, not exceed, the pool

On at least one span_full cell (2h1p n=4 or 3h1p n=5), core Φ equals pool(n)
and the core is the full node set. Combined with H3: full span saturates the
ceiling without breaking it.
