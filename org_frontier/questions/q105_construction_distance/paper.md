# Q105 — Construction distance: building a triad is restoring liveness at a party

## Question

The program reads whether a form is triadic. Q93 read the collapse side of the dyad/triad boundary: a triad
is one edit from dyadic. The build side is unread. This study asks the inverse — how far a dyadic form is
from a triadic one, and where the edit that crosses the boundary sits — opening the program's prescriptive
turn from diagnosis to design.

## Method

The 256 strict-mediation forms are the 8-bit points of a hypercube: a two-bit read for each outer party off
the mediator (bits 0-3) and a four-bit mediator function (bits 4-7). A single-bit edit moves to a
Hamming-adjacent form, so the construction distance of a dyadic form is its minimal Hamming distance to any
of the 24 triadic forms. The distance is computed for all 232 dyadic forms, and for the distance-1 forms the
building bit is recorded as a mediator bit or a party's read.

## Results

The construction distance is 1 for 120 dyadic forms, 2 for 88, and 3 for 24, so ninety percent are within
two edits of a triadic form. Among the 120 distance-1 forms, a third are built by a mediator-bit edit and
two thirds at a party's read. The broadcast has distance 1, built at a mediator bit.

| construction distance | dyadic forms |
|---|---|
| 1 | 120 |
| 2 | 88 |
| 3 | 24 |

| | result |
|---|---|
| H1 broadcast one mediator-bit edit from a triad | confirmed |
| H2 most dyadic forms within distance 2 | confirmed (0.90) |
| H3 the distance varies | confirmed |
| H4 distance-1 builds at a mediator bit | refuted (0.33) |

## Interpretation

The dyad/triad boundary is thin from both sides. The construction distance and the fragility margin agree:
a triad is a few edits from a dyad either way, and most dyadic forms sit one or two edits from demanding the
competency. A coordination that does not demand algorithmacy is, almost always, a small intervention away
from one that does, which makes the competency a design target rather than a fixed property of a setting.

Building the triad restores liveness, not the binding. Two thirds of the single-edit builds are at a party's
read, not the mediator's function. The law has two conditions — the mediator reading all parties, and the
parties keeping themselves live to its commit — and on this family the first is usually already met: the
mediator structurally reads both parties, so the binding is present in most dyadic forms. What separates
them from the triad next to them is liveness, and the building edit supplies it at a party's read. The
broadcast, dyadic because its mediator does not read the counterpart, is the case where the build is at the
mediator; it is the exception, not the rule.

The design lever is therefore at the parties. A designer who wants a coordination to demand the competency
does not add a read to a mediator that already reads everyone; they close a loop at a party so it stays live
to the joint determination. This is Finding 3 read from the design side: liveness is the condition that most
often distinguishes a dyad from its neighbouring triad, so it is the condition a designer most often
supplies, and the one whose loss most often breaks a triad. The competency is built and broken at the
parties' reads more than at the hub.

## Limitations

In-silico; exact verdict over the strict-mediation family. That family has the mediator structurally able to
read both parties, so binding is common and liveness is the scarce condition; in a family where binding is
more often absent, the build would shift toward the mediator, and the parties-not-mediator result is for
this family. Construction distance is the minimal Hamming distance over the 8-bit encoding, counting bit
edits rather than a weighted design cost.
