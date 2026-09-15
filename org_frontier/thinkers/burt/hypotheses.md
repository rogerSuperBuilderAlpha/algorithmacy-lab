# Burt — Stage 3 hypotheses (fixed before computing)

## The rendering that all five share

A **broker** (ego, E) is a node that reads its contacts and that its contacts read. Burt's two benefits are
two rules for E. The **information broker** combines nonredundant contacts — E' = AND of contacts — since the
benefits of contacts across a hole are "additive rather than overlapping." The **control broker** chooses
between substitutable contacts — E' = OR of contacts — since the tertius can "play their bids against one
another": either will do. A **contact** reads E, and reads any contact it is tied to, disjunctively: X' = OR
of its sources (information from any source suffices). A **tie between contacts** (closure by cohesion) adds
a source to each. A contact that reads nothing is a constant.

**Value added** by a party, V(E), is the Φ of the major complex of the whole minus the Φ of the major complex
of the network with E and its edges deleted. This is Burt's own phrase for the broker's contribution
("brokerage across structural holes is the source of value added") and the lab's quantity for it.
**Membership** is whether E is in the major complex. **Constraint** C_E is Burt's aggregate constraint with
p_ij = 1/degree(i) on the undirected tie graph.

## H1 — Closure removes the broker, for both benefits (C1, C3)

- **H1 (Burt).** For the information broker and the control broker alike, a tie between the two contacts
  removes E from the core, or drives V(E) to zero.
- **H0.** One of the two brokers stays in the core with V(E) > 0 under closure.
- **Lab prior.** Against Burt on the information broker: q214 (probe #368) classified the conjunctive
  combiner *intrinsic* — it stays in the core when the bypass opens — and the relay *contingent*. The two
  benefits are expected to have different structural standing, which Burt's "the same holes generate both"
  denies.

## H2 — Structural equivalence is redundancy (C2)

- **H2 (Burt).** When E's two contacts read the same source Z and not each other, the core holds at most one
  of them, and V(E) equals what E adds with a single contact; when they read different sources, the core
  holds both.
- **H0.** Both structurally equivalent contacts are in the core with V(E) above the single-contact value.
- **Lab prior.** With Burt on eviction: exact duplicates have read as one (Latour H2, probe #390, evicted a
  delayed copy).

## H3 — Advantage falls with constraint (C4, graded)

- **H3 (Burt).** Over ego networks of three contacts with 0, 1, 2 (path), and 3 (triangle) ties among them,
  V(E) for the information broker is strictly decreasing in Burt's aggregate constraint C_E.
- **H0.** V(E) is non-monotone or increasing in C_E.
- **Lab prior.** Open. Mutual ties among contacts raise the contacts' own Φ (Simmel H2, probe #370: cliques
  bind at n(n−1)), which subtracts from V(E); whether the whole's Φ rises faster is not known.

## H4 — A hole at your own end: the rival broker (C4)

- **H4 (Burt).** A second broker R reading the same two contacts and read by them removes E's autonomy: V(E)
  with the rival is below V(E) without it, and E and R are not both in the core.
- **H0.** V(E) unchanged, or both brokers in the core.
- **Lab prior.** With Burt on V(E). Open on membership: two identical brokers may both be evicted, one, or
  neither.

## H5 — Closure within, brokerage beyond (C5)

- **H5 (Burt).** For a broker E in a group {E, A₁, A₂} with one outside contact O, V(E) is highest in the
  configuration with a tie inside the group (A₁–A₂) and a hole to O, against three others: no ties, closure
  across the hole (O tied to an insider), and closure everywhere.
- **H0.** Another configuration maximizes V(E), or the maximum is tied.
- **Lab prior.** Open.

## Not tested here

Access, timing, referrals; efficiency and effectiveness; the vision mechanism; the market-level theory
(`exegesis.md`).
