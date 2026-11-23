# Bigger and weighted votes under noise: the heavy voters stay bound, the whole group never does

*We took the noisy-vote experiments to five voters and to votes where some people count double. One rule held everywhere we looked. A pattern we had started to trust did not.*

## The question

Across the [earlier posts](README.md), a coordinator read people's yes/no signals with some error,
applied a voting rule, and everyone acted on the result. We measured integrated information Φ (IIT 4.0,
computed exactly with PyPhi): how far that setup fails to split into independent parts. Φ is not a claim
that anything is alive or aware.

Two things looked solid with three and four voters. First, under a majority-style rule, the whole group was
never among the most tightly bound parts. Second, the strongest part had exactly 4 times the whole
system's Φ with three voters and 5 times with four, as if the ratio were the number of nodes. Do these
hold with five voters, and with weighted votes?

## What we ran

- **Weighted votes:** four voters, two of whom count double (weights 1, 1, 2, 2), with the decision
  threshold set at 2, 3, 4 or 5 points, at error rates 0, 5%, 20% and 40%.
- **Five voters:** a plain 3-of-5 majority at 10% and 20% error.

For every state the system can reach, we computed Φ for every sub-group, so ties show up. About five
minutes of compute. Predictions were committed first.

## What we found

**The whole group is never bound tightest.** In every noisy case, weighted or five-voter, the full group
never appears among the most tightly bound sub-groups.

**Heavy voters stay bound to the coordinator.** With a threshold of 2 or 5 points, the coordinator plus
the two double-weight voters is the tightest sub-group at every error rate (Φ = 1.67 at 5% error, 0.83
at 20%, 0.037 at 40%, tied there with each heavy voter alone).

**Noise creates integration where there was none.** With a threshold of 3 or 4 points, the clean rule has
no integrated sub-group at all, yet with noise the whole system's Φ is positive at every rate (0.032 at
20% error).

**The node-count pattern breaks.** For the 3-of-5 majority the strongest sub-group has 16 times the whole
system's Φ (0.0682 vs 0.0043 at 20% error), not 6. And it is a 15-way tie: every pair and every trio that
includes the coordinator scores the same.

## What it means

The claim worth keeping is about membership: when a vote-counting coordinator has noise, the people it
binds most tightly are some subset, never everyone, and with weighted votes it is the people whose votes
decide the outcome. The neat ratio we noticed earlier was a small-group coincidence or depends on the
rule, and we are dropping it as a candidate law. This is why we register predictions before running: two
of ours failed here, and they were wrong in a way worth knowing.

## Limits

Small yes/no models, independent errors only, voters never err, everyone updates at once. One weight
pattern and one five-voter rule. Ties are judged at a 1e-9 cutoff.

## The code

- Study: [org_frontier/studies/five_six_node_quorum_ties/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/five_six_node_quorum_ties)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/five_six_node_quorum_ties/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/five_six_node_quorum_ties/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/five_six_node_quorum_ties/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
