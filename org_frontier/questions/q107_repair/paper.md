# Q107 — Repair is lever-specific: no routing around the damage

## Question

Q106 cataloged the design operations as three reversible levers. Repair sharpens the catalog: when a triad
is broken on one lever, must the repair restore that lever, or can a different edit route around the damage
and restore the triad another way? The first means coordination has no repair redundancy; the second means
a substitute condition can stand in for a broken one.

## Method

The read-recipient triad, encoded over the 256-form family, is damaged two ways: its binding broken (the
mediator's function made independent of the counterpart) and its liveness broken (the counterpart's read of
the mediator made constant). For each, the repair distance is the construction distance to a triadic form,
and the bits achieving a distance-1 repair are read against the damaged lever's bit range.

## Results

Both damaged forms are one edit from triadic, and the edit is at the damaged lever. The binding-damaged form
repairs at a mediator bit; the liveness-damaged form at the counterpart's read bit. Neither repairs at the
other lever.

| damage | repair distance | repair bits | lever |
|---|---|---|---|
| binding broken | 1 | {5, 6} | mediator |
| liveness broken | 1 | {3} | counterpart read |

| | result |
|---|---|
| H1 both repairable | confirmed |
| H2 binding repaired at the mediator | confirmed |
| H3 liveness repaired at the party's read | confirmed |
| H4 repair is lever-specific | confirmed |

## Interpretation

Repair is lever-locked because each condition is necessary. The law makes a party bound only when the
mediator reads it and it stays live; both conditions are required, so removing one cannot be compensated by
strengthening the other. A binding-damaged form is dyadic until the binding returns, however live its
parties are, and a liveness-damaged form is dyadic until liveness returns, however well the mediator reads.
The repair must supply the missing condition in its own place, and no other edit routes around it.

This completes the boundary account the design wave built. Q105 found the boundary thin and the build
usually at a party's read; Q106 named the three levers; Q107 shows that damage and repair are lever-locked.
Together they say that the dyad/triad boundary is crossed one condition at a time: a build supplies a
condition, a break removes one, and a repair restores the specific condition that was removed. There is no
shortcut that crosses the boundary by trading one condition for another.

The result is the repair form of Q104's no-redundancy finding. Q104 found every edge of the minimal triad
load-bearing; Q107 finds every condition load-bearing in the same way — no condition whose loss another
repairs. For the security reading the wave shares with Q84 and Q97, the lesson is concrete: an adversary who
breaks a coordination on one lever forces the repair to that lever, and a defender who identifies the
damaged lever knows where to act. Damage localizes the repair, because the conditions do not substitute for
each other.

## Limitations

In-silico; exact verdict over the strict-mediation family. Two damages, binding and liveness, on the
read-recipient triad; the requirement lever needs a larger form and is not tested here. Both damages are one
edit from triadic, so lever-specificity is read at distance 1; whether a multi-edit repair could route
around a deeper damage is untested.
