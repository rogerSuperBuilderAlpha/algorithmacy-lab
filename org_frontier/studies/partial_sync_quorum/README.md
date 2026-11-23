# Partial synchrony on quorum hubs

The mediator and three parties update in ordered blocks: all 75 ordered partitions of the four nodes,
on OR3, MAJ3, AND3. Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/partial_sync_quorum/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/partial_sync_quorum/run.py --write   # full run, ~23 s
```

**Result: MEDIATOR_MUST_LEAD_WITH_A_PARTY.** OR3 and AND3 are whole-system irreducible in 13 of 75
schedules, exactly those whose first block holds S and at least one party (Φ 3.0, 2.0, 1.0 for three,
two, one parties alongside S); MAJ3 is 0 under all 75.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
