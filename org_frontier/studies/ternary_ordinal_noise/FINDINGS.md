# Neighbour-only slips raise Φ but do not change who is bound together, until noise is heavy

Exact IIT 4.0 Φ on the multivalued overlay `third_party/pyphi_iit4_mv` (stock pin `b78d0e342`
underneath). Hypotheses were fixed in [hypotheses.md](hypotheses.md) and pushed in commit `12fb327a`
before any computation.

## Setup

Two noise shapes on {0,1,2} readings at rate r. **Uniform**: slip to either other value (r/2 each).
**Ordinal**: 0 → 1 and 2 → 1 with probability r; 1 → 0 or 2 with r/2 each; never 0 ↔ 2.
Hub: mediator S + three parties; S commits median or min of its readings; parties copy S.
Triad: W' = S, C' = S, S' = |W − C| or min(W, C); binary XOR on {0,1} as reference. Whole Φ = largest
full-system φ over reachable states; "full core" = the whole system is the maximal complex at every
whole-Φ state. Control passed: uniform hub median at r = 0.1 = 0.022209 and uniform |W − C| triad at
r = 0.1 = 0.759836 (the earlier studies' values).

## Whole-system Φ (full core: ✓ yes, ✗ no)

| case | shape | 0.01 | 0.05 | 0.1 | 0.2 | 0.4 |
|---|---|---:|---:|---:|---:|---:|
| hub median | uniform | | 0.012445 ✗ | 0.022209 ✗ | 0.033668 ✗ | 0.029390 ✗ |
| hub median | ordinal | | 0.013180 ✗ | 0.025018 ✗ | 0.043601 ✗ | 0.055977 ✗ |
| hub min | uniform | | 3.886383 ✓ | 3.133882 ✓ | 1.940021 ✓ | 0.549502 ✓ |
| hub min | ordinal | | 3.980332 ✓ | 3.295721 ✓ | 2.173498 ✓ | 0.234264 ✓ |
| triad abs(W − C) | uniform | 1.049206 ✓ | 0.913476 ✓ | 0.759836 ✓ | 0.503242 ✓ | 0.169599 ✗ |
| triad abs(W − C) | ordinal | 1.066891 ✓ | 0.994459 ✓ | 0.903754 ✓ | 0.680000 ✓ | 0.275868 ✗ |
| triad min | uniform | 3.078421 ✓ | 2.727286 ✓ | 2.321394 ✓ | 1.616684 ✓ | 0.610558 ✓ |
| triad min | ordinal | 3.092597 ✓ | 2.793215 ✓ | 2.441275 ✓ | 1.811248 ✓ | 0.842346 ✓ |
| triad XOR {0,1} | flip | 0.475960 ✗ | 0.387335 ✗ | 0.292615 ✗ | 0.150826 ✗ | 0.014712 ✗ |

## Scores

- **H1 SUPPORTED.** Under ordinal noise the hub median never has a full core (cores {S,Pi,Pj} or {S,Pi}).
- **H2 SUPPORTED.** Under ordinal noise the hub min has the full group at every rate.
- **H3 REFUTED at r = 0.4.** Ordinal hub min is above uniform at r = 0.05, 0.1, 0.2 but below at 0.4
  (0.234264 vs 0.549502).
- **H4 REFUTED at r = 0.4.** Uniform |W − C| triad has a full core at 0.05, 0.1 and 0.2, not at 0.4,
  where the maximal complex is {S,C}, {W,S} or {W,S,C} depending on the state (best core φ 0.176237).
- **H5 REFUTED at r = 0.4.** Same pattern under ordinal noise: full core to 0.2; at 0.4 the core is
  {W,S} (φ 0.304181).
- **H6 SUPPORTED.** Binary XOR never has a full core; {W,S} wins at every rate.

## Reading

The shape of the noise changes how much Φ there is but not who is bound together, except near heavy
noise. Neighbour-only slips keep more of each reading's information, and at r ≤ 0.2 they give more Φ
in all four three-valued cases. At r = 0.4 the two shapes part ways: the hub min has less Φ under ordinal slips than
under uniform ones, while the median keeps rising under ordinal slips (0.055977, its highest value on this
grid). We have not traced why; item 2 of the backlog compares the per-state values. The comparison triad (|W − C|) binds the whole trio from very small noise
(0.01) up to 0.2 under either shape, while its binary XOR version never does: the gain from the middle
value found in `ternary_lift_panel` is not a single-rate accident, but it does not survive r = 0.4.

## Limits

Two noise shapes, independent slips, synchronous update, three or four nodes, one lift per rule here.
The maximal-complex API returns one complex per state; ties are not enumerated. 1e-9 threshold.

## Reproduce

```sh
python org_frontier/studies/ternary_ordinal_noise/run.py --quick   # about 10 s (CI check)
python org_frontier/studies/ternary_ordinal_noise/run.py --write   # about 3.5 min
```

Python 3.12, PyPhi 1.2.1.dev1470+gb78d0e342 plus the vendored overlay. The full run took 210 s on the
lab box. An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this
report; every number above is printed by `run.py` or stored in `results/`. No human review is claimed.
