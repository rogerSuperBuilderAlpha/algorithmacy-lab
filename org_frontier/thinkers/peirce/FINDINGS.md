# Peirce — findings

Peirce's genuine triad and the lab's irreducible whole are two different lines, and they cross in both
directions. Read as the largest number of parties any irreducible IIT-4.0 distinction spans (its *adicity*),
Peirce's grades order exactly — monads 1, a chain of dyads 2, the joint rule 3 (H2 confirmed) — and genuine
giving carries a three-term fact that the two-step imitation lacks even though both are Φ = 2.0 wholes with
all three in the core (H3 confirmed). Two-input rules compound into four-term facts in 58 of 60 random
four-element forms, so triads compose upward (H5 confirmed). The negative clause — dyads never compose into a
triad — fails as pre-registered: 78 of 89 one-input wirings reach adicity 3 or 4 (H1 refuted), but every one
of them does so on the *effect* side, at a branch point where one element is read by two or more; the
maximum *cause*-side adicity across all 89 wirings is 2, and the 11 unbranched wirings never exceed adicity 2
on either side. The exceptions are the junctions Peirce himself, against Kempe, called triadic. The sign
relation with an exogenous object has a three-term fact but no whole — Φ = 0, the object alone in the core —
and binds all three only when interpretation feeds back on the object (H4 partial).

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | dyads never compose into a triad | **REFUTED** | 89 one-input wirings: adicity {2: 11, 3: 66, 4: 12}; Φ > 0 in 8 (the pure 3- and 4-cycles, all adicity 2, Φ = 2.000); post hoc: max cause-side adicity 2 in all 89; branched 78 all Φ = 0 |
| H2 | monadic < dyadic < genuine | **CONFIRMED** | adicity 1, 2, 3; degenerate forms Φ = 0.000 with no 3-member complex |
| H3 | giving genuine, imitation degenerate | **CONFIRMED** | genuine: adicity 3 (R ← {G,T}, φ = 2.000), Φ = 2.000 {G,T,R}; degenerate: adicity 2, Φ = 2.000 {G,T,R} |
| H4 | sign, object, interpretant bound with object exogenous | **PARTIAL** | exogenous: adicity 3 ({O,S} → {S,I}, φ = 1.000), Φ = 0.000, core {O}; pragmatic (O'=I): adicity 3 (I ← {O,S}), Φ = 2.000 {O,S,I} |
| H5 | triads compose into tetrads | **CONFIRMED** | 60 two-input forms: adicity {3: 2, 4: 58}; cause-side 4 in 43; Φ > 0 in 46; four-member core in 7, Φ = 3.000 in 4 |

Instrument control (conjunctive triad, Φ = 2.000000, core {A, M, B}, adicity 3 on M ← {A, B} at φ = 2.000)
passed in all five probes.

## Caveats

- Adicity is one rendering of "genuine relation"; the cause/effect split was read post hoc and does not
  change H1's verdict.
- In-silico: forms of three and four binary elements. The H5 sample is 60 forms at seed 0, not the space.
- Peirce's categories as modes of being, and thirdness as "thought or meaning," are not carried.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_irreducibility
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_degeneracy
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_giving
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_sign
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_polyads        # 60 forms, ~9 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_polyads 12     # CI prefix
```
