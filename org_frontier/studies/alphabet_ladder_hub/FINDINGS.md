# With four answer values the vote hub follows the same laws, and the core ratio is 3k − 2

Exact IIT 4.0 Φ on the multivalued overlay `third_party/pyphi_iit4_mv` (stock pin `b78d0e342`
underneath). Hypotheses were fixed in [hypotheses.md](hypotheses.md) and pushed in commit `b6f4d0b4`
before any k = 4 value was computed.

## Setup

Mediator S + three parties on {0,…,k−1}; S misreads each party with probability r, uniformly to one of
the k − 1 other values; S commits median or min; parties copy S. k = 4: median at r = 0, 0.05, 0.1, 0.2;
min at r = 0 and 0.1. Controls passed: k = 2 median at r = 0.1 = 0.026981, k = 3 = 0.022209.

## Results (pre-registered run, `run.py`)

| rule, k = 4 | r | whole Φ | maximal complex at state 0000 / 3333 | core φ ÷ whole Φ there |
|---|---:|---:|---|---:|
| median | 0 | 0 | – | – |
| median | 0.05 | 0.009930 | {S,P3} | 6.748930 |
| median | 0.1 | 0.017985 | {S,P1} | 6.584362 |
| median | 0.2 | 0.028269 | {S,P2} | 6.473214 |
| min | 0 | 6.000000 | {S,P1,P2,P3} | 1 |
| min | 0.1 | 4.041569 | {S,P1,P2,P3} | 1 |

For the median, eight states attain the whole Φ (S at 0 or 3; parties all at one value). The
pre-registered procedure computed the maximal complex at the first of them only (0000).

## Scores

- **H1 SUPPORTED.** Median at r = 0: whole Φ 0 in all 16 reachable states.
- **H2 SUPPORTED.** Median whole Φ positive at every noisy rate; the maximal complex is a pair or triple.
- **H3 REFUTED (as pre-registered).** At state 0000 the ratio drifts: 6.748930, 6.584362, 6.473214.
- **H4 REFUTED (as pre-registered).** Not 10 at state 0000.
- **H5 SUPPORTED.** Min at r = 0: 6.000000 = 3 log₂ 4; full group at r = 0 and 0.1.

## Post-hoc check (not pre-registered): every whole-Φ state

The hypotheses file said the other whole-Φ states were relabelings of 0000. That was wrong: 0000, 3000,
0111 and so on differ in values, not just in party labels. `allpeaks.py` computes the maximal complex at
all eight (results in `results/allpeaks_median_k4.json`):

| r | best core φ (states 3000, 0333) | ÷ whole Φ | other states' ratios |
|---|---:|---:|---|
| 0.05 | 0.099304 | 10.000000 | 6.748930 (0000, 3333), 5.586817 (x111, x222) |
| 0.1 | 0.179851 | 10.000000 | 6.584362, 5.642757 |
| 0.2 | 0.282690 | 10.000000 | 6.473214, 5.829827 |

`ternary_majority_noise` reported the best core φ over all whole-Φ states (4 for k = 2, 7 for k = 3).
On that same definition the k = 4 ratio is exactly 10 at every rate, matching 3k − 2. The exact value
sits where S disagrees with the parties at the two extreme values (3000, 0333). Because this was found
after the pre-registered procedure failed, it should be treated as a post-hoc observation until a
fresh test (for example k = 5) confirms it.

## Reading

Three things carry over from yes/no to four-valued answers: a deterministic median never integrates;
noise makes it slightly integrated but never as the whole group; an extreme rule (min) binds the whole
group with Φ = 3 log₂ k when clean. The ratio between the tightest subgroup and the whole follows
3k − 2 on this panel. We have not derived it.

## Limits

One hub size (three parties), uniform independent noise, synchronous update, three noisy rates, k ≤ 4.
The 3k − 2 law is three points and post hoc. 1e-9 threshold.

## Reproduce

```sh
python org_frontier/studies/alphabet_ladder_hub/run.py --quick       # about 15 s (CI check)
python org_frontier/studies/alphabet_ladder_hub/run.py --write       # about 9 min (516 s on the lab box)
python org_frontier/studies/alphabet_ladder_hub/allpeaks.py --write  # about 4.5 min
```

Python 3.12, PyPhi 1.2.1.dev1470+gb78d0e342 plus the vendored overlay. An AI assistant working as the
open harness around IIT 4.0/PyPhi wrote the scripts and this report; every number above is printed by
the scripts or stored in `results/`. No human review is claimed.
