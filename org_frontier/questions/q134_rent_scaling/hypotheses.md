# Q134 — hypotheses (fixed before computing)

Q111 found the faithful mediator of the three-party triad captures two-thirds of the coordination's
integrated value, read as concentrated platform power. Q134 asks whether the two-thirds is scale-invariant.
The form is the conjunctive star: a mediator S commits iff all outer parties warrant it (S' = P1 ∧ … ∧ Pk),
each outer party reads S. The Shapley value distributes the system's Φ (which scales as Φ = n − 1).

- **H1.** The mediator's share is scale-invariant at two-thirds, independent of the number of parties.
- **H2 (alternative).** The share changes with scale, declining as parties are added — the additional
  parties dilute the mediator's slice while the total grows.
- **Null.** No interpretable trend.

Method: build the conjunctive star for k = 2, 3, 4 outer parties (n = 3, 4, 5); Shapley value of subsystem Φ
at the integrating state; the mediator's share and each outer party's share.
