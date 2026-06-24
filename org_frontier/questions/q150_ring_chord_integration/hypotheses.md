# q150 — hypotheses

Setup: a conjunctive ring of six nodes, each node the AND of its two ring neighbors. One chord
joins the opposite pair A and D, giving each endpoint a third input, its chord partner. The chord
creates a shorter competing cycle (A-D-...-A through three nodes instead of the full six-node loop).

## H1 (fixed before computing)

One chord raises ring Φ and shifts the MIP cut off the chord onto the longer arc. The chord creates
a shorter competing cycle that is no longer the cheapest cut, so the minimum-information partition
should avoid severing the chord and the whole-system Φ should rise.

Null: the chord leaves Φ and the MIP cut unchanged.

H1 is read as a conjunction. Both the Φ rise and the cut shift must hold for support.

## H2 (fixed before computing)

The chorded nodes gain Shapley value at the expense of the far arc. A single long-range tie
redistributes captured Φ toward its endpoints, so A and D claim a larger share of the subsystem Φ
at the integrating state and the four far-arc nodes claim less.

Null: Shapley values are unchanged by the chord.

## Scope

In-silico. Both forms are synthetic Boolean coordination models. The study characterizes how an
exact-Φ read responds to one long-range tie. It does not measure integration or value capture in
any real group.
