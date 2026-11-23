# Not just anyone in the loop

*Two posts ago, letting a particular group member work the switch made the group bind more tightly. Last time we showed it wasn't the delay. This time we checked whether any member of the loop would do. It wouldn't.*

## The question

Our setup: a platform listens to two people. The first copies the platform directly; the second hears
the platform through a go-between, who combines the platform's message with a switch. When the switch
copied the first listener instead of the platform, the group bound more tightly in 16 of 48 cases
([post](2026-11-23-who-works-the-switch.md)). The [last post](2026-11-23-not-just-a-delay.md) showed it
wasn't the delay. Our after-the-fact guess was that it mattered that the first listener is part of the
platform's loop.

The second listener and the go-between are also part of that loop. If the guess is right, letting either
of them work the switch should give the same higher numbers. We wrote that prediction down before running.

We measure this with integrated information Φ (IIT 4.0, computed exactly with PyPhi). Φ measures how far a
setup fails to split into independent parts. It is not a claim that anything is alive or aware.

## What we ran

The same three cases as last time, with the switch copying the second listener or the go-between itself.
Six cases, about 20 seconds of computing.

## What we found

| case | switch copies platform | first listener | second listener | go-between |
|---|---:|---:|---:|---:|
| "both" platform, "both" go-between | 2.0 | 2.0 | 2.0 | 2.0 |
| "both" platform, "platform and not switch" go-between | 0.415 | 0.830 | 0 | 0 |
| "either-but-not-both" platform, "both" go-between | 0.5 | 2.0 | 1.0 | 0.5 |

The prediction failed. With the second listener or the go-between on the switch, the middle case splits
completely (Φ = 0), and the last case stays well below 2.0.

## What it means

Not every member of the loop works the same. Putting the second listener or the go-between on the switch
creates a small extra loop that doesn't go through the platform: the switch feeds the go-between, which
feeds the second listener, which feeds the switch (with the go-between on the switch, the two simply feed each other). That small loop shows up as one of the strongest units
on its own. The first listener only repeats the platform and adds no side loop. That explains why the
other two don't help, but not exactly why the first listener does. We're leaving that open rather than
guessing.

## Reproduce it

Everything is in the lab repo at
[`org_frontier/studies/switch_loop_member/`](../../org_frontier/studies/switch_loop_member/), with the
predictions in `hypotheses.md` and every number in `results/results.json`.
