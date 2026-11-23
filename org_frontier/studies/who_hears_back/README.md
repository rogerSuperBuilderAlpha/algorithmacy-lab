# Who hears back: a platform that reads some users and answers some users

Platform P with four parties. P computes AND (or OR) over the r parties it reads; the t parties it answers
copy P; the rest keep their own last state. 20 AND forms (r = 1..4, t = 0..4) plus two OR forms.
Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/who_hears_back/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/who_hears_back/run.py --write   # full run, ~1 min
```

**Result: ONLY_THE_LOOP_BINDS.** The whole five-node system is integrated only when the platform reads and
answers all four parties (Φ = 4.0). Otherwise the tightest unit is the platform plus the parties it both
reads and answers: φ = 2.0 for one or two such parties, 3.0 for three. Parties it only reads, or only
answers, never join that unit; with nobody answered, each party alone is the top unit (φ = 1.0).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
