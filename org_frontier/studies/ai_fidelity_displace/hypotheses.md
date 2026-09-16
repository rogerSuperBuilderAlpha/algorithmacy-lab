# AI fidelity displace — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #40).** Does an AI that
online-learns the counterpart's policy displace the counterpart over
training, and does the displacement track model fidelity (#69)?

**Already known (cited, not reopened).**
- #37–#39 pointers only (protocol / tool / HITL membership bridges).
- Probe #69 (`probe_model_fidelity`): with `W'=S∧M`, C stays in at
  dead/static/lagged; displaced at full `M'=S` (core `{W,S,M}`).
- Probes #4/#9: blended model displaces C; C and M never coexist.
- Probe #79 adaptive mediator / #80 learning-vs-Φ — different axes
  (reliability drift; success≠Φ); pointers only.
- Formal / stoch–temporal / estimation / construct-omit closed.

**Universe.** Exact binary IIT-4.0 Φ. Nodes `(A, S, C, M)` = AI agent,
system commit, counterpart, learned model of C’s policy. **Honest
proxy:** discrete fidelity rungs stand in for training epochs — this
is **not** SGD / online RL training; no gradients, no replay buffer.
In-silico Boolean abstractions only.

**Definitions (fixed).**
- **fidelity ladder (designed order):** dead → static → wrong-self →
  observe-C → S∧C partial → S∨C partial → full (`M'=S` = C’s rule).
- **displace:** C ∉ major complex.
- **model joins:** M ∈ major complex.
- Agent acts on the model throughout the primary ladder:
  `A'=S∧M`, `S'=A∧C`, `C'=S`.

## Panel

| rung | M' | role |
|---|---|---|
| dead / static / self | 0 / M / A | low fidelity |
| obs_C / S∧C / S∨C | C / S∧C / S∨C | mid fidelity |
| full | S | perfect policy clone |
| controls | unused / pure-act / #69 iso | boundary |

## H1 — C membership declines with fidelity

Along the designed ladder, low-fidelity rungs keep C in the major
complex and the full-fidelity rung puts C out. Null: full keeps C, or
a low rung already ejects C while full does not reverse the pattern.

## H2 — sharp threshold, not smooth glide

The ladder does **not** show a smooth Φ decay with fidelity. C’s
membership (and M’s join) flips at a discrete rung rather than grading
across intermediates. Null: Φ falls monotonically rung-by-rung with a
graded C-out pattern.

## H3 — at full fidelity, M joins and displaces C

At `M'=S`, M is in the major complex and C is out (no coexistence).
Null: coexistence, or M stays out at full.
