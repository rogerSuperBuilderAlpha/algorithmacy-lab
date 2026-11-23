# Who works the switch doesn't change who is bound, only how tightly

*We reran all 48 go-between cases with a different group member working the switch. The same 28 cases hold together, but in 16 of them the binding gets stronger.*

## The question

The [last post](2026-11-23-every-go-between-rule.md) checked all 16 rules a go-between could use to combine
a platform's message with a switch, under three platform rules, with the platform working the switch.
Does the picture change if someone else works the switch? We reran everything with the switch worked by the
person who hears the platform directly, with predictions written down first.

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Same five members and the same 48 cases. Only the switch's driver changes, from the platform to its direct
listener. About nine minutes of computing.

## What we found

**The same cases hold together.** Exactly the same 28 of 48 cases have Φ above zero as before, and the same
20 split. The rules from the last post all carry over: reversing the output never matters, ignoring the
switch splits the group, and for "both" and "either" platforms the go-between's sensitive point has to
match what the platform listens for.

**But 16 cases bind more tightly.**

| cases | switch worked by the platform | switch worked by the direct listener |
|---|---:|---:|
| "exactly one" platform, any go-between that uses the switch (12 cases) | 0.5 | 2.0 |
| "both"/"either" platform, off-centre sensitive point (4 cases) | 0.415 | 0.830 |

The other non-zero cases stay at 2.

Two of three predictions held. We had predicted that the values would also stay the same, and they did not.

## What it means

Which members a platform binds is set by the rules they follow. It does not depend on which of them
works the switch, at least for these two choices. How strongly the whole group holds together does depend
on it. For algorithmacy, that separates two questions that are easy to run together. Who is part of the
platform's whole is a question about rules. How strongly the whole holds is also a question about who
listens to whom.

## Limits

Yes/no units, everyone updates at once, five members, two possible switch drivers. Ties are judged at a
1e-9 cutoff, pooled over all states where the top value appears.

## The code

- Study: [org_frontier/studies/gate_census_r1/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/gate_census_r1)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/gate_census_r1/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/gate_census_r1/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/gate_census_r1/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
