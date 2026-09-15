# Heider — findings

Under signed majority with hold, Heider's balanced triads have no irreducible structure and his unbalanced
ones are maximal wholes. The two balanced sign patterns (+++ and +−−) have Φ = 0.000 and no complex, and
rest at the two states that satisfy every relation. The two unbalanced patterns (++− and −−−) have Φ = 6.000
with all three persons in the core, no state that satisfies every relation, and attractors that are six
frozen unsatisfied fixed points and one two-cycle. The eight sign patterns fall into exactly two structural
classes by sign product, as Cartwright and Harary said, but the class Heider called the unit is the one that
factors (H1 partial). Balance rests and imbalance does not (H2 confirmed). The all-negative triad is the
one-negative triad relabeled (H3 refuted). In a six-element form where relations are elements too, the core
is two persons and their relation, {p, o, Lpo} at Φ = 3.000: attitudes and relations do bind, as a dyad, and
every fixed point of the coevolution is a balanced rest state (H4 confirmed). On four persons, Φ does not
follow Cartwright–Harary's degree of balance: the balanced class and six of the seven unbalanced classes
have Φ = 0, and the one class with every person frustrated has Φ = 12.000 with all four in the core — at the
same b(G) = 3/7 as the six that factor (H5 refuted). Tension binds; balance dissolves.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | balance is a property of the sign product; the balanced class is the unit | **PARTIAL** | 2 classes, matching the product; Φ(balanced) = 0.000, Φ(unbalanced) = 6.000 |
| H2 | balanced triads rest; unbalanced have no rest state | **CONFIRMED** | balanced: 2 rest attractors each; unbalanced: 0 rest states, 6 frozen fixed points + 1 two-cycle each |
| H3 | −−− is a third kind | **REFUTED** | ppm and mmm: Φ 6.000 both, core 3 both, 7 attractors both |
| H4 | attitudes and relations make one whole | **CONFIRMED** | coevolving: Φ_MIP 0.000; core {p, o, Lpo} 3.000; 8 fixed points, all balanced rest states; 12 two-cycles |
| H5 | Φ rises with degree of balance on four persons | **REFUTED** | b = 1: Φ 0.000, core {c, d}; six classes at b = 3/7: Φ 0.000, single-node core; matching class at b = 3/7: Φ 12.000, core all four |

Instrument control (conjunctive triad, Φ = 2.000000, core {A, M, B}) passed in all five probes.

## Post-publication note (Davis paper, probes #424–#428)

The H3 verdict is withdrawn as an artifact of the alphabet. One bit per person is two camps. With a camp
alphabet of k ≥ 3 (`../davis/`), −−− rests in Davis's three-singleton partition and its core falls to two
persons at Φ = 2.000; ++− stays a whole of three at 6.000. The two unbalanced triads coincide only when a
third camp is denied.

## Caveats

- One rule: signed majority with hold (self-dual, symmetric in the two others, holds on a tie). Under a
  conjunctive rule (q214, probe #368) the all-positive triad read Φ = 6.0; the rule decides the verdict, and
  the paper says so.
- Synchronous update: the coevolving form's twelve two-cycles alternate attitude and relation updates and
  may be an artifact of simultaneity.
- Six-node form: about 2–4 minutes; the CI check is marked slow.
- Two implementation errors were caught before results were read into the paper: the K4 rule omitted the
  self vote (fixed to match `methods.md`), and the triangle count in `cycles_k4` was wrong (fixed). The
  triad results were unaffected by the first; H5 was recomputed after both.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_balance
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_tension
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_allnegative
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_coevolution
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_degree
```
