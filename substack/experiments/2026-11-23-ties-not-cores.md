# Nobody was dropped: the shrinking groups were ties

*An earlier post said that as noise rose, fewer people stayed bound to the coordinator. Counting ties properly, every person stays in.*

## The question

In the [first post of this series](2026-11-23-noisy-majorities.md), we reported that under a noisy majority
vote, the most tightly bound group got smaller as errors grew: first the coordinator plus two people, then
the coordinator plus one. Later runs showed the top spot is usually shared by several groups with exactly
the same Φ. PyPhi returns only one of them. So was anyone actually dropped, or was that just which tied
group the software happened to report?

Φ here is integrated information (IIT 4.0, computed exactly with PyPhi): how far a setup fails to split
into independent parts. It is not a claim that anything is alive or aware.

## What we ran

The same seven voting rules as the first post (any yes, majority, all yes with three people; 1, 2, 3 or 4
of four people) at the same eight error rates, 1% to 45%. This time we listed every group tied for the top.
56 cases, under a minute. Predictions committed first.

## What we found

**Nobody was dropped.** For majority-type rules, every person is in a tied top group at every error rate.
Under majority of three, the three pairs (coordinator plus one person) tie at 10% error and above, and below
that the three pairs and three trios all tie. The single "core" we reported before was one of these ties.

**The whole group is never on top under majority-type rules,** at any rate. That part of the earlier result
holds.

**An exception we reported was also a tie.** We had said the four-person "any yes" rule lost the whole group
at 40% error. Counting ties, the whole group is still on top there, tied with 14 smaller groups.

**At high error, even "any yes" stops singling out the whole.** Up to 30% error, the whole group is the one
top group. At 40% and 45%, every group that includes the coordinator ties with it (Φ 0.0233 at 40% for three
people). We had predicted the whole would stay alone on top; that was wrong.

| rule | groups tied at the top, 1% → 45% error | whole group among them? |
|---|---|---|
| majority of 3 | 6, then 3 from 10% on | never |
| 2 or 3 of 4 | 14 → 10 → 4 | never |
| any yes / all yes, 3 people | 1 up to 30%, then 7 | always |
| any yes / all yes, 4 people | 1 up to 30%, then 15 | always |

## What it means

This corrects our own earlier reading. A noisy majority doesn't push people out of the bound group one by
one. It binds each person to the coordinator equally and never binds them all together. For algorithmacy,
the third party's hold on each person is symmetric; what's missing is the whole.

## Limits

Equal-vote rules with three or four people; independent errors; people copy the decision exactly. Ties are
judged at a 1e-9 cutoff.

## The code

- Study: [org_frontier/studies/tie_set_membership/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/tie_set_membership)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/tie_set_membership/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/tie_set_membership/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/tie_set_membership/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
