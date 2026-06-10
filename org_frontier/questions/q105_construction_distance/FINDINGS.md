# Q105 findings — the boundary is thin from the build side, and triads are built at the parties, not the mediator

Three hypotheses confirmed, one refuted in the direction that teaches the most. A dyadic form is usually a
single edit from a triadic one, and almost always within two, so the dyad/triad boundary is as thin from the
build side as Q93 found it from the collapse side. But the building edit usually sits at a party's read, not
the mediator's function: most dyadic forms already have the mediator reading both parties and are dyadic
only because liveness is broken, so building the triad restores liveness rather than adding the binding.

| construction distance | dyadic forms |
|---|---|
| 1 | 120 |
| 2 | 88 |
| 3 | 24 |

Of the 232 dyadic forms, 0.90 are within distance 2. Among the 120 distance-1 forms, 0.33 are built by a
mediator-bit edit; the rest are built at a party's read. The broadcast has distance 1, built at a mediator
bit.

| H | Result | Verdict |
|---|--------|---------|
| H1 | the broadcast is one mediator-bit edit from a triad | confirmed |
| H2 | most dyadic forms are within construction distance 2 | confirmed (0.90) |
| H3 | the construction distance varies | confirmed (1, 2, 3) |
| H4 | distance-1 builds happen at a mediator bit | refuted (0.33) |

From `probe_construction_distance.py`.

## What it says

The build side of the boundary is thin. More than half the dyadic forms are a single edit from a triadic
one, and ninety percent are within two; the farthest is three (H2, H3). The construction distance is the
design dual of Q93's fragility margin, and the two agree on the shape of the boundary: it is thin from both
sides, a few edits wide. A coordination that does not demand the competency is, almost always, a small
intervention away from one that does.

Triads are built at the parties, not the mediator, and that is the substantive result. Only a third of the
single-edit builds are at the mediator's function; two thirds are at a party's read (H4 refuted). The reason
is the law's two conditions. The binding (the mediator reading all parties) is already present in most
dyadic forms, so it is not what the build adds. What is missing is liveness, the parties keeping themselves
live to the mediator's commit (Finding 3), and the building edit restores it at a party's read. The
broadcast is the exception that confirms this: it is dyadic because the mediator does not read the
counterpart, so its build is at the mediator (H1). But the broadcast is atypical; most dyadic forms fail on
liveness, and their build is at a party.

The design lever for algorithmacy is at the parties. A designer who wants a coordination to demand the
competency does not usually add a read to the mediator, which already reads everyone; they restore a party's
read that keeps it live to the joint determination. The competency is built by closing the loop at a party,
not by extending the hub. This reads Finding 3 from the design side: liveness is the condition that most
often separates a dyad from the triad next to it, so it is the condition a designer most often supplies.

## Caveats

- **Mixed result.** H1, H2, H3 confirmed; H4 refuted, the refutation locating the build at the parties.
- **Strict-mediation family.** The 256 forms have the mediator structurally able to read both parties; in a
  family where the binding is more often absent, builds would shift toward the mediator. The result is for
  this family, where binding is common and liveness is the scarce condition.
- **Hamming distance.** Construction distance is the minimal Hamming distance to a triadic form over the
  8-bit encoding; it counts bit edits, not a weighted cost. In-silico, exact verdict.
