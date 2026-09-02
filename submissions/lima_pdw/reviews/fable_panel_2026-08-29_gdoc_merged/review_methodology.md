# Methodology Review — PAPER_gdoc_merged_2026-08-29.md
**Reviewer lens:** research design and qualitative methods (insider action research, abduction, psychometrics, sampling, empirical strategy)
**Manuscript:** "Algorithmacy: A Competency for Coordinative Co-optation" (Paper 2, OS/OT PDW Lima, Oct 2026)

---

## Verdict

**Major revisions** — the right verdict for a PDW, where the point is to arrive with the weaknesses named. **The single most important fix:** the four-study research agenda runs a confirmatory factor analysis (Study 2) on an algorithmacy scale that no study in the agenda ever builds. Insert the missing scale-development step — item generation from the Study 1 corpus, content validation, exploratory factor analysis — and pair it with an explicit design-freeze commitment for the gate mechanism, because pooling survey waves across cohorts whose evaluation gate the action-research cycle keeps redesigning violates the measurement-invariance assumption the pooled CFA depends on.

---

## Step 0 — Register and bar

This is a formal OT construct-development paper in the *Organization Theory* / *Annals* genre: dense, citation-saturated, claim-first paragraphs; a Suddaby-style construct-clarity architecture; a methods appendix in the Coghlan–Brannick insider-AR idiom. The bar I hold it to: the house style (named agents, active voice, first person for authorial labor, cohesion mechanisms, no self-narrated rigor) plus the methods standards of the ASQ/OS qualitative tradition it cites — Pratt (2009), Tracy (2010), Timmermans & Tavory (2012) — applied to its own design.

---

## Part 1 — Theoretical rigor and argument structure (methodological focus)

### 1.1 What the design gets right

Before the attacks, the credits, because they are real:

- The **core-project / thesis-project distinction** (Coghlan & Brannick, 2014) is correctly deployed (lines 285, 545): the developmental cohorts are explicitly demoted to instrument-calibration ground, not smuggled in as data. This is the move most insider-AR papers botch.
- The **abductive apparatus** is the genuine article, not decoration: sensitizing concepts (Blumer; Bowen), first-order Gioia coding before second-order categories, the three Timmermans–Tavory moves named and operationalized (revisiting, defamiliarization, alternative casing), and — rarest of all — a **pre-specified disconfirming case** (line 572: a participant who resolves gate breakdowns through pure technical mastery falsifies the triad's necessity). Table B1's per-module falsification criteria are better than most published qualitative designs.
- The **power honesty in Appendix B** (line 578): "Given a cohort size of approximately fifty students, the panel is not powered to perform exploratory or confirmatory factor analyses." Exactly right, and exactly what a referee wants to see conceded before they say it.
- IRB status is documented: Bentley University IRB exempt determination, Protocol 260511078 (line 578). Settled.
- Each of the seven construct hearings ends by naming what algorithmacy **inherits** from the rejected framework (Spitzberg's criteria, Hancock's optimization-goal parameter, Rahman's rival hypothesis, Zhou's protocol). That inheritance discipline is what separates a construct review from gap-mongering.

### 1.2 The two claims a hostile referee attacks first

**Attack 1 — the psychometric plan, and it does not survive as written.** Three compounding problems:

1. *The missing study.* Study 1 produces qualitative incidents plus a 50-person descriptive panel. Study 2 (line 615) "powers a formal confirmatory factor analysis" at N=200–250. But no study generates the items. Zhou et al. (2025) — the paper's own benchmark — ran 99 interviews → 14 candidate items → expert content validation → **EFA (N=275)** → CFA (N=213). The manuscript reproduces this sequence admiringly at line 120 and then omits its middle from its own agenda. A referee will read Study 2's "pre-registered latent correlation hypotheses" and ask: correlations of *what instrument*? The same problem infects the wave-2 plan (line 578) to run Zhou's scale "as a descriptive convergence check with *interpreting* and *specifying intent*" — a convergence check requires an algorithmacy measure at wave 2 that does not yet exist.
2. *Pooling across non-stationary cohorts.* Study 2 pools "survey administrations across successive cohorts until reaching a sample size of 200 to 250" (line 617). But the paper's own action-research narrative (line 529) boasts that "cyclical evaluations drove substantive structural modifications: site variations altered peer-evaluation networks, gate refinements systematically varied information visibility." At ~50 per cohort that is four to five cohorts, and if the gate keeps evolving between them, the pooled sample measures responses to different stimuli. The AR virtue (iterative redesign) and the psychometric plan (pooling) are in direct conflict. The fix is cheap to state and essential: commit to freezing the gate configuration across the pooled cohorts, or model cohort as a grouping variable and test configural/metric invariance before pooling.
3. *N=200–250 for a second-order model.* Defensible only by the Zhou benchmark; say so, and pre-commit to the invariance tests above so the benchmark comparison is legitimate.

**Attack 2 — the site-construct fit, and it survives only if reframed as conditional.** Line 291 claims "Structural properties of the coordination gate **refute** this interpretation" (that Hult is an ordinary pedagogical hybrid). Two paragraphs later (line 293) the paper concedes that the formal design "is documenting" — i.e., has not yet documented — "whether the platform algorithm deterministically allocates peer reviewers to specific submissions or allows participants to self-select into evaluation queues." But the scope condition for coordinative co-optation is an algorithm that *matches unchosen parties* (lines 48, 493). If reviewers self-select, the "unchosen parties" condition fails and the site slides toward the Upwork-style hybrid boundary the paper itself assigns to Sutherland et al.'s setting (line 188). "Refute" overclaims a verdict that rests on an admittedly undocumented parameter. Downgrade to a conditional: the site instantiates the form *if* the pairing is algorithmic, and the protocol documents which.

Two related site problems the same referee will stack on:

- **Who set the weights?** Line 29 says the weighting "remains concealed from everyone: the submitter, the peer reviewers, and the instructor." Line 291 calls the parameters "proprietary" — proprietary to whom, in a course the investigator designed? If the investigator-designer knows (or once knew, or can inspect) the aggregation rule, opacity is asymmetric: real for participants, absent for the researcher. Say so plainly. And then notice the buried asset: **a researcher who holds the ground-truth rule can score participants' interpretings against it** — an accuracy criterion no gig-platform study (Rahman, Zhou, Sutherland) could ever have, because their platforms' rules were opaque to the researchers too. The manuscript never claims this advantage. It should; it converts the insider position from a liability to be managed into the design's distinctive payoff.
- **Bindingness intensity.** The paper claims a "hard case" only for opacity (line 551). It is an *easy* case for bindingness: the gate binds course progression, not livelihood. Rahman's freelancers faced account death; these participants face a resubmission. A referee will ask whether stakes-dependent behaviors (constrained reactivity, in Rahman's terms) can appear at all under grade-level stakes. One sentence conceding the stakes gradient, plus Study 4's commercial sites as the stakes test, closes this.

### 1.3 The insider role-duality argument — mostly survives, one overclaim

The safeguards (line 553) are the standard, correct set: instructor role confined to macro-design, no vote or override, anonymized intake, interviews after evaluative cycles close, auditable trail. Anteby (2013) and Brannick & Coghlan (2007) are the right anchors. The overclaim is "**complete anonymity** from the instructional and research team" (line 576). With N≈50, a self-derived token "derived from invariant personal elements" (a quasi-identifier by construction — that is what Yurek-style codes are), and critical-incident narratives rich in incident-specific detail, deductive re-identification by the instructor is plausible. No IRB issue — the design is fine — but the *claim* should be "researcher-blind at intake and by procedure," not "complete anonymity." Referees punish absolute words they can defeat with one thought experiment.

### 1.4 The abductive stopping rule — needs one repair

Study 1 (line 611): analysis proceeds "not to a traditional grounded-theory saturation metric but to an abductive sufficiency criterion — the threshold at which incremental incidents generate no empirical casings that the derived operations cannot accommodate." Distinguishing this from saturation is smart. But as phrased the rule is confirmation-shaped: it stops when new incidents *fit the pre-derived operations*, which is exactly the failure mode abduction exists to prevent — Timmermans & Tavory's engine is surprise, not accommodation. The protocol already contains the antidote (the alternative-casing move, line 570, and the negative-case definition, line 572); wire them into the stopping rule: analysis stops when incremental incidents neither produce casings the operations cannot accommodate *nor* fit a rival framework (skill acquisition, gig literacy, dyadic sensemaking) better than the triadic one. With that clause, the rule survives; without it, a grounded-theory referee reads it as saturation with a confirmation bias and a new name.

### 1.5 The harness interview protocol

The in-editor, AI-administered critical-incident design is the paper's most novel instrument and gets the least methodological defense. What is present is good: Flanagan (1954) anchoring, incident-forcing prompts, reframing on refusal, terminology suppression to elicit native categories, client-side redaction with participant validation of the final transcript. What is absent, and a methods referee will ask:

- **Interviewer-agent validity.** An LLM interviewer probes differently across participants and sessions. Nothing addresses probing consistency, drift in the agent's behavior, or how the agent's own generative tendencies are kept out of the elicited incidents. One paragraph — fixed protocol version, logged prompts, transcript-validation step already in place — would answer it.
- **Pilot N.** The manuscript says "an initial diagnostic run" (line 312) and "initial pre-qualitative runs" (line 582) without ever stating the number. The actual base is two piloted transcripts with no completed coding. State it. "Two pilot administrations" costs nothing and forecloses the suspicion that vagueness is hiding a smaller N than it is — which, here, it is.

### 1.6 Empirical-status honesty — consistent with three slips

The paper's macro-framing is honest and repeatedly so: "the multi-wave field investigation remains prospective" (line 316); "Formal data collection... will systematically evaluate" (line 312); the Conclusion explicitly limits the contribution to architecture plus a piloted apparatus. The slips:

1. **Line 312:** "Preliminary piloting of the in-editor interview protocol provides early operational insights into the micro-mechanisms of triadic coordination." One participant's LLM-routing adaptation is an *instrument-refinement finding* (as Appendix B correctly classifies it at line 585), not an insight into the phenomenon's micro-mechanisms. This is the paper's single clearest overclaim relative to two uncoded transcripts.
2. **Line 285:** present tense for a Spring 2027 study — "the investigator executes no further administrative interventions within the focal cohorts, and data collection protocols remain strictly anonymized." Nothing has been collected from focal cohorts; write "will execute," "will remain." Same for the main-text consent sentence (line 310), which reads prospective while Appendix B's IRB sentence reads completed — harmonize the tenses so the reader learns in the main text that approval is in hand and fielding is Spring 2027.
3. **The "Instruments and Status" section (line 308) contains no status.** No date, no N, no count of pilot runs. The honest numbers — Spring 2027, one cohort of ~50, two pilot interviews, panel not powered for factor analysis — live only in Appendix B. A PDW reader (and any referee) reads the main text first; the burial reads as reluctance even though the appendix is candid. Surface three sentences.

### 1.7 An internal inconsistency in the construct's own measurement logic

Where does the candidate fourth operation come from? Section "Constitutive Operations" (line 212) integrates evaluative attribution "directly within *interpreting*." The RQ discussion (line 304) says RQ4 "explicitly decouples error attribution from *keeping track*," and Appendix B (line 517) says it is "a candidate fourth dimension rather than a component of longitudinal tracking." Study 1 (line 613) then tests it against "baseline sensemaking" (interpreting again). The manuscript wavers between attribution-as-facet-of-interpreting and attribution-versus-tracking. Pick one host — interpreting, per line 212 — and state once that RQ4 tests whether attribution separates from *both* interpreting and keeping track. As written, a careful referee can quote the paper against itself on its own measurement model.

### 1.8 Remaining agenda items

- **Study 3** specifies constructs and controls (human capital, task complexity, tenure) but no sample, setting, or N. As the test of Propositions 1–2 it is currently a hypothesis with no design attached; even a one-sentence sample spec would help.
- **Duplicate RQ roadmap:** the four RQs appear nearly verbatim at lines 299–302 and 512–515. Appendix repetition is tolerable, but trim one to a pointer.
- **Polemic to ground:** "Algorithmic coordination regimes operate by systematically inverting these standards" (line 255). "Systematically inverting" is a rhetorical escalation of what the evidence supports — the four ODR standards are *absent*, per the cited sources, not inverted by design. Rewrite in precise terms: each of Wing et al.'s four guarantees is withheld in the settings Curchod et al. document. Same instinct at line 543 — "demonstrates that opacity constitutes an intrinsic property of algorithmic coordination" from three course iterations the author built; three researcher-configured sites cannot demonstrate intrinsicness, only recurrence across configurations.
- **Citation apparatus (verify before adopting — I flag, the author confirms):** (a) **Riordan (1995)** cited at line 553 and **Yurek, Vasey, & Havens (2008)** cited at line 576 are missing from the reference list. (b) Table 1 (line 68) cites "Mohlmann, 2021" — the list's entry is Möhlmann, Zalmanson, Henfridsson, & Gregory (2021), so the in-text form should be "Möhlmann et al., 2021" with the umlaut. (c) The anonymous 2026 JMIR preprint (line 334, "authors not retrievable") sits in the reference list but is never cited in text — the Clinical Medicine bullet (line 322) that presumably needs it carries no citation. Either cite it there and defend citing an unrefereed authorless preprint, or cut both. (d) Typo, line 495: "gig and platform platforms."

---

## Part 2 — AI-slop audit (register-aware)

**The good news first, because it is measurable:** zero `has been / have been` agentless throat-clears in 18,300 words; zero banned emphasis openers (no "Crucially," "Importantly," "Notably"). The lexical layer has been cleaned hard.

**Em-dash count: 13 total (~0.7 per 1,000 words).** No crutch use; the instances present are the legitimate kind — the gloss-weld at line 162 ("communicative literacy—operationalized as a clinician explaining algorithmic outputs to a patient whom the system does not simultaneously govern or bind—") and the dimension-list appositive at line 100 are exactly what the device is for. The register problem runs the *other* way: the house calibration puts the venue at ~3 per 1,000, and this manuscript introduces construct after construct without welding the gloss on. No flag for overuse; a mild prescription for more welding at first-use of coined terms.

The slop that remains lives one layer up. Four findings:

### 2.1 Uniform density — the inverse of uniform punchiness, same tell

Every paragraph has the same shape: a dense claim-first topic sentence, then four to six equally dense unpacking sentences, each 25–40 words, each carrying two abstractions and a subordinate clause. There is not one short declarative sentence in the body. The house corpus punctures dense builds with "It does not." / "The claim is contested." — this manuscript never exhales. Read lines 158–162 aloud: six consecutive sentences of near-identical length and syntactic weight. The fix is not more polish; it is variance. Examples of where a puncture lands:

- After line 100's build ("No combination of autonomy or message magnitude transforms an assistant that edits text into an autonomous institutional authority..."), add: **"An editor is not a judge."**
- After line 128's build on Zhou's dyadic ceiling: **"The scale cannot see the counterpart because the construct never let her in."**
- Line 291, replace "Structural properties of the coordination gate refute this interpretation" with the conditional (see Part 3, R2) and let the short sentence do the verdict work.

### 2.2 The jargon drumbeat

Counts across 18,300 words: **"structural" ×97, "architecture/architectural" ×43, "constitutive" ×23.** "Structural" appears in consecutive sentences dozens of times, often doing no work ("structural omission," "structural boundary," "structural vacancy," "structural impasse," "structural reversion," "structural parameterization"). This is nominalization-as-rigor: the adjective performs precision it does not add. Cut half of "structural" with zero loss of meaning — most instances modify nouns that are already structural ("boundary," "position," "configuration"). Same treatment for "architecture" wherever "design," "gate," or "rule" would serve. Test each: does the sentence change truth-value without the word? If not, cut.

### 2.3 Verbatim formula repetition

The triple "opaque, adaptive, and (mutually) binding" and its two-term variants appear **~18–23 times.** The house rule: the definitional instance earns the full formula once per major section; after that, rename the thread entity ("the triad," "these three properties," "the arrangement," "such systems"). Similarly "theoretical/structural vacancy" ×6 — the gap is real and was earned once in the Introduction; by line 172 the reader is being told again what she was told at 23, 27, 56, 88, and 160. Keep the Introduction instance and the "What These Boundaries Share" instance; convert the rest to pronouns of the argument.

### 2.4 Agentless passive in the methods — flag each, named-agent rewrites supplied

This is where the passive hides the one agent the insider-AR framing is supposed to foreground: the author. Solo-authored paper; the Annals calibration (Rahman, Cameron, Suddaby all solo) prescribes "I." The manuscript instead uses "we" ×20 and, in the methods, no agent at all:

| Line | Text as written | Named-agent rewrite |
|---|---|---|
| 553 | "Role duality is managed through deliberate structural safeguards rather than methodological disavowal" | "I manage the dual role through structural safeguards rather than disavowal" |
| 553 | "The investigator's instructional role is restricted to macro-level course design" | "I restrict my instructional role to macro-level course design" |
| 553 | "participant intake... is strictly anonymized at the client level" | "the intake client anonymizes participants before any record reaches me" |
| 517 | "the primary investigator's dual role... is treated as an epistemic asset" | "I treat the dual role as an epistemic asset" |
| 578 | "Ethical oversight was established under Bentley University Institutional Review Board exempt determination Protocol 260511078" | "Bentley University's Institutional Review Board determined the study exempt (Protocol 260511078)" |
| 578 | "Formal large-sample discriminant validity testing is reserved for subsequent field studies" | "I reserve large-sample discriminant testing for Study 2" |
| 586 | "The protocol was refined to replace generalized summaries with mandatory incident anchors" | "I refined the protocol to force incident anchors in place of generalized summaries" |
| 623 | "Discriminant validity is evaluated using the heterotrait-monotrait ratio" | "I evaluate discriminant validity with the heterotrait-monotrait ratio" |
| 484 | "each coordination form is evaluated across six core questions" | "Paper 1 evaluates each coordination form across six questions" |

The pattern matters beyond style: an insider-AR paper whose central methodological claim is that the researcher's position is an epistemic asset should not write its methods as if no researcher were present.

### 2.5 Performed rigor (two instances)

- Line 553: "The research design secures methodological trustworthiness through an auditable research trail (Pratt, Kaplan, & Whittington, 2020; Tracy, 2010)." This names the virtue instead of the practice — a sentence about the paper's own care, which the house style bans outright. Rewrite with contents: "I log every protocol version, coding memo, and analytic decision in a dated audit trail (Pratt, Kaplan, & Whittington, 2020; Tracy, 2010)."
- Line 293: "To maintain methodological transparency, two specific operational parameters of the gate mechanism warrant explicit identification as ongoing design specifications" — self-narrated rigor plus euphemism ("ongoing design specifications" = "not yet documented"). Rewrite: "Two parameters of the gate remain undocumented, and the protocol records both before fielding: whether the algorithm assigns reviewers or participants self-select, and what exit and escalation rights a contested verdict carries."

**Not flagged as slop, deliberately:** the pilot/flight-control analogy (line 15) and the pull-request vignette (line 29) are the paper's two concrete anchors and its most human passages; the Stark "co-opted" quartet (line 48) is a carried signature from the source, not a tic; the inheritance paragraphs closing each construct hearing are structured repetition doing analytic work, not formula.

---

## Part 3 — Line-level revisions, ranked by impact

**R1 (highest value — the agenda hole).** Add to Appendix C, between Studies 1 and 2, or as Study 2's opening move:
> "Study 2 first converts the Study 1 incident corpus into a candidate item pool — one item per recurrent first-order code, following Zhou et al.'s (2025) generation protocol — submits the pool to expert content validation, and fits an exploratory factor analysis on the first pooled cohorts before any confirmatory model. The gate configuration is frozen across all pooled cohorts, and I test configural and metric invariance across cohorts before pooling; failure of metric invariance halts pooling and the cohorts are modeled as separate groups."

**R2 (the site-fit overclaim, line 291).** Replace "Structural properties of the coordination gate refute this interpretation." with:
> "The gate's structure resists this reading — provided one parameter holds. If the platform assigns reviewers algorithmically, the gate matches unchosen parties and the site instantiates the form; if participants self-select into evaluation queues, the site slides toward the hybrid boundary Sutherland et al. (2020) describe. The protocol documents which, before fielding."

**R3 (the pilot overclaim, line 312).** Replace "Preliminary piloting of the in-editor interview protocol provides early operational insights into the micro-mechanisms of triadic coordination." with:
> "Two pilot administrations of the in-editor protocol tested whether the modules elicit codable critical incidents. They did — and one produced an unanticipated adaptation worth building into the coding rubric."

**R4 (the anonymity absolute, line 576).** Replace "preserving complete anonymity from the instructional and research team" with:
> "keeping the panel researcher-blind by procedure: no name, token key, or intake record reaches me, though with a cohort of fifty I cannot rule out incidental recognition from incident details, and the coding protocol strips identifying particulars for that reason."

**R5 (the stopping rule, line 611).** Extend the sufficiency criterion:
> "—the threshold at which incremental incidents neither present casings the three operations cannot accommodate nor fit a rival framing (skill acquisition, gig literacy, dyadic sensemaking) better than the triadic construct. Fit alone does not stop the analysis; the alternative-casing pass must also come back empty."

**R6 (the researcher's ground-truth asset — new sentence for §"Research Site Architecture," line 551).**
> "The insider position carries an advantage no field study of commercial platforms has held: because I configured the gate, the true aggregation rule is available as a criterion, and participants' interpretings can be scored for accuracy against it rather than only coded for content."
(With one honest companion sentence resolving line 29: state who set the weights and from whom, exactly, they are concealed.)

**R7 (status into the main text, §"Instruments and Status," line 308).** Add:
> "The status, plainly: Bentley's IRB has determined the study exempt (Protocol 260511078); the formal cohort — roughly fifty students in a sixteen-week Hult course — fields in spring 2027; two pilot interviews are complete and none of the formal corpus has been collected or coded. The single-cohort panel tracks within-person trajectories; it is not powered for factor analysis, which Study 2 takes up at N=200–250."

**R8 (RQ4 host, line 304).** Replace "The formulation of RQ4 explicitly decouples error attribution from *keeping track*" with:
> "RQ4 tests whether evaluative attribution — provisionally housed within *interpreting* (see Constitutive Operations) — separates empirically from both *interpreting* and *keeping track*."

**R9 (the ODR polemic, line 255).** Replace "Algorithmic coordination regimes operate by systematically inverting these standards" with:
> "Each of these four guarantees is withheld in the settings the literature documents: decision rules stay unobservable (Rahman, 2021), determinations carry no accountable office, contestation routes to the platform's own apparatus (Zhou et al., 2025), and enrollment substitutes defaults for consent."

**R10 (rhythm punctures — three insertions).** After line 100's final sentence: "An editor is not a judge." After line 128: "The scale cannot see the counterpart because the construct never let her in." After line 172's four-condition verdict sentence: "No candidate passes."

---

## Findings ranked, most damaging first

1. **Missing scale-development study + cohort-pooling under a changing gate** (Appendix C, Studies 1–2, lines 611–623; cohort redesign at line 529). The CFA has no instrument and the pooled sample no invariance argument. — R1.
2. **Site-fit verdict rests on an undocumented parameter** ("refute," line 291, vs. the concession at line 293); compounded by "concealed from everyone"/"proprietary" (lines 29, 291) never stating who set the weights, and the unclaimed ground-truth advantage. — R2, R6.
3. **Pilot overclaim** ("insights into the micro-mechanisms," line 312) and unstated pilot N (two transcripts, uncoded; lines 312, 582). — R3, R7.
4. **Empirical status buried in Appendix B** (N≈50, Spring 2027, power concession at line 578) while the main-text "Status" section (line 308) carries no status; tense slips at lines 285 and 310. — R7.
5. **Confirmation-shaped abductive stopping rule** (line 611). — R5.
6. **"Complete anonymity" overclaim** (line 576) against N≈50 + quasi-identifying token + rich narratives. — R4.
7. **RQ4 host inconsistency** (interpreting at line 212 vs. keeping-track framing at lines 304, 517). — R8.
8. **Methods-section agentless passives and "we" in a solo paper** (lines 484, 517, 553, 578, 586, 623; "we" ×20). — Part 2.4 table.
9. **Citation apparatus:** Riordan (1995) and Yurek et al. (2008) cited but absent from references (lines 553, 576); "Mohlmann, 2021" in-text form (line 68); uncited anonymous JMIR preprint in the list (lines 322, 334); "platform platforms" typo (line 495). Author to verify each before adopting.
10. **Prose-layer uniformity:** uniform sentence density with no punctures; "structural" ×97 / "architecture" ×43 / "constitutive" ×23; the opaque-adaptive-binding formula ×~20; "vacancy" ×6. — Part 2.1–2.3, R10.
11. **Ungrounded polemic escalations** ("systematically inverting," line 255; "demonstrates that opacity constitutes an intrinsic property," line 543). — R9.
12. **Study 3 has no sample specification; interviewer-agent validity undiscussed; bindingness stakes-gradient unacknowledged; duplicate RQ roadmap.** One to two sentences each.
13. **Under-welded glosses:** em-dashes at 0.7/1k against a venue norm near 3/1k — add gloss-welding appositives at first use of coined terms rather than trimming.

---

## Closing note

The paper's biggest genuine strength is its falsifiability discipline — a construct paper that pre-specifies its own disconfirming case (the participant who wins on pure technical mastery), per-module falsification criteria in Table B1, an HTMT threshold that can kill a dimension, and a cohort-level prediction (line 261) whose failure mode is stated before any data exist. Most PDW construct papers arrive unfalsifiable; this one arrives with its kill conditions printed.

The one thing only the author can supply, which no reviewer can fabricate or check: the ground truth of his own gate. Who set the aggregation weights, whether he can inspect them, and whether reviewers are assigned or self-select — these are facts about an instrument he built, and the site-fit argument, the opacity claim at line 29, and the unclaimed accuracy-scoring advantage in R6 all live or die on them. Two sentences of plain disclosure, from the only person who knows, would do more for this manuscript's methodological credibility than everything else in this review combined.
