# Simmel — Stage 4 methods

Every form is a set of Boolean update rules over binary nodes, one per party, and every number is exact
IIT-4.0 Φ computed with PyPhi. A reader should be able to reproduce each test from this file alone.

## Shared infrastructure

- Verdict (whole-system Φ over the minimum-information partition, max over reachable states):
  `org_frontier.probes.lib.verdict`.
- Major complex (the maximal irreducible complex, max over reachable states): `org_frontier.probes.lib.major_complex`.
- Boolean influence of a node on a rule: fraction of input states in which flipping the node flips the output,
  computed in `forms.py`.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`. All forms are in `forms.py`; each probe
  imports from there and writes `results/<probe>.json`.

## Instrument control (run first, in every probe)

The conjunctive triad A'=M, M'=A∧B, B'=M must read triadic at Φ = 2.000000 with core {A, M, B}. No comparison
is read until it does.

## Forms

Node order is the label order given. `∧` AND, `∨` OR, `⊕` XOR, `maj` majority, `¬` NOT.

### H1 — superindividual triad
| form | rules | reading |
|---|---|---|
| `dyad_mutual` | A'=B, B'=A | two who depend on each other and no one else |
| `dyad_cut` | A'=A, B'=B | the dyad with its tie removed: "only the other remains" |
| `triad_mutual` | A'=B∧C, B'=A∧C, C'=A∧B | each member reads both others |
| `triad_broken_line` | A'=C, B'=C, C'=A∧B | the direct A–B tie removed; A and B joined only through C |

Decision rule. H1 confirmed iff (i) `triad_mutual` core = {A,B,C}; (ii) Φ(`triad_mutual`) > Φ(`dyad_mutual`);
(iii) `triad_broken_line` is triadic with A and B both in the core; (iv) `dyad_cut` has Φ = 0. All four or
the hypothesis is partial/refuted as stated in the results.

### H2 — the decisive step
| form | rules |
|---|---|
| `clique_n` for n = 2..5 | each node' = ∧ of all other nodes (n = 2 is `dyad_mutual`, n = 3 is `triad_mutual`) |

Measure: whole-system Φ_MIP (max over reachable states). Decision rule. H2 confirmed iff
ΔΦ(2→3) > ΔΦ(3→4) and ΔΦ(3→4) ≥ ΔΦ(4→5). If Φ grows linearly or faster, refuted. Also report the core at each n.

### H3 — majority
| form | rules |
|---|---|
| `majority_triad` | A'=maj(A,B,C), B'=maj(A,B,C), C'=maj(A,B,C) |
| `unanimity_triad` | A'=A∧B∧C, B'=A∧B∧C, C'=A∧B∧C (comparison: a whole that cannot outvote anyone) |
| `unanimity_dyad` | A'=A∧B, B'=A∧B (the dyad's only collective rule) |

Decision rule. H3 confirmed iff `majority_triad` is triadic with core {A,B,C}. Refuted if dyadic. The two
unanimity forms are reported for contrast and do not decide H3.

### H4 — the nonpartisan scale
| form | rules | reading |
|---|---|---|
| `arbitrator` | A'=M, B'=M, M'=A∧B | parties adopt M's determination; M states what both can insist upon |
| `mediator` | A'=A∧M, B'=B∧M, M'=A∧B | parties keep their own will and read only M; M never reaches a decision |
| `mediator_eliminated` | A'=B, B'=A, M'=A∧B | parties unite directly; M still listens, no one reads him |

Decision rule. H4 confirmed iff M ∈ core(`arbitrator`), M ∈ core(`mediator`), M ∉ core(`mediator_eliminated`),
and Φ(`arbitrator`) > Φ(`mediator`) > 0. Partial if the membership pattern holds but the ordering fails, or if
`mediator` factors (M out) — the latter is the lab-prior outcome and is reported as a refutation of the middle
term.

### H5 — the *tertius gaudens* and the balance of forces
Four nodes: contestants A and B, the third T, and the outcome O. A pushes for O = 1, B pushes against, and T
lends its weight to A's side when T = 1 and to B's side when T = 0. O' = 1 iff w_A·A + w_T·T > w_B·B + w_T·(1−T).
All three parties read the outcome: A'=O, B'=O, T'=O. Only the weights vary.

| regime | (w_A, w_B, w_T) | O' reduces to |
|---|---|---|
| `balanced` | (1, 1, 1) | T ∧ (A ∨ ¬B) — the third turns the scale |
| `intermediate` | (2, 1, 1) | (A∧T) ∨ (A∧¬B) ∨ (T∧¬B) |
| `dictator` | (3, 1, 1) | A |

Measures: whole-system verdict and Φ, the major complex, and T's Boolean influence on O'. Decision rule. H5
confirmed iff T ∈ core(`balanced`), T ∉ core(`dictator`), and both T's influence and T's membership are
monotone non-increasing from balanced to intermediate to dictator. Refuted if T is out of the core under
`balanced` or in under `dictator`.

## Reporting

Each probe prints one line per form (`form  verdict  Φ_MIP  core  coreΦ`) and one verdict line per
hypothesis (`H<k> (...): CONFIRMED | PARTIAL | REFUTED`). Numbers are read into `paper.md` and `FINDINGS.md`
verbatim and registered in `ci/reproduce.json`.
