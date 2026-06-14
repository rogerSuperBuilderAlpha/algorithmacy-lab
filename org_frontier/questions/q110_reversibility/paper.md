# Q110 — Reversibility: the boundary is cheap toward the dyad, dear toward the triad

## Question

Q93 read the collapse side of the dyad/triad boundary and Q105 the build side. Hamming distance is
symmetric form to form, so the boundary's shape is a distributional question: are triads as far from dyads
as dyads are from triads, or is the boundary thin from one side and thicker from the other? This closes the
design wave by comparing the two distributions.

## Method

The 256-form family is classified into 24 triadic and 232 dyadic forms. The fragility margin of a triadic
form is its minimal Hamming distance to any dyadic form; the construction distance of a dyadic form is its
minimal Hamming distance to any triadic form. The two distributions are compared.

## Results

Every triadic form has fragility margin 1; the construction distances are 1 for 120 dyadic forms, 2 for 88,
and 3 for 24. The fragility margin is uniformly 1, mean 1.00; the construction distance varies, mean 1.59.

| direction | distribution | mean |
|---|---|---|
| break a triad | {1: 24} | 1.00 |
| build a triad | {1: 120, 2: 88, 3: 24} | 1.59 |

| | result |
|---|---|
| H1 every triad one edit from a dyad | confirmed |
| H2 not every dyad one edit from a triad | confirmed |
| H3 the boundary is asymmetric | confirmed |
| H4 building costs more than breaking | confirmed |

## Interpretation

The dyad/triad boundary is asymmetric, and the asymmetry favors destruction. A triad is always one edit
from a dyad: every triadic form has a dyadic neighbour, so a single perturbation breaks any coordination
that demands the competency. A dyad is one to three edits from a triad: most dyadic forms are two or three
moves from one that demands it, so building the competency usually takes more than a single edit. Breaking
costs one move; building costs 1.59 on average. The boundary is thin where a triad sits and thicker where a
dyad does.

The asymmetry is structural, not metric. Hamming distance is symmetric, so a triad one edit from a dyad
means that dyad is one edit from a triad. What differs is the density of forms on each side: triadic forms
are the 9.4% minority and sit among the dyadic majority, so each is surrounded by dyads and breakable in one
move, while the dyadic forms are the many and are not all adjacent to the few triads, so building one often
requires reaching across two or three edits. The asymmetry is the shadow of the rarity of irreducible
coordination.

This states the design wave's through-line as a number. Every edge of the minimal triad is load-bearing
(Q104), the build is usually at a party (Q105), the levers are three (Q106), repair is lever-specific
(Q107), and the parties are knife-edge controls (Q108). All say the triad is held by exact conditions that
a single move can remove. Q110 totals it: removing a condition is one edit, and supplying one is more.
Algorithmacy is cheap to break and dear to build, so a designer's task of installing it, and a defender's of
keeping it, is structurally harder than an adversary's of removing it. The competency, once built, sits one
perturbation from loss.

## Limitations

In-silico; exact verdict over the strict-mediation family. The family's 9.4% triadic density drives the
asymmetry; a denser family would lower the construction distances, though the fragility margin stays near 1
while triads are rare. Both distances are Hamming distances over the 8-bit encoding, counting bit edits
rather than a weighted design cost.
