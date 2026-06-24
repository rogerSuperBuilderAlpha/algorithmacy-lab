# Q140 — hypotheses (fixed before computing)

The Shapley value distributes a coordination's value by marginal contribution (Q111). The core asks which
allocations are stable — no sub-coalition can break away and do better. Q140 computes the core of the
mediated triad and asks what an interested mediator does to it. The value of a coalition is its subsystem Φ;
the core is {x : x(N) = v(N), x(S) ≥ v(S) ∀S}.

- **H1.** In the faithful coordination the core gives the parties nothing: because either party with the
  mediator reaches the full value (v(WS) = v(SC) = v(N)), each party is substitutable, and the only stable
  allocation hands the mediator everything. The Shapley two-thirds understates the mediator's structural power.
- **H2.** As the mediator turns interested and sub-coalition values fall to zero, the core expands to the whole
  simplex: any split of the reduced value is stable, so the parties can keep all of it.
- **Null.** The core is unchanged by interest.

Method: the Q126 interested mediator (AND, approve) at k = 0, 1; the value of every coalition at the
integrating state, and the parties' maximum collective core payoff.
