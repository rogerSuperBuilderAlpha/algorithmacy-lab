# Weakest Boolean render — findings

**Verdict: ROLE_COUNTS_HUB_WEAKEST.** The weakest Boolean render of the
committed public OSS coordination logs that still recovers the conjunctive
Φ=n−1 scaling signature is **role-count cardinality → conjunctive hub
template**. Activity thresholds/fits and institutional elicits miss that
bar. Weaker count-only wirings (identity, cycle-copy, k-of-n) also miss.

In-silico; exact binary IIT-4.0. Hypotheses fixed in `hypotheses.md`.
Answers RESEARCH_AGENDA_V3 #13. Extends V2 #45
`LAW_ONLY_UNDER_STRONG_MODEL` by ranking the three named render classes
by weakness.

**Validation gap.** Evidence about Boolean *renders* of public recurrence
CSVs, not about measured organizations. The hub template is a modeling
choice; role schemas are public pipeline labels (PyPhi triad / sklearn–k8s
four-role), not ethnographic role inventories.

## Already known

| prior | result |
|---|---|
| V2 #45 real Boolean renders | LAW_ONLY_UNDER_STRONG_MODEL — elicits/fits miss; forced hub recovers |
| Probe #116 | conjunctive hub Φ=n−1, full core |
| V3 #12 noise×compose | SAME_PSTAR_COMPOSED (pointer) |

## Panel (signature = Φ≈n−1 and \|core\|=n)

| class | cell | n | Φ | \|core\| | SIG |
|---|---|---:|---:|---:|:---:|
| control | hub | 3,4 | 2,3 | 3,4 | yes |
| role counts | identity | 3,4 | 1,1 | 1,1 | no |
| role counts | cycle-copy | 3,4 | 2,2 | 3,4 | n=3 only |
| role counts | k-of-n | 3,4 | 6/12 | n | no |
| **role counts** | **hub** | **3,4** | **2,3** | **3,4** | **yes** |
| activity | fit (core/recent) | 3,4 | 1,1 | 1,1 | no |
| activity | thr k=1 / k=n−1 | 3,4 | 6/12 | n | no |
| institutional | pyphi v9 triad | 3 | 2 | 3 | yes* |
| institutional | sklearn v10 | 4 | 2 | 3 | no |
| institutional | k8s v11 | 4 | 2 | 3 | no |

\*n=3 triad match only — does not clear the scaling bar.

## Hypotheses

| H | result |
|---|---|
| H1 institutional elicits miss scaling bar | **SUPPORTED** |
| H2 activity thresholds/fits miss scaling | **SUPPORTED** |
| H3 role-count→hub recovers scaling bar | **SUPPORTED** |
| H4 weaker count-only forms miss scaling | **SUPPORTED** |
| H5 panel closed | **SUPPORTED** |

## Reading

Richer information does not buy the law. Institutional elicits and
activity time series are *stronger* inputs than a role count, yet they
fail Φ=n−1 at n≥4. The minimal recovering recipe uses only the
cardinality of the public role schema and the conjunctive hub template —
the same strong modeling move #45 isolated, now ranked as weakest among
the three named classes. Cycle-copy can match the n=3 triad but not the
scaling law.

## Best next (V3)

**#14** Wageman×landmark — does measured W predict the Φ landmark
(ring-4 vs hub-(n−1) vs pool)? Alternate **#15** topology-aware imputer.

## Reproduce

```
python org_frontier/studies/weakest_boolean_render/analyze_weakest_render.py
```
