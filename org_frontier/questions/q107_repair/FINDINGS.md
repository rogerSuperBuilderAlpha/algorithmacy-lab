# Q107 findings — repair is lever-specific: the broken condition must be the one restored

All four hypotheses confirmed. A triad damaged on one lever is repaired at that lever and not another:
binding damage at the mediator, liveness damage at the party's read. Coordination has no repair redundancy.
The condition that was broken is the condition that must be supplied; a different edit does not route around
the damage.

| damage | repair distance | repair bits | lever | lever-specific |
|---|---|---|---|---|
| binding broken (mediator ignores the counterpart) | 1 | {5, 6} | mediator (4-7) | yes |
| liveness broken (counterpart's read made constant) | 1 | {3} | counterpart read (2-3) | yes |

| H | Result | Verdict |
|---|--------|---------|
| H1 | both damaged triads are repairable | confirmed |
| H2 | binding damage is repaired at the mediator | confirmed |
| H3 | liveness damage is repaired at the party's read | confirmed |
| H4 | repair is lever-specific (no routing around) | confirmed |

From `probe_repair.py`.

## What it says

A broken triad is repaired at the lever that broke. The binding-damaged form, where the mediator no longer
reads the counterpart, is repaired by a single edit to the mediator's function (H2). The liveness-damaged
form, where the counterpart no longer reads the mediator, is repaired by a single edit to the counterpart's
read (H3). Each repair is a single edit, so both forms are one move from triadic (H1), but the move is fixed
by the damage.

Repair cannot route around the damage. The binding-damaged form has no distance-1 repair at a party's read,
and the liveness-damaged form has none at the mediator (H4). Strengthening a different condition does not
restore the triad; the broken condition itself must be supplied. This is the repair form of the law's
necessity: each condition is necessary for the triad, so removing one cannot be compensated by another, and
the form stays dyadic until the missing condition returns. A coordination is not held by a redundant set of
supports that can substitute for each other; it is held by three distinct conditions, each required, each
repairable only in its own place.

The result sits with Q104 and completes the boundary account. Q104 found every edge of the minimal triad
load-bearing — no edge whose loss the others absorb. Q107 is the same at the level of conditions: no
condition whose loss another condition repairs. Q105 mapped the build side of the boundary and found it
thin; Q106 named the levers; Q107 shows that on this boundary, damage and repair are lever-locked. A
designer who breaks a coordination on one lever, by accident or by attack, can repair it only by restoring
that lever, and a defender who knows which lever was struck knows where the repair must go.

## Caveats

- **Confirmatory.** All four predictions held; lever-specific repair follows from the law's necessity.
- **Two damages.** Binding and liveness damage on the read-recipient triad; the requirement lever needs a
  larger form and is not read here. The result is for the two levers tested.
- **Distance-1 repairs.** Both damages are one edit from triadic, so the lever-specificity is read at
  distance 1; whether a multi-edit repair could route around a deeper damage is untested. In-silico, exact
  verdict.
