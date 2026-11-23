# Gate source: does the switch rejoin the group if the group can reach it?

Platform P' = R1 ∧ R2; R1 copies P; R2 hears P through a relayer C1 gated by a switch G (C1' = P ∧ G or
P ∨ G). The switch either holds its own setting (G' = G) or copies a group member (P, R1 or C1). Exact IIT
4.0 φ for every subset in every reachable state; tie sets pooled over all top states.

```
python org_frontier/studies/gate_source/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/gate_source/run.py --write   # full run, ~18 s
```

**Result: REACHABLE_AND_GATE_REJOINS.** With an AND gate, a switch driven by P, R1 or C1 restores whole Φ =
2.0 and joins the top tie set; a self-held switch leaves whole Φ at 0. With an OR gate, whole Φ is 0 both
for a self-held switch and for one driven by P.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
