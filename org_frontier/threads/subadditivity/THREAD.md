# Thread — integration does not aggregate

"The whole is more than the sum of its parts" is the slogan integrated information is supposed to make
precise, and the dissertation leans on it. As a cooperative game it has an exact name. Score a coalition of
parties by v(S) = φ_s(S), its system integrated information, and the slogan reads as superadditivity:
v(S ∪ T) ≥ v(S) + v(T) for disjoint coalitions. The integration game does not have that property. Saying
what it has instead replaces a loose slogan with the right one. Reproduce with
`python org_frontier/threads/subadditivity/subadditivity.py` (seed 11, 300 three-node forms).

## Setup

The value of a coalition is the integrated information of its parts taken together, maximized over
reachable states, with single parties scored at their own intrinsic φ. Superadditivity asks whether joining
two disjoint coalitions is worth at least their separate values. The dual edge cases carry the result:
whether two parties that integrate with no one alone can form an integrating dyad, and whether the whole
integrates at least as much as its tightest pair.

## The arc

**The integration game is subadditive.** A subadditive split — a disjoint S, T with v(S ∪ T) < v(S) + v(T) —
appears in 296 of 300 forms, 98.7%. Only 4 forms are superadditive throughout. Adding a party to a coalition
lowers its integration somewhere in 294 of 300, 98%. Integrated information does not aggregate: the φ of a
whole is not the φ of its parts added up, and joining parts usually destroys integration instead of
banking it. The slogan, read as a claim about Φ, is false; the word that survives is irreducible.

**The subadditivity comes from where integration lives.** A single party can carry substantial intrinsic
φ, and two such parties joined are scored by the irreducibility of the pair across its own partition, a
smaller quantity than the two standalone values summed. Integration is a property a particular subset has,
read off that subset, and it does not carry across a merge. This is the same fact the exclusion postulate is
built on, seen as a set function.

**The synergy the slogan reaches for is real, but it lives at the bottom.** Two parties that integrate with
no one alone — v = 0 each — form an integrating dyad in 232 of 300 forms, 77%. Coordination creates
irreducibility from nothing. The genuine "more than the parts" effect is the first step up from isolated
parties, where a relation appears that neither party had alone, a one-step lift that stops paying as the
coalition grows.

**At the top, a party dilutes.** The whole integrates less than its tightest pair in 197 of 300 forms, 66%,
and when it does the drop is large: a mean gap of 1.24 in φ between the best pair and the trio. A third
party lowers the integration of a coordinating group below the dyad inside it. Every one of these forms has
a major complex that is a proper subset, 197 of 197, because the whole falling below a pair is exactly the
exclusion postulate selecting that pair.

## What the thread establishes

Integrated information is subadditive as a coalition game: 99% of forms violate superadditivity, and the φ
of a whole is not its parts summed. The synergy the slogan names is real only at the bottom edge, where
coordination lifts two isolated parties into an integrating dyad, 77% of forms. Above that edge integration
dilutes — the trio sits below its tightest pair in two thirds of forms, by more than a full unit of φ — and
that dilution is the exclusion postulate keeping the proper subset. The dissertation should say irreducible,
not more-than-the-sum: the whole is rarely more than the sum, and the claim worth making is that a selected
subset is irreducible.

## Limits, honestly

The subadditivity is driven by single parties carrying intrinsic φ; under a convention that scores a lone
party at zero, the bottom-edge synergy is what remains and the top-edge dilution still bites. The
dilution-equals-proper-complex coincidence is a restatement of the coalition-structure thread's result that
the major complex is the argmax coalition, not a second finding. The 4 superadditive forms are the
degenerate ones where only the whole integrates. Everything is in-silico on three-node Boolean forms over a
sampled population. The contribution is conceptual: it puts a precise cooperative-game property under a
slogan the program uses, and the property is subadditivity, so the slogan needs the more careful word.
