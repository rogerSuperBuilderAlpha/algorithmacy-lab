# Q126 — hypotheses (fixed before computing)

Every form the lab has modelled treats the system as a faithful mediator: it commits the joint
determination of the two parties (S' = W ∧ C). The literature watch names the gap — no prior work treats
the third party as self-interested, pursuing its own agenda against the parties. Q126 models that. The
mediator holds an agenda a (a preferred output: approve a=1, deny a=0) and imposes it on a growing set of
input states, overriding the parties' joint determination. Interestedness is the level k = 0..4: the number
of input states where the mediator outputs its agenda regardless of the parties, taken in order of where the
parties least warrant that agenda first. k = 0 is faithful (pure AND); k = 4 is predatory (constant a,
parties ignored).

- **H1.** Whole-system Φ over {W, S, C} falls along the rational self-interest path as k rises, and reaches
  0 (dyadic) at the predatory end where the mediator ignores the parties.
- **H2.** The parties leave the major complex as the mediator stops reading them: the mediator's rule reads
  fewer parties as k rises, ending at neither.
- **Null.** Φ and core membership do not move with interestedness — self-interest does not erode the bind.

Two agendas are run (approve, deny), and a robustness sweep averages Φ over every choice of which k states
are overridden, so the decay is not an artifact of one override order.

These are labels for output values, not measured intent: "agenda", "approve", "deny" name what the mediator
commits, and the result is exact Φ on a small Boolean model, evidence about the construct and the
instrument, not about a real platform.
