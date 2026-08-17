# Manuscript notes

Decision log and parking lot. Newest entries at the top.

## 2026-08-17 — the mechanical pass, and where it belonged

The copyeditor's finding was that 120 of 124 reference titles were in Title Case where Intellect
Harvard is sentence case, confirmed against both worked examples in `JOURNAL_SPEC.md`. The fix went
into `render_refs.py` rather than into `references.bib`, because the spec says the bibliography is
stored in an APA-ish shape and rendered into house style; sentence case is a rendering decision and
belongs with the renderer.

**Hand review earned its keep.** A first pass down-cased 740 distinct words and I checked the list
rather than trusting it. Eight false positives: Derrida, Le Petit Chef, Belgium, Kiwi, Kingdom's,
Macromarketing, 7Es and Mr. Roboto. Two were structural rather than lexical — possessives escaped
the protected-word lookup, and alphanumeric names like 7Es were not recognized as names at all. Both
fixed, plus the specific names added to the protected set. Second pass: no false positives.

Also into the renderer, so they cannot regress: `pp.` no longer precedes a bare article number
(twelve entries; an article number is not an extent); two or more editors take `eds` rather than
`ed.`; nested single quotes inside a single-quoted title become double, per the Notes; LaTeX `--`,
the stray en-dash-plus-hyphen and hyphenated volume ranges are normalized; and the sort folds
diacritics so Möhlmann files under M instead of after Z.

Three bugs of my own on the way, all caught by checking the output rather than the code: a regex
replacement string cannot carry `\u` escapes, a heredoc doubled the backslashes so the volume-range
pattern matched nothing, and `unicodedata` was imported inside a function so it was not in scope at
the sort. The lesson is the same each time — verify the artifact, not the edit.

**Body fixes.** One American spelling (`toward` → `towards`, the odd one out against four
`towards`). The generic guest is `she` throughout; one sentence said `they` and one `their` inverted
its own meaning, both repaired. One object had three names — design *features*, *principles*,
*affordances*, and *practical* versus *diagnostic* questions — now uniformly *features* and
*diagnostic*, matching the heading and the abstract. The three direct quotations now take single
marks per the Notes.

**Not done, deliberately: page locators for the three quotations.** The Notes require them and I do
not have verified page numbers; two of the three were verified from publisher abstracts, which carry
none. Inventing one is the exact failure this project has twice caught in its own citations. The
author supplies them or the quotations become paraphrase.

**Measured after.** Body 6,525. Sentence mean 19.6 against Pierre's 20.2, paragraph mean 120.9
against 123, zero em-dashes, two authorial first persons, zero double quotes in the body, zero
occurrences of the journal name outside the reference entries, 152 citations all resolving, 124
entries, zero alphabetical breaks.

**Still open.** The front matter, where the editor found the abstract at 199 of 200 words with an
undischarged clause, a systematically wrong section map in `RESPONSE_TO_EDITOR.md`, and the seven
mandatory components not yet in the file. Tier 3 of the synthesis. And the reference-counting
ruling, which `JOURNAL_SPEC.md` still contradicts.

## 2026-08-17 — eight-reviewer panel, then Tier 1 and Tier 2 applied

Panel and synthesis in `reviews/2026-08-17/`. Six minor, one major at the light end, one
mechanics-only. **No reviewer attacked the argument.** Every finding was a source read too thinly, a
claim scoped too widely, or an internal inconsistency.

**Two claims that could have been killed both survived verification.** Nothing published asks
whether a system taking the host's functions inherits the host's obligations, so the novelty claim
holds. Section 7's absence claim holds on all four named works, including Mameli et al., whose
open-access full text a reviewer read: 'friction' never occurs, 'seamless' occurs once and
affirmatively.

**Checks run before writing.** Germann Molz 2026 confirmed: the phrase 'guests without hosts' was
coined for the *blurring* of hosting and guesting, and her 2026 article extends it to extractive
algorithmic governance and to the replacement of human workers by robots and AI. Section 1 had
reported only the extension. Sharma and Mattila confirmed as the nearest neighbour, arguing rights
and responsibilities through stakeholder theory and recommending firms decide which employee duties
shift to the machine. Bovens's core definition confirmed — actor and forum, obligation to explain
and justify, forum can question and judge, consequences may follow.

**Tier 1, correctness.** Section 2 no longer cites Spektor for a front-desk claim; it is a
housekeeping study whose room assignment allocates rooms *to housekeepers*, and section 3 already
said so, so the paper had contradicted itself forty lines apart. Zhou's remediating dimension is now
described by its validated items rather than by an interview exemplar, which strengthens the point:
every validated item locates the remedy in the worker and most route around the institution. 'The
first validated scale' became 'a validated scale'. Sharma and Mattila differentiated on the right
axis. Section 4's rule made accountability the necessary condition, since 'all three withheld at
once' had ruled out the paper's own transparent-but-substitutive case. The guest-to-host instrument
absence narrowed to obligation. The smoothness claim scoped to this field. Garcia reconciled across
sections 3 and 4. Padigar corrected to 2025.

**Anonymity.** Three leaks removed: the venue line and drafting note at the head of the file, and a
sentence in section 1 naming the journal. The six remaining occurrences are reference entries.

**Tier 2, the spine.** Section 3's duty paragraph rebuilt, composing three reviewers' findings.
Furtado: the uniqueness claim was false and its counterexample sat one clause earlier, since
fiduciary duty is the standard case of an obligation constituting its bearer's role — so the claim
now runs on bare presence and on ownership rather than performance. Ellery: 'owed simply because
someone has arrived' imported unconditional hospitality into a commercial setting, so the paragraph
now carries the tradition's own distinction, conditional at admission and unconditional in
reception, which states the thesis more sharply than the original did. Reviewer 2: section 1's
promise was discharged by assertion, so the argument is now made — a system can perform a welcome
and cannot stand in a forum to answer for one. Kropf moved from friend to adversary and is answered
from his own limit.

Also: Bulley restored to the post-threshold argument he actually makes, rather than the
threshold-moment reading he wrote to argue against; Belanche inserted, retiring the only reference
cited nowhere and supplying the paper's best empirical corroboration; hospitality algorithmacy and
coordinative sovereignty named in section 5, which the abstract had promised and the body never
delivered; and the title's question answered in section 9.

**Measured after.** Body 6,525 against a 6,000 floor. Sentence mean 19.6 against Pierre's 20.2,
paragraph mean 120.8 against 123, zero em-dashes, two authorial first persons, 152 in-text citations
all resolving, no new references added — the absence claims were narrowed rather than answered with
sources that would have needed verification and cards.

**Still open.** Tier 3 in the synthesis, the copyeditor's mechanical pass (120 reference titles need
sentence case, by hand), the front matter defects the editor found, and the reference-counting
ruling that `JOURNAL_SPEC.md` still contradicts.

## 2026-08-15 — second slop pass, after Roger caught what the first one missed

Roger flagged the §6 opener the first pass had itself written: "Design guidance in this area has
to contend with a genuine disagreement, and the disagreement runs through the special issue's own
editorial team." The first pass hunted the taxonomy's named patterns and missed a whole class:
personified abstractions doing throat-clearing ("design guidance has to contend", "the well-being
question deserves particular attention", "the phygital character is worth emphasizing", "the
limits should be stated plainly", "it is worth being precise"), announcer clefts ("what is
striking is"), and decorative intensifiers ("genuine disagreement"). Eleven more rewrites, all in
buildout additions, each replaced by Pierre's pattern: the sentence's subject is the actual actor
and the first clause states the claim. "Researchers disagree about whether guests should see the
technology at all." "These encounters are phygital in a precise sense." "These distinctions bear
directly on well-being."

The same sweep caught something worse than style: four sentences named "the special issue", its
editors, or the paper's positioning inside manuscript prose — outline-speak leaked into the paper,
and a double-blind submission cannot say "the special issue's own editorial team" or "one of this
field's own editors". All four removed; the citations stay and the frame goes. A grep for
special-issue and editor language is now part of any future pass, alongside the taxonomy.

Body after both passes: 5,785 words with citations.

## 2026-08-15 — the slop pass: every sentence checked against the exemplars and Pierre's voice

Sentence-by-sentence review of DRAFT.md against three benchmarks: the measured H&S register in
REGISTER.md (Lugosi 2021 and Lynch et al. 2021, both measured from retrieved full texts), Pierre's
rewrite as the voice standard, and the project's slop taxonomy. Recent issues are paywalled, so
the 2021 measurements stand as the venue benchmark. Rule applied throughout: Pierre's sentences
are presumed clean and stay; the buildout additions get full scrutiny, since imitation prose is
where slop lives.

Twenty changes, all to buildout additions, logged here so any call can be reversed:

*Em-dashes, all four removed.* The scoring-system appositive (§4), the categories list (§7), the
no-record list (§7), and the gains list (§8) all restructured into commas or subordinate clauses.

*Staccato verdict pairs, all dissolved.* "It does not claim X. It claims Y" (§7) folded into one
colon sentence. "That is not a property of the worker at all. It is a property of the institution"
(§5) folded into a since-clause. "Do not merely automate a task. They remove the person" (§5)
folded. "Is not a matter of X. It is a matter of Y" (§8 human-centricity) rebuilt without the
frame. "The frameworks describe this as fluidity. It can be described as a relay" (§3) merged.

*Tidy triads loosened.* "A room key that works or does not, a queue that moves or holds, a price
that appears" cut to two items (§3). "In responsiveness, in consistency, in what a small team can
offer" cut to two (§8). "Her history, her record, or her profile" cut to two (§4). The
first-time-user list rebuilt as a whether-clause (§7). Kept: the duty lists in §3 and the
criteria, which are definitional rather than decorative.

*Announcer clauses cut.* "The pattern across these duty vocabularies is instructive" → "Set side
by side, these duty vocabularies share a structure" (§3). "Uneven in an instructive way" → "uneven"
(§3). Both parenthetical "(Table N summarizes...)" asides converted to plain sentences.

*Not-X-but-Y constructions removed from additions.* "Not a person as such, but a party with the
power" → "someone with the power to change the answer" (§6). "Not foreign to the literature" →
"comes close to these ideas" (§2). "Rather than" trimmed where mine and argumentative (Hemmer
sentence rebuilt with a semicolon); left where Pierre's own or a plain comparative.

*Verdict-snap tails cut.* "Whatever the interface looks like" → "however similar the two
interfaces may look" (§4). "That difference matters once..." softened into a which-clause (§2).

*Repetition fixed.* Three consecutive sentences opening on "That work / This paper / This paper"
in §1 rebroken; "What it did not do, and what this paper attempts" (§2) converted to declarative.

Measured after the pass: 5,875 body words; sentence mean 20.2 (Pierre's own mean — shorter than
the 2021 exemplars' 26–30, and his readability governs per Roger's instruction); paragraph mean
123 against Lugosi's 129; zero em-dashes; zero rhetorical questions in running prose (the §4
five-questions sentence is a genuine enumerated diagnostic immediately formatted as Table 1, the
form Lugosi's display questions license); exactly one authorial first person ("we need to know",
§1), matching the spend-it-once rule; no bold in running text; citations parenthetical throughout.

## 2026-08-14 — the buildout executed: DRAFT.md at 5,916 words in Pierre's voice

The BUILDOUT.md plan executed against Pierre's 6,000-word target. Body now 5,916 with citations
(5,471 prose), 124 references rendered, every in-text citation machine-checked against the
rendered list, no LaTeX residue. Pierre's sentences stand unchanged throughout; every extension is
written in his register — explanatory, hedged where the evidence hedges, signposted.

What went in, by section. §1: the Germann Molz differentiation ("guests without hosts" quoted; her
question asked, then the question that follows from it). §2: the criteria couched in the
experience tradition (Batat 2019); the two narrowed absences stated precisely (Manfreda and
Harkison; Shi et al.); the platform-hospitality lineage paragraph (Cheng and Foley; Roelofsen and
Minca; Germann Molz 2018; Edelman; Cui). §3: the dual-place relay paragraph (the editor's
physicalization/digitalization ask, answered with "who holds authority at each handover"); the
nearest-miss paragraph (Liu; Lee and Lu; Sharma and Mattila) closing on the duty pattern (care for
need, fiduciary for trust, governance for risk, welcome for arrival) and Introna's unreversed
machine-as-guest; the split verdict on discretion. §4: Table 1; the Garcia pricing vignette and
the Batat AR augmentative case; the threshold confirm-against-score paragraph. §5: the Zhou
differentiation argued (the scale measures the person, the appeal's answer is a property of the
institution); the lending paragraph extended with its two fragilities; the untested interaction
stated with Lin et al. 2026 as the near-miss proof. §6: the Mosca-against-Mosca opening; the Choi
and Chao complication folded into the authority reading; the shadow-work expansion of
bypass-ability. §7: the narrowing paragraph with two verbatim Batat goal-statements and Mameli as
the currency check; the cultural-scripting expansion; the remedy-complication paragraph (Cui;
Filippas). §8: the human-centricity throughline; the well-being paragraph restructured to open in
the editors' architecture (Batat 2022 TLR; De Vos 2024 valences) with the three absence carriers;
the gains paragraph; Table 2; the limits paragraph with three empirical directions. §9 untouched.

Remaining before submission, unchanged: PHIVE and Germann Molz full texts gate §7 and §1 final
wording; AGENDA 43 (Roger) and 1b/19/31 (Pierre); front matter refresh against this draft;
Phase 4 reads.

## 2026-08-14 — Pierre's rewrite is the governing voice; DRAFT.md is the citation pass on it

Pierre rewrote the section brief into readable prose and sent it back with "just need the language
to be a little more readable" and "I think we are approaching the point where we can do a full
buildout." Roger's instruction: do not veer from this writing style. That supersedes the measured
Lugosi register in REGISTER.md wherever the two disagree. The differences are real: Pierre
explains where the brief asserted, hedges where it ruled ("may", "can", "tends to"), unpacks
compressed formulations into two sentences, and keeps the signposting the brief deleted ("This
distinction exposes...", "There is, however, a limit..."). His formulations of the key beats are
now canonical — "somebody still owes the guest a welcome" kept; "a place where frustration is
deposited" for the authority-less employee; "some problems require people to become more capable;
others require institutions to become more answerable" as the division's statement.

DRAFT.md is his text verbatim plus citations and nothing else — every insertion is a parenthesis,
104 references rendered at the foot from `cited_keys_draft.txt`. One new sentence only, in §3,
carrying the Casalegno/Civera/Mosca/Freeman warrant, flagged for Pierre since it is the one place
the text is not his. Citation choices worth recording: PHIVE not cited (metadata-only, nothing may
be attributed); Dar volume not cited (same rule; Moganadas and Park carry the §8 absence); one
Batat 2022 and one Batat 2024 cited (TLR and PH-CX) so the list needs no a/b disambiguation;
spektor2023designing carries the §2 front-desk sentence, not the duplicate-named spektor2023;
Keegan and Krzywdzinski excluded until publisher-verified. Ehsan/seamful XAI turned out to be a
card with no bib entry — the same defect Germann Molz had — fixed in the same pass.

The full buildout now means: expand DRAFT.md section by section in Pierre's voice, pulling
argument detail from OUTLINE.md and sources from the library, with the nine P9 repairs applied in
the expansion rather than patched afterwards.

## 2026-08-11 — the P9 sources landed in the bibliography, and the card library was found stale

Three defects fixed, one of them not the one we set out to fix.

**One. The P9 sources are in `references.bib`.** Sixty-one new entries, taking the file from 172 to
234, each with a verification date and read depth, and each with a card in `library/cards/`. Until
this ran, the forty-plus sources annotated in `literature/LIBRARY.md` could not have rendered.

**Two. Germann Molz was never in the bibliography.** The card was written on 8 August and flagged
`must-engage`; the source itself was never added, so even a manuscript that engaged her could not
have cited her. Now added, and the card's hold rationale rewritten to point at the outline's plan
rather than at an open displacement question.

**Three, unplanned and larger. The card library had gone stale and nobody knew.** Running the CI
gate for the first time in three days returned 101 errors, none of them from the sixty-one new
cards. Diagnosis by DOI rather than by name: nine citekeys had been renamed without the cards
following, six of those the year corrections this project made during its own verification sweeps —
Lv 2025 to 2024, Nguyen 2025 to 2024, Padigar 2025 to 2024, Pedersen 2023 to 2022, Wang 2025 to
2024, Xu 2021 to 2020. Sixteen cards said held, rejected or superseded for sources the manuscript
now cites. Three were orphans asserting cited status for sources in neither the bibliography nor the
manuscript. All are fixed, with a dated stamp on every corrected card saying the prose beneath the
frontmatter predates the correction.

Fifty-four errors remain and they are all one kind: a source the manuscript cites that has no card.
That is the backlog, it is listed in `CARDS_INDEX.md`, and most of the content for it already exists
in prose in `literature/LIBRARY.md`. It is not fixed and should not be fixed by generating
annotations nobody has verified.

**The lesson, which is the same one the library README already recorded.** State a human has to
remember to update is state that goes wrong silently. The card library was built on 8 August
precisely because two research rounds had skipped their update step, and then the manuscript moved
for three days while the library stood still. The P9 pass rediscovered Germann Molz from scratch
because it searched the literature instead of reading the project's own must-engage flag. Running
`build_index.py --check` before a research pass, not after, would have saved that.

## 2026-08-11 — library restructured on the editor spine, outline rebuilt on the abstract

Two changes, both structural.

**LIBRARY.md cluster 1 is no longer "the phygital frameworks and the editors' corpus," discharged
early as a positioning obligation.** It is now "The special issue's editors — the paper's spine,"
organized by editor (1a Batat, 1b Mosca, 1c De Vos, 1d the adjacent field the paper argues past), and
it names the three relations the paper uses: warrant, nearest approach, live objection. Twenty-one
editor entries with the standard three annotations, most of them new from P9. Forty-plus P9 sources
were also annotated into clusters 2 through 13. Standing caveat recorded in the header: none of them
is in `references.bib` yet, so none can render, and adding them is the next mechanical job.

**OUTLINE.md is rebuilt on Pierre's abstract as its organizing device.** Every section now opens with
the abstract sentences it discharges, quoted. The correspondence turned out to be near-exact —
abstract ¶1 splits across §1 and §2, ¶2 is §3, ¶3 is §4 and §5, ¶4 is §6 and §7, ¶5 is §8 and §9 —
so the outline is now readable as a demonstration that the paper delivers the blessed text rather
than a paper adjacent to it. Under each section heading, three lines: the abstract commitment, the
editor spine that carries it, the general literature that professionalizes it. The order is fixed
throughout: Pierre's claim, the editors, the field.

The editor spine is load-bearing rather than decorative, and the test is that removing it would cost
the paper real arguments. §2's five criteria now arrive through Batat's *consideration* and the 7Es
before Derrida. §3's redistribution premise is Casalegno, Civera, Mosca and Freeman rather than an
assertion. §4's distinction is couched in Mosca and Civera's residual-against-integrated CSR. §5's
accountability paragraph names what Civera, Mosca, Casalegno and Maple lack — the forum. §6 opens on
Mosca and La Rosa recommending concealment and settles it with Mosca 2026 and De Vos et al. 2026.
§7's target is stated with three primary Batat quotations. §8's well-being levels are Batat's TLR and
its valences are De Vos's enchantment typology. Nine sections, three editors, every claim placed at
home before it goes abroad.

## 2026-08-11 — P9: the editor-grounding and final-corner pass, and the outline rebuilt on it

Eight refutation-default units in parallel: Batat's full corpus; Mosca and De Vos corpora; a complete
*Hospitality & Society* sweep; the scoop-and-adversary hunt against both uncontested moves; and
corner sweeps for §4, §5, §6/§7 and §2/§8. Written up in
[`../literature/P9_FINDINGS.md`](../literature/P9_FINDINGS.md).

**The pass's largest finding.** Germann Molz (2026), 'Guests without hosts: On the digital
biopolitics of network hospitality', *H&S* 16:1, 63–82. Same journal, five months before the
submission window, by the author of the journal's founding network-hospitality line, on algorithmic
governance producing hostless hospitality. Riordan 2024 is no longer the journal's nearest
engagement and the sentences saying so are now wrong. The paper survives on differentiation and is
better for it: she asks what becomes of hospitality when the host is erased, and this paper asks
whether the successor inherits the obligation. Her title poses a question this paper answers.
Engagement belongs in §1 and §3, not a footnote.

**Both uncontested moves survive, both narrowed.** The host question took four wounds (Lee and Lu
2024 attributional; Sharma and Mattila 2025 governance; Liu et al. 2026 experiential; Germann Molz
2026 biopolitical) and no kill — nobody theorizes the algorithmic party as occupying a position that
owes. The seamlessness critique narrows to the value itself, because Batat has now published her own
dark-side work (PHIVE 2026 on the good, the bad and the ugly of AI marketing; binge delivery 2025 on
phygital vulnerability) and Weaver 2025 criticizes fast hospitality in this journal. Narrowing
improves it: everything around smoothness has been questioned; smoothness has not.

**Two §2 absences had to be narrowed or they were false.** Manfreda and Harkison 2025 theorize
reciprocal hospitableness in commercial luxury lodges, with concrete guest-side behaviours, framed as
gratitude rather than obligation — so the claim narrows to what the guest *owes*. Shi et al. 2025
validate a scale measuring what residents gain from tourist interaction — so the instrument claim
narrows to guest conduct toward a commercial host, and must exclude the customer-incivility
tradition. The §8 absence held under exhaustive search, and now carries three citations instead of
an assertion.

**Two collisions to cite and differentiate.** Zhou et al. 2025 published the first validated
algorithmic-competency scale (understanding, embracing, leveraging, remediating); their remediating
dimension folds appeal capacity into individual competency, which is the exact conflation §5 exists
to undo, so the collision motivates coordinative sovereignty. Hemmer et al. 2025 published a
checkable condition for human-AI complementarity; it is an ex-post performance test on internal
decision tasks with no place for answerability to an outsider.

**The architecture Roger asked for, now applied.** OUTLINE.md rewritten so every section moves
through three layers in order: the claim in Pierre's vocabulary, couched in the editors' own
scholarship, then professionalized by the general literatures. The editor layer is real, not
decorative — Batat's TLR carries §8's two-level well-being structure and her 7Es scaffold §2's five
criteria; Casalegno, Civera, Mosca and Freeman 2020 supply §3's redistribution premise; Mosca and La
Rosa 2019 recommending that technology be *concealed* becomes the opening objection of §6's
transparency paragraph, answered by Mosca 2026 endorsing transparency and oversight and by De Vos et
al. 2026 on obscured purpose producing resistance. The editors disagree with each other and the
affordance settles it.

## 2026-08-11 — OUTLINE.md rebuilt against the finished research programme

Complete replacement of the outline, superseding the pre-audit version. Now paragraph-by-paragraph
for all nine sections with measured word counts from the current draft (§1: 1,078w/6¶; §2:
1,169w/7¶; §3: 1,692w/9¶; §4: 911w/4¶ + Table 1; §5: 1,311w/6¶; §6: 877w/5¶; §7: 1,101w/5¶; §8:
962w/5¶ + Table 2; §9: 96w/1¶; body total 9,197w against the 6,850 budget). Each paragraph carries
its argumentative move and citation anchors, post-audit wording throughout (Lind/Folger voice
repair, Bayamlıoğlu, counterparty formulation, P8 compounding calibration). Closes with the
back-matter block (pointer to FRONT_MATTER.md) and a "What still gates submission" table (AGENDA
43 for Roger; 19/1b/31 for Pierre; library errands 50; the trim checked against CLAIMS.md; Phase 4
reads). Committed to device same day.

## 2026-08-11 — full-text verification review against the library

Every claim-bearing sentence in the introduction and manuscript checked against the consolidated
library; every gap statement checked against the verified absences. Findings and fixes:

**Two claims stood stronger than the audit allows, in both §1 and the 5Cs introduction.** The
compression had preserved pre-audit wording: "the nearest approach" (Belanche) is now scoped to the
service literature, with machine ethics acknowledged as nearer still (Kropf now cited in the 5Cs
introduction, added to its references); and the bare counterparty claim ("nobody to negotiate
with") is now the audited version in both files — the guest keeps an addressee for complaint and
compensation and loses the party with authority over the rules. The 5Cs complication also carried
"the substitution has passed without remark," killed in §3 during the audit but surviving here;
reworded to the template formulation.

**One uncited legal claim now carries support.** §5's statement that data-protection law grants the
mediated party the right to express her view and contest the decision cites Bayamlıoğlu (2022),
verified in U5, added to bib and library.

**Gap statements all check out.** Five gap claims stand in the text and each maps to a verified
absence: no instrument measuring anything flowing from guest to host (P1); guest-facing algorithmic
hospitality thin and largely unstudied (U4, softened wording in place); no study modelling prior
voice climate under algorithmic management (P8); individual-level automation evidence and
collective-level well-being evidence unmet (P7); every affordance-to-outcome relationship a
proposition (P7/U7 — the Kim/Hou preference floor is preference evidence, not an affordance test,
so the claim holds as worded).

Manuscript now 127 cited references; introduction 27. Both reference lists re-rendered.

## 2026-08-11 — the library consolidated

[`../literature/LIBRARY.md`](../literature/LIBRARY.md) now holds the whole corpus in one place:
all 126 cited sources in thirteen clusters ordered by the work they do in the paper, each with
three annotations — where it sits, what it argues, what it uniquely adds — plus the forty-five
verified reserve entries grouped by why they are held, and the two do-not-cite lab anchors.
Abstract-depth sources are marked ⚠ so the no-attribution-from-abstracts rule travels with the
library. One true duplicate found and merged during assembly (munasinghe2022beyond, same DOI as
munasinghe2022 — it slipped the render guard because only one key was cited). Bib now 171 entries.
LIBRARY.md is the reader's map; references.bib remains the source of record.

## 2026-08-09 — P8 run; the research programme is complete

The compounding claim is in §5, stated at exactly the strength the evidence carries: hospitality's
voice conditions are impaired before any algorithm arrives (Jung and Yoon; Al-Hawari; Papadopoulos
et al. on silence as the sector's dominant response to grievance), dissatisfaction routes to exit
rather than collective voice (Zientara et al., in Hirschman's own terms), and algorithmic mediation
therefore compounds an existing suppression — as inference from converging evidence, with the
untested interaction named as a research opening. Fuller and Smith (1991) entered §3, giving the
felt-control craft paragraph its lineage: management by customers is an old control form acquiring a
new instrument. FOUNDATION Part 7 records the pass; AGENDA 7a is closed. Every prompt in
RESEARCH_PROMPTS.md is now run or absorbed. Library: 172 verified entries, 126 cited.

## 2026-08-09 — phronesis pass landed; Pierre-facing documents synced with the audit

Pierre's balance note now has its answer in the draft. §3 closes on the h-team craft, built from
Roger's own framing in the email thread: a practised team manufactures the guest's sense of control,
deferring visibly while deciding invisibly, and algorithmic direction disturbs the craft at its
hinge, opening a gap between felt control and actual control inside the front desk. §5 adds the
floor-level form of the competence, the agent who lends the guest her own specification. The section
that carried the most philosophy now ends on management ground.

The audit's corrections propagated to everything Pierre will read. The manuscript's §1 and
INTRODUCTION.md no longer resolve Lynch toward tactics alone; SHORT_DRAFT.md drops the staccato
capacity/obligation pair in both places it survived, carries the machine-ethics positioning, states
the algorithmacy specialization, and replaces the false Folger sentence with the conditional voice
claim (Lind added to its references alongside Goodwin and Ross). Body 8,901 words.

## 2026-08-09 — editor asks complete: well-being, gains, roadmap in §8

The last Phase-2 block is in. §8 now carries the human-centricity throughline in one sentence, a
well-being paragraph at two levels and three valences (TSR anchor via Anderson and Ostrom; the
individual/collective split via Galeone and Sebastiani and Uysal; negative evidence from Pan and
Nayak; ambivalence from Christou; the design-dependence of collective outcomes from Parkinson), the
claimable absence (individual-level automation evidence and collective-level well-being evidence
have not met), and the societal register pointed through Riordan. The managerial paragraph states
gains and challenges concretely, and Table 2 sets the framework out as a five-stage transformation
roadmap ascending in institutional cost, closing on the line practitioners need: a property that
stops after stage three has automated its hospitality without deciding who answers for it.

All seven of the editor's asks are now delivered or assigned: title (19, Pierre), dual-place (20,
§3 relay), human-centricity (21), well-being (22), gains/challenges (23, phronesis register pass
still owed), roadmap (24), APA and H&S citations (25, running throughout). Body 8,695; references
120; ceiling remains deferred to proof.

## 2026-08-09 — audit repairs executed; anonymity guard caught a self-citation

AGENDA items 44–49 are in the draft. Section by section: §7 rebuilt on Lind, Kanfer and Earley with
Folger cited for the interaction and the frustration effect folded into the argument; Costanza-Chock
grounds torque at travel's own threshold; the remedy paragraph cites cold-start and reputation
inflation instead of coining, and owns the Padigar narrowing. §2 drops "rather than moral," re-scopes
Pijls as measuring the trace rather than the position, and turns Beatty's rival account into support.
§3 adds the machine-ethics positioning paragraph (Kropf; Santoni de Sio and Mecacci; Introna's
machine-as-guest inversion), rewords the substitution claim, adds Liu's robotic hospitableness,
corrects the Möhlmann gloss, and adds Garcia on durable revenue-manager latitude. §4 gains the
accountability translation sentence (Okhuysen-Bechky task sense vs Bovens answerability) and the
levels-of-automation/R&K positioning. §5 states the algorithmacy specialization, cites Bovens and
Metcalf for the relational reading, and carries the counterparty reformulation plus the
consumer-sovereignty boundary and Shryock. §6 splits the nulls by kind, concedes Martin-Waldman and
Yurrita, and respecifies human accessibility as access to a person empowered to reverse.

**The render guard earned its keep again**: the §5 specialization initially cited (Algorithmacy Lab
2026), which is marked DO-NOT-CITE in the bib — unretrievable by a referee and deanonymizing under
blind review. Rephrased without citation; the sentence now names the broader notion inline.
**Roger still owns item 43**: whether this wording of the specialization (and the silent parking of
the affective facet) is the reconciliation he wants with the public definition.

Body now 8,140 words; projected total ~11,570 against the 9,000 ceiling, per the standing decision
that the ceiling is a proof-stage problem. Cited references: 113. The trim, when it comes, starts
from CLAIMS.md — anything cut must not reopen a repaired wound.

## 2026-08-09 — governing rule set: deliver the abstract, grounded in the editors' work

Roger confirmed the strategy: stay close to Pierre's locked abstract, which the editor blessed, and
address the debates the SI editors raise in their own published work. This settles the restructure
question left open after the prior-art map — the contribution stays the abstract's (AI as
constitutive mediator), the host argument and the seamlessness critique are sharpenings inside that
arc, and the seamlessness-to-lead option is off the table.

New authority file: [`ABSTRACT_MAP.md`](ABSTRACT_MAP.md), mapping all seventeen abstract commitments
to sections, editor-work anchors, and status. Three drift points found and fixed against the
abstract's own wording:

- **Presence was missing.** The abstract names five relational criteria; every draft had quietly
  reduced them to four. Restored in §2 and the short draft.
- **The research question had been paraphrased away.** "When does it leave the practice intact" is
  not the abstract's question. Restored near-verbatim in §1 of both the manuscript and
  INTRODUCTION.md.
- The editor's letter endorses the host framing in her own words ("an active participant in hosting,
  rather than a neutral technological layer") — recorded in the map so nobody re-litigates whether
  the host argument departs from the blessed abstract.

Advisory items stay advisory: the outcome-sentence restructure and the contest clause go to Pierre
with evidence, not into the draft.

## 2026-08-09 — introduction rebuilt on the 5Cs; prose rules tightened

**§1 now follows Lange and Pfarrer's five building blocks**, one paragraph each: common ground
(hybrid environments, the field's frameworks, and the triad as settled), complication (every name the
literature gives the third party denotes a thing that acts and none denotes a thing that owes; the
position marked employee got filled and the one marked host stayed empty), concern (hospitality
confers standing, and where an intermediary decides, that standing has no counterparty), course of
action, contribution. 642 words in paragraphs of 139, 128, 150, 130 and 95.

The opening vignette is gone from both drafts. A hospitality audience knows how check-in works, and
walking them through it read as condescension.

**Four prose faults were found and swept, and they should not come back.**

1. **Forward-reference scaffolding.** "The shape that claim takes in this field does work for us
   later", "and they organize what follows", "this is where design sections usually fail". Ten
   instances removed from each draft. Say the thing; do not promise it.
2. **Announcing a question instead of asking it.** "What that literature has not asked is whether the
   third party occupies the position of host." Five of these became actual interrogatives: *Is the
   third party a host? Who holds authority at each handover? What does it owe her? What obliges this
   one?*
3. **Unattributed field-wide proclamation.** "Hospitality scholarship has spent two decades resisting
   precisely that reading" was a historiographical claim with a citation cluster hung on it. Now
   attributed to people who make it: Hemmington on hospitality businesses being misdescribed as
   service operations, Lynch et al. reviewing the journal's decade, Shabnam et al. naming the gap from
   inside the phygital programme.
4. **Roll-call paragraphs.** §2 of the short draft was five author summaries and four unused
   definitions. It now argues one claim: hospitality confers standing, the standing is negotiating
   room and not benevolence, and Bulley locates where it gets taken away. §3, §4, §6 and §8 rebuilt
   the same way. Also gone: "We derive the affordances", "We move algorithmic systems out of the
   category", "The triad is not ours and we should say so early".

Bulley was carrying near-identical sentences in §1 and §2; §2's now develops rather than repeats.
Body is 6,778 against the 6,850 budget. Projected total 9,558, still over the 9,000 ceiling by 558.

## 2026-08-09 — §3 rewritten to concede the triad; the paper is now over ceiling

§3 no longer claims the triad. It concedes it in the opening paragraph, citing Larivière et al.
(2017), Odekerken-Schröder et al. (2021), Li et al. (2021), van Doorn et al. (2023) and Gursoy (2026),
then states plainly that the structure is established and our question begins where that literature
leaves off. A new second paragraph carries the contribution: the vocabularies that literature uses are
consistent and consistently unhospitable, Belanche et al. (2020) come nearest and still study blame
attribution rather than obligation, and a host owes a welcome that no employment relation generates
or discharges. A third paragraph positions against Batat and Shabnam et al., and lands the editor's
dual-place ask by describing phygitalization as a relay across which authority changes hands rather
than as fluidity. The discretion paragraph now carries the split verdict, with Spektor et al. (2023,
2025) as documented back-of-house evidence and Bendoly (2013) cited as the complication it is.
Riordan (2024) enters the closing paragraph as this journal's existing name for the negative pole.

§1's contribution preview was rewritten because it had become false: it previewed a triadic claim the
paper no longer makes.

**Three script and data defects found and fixed, all of which had already reached the draft.**

- `render_refs.py`'s `clean()` handled accents from a hardcoded table, so `Sch\"anzel`, `Casal\'o` and
  `Flavi\'an` rendered as raw LaTeX in the reference list. Replaced with generic accent handling over
  braced and bare forms, plus `\#`, `\%` and `\_`. The rendered list is now free of escapes.
- Belanche et al. (2020) existed under two bib keys and rendered twice. Merged into `belanche2020`
  with both notes preserved. **Added a same-DOI guard to `render_refs.py`** which aborts the render
  rather than emitting a duplicate, since this is the second duplication incident today.
- The orphan sweep that removed uncited keys produced two false positives, because it matched
  surnames against the body before unescaping them. Caught and restored; the check now cleans first.

**The reckoning.** Body 7,019 against a 6,850 budget. References 88 entries, 2,288 words. Projected
total **9,765 against a 9,000 ceiling: 765 words over.** The editor's remaining asks — well-being
expansion, managerial payoff, roadmap, human-centricity throughline — are not yet in the draft and
would add several hundred more.

The over-run is not evenly distributed and the shape tells you where to cut. §2, §3 and §7 are
collectively 1,093 words above their original budgets, and all three grew for reasons the research
justified. §4 and §6 sit 722 words *below* theirs and are the two sections the outline protects,
which means the protection has been achieved by under-writing rather than by discipline. §4 carries
the diagnostic table that answers "interesting but unfalsifiable" and §6 carries the design
contribution the editor asked to see strengthened. Neither should be cut, and both may need to grow.

Candidates for the 765, in the order we would take them:

1. **§5, 802 words.** The outline says algorithmacy and coordinative sovereignty get one pass and no
   restatement, with the apparatus cited to the sovereignty arm. Whether §5 currently honours that is
   the lead author's call, and it is the single largest discretionary block in the paper.
2. **References.** Fifty-seven of 88 are cited once. Twenty cuts returns 520 words. Each cut removes
   a claim's support, so this is an argument-by-argument decision rather than a trim.
3. **§3's knowledge paragraph.** Rahman and Calo and Rosenblat carry the asymmetry point; the
   paragraph is supporting rather than load-bearing now that the host argument leads.

## 2026-08-09 — §2 and §7 revised; the word budget is now the binding constraint

Phase 2 opened on the two sections the missing full texts do not block.

**§2 regrounded from P1**, 850 to 1,197 words. Additions: the journal's founding editorial locating
hospitality in social control, exchange and metaphor (Lynch et al. 2011); Bulley (2015) qualifying
Derrida in these pages, since host authority is exercised continuously inside the space rather than
spent at the threshold, which is what licenses a paper about mediation after check-in; a new paragraph
stating the return to the guest as relational and negotiated rather than moral, with Lynch (2017)
cited for the equivocal finding a reviewer would otherwise raise against us, Pijls et al. (2017) for
the field's own instrument locating acknowledgment, and Kekstaite (2022) for reciprocity as an
achievement that can therefore be designed away; two named absences claimed as gaps (no theorization
of the guest's reciprocal obligation in commercial settings, no instrument measuring anything flowing
from guest to host); and Farmaki and Kaniadakis (2020) so the third party reads as something
hospitality scholarship registered before information systems arrived to announce it.

**§7 promoted**, 600 to 936 words. It now opens by naming the target precisely: seamlessness is a
stated commitment of the frameworks this special issue builds on, with Batat's own "fluidifying the
journeys of customers" quoted and Shabnam et al. (2026) shown to critique opacity and rigidity while
leaving smoothness alone. Lynch's social-oil observation opens the critique in the field's voice
before any design literature is consulted. Walters et al. (2021) puts cultural variation beyond
dispute at scale. Phillips et al. (2024) adds the retail evidence that the cost of smoothness is not
confined to guests a system fails to fit.

**Reference list re-rendered**, 68 to 77 entries. Reconstructed `cited_keys.txt`, which had not been
kept, by matching the rendered list back to the bib. Two duplicate bib keys removed
(`lynch2021reprise`, `batat2026psr` — both were added twice in round 2). Added the missing
`## References` heading, which the Notes for Contributors require and the draft lacked.

**The constraint.** Projected total is **8,965 against a 9,000 ceiling**. Body sits at 6,471 with 379
words of headroom; total headroom is 35 words. Fifty-seven of 77 references are cited once. The
editor's remaining asks — dual-place process, human-centricity, well-being expansion with societal
implications, managerial payoff, roadmap — cannot all be funded from 35 words. Something gets cut,
and the decision is the authors'. `wordcount.py --refs` default corrected from 61 to 77; it had been
under-reporting the total by roughly 400 words.

**One discrepancy left standing.** Padigar et al. is carried as 2024 in the bib and manuscript;
round 2 reported it as 2025. Volume 42:1 and pages 21–43 agree across both. Online-first versus issue
year is the likely explanation. Resolve before proof rather than churn the draft now.

## 2026-08-09 — the triad is nine years old, and the paper is better for it

Full-text retrieval on the four blocking texts returned one of four, and turned up something larger
than the texts. **The customer–employee–technology triad has been explicit since 2017** and has been
re-derived at least five times, carrying the literal name "service triad" in *JOSM* and "encounter
triad" in *IJHM*. Gursoy (2026) is the most recent statement, not the first. Dated table in
[`../literature/FOUNDATION.md`](../literature/FOUNDATION.md) Part 5.

**Nobody treats the third party as a host.** Every prior characterization is a tool, an automated
social presence, an employee substitute, a frontline actor, an object of blame attribution, a
mediator, a facilitator, a collaborator, a co-creator, or an algorithmic actor. None reaches for
hospitality's ethical vocabulary. That absence was searched for directly and is safe to claim. No
peer-reviewed critique of seamlessness was found either, held with slightly less confidence.

So the contribution is now two normative claims rather than one structural claim: the third party
occupies the **host** role and hospitality loads the host with obligations the employment relation
does not generate; and **seamlessness is not self-evidently hospitable**. The triad becomes a
sixty-word concession in §3 with three citations. That is a sharper paper than the one that had to
defend the triad as novel, and the concession removes its largest exposure.

Gursoy's own close helps rather than hurts: precision to the machine, empathy to the human. He
reserves the relational register for the human and draws exactly the line this paper questions.

**One more gain, in §6.** Spektor et al. (2025) was retrieved in full. The self-sequencing affordance
that lets hotel workers reorder their own room assignments was negotiated into the **union contract**,
not built as a technical feature. Adjustability existed because an institution constituted the forum.
That is the arm's best hospitality-native evidence for why coordinative sovereignty must be a second
construct rather than a facet of algorithmacy, and it sharpens the managerial implication: some
affordances are discharged by design, others only by institutional arrangement.

Still needed: Gursoy and PH-CX have no legitimate open copy and want Bentley ILL. Zheng et al. (2025)
sits in the Surrey repository behind an anti-bot layer and can be pulled by hand in a browser.

## 2026-08-09 — round 2 research run; the contribution needs re-pointing

P1, P2, P6 and P7 run in parallel, then a separate mechanical verification sweep over every citation
returned. 54 verified entries added. Full write-up in
[`../literature/FOUNDATION.md`](../literature/FOUNDATION.md) Part 4; new agenda items 26–35.

**The verification sweep caught a wrong author list** — three of five named authors had nothing to do
with the paper they were attached to — plus a volume error, a year error, and an uncited corrigendum.
Second such catch on this project. The rule holds.

**The finding that matters most: the triadic move is already published in a hospitality journal.**
Gursoy (2026, *JHMM*) reconceptualizes hospitality encounters as customer–employee–AI triads with
agency redistributed and interpretive labour transformed. Roederer et al. (2026) find AI acting as a
third agent. Zheng et al. (2025) name a phygital tourism experience triad. Shabnam et al. (2026)
already name algorithmic mediation of agency inside the phygital literature. Triadicity as such is
no longer available as the contribution.

Two moves survive, and the paper should be re-pointed onto them. The **host role** rather than the
third node: hospitality theory loads the host with obligation in a way "employee" does not, and the
normative asymmetry is an argument only a hospitality-theory paper can make. And the **seamlessness
critique**, which is the paper's one uncontested move — TPSR critiques opacity and rigidity but not
smoothness, PH-CX positively endorses fluidity, and the friction literature that would trouble it
sits entirely outside phygital scholarship. §7 was budgeted at 600 words as the smallest substantive
section. That allocation now looks wrong.

Three other things change the draft. §3's employee half splits into documented back-of-house and
undocumented guest-facing, which is a finding about the field rather than a hole. Bendoly (2013) runs
against the revenue-management claim and must be cited as a complication before a reviewer raises it.
And §2's moral reading of hospitality's return to the guest is refuted by the source §2 most needs to
cite; relational-and-negotiated is both better supported and sharper.

## 2026-08-09 — SI editor approved, co-author steer, six revision items opened

Email chain with Pierre, 2026-08-07 to 2026-08-09. Sequence:

- Pierre sent the locked abstract to SI editor Dr Wided Batat for blessing.
- Editor response (2026-08-08): abstract is "a compelling and theoretically rich contribution,"
  full submission warmly encouraged. Six concrete revision requests attached — see the new table in
  [`../cfp/ALIGNMENT.md`](../cfp/ALIGNMENT.md). None of the frozen constructs are challenged; the
  asks are emphasis, framing, and citation, not theory.
- Pierre's read (2026-08-09): "this is a management paper not a philosophy one... get the balance
  between the logic and the phronesis right," and proposes a short draft as the next move.

**Status correction for Pierre:** a full draft already exists (`manuscript.md`, ~6,800-word body,
all nine sections, register-checked against venue exemplars). His "short draft next" note likely
predates seeing it — reply should surface the draft rather than start one. His phronesis note is
still live and separate from the completion question: the draft leans on the triadic/algorithmacy
apparatus (logic) more than on managerial judgment-in-practice (phronesis). Roger's own aside in the
thread — the guest-control-through-a-subservient-h-team framing — is a phronesis-register example
worth testing against section 4 or 8.

New open items from this round are logged in [`AGENDA.md`](AGENDA.md) under "Editor and co-author
feedback." The title question (editor proposes dropping "Algorithmic Mediation, Guest Agency and
the") is a co-author call, same rule as the abstract: Pierre's wording, Pierre's conversation.

## 2026-08-07 — register measured, first draft rewritten

The first complete draft applied the repo's house register — Nagel-plain, no first person, short
declaratives, bolded construct names — to a critical social science journal, and it read as a report
rather than an article. The planning documents had said to measure register from venue exemplars;
that step was skipped and house style was inherited instead.

Corrected by reading two full texts from the journal's own author community, Lynch et al. (2021) in
*H&S* and Lugosi (2021) in *Tourist Studies*. Both use the first person freely, run 150–250-word
paragraphs, subordinate heavily, and make the cited author the grammatical subject. The manuscript
was rewritten against those findings and the ruling recorded in
[`REGISTER.md`](REGISTER.md), which also scopes the suspension of the repo rule to the manuscript
alone.

One dimension still short of the exemplars: paragraph mean sits at 102 words against their 150–250.
A further pass would close it.

## 2026-08-07 — plan review: schedule, word budget, citations

Review of the baseline library against the plan produced four decisions.

- **The dissertation pass stops gating the freeze.** 28 days remain; constructs freeze on the
  locked abstract, and the genealogy pass runs in a one-day box alongside drafting.
- **The word limit is 5,000–8,000 words.** The outline now carries a per-section budget totalling
  7,600. Algorithmacy and coordinative sovereignty get one pass in section 5 and no restatement —
  the pile-up mitigation in `PLAN.md` was previously written down but not enforced anywhere.
- **Citations verified.** All seven external entries checked against publisher records. The Addis
  et al. DOI was wrong by one digit (`…057590` → `…057593`) and an author's given name was wrong
  (Lori → Lane). PH-CX, the phygital research paradigm, and PSR are three distinct Batat works;
  the map had been calling the 2024 QMR guest editorial "PSR". Batat (2026, *JSM*) is PSR proper
  and is now seeded.
- **Section 4 gains a diagnostic table.** The augmentative/substitutive poles were asserted with no
  procedure for classifying a real touchpoint — the likeliest reviewer objection.

Open worry not yet resolved: the CFP is uncorroborated outside the kickoff PDF. Intellect's journal
page lists no special-issue calls. Re-read the PDF before trusting 4 September.

## 2026-08-07 — baseline library opened

- Arm scaffolded under `org_frontier/hospitality_phygital/`.
- Abstract locked as author-supplied pitch.
- Dissertation tree absent in the cloud public clone; construct freeze waits on local review
  ([`../DISSERTATION_REVIEW.md`](../DISSERTATION_REVIEW.md)).
- Critical path is the journal full paper (window through 4 September 2026), not new Φ work.

## Parking lot

- Reference style from the Notes for Contributors (`HOSP_NFC_May_26.pdf`) — length confirmed at
  5,000–8,000 words; style still to read.
- Decide whether APA Summit attendance materials (talk deck) belong in this arm later.
- Possible vignette set: mobile check-in; algorithmic room assignment; AI concierge; reputation-
  mediated upgrade denial.
