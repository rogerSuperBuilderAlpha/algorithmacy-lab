# Q122 findings — the game is valid where the wave used it, and the critique holds where it bites

All four hypotheses confirmed, and the audit is two-sided. On every form whose value the wave reported as
surplus, the game is monotone and superadditive, so the cooperative-game reading is licensed there. On the
degenerate monitor-only form, the game is non-monotone, so its −0.833 is the Shapley value of a
value-destroying game, exactly as the critique charged. The negative survives unclamping, no mere artifact of the floor. The whole value structure is relative to the integrating background; it vanishes at the all-zeros
state.

| form | class | monotonicity violations | superadditivity violations |
|---|---|---|---|
| read-recipient triad | productive | 0 | 0 |
| bidirectional principal | productive | 0 | 0 |
| market N=2 | productive | 0 | 0 |
| market N=3 | productive | 0 | 0 |
| monitor-only principal | degenerate | 3 | 5 |

| vector | clamp+bg1 (published) | raw+bg1 (no clamp) | clamp+bg0 (all-zeros) |
|---|---|---|---|
| read-recipient | E,R 0.333; M 1.333 | identical | all 0 |
| bidirectional principal | E,R,P 0.417; M 1.750 | identical | all 0 |
| monitor-only principal | E,R 0.167; M 0.5; P −0.833 | identical | all 0 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | v is monotone on every productive form | confirmed (0 violations) |
| H2 | v is superadditive on every productive form | confirmed (0 violations) |
| H3 | v is non-monotone on the degenerate monitor-only form | confirmed (3 violations) |
| H4 | the vectors are clamp-invariant but background-relative | confirmed |

From `probe_game_validity.py`.

## What it says

Where the wave reported a value distribution, the game is well-formed. The read-recipient triad, the
bidirectional principal, and the all-required markets at N = 2 and N = 3 are all monotone and superadditive
over the full subset lattice, with zero violations (H1, H2). On these forms adding a party never destroys
value, and a coalition is worth at least the sum of its parts, so the surplus-division reading of the Shapley
value holds. The cooperative-game claims of Q111, the bidirectional half of Q114, and Q115 stand on a valid
game, and the critique's blanket charge that subsystem-Φ is "not a valid characteristic function" does not
apply to the forms where the wave actually used it.

The critique is right about the monitor-only case. The monitor-only principal, a read-only owner that factors
the whole system, sits on a non-monotone game: three subset pairs lose value when the monitor is added, and
five coalition pairs break superadditivity (H3). Its −0.833 is the Shapley value of a game in which adding the
party destroys value, far from a fair share of a surplus. The Q114 contrast case must be read that way, as value
destruction in place of rent, and the welfare vocabulary should be dropped for it. The audit concedes this
cleanly: where the critique bites, it bites.

The negative is genuine, no clamp artifact. Recomputing every headline vector with the max(0, ·) clamp
removed leaves all of them unchanged, including the −0.833 (H4). The clamp floors coalition values that were
already non-negative at these states, so it never binds, and the negative Shapley value comes from a genuine
negative marginal contribution, never from the flooring convention. The critique's specific claim that the
negatives are clamp artifacts is refuted; the negative is a faithful report of a non-monotone game.

The value structure is relative to the integrating background. At the all-zeros background every vector
collapses to zero: the forms carry no value there at all (H4). The reported numbers are properties of the
all-ones state, which for these forms is the maximally integrated reachable state, the same state at which the
verdict is read. So the choice is principled, the value being read where the coordination integrates, but the
critique's background-dependence point is correct in substance: the values are not background-free, and every
reported figure should be understood to fix the integrating background. A study that wanted background-free
values would have to aggregate over states, which the wave did not do.

The net for the defense agenda: T2 and T3 are answered with a split verdict. The game is valid, and the
surplus reading licensed, on the productive forms; the monitor-only −0.833 is value destruction on a
non-monotone game, which the prose should say plainly; the negatives are not clamp artifacts; and the values
are background-relative to the integrating state, a scope condition the wave should state in place of a fatal
flaw.

## Caveats

- **Two-sided, and the risky claim was real.** H3 could have come back monotone, vindicating the monitor-only
  prose; it did not. H1 and H2 could have shown violations on a productive form; they did not. The audit was
  free to concede or vindicate on each, and did both.
- **The forms, not the whole family.** The audit covers the forms the wave reported (the triad, the two
  principal couplings, the markets at N = 2 and N = 3), short of every coordination form. Monotonicity and
  superadditivity are properties of these games, unproven for all.
- **Two backgrounds.** The background sensitivity is checked at all-ones and all-zeros. A full treatment would
  aggregate over reachable states or marginalize the complement; the all-zeros collapse already shows the
  values are background-relative.
- **Exact Φ throughout.** The value function is the wave's own, with exact subsystem Φ. In-silico.
