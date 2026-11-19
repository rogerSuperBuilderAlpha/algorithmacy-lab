# Project review against the full reviews, and a gap map on the duties of the host

10 November 2026 · for Roger and Pierre · resubmission due 14 December 2026

*Drafted by Claude (Fable review agent). None of this is the authors' wording. I edited no existing file and committed nothing.*

**How to read the evidence.** Every quotation and locator below comes from a file in this project, and the file is named beside it. I had no web or database access in this run. Any work named from my own knowledge carries the tag **UNVERIFIED LEAD**: its author, year, venue and content are from memory, may be wrong, and need a Crossref or publisher record and a full read before they go anywhere near the draft. I give no page numbers for those works.

**Conflicts flagged before acting.**

1. The repo `AGENTS.md` says to commit and push after every step. The brief for this review says not to commit. I followed the brief.
2. `literature/FOUNDATION.md` (l. 642–645) advises against citing Kant directly, because "a domain reviewer reads a direct Kant citation as the paper reaching outside its field". The brief asks me to consider Kant. I list him as a lead and repeat the caveat.
3. `RESEARCH_PLAN.md` (E.1, "Exclude") told the 8 November searches to drop "liability-allocation papers without a theory of the duty's origin". Reviewer 2's full report asks for exactly that allocation (R2.2d). The exclusion rule should be lifted for the next search.
4. I know the editor's summary only through the E-rows of `REVISION_PLAN.md` ("Concern map"). The decision letter itself is not in `manuscript/reviews/journal_2026-11/`. "New" in section 1 means "not visible in those E-rows".

**The finding that ranks first.** The paper argues that an obligation survives delegation, but the sources it uses for survival (Kong, Kropf et al., Nissenbaum) are about the duty to *answer* for an outcome. The duty the paper needs is the prior one: what a host owes a guest in the first place. That first-order duty rests on one secondary quotation (King 1995, as quoted by Xiang et al. 2022), one book chapter held at metadata depth (Lashley 2000), and an anthropologist writing about Bedouin households (Shryock 2012). Reviewer 2's points 1, 2 and 4 and Reviewer 3's objection to "the single duty" all land on that gap. The authors' own diagnosis ("we just kind of assume it all the way through") is correct, and sections 2–5 below show where.

---

## 1. Review-to-plan coverage

Status key: **Addressed** = a located change answers the point. **Partly** = a change exists but does not meet what the full review asks. **Missed** = no current file answers it. Files: RP = `REVISION_PLAN.md`; PO = `PITCH_AND_OUTLINE.md` (line numbers are that file's); CF = `CITATION_FIXES.md`; RPl = `RESEARCH_PLAN.md`.

### Reviewer 1

| ID | Point | Status | Where, and what is short |
|---|---|---|---|
| R1.1 | Cite Wilson-Nash et al., "No App, No Entry" | Addressed | RP concern map R1.1; PO §7 "A real alternative" (l. 187–189); pitch l. 13 |
| R1.2 | Add host–guest negotiation literature, to show interaction that is "more than functional" and creates value for guests; suggested for v4 §3 | Partly | PO §3 "Negotiation as the practice of standing" (l. 88–91). Three sources carry it. Xiang et al. document a compensation, not a negotiated exception (card `xiang2022covid`). Di Domenico and Lynch show hosts setting rules and guests deferring (card `didomenico2007host`: "PARTLY"). Lugosi 2014 is abstract-only. None addresses the value-creation half of the request |
| R1.3 | Remind the reader what "the split" is | Addressed | RP §4; PO §4 "Naming the split" (l. 111) |
| R1.4 | Give the test a preamble and a stated purpose; improve it in the abstract | Partly | PO §5 Table 1 and abstract (l. 35) supply the derivation and the one-sentence test. The *purpose* R1 names (deciding when a touchpoint may replace or augment hosting) is not stated in the outline |
| R1.5 | Which "framework" does §8 mean? | Partly | RP §8 promises a named referent each time. PO §8 still ends "The framework helps organizations…" (l. 231), and the pitch has "This framework identifies a failure mode" (l. 15) directly after naming the roadmap |
| R1.6 | Full proofread; "it" and "this" without referents | Addressed in plan only | RP concern map R1.6, "final pass". No file assigns it |

### Reviewer 2

| ID | Point | Status | New vs editor summary | Where, and what is short |
|---|---|---|---|---|
| R2.1a | Where the host's obligation comes from | Partly | No (E.1) | PO §2.1 (l. 52) asserts it through Xiang et al. citing King 1995. §2.3 (l. 67) says it is "owed to an arrival from the threshold onward". `WS_A_obligation.md` §4 records that no source read says arrival triggers an obligation. No file says why a *commercial* party acquires it |
| R2.1b | Why it remains after delegation | Partly | No (E.1) | PO §2.2 (l. 58–63). The sources cover answerability for harm, not the host's first-order duty (see section 2 below) |
| R2.1c | Who actually holds it; what makes it non-transferable | Partly | No (E.1) | PO §2.1 "The holder" (l. 53) and "Employee and host are not the same" (l. 56): "the institution that opened the threshold". Non-transferability now rests on "The role of hosting can move to a machine. The answering cannot" (l. 63), which is about answering |
| R2.1d | The argument "especially in Figure 1" | Missed | **Yes** | No figure exists in `DRAFT.md`, in the 8 November copy of the submitted text, or in the outline. Either the submitted Word file carried a figure the markdown lost, or R2 means the chain in v4 §3. The authors need to open the submitted file and find out |
| R2.1e | Responsibility "may sit with the hotel company, operator, employee, platform, vendor, or several actors at once" | Missed | **Yes** | PO treats "the institution" as one party throughout. The actors appear only as a list in §4 (l. 105) and in the conclusion (l. 249). No file says which of owner, brand, operator, platform or vendor is the host |
| R2.2a | Theory of role obligation: what activates the obligation | Partly | **Yes** (the four sub-questions) | Same as R2.1a. Activation is asserted, not theorized |
| R2.2b | Who initially bears it | Partly | **Yes** | Same as R2.1c |
| R2.2c | What can and cannot be delegated | Partly | Partly (E.1 "whether it transfers") | PO l. 63 gives one line. No file sorts the host's duties into delegable performance and non-delegable remainder |
| R2.2d | How responsibility is shared among multiple actors | Missed | **Yes** | Nothing. RPl's exclusion rule kept the relevant literature out (conflict 3 above) |
| R2.2e | Risk that the argument reads as ordinary organizational delegation or algorithmic accountability | Partly | No (E.1, E.3) | PO §2.3. The two differentiators ("prior to harm", "includes the exception") are the authors' own and are untested against R2.4's comparators |
| R2.3a | Circularity: standing means someone must answer; accountability means someone must answer a guest with standing | Missed | **Yes** (E.2 said only "needs refinement") | PO reproduces it. §2.4 (l. 72) defines accountability as "the duty to answer someone entitled to ask"; §3 (l. 77) defines standing as "the guest's authority to address claims"; Table 1 (l. 126) pairs "Standing" with "Accountability" and the failure "No one is obliged to answer" |
| R2.3b | Distinguish having standing from being able to exercise it | Addressed | **Yes** | PO §3 "Held and exercised" (l. 82), after `WS_B_standing.md` §9 raised it independently |
| R2.4 | Why hospitality matters to the mechanism, when banking, healthcare and e-commerce show the same problems | Partly | Partly (E.3 named service management only) | PO §2.3 (l. 66–69), §8 "What the hospitality lens adds" (l. 223), pitch l. 21. The contrast drawn is with service management and algorithmic accountability. Banks and hospitals also owe duties before harm and also grant exceptions, so the two differentiators do not separate hospitality from R2's examples |
| R2.5a | Which decisions need immediate interruptibility and answerability, and which do not | Missed | **Yes** | PO §5 has seeds: check-in that confirms against check-in that scores (l. 152) and "Guest acceptance depends on the stakes" (l. 153). No typology, and nothing on timing ("immediate") |
| R2.5b | Which formats the framework explains best (hotels, short-term rentals, highly automated services) | Partly | Partly | PO §9 (l. 236–239) lists luxury/budget, hotels/platforms, EU/elsewhere in a 300-word section. It names contrasts; it does not say where the framework's explanatory power falls off, or why |

### Reviewer 3

| ID | Point | Status | New vs editor summary | Where, and what is short |
|---|---|---|---|---|
| R3.1 | Style and rhetoric obscure the message; "wasn't sure whether AI assistance was the problem or a possible solution" | Partly | Partly (E.5 gave tone only; the AI remark is new) | RP "Tone flags". The outline keeps the register R3 objects to: "A claim without an addressee is like an apology found in a diary" (PO l. 81), "The danger is that hollow voice works" (l. 202), and the closing line (l. 250). See section 6, item 3 |
| R3.2 | Named phrases: opening anecdote; "we talk" (p2); "the answer is boring" (p2); "condemns…blesses" (p13); the "bite" of the six questions (p13); "sitting ducks" (p14); a six-line sentence (p18) | Partly | **Yes** (the list) | RP tone table covers the anecdote, "we talk", "boring", "condemns/blesses" and "sitting ducks". It does not list "The six questions bite hard" (`DRAFT.md` l. 100) or the long sentence on p18 (likely the chain sentence at `DRAFT.md` l. 126) |
| R3.3 | The Airbnb experiment passage (p19) is hard to follow | Addressed | **Yes** | RP §7 row: "Cut the Airbnb-remedy paragraph" |
| R3.4 | Not persuaded the heir question is "boring" | Partly | **Yes** | PO §1 "The heir question, briefly" (l. 45) drops the word and keeps the dismissal in two sentences. R3's objection is to the dismissal |
| R3.5 | Claims under a general "we" lack evidence; unwarranted assumptions | Partly | **Yes** | "Notice how we talk" is cut. PO l. 41 keeps the claim it introduced ("The literature describes phygital technology by what it does: tool, mediator, facilitator, co-creator") |
| R3.6 | Bitner et al. 2000 is not a credible source for conceptions of AI | Addressed, incidentally | **Yes** | RPl reference budget drops Bitner. The surviving sentence (PO l. 41) still needs two sources that are about AI |
| R3.7 | The front of the paper treats technology reductively; phygital technology takes many forms | Missed | **Yes** | The pitch lists four functions (l. 7). No file distinguishes kinds of system (decision systems, interfaces, robots, platforms) or says which the argument covers |
| R3.8 | Hosting is equated with hotel reception; do the claims hold in other hosting contexts? | Missed | **Yes** | PO cases: hotel pricing, hotel check-in, one restaurant projection. §9 offers "Hotels against platforms" only |
| R3.9 | Authority is treated as absolute; it is always organisationally constrained | Missed | **Yes** | PO l. 72–73 defines authority as "the power to change the decision or the rule" and says that in a face-to-face welcome "all four sit in one person". §7 asks for "reachable human staff who retain the authority to reverse" (pitch l. 13). The library already holds the counter-evidence (section 3: Golubovskaya p. 1297; Beatty p. 167; Xiang "after checking with hotel management") |
| R3.10 | p6: the claims about what guests owe are "highly questionable"; the residents' scale is irrelevant; "measuring guest's standing" is hard to decipher | Partly | **Yes** | RP §3 cuts the lodge and residents examples. PO l. 92 keeps "Hospitality runs both ways" and the Pijls measurement point. The guest's reciprocal duties are dropped, not worked out |
| R3.11 | p8: a "single duty" that defines the role ignores that welcome sits in a social and organisational context and is not one thing | Missed | **Yes** | R3 is paraphrasing `DRAFT.md` l. 59 ("A welcome is triggered by one thing only… any duty that makes a role"). PO keeps one obligation, one trigger and one holder (l. 52–56, 67) and defines welcome as four things "held together" (l. 87) |
| R3.12 | Parts 6 and 7 meander | Partly | No (E.4) | RP cuts in §6–§7; each section opens on a claim. PO §7 still carries nine topics in 950 words (l. 173–203) |
| R3.13 | "Roadmap of rising commitment" and "forum" are unqualified | Partly | **Yes** | CF §1.3 corrects the Bovens reading. PO Table 3, stage 4 (l. 212) still says "Create a forum obliged to answer challenges", which repeats the error CF corrected. "Forum" is nowhere defined |
| R3.14 | Table 2 needs a longer explanation and a clear link to what precedes it | Partly | Partly (E.6) | PO Table 3 adds a "Condition it secures" column. A longer explanation competes with the word budget (section 6, item 2) |
| R3.15 | Work backwards from the contribution so the content builds to it | Partly | No (E.4, E.7) | RP restructure. The first contribution depends on the unbuilt obligation |
| R3.16 | Unconvinced by the contributions in §8 | Partly | No (E.7) | PO §8 (l. 217–220). The contribution list differs across four files (section 6, item 4) |
| R3.17 | An "emergent question" about AI appears in §8; unclear whether it was the question all along. Terms shift between AI, technology and algorithmic systems | Partly | **Yes** | PO l. 46 states one research question. No file fixes the vocabulary: the pitch alone uses "algorithmic systems", "software", "automated processes", "automated touchpoints", "machine" and "code, agents, interfaces" |
| R3.18 | "These distinctions touch well-being": which distinctions, and what is the link? | Partly | **Yes** | RP cuts well-being to two sentences; PO l. 228–230 keeps a speculative aggregate claim. The editor asked for well-being (`RESPONSE_TO_EDITOR.md`, table row 4), so it cannot simply go. Two sentences will be less clear, not more |
| R3.19 | "A direction for research rather than a finished theory" and "the two levels" confuse | Partly | **Yes** | Mostly removed by the cut in R3.18; not addressed as such |
| R3.20 | Limitations and future research need more detail and a clearer agenda | Partly | No (E.7) | PO §9, 300 words, three studies |
| R3.21 | The conclusion should say what the paper achieved against its questions and set an agenda | Partly | No (E.7) | PO §10 returns to the pricing case and closes on the v4 epigram |
| R3.22 | Evidence is inconsistent and unconvincing across the paper | Partly | Partly | CF lists sixteen v4 sentences their sources do not support. The outline applies most of the fixes; three slips remain (section 6, items 5–7) |

**Count.** Of 43 numbered points, the current materials address 6 (one of them, R1.6, in the plan only), partly address 28 and miss 9. The nine misses are R2.1d, R2.1e, R2.2d, R2.3a, R2.5a, R3.7, R3.8, R3.9 and R3.11. Six of the nine (R2.1e, R2.2d, R2.3a, R3.8, R3.9, R3.11) concern who the host is, what the host owes, and under what constraints. That is the authors' concern stated as a count.

---

## 2. How the project currently handles host duties

### 2.1 The submitted draft (v4, `manuscript/DRAFT.md`)

v4 asserts the obligation by definition of the word "host" and argues for it in one paragraph, in §4.

| Location | Passage | What the passage does | Grounding |
|---|---|---|---|
| Abstract, l. 5 | "does it also take on what a host owes the guest? It does not." | Assumes a host owes something | None |
| §1, l. 13 | "A guest is someone a host is expected to receive (Hemmington 2007)." | Asserts | Hemmington's card (`hemmington2007`) lists "the host-guest relationship, generosity… and the security of strangers". Expectation, not duty |
| §1, l. 15 | "the word host carries an obligation… A host takes in the arriving stranger and accepts some responsibility for how that person is received (Lashley 2000)." | Asserts from the meaning of a word | `lashley2000towards` is a metadata-depth card. No one on the project has read the chapter |
| §1, l. 15 | "The host's power over the guest runs through the whole stay, and so does what the host owes (Bulley 2015)." | Asserts | Card `bulley2015ethics`: "SUPPORT: PARTIAL… The 'owes' clause rests on the authors' own inference." Setting is refugee camps |
| §1, l. 17 | "A contract can spell out the services you must deliver. It cannot, on its own, explain the obligation that runs between a host and a guest." | Asserts that the obligation exceeds contract | None |
| §1, l. 21 | "the obligation does not need to move into the machine. It needs to stay findable" | Leans on the obligation | — |
| §2, l. 31 | "Obligation is what the host owes the guest, at a minimum, a welcome… We stipulate the other three" | Stipulates | The paper says so |
| §2, l. 33 | "Welcome, in short, is recognition, admission, responsiveness, and the capacity for a negotiated exception, all held together." | Stipulates the content | None |
| §4, l. 59 | "A welcome is triggered by one thing only: someone has arrived… The ownership of a welcome, as distinct from its performance, cannot be handed off without handing off the role itself." | **The only argument** | CF §1.1: the trigger typology attributed to Santoni de Sio and Mecacci is not in their paper. CF §2: the trustee comparison has no source. `WS_A_obligation.md` §4: no source says arrival triggers an obligation |
| §4, l. 67 | "leaves the obligation with no forwarding address" | Leans | — |
| §5, l. 77 | "some identifiable party has to be obliged to receive and answer a challenge, because standing is empty if no one must respond" | Derives accountability from standing | Circular with l. 29 (below) |
| §9, l. 166 | "somebody still owes the guest a welcome." | Leans | — |

R3.11 targets l. 59 directly. R2.1 and R2.2 ask for l. 59 to be expanded into a theory. The September internal panel had already found the paragraph's uniqueness claim false: "ownership non-delegability is generic to every role-making duty (controller and processor, hospital and outsourced nursing, trustee and delegate), so welcome is not unique on that axis" (`reviews/2026-09-03/SYNTHESIS.md`, adjudication 9). The same panel flagged that "'owed simply because someone has arrived' imported unconditional hospitality into a commercial setting" (`manuscript/NOTES.md`, l. 647–649). Both problems predate the journal reviews.

### 2.2 The pitch and outline (`PITCH_AND_OUTLINE.md`)

The new materials move the obligation to the front and source it better. They still assert its origin and its holder, and they switch between two different duties without saying so.

| Location | Passage | What the passage does | Grounding |
|---|---|---|---|
| Pitch, l. 7 | "neither addresses what becomes of the host's prior obligation to the guest" | Assumes a prior obligation | — |
| Pitch, l. 9 | "commercial hosts owe guests care, sanctuary, and welcome because they control the physical premises (Shryock 2012: S25, S30; Xiang et al. 2022; O'Gorman 2009)" | Asserts origin (control of premises) | The "because" is the authors'. Card `shryock2012breaking`: "sovereignty is manifest in the ability to act as host" (p. S25); `WS_A` §4: moving this "to a commercial property is the authors' step". Xiang et al. give no ground at all |
| Pitch, l. 11 | "Every institutional duty generates a correlative claim… Delegating frontline tasks to software transfers the execution of hosting, but the obligation to answer remains with the organization" | Argues retention, for the duty to answer | Kong and Kropf et al. cards support this for answerability |
| Pitch, l. 21 | "Hospitality asks what is owed to a person simply because they walked in the door, treating the capacity to negotiate an exception as an inherent part of that obligation." | Asserts the trigger and the content | No source (REVISION_PROPOSAL §1.7 lists both as "the authors' own argument") |
| Outline §1, l. 44 | "Hospitality already holds that the commercial host is obliged to the guest (Xiang et al. 2022, citing King 1995)." | Asserts by citation | One sentence in a literature review, quoting a source no one on the project has read |
| Outline §2.1, l. 52–56 | Obligation, holder, rival, displacement, "That obligation belongs to the institution that opened the threshold." | Asserts holder | Shryock p. S30 names "the hospitality industry" as the modern carer for strangers; it does not say which legal or organizational party |
| Outline §2.2, l. 58–64 | Nissenbaum, Kong, Kropf et al., Santoni de Sio and Mecacci; "The role of hosting can move to a machine. The answering cannot." | Argues, with full-text sources | All four concern answering for harm |
| Outline §2.3, l. 66–69 | "Prior to harm… Includes the exception… What this answers. Why the obligation remains, where it originates, whether it transfers" | Asserts | The bullet claims to answer four questions with two unsourced statements |
| Outline §3, l. 77 | "Standing is the correlate of the host's obligation" | Derives standing from the obligation | Sound in form (Hohfeld, Darwall cards), but inherits whatever the obligation lacks |
| Outline §5, Table 1, l. 120–126 | Recognition → common understanding; Negotiation → predictability; Standing → accountability | Derives the test from "the welcome" | The welcome's elements are stipulated (v4 l. 33) |
| Outline §10, l. 248 | "The obligation is still owed, and the institution that delegated still owes it." | Leans | — |

### 2.3 Four structural problems in the handling

**(a) Two duties under one name.** The paper needs a first-order duty (the host owes the guest reception, safety, care) and a second-order duty (the host must answer for how the first was met). The pitch moves from one to the other inside a single paragraph: "the host's prior obligation to the guest" becomes "answerability relocates to the delegating organization" (l. 7), and "Every institutional duty generates a correlative claim" becomes "the obligation to answer remains with the organization" (l. 11). Kong's principle is about answerability "for the foreseeable types of outcome" (card `kong2026delegation`, p. 5). It says nothing about whether a duty to welcome exists or survives. So the retention argument is sourced for the duty the paper says is generic, and unsourced for the duty the paper says is hospitality's own (PO §2.3). This is why R2 can say the argument "risks looking like a more familiar problem of organizational delegation or algorithmic accountability".

**(b) The circle R2.3 names is in the definitions.** Follow the chain in the outline:

- The obligation's content is the welcome. The welcome includes "the capacity for a negotiated exception" (l. 87), and Table 1 lists "Standing" as an element of the welcome (l. 126).
- Standing "is the correlate of the host's obligation" (l. 77).
- Accountability is "the duty to answer someone entitled to ask" (l. 72), and it is the condition that secures standing (l. 126).

So the obligation contains standing, standing is defined by the obligation, and accountability is defined by an entitlement that is standing under another name. v4 has the same loop in prose: "A guest has standing when their words count as a claim addressed to someone… obliged to respond" (`DRAFT.md` l. 29) and "some identifiable party has to be obliged to receive and answer a challenge, because standing is empty if no one must respond. Call this accountability" (l. 77). The outline's held/exercised distinction (l. 82) answers R2.3b and leaves R2.3a where it was. A way out is in section 5.

**(c) The welcome has two inventories.** §3 gives four elements: "Recognition, admission, responsiveness, and the capacity for a negotiated exception" (l. 87). Table 1 gives three: recognition, negotiation, standing (l. 124–126). Admission and responsiveness have no condition; standing appears in the table and not in the definition. Since the test is said to derive "from the basic structure of a welcome" (pitch l. 13), the derivation needs one list.

**(d) The baseline is the thing R3 disputes.** "In a face-to-face welcome all four sit in one person" (l. 73). This is true of an owner-host in a private house. It was never true of a hotel receptionist, whose authority the organization sets. R3.8 (hosting equated with reception) and R3.9 (authority treated as absolute) both attack this baseline, and the split in §4 is measured against it.

---

## 3. What the library already holds on host duties

"Uses it correctly" refers to the pitch and outline unless v4 is named. Locators are those printed on the cards in `library/cards/`.

### Hospitality theory

| Card | Depth | What it supports | Use in the outline |
|---|---|---|---|
| `lashley2000towards` | **metadata** | Card: three domains, commercial "inheriting its meanings from the other two". No quotation | **Over-read.** PO l. 52 says "Lashley (2000) holds that a genuine welcome differs from being welcomed as a valued customer." The project has that sentence only as Slattery quotes it from "Lashley and Morrison 2000: 13" (card `slattery2002finding`, p. 22), flagged in `WS_C` as "secondary quotation, not checked". v4 l. 15 hangs "the word host carries an obligation" on the same unread chapter |
| `derrida2000hospitality` | **metadata** | Conditional and unconditional hospitality, as a "canonical framing" | Not in the new outline. RP §2 still cites it for "locate the host's obligation at the threshold". Unconditional hospitality is the opposite of a commercial host's duty (`WS_A` §4) |
| `lynch2011theorizing` | full-text | The journal's founding statement; antonym pairs including "conditional/unconditional". No statement of host duty on the card | Not in the outline. RP §2 lists it for origin; the card does not support that |
| `lynch2017mundane` | **metadata** | Nothing checkable. Card: "SUPPORT: NOT CHECKABLE" for v4's list of guest moves | Not in the outline. v4 l. 27 rests on it |
| `lynch2021critical`, `lynch2021reprise` | full / abstract | Field reviews. No duty content on the cards | Not used |
| `bulley2015ethics` | full-text | Host *power* continues after the threshold (PDF pp. 3, 11). Card: the commercial "owes" is the authors' inference; Bulley does treat hospitality as "ethical responsibility-taking for others" (PDF p. 7) | Not in the outline. Usable for the claim that the relation runs through the stay; not for a commercial obligation |
| `lugosi2008` | full-text | "hospitable interaction is an acknowledgement of the other" | Not in the outline. Supports recognition as content |
| `lugosi2014hospitality` | **abstract** | Hospitality "can be used purposefully to establish power relations and invoke obligations" (abstract). The obligations it names run toward conforming and reciprocating, i.e. from the guest or member | PO l. 91 uses it accurately at abstract level. Needs a full read; it may bear on the guest's duties (R3.10) more than on the host's |
| `hemmington2007` | full-text | "the host-guest relationship, generosity… and the security of strangers" as elements of commercial hospitality | Not in the outline. "Security of strangers" is the nearest held hospitality-management statement of a protective duty |
| `brotherton1999towards` | abstract, rejected | Definitional. The Brotherton and Wood definition (via Slattery p. 23) calls hospitality "voluntarily entered into" | Not used. Note the word "voluntarily": the field's best-known definition cuts against an obligation |
| `slattery2002finding` | full-text | The rival: "The buyers are not guests, they are customers. The relationship is not philanthropic it is economic" (p. 21). Also the corporate context of chains, brands and portfolios (pp. 24–25) | Used correctly as rival (PO l. 54). **Under-used**: pp. 24–25 are the only held hospitality source on the multi-actor structure R2.1e asks about |
| `golubovskaya2017meaning` | full-text | Displacement of the hospitality lexicon (pp. 1296, 1299–1300). Hospitality as "an attitude and spirit" (p. 1287). Obligation is one definition among several, not adopted (p. 1284) | Used correctly for displacement (PO l. 55). **Under-used** on two points: "commercial hospitality often empowers the guest, whose only obligation is to pay and behave reasonably (King, 1995)" (p. 1286) is a located statement of the guest's duties (R3.10); and a manager's "they are here as your guests, but they cannot demand everything… we have own standard" (p. 1297) is located evidence that host authority and guest claims are organisationally bounded (R3.9) |
| `xiang2022covid` | full-text | Hotels "as 'hosts,' are obliged to provide care, comfort, ease, welcome, and safety to the guests (King, 1995)". A compensation approved "after checking with hotel management" | PO l. 52 uses the quotation accurately. **It bears more weight than it can carry.** It is the only sourced statement of the first-order duty, it is secondary, and the card notes that "'Host' here is the hotel and its staff together; the study does not separate the institution's obligation from the employee's performance" |
| `didomenico2007host` | full-text | In commercial homes "the balance of power… is perceived by hosts to rest firmly with them" (p. 332); guests do not complain (p. 333) | **Partly over-read.** PO l. 90 and pitch l. 17 use it to show presence is not enough. In these homes the person present is also the owner with full authority, so the case shows something stronger and less convenient: a reachable host with authority still did not produce guests who press claims. What stops them is a norm of guest conduct ("it's not the done thing"). That is evidence about the guest's duties, and it complicates the thesis that an address is what standing needs |
| `manfreda2025reciprocal` | abstract | Guests reciprocate from gratitude, "rather than formal obligation or indebtedness" | Cut from the outline. Still relevant to R3.10 |
| `munasinghe2022` | abstract | A triadic host–guest model in which social context is the third element | Not used. Bears directly on R3.11 (welcome in its social context) |

### Anthropology

| Card | Depth | What it supports | Use in the outline |
|---|---|---|---|
| `shryock2012breaking` | full-text | Hosting as "a test of sovereignty" (p. S20); guests "depend on their hosts for protection and respect" (p. S23); "hosts and guests cannot interact as equals" (p. S28); breakdown when parties dispute "who is sovereign, who belongs, and who owes or should offer respect" (p. S30); the industry as modern carer (p. S30) | Quotations accurate (PO l. 53). **Over-read in the pitch** (l. 9), which turns "sovereignty is manifest in the ability to act as host" into a causal ground for a commercial duty. The card warns that Shryock supports origin "only indirectly" and that the bib gloss "host authority is constituted by guest obligation" overstates him. The article's subtitle is "Bad Hosts, Bad Guests": it is the project's best held source on reciprocal duties, and the outline does not use it for that |
| `candea2012return` (bib entry only, no card) | metadata | Nothing read | Not used. Same special issue as Shryock |

### Delegation and responsibility

| Card | Depth | What it supports | Use in the outline |
|---|---|---|---|
| `kong2026delegation` | full-text | Answerability "relocated to the prior act of delegation" (p. 5); grounded in control over delegating; "A role matters derivatively rather than intrinsically" (p. 4); fiduciary duty "set aside" (p. 4); indexed to foreseeable harm (p. 5); being answerable is kept apart from being *held* answerable (p. 4) | Used correctly (PO l. 60). Two consequences the outline has not drawn. Kong is evidence against grounding the obligation in the role, which is R2's own framing ("role obligation"). And Kong already supplies "address" as vocabulary (pp. 10, 13), so the paper's addition must be the first-order duty and reachability |
| `kropf2026blame` | full-text | A robot can hold a scoped role; its "answerability… is currently inconceivable" (p. 9). Built on "the role responsibility described by Vincent… whereby she refers to Hart" (p. 2). The robot's role is not the nurse's (p. 4) | Used correctly (PO l. 61). The card names the role-obligation lineage (Vincent, Hart) that R2.2 asks for; no one has followed it |
| `nissenbaum1996accountability` | full-text | Without new lines, accountability "will be lost" (PDF p. 11); "many hands" | Used correctly in the outline (l. 59). The pitch (l. 9) cites her for answerability *relocating* to the institution; her claim is that it is lost unless rebuilt (CF §2) |
| `santonidesio2021gaps` | full-text | Officers must be able to explain "the behaviour of their institution… no matter how much technology is involved" (§4.3) | Used correctly (PO l. 62). The setting is public organisations |
| `bovens2007accountability` | full-text | The actor answers; the forum questions and can sanction (pp. 450, 452). Many hands (p. 457, per `VERIFY_verifier_3.md`) | Bullet at PO l. 192 is right. Table 3, stage 4 (l. 212) contradicts it |
| `casalegno2020circular` | full-text | Reallocated roles whose "power and responsibilities" should "overlap and converge" | Not in the outline. A held source for shared responsibility (R2.2d), and by the editor's co-authors |
| `gursoy2026reconceptualizing` | full-text | "Algorithmic governance shifts authority from interpersonal judgment to computational logics, raising questions about accountability when harm, bias, or exclusion arise" (p. 160); "distributed responsibility" named as a theory gap (p. 154) | **Over-read in the pitch** (l. 11), which attaches "(Gursoy 2026: 160)" to "authority–answerability split". The term is the paper's. Gursoy's sentence is harm-indexed, which is the side of the line the paper says it is not on |
| `sharmamattila2025rights` | full-text | Asks "who should be blamed? The restaurant company, the robotic manufacturer… the algorithm creators… Or was the manager on duty responsible?" (p. 911); "What are the rights and responsibilities of a human employee, and how should the firm… translate those into the service robot context?" (p. 915) | Dropped to two sentences in the plan. It is the one held hospitality-journal source that poses R2.1e's multi-actor question |
| `eu2024aiact` | full-text | Art. 86: explanation owed by the *deployer*. The Act separates provider from deployer | Used for regulation (PO l. 224–227). Also usable as a statutory answer to "vendor or operator?" (R2.2d) |

### Standing

| Card | Depth | What it supports | Use in the outline |
|---|---|---|---|
| `hohfeld1913fundamental` | full-text | Duty as "the invariable correlative" of a claim (p. 33) | Outline l. 79 is accurate ("Every duty owed to someone"). **The pitch over-reads** (l. 11): "Every institutional duty generates a correlative claim." Only directed duties do. Darwall's chapter separates obligation "period" from bipolar obligation (card summary) |
| `darwall2013bipolar` | full-text | The obligee's "individual authority or standing" (p. 27); address needs an addressee (p. 31); obligations arise in "various keys", conventional and legal (p. 28, per `WS_B` §9) | Used correctly. Darwall's promise example ("a promisee has a distinctive normative standing", p. 20) points to undertaking as a ground for the obligation, which the outline has not used |

### Negotiation, discretion and constrained authority

| Card | Depth | What it supports | Use in the outline |
|---|---|---|---|
| `beatty2016compliance` | full-text | Special requests; the commonest reason for refusal is that the request is "in violation of company policy or possibly illegal" (p. 167); employees consulted supervisors in about 10% of cases or none (note 4, p. 171). Sample: oil-change and pest-control technicians | Not in the outline. Located evidence for R3.9, with the sample caveat stated |
| `pedersen2022` | full-text | Frontline discretion and "the ethics of office" (title) | PO l. 108 uses it for workarounds. The "ethics of office" frame is a role-obligation account of frontline staff and may serve R2.2; I did not re-read the card for this |
| `lipsky1980street` | not checked this run | Street-level discretion | Not in the outline |

### Platforms and automation

| Card | Depth | What it supports | Use in the outline |
|---|---|---|---|
| `germannmolz2026` | **abstract** | "Guests without hosts"; Airbnb as inhospitable governance | PO l. 42 builds the paper's positioning on it. The card carries `must-engage` and `abstract-only-debt`; the author co-edits the journal. This is the largest unread source in the argument |
| `germannmolz2018scale` | full-text | "the moral responsibility of hospitality is not necessarily about caring for one another's physical and emotional needs, but about safeguarding reputations" (p. 237); platforms transfer "legal and tax liabilities onto homeowners" (p. 245) | Used correctly as precedent (PO l. 64). **Under-used**: p. 237 is a located statement of how a platform changes the *content* of the host's duty, and p. 245 of how it reallocates duties among actors |
| `riordan2024digitally`, `roelofsenminca2018`, `chengfoley2019` | abstract / abstract / not checked | Platform governance of hosts and workers | Cheng and Foley at PO l. 112. Riordan and Roelofsen and Minca are abstract-only |
| `liu2026hospitableness` | full-text | "hospitableness is fundamentally unidirectional…: a host's disposition to care for a guest without expectation of reciprocity" (p. 2); robots produce "experiential effects", not "a moral disposition" (p. 9) | Pitch l. 7 cites it for software that greets guests. The p. 2 sentence is a held statement of the Telfer-line view that hosting is a personal disposition, which is the alternative to the paper's institutional holder |

**Summary of section 3.** The library holds one secondary sentence on what a commercial host owes (Xiang et al., from King), good full-text sources on who must answer after delegation, and good full-text sources on the form of standing. It holds nothing on why a commercial host is bound, nothing read on host duties from the field's founders (Lashley, Telfer, King, Derrida are all metadata-depth or absent), nothing on law, and nothing on how duties divide among owner, brand, operator, platform and vendor. Four held cards contain material on guests' duties and constrained authority that the outline does not use.

---

## 4. Gap map: literatures on the duties of the host

For each tradition: the reviewer points it serves, what the project holds, and candidate works. Bibliographic details on **UNVERIFIED LEAD** lines are from my memory and must be checked. "Record in project" means a project file reports a Crossref or database record; it does not mean anyone read the work.

### (a) Hospitality studies on host duties and hospitableness

**Why it matters.** R2.1a (origin), R3.11 (welcome is not one thing), R3.8 (hosting beyond reception), and the editor's request for hospitality-specific theory. The journal's readers will expect the paper's account of host duty to come from here first. This tradition also contains the main internal objection to the paper's holder: one line treats hospitableness as a *personal virtue or motive* of individual hosts, which an institution cannot have.

**Held.** Section 3, "Hospitality theory". In short: Xiang et al. (full), Hemmington (full), Lugosi 2008 (full), Slattery and Golubovskaya et al. (full, as rival and displacement), Lashley and Derrida (metadata).

**Candidates.**

- Telfer, "The philosophy of hospitableness", in Lashley and Morrison (eds), *In Search of Hospitality*, pp. 38–55. Record in project (`WS_A` §3; Crossref dates it 2001). Not read. `WS_A` guesses from the title that it treats hospitableness as a personal virtue. If so, it is the position the institutional holder must answer, and Liu et al. (p. 2) show it is still current.
- Telfer, "Hospitableness", *Philosophical Papers* 24(3), 183–196 (1995). Record in project (`WS_A` §3). Not read.
- Telfer, *Food for Thought: Philosophy and Food* (1996), which I recall contains the fuller account of hospitableness and the motives of hosts, including commercial ones. **UNVERIFIED LEAD**
- King, "What is hospitality?", *International Journal of Hospitality Management* (1995). The project's only statement of the commercial host's obligation comes from this article at second hand (Xiang et al.; Golubovskaya et al. p. 1286). It should be read and cited directly. **UNVERIFIED LEAD** as to volume and pages; the article's existence is attested by two held full-text sources that cite it.
- Lashley, "Towards a theoretical understanding" (held, metadata). Read it. The sentence the outline attributes to Lashley is known only through Slattery.
- Selwyn, "An anthropology of hospitality", in Lashley and Morrison (2000). I recall it argues that hospitality establishes or transforms relationships and carries moral obligation. **UNVERIFIED LEAD**
- Brotherton and Wood, chapter in Lashley and Morrison (2000), source of the "voluntarily entered into" definition quoted in Slattery (p. 23). Known in the project only through Slattery.
- Brotherton's reply to Slattery, *JoHLSTE* 1(2), 76–79, and the rest of the exchange. Records in project (card `slattery2002finding`). Not read. The directory `research/sources/brotherton2002finding/` exists and is empty.
- Lashley, Lynch and Morrison (eds), *Hospitality: A Social Lens* (2007). Record in project (`WS_C`). Not read. Chapters of interest include O'Gorman's "Dimensions of hospitality" (record in `WS_A`) and Di Domenico and Lynch on commercial homes (record in `WS_C`).
- O'Gorman, "Origins of the commercial hospitality industry", *IJCHM* 21(7), 777–790 (2009). Record in project and read in full by Workstream A (`research/sources/ogorman2009origins/`), **but no card exists**, and the authors' pitch cites it (l. 9). `WS_A` quotes it on "the increasing legal control" that commercial hospitality was subject to (pdf p. 11) and on Hammurabi's rules for tavern-keepers (pdf p. 4). It is the project's one bridge from hospitality studies to tradition (d).
- O'Gorman, *The Origins of Hospitality and Tourism* (2010), a book-length treatment. **UNVERIFIED LEAD**
- Germann Molz and Gibson (eds), *Mobilizing Hospitality: The Ethics of Social Relations in a Mobile World* (2007). **UNVERIFIED LEAD**
- Bell, "The hospitable city: social relations in commercial spaces", *Progress in Human Geography* (2007), on hospitality in bars, restaurants and hotels as more than commercial exchange. Serves R3.8. **UNVERIFIED LEAD**
- Ritzer, "Inhospitable hospitality?", in *Hospitality: A Social Lens* (2007), on rationalized hospitality. **UNVERIFIED LEAD**
- Aramberri, "The host should get lost: paradigms in tourism theory", *Annals of Tourism Research* (2001), which I recall argues that the host–guest covenant does not describe commercial tourism. A second rival beside Slattery, in a preferred venue. **UNVERIFIED LEAD**
- Lashley, "Hospitality and hospitableness", *Research in Hospitality Management* (2015); Blain and Lashley, "Hospitableness: the new service metaphor?" (2014); Tasci and Semrad, "Developing a scale of hospitableness", *IJHM* (2016). Later work on hospitableness as trait and motive. All three **UNVERIFIED LEAD**
- Munasinghe et al. (2022), held at abstract depth. Read in full for R3.11: its third element is the social and cultural context of the encounter.

### (b) Philosophical hospitality

**Why it matters.** R2.1a and R2.2a (what activates the obligation). The philosophical tradition supplies the distinction the pitch currently blurs: an unconditional welcome owed to whoever arrives, against conditional hospitality governed by law, contract and the host's sovereignty. Pitch l. 21 ("simply because they walked in the door") takes the unconditional side for a commercial host, which the September panel and `WS_A` both flagged.

**Held.** `derrida2000hospitality` (metadata), `bulley2015ethics` (full), `introna2010measure` (abstract), Shryock's reading of Kant and Derrida (full; p. S30).

**Candidates.**

- Kant, *Toward Perpetual Peace* (1795), Third Definitive Article. As I recall it, Kant limits cosmopolitan right to "conditions of universal hospitality": a stranger has a right not to be treated with hostility on arrival (a right to visit), while the right to be a *guest* requires a further agreement. That is a two-stage activation, arrival and then admission, and it fits a commercial setting better than Derrida's unconditional welcome. Note the project's own caution against citing Kant directly (conflict 2). **UNVERIFIED LEAD** as to edition and wording.
- Derrida and Dufourmantelle, *Of Hospitality* (held, metadata). Read the passages on the "laws" of conditional hospitality against "the law" of unconditional hospitality before citing either side.
- Derrida, "Hostipitality", *Angelaki* (2000); Derrida, *Adieu to Emmanuel Levinas* (1999); Derrida, *On Cosmopolitanism and Forgiveness* (2001). All **UNVERIFIED LEAD**
- Levinas, *Totality and Infinity*, for responsibility to the other as prior to choice, the source of the "prior obligation" idea. Likely too far from the venue to cite; useful to know what Derrida is drawing on. **UNVERIFIED LEAD**
- Ricoeur on "linguistic hospitality" in *On Translation*. Its one point of contact is the outline's "employee as translator" (§6). Low priority. **UNVERIFIED LEAD**
- Critiques and extensions: Still, *Derrida and Hospitality: Theory and Practice* (2010); Rosello, *Postcolonial Hospitality: The Immigrant as Guest* (2001); Dikeç, Clark and Barnett, "Extending hospitality: giving space, taking time", *Paragraph* (2009); Benhabib, *The Rights of Others* (2004). All **UNVERIFIED LEAD**
- Brown (2010) and Kyslan (2026) on Kantian cosmopolitan hospitality surfaced as Consensus hits in `WS_B` §2 (query 9). Records seen there; nothing read.

### (c) Anthropology of host–guest relations and the duties of guests

**Why it matters.** R3.10 (what guests owe), R2.2a (activation), R1.2 (negotiation), R2.3 (standing). Anthropologists treat hospitality as a rule-governed relation with duties on both sides. The guest's standing in that literature is conditional on the guest's own conduct, and the host's duty includes protection. That gives the paper something it lacks: an account in which a guest can *lose* standing, and so an account of what standing is beyond the presence of an addressee.

**Held.** `shryock2012breaking` (full); `candea2012return` (bib entry, metadata; no card); Golubovskaya et al. p. 1286 on the commercial guest's "only obligation"; Di Domenico and Lynch pp. 332–335 on house rules; `manfreda2025reciprocal` (abstract); `library/CLAIMS.md` slug `guest-obligation-untheorized`, narrowed on 11 August.

**Candidates.**

- Pitt-Rivers, "The law of hospitality" (first published 1968 under a longer title in Peristiany's *Contributions to Mediterranean Sociology*; later in *The Fate of Shechem*, 1977; reprinted, I believe, in *HAU* in 2012). As I recall it: the stranger becomes a guest by a host's act of incorporation; host and guest each hold duties (the host to honour and protect, the guest to honour the host, accept what is offered and not usurp the host's place); and breach on either side ends the relation. This is the most direct source for "what activates the obligation" in a relational key. **UNVERIFIED LEAD**
- Candea and da Col, "The return to hospitality", *JRAI* 18(S1), S1–S19 (2012). Record in project (`literature/references.bib`, verified 9 August, metadata depth). Not read.
- Shryock, "Thinking about hospitality, with Derrida, Kant, and the Balga Bedouin", *Anthropos* (2008). **UNVERIFIED LEAD**
- Selwyn (2000), as in (a). **UNVERIFIED LEAD**
- Herzfeld, "'As in your own house': hospitality, ethnography, and the stereotype of Mediterranean society" (1987), on hospitality as a means of holding the guest in moral debt. **UNVERIFIED LEAD**
- Mauss, *The Gift*, for the obligation to give, receive and reciprocate. Background only. **UNVERIFIED LEAD**
- Smith (ed.), *Hosts and Guests: The Anthropology of Tourism* (1977; 2nd ed. 1989), the origin of the host–guest frame in tourism studies, with Aramberri (2001) as its critic. **UNVERIFIED LEAD**
- On guests' duties in commercial settings: Sherman, *Class Acts: Service and Inequality in Luxury Hotels* (2007), which I recall documents reciprocity and guests' sense of obligation toward workers; and work on customer misbehaviour, for example Harris and Reynolds, "The consequences of dysfunctional customer behavior", *Journal of Service Research* (2003). Both **UNVERIFIED LEAD**

`literature/FOUNDATION.md` (l. 646–648) records the project's own earlier finding: "No theorization of the guest's reciprocal obligation in a commercial setting. Guest obligation and bad guesthood are theorized richly in refugee, migration and private-hosting literatures, not in commercial hospitality journals." R3 read the v4 version of that claim as "highly questionable". The safer course is to cite what the anthropologists and the law say guests owe and stop claiming an absence.

### (d) Legal history: the innkeeper's duty to receive and duty of care

**Why it matters.** This is the strongest candidate answer to R2.1 and R2.2, and the only one that answers R2.4 with a fact instead of an assertion. As I understand the doctrine (all of it to be verified):

- *Activation.* The common law treated innkeeping as a "common calling". A person who held a house out as an inn for travellers came under duties that an ordinary trader did not. The duty attached when a traveller presented, in a fit state and able to pay, and the inn had room.
- *Content.* A duty to receive; a duty to take reasonable care for the guest's safety; a strict liability for the guest's goods within the inn.
- *Holder.* The innkeeper as proprietor, not the servant who opened the door. The innkeeper answered for servants' acts.
- *Delegation.* Performance by servants was ordinary. The duty stayed with the innkeeper. Modern tort law generalizes this as the "non-delegable duty".
- *Reciprocity.* The guest owed payment and orderly conduct; the innkeeper could refuse or eject on reasonable grounds and held a lien on the guest's goods.
- *Hospitality-specific?* Partly. The duty to serve all comers was shared with common carriers and a few other callings, and it did not bind shops, banks or ordinary sellers. So the honest answer to R2.4 is "hospitality and a small family of public callings", which is a real boundary.
- *Boundary conditions.* The law distinguished inns from private lodging and boarding houses, and travellers from lodgers. That distinction maps onto hotels against short-term rentals (R2.5b).

The legal duty is thin. It contains reception, safety and custody of goods. It does not contain a negotiated exception or a duty to explain. The paper would use the law for the structure (who is bound, by what act, with what remainder after delegation) and argue the richer content from (a) and (c). The law is also jurisdiction-bound, which the paper already concedes for the AI Act (PO l. 239).

**Held.** Nothing carded. O'Gorman 2009 (read, uncarded) on early legal control of commercial hospitality. `literature/CLAIM_AUDIT_PLAN.md` (U1) searched "law of algorithmic accountability" only. The project has never searched this tradition.

**Candidates.** All **UNVERIFIED LEAD** unless stated.

- *Calye's Case* (1584), the classic statement of the innkeeper's liability for guests' goods. **UNVERIFIED LEAD**
- *Lane v Cotton* (1701), Holt CJ on the duty of those in public employment to serve all. **UNVERIFIED LEAD**
- *Constantine v Imperial Hotels Ltd* [1944] KB, on an innkeeper's wrongful refusal to receive a guest. **UNVERIFIED LEAD**
- Hotel Proprietors Act 1956 (UK), which I recall defines a hotel as an establishment held out as offering food, drink and sleeping accommodation, without special contract, to any traveller who appears able and willing to pay and is in a fit state to be received. If the wording is as I recall, it is a statutory statement of activation conditions. **UNVERIFIED LEAD**
- Occupiers' Liability Act 1957 (UK), the "common duty of care" to visitors; and the equivalent premises-liability doctrine for invitees in US law. **UNVERIFIED LEAD**
- Civil Rights Act of 1964, Title II (US), and *Heart of Atlanta Motel v United States* (1964), on public accommodations. **UNVERIFIED LEAD**
- Wyman, "The law of the public callings as a solution of the trust problem", *Harvard Law Review* (1904); Burdick, "The origin of the peculiar duties of public service companies", *Columbia Law Review* (1911). Classic accounts of why some trades carry a duty to serve. **UNVERIFIED LEAD**
- Beale, *The Law of Innkeepers and Hotels* (1906). **UNVERIFIED LEAD**
- Singer, "No right to exclude: public accommodations and private property", *Northwestern University Law Review* (1996). **UNVERIFIED LEAD**
- Sandoval-Strausz, *Hotel: An American History* (2007), and his article on travellers, strangers and public-accommodations law in *Law and History Review* (2005). A historian's account of the innkeeper doctrine as the legal form of hospitality to strangers; the closest thing to a bridge between this tradition and hospitality studies. **UNVERIFIED LEAD**
- Non-delegable duties in tort, for example *Woodland v Swimming Teachers Association* [2013] UKSC, where I recall the court set out when a duty holder remains liable for a function it has contracted out. Serves R2.2c directly. **UNVERIFIED LEAD**
- A current hospitality-law textbook for the state of the doctrine and its civil-law counterparts. No specific title offered.
- Recent arguments for treating digital platforms as common carriers or public accommodations, which would bear on whether a booking platform inherits host duties. I can name no specific article with confidence. **UNVERIFIED LEAD**

### (e) Moral philosophy of role obligations and special obligations

**Why it matters.** R2.2 asks in so many words for "a clearer theory of role obligation". It also bears on R2.3: a theory of how role obligations are acquired gives the obligation a ground that does not mention standing.

**Held.** Kropf et al. p. 2 names the lineage (Vincent, after Hart). Kong p. 4 gives the opposing view (roles derivative of control). Darwall p. 28 on obligations in "various keys". Hart's Postscript has a record (`WS_A` §3; `PAPERS_TO_GET.md` item 7) and is unread. CF §2 abandoned the role ground ("ownership moves only with the role") because neither Kong nor Kropf supports it; no one then looked for a source that does.

**Candidates.**

- Hart, "Postscript: Responsibility and Retribution", in *Punishment and Responsibility* (2nd ed. 2008), pp. 210–237. Record in project. Not read. Source of "role-responsibility".
- Vincent, "A structured taxonomy of responsibility concepts" (2011), the account Kropf et al. build on. Named on the Kropf card; details **UNVERIFIED LEAD**
- Hardimon, "Role obligations", *Journal of Philosophy* (1994). As I recall, it distinguishes contractual roles (entered by choice, binding because one signed on) from non-contractual ones, and argues that a role obligation binds through the role's institutional definition. A commercial host is a contractual role in this sense: the hotel chose to open. **UNVERIFIED LEAD**
- Goodin, *Protecting the Vulnerable* (1985), which grounds special obligations in another's dependence on one's actions. It fits Shryock's "depend on their hosts" (p. S23) and would explain why a guest asleep in the host's building is owed more than a customer at a counter. A candidate answer to R2.4. **UNVERIFIED LEAD**
- Scheffler, "Relationships and responsibilities", *Philosophy and Public Affairs* (1997); Simmons, *Moral Principles and Political Obligations* (1979) for the voluntarist objection that roles bind only when assumed. Both **UNVERIFIED LEAD**
- Fiduciary theory: Frankel, "Fiduciary law", *California Law Review* (1983); Miller, "A theory of fiduciary liability", *McGill Law Journal* (2011). The September panel judged fiduciary duty "the standard case of an obligation constituting its bearer's role" (`manuscript/NOTES.md`, l. 646–647), and v4's trustee comparison went unsourced. Either source it here or leave it out. Both **UNVERIFIED LEAD**
- Assumption of responsibility (undertaking) as a ground of duty in tort, which pairs with Darwall's promise example. No specific source offered with confidence. **UNVERIFIED LEAD**
- Dare and Swanton (eds), *Perspectives in Role Ethics* (2020); Applbaum, *Ethics for Adversaries* (1999). Both **UNVERIFIED LEAD**
- Solomon, Surprenant, Czepiel and Gutman, "A role theory perspective on dyadic interactions: the service encounter", *Journal of Marketing* (1985). The service field's own use of role theory, and so a way to show what a role *obligation* adds to role *expectations*. **UNVERIFIED LEAD**
- `pedersen2022` (held, full text): "the ethics of office" for frontline staff. Re-read for what it says about duties that attach to an office.

### (f) Organisational and distributed responsibility

**Why it matters.** R2.1e and R2.2d (how responsibility is shared among hotel company, operator, employee, platform and vendor); R3.9 (authority is organisationally constrained). The outline's "institution" hides the structure that makes the reviewer's question hard: in a branded hotel the building's owner, the brand, the management company, the booking platform and the software vendor are usually different firms.

**Held.** Nissenbaum (full; many hands). Bovens (full; many hands at p. 457). Santoni de Sio and Mecacci (full). Casalegno et al. (full; converging responsibilities). Slattery pp. 24–25 (corporate context). Sharma and Mattila p. 911 (who is blamed). Gursoy p. 154 ("distributed responsibility" as a gap). Germann Molz 2018 p. 245 (platform shifts liabilities). `eu2024aiact` (provider and deployer). `WS_A` §1 dropped Constantinescu and Kaptein (2025), Lüthi et al. (2023) and Taylor (2024) because they "allocate responsibility among agents"; those records exist in the Consensus results and are now relevant.

**Candidates.**

- Thompson, "Moral responsibility of public officials: the problem of many hands", *American Political Science Review* (1980). **UNVERIFIED LEAD**
- Bovens, *The Quest for Responsibility* (1998). **UNVERIFIED LEAD**
- van de Poel, Royakkers and Zwart, *Moral Responsibility and the Problem of Many Hands* (2015). **UNVERIFIED LEAD**
- Cooper et al., "Accountability in an algorithmic society" (FAccT 2022). Seen as a Consensus hit in `WS_A` §1; not carded, not read.
- French, *Collective and Corporate Responsibility* (1984); List and Pettit, *Group Agency* (2011). For the claim that an organization, and not only its members, can be the obligor. Both **UNVERIFIED LEAD**
- Young, "Responsibility and global justice: a social connection model" (2006), for shared responsibility across a chain of firms. **UNVERIFIED LEAD**
- Hotel industry structure: work on management contracts and franchising, for example deRoos, "Hotel management contracts: past and present", *Cornell Hospitality Quarterly* (2010). **UNVERIFIED LEAD**
- Franchisor and brand liability to guests under apparent-agency doctrine (the guest relies on the brand's holding-out). This is the legal form of "who is the host when the sign says one name and the operator is another". I can name no case with confidence. **UNVERIFIED LEAD**
- Platform terms that define the platform as a non-party to the stay, and regulatory responses. Edelman and Geradin, "Efficiencies and regulatory shortcuts: how should we regulate companies like Airbnb and Uber?" (2016), is one I recall. **UNVERIFIED LEAD**
- GDPR controller and processor, as a second statutory model of a duty that stays with the party who determines purposes while processing is contracted out. The September panel used this example (`SYNTHESIS.md`, adjudication 9).

### (g) Host–guest negotiation and power in commercial hospitality

**Why it matters.** R1.2; R3.9; R3.8. The reviewer wants evidence that host–guest interaction is negotiated and creates value. R3 wants the authority behind that negotiation shown as bounded.

**Held.** Xiang et al. (full), Di Domenico and Lynch (full), Lugosi 2014 (abstract), Beatty et al. (full; non-hospitality sample), Golubovskaya et al. pp. 1294–1297 (power (in)equality theme). `WS_C` notes that the card file `farmaki2020power` does not exist. `WS_C` also recorded, without carding, Jonsson and Nyberg (2022) "Hospitality through negotiations", Hayes (2024, *Hospitality & Society*) on omotenashi, and Camilleri and Neuhofer (2017).

**Candidates.**

- Sherman, *Class Acts* (2007), as in (c): luxury-hotel ethnography with negotiation of entitlement between guests and workers. **UNVERIFIED LEAD**
- Lugosi, "The production of hospitable space: commercial propositions and consumer co-creation in a bar operation", *Space and Culture* (2009). Serves R3.8 (a bar). **UNVERIFIED LEAD**
- Lynch, "The commercial home enterprise and host", *IJHM* (2005). **UNVERIFIED LEAD**
- Wood, "Hotel culture and social control", *Annals of Tourism Research* (1994). **UNVERIFIED LEAD**
- Guerrier and Adib, "'No, we don't provide that service': the harassment of hotel employees by customers", *Work, Employment and Society* (2000), on the limits of what a guest may claim. **UNVERIFIED LEAD**
- Korczynski, *Human Resource Management in Service Work* (2002), on the "customer-oriented bureaucracy" and the managed appearance of customer sovereignty. Serves R3.9. **UNVERIFIED LEAD**
- Employee empowerment in hotels: Lashley's work on empowerment in services (1990s); Hales and Klidas, "Empowerment in five-star hotels: choice, voice or rhetoric?", *IJCHM* (1998). Evidence on how much authority frontline staff ever had. Serves R3.9. Both **UNVERIFIED LEAD**
- Bitner, Booms and Tetreault, "The service encounter: diagnosing favorable and unfavorable incidents", *Journal of Marketing* (1990), on employee responses to special requests, in hotels and restaurants among other settings. **UNVERIFIED LEAD**
- Hayes (2024), *Hospitality & Society*, on co-created hospitable moments. Record seen in `WS_C`; closed access; not read. It is in the target journal.
- Farmaki and Kaniadakis, "Power dynamics in peer-to-peer accommodation", *IJHM* (2020). The plan lists `farmaki2020power` as held; no card file exists. **UNVERIFIED LEAD** as to details.

### (h) Host duties under platforms and automation

**Why it matters.** R2.1e (platform and vendor as possible holders), R2.5b (formats), R3.7 (kinds of technology), and the positioning against Germann Molz (2026).

**Held.** `germannmolz2026` (abstract, must-engage), `germannmolz2018scale` (full), `riordan2024digitally` (abstract), `roelofsenminca2018` (abstract), `chengfoley2019`, `jhaver2018anxiety`, `liang2017superhost`, `leick2024professionalisation`, `bosma2022platformed`, `liu2026hospitableness` (full), `leelu2024consciousness`, `sharmamattila2025rights` (full), `gao2026hostessing`, `gursoy2026reconceptualizing` (full), `tussyadiah2020automation`, `ivanov2019ultimate` (abstract). I did not open the cards for Jhaver, Liang, Leick, Bosma, Lee and Lu, Gao or Tussyadiah in this run.

**Candidates.**

- Germann Molz (2026) in full. Until someone reads it, the paper cannot say what the nearest prior work claims about host obligation. Held; the task is the read.
- Farmaki, Stergiou and Kaniadakis, "Self-perceptions of Airbnb hosts' responsibility: a moral identity perspective", *Journal of Sustainable Tourism* (about 2019). If it is what I recall, it studies what platform hosts think they owe. **UNVERIFIED LEAD**
- Ikkala and Lampinen, "Monetizing network hospitality: hospitality and sociability in the context of Airbnb" (CSCW 2015); Lampinen and Cheshire, "Hosting via Airbnb" (CHI 2016). Both **UNVERIFIED LEAD**
- Germann Molz's earlier work on "network hospitality" (around 2012–2014), cited inside her 2018 article as "Germann Molz 2014a" (card `germannmolz2018scale`, p. 244). **UNVERIFIED LEAD** as to title and venue.
- Robot and AI ethics in hospitality beyond perception studies: Tuomi, Tussyadiah and Stienmetz, "Applications and implications of service robots in hospitality", *Cornell Hospitality Quarterly* (2021); McCartney and McCartney, "Rise of the machines", *IJCHM* (2020); Wirtz et al., "Brave new world: service robots in the frontline", *Journal of Service Management* (2018). All **UNVERIFIED LEAD**
- Evidence on unstaffed or "contactless" hotels and self-check-in rentals, the limiting case R2.5b names as "highly automated services". I can name no study with confidence. **UNVERIFIED LEAD**

---

## 5. Where the authors' position could sit

The three positions below differ on what activates the obligation and who holds it. They are not exclusive. I state what each answers, what each costs, and then a recommendation the authors are free to reject.

### Position A — Threshold sovereignty

**Claim.** The obligation arises when a party that controls a space admits a stranger into it. Whoever is sovereign over the premises holds it, because the admitted person now depends on that party for safety, access and terms.

**This is the current position** (pitch l. 9; PO l. 53, 56, 67).

- *Answers.* R2.1a and R2.1c in outline. R2.4 in part: the guest's body, sleep and belongings are inside the host's space, which is not true of a bank customer or an online shopper (though it is true of a hospital patient). R2.5b: the framework should fit best where one party controls the premises and weaken where control is split (short-term rentals) or absent (delivery).
- *Does not answer.* R2.1e and R2.2d: in a branded, managed hotel "sovereignty over the premises" is divided among owner, brand and operator, so the position restates the question. R3.11: one trigger, one duty. R2.3a: untouched. R3.8: threshold imagery favours the front desk.
- *Risks.* Shryock's host is a household; the commercial transfer is the authors' step (`WS_A` §4). Di Domenico and Lynch show sovereignty producing host *power* and guest silence. "Simply because they walked in the door" reads as unconditional hospitality.
- *Needs.* (b) for conditional against unconditional welcome; (c), especially Pitt-Rivers and a fuller use of Shryock; Bulley; O'Gorman 2009 carded; Goodin on dependence from (e).

### Position B — Public calling

**Claim.** The obligation arises because the host holds itself out to the public as ready to receive. A party that professes hospitality as its trade undertakes duties to whoever presents in the expected way. The proprietor holds them. Staff, contractors and systems perform them, and the duty stays where the holding-out was made.

- *Answers.* R2.1a and R2.2a (activation by holding out, plus the guest's presenting). R2.1c and R2.2b (the proprietor, not the servant). R2.2c (performance delegable, duty not). R2.4, with a historical fact: the law imposed a duty to receive on innkeepers and carriers and not on banks or shops. R2.5b (inn against lodging house maps to hotel against short-term rental). R3.10 (the guest's reciprocal duties are part of the doctrine). R3.9 (the host's authority was always bounded by law and by the terms of the holding-out). R2.1e in part: "who holds out?" is an answerable question for brand, operator and platform.
- *Does not answer.* The richer content. The legal duty covers reception, safety and goods; it has no negotiated exception and no duty to explain. R3.11 only in part.
- *Risks.* Jurisdiction (common law). A critical-hospitality readership may read a legal ground as reductive. None of it is held or verified; the authors would be entering a literature new to the project five weeks before the deadline. Every doctrinal statement in section 4(d) is from my memory.
- *Needs.* (d) in full; O'Gorman 2009 as the bridge from hospitality studies; Sandoval-Strausz if it proves to be what I recall; non-delegable duty from tort.

### Position C — Institutional role obligation

**Claim.** "Host" is a social role with obligations attached. In commercial hospitality an organization occupies that role by choosing to open for guests. Employees hold job duties derived from the organization's role by contract; they do not hold the role. Tasks within the role can be delegated to people or systems. The role's obligations stay with its occupant until another party takes the role and is recognized as holding it.

- *Answers.* R2.2 in R2's own vocabulary. R2.2c (tasks against role). R3.11: role obligations are defined by social and organisational expectations, so the welcome is plural and context-dependent by construction. R3.8: the role of host exists in restaurants, bars and events as well as hotels, with different content. R3.9: the role's occupant is an organization, and each employee's authority is whatever the organization assigns. R2.2d in part: several organizations can share or split a role, and the question becomes which of them guests and the public recognize as host.
- *Does not answer.* R2.4 by itself. Role obligations exist in every institution, banks and hospitals included. Hospitality-specific content has to come from (a), (c) or (d).
- *Risks.* Kong treats roles as derivative of control (p. 4), so the paper must say where it differs and why. Hart is unread. Telfer's line makes hospitableness a personal virtue, which an institution cannot have; the paper would need to separate the obligation of the role from the hospitableness of the person. Slattery denies that "host" is the right name for the commercial role at all.
- *Needs.* (e) Hart, Hardimon, Vincent; (f) for shared roles; Telfer and King from (a); Kropf et al. and Kong, already held.

### Recommendation

I recommend C as the frame, B as its main evidence, and A as description, for four reasons.

1. **C is the theory R2 asked for by name**, and it is the only position that answers R3.11, R3.8 and R3.9 by its structure. A defended alone leaves all three open.
2. **B supplies what C lacks.** It gives a concrete activation condition, a named holder, a rule about delegation, reciprocal guest duties and a hospitality-specific boundary. It turns "we assert the obligation" into "this trade has carried this obligation, enforceably, for centuries". It also lets the paper concede R2.4 honestly: the *mechanism* of lost address is general, and what hospitality contributes is a role whose duties to the person received are unusually old, unusually personal and unusually well specified.
3. **A is where the paper's best prose and its held anthropology already sit.** It works as the account of what the role is like from the guest's side (dependence, asymmetry, being in another's space). It does not work as the ground, because of the divided-sovereignty problem.
4. **Cost.** B is unverified and new to the project. If the legal reading does not hold up, or five weeks is too short, C with (a) and (c) is a defensible fallback: Telfer, King, Lashley and Pitt-Rivers read in full would already replace assertion with a positioned account.

Two repairs apply whichever position the authors take.

- **Separate the two duties, and break the circle with the separation.** The first-order duties (receive, protect, attend, hear a request) are owed to the guest and grounded by A, B or C. *Standing* is the guest's position as the person to whom those first-order duties are owed; Hohfeld and Darwall support exactly that and no more. *Accountability* is the organizational arrangement by which the holder answers for how the first-order duties were met. On those definitions standing does not mention answering, accountability does not define standing, and "held against exercised" (PO l. 82) becomes the difference between having the claim and having an arrangement through which to press it. Kong, Kropf et al. and Nissenbaum then do the job they are suited to: showing that the second-order duty stays with the delegator.
- **Decide whether the negotiated exception is owed or merely possible.** The pitch treats it as "an inherent part of that obligation" (l. 21). The held evidence shows compensation (Xiang et al.), deference (Di Domenico and Lynch) and managerial limits (Golubovskaya et al. p. 1297). A weaker claim fits the evidence and still does the paper's work: what is owed is a hearing by someone with the authority the organization has in fact assigned, not the exception itself.

---

## 6. Other project-level problems, ranked

1. **The first-order duty is unbuilt** (sections 2–5). Everything else is smaller.
2. **The word budget and the reviews pull in opposite directions.** The outline allots 6,750 words of body and 2,250 of references (PO l. 27). R2 wants a theory of role obligation, multi-actor allocation, a response on banking and healthcare, and boundary conditions. R3 wants a longer explanation of the roadmap table, fuller limitations, a fuller agenda and a fuller conclusion. §2 has 1,000 words for origin, holder, delegation, distinctness and four definitions. Something has to shrink. R3 found §6 and §7 the weakest ("meandered"), and they hold 1,500 words between them. The open decision in RP ("Confirm whether the 9,000-word all-inclusive limit applies") is still unchecked and now matters more.
3. **R3's style objection reaches the outline, and R3 raised AI assistance.** The tone table catches v4's colloquial lines. The outline's own bullets carry the same habit in a different register: paired short sentences that close on a turn ("The role of hosting can move to a machine. The answering cannot."; "What failed is the address."). The revision scaffolding is machine-drafted throughout, and each file says so. The pitch is the authors' text. For this reviewer, §2 and §3 should be drafted by the authors from the sources, in the venue's 150–250-word paragraphs (`AGENTS.md`, editing rules), with the outline as a checklist and not as prose to adapt.
4. **The contributions differ across four files.** v4 §8: AI as constitutive mediator; competence against standing; the test (`DRAFT.md` l. 148–152). RP §8: a theory of hosting obligation; relational and conferred standing; the test with its roadmap. Pitch l. 15: where the obligation lies; guest standing; the five-stage roadmap (the test is not named as a contribution). PO §8: the pitch's three, then "AI as a constitutive mediator", "Human-centricity" and "What the hospitality lens adds" as further bullets. R3 was "unconvinced that the stated contributions were achieved". The paper needs one list, and `WS_C` already warned that the first item cannot be the obligation itself, since "the field already says that hospitality is an obligation".
5. **PO Table 3, stage 4 repeats an error CF corrected.** "Create a forum obliged to answer challenges" (l. 212) reverses Bovens, for whom the actor answers and the forum questions (CF §1.3; PO's own bullet at l. 192 has it right). R3.13 asks what "forum" means.
6. **Sources in the pitch and outline that the project has not read or carded.** O'Gorman 2009 (no card; pitch l. 9, PO l. 53). Lashley 2000 (metadata; the attributed sentence is second-hand). King 1995 (second-hand). Germann Molz 2026 (abstract; carries the positioning). Lugosi 2014 (abstract). The authors' rule is that nothing enters a draft unverified.
7. **Four points where the authors' pitch outruns its sources.** I flag them for the authors and have changed nothing.
   - l. 9: "because they control the physical premises". The causal link is the authors'; see section 3, Shryock.
   - l. 9: algorithmic governance "relocating answerability to the delegating institution (… Nissenbaum 1996 …)". Nissenbaum says accountability "will be lost" unless new lines are built (card, PDF p. 11; CF §2).
   - l. 11: "Every institutional duty generates a correlative claim". Hohfeld's correlativity holds for duties owed *to* someone (card, p. 33; Darwall card, pp. 20, 28).
   - l. 11: "an authority–answerability split (Gursoy 2026: 160)". The term is the paper's. Gursoy's sentence concerns accountability "when harm, bias, or exclusion arise" (card, p. 160).
8. **The opening case does not show a guest.** Garcia et al. study managers and pricing recommendations; "the guest who questions the rate meets an employee who cannot answer for it" (PO l. 39) is the authors' construction (CF §2, last item). R3 objected to "leaps" and to the hotel desk as the model of hosting; the new opening has both.
9. **Stale statements in `REVISION_PLAN.md`.** Its §2 still attributes the trigger typology to Santoni de Sio and Mecacci, keeps the trustee comparison and "ownership moves only with the role", and its §3 says standing "exists only when a counterparty… is within reach". CF and REVISION_PROPOSAL withdrew all four. Its header says the R2 and R3 reports are not in hand. Anyone who reads RP first will be misled.
10. **Small inconsistencies across files.** The title differs (REVISION_PROPOSAL: "…and the Address of Hospitality's Obligation"; PO and v4: "…and Responsibility in Phygital Hospitality"). §2 has three titles (RP "Hosting as an obligation of the threshold"; REVISION_PROPOSAL "The host's obligation and its address"; PO "The host's obligation under delegation"). §7 is 900 words in RP and 950 in PO. The welcome has four elements in PO §3 and three in Table 1.
11. **Well-being satisfies neither reader.** The editor asked for it (`RESPONSE_TO_EDITOR.md`); R3 found the link unclear; the plan cuts it to two sentences that keep the speculative aggregate claim (PO l. 230). It needs either a stated mechanism or an explicit hand-off to future research.
12. **No file fixes the vocabulary for the technology** (R3.7, R3.17). A short typology (systems that decide, interfaces that present, robots that perform, platforms that intermediate) would also serve R2.5a, because the decision-making kind is the one that needs answerability.

---

## 7. Research questions for a deep-research phase

Each question names the reviewer points and outline sections it serves. All searches should record database, query and date, and return records before any reading.

1. **Activation and holder in innkeeper law.** In English and US common law, what conditions brought the innkeeper's duties into force (holding out as an inn, the arrival of a traveller, fitness, ability to pay, available room), what did the duties contain (reception, safety, goods), and who bore them (proprietor or servant)? Which legal-history and hospitality-law sources state this, and has any hospitality-studies author used the doctrine to ground host obligation? *R2.1a, R2.1c, R2.2a, R2.2b, R2.4; PO §2.1, §2.3.*
2. **Delegable performance, non-delegable duty.** What do role-obligation theory (Hart's role-responsibility; Hardimon; Vincent) and the tort doctrine of non-delegable duty say about which part of a role-holder's obligation can pass to an employee, contractor or system and which cannot? Does any source apply either to hotels, for example the innkeeper's liability for servants and contractors? How does that account differ from Kong's control-based ground (2026: 4)? *R2.2c, R2.1b; PO §2.2.*
3. **Who is the host among several firms.** How do hospitality-management, legal and platform-governance sources allocate duties to the guest among property owner, brand or franchisor, management company, employee, booking platform and technology vendor (management contracts, franchise apparent agency, platform terms of service, the AI Act's provider and deployer, GDPR controller and processor)? Which party do guests and courts treat as holding out as host? *R2.1e, R2.2d; PO §2.1, §4.*
4. **Does hospitality differ from banking, healthcare and e-commerce on this mechanism?** Do banks (fiduciary and duty-of-care obligations) and hospitals (duty to treat on presentation) already carry pre-harm duties and negotiated exceptions? If so, what remains distinctive of hosting in the hospitality literature: bodily presence in the host's space, dependence, temporariness, the duty to receive strangers? Is there a published comparison? *R2.4, R2.2e; PO §2.3, §8.*
5. **Virtue or institution.** Does the hospitableness literature (Telfer; King 1995; Lashley; later scale work; Liu et al. 2026: 2) treat the host's duty as a personal disposition and motive, or as an obligation of a role or organization? How have hospitality scholars reconciled a commercial motive with a duty to the guest, and who has argued it cannot be done (Slattery; Aramberri)? *R2.1a, R3.11; PO §2.1.*
6. **What guests owe, and how it conditions their standing.** What do anthropological accounts (Pitt-Rivers; Shryock; Candea and da Col; Selwyn), King (1995) and innkeeper law (payment, conduct, the right to eject) say about the guest's duties, and under what conditions a guest loses the claim to be received or heard? Is there empirical work on guests' sense of obligation in commercial settings beyond Manfreda and Harkison (2025)? *R3.10, R2.3; PO §3.*
7. **Negotiation and bounded authority in commercial hospitality.** Which empirical studies in hotels, restaurants and bars document a guest's request or refusal changing an outcome, and what do they show about the limits the organization places on frontline authority (empowerment studies, special-request studies, luxury-hotel ethnography)? Preference to *Hospitality & Society*, *IJHM*, *Annals of Tourism Research*, *IJCHM*. *R1.2, R3.9; PO §3, §4.*
8. **Hosting beyond the hotel desk, and where the host role thins out.** Across restaurants, bars, events, hostels, cruise ships, short-term rentals, self-check-in rentals and unstaffed hotels, who is treated as host and what duties are recognized? Is there evidence on guest recourse in unstaffed or contactless properties? For which formats does the literature say no party holds the host role? *R3.8, R2.5b; PO §5, §9.*
9. **Which decisions need immediate recourse.** What typologies of automated decisions exist by stakes, reversibility and time-criticality (admission and ejection, pricing, room assignment, safety, routine requests), and what evidence, from service recovery or from law ("legal or similarly significant effects"), indicates which require a reachable person at the moment of decision and which tolerate delay? *R2.5a, R3.7; PO §5, §7.*
10. **Standing without circularity.** In the philosophy of directed duties, how do authors separate (i) the first-order duty, (ii) the obligee's standing to claim its performance, and (iii) accountability for breach (Darwall 2013; Hohfeld 1913; Feinberg's "The nature and value of rights"; Duff, as cited by Coeckelbergh 2019; Bovens 2007)? Is there an account in which standing is fixed by the first-order duty alone, so that accountability can be defined afterwards without reference back? *R2.3a, R2.3b; PO §2.4, §3, §5 Table 1.*
