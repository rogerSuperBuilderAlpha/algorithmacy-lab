# Bowen — findings

Bowen's triangle, rendered with togetherness as reading and anxiety as flip noise, is not a whole of three:
it is a twosome that can move. In calm the major complex is the insiders {A, B} and the outsider C is out.
When the uncomfortable insider A involves C, the complex becomes {A, C} at Φ = 2.000 and B is the new
outsider — the third displaces an insider rather than joining (H2 refuted as pre-registered; the shift is
Bowen's own positional rotation). Under uniform anxiety the triangled form retains a smaller fraction of its
Φ than the dyad at every ε (0.794 vs 0.836 at ε = 0.05; 0.167 vs 0.238 at 0.3) and its core is never the
triad (H1 refuted). Anxiety at the outsider costs the whole least — 0.100 against 0.237 at ε = 0.1 — and
anxiety at C alone sends the core back to {A, B}: the anxious party is the one left out (H3 confirmed). Four
parties interlocked are one complex of four at ε = 0 (Φ = 2.000) and a triangle {A, C, D} at every ε > 0,
retaining less than the three (H4 refuted as pre-registered; the triangle appears under anxiety). A neutral
third — read by both, reading both, holding — is outside the complex where a reactive third is inside at
Φ = 6.000, and the twosome retains no more with it than alone (H5 partial). Only the fully reactive
triangle, where both insiders involve the third, is a whole of three; it holds more absolute Φ than the dyad
at every ε and a smaller fraction.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | the triangle is the smallest stable system | **REFUTED** | fraction retained, triangled vs dyad: .794/.836, .618/.687, .347/.434, .167/.238; triangled core {A,C} at every ε |
| H2 | calm twosome + outsider; tension involves the third | **REFUTED** | calm core {A,B} ✓; triangled core {A,C} at 2.000, whole 1.000 — B displaced, not C joined |
| H3 | under stress the outside position costs least | **CONFIRMED** | loss at ε=.1: A .237, B .237, C .100; at .2: .458, .458, .200; anxiety at C moves the core to {A,B} |
| H4 | interlocking triangles | **REFUTED** | ε=0: core {A,B,C,D} 2.000; ε>0: core {A,C,D}; fraction four vs three .728/.794, .520/.618, .244/.347, .097/.167 |
| H5 | detriangling | **PARTIAL** | (a) neutral C out, reactive C in (6.000) ✓; (b) insiders' core fraction with neutral third vs dyad: .836/.836, .686/.687, .423/.434, .210/.238 ✗ |

Post hoc (not a verdict): the reactive triangle stays {A, B, C} at every ε, Φ 6.000 → 4.600 → 3.466 →
1.832 → 0.831; absolute Φ above the dyad's throughout, fraction below (.767 vs .836 at ε = 0.05).

Instrument control passed in all five probes on both checks (rules: Φ = 2.000000, core {A, M, B}; noise
path at ε = 0: Φ = 2.000000).

## Caveats

- One rendering: conjunctive reading, flip noise, hold-when-neutral. "Triangled" = one insider involves the
  third; "reactive third" = both do. The two give different verdicts on whether the triangle is a unit.
- Stability was pre-registered as fraction retained; absolute Φ favors the joint triangle over the dyad.
- H4 (a) was pre-registered at ε = 0 and fails there; it holds at every ε > 0.
- In-silico: two- to four-node forms. No family or person is measured.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_stable
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_twosome
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_outside
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_interlock
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_detriangle
```
