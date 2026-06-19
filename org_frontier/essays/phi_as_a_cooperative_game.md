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
exclusion postulate keeps as the locus of integration — is the subset that maximizes φ_s, the argmax of
the characteristic function. The threads ask what kind of game v is, how the major complex sits in it, and
how the credit for the coordination's integration distributes among the parties. The construction is a
re-description of structure φ_s already has, in a language built for exactly these questions.

Two scope conditions govern everything below, and both qualify the numbers. First, **the forms are random
Boolean truth tables** — each node's update rule is drawn by independent coin-flips — sampled for coverage,
not a model of any organizational population. Every percentage here is a frequency over that distribution,
and a uniform-random Boolean network is generically near-chaotic or near-constant; coordination forms are a
structured corner of the space. The rates are properties of φ_s on a coverage sample, and they move with
the population. A prior study in the program, [q122](../questions/q122_game_validity/paper.md), audited the
same value function on the *structured* coordination forms the dissertation actually uses and returned a
split verdict: there the game was monotone and superadditive with zero violations, the opposite of the
random-form behavior reported below. Where the two populations disagree, the structured one carries the
dissertation's claims. Second, **the singleton convention is not uniform across the threads**: the
membership game scores a lone party at zero, the allocation games at the party's intrinsic φ. Several
results below depend on which, and the text flags it where it bites.

## The major complex is the coalition that forms

The exclusion postulate, in coalition language, selects the maximally integrated coalition: the major
complex is the φ_s-argmax subset, up to ties, in every form. This is near-definitional, since IIT defines
the major complex as the subset of maximal φ_s, so the 100% is a consistency check that the translation
v(S) = φ_s(S) is faithful. The empirical content sits in the next step. The same postulate
applied recursively — keep the maximal complex, remove it, recurse — is a greedy generator of a coalition
structure, and that structure matches the partition of maximal total worth 88% of the time, near-optimal
and myopic in the rest. The argmax of a set function is not itself a named cooperative-game solution
concept; the clean object here is the correspondence between exclusion and argmax selection, and between
condensation and greedy coalition-structure generation.

This reading also settled a residual the program had read as deep. Single-node membership in the major
complex tracks the exact Shapley value over v at rank-AUC 0.87, not 1.0, and the gap looked structural.
Scoring each coalition by its worth across all states, instead of at the one state where the complex
forms, was the source: at the right state a node-level marginal recovers membership at AUC 0.98. The
ceiling was state aggregation.

## The mediator has three names

When a form has a single bottleneck — a party in every integrating coalition — that party answers to three
descriptions at once, and the game ties them together. It is the **pivotal** party, carrying the largest
Shapley value. It is the **bottleneck** itself, a veto player. And it sits where a platform sits, with **no
outside option** for the others. The standard theorem that a veto player carries the maximal Shapley value
is about simple or monotone games and a party in every *winning* coalition; this game is neither simple nor
monotone, and the bottleneck is defined over *integrating* coalitions, so the theorem motivates the question
but does not apply. The result is therefore empirical, not deductive: when a single bottleneck exists, it is
the Shapley-argmax party in every form found, 115 of 115. The motivating intuition holds, and the proof that
would guarantee it does not transfer.

A bottleneck is necessary for irreducible mediation and not sufficient for it. A quarter of single-
bottleneck forms are dyadic hubs: a party bridges two parties one at a time, indispensable to each pairing,
yet the three never bind into one irreducible determination. The hub conveys across two channels; the
mediator commits one. This is the dissertation's commit-versus-convey line in cooperative-game form, and it
keeps structural indispensability and committed determination as two different properties.

## Integration does not aggregate

The slogan that integrated information is supposed to make precise — the whole is more than the sum of its
parts — has a wrong formalization that is worth ruling out. Read as superadditivity, v(S ∪ T) ≥ v(S) + v(T),
it almost never holds on these random forms: 99% have a disjoint split where the whole is worth less than
its parts. Two caveats keep this from being a refutation of IIT. The sum v(S) + v(T) is inflated by scoring
each lone party at its intrinsic φ, and comparing φ across system sizes is a comparison IIT itself treats as
not meaningful, so part of the subadditivity is a bookkeeping choice rather than a fact about integration.
And IIT never claimed φ is superadditive: it cashes out "more than the sum of the parts" as irreducibility,
φ > 0 for the whole, not as φ_whole > Σφ_parts. So the finding concerns the formalization: superadditivity
is the wrong reading of the slogan. The synergy the slogan reaches for is real at the bottom edge,
where two parties that integrate with no one alone form an integrating dyad. Above that edge a third party
dilutes, dropping the whole below its tightest pair. The word the structure supports is irreducible: a
selected subset is irreducible, and integration
is a property that subset has, not a quantity that accumulates across a merge.

## The credit has no stable split

The empty core, the credit concentration below, and the subadditivity above are one mechanism seen three
times: φ_s does not aggregate across a merge, so a tight subset out-values the whole that contains it. On
the allocation side this is sharp. If a pair out-values the whole, no way of dividing the whole's worth
keeps that pair in, so the core is empty — in 96% of three-party random forms and in every four-party random
form tested, with the Shapley value stable in 2%. The cause is exact: among the forms where a pair
out-values the whole, the core is empty in every one, which is the dilution restated as a blocking pair, not
a second finding. And the bottleneck that captures the credit does not stabilize it. A veto player
guarantees a non-empty core in a monotone simple game; this game is neither, and the guarantee fails. The
mediator holds the credit and not the peace.

Who is paid follows the same mechanism. In a triadic form the credit concentrates on one party — a majority
of it in 86% of random forms — and the degree tracks exclusion. When all parties are in the major complex
the credit is shared; when exclusion drops a party it goes to one, and the dropped party's Shapley value
turns negative. A party outside the irreducible core lowers the integration of the coalitions it joins, so
its marginal contribution is below zero, and the central party is credited past the whole's worth to balance
the books. This is the same dilution again, now read as a payment.

## Normalizing exclusion, and what it would cost

A standing objection to integrated information is that Φ grows with system size and should be normalized
before systems are compared. A per-element exclusion rule keeps the subset of largest φ_s per party, and on
these forms that subset is a single party in 94% of cases, against an absolute major complex that averages
above one. The mechanism is mundane: dividing by size rewards the smallest unit, so a lone party with
intrinsic φ wins the per-element contest. The control settles how much this is about coordinations. Forbid
singletons and score density over coalitions of two or more, and the per-element and absolute rules agree in
91% of forms — the collapse is the lone party winning, not a re-ranking of multi-party coordinations. So the
claim this supports is narrow: per-element normalization, applied across the whole lattice, lets a single
element win on density, and absolute φ_s avoids that. The literature's normalization critique is about large
systems where un-normalized Φ assigns high values to intuitively inert grids, a regime these three- and
four-node models do not reach, so this is a small point in its favor, not an answer to it.

## Four parties, and bottlenecks that are sets

Every result above was first found on three-party forms, the smallest case with a mediated triad, and the
four-party thread checks them against the charge of being artifacts of a six-coalition lattice. They hold on
the fifty four-party forms tested: the major complex is still the argmax coalition, the game is still
subadditive, a single bottleneck is still the Shapley-argmax party, and the empty core holds in every one.
One structure appears that three parties cannot show — a bottleneck that is a set, a group of parties each in
every integrating coalition. The frequencies here rest on small single-seed samples — a joint bottleneck
turned up in one of fifty forms, and the within-set sharing is measured over twenty-two veto pairs — so the
counts are unstable and only the qualitative shape is claimed. Inside such a set the credit splits two ways,
governed by the symmetry axiom: two co-bottlenecks are paid identically when they are interchangeable in the
game, a theorem, and split it unevenly, around 0.4, when they are not. The mix of the two regimes is roughly
even in the sample but its rate is a small-sample estimate. Joint indispensability shares the reward only
between parties that play the same role.

## What is recovered and what is added

Several results are textbook cooperative game theory, instantiated on these models, and their appearance is
a check that the translation is faithful rather than a discovery. A veto player carries the maximal Shapley
value; interchangeable players carry equal Shapley; a subcoalition worth more than the whole empties the
core. These had to hold, and they do, exactly.

What the program adds, stripped of the recovered theorems and the near-definitional argmax identity, is
narrower than the list of threads suggests. The subadditivity, the empty core, and the credit concentration
are one mechanism — φ_s not aggregating across a merge — read three ways, and that mechanism is itself the
exclusion postulate seen as a set function. So the genuinely standalone additions are two. One is a
diagnostic correction: the prior 0.87 membership ceiling was an artifact of scoring coalitions across all
reachable states instead of at the state where the complex forms, and at the right state a node-level
marginal recovers membership at 0.98. That is the strongest result here, a real self-correction. The other
is a set of measured frequencies on the random-form population — the empty-core rate, the condensation gap,
the concentration of credit, the interchangeable-pair mix — which describe φ_s on a coverage sample and
await an organizationally motivated population to mean more. The game theory supplies the questions and the
names; the answers are facts about Φ on these models, and the lens re-describes rather than predicts.

## What it says for the dissertation

The cooperative-game objects are candidate formalizations of the dissertation's constructs, offered for
their suggestiveness, with one gap that sets the limit: the forms are random Boolean truth tables, and there is
no mediator, platform, or party-with-an-outside-option wired into the population. A node is called the
mediator after the fact, because a random form happened to make it indispensable. So these are analogies,
not identities. Algorithmacy — a mediating system that commits a determination both parties must heed —
has a candidate image as a form whose major complex binds the parties irreducibly, with the committing
system the veto player that carries the credit. Commit-versus-convey has the firmest contact with the math,
since it is a structural distinction the models exhibit: the triadic mediator binds where the dyadic hub
relays, and a quarter of single-bottleneck forms fall on the relay side. The platform reading and the
contestability reading are looser, the second especially, since the empty core is a mechanical consequence
of φ_s being subadditive on this sample, a property of the measure more than of coordination. The experiment
that would turn the analogies into findings is not yet built: a population with a designated mediator
architecture, on which one could test whether the veto player coincides with the designed mediator above
chance. Until then irreducibility is explored on these models, not established for organizations. None of
this replaces Φ. Integrated information is the object, and cooperative game theory is a language that makes
the shape of that object legible and ties it to how coordination is theorized elsewhere.

## Revision note

This essay was revised in response to a four-member committee panel
(`cooperative_game_committee_review.md`). The changes, by the panel's consolidated list: every percentage is
now marked a frequency over a random-Boolean coverage sample chosen for breadth (1); q122's
split verdict on the structured forms is cited in the construction section (2); the dissertation section is
demoted from identity to analogy with the missing-experiment gap named (3); the veto–Shapley and symmetry
results are stated as empirical, with the theorems flagged as motivating but inapplicable on a non-monotone
game (4); the argmax-is-major-complex identity is labelled near-definitional where it appears, beyond
the recovery section alone (5); the size-≥2 normalization control (91% agreement) is added and the claim narrowed
(6); the singleton convention is named and "the slogan is false" reframed as "superadditivity is the wrong
reading" (7); the empty-core, concentration, and subadditivity results are stated once as one mechanism, and
"solution concept" and "winner-take-all coalition formation" are demoted to argmax language (8).

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
