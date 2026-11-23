# A counting rule predicts how weak the whole is next to its strongest part

*We fitted a formula to four noisy voting setups, then tested it on four new ones. It got all of them right.*

## The question

In this series a coordinator reads people's yes/no signals with some error, applies a voting rule, and
everyone acts on the result. We measure integrated information Φ (IIT 4.0, computed exactly with PyPhi):
how far the setup fails to split into independent parts. It is not a claim that anything is alive or
aware.

Earlier runs kept finding a neat pattern. Under majority-type rules, the most tightly bound part of the
setup (the coordinator plus one or two people) always had a Φ that was an exact whole-number multiple of
the whole group's Φ: 4 times for majority of three, 5 for 2-of-4, 16 for 3-of-5. [Last
time](2026-11-23-bigger-and-weighted-quorums.md) we showed the obvious guess, "the number of members",
was wrong. So what sets it?

## The guess, made before running anything new

Take the smallest group of people that can settle the vote on its own: q people to force "yes", or
n − q + 1 to force "no", whichever is smaller. Count every group of people too small to do that,
including nobody at all. Majority of three: only nobody and the three single people, so 4. 3-of-5: nobody,
5 singles and 10 pairs, so 16. That fits the four known cases, but we picked it to fit them, so they
prove nothing. We wrote it down, committed it, and then ran cases we had never computed.

## What we found

| rule | groups too small to settle it | strongest part ÷ whole |
|---|---:|---:|
| 2 of 5 (new) | 6 | 6.000000 |
| 4 of 5 (new) | 6 | 6.000000 |
| 1 of 4, "any yes" (new) | 1 | 1.000000 |
| 1 of 5, "any yes" (new) | 1 | 1.000000 |
| majority of 3 (known) | 4 | 4.000000 |
| 3 of 5 (known) | 16 | 16.000000 |

All five predictions held. For 2-of-5 at a 20% error rate the whole group's Φ is 0.0323 and the strongest
parts (the coordinator with any one person) are 0.1939, exactly six times as much, at both error rates we
tried. For "any yes" rules the only group too small to settle anything is nobody, the count is 1, and the
whole group is as tightly bound as any part.

## What it means

How weak a noisy vote's whole is, next to its strongest part, comes from the rule's arithmetic: how many
groups of voters can't decide anything alone. The more such groups, the more the binding is spread over
small pieces and the less it belongs to the whole. Majority-type rules have many; "any yes" and "all yes"
rules have one. That is a sharper version of the lab's quorum result: under these rules the coordinator's
binding of everyone together is real but thin, and the thinness is countable.

## Limits

Equal votes only; the coordinator misreads people independently; people copy the decision exactly; two
error rates; at most five people. A weighted rule we computed earlier also gives 6 and isn't covered by
the formula as written. We found the law; we have not derived it.

## The code

- Study: [org_frontier/studies/quorum_ratio_law/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/quorum_ratio_law)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/quorum_ratio_law/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/quorum_ratio_law/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/quorum_ratio_law/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
