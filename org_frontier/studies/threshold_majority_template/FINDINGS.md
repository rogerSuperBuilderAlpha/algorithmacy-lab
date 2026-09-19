# Threshold / majority template — findings

**Verdict: COLLAPSES_TO_REDUNDANCY.** Threshold / majority determination at
n≥4 is **not** a new template. Intermediate k always **factors** once
pivotality is lost — including on shared-mediator and recurrent carriers
that restore triadicity under AND. Only extremes (k=1 OR, k=all AND) keep
a full core. The #10/#67/#117 redundancy-factors pattern holds.

In-silico; binary exact IIT-4.0; n≤5. Hypotheses fixed in `hypotheses.md`
before computing. Grows from V3 #2 / probes #10/#67/#117 / V2 #15–#16.
Ternary / residual-cascade / M3 noted only.

## Already known

| prior | result |
|---|---|
| #10 / #67 majority 2-of-3 | factors → dyadic |
| #117 plain k-of-n hub | only extremes keep full core |
| V2 #16 shared-mediator AND | full-core merge Φ=4 |
| V2 #15 recurrent AND breadth | full-core span |

## Panel (abbrev.)

| cell | role | kind | core Φ |
|---|---|---|---:|
| triad_and | anchor | **full_bind** | 2.0 |
| hub n=4 k=1 / k=3 | extreme | **full_bind** | 3.0 |
| hub n=4 k=2 | intermediate | **factors** | — |
| hub n=5 k=1 / k=4 | extreme | **full_bind** | 4.0 |
| hub n=5 k=2 / k=3 | intermediate | **factors** | — |
| shared_and | AND restore | **full_bind** | 4.0 |
| shared_maj 2of4 / 3of4 | maj on restore | **factors** | — |
| rec_and_b3 | AND restore | **full_bind** | 3.0 |
| rec_maj_b3 | maj on restore | **factors** | — |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 anchors + plain-hub redundancy pattern | **SUPPORTED** |
| H2 AND carriers restore/bind full core | **SUPPORTED** |
| H3 majority on restored carriers factors | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

Topology that restores triadicity under conjunctive seats does not rescue
majority. Shared-mediator and recurrent breadth carriers bind fully under
AND and factor under intermediate threshold on the same wiring. Majority
adds no sixth determination algebra; it is the redundancy-factors pattern
at every carrier tested.

Validation gap: Boolean models, not organizations.

## Best next (V3)

V3 #3 (mixed-algebra seats: parity + conjunctive on one mediator).

## Reproduce

```
python org_frontier/studies/threshold_majority_template/analyze_threshold_majority.py
```
