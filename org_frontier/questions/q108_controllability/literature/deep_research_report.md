# Q108 literature — control nodes

## From operations to control

Q106 named the design levers; Q107 showed repair is lever-specific. Control asks a related question: if a
designer can set only one party's reads, from which party can the verdict be steered, and how robustly?
A control node is a party from which both verdicts are reachable. The mediator and the outer parties differ
in their function spaces — the mediator has sixteen two-input functions, each outer party four one-input
functions — so they may differ as control points.

## The expected control structure

The law predicts the shape. The mediator binds the parties, and its richer function space should give it
more ways to maintain or reach a triad, making it the dominant control node. The outer parties supply
liveness, which Finding 3 makes a single condition: a party is live only if it reads the mediator as it is,
so only the live read preserves the triad and any other breaks it. The outer parties should therefore be
knife-edge controls — able to steer the verdict but not to hold the triad against a change of their read.

## Method context

The sweeps vary one party's function over the 256-form encoding and read the verdict, with no perturbation
simulation.
