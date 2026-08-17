# Review — platform studies and algorithmic management lens

**Target:** `chapter/chapter_v3.md` (read in full, 5,414 body words, 71 notes).
**Focus per commission:** §5, "The new selectors," with cross-section consequences where §5's claims
are set up in §2 or spent in §7.
**Reviewer's sources opened for this pass:** Binns et al. full text (arXiv 2506.15278v1, extracted
locally); Dubal, *On Algorithmic Wage Discrimination* (Columbia Law Review publisher PDF, extracted
locally); *Uber Technologies, Inc. v. City of Seattle*, slip op. (ca9.uscourts.gov, extracted locally);
Stark and Pais, *Sociologica* 14(3), publisher galley (extracted locally); Kellogg, Valentine and
Christin abstract and Cameron abstract (OpenAlex reconstructions). Everything I mark `verified` below
I read myself in this session. Everything I could not open is in the VERIFY section at the foot, and I
have asserted no correction from it.

---

## VERDICT

**Minor revisions**, and I mean that as a compliment to a section that has clearly already survived one
brutal pass. §5 is the most disciplined platform-studies writing in the chapter: it knows where its
evidence is thin and mostly says so out loud. Three of my findings are real defects rather than
polish, and one of them — the second — is the kind a referee opens with.

**The single most important fix:** §2 promises that Uber "reads both parties in detail," and §5 spends
a whole sentence conceding that nobody has shown ride-hail *matching* reads anybody. Those two
sentences cannot both stand. Fix §2, not §5 — §5 is the honest one.

---

## STEP 0 — REGISTER, AND THE BAR

**Register identified:** first-person film-studies criticism on the Hansen/Bordwell model — "I" as the
steering wheel, scenes before theses, contractions, concessions taken in stride, questions asked and
then actually answered. Section 5 is the same voice turned on a technical literature: it reports what
an audit found, names what the audit cannot support, and keeps the pronoun.

**The bar I will hold it to:** make it better at being itself. I have not flagged first person,
contractions, em-dashes or parallelism as such — §5 runs 4 em-dashes in 738 words, the second-lowest
density in the chapter, and every one of them is landing a beat rather than bolting on an aside. Where
I propose a rewrite, it is shorter or the same length, more concrete, and in the author's own diction.
Any suggestion of mine that came out more nominalised than the original I deleted before writing this.

---

## PART 1 — THEORETICAL RIGOR AND STRUCTURE

### 1.1 The load-bearing crack: §2 asserts what §5 retracts

§2 runs the three questions on three cases in one breath:

> "Austin acts on the whole street, is one route among many, and reads types at most. The camera picks
> one person out of the crowd, is the only way that person reaches you, and knows nothing about
> anybody. **Uber picks the pair, is the only route to the match, and reads both parties in detail.**"

§5, doing the honest thing:

> "no published engineering account describes ride-hail dispatch as reading rider or driver identity in
> order to choose the pair, and Uber's and Lyft's own descriptions run on collective wait time and
> marketplace value. The evidence sits on the pricing side."

Question 3 is "Does it know who these particular people are, **and change what it does accordingly**?"
§2 answers yes for Uber on the strength of the matching case. §5 says the matching case is not there.
A referee reading in order meets the strong claim first, believes it, and then watches the chapter take
it back sixty lines later without noticing it has done so.

This is a two-word repair and it costs the chapter nothing, because §5's honesty is what makes the
argument credible in the first place. See R2 in Part 3.

There is a second, quieter version of the same problem in the same §2 sentence. "**is the only route to
the match**" is doing counterfactual work (question 2) that a platform-studies referee will not grant
as stated. Drivers multi-home; riders multi-home; Uber is emphatically *not* the only route to a ride.
It is the only route to *that particular* match. The distinction is the chapter's own and the fix is
one word.

### 1.2 The three powers are not three powers of equal standing, and the section half-admits it

Prices, reads, removes. The evidentiary standing runs:

- **Prices** — one participatory audit, one company, one country, 1.5M trips, self-selected sample.
  Strong for what it is.
- **Removes** — two courts, on two continents, one of them a published federal appellate opinion.
  Strongest of the three.
- **Reads** — Dubal asserts differential pay flatly; personalisation is her marked inference; the
  matching evidence does not exist; the pricing evidence is *the same evidence already spent on power
  one*.

So power two has no independent evidence base. §5 says so — "The evidence sits on the pricing side" —
and then leaves the taxonomy at three anyway. A hostile platform-studies referee closes on exactly
this: *your second power is your first power described differently.*

I do not think it is, and the chapter has the material to say why. Differential pay for the same work
at the same time is evidence of reading, because to pay two people differently you must first
distinguish them. What is unevidenced is reading-in-order-to-*match*. That is one clause, not a
restructure, and it converts a concession into a distinction. The Amsterdam case is also a reading case
— the deactivations were triggered by a fraud signal and the remedy was disclosure of how the decision
was reached — so the chapter actually has reading evidenced at two of the three sites and only absent
at the third.

### 1.3 Prior art the section does not meet: the 6 Rs

**This is the finding I would put second in the letter, and it is the one that most exposes the
chapter.** Kellogg, Valentine and Christin's "Algorithms at Work" (*Academy of Management Annals* 14,
no. 1: 366–410) is the field's standard taxonomy of what algorithms do to workers, and it is a list of
six: *restricting, recommending, recording, rating, replacing, rewarding* — direction, evaluation,
discipline. I pulled the abstract and confirmed the six terms and the grouping this session.

The chapter's three powers map onto it almost cleanly. Prices ≈ rewarding. Reads ≈ recording and
rating. Removes ≈ replacing and restricting. A platform-studies reader will make that mapping in about
four seconds and will want to know what the chapter's list adds.

It adds something real, and the chapter should say it in one sentence: **the 6 Rs run vertically, from
an employer down to a worker. The chapter's powers run triadically, from a third party across a pair it
assembled.** That is the whole point of the setting/selector apparatus and it is precisely what a
control-over-workers taxonomy cannot express. The paper is in §5's own outline bibliography
(`outline_v3.md`, "the repertoire of evaluation and discipline") and it never made it into the chapter.
Restore it as an antagonist, not as a citation of courtesy. See R4.

### 1.4 The defence against 1.3 was cut in compression — and the version the research file recommends is misquoted

Stark and Pais, "Algorithmic Management in the Platform Economy," is the one paper that makes the
vertical/triadic argument in the field's own voice. The outline flags it for §5. The chapter cites it
nowhere. So the section lost its own best shield against the 6 Rs objection.

**And there is a trap waiting if the author restores it from the research file.** `research/deep/
2026-08-01_s5.md` (Finding 2) and `outline_v3.md` both recommend this sentence, presented as verbatim
at p. 49:

> "Triangular rather than vertical, and not as a panopticon, the lines of vision in algorithmic
> management are not lines of supervision."

I downloaded the publisher galley and extracted it. **That sentence is not in the article.** The real
text, on printed **p. 56** (confirmed by folio arithmetic against the page footers: the page ending
before it carries the folio 55), reads:

> "Triangular rather than vertical, the lines of vision in algorithmic management are not those of a
> panopticon — and, strictly speaking, are not supervisory."

The research file's version paraphrases the second half and puts it seven pages early. "Rankings but not
ranks" *is* on p. 49, exactly as the file says — the two locators appear to have been fused. The chapter
is clean on this because it dropped the source entirely; the *outline* is not, and a restoration done
from the outline would print a misquotation into a chapter whose whole methodological pride is that it
does not do that.

### 1.5 Cameron is scoped away, not met — and the answer is already in the abstract the chapter quotes

The commission asks whether the Cameron objection is genuinely met. It is not. It is relocated.

> "Her subject is the management regime — when to work, which nudges to take, how to game the inputs —
> rather than the act of matching. So the contrast is not between a cut and a match. It is between a
> cut and a regime that prices and removes."

The move is: *she is talking about a different object, so she does not bear on mine.* That disposes of
her only if the chapter's object is matching alone — but §5's own thesis is that the selector "prices
and removes," and pricing and removal are exactly the regime Cameron's workers consent to. The
objection survives the relocation intact: *the people your selector selects experience it as a source
of choice, and they are not wrong.*

The answer is sitting in the abstract the chapter already has in hand. I reconstructed it from OpenAlex
this session; Cameron finds consent produced by two tactic sets — engagement tactics, where workers
follow the nudges, and **deviance tactics, "where individuals manipulate their input into the system."**
Deviance is choice exercised *against* the selector. Nobody games a cut. Nobody manipulates their input
into a film. That is a genuine asymmetry, it is Cameron's own finding, and it costs about ten words to
say. R6 supplies the sentence, and it comes in *shorter* than what it replaces.

Two smaller things in the same paragraph. "**when to work**" is not in the abstract, and note 54 cites
the abstract because the body is unreachable — so one third of the three-item gloss is asserted from a
paper nobody on the project has opened. Drop it; the other two items ("nudges," "manipulate their
input") are both traceable. And the quantifier is handled correctly — "many workers report" — which I
note because the research file worried about it and the chapter got it right.

### 1.6 The surge argument is right, and one sentence away from being unassailable

The commission asks specifically whether the surge argument is "has not been shown to know" rather than
"shown not to know." **It is, and it is done well.**

> "All I can say is that surge has not been shown to know who the two parties are — a model that
> abstracts away from identity establishes nothing about identity."

That is the correct epistemic shape, it is stated in one clause without self-congratulation, and the
Besbes attribution is properly hedged as a model rather than a description: "Besbes, Castro and Lobel
**model** a platform that 'selects prices for different locations' and **find an optimum** that induces
overcongestion." The quoted phrase is verbatim from the published abstract. The third lens's objection
in the research file — that a stylised model cannot establish what the real mechanism does or doesn't
know — is fully absorbed. Good.

**The gap:** the chapter's own next paragraph brings in Dubal, and Dubal's headline instance of
differential pay *is the surge multiplier*. At 1936 and 1949 (I read both this session):

> "the surge multiplier presented to Diego may differ from the multiplier presented to Marta, even if
> both workers are working in the same area at the same time."

A reader who knows Dubal — and a platform-studies referee does — will read the surge paragraph, then
the Dubal paragraph, and conclude the chapter contradicts itself within eighty words. The chapter's
scoping ("In the economics, surge is...") is technically enough, but it relies on the reader noticing
that "the economics" excludes a law review, which is a lot to ask of a silent qualifier.

The disarming fact is one I verified: Dubal's Diego/Marta sentence is illustrative, not measured. Diego
and Marta are her interview pseudonyms, the verb is "**may** differ," and the sentence is prefaced "For
example." It is an illustration of a claim, not a measurement of surge. Saying so costs thirteen words
and closes the section's only live internal contradiction. See R9.

### 1.7 The removal contrast equivocates against §4

> "A camera can pass you over. It cannot price your passage and it cannot take you off the street."

§4 has already established, at some rhetorical cost, that this camera does exactly the removing kind of
thing: "Two abandonments in the opening minutes — the director, then a tragedy — teach the rule the rest
of the film runs on. **Nobody is owed a return.**"

So the camera *can* take you off the screen, permanently, and the chapter has made a small feature of
it. The real difference is not that the camera cannot remove but that its removal costs the removed
party nothing outside the frame. Say that and the contrast gets sharper, not weaker. R10, +5 words.

### 1.8 The power count does not survive into §7

§5: "it comes to three things" — prices, reads, removes.

§7: "Amazon publishes its own account of how titles are licensed for Prime Video, and **three of the
powers described above** are in it. It reads... It removes... **And it declines to explain**... **The
fourth power** is missing from the page."

There are only three powers, and "declines to explain" is not one of them. §7 counts four and gets
there by promoting a refusal that §5 never named. This is not a quibble — it is the arithmetic of the
chapter's central apparatus, and it appears in the closing section where a referee is already tallying.

I think the right fix is the generous one, because §5 already has the material. The Amsterdam remedy in
§5 *is* the opacity power: the court ordered disclosure of how the decision was reached, and got no
reinstatement. That is a platform that removed and would not explain, litigated. Either name opacity as
a fourth power in §5, or fix §7's arithmetic to two-plus-a-refusal. R3 gives the cheaper of the two.

### 1.9 What §5 does that I want to praise before Part 2

The pricing paragraph is the best-argued 90 words in the chapter. It puts an audit in the slot where a
lesser draft would put surge, it quotes the finding rather than a summary of it, it reports the mean
*against* the median instead of only the number that helps, and it names the mechanism ("A price
computed twice, per match") rather than a metaphor for it. That paragraph is why my verdict is minor
revisions.

---

## PART 2 — THE FOUR BANS, AND THE SLOP AUDIT

### Ban 1, no metaphor doing argumentative work — CLEAN in §5

I found no metaphor carrying a claim in this section. "A price computed twice" is literal. "A camera can
pass you over" is literal about a camera. "The evidence sits on the pricing side" is a spatial idiom for
a stated fact, not a substitute for one. Nothing to report.

### Ban 2, no throat-clearing — TWO HITS

> "Surge pricing is the wrong example here, **and saying why sharpens the distinction**."

The first clause is a claim. The second announces that a point is coming and grades it in advance. Cut
seven words, keep the claim. This is the same species as the "It is worth saying where this power is
best evidenced…" line the cut ledger already killed in this very section; it grew back in a nicer suit.

> "**The best evidence for this power is not where a reader would expect it:** no published engineering
> account describes ride-hail dispatch as reading rider or driver identity..."

Announces a surprise, then delivers it. The surprise is more surprising unannounced. Cut eleven words
and start on "No published engineering account."

Between them these two pay for a third of my additions.

### Ban 3, no meta-commentary — CLEAN in §5

"What a decade of subsequent work adds is a precise account of what a selector can do that a camera
cannot, and it comes to three things" is enumeration, not roadmapping — it describes the literature,
not the chapter. No forward references to later sections. No "as I said above." Clean.

### Ban 4, no unexplained jargon — ONE MISS

**"participatory audit"** arrives undefined and does load-bearing work: it is the entire warrant for the
pricing power, and a film-studies reader has no idea whether it means an academic study, an activist
report, or a regulator's inspection. It means something quite specific and quite good — drivers
exercised GDPR subject-access rights, pooled the records Uber holds on them, and researchers analysed
the pool. Six words of gloss buy the definition *and* the self-selection caveat at once. R8 folds both
into the sentence it already has.

Everything else clears: surge is defined in the act of being used ("a price attached to a place and a
time whose designed effect is to move drivers across a map"), deactivation is glossed by context, and
the chapter wisely says "cut" throughout rather than "take rate."

### Slop audit — the register is intact; two uniformity tells

**Nominalisation:** none worth reporting. The section runs on verbs — prices, reads, removes, bars,
computed, deactivated. This is the opposite of the disease.

**Performed rigor:** "All I can say is that surge has not been shown to know who the two parties are"
reads to me as doing real epistemic work rather than narrating virtue, and I would keep it. But note the
pattern across the chapter's last three sections: "All I can say is," "I will assert the differential pay
and leave the personalisation where she leaves it," "I want to draw that difference in the right place,"
"I am not going to supply it," "What would make selectors contestable… I cannot answer." Five
first-person modal honesty-moves in roughly 2,200 words, all the same shape. Individually each is good.
As a set they become a tic, and the reader starts hearing the shape instead of the content. I would
convert one or two to flat statements of the limit with no "I" in them — not because first person is a
problem, but because the *uniformity* is.

**Landing-line drumbeat — the one real slop finding.** Five of §5's six paragraphs exit on a polished
epigram:

- "A price computed twice, per match, and disclosed to neither party in full."
- "…a model that abstracts away from identity establishes nothing about identity."
- "The evidence sits on the pricing side."
- "It is still a court saying that removing a worker from a platform is conduct a city may regulate."
- "It is between a cut and a regime that prices and removes."

Every one is a good sentence. Five in a row is a metronome, and it is the single most machine-like
feature of the section. Two of my repairs happen to fix it as a side effect: R1 rewrites the first into
a working sentence with a verb, and R6 rewrites the last. That leaves three, which is a rhythm rather
than a drumbeat.

**Antithesis machine:** §5's closing three sentences run it three times consecutively — "rather than the
act of matching / the contrast is **not** between a cut and a match / **It is** between a cut and a
regime." R6 collapses this to one.

**Enumerator drift:** "The first is that it prices each match" / "The second **thing** is that it reads
the parties" / "The third **thing** is that it can remove a party." Pick one. Dropping both "thing"s
saves two words and reads better.

**Em-dashes:** 4 in 738 words in §5 — well within the chapter's own norm and below §4 (9) and §6 (8). No
paired-dash crutches. Nothing to do.

**Filler transitions:** zero. **Rhetorical inflation** (delve, landscape, navigate-as-filler, crucial):
zero. This section has been scrubbed and it shows.

---

## PART 3 — RANKED LINE REVISIONS, PASTE-READY

Ranked by how much each improves the chapter. Word deltas given because the draft is 408 over an
unconfirmed ceiling; net for the whole set is about **+51 words**, and `v3_cut_ledger.md` already ranks
§7's Tzioumakis paragraph (~85 words) as the first thing to go. That one cut pays for all of this with
34 to spare.

---

**R1 — §5, pricing paragraph. The verified overreach.** *(+4 words)*

CURRENT:
> A price computed twice, per match, and disclosed to neither party in full.

PROBLEM: the source establishes only the *driver's* side. I searched the full Binns text this session
for any statement about what the passenger is shown regarding the driver's fee: there is none, in
either direction. The project's own verification pass struck this exact symmetry ("The symmetry claim
is unsupported in one direction… Drop 'keeps each side from seeing the other's'") and it has come back
wearing "neither party in full." This is the one sentence in §5 that a referee can falsify by opening
the cited paper.

REPLACE WITH:
> A price computed twice, per match, and half of it the driver may not even ask about.

---

**R2 — §2, the three questions run on three cases. The load-bearing crack.** *(+1 word)*

CURRENT:
> Uber picks the pair, is the only route to the match, and reads both parties in detail.

REPLACE WITH:
> Uber picks the pair, is the only route to that particular match, and knows a great deal about both.

WHY: "that particular match" survives multi-homing, which "the only route to the match" does not. "Knows
a great deal about both" is true and defensible; "reads both parties in detail" is the strong
reading-to-match claim that §5 spends a sentence retracting. §5 then reads as *narrowing* §2 rather than
contradicting it.

---

**R3 — §7, the arithmetic.** *(+9 words)*

CURRENT:
> …and three of the powers described above are in it. It reads: … It removes: … And it declines to
> explain: … The fourth power is missing from the page and I am not going to supply it; Amazon
> publishes nothing about pricing.

REPLACE WITH:
> …and two of the three powers are on the page, along with the refusal the Amsterdam drivers had to go
> to court over. It reads: … It removes: … And it declines to explain: … The missing power is pricing,
> and I am not going to supply it; Amazon publishes nothing about it.

WHY: three powers, two present, one missing, plus a refusal §5 has already litigated. The arithmetic
closes and §7 gains a spine back to §5's strongest paragraph.

---

**R4 — §5, first paragraph. Meet the 6 Rs.** *(+38 words, plus a note)*

INSERT after "…and it comes to three things.":
> The field already has a list of what algorithms do to the people who work under them — restricting,
> recommending, recording, rating, replacing, rewarding.[^n] That list runs from an employer down to a
> worker. Mine runs from a third party across a pair it put together, which is a different geometry and
> a shorter list.

NOTE:
> [^n]: Katherine C. Kellogg, Melissa A. Valentine, and Angèle Christin, "Algorithms at Work: The New
> Contested Terrain of Control," *Academy of Management Annals* 14, no. 1 (2020): 366–410. Their "6 Rs"
> group as direction (restricting, recommending), evaluation (recording, rating), and discipline
> (replacing, rewarding).

WHY: this is the referee's first question and it currently has no answer in the text. Optionally add
Stark and Pais on the same point — but if you do, use the verbatim sentence in the VERIFY section
below, at p. 56, **not** the version in the research file.

---

**R5 — §5, the Cameron paragraph. Meet her instead of relocating her.** *(−9 words)*

CURRENT:
> Her subject is the management regime — when to work, which nudges to take, how to game the inputs —
> rather than the act of matching. So the contrast is not between a cut and a match. It is between a
> cut and a regime that prices and removes.

REPLACE WITH:
> Her subject is the regime, not the match — which nudges to follow, and how to manipulate the inputs
> when a worker would rather not follow them. That second tactic answers her for me: nobody games a cut.
> The contrast I want runs between a cut and a regime that prices and removes.

WHY: "manipulate their input into the algorithmic management system" is Cameron's own phrase for her
deviance tactics, and deviance is what felt compulsion looks like from the inside. It converts her from
an objection absorbed into an objection answered on her own evidence. It also drops "when to work,"
which is not in the abstract and cannot be sourced from a body nobody has read. And it saves nine words
and kills the section's triple-antithesis ending.

---

**R6 — §5, pricing paragraph opening. The scope fix.** *(+14 words)*

CURRENT:
> Since the first quarter of 2023 in London, on the evidence of a participatory audit of 1.5 million
> trips by 258 drivers, "the price the passenger pays and the fee the driver receives vary independently
> of each other."

PROBLEM (verified in the full text this session): Binns et al. say dynamic pricing "was first announced
in London (where the majority of drivers in our dataset work) in February 2023" and that "rollout was
completed across the UK by summer 2023." The abstract describes "1.5 million trips from 258 drivers **in
the UK**." The chapter's syntax fuses a London rollout date to a UK sample and reads as though the audit
were of London trips. It also leaves "participatory audit" undefined and the self-selection in the note.

REPLACE WITH:
> Uber split the two sides of the price in London in early 2023 and finished the rollout across Britain
> by that summer. Drivers who volunteered their own records let researchers audit 1.5 million trips from
> 258 of them: "the price the passenger pays and the fee the driver receives vary independently of each
> other."

WHY: correct on scope in both directions, defines the method in the act of using it, and "who
volunteered" carries the self-selection into the body where a referee will look for it. Keep note 48 as
it stands — it is already honest.

---

**R7 — §5, surge paragraph. Close the Dubal contradiction.** *(+13 words)*

CURRENT:
> All I can say is that surge has not been shown to know who the two parties are — a model that
> abstracts away from identity establishes nothing about identity.

REPLACE WITH:
> All I can say is that surge has not been shown to know who the two parties are. Dubal offers the
> contrary instance, but her two drivers are pseudonyms and her verb is "may differ" — an illustration,
> not a measurement — and a model that abstracts away from identity establishes nothing about identity
> either.

WHY: verified against Dubal at 1949. Diego and Marta are her interview pseudonyms, the sentence is
prefaced "For example," and the verb is "may differ." The one apparent contradiction in §5 dissolves,
and the chapter looks like it has read its opponent rather than avoided her.

---

**R8 — §5, the reads-the-parties paragraph. Two throat-clears out, one distinction in.** *(−11 words net)*

CURRENT:
> The best evidence for this power is not where a reader would expect it: no published engineering
> account describes ride-hail dispatch as reading rider or driver identity in order to choose the pair,
> and Uber's and Lyft's own descriptions run on collective wait time and marketplace value. The evidence
> sits on the pricing side.

REPLACE WITH:
> No published engineering account describes ride-hail dispatch as reading rider or driver identity in
> order to choose the pair, and Uber's and Lyft's own descriptions run on collective wait time and
> marketplace value. What is evidenced is reading in order to price, and to pay two people differently
> you have first to tell them apart.

WHY: drops the announcement, and turns the concession into the distinction it should have been. The
second power stops looking like the first power renamed.

---

**R9 — §5, surge paragraph opening. Ban 2.** *(−7 words)*

CURRENT:
> Surge pricing is the wrong example here, and saying why sharpens the distinction.

REPLACE WITH:
> Surge pricing is the wrong example here.

---

**R10 — §5, the camera contrast. Stop equivocating against §4.** *(+5 words)*

CURRENT:
> A camera can pass you over. It cannot price your passage and it cannot take you off the street.

REPLACE WITH:
> A camera drops people for good and it costs them nothing. It cannot price your passage and it cannot
> take you off the street.

---

**R11 — §5, the Ninth Circuit. Mark the split.** *(+2 words)*

CURRENT:
> in March 2026 a Ninth Circuit panel let Seattle's deactivation ordinance stand, holding that "when
> conduct is nonexpressive, as is the case here, it is not subject to First Amendment scrutiny."

REPLACE WITH:
> in March 2026 a Ninth Circuit panel refused to enjoin Seattle's deactivation ordinance, holding over a
> partial dissent that "when conduct is nonexpressive, as is the case here, it is not subject to First
> Amendment scrutiny."

WHY: verified in the slip opinion this session. The quotation is exact and straddles pp. 12–13 as the
note says, the disposition is "AFFIRMED" on a denial of a preliminary injunction (so "refused to enjoin"
is the precise verb, and "let stand" slightly overstates), and Bennett, J., dissented in part on
*precisely* this holding — "I believe the Ordinance compels speech and is thus subject to the First
Amendment." A chapter this careful about the disclosure/reinstatement distinction should not report a
2–1 holding as a panel holding.

**Free gift while you are in there:** Bennett's ground is that the ordinance compels the platforms "to
draft and provide workers a written" deactivation policy. That is a court fight about whether a platform
can be *made to explain a removal* — which is R3's fourth power and §7's Amazon "may not be resubmitted
or appealed" sentence, arriving from the other direction. One clause connects the chapter's last two
sections through a live piece of litigation.

---

**R12 — §5, pricing figures. Two small precision fixes.** *(+2 words)*

CURRENT:
> Across that sample the company's median cut rose from 25 to 29 percent while the mean held at 25, the
> increase concentrated on the highest-fare trips.

REPLACE WITH:
> Across that sample the median driver's cut to Uber rose from 25 to 29 percent while the mean held at
> 25, the increase concentrated on the higher-fare trips.

WHY: verified. §5.1 reads "Uber's median take rate **per driver** has increased from 25% to 29%" — it is
the median of driver-level averages, not the median trip, and "median cut" alone invites the wrong
reading. And the source says "higher take rates are concentrated among **higher**-fare trips"; the
chapter's "highest" is a superlative the source does not use.

---

**R13 — §5, Dubal's inference. Show why it is one.** *(+4 words)*

CURRENT:
> She goes further, and marks it as inference when she does — the wage manipulators "appear to be
> personalized based on what Uber's machine learning systems know…"

REPLACE WITH:
> She goes further by analogy with consumer price discrimination, and marks the step as she takes it —
> the wage manipulators "appear to be personalized based on what Uber's machine learning systems know…"

WHY: verified at 1949. The full clause is "But **based on what is known about price discrimination in
the consumer context**, these wage manipulators appear to be personalized…" — the analogy is what makes
it an inference rather than modesty about something observed. As it stands, a reader sees only "appear
to be" and may read it as hedged reporting. Four words make the epistemics visible.

The commission asked whether Dubal's inference is correctly marked as inference. **It is** — this is a
sharpening, not a correction. And I verified the footnote too: "We have no way to judge the accuracy of
this statement" at 1935–36 n.19 is Dubal's own sentence, following her citation of Uber's denial. The
chapter's "Dubal's own footnote says" is accurate.

---

**R14 — §5, enumerator parallelism.** *(−2 words)*

"The second **thing** is that it reads the parties" → "The second is that it reads the parties."
"The third **thing** is that it can remove a party" → "The third is that it can remove a party."

---

## COMMISSION QUESTIONS, ANSWERED DIRECTLY

**Are the three powers each properly evidenced?** Prices: yes, well, with one verified overreach (R1) and
one scope slip (R6). Removes: yes, best of the three, with one unmarked 2–1 split (R11). Reads: **no
independent evidence base**, which the section half-admits and should fully admit as a distinction
rather than a shrug (R8, §1.2).

**Is Binns correctly scoped to London and a self-selected UK sample?** Partly. London is in the body; the
UK-wide sample and the self-selection are in the note only, and the body's syntax makes the audit read as
London-based. Verified against the full text; R6 fixes it in fourteen words.

**Is the surge argument right that surge has not been *shown to know* rather than *shown not to know*?**
**Yes.** Correctly and economically stated, with the Besbes model properly marked as a model. The only
gap is that Dubal's contrary instance goes unaddressed eighty words later (R7).

**Is Dubal's inference correctly marked as inference?** **Yes.** R13 is a sharpening only — the analogy
that makes it an inference is currently invisible.

**Is the Cameron objection genuinely met rather than absorbed?** **No.** It is relocated and then declared
disposed of. R5 meets it, on Cameron's own evidence, in fewer words than the current version.

---

## BIGGEST GENUINE STRENGTH

The section knows the difference between what an audit measured and what a model assumed, and it writes
the difference into the prose rather than into a footnote. "A model that abstracts away from identity
establishes nothing about identity" is the best sentence about method I have read in a film-studies
chapter, and the decision to demote surge — the most quotable, most familiar, most *available* example
in the whole platform literature — because the evidence points somewhere less glamorous is a scholarly
decision most authors would not make. The pricing paragraph earns the chapter's central claim on one
audit's worth of evidence and does not pretend to more. That restraint is what will get this past a
platform-studies referee.

## THE ONE THING ONLY THE AUTHOR CAN SUPPLY

**Cameron's body text, through a university library.** SAGE 403s every automated route — I tried, the
project tried three times, nobody has read past the abstract. The chapter currently characterises her
subject in three specifics, one of which ("when to work") cannot be sourced from the abstract, and it
rests its answer to the strongest objection in the section on a paper it has read the first 200 words
of. Twenty minutes with the PDF would let the author (a) confirm the deviance material R5 leans on, (b)
find out whether Cameron discusses the *match* anywhere — if she does, the relocation defence collapses
and needs rebuilding, and better to find that out now than in a referee report, and (c) settle whether
her drivers experience the pricing power the way §5 says they do. This is the only remaining gap in §5
that no amount of careful writing can close.

Second, smaller, and also author-only: the Amazon Prime Video Direct page and the two Uber Help pages
are living corporate documents with no version history. Capture all three to the Internet Archive and
cite the snapshot beside the live URL before this goes to press. A referee who clicks a changed page and
finds different text will not assume the chapter was right when it was written.

---

## VERIFY — what I checked, and what I could not

**Checked myself this session, confirming the chapter:**
- Besbes, Castro and Lobel, "selects prices for different locations" and the overcongestion/priced-out
  optimum — verbatim in the published abstract.
- Dubal at 1936 on differential pay; at 1949 on personalisation, including the consumer-context analogy;
  at 1935–36 n.19, where "We have no way to judge the accuracy of this statement" is **Dubal's own
  sentence**, following her citation of Uber's denial. The chapter's attribution is correct.
- *Uber Technologies, Inc. v. City of Seattle*: "When conduct is nonexpressive, as is the case here, it
  is not subject to First Amendment scrutiny" — verbatim, straddling pp. 12–13 exactly as note 53 says,
  disposition "AFFIRMED" on denial of a preliminary injunction.
- Binns et al.: 1.5 million trips, 258 drivers, "vary independently of each other," "Uber's median take
  rate per driver has increased from 25% to 29%," "Mean average take rates have remained at 75%."
- Cameron: both quoted phrases present in the abstract; volume 69, issue 2, pages 458–514 confirmed.

**Checked myself, correcting or narrowing something:**
- Binns geographic scope: dynamic pricing "first announced in London (where the majority of drivers in
  our dataset work) in February 2023"; "rollout was completed across the UK by summer 2023"; sample is
  "258 drivers in the UK." → R6.
- Binns on passenger disclosure: **nothing** in the full text establishes what the passenger is or is not
  shown about the driver's fee. → R1.
- Binns "higher-fare," not "highest-fare"; "median take rate per driver," not median trip. → R12.
- Ninth Circuit: Bennett, J., dissenting in part, on exactly the quoted holding. → R11.
- Kellogg, Valentine and Christin's 6 Rs confirmed as restricting, recommending, recording, rating,
  replacing, rewarding, grouped as direction / evaluation / discipline. → R4.
- **Stark and Pais, and this one is a warning about the research file, not the chapter.** The sentence
  the research file and outline recommend for §5 — "Triangular rather than vertical, and not as a
  panopticon, the lines of vision in algorithmic management are not lines of supervision," attributed to
  p. 49 — **is not in the article.** I extracted the publisher galley. The real sentence, on printed
  **p. 56** (folio 55 sits at the foot of the preceding page), reads: "Triangular rather than vertical,
  the lines of vision in algorithmic management are not those of a panopticon — and, strictly speaking,
  are not supervisory." "Rankings but not ranks" is correctly placed at p. 49. Do not restore this
  source from the outline without re-checking the galley.

**Could not confirm — asserted nothing on these:**
1. Whether the *passenger* is shown anything about the driver's fee. Undocumented in both directions;
   Binns establishes only the driver's side. §5's opening claim that "nothing in the design lets the two
   settle anything between themselves" is well supported for the driver and unsupported-but-unrefuted for
   the rider. If a rider-side source exists, I did not find it; if none does, one clause naming which
   direction the evidence runs would be cheap insurance.
2. **Cameron's body text.** SAGE 403 by every route. "When to work" is not in the abstract, and no
   page-level body quotation should be printed. See "author-only" above.
3. Castillo, "Who Benefits From Surge Pricing?" — econometricsociety.org returned 403 to me as it did to
   the research pass. Note 49's "rider surplus rising and driver surplus falling" matches the OpenAlex
   abstract reconstruction, but neither I nor the project has read the version of record. Low risk, since
   the claim sits in a note.
4. Binns et al. ACM pagination, 1484–1497. I read arXiv v1; the ACM DL 403s. Crossref/DBLP corroborate
   per the research file, and I did not re-check them.
5. Rosenblat and Stark's support for "nothing in the design lets the two settle anything between
   themselves" as of 2016 — I did not open it this pass. Note 47's caveat about the changed interface is
   the right instinct either way.
