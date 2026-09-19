# Imputer under exact Φ — findings

**Verdict: COPY_RESTORES_RING_FAILS.** Under hide-party, V3 #15’s
**copy-W** imputer restores exact-Φ ranking (1.000→0.896), but the
**ring prior** that restored MI does not (→0.806). Imputation is not
MI-only, and it is not a blanket transfer: party-echo completes Φ
rank; cycle-copy does not.

In-silico; exact binary IIT-4.0 via `classify_rules`. Hypotheses fixed
in `hypotheses.md`. Answers RESEARCH_AGENDA_V4 #4. Extends V3 #15
`IMPUTER_RESTORES_AUC` and V4 #1–#3 exact-Φ arc.

**Validation gap.** Structural rule-swap is the exact-Φ analogue of
trajectory imputation, not a field missing-data model; AUCs are about
designed Boolean forms, not organizations.

## Already known

| prior | result |
|---|---|
| V3 #15 | IMPUTER_RESTORES_AUC — ring MI 0.550→0.944; copy-W 0.932 |
| V4 #1–#3 | exact-Φ joint / phase / zero-duty–retain; retain fails with zero |
| V2 #24 | role-gated hide-party collapse |

## Panel (`family_n3`, SEED 15)

| screen | AUC |
|---|---:|
| MI full | **1.000** |
| MI hide party C | **0.550** |
| MI ring prior | **0.944** |
| MI naive copy-W | **0.932** |
| Φ full | **1.000** |
| Φ omit C | **0.750** |
| Φ copy-W (`C'=W`) | **0.896** |
| Φ ring (`C'=S`) | **0.806** |
| Φ const-0 | **0.500** |

Restore bar: AUC ≥ 0.85 or within 0.10 of full. Cliff: AUC < 0.70 or
drop ≥ 0.20.

## Hypotheses

| H | result |
|---|---|
| H1 MI restore replicates #15 | **SUPPORTED** |
| H2 copy-W restores exact Φ | **SUPPORTED** |
| H3 ring prior restores exact Φ | **REFUTED** |
| H4 omit cliffs + const0 fails | **SUPPORTED** |
| H5 full Φ holds | **SUPPORTED** |

## Reading

MI restore from V3 #15 replicates exactly. Completing the hidden
party’s update with **copy-W** puts exact-Φ ranking back above the
restore bar. Completing it with the **ring generative rule** (`C'=S`)
does not — soft fail (0.806), not a cliff. Omitting C cliffs by drop
(1.000→0.750); constant-0 fails. So the #15 ring win is **screen-
specific**: it rescues mean-MI, not exact Φ. Copy-W is the imputer that
transfers. Practice: do not treat a topology prior that fixes MI as Φ-
safe; party-echo is the cheap structural fill that also ranks under Φ
here.

## Best next (V4)

**#5** — across topologies, does a topology-matched imputer beat a
mismatched prior under exact Φ?

## Reproduce

```
python org_frontier/studies/imputer_exact_phi/analyze_imputer_phi.py
```
