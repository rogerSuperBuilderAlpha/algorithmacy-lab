# Which three-valued version of a rule you pick can decide whether the triad is one unit

Exact IIT 4.0 Φ on the multivalued overlay `third_party/pyphi_iit4_mv` (stock pin `b78d0e342`
underneath). Hypotheses were fixed in [hypotheses.md](hypotheses.md) and pushed in commit `a66777a2`
before any computation.

## Setup

Triad W' = S, C' = S, S' = f(W, C). Binary rules AND, OR, XOR, copy (S' = W) on {0,1}; seven
three-valued lifts on {0,1,2} (table in `hypotheses.md`). r = 0 and r = 0.1 (S misreads each input,
uniformly to another value). Whole Φ = largest full-system φ over reachable states; "triadic" = the
full triad {W,S,C} is the maximal complex at every whole-Φ state. Controls passed: binary AND at (1,1,1)
is 2.0; ternary min at (2,2,2) is 3.169925.

## Results

| rule | version | whole Φ, r = 0 | triadic | whole Φ, r = 0.1 | triadic |
|---|---|---:|---|---:|---|
| AND | {0,1} | 2.000000 | yes | 1.373755 | yes |
| AND | min | 3.169925 | yes | 2.321394 | yes |
| AND | all-top (2 only if both 2) | 3.169925 | yes | 2.321394 | yes |
| OR | {0,1} | 2.000000 | yes | 1.373755 | yes |
| OR | max | 3.169925 | yes | 2.321394 | yes |
| OR | capped sum | 3.169925 | yes | 2.321394 | yes |
| XOR | {0,1} | 0.500000 | no ({W,S} 1.0) | 0.292615 | no ({W,S} 0.356848) |
| XOR | abs(W − C) | 1.084963 | 1 of 3 states | 0.759836 | yes |
| XOR | (W + C) mod 3 | 0.528321 | no ({W,S} 1.056642) | 0.350405 | no |
| copy | both | 0 | no | 0 | no |

## Scores

- **H1 REFUTED.** One agreeing lift changes the verdict: abs(W − C) agrees with XOR on {0,1}, but at
  r = 0.1 the full triad is the maximal complex at all three whole-Φ states (020, 121, 222; φ 0.759836),
  where binary XOR has the pair {W,S} at all four. At r = 0 the full triad wins at 121 (1.084963); at
  020 and 222 the pair {W,S} wins (1.584963). Every other agreeing lift keeps its binary verdict.
- **H2 SUPPORTED.** Every agreeing lift has whole Φ at least its binary rule's at r = 0.
- **H3 SUPPORTED.** All-top AND stays triadic; sum mod 3 stays non-triadic.
- **H4 SUPPORTED.** Copy has whole Φ 0 in both alphabets (C feeds nothing).
- **H5 REFUTED.** Max and capped sum give the same whole Φ (3.169925 at r = 0; 2.321394 at r = 0.1),
  as do min and all-top. Their other states differ (e.g. state 010: max 0.194988, capped sum 1.084963
  at r = 0), so the lift changes the state-by-state profile but not the peak.

## Reading

For the conjunctive and disjunctive triads, the verdict and the peak Φ do not depend on how the rule is
extended: the peak sits at the all-high (AND) or all-low (OR) state, where every lift behaves the same.
For the parity triad the extension matters. Binary XOR reports only whether the two parties differ, and
the mediator plus one party out-integrate the whole. When the mediator reports how far apart they are
(|W − C|), the whole triad becomes the integrated unit under noise; when it reports their sum around a
three-step clock (mod 3), it does not. So a verdict computed on yes/no models of a parity-type
arrangement is not automatically the verdict for a richer version of it; the richer rule has to be
specified and checked.

## Limits

Three nodes, synchronous update, one noise level, one noise shape. Seven lifts out of many. The
maximal-complex API returns one complex per state; ties are not enumerated. The 1e-9 threshold is the
repository default.

## Reproduce

```sh
python org_frontier/studies/ternary_lift_panel/run.py --quick   # about 3 s (CI check)
python org_frontier/studies/ternary_lift_panel/run.py --write   # about 5 s
```

Python 3.12, PyPhi 1.2.1.dev1470+gb78d0e342 plus the vendored overlay. An AI assistant working as the
open harness around IIT 4.0/PyPhi wrote the script and this report; every number above is printed by
`run.py` or stored in `results/`. No human review is claimed.

See also: `ternary_majority_noise` (the four-node hub) and `ternary_ordinal_noise` (noise sweep, neighbour-only misreadings).
