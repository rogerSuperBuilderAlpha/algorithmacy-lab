# Correlated party duty cycles — findings

**Verdict: ALTERNATION_RECREATES_CLIFF.** Alternating observation of the
two parties (each δ≈0.5, never jointly observed) does **not** soften
V2 #24’s δ=0 cliff — MI AUC stays near chance (0.571 vs full 0.892).
Any zero-duty party also cliffs. Phase-locked same-slot duty at δ=0.5
holds (0.898). The cliff is about losing **party–party joint
observation**, not about mean duty alone.

In-silico; exact binary IIT-4.0 labels; family_n3 mean-MI. Hypotheses
fixed in `hypotheses.md`. Answers RESEARCH_AGENDA_V3 #16 (last V3
cell). Extends V2 #24 `HIDDEN_COLLAPSE_INTERMITTENT_CLIFF` with
correlated duty schedules; does not reopen the full δ grid.

**Validation gap.** Duty masks are designed observation schedules on
synthetic trajectories, not field logging policies; AUC is about the
cheap screen, not about recovering true Φ.

## Already known

| prior | result |
|---|---|
| V2 #24 partial observation | HIDDEN_COLLAPSE_INTERMITTENT_CLIFF — hide party collapses; δ≥0.10 holds; cliffs at δ=0 |
| V3 #15 topology-aware imputer | IMPUTER_RESTORES_AUC — ring prior restores hide-party MI |
| ESTIMATION_ARC | topology bottleneck; lane closed on #21–#25 |

## Panel (`family_n3`, T=2000, noise=0.08)

| regime | MI AUC |
|---|---:|
| full | **0.892** |
| zero-duty C | **0.505** |
| zero-duty W | **0.528** |
| sparse C δ=0.10 | **0.896** |
| alt W/C (alternating, no joint WC) | **0.571** |
| phase W/C δ=0.50 (same slots) | **0.898** |
| hide mediator | **0.889** |

Soften bar: AUC ≥ 0.85 or within 0.10 of full. Cliff bar: AUC < 0.70
or drop ≥ 0.20.

## Hypotheses

| H | result |
|---|---|
| H1 zero-duty recreates cliff | **SUPPORTED** |
| H2 alt_WC softens cliff | **REFUTED** |
| H3 phase_WC softens | **SUPPORTED** |
| H4 sparse δ=0.10 holds | **SUPPORTED** |
| H5 hide mediator stays ≥0.85 | **SUPPORTED** |

## Reading

#24’s cliff is not repaired by giving each party a healthy mean duty if
the parties never co-occur in the log. Strict alternation kills
complete-case MI(W,C) while leaving WS and CS pairs; the screen still
collapses. Phase-locking the same half of slots at δ=0.5 preserves
joint WC and holds. Sparse independent δ=0.10 on one party also holds.
Practice: do not treat “both parties logged half the time” as safe —
if their duty cycles are anti-correlated, the cheap MI screen fails the
same way as total silence on one party. Cascade / exact Φ remains the
backstop when party–party joints are missing.

## Best next

V3 agenda closed. See [`V3_LANE_CLOSE.md`](../../V3_LANE_CLOSE.md).
Suggested V4 first cell: field / multi-family transfer of the
party–party joint-observation requirement (does the alternation cliff
survive outside strict-mediation family_n3?).

## Reproduce

```
python org_frontier/studies/correlated_party_duty/analyze_duty.py
```
