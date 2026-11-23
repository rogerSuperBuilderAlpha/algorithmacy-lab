# Noisy majorities have no noise threshold, and still never bind the whole group

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`) on seven counting quorums at ten input-observation error
rates. Extends probe 464 (`org_frontier/probes/weighted_quorum/input_noise/`), which tested only
η = 0, 0.1 and 0.5. Hypotheses and decision rules were fixed in [hypotheses.md](hypotheses.md) and
pushed in commit `82d58785` before the first computation.

## Setup

A mediator S commits a quorum rule over what it observes of n parties; each party copies S. S sees
each party through an independent bit-flip error η; the parties' actual states are not altered.
Forms: OR3, MAJ3 (2 of 3), AND3; ANY4, 2of4, 3of4, ALL4. Rates: 0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3,
0.4, 0.45, 0.5. "Whole Φ" is the maximum over reachable states of whole-system Φ; "full-group core"
means the full group is the major complex in every state that attains the maximum core φ.

## Whole-system Φ

| form | 0 | 0.01 | 0.02 | 0.05 | 0.1 | 0.2 | 0.3 | 0.4 | 0.45 | 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| OR3 / AND3 | 3.0000 | 2.8687 | 2.7413 | 2.3818 | 1.8546 | 1.0415 | 0.4995 | 0.0233 | 0.0147 | 0 |
| MAJ3 | 0 | 0.0035 | 0.0069 | 0.0158 | 0.0270 | 0.0366 | 0.0320 | 0.0180 | 0.0091 | 0 |
| ANY4 / ALL4 | 4.0000 | 3.7867 | 3.5819 | 3.0169 | 2.2255 | 1.1110 | 0.4662 | 0.0093 | 0.0066 | 0 |
| 2of4 / 3of4 | 0 | 0.0042 | 0.0081 | 0.0181 | 0.0296 | 0.0358 | 0.0273 | 0.0131 | 0.0061 | 0 |

Complement pairs (OR/AND, ANY4/ALL4, 2of4/3of4) give identical values; they are not independent
replications. Full values are in [results/sweep.csv](results/sweep.csv).

## Scores

- **H1 SUPPORTED.** MAJ3 whole Φ is positive at every noisy rate, from 0.003516 at η = 0.01. There
  is no noise threshold on this grid: any input error in the tested range makes the majority hub's
  whole system irreducible. It rises to a peak of 0.036624 at η = 0.2 and falls back to 0 at 0.5.
- **H2 SUPPORTED.** No interior quorum (MAJ3, 2of4, 3of4) has the full group as its major complex at
  any rate. The returned core shrinks as noise grows: MAJ3 goes from {S,P2,P3} (η ≤ 0.05) to {S,P3}
  (η ≥ 0.1); 2of4 and 3of4 return {S,P2,P3,P4} or {S,P3,P4} at η = 0.01 and {S,P4} from η = 0.2.
- **H3 REFUTED, at one rate.** OR3 and AND3 keep the full group at every noisy rate. ANY4 and ALL4
  keep it at every noisy rate except η = 0.4, where two reachable states tie at the maximum core
  φ = 0.009264: one returns the full group, the other returns {S,P4}. At η = 0.45 the full group is
  back. At η = 0.4 the two all-parties-off states of ANY4 return no core at all.
- **H4 SUPPORTED.** 2of4 and 3of4 whole Φ is positive at every noisy rate (peak 0.035822 at η = 0.2).

Descriptive: at its peak the interior quorum's whole Φ is small next to the extreme quorum at the same
rate: MAJ3 0.036624 is 0.035 × OR3; 2of4 0.035822 is 0.032 × ANY4. In 22 of the 24 noisy interior
cases the largest core φ equals the whole-system Φ times the node count to within 1e-6 relative
(4 for three parties, 5 for four), e.g. MAJ3 at η = 0.2: 0.146494864 = 4 × 0.036623716. The two
exceptions are 2of4 and 3of4 at η = 0.45, where the ratio is 4.03. This is an observed regularity on
this panel; we have not derived it.

## What changes in the O01 law

The atlas law joins two claims about interior quorums: zero whole-system Φ, and no full-group major
complex. Across this grid the first claim fails at every nonzero noise rate below 0.5, with no
threshold. The second claim holds at every rate. The extremes-only law therefore survives input noise
as a claim about major-complex membership (who is bound together), not as a claim about whole-system
Φ. The four-party extreme quorums show that the membership half is itself fragile near η = 0.4,
where the full-group core holds in only one of four reachable states and ties with a pair.

## Limits

Small Boolean models, not real committees. Independent, uncorrelated observation errors only; actual
party states never err; synchronous update. Counting quorums only (no weighted rules in this sweep).
The maximal-complex API returns one complex per state, so symmetric ties among parties (which party
appears in {S,P3} or {S,P4}) are not enumerated. One state of ANY4/ALL4 at η = 0.4 reports a negative
whole-system Φ (−0.093255), a numerical artifact of the instrument at that rate; it is not the maximum
and does not enter any score. The 1e-9 cutoff is the repository default.

## Reproduce

```sh
python org_frontier/studies/quorum_noise_sweep/sweep.py --quick   # OR3 + MAJ3, about 35 s (CI check)
python org_frontier/studies/quorum_noise_sweep/sweep.py --write   # full panel, about 9 min
```

Run on Python 3.12, PyPhi 1.2.1.dev1470+gb78d0e342, via the venv `tools/start.py` creates. The full run
took 8 min 45 s on the lab box. An AI assistant working as the open harness around IIT 4.0/PyPhi
wrote the script and this report; every number above is printed by `sweep.py` or stored in `results/`.
No human review is claimed.
