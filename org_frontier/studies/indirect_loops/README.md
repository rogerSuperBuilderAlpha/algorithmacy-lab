# Indirect loops: when the people a platform answers pass it on to the people it reads

Platform P reads A1, A2 and answers A3, A4. A1 and A2 either act alone (self-loop) or copy an answered
party, closing a loop through other people. Six forms, including the direct-loop control.
Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/indirect_loops/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/indirect_loops/run.py --write   # full run, ~10 s
```

**Result: RELAYED_LOOPS_BIND_THE_WHOLE.** With disjoint read and answer sets and no relay, P is in no top
unit (the self-looping parties top at φ = 1.0). When answered parties pass the decision to the read
parties, each relay loop {P, reader, relayer} is a top unit at φ = 2.0, and with two relays the whole
five-node group is irreducible (Φ = 2.0) and ties for top in the states where both readers are on. The
direct-loop control, with the same platform rule, has whole Φ = 0.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
