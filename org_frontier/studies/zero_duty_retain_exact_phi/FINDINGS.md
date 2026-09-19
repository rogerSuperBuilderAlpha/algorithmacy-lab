# Zero-duty vs party–mediator retain — findings

**Verdict: RETAIN_FAILS_WITH_ZERO.** Under exact Φ, **zero-duty on a
party cliffs** (multifamily 1.000→0.592; family_n3 1.000→0.750), and the
induced **party–mediator retain** path fails with it (same AUCs:
0.592 / 0.750). There is no escape through Φ({M,A}) alone. Omitting
the mediator also cliffs (0.559). The cliff is not “only missing
party–party joints while a retain path still ranks.”

In-silico; exact binary IIT-4.0 via `classify_rules`. Hypotheses fixed
in `hypotheses.md`. Answers RESEARCH_AGENDA_V4 #3. Extends V4 #1/#2
joint-observation arc.

**Validation gap.** Retain/zero-duty are induced-subsystem Φ scores
with frozen omitted bits, not logged duty masks; multifamily is
designed N=24.

## Already known

| prior | result |
|---|---|
| V4 #1 | TRANSFER_PARTIAL_EXACT_PHI — alt cliffs multifamily |
| V4 #2 | PHASE_RESTORES_JOINT — joint (not mean duty) restores |
| V3 #16 / V2 #24 | MI hide-party / zero-duty cliffs |

## Panel AUCs

| panel | screen | AUC |
|---|---|---:|
| multifamily | phi_full | **1.000** |
| multifamily | phi_zero_duty_B | **0.592** |
| multifamily | phi_retain_MA | **0.592** |
| multifamily | phi_omit_M | **0.559** |
| family_n3 | phi_full | **1.000** |
| family_n3 | phi_zero_duty_B | **0.750** |
| family_n3 | phi_retain_MA | **0.750** |

On family_n3, zero≡retain on **48/48** forms (n=3 identity). On
multifamily, **20/24** identical; panel AUCs still match.

## Hypotheses

| H | result |
|---|---|
| H1 zero-duty cliffs multifamily | **SUPPORTED** |
| H2 retain_MA holds multifamily | **REFUTED** |
| H3 zero-duty cliffs family_n3 | **SUPPORTED** |
| H4 omit-mediator cliffs multifamily | **SUPPORTED** |
| H5 full holds + n=3 identity | **SUPPORTED** |

## Reading

With a party fully absent, scoring the remaining party–mediator pair
does not keep exact-Φ ranking above the cliff bar. That rules out a
“retain path still ranks” escape. Together with V4 #2 (phase restores
when parties are jointly admitted), the picture is: **joint
party–mediator–party structure** is needed for the full-form exact-Φ
screen; neither anti-correlated half-duty nor a leftover pair after
zero-duty substitutes for it. Omitting the mediator likewise cliffs,
so critical-role absence in general is enough under these subsystem
scores.

## Best next (V4)

**#4** — does V3 #15’s ring-prior (or copy-W) restoration transfer
under exact-Φ scoring?

## Reproduce

```
python org_frontier/studies/zero_duty_retain_exact_phi/analyze_retain.py
```
