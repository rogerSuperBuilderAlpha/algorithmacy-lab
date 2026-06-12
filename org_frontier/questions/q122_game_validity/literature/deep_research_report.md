# Q122 — Stage 2 literature: when is subsystem-Φ a valid cooperative game?

## The question in context

The critical review's T2/T3 charge that the value wave reads welfare off a malformed game. The cooperative
game theory is clear about what "well-formed" means, and the audit turns on those definitions.

## What the field establishes

- **The Shapley value exists for any set function with v(∅)=0.** So the numbers always compute. The welfare
  reading needs more: efficiency (Σ shares = v(N)) is automatic, but the surplus interpretation, that a
  share is what a party is worth in the coalition, leans on superadditivity (coalitions create value) and,
  for "no party subtracts," monotonicity (Shapley 1953; Shapley & Shubik 1969).
- **Monotone and superadditive are not generic for integrated information.** IIT's Φ is built on the
  least-reducible partition, so it is by construction non-additive across a partition; there is no theorem
  that adding an element raises Φ. Whether v is monotone and superadditive is therefore an empirical question
  about the specific forms, not a property to be assumed.
- **Negative Shapley values mean a non-monotone game.** A party gets a negative Shapley value only when its
  marginal contribution is negative for some coalition, i.e. adding it destroys value. So a negative share is
  not in itself an artifact; it is a faithful report that the underlying game is non-monotone there.
- **A subsystem's Φ depends on its background.** IIT conditions the complement on a state; the value of a
  subset is read against a background. Different backgrounds give different games, so any reported value is
  relative to the chosen background, and the integrating state is the natural choice when it is also where the
  verdict is read.

## The gap Q122 fills

The wave computed Shapley values but never audited the game: whether v is monotone and superadditive on the
forms used, whether the negatives survive without the clamp, and how far the values depend on the background.
Q122 runs that audit, so the welfare language can be kept where the game supports it and dropped where it does
not.
