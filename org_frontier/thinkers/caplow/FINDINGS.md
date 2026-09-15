# Caplow — findings

Rendered by his own assumptions — the stronger partner controls the coalition's stance, strength adds in
the outcome, every member reads the outcome — Caplow's coalitions are wholes only when the partners are
equal. Of the twenty winning coalitions across his eight types, the five with equal partners bind (both
partners in the major complex, core Φ = 2.000) and the fifteen with unequal partners never do; the junior
partner is a spectator and the core is the senior partner and the outcome (H5 refuted). Caplow's predicted
coalition is the binding one in Types 1, 2, 4, and 6 and not in Types 3, 5, 7, and 8, where his prediction
rests on a weaker member's wish to control the isolate (H1 partial). Among binding coalitions A is a member
in 2 of 5 against 4 for B and 4 for C — strength is weakness (H2 confirmed) — though across all 24 forms A is
in the core 18 times to B's 7 and C's 6. When A ≥ B + C, BC never binds; at exact equality the blocking BC
coalition in Type 7 pulls A and B into one whole, {A, B, O}, and the precoalition forms have no complex at
all (H3 partial). In Type 5 the revolutionary coalition removes A from the core and the conservative and
improper ones keep him, but no Type 5 coalition binds both partners (H4 partial). The precoalition
condition has no irreducible structure in six of eight types; the coalition is what makes a whole.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | power predicts the coalition | **PARTIAL** | binding = predicted in Types 1, 2, 4, 6; differs in 3 (BC binds, not AB/AC), 5 (none), 7 (none), 8 (none) |
| H2 | strength is weakness | **CONFIRMED** | membership in 5 binding coalitions: A 2, B 4, C 4; in the core over 24 forms: A 18, B 7, C 6 |
| H3 | A ≥ B + C: no coalition against A | **PARTIAL** | BC never binds in Types 4, 6, 7, 8; A in every coalition core; t7_BC core {A, B, O} 2.000; t7_pre and t8_pre have no complex |
| H4 | conservative / revolutionary / improper | **PARTIAL** | Type 5: AB core {A, O}, AC {A, O}, BC {B, O}; A out only under BC; no coalition binds both partners |
| H5 | strength is additive | **REFUTED** | 20 winning coalitions, 5 bind; equal partners 5/5, unequal 0/15 |

Whole-system Φ_MIP is 0.000 for all 32 forms (the isolate or the junior partner is always a spectator); the
reading is the major complex. Instrument control (conjunctive triad, Φ = 2.000000, core {A, M, B}) passed
in all five probes.

## Caveats

- One rendering of "control": the stronger partner's stance is the bloc's stance. A graded within-bloc
  rule would be another paper; `paper.md` Limitations names it.
- In-silico: four binary elements per form; the eight weight vectors are Shenoy's representatives, one per
  type.
- The precoalition observation and the Type 7 blocking whole were not pre-registered.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_types
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_weakness
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_dominance
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_kinds
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.caplow.probe_caplow_additivity
```
