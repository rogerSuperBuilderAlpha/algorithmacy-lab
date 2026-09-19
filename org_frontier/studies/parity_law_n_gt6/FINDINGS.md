# Parity law under n>6 hub embeddings — findings

**Verdict: LAW_HOLDS_NGT6.** The parity-hub law Φ = 2^(2−n) remains
**exact** at n∈{6,7} with full cores. The named hub-preserving cut H is
the MIP at all-1s and matches exact Φ — **no topology residual** when
the cut formula stands in for full enumeration.

In-silico; binary exact IIT-4.0. Hypotheses fixed in `hypotheses.md`.
Answers `RESEARCH_AGENDA_V3` #10. Extends V2 #47/#49/#115 past the n≤5
MIP window.

## Already known

| prior | result |
|---|---|
| #115 parity_hub | XOR hub decays vs conjunctive n−1 |
| #47 scaling_laws_closed_form | cut sel_c = 2^(2−n) proved; exact Φ n≤5 |
| #49 mincut_mip | MIP = H for parity n≤5 (I=1 uniqueness partial) |

## Panel

| n | exact Φ | law 2^(2−n) | full core | H is MIP | cut = exact |
|---:|---:|---:|:---:|:---:|:---:|
| 3 | 0.5 | 0.5 | yes | yes | yes |
| 4 | 0.25 | 0.25 | yes | yes | yes |
| 5 | 0.125 | 0.125 | yes | yes | yes |
| **6** | **0.0625** | **0.0625** | yes | yes | yes |
| **7** | **0.03125** | **0.03125** | yes | yes | yes |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 controls n=3..5 reproduce | **SUPPORTED** |
| H2 exact law at n>6 | **SUPPORTED** |
| H3 H-cut MIP matches exact | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

**#10 exact or residual?** Exact. Crossing n=6 does not invent a new
parity Φ atom or displace H as MIP. The closed-form cut prediction
2^(2−n) remains a faithful proxy for exact major-complex Φ through n=7
on the standard hub embedding. The #49 general-n I=1 uniqueness residual
is not a Φ-value residual in this window.

**Limits.** Standard `parity_hub` wiring only; all-1s SIA; SET_UNI/BI;
n≤7 (n=8 not required once n=7 decides). No organization measured.

## Best next

**V3 #11** (graded×topo on ring/hub/necklace) — recommended next cell.

## Reproduce

```
python org_frontier/studies/parity_law_n_gt6/analyze_parity_n_gt6.py
```
(loads committed census; `--rebuild` recomputes exact Φ, ~10 min)
