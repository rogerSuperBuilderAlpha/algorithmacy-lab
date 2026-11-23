# Backlog: party_noise_factor

1. Why the factor holds exactly for some interior rules ((1,1,1,2) quota 3, 3-of-5; and several
   others at ε = 0.3 only) and fails for others, especially at ε = 0.4.
2. At η = 0.2, ε = 0.4, 2-of-5 and 4-of-5 whole Φ rises from 0.032322 to 0.075400. Which reachable
   states or cuts drive that increase?
3. The missed cases had a measured / Φ(η, 0) ratio that did not depend on η: 0.9604 and 0.5184 for
   (1,1,1,2) quotas 2 and 4 at ε = 0.3 and 0.4; 0.7776 for (1,1,2,2) quota 3 at ε = 0.4; 2.3328
   for 2-of-5 and 4-of-5 at ε = 0.4. These were noticed after the run.
4. Still open from `weighted_swap_symmetry`: a formula for the extreme (one-of-n and all-of-n)
   rules, and a derivation of the original factor from the party-side noise model, now known not
   to be general.

Status: items 1–4 open as of 2026-11-23 (PR #960). This study tests and refutes item 1 of
`weighted_swap_symmetry/BACKLOG.md`.
