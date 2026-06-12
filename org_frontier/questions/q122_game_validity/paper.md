# Q122 — Is the value function a valid cooperative game? A split verdict

## Question

The critical review charged that the value wave reads welfare off a malformed game: that subsystem-Φ is not
monotone or superadditive, that the negative Shapley values are clamp artifacts, and that the game is an
artifact of the frozen background (T2, T3, T5). This audits those charges on the forms the wave used.

## Method

The wave's own value function, v(S) = the subsystem-Φ of S with the complement frozen at a background state,
recomputed with the clamp on and off and at the all-ones and all-zeros backgrounds. Monotonicity (does v fall
when a party is added) and superadditivity (is v(S∪T) ≥ v(S)+v(T)) are checked over the full subset lattice of
each form: the productive forms (the triad, the bidirectional principal, the markets at N = 2 and N = 3) and
the degenerate monitor-only form.

## Results

The game is monotone and superadditive on every productive form, non-monotone on the degenerate one, and the
headline vectors are clamp-invariant but collapse to zero at the all-zeros background.

| form | class | monotonicity violations | superadditivity violations |
|---|---|---|---|
| read-recipient triad | productive | 0 | 0 |
| bidirectional principal | productive | 0 | 0 |
| market N=2 | productive | 0 | 0 |
| market N=3 | productive | 0 | 0 |
| monitor-only principal | degenerate | 3 | 5 |

| | result |
|---|---|
| H1 v monotone on every productive form | confirmed |
| H2 v superadditive on every productive form | confirmed |
| H3 v non-monotone on the degenerate form | confirmed |
| H4 vectors clamp-invariant but background-relative | confirmed |

## Interpretation

Where the wave reported a value distribution, the game is well-formed. The triad, the bidirectional principal,
and the all-required markets are monotone and superadditive across their full subset lattices, with no
violations. Adding a party never destroys value on these forms, and a coalition is worth at least its parts, so
the Shapley value's surplus-division reading is licensed. The critique's blanket charge against subsystem-Φ as a characteristic function fails for the forms the wave actually used; Q111, the bidirectional
half of Q114, and Q115 rest on valid games.

The critique is correct about the monitor-only case, and the audit concedes it. The monitor-only principal, a
read-only owner that factors the system, sits on a non-monotone game: adding the monitor destroys value on
three subset pairs and breaks superadditivity on five. Its −0.833 is the Shapley value of a value-destroying game, far from a fair share of surplus, and the Q114 contrast prose names value destruction in place of rent. Where the critique bites, it bites, and the honest reading drops the welfare vocabulary for this form.

The negative is genuine. Recomputing every vector with the clamp removed changes nothing, the −0.833 included:
the clamp floors values that were already non-negative at these states, so it never binds, and the negative
share is a faithful report of a negative marginal contribution. The specific charge that the negatives are
clamp artifacts is refuted.

The values are relative to the integrating background. At the all-zeros background every vector collapses to
zero; the forms carry value only at the all-ones state, which is their maximally integrated reachable state and
the state at which the verdict is read. The choice of background is principled, the value being read where the
coordination integrates, but the substance of the background-dependence point stands: the values are background-bound, and every figure fixes the integrating background. Reporting that scope condition is the
honest remedy, and a background-free value would require aggregating over states, which the wave did not do.

The split verdict answers T2 and T3 without either vindicating or sinking the wave wholesale. The game is
valid and the surplus reading licensed on the productive forms; the monitor-only −0.833 is value destruction
on a non-monotone game, which the prose should say plainly; the negatives are genuine, never clamp artifacts; and the
values are background-relative to the integrating state, a scope condition to state rather than a fatal flaw.

## Limitations

In-silico; exact subsystem Φ. The audit covers the forms the wave reported, short of every coordination form, so
monotonicity and superadditivity are established for these games, not proven in general. Background sensitivity
is checked at all-ones and all-zeros; a full treatment would aggregate over reachable states or marginalize the
complement, which the all-zeros collapse already motivates. The value function is the wave's own.
