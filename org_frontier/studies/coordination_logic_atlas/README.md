# Coordination-logic atlas

Fifty exact-Φ experiments mapping what makes a coordination form irreducible, across five axes the
logbook does not sweep systematically: quorum thresholds, four-node topology, redundancy and
degeneracy, inhibition and valence, and heterogeneity. A contribution study built on the
`org_frontier` instrument.

## Run it

From the repo root, with the venv active (see [`GETTING_STARTED.md`](../../../GETTING_STARTED.md)):

```bash
python -m org_frontier.studies.coordination_logic_atlas.run
```

The run validates the instrument on its two controls, classifies all fifty forms, prints a
per-theme table, and writes [`results/atlas.csv`](results/atlas.csv).

## Files

- [`hypotheses.md`](hypotheses.md) — the five theme hypotheses and the per-form predictions, fixed
  from the bidirectionality and pivotality principles before the run.
- [`methods.md`](methods.md) — how each form is built, the instrument control, the decision rule.
- [`atlas.py`](atlas.py) — the fifty builders and their predictions.
- [`run.py`](run.py) — the runner.
- [`FINDINGS.md`](FINDINGS.md) — the results: 36/50 matched, and the fourteen misses resolved into
  three mechanisms (substitutability, spectators, synchronization/absorption).
- [`results/atlas.csv`](results/atlas.csv) — every form's verdict, Φ, major complex, and core Φ.

## Headline

A k-of-n quorum mediator is irreducible only at the extremes — unanimity (`k=n`) and any-one
(`k=1`) — and dyadic at every interior threshold, with no gradient between. Twelve of the fifty are
anchors that reproduce known verdicts (the conjunctive law, parity, two independent dyads); the
other thirty-eight are new tests.
