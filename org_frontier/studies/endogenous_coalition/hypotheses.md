# Endogenous coalition — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #30).** If parties choose whether to
join a coalition, do they endogenously form the coalition that
maximizes their own core membership (#66 imposed it)?

**Already known (cited, not reopened).**
- Probe #1 / #66: imposed counterpart coalition relocates the core to
  the coalition and can eject worker/principal.
- Probe #37: coalition beats principal when both imposed.
- #29 CONFLICT_ENCODING — pointer only.
- Other lanes closed.

**Universe.** Exact binary IIT-4.0 Φ. Counterpart agents each choose
join∈{0,1} (peer channel on/off). Payoff = 1 iff in the major complex
(maximize own core membership). **Solution concept:** pure-strategy
Nash by full enumeration of join profiles (candid; not mixed/correlated
eq, not evolutionary dynamics).

**Definitions (fixed).**
- **Max-own-core set** for player i: join profiles maximizing i’s
  membership bit.
- **Recovers:** every pure Nash profile gives every player their
  maximum membership pay (Nash ⊆ ∩_i max-own-core sets’ pay level).
- **Mismatch:** some max-own-core profile for a player is not Nash.
- **Multiple stable:** ≥2 distinct pure Nash profiles.

## Games (designed)

| id | sketch |
|---|---|
| weak_k2 | C_i'=S∨C_j if join else S; S'=W∧C1∧C2 |
| weak_k2_P | same + active gating/monitoring P (#66 setting) |
| strong_k2 | C_i'=C_j if join else S (sync) |
| weak_k3 | three counterparts, weak peer OR |

## H1 — endogenous recovers max-own-core

Every pure Nash profile yields max membership pay for all counterpart
players. Null: some Nash leaves a player below their max-own-core pay.

## H2 — mismatch / coordination failure

At least one profile that maximizes some player’s membership is **not**
a pure Nash (individual max-own-core ≠ equilibrium). Null: every
max-own-core profile is Nash.

## H3 — multiple stable coalitions

At least one designed game has ≥2 pure Nash profiles. Null: unique
Nash in every game.
