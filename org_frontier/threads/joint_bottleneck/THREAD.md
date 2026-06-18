# Thread — inside a joint bottleneck the credit is shared

The four-party thread found a structure three parties cannot show: a bottleneck that is a set of parties,
each of them in every integrating coalition. The single bottleneck of the three-party case took almost all
the Shapley credit and left the runner-up at or below zero — winner-take-all. This thread asks what happens
inside a bottleneck that is a set, and finds the opposite: the set captures the credit together and splits
it roughly evenly. Reproduce with
`python org_frontier/threads/joint_bottleneck/joint_bottleneck.py` (seed 11, 400 four-party forms scanned;
slow, joint bottlenecks are rare).

## Setup

A joint bottleneck is a veto set of two or more parties: every coalition that integrates contains all of
them. Each member is therefore a veto player on its own, by the definition of the intersection. The open
question is the credit. At three parties the credit concentrated on one party and the others lost; with a
joint bottleneck there are two indispensable parties, and either one of them dominates the way a single
mediator did, or they share. Scanning 400 four-party forms turns up 16 with a joint bottleneck — rare, as
the four-party thread warned, and the sample is small.

## The arc

**The credit concentrates on the set.** In all 16 joint-bottleneck forms the bottleneck members are the top
Shapley parties: the two or three parties that sit in every integrating coalition are exactly the two or
three best-paid. Nearly every member carries a positive Shapley value, 15 of 16. The set captures the
credit the way a single mediator did, and the unit that captures it is the set.

**Inside the set the credit is shared.** The within-set ratio of the smallest member's Shapley to the
largest averages 0.78, where 1 is a perfectly even split and a winner-take-all set would fall toward zero.
The two indispensable parties are paid comparably. The runner-up seat, which a single mediator drove to zero
or below, is held here by a co-bottleneck who is a partner rather than a casualty. One form runs unequal, a
ratio of 0.12, so the sharing is a tendency and not a law.

**Outsiders are weakly excluded.** Every party outside the bottleneck has a non-positive Shapley value in 9
of 16 forms — less categorical than the three-party exclusion, where the dropped party was usually a net
drag. With four parties an outsider sometimes keeps a small positive share, so the line between the
indispensable set and the rest is sharp on the inside and softer on the outside.

## What the thread establishes

A joint bottleneck generalizes the single mediator in the way the structure suggests and the credit does
not. The set is collectively indispensable, its members are the top-paid parties in every case found, and
within the set the credit is shared roughly evenly rather than seized by one. The winner-take-all of the
three-party case was a feature of the bottleneck being a single party. When indispensability is joint, so is
the reward, and the second seat turns from a drain into a partner.

## Limits, honestly

Sixteen forms is a small sample, forced by joint bottlenecks being rare and four-node exact Φ being slow;
the members-are-top-paid result is unanimous across those sixteen, but the sharing ratio and the outsider
result are tendencies with visible exceptions, and the thread reports them as such. Whether the sharing is
the symmetry a cooperative-game treatment would predict for interchangeable veto players, or something
weaker, is not settled here — the within-set ratio sits near 0.78, not at 1. The scan is over random Boolean
forms at one seed, and the count of joint bottlenecks will move with the population. Everything is in-silico.
The result is the next step the four-party thread named: the joint bottleneck is real, its members each
inherit veto standing, and the credit they capture they share.
