# A three-valued majority behaves like the yes/no majority: noise binds it a little, never as a whole

Exact IIT 4.0 Φ on the multivalued overlay `third_party/pyphi_iit4_mv` (stock pin `b78d0e342`
underneath). Hypotheses were fixed in [hypotheses.md](hypotheses.md) and pushed in commit `5da2d68e`
before the full computation; the timing-pilot values seen before that file are listed in it.

## Setup

Mediator S and three parties P1–P3, all on {0,1,2}. S reads each party; with probability r it misreads
it as one of the other two values (r/2 each). S commits median (three-valued majority), min (lift of
AND3) or max (lift of OR3) of its readings; each party copies S exactly. Binary controls: same code on
{0,1} (misreading = bit flip). Rates r = 0, 0.05, 0.1, 0.2, 0.4. Whole Φ = largest full-system φ over
reachable states; at every state attaining it we ran the maximal-complex search.

Controls passed: binary MAJ3 at r = 0.2 is 0.036624, OR3 is 3.0 at r = 0 and 1.041518 at r = 0.2
(`quorum_noise_sweep`); ternary min equals ternary max at every rate.

## Whole-system Φ

| rule | alphabet | 0 | 0.05 | 0.1 | 0.2 | 0.4 |
|---|---|---:|---:|---:|---:|---:|
| majority (MAJ3) | {0,1} | 0 | 0.015761 | 0.026981 | 0.036624 | 0.017987 |
| median | {0,1,2} | 0 | 0.012445 | 0.022209 | 0.033668 | 0.029390 |
| AND3 / OR3 | {0,1} | 3.000000 | 2.381786 | 1.854569 | 1.041518 | 0.023283 |
| min / max | {0,1,2} | 4.754888 | 3.886383 | 3.133882 | 1.940021 | 0.549502 |

## Scores

- **H1 SUPPORTED.** The deterministic ternary median has whole Φ 0 in all nine reachable states.
- **H2 SUPPORTED.** With any tested noise the median's whole Φ is positive (0.012445 at r = 0.05).
- **H3 SUPPORTED.** At every noisy rate the median's maximal complex at each whole-Φ state is a proper
  subset: a pair {S,Pi} or a triple {S,Pi,Pj}, never {S,P1,P2,P3}.
- **H4 SUPPORTED.** Ternary min without noise has whole Φ 4.754888 = 3 log₂ 3, against 3.0 = 3 log₂ 2
  for binary AND3.
- **H5 SUPPORTED.** Ternary min (and max) keeps the full group as its maximal complex at every rate.
- **H6 REFUTED at one rate.** The median is below MAJ3 at r = 0.05, 0.1 and 0.2, but above it at r = 0.4
  (0.029390 vs 0.017987).

## Descriptive

- **Core ratio 7, not 4.** For binary MAJ3 the best core φ is 4 × whole Φ at every noisy rate (as
  `quorum_noise_sweep` found). For the ternary median it is 7 × whole Φ at every noisy rate, to 1e-14
  (e.g. 0.235679 vs 0.033668 at r = 0.2). Observed, not derived.
- **The r = 0.4 reversal is a chance-level effect.** At r = 0.4 a binary reading is close to a coin flip
  (chance is 0.5); a ternary reading is still far from chance (2/3). The ternary rows have not reached
  their own chance point on this grid. The ternary min at r = 0.4 also keeps 0.549502, against 0.023283
  for AND3.
- **Peaks.** The median's whole Φ peaks at the six reachable states where S holds 0 or 2 and the parties
  agree; min peaks at 2222 and max at 0000 at every rate, while binary AND3/OR3 move their peak at 0.4.

## Reading

O04 asked whether the two-condition membership account holds when a party has more than two states.
`ternary_pivotality` answered it on the three-node triad (state-dependent); this study adds the
quorum side. The quorum law's membership half carries over to three values: the middle rule (median)
never binds the whole group, the extreme rules (min, max) always do. The extra middle value adds Φ to
the extreme rules (by log₂ 3 per party in the clean case), and it raises the majority's core-to-whole
ratio from 4 to 7, but it does not change who is bound together.

## Limits

Three parties, synchronous update, independent and uniform misreadings, parties copy exactly. One
ternary lift per rule (median, min, max); other lifts (e.g. a rule that treats 1 as abstain) are not
tested. The maximal-complex API returns one complex per state, so ties among symmetric parties are not
enumerated. The 1e-9 threshold is the repository default.

## Reproduce

```sh
python org_frontier/studies/ternary_majority_noise/run.py --quick   # about 10 s (CI check)
python org_frontier/studies/ternary_majority_noise/run.py --write   # about 3 min
```

Python 3.12, PyPhi 1.2.1.dev1470+gb78d0e342 plus the vendored overlay. The full run took 166 s on the
lab box. An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this
report; every number above is printed by `run.py` or stored in `results/`. No human review is claimed.
