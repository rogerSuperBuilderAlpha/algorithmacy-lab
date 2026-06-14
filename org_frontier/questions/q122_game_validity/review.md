# Q122 — Stage 1 review: cooperative-game validity of the value function

## The question

The critical review (CRITICAL_REVIEW_Q111_Q117.md, T2/T3/T5) charged that the value wave reads welfare off a
malformed game: that subsystem-Φ is not monotone or superadditive, so the surplus reading is unlicensed; that
the negative Shapley values are clamp artifacts; and that the game depends on the frozen background. This
study audits those charges on the forms the wave used.

## What the lab already knows that bears on this

- **The wave reported Shapley values of subsystem-Φ (Q111-Q116) without auditing the game.** Whether v is
  monotone and superadditive on the forms used, and whether the negatives survive the clamp, was never checked.
- **A read-only element factors the whole system (Q74); the monitor-only principal captures -0.833 (Q114).**
  This is the prime suspect for a non-monotone game and a value-destruction reading.
- **The verdict is read at the maximally integrated reachable state, all-ones for these forms (classifier).**
  The value function uses the same state, so the background is principled, but its sensitivity is untested.

## The gap

The cooperative-game machinery was used across six studies but never validated as a game. Whether the welfare
language is licensed on the forms where it was used, and where exactly the critique bites, is untested.
