# Davis — Stage 3 hypotheses (fixed before the Φ runs)

## The rendering that all five share

The Heider paper gave each person one bit — an attitude — and found the two unbalanced sign patterns (++−
and −−−) indistinguishable: both Φ = 6, all three in the core, no rest state. One bit is two camps, and two
camps is Cartwright–Harary's two-plus-set restriction built into the instrument. Davis's clustering needs
more. Here a **person** holds a **camp** from an alphabet of k ∈ {2, 3, 4}, encoded in two bits per person
(camp = x + 2y; codes ≥ k are invalid and a person in one leaves it). Each step a person moves to the camp
of least **strain** — a positive tie wants the same camp, a negative tie a different one — holding the
current camp when it is among the least-strained and otherwise taking the lowest-numbered least-strained
camp. k = 2 is the Heider paper's rule up to encoding. A **rest state** is a camp assignment satisfying
every tie. The **structure** is the major complex, reported in persons (a person is in the core when either
of its bits is).

Forms: the four signed triangles ppp, ppm, pmm, mmm at k = 2, 3, 4; the signed K4 (all 64 sign patterns) at
k = 4, dynamics only; the **path** p –– o –– q with no p–q line at k = 4.

Disclosure. Before these hypotheses were written, the dynamics (rest states, attractors) of the four
triangles at k = 2, 3, 4 and of the path were computed as an instrument check, and one Φ run (mmm at k = 4)
was made to time the six-unit computation. H1 and H5's dynamics clause are therefore not blind; H2–H3 and
the K4 census were not run before this file was fixed.

## H1 — Theorem 1 on triangles (C2)

- **H1 (Davis).** With k ≥ 3, ppp, pmm, and mmm have rest states and ppm has none; with k = 2, mmm has none.
- **H0.** A rest state for ppm at any k, or none for mmm at k ≥ 3.
- **Lab prior.** With Davis (combinatorial; seen in the pre-check).

## H2 — The structural classes follow clusterability, not balance (C1, C2)

- **H2 (Davis).** At k = 4 the forbidden pattern ppm has all three persons in its core, and each of the
  three clusterable patterns (ppp, pmm, mmm) has fewer than three.
- **H0.** A clusterable pattern with all three in the core, or ppm with fewer.
- **Lab prior.** Open. The Heider paper found the satisfiable patterns dissolve (Φ 0) and the unsatisfiable
  bind; whether a two-bit encoding keeps that is not known. mmm at k = 4 was seen at core {p, q}.

## H3 — The all-negative verdict depends on the alphabet (C2 against Heider H3)

- **H3 (Davis).** mmm has all three persons in its core at k = 2 and fewer than three at k = 3 and k = 4;
  ppm has all three at every k.
- **H0.** mmm's core size does not change with k, or ppm's does.
- **Lab prior.** With Davis: the Heider result was the two-camp case.

## H4 — Theorem 1 on complete four-person graphs, and uniqueness (C2, C3)

- **H4 (Davis).** Over the 64 sign patterns of K4 at k = 4: rest states exist iff the pattern is
  clusterable (no cycle with exactly one negative line), the triangle test agrees with the cycle test on
  every pattern, and every clusterable pattern has exactly one partition at rest.
- **H0.** Any pattern where rest and clusterability disagree, or a clusterable complete pattern with two
  partitions.
- **Lab prior.** With Davis.

## H5 — The incomplete graph (C3)

- **H5 (Davis).** The path p –– o –– q (no p–q line) at k = 4 is clusterable with more than one partition
  at rest, and its core has fewer than three persons (it dissolves like the clusterable class).
- **H0.** One partition, or all three persons in the core.
- **Lab prior.** With on partitions (seen: 2). Open on Φ — the path is the lab's mediated-triad shape, and
  that shape binds under a conjunctive rule.

## Not tested here

Directed ties and semicycles; ranked clusters; Φ on K4 (eight units is beyond the exact budget here).
