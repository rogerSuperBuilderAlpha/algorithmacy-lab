# Party-side noise matches mediator-side noise only for the extreme rules, and only at the unanimous state

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), full group, every reachable state. Hypotheses pushed in
`e0e5a60f` before computation. Controls passed: deterministic TPM at r = 0 for both placements, and four
`noise_placement` values reproduced to 1e-6 (OR3 party 1.854569 at 0.1 and 0.170446 at 0.4; MAJ3 mediator
0.036624 at 0.2; MAJ3 party 0 at 0.2).

## Whole-group Φ (largest over reachable states)

| form | placement | 0.05 | 0.1 | 0.2 | 0.4 |
|---|---|---:|---:|---:|---:|
| OR3 = AND3 | mediator | 2.381786 | 1.854569 | 1.041518 | 0.023283 |
| OR3 = AND3 | party | 2.381786 | 1.854569 | 1.041518 | 0.170446 |
| 1of4 = 4of4 | mediator | 3.016929 | 2.225483 | 1.110953 | 0.009264 |
| 1of4 = 4of4 | party | 3.016929 | 2.225483 | 1.110953 | 0.136357 |
| MAJ3 | mediator | 0.015761 | 0.026981 | 0.036624 | 0.017987 |
| 2of4 = 3of4 | mediator | 0.018144 | 0.029591 | 0.035822 | 0.013068 |
| MAJ3, 2of4, 3of4 | party | 0 | 0 | 0 | 0 |

Full data, including φ at every reachable state: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** AND3 equals OR3 under each placement and rate (bit-flip duality), peaking at 1111
  where OR3 peaks at 0000.
- **H2 SUPPORTED.** 1of4 party-only equals mediator-only at 0.05 and 0.1, and also at 0.2 (1.110953).
- **H3 SUPPORTED.** 2of4 and 3of4 have whole Φ exactly 0 under party-only noise at every rate, as MAJ3 does.
- **H4 SUPPORTED.** OR3 peaks at the same state (0000, everyone "no") under both placements at 0.05–0.2.
- **H5 SUPPORTED.** 4of4 matches 1of4 under both placements.

## Where the equality comes from (descriptive, after scoring)

Per-state values in `results.json` show what is going on. Under party-only noise all 16 (or 32) states are
reachable, but the full group has positive φ in exactly one: the unanimous state at the rule's
default outcome (0000, everyone "no", for any-yes; 1111 for all-yes). Under mediator-only noise only 4
states are reachable and the full group has positive φ in all four, with the unanimous state the largest
up to r = 0.2. In that state the two placements give the same φ to six decimals (OR3: 1.041518 at 0.2;
1of4: 1.110953 at 0.2). At r = 0.4 the mediator-noise value at the unanimous state drops to 0 and the peak
moves to 0111 (OR3 0.023283), while the party-noise value stays at the unanimous state (0.170446). So the
"equality" in `noise_placement` is a coincidence of one state's φ, not of the two whole systems. We have
not derived analytically why that state's φ is placement-invariant for r ≤ 0.2.

Interior quotas show the opposite pattern: under party-only noise no state has positive full-group φ;
under mediator-only noise all four reachable states have the same φ (MAJ3 0.036624 at 0.2 in each).

## What it means

Where the error sits splits the seven rules into the same two families the deterministic quorum law
already names. For the extreme rules, the binding of the whole shows up in the state where everyone
agrees, and it does not matter whether the coordinator or the parties err, until errors get large. For
interior quotas the whole is bound only through the coordinator's misreading; if the coordinator reads
cleanly, party-side mistakes never make it bound.

## Limits

Three- and four-party yes/no models; equal weights; independent errors; synchronous update; four rates.
Full-group φ only (subset tie sets were not recomputed here). The state-level equality is observed, not
derived.

## Reproduce

```sh
python org_frontier/studies/placement_equality/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/placement_equality/run.py --write   # full run, ~2.2 min
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
