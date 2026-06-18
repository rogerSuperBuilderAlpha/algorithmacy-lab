# Thread — the cooperative-game laws at four parties

Seven threads read integrated information as a cooperative game, and all of them ran on three-party forms.
Three parties is the smallest case where a mediated triad exists, and it is small enough to be suspect: a
bottleneck reads off a single complement pair, the coalition lattice has six members, and a result can hold
for reasons that vanish with scale. This thread re-runs the load-bearing laws on four-party forms. They
hold, the empty core holds more strongly, and one new thing appears — a bottleneck that is a set of parties.
Reproduce with `python org_frontier/threads/four_party/four_party.py` (seed 11, 50 four-party forms; slower
than the three-party threads, four-node exact Φ).

## Setup

The same construction at one more party: random four-node Boolean forms, the game v(S) = φ_s(S) over the
fifteen non-empty coalitions, the major complex at the state where it is largest. The checks are the claims
the earlier threads established at three parties — the major complex is the argmax coalition, the game is
subadditive, the core is empty, a single bottleneck is the Shapley-argmax party, and the credit concentrates.

## The arc

**The structural laws hold.** Across 50 forms the major complex is the φ_s-argmax coalition in every one,
the game has a subadditive split in every one, and a single bottleneck is the Shapley-argmax party in all 7
forms that have one. The three-party results were not artifacts of the six-coalition lattice. The major
complex still selects the maximally integrated coalition, integration still fails to aggregate, and the
bottleneck still carries the pivotal weight when there is a single one.

**The empty core gets stronger.** At three parties the core was non-empty in 4% of forms. At four parties it
is empty in all 50. More parties mean more coalitions that can out-value the whole, so a stable split of the
credit is harder still to find. The contestability the core-stability thread found does not soften as
coordinations grow; it deepens.

**The credit still concentrates.** Among the irreducible forms the top party's mean Shapley share is 0.75,
well above the 0.25 of an equal four-way split. Concentration survives the extra party, though it is less
extreme than the three-party 1.0-plus, since a fourth party gives the credit somewhere else to go.

**A bottleneck can now be a set.** At three parties the parties in every integrating coalition were at most
one. At four they can be more: the veto-set sizes here are 42 forms with none, 7 with a single bottleneck,
and 1 with a joint bottleneck of three parties that no integrating coalition leaves out. A joint bottleneck
is a group that is indispensable together, the set-valued version of the single mediator. It is rare in this
sample, 1 of 50, and a different draw (seed 4, 40 forms) showed about one in eight, so its frequency is not
pinned down. The structure is the point: only four parties or more can show it.

## What the thread establishes

The cooperative-game reading of integrated information is not a three-party accident. The major complex as
argmax coalition, the subadditivity of φ_s, the empty core, the bottleneck as Shapley-argmax party, and the
concentration of credit all carry to four parties, and the empty core carries more strongly, empty in every
form here against 96% at three parties. The one genuinely new feature is the joint bottleneck: with four
parties a set of parties can be collectively indispensable, which the single complement pair of the
three-party case could not express.

## Limits, honestly

Fifty forms is a small sample, forced by four-node exact Φ being slow; the laws that read 100% are robust to
that, but the joint-bottleneck frequency is not, and this thread does not claim a rate for it. Four parties
is still small, and whether joint bottlenecks have their own veto-and-Shapley structure — whether each
member of a joint bottleneck is pivotal, or only the set is — is the question this thread opens and does not
answer. The mean top share at four parties is reported over the irreducible forms in the sample and will
move with the population. Everything remains in-silico on Boolean forms. The result is a generality check
that the earlier threads needed: the laws are not artifacts of the smallest case, and the set-valued
bottleneck is the next thing to study.
