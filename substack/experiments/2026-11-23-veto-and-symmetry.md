# Why a veto splits apart: it's about fairness between the parties, not about them moving together

*An old explanation in the lab said a veto rule fails to hold three parties together because it pushes them into lockstep. We tested that across all 256 small setups of its kind. It's wrong, and a simpler rule replaces it with no exceptions.*

## The question

Picture a coordinator sitting between a worker and a counterpart. Each step, the coordinator makes a
yes/no decision from what the two of them did, and each of them then acts on that decision. The lab asks
whether such a setup hangs together as a whole or splits into separate parts, using integrated
information, Φ, from IIT 4.0, computed exactly with PyPhi. Φ above zero means no cut separates the parts
without losing something. It measures structure, not life or awareness.

A coordinator that says yes only when both say yes (an AND rule) holds the three together. A veto rule
("yes if the worker says yes and the counterpart doesn't object") splits apart, even though both parties
feed into it and both act on it. An earlier study explained that by saying the veto pushes the two
parties into lockstep. It also said how to test the explanation: break the lockstep and see what happens.

## What we ran

Every setup of this shape: the worker and the counterpart each react to the coordinator's last decision
(follow it, do the opposite, or ignore it), and the coordinator uses any yes/no rule of the two. That's
256 setups. Before computing, we wrote down a rule we expected to predict which ones hang together. The
run takes about five seconds.

## What we found

**Lockstep is not the reason.** When both parties simply follow the coordinator, they always end up
matching each other, whatever the rule. That is true for the AND rule too, and it holds together. Of the
64 setups where the two parties always match, 12 hold together.

**Fairness between the parties is the reason.** Our rule, written down beforehand, gets all 256 right:
the setup holds together exactly when both parties react to the coordinator and the coordinator's rule
treats them the same way. AND, OR and "exactly one of them" treat the two parties alike. The veto does
not: it lets one party's yes count and the other's count only as an objection.

**Flip one party's reaction and the verdict flips.** If the counterpart does the opposite of whatever the
coordinator decided, the two parties always disagree. Now the veto treats them alike in effect, and it
holds together. The AND rule no longer does, and it splits.

| setup | Φ |
|---|---:|
| veto, both parties follow the coordinator | 0 |
| veto, counterpart does the opposite | 2.0 |
| AND, both parties follow | 2.0 |
| AND, counterpart does the opposite | 0 |

## What it means

When two parties carry the same information and the coordinator weighs them unequally, the second party
adds nothing the first one didn't already supply, so the arrangement splits. When the coordinator weighs
them equally, both remain necessary, and the three-way arrangement can't be reduced to pairs. For thinking
about platforms: whether a mediator binds the people around it depends on how its rule treats the
people relative to how they respond to it, not on the wiring alone, and not on whether they end up acting
alike.

## Limits

Three-party yes/no setups where the parties connect only through the coordinator. Bigger groups, direct
contact between parties, memory and noise are untested. We found the rule; we haven't derived why the
theory produces it.

## The code

- Study: [org_frontier/studies/lockstep_symmetry/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/lockstep_symmetry)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/lockstep_symmetry/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/lockstep_symmetry/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/lockstep_symmetry/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
