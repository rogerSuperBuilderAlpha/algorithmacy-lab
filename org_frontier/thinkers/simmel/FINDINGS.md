# Simmel — findings

Simmel's triad is a superindividual whole when its members are mutually necessary, not when they are three or
can outvote one another: the mutual triad binds at Φ = 6.0 against the dyad's 2.0 and the pair stays bound
through the third when its direct tie is cut (H1 confirmed); the majority triad has no irreducible structure
at all, Φ = 0 (H3 refuted); Φ grows as n(n−1) across cliques so the 2→3 step is not distinguished (H2 refuted);
the mediator binds exactly as much as the arbitrator and leaves the core once his parties unite directly (H4
partial); and the *tertius gaudens* holds the core alone — {T, O} — when the contestants are balanced, tracking
influence 0.75 → 0.50 → 0.25 (H5 confirmed).

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | superindividual triad | **CONFIRMED** | dyad 2.000 {A,B}; triad 6.000 {A,B,C}; broken line 2.000 {A,B,C}; cut dyad 0.000 |
| H2 | 2→3 is the decisive step | **REFUTED** | Φ = 2, 6, 12, 20 for n = 2..5; ΔΦ = +4, +6, +8 |
| H3 | majority binds all three | **REFUTED** | majority triad Φ = 0.000, no complex; unanimity 6.000 {A,B,C} |
| H4 | arbitrator > mediator > eliminated | **PARTIAL** | M in, in, out; Φ 2.000, 2.000, 0.000 (pair remains at 2.000) |
| H5 | third's standing tracks the balance | **CONFIRMED** | infl(T) .750/.500/.250; core {T,O} 2.000 → {T,O} 0.277 → {A,O} 2.000 |

Instrument control (conjunctive triad, Φ = 2.000000, core {A, M, B}) passed in all five probes.

## Caveats

- One Boolean rendering per claim; alternatives named in `paper.md` Limitations were not run.
- In-silico: models of three to five binary elements, not groups of people. Clique sweep stops at n = 5.
- The post hoc proportional reading of H2 (ratios 3, 2, 1.67) is reported and does not change the verdict.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_superindividual
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_number 5
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_majority
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_nonpartisan
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_gaudens
```
