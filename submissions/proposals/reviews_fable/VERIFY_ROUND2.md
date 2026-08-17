# Round-2 adversarial verification — OT configurational manuscript (2026-07-09)

Verifier: adversarial pass over the round-2 revisions against `SYNTHESIS.md`, with
`q215_phi_family_robustness/FINDINGS.md` and `ot_configurational_nature_2027_supplement.md` as the
evidence base. Line numbers refer to `ot_configurational_nature_2027_manuscript.md` as of this pass.
Verdict scale: PASS / PARTIAL / FAIL.

Scoreboard: A PASS, B PASS, C PARTIAL, D PASS, E PASS, F PARTIAL, G PASS, H PASS, I PASS,
J five fresh findings (two substantive, three hygiene).

---

## A. §2 versioning paragraph — PASS

Targets synthesis item 1 (pin the formalism). The paragraph (lines 197–215) states the
operationalization and the triple:

> "Every verdict this essay reports uses one operationalization: IIT 4.0's system-level measure,
> computed exactly in the PyPhi toolbox (Mayner et al., 2018), each model evaluated at a stated
> state. A verdict is therefore a property of the triple (model, measure, state)"

and reports the q215 result without inflation:

> "Recomputing the headline forms under IIT 3.0 on identical models and states, every verdict of
> *binds* replicates, as do the factorings by disconnection or by an ignored party; the three subtle
> factorings — the interior quorum, the synchronized veto, the maximal wiring — do not, because
> IIT 3.0 registers residual structure there as positive Φ."

Checked against FINDINGS.md: binds-agreements (CTRL+, E1, E3, E4, E6), factor-agreements (CTRL−
disjoint dyads = disconnection, E7 dropped rider = ignored party), splits exactly E2/E5/E8. The
manuscript neither hides the 3/8 splits nor claims the subtle factorings replicate, and it gives the
reason for choosing 4.0 (a criterion needs zeros; the 4.0 partition family contains the
party-respecting cuts) that FINDINGS.md itself recommends. The 5/8 split is reported accurately.

Two residual press-points, neither a verdict-changer:

1. "Where this essay says *binds*, the claim is family-robust" (line 209). The tested "family" is two
   members — IIT 4.0 and IIT 3.0 under one partition scheme (`DIRECTED_BI`, per FINDINGS' scope
   note: "No claim about other members of the wider Φ family (stochastic measures, 2.0, geometric
   variants), other partition schemes for 3.0, or larger systems"). The sentence follows FINDINGS'
   own recommended wording, so this is faithful transcription, but a formalist reviewer (seat 06)
   knows the family is bigger. Cheap hedge: "robust across both formalizations tested (IIT 3.0 under
   directed bipartitions, and 4.0)".
2. The state policy that actually generates verdicts — sign of the maximum over reachable states —
   is stated in the supplement's Part A preamble, not in the manuscript. "Each model evaluated at a
   stated state" is true of the exhibits but a reviewer holding the supplement will ask why the
   maximizing state is the right state. One clause in §2 would close it.

## B. §3 worked model box — PASS

Targets synthesis item 9 (define the load-bearing terms; the editor's two-minute box). The box
(lines 230–239):

> "Take three elements, a worker W, a mediating system M, a counterpart C, each binary, updating
> simultaneously by fixed rules: W copies M's last state; M turns on when W and C were both on; C
> copies M's last state."

This is exactly the supplement's CTRL+ read-recipient triad under relabeling (E′ = M; M′ = E ∧ R;
R′ = M, with E=W, R=C). The stated verdict —

> "Φ is positive (2.0, exactly computed, at the state where all three are on) and the complex is
> all three elements"

— matches the supplement's E-table (state 111, IIT 4.0 Φ = 2.0000, fixed point 111 → 111; hand-check
of the update rules confirms the transition table). The three partitions named ({W | M, C},
{C | M, W}, {M | W, C}) each sever a constraint the rules actually carry: M's rule reads both W and
C, and both copy M. Internally consistent.

Definitions: "Call that arrangement *strict mediation*, and call M's update a *commit*: a
determination that reads both parties jointly and that both parties answer to next step" — both
terms now defined at the worked example, before their load-bearing uses in §4 (the 660-form set,
line 358), §5 (the design moves, line 432), and §7. Synthesis item 9 is answered.

Two notes, sub-verdict: (i) §2 uses "commits a determination" twice (lines 143, 181) before the
formal §3 definition; both uses carry an inline gloss, so this reads as ordinary English ahead of a
term of art, but moving one defining clause into §2's state-individuation sentence would be safer.
(ii) The supplement reports whole-system Φ only; the box's "the complex is all three elements" (a
subset-comparison claim) has no supplement table behind it.

## C. §3 quorum gloss — PARTIAL

Targets synthesis item 2, first half (the false "no single party is pivotal"). The new gloss
(lines 252–262) is correct as stated:

> "a voting theorist will rightly object that majority members are pivotal in the voting sense: in
> a two-of-three majority each member is decisive in a third of the orderings, and no member is a
> dummy. That is pivotality to the *outcome*. What the partition reads is sensitivity to
> *identity*: at an interior threshold the commit depends on how many parties are active, never on
> which"

Shapley–Shubik in a 2-of-3 majority game: each player pivotal in 2 of 6 orderings = 1/3; no dummies.
Both facts stated correctly, the outcome/identity distinction is the right repair, and the extremes
sentence ("under unanimity every party can individually veto, under any-one every party can
individually carry") is accurate. §6's game-theory row now carries the matching qualifier ("its
pivotality is identity sensitivity, not voting power, a distinction section 3 draws"). The false
claim in its original form is gone from §3.

But the false claim survives in §5. Line 422, the substitution operator:

> "The threshold moves off its extreme, pivotality goes to zero, and the whole factors."

At an interior threshold pivotality is not zero on either of the paper's own two readings. In the
outcome sense it is 1/3 (Shapley–Shubik) or 1/2 (Banzhaf). And in §4's own definition — "causal
pivotality, the sensitivity of the joint determination to that element's state" (line 362) — it is
also nonzero, because at a split state (one other on, one off) the third party's state decides the
commit. What goes to zero is identity-sensitivity: which party is which stops mattering. The
sentence reinstates, in compressed form, exactly the claim the panel refuted.

There is a second, quieter version of the same wobble: §3 says the criterion tracks
identity-sensitivity, not state-sensitivity; §4 defines pivotality as state-sensitivity; §5 uses
the bare word. One word, two defined meanings, and the quorum is the case where they diverge.

Exact fix: line 422 → "The threshold moves off its extreme, identity-sensitivity goes to zero —
the commit still counts the parties but no longer distinguishes them — and the whole factors."
Optionally, one clause in §4 noting that its pivotality measure and §3's identity-sensitivity
coincide on strict-mediation forms but come apart on symmetric thresholds.

## D. §3 face-validity paragraph — PASS

Targets synthesis item 4 (criterion condemns good design). Lines 264–270:

> "Organizations build interior thresholds on purpose: majority rule, redundancy, slack are
> designed so that no individual is indispensable, and that is robustness, not failure. Φ of zero
> at an interior threshold does not condemn the design; it classifies it. The criterion measures
> constitution, not merit, and the two run orthogonally: a robust aggregate is often exactly what a
> designer should want, and a tightly constituted whole is also a fragile one, as section 5's
> asymmetry makes precise."

This is the reframe the synthesis asked for, stated in the paper's own voice, and it does the extra
work of connecting constitution-as-fragility forward to §5, which turns the defensive paragraph
into a load-bearing one. The panel's named authorities (Landau on redundancy, Cyert & March on
slack) are not cited; the argument stands without them, but adding Landau (1969) would cost one
line and pre-empt seat 03.

## E. §3 Thompson paragraph — PASS

Targets synthesis item 5 (credit the ancestors), Thompson half. Lines 319–327:

> "Thompson (1967) did not just note interdependence; he ordered it within the single arrangement
> (pooled, sequential, reciprocal), which makes his typology a within-case account of how jointly a
> set of parts determines, the closest thing the classical canon has to the criterion itself."

The mapping is accurate to the standard reading: pooled = discrete contributions to a common whole,
parts substitutable (the manuscript's "contributions summed with each part substitutable" →
interior-threshold quorum, factors); reciprocal = outputs of each become inputs of the others,
most intensely interdependent ("Reciprocal interdependence binds, as Thompson said" — Thompson said
most interdependent, not "binds," but the attribution is to his ordering, which is fair). The cycle
as the ordering's limit — "a purely sequential chain, closed into a cycle, binds too: full
constitution without a single reciprocal pair, a case the verbal typology has no slot for" — is
defensible: Thompson's reciprocal is illustrated pairwise (maintenance/operations), and a 4-cycle
of copyists contains no mutually adjusting pair. A Thompson loyalist could reply that a closed loop
is reciprocal at the system level ("each poses contingency for the others"), so "no slot" is
arguable rather than settled; but it is an interpretive claim, not a misattribution, and the
paragraph gives Thompson priority explicitly ("The criterion is not the first within-case ordering
of joint determination; it is the first with a decision procedure attached"). Simon–Ando and
community detection get their credit in §2 (lines 152–160) with the correct realized-vs-
counterfactual distinction; Doty–Glick–Huber get theirs in §7 (line 622); Schneider & Rohlfing in
§6 (line 527). Item 5 is answered across the four sites.

## F. §4 Shapley reframe — PARTIAL

Targets synthesis item 2, second half (near-circular convergence). The §4 body is fixed cleanly
(lines 381–397). Characteristic function: defined —

> "Define an integration game on the configuration's elements: the worth of a coalition is the
> integration of the sub-arrangement it induces (the empty coalition worth zero)"

Circularity: conceded in terms —

> "This is a translation, not an independent confirmation. The game's worth function is built from
> Φ, so Shapley-graded pivotality predicting complex membership shows that one formalism's
> decomposition tracks its own boundary concept, a coherence result inside the borrowed apparatus
> rather than two disciplines agreeing from different starting points."

And §6 matches (lines 548–554): "its agreement is internal coherence of the borrowed apparatus,
translated into a notation organization theorists already read, not a second discipline arriving at
the same verdict unprompted." The efficiency claim ("the values decompose the whole exactly (they
sum to its Φ)") is the Shapley efficiency axiom applied to v(N) = Φ, correct. The two-thirds/
one-sixth split checks out against the lab's own computations (q131: values 0.333/1.333/0.333 on
Φ = 2.000; q149 replicates), so the arithmetic is sound — though see J.3 on where a reader can
verify it.

What keeps this at PARTIAL: the abstract still sells the convergence the body retracted. Lines
21–22:

> "The same verdict recurs across four other literatures in different vocabularies, one
> correspondence with computation behind it."

The four "other literatures" include cooperative game theory. For that row, "the same verdict
recurs" is precisely the two-formalisms-agreeing reading §6 now disavows — the verdict does not
recur there; it is decomposed there. And "one correspondence with computation behind it" is the
phrase the synthesis flagged as the retained circularity target. A reviewer who reads abstracts
against conclusions (seat 08 does) will quote these two sentences at each other.

Exact fix, abstract: "The same verdict recurs across four other literatures in different
vocabularies — one of them an exact decomposition of the criterion's own quantity, the others
structural correspondences exhibited on the models." Or drop the game-theory row from the
recurrence count and say "three other literatures, plus a translation into cooperative game
theory."

Minor press-point, not scored: §4's "the Null Player axiom transfers... which is the
substitutability collapse in game-theoretic dress" is an axiom statement, not a claim that quorum
parties are null players in the integration game — but the lab's own q149 found negative party
Shapley values in that game, so a careful reader may ask whether substitutable parties are null or
negative. One qualifying clause would forestall it.

## G. §4 "decidable relative to a stated encoding" — PASS

Targets synthesis item 3. Line 404:

> "Whether some actor is 'really part of' an institutional configuration is decidable relative to a
> stated encoding, and the analyst's discretion, which QCA exercises in the visible choice of
> conditions, moves here into the transition rules, a displacement section 7 prices (four of ten
> demonstration cases flip under defensible re-encoding) and turns into theory rather than
> concealing."

The qualifier is present, the 4/10 figure is priced into the same sentence, and the same figure
appears consistently in §2 (lines 184–187) and §7 (lines 590–592). Grep confirms no other
occurrence of "decidable" or "definite truth value" in the manuscript. The editor's constructive
turn — encoding-as-contestation as a theme-2 power point — is delivered in §7 (lines 598–604: "a
platform that gets its coordination encoded as pairwise contracts has factored itself out of
accountability for the whole, before any computation runs"), which is the strongest new paragraph
in the revision. Language reconciled; no overclaim found. The remaining exposure is evidential,
not linguistic — the 4/10 cases themselves are a supplement IOU — and is scored under J.2.

## H. §5 leakage fix — PASS

Targets synthesis item 7. Three checks:

1. Multihoming: gone. Grep finds no "multihoming"/"multi-homing" anywhere in the manuscript. The
   routing-around concept is now named correctly (lines 458–461):

   > "platform research studies the counterfactual directly as disintermediation or leakage:
   > parties who meet through the platform taking the relationship off it, which platforms fight
   > with contractual and design constraint (Gu & Zhu, 2021; Cutolo & Kenney, 2021)."

   That is Gu & Zhu's actual object (disintermediation in an online freelance marketplace), used
   for what it found.
2. Kellogg §2: now cited for opacity (lines 140–142: "the generating mechanism is typically opaque
   to the parties and the researcher alike (Kellogg et al., 2020; Rahman, 2021)") — their actual
   terrain — and the application-layer bet is stated as the paper's own wager against that opacity,
   with the failure condition named ("The bet fails exactly where committed determinations
   themselves are hidden"). The citation-integrity problem is repaired.
3. Power beyond forbidden ties: the scope limit is explicit (lines 503–510: "where the hold is
   opacity or a reputation that cannot be carried out the door, there is no single tie to restore,
   and the counterfactual generalizes to lifting a bundle of constraints at stated costs, work the
   agenda takes up rather than work this essay completes"). This is the extension-or-scope-limit
   the synthesis demanded, taken as scope limit.

Two residues a platform reviewer could still poke, neither breaking: Hagiu & Wright (2015), named
in the synthesis as the second leakage source and nearest rival, is still unengaged and uncited;
and §6's platform row (line 544) lists "disintermediation / single-homing" as the native test —
defensible under Armstrong's competitive-bottleneck logic (the row cites Armstrong 2006), but
"single-homing" sits close enough to the old homing/leakage conflation that swapping it for
"disintermediation / leakage" would be safer.

## I. §5 catalog honesty — PASS

Targets synthesis item 6, catalog half. The acknowledgment is in the manuscript's own voice (lines
475–478):

> "the catalog was coded by the same hands that knew the outcomes, so the exercise disciplines the
> distinction rather than testing it. So weighed, the pattern still instructs."

"Retrodictive traction" is gone; the claim is now "consistent with the historical record," with the
blind-coding test explicitly deferred ("A predictive test would code arrangements blind and wait,
which is the agenda's business, not this essay's"). Numbers check against supplement Part B:
necessary = 13/51 (25.5%) = "about a quarter"; contingent = 25/51 (49%) = "about half"; the named
exemplars match the catalog (clearinghouse_ccp, stock_exchange, escrow_conditional under necessary;
franchise law, walled garden, exclusive contracts, network standard, search friction under
contingent constraint types; newspaper_classifieds and retail_middleman_dtc as the internet-era
dissolutions, correctly described as unconstrained rather than contingent). The catalog list and
coding rules the synthesis asked for are in the supplement. Consistent — but see J.4 for what the
supplement's Part B construction hands a hostile reviewer.

## J. New errors — five findings

**J.1 (substantive; also scored under C). §5 line 422, "pivotality goes to zero."** False on both of
the paper's own definitions at an interior threshold (Shapley–Shubik 1/3; §4's state-sensitivity
nonzero at split states). The one surviving instance of the refuted claim. Fix given under C.

**J.2 (substantive). §7's supplement description overclaims what the supplement contains.** Line
594–595: "the online supplement gives every exhibit's full transition table, its per-state Φ under
both measures, and the catalog's coding rules." Part A covers exactly the ten q215 forms (eight
exhibits, two controls). Missing entirely: the §4 owner-outside-the-complex four-node model, the §4
coalition/holistic-ceiling case (the exhibit the synthesis's item 8 fix rests on), the §5 five
design moves, the §7 ride-hail vs partial-mediation pair, the 660-form enumeration behind the
membership law and its four-in-ten/nine-in-ten figures, the Shapley decomposition behind the
two-thirds/one-sixth split, and the §3 "order of a tenth of the class" census. Part C is an IOU in
so many words ("will be included in the submission package"), so the 4/10 flip figure — cited three
times — is not yet rebuildable by a reader. The manuscript's preamble ("Every number cited as an
illustration is exactly computed and reproduces from the model's stated encoding") is true of the
lab (the Shapley split verifies against q131/q149; the catalog regenerates), but a reviewer holding
only manuscript + supplement can test the §7 sentence and watch it fail. Fix: either extend the
supplement (the encodings exist in the lab tree) or scope the §7 sentence to what Part A/B deliver
and mark Part C's status in the manuscript.

**J.3 (hygiene). The 51/51 pre-registration agreement in Part B is true by construction.** The
margin column is constant per template (relay 2.000, additive 1.585, conjunctive and free 0.000)
and class maps one-to-one onto template, so the computed class is a function of the hand-coded
template, and "Entries whose computed class differs from the pre-registered expectation: none" is
guaranteed before any computation runs. Coupled with "pre-registered prediction, fixed before
classification ran" two sentences after "outcomes were known to the coders," this invites the
hostile seat to call the agreement vacuous and re-raise item 8 (Φ adds nothing over the coding).
The manuscript's own framing ("disciplines the distinction rather than testing it") is the right
one; the supplement should drop "pre-registered," state that expected and class are linked through
the template by construction, and let the four-template margins stand as what they are — the
calculus's prices for the four structural positions, not fifty-one independent predictions.

**J.4 (hygiene). The general k-of-n quorum law rests on n = 3 evidence in the supplement.** §3
claims "the quorum system is irreducible at exactly two thresholds, unanimity (k = n) and any-one
(k = 1), and factors at every interior threshold... the collapse admits no gradient" (lines
248–251). At n = 3 there is exactly one interior threshold, so "every interior threshold" and "no
gradient" are exhibited by a single point. If the lab has the n ≥ 4 sweep, one supplement row
settles it; if not, scope the sentence to the computed case.

**J.5 (hygiene). State-policy asymmetry between manuscript and supplement.** The supplement states
the verdict rule ("verdicts in the manuscript are the sign of the maximum over reachable states");
the manuscript says only "each model evaluated at a stated state" (§2). The worked triad makes the
gap visible: under 4.0 its Φ is 0.0 at three of four reachable states and 2.0 at the fourth, and
the manuscript's verdict is *binds*. Defensible (the synthesis asked for a state policy; one
exists) but it lives in the wrong document. One clause in §2 — "a form binds when some reachable
state is irreducible" — closes it.

No arithmetic errors found: the 2.0/two-thirds/one-sixth triangle is internally consistent
(0.333 + 1.333 + 0.333 = 2.0; shares 1/6 + 2/3 + 1/6 = 1) and matches the lab record; the 13/25 of
51 fractions match Part B; the q215 numbers are transcribed without error; the worked box's
transition claims reproduce by hand from the stated rules.

---

## Bottom line

Seven of nine targeted fixes hold under adversarial reading, several (the §7 encoding-power
paragraph, the face-validity paragraph, the strict-mediation box) stronger than the synthesis asked
for. Two are incomplete rather than wrong: one sentence in §5 reinstates the refuted pivotality
claim, and the abstract retains the convergence framing the body retracted. The genuinely new
exposure is J.2: the manuscript now promises a supplement that Part A/B only partly deliver, and
Part C is an IOU standing behind a number cited three times. All fixes are one-sentence to
one-table jobs; nothing found requires re-computation.
