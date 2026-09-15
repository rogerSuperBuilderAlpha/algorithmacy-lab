# Girard — findings

Girard's triangle is never a whole of three. With subject, mediator, and object as nodes and imitation as
reading, single internal mediation has as its major complex the mediator and the object, {M, O} at Φ = 2.000,
and the subject — whose desire is a copy of the mediator's — is outside it and dispensable (share 0). Double
mediation has as its complex the two rivals, {S, M} at 2.000, and the object is outside and dispensable
(share 0); the pair's Φ is exactly the bare dyad's. External mediation binds nothing across the spheres.
As the mediator draws nearer — reading the subject with probability 0.25, 0.5, 0.75, 1 — the rivals' complex
forms at p = 0.5 and rises 1.000 → 1.500 → 2.000, and the object enters at no distance. Two pre-registered
hypotheses fell: H1 (subject and object one through the mediator) — they are not, the subject is out; H2
(internal core = the triad) — it is {M, O}, and the external clause tripped on a self-holding source counted
as a one-node complex. Girard's own line on p. 2 states the result: "the triangle is no Gestalt. The real
structures are intersubjective." The instrument names which pair.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | subject and object are one through the mediator | **REFUTED** | internal core {M, O} 2.000, S out (whole 1.000); minus M: no complex ✓ |
| H2 | external: no contact; internal: three one | **REFUTED** | external: S, O not one ✓ but M alone is a self-holding one-node complex (1.000), clause failed; internal core {M, O}, not the triad |
| H3 | the object is a means of reaching the mediator | **CONFIRMED** | double core {S, M} 2.000 = dyad 2.000; O out |
| H4 | distance | **CONFIRMED** | core Φ over p = .25/.5/.75/1: 0 (M alone) → 1.000 → 1.500 → 2.000; O in core at no p |
| H5 | doubles | **CONFIRMED** | double shares S 2.000, M 2.000, O 0; internal shares S 0, M 2.000, O 0 |

Instrument control passed in all five probes (Φ = 2.000000, core {A, M, B}; stochastic path 2.000000 in H4).

## Caveats

- One rendering: S copies M; O = M ∧ S; internal M = S ∧ O; double M = S. A mediator who reads the object
  disjunctively, or an object valued by either party, would be different forms.
- The external clause of H2 failed on the self-holding-source artifact (a held node is a one-node complex at
  Φ = 1); S and O are not one, as Girard says.
- Escalation ("with every cycle it increases in intensity") is not representable in Boolean states.
- In-silico; two- and three-node forms. No novel or reader is measured.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_triangle
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_mediation
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_object
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_distance
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_doubles
```
