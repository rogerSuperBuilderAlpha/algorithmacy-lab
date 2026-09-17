# Political economy arc — #29–#36 (closed)

Short spine for the political-economy lane on `RESEARCH_AGENDA_50_V2`
(PR #739). Exact binary IIT-4.0 Φ; in-silico. Construct/omit,
estimation, stoch-temporal, formal #47–#50, and AI #37–#41 stay closed
except as pointers.

## Status — all answered

| # | study | verdict |
|---|---|---|
| 29 | `dual_principal_conflict/` | CONFLICT_ENCODING |
| 30 | `endogenous_coalition/` | MULTI_NASH_MAXPAY |
| 31 | `worker_union_scale/` | UNION_MIRRORS_COAL |
| 32 | `rival_platforms/` | RIVAL_ENCODING |
| 33 | `regulator_capture/` | SHARP_FULL_CAPTURE |
| 34 | `algo_transparency/` | OPEN_ACT_CUT |
| 35 | `gig_substitution/` | DROP_AT_FIRST_SUBST |
| 36 | `ejection_order/` | **CO_EJECT_TO_OWNER** |

## Working picture (synthesis)

**Encoding decides conflict and rivalry.** Dual principals
(#29) and rival platforms (#32) have no single winner rule:
extractive asymmetry captures; joint COMMIT_READ / cross-binding
shares; unresolved or substitutable encodings collapse.

**Coalitions are multi-Nash; unions mirror them.** Endogenous join
(#30) sustains both all-out and all-in at max own-core pay. Worker
unions (#31) match counterpart-coalition scaling cell-for-cell and
**do not vanish** at n=6 the way #97’s random single-mediator
triadicity does.

**Oversight becomes capture at one cut.** A regulator that gates and
is gated (#33) stays oversight until fully platform-determined
(`R'=W∧S∧C`); that step is `{S,R}` — sharp, not a membership glide.

**Openness without action is theater.** Publishing the commit rule
(#34) without parties acting leaves the party core unchanged; acting
on the opened rule can flip core membership or raise Φ only. Not
channel transparency (#24).

**First substitution drops the worker.** In a symmetric gig match
(#35), any positive substitution rate `r=1−m/k>0` ejects every
individual worker from the major complex; all-required solidarity
never does through k=4.

**Extractive ejection is co-loss to the owner.** Tilting the commit
toward the principal (#36 / #110) sends `{W,S,C}` → null → `{S,P}`
with W and C leaving together. No transferable fine order W≺C≺R;
regulator residuals are encoding-local. The stakeholder prediction
is party co-ejection under owner tilt, not a ranked first-loss list.

## Lane status

**Closable.** #29–#36 answered under exact binary IIT-4.0 Φ. Residual
gap (if any): empirical mapping of these encodings onto measured
platforms — out of scope for this in-silico lane.

## Reproduce

```
python org_frontier/studies/ejection_order/analyze_eject.py
```
