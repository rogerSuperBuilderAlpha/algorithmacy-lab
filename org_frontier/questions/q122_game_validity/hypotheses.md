# Q122 — Stage 3 hypotheses (fixed before computation)

Four hypotheses auditing whether the value wave's cooperative game is well-formed, answering the critical
review's T2/T3/T5. The review charged that subsystem-Φ is not monotone or superadditive, so the "value
distribution" reading is unlicensed; that the negative Shapley values are clamp artifacts; and that the game
is an artifact of the frozen background. This study tests those three charges directly on the forms the wave
used. Written and committed before the run; the instrument is the wave's own value function, recomputed with
the clamp and background as parameters.

The audit is two-sided by design: it can vindicate the machinery on the forms where it was used productively
and concede it on the forms where the critique bites. The hypotheses are written to let it do both.

## H1 — The value function is monotone on every productive form

- **Claim:** On the read-recipient triad, the bidirectional principal, and the all-required markets at N = 2
  and N = 3, the value function never falls when a party is added: zero monotonicity violations over the full
  subset lattice.
- **H0:** Some productive form has a monotonicity violation.
- **Predicted outcome:** zero violations. H0 refuted. Where the wave reported a value distribution, the game
  is monotone, so adding a party never destroys value.

## H2 — The value function is superadditive on every productive form

- **Claim:** On the same four forms, v(S ∪ T) ≥ v(S) + v(T) for all disjoint S, T: zero superadditivity
  violations.
- **H0:** Some productive form has a superadditivity violation.
- **Predicted outcome:** zero violations. H0 refuted. The game is superadditive where used, so the
  surplus-division reading of the Shapley value is licensed there.

## H3 — The value function is non-monotone on the degenerate monitor-only form

- **Claim:** The monitor-only principal, a read-only owner that factors the system, has a non-monotone value
  function: at least one monotonicity violation.
- **H0:** It is monotone too.
- **Predicted outcome:** violations exist. H0 refuted. The −0.833 of Q114 is the Shapley value of a
  value-destroying game, not a fair share of surplus. This is the study's genuinely uncertain claim, and the
  honest concession: the critique is correct for this case, and the monitor-only finding must be read as
  value destruction, not distribution.

## H4 — The vectors are clamp-invariant but background-relative

- **Claim:** Removing the max(0, ·) clamp leaves every published Shapley vector unchanged (so the negative
  values are not clamp artifacts), while moving the background from all-ones to all-zeros collapses every
  vector to zero (so the values are relative to the integrating background).
- **H0:** The clamp changes the vectors, or the all-zeros background leaves them unchanged.
- **Predicted outcome:** clamp-invariant and zero at all-zeros. H0 refuted. The negative value is genuine,
  not a clamp artifact, and the whole value structure is a property of the integrating state, which the
  reported numbers should be understood to fix.
