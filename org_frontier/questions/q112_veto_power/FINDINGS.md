# Q112 findings — destruction is democratic, value is concentrated

All four hypotheses confirmed. Every core party can collapse the coordination by withdrawing, so the veto is
held equally. Yet the value concentrates at the mediator (Q111). The two come apart because the coordination
is not a unanimity game: the two outer parties produce nothing together, so the mediator's productivity in
partial coalitions concentrates the value while the power to destroy stays universal.

| party | holds a veto | Shapley value |
|---|---|---|
| worker (E) | yes | 0.333 |
| mediator (M) | yes | 1.333 |
| recipient (R) | yes | 0.333 |
| spectator (X) | no | — |

Sub-coalition values: {E, R} = 0, {M, R} = 2, {E, M} = 2.

| H | Result | Verdict |
|---|--------|---------|
| H1 | every core party holds a veto | confirmed |
| H2 | a non-core spectator holds no veto | confirmed |
| H3 | veto is universal but value is unequal | confirmed |
| H4 | the coordination is not a unanimity game | confirmed |

From `probe_veto_power.py`.

## What it says

Every bound party can break the coordination. Withdrawing the worker, the mediator, or the recipient — by
going constant — collapses the triad to dyadic (H1). Each core party is a veto player: the coordination
exists only with all of them, so any one can hold it hostage. A read-only spectator cannot: its withdrawal
leaves the major complex {E, M, R} intact (H2). The veto is the law read as a game — every party bound into
the one irreducible joint determination is a party whose loss ends it.

Veto power and value capture are different. All three core parties hold a veto, yet their Shapley values are
unequal — the mediator's 1.333 against 0.333 each (H3). The power to destroy is held equally; the value is
held unequally. A worker or a recipient can break the coordination as surely as the mediator can, but
captures a sixth of its value to the mediator's two-thirds. Destruction is democratic; rent is not.

The reason is that the coordination is not a unanimity game. In a pure unanimity game every player is a veto
player and the value splits equally, but here the sub-coalition values are asymmetric: the two outer parties
together are worth nothing, while either with the mediator is worth the full two (H4). The mediator is more
than a veto player — it is productive in partial coalitions, pairing with either party to produce value,
while the outer parties produce value only through it. That productivity, not the veto, is what concentrates
the value. Every party can stop the coordination; only the mediator makes it.

The political-economy reading is sharp. In a mediated coordination, the parties hold equal power to refuse —
each can walk away and end it — but the mediator captures the rent, because the value flows through the
party the others cannot coordinate without. The workers' and the counterpart's power is the threat of
collapse; the platform's power is the capture of value. The two are not the same, and the structure assigns
them to different parties.

## Caveats

- **Confirmatory.** All four predictions held.
- **Defection as going constant.** A party defects by becoming constant; other defections (a different read)
  also break the triad, as Q108's knife-edge showed, so the veto is robust to the choice of defection.
- **One triad.** The veto-value split is read on the read-recipient triad; the all-required market of Q113
  is a different case, where the value distributes equally. In-silico, exact verdict and Φ.
