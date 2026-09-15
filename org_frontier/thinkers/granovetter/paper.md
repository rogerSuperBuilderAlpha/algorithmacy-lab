# Paths and cycles: Granovetter's weak ties under exact Φ

<code + data: org_frontier/thinkers/granovetter/ ; probes #399–#403 in probes/PROBES.md ; standard in
org_frontier/thinkers/PAPER_STANDARD.md>

## Abstract

Granovetter's argument runs from a definition of tie strength to a claim about communities: strength is a
graded, symmetric quantity whose first dimension is time; two strong ties from one person close into a triad;
therefore bridges between groups are weak; therefore weak ties carry diffusion and their removal damages
transmission most; therefore a community of cliques without weak ties between them is cohesive locally and
fragmented as a whole, and weak ties are what integrate it. This paper renders a tie as Granovetter defines
it — symmetric, with a strength p that is the probability each endpoint reads the other on a given step — and
reads each form with exact IIT-4.0 Φ on the resulting probabilistic TPM, with the major complex, and with a
count of pairs joined by a path. Five hypotheses were fixed before computing. Strength is graded: a dyad's
Φ rises 0.252 → 0.658 → 1.236 → 2.000 as p rises from 0.25 to 1 (H1 confirmed). The forbidden triad closes as
Granovetter said: open Φ = 2.000, weak-closed 2.830, strong-closed 6.000, all members in every core (H2
confirmed). A bridge between two cliques transmits and does not integrate: weak or strong, it joins 12 pairs
by path and leaves one dyad as the major complex (H3 refuted). Cutting the weak bridge costs more transmission
than cutting a strong tie and no more integration (H4 partial). Three cliques in a weak chain remain a dyad's
complex; in a weak ring they are one whole of six at Φ = 2.490 (H5 partial). Granovetter's integration is a
path and the instrument's is a cycle; they agree wherever the weak ties close. Results are about Boolean
models, not about any community.

## Introduction

Granovetter's 1973 paper is a chain of deductions from one definition. The strength of a tie is "a (probably
linear) combination of the amount of time, the emotional intensity, the intimacy (mutual confiding), and the
reciprocal services which characterize the tie" (1361). Stronger ties overlap more in their friends; so two
strong ties from one person tend to close; so the configuration in which they do not — the forbidden triad —
can be treated as absent; so a strong tie is almost never the only path between two groups; so "all bridges
are weak ties" (1364); so what diffuses travels farther through weak ties and their removal costs
transmission most; so a community whose cliques are joined by no weak ties is fragmented, though "the local
phenomenon is cohesion" (1374). The paper ends on the paradox that weak ties, "often denounced as
generative of alienation," are "indispensable ... to their integration into communities" (1378).

Every link in the chain is a claim about paths — whether information or influence can get from one point to
another. The lab's criterion is a claim about something else that also goes by the name integration: whether
a set of parties is an irreducible whole, with positive Φ and a major complex the whole cannot be cut from
without loss. The two are not the same. A path carries a difference from A to B; irreducibility requires that
what B does return to A. Bridges, by Granovetter's own definition, are lines with no alternative path, which
is to say no return except through themselves. Centola and Macy (2007) opened one gap between transmission
and something else a tie does — behaviors that need reinforcement do not cross long ties — and the present
question is a second: whether the ties that transmit are the ties that bind.

Granovetter's definition makes his rendering available. Time is the first dimension of strength, and a tie
read each step with probability p is a symmetric tie of strength p, which is what his footnote requires
("ties discussed in this paper are assumed to be positive and symmetric"). The lab's instrument takes
probabilistic transition matrices, so weak ties can be weak in his sense rather than in a substitute's. This
paper runs five of his claims on that rendering: the graded dyad (H1), the forbidden triad and its closures
(H2), the bridge (H3), the cut (H4), and the community of cliques (H5).

## Granovetter's account

The definition comes first, with two stipulations: strength is graded and ties are symmetric (1361). The
overlap hypothesis follows — "the stronger the tie between A and B, the larger the proportion of individuals
in S to whom they will both be tied" (1362) — on the reasoning that time spent with A is time B and C spend
near each other, and that cognitive balance then pulls them together.

From overlap comes the forbidden triad: with A–B and A–C strong, the B–C tie absent is "the triad which is
most unlikely to occur," and Granovetter exaggerates this to a rule, "that the B–C tie is always present
(whether weak or strong), given the other two strong ties" (1363). From the rule comes the theorem about
bridges. A bridge is "a line in a network which provides the only path between two points" (Harary, Norman,
and Cartwright, 1965), and "if the stipulated triad is absent, it follows that, except under unlikely
conditions, no strong tie is a bridge," since the other strong ties of its endpoints would close around it
(1364). A local bridge of degree n is a tie whose endpoints' shortest other path has length n, and it matters
more as n grows (1365).

Diffusion follows: "removal of the average weak tie would do more 'damage' to transmission probabilities
than would that of the average strong one," and "whatever is to be diffused can reach a larger number of
people, and traverse greater social distance ... when passed through weak ties rather than strong" (1366).
Community follows from diffusion. A community "completely partitioned into cliques, such that each person is
tied to every other in his clique and to none outside," could not organize; it is "extremely fragmented" at
the macroscopic level while cohesive locally (1373–1374). Gans's West End, which failed to resist urban
renewal, is the case. Weak ties that are bridges are what integrate such a community; strong ties, "breeding
local cohesion, lead to overall fragmentation" (1378).

## From claims to forms

A **tie** is symmetric and has a strength p ∈ [0, 1]. Each step, each endpoint reads the other with
probability p, independently; **strong** is p = 1, **weak** p = 0.5, **absent** p = 0. A node's next state is
the AND of the inputs it read this step; a node that read nothing holds its state. The state-by-node TPM is
the expectation over read sets, so a network with weak ties is stochastic, and Φ is computed exactly on it.
With strong ties only, the machinery reproduces the lab's deterministic forms: the tie-built conjunctive
triad has Φ = 2.000000, the control value.

**Transmission** is Granovetter's path: the number of ordered pairs joined by a path of ties of any strength.
**Integration** is Φ_MIP of the whole, maximized over reachable states, and the major complex with its Φ.

Five families follow. **Dyad** (H1): one tie at p = 0.25, 0.5, 0.75, 1. **Triad** (H2): A–B and A–C strong;
B–C absent, weak, or strong. **Bridge** (H3): two strong dyads a₁–a₂ and b₁–b₂ joined by a₂–b₁ at p = 0.5 or
1. **Cut** (H4): the weak-bridged form with the bridge removed, or with a₁–a₂ removed. **Community** (H5):
three strong dyads, isolated; joined by weak ties in a chain (a₂~b₁, b₂~c₁); in a ring (adding c₂~a₁); and in
a strong ring.

## Hypotheses

Fixed in `hypotheses.md`. The machinery was smoke-tested on the dyad and the bridge before H2–H5 were fixed;
the H1 and H3 numbers were therefore seen first and are reported unchanged, and the hypotheses say so.

- **H1 (Granovetter) — strength is graded.** Φ(dyad) strictly increasing in p. *Prior:* with.
- **H2 (Granovetter) — the forbidden triad closes.** Φ(open) < Φ(weak-closed) < Φ(strong-closed), all three
  in every core. *Prior:* with, on the open–strong ordering; open on the weak closure.
- **H3 (Granovetter) — a weak bridge does what a strong one does.** Transmission equal and the major complex
  spans both dyads under both. *Prior:* against on integration.
- **H4 (Granovetter) — the weak bridge's removal does more damage** on transmission and on integration.
  *Prior:* with on transmission, against on integration.
- **H5 (Granovetter) — weak ties integrate the community.** Chain and ring both have a major complex spanning
  all three dyads. *Prior:* against for the chain, open for the ring.

Decision rules are in `methods.md`.

## Methods

**Instrument.** Exact IIT-4.0 Φ (Albantakis et al., 2023) via PyPhi (Mayner et al., 2018) on probabilistic
state-by-node TPMs; whole-system Φ as the maximum over all reachable states of system Φ; major complex as
PyPhi's maximal complex, maximized over reachable states. Both mirror `org_frontier.probes.lib` for the
deterministic case.

**Control.** Every probe first runs the conjunctive triad by rules (Φ = 2.000000, core {A, M, B}) and then
by ties (Φ = 2.000000). All five probes passed both.

**Forms.** As in the previous section and Appendix A; two to six nodes; the six-node forms take one to three
minutes each.

**Procedure.** Five probes, one per hypothesis; each prints the controls, one line per form (Φ_MIP, core,
core Φ, transmission), and a verdict. Results in `results/`, registered in `ci/reproduce.json` (probes
#399–#403).

**Scope.** Results are about the Boolean models. No community, tie, or person is measured.

## Results

Table 1 collects the forms.

| H | form | Φ_MIP | core | core Φ | transmission |
|---|---|---|---|---|---|
| 1 | dyad p = 0.25 | 0.252 | {a, b} | 0.252 | 2 |
| 1 | dyad p = 0.50 | 0.658 | {a, b} | 0.658 | 2 |
| 1 | dyad p = 0.75 | 1.236 | {a, b} | 1.236 | 2 |
| 1 | dyad p = 1 | 2.000 | {a, b} | 2.000 | 2 |
| 2 | open (forbidden) | 2.000 | {A, B, C} | 2.000 | 6 |
| 2 | weak-closed | 2.830 | {A, B, C} | 2.830 | 6 |
| 2 | strong-closed | 6.000 | {A, B, C} | 6.000 | 6 |
| 3 | bridge weak | 0.830 | {b₁, b₂} | 2.000 | 12 |
| 3 | bridge strong | 2.000 | {b₁, b₂} | 2.000 | 12 |
| 4 | cut bridge | 0 | {b₁, b₂} | 2.000 | 4 |
| 4 | cut strong (a₁–a₂) | 0 | {b₁, b₂} | 2.000 | 6 |
| 5 | isolated | 0 | {c₁, c₂} | 2.000 | 6 |
| 5 | weak chain | 0.830 | {a₁, a₂} | 2.000 | 30 |
| 5 | weak ring | 2.490 | all six | 2.490 | 30 |
| 5 | strong ring | 4.000 | all six | 4.000 | 30 |

*Table 1. Whole-system Φ_MIP, major complex and its Φ, and ordered pairs joined by a path. Controls passed in
every probe.*

### H1 — strength is graded: CONFIRMED

The dyad's Φ rises with p at every step, 0.252, 0.658, 1.236, 2.000, and the pair is the complex at every
strength. Granovetter's "probably linear" is not linear here — the increments grow, 0.41, 0.58, 0.76 — but
the quantity is graded, monotone, and zero at p = 0. Strength as time is strength as integration.

### H2 — the forbidden triad closes: CONFIRMED

The open triad is the lab's conjunctive triad: A reads B and C, each reads A, Φ = 2.000, all three in the
core. Closing B–C with a weak tie lifts the whole to 2.830; closing it with a strong tie to 6.000. All three
members remain in every core. Granovetter's exaggeration — that the third tie is "always present (whether
weak or strong)" — reads as a gradient the instrument confirms: each increment of closure adds integration,
and the weak closure sits between absent and strong as his ordering requires. What the instrument adds is that
the open form is already a whole; the forbidden triad is not a configuration lacking integrity but one with
less of it than its closures.

### H3 — a weak bridge does what a strong one does: REFUTED

Transmission is identical: 12 ordered pairs under either bridge. Integration is not what Granovetter's
argument needs under either. With a weak bridge the four-node whole reaches Φ_MIP = 0.830 and the major
complex is one dyad, {b₁, b₂}, at 2.000: the bridge is outside the complex and so is the other dyad. With a
strong bridge the four-node whole reaches 2.000 — the same as one dyad — and exclusion returns the dyad. The
bridge, weak or strong, transmits across and integrates nothing across. The verdict is refuted on both
sides, not partial: even the bridge Granovetter says cannot exist fails to join the groups it spans.

### H4 — the weak bridge's removal does more damage: PARTIAL

On transmission Granovetter is right. Cutting the weak bridge loses eight of twelve pairs; cutting a strong
within-dyad tie loses six. On integration neither cut moves the major complex, which is the surviving dyad at
2.000 in both cases, and both cuts take the whole's Φ_MIP from 0.830 to 0. The bridge was never in the
complex; the strong tie was, but its dyad's loss is masked by the other dyad's survival. Damage to
transmission and damage to integration are measured on different objects, and on the second the bridge has
nothing to lose.

### H5 — weak ties integrate the community: PARTIAL

Three isolated dyads are three complexes of two; the whole has Φ_MIP = 0 and transmission 6. A weak chain
raises transmission to 30 and integration to 0.830, with the major complex still a dyad, {a₁, a₂}: the
community transmits end to end and is, on this criterion, still fragmented. A weak ring — one more weak tie,
closing c₂~a₁ — makes the six a single complex at Φ = 2.490, above any dyad's 2.000, and a strong ring makes
them one at 4.000. Granovetter's aerial view finds a whole when the weak ties return to where they started
and not before.

## Discussion

One line runs through the five results. Transmission is a property of paths; irreducibility is a property of
cycles. A tie of any strength that lies on a path carries a difference across it, and Granovetter's counts —
twelve pairs, thirty pairs, eight lost against six — are all counts of paths. A tie contributes to a complex
only when what it carries comes back, and the forms sort exactly on that. The dyad is a two-cycle and its Φ
grades with strength (H1). The forbidden triad is two two-cycles through A and its closures add a third (H2).
The bridge is a path between two cycles and joins neither to the other (H3, H4). The chain is a longer path
and does the same; the ring is a cycle through all three cliques and binds them (H5).

The bridge result is the paper's center, and it holds for the strong bridge as for the weak one. That is
what makes it a result about bridges rather than about weakness: Granovetter's theorem that bridges are weak
is beside the point for integration, because a bridge of any strength is a line with no return except
through itself, and a line with no return is outside every complex that does not contain both its ends and
a second path between them. The path a₁–a₂–b₁–b₂ has Φ_MIP = 2.000 as a whole when its bridge is strong,
which equals one dyad; the ring of six has 2.490 with weak joins and 4.000 with strong. Closing the path is
what lifts the whole above its parts. Granovetter's local bridge of degree n — a tie whose endpoints have
another path of length n — is, in these terms, a tie on a cycle of length n + 1, and it is the cycle that
integrates. His intuition that a local bridge "will be more significant ... as its degree increases" is
about how many people depend on it for transmission; for integration the dependence runs the other way,
since a bridge with no alternative path binds nothing and one with a short alternative path lies on a short
cycle.

H2 shows the two criteria agreeing, and shows why. The forbidden triad is not fragmented by Granovetter's
standard or by the instrument's: it is a whole of three at Φ = 2.000, and each closure is a whole of three
with more. His rule that the third tie is present is, read structurally, a claim that the more integrated
form is the one that persists, and the gradient 2.000 → 2.830 → 6.000 is that claim in numbers. It also
relocates the paradox he ends on. Strong ties "breeding local cohesion" produce the 6.000 clique and the
2.000 dyad; the same cliques are joined into a larger complex only by ties that close a cycle around them,
and those ties can be weak (the ring at 2.490) but cannot be bridges.

H1 belongs beside the Burt paper's H3. There, closure among a broker's contacts was a cliff: the first tie
took all of the broker's value added. Here, strength within a tie is a slope: Φ rises with p at every step.
The difference is not in the instrument but in what is being graded. Burt's constraint grades the presence of
other paths, and a second path is either there or not; Granovetter's strength grades the frequency of one
path, which is a continuous quantity that the TPM carries continuously into Φ.

Centola and Macy (2007) found that long ties spread simple contagions and fail for complex ones, which need
reinforcement from more than one contact. The present result is a different cut across the same seam.
Reinforcement is a property of a node's inputs — how many must agree — and this paper's nodes are
conjunctive throughout, so every form here is a complex contagion in their sense. What separates the bridge
from the ring is not the number of confirming inputs but whether the tie's effect returns to it. A theory of
what weak ties do has at least three layers — carry, reinforce, bind — and Granovetter's is the first.

## Limitations

One rendering of strength: read probability, conjunctive integration of what is read, hold when nothing is
read. A node that took the majority or the disjunction of its reads would be a different form, and the lab
has found majority rules to factor where conjunctive ones bind. Weak is p = 0.5 throughout; the H1 gradient
suggests the bridge and ring results would move with p but not reverse. The H1 and H3 numbers were seen in
the machinery check before H2–H5 were fixed. H3's strong bridge ties whole and part at 2.000 and the verdict
rests on exclusion at a tie. H4's integration measure, major-complex Φ, cannot register the loss of a dyad
when another dyad survives; whole-system Φ_MIP falls to zero under either cut, which is equal damage, not
less. The six-node forms are at the instrument's practical limit, and larger cliques were not run.

Results are about Boolean models. No community, tie, or person is measured, and nothing here says whether
any West End was fragmented.

## Conclusion

Granovetter's tie strength is a graded quantity on this criterion, and his forbidden triad closes in the
order he gave. His bridges transmit and do not integrate — weak or strong, they join two groups by path and
leave each group its own complex — and cutting one costs transmission and nothing else. His community of
cliques becomes one whole when the weak ties between cliques form a ring, and not when they form a chain.
Weak ties are the strength of a community's paths. Its integration, in the sense of a whole the parts cannot
be cut from, is the work of cycles, and the weak ties that do that work are the ones that come back.

## References

Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0. *PLoS Computational Biology*, 19(10),
e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Burt, R. S. (1992). *Structural holes: The social structure of competition*. Harvard University Press.

Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of
Sociology*, 113(3), 702–734. https://doi.org/10.1086/521848

Davis, J. A. (1967). Clustering and structural balance in graphs. *Human Relations*, 20(2), 181–187.
https://doi.org/10.1177/001872676702000206

Granovetter, M. S. (1973). The strength of weak ties. *American Journal of Sociology*, 78(6), 1360–1380.
https://doi.org/10.1086/225469

Granovetter, M. (1983). The strength of weak ties: A network theory revisited. *Sociological Theory*, 1,
201–233. https://doi.org/10.2307/202051

Harary, F., Norman, R. Z., & Cartwright, D. (1965). *Structural models: An introduction to the theory of
directed graphs*. Wiley.

Mayner, W. G. P., et al. (2018). PyPhi: A toolbox for integrated information theory. *PLoS Computational
Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343

## Appendix A — Forms

All in `forms.py`. A tie {i, j} of strength p: each step, i reads j with probability p and j reads i with
probability p, independently. Node rule: AND of the inputs read this step; hold if none.

- **H1** (a, b): a–b at p ∈ {0.25, 0.5, 0.75, 1}.
- **H2** (A, B, C): A–B = A–C = 1; B–C ∈ {0, 0.5, 1}.
- **H3** (a₁, a₂, b₁, b₂): a₁–a₂ = b₁–b₂ = 1; a₂–b₁ ∈ {0.5, 1}.
- **H4** as H3 at 0.5; `cut_bridge` drops a₂–b₁; `cut_strong` drops a₁–a₂.
- **H5** (a₁, a₂, b₁, b₂, c₁, c₂): three dyads at 1; `chain` adds a₂–b₁, b₂–c₁ at 0.5; `ring` adds c₂–a₁ at
  0.5; `strong_ring` the same three at 1.

## Appendix B — Reproduction

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_strength
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_triad
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_bridge
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_damage
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_community
```

Registered as `thinkers-granovetter-h1-strength` … `thinkers-granovetter-h5-community` in
`ci/reproduce.json`; the community probe takes about six minutes, the rest seconds.
