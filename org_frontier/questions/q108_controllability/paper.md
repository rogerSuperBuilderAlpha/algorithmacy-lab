# Q108 — Controllability: the hub steers robustly, the spokes on a knife-edge

## Question

Q106 named the design levers and Q107 showed repair is lever-specific. Control asks which party, if a
designer can set only its reads, the verdict can be steered from, and how robustly. A control node is a
party from which both verdicts are reachable; the mediator and the outer parties may differ as control
points because their function spaces differ.

## Method

Starting from the read-recipient triad, each party's function is varied over all its settings while the
others stay fixed, and the triadic settings are counted. The worker and counterpart sweep four one-input
functions each; the mediator sweeps sixteen two-input functions.

## Results

Every party reaches both verdicts, so all three are control nodes. The mediator has six triadic-preserving
settings of sixteen; each outer party has exactly one of four — its live read.

| party | triadic settings / total |
|---|---|
| worker | 1 / 4 |
| counterpart | 1 / 4 |
| mediator | 6 / 16 |

| | result |
|---|---|
| H1 mediator is a control node | confirmed |
| H2 each outer party is a control node | confirmed |
| H3 mediator is dominant | confirmed |
| H4 outer parties are knife-edge | confirmed |

## Interpretation

The coordination is controllable from any position, but not equally. From the mediator, six of sixteen
functions hold the triad, so the hub has a wide band of triad-preserving settings and a designer steers most
freely there. From an outer party, one of four reads holds the triad (the live read) and the other three
break it, so the spoke holds the coordination on a single setting. The hub steers robustly; the spokes steer
on a knife-edge.

The knife-edge is Finding 3 read as control. Liveness is one condition, supplied by one read: a party is
live only if it reads the mediator as it is, so the live read is the unique setting that keeps the party
bound, and any other read drops it out. A party therefore cannot vary its read and keep the triad; its
control over the verdict is the power to break it by moving off the live read, not the freedom to hold it
across settings. The mediator, binding rather than supplying liveness, has the richer function space and the
wider hold.

The asymmetry frames the wave. Building a triad is located at the parties (Q105) because supplying a
missing live read is the common build, and the parties are load-bearing (Q104) because their single live
read is the one the triad hangs on. Control completes the picture: toward the triad, control concentrates at
the hub, where many settings hold; toward the dyad, control is available at every spoke, where all but one
setting breaks it. For a defender, the lesson is that the parties are the soft control surface — a single
read away from collapse — while the mediator is the hard one.

## Limitations

In-silico; exact verdict over the strict-mediation family. Control is read from one base form, the
read-recipient triad; the live-read requirement for the parties is general, but the exact counts could
shift on another form. The sweep varies one party at a time; joint control by two parties at once is
untested.
