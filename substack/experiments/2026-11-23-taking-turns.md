# When people take turns, no group holds together as a whole

*Make the coordinator and the people act one after another instead of all at once, and every voting rule splits apart, in all 24 possible orders. Who goes first decides which piece is left bound.*

## The question

In the setups from the [earlier posts](README.md), a coordinator and three people all act at the same
moment: the coordinator decides from what the people did last step, and the people follow the
coordinator's last decision. Real groups often take turns instead. The coordinator decides, then one
person reacts, then the next, each seeing what the others just did.

Does taking turns change whether the group holds together? We measured integrated information Φ (IIT
4.0, computed exactly with PyPhi), which says how far a setup fails to split into independent parts. It
is not a claim that anything is alive or aware.

## What we ran

Three rules ("any yes", majority, "all yes"). Four members, so 24 possible turn orders. 72 setups, no
noise, about 7 seconds. For every state the system can reach, we computed Φ for every sub-group.
Predictions committed first. We expected some orders to keep "any yes" and "all yes" whole. None did.

## What we found

**Taking turns splits every setup.** Whole-system Φ is zero in all 72. Acting at the same moment, "any
yes" and "all yes" each have Φ = 3. In every turn order, they fall apart.

**Who goes first decides what is left.**

| when the coordinator acts | tightest-bound piece ("any yes" or "all yes") | its Φ |
|---|---|---:|
| first | the three people, without the coordinator | 6 |
| second | the coordinator and the two people after it | 6 |
| third | the coordinator and the last person | 2 |
| last | the coordinator alone | 1 |

**When the coordinator goes first, the people bind to each other and the coordinator drops out.** Each
person copies a decision the coordinator made a moment earlier from the answers everyone gave last step. So in
effect each person is responding directly to the others, and the coordinator is just passing the signal
along. The three people form a tighter unit (Φ = 6) than the whole group did when everyone acted at once
(Φ = 3).

**Majority still never holds together,** in any order.

## What it means

Whether a three-way arrangement holds together depends on timing as well as on the rule. In these setups,
the same rule with the same people binds as a whole only when everyone acts on the same beat. Once members take turns,
the coordinator stops being a third party that holds everyone together. It either becomes a relay the
people talk through, or a unit off by itself. In algorithmacy terms, a platform that hands decisions
along in sequence works as a pipe, not as a binding third party.

## Limits

Three-person yes/no models only, no noise, one fixed order per setup. We did not compute truly random
turn-taking (one member at random each step). The [slow-coordinator post](2026-11-23-the-slow-coordinator.md)
approximated it, and "any yes" stayed slightly whole there (Φ 0.196).

## The code

- Study: [org_frontier/studies/update_order_quorum/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/update_order_quorum)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/update_order_quorum/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/update_order_quorum/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/update_order_quorum/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
