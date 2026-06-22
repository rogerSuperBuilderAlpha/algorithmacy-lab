# Who is in the irreducible core — twenty steps deep

Q8 from the [mediation-boundary thread](../mediation_boundary/QUESTIONS.md), taken twenty steps deep. The
first three dives asked whether a coordination is irreducible. This one asks which parties are in the
irreducible whole when it is, reading the major complex as the lab's measure of membership, and maps the
rules that put a party in the core or push it out. The arc reaches a single principle: the core is the
tightest-coupled subset, and parties compete for a place in it. Each step's question is drawn from the
previous step's result; every number reproduces from [`chain.py`](chain.py).

## The chain

**1 — The baseline and the first exclusions.** Question: from a full triad, what drops a party out? The
committing triad S = W ∧ C holds all three in the core. A party read against the grain (S = W ∧ ¬C) leaves,
and a decoupled party leaves; in both the core is the remaining pair. → Does a party need to be coupled in
both directions?

**2 — Bidirectional coupling is required.** Question: is a half-coupled party in the core? No. Add a fourth
node that reads the mediator but is unread, an observer, and it stays out; add one that is read but reads
nothing, an emitter, and it stays out too. Both half-coupled nodes are excluded, the core staying the
fully-coupled triad. A party must both read and be read to belong. → What happens to parties that are
interchangeable?

**3 — Substitutable parties all leave.** Question: when two parties are pooled, does one stay as a
representative? Neither stays. S = W ∧ (C ∨ D) drops both C and D, the core shrinking to the worker-mediator
pair. Substitutability excludes every pooled party at once. → Does the core grow as a coordination deepens?

**4 — The core localizes to a link.** Question: in a chain, is the whole chain in the core? No. The chain
W to S1 to S2 to C is irreducible at Φ = 2, but the core is a single adjacent pair, S2-C. Depth preserves
irreducibility without growing the core; the binding concentrates in one link. → Which party leaves when a
coordination routes through gates?

**5 — The proposer is excluded.** Question: under a review-and-merge structure, is the author in the core?
No. The four-role review model, author then reviewer then merger then codebase, has a core of reviewer,
merger, codebase, and leaves the author out. The party that proposes a change is not part of the bound whole
that decides it, the structural face of v10. → Can the mediator itself be excluded?

**6 — Even the mediator can leave.** Question: is the mediator always in the core? No. A pure relay, where
the mediator only passes a signal along, has a core of the single source node. Membership is about being in
a cycle, not about playing the mediating role. → Can an outside party take a core seat from the originals?

**7 — A coupled principal seizes the core.** Question: can a fourth party displace the worker and
counterpart? Yes. A principal coupled to the mediator both ways, reading and read, contracts the core to the
mediator-principal pair, dropping the worker and counterpart the system coordinates. The parties a system is
built to bind can be displaced from the bound whole. → Is membership predictable from the wiring?

**8 — Mutual coupling predicts membership.** Question: does a node's two-way coupling forecast its place in
the core? Moderately. Across random forms a node's mutual, two-cycle coupling separates the in-core from the
out-of-core at AUC 0.72, better than chance and short of certain, with the determination carrying the rest.
→ When does the core shrink to a single node?

**9 — The minimal core is one node.** Question: how small can the core get? A single node, the source of a
relay or a self-looping node otherwise cut off. The smallest irreducible whole is one element, and a
coordination can have its binding sit entirely in a part of itself. → Which specific party leaves under an
adverse gate?

**10 — The against-the-grain party leaves.** Question: when a mediator reads one party in the opposite
direction, which party drops? That one. S = W ∧ ¬C drops C; S = ¬W ∧ C drops W. The mediator binds the
parties it reads with the grain and sheds the one it reads against. → Is the core ever two disconnected
pieces?

**11 — Displacement has a sharp threshold.** Question: how strongly must an outside party couple to take a
seat? Enough to out-couple the incumbents. Turning a principal's coupling up as a continuous knob, it joins
the core only at full strength and not before, so membership has a threshold and the contest is won by
coupling more tightly than the parties already in. → What shape does the seized core take?

**12 — The core is one connected cycle.** Question: can the major complex span disconnected parts? No. With
a worker-mediator two-cycle and a separate self-looping counterpart, the core is the connected pair and the
self-loop stays out. The complex is one connected tightest cycle, not a union of pieces. → What does
membership say about governance?

**13 — Governance moves the proposer in or out.** Question: does the review process change who is bound? It
does. The light merge gate, opened and merged with the worker positive, holds all three in the core. The
heavy review gate, with a distinct reviewer approval, excludes the author. A heavier process structurally
pushes the proposer out of the bound whole. → How does membership relate to the verdict?

**14 — The whole verdict needs the full core.** Question: does a partial core still read as committing? Not
generically. Across random forms a core of all parties carries a high whole-system Φ, while a smaller core
carries near zero: a party dropping out factors the whole. The triadic verdict is the full core, and
membership is the finer reading underneath it. → What is the principle behind all of this?

**15 — The tightest-coupled subset wins.** Question: is there one rule? There is. Every exclusion is a case
of it: the decoupled, the half-coupled, the against-the-grain, the substitutable, and the displaced parties
are the ones outside the tightest mutual coupling, and the core is the subset bound most tightly to itself.
Membership is a competition, and the winners are the closely-coupled. → What does this add beyond the
verdict?

**16 — Membership is the finer reading.** Question: what does the core say that the verdict does not? It
says which parties are bound, not only whether the form binds. Two committing forms can bind different
subsets, and a form can be irreducible in a part while a party it nominally includes sits outside. The
verdict is one bit; membership names the bound. → Can the wiring alone give it?

**17 — The wiring gives most of it.** Question: is exact Φ needed for membership? For most of it the wiring
suffices, mutual coupling reaching AUC 0.72, and the rest needs the determination, since the same
connectivity can bind or shed a party by its function alone, as the against-the-grain case shows. Membership
sits in the cause-effect structure, like the verdict. → What does displacement mean for a real coordination?

**18 — Parties drop out of their own coordination.** Question: who can a real arrangement exclude? The
parties it exists to coordinate. A heavily-coupled principal contracts the core to itself and the system; a
heavy review process excludes the author. The worker can be outside the irreducible whole that the system
runs, which is the membership reading of disintermediation and capture. → What is the whole map?

**19 — What membership adds.** Question: why read the core at all? Because the verdict says a coordination
binds and the core says whom. It distinguishes the committing triad that binds all three from the one that
binds a pair and sheds the third, and it locates where in a deep or owned arrangement the binding actually
sits. → What are the rules, together?

**20 — The rules of core membership.** A party is in the irreducible core when it is bound, both reading and
read, into the tightest mutual coupling, and out of it when it is decoupled, half-coupled, read against the
grain, substitutable, a feedforward relay, or out-coupled by a rival. The core is one connected cycle, can
shrink to a single node, localizes to a link in a chain, needs the full set of parties for the whole to read
as committing, and is predicted by mutual coupling at AUC 0.72 with the determination carrying the rest. The
parties a system is built to coordinate can be displaced from the whole it runs.

## What the dive establishes

Core membership has rules, and they reduce to one: the irreducible core is the tightest-coupled subset, and
parties compete for it. A party belongs when it is bound both ways into that subset and is shed when it is
decoupled, half-coupled, read against the grain, substitutable, a relay, or out-coupled by a more tightly
bound rival. The core is one connected cycle, as small as a single node, and localized to a link in a deep
chain. The whole-system verdict is the special case where every party is in the core, so membership is the
finer reading beneath the binary commit-or-convey, naming which parties are bound rather than whether the
form binds. The governance consequence is sharp: a system can contract its irreducible core to itself and
its owner, or push the proposer out under heavy review, so the parties a coordination exists to bind can sit
outside the whole it runs.

## Connections

The dive answers Q8 and ties to the others. The against-the-grain exclusion is the membership face of dive
1's co-monotonicity law, and the displacement threshold echoes dive 2's continuous margin. Membership is
what dive 3's mediator-centrality recovered behaviorally at AUC 1.00. The exclusions connect to the
[observer](../observer/THREAD.md) thread (the half-coupled spectator), the
[substitutability](../substitutability/THREAD.md) thread (the pooled party), the
[principal](../../principal/) study (the coupled owner that seizes the core), and the real-data governance
of [v9](../../recurrence/event_series/) and [v10](../../recurrence/review_heavy/).
