# Backlog: majority_factor_split

1. Why (1,1,1,3) quota 3 follows the factor exactly, even though the weight-3 party can win alone,
   while (1,1,1,2) quota 2, which also has a singleton-winning party, missed the factor in
   `party_noise_factor`. Write a new distinguishing property and test it.
2. At ε = 0.4, 2-of-4 and 3-of-4 have measured / Φ(η, 0) = 0.648 at both η. That ratio was noticed
   after the run.
3. Still open from `party_noise_factor`: the rise in 2-of-5 and 4-of-5 at ε = 0.4; a formula for
   the extreme (one-of-n and all-of-n) rules; a derivation of the original factor, now known not to
   be general, and not to split on singleton-winning parties or unique odd-weight majorities.

Status: items 1–3 open as of 2026-11-23. This study tests and refutes item 1 of
`party_noise_factor/BACKLOG.md`.
