# Graded × topology carriers — findings

**Verdict: SHARP_HOLDS_ACROSS_TOPO.** Graded min-commit
(`x'=min(·)` / hub `S'=min(W,C)`) keeps **discrete** structure labels
(NULL / DYADIC / TRIADIC) while Φ grades on **hub**, **ring** (n=3,4),
and **necklace** (n=6). No carrier forces a class flip the fixed-hub
V2 #2 panel never saw — every diagonal path is NULL → DYADIC → TRIADIC.

In-silico. Exact IIT-4.0 via `pyphi_iit4_mv`. k=3. Hypotheses fixed in
`hypotheses.md`. Answers RESEARCH_AGENDA_V3 #11. Grows from V2 #2
`SHARP_CLASS_GRADED_PATH` and V3 #4 necklace carrier.

## Already known

| prior | result |
|---|---|
| V2 #2 graded commit (hub) | SHARP_CLASS_GRADED_PATH — NULL→DYADIC→TRIADIC |
| V3 #4 local-triad necklace | COMPOSE_LANDMARK_OR_COLLAPSE (binary) |
| binary ring / hub landmarks | Φ=4 / Φ=n−1 |

## Panel (diagonal L on (L,…,L))

| carrier | n | L=0 | L=1 | L=2 |
|---|---:|---|---|---|
| hub | 3 | NULL Φ=0 | DYADIC Φ≈0.39 | TRIADIC Φ≈3.17 |
| ring | 3 | NULL Φ=0 | DYADIC Φ≈0.47 | TRIADIC Φ≈9.51 |
| ring | 4 | NULL Φ=0 | DYADIC Φ≈0.52 | TRIADIC Φ≈6.34 |
| necklace | 6 | NULL Φ=0 | DYADIC Φ≈0.52 | TRIADIC Φ≈3.17 |

Necklace L≥1 uses exhaustive SIA over subsystems of size ≤4 (size-5
spot checks at L=1 sit at Φ≈0.12 ≪ dyad). At L=2 a local triad ties
the dyad Φ, so the class is TRIADIC under largest-first major complex.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 structure class stays sharp on all carriers | **SUPPORTED** |
| H2 Φ grades with L on all carriers | **SUPPORTED** |
| H3 class path = hub NULL→DYADIC→TRIADIC | **SUPPORTED** |
| H4 panel closed | **SUPPORTED** |

## Reading

Topology changes **magnitudes** (ring-3 L=2 Φ≈9.51 vs hub ≈3.17) and
which nodes sit in the mid-path dyad, but not the **label sequence**.
Graded commit’s sharp-class path is carrier-stable on this panel: ring
and necklace do not invent flips absent from the fixed-hub study.

Validation gap: evidence about Boolean / ternary models, not about
real organizations. Necklace major complex at full n=6, k=3 remains
costly; class verdict for L≥1 rests on size≤4 exhaustiveness plus
size-5 dominance checks.

## Best next (V3)

**#12** noise × composed carrier (party-vs-mediator noise on necklace /
multi-hub span) — continues section D. **#13** validation bridge is the
alternate if empirical render is the priority.

## Reproduce

```
python org_frontier/studies/graded_topo_carriers/analyze_graded_topo.py
```

(default loads committed necklace census; `--rebuild-necklace` recomputes
size≤4 exhaustive SIA, minutes)
