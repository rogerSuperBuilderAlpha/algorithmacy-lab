# Q219 — Who decides an insurance claim? · Stage 1 review

**Question.** When a claimant (C) files a claim that an auto-adjudication engine (E) screens and a human
adjuster (A) may review, which wiring of the three makes the claim decision an irreducible three-party
determination (triadic), and which lets it factor into a pair plus a bystander (dyadic)?

**Agenda id.** None. A new question, drawn from automated claims handling. It sits next to
RESEARCH_AGENDA_50_V2 #39 (`studies/hitl_rubber_stamp/`), which it extends from a generic human-AI loop
to a named insurance workflow with three concrete routing designs.

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #39 study `hitl_rubber_stamp` | HUMAN_COMMIT_READ: a human joins the major complex iff it is in the commit's determination **and** reads the commit; rubber stamps, static vetoes, and read-only observers stay out; an override (S'=H) leaves H in a private {H,S} dyad | Closest prior. Fixes the membership rule this study applies to the adjuster. It used four nodes (H, AI, S, C) with a separate commit node; this study folds the commit into the adjuster or the engine and asks the question for three concrete claims-routing designs |
| #76 regulator | Observer and static veto stay out; a veto that also responds to outcomes joins | Predicts the adjuster's place when it only sees flagged claims (variant b) |
| #21 contestability | Any override or contestability path drops the bound party out (dyadic {S,C}) | Bears on variant c, where the engine learns from adjuster overrides |
| Q11 `questions/q11_oscillatory_scaling/` (and `studies/oscillatory_scaling/`) | The rotating ring `rot_ring(n)`, x_i' = x_{i−1}, a traveling wave of period n, is triadic at Φ_MIP = 2.0 with the full core at n=3..6 | `rot_ring(3)` is the pipe (a) exactly: C'=A, E'=C, A'=E with C, E, A = x0, x1, x2. Settles the pipe prediction as triadic; H1 becomes a replication under the claims labels |
| #116, #103, #105 conjunctive law | An all-required (AND) commit binds every member; Φ = n−1 with the full node set as core | Grounds the prediction that a conjunctive adjuster reading both engine and claimant keeps all three in the core |
| STRUCTURAL_FINDINGS 2–3 | Strict mediation is necessary, not sufficient; the mediator must read all parties and each party's own read must keep it live to the commit | Grounds the pipe (a) prediction: no node in the pipe reads two sources |
| STRUCTURAL_FINDINGS 5 | Substitutability of any role collapses the triad | Bears on variant b, where a claim closes by auto-approval **or** by the adjuster |
| STRUCTURAL_FINDINGS 6 / `multiparty/chains.py` | A mediator chain stays triadic at Φ = 2.0 when each mediator ANDs its two neighbours | Contrast for the pipe: the chain's mediators read both neighbours; the pipe's nodes read one |
| q63 H5 liveness | A recipient read but frozen (R'=R) makes the form dyadic | Grounds the claimant-freezing hypothesis (H5) |
| q68 triage gating | A recipient-side triage agent joins the core only when coupled both ways; monitoring-only or gating-only stays out | Same bidirectional rule, applied to a triage agent |
| `threads/delegation` | Delegation moves standing to the intermediary; the delegating worker is least central | Prior that the engine, standing between claimant and adjuster, may hold standing the claimant loses |
| `studies/irreducibility_catalog` | `insurance_broker` (insured · broker · carrier) reads **partial**, Φ = 1.585, because direct quoting runs alongside | The lab's only insurance form. It models brokerage, not claims adjudication |
| Open PR #811 (q217 robot shared control) | Shared control R'=H∧P with feedback to both is triadic; teleoperation and full autonomy are dyadic | Parallel human + automation structure in robotics; not yet merged |

## The gap

The lab has the membership rule for a human in an AI loop (#39), the oversight ladder (#76), the
conjunctive law, and the liveness condition, but no form in the record models claims adjudication. The
catalog's insurance entry is a broker, and #39 keeps the commit in its own node. No probe asks which of the
three standard claims-routing designs (a pass-through pipe, threshold auto-approval with flagged review,
and a fraud-flag loop in which the engine learns from adjuster overrides) is triadic, or where the
adjuster sits in each. The question is therefore open. Its answer is expected to follow largely from the
standing findings, so its value lies in the explicit forms and in one prediction the record does not
settle: whether the triad in the threshold design exists only in flagged states. The pipe's verdict is
already on record, because Q11's three-node rotating ring is the same form; H1 replicates it under the
claims labels.
