# Q215 — Stage 4 methods

## Shared infrastructure
- TPM/CM construction: `classifier.classifier` (`tpm_from_rules`, `cm_from_rules`) — identical inputs
  to both arms.
- Reachable-state enumeration: `foundations.proxy_audit.exact_phi.reachable_states`.
- Arm A (IIT 4.0): `pyphi.new_big_phi.sia(Subsystem(net, state)).phi` on the whole system — the lab's
  standard instrument (same call family as `probes/lib.py`).
- Arm B (IIT 3.0): `pyphi.compute.sia(Subsystem(net, state)).phi` on the whole system, library
  defaults, same TPM, same states.
- Python: repo root, `venv-4.0`.

## Measure and decision rule (fixed before the run)
For each form and each arm: Φ_max = max over reachable states of whole-system Φ; verdict = BINDS if
Φ_max > 1e-9 else FACTORS. A hypothesis is CONFIRMED iff every form it covers gets the predicted
verdict in BOTH arms. H5 additionally requires Φ = 0 at *every* reachable state in both arms, not
just at the max. Per-state values for both arms go to `results/phi_family.csv`.

## Instrument controls (run first; abort comparison on failure)
- read-recipient triad (E′=M, M′=E∧R, R′=M): must BIND in both arms (4.0 anchor: Φ = 2.0, q111/q210).
- two disjoint copy dyads (A′=B, B′=A, C′=D, D′=C): must FACTOR in both arms.

## Forms (exact rules; little-endian, rules[j](x) returns node j's next bit)
| id | form | rules | source |
|---|---|---|---|
| CTRL+ | read-recipient triad | [x1, x0∧x2, x1] | q111 `forms.py` |
| CTRL− | two disjoint dyads | [x1, x0, x3, x2] | atlas B5 |
| E1 | quorum(3,1) | parties copy S; S′ = (ΣP ≥ 1) | atlas `quorum(3,1)` |
| E2 | quorum(3,2) | parties copy S; S′ = (ΣP ≥ 2) | atlas `quorum(3,2)` |
| E3 | quorum(3,3) | parties copy S; S′ = (ΣP ≥ 3) | atlas `quorum(3,3)` |
| E4 | rotation | [x3, x0, x1, x2] | atlas B10 |
| E5 | one-sided veto | [x1, x0∧¬x2, x1] | atlas D1 |
| E6 | dispatch, full | [¬x1, x0∧x2, x2∧¬x1] | paper2 results §2 |
| E7 | dispatch, rider dropped | [¬x1, x0, x2∧¬x1] | paper2 results §2 |
| E8 | maximal wiring | [¬(x1∨x2), ¬x0∧x2, ¬(x0∧x1)] | paper2 results §5 |

## Notes
- Magnitude differences between arms are expected and reported but carry no verdict weight.
- Descriptive extra (no hypothesis): each arm's best complex (4.0 `maximal_complex`, 3.0
  `major_complex`) at the argmax state, to see whether membership, not just sign, agrees.
