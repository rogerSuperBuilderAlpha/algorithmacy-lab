# Review 5 — Systems thinking / complexity science reviewer

**Manuscript:** "When is a combination a configuration? Integrated information and the constitution of
organizational wholes" (Organization Theory, Special Themed Section: Theorizing the Configurational Nature
of Organizational Phenomena, Catalysing & Crystallizing format)

**Reviewer lens:** systems thinking and complexity science — Simon, Kauffman/NK, Levinthal, Rivkin,
loose coupling, emergence and self-organization, and the ceremonial-versus-meaningful-use question raised
by Kimsey et al. (2025).

---

## VERDICT

**Major revisions.** The core idea deserves this venue, but the paper overstates the gap it fills
(complexity science already has within-case decomposability tests it never engages), sells a
near-circular game-theoretic corroboration as independent convergence, and leaves the measure itself
underspecified (which Φ, which IIT version) in a way that puts its own "meaningful use" claim at risk.

## Summary of the contribution

The paper proposes a within-case criterion for when a combination of organizational elements constitutes
one configuration rather than an aggregate: model the arrangement as a small discrete dynamical system,
compute integrated information (Φ) over all partitions, and call the arrangement a configuration exactly
when every partition destroys some of its cause-effect structure. From this one criterion the paper
derives a membership account (the complex, with graded core-periphery structure predicted by pivotality),
a dissolution theory (three operators — substitution, bypass, constraint-lifting — none of which is
formation reversed), and a distinction between necessary and contingent irreducibility that gives power a
formal seat. Small exactly-solved Boolean models illustrate throughout, and a closing section maps the
criterion onto tests native to game theory, platform economics, bargaining, and communication theory. The
paper positions all of this as complementary to QCA: across-case regularity from set analysis, within-case
constitution from the partition test.

Read as a Catalysing & Crystallizing essay, this is the right genre: a theory paper with models as
instruments, in the Davis, Eisenhardt and Bingham (2007) tradition, not a methods paper. The register is
disciplined and the best results (the quorum collapse, the maximal-wiring collapse, the coalition-inside-
a-configuration example) are genuinely instructive. My concerns are about accuracy toward the complexity
literatures the paper leans on, and about whether the criterion's own foundations are stated tightly
enough to survive the scrutiny the paper invites.

## Major issues

**1. The gap claim overreaches: complexity science has within-case decomposability tests, and the paper
never engages them.** Section 1 claims flatly that "no within-case test decides, for a given arrangement,
whether it is one whole," and Section 2 renders Simon (1962) as description awaiting a test
("Simon described how far a system sits from a clean modular cut, and the partition asks... exactly what
the cheapest cut destroys"). This is not accurate as intellectual history. Simon and Ando (1961) gave
near-decomposability an exact within-case criterion for dynamical systems — block-dominance of the
interaction matrix plus timescale separation, with an aggregation theorem saying precisely when the
subsystems can be analyzed as if independent. Markov-chain lumpability does the same for exactly the class
of transition systems this paper builds. Network science supplies modularity maximization, community
detection, and block models; the NK literature itself decomposes influence matrices into patterned
interaction structures (Rivkin & Siggelkow on design; Ethiraj & Levinthal 2004 on modularity mistakes).
A reviewer from my corner reads the current framing as conscription: Simon is cited for the vocabulary and
denied his mathematics.

The irony is that the paper has the ammunition to win the honest version of this comparison and does not
use it. The quorum, synchronization, and maximal-wiring results are exactly the cases where
topology-reading and correlation-reading measures disagree with a counterfactual, partition-and-noise
measure. That is the differentiating argument. Make it.

*Fix (paste-ready, for Section 1 or 2):* "Complexity science has within-case decomposability tests of its
own. Simon and Ando (1961) gave near-decomposability an exact criterion for dynamical systems, lumpability
does the same for Markov chains, and network science reads modular structure off the graph (Newman, 2006).
Each reads correlation, timescale separation, or topology. None runs the counterfactual: sever the
constraints between the parts, replace them with noise, and measure what the joint determination loses.
The quorum and maximal-wiring results below are the cases where the two families part company — maximal
wiring with zero irreducibility — and they are why the counterfactual test is not redundant with the
measures the field already owns." Then narrow the Section 1 gap sentence to "no within-case test *in the
configurational tradition*," which is defensible.

**2. The Shapley convergence is close to circular, and the pivotality story equivocates between two
different games.** Section 3 explains the quorum collapse by saying "at an interior threshold no single
party is pivotal, because the others can reach or miss the count without it." In the standard voting-power
sense this is false: in a 2-of-3 majority gate, each party is decisive in every state where the other two
split, and the Shapley–Shubik index of every player is 1/3 — there are no null players in a majority game.
Section 6 then claims "the Null Player axiom is the substitutability collapse of section 3 in a second
notation." It is not, in the outcome game. The paper escapes only because Section 4 quietly switches games:
the Shapley values are computed "in the integration game," i.e., an element's average marginal
contribution *to the whole's integration*. But if the characteristic function is built from Φ, then
"Shapley values in the integration game predict complex membership" is Φ predicting Φ — a decomposition of
the measure, useful as such, but not "two formalisms, built for different purposes, grad[ing] the same
underlying property." The convergence, as sold, is engineered.

*Fix:* (a) Restate the quorum mechanism precisely — something like: "at an interior threshold each party's
constraint is decisive only in split states, and the constraint it contributes there can be reproduced,
across the state distribution, by the remaining parties; the minimum-information partition exploits
exactly this redundancy" — and show the MIP for the 2-of-3 gate so the reader can see what the cheap cut
severs. (b) In Sections 4 and 6, define the integration game explicitly, concede in one sentence that
outcome-pivotality (Shapley–Shubik) and integration-pivotality diverge at the majority gate — the majority
player has maximal voting power and zero integration contribution — and reframe the game-theoretic row as
a decomposition result, not an independent convergence. This divergence is actually a *finding*: voting
power and constitutive membership are different properties, and the paper is the first place I have seen
that can say so exactly.

**3. Which Φ? The measure is underspecified, and the criterion's verdicts may not be stable across the
Φ family.** The paper cites IIT 3.0 (Oizumi et al., 2014), IIT 4.0 (Albantakis et al., 2023), and PyPhi
(Mayner et al., 2018) without ever saying which measure and version generates the verdicts. This matters
more than a version footnote: the two formulations differ in distance measures, in how causes and effects
are evaluated, and in complex identification, and the broader literature (Mediano and colleagues have made
this point at length) shows that candidate integration measures diverge qualitatively on the same systems.
The paper's central objects are binary verdicts — Φ zero versus positive, element in or out of the
complex — and the reader cannot tell whether the quorum collapse, the rotation result, or the 660-form
membership law are robust across the family or artifacts of one operationalization. For a paper whose
whole contribution is "a definite truth value on a definite model," this is a load-bearing omission. It is
also where a hostile reviewer lands first.

*Fix:* State the exact formalism and version in Section 2 (one sentence), and add to Section 7's
sensitivity discussion a second axis alongside encoding sensitivity: verdict robustness across measure
variants, reported the same way the four-of-ten encoding flips are reported. If the headline results
(quorum, rotation, maximal wiring, bidirectional-coupling law) hold under both IIT 3.0 and 4.0, say so —
that is a strong sentence to be able to write. If they do not, the paper needs to know.

**4. The Kimsey et al. "meaningful use" claim boomerangs unless the encoding discipline gets teeth.**
Section 6 offers the criterion as a meaningful rather than ceremonial use of systems thinking. I am
sympathetic, and the non-obvious verdicts (busy quorum factors, idle cycle binds) are real inferential
work — this is not systems vocabulary as ornament. But the paper's own Section 7 reports that four of ten
stylized cases flipped verdicts under defensible re-encodings. With that much analyst freedom, Φ can
become the most sophisticated ceremonial instrument yet built: the analyst encodes until the verdict
matches the intuition, then cites the mathematics as warrant. The paper's answer — state the three
commitments, report sensitivity — is the right kind of answer but currently a norm, not a procedure.
Meaningful use, in Kimsey et al.'s sense, requires that the systems apparatus be able to *lose*: the
encoding must be fixed before the verdict is known.

*Fix:* Add three or four sentences to Section 7 specifying an encoding protocol: rules committed from the
arrangement's own documents (contracts, interface specifications, the typologist's stated couplings — as
the canon-testing agenda already does) before any computation; verdicts reported with their sensitivity
class over the defensible-encoding neighbourhood; a flipped verdict treated as a finding about where
constitution lives, as the paper already argues, not as license to choose. The canon-testing paragraph in
the agenda does this implicitly; make it the general rule.

**5. The formation/dissolution asymmetry is asserted, not derived, and the paper's own operators undercut
it as written.** Section 5 claims dissolution needs one operator to fire while formation "must build a
joint determination... constructive, path-dependent work." But substitution is parameter drift and drift
is reversible: moving sign-off from two-of-three to unanimity creates a configuration in one move, exactly
as the reverse dissolves one. And the paper itself says an architect can "manufacture contingent
irreducibility by erecting constraints" — one move again. So the asymmetry does not follow from the
operators. What would ground it is measure-theoretic, and the paper already has the number: within the
enumerated class, bound forms are "on the order of a tenth." If bound forms are rare, a random perturbation
from a bound form usually lands factored and a random perturbation from a factored form rarely lands
bound — that is the asymmetry, and it is sitting unused two sections earlier. Simon's watchmaker parable
makes the same point dynamically and is the natural citation: Tempus's fully integrated watch cannot be
assembled from stable intermediates and falls apart in one interruption. The paper cites Simon (1962) and
leaves his best argument on the table. Relatedly, the paper's tone valorizes irreducibility ("a special
achievement"); a complexity reader will note that on NK landscapes full interdependence is the *chaotic*
regime — maximally integrated systems are the ones that cannot adapt — and that fragility is the price the
asymmetry argument itself names. One sentence acknowledging that high Φ is a descriptive verdict, not a
design recommendation, would prevent the misreading.

*Fix (paste-ready, Section 5):* "The asymmetry is a claim about measure, and the enumeration of section 3
already carries it: bound forms are on the order of a tenth of the class, so a perturbed configuration
usually lands among aggregates while a perturbed aggregate rarely lands bound. Simon's (1962) watchmakers
say the same thing dynamically — the fully integrated assembly has no stable intermediates, so it must be
built in place and comes apart in one interruption. Irreducibility is in this sense expensive to hold, and
nothing in the criterion says holding it is good: on rugged landscapes, full interdependence is the regime
in which adaptation fails (Levinthal, 1997; Rivkin, 2000)."

**6. The quorum verdict cuts against the tradition the paper is addressing, and the paper should face
that instead of only celebrating it.** A majority vote is the canonical *jointly determined* organizational
outcome — boards, committees, standard-setting bodies. The criterion classifies the majority gate as an
aggregate, with no gradient. Presented as discriminating power, this will read to many configurational
scholars as a reductio: whatever Meyer et al. (1993) meant by parts taking meaning from the whole, a board
that decides by majority was surely inside it. The paper should either bite the bullet explicitly — the
tradition's word "whole" has bundled joint outcome-determination with constitutive irreducibility, and the
criterion splits them, majority governance being the paradigm of the first without the second — or concede
that the criterion formalizes one precise sense of constitution among the senses in use. The same
confrontation is owed in the other direction for the rotation: a ring of four copyists is a shift register,
and calling it a bound configuration strains organizational intuition at least as much as the quorum
verdict does. Both verdicts may be right; neither is defended against the intuition it violates. And keep
the emergence boundary explicit while doing so: Φ measures irreducibility of cause-effect structure, not
emergent macro-behavior — the majority gate is a textbook case of emergent collective behavior with zero
integration, which is the cleanest possible demonstration that the two concepts are distinct, and the paper
never says it.

## Minor issues

1. **Kauffman is named but not cited.** Section 2 credits "Kauffman's NK model" with no reference entry.
   Cite Kauffman (1993), *The Origins of Order*, or Kauffman & Levin (1987). Also, "statistical physics,
   via Kauffman's NK model" compresses the history: NK came out of theoretical population biology (Wright's
   fitness landscapes) with spin-glass mathematics; "spin-glass physics, via Kauffman's NK model" or
   "theoretical biology" would both be more accurate.
2. **Provenance of the computed results.** The 660-form enumeration, the ten-case demonstration, and the
   51-intermediary catalog carry quantitative claims ("four in ten to nine in ten," "about a quarter...
   about half") with no appendix, repository, or supplementary encoding list, despite the abstract's
   promise that every number "reproduces from the model's stated encoding." For this format an online
   appendix with the encodings and the solver version is the minimum.
3. **Hindsight risk in the retrodiction.** The internet-disintermediation sort (Section 5) classifies a
   hand-assembled catalog with outcomes already known. Say in one clause that the sort is retrodictive
   and the catalog was assembled with hindsight, and let the forward-looking platform agenda carry the
   predictive weight.
4. **Orton & Weick, one step further.** The two-dimensional caveat is welcome and better than most
   borrowings manage. But in Orton and Weick's (1990) own typology, a system whose cheapest partition is
   free is *decoupled*, not loosely coupled; loose coupling pairs responsiveness with distinctiveness. The
   natural translation is positive-but-modest Φ over parts that remain integrated in their own right —
   worth one sentence, since it makes loose coupling a structural regime rather than a low band on a scale.
5. **Antithesis density.** The "X is not Y" engine runs hot in places ("Connection is not constitution";
   "a property of joint determination, not of headcount or wiring density"; "a partnership, not a
   takeover"; "one causal thing"). Each instance is fine; the accumulation is a cadence. Cut roughly a
   third, keeping the load-bearing ones (the quorum paragraph's closer earns its place).
6. **Table 1's authority outruns its text.** The paper is admirably careful that only the game-theoretic
   row "has computation behind it," but the table renders all five rows with equal visual weight. Mark the
   correspondence strength in the table itself (e.g., a column: computed / exhibited).

## Bottom line

This is the rare borrowing paper where the formal core actually does inferential work: the quorum and
maximal-wiring collapses, the coalition-inside-a-configuration result, and the necessary/contingent
distinction are contributions a complexity scientist can respect, and the essay format fits the section's
call. But the paper currently wins its gap by not looking at the decomposability tests my field already
owns, corroborates its membership law with a game it built from the measure itself, and computes verdicts
with an instrument it never fully specifies. All three are fixable, and fixing them would make the paper
stronger in exactly the direction it wants to go — from an affinity of sensibility to a criterion that can
lose, which is what meaningful use of systems thinking means. Major revisions, with genuine enthusiasm for
the revised version.
