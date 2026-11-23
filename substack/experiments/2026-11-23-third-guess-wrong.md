# A third guess that didn't hold

*We've been chasing one surprising result for three posts. This is the third explanation we wrote down in advance, and the third that failed.*

## The question

In our platform setup, the group bound more tightly when a switch copied the person who simply repeats
the platform, instead of copying the platform itself ([post](2026-11-23-who-works-the-switch.md)). The
last two posts ruled out two explanations: it isn't the delay
([post](2026-11-23-not-just-a-delay.md)), and it isn't that this person is part of the loop
([post](2026-11-23-not-any-loop-member.md)).

The guess left standing was more specific: the switch has to copy someone who only repeats the platform
*and* whom the platform listens to. We tested that in a different setup, with predictions written down
first. Now the platform listens to three people and acts only when all three say yes. Two of them simply
repeat the platform, and the third hears it through the go-between. The switch copies either the platform
or one of the repeaters.

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

Six members, two go-between rules ("both" and "platform and not switch"), two switch drivers. Four cases,
about two and a half minutes of computing.

## What we found

| go-between rule | switch copies platform | switch copies a repeater |
|---|---:|---:|
| "both" | 1.0 | 1.0 |
| "platform and not switch" | 0.415 | 0.415 |

Copying the repeater changes nothing. The prediction that it would raise the second number failed.

Two smaller things showed up. With three listeners, even the clean "both" rule gives the whole group only
1.0, where the two-listener setup gave 2.0, and the whole group never ties for the strongest unit. And the
0.415 is the same number the two-listener setup gave when the switch copied the platform.

## What it means

Three explanations written down ahead of time have now failed: delay, loop membership, and copying a
repeater the platform listens to. The original effect may just be a feature of the two-listener setup
rather than a general rule. We're reporting it that way instead of reaching for a fourth story after the
fact.

## Reproduce it

Everything is in the lab repo at
[`org_frontier/studies/echo_switch/`](../../org_frontier/studies/echo_switch/), with the predictions in
`hypotheses.md` and every number in `results/results.json`.
