# Alphabet ladder: two, three and four possible answers on the same vote hub

The mediator + three parties hub of `ternary_majority_noise` with k = 4 answer values (k = 2 and 3 as
controls): S misreads each party with probability r and commits the median or min of its readings;
parties copy S. Exact IIT 4.0 on the multivalued overlay `third_party/pyphi_iit4_mv`.

```
python org_frontier/studies/alphabet_ladder_hub/run.py --quick     # CI subset, ~15 s
python org_frontier/studies/alphabet_ladder_hub/run.py --write     # pre-registered run, ~9 min
python org_frontier/studies/alphabet_ladder_hub/allpeaks.py --write  # post-hoc all-state check, ~4.5 min
```

**Result: THE_PATTERNS_EXTEND_IN_K.** Min without noise: whole Φ 6.000000 = 3 log₂ 4 (after 3 log₂ 2 and
3 log₂ 3), full group at r = 0 and 0.1. Median: whole Φ 0 without noise, small and positive with noise,
never the full group. Its best core φ over whole-Φ states is exactly 10 × whole Φ at r = 0.05, 0.1, 0.2
(after 4 and 7: 3k − 2), found only in the post-hoc all-state check; the pre-registered one-state
procedure missed it.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/](results/),
[BACKLOG.md](BACKLOG.md).
