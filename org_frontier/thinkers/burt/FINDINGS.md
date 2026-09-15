# Burt — findings

Burt's hole is a cliff, not a slope. A broker combining two disconnected contacts adds Φ = 2.000 to the
whole and has a positional advantage of 2.000 over them; one tie between the contacts drives both to zero.
The information broker (E = X ∧ Y) is evicted from the core by that tie; the control broker (E = X ∨ Y) stays,
because under closure it is a peer in an OR-clique of three at Φ = 6.000 with no advantage over anyone (H1
partial: the advantage goes in both cases, the membership in one). Structurally equivalent contacts count as
one — one of the pair is evicted — but so do nonredundant ones: the five-node whole is irreducible at 2.000
and tied with its sub-triad, and the broker's value added is 2.000 with one, two equivalent, or two
nonredundant contacts (H2 refuted on the pre-registered rule). Over three contacts with 0, 1, 2, 3 ties among
them, Burt's constraint rises 0.333 → 0.611 → 0.840 → 0.926 and the broker's value added falls 3.000 → 0 → 0
→ 0: the first tie takes everything (H3 partial: non-increasing, not strict). A rival broker spanning the
same hole destroys both: the whole becomes reducible, the core shrinks to {R, Y} at 0.189, and each broker's
presence lowers the core Φ by 1.811 (H4 confirmed). Closure inside the broker's group, across the hole, or
everywhere all drive value added to zero; the open network is the only one in which the broker adds (H5
refuted: Burt 1992 beats Burt 2001).

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | closure removes the broker, for information and control alike | **PARTIAL** | info: open V(E)=2.000, closed core {X,Y}, V(E)=0; control: closed core {E,X,Y} Φ 6.000, V(E)=4.000 but positional advantage 0 |
| H2 | structurally equivalent contacts count as one; nonredundant as two | **REFUTED** | equivalent: core {E,Y,Z}, Φ_MIP 1.000 (X evicted); nonredundant: Φ_MIP 2.000 but major complex {E,Y,Z2} at 2.000 (tie); V(E)=2.000 in single, equivalent, nonredundant |
| H3 | value added falls strictly with constraint | **PARTIAL** | C_E 0.333/0.611/0.840/0.926; V(E) 3.000/0/0/0 |
| H4 | a rival spanning the same hole removes autonomy | **CONFIRMED** | alone V(E)=2.000; with rival Φ_MIP 0, core {R,Y} 0.189, V(E)=V(R)=−1.811 |
| H5 | closure within + brokerage beyond maximizes value added | **REFUTED** | V(E): open 3.000, within 0, across 0, everywhere 0 |

Instrument control (conjunctive triad, Φ = 2.000000, core {A, M, B}) passed in all five probes.

## Caveats

- Contacts read disjunctively (any source suffices); the information broker reads conjunctively. Other
  rules would be other forms.
- Value added is Φ(core of whole) − Φ(core without the party); positional advantage subtracts the best
  contact's value added. Both are the lab's quantities, not Burt's.
- H2's nonredundant form fails on a tie: the whole of five and its sub-triad are both irreducible at 2.000.
- In-silico: three- to five-node Boolean forms.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_closure
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_equivalence
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_constraint
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_rival
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.burt.probe_burt_complement
```
