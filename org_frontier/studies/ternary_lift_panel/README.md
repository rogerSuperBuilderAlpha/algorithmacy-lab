# Ternary lift panel: the same triad rule on yes/no and on three-valued nodes

The three-node triad W' = S, C' = S, S' = f(W, C) for AND, OR, XOR and copy, each on {0,1} and under
one or two three-valued extensions (lifts), deterministic and with S misreading inputs at r = 0.1.
Exact IIT 4.0 on the multivalued overlay `third_party/pyphi_iit4_mv`.

```
python org_frontier/studies/ternary_lift_panel/run.py --quick   # CI subset, ~3 s
python org_frontier/studies/ternary_lift_panel/run.py --write   # full run, ~5 s
```

**Result: THE_LIFT_CAN_FLIP_THE_VERDICT.** AND and OR stay triadic under every lift (peak Φ 3.169925 =
2 log₂ 3 deterministic, 2.321394 at r = 0.1, the same for every lift of each). Binary XOR is not triadic
(the pair {W,S} out-integrates the whole); its "how far apart" lift |W − C| is triadic at every whole-Φ
state at r = 0.1 and at one of three at r = 0, while its "sum mod 3" lift stays dyadic.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).

Pull request: [#928](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/pull/928).
