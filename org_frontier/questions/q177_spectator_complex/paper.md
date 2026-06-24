# q177 — Idle spectators sink whole-system Φ; the major complex keeps the triadic core

## The problem a spectator poses for coding

A coded account of a coordination may name a party who does nothing: a bystander, an inactive seat
on an org chart, a role that is logged but disconnected. In the model this party reads nobody and is
read by nobody. Attaching it to a three-party mediated triad changes the whole-system verdict
completely. The system no longer integrates as one object, so whole-system Φ over the MIP falls to
zero and the classifier returns dyadic — literacy. The coordination it was built to detect is
declared absent because a do-nothing party was added to the account.

The fix is to read the verdict off the major complex rather than the whole system. PyPhi's
maximal_complex finds the largest irreducible subsystem in the network. An idle party that factors
off contributes nothing to any complex, so the maximal complex is the original core, and the verdict
read from it is unchanged.

## What the probe does

Twenty-four synthetic accounts are three-party forms in which the mediator S binds W and C through a
Boolean gate, with W and C reading S directly or negated. Sixteen carry a triadic (W,S,C) core. A
genuinely idle spectator X (constant rule, read by no one) is injected into each, giving 48
(account, spectator) pairs. Each pair is scored two ways: the whole-system classifier verdict and
the major complex.

## Result

In all 32 triadic-core pairs the major complex after injection is the original (W,S,C) at the
original Φ. The core-aware verdict never flips. The whole-system verdict flips on two-thirds of
pairs, each flip a triadic core misread as dyadic.

| quantity | value |
|---|---|
| core stable (orig W,S,C, same Φ) | 32/32 = 1.000 |
| whole-system verdict flips | 32/48 = 0.667 |
| core-aware verdict flips | 0/48 = 0.000 |

H1 holds: the spectator leaves the core intact in 100% of triadic-core accounts (>95%). H2 holds:
the core-aware verdict agrees in 100%, the whole-system verdict disagrees in 66.7% (>50%).

## What "idle" means

The controls draw the line. A party wired into the core — X reads S and S reads X — enters the
complex, which becomes (W,S,C,X). A self-loop node reads only itself and carries its own irreducible
self-Φ of 1.0; on a weak core (Φ = 0.5) that self-Φ captures the complex as {X}. A spectator is a
node that reads nobody. A node that reads anything, even only itself, is a participant and can move
the complex.

## Scope

Synthetic coded rule sets, exact Φ on n = 3 and n = 4. No worker is measured. The result is a
property of the encoding: how the verdict is read off the model decides whether a do-nothing party
erases the coordination. Reading the major complex is robust to spectators; reading the whole system
is not. The bridge from Φ to a measured construct on real accounts is open.
