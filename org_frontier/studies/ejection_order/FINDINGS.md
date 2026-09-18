# Extractive ejection order — findings

**Verdict: CO_EJECT_TO_OWNER.** An extractive commit’s ejection order
**reproduces #110**: `{W,S,C}` → null → `{S,P}` with **W/C co-ejection**
(role symmetry #55). There is **no transferable fine order** W≺C≺R.
Regulator standing and single-party ablation are **encoding-local**.
The predictive claim for stakeholders is co-loss of parties under
owner tilt — not a ranked first-loss list. In-silico only.

Hypotheses fixed in `hypotheses.md`. Cited: #110/#78/#55; #29–#35
pointers only. Closed lanes stay closed. Candid N.

## Hypotheses

| H | result |
|---|---|
| H1 #110 path co-eject→owner | **SUPPORTED** |
| H2 strict W≺C≺R fine order | **REFUTED** |
| H3 encoding sets residual | **SUPPORTED** |

## Path (witnesses)

| form | core |
|---|---|
| w_P=0 (#110) | {W,S,C} |
| w_P=1 | ∅ (null) |
| w_P≥2 | {S,P} |
| +R gate thr=3, w_P=0 | {W,S,C,R} |
| +R … w_P=1,2 | ∅ |
| +R … w_P=3 | {S,P} |
| S'=P∧R | {S,P,R} |
| S'=P, R monitors | {S,P} |
| ablate W / C from commit | {S,C,P} / {W,S,P} |

## vs “who loses standing first”

#110 already answers the transferable part: parties lose together;
owner-core remains. Extending R does not produce a universal
first-loss ranking — R can share an early oversight core, exit through
null with the parties, or join a late `{S,P,R}` only when the commit
encoding binds R. Ablation shows a party loses alone only when removed
from the commit (local, not a tilt-order law).

## Limits

Boolean designed panel; threshold weights discrete; no organization
measured; “predict real stakeholders” = structural ranking on the
model, not an empirical forecast.

## Best next

**PE lane closable** — synthesis in `POLITICAL_ECONOMY_ARC.md`.

## Reproduce

```
python org_frontier/studies/ejection_order/analyze_eject.py
```
(~10 s)
