# Regulator capture — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #33).** A regulator that gates the
platform but is itself gated by it: at what coupling does oversight
become capture (#76, #111)?

**Already known (cited, not reopened).**
- #76: observer and static veto stay out; veto+responsive
  (`S'=W∧C∧R`, `R'=S`) joins — effective oversight must be
  bidirectional.
- #111: number does not rescue observe-only; joint gate
  `S'=W∧C∧R1∧R2` with responsive reads puts both regulators in.
- Principal FINDINGS: heavily coupled principal can hollow the core to
  `{S,P}` (pointer for the capture analogue).
- #29–#32 CONFLICT_ENCODING / MULTI_NASH_MAXPAY / UNION_MIRRORS_COAL /
  RIVAL_ENCODING — pointers only.
- Other lanes closed.

**Universe.** Exact binary IIT-4.0 Φ. Nodes `(W, S, C, R)` = worker,
system, counterpart, regulator. Designed coupling panel + R-read
sweep under mutual gate `S'=W∧C∧R`. Candid N. In-silico Boolean
abstractions.

**Definitions (fixed).**
- **Out:** `"R" ∉` major complex.
- **Oversight:** R in core and both W and C in core (regulator joins
  without ejecting parties).
- **Partial:** R in core but at least one of {W,C} out (hollowed but
  not pure `{S,R}`).
- **Capture:** major complex equals `{S,R}` (platform+regulator core;
  parties ejected).
- **Sharp threshold:** capture appears at one discrete coupling step
  with oversight (or partial) on the adjacent weaker step — not a
  multi-rung glide of party membership.
- **Smooth shift:** party membership in the major complex changes
  gradually across ≥3 ordered coupling rungs (Φ or n_parties monotone
  glide), with no single-step jump into `{S,R}`.

## Panel (designed)

| id | role |
|---|---|
| observer / veto_only / veto_resp | #76 ladder |
| R-read sweep under `S'=W∧C∧R` | coupling (static → full {W,S,C}) |
| no-gate R-read control | gate necessary |
| extractive `S'=R` / `S'=R∨(W∧C)` | capture witnesses |
| joint two-regulator (#111 pointer) | coalition contrast |

## H1 — sharp capture threshold in coupling

There exists an ordered coupling (R-read cardinality or named rung)
where the weaker step is oversight or partial and the next step is
capture (`{S,R}`). Null: no such adjacent pair, or capture never
appears.

## H2 — smooth membership shift

Party membership (count of {W,C} in core) glides across ≥3 ordered
R-read rungs under the mutual gate, without a single-step jump into
capture. Null: the ordered sweep is discrete (out/partial/oversight
then a jump to capture) rather than a smooth glide.

## H3 — regulator stays out / always in under designed forms

Either every designed form has R out, or every form has R in. Null:
both out and in (oversight or capture) appear on the panel.
