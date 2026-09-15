# A third camp: Davis's clustering against the lab's Heider result

<code + data: org_frontier/thinkers/davis/ ; probes #424–#428 in probes/PROBES.md ; standard in
org_frontier/thinkers/PAPER_STANDARD.md>

## Abstract

Davis (1967) replaced one word in Cartwright and Harary's balance condition — a signed graph is *clusterable*
iff no cycle has *exactly one* negative line, where balance had said *an odd number* — and thereby admitted
the all-negative triangle, which balance forbids, as the paradigm of a group with three camps. The lab's
Heider paper had found ++− and −−− identical under exact Φ: 6.000, all three persons in the core, no rest
state. That paper gave each person one bit, and one bit is two camps — Cartwright–Harary's two-plus-set
restriction built into the instrument. This paper gives each person a camp from an alphabet of k ∈ {2, 3, 4},
encoded in two bits, with a least-strain update, and re-asks. Davis's theorem holds on all four triangles
and all 64 signed K4 patterns (H1, H4 confirmed): rest states exist iff clusterable, the triangle test
suffices, the clustering is unique. At k = 4 the four triangles sort as Davis says — the forbidden ++− alone
has all three persons in its core, at Φ = 6.000, the Heider number; the three clusterable patterns do not
(H2 confirmed). The all-negative triangle's verdict changes with the alphabet: all three in the core at
k = 2, two at k = 3 and 4 (H3's central clause confirmed; the ++− clause fell at k = 3, an encoding with a
dead code — partial). The negative path with no closing line clusters two ways and its core is one pair (H5
confirmed). The Heider paper's refutation of the all-negative triad as a third kind is withdrawn: it was the
two-camp verdict. Results are about Boolean models.

## Introduction

The lab's Heider paper ended on a refutation. Heider (1958) had thought the all-negative triad — three
persons who each dislike the other two — "too indetermined" to be balanced or unbalanced, a third kind;
Cartwright and Harary (1956) made it simply unbalanced, its sign product negative; the lab's instrument
agreed with Cartwright and Harary and went further, finding −−− and ++− the same structure: Φ = 6.000,
all three persons in the core, no rest state, the same seven attractors. Davis (1967) says otherwise. In a
seven-page paper whose theorem was, he notes, supplied by Cartwright and Harary themselves, he defines a
graph as *clusterable* when its points partition into any number of plus-sets — friends within, enemies
between — and proves that a signed graph is clusterable iff it contains no cycle with exactly one negative
line. Balance, with its two plus-sets, is the special case. The all-negative triangle is clusterable with
three.

The contest is direct and it turns on the instrument. The Heider paper gave each person one bit, an
attitude, and one bit is two values: two camps. Under two camps the all-negative triangle cannot rest for the
same reason it is unbalanced — three mutually different persons need three values — and the instrument's
verdict that −−− is a whole under tension is, on Davis's reading, a verdict on a group that was forbidden a
third camp. Whether Φ agrees with Davis when the third camp is allowed is a question the lab can compute,
and the answer bears on a result the lab has already published.

Five hypotheses were fixed before the Φ runs. Davis's theorem on the four triangles (H1); whether the
structural classes under Φ follow clusterability at k = 4 (H2); whether the all-negative verdict changes
with the alphabet while the forbidden triangle's does not (H3); the theorem on all 64 sign patterns of K4,
with the triangle test and uniqueness (H4); and the incomplete graph (H5). Four confirmed, one partial, and
the partial's central clause is the one that bears on the Heider result.

## Davis's account

Cartwright and Harary (1956) had generalized Heider to signed graphs: a graph is balanced iff every cycle has
an even number of negative lines, and — the structure theorem — a balanced graph's points partition into at
most two plus-sets, all positive lines within a set and all negative lines between the two. Davis begins
from the observation that groups do not stop at two cliques. He defines a signed graph as clusterable when
its points can be partitioned into subsets, of any number, such that every positive line joins two points
of the same subset and every negative line joins two points of different subsets (1967, p. 181). Then the
theorem: "a signed graph is clusterable if and only if it contains no cycle with exactly one negative line"
(p. 181; Doreian and Mrvar 1996, p. 156, quote it as "no semicycles with exactly one negative arc").

The change from *odd* to *exactly one* has one consequence for the triangle. Balance forbids ++− (one
negative) and −−− (three). Clustering forbids only ++−. The friend of two enemies is the one position no
partition can place — Davis's "crosspressure hypothesis" (p. 184, n. 3; Davis 1963). Three mutual enemies
are three plus-sets. For complete graphs the cycle condition reduces to the triangles (p. 183), and a
complete clusterable graph has a unique clustering: the plus-sets are the components of the positive
subgraph. Incomplete graphs can cluster in more than one way.

Doreian and Mrvar (1996) build the partitioning approach on Davis; Davis and Leinhardt (1972) carry
clustering into the ranked-clusters model and the triad census. Neither asks what the instrument here asks:
whether a group with three camps is, as a causal structure, a whole or a set of pairs.

## From claims to forms

A **person** holds a **camp** from an alphabet of k ∈ {2, 3, 4}, encoded in two bits (camp = x + 2y). Codes
at or above k are invalid, and a person in one leaves it. Each step a person moves to the camp of least
**strain** — a positive tie wants the same camp as the other, a negative tie a different one — holding the
current camp when it is among the least-strained and otherwise taking the lowest-numbered least-strained
camp. At k = 2 this is the Heider paper's signed-majority-with-hold up to encoding. A **rest state** is a
camp assignment satisfying every tie. **Clusterable** and **balanced** are computed from the cycles. The
**structure** is the major complex, reported in persons: a person is in the core when either of its bits
is.

Forms. The four signed triangles ppp, ppm, pmm, mmm — edges po, pq, oq — at k = 2, 3, 4. All 64 sign
patterns of K4 at k = 4, dynamics only (eight units is beyond the exact budget). The **path** p –– o –– q,
both lines negative and no p–q line, at k = 4.

The rendering's risks are the encoding and the tie-break. Two bits carry four codes; at k = 2 and k = 3 some
codes are dead, and a dead code is a place a person can be knocked into and must climb out of. The clean
comparison is therefore the Heider paper's one bit (two camps, bits full) against k = 4 here (four camps,
bits full). The lowest-camp tie-break is a bias toward camp 0; it moves which bits carry the core, not, in
any predictable way, how many persons.

## Hypotheses

Fixed in `hypotheses.md` before the Φ runs, with a disclosure: the triangle and path dynamics and one Φ run
(mmm at k = 4, for timing) were seen first.

- **H1 (Davis) — Theorem 1 on triangles.** At k ≥ 3, ppp, pmm, mmm have rest states and ppm none; at
  k = 2, mmm has none. *Prior:* with.
- **H2 (Davis) — the classes follow clusterability.** At k = 4, ppm has all three persons in its core; ppp,
  pmm, mmm each fewer. *Prior:* open.
- **H3 (Davis) — the all-negative verdict is the two-camp verdict.** mmm has three persons in its core at
  k = 2 and fewer at k = 3, 4; ppm has three at every k. *Prior:* with.
- **H4 (Davis) — Theorem 1 on K4.** Over 64 patterns: rest ⇔ clusterable; triangle test = cycle test; one
  partition per clusterable pattern. *Prior:* with.
- **H5 (Davis) — the incomplete graph.** The negative path has ≥ 2 partitions at rest and fewer than three
  persons in its core. *Prior:* with on partitions; open on Φ.

## Methods

**Instrument.** Exact IIT-4.0 Φ (Albantakis et al., 2023) via PyPhi (Mayner et al., 2018), which is binary;
the two-bit encoding is how a k-valued unit is presented to it. Six-unit runs take 30 s to 8 min each.
Dynamics from the deterministic synchronous TPM; rest states by enumeration; cycles by search.

**Control.** Every probe first runs the conjunctive triad (Φ = 2.000000, core {A, M, B}). All passed.

**Procedure.** Five probes, one per hypothesis. Results in `results/`, registered in `ci/reproduce.json`
(#424–#428; the two long Φ probes marked slow).

**Scope.** Results are about Boolean models. No group is measured.

## Results

| pattern | k | clusterable | balanced | rest states | partitions | Φ_MIP | core (persons) | core Φ |
|---|---|---|---|---|---|---|---|---|
| +++ | 4 | yes | yes | 4 | 1 | 0 | none | 0 |
| ++− | 4 | **no** | no | 0 | — | 0 | {p, o, q} | **6.000** |
| +−− | 4 | yes | yes | 12 | 1 | 1.660 | {p, o} | 2.000 |
| −−− | 4 | yes | **no** | 24 | 1 | 0.578 | {p, q} | 2.000 |
| −−− | 3 | yes | no | 6 | 1 | 0.193 | {o, q} | 2.000 |
| −−− | 2 | yes | no | 0 | — | 0 | {p, o, q} | 1.024 |
| ++− | 3 | no | no | 0 | — | 0 | {p, o} | 2.000 |
| ++− | 2 | no | no | 0 | — | 0 | {p, o, q} | 0.639 |
| path −− | 4 | yes | yes | 36 | 2 | 0 | {o, q} | 2.000 |

*Table 1. The triangles and the path. Rest states count camp assignments; the Heider paper's one-bit
results for ++− and −−− were Φ 6.000, core all three, 0 rest states.*

| negative lines | 0 | 1 | 2 | 3 | 4 | 5 | 6 | total |
|---|---|---|---|---|---|---|---|---|
| patterns | 1 | 6 | 15 | 20 | 15 | 6 | 1 | 64 |
| clusterable | 1 | 0 | 0 | 4 | 3 | 6 | 1 | 15 |
| balanced | 1 | 0 | 0 | 4 | 3 | 0 | 0 | 8 |

*Table 2. The K4 census at k = 4. Rest states exist for exactly the 15 clusterable patterns; the triangle
test agrees with the cycle test on all 64; every clusterable pattern has one partition at rest.*

### H1 — Theorem 1 on triangles: CONFIRMED

With three or four camps, ppp, pmm, and mmm have rest states — 3, 6, 6 at k = 3; 4, 12, 24 at k = 4 — and
ppm has none at any k. With two camps mmm has none. The all-negative triangle rests as soon as a third camp
exists, in exactly one partition: three singletons.

### H2 — the classes follow clusterability: CONFIRMED

At k = 4 the forbidden triangle ++− has all three persons in its core at Φ = 6.000 — on the three high bits,
which is the Heider paper's one-bit triad reproduced inside the two-bit encoding. The three clusterable
triangles do not: +++ has no complex; +−− has a core of two persons, p and o, the positive pair, at 2.000;
−−− has a core of two persons, p and q, one negative pair, at 2.000. The instrument's classes are Davis's,
not Cartwright–Harary's: one pattern apart, three together.

### H3 — the all-negative verdict is the two-camp verdict: PARTIAL

The central clause held. The all-negative triangle has all three persons in its core at k = 2 and two at
k = 3 and k = 4; its verdict changes when a third camp exists. The comparison clause fell at one point: ++−
has three persons in its core at k = 2 and k = 4 but two at k = 3. The k = 3 encoding carries a dead code
(11) that a person can be pushed into and must leave, and it is the least clean of the three alphabets; at
the two alphabets whose bits are full — the Heider paper's one bit and k = 4 — the forbidden triangle is a
whole of three at 6.000 both times and the all-negative triangle is a whole of three at one and a pair at
the other.

### H4 — Theorem 1 on K4: CONFIRMED

Over the 64 sign patterns of the complete four-person graph with four camps, rest states exist for exactly
the 15 patterns with no cycle of exactly one negative line, the triangle test picks out the same 15, and each
has exactly one partition at rest. Eight of the 15 are balanced; the other seven — the all-negative K4 and
the six with five negative lines — are clusterable with three or four camps and forbidden under balance.

### H5 — the incomplete graph: CONFIRMED

The negative path p –– o –– q with no p–q line is clusterable two ways — {p}{o}{q} and {p, q}{o} — and both
appear among its 36 rest states. Its whole has Φ_MIP = 0 and its core is the pair o and q at 2.000: one of
the two negative ties, not the mediator with both.

## Discussion

The Heider paper's H3 was: −−− is not a third kind; it is ++− relabeled. That verdict is withdrawn. It was
true of a group that had two camps to choose from, and Davis's point is that such a group is the special
case. Given a third camp the all-negative triangle rests, in exactly the partition Davis names, and its
structure under Φ moves from the class of the forbidden triangle to the class of the balanced ones — a pair,
not a whole of three. The instrument sides with Davis over Cartwright and Harary, and it does so for Davis's
reason: the only triangle that cannot be placed at any alphabet is the friend of two enemies.

What the clusterable class looks like under Φ is the paper's second result, and it corrects the Heider
paper on a smaller point. That paper reported balance as *dissolving* — Φ = 0, no complex. With two bits per
person the clusterable patterns that carry a negative tie do not dissolve; they resolve to a pair. +−−'s
core is the positive pair; −−−'s is one negative pair; the path's is one negative pair. Only +++ has no
complex. The pattern is that a satisfiable signed structure leaves one tie standing as its irreducible part
and the rest as background, and which tie stands depends on the tie-break. This is consistent with the
series: Girard's and Serres's forms also resolved to pairs. The forbidden triangle is the exception, and it
is the exception at every alphabet whose bits are full — a whole of three at Φ = 6.000 with one bit and with
two.

The census on K4 is Davis's theorem run as dynamics, and it holds without exception. Its one added finding
is about synchrony: eleven of the fifteen clusterable patterns have attractors that are not rest states,
because two persons who both move at once can swap camps forever. That is a property of simultaneous update
and not of the structure; the theorem is about the existence of rest states and the census tests it as
such.

The dead-code encodings are the paper's weakness and are reported as such. Two bits carry four codes; at
k = 2 and k = 3 a person can be knocked into a code that is not a camp, and the Φ values at those alphabets
(1.024 and 0.639 for the two unbalanced triangles at k = 2, where one bit gave 6.000) show the encoding
doing work the structure is not. H3's failed clause is at k = 3. The comparison the paper rests on is the one
between full alphabets — one bit against k = 4 — and there the result is clean.

## Limitations

PyPhi is binary, and a k-valued person is two bits; the two-bit unit is not the person, and the core is
reported in persons by a rule (either bit in). Dead codes at k = 2 and k = 3 confound those alphabets. The
tie-break biases which pair the clusterable patterns resolve to. Synchronous update produces swap cycles.
Φ on K4 was not run. Rest-state existence is tested; convergence is not claimed.

Results are about Boolean models. No group is measured.

## Conclusion

Davis's theorem holds on every triangle and every signed K4 the lab can enumerate, and the instrument sorts
the triangles as Davis does once a third camp exists: the friend of two enemies is a whole of three at
Φ = 6.000, and three mutual enemies are a pair with a bystander. The Heider paper's finding that the
all-negative triad is the forbidden triad relabeled was a finding about two camps, and is withdrawn.

## References

Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0. *PLoS Computational Biology*, 19(10),
e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Cartwright, D., & Harary, F. (1956). Structural balance: A generalization of Heider's theory. *Psychological
Review*, 63(5), 277–293. https://doi.org/10.1037/h0046049

Davis, J. A. (1963). Structural balance, mechanical solidarity, and interpersonal relations. *American
Journal of Sociology*, 68(4), 444–462. https://doi.org/10.1086/223401

Davis, J. A. (1967). Clustering and structural balance in graphs. *Human Relations*, 20(2), 181–187.
https://doi.org/10.1177/001872676702000206

Davis, J. A., & Leinhardt, S. (1972). The structure of positive interpersonal relations in small groups. In
J. Berger, M. Zelditch, & B. Anderson (Eds.), *Sociological theories in progress* (Vol. 2, pp. 218–251).
Houghton Mifflin.

Doreian, P., & Mrvar, A. (1996). A partitioning approach to structural balance. *Social Networks*, 18(2),
149–168. https://doi.org/10.1016/0378-8733(95)00259-6

Harary, F. (1953). On the notion of balance of a signed graph. *Michigan Mathematical Journal*, 2(2),
143–146. https://doi.org/10.1307/mmj/1028989917

Heider, F. (1958). *The psychology of interpersonal relations*. Wiley.

Mayner, W. G. P., et al. (2018). PyPhi: A toolbox for integrated information theory. *PLoS Computational
Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343

## Appendix A — Rule and forms

All in `forms.py`. Person i, camp c_i ∈ {0, …, k − 1}, bits x_i = c_i mod 2, y_i = c_i div 2.
strain_i(c) = #{positive ties (i, j) : c_j ≠ c} + #{negative ties (i, j) : c_j = c}. Next camp: c_i if valid
and among argmin; else min argmin.

- Triangles: persons p, o, q; ties po, pq, oq with signs +++ / ++− / +−− / −−−; k ∈ {2, 3, 4}.
- K4: persons p, o, q, r; six ties; all 64 sign patterns; k = 4; dynamics only.
- Path: ties po −, oq −; no pq; k = 4.

## Appendix B — Reproduction

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_theorem
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_classes    # ~18 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_alphabet   # ~18 min
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_census
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_path       # ~2 min
```

Registered as `thinkers-davis-h1-theorem` … `thinkers-davis-h5-path` in `ci/reproduce.json`; H2 and H3 are
marked slow.
