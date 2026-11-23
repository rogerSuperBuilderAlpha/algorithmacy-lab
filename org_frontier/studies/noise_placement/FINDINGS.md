# Errors on the parties' side never make a majority irreducible; errors on the mediator's side do

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `3f935d2f` before computation. Controls passed: deterministic TPM at r = 0; `mediator` equals
probe 464's `input_tpm` and reproduces MAJ3 whole Φ 0.026981 at r = 0.1.

## Setup

Three parties, mediator S commits OR3 or MAJ3. Noise rate r sits in one of three places: **mediator**
(S misreads each party), **party** (each party miscopies S), or **both**. r ∈ {0, 0.05, 0.1, 0.2, 0.4}.
Party noise makes all 16 states reachable (4 without it). "Top" is the largest subset φ over states; the
tie set is listed at the state where it occurs.

| form | placement | 0.05 | 0.1 | 0.2 | 0.4 |
|---|---|---:|---:|---:|---:|
| MAJ3 whole Φ | mediator | 0.015761 | 0.026981 | 0.036624 | 0.017987 |
| MAJ3 whole Φ | party | 0 | 0 | 0 | 0 |
| MAJ3 whole Φ | both | 0.015758 | 0.026944 | 0.036060 | 0.013876 |
| MAJ3 top subset φ | party | 0.262857 | 0.249022 | 0.221353 | 0.105214 |
| OR3 whole Φ | mediator | 2.381786 | 1.854569 | 1.041518 | 0.023283 |
| OR3 whole Φ | party | 2.381786 | 1.854569 | 1.041518 | 0.170446 |
| OR3 whole Φ | both | 2.042084 | 1.351981 | 0.533257 | 0.005029 |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** With noise only on the party side, MAJ3 whole Φ is 0 at every rate. Yet pairs
  {S,Pi} are irreducible (top φ 0.262857 at r = 0.05, falling to 0.105214 at 0.4), tied two ways at the
  state where they peak.
- **H2 SUPPORTED.** With noise on both sides, MAJ3 whole Φ is positive at every rate and close to the
  mediator-only value (0.036060 vs 0.036624 at r = 0.2).
- **H3 REFUTED, at one rate.** Under party-only noise OR3 keeps the full group as the top subset up to
  r = 0.2, but at r = 0.4 the top is the three trios {S,Pi,Pj} (0.189385 vs full group 0.170446).
- **H4 SUPPORTED.** MAJ3's full group is never in the top tie set, under any placement or rate.

Descriptive: OR3 whole Φ under party-only noise equals the mediator-only value to six decimals at
r = 0.05, 0.1 and 0.2 (e.g. 1.854569 at 0.1), and differs at 0.4 (0.170446 vs 0.023283). We have not
derived why.

## What it means

The integration a noisy majority shows comes from the mediator's reading of the parties, not from noise
in general: put the same noise on the parties and the whole stays exactly reducible, though
mediator-party pairs become bound. Algorithmacy's point is that the binding third party's reading is what
matters; here, which side of that reading the error sits on decides whether the three-party whole holds
together. The membership half of the quorum law held again: the majority never binds the full group.

## Limits

Three-party yes/no models; independent errors; synchronous update; five rates. Ties at the 1e-9 cutoff.
The OR3 equality is observed, not explained.

## Reproduce

```sh
python org_frontier/studies/noise_placement/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/noise_placement/run.py --write   # full run, ~33 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
