# Two, three, four answers: the same vote rules, and a number that grows by three

*Give people four possible answers instead of two or three, and the lab's vote results still hold. A ratio we couldn't explain turns out to follow a simple line, though we found it after our planned check missed it.*

## The question

In [an earlier post](2026-11-23-three-way-votes.md) we gave voters three answers (no, maybe, yes)
instead of two. The rules held: a majority vote run by a coordinator who sometimes misreads people never
binds the whole group, and an "all yes" rule always does. We also saw two exact numbers we couldn't
explain. The tightest subgroup in the majority vote was exactly 4 times as integrated as the whole group
with two answers, and exactly 7 times with three. And the "all yes" rule's integration was exactly
3 × log₂(number of answers). What happens with four answers?

Φ (IIT 4.0, computed exactly with PyPhi) measures how far a setup fails to split into independent parts.
It is not a claim that anything is alive or aware.

## What we ran

A coordinator and three people, each holding one of four values. The coordinator misreads each person
with probability r (0%, 5%, 10% or 20%) and decides by the middle reading (majority) or the lowest ("all
yes"); everyone adopts the decision. We wrote down predictions first, including a guess that the ratio
would be 10, on the line through 4 and 7.

## What we found

**The rules hold with four answers.** The clean majority vote falls apart (Φ = 0). With errors it is
slightly integrated (0.0099 at 5%, 0.0180 at 10%, 0.0283 at 20%) but never as a whole group. The clean
"all yes" rule binds everyone with Φ = 6.0, exactly 3 × log₂ 4, as predicted.

**Our planned check for the ratio was wrong, and the ratio is 10 anyway.** We planned to look at the
tightest subgroup in just one of the eight situations where the whole group peaks, assuming the others
were mirror images. They aren't, and in that one situation the ratio was about 6.6, so the prediction
failed as written. When we then checked all eight, two of them (the coordinator's value at one extreme,
everyone else at the other) give exactly 10 at every error rate. So the series is 4, 7, 10: three times
the number of answers, minus two. Because we found it after the planned check failed, we're treating it
as a lead to test again with five answers, not as settled.

## What it means

The lab's claims about majority votes and "all yes" rules are not artifacts of yes/no models. They hold
as people's answers get finer. And the hidden regularity in how a majority vote's subgroups outweigh the
whole seems to grow in a simple, steady way with the number of answers, which makes it worth deriving.

## Limits

Three people, four answer values at most, even errors, everyone updating at once. The 3k − 2 pattern
rests on three points and a check we added after seeing the first result.

## The code

- Study: [org_frontier/studies/alphabet_ladder_hub/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/alphabet_ladder_hub)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/alphabet_ladder_hub/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/alphabet_ladder_hub/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/alphabet_ladder_hub/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
