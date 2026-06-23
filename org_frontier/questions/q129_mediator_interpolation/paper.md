# Q129 — Faithful to predatory: an adaptive objective re-integrates the system by displacing a party

## Question

The interested-mediator arc has two endpoints. A faithful mediator commits the parties' joint determination
(S' = W ∧ C) and the coordination is irreducible. A predatory mediator commits only its own objective
(S' = O); Q126 found this erodes the coordination with a fixed agenda, and Q128 found an adaptive objective
makes the four-node system irreducible again. Q129 fills in between — the mediator serves its objective on m
of the four input states and commits faithfully on the rest — and asks where, along that interpolation, the
coordination survives, with the objective frozen and with it adaptive.

## Method

Four nodes: worker W, system S, counterpart C, objective O. At mix level m = 0..4 the mediator serves its
objective (S' = O) on m input states and commits S' = W ∧ C on the rest; the parties read the system. The
objective is frozen (O' = O) or adaptive (O' = W ∧ C). Because the objective can be a disconnected spectator
at low mix, two readings are taken at each m: the parties bound together in the major complex (the lab's
convention for forms with spectators), and the whole four-node system irreducible (Q128's measure). Both are
run along a fixed order and averaged over every choice of which states serve the objective. Full method in
[`methods.md`](methods.md); hypotheses fixed before computing in [`hypotheses.md`](hypotheses.md).

## Results

The two readings diverge and give opposite answers about which objective preserves the coordination.

Read as the parties bound in the irreducible core, a frozen objective holds the bind until full predation —
the major complex is {W, S, C} at Φ = 2.0 through m = 3, breaking only at m = 4 — while an adaptive objective
breaks it at the first step (m = 1 restructures the core to {S, C}, displacing the worker).

| m | frozen: parties bound? | adaptive: parties bound? |
|---|---|---|
| 0 | yes (WSC, 2.0) | yes (WSC, 2.0) |
| 1–3 | yes (WSC, 2.0) | no (SC, 0) |
| 4 | no (O, 0) | no (SCO, 0) |

Read as the whole four-node system irreducible, the answer flips. The frozen objective never makes the system
irreducible — it is a disconnected spectator. The adaptive objective makes it irreducible exactly at full
predation (m = 4, Φ = 1.0), Q128's result, but with core {S, C, O}: the system is irreducible because the
objective has joined it. Raw output in [`results/output.txt`](results/output.txt).

## Interpretation

The hypotheses assumed one notion of survival; the result is that the notion has to be named. An adaptive
objective is coupled — read by the system, reading both parties — so when the mediator serves it, the
objective enters the cause-effect structure and the major complex reorganizes around it, pushing a party out.
A frozen objective is disconnected and cannot join, so it leaves the parties' bind untouched until the
mediator stops committing the joint determination entirely.

This reconciles Q129 with Q128. Q128's re-integration is the system staying irreducible, not the two original
parties staying bound. Read as "are the parties still one irreducible whole," a frozen self-interest preserves
the coordination longer, because it never inserts itself; read as "is the system that now contains them
irreducible," an adaptive self-interest preserves it, by inserting itself. The displacement is the price of
the re-integration: the adaptive system keeps a triad, but it is the system, a counterpart, and the system's
own objective — the worker has been pushed to the edge.

The organizational reading is concrete. A platform that runs on a fixed rule erodes the coordination only
when it stops mediating altogether, and until then the worker and counterpart stay bound. A platform that
learns from both sides keeps an irreducible coordination going further, but the coordination it keeps is
increasingly between itself and one side, with the other displaced. Whether that counts as preserving the
coordination depends on whose coordination is being asked about.

## Limitations

Exact Φ on a four-node Boolean model; evidence about the construct and the instrument, not about a real
platform. The interpolation order matters, and both a fixed order and the order-averaged mean are reported.
The adaptive objective tested is O' = W ∧ C; OR and XOR adaptations re-integrate with different core
compositions (Q128). An objective with its own memory, or on a slower timescale than the parties, is the
natural next model and could change which party is displaced.
