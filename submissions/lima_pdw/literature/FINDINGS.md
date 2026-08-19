# What the hearings change

Written 2026-08-19, from the Phase 1 construct hearings in [`steelmans/`](steelmans/) and the Phase 2
architecture memos in [`models/`](models/). The plan that asked for both is
[`../manuscript/RESEARCH_PLAN.md`](../manuscript/RESEARCH_PLAN.md). Nothing here is an edit to
[`../manuscript/PAPER.md`](../manuscript/PAPER.md); the sentences are the author's.

## From the Phase 1 hearings

## One claim in the draft is falsifiable as written

**§3, AI Literacy: "none names another person."** Long and Magerko's tenth competency is called **Human
Role in AI**. A reviewer with the table finds it immediately, and the sentence is absolute enough that
finding it is enough. The claim survives narrowed, and the narrowing is stronger than the original:
*no competency names another person as a party to the interaction*, and the one competency that names
humans at all names them as the system's designers and supervisors. `cards/long2020.md` carried the
same absolute sentence and is narrowed with it.

**Verified against the camera-ready** (Internet Archive; ACM refused every route and the authors' own
copy no longer resolves). Competency 10 reads: "Recognize that humans play an important role in
**programming, choosing models, and fine-tuning AI systems**." Every instance of "collaborate" and
"communicate" in the paper points at AI or sits in the *design considerations*, where peer
collaboration among learners appears as Design Consideration 11 — **other humans are in the pedagogy
and never in the competencies**. The grouping is 4 / 2 / 9 / 1 / 1 across the five questions. All
seventeen are transcribed at [`steelmans/longmagerko2020.md`](steelmans/longmagerko2020.md); cite by
competency number, not page.

Two things the full text hands us rather than costs us. They place AI literacy in the **literacy
family** exactly as the locked introduction does — literacy, then digital, computational, scientific,
data — so the parallel is not ours alone and saying so pre-empts a reviewer. And their **selection
rule** (does it reflect the definition, is it supported by numerous sources, is it useful to designers)
admits a competency on the literature's agreement, which makes §4's claim to *derive* rather than
collect sharpest against their rule rather than against their count.

## One verification passed, and the plan's condition is discharged

**Zhou items 5, 8 and 11.** The plan required checking the working-paper transcription against the
journal before quoting items as final. The journal version was on the dissertation shelf all along —
`dissertation/research/sources/pdfs/zhou2025_algorithmic_competency.pdf`, APJHR 63: e70004, open
access. All twelve items, both loading sets, the dimension assignments and the numbering match
[`ZHOU_2025_INSTRUMENT.md`](ZHOU_2025_INSTRUMENT.md) exactly. Two typographic differences, neither
substantive. **The instrument file may now be cited as final**, and Zhou should be cited to an article
number, not a page range.

## Three cheap upgrades, each half a sentence

**§3, Zhou: the appeal item.** *Remediating* item 6 reads "I can use platform APP functions (i.e.,
reporting exceptions and appealing) to resolve vulnerabilities in AM," and the interview behind it is
"When receiving unfair ratings from customers, I can use evidence like recordings to appeal to the AM."
A worker disputes the customer's rating **to the algorithm**. That is the only place in the rival scale
where anyone contests an outcome, and the contest is routed to the apparatus — our claim about the form,
appearing as a validated item in someone else's instrument. It also pairs with §5: our first respondent
never contested an outcome because no channel read as the place for it. Zhou's workers have the channel
and it still does not reach the counterpart.

**§3, Hancock: quote the body definition, not the abstract.** The article states the definition twice.
The abstract says "interpersonal communication in which an intelligent agent…"; the *Conceptualizing
AI-MC* section says "mediated communication between people in which a computational agent operates on
behalf of a communicator by modifying, augmenting, or generating messages to accomplish communication
or interpersonal goals," introduced as the authors' formal definition. §3 quotes the abstract. Both are
theirs, so this is not an error — but the body version puts "between people" inside our own quotation
and pre-empts the objection that we flattened a triad. This is the single most exposed hearing in §3
and it costs nothing to armour it.

**§3, Rahman: the private feedback, and the eighteen clients.** Rahman interviewed 18 clients and
recorded, per client, whether they knew how their actions moved a freelancer's score — because the
platform blocked the direct route: "Registered freelancers could see a client's full profile only after
applying for their job, and even then, TalentFinder withheld their contact information." And the
platform told clients their rating "will be kept anonymous and never shared directly with the
freelancer." **That is the counterpart's judgement, routed through the system and withheld from the
person it judges — our structural claim, documented as a 2015 interface decision.** One sentence in §3
converts Rahman from a boundary into the paper's best independent evidence that the position exists.

## One finding that bears on the review's first item

The live review's finding 1 proposes repairing §4's Spitzberg and Cupach citation, on the grounds that
their relational model rejects competence-as-individual-ability. **Spitzberg (2006), which we have in
full, supplies the same result without waiting on a library copy of the 1984 book.** He writes that
"competent interactants can facilitate the competence of cointeractants" and that "an incompetent
interactant can diminish a normally competent cointeractant's performance," and every outcome criterion
in his model is perceived or felt by the partner: appropriateness is "perceived legitimacy or fit of a
message to the context," satisfaction is "positive affect associated with fulfillment of positively
valenced expectancies." The book stays on the acquisition list, and the argument no longer waits on it.

The consequence for §4 is the review's own: our arrangement does not lower the score on his criteria.
**It removes the instrument**, because the party who administers the judgement never reaches a position
from which she could render it.

## What the hearings confirmed, with nothing to change

- **§3's Spitzberg hearing.** The five-part model, the four skill clusters, the five context facets and
  "the hypothesized structure did not appear as drawn" all check out. His own words: the items "were not
  as multidimensionally complex as originally anticipated," and factor analysis yields "four reliable
  factors that roughly parallel motivation, knowledge, skills, and outcomes."
- **§3's Rahman hearing.** The five components are quoted accurately against his one-sentence statement
  of them, and the reactivity typology, the two mechanisms and the 2015 Success Score are all correct.
- **§3's Zhou hearing.** Accurate to the journal, including item 8 verbatim and the α of .85.
- **§3's Hancock parameters.** Magnitude, medium, optimization goal, autonomy, role orientation are the
  authors' own vocabulary. Synchronicity is a sixth and can stay out.

## From the Phase 2 architecture memos

### The prior-art exposure has a second and third instance, both in *ASQ*

The 19 August review found that §3's "the missing piece is a position" is falsifiable by Katsh and
Rifkin's fourth party. Reading Cameron and Curchod as architecture turned up two more, and both are in
the journal this paper is aimed at.

**Curchod, Patriotta, Cohen and Neysen (2020) named the triad outright**, in *ASQ* 65(3):

> First, in place of traditional dyadic exchanges, customer reviews enact triadic relationships among
> the platform operator, buyers, and sellers that generate multiple accountabilities.

Their central mechanism is our asymmetry in their own words — buyers keep "their track record hidden,
their identity private, and their direct e-mail confidential" while "the track records and details of
sellers were visible to all" — which they call a **visibility gap**. They add a second mechanism the
paper has not named: an implicit **coalition of interests between a mass of invisible buyers and a
distant platform owner**. `PAPER.md` §2 cites them once, for ratings that cannot be carried to another
site. That is the least of what they show.

**Cameron (2024) drew the geometry**, in *ASQ* 69(2), Table 1: geometry of control arrangement is
*dyadic* in manufacturing, *triadic* in service, *triadic or quadratic* in on-demand work, whose system
of production she calls the "algorithmic labor triangle: app–worker–customer—(merchant)."
**`PAPER.md` does not cite Cameron at all.**

Scoped to *competence constructs*, §3's close survives both: neither theorises a competence. Unscoped,
it does not. The repair is the review's own repair, applied twice more — concede the antecedent, keep
the question. And the concession pays: a paper arguing that this arrangement has three parties is
stronger when it can say the geometry is already recognised in the venue, and that what is missing is
not the diagram but a competence written for it.

Two things worth taking rather than defending against. Curchod's **visibility gap** is a published
antecedent for asymmetric interpretation. Their **coalition** names why the counterpart is not available
as an ally — her interest and the platform's are joined in the evaluation procedure — which is sharper
than "the algorithm sits between them."

### Three ASQ papers, one genre convention

Rahman, Cameron and Curchod independently order their findings the same way: **establish the condition
completely, then report the conduct**. Rahman spends half his findings proving the cage is closed before
any worker acts. Curchod separates the two levels of asymmetry from "Sellers' Working around the
Algorithm." Cameron establishes the segmented work structure before the tactics. All three keep theory
under a fifth of the article and let findings be the largest block. The memos in [`models/`](models/)
carry the section skeletons, page budgets, and what does not transfer at our N.

Two concrete jobs that cost little: **a comparison table in §2** (Paper 1's six questions across five
forms, which §2 currently narrates and which would make the open cell visible rather than asserted),
and **the protocol block structure as an appendix** in §5 — Curchod prints his interview protocol in
full, and this venue expects the instrument to be inspectable.

## From the field-level and instrument work (added later on 2026-08-19)

### §3 can stop sampling and start reporting a property of the field

Three reviews audit the whole algorithmic- and AI-literacy field:
Oeldorf-Hirsch and Neubaum (**50** studies reviewed of 96 screened, four databases), Gagrčin, Naab and
Grub (**169** studies), and Iyamu and colleagues (**12** studies, seven databases, a scoping review of
health workers). Two were read at full text; Gagrčin is abstract-only and labelled as such.
[`steelmans/field_stocktakings.md`](steelmans/field_stocktakings.md).

The strongest result is not a word count, though the word counts hold — "interpersonal" appears zero
times in either full text, and "communicative" zero times in Oeldorf-Hirsch and Neubaum. It is that
**Iyamu and colleagues looked for the counterpart-facing competence and found the field had left the
slot empty.** Their charting framework is Nutbeam's, whose third level is *communicative*: "interacting
with AI systems and explaining AI-mediated information," including "supporting patients to do so." Their
finding: "communicative literacy was largely absent from both conceptual frameworks and measurement
instruments," and the one study that came closest described it "in relation to integrating AI systems in
workflows and collaborating effectively with them rather than competencies related to explaining
AI-mediated information, negotiating uncertainty, or supporting patient and community decision making."

A framework supplied the slot; the literature filled it with more system-facing measurement. That
converts §3's close from a claim about seven readings into a documented property of a field — and it
carries a scope condition, because Nutbeam's level *is* about a second human, so §3 cannot say the field
never mentions another person.

Two more things worth taking. Both field definitions — DeVito's and Dogruel's, quoted in the memo — have
exactly two terms, a user and an algorithm. And Oeldorf-Hirsch and Neubaum's measurement problem, that a
researcher cannot score correctness because the algorithm is unknown to her too, is a published argument
for defining the competency on what a person *does* rather than what she *knows*, which is what the
locked definition already does.

### The fourth party is an antecedent, not a rival

[`steelmans/odr_fourth_party.md`](steelmans/odr_fourth_party.md) gives the eighth hearing §3 lacks.
Katsh and Rifkin named the fourth party in 2001 and Wing, Martinez, Katsh and Rule revisited it in 2021
with machine learning in the systems. The literatures divide cleanly: **ODR asks what the system owes
and answers for its design; algorithmacy asks what a party must be able to do.** Their four ethical
requirements — transparency, accountability, contestability, consent — are close to the negation of what
§4 says the form withholds, which makes the withholding list principled rather than assembled. Written
at card depth, and the memo says so at the top: both sources are unretrievable right now.

### The harness is a strong collection instrument with no analysis instrument

[`../interview/METHODS_AUDIT.md`](../interview/METHODS_AUDIT.md) checks every rule in `AGENT.md` and the
protocols against the methods literature §5 cites. Nine rules have warrants in that literature and none
of them says so — the incident rule is Pratt's showing-not-telling enforced at collection, the
no-vocabulary rule is Bowen's sensitizing concepts kept from sorting the data, the verbatim markers are
Gioia's in-vivo discipline, the `reviewed_by_human` gate is an inspectable consent trail of the kind
Pratt, Kaplan and Whittington argue for.

**What does not exist is the analysis half.** §5 claims abductive analysis, first-cycle coding in the
participant's words, a declined data structure and bricolage. There is no codebook, no coding rule, no
memo file, no discard log, no negative-case register. The abduction claim is the one that bites, because
abduction has machinery: Timmermans and Tavory define it as inference from **surprising** evidence and
name three processes — revisiting, defamiliarization, alternative casing. A design that never records
what surprised the analyst cannot be abductive. The audit proposes four short files that would fix it,
none of which touches `PAPER.md` or requires a response to exist.

Four other gaps, in the audit: there is no sampling rule (Pratt's "enough is a function of the question"
needs the question's demands stated, and the open invitation is recruitment rather than sampling); no
saturation rule if anyone ever says enough; Tracy still orphaned though the audit shows her doing real
work in the instrument; and the protocols do not record whether a block finished with an incident or a
characterisation, which is the thing the paper claims they enforce.

## Checked while the memos were being written

**"Several responses" is one response.** The intake bucket holds a single object as of 2026-08-19.
§5 says "We have obtained several responses" and the **locked abstract** says "several responses
obtained to date." This is the number the 19 August review's finding 6 asked for, and correcting the
abstract requires an unlock. Full note, with what was and was not checked, at
[`../AGENDA.md`](../AGENDA.md) item 7. No response content was read, quoted, or written anywhere in
this repository.

## Still to acquire

1. ~~**The ACM competency table** for Long and Magerko~~ — **closed 2026-08-19** from the camera-ready
   on the Internet Archive. All seventeen are transcribed. Phase 1 leaves no gap.
2. **Spitzberg & Cupach (1984)**, the book. No longer gating §4 (see above), still the honest source for
   anything attributed to it directly.
3. **Page anchors** for Spitzberg (2006), Hancock et al. (2020) and Long & Magerko (2020). The first
   two were read from publisher HTML and the third from a camera-ready. One library session fixes all
   three. Long and Magerko can be cited by competency number in the meantime.
4. **One later empirical HMC study and one later empirical AI-MC study**, so those two are not only
   agendas. Not hinges, per the plan.
