# Φ-ascent adaptive mediator — findings

**Verdict: PLATEAU_ELSE_POOL.** A mediator that greedily climbs exact
Φ does **not** converge to the conjunctive hub. Under fixed party
reads (W′=C′=S), S′-rule ascent stops on a **46-form Φ=2 plateau**
(AND/OR among them; only 0.8%/1.2% of starts terminate at AND/OR).
When the move set can open topology, ascent reaches the catalog
Φ-maximum: **pool uniquely at n=4** (Φ=12); **pool/ring tie at n=3**
(Φ=6). Opposite of #79's drop-a-party path (Φ 2→0, dyadic at r=0).

In-silico; exact IIT-4.0; candid N (n=3 exhaustive S′; n∈{3,4}
topology catalog). Hypotheses fixed in `hypotheses.md`. Cited: #79;
zoo #104/#116/#132; `STOCH_TEMPORAL_ARC.md`. Estimation / construct /
omit / ladder closed.

## Panel A — mechanism (256 S′ masks)

| | |
|---|---|
| Φ\* | 2.0 (46 maximizers) |
| AND hub in max? | yes (2/256 terminals) |
| OR hub in max? | yes (3/256 terminals) |
| Distinct terminals | 59 |

## Panel B — topology catalog

| n | hub Φ | pool Φ | ring Φ | all starts → |
|---:|---:|---:|---:|---|
| 3 | 2 | **6** | **6** | catalog max (5→pool, 1 stays ring) |
| 4 | 3 | **12** | 4 | **pool** (6/6) |

## vs #79

| epoch | r | Φ | verdict |
|---:|---:|---:|---|
| 0 | 1.00 | 2.000 | triadic |
| 4 | 0.00 | 0 | dyadic |

#79 learns *away* from a party and collapses. Φ-ascent learns *toward*
integration and climbs — but not to a unique hub.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 to conjunctive hub | **REFUTED** |
| H2 to pool / catalog max | **SUPPORTED** |
| H3 somewhere else / plateau | **SUPPORTED** |

## Reading

Hub is a maximizer under strict mediation, not the attractor of greedy
mechanism search. Opening topology selects the strongest coupling in
the menu — the all-required pool once n separates it from the ring.
Designed witnesses: 256-mask plateau; n=4 pool basin; #79 contrast.

## Limits

Discrete greedy ascent only; fixed party reads on Panel A; six-form
topology catalog; n≤4. No continuous weights, no organization
measured.

## Best next experiment

Done: #12 **STILL_DEPENDENT** (`continuous_time_invariance/`).
Stoch-temporal lane **closable** (`STOCH_TEMPORAL_ARC.md`). Prefer
agenda **#15+** (hierarchy / topology). Do not reopen estimation /
construct / omit / ladder.

## Reproduce

```
python org_frontier/studies/phi_ascent_mediator/analyze_ascent.py
```
(~12 s)
