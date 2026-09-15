# Granovetter — findings

Weak ties transmit; only weak ties that return integrate. With a tie rendered as Granovetter defines it —
symmetric, graded, read each step with probability p — the Φ of a dyad rises smoothly with strength,
0.252 → 0.658 → 1.236 → 2.000 at p = 0.25, 0.5, 0.75, 1 (H1 confirmed). The forbidden triad is the
conjunctive triad at Φ = 2.000; closing it with a weak tie lifts it to 2.830 and with a strong one to 6.000,
all three members in every core (H2 confirmed). A bridge between two strong dyads, weak or strong, gives 12
transmitting pairs and no complex that spans them: the major complex is one dyad at 2.000, and the bridged
whole reaches 0.830 (weak) or ties at 2.000 (strong) (H3 refuted). Cutting the weak bridge costs eight
transmitting pairs against six for a strong tie, and neither cut moves the major complex (H4 partial). Three
strong dyads joined in a weak chain remain a dyad's complex; joined in a weak ring they are one whole of six
at Φ = 2.490, and in a strong ring at 4.000 (H5 partial). Granovetter's integration is a path; the
instrument's is a cycle. The two agree wherever the weak ties close.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | strength is graded | **CONFIRMED** | dyad Φ 0.252 / 0.658 / 1.236 / 2.000 at p = .25 / .5 / .75 / 1 |
| H2 | the forbidden triad closes, weak below strong | **CONFIRMED** | open 2.000 < weak-closed 2.830 < strong-closed 6.000; core {A,B,C} each |
| H3 | a weak bridge joins two cliques as a strong one does | **REFUTED** | reach 12 both; major complex {b1,b2} 2.000 both; whole Φ_MIP 0.830 (weak), 2.000 (strong, tie) |
| H4 | cutting the weak bridge does more damage | **PARTIAL** | transmission: bridge −8 vs strong −6; major-complex Φ: 0 lost either way (whole Φ_MIP 0.830 → 0 either way) |
| H5 | weak ties between cliques make the community one whole | **PARTIAL** | chain: core {a1,a2} 2.000, whole 0.830; ring: core all six 2.490; strong ring 4.000; isolated: whole 0 |

Instrument control passed in all five probes on both checks (rules: Φ = 2.000000, core {A, M, B}; ties:
Φ = 2.000000).

## Caveats

- One rendering of strength (read probability, AND-of-read, hold when nothing read). Weak = 0.5 throughout.
- H1 and H3 numbers were seen in the machinery check before H2–H5 were fixed (`methods.md`).
- H3's strong bridge ties whole and part at 2.000; exclusion picks the part.
- H4's integration measure (major-complex Φ) is masked by the surviving dyad; whole-system Φ_MIP falls
  from 0.830 to 0 under either cut.
- In-silico: two- to six-node forms; stochastic TPMs; the six-node ring takes ~3 minutes.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_strength
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_triad
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_bridge
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_damage
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_community
```
