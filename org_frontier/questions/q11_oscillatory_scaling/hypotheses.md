# Q11 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether a coordination form that settles onto a limit cycle carries a Φ(n)
scaling law distinct from the fixed-point families in the zoo (Probe 132): the conjunctive hub Φ=n−1
(#116), the pool Φ=n(n−1), the parity hub Φ=2^(2−n) (#115/#120), and the AND-neighbor ring capped at
Φ=4 for n≥4. The construction builds genuine cyclers — a ring with a rotating update (a traveling wave
of period p tied to ring size by the winding constraint T₂·N=nP, Kashchenko 2023; Rohlfshagen 2004) and
a mediated form with a periodic commit — at n=3,4,5,6, discretized to a TPM at grain 1, and reads
Φ_MIP, the dyadic/triadic verdict, the MIP location, the major complex via
`pyphi.compute.major_complex()`, and the attractor period p at each n. The review's prior probes
(#132, #116, #115/#120, #133, #57, #32, #60, #81, #125, #127, #130) and the report's mechanisms
(Esteban 2018 / Kalita 2019 periodic orbits as Φ-carriers; Mediano 2021 metastable-Φ peak and τ
dependence; Aguilera 2019a ϕ(τ) over update count; Balduzzi 2008 low Φ on fixed-point attractor states;
Kashchenko 2023 integer winding) supply the structural priors each null rests on. Written and committed
before any test runs.

## H1 — The rotating ring is a fifth law, distinct from the capped Φ=4
- **Claim:** The rotating-update ring carries a Φ(n) law that is not the AND-neighbor ring's cap. Its
  Φ_MIP either grows with n (linear or logarithmic) or caps at a value other than 4, so over n=3,4,5,6
  the rotating ring and the #132 capped ring are separable at matched n. A traveling wave keeps every
  node informative about the global phase at all times, unlike the AND-collapse that holds one fixed
  state and suppresses Φ (Balduzzi 2008), so the closure-plus-rotation builds a different irreducibility
  than the static ring.
- **H0:** The rotating ring reproduces the capped ring. Closing a chain into a loop and adding rotation
  changes the attractor type but not the integration the loop can carry, so Φ_MIP settles to the same
  constant the AND-neighbor ring did (Φ=4 for n≥4, Φ=2 at n=3) — the topology, not the update rule, sets
  the law, and the zoo's four laws are complete.
- **Predicted outcome:** Φ_MIP(n) for the rotating ring differs from 4 at some n≥4 (and from the capped
  ring at matched n=4,5,6), tracing a curve that is monotone in n or caps at a new value, giving a fifth
  distinct shape. H0 is refuted: an oscillatory attractor adds a law the fixed-point zoo does not
  contain.

## H2 — The cycle period enters the law as a term
- **Claim:** Φ_MIP for the limit-cycle family depends on the attractor period p, not on n alone. Across
  the rotating ring (where the winding constraint ties p to ring size) and the periodic-commit mediated
  form (where p is set independently of member count by the commit cadence), Φ_MIP is a function of p —
  forms with equal n but different p take different Φ, and forms with different n but equal p line up.
  This is the τ/update-count dependence (Aguilera 2019a; Mediano 2021) realized as an actual cycle
  period in a Φ_MIP law, a term no static fixed-point family carries.
- **H0:** The period does not enter the law. Φ_MIP at grain 1 reads one transition and is blind to how
  many steps the global state takes to return, so the period is a sampling caveat (#32, #60) and never a
  variable in Φ(n); the law is a function of n (and topology) alone, and two forms with the same n but
  different p take the same Φ.
- **Predicted outcome:** Holding n fixed and varying p in the periodic-commit mediated form moves
  Φ_MIP, and the rotating ring's Φ collapses onto a single curve when plotted against p rather than n.
  H0 is refuted: p is a term in the law. (If H2 holds and H1's null also held, Φ depending on p while
  topology fixes the cap would itself be a contradiction the sweep resolves.)

## H3 — Distributing the parity flip around a ring breaks the decaying law
- **Claim:** A rotating ring built from per-node flips (the spatial chain of XOR-like updates the review
  names) does not inherit the parity hub's decaying law Φ=2^(2−n) (#115/#120). Distributing the flip
  around a loop, where each node reads only its neighbor rather than a shared global commit, keeps Φ from
  halving each step; the rotating ring's Φ stays bounded away from the parity-hub floor at every n where
  the hub has already fallen below it. The hub's decay is a property of the single shared XOR commit, not
  of the flip rule, and removing the hub removes the decay.
- **H0:** The flip rule sets the law wherever it sits. A ring of flips is a parity construction, so it
  decays the same way the XOR hub does (Φ→2^(2−n)), the rotating ring's Φ falls toward the same floor as
  n grows, and the parity hub and the rotating ring are law-equivalent.
- **Predicted outcome:** At n=5,6 the rotating-flip ring's Φ_MIP sits above 2^(2−n) and does not track
  the hub's halving, so the two diverge as n grows. H3 is distinct from H1: H1 separates the rotating
  ring from the *capped AND-neighbor* ring, H3 separates it from the *decaying parity hub*, the closest
  cycling-rule cousin in the zoo. H0 is refuted: topology, not the flip, governs whether parity decays.

## H4 — The limit-cycle family stays triadic across n
- **Claim:** Both cyclers — the rotating ring and the periodic-commit mediated form — return a triadic
  verdict at every n=3,4,5,6, with the full node set in the major complex. A sustained cycle holds no
  single state and keeps the joint determination irreducible, so the limit-cycle family lands on the
  triadic side at each size even though #130 showed a cycle is neither necessary nor sufficient for
  triadicity in general wirings; *these constructed* cyclers are built to integrate, so the general
  non-implication does not block a triadic verdict here.
- **H0:** Cycling does not secure triadicity. Per #130 no attractor predicate separates the verdict, so
  the constructed cyclers behave like the general population — at least one of them reads dyadic at some
  n, or its major complex sheds nodes (a center-periphery drop like #128), and the limit cycle buys no
  verdict guarantee.
- **Predicted outcome:** `major_complex()` returns the full n-node set with a triadic verdict at every
  n=3..6 for both forms, and the MIP is balanced rather than shearing off a periphery. H0 is refuted for
  these constructions: a built-to-integrate limit cycle is reliably triadic across the swept sizes, even
  though cycling is not a general predicate for it (#130).

## H5 — The detectable band widens with period: grain flips the verdict only at grain ≳ p
- **Claim:** Reading the rotating ring at a coarser temporal grain flips its verdict to dyadic only once
  the grain reaches the order of the attractor period p, and because the rotating ring of size n has
  period p≈n (longer than the corpus forms' periods of 1–2 in #60), its detectable band is wider — the
  triadic verdict survives to a larger grain than the short-period corpus forms did. The grain-flip
  threshold tracks p (#60), so a deliberately long-period form pushes the flip point out.
- **H0:** The grain-flip threshold is fixed near grain 2 regardless of period. The corpus forms flipped
  at grain k=2 (#32, #60) and the slowed-clock/grain collapses landed at 2, so the rotating ring also
  flips at grain 2 independent of its longer period, and building a longer cycle does not widen the
  detectable band.
- **Predicted outcome:** Sweeping the observation grain on the rotating ring, the triadic verdict holds
  past grain 2 and flips to dyadic only near grain ≈ p (which grows with n), so the n=6 ring tolerates a
  coarser grain than the n=3 ring before collapsing. This ties the grain band to the constructed period
  rather than a fixed k=2. H0 is refuted: the detectable band scales with the cycle period, and a
  long-period oscillator is verdict-robust across a wider grain range than the short-period corpus.
