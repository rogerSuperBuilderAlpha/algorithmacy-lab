# Joint-observation cliff under exact Φ — findings

**Verdict: TRANSFER_PARTIAL_EXACT_PHI.** V3 #16’s MI alternation cliff
replicates on family_n3 (0.967→0.585). Under an **exact-Φ** screen,
alternation is only a soft drop on mediation family_n3 (1.000→0.812,
below the cliff bar) but **does cliff on the multifamily panel**
(1.000→0.660). Cross-topo transfer holds for exact Φ; the
mediation-family exact-Φ screen is more robust than MI.

In-silico; exact binary IIT-4.0 via `classify_rules`. Hypotheses fixed
in `hypotheses.md`. Answers RESEARCH_AGENDA_V4 #1. Extends V3 #16
`ALTERNATION_RECREATES_CLIFF` from MI-only / family_n3 to exact-Φ /
cross-topo.

**Validation gap.** Exact-Φ “alt” is an induced-subsystem score
(mean Φ on mediator–party pairs with omitted bits frozen), not a
trajectory mask; multifamily N=24 is designed, not a census.

## Already known

| prior | result |
|---|---|
| V3 #16 correlated party duty | ALTERNATION_RECREATES_CLIFF — MI alt ≈ chance; phase holds |
| V2 #24 partial observation | HIDDEN_COLLAPSE_INTERMITTENT_CLIFF |
| V3 lane close | suggested exact-Φ / multifamily transfer as V4 opener |

## Panel AUCs

| panel | screen | AUC |
|---|---|---:|
| family_n3 | phi_full | **1.000** |
| family_n3 | phi_alt | 0.812 |
| family_n3 | phi_zero_duty_B | 0.792 |
| family_n3 | mi_full | **0.967** |
| family_n3 | mi_alt | **0.585** |
| multifamily | phi_full | **1.000** |
| multifamily | phi_alt | **0.660** |

Cliff: AUC < 0.70 or drop ≥ 0.20 from phi_full. Hold: AUC ≥ 0.85.

## Hypotheses

| H | result |
|---|---|
| H1 MI alt cliffs on family_n3 | **SUPPORTED** |
| H2 exact-Φ alt cliffs on family_n3 | **REFUTED** |
| H3 exact-Φ alt cliffs on multifamily | **SUPPORTED** |
| H4 exact-Φ full holds both panels | **SUPPORTED** |
| H5 exact-Φ zero-duty cliffs family_n3 | **SUPPORTED** |

## Reading

Losing joint party observation still matters under exact Φ, but the
damage is screen- and family-dependent. MI on mediation family_n3
collapses under alternation; exact Φ on the same family only softens.
On a hub/chain/pool/ring multifamily panel, the exact-Φ alt screen
crosses the cliff bar. Zero-duty under exact Φ also cliffs on
family_n3 (drop 0.208). Practice: do not treat the MI cliff as a
literal exact-Φ theorem on mediation forms; do expect exact-Φ
joint-observation failure once topology leaves that family.

## Best next (V4)

**#2** closed (`PHASE_RESTORES_JOINT`). Next **#3** — exact-Φ zero-duty
vs induced party–mediator retain.

## Reproduce

```
python org_frontier/studies/joint_obs_cliff_exact_phi/analyze_transfer.py
```
