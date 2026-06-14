# Coordination-logic atlas — methods

## Shared infrastructure
- Verdict / Φ: `org_frontier/classifier/classifier.py` (`classify_rules`). A form is triadic when
  whole-system Φ_MIP > 1e-9 in some reachable state.
- Major complex (core membership): `org_frontier/probes/lib.py` (`major_complex`), the maximal
  irreducible subset of nodes over reachable states.
- Instrument controls: `org_frontier/classifier/validate.py` (`factoring_control`,
  `irreducible_control`).
- Python: run from the repo root with the project venv active (see `GETTING_STARTED.md`).

## Instrument control (run first)
The run computes both canonical controls before any atlas verdict. The factoring control
(`W'=S, S'=W, C'=C`) must read dyadic; the irreducible control (`W'=S∨C, S'=W∧C, C'=W⊕S`) must
read triadic. If either fails the run aborts.

## Construction
Every form is a list of per-node Boolean rules, little-endian: `rules[j](x)` reads the current
state tuple `x` and returns node `j`'s next bit. All fifty builders, their node labels, and their
pre-registered predictions are in `atlas.py`; the runner `run.py` classifies each, records the
whole-system verdict and the major complex, and writes `results/atlas.csv`.

- **Theme A (`quorum`).** `n` parties (nodes `0..n-1`) read a mediator (node `n`); the mediator
  fires iff `sum(parties) ≥ k`. Twelve cells: `n∈{2,3,4,5}`, `k` spanning the extremes and an
  interior value. Decision rule: triadic iff whole-system Φ > 1e-9.
- **Theme B (`topology`).** Four nodes `A,B,C,D`, ten wirings (star, complete, AND-ring,
  line, two independent dyads, two-hub matrix, feed-forward star, hub-plus-isolated, bipartite,
  copy-cycle). Decision rule: triadic iff whole-system Φ > 1e-9; the major complex records which
  parties remain irreducible.
- **Theme C (`redundancy`).** Three to five nodes; duplicate mediators, parallel relays, triple
  modular voting, hot standby, degenerate and substitutable workers, unread copies, series
  mediators, independent backup pairs, trivial readout. Decision rule as above; the major complex
  shows whether a redundant element joins or sheds.
- **Theme D (`inhibition`).** Three nodes `W,S,C`; the mediator is veto (`W∧¬C`), NAND, NOR,
  implication (`¬W∨C`), mutual inhibition (`¬W∧¬C`), inverting feedback, or a parity-agreement
  gate (XNOR), plus a one-sided veto whose source does not read back. Decision rule as above.
- **Theme E (`heterogeneity`).** Three to five nodes; asymmetric arity, party memory
  (`W'=W∨S`), a constant-policy node, read-only and one-way managers, a dominated party, a policy
  override, graded fan-out. Decision rule as above; the major complex shows which nodes shed.

## Anchors
Twelve forms reproduce a known result and are flagged `anchor=True` in the output: the quorum
extremes (the conjunctive/disjunctive law, `Φ=n-1`), two independent dyads, the trivial-readout
triad, the double-negation control, and the XNOR parity gate. They check that the atlas reproduces
established verdicts; the other thirty-eight are new tests.

## Reproduction
```
python -m org_frontier.studies.coordination_logic_atlas.run
```
Deterministic: the forms are fixed Boolean functions and exact Φ has no sampling. The run prints a
per-theme table and a summary, and writes `results/atlas.csv`.
