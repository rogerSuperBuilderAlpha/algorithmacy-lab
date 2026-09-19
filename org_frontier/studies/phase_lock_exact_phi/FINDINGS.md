# Phase-locked duty under exact Φ — findings

**Verdict: PHASE_RESTORES_JOINT.** At matched mean party duty δ=0.5,
**phase-locked same-slot** observation restores exact-Φ ranking on the
multifamily panel (AUC **1.000**) where **alternation** cliffs
(**0.660**). Joint observation — not mean duty — is the causal factor.
MI echoes the same pattern on family_n3 (phase 0.913 vs alt 0.592).

In-silico; exact binary IIT-4.0 via `classify_rules`. Hypotheses fixed
in `hypotheses.md`. Answers RESEARCH_AGENDA_V4 #2. Extends V4 #1
`TRANSFER_PARTIAL_EXACT_PHI` and V3 #16’s MI phase-hold.

**Validation gap.** Exact-Φ “phase” admits the full form by design
(joint slots exist); “alt” scores induced mediator–party pairs. Duty
masks for MI are synthetic schedules, not field logs.

## Already known

| prior | result |
|---|---|
| V4 #1 exact-Φ transfer | TRANSFER_PARTIAL_EXACT_PHI — alt cliffs multifamily; soft on family_n3 |
| V3 #16 correlated duty | ALTERNATION_RECREATES_CLIFF — MI phase holds, alt cliffs |
| V2 #24 | HIDDEN_COLLAPSE_INTERMITTENT_CLIFF |

## Panel AUCs (δ=0.5 matched)

| panel | screen | AUC |
|---|---|---:|
| multifamily | phi_full | **1.000** |
| multifamily | phi_alt | **0.660** |
| multifamily | phi_phase | **1.000** |
| family_n3 | phi_phase | **1.000** |
| family_n3 | mi_full | **0.917** |
| family_n3 | mi_alt | **0.592** |
| family_n3 | mi_phase | **0.913** |

Mean party duty: alt=0.500, phase=0.500.

## Hypotheses

| H | result |
|---|---|
| H1 exact-Φ alt cliffs multifamily | **SUPPORTED** |
| H2 exact-Φ phase holds multifamily | **SUPPORTED** |
| H3 exact-Φ phase holds family_n3 | **SUPPORTED** |
| H4 MI phase holds / alt cliffs | **SUPPORTED** |
| H5 mean duty matched at 0.5 | **SUPPORTED** |

## Reading

Holding mean duty fixed, only the correlation of party observation
changes the exact-Φ screen: co-presence (phase) recovers full-form Φ
ranking; anti-correlation (alt) does not. The V4 #1 multifamily cliff
is therefore a joint-observation failure, not a duty-budget failure.
Same lesson for MI on mediation family_n3.

## Best next (V4)

**#3** — under exact Φ, is zero-duty of one party still enough to cliff,
or can an induced party–mediator subsystem retain rank?

## Reproduce

```
python org_frontier/studies/phase_lock_exact_phi/analyze_phase.py
```
