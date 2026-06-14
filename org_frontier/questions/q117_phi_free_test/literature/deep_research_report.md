# Q117 — Stage 2 literature: a Φ-free test for an integrated-information verdict

## The question in context

Q117 asks whether the program's exact-Φ verdict has a closed-form surrogate: a predicate, computed from the
form's truth tables without running PyPhi, that reproduces the verdict with no error. The motivation is both
practical (exact Φ is exponential; a structural test would be cheap) and theoretical (a necessary-and-
sufficient structural condition is a law, where an oracle is a black box).

## What the program and the field already establish

- **Triadic forms carry a feedback cycle.** The probe loop found the integration of the strict-mediation
  triad rides a cycle through all three parties (probes 25, 39), with a 4-edge minimum at n=3 (probe 35).
  The cycle is the natural candidate for a necessary condition.
- **Cheap dependence measures fail.** O-information, PID terms, and pairwise sensitivity do not separate the
  verdict (probes 45-47). This warns that a sufficient condition, if one exists, is unlikely to be a simple
  correlational quantity, and is more likely a logical property of the determination.
- **Integrated information is not generally reducible to connectivity.** IIT distinguishes a system's causal
  structure from its wiring diagram: the same connectivity can carry different Φ depending on the mechanisms
  (Albantakis et al. 2023). This predicts that topology alone will underdetermine the verdict, and that the
  deciding property lives in the truth tables.
- **Canalization and the logic of the update matter.** Whether a Boolean function is degenerate, canalizing,
  or genuinely combinatorial governs how information is integrated (the Boolean-network tradition). A Φ-free
  test, if it exists, should turn on such a logical property of the mediator and its composition with the
  outer reads.

## The gap Q117 fills

The program has the cycle as a candidate necessary condition and a warning that connectivity will not
suffice, but it has never tested a Φ-free predicate against the oracle on a complete family, nor found the
logical condition that would close a necessary condition into a sufficient one. Q117 enumerates the whole
256-form family and asks whether topology decides the verdict, and if not, what logical composition does.
