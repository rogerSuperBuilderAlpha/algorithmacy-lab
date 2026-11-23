# Shared errors keep a majority at zero; any independent error makes it irreducible

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`) on three-party quorum hubs under three input-noise models with
the same per-reading error rate e. Backlog items 1 and 3 of `quorum_noise_sweep/`. Hypotheses were
pushed in `d751b858` before the first computation.

## Setup

Mediator S commits OR3, MAJ3 (2 of 3) or AND3 over its readings of three parties; each party copies S.
Each reading is wrong with marginal probability e. `indep`: errors independent (probe 464's model;
the TPM matches probe 464's entrywise). `common`: with probability e all three readings flip together.
`mix`: a shared flip XOR an independent flip, each with probability q = (1 − √(1 − 2e))/2.
e ∈ {0, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45}; 72 cases. Full table: [results/results.csv](results/results.csv).

## Whole-system Φ

| form / model | 0.01 | 0.05 | 0.1 | 0.2 | 0.3 | 0.4 | 0.45 |
|---|---:|---:|---:|---:|---:|---:|---:|
| MAJ3 indep | 0.003516 | 0.015761 | 0.026981 | 0.036624 | 0.032046 | 0.017987 | 0.009125 |
| MAJ3 common | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| MAJ3 mix | 0.001772 | 0.008211 | 0.014743 | 0.022432 | 0.022542 | 0.014898 | 0.008279 |
| OR3 / AND3 indep | 2.868690 | 2.381786 | 1.854569 | 1.041518 | 0.499504 | 0.023283 | 0.014689 |
| OR3 / AND3 common | 2.955645 | 2.779699 | 2.563197 | 2.142458 | 1.739799 | 1.357821 | 1.175627 |
| OR3 / AND3 mix | 2.911657 | 2.568562 | 2.163084 | 1.432411 | 0.815185 | 0.325780 | −0.016127 |

All three models give OR3 Φ = 3 and MAJ3 Φ = 0 at e = 0. OR3 and AND3 are complements and give
identical values; they are not independent replications.

## Scores

- **H1 SUPPORTED.** Under `common`, MAJ3 whole Φ is 0 at every rate and the mediator's next-state
  probability takes only two values, as the self-duality argument in hypotheses.md predicted.
- **H2 SUPPORTED.** Under `mix`, MAJ3 whole Φ is positive at every nonzero rate (0.001772 at e = 0.01,
  highest 0.022542 at e = 0.3). It is lower than under `indep` at every rate (e.g. 0.022432 vs 0.036624
  at e = 0.2).
- **H3 REFUTED, at one rate.** OR3 and AND3 keep the full group under `common` at every rate and under
  `mix` up to e = 0.4. Under `mix` at e = 0.45 every reachable state returns no core, and the
  instrument reports a negative whole-system value (−0.016127), which we read as zero, not as a result.
- **H4 SUPPORTED.** MAJ3 never has the full group as its major complex under any model (its returned
  core is {S,P3} under `mix` at e = 0.2, for example).
- **H5 SUPPORTED.** In every MAJ3 case with positive Φ (14 cases: `indep` and `mix`), the largest core φ
  is 4 × whole-system Φ within 1e-6 relative; e.g. `mix` e = 0.2: 0.089730 vs 0.022432.

## What it means

What turns a noisy majority irreducible is not error as such but error that differs between parties.
When the mediator's mistakes are fully shared, the majority stays exactly factorable at every rate;
with half the error shared and half independent, it is irreducible at every rate tested, at 50% to
91% of the independent-noise value (the share rises with e). Shared errors are also much kinder to the extreme
rules: at e = 0.45 OR3 keeps Φ = 1.175627 under `common` against 0.014689 under `indep`. Across all
three models the membership half of the O01 law holds for the majority: it never binds the whole group.

## Limits

Three-party counting rules only; the parties never err and update synchronously. Two correlation
structures and one mixture weight. The maximal-complex API returns one complex per state, so ties among
symmetric parties are not enumerated. H5 is checked on three-party majorities only; the five-party
test in backlog item 3 is still open. The negative value at OR3/AND3 `mix` e = 0.45 is a numerical
artifact of the instrument.

## Reproduce

```sh
python org_frontier/studies/quorum_correlated_noise/correlated.py --quick   # CI subset, ~6 s
python org_frontier/studies/quorum_correlated_noise/correlated.py --write   # full panel, ~90 s
```

Python 3.12, PyPhi 1.2.1.dev1470+gb78d0e342, via the `tools/start.py` venv. Full run 1 min 31 s. An
AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `correlated.py` or stored in `results/`. No human review is claimed.
