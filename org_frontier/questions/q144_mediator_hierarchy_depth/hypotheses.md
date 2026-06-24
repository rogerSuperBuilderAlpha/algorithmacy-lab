# Q144 hypotheses — mediator hierarchy: depth versus breadth

A balanced k-ary mediator hierarchy is a tree of AND-gates feeding one apex. Leaves sit at the bottom,
internal mediators in the middle, a single apex on top. A feedback edge from the apex back to the leaves
closes the tree into a recurrent dynamical system, so the exact instrument has reachable states to read.
Two axes describe the tree: depth d, the number of mediator layers between a leaf and the apex; and
breadth b, the number of children each node has.

The scaling zoo fixes two laws to compare against. A serial chain holds Φ constant at 2. A fully-coupled
pool grows Φ as n(n-1). The question is which law the mediator tree follows along each axis.

## H1 (fixed before computing)

At fixed leaf count, adding mediator depth leaves Φ flat at the chain constant, because each layer is a
two-bit serial bottleneck.

Null: Φ rises or falls monotonically with depth at fixed breadth.

## H2 (fixed before computing)

At fixed depth, adding breadth grows Φ super-linearly toward the pool law, so breadth and depth are
separable axes with opposite scaling.

Null: breadth at fixed depth leaves Φ flat or decays.

## Scope

In-silico. Boolean dynamical models, exact IIT-4.0 Φ over the major complex. No party is measured. The
trees are synthetic constructions chosen to isolate depth and breadth; they do not model a fielded
organization, and the validation gap to real coordination stands. The result describes how Φ scales in
these constructions, not a fact about any human system.
