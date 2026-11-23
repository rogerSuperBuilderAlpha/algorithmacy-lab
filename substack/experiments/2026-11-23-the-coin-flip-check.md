# We checked whether a hidden coin-flip in the software changed any of our results. It didn't.

*Our last experiment found that the IIT software sometimes settles ties arbitrarily, and that this could flip a verdict. So we went back over more than 4,100 earlier setups to see whether any published answer had depended on it.*

## The question

This lab asks whether a coordination setup hangs together as a whole or splits into parts. It answers
with integrated information, Φ, from IIT 4.0, computed exactly with the PyPhi software. Φ above zero means
no cut separates the parts without losing something. It measures structure, not life or awareness.

In our [previous post](2026-11-23-each-could-swing-it.md), we found a weak spot. Partway through the
calculation, the software has to pick the most likely past and future states of the system. Sometimes
several are exactly tied, and the software takes whichever comes first on its list. Its own code says ties
are "arbitrarily broken (for now)". For 24 of 256 three-person setups, a different pick would have changed
the answer.

That raises an obvious worry: had any of the lab's earlier results depended on that arbitrary pick?

## What we ran

We re-checked the setups the lab's main claims rest on, trying every tied option instead of just the
first:

- all 4,096 three-party setups where each party responds to the other two,
- the 256 of those where two people connect only through a coordinator,
- the 15 named setups the lab's papers cite,
- 47 setups from the lab's earlier "atlas" study (up to five parties).

Predictions committed first. About two and a half minutes on four processors.

## What we found

**Ties are everywhere, but harmless here.** 3,984 of the 4,096 three-party setups have at least one tied
choice somewhere in the calculation.

**Not one answer changed.** In every group, the setups that hang together are the same whichever tied
option the software picks: 2,288 of 4,096, 24 of 256, 7 of the 15 named setups, 24 of the 47 atlas
setups. Even the size of Φ stayed exactly the same.

| group | setups | hang together | answer depends on the tie |
|---|---:|---:|---:|
| all three-party setups | 4,096 | 2,288 | 0 |
| two people through a coordinator | 256 | 24 | 0 |
| named setups from the papers | 15 | 7 | 0 |
| atlas setups (up to five parties) | 47 | 24 | 0 |

## What it means

The weak spot is real, but it shows up in a narrow place: setups where several people are interchangeable,
like three voters who all copy the same coordinator. The results the lab's main argument rests on, that
some three-way arrangements cannot be reduced to pairs while others can, do not depend on it. For future
work with interchangeable parties, we'll report both possible answers when a tie matters.

## Limits

We checked ties in the system's overall past and future states, not every tie deep inside the software.
Six-party atlas setups were skipped to keep the run short.

## The code

- Study: [org_frontier/studies/tie_audit/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/tie_audit)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/tie_audit/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/tie_audit/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/tie_audit/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
