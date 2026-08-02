# Review -- platform studies / algorithmic management

**Verdict:** minor revisions
**Target:** chapter_v3.md (post-followup; panel 3)

## Step 0 -- register

The first-person film-critical register is working and should stay. Section 5 now has the right manner for
platform studies: it distinguishes models from measurements, uses court cases with care, and concedes the
weak point in the matching evidence. The remaining problems are not tonal. They are source fit and
architecture: one current sentence misdescribes Cameron, one sentence in section 2 still promises more than
section 5 can support, and the section uses the field's platform geometry without citing the field's closest
formulation.

Verification note: I retrieved sources in this session where corrections below depend on them. Verified
sources: Cameron's full SAGE text; Binns et al., FAccT 2025; Dubal's working-paper/PDF text; Lee, Kusbit,
Metsky and Dabbish 2015; Stark and Pais 2020; Stark and Vanden Broeck 2024; and the Kellogg, Valentine and
Christin abstract/PDF text. I did not re-retrieve the Amsterdam decision or the Ninth Circuit decision, and
I make no correction to those claims.

## Part 1 -- Theoretical rigor and structure

### 1. Cameron is now the live factual fault in section 5

**Verified.** I retrieved Cameron's full SAGE text in this session. The current chapter says:

> Her subject is the management regime -- when to work, which nudges to take, how to game the inputs --
> rather than the act of matching.

Cameron does not leave matching outside the object. She names five algorithmic functions in the ride-hailing
system: "matching, work instructions, demand-based pricing, bonus pricing, and ratings." Her table states
that matching "assigns task to workers." Her deviance section then says drivers "circumvented the blind
matching algorithms by selecting and screening rides," and gives examples of pre-selecting riders and
screening assigned rides.

The chapter's contrast can survive, but the sentence has to move. Cameron's subject is not the match alone.
It is the whole regime in which matching is one step and workers still have narrow inputs to manipulate. That
actually sharpens the camera/platform difference: nobody manipulates input into a cut.

Paste-ready fix:

> Her subject is the regime, not the match alone: accepting, rejecting, screening, manipulating inputs,
> following nudges, and trying to make the blind match yield a chosen rider. That helps the contrast. Nobody
> games a cut. A platform match is one step in a regime that prices, rates, sanctions, and removes.

If this fix is used, the bibliography entry for Cameron can no longer say "Abstract consulted only."

### 2. Section 2 still gives Uber a cleaner "reads both parties" answer than section 5 can defend

This is an internal contradiction, supported by the verified platform sources. Section 2 runs the three
diagnostic questions across the cases:

> Uber picks the pair, is the only route to the match, and reads both parties.

Section 5 later says:

> No published engineering account describes ride-hail dispatch as reading rider or driver identity in
> order to choose the pair...

The section 5 sentence is the honest one. The evidence for reading is strong around pricing, ratings,
sanctions, and work allocation. It is thin for identity-sensitive matching. The difference matters because
question 3 asks whether the third "knows who these particular people are, and change what it does
accordingly." If the first demonstration of the test says Uber clears that question at the moment of
matching, a platform-studies reader will expect section 5 to prove it.

The fix should be made in section 2, not section 5:

> Uber picks the pair and is the only route to that particular match. Its strongest evidence for reading
> comes after and around the match, when the platform prices, rates, and can remove.

This keeps the selector claim and removes the unsupported implication that Uber's matching engine has been
shown to read driver or rider identity in order to make the pair.

### 3. The section now meets Kellogg, but it still needs Lee and Stark/Pais

**Verified.** The current section has fixed the largest prior-art gap:

> Katherine Kellogg, Melissa Valentine, and Angele Christin catalogue algorithmic control as six functions
> running from an employer down to a worker; what follows runs sideways, from a third party across a pair it
> has itself assembled.

That is the right distinction. The problem is that the two field anchors around it are still missing.

First, the opening claim says:

> That much has been true since researchers first studied the app.

The note cites Rosenblat and Stark 2016. Lee, Kusbit, Metsky and Dabbish 2015 is the earlier study that
coined "algorithmic management" and studied Uber/Lyft work assignment, dynamic pricing, and evaluation. It
should be in the note and probably in the sentence.

Paste-ready fix:

> That much has been true since Lee, Kusbit, Metsky and Dabbish named algorithmic management in their
> Uber/Lyft study, and Rosenblat and Stark then made information asymmetry the center of the case.

Second, Stark and Pais give the platform-studies version of the "sideways" geometry. Their abstract says
platform owners co-opt providers and users in "a triangular geometry," enrolling them in algorithmic
management without delegated managerial authority. Stark and Vanden Broeck extend the same point in 2024
with the platform as the characteristic organizational form of algorithmic management. The chapter's
accepted abstract names both. The chapter's current bibliography names neither.

Paste-ready insertion after the Kellogg sentence:

> Stark and Pais name the platform geometry more directly: providers and users act on their own behalf, while
> the platform turns those acts into management without giving either party authority. That is the sideways
> relation this section needs.

### 4. The surge paragraph still needs one sentence to meet Dubal

**Verified.** The current surge paragraph is properly cautious:

> All I can say is that surge has not been shown to know who the two parties are -- a model that abstracts
> away from identity establishes nothing about identity.

That is right as a claim about the economics model. But the next paragraph brings in Dubal, and Dubal's
headline illustration is a surge multiplier: Diego and Marta may receive different surge multipliers in the
same area at the same time. A platform-studies reader will notice the apparent contradiction.

The chapter can close it without retreating. Dubal's example is illustrative, not measured. The verb is
"may," the two names are interview pseudonyms, and the personalization claim is made by analogy with
consumer price discrimination.

Paste-ready replacement:

> Surge has not been shown to know who the two parties are. Dubal's contrary example is a surge multiplier,
> but she gives it as an illustration, not a measurement: her verb is "may," and the personalization claim
> rests on analogy with consumer price discrimination. A model that abstracts away from identity establishes
> nothing about identity either.

This also removes one of the repeated "All I can say" self-scruple moves.

### 5. The "reads" power is defensible, but its object should be named more exactly

Section 5 now adds the crucial distinction:

> So the evidence for reading sits on the pricing side, which is not the same as the pricing power over
> again. To pay two people differently you have first to tell them apart. What has no evidence behind it is
> reading in order to match.

That is much better than the prior version. The remaining ambiguity is "two people." In Dubal, the two
people are two drivers doing the same work at the same time. In Binns, the measured split is between the
passenger fare and the driver fee, but the audit does not show passenger identity-based personalization.
The paragraph should state the object of reading: driver, trip, market, and sometimes rider-side fare, not
identity-sensitive pair selection.

Paste-ready adjustment:

> What is evidenced is reading in order to price, rate, and sanction: driver, trip, market, and customer-side
> fare. What has no evidence behind it is reading in order to match.

This is a small change, but it keeps the second power from looking like the first power repeated.

## Part 2 -- The four bans, and AI-slop audit

### Ban 1 -- metaphor doing argumentative work

Mostly clean in section 5. "Sideways" is a metaphor, but the literal claim follows immediately: a third
party acts across a pair it assembled. If the Stark and Pais sentence is added, the geometry becomes an
explicit platform-studies term and the risk disappears.

### Ban 2 -- throat-clearing

One hit:

> The difference has to be drawn in the right place, though...

The sentence announces care before making the Cameron point. The Cameron rewrite above starts on the source
and removes the announcement.

"Surge pricing is the wrong example here" is not throat-clearing. It is a claim, and the next sentences
explain it.

### Ban 3 -- meta-commentary / forward-backward reference

Section 5 is mostly clean. The Cameron opener above is the one meta-commentary problem. The opening
enumeration -- "it comes to three things" -- is acceptable because the list is the section's object.

### Ban 4 -- unexplained jargon

One miss:

> subject-access data

This carries the warrant for the Binns audit. A film reader may not know that this means data drivers
obtained from Uber through data-access rights. Replace it with:

> drivers pooling records they obtained from Uber through data-access requests

"Take rate" is technical, but the preceding sentences explain fare, fee, and Uber's cut well enough.
"Deactivation" is clear from context.

### AI-slop audit

The section is much cleaner than the prior panel version. The 6 Rs are met, the power count is fixed, and
the Binns paragraph no longer overclaims passenger-side disclosure. Two structural tics remain:

1. The self-scruple cluster: "All I can say," "I will assert," and "The difference has to be drawn..." all
   occur within a short span. Keep the Dubal caution, but state at least one limit flatly.
2. The Cameron paragraph still runs an antithesis machine: "rather than the act of matching," "not between a
   cut and a match," "It is between..." The Cameron rewrite collapses that run.

No problem with first person as such. The issue is repetition of the same self-qualifying move.

## Part 3 -- Line-level revisions (paste-ready)

### R1 -- Section 2, Uber in the diagnostic sentence

Current:

> Uber picks the pair, is the only route to the match, and reads both parties.

Replace:

> Uber picks the pair and is the only route to that particular match. Its strongest evidence for reading
> comes after and around the match, when the platform prices, rates, and can remove.

### R2 -- Section 5, Cameron paragraph

Current:

> Her subject is the management regime -- when to work, which nudges to take, how to game the inputs --
> rather than the act of matching. So the contrast is not between a cut and a match. It is between a cut and
> a regime that prices and removes.

Replace:

> Her subject is the regime, not the match alone: accepting, rejecting, screening, manipulating inputs,
> following nudges, and trying to make the blind match yield a chosen rider. That helps the contrast. Nobody
> games a cut. A platform match is one step in a regime that prices, rates, sanctions, and removes.

### R3 -- Section 5, early ride-hailing source

Current:

> That much has been true since researchers first studied the app.

Replace:

> That much has been true since Lee, Kusbit, Metsky and Dabbish named algorithmic management in their
> Uber/Lyft study, and Rosenblat and Stark then made information asymmetry the center of the case.

Add Lee et al. 2015 to the note and bibliography.

### R4 -- Section 5, platform geometry citation

Insert after the Kellogg sentence:

> Stark and Pais name the platform geometry more directly: providers and users act on their own behalf, while
> the platform turns those acts into management without giving either party authority. That is the sideways
> relation this section needs.

Add Stark and Pais 2020 to the note. If the author wants the broader organization-theory frame, add Stark
and Vanden Broeck 2024 as a see-also rather than crowding the body.

### R5 -- Section 5, surge and Dubal

Current:

> All I can say is that surge has not been shown to know who the two parties are -- a model that abstracts
> away from identity establishes nothing about identity.

Replace:

> Surge has not been shown to know who the two parties are. Dubal's contrary example is a surge multiplier,
> but she gives it as an illustration, not a measurement: her verb is "may," and the personalization claim
> rests on analogy with consumer price discrimination. A model that abstracts away from identity establishes
> nothing about identity either.

### R6 -- Section 5, Binns method gloss

Current:

> an audit built from drivers pooling their own subject-access data -- 1.5 million trips, 258 drivers --

Replace:

> an audit built from drivers pooling records they obtained from Uber through data-access requests -- 1.5
> million trips, 258 drivers --

### R7 -- Section 5, Dubal self-scruple

Current:

> I will assert the differential pay and leave the personalisation where she leaves it.

Replace:

> The differential pay is supported; the personalisation stays where she leaves it.

### R8 -- Bibliography / notes

If R2 is used, remove "Abstract consulted only" from Cameron's bibliography entry. Add:

> Lee, Min Kyung, Daniel Kusbit, Evan Metsky, and Laura Dabbish. "Working with Machines: The Impact of
> Algorithmic and Data-Driven Management on Human Workers." In *Proceedings of the 33rd Annual ACM
> Conference on Human Factors in Computing Systems*, 1603-1612. New York: ACM, 2015.

Add:

> Stark, David, and Ivana Pais. "Algorithmic Management in the Platform Economy." *Sociologica* 14, no. 3
> (2020): 47-72.

Optional see-also:

> Stark, David, and Pieter Vanden Broeck. "Principles of Algorithmic Management." *Organization Theory* 5,
> no. 2 (2024).

## Standing author tasks this lens cannot close

1. Save Cameron's full text or PDF and update the notes only after the author has read the body. I could
   retrieve it in this session, but the chapter should not silently rely on a source the author has not
   opened.
2. Shepardize the Ninth Circuit deactivation case before press. The chapter correctly marks it as a
   preliminary-injunction ruling, but litigation can move.
3. Archive living platform pages used elsewhere in the chapter. Uber, Lyft, and Amazon pages change without
   preserving the version the chapter saw.

## What this lens is not judging

I am not judging the film-narrative account in section 4, the Austin evidence in section 3, the streaming
distribution argument in section 7 except where it depends on section 5's powers, or Chicago hygiene beyond
the platform-studies notes named above.
