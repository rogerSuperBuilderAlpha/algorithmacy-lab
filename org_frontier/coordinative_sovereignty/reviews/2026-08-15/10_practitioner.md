# Reviewer 10 — Dorian Ekwueme · trade-association policy analyst

`10_practitioner.md` · panel of 2026-08-15 · manuscript: `chapter/chapter_v2.md`

---

## 1. Who I am

I run policy for a European association of small software firms and marketplace sellers — about six
hundred members, median headcount eleven, the largest around two hundred. I am not an academic. I have
a law degree I stopped using in 2016 and nine years of filing consultation responses, drafting board
papers, and sitting in DG CONNECT stakeholder rooms where my members get four minutes. Right now I have
two things on my desk: a board meeting in September at which I have to explain why our app-store
workstream produced a fee schedule instead of a market, and a consultation response on the Digital
Omnibus that has to argue against the P2B repeal without sounding like an association defending its own
grievance procedure. A member of our academic advisory group sent me this chapter with the note "the
diagnostic is the bit." I came to it wanting one thing: a defensible way to tell my board which of our
dependencies are worth fighting and which are worth negotiating, in language a Commission official will
accept. I came in sceptical, because I have read a lot of academic work on platform power and almost
none of it survives contact with a firm that has forty employees and no legal budget.

## 2. Step 0 — register and bar

The register is an academic chapter for an academic volume, and I am judging it as such. I am not going
to complain that it is 15,000 words, that it has no executive summary, or that it cites Bodin. Those are
the genre, and the genre is not mine.

**What I will judge hard:** §5's diagnostic, §7's instrument table, and §8's decision procedure. Those
three are addressed to me — §8 explicitly ("the diagnostic gives managers a decision procedure"). If a
procedure is addressed to a practitioner, it has to run on a practitioner's information set. That is the
whole of my bar, and I will apply it without mercy, because it is the only thing I can give this panel
that the other nine reviewers cannot.

**What I will let pass:** §2, §6, §9, all citation form, the masked self-citations, the absence of first
person, and every question about whether Habermas is being read correctly. I skipped most of §2 and
almost all of §6 on the first pass and I will report honestly on what that cost me (part 3, §6 entry).

**How I ran it.** I took a real member profile: a Netherlands-based ISV, forty employees, a scheduling
and rota product for small clinics and salons, sold as a mobile app with an in-app subscription. Eighty
percent of revenue arrives through one application store. A further fifteen percent arrives through a
vertical SaaS marketplace where the product is listed as an integration partner to an accounting suite.
The remaining five percent is direct enterprise sales. Call the firm Vantor. Everything below is Vantor
run through §5 and §8, function by function, with the stalls written down where they happened.

---

## 3. Part 1 — the read

### 3.1 Running §5's diagnostic on Vantor, function by function

§5.4 tells me to classify functions rather than firms, so I broke the store into the eleven things it
actually does for Vantor. §5.2 gives me the operation: restore the direct developer-to-user tie and
recompute whether the mediator still binds. §5.2's joint-determination criterion gives me the test for
necessity: does the function produce a determination that depends jointly on both parties and that
neither could produce alone.

| # | Function | Bypass verdict | Could I actually reach it? |
|---|---|---|---|
| 1 | Binary distribution and update delivery | contingent (architectural, not integrating) | **stalled — "comparable cost" undefined** |
| 2 | Search ranking inside the store | splits by buyer segment | **stalled — split not computable** |
| 3 | Payment and commission collection | contingent (chapter classifies it for me) | yes |
| 4 | Identity and entitlement (who holds a valid subscription) | reducible, bundled to #3 | yes |
| 5 | App review / update approval gate | **contingent by the test, unbypassable in fact** | classified, and the verdict is wrong for me |
| 6 | Ratings and reviews shown to buyers | splits by buyer segment, as #2 | stalled with #2 |
| 7 | Refund and billing dispute adjudication | necessary (joint determination) | yes — and this surprised me |
| 8 | OS permission and privacy-label enforcement | **no cell in the taxonomy** | no |
| 9 | Editorial featuring | splits by buyer segment, as #2 | stalled with #2 |
| 10 | Demand aggregation (introducing buyers who would never have found Vantor) | necessary | yes, in principle |
| 11 | First-party competition (the store ships a rival scheduling feature) | **no cell in the taxonomy** | no |

Six of eleven I can classify. Three stall on missing information. Two fall outside the framework
entirely. Below, the ones that matter.

**Where it worked.** Function 3 is the chapter's own worked example and it holds up under my hands.
"Node says necessary and edge says contingent, on the same function, in the same firm" is exactly what
Vantor's payment gate is, and I have never had a clean way to say that. Function 7 is the pleasant
surprise: apply the chapter's joint-determination criterion honestly to refund adjudication and it comes
back **necessary**, because a refund decision genuinely depends on both the buyer's claim and the
developer's evidence and neither party alone can commit the outcome. That is right, it is
counter-intuitive, and it means the chapter is telling Vantor to build voice over the store's dispute
process rather than over its commission. That is better advice than my association currently gives, and
the chapter never notices it has produced it. **[FIX IF TIME]** — one sentence in §5.4 naming dispute
adjudication as a necessary function would earn the section its keep with practitioners.

**Stall 1 — "comparable cost" has no threshold.** §5.2 asks: "Could these two parties reach each other
at comparable cost if no rule, contract, or architecture stood in the way?" Comparable to whom? For
Vantor, self-distributing a signed binary means an installer, an update channel, a code-signing story,
and a support burden for OS security warnings — call it two engineer-quarters and a permanent tail. A
two-hundred-person member absorbs that. Vantor does not. So function 1 is contingent for one member and
necessary for another, on the same platform, in the same market, and the chapter's own text says the
diagnostic "sorts functions for a given dependent party." Consistent — but it means the classification
is a function of firm size and the chapter never says so. The moment I put this in front of a board, the
first question is "compared to what budget," and I have no answer from the text. **[FIX NOW]** — one
clause fixing the reference point ("at a cost the dependent party could bear without changing its scale")
turns an unanswerable question into an answerable one.

**Stall 2 — the segment split is not computable from what a firm holds.** §5.2's traveler example is the
core of the framework and it is the point where I lost the ability to run it. Ranking is contingent for
the buyer who already knows Vantor and necessary for the buyer who does not. To get a verdict I need the
proportion. The store gives me install source attribution and partial search-term data, so I can get
close on *how* people arrived. What I cannot get, and what nobody but the platform holds, is the
counterfactual: of the buyers who arrived through generic search, how many would have found Vantor
through another route. That is a demand-substitution estimate. The platform has it; I do not; no
regulator has ever ordered it disclosed. So the framework's central classification, on the function that
decides eighty percent of Vantor's revenue, resolves to "somewhere between contingent and necessary,
proportion unknown." **[FIX NOW, cheaply]** — the chapter should say plainly, once, that the segment
split is the information the platform holds and the dependent party does not, and that a firm should run
the diagnostic on the *conservative* assumption (treat the discovery share as necessary) until it can do
better. That is a two-sentence fix and it converts a stall into a rule.

**Stall 3 — the app review gate, and the constraint that is not a rule.** This is the finding I most want
the author to read. §5.2 defines a contingent mediator as one whose "position rested on the absence of the
direct tie, an absence usually held in place by an external constraint," and every worked example makes
that constraint a rule or a contract — franchise law, a parity clause, an anti-steering term. Run the test
on app review: restore the direct tie and the review gate has no force over a direct install, and review
depends only on Vantor's submission, not jointly on Vantor and the buyer. Verdict: **contingent**.

That verdict is wrong for my members in every way that matters. Review is the function that ends
businesses — an arbitrary rejection three days before a launch, a policy reinterpretation applied
retroactively, an update held for a fortnight with no reasons that survive reading. And it is
unbypassable, not because a contract forbids the bypass but because the buyer will not install software
that has not passed a gate, and the operating system is built to make sure of that. The constraint is
buyer trust and platform architecture, and neither is liftable by the instruments the chapter prescribes
for contingent mediators. "Interoperability, portability, break the lock-in" does nothing to a rejection.

So the taxonomy has a hole: a function that is contingent by the structural test and unexitable in fact,
because the constraint holding it is not a rule anyone can repeal. The chapter's own hedge — "*usually*
held in place by an external constraint" — is where the hole hides. **[FIX NOW]** — either name the case
or restate the criterion. Draft in part 5.

**Stall 4 — the tolled bypass.** Vantor's payment gate is the chapter's flagship contingent function, and
Europe opened it. My members implemented external purchase links. What arrived was not exit; it was a
revised fee schedule that priced the outside route at close to the inside one. The bypass is open and
nobody uses it, because the mediator sets the price of the bypass.

The chapter has no cell for this, and it matters because it is the *normal* outcome, not the exception.
§5.3 treats bypassability as "the availability of exit" and §7's table says anti-steering remedies "open
the bypass" against a contingent mediator. Both are true and neither is sufficient: a bypass whose toll
the mediator sets is a repriced gate. The chapter's hotel case is read as classification error ("a hotel
that spent the decade trying to leave mistook the necessary function for the contingent one"). My read
of my own sector is different: we classified correctly, we won the remedy, and the gatekeeper repriced.
Those are two different failure modes and the chapter only has one. **[FIX NOW]** — this is the single
most important addition for a practitioner reader, and it costs a paragraph. Draft in part 5.

**No cell — the mediator as competitor (function 11).** The store ships a first-party product that
overlaps Vantor's. §3.3 gets within touching distance ("a mediator optimizing for objectives of its own
reshapes the coordination around those objectives") and then §5's diagnostic never asks whether the
mediator competes with the party being classified. Self-preferencing is the single largest item in every
consultation response my association has filed in four years. A framework for platform-dependent firms
that has no cell for it will read, to anyone in my job, as written from outside. **[TOO LATE — CARRY
FORWARD]** — this is a section, not a sentence, and it is the obvious extension paper.

**No cell — the non-triadic dependency (the marketplace channel).** Vantor's other fifteen percent runs
through a SaaS marketplace, and the binding dependency there is not the listing; it is the host product's
API. If that API changes, Vantor's product stops working. The API is not a mediator standing between two
parties — it is an input — so the diagnostic has nothing to say about it, and §2.3 has already handed the
"industrial strand" off with the line "the literacy frame reaches it only partly." Fine as scope. But it
means the framework covers one of my members' two standing dependency problems. **[FIX IF TIME]** — a
scope sentence in §5.4 saying the diagnostic covers mediated coordination and not technical dependency
would stop a practitioner reader from expecting more than is on offer.

### 3.2 Running §8's decision procedure — what I do on Monday

§8: "Where it depends on a necessary mediator, exit is closed and the move is toward voice: organize with
other dependent firms, pool data, demand contestable systems, seek a standing channel of governance."

For Vantor, the diagnostic returns *necessary* on demand aggregation, on refund adjudication, and — on my
own conservative rule — on the discovery share of ranking. That is most of the revenue. So the verdict is
"necessary, build voice." Here is what I can actually do with each of the four instructions.

**"Organize with other dependent firms."** Already done. This instruction describes my own existence. My
members joined an association a decade ago and it is why they have four minutes in the room instead of
none. The chapter's first move is a move my sector completed before the chapter was written, and it has
nothing to say about what an association does *after* it exists. That is not a defect of the argument, but
it is the reason §8 reads thinner to me than it will to a reviewer who has not tried it.

**"Pool data."** This is the one genuinely operational instruction in the chapter, and I can start it on
Monday. Concretely: a shared incident register across members — dated ranking positions by keyword,
rejection notices with the cited policy clause, review turnaround times, revenue-by-source exports,
fee-schedule changes with effective dates. Standard fields, association-held, member-anonymized for
publication. Two weeks of my analyst's time to specify, one meeting to get sign-off.

But notice what I am pooling. The chapter's data-trust paragraph (§7) is about pooling *the data the
mediation runs on* — personal data, under a fiduciary, via the DGA and now the Data Act. That is not what
I would pool and it is not reachable by a forty-person firm anyway. I would pool **observations of platform
behavior**: the evidence base that turns forty separate anecdotes into a pattern a regulator can act on.
The chapter has no instrument for that, it is the cheapest instrument my sector has, and it is exactly
what §3.2's Ananny-and-Crawford point implies — a disclosure that no party can act on produces nothing,
and the counterpart is that an *observation* many parties pool produces standing. This is the missing
page (part 6 below).

**"Demand contestable systems."** Of whom? Vantor cannot demand anything of the store. It can ask my
association to ask the Commission. That is a two-step the sentence does not contain, and stated flat it
reads to a practitioner as a wish.

**"Seek a standing channel of governance."** Same problem, worse. The one standing channel a business user
actually had in European law is the P2B Regulation's internal complaint-handling and mediation, and §8
itself reports that the Commission has proposed to repeal it. So the chapter tells Vantor to seek a
standing channel four paragraphs after telling it the channel is being withdrawn, and never connects the
two. **[FIX NOW]** — connecting them is one clause and it converts §8 from advice into an argument I can
put in a consultation response.

**Monday, honestly:** I open the incident-register spec, I put "revenue behind necessary functions" on the
September board agenda (see below), and I add one paragraph to the Omnibus response using the chapter's
P2B sentence. Three actions, one of which the chapter gave me and two of which I bring. That is a real
payoff and a smaller one than §8 implies.

**The board metric the chapter hands me and never states.** Running the diagnostic across Vantor's
functions produces a number: the share of revenue sitting behind necessary functions versus the share
behind contingent ones. The first is a governance exposure that will not go away and has to be managed
for years; the second is a project with an end date. I would put that split on a board slide tomorrow.
The chapter contains everything needed to produce it and never says it. **[FIX NOW]** — one sentence in
§8. It is the highest ratio of practitioner value to authorial effort anywhere in the manuscript, and
draft text is in part 5.

### 3.3 §7's table — how many of seven can a forty-person firm reach?

I scored each row twice: reachable by Vantor acting alone, and reachable by my association acting for
Vantor.

| Instrument | Vantor alone | Association | Note |
|---|---|---|---|
| Interoperability and portability | no | partly | Only a regulator deploys it; we can advocate. |
| Antitrust and anti-steering remedies | **yes** | yes | Vantor can *use* an existing remedy; informing the Commission of non-compliance is cheap. VERIFY the mechanism. |
| Contestability of individual decisions | **yes** | yes | Via P2B complaint-handling and mediation, not GDPR Art. 22 — Vantor is not a natural person. Being repealed. |
| Collective bargaining | **no, and legally hazardous** | conditionally | See below. |
| Data trusts and data intermediaries | no | partly | DGA registration is not a forty-person burden. |
| Cooperative ownership | no | no | Building a rival app store is not on Vantor's agenda in any decade. |
| Oversight boards | no | no | A firm cannot create one; it can only appear before one that exists. |

**Two of seven, and one of those two is being repealed.** That is the honest count, and it is the answer
to the question the brief put to me. §7 is a good table with the wrong column headings for its stated
audience. It sorts instruments by *what they do to a mediator*, which is a policymaker's question, and
the chapter says so in its own last line ("the diagnostic is what tells a policymaker where to put each
one"). But §8 then hands the same repertoire to a manager. The mismatch is the chapter's main
practitioner defect and the fix is a third column. **[FIX NOW]** — draft in part 5.

**The collective-bargaining row is a legal problem, not a framing one.** §7: "Where platform workers or
platform-dependent firms can organize, they can negotiate over how assignments are made, how deactivation
is decided, and how ranking is governed." For workers, fine. For **firms**, that sentence describes
independent undertakings coordinating their commercial terms through an association, which is the thing
competition law exists to prohibit. There are routes — advocacy, joint representation before a regulator,
the exemptions that cover genuinely dependent self-employed — but a bare "platform-dependent firms can
negotiate" is not one of them. If I lift that sentence into a board paper, our counsel strikes it, and if
a member acts on it I have a problem. This is the one place in the chapter where following the advice
could hurt a member. **[FIX NOW]** — one clause. Draft in part 5.

**One row is undersold.** "Contestability of individual decisions | marginal | voice at the level of the
case." Against a *contingent* mediator, case-level contestation is not marginal for a firm — it is how the
pattern gets documented. Forty complaint records with dated rejection reasons are the raw material that
gets a regulator to open a bypass. The chapter's own §3.2 argument (reading without a channel to act
produces nothing) has a mirror image it never states: complaining without a pooled record produces
nothing either. **[FIX IF TIME]**

### 3.4 Where the chapter loses me, with the sentence

- **§2.1, first sentence:** "Before writing, speech and memory carried authority, and law was what the
  elders could recite." I stopped reading here and resumed at §2.3's last two paragraphs. No cost.
- **§5.1:** "The companion paper develops measures that grade the borderline cases, where the answer is
  close or the parties are many (Author, 2026)." This is where I stopped trying to run §5.1. I am told a
  test exists, told I cannot have it, and given a section heading that promises a procedure. §5.1 as it
  stands is a distinction without an operation. **[FIX IF TIME]** — a two-line rule of thumb ("if
  removing either party's input changes the determination, treat it as constitutive") would let a
  practitioner do the step instead of noting that it exists.
- **§5.3:** "Bypassability is the availability of exit, and necessity does not produce voice: it
  forecloses exit and leaves voice as the residual lever, one available against contingent third parties
  too and the only one left where the third party is necessary." I read this three times and diagrammed
  it before it resolved. One sentence carrying four relations. **[FIX IF TIME]**
- **§6:** I read the first sentence of each paragraph and skipped the rest. Nothing in it changed an
  action. Verdict on the theory apparatus is in part 3.5.
- **§7, collective bargaining:** the sentence quoted above. It loses me because it is wrong, not because
  it is dense.

### 3.5 Does the theory apparatus earn its space for me?

Asked directly, so answered directly: **no, twice over, with two exceptions I would fight to keep.**

I skipped §2.1 and §2.2 entirely and lost nothing I needed. I skipped §6's four strands — republicanism,
relational autonomy, Markell, Ostrom — and lost nothing that changed a decision.

The two exceptions:

1. **§2.3's closing paragraph.** "Faced with platform coordination the literate response is to demand more
   disclosure, more documentation, more rights to read, because reading is what the literate know how to
   do." That is the most useful paragraph in the first half of the chapter for my work. It is the reason
   my sector has spent four years asking for transparency duties and getting them and not getting better,
   and it is going into a consultation response. Keep it; it does not need §2.1 or §2.2 in front of it.
2. **§6's Ostrom and Schlager paragraph.** "Not collective ownership of the platform but collective-choice
   arrangements over the coordination's rules, standing the owner cannot unilaterally rewrite without
   contest." That is precisely the ask I want to put to the Commission, and Schlager and Ostrom give it a
   respectable name that is not "we want a seat." Genuinely valuable. It does not need the three strands
   that precede it.

So roughly two paragraphs out of perhaps four thousand words of theory do work for a reader like me. I am
not telling an academic volume to cut its theory — that is the genre and other reviewers own that
question. But the author asked, and the answer is that a practitioner reader reaches §5 by skipping, and
the chapter would lose nothing with me if §2 and §6 were half their length.

---

## 4. Part 2 — style and slop audit

I am not the panel's prose reviewer, so this is short and confined to things that impede a
non-academic reading.

1. **Verbatim refrain.** "the tie that strict mediation forbids" appears in §1 and again in §5.2, and
   "restore the direct tie" recurs four times across §1, §5.1, §5.2, §5.5. The first repetition read as
   emphasis, the third as filler. Vary or cut the §1 instance.
2. **Self-narrating rigor.** §3: "Three things have to be kept apart to see what is actually new." The
   brief flags this pattern. Rewrite: "The coordination logic is old. So is the topology. What is new is
   what their conjunction does to governance."
3. **Instruction to the reader.** §3.3 opens "Attend to what the mediator captures and the stakes come
   into focus." Rewrite: "What the mediator captures sets the stakes."
4. **A fifty-word sentence with four coordinating ands.** §2.2: "A written rule persists while memory
   drifts, travels without its author, and can be laid beside another writing and compared, and these
   three properties — persistence, portability, and comparability — made a new scale of coordination
   possible, and with it a new kind of political authority." I lost the thread at "and these three
   properties." Split after "compared."
5. **Restatement.** §5.2 ends "and the answer varies by actor," then the next sentence says "A mediator's
   classification therefore depends on which coordination is being asked about." Same claim twice. Cut
   the first.

Against that: the abstract's opening sentence, "None of it will show up on a compliance audit," and "Node
says necessary and edge says contingent, on the same function, in the same firm" are the best-written
practical sentences I have read in an academic chapter this year. Whatever the v2 rewrite did to those,
it worked.

---

## 5. Part 3 — paste-ready revisions

Written in the chapter's register: named agents, no first person.

**(a) §7, replacement table with a bearer-and-reach column.** This is my single most important fix. It
costs one column and converts a theory table into an instrument a firm can act on.

| Instrument | Against a contingent mediator | Against a necessary mediator | Who can invoke it |
|---|---|---|---|
| Interoperability and portability | restores exit | access on regulated terms, which is voice | a regulator; dependent parties only through advocacy |
| Antitrust and anti-steering remedies | opens the bypass | alters conduct, not dependence | a regulator or a complainant; a dependent firm can use a remedy already granted |
| Contestability of individual decisions | documents the pattern that justifies a bypass | voice at the level of the case | a natural person under Art. 22; a business user under the P2B complaint and mediation route |
| Collective bargaining | marginal | voice at the level of the rule | workers and their representatives; firms only within the limits competition law sets on associations of undertakings |
| Data trusts and data intermediaries | leverage toward exit | leverage toward voice | a collective with the capacity to register and administer one |
| Cooperative ownership | may fund an alternative | changes the owner, not the leaveability | a collective with capital at the required scale |
| Oversight boards | marginal | voice, bounded by the constituting platform | the platform constitutes it; dependent parties appear before it |

**(b) §7, collective-bargaining paragraph, added clause.** After "Where platform workers or
platform-dependent firms can organize, they can negotiate over how assignments are made, how deactivation
is decided, and how ranking is governed":

> The two bearers face different limits. Labour law protects the workers' case and, in Europe, now
> encourages it; competition law constrains the firms' case, since independent undertakings coordinating
> commercial terms through an association engage the prohibition on restrictive agreements, and the route
> open to dependent firms runs through representative standing before a regulator rather than through
> bargaining with the platform directly.

**(c) §5.2, the constraint that is not a rule.** After "an absence usually held in place by an external
constraint":

> The qualification matters, because not every constraint is liftable. A rule, a contract, and an
> architectural block can each be repealed, renegotiated, or mandated open, and the instruments of
> section 7 are addressed to constraints of that kind. Where the absence of the direct tie is held
> instead by the counterpart's unwillingness to transact outside the mediator — by the buyer who will not
> install software that has passed no gate, or the traveler who will not book a hotel that carries no
> rating — the function is contingent in structure and unexitable in fact, and the strategy the verdict
> implies is voice notwithstanding the classification.

**(d) §5.2 or §8, the tolled bypass.** I would put this at the end of §5.3, where exit is introduced:

> An opened bypass is not yet an exit. Where the mediator retains the power to price the alternative
> route, a remedy that restores the direct tie returns a capability whose cost the mediator still sets,
> and the dependent party's position may not improve at all. Contingency establishes that exit is
> available in principle; whether it is available in fact depends on who sets its terms, which is itself
> a question about standing and therefore about voice.

**(e) §8, the board metric.** After "and the hotels of section 5.5 show what that waste looks like at
sector scale":

> Run across a firm's dependencies, the diagnostic yields a figure a board can act on: the share of
> revenue that arrives through necessary functions against the share that arrives through contingent
> ones. The first names a governance exposure that will persist and has to be managed; the second names a
> project with a completion date. Firms that report platform dependence as a single percentage cannot
> tell the two apart.

**(f) §5.2, the practicability reference point.** Replace "at comparable cost" with:

> at a cost the dependent party could bear without changing its scale

**(g) §8, connecting the standing channel to its withdrawal.** After "seek a standing channel of
governance," add:

> The Platform-to-Business Regulation supplies the clearest existing instance of such a channel for a
> dependent firm, and its proposed repeal would close it, which is the practical stake of the
> simplification package for the actors this section addresses.

---

## 6. Verdict

**Minor revisions**, and the organizational payoff is **real but oversold** — genuinely real in §5.2 and
§5.4, oversold in §7 and §8.

That is a better verdict than I expected to give. The diagnostic is not decoration. I ran it on a real
member across eleven functions and it classified six of them, corrected one belief I held (refund
adjudication is necessary, and my association has been treating it as a service-quality complaint), and
produced a board metric the author has not noticed he has produced. Three sentences from it are going
into a live consultation response this month. Very little academic work on platform power clears that bar.

**The single most important fix:** the third column in §7's table, naming who can invoke each instrument.
Without it, §8 tells a forty-person firm to reach a repertoire that a regulator deploys, and every
practitioner reader will notice.

**The chapter's biggest genuine strength:** the node/edge distinction in §5.2, stated as "Node says
necessary and edge says contingent, on the same function, in the same firm." That is a real analytical
move, it is stated in a sentence a non-academic can carry into a meeting, and it names something my sector
has been arguing badly for four years.

**The one thing only the author can supply:** whether the necessary/contingent verdict is meant to survive
a mediator that prices its own bypass. Everything in my sector turns on that, the manuscript is silent,
and no reviewer can settle it from outside the framework.

**The one page the chapter is missing:** *What the dependent firm does with a necessary verdict, on its
own, this quarter.* Not the instrument catalog, which belongs to regulators, but the firm-level page —
who inside a forty-person company owns algorithmacy and at what fraction of a role; the evidentiary
discipline that makes every other instrument work (dated ranking records, rejection notices with the
cited clause, revenue by acquisition source, fee-schedule changes with effective dates, kept as a matter
of routine because in every proceeding the binding constraint is evidence and only the dependent firm can
generate it); what to pool with an association and what to keep; and the revenue-behind-necessary-functions
figure to take to a board. §8 gestures at "pool data" and means something else by it. This page is the
difference between a chapter practitioners cite and one they use, and it is about 500 words.

---

## 7. Citation behavior

**Would I cite it in a consultation response?** Yes, and I will. Two things specifically. First, the P2B
sentence — "which would remove the only duty in European law to disclose the main parameters of ranking
to the business users being ranked" — is the cleanest statement of our Omnibus position I have seen, and
having it in an academic chapter rather than an association paper is worth more than the sentence itself.
Second, the node/edge distinction, to argue that a function can be non-substitutable and still bypassable,
which is the argument we lose every time we make it in our own words.

**Would I circulate it to members?** No. Fifteen thousand words, and §2 loses a founder in the first three
minutes. What I would circulate is a two-page extract — §5.2 from "Triadic coordination comes in two
kinds" through the App Store paragraph, §5.4's portfolio paragraph, and §8's decision procedure — under
our own cover note. I would ask the author for permission to do that, which is the strongest signal I can
give about the work.

**Would I use it in a board paper?** Yes, three sentences and an appendix. The opening line of the
abstract is my first paragraph. "A firm that invests in regulatory compliance secures a digital position
and acquires no ability to predict or contest the algorithmic determinations that set its market
outcomes" and "None of it will show up on a compliance audit" are the two sentences that will get a board
to fund a workstream. The appendix is the Vantor table in part 3.1 of this review. I would not put the
hotel decade in a board paper — it is a contested empirical claim and I do not have the standing to
defend it if a director's spouse works in hospitality.

**What would raise it from cited to relied upon:** the third column and the missing page. With both, this
becomes the reference document my association hands new members. Without them, it is three good sentences
and a diagnostic I have to finish myself.

---

## 8. VERIFY

I am not an academic and I will not assert a legal citation I have not confirmed. Everything below is
something I believe from my job and that the author must check before press. Reviewer 05 owns the
chapter's own legal claims; these are claims *my review* rests on, flagged so the author does not adopt
them on my authority.

1. **VERIFY** — the mechanism by which a third party can inform the Commission of gatekeeper
   non-compliance under the DMA, and whether it is genuinely low-cost for a small firm. I have cited it as
   reachable in part 3.3 on the basis of practice, not the text.
2. **VERIFY** — that the P2B Regulation's internal complaint-handling and mediation provisions run to
   business users, and the article numbers, before the author adopts my claim that they are the only
   case-level channel a dependent *firm* holds.
3. **VERIFY** — the competition-law position on associations of undertakings coordinating commercial terms,
   and any exemption covering dependent self-employed, before paste-ready revision (b) goes in. The
   drafting there is deliberately general because I am confident about the risk and not about the
   boundary.
4. **VERIFY** — the external-purchase fee structures that followed the 2025 anti-steering enforcement.
   My tolled-bypass finding is drawn from what my members report, and the author should not state the
   fee mechanics in the chapter without a citable source. The conceptual point in revision (d) stands
   without them.
5. **VERIFY** — whether application-store analytics disclose install-source attribution in the form my
   part 3.1 stall assumes. If the platforms disclose more than I think, stall 2 weakens; if they disclose
   less, it strengthens. Either way the author should not repeat my characterization unchecked.
