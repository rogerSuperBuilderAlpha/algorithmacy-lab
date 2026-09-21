# Parity-hub law for n>8 — findings

**Verdict: LAW_HOLDS_NGT8.** The parity-hub law Φ = 2^(2−n) survives
n>8 under the named H-cut formula and a feasible exact SIA check: H-cut
φ matches the law at n∈{8,9,10}; full SIA at n=8 keeps H as MIP with
φ = law. **No topology residual** in the lean window.

In-silico; binary exact IIT-4.0 where feasible. Hypotheses fixed in
`hypotheses.md`. Answers `RESEARCH_AGENDA_V4` #9. Extends V3 #10
`LAW_HOLDS_NGT6` and V2 #47/#49 past the n≤7 major-complex census.

## Already known

| prior | result |
|---|---|
| V2 #47 scaling_laws_closed_form | H-cut φ_s = 2^(2−n) proved; exact Φ n≤5 |
| V2 #49 mincut_mip | MIP = H for parity n≤5 (I=1 uniqueness partial) |
| V3 #10 parity_law_n_gt6 | **LAW_HOLDS_NGT6** — exact Φ = law, full core, H MIP at n∈{6,7} |

## Regime

| n | method | note |
|---:|---|---|
| 3–7 | exact major-complex + SIA | V3 #10 census (controls) |
| 8 | full SIA at all-1s + named H-cut | exact MIP identity feasible (~16 min) |
| 9–10 | named H-cut only | cut-only; major-complex not recomputed |
| ≥11 | out of lean scope | H-cut SS cost grows; leave for later |

Major-complex census stays at n≤7. For n≥8 this cell is a **cut/SIA
regime**: H-cut φ is exact evaluation of the named partition; full SIA
at n=8 proves that partition is the MIP.

## Panel

| n | law 2^(2−n) | H-cut φ | SIA φ | H is MIP | match |
|---:|---:|---:|---:|:---:|:---:|
| 3 | 0.5 | — | 0.5 | yes | yes (V3) |
| 4 | 0.25 | — | 0.25 | yes | yes (V3) |
| 5 | 0.125 | — | 0.125 | yes | yes (V3) |
| 6 | 0.0625 | — | 0.0625 | yes | yes (V3) |
| 7 | 0.03125 | — | 0.03125 | yes | yes (V3) |
| **8** | **0.015625** | **0.015625** | **0.015625** | **yes** | **yes** |
| **9** | **0.0078125** | **0.0078125** | — | — | **yes (cut)** |
| **10** | **0.00390625** | **0.00390625** | — | — | **yes (cut)** |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 V3 #10 controls LAW_HOLDS_NGT6 | **SUPPORTED** |
| H2 H-cut φ = law at n∈{8,9,10} | **SUPPORTED** |
| H3 H is MIP at n=8; φ = law | **SUPPORTED** |
| H4 no residual in checked window | **SUPPORTED** |

## Reading

**#9 exact or residual?** Exact under the lean window. Crossing n=8
does not invent a new parity Φ atom or displace H as MIP: full SIA at
n=8 returns φ = 2^(2−8) with H as MIP, and named H-cut φ tracks the
law through n=10. The closed-form cut prediction remains a faithful
proxy past the V3 #10 major-complex ceiling. Topology residuals do not
appear in this check.

**Limits.** Standard `parity_hub` wiring only; all-1s evaluation;
SET_UNI/BI H-cut; major-complex not recomputed for n≥8; SIA MIP proof
only at n=8 (n≥9 SIA left unrun in lean). No organization measured.

## Best next

**V4 #10** — composed-topology landmarks at n≥6 under a denser
random-coupling draw.

## Reproduce

```
python org_frontier/studies/parity_law_n_gt8/analyze_parity_n_gt8.py
```
(loads committed H-cut panel + sia_n8; `--rebuild-cuts` recomputes
H-cuts ~1 min; `--rebuild-sia` recomputes n=8 SIA ~16 min)
