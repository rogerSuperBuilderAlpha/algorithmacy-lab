# It wasn't the delay

*Last time, moving the switch to a different group member made the group bind more tightly. A simple explanation was that the switch was just working from older news. We tested that, and it's wrong.*

## The question

In the [last post](2026-11-23-who-works-the-switch.md), a go-between combined the platform's message with
a switch. When the switch copied the person who hears the platform directly, instead of copying the
platform itself, 16 of 48 cases bound more tightly. That listener is just repeating the platform one step
late, so maybe the only thing that mattered was the delay: the switch was acting on news that was one step
older.

To test that, we gave the switch the same one-step delay in a different way: an extra helper who copies the
platform and passes it to the switch, and talks to nobody else. If delay is the whole story, the helper
should give the same numbers as the direct listener. We wrote down those predictions before running.

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Three cases from the last two posts, each with three ways of driving the switch: copy the platform, copy
the direct listener, or copy the extra helper (who copies the platform). The helper makes the group six
members instead of five. A few minutes of computing.

## What we found

| case | switch copies platform | switch copies listener | switch copies helper |
|---|---:|---:|---:|
| "both" platform, "both" go-between | 2.0 | 2.0 | 1.0 |
| "both" platform, "platform and not switch" go-between | 0.415 | 0.830 | 1.0 |
| "either-but-not-both" platform, "both" go-between | 0.5 | 2.0 | 0.5 |

All three predictions failed. The helper does not reproduce the listener's numbers:

- Under the "either-but-not-both" platform, the helper gives 0.5, the same as copying the platform
  directly, not the 2.0 the listener gave.
- Under the "both" platform, the helper gives 1.0 in both cases, and in neither case does the whole group
  tie for the strongest unit. Adding the helper made the clean "both/both" case bind less tightly
  (2.0 down to 1.0).

## What it means

How old the switch's information is doesn't explain the change. What seems to matter is who the switch
listens to. The direct listener is already part of the platform's loop, since the platform reads it back.
The helper isn't, and adding it is not the same as reusing someone already in the loop. That reading
comes after the fact. The next test is to let the helper also feed the platform and see whether that
restores the higher values.

## Reproduce it

Everything is in the lab repo at
[`org_frontier/studies/switch_delay/`](../../org_frontier/studies/switch_delay/), with the predictions in
`hypotheses.md` and every number in `results/results.json`.
