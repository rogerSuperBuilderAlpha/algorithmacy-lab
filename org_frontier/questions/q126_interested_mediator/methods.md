# Q126 — methods

## The model

The triad W (worker), S (system/mediator), C (counterpart), with W' = S and C' = S (the parties read the
system) and S' an interested mediator of the two parties' inputs. The faithful mediator is the joint
determination S' = W ∧ C — commit only when both parties warrant it, the canonical strict-mediation triad
(triadic, Φ_MIP = 2.0, core {W, S, C}), used as the control.

An interested mediator holds an agenda a ∈ {1 (approve), 0 (deny)} and imposes it. At interestedness level
k = 0..4 it outputs a, regardless of the parties, on the k input states where the parties least warrant a,
and commits the faithful AND elsewhere. Warrant for approve is the number of parties on; warrant for deny is
the number off. So an approve agenda overrides first the states with the fewest parties on, and a deny
agenda overrides first the states with the most on — the parties' point of agreement. k = 0 is faithful;
k = 4 is the constant mediator that ignores the parties.

## Measures, per level

- **Φ_MIP and structure** — exact IIT-4.0 Φ over the whole system via the lab's classifier; triadic when
  Φ_MIP > PHI_EPS in some reachable state.
- **major complex** — the irreducible core and which parties remain in it.
- **parties read** — which of W, C the mediator's rule actually depends on, by the connectivity-matrix flip
  test (`cm_from_rules`).

## Robustness — order-averaged decay

The level-k override set above takes the least-warranted states first (the rational self-interest path). To
check the decay is not an artifact of that order, Φ is also averaged over every C(4, k) choice of which k
states the agenda overrides, for each k and each agenda.

## Reproduce

```
python -m org_frontier.questions.q126_interested_mediator.probe_interested_mediator
```

Output is saved in [`results/output.txt`](results/output.txt). The run is a few seconds (three nodes).
