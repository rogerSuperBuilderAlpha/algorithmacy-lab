# Q126 — The interested mediator: self-interest erodes coordination irreducibility

## Question

Every coordination form the lab has modelled treats the system as a faithful mediator: it commits the joint
determination of the two parties, S' = W ∧ C, committing only when both warrant it. The literature watch
names the gap this leaves — no prior work treats the third party as self-interested, a system that pursues
its own agenda against the parties it coordinates. Q126 models that system and asks what exact Φ does as it
serves itself.

There are two opposite intuitions. One says a self-interested system becomes a stronger, more autonomous
player, binding the parties more tightly to it and raising Φ. The other says self-interest is corrosive: a
system committing its own agenda stops genuinely mediating between the parties, and the coordination loses
its irreducibility. The instrument settles which.

## Method

The triad is W (worker), S (system), C (counterpart), with W' = S, C' = S, and S' an interested mediator
of the two parties. The mediator holds an agenda a — approve (a = 1) or deny (a = 0) — and imposes it at
interestedness level k: it outputs a, regardless of the parties, on the k input states where the parties
least warrant a, and commits the faithful AND elsewhere. k = 0 is faithful (the canonical triad, the
control); k = 4 ignores the parties entirely. For each level the run reads exact Φ over {W, S, C}, the
major complex, and which parties the mediator's rule still depends on. A robustness sweep averages Φ over
every choice of which k states are overridden. Full method in [`methods.md`](methods.md); hypotheses fixed
before computing in [`hypotheses.md`](hypotheses.md).

## Results

Self-interest erodes the coordination. Along the rational path — the mediator overriding first where the
parties least warrant its agenda — Φ falls to zero, the parties drop out of the core, and the form goes
dyadic. Φ never rises.

| k | approve: Φ / structure / core | deny: Φ / structure / core |
|---|---|---|
| 0 | 2.000 / triadic / WSC | 2.000 / triadic / WSC |
| 1 | 0.500 / triadic / WSC | 0.000 / dyadic / (none) |
| 2 | 0.000 / dyadic / WS | 0.000 / dyadic / (none) |
| 3 | 0.000 / dyadic / (none) | 0.000 / dyadic / (none) |
| 4 | 0.000 / dyadic / (none) | 0.000 / dyadic / (none) |

The asymmetry between the two agendas is the sharp finding. A **denying** mediator collapses the bind at the
first override. Overriding toward deny starts at the parties' point of agreement — the one state where both
warrant a commit — and removing it leaves the mediator constant, so the coordination factors at once. An
**approving** mediator tolerates one override, its Φ dropping to 0.5 while still triadic, before collapsing
at k = 2. Gatekeeping self-interest corrodes faster than permissive self-interest.

Averaging Φ over every choice of which states are overridden confirms the decay is not an order artifact and
sharpens the asymmetry: deny falls linearly (2.0, 1.5, 1.0, 0.5, 0.0), each overridden state removing a
fixed share of the binding, while approve is non-monotone (2.0, 0.625, 0.417, 0.500, 0.0) because some
approve-override sets build parity-like mediators that re-integrate the parties. Permissive self-interest
has accidental re-integration pockets; gatekeeping self-interest is cleanly corrosive. Raw output in
[`results/output.txt`](results/output.txt).

## Interpretation

The system's power to bind two parties into one irreducible joint determination is a property of faithful
mediation. When the system commits its own agenda instead, it reads the parties less, they fall out of the
irreducible core, and the triadic coordination factors into a dyadic one. The conjecture that an interested
system becomes a stronger autonomous player with higher Φ is refuted on this model: Φ falls, not rises.
Self-interest does not make the platform a bigger part of the coordination — it dissolves the coordination
the platform was mediating.

The agenda asymmetry gives the reading its edge. A gatekeeper — a system whose self-interest is to deny —
overrides the parties exactly where they agree, and that is the most disintegrating move available: it
destroys the bind at the first step. A permissive system, whose self-interest is to approve, can impose its
agenda in low-warrant states without immediately breaking the coordination, and can even, by accident,
re-integrate the parties through a parity-like rule. Self-interest erodes coordination irreducibility, and
denial erodes it fastest.

## Limitations

Exact Φ on a three-node Boolean model; evidence about the construct and the instrument, not about a real
platform. "Agenda", "approve", and "deny" label committed output values, not measured intent. The faithful
baseline is AND; an OR baseline ("commit iff either party warrants") would relabel which states each agenda
overrides and is the natural robustness extension. The agenda here is a fixed stance; a self-interested
system that adapts its agenda to the parties — a learning intermediary — is a separate model and the natural
next question.
