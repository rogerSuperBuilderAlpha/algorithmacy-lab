# q171 — Drift Binding with an Agenda: Whether the Two Opacities Stack

A mediator stands between two parties and commits their joint determination. The lab has modelled two
ways it can stop being faithful. It can drift, retraining on what it is fed so its rule is a moving
target. It can be interested, imposing its own agenda on the states where the parties least warrant it.
This study puts both on the same mediator and asks whether the two erosions of the binding add.

## The construction

The mediator triad has the worker W, the system S, and the counterpart C. The parties read S faithfully.
S's commit rule carries the opacity. Drift d follows the predictive-processing battery: the faithful
gate W ∧ C fires with probability (1 − d) and a flipped rule W ∨ C with probability d. Interest k
follows the Q126 mediator: the agenda a overrides the k least-warranted (W, C) states, the faithful arm
runs elsewhere. The bridge crosses them, applying the drift only to the faithful arm, the states the
parties still rule. Whole-system Φ at each cell is the exact maximum big-Φ over states.

## What the sweep finds

Two predictions were fixed before computing. The first held that combined Φ would fall below the product
of the two separate decays: drift and agenda destroying the binding super-additively. The sweep refutes
it. At every interior cell the combined Φ sits above the multiplicative null, not below. At approve
d = 0.5, k = 1 the combined Φ is 0.415 against a null of 0.052. The two opacities are sub-additive.

The second prediction held that drift would sometimes raise Φ on an interested mediator. The sweep
supports it. Under the deny agenda at k = 1 the pure-interest baseline is Φ = 0, because overriding the
one state where the parties warrant the commit removes all party-dependence. Drift restores it: Φ climbs
from 0 to 0.415 as d rises to 0.5. Retraining partially re-integrates an interested mediator.

## Why one masks the other

Interest erodes the binding by deleting party-dependence in the states it overrides. Drift erodes it by
averaging the faithful states toward a coin flip. The two act on different states. Where interest has
already flattened a state, drift has nothing left to erode there, so the joint effect is milder than the
product. On the deny agenda the interaction reverses sign: the agenda removes the dependence in one
state, and the drift puts dependence back into the others, lifting Φ off the floor.

## Scope

The model is three Boolean nodes read with exact Φ. The finding is a property of how the two
constructions compose. No worker, mediator, or platform is measured. The empirical reading is on
synthetic data. The contribution is what the instrument shows about the structure of combined opacity,
a question the binary commit/convey verdict cannot reach on its own: that two routes to a noisy commit
can cancel rather than compound.
