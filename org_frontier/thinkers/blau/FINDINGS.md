# Blau — findings

Contingency is what makes power a relation. A supplier who serves regardless binds nothing — the Serres
arrow — and one whose service is contingent on compliance is a complex of two at Φ = 2.000 (H1 confirmed).
The supplier's position then falls in three steps as Blau's alternatives open. An alternative supplier
turns the dependent into the core's indispensable member and the suppliers into interchangeable ones: the
supplier's value added goes from 2.000 to 0 and its advantage from 0 to −2.000 (H2 confirmed; the form is the
Burt control broker seen from the contacts' side). Two subordinates who comply only together become the
core, {B1, B2} at 2.000, with the superior outside it and still indispensable (V(S) 2.000, advantage 2.000 →
0; H3 confirmed). Legitimation finishes it: when a subordinate complies because the peer does, the two keep
complying after the superior stops serving (011 → 111, where power gives 011 → 100), the subordinates are
the core at 2.000, and the superior's value added is 0 — outside and dispensable (H4 confirmed). Opposition
is not legitimation's mirror. Shared opposition rests with the superior yielding and the isolated
subordinates' opposition never rests, as Blau says; but disapproval binds the pair at 0.369 where approval
binds it at 2.000 (H5 partial). The superior's position across the five forms is a gradient: in the core and
indispensable (power); outside and indispensable (organized subordinates — Serres's position); outside and
dispensable (authority).

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | contingent service makes power a relation | **CONFIRMED** | independent: no complex; contingent: {S, B} 2.000 |
| H2 | an alternative supplier removes the superior's power | **CONFIRMED** | single V(S) 2.000, adv 0; alternatives V(S1) 0, adv −2.000, core {S1, S2, B} with V(B) 2.000 |
| H3 | organizing the dependent shifts power | **CONFIRMED** | S adv 2.000 → 0; B V 0 → 2.000; organized core {B1, B2} 2.000, V(S) 2.000 |
| H4 | legitimate authority is carried by the subordinates | **CONFIRMED** | authority 011 → 111, power 011 → 100; authority core {B1, B2} 2.000, V(S) 0 |
| H5 | opposition mirrors legitimation | **PARTIAL** | authority core {B1, B2} 2.000; opposition_shared core {B1, B2} 0.369; shared rests at 111, isolated never |

Instrument control passed in all five probes (Φ = 2.000000, core {A, M, B}).

## Caveats

- One rendering per alternative; the first (repay with a counter-service) and fourth (do without) were not
  modeled.
- The opposition forms are the Coleman paper's norm forms relabeled; their numbers were re-derived and
  agree.
- Value added reads a deleted variable as 0.
- In-silico; two- and three-node forms. No superior or subordinate is measured.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_contingent
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_alternatives
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_organized
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_authority
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_opposition
```
