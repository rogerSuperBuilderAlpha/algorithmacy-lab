# Q128 — The adaptive mediator: self-interest and irreducible coordination can coexist

## Question

Q126 found that a self-interested mediator with a fixed agenda erodes the coordination: a predatory system
that commits only its own objective, never reading the parties, drives the form to dyadic. But a real
platform's objective is not a fixed stance — it is learned from what the workers and counterparts do. Q128
asks whether adaptation rescues the bind. When the predatory mediator's objective is itself derived from the
parties, does the coordination stay irreducible, and does the objective become a member of the irreducible
core?

The model is four nodes — worker W, system S, counterpart C, objective O. The mediator is predatory in the
strongest sense, S' = O: it commits exactly its objective and never reads the parties directly. The parties
read the system, W' = S and C' = S. The objective updates by an adaptation rule O' = g(W, C), swept from no
adaptation (a frozen stance) to full.

## Method

For each adaptation rule the run reads exact Φ over the four-node system, the major complex, whether the
objective is in it, and how many parties are in it. The rules range over reading neither party (frozen),
one party (O' = W, O' = C), and both (O' = W ∧ C, W ∨ C, W ⊕ C). The control is the faithful three-party
triad. Full method in [`methods.md`](methods.md); hypotheses fixed before computing in
[`hypotheses.md`](hypotheses.md).

## Results

Adaptation re-integrates the coordination, but only when the objective reads both parties.

| adaptation O' | reads | structure | Φ_MIP | core | O in core | parties in core |
|---|---|---|---|---|---|---|
| O (frozen) | neither | dyadic | 0.000 | O | yes | 0/2 |
| W | W only | dyadic | 0.000 | WSO | yes | 1/2 |
| C | C only | dyadic | 0.000 | SCO | yes | 1/2 |
| W ∧ C | both | triadic | 1.000 | SCO | yes | 1/2 |
| W ∨ C | both | triadic | 1.000 | SCO | yes | 1/2 |
| W ⊕ C | both | triadic | 0.500 | WSCO | yes | 2/2 |

The predatory mediator is dyadic when its objective is frozen or tracks a single party, and triadic exactly
when its objective encodes both. Whenever the form re-integrates the objective is in the core; under the XOR
adaptation all four nodes — worker, system, counterpart, and the system's own objective — enter the
irreducible core. Raw output in [`results/output.txt`](results/output.txt).

## Interpretation

The fixed-agenda erosion of Q126 was not a fact about self-interest as such, but about a self-interest that
does not listen. A system that acts only on its own objective still binds the parties it coordinates,
provided that objective is learned from both of them. The binding no longer runs party-to-party through a
faithful mediator; it routes W, C → O → S → W, C. The parties shape the objective, the objective drives the
commit, and the commit returns to the parties, closing an irreducible loop that the objective sits inside.

The both-parties condition is the lab's core requirement appearing one level up. Irreducible coordination
needs both parties bound; a self-executing system meets that requirement only through an objective that
carries them both. An objective that attends to one party, or to none, cannot hold the coordination
together, however adaptive it is in form. So the question of whether an interested platform dissolves the
coordination it mediates turns on what its objective is a function of: learn from both sides and the bind
survives, with the platform's own goal now a constitutive part of it; learn from one side or neither and the
coordination factors.

## Limitations

Exact Φ on a four-node Boolean model; evidence about the construct and the instrument, not about a real
platform. "Objective", "agenda", and "predatory" label the update rules, not measured intent. The mediator
is the extreme case S' = O; intermediate mixtures of objective-serving and direct party-reading, an
objective with its own memory, and a slower adaptation timescale than the parties are the natural next
models.
