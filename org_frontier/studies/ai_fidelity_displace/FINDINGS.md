# AI fidelity displace — findings

**Verdict: SHARP_FULL_DISPLACE.** An AI that acts on a learned model of
the counterpart’s policy displaces C at **full** fidelity only
(`M'=S` → core `{A,S,M}`, C out). Low-fidelity rungs keep C. Φ stays
flat (~2) — not a smooth glide. Mid rungs can eject C **without** M
joining. Matches #69 under AI relabeling. Candid: fidelity rungs are
an honest proxy for training epochs, not actual SGD.

In-silico; candid N (designed ladder). Hypotheses fixed in
`hypotheses.md`. Cited: #69/#4/#9; #37–#39 pointers only. Formal /
stoch–temporal / estimation / construct-omit closed.

## Hypotheses

| H | result |
|---|---|
| H1 C declines (low in, full out) | **SUPPORTED** |
| H2 sharp threshold, not Φ glide | **SUPPORTED** |
| H3 full: M joins and displaces C | **SUPPORTED** |

## Fidelity ladder (`A'=S∧M`, `S'=A∧C`, `C'=S`)

| rung | M' | Φ | core | C | M | displace |
|---|---|---:|---|:---:|:---:|:---:|
| dead | 0 | 2 | {S,C} | in | out | no |
| static | M | 2 | {A,S,C} | in | out | no |
| self | A | 2 | {S,C} | in | out | no |
| obs_C | C | 2 | {A,S} | **out** | out | no |
| partial_and | S∧C | 2 | {A,S} | **out** | out | no |
| partial_or | S∨C | 2 | {A,S,C} | in | out | no |
| **full** | **S** | 2 | **{A,S,M}** | **out** | **in** | **YES** |

## Controls / witnesses

- `full_unused` / `full_pure_act`: M full but unused or pure-act → C
  stays; blend required (#4/#38).
- `#69 iso`: `(W,S,C,M)` full ≅ AI full.
- Mid C-out without M join: `obs_C`, `partial_and` — ejection ≠
  model-takeover.

## Reading

Displacement **tracks** fidelity as a **threshold**, not a curve: only
the perfect policy clone hands the core to M. Partial clones do not
gradually promote M. Some mid-fidelity updates drop C from the major
complex while leaving a lean `{A,S}` — a different cut from
model-displacement. Online learning that stops short of full
counterpart-policy fidelity should not be read as having “taken C’s
place” in the irreducible core.

## Limits

Boolean fidelity rungs ≠ SGD / online RL; n=4; no live training loop;
no organization measured.

## Best next

**#41** — MARL emergent structure vs learnability (static ABM nulls
#98/#107).

## Reproduce

```
python org_frontier/studies/ai_fidelity_displace/analyze_fidelity.py
```
(~6 s)
