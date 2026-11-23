# Cause and effect at the unanimous state, under both placements

Item 1 of `placement_equality/BACKLOG.md`. Pre-registered comparison of the IIT 4.0 system-level
cause and effect analyses of OR3 at 0000 and 1-of-4 at 00000, at r ∈ {0.2, 0.4}, under
mediator-side and party-side noise. System φ is the minimum of the cause value and the effect value.

```
python org_frontier/studies/unanimous_repertoires/run.py --quick   # CI subset, ~4 s
python org_frontier/studies/unanimous_repertoires/run.py --write   # full run, ~9 s
```

**Result: H1 and H3 refuted; H2 supported.** At r = 0.2 the placements do not share a full
cause-and-effect analysis. For OR3 at 0000, cause φ is 1.041518 (mediator) versus 2.002920 (party),
while effect φ is 1.041518446253012 either way. The already-known match of system φ is a match of
those effect values. At r = 0.4, mediator effect φ falls to −0.1242086202819146, which is why the
match of system φ breaks.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
