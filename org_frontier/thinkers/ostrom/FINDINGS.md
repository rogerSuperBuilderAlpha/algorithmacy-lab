# Ostrom — findings

When the monitored are the monitors, the monitored are the structure. In a form where each of three
appropriators complies if the others comply or if the other two jointly sanction, and sanctions when either
other defects, the major complex is the three compliance nodes at Φ = 2.862 and the whole of six is
irreducible at 0.830; every appropriator is in, and the sanction bits sit outside the core each adding 0.862
(H1 confirmed). Coleman's closed norm, run beside it, has the two sanctioners as the core and the sanctioned
party outside. The same form rests at all-comply with no sanction standing, and each single lapse returns to
that rest in four steps; Coleman's form rests only with the sanction standing (H4 confirmed). Self-governance
— a clique of contingent commitments — is a whole of three at 6.000 against the enforcer's star at 3.000,
but the enforcer holds no edge (every member of the star adds 3.000), and privatization leaves each
self-holding appropriator a complex of one at 1.000 (H2 partial). Nesting two such cliques under a
federation does not make the seven one: the nest is irreducible at 2.000 and exclusion returns a single
local clique at 6.000; the federation is outside the core and indispensable (value added 6.000), the
delegates add 4.000, the rank and file 0 (H3 refuted; both local cliques are irreducible at 6.000 at the
all-on state, post hoc). A defined boundary works — an outsider who watches and is not read changes nothing
and adds nothing — but a breach does not change the core or its Φ; it makes the outsider indispensable at
6.000 while leaving him outside (H5 partial). Three patterns recur from earlier papers: mutual monitoring
keeps everyone in where Coleman's one-way sanction did not; nesting reproduces the Coleman parents result
one level up; and the party outside the complex and necessary to it is Serres's.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | the monitored are in the structure | **CONFIRMED** | mutual core {c1, c2, c3} 2.862, whole 0.830, every V 0.862; coleman_closed core {B, C}, A out |
| H2 | self-governance > Leviathan; enforcer has the edge; division binds nothing | **PARTIAL** | self 6.000 (all in) vs leviathan 3.000 (all four in, all V 3.000, L advantage 0); private: singleton self-hold complexes at 1.000 |
| H3 | nested layers are one whole, each layer still a whole | **REFUTED** | nested Φ_MIP 2.000, core {a1, a2, a3} 6.000; V: F 6.000, a1 b1 4.000, others 0; unnested two triads |
| H4 | compliance rests with the sanction retired | **CONFIRMED** | mutual fixed point 111000 only; lapses return in 4 steps; coleman_closed fixed point 111 |
| H5 | a boundary keeps the outsider out; a breach changes the whole | **PARTIAL** | bounded: core and Φ unchanged, V(O) 0; breached: core and Φ unchanged, V(O) 6.000 |

Instrument control passed in all five probes (Φ = 2.000000, core {A, M, B}).

## Post-hoc (disclosed)

- H3's second clause evaluated the local triads at the state where the whole's major complex is maximal
  (1110001, group b off); at 1111111 both triads have subsystem Φ = 6.000, {a1, a2, a3, F} has 2.000, and
  {a1, b1, F} has 2.000 (`results/posthoc_nested_allon.json`). The refutation stands on the first clause.

## Caveats

- H2's privatization clause failed on PyPhi counting a self-holding node as a complex of one; "binds
  nothing" should have been written as "no complex above one."
- H5's breach clause asked for a change in core or Φ; the breach changed neither and changed value added
  instead. The hypothesis under-specified the quantity.
- The mutual form's sanction lifts on compliance without memory; graduated sanctions were not modeled.
- A deleted variable reads 0, so deleting F or O collapses any conjunction that read it.
- In-silico; three- to seven-node forms. No commons is measured.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_monitors     # ~5 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_solutions
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_nested       # ~10 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_compliance
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_boundary
```
