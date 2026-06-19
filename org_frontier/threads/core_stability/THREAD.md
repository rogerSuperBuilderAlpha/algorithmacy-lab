# Thread — the integration credit has no stable split

The subadditivity thread showed φ_s does not aggregate: a tight pair often out-values the whole that
contains it. This thread reads that fact on the allocation side and finds a sharp consequence. The credit
for a coordination's integration almost never has a stable division among the parties. Reproduce with
`python org_frontier/threads/core_stability/core_stability.py` (seed 11, 300 three-node forms).

## Setup

Score a coalition by v(S) = φ_s(S). An allocation splits the whole's worth v(N) among the parties. It is
*stable* — in the core — when no coalition can beat its share by walking: sum(x) = v(N) and, for every
coalition S, the parties in S receive at least v(S). The Shapley value is the canonical fair allocation,
each party paid its average marginal contribution. The questions: does a stable allocation exist, is the
fair one stable, and what decides it.

## The arc

**A stable split almost never exists.** The core is non-empty in 11 of 300 forms, 3.7%. For 96% of
coordination forms, every way of dividing the whole's integrated information leaves some coalition able to
do better on its own. There is no settled answer to who is owed how much of the coordination's
irreducibility.

**The fair split is almost never stable either.** The Shapley value lands in the core in 7 of 300 forms,
2.3%. Paying each party its average marginal contribution leaves a coalition wanting to walk in 98% of
forms, because the core it would have to land in usually does not exist.

**Subadditive dilution is what empties the core.** Split the forms by whether the whole out-values its
tightest pair. Among the 197 forms where a pair out-values the whole, the core is empty in every one,
0 of 197. A pair worth more than v(N) demands more than the whole has to give, so no allocation can satisfy
it. The empty core is the dilution of the subadditivity thread, read as an allocation. Among the 103 forms
where the whole holds its own against every pair, a stable split exists 10.7% of the time — holding the top
is necessary for stability, and the rest is the further balance the core demands across all coalitions.

**A bottleneck confers power, not stability.** The veto thread found the mediator is a veto player and
carries the largest Shapley value. A veto player guarantees a non-empty core in a monotone simple game.
This game is neither monotone nor simple, and the guarantee fails: forms with a veto player have a stable
split in 8 of 236, 3.4%, no better than the rest. The mediator's structural power buys it the largest
share of the credit and no power to make the division hold.

## What the thread establishes

The integration game has an empty core in 96% of forms, and the Shapley value is stable in 2%. A
coordination's irreducibility cannot be divided among its parties so that all of them stay: a tighter
subgroup almost always has the standing to break away. The cause is subadditivity — a pair out-values the
whole, which empties the core outright (0 of 197 dilution forms stable). And the bottleneck that dominates
the Shapley value does not stabilize the split, because the theorem that would make it do so needs a
monotone game and this one is not.

## Limits, honestly

The empty core follows from subadditivity, which the previous thread already established; this thread adds
the allocation reading and the exact mechanism, not a new property of φ_s. Core membership and the Shapley
value are computed on the game with single parties scored at their intrinsic φ; that intrinsic worth makes
individual rationality demanding and contributes to the empty cores, alongside the dilution that does the
main work. The veto-player negative result is a correct reading of the classical theorem's hypotheses, not
a surprise once the game is seen to be non-monotone. Everything is in-silico on three-node Boolean forms
over a sampled population. The organizational reading is the result worth carrying: a mediated coordination
holds together as a process while its credit stays contestable, and the party at the bottleneck takes the
largest share without securing the peace.

The population caveat turns out to be load-bearing. The [structured-forms thread](../structured_forms/THREAD.md)
re-runs the empty core and the dilution that empties it on the strict-mediation mediated triad, the structure
the dissertation models, and both reverse: the core is non-empty in every triadic form and no pair out-values
the whole. The contestability above is the random sample's; on the structured coordination forms the credit
splits stably. The "no stable split" headline holds for the random population and fails for the structured
one.
