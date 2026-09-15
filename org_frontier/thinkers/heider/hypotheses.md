# Heider — Stage 3 hypotheses (fixed before computing)

## The rendering that all five share

Three persons p, o, q, each with a binary attitude toward a common object x (1 = likes x, 0 = does not).
Each pair has a fixed sign σ ∈ {+, −}: the L relation, taken as symmetric (Heider: "psychologically it tends
to become symmetrical"). A signed input from j to i is s_j when σ_ij = + and ¬s_j when σ_ij = −: a friend's
attitude pulls toward itself, an enemy's away. The attitude rule is **signed majority with hold**:

    s_i' = maj(σ_ij·s_j, σ_ik·s_k, s_i)

— adopt what the two signed inputs agree on; when they disagree, hold. The rule is self-dual (complementing
every attitude complements every output), so flipping one person's encoding flips the signs of that
person's two relations without changing the dynamics. Balanced patterns are exactly those that can be
flipped to +++ (Cartwright–Harary's structure theorem in this language); unbalanced ones flip to ++−.

A relation σ_ij is **satisfied** at a state when σ_ij = + and s_i = s_j, or σ_ij = − and s_i ≠ s_j. A state
that satisfies every relation is a **rest state**.

Forms: the four sign patterns up to relabeling on three persons (`ppp`, `ppm`, `pmm`, `mmm`), all eight
patterns for the class check, a six-element **coevolving** form in which the three signs are elements too
(σ_ij' = [s_i = s_j]: like those who agree with you), and the switching classes of the signed complete graph
on four persons for the degree-of-balance test.

## H1 — Balance is a property of the sign product (C1)

- **H1 (Heider / Cartwright–Harary).** The eight sign patterns fall into exactly two structural classes —
  identical Φ, identical core size, identical attractor structure within each — and the classes are the
  balanced patterns (product +) and the unbalanced (product −). Heider's addition: the balanced class is the
  "unit," so Φ(balanced) > Φ(unbalanced).
- **H0.** Some balanced pattern differs structurally from another balanced pattern, or Φ(balanced) ≤
  Φ(unbalanced).
- **Lab prior.** Two classes: by the self-duality of the rule, patterns in the same switching class have
  identical dynamics up to relabeling, and Φ is relabeling-invariant. On which class has the higher Φ, no
  prior. The majority triad (Simmel H3, probe #371) had Φ = 0; +++ under signed majority with hold is that
  triad, so Φ(balanced) = 0 is expected and the direction of the inequality is open.

## H2 — Forces toward balance; imbalance is tension (C2)

- **H2 (Heider).** Every balanced pattern has rest states and every attractor of its dynamics is a rest state.
  No unbalanced pattern has a rest state, and its attractors are cycles or states that leave a relation
  unsatisfied.
- **H0.** An unbalanced pattern has a rest state, or a balanced pattern has an attractor that is not one.
- **Lab prior.** Agrees on the rest states (frustration). Whether the unbalanced attractors are cycles
  ("forces ... will arise") or frozen unsatisfied states ("if a change is not possible ... tension") is open.

## H3 — The all-negative triad is a third kind (C4)

- **H3 (Heider).** The −−− triad differs structurally from the ++− triad: in Φ, in core, or in the number
  of attractors ("too indetermined").
- **H0.** −−− and ++− are structurally identical.
- **Lab prior.** Against Heider and with Cartwright–Harary: −−− flips to ++− by complementing one person.
  Two kinds, not three.

## H4 — Attitudes and relations influence each other (C3)

- **H4 (Heider).** In the coevolving form (three attitudes and three signs, σ_ij' = [s_i = s_j], attitudes
  by signed majority with hold), the major complex contains attitudes and signs together: the two processes
  make one whole.
- **H0.** The core is attitudes only, signs only, or empty.
- **Lab prior.** No prior. The signs read pairs of attitudes and the attitudes read signs, so nothing is
  read-only; whether the whole is irreducible or splits is what the computation decides.

## H5 — Degree of balance (C5, Cartwright–Harary)

- **H5 (Cartwright–Harary, reading Heider).** Over the switching classes of the signed complete graph on four
  persons under signed majority with hold, Φ is monotone non-decreasing in the degree of balance b(G) =
  positive cycles / all cycles, with the balanced class (b = 1) at the maximum.
- **H0.** Φ is not monotone in b(G), or the balanced class is not at the maximum.
- **Lab prior.** Against: if Φ(balanced) = 0 at three persons, the balanced class at four is expected at
  zero too, and any Φ > 0 in a frustrated class inverts the ordering.

## Not tested here

L versus U; envy, jealousy, competition; self-regard; means-end reasoning (`exegesis.md`).
