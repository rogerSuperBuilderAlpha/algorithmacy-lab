# Fable read, research run rr-2026-11-h, list (b)

10 November 2026. *Drafted by Claude (Fable reader). None of this is the authors' wording.* I followed `FABLE_BRIEF.md` as adapted for run rr-2026-11-h. I read each of the twelve cards against its saved source, or against a record re-fetched today where no source is saved, then read `WS_H3`, `WS_H4` and `WS_H5` in full against the corrected cards, then `DRAFT.md` (v4) and `PITCH_AND_OUTLINE.md`. I edited the twelve cards and the three WS files only. I did not touch the manuscript, the pitch, the outline, `references.bib`, `CLAIMS.md` or `CARDS_INDEX.md`, and I committed nothing.

**Conflict flagged.** The repo `CLAUDE.md` and the arm's `AGENTS.md` say to branch, commit and push after every step. The brief says not to commit. I followed the brief.

**Validator.** `build_index.py --check` reports no new error on my twelve cards. The standing failures ("not in references.bib", "bib note") remain for the main session.

---

## 1. Were the fixes applied after VERIFY_H_v1 and v2 right?

Every fix logged on my cards and at the end of the three WS files is right against the source. Six places needed more work than the verifiers asked for:

1. **Cobbe et al., over-corrected.** The fix removed "allocation must follow factual control" and added "they state no general allocation rule". The authors do state a direction: "Accountability should thus be allocated to actors across supply chains based on a proper understanding of their technological and political economic dynamics" (arXiv p. 8, §4.1.2). Card and WS_H3 now quote it.
2. **WS_H5, a fix made on the card and missed in the WS.** "Differential pricing becomes significant only if ..." was still there. WP251 p. 22 says "could also have a significant effect if, for example".
3. **Golubovskaya et al., p. 1297, missed by the verifier.** The card placed the manager's remark under "organizational culture" and "in one breath" with "empowering the frontline staff". The remark sits under "leadership" and comes from P-7; the "empowering" line is P-15, in another paragraph. The authors present the remark as giving staff "confidence and power to feel like a 'host'", the opposite of the bound on staff authority H4 read into it.
4. **Baum and Laux, locator.** The braking quotation is on p. 8, not pp. 7–8.
5. **Cobbe et al., locator.** "We do not offer concrete technical or organisational proposals" is on arXiv p. 2, not pp. 2–3. (VERIFY_H_v2 says both.)
6. **Crinkley, reporter pages.** I re-fetched the Caselaw Access Project copy and saved it in `sources/crinkley1988holiday/fable/`. Doctrine and test are at 166; the appearance holding and the reliance finding are at 167, not "166–67".

---

## 2. Cards

| Card | Result |
|---|---|
| `crinkley1988holiday` | **Changed.** Reporter pages re-mapped from a saved copy. Added: the brand's liability is vicarious only (para 49); the dissent concurs that liability was a jury question (para 59); the opinion itself records a contrary North Carolina decision, *Hayman* (fn 3), and the dissent's diversity objection (para 68). "Designed and built" completed with "originally ... and sold in 1976". |
| `cobbe2023understanding` | **Changed.** The authors' own allocation sentence quoted (p. 8, §4.1.2); "We do not offer..." moved to p. 2; their adoption of the mechanism sense quoted (p. 2); the proceedings-page map recorded as the verifier's, unchecked by me. |
| `kaniadakis2022responsibilisation` | **Changed.** "The party with the duties and the least authority" withdrawn as H3's phrase: the same hosts screen and decline guests (p. 12). Added two host statements of what guests owe (p. 14) and the sample breakdown (p. 8). |
| `pittrivers2012law` | **Changed.** The "no right to make claims" reading qualified: the guest holds a right "to respect" (p. 514) and is owed protection, precedence and attention (p. 516); what is withheld is pressing the claim. P. 509 marked as said of the beggar. "Host's prerogative" completed with "in the placing of his guests". Oblique protest, return hospitality and the door as the limit of the host's responsibility added (pp. 513–515). |
| `hewagama2019service` | **Changed.** "Not held by whoever the guest meets" withdrawn: the abstract says graduated by rank, not absent at the front line. "Authority to make an exception" marked as the paper's term. Abstract re-fetched; depth stays abstract. |
| `hales1998empowerment` | **Changed.** "Responsibility without voice over the rules" restated in the abstract's words: neither choice nor voice. One note added on what that does to the paper's baseline. Depth stays abstract. |
| `didomenico2007host` | **Changed, slightly.** Both applied fixes confirmed. One located line added (p. 332, "always at their beck and call"). |
| `lugosi2009production` | **Changed.** "To a community, not to the operator" corrected to the source's "not just to the hosts/commercial providers" (Conclusion). One quotation added. Version of record still unchecked. |
| `golubovskaya2017meaning` | **Changed.** P. 1297 relocated and re-read (item 3 above); P-9 (p. 1298) completed with "a bare minimum at most" and marked as a stated stance, not an observed removal; pointer to the new `king1995what` card. |
| `baum2026constitutive` | **Changed.** Locator fixed; the proposed test, set in quotation marks with a page number, marked as H5's wording; three quotations added (p. 6; p. 6 n. 9; p. 12); note that a guest's later appeal is not the source's asynchronous mode. |
| `gdpr2016art22` | **Changed.** "Secures a later appeal" in Where-it-enters conditioned and marked as H5's reading. Added that outside the Art. 22(2) exceptions the Article works as a prohibition. |
| `article292018guidelines` | **Changed.** EDPB endorsement verified from the Board's page (date still unverified). Three quotations added (pp. 19, 21, 23). "Says nothing about timing" refined: p. 27 calls the intervention a "review". |

No `status` or `read_depth` changed. No flag changed.

---

## 3. WS files

Each change is listed at the end of its file under "Fable corrections". The ones that alter a conclusion:

- **WS_H3.** "They disclaim control in contract (Cobbe et al., p. 10)" was the reverse of the source: providers disclaim accountability while using service agreements "to maximise control over deployment" (p. 10). "In Kaniadakis & Farmaki's interviews, responsibility is 'removed ...'" quoted the authors' introduction as a finding. "R2.1e and R2.2d, fully" reduced to one US appellate decision plus H3's own proposal.
- **WS_H4.** "v4's p. 6 sentence ... is wrong as a claim about the field" withdrawn. In v4 "Neither" refers to two studies, and v4's field-level claim is that the guest's side is unmeasured, which no source here contradicts. "Di Domenico and Lynch show standing absent with the address present" reduced to one withheld complaint in one researcher's note, beside the same source's evidence that hosts answer paying guests' demands (pp. 332, 335). "Every hospitality source ... assigned and graded" corrected. Pitt-Rivers's support for standing as *held* added.
- **WS_H5.** "A later appeal is asynchronous" marked as H5's analogy. The "law secures the later appeal" reading limited to the Art. 22(2) exceptions. The pricing "only if" removed.

Everything else in the three syntheses follows from the cards as corrected, or is already labelled as the workstream's inference.

---

## 4. For the authors

Quoted sentences are yours, from the pitch and from v4, or the outline's where marked. None of the twelve sources is cited in v4, so nothing below is a miscitation in v4; the one citation at issue is in the pitch (item 4). Items are ranked by how much the argument leans on the sentence.

### 1. The guest's power to press claims is not part of hospitality in these sources. It belongs to the commercial side.

Sentences:

- v4 §2: "A guest can ask a question, turn down an offer, demand an explanation, challenge a decision, or ask to be treated as an exception to the usual rule (Lynch 2017; Beatty et al. 2016). These moves are part of what separates hospitality from plain service."
- Pitch: "Every institutional duty generates a correlative claim, giving the guest the standing to direct demands back to the host (Hohfeld 1913: 33; Darwall 2013: 28, 31–32)."
- Pitch: "Hospitality asks what is owed to a person simply because they walked in the door, treating the capacity to negotiate an exception as an inherent part of that obligation."
- Outline §3 (Claude's draft): "Standing is the correlate of the host's obligation: the guest's authority to address claims to the institution that owes the welcome." Outline §2.3: "The obligation includes the capacity to make a negotiated exception".

**Contradicted, in part.** Pitt-Rivers lists the same moves as breaches of the guest's role. A guest who "makes claims or demands ... usurps the host's right to ordain according to his free will, even where custom lays down what he should wish to ordain" (2012, p. 515). A guest who "refuses what is offered" thereby "infringes the role of guest" (p. 515). The dissatisfied guest "has no recourse but to retire from his role altogether by walking out" (p. 513). Pitt-Rivers places demands and criticism with the community member, not the guest: he was kept a guest, "where I had no rights", and out of the status "where I might assert myself, make demands and criticisms" (p. 512). On correlativity he says the opposite of the pitch for one case: "even though a diffuse obligation exists towards the beggar, he is not endowed with any corresponding right" (p. 509). Di Domenico and Lynch's researcher's note draws the line where Pitt-Rivers does: "in a hotel one might complain about the beds being uncomfortable, but as the guest in the home one does not, it's not the done thing" (2007, p. 333).

**Supported, in part.** The host's side of the sentence stands. The host infringes if he "fails to protect his guest" or fails "to show concern for their needs and wishes" (p. 516); the guest holds a right "to respect" (p. 514); "each must accede to the desires of the other" (p. 513). So the sources support an obligation owed to the guest, and standing as *held*. They do not support the guest's demand, or a negotiated exception at the guest's instance, as hospitality's own.

**"Simply because they walked in the door": qualified.** Guest status is conditional on conduct in every source that addresses it: any infringement "entitles the person slighted ... to relinquish his role" (Pitt-Rivers p. 517); the commercial guest's "only obligation is to pay and behave reasonably" (Golubovskaya et al. 2017, p. 1286, reporting King 1995, unread); "We've thrown people out before" (Di Domenico and Lynch, p. 334).

What follows: the argument needs a sentence saying where the guest's claim comes from, since the anthropology of hospitality withholds it. H4's proposal (payment, public calling) is an inference no source here states.

### 2. "These four sit in one person" does not describe the staffed hotel.

- v4 §2: "In an ordinary face-to-face welcome these four sit in one person." (Outline §2.4 repeats it.)
- v4 §7: "They lose the pause at the desk where an experienced employee might once have seen that the standard rule did not fit, and made an exception."
- v4 §4: "The craft depends on the employee keeping some of the decision-making power they seem to give away."

**Contradicted for hotels; supported for the owner-run commercial home.** In thirty Sri Lankan hotels service recovery was "carefully stage-managed and 'staircased' ... with empowerment strongly related to hierarchical level" and "deliberately graduated according to rank" (Hewagama et al. 2019, abstract only). In Amsterdam five-star hotels "there was little 'empowerment' in practice and what there was amounted to increased employee responsibility rather than greater choice over how work was done or more voice in organizational decisions" (Hales and Klidas 1998, abstract only). Hotels already generate "standardized procedures and scripted interactions which mitigate employee freedom" (Golubovskaya et al., p. 1295). And in 1981, with no algorithm anywhere, the welcome at a Holiday Inn desk was split among three firms: owners, TRAVCO "in actual day-to-day control", and the franchisor (*Crinkley*, para 7, 844 F.2d at 159). The baseline does hold where Di Domenico and Lynch found it: owner-hosts who set the rules, admit and eject (pp. 332–335).

What follows: the split the paper names predates the algorithm. The phygital claim is safer as a claim about what happens to an already graded path to authority. Two of these three sources are abstract-only.

### 3. "The organization" and "the institution" are several firms.

- Pitch: "answerability relocates to the delegating organization rather than dissolving into the machine"; "the obligation to answer remains with the organization"; "it establishes where the obligation to host lies under algorithmic delegation".
- Outline §2.1 (Claude's draft): "That obligation belongs to the institution that opened the threshold."
- v4 §4: "A host who gives the answering to a system has given it to no one."
- Outline §4 (v4 §3): "Commercial hospitality inserts the company and its employee. Phygital hospitality inserts an algorithm."

**Supported in structure, qualified on the singular.** *Crinkley* supports the core move: a contractual disclaimer does not shed answerability ("the denial of an agency relationship in a franchise agreement is not alone determinative of liability", para 51, at 167). But the court held three parties answerable to the same guests (para 9, at 159), and it reached the brand because the brand held the property out as its own and the guests relied on that (paras 49–52), not because the brand controlled the premises. The holding is one US circuit applying North Carolina law, on reliance evidence the court called "marginal" (para 52), against a contrary state decision it had to distinguish (fn 3). On the technology side, what phygital hospitality inserts is a chain of firms: "there is ... typically no one actor in overall control of a supply chain" (Cobbe et al. 2023, arXiv p. 7), and the vendor keeps control while it "disclaim[s] legal accountability" (p. 10). The deploying hotel may have "no access to the provider's systems, control over them, or knowledge of how they work" (p. 8). In short-term rentals hosts see the platform as "orchestrator of the guest–host relations" that treats "hosts as Airbnb employees" (Kaniadakis and Farmaki 2022, p. 14; hosts' perceptions only).

**"Because they control the physical premises"** (pitch, second paragraph): supported by Pitt-Rivers, "A host is host only on the territory over which on a particular occasion he claims authority" (p. 514), and qualified by *Crinkley*, where the party held answerable for holding out neither owned the premises nor ran them day to day. Pitt-Rivers also bounds the duty at the edge of the territory, where "the host is quit of his responsibility" (p. 514). A premises-control ground does not obviously reach the booking app.

### 4. An address is necessary. One source suggests it is not sufficient, and the pitch's citation for the point shows something else.

- Pitch: "Crucially, the argument does not treat the physical presence of frontline workers as a substitute for standing (Di Domenico and Lynch 2007: 332–333), since floor staff often lack the authority to alter system rules (Gursoy 2026: 160; Möhlmann et al. 2021)."
- Pitch: "the failure of automated hospitality lies in this structural loss of someone for the guest to address"; "only institutions can establish the addressee required to exercise a claim".
- Outline §3 (Claude's draft): "Presence alone is not enough. In commercial homes the balance of power rests 'firmly' with hosts, and guests do not complain (Di Domenico and Lynch 2007: 332–333)."
- v4 §7: "Friction, on this reading, is the moment at which standing can be exercised, and nothing more."

**Qualified.** Di Domenico and Lynch's pages 332–333 concern owner-hosts, not frontline workers, and those hosts held full authority. The guest's complaint was withheld for a different reason: "The social niceties and obligations inherent in the interaction" (p. 333). So the pages support "presence is not a substitute for standing" but not the "since" clause attached to it. Three cautions on the outline's wording: the balance of power "is perceived by hosts to rest firmly with them" (p. 332; the outline drops "perceived by hosts"); "guests do not complain" rests on one covert researcher's note (p. 333); and the same hosts are "always at their beck and call" (p. 332) and "must meet the desires and demands of the paying guest" (p. 335). The source to cite for a present human who cannot change anything is Baum and Laux: a human who "rubberstamps without genuine judgment does not thereby become an overseer" (2026, arXiv p. 12), and WP251: oversight must be "meaningful, rather than just a token gesture ... carried out by someone who has the authority and competence to change the decision" (p. 21).

### 5. Interrupting and reversing are different things, and the pitch asks for one under the name of the other.

- Pitch: "Instead, hospitality systems must be designed around interruptibility. Preserving guest standing requires constitutional safeguards within the organization: reachable human staff who retain the authority to reverse algorithmic decisions".
- v4 §7: "The fourth: a person must stay reachable who can actually reverse or revise the decision ... Keeping a human in the loop is not enough."
- v4 §5: "An opaque algorithm can still help hospitality, if its rules are reasonably steady and an empowered employee can question or override it."
- Outline §7 (Claude's draft): "The deploying entity is best placed to reverse a decision (Lyons et al. 2021)."

**Supported on authority; qualified on timing.** The authority requirement has strong support: humans need "the capacities, information, and authority to make that position meaningful and effective" (Baum and Laux, p. 2); "Any review must be carried out by someone who has the appropriate authority and capability to change the decision" (WP251, p. 27). "Keeping a human in the loop is not enough" is Baum and Laux's own point (pp. 11–12). On timing, they separate what the pitch joins: the test is "not elapsed time but whether intervention can occur before the token output becomes effective" (p. 6). Reversal after the fact is not interruption, and review that only shapes "future iterations" (p. 7) does not reach the guest in front of the desk. Some decisions are too fast for anyone; there the only human control is a rule set in advance (p. 8) that stays revisable (p. 6, n. 9). So "must be designed around interruptibility" needs a scope. H5's typology offers one; it is H5's inference, and no source makes it for hotels.

Two further limits. In Baum and Laux the person who interrupts is the overseer, not the person affected; the guest-initiated interruption is the paper's own idea. And "within the organization" meets Cobbe et al.: the deploying firm can change the outcome at the desk but may be unable to see or change the vendor's rule (pp. 8–9), which qualifies "best placed to reverse".

### 6. Algorithmic governance does say something about how a person addresses a human when a machine decides.

- Pitch: algorithmic governance "has nothing to say about duties owed upon arrival or an account of how a guest can exercise standing when a machine stands in for the host."
- Outline §8 (Claude's draft; outside the sections you named, included because the hit is direct): "The address of hospitality's obligation is, for now, a matter for institutions rather than law."

**Contradicted on the second half, supported on the first.** GDPR Art. 22(3) gives the person subject to a solely automated decision "at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision". The regulators read Art. 22(1) as "a general prohibition" that "applies whether or not the data subject takes an action" (WP251, p. 19), and name "cancellation of a contract" as a legal effect (p. 21). That is an account, in law, of an addressee and of who must supply it. It is narrower than the paper's: it bites only on solely automated decisions with legal or similarly significant effect, it states no timing, and it says nothing about arrival. I found no case applying it to a hotel decision. The pitch's sentence is safe if it says that algorithmic governance gives the affected person a right to contest significant decisions and nothing about what is owed on arrival.

### 7. What guests owe is stated in the literature; v4's narrower claim survives.

- v4 §2: "Neither asks what, if anything, a guest owes a commercial host." "The guest's side of the commercial bargain remains, for practical purposes, unmeasured".
- Outline §3 (v4 §2): "The field measures whether guests feel welcomed but not the guest's own standing."

**Supported as written; the impression it leaves is contradicted.** "Neither" refers to two studies, and the field-level claim is about measurement. None of these sources measures what guests owe. But the question is asked and answered: Pitt-Rivers lists the guest's infringements (p. 515) and the loss of the role (p. 517); the commercial guest's duty is "to pay and behave reasonably" (Golubovskaya et al., p. 1286, reporting King); "guests have obligations to respect the rules of the host and to reciprocate" (Lugosi 2009, accepted manuscript, section "Hospitality"); Airbnb hosts say of guests that "their responsibility is to understand what the sharing economy is all about" (Kaniadakis and Farmaki, p. 14). R3.10 has a point about the impression, not about the sentence.

### 8. Smaller points

- **v4 §3:** "Traditional hospitality is a straight line: host and guest, where the one who receives you is the one you can address." Qualified: in Pitt-Rivers's traditional case the guest may honour the host and may not press a claim on him (pp. 513–515).
- **v4 §4:** "A welcome is triggered by one thing only: someone has arrived." Qualified: the beggar who presses his claim "falls back into the role of hostile stranger" (Pitt-Rivers, p. 509); arrival opens the question, and the host's acceptance and the guest's conduct settle it.
- **Outline §4 (v4 §4):** "Discretion acts on the single case; authority acts on the rule. A guest can meet someone with the first power and never reach anyone with the second." Supported as a distinction by Hales and Klidas's "choice" against "voice" (abstract; they do not make the paper's link). Qualified by their finding: staff had little of either.
- **Outline §4 (v4 §4):** "Authority drifts to whoever configures the rules (Gursoy 2026: 160)." Supported for vendors: providers reserve "rights to dictate terms of use and change, withdraw, or cancel products and services at will" (Cobbe et al., p. 10).
- **Outline §5 (v4 §5):** "A system that scores a profile decides how the guest will be received". Supported in kind: Recital 71 treats profiling of "personal preferences or interests, reliability or behaviour" as the paradigm case once it has significant effect.
- **Outline §5:** "Pricing ... fails on predictability and accountability." Qualified in legal weight: differential pricing "could also have a significant effect if, for example, prohibitively high prices effectively bar someone from certain goods or services" (WP251, p. 22).
- **Outline §7, Table 3, stage 4:** "Create a forum obliged to answer challenges, with authority to act." Supported: WP251 p. 27; Cobbe et al.'s definition of accountability as an actor giving accounts to a forum (p. 2).
- **Outline §9:** "Hotels against platforms." Supported as a real boundary: hosts refuse the hotel role ("I am not a butler though nor am I a receptionist in a hotel", Kaniadakis and Farmaki, p. 14). "The EU against other jurisdictions": the legal sources here are EU (GDPR, WP251) and one US circuit (*Crinkley*); neither travels. "Luxury against budget": the two frontline-authority sources that name a segment are both upscale (Hales and Klidas, five-star; Golubovskaya et al., "upscale hotels", p. 1300).
- **Pitch:** "industry practice has repeatedly reduced hospitality to transaction management (Golubovskaya et al. 2017: 1296, 1299–1300 ...)". The pages support displacement by service terminology in one cross-sectional study; "repeatedly" and "transaction management" are not the source's.

### Debts before any of this enters the draft

- Hewagama et al. and Hales and Klidas were read at abstract depth only. Item 2 leans on both.
- King (1995) is known only through Golubovskaya et al., p. 1286.
- Lugosi (2009) was read in the accepted manuscript; wording and pages are unchecked against the version of record.
- Baum and Laux was read in arXiv v2; the LNCS chapter is unread, and Crossref gives a 2027 print date.
- Cobbe et al. page numbers in the draft should be the proceedings pages (arXiv page + 1185, per VERIFY_H_v2; I did not re-check the version of record).
