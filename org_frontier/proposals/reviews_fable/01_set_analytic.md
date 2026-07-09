# Review 1 — Set-analytic / QCA reviewer

**Manuscript:** "When is a combination a configuration? Integrated information and the constitution of
organizational wholes" — Organization Theory, Special Themed Section "Theorizing the Configurational
Nature of Organizational Phenomena" (Catalysing & Crystallizing)

**Reviewer register note.** The piece is a theory essay in an impersonal, claim-first register with
computed illustrations; I hold it to that bar, not to the conventions of an empirical QCA paper. My
comments concern content and fairness to the set-analytic tradition, with prose remarks confined to the
minors.

---

## VERDICT

**Major revisions.** The central distinction — across-case set membership versus within-case causal
unity — is real, and the essay's framing of the two as complements is the right one. But the novelty
claim overreaches against set-theoretic within-case work, the borrowed formalism is underspecified at
exactly the points where verdicts depend on it, and the encoding problem receives far less discipline
than QCA gives the analogous problem of calibration.

## Summary of the contribution

The essay argues that configurational theorizing presupposes, without formalizing, a claim of
constitution: that a given arrangement is one causal whole rather than an aggregate of smaller
determinations. QCA formalizes constitution at the level of the outcome — which combinations of
conditions travel with a result across cases — but does not test, of a single arrangement modeled as its
interacting parts, whether that arrangement is one joint determination. The essay imports the formal
core of integrated information theory (partitions of a cause-effect structure, Φ as the cost of the
cheapest cut, the complex as the maximal irreducible subset) and proposes: a combination is a
configuration when every partition of its elements loses constraint. From the criterion it derives an
account of membership (computed cores and peripheries, graded by pivotality, converging with Shapley
values), a theory of dissolution (three operators — substitution, bypass, constraint-lifting — none of
them formation reversed), and a distinction between necessary and contingent irreducibility that gives
power a formal seat: some core members do integrating work no direct tie can reproduce; others are held
in place by a constraint that forbids the parties to meet. Small Boolean models illustrate throughout;
the essay claims theory, not measurement. Section 6 positions the criterion as a complement to QCA and
exhibits looser correspondences with cooperative game theory, platform economics, bargaining, and
communication theory.

I read the essay as in scope for the section: it is a generative cross-disciplinary import, not a
methods paper, though Major issue 7 flags where that line wobbles.

## Major issues

**1. "Has no formal test" overclaims against set-theoretic within-case research.** The abstract says the
within-case question "has no formal test," and section 1 says the boundary question "has no answer
inside the theory." A set-analytic reader will object on both counts. Schneider and Wagemann (2012)
build within-case analysis into their standards of good practice; Schneider and Rohlfing (2013)
formalized set-theoretic multimethod research, with explicit rules for selecting cases from the truth
table and tracing mechanisms inside them; and Ragin and Becker (1992) theorized "casing" — the
question of what the case is and where its boundary falls — a generation ago. The manuscript's novelty
survives this literature, but narrowed: post-QCA process tracing asks *how* a condition produces an
outcome within a case; the essay asks whether the arrangement *is one causal thing at all*. That is a
different question, and the essay should say so explicitly rather than leave the field looking blank
where it is merely aimed elsewhere. Paste-ready for section 1 (after "...whether that arrangement is a
single whole," line 71): *"Set-theoretic multimethod research does send the analyst back into cases,
with formal rules for choosing which ones and tracing mechanisms inside them (Schneider & Rohlfing,
2013; Schneider & Wagemann, 2012), and Ragin and Becker (1992) theorized the prior question of what
bounds a case at all. But process tracing tests the mechanism connecting condition to outcome; it does
not test constitution — whether the traced arrangement is one joint determination or several running
side by side. That within-case question is the gap this essay addresses."* Adjust the abstract's "has
no formal test" accordingly ("no formal test for constitution"), and soften "no answer inside the
theory" to "no computed answer" — casing is an answer, just an informal one.

**2. The QCA contrast in section 6 trades silently on a type difference.** "An arrangement can be a
QCA-configuration and an aggregate" is true, but partly because the two formalisms quantify over
different objects: QCA conditions are *attributes of a case* (e.g., high formalization, munificent
environment); the criterion's elements are *interacting parts within the case* (dispatcher, driver,
rider). The essay's contrast reads as if both operate on the same roster and reach different verdicts.
State the type difference and the bridge it demands: to use the two together on the same phenomenon,
the analyst must say which condition-attributes are realized by which interacting parts, and that
mapping is itself a theoretical commitment on a par with calibration. One paragraph in section 6 fixes
this and strengthens the complementarity claim — the division of labour is cleaner once the objects
differ by construction. Relatedly, note the irony the essay leaves unclaimed: the enumerated results
(660 forms, membership rates rising from four in ten to nine in ten) are *across-model regularities* —
a truth-table analysis over a population of model forms. The essay does cross-case analysis on its own
models to establish its within-case criterion. Owning this would be graceful and would open a real
methodological bridge: QCA over model catalogs.

**3. The formalism is underspecified where verdicts depend on it.** The manuscript cites both IIT 3.0
(Oizumi et al., 2014) and IIT 4.0 (Albantakis et al., 2023), which differ in distance measure and
partition scheme and can differ in verdicts. It never states which version the computations use, and —
more damaging — Φ in IIT is *state-dependent*, yet every verdict in the essay is reported as a property
of the arrangement ("the quorum system is irreducible at exactly two thresholds"). Irreducible at which
states? At every reachable state, at some state, at a designated operating state? The quorum theorem,
the rotation result, and the 660-form membership law are all uninterpretable at the level of precision
the essay elsewhere demands of itself until this is fixed. Second inconsistency: section 3's criterion
quantifies over "every partition of the elements," but section 2's third modeling commitment restricts
attention to "the party partition... along the lines between the parties whose relation is in
question," and section 3's fifth result speaks of "a party-respecting partition." A restricted
partition set weakens Φ > 0 claims relative to the full minimum-information partition; say which
quantifier the criterion actually uses and why. Fix: a short specification paragraph at the end of
section 2 — version, measure, software (PyPhi is already cited), state policy, partition scheme — and
one sentence in section 3 reconciling "every partition" with the party partition.

**4. Encoding receives less discipline than QCA gives calibration, and the essay knows it.** Four of
ten stylized cases changed verdict under a defensible re-encoding — a 40% flip rate. If a QCA paper
reported that defensible recalibration flipped set membership for 40% of its cases, no journal in this
tradition would print the solution; Ragin (2008) devotes chapters to calibration precisely to prevent
it, and Greckhamer, Furnari, Fiss and Aguilera (2018) codify the robustness reporting that has become
standard. The essay's remedy — "state the load-bearing rules and report the verdict with its
sensitivity" — is a gesture where QCA has a protocol. The reframing of sensitivity as informative
("which rule flips a case locates where the constitution lives") is genuinely good and should stay,
but it does not substitute for a reporting standard. Paste-ready for section 7, second boundary: *"A
verdict is reportable when it comes with: (i) the element roster and the exclusions it required; (ii)
the state-individuation rule; (iii) each transition rule with the evidence that licenses it; (iv) the
partition scheme; and (v) the verdict under each defensible re-encoding the analyst can name, with the
flipping rule identified. This is the discipline calibration imposes on set-analytic work (Ragin,
2008; Greckhamer et al., 2018), owed here in kind."*

**5. Equifinality and asymmetry go missing after being named.** Section 1 correctly identifies
conjunction, equifinality, and asymmetry as the neo-configurational core (Misangyi et al., 2017;
Furnari et al., 2021), but the criterion is developed against conjunction alone. Two questions a
set-analytic reader will ask and the essay should answer. (a) Does the criterion admit within-case
equifinality — distinct irreducible structures producing the same behavior — and its converse,
behaviorally identical arrangements with opposite verdicts? The synchronization result (section 3)
comes within a sentence of the converse and does not name it. (b) The dissolution asymmetry of section
5 — organizing and disorganizing are not inverses — is a within-case sibling of set-theoretic causal
asymmetry, where the absence of an outcome is not explained by negating the recipe for its presence.
The parallel is available, flattering to both traditions, and unclaimed. One paragraph each; the
second belongs in section 6's QCA paragraph.

**6. The essay's numbers cannot be checked from the essay.** 660 strict-mediation forms; fifty-one
intermediary types read as roughly a quarter necessary and half contingent; ten cases with four flips;
"on the order of a tenth of that class"; membership from four in ten to nine in ten. The front matter
promises that every number "reproduces from the model's stated encoding," but no encoding is stated in
the manuscript — the models are described, never given. QCA's norm is publishing the truth table; the
equivalent here is an online appendix or repository with the transition tables, the enumeration
procedure for the 660 forms, and the intermediary catalog with its coding rules. Without it, the
quantitative texture is rhetoric. Either supply the apparatus or cut the census numbers and keep only
worked examples whose rules appear in the text.

**7. Scope risk: parts of the essay drift toward the excluded methods genre.** The section brief
excludes purely methodological contributions. The essay's spine is theory — constitution, membership,
dissolution, the necessary/contingent distinction — and the closing sentence rightly says the concepts
travel "with or without the borrowed formalism." But section 2's modeling commitments and the "encode
and test the canon" agenda item read as procedure, and my fixes under issues 3–4 add more. Manage the
tension explicitly: keep the protocol material in a boxed appendix or the online supplement, and let
the body argue the concepts. The necessary/contingent distinction, the brokerage payoff (the *tertius
iungens* as self-liquidating is the best single result in the paper), and the dissolution operators
are the contribution this section wants; the computational recipe is the supporting apparatus.

## Minor issues

1. **The quorum result needs its objection stated.** Most readers will balk at Φ = 0 for a majority
   committee — the arrangement organizational life treats as the very type of joint determination.
   The substitutability explanation is there, but add one sentence conceding the counterintuition and
   one saying whether the result is robust across IIT versions and distance measures or specific to
   the computed one. If it is metric-specific, the "sharp boundary" language should soften.
2. **"Strict mediation" is used (sections 4, 5, 7) but never defined.** Define it at first use.
3. **Verify the Hancock, Naaman and Levy (2020) attribution.** The "transmit / transform / commit
   ladder" is presented as their line; my recollection of that paper's dimensions does not include
   "commit." If the ladder is the authors' synthesis over Hancock et al. and Kellogg et al., say so.
4. **Missing references** implied by the majors: Schneider & Wagemann (2012), Schneider & Rohlfing
   (2013), Ragin & Becker (1992), Greckhamer, Furnari, Fiss & Aguilera (2018).
5. **Landing-line drumbeat in section 3.** Each of the five results exits on an aphorism ("Connection
   is not constitution." "A rotation binds." "...has to be computed."). Any two of these are strong;
   five in sequence become a metronome. Let one or two results end on the mechanism instead.
6. **Campbell & Fiss (2026) is cited as in press**; confirm final details at proof stage.
7. Section 6's table omits a QCA row by design (QCA is the complement, not a neighbour). The design is
   right; a half-sentence saying the omission is deliberate would pre-empt the reader who goes looking.

## Bottom line

The essay does something this section asked for and few submissions will attempt: it imports a formal
core from a distant discipline, translates it with care, and generates concepts — computed boundaries,
graded membership, dissolution operators, necessary versus contingent irreducibility — that
configurational theorizing can use in words even if it never computes a Φ. Its treatment of QCA is
fair and its complementarity framing is correct; nothing here misrepresents conjunctural causation,
and the within-case/across-case division of labour is genuine. What stands between this draft and
publication is discipline of the kind our own tradition had to learn: the novelty claim must be
narrowed against set-theoretic within-case research, the formalism must be pinned down (version,
state-dependence, partition scheme) before its theorems mean anything, the encoding problem needs a
calibration-grade protocol rather than a gesture, and the numbers need an apparatus a reader can
check. All of this is doable within the essay's existing architecture, which is why I recommend major
revisions rather than rejection. I would want to see this paper again.
