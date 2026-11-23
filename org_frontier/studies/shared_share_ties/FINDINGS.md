# The more an error is shared, the less a majority holds together; and its "core" is a many-way tie

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`). Backlog items 2 and 4 of `quorum_correlated_noise/`.
Hypotheses pushed in `1d9ccbb6` before the study's computation (one disclosed API smoke test aside).

## Part A: shared share of the error

Three-party OR3 and MAJ3. Each reading's error is a shared flip XOR an independent flip, with the shared
part a = s·e, so the per-reading error stays e while the shared share s goes from 0 (independent) to 1
(all readings flip together).

| whole Φ | s = 0 | 0.25 | 0.5 | 0.75 | 0.9 | 1 |
|---|---:|---:|---:|---:|---:|---:|
| MAJ3, e = 0.1 | 0.026981 | 0.021645 | 0.015487 | 0.008340 | 0.003494 | 0 |
| MAJ3, e = 0.2 | 0.036624 | 0.031570 | 0.024615 | 0.014705 | 0.006625 | 0 |
| OR3, e = 0.1 | 1.854569 | 1.986552 | 2.143729 | 2.332882 | 2.465415 | 2.563197 |
| OR3, e = 0.2 | 1.041518 | 1.175627 | 1.369413 | 1.664032 | 1.920648 | 2.142458 |

- **H1 SUPPORTED.** MAJ3 Φ falls at every step as s rises, at both rates.
- **H2 SUPPORTED.** MAJ3 Φ is positive at every s < 1 (still 0.003494 at s = 0.9, e = 0.1) and 0 at s = 1.
- **H3 SUPPORTED.** OR3 Φ rises at every step as s rises, at both rates.

There is no cliff: the majority loses integration gradually as errors become shared, and only reaches
zero when they are fully shared. At e = 0.2, half-shared error keeps 67% of the independent-error value
(0.024615 / 0.036624) and 90%-shared error keeps 18% (0.006625 / 0.036624).

## Part B: every subset's φ, state by state

Independent errors. For each reachable state, system φ of every subset PyPhi accepts (the same
`reachable_subsystems` enumeration `maximal_complex` uses; subsets whose conditioned state is unreachable
are skipped, 7 or 15 per state in the states where S and the parties disagree).

- **MAJ3 at e = 0.1 and 0.2:** in all four states the maximum is a clean three-way tie among {S,P1},
  {S,P2}, {S,P3} (φ = 0.107922 and 0.146495). The full group sits at 0.026981 and 0.036624. So the {S,P3}
  reported earlier is one arbitrary pick from a symmetric tie.
- **MAJ3 at e = 0.05:** the tie is six-way, all three pairs and all three triples with S, at φ = 0.063043.
- **2of4 at e = 0.1, state (0,1,1,1,1):** all 15 subsets that contain S tie at φ = 0.015666, including the
  full group. At e = 0.2 in the same state, 14 subsets tie at 0.042177 (every subset with S except the
  full group, which is at 0.035822).
- Other 2of4 states give 4-way ties of the pairs (e.g. e = 0.2, all-off state: 0.179110) or 10-way ties
  of pairs and triples.

Scores: **H4 REFUTED** (the maximizers are not always a single size class: 8 of the 20 states mix
sizes). **H5 REFUTED** (2of4, e = 0.1, state 01111: the full group ties for that state's maximum).

## What it means

Two things. First, how much a majority coordinator holds together depends smoothly on how much of its
error is shared, not on whether errors exist. Second, the "core" of a noisy interior quorum is not a
privileged pair; it is a large tie among symmetric subsets, and in one four-party state the whole group
is part of that tie. This does not overturn the earlier membership result, which was read at the states
with the largest core φ: there the full group is never among the maximizers (2of4, e = 0.1: 0.147954 for
pairs vs 0.029591 for the full group). It does mean "who is bound together" should be reported as a tie
set, not as one returned complex.

## Limits

Small yes/no models; parties never err; synchronous update. Part A has one mixing scheme and two error
rates. Part B covers independent errors only and five cases. Ties are judged at the repo's 1e-9 cutoff.

## Reproduce

```sh
python org_frontier/studies/shared_share_ties/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/shared_share_ties/run.py --write   # full run, ~41 s
```

Python 3.12, PyPhi 1.2.1.dev1470+gb78d0e342. An AI assistant working as the open harness around IIT
4.0/PyPhi wrote the script and this report; every number is printed by `run.py` or stored in
`results/results.json`. No human review is claimed.
