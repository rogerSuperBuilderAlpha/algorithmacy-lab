# Integrated information as a cooperative game

A synthesis of ten exploratory threads that read exact IIT-4.0 integrated information as a cooperative
game on the parties of a coordination form. Each thread is a self-contained dive with its own reproducible
script; this essay states the one construction they share, the structure it reveals, what that structure
recovers from textbook game theory, and what it adds. It introduces no new computation. The threads are
listed at the end with their headline results.

## The construction

Model a coordination arrangement as a small Boolean dynamical system whose nodes are the parties — a
worker, a mediating system, a counterpart, sometimes a fourth. For any subset S of parties, the system
integrated information φ_s(S) measures how irreducible the subset's cause-effect structure is, maximized
over the states the subset can reach. Read φ_s as the worth of a coalition: v(S) = φ_s(S). The parties are
the players, and a coalition's worth is how irreducibly it coordinates.

This turns IIT's central object into a game-theoretic one. The **major complex** — the subset IIT's
exclusion postulate keeps as the locus of integration — is the subset that maximizes φ_s. In the game it
is a solution concept: the coalition that forms. The threads ask what kind of game v is, what solution
concept the major complex implements, and how the credit for the coordination's integration distributes
among the parties. The construction is a re-description of structure φ_s already has, in a language built
for exactly these questions.

## The major complex is the coalition that forms

The exclusion postulate, in coalition language, selects the maximally integrated coalition. The
coalition-structure thread confirms this directly: the major complex is the φ_s-argmax subset in every
form, up to ties. The same postulate, applied recursively — keep the maximal complex, remove it, recurse —
is a greedy generator of a coalition structure, and that structure matches the partition of maximal total
worth 88% of the time. Exclusion is a winner-take-all coalition-formation rule, near-optimal as a
structure generator and myopic in the rest.

This reading also settled a residual the program had read as deep. Single-node membership in the major
complex tracks the exact Shapley value over v at rank-AUC 0.87, not 1.0, and the gap looked structural.
Scoring each coalition by its worth across all states, rather than at the one state where the complex
forms, was the source: at the right state a node-level marginal recovers membership at AUC 0.98. The
ceiling was state aggregation.

## The mediator has three names

In a mediated triad the same party answers to three descriptions, and the game ties them together. It is
the **pivotal** party, carrying the largest Shapley value. It is the **bottleneck**, a party in every
integrating coalition — a veto player. And it is the party with **no outside option**, the platform
position. The veto reading explains the Shapley reading: a veto player carries the maximal Shapley value
by a standard theorem, so the mediator dominates the credit because every productive coalition needs it.
On the models this holds exactly — when a single bottleneck exists, it is the Shapley-argmax party in every
case.

A bottleneck is necessary for irreducible mediation and not sufficient for it. A quarter of single-
bottleneck forms are dyadic hubs: a party bridges two parties one at a time, indispensable to each pairing,
yet the three never bind into one irreducible determination. The hub conveys across two channels; the
mediator commits one. This is the dissertation's commit-versus-convey line in cooperative-game form, and it
keeps structural indispensability and committed determination as two different properties.

## Integration does not aggregate

The slogan that integrated information is supposed to make precise — the whole is more than the sum of its
parts — is, as a claim about φ_s, false. Read as superadditivity, v(S ∪ T) ≥ v(S) + v(T), it almost never
holds: 99% of forms have a disjoint split where the whole is worth less than its parts, and adding a party
to a coalition usually lowers its integration. The synergy the slogan reaches for is real only at the
bottom edge, where two parties that integrate with no one alone form an integrating dyad. Above that edge a
third party dilutes, dropping the whole below its tightest pair by more than a full unit of φ. The word the
structure supports is irreducible, not more-than-the-sum: a selected subset is irreducible, and integration
is a property that subset has, not a quantity that accumulates across a merge.

## The credit has no stable split

Subadditivity has a sharp consequence on the allocation side. If a tight pair out-values the whole, no way
of dividing the whole's worth keeps that pair in, so the core is empty. It is empty in 96% of three-party
forms and in every four-party form tested, and the Shapley value — the canonical fair split — is stable in
2%. The contestation has an exact cause: among the forms where a pair out-values the whole, the core is
empty in every one. And the bottleneck that captures the credit does not stabilize it. A veto player
guarantees a non-empty core in a monotone simple game, but this game is neither, and the guarantee fails.
The mediator holds the credit and not the peace.

Who is paid follows the same logic. In a triadic form the credit concentrates on one party — a majority of
it in 86% of forms — and the degree tracks exclusion. When all parties are in the major complex the credit
is shared; when exclusion drops a party the credit goes winner-take-all, and the dropped party's Shapley
value turns negative. A party outside the irreducible core does not merely fail to add integration. Its
presence lowers the integration of the coalitions it joins, so it is charged for the drop, and the central
party is credited past the whole's worth.

## Why the credit cannot be normalized away

A standing objection to integrated information is that Φ grows with system size and should be normalized
before systems are compared. The game says what normalizing would cost. A per-element exclusion rule keeps
the subset of largest φ_s per party, and that subset is a single party in 94% of forms and in 92% of
triadic ones, against an absolute major complex that averages well above one. Dividing by size rewards the
smallest unit, so the multi-party core the whole framework is about collapses to a point. Absolute φ_s is
what lets IIT pick out a coordination at all. The objection, run on the models, argues for the choice it
meant to question.

## Four parties, and bottlenecks that are sets

Every result above was first found on three-party forms, the smallest case with a mediated triad, and the
four-party thread checks them against the charge of being artifacts of a six-coalition lattice. They hold:
the major complex is still the argmax coalition, the game is still subadditive, a single bottleneck is
still the Shapley-argmax party, and the empty core holds more strongly. One structure appears that three
parties cannot show — a bottleneck that is a set, a group of parties each in every integrating coalition.
Inside such a set the credit is governed by the symmetry axiom and nothing softer: two co-bottlenecks are
paid identically when they are interchangeable in the game and split the credit about 0.4 to 1 when they
are not. Joint indispensability shares the reward only between parties that play the same role.

## What is recovered and what is added

Several results are textbook cooperative game theory, instantiated on these models, and their appearance is
a check that the translation is faithful rather than a discovery. A veto player carries the maximal Shapley
value; interchangeable players carry equal Shapley; a subcoalition worth more than the whole empties the
core. These had to hold, and they do, exactly.

What the program adds is the mapping and the measurements. That IIT's exclusion postulate is the argmax of
the φ_s coalition game, and condensation a greedy coalition-structure generator, is a translation of a
physical postulate into a solution concept, and it is exact on the models. That φ_s is subadditive, that
its core is almost always empty, that normalizing it collapses the major complex to a point — these are
properties of integrated information read through the game, not properties of the game alone. And the
quantitative findings are the program's own: the 0.87 membership-AUC and its diagnosis as state
aggregation, the 96% empty-core rate, the concentration of credit and its tracking of exclusion, the mix of
interchangeable and distinct co-bottlenecks. The game theory supplies the questions and the names; the
answers are facts about Φ.

## What it says for the dissertation

The cooperative-game lens grounds the dissertation's claims about mediated coordination in precise objects.
Algorithmacy — a mediating system that commits a determination both parties must heed — is a form whose
major complex binds the parties irreducibly, and the committing system is the veto player that captures the
credit and has no outside option. Commit-versus-convey is the line between the triadic mediator and the
dyadic hub, between a bottleneck that binds and one that relays. The platform's hold on value is the
mediator's Shapley dominance, and the instability of that hold is the empty core: the arrangement runs as a
process while the credit for it stays contested. None of this replaces Φ. The exploration is the
contribution — integrated information is the object, and cooperative game theory is a language that makes
the shape of that object legible and ties it to how coordination is theorized elsewhere.

## The threads

| Thread | Headline |
|--------|----------|
| [shapley_membership](../threads/shapley_membership/THREAD.md) | Major-complex membership tracks the exact Shapley value (AUC 0.87); the mediator dominates it. |
| [coalition_structure](../threads/coalition_structure/THREAD.md) | The major complex is the argmax-φ_s coalition; condensation ≈ the optimal coalition structure (88%). |
| [veto_player](../threads/veto_player/THREAD.md) | The mediator is a veto player (Shapley-argmax, 100%); a veto player is necessary, not sufficient, for an irreducible determination. |
| [subadditivity](../threads/subadditivity/THREAD.md) | Integration does not aggregate: φ_s is subadditive in 99% of forms; the slogan is false. |
| [core_stability](../threads/core_stability/THREAD.md) | The integration credit has no stable split: the core is empty in 96%, emptied by subadditive dilution. |
| [credit_concentration](../threads/credit_concentration/THREAD.md) | The credit concentrates on one party, by an amount exclusion sets; excluded parties carry negative Shapley. |
| [normalization](../threads/normalization/THREAD.md) | Normalizing φ_s collapses the major complex to one party (94%); absolute φ_s is load-bearing. |
| [four_party](../threads/four_party/THREAD.md) | The laws hold at four parties, the empty core more strongly; a bottleneck can be a set. |
| [joint_bottleneck](../threads/joint_bottleneck/THREAD.md) | A joint bottleneck captures the credit as a set and shares it among its members. |
| [bottleneck_symmetry](../threads/bottleneck_symmetry/THREAD.md) | Co-bottlenecks are paid equally exactly when interchangeable; the sharing is the symmetry axiom, bimodal. |
