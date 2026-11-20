# Adjudication of run 2026-11

*Written by Claude (Fable 5.2), adjudicator for the lead, 2026-11-19. Working notes for the author, not paper prose;
none of the text is his. Inputs: `CONFLICTS_FOR_LEAD.md` (54 conflicts, agent SB), `EVIDENCE_MAP.md`,
`COUNTER_EVIDENCE.md`, `GAP_REPORT.md` Parts A and B, `STRUCTURE.md`, `ARGUMENT_AND_OUTLINE.md` (v3), the concept
ledger, the 65 run cards, the library cards named below, and the four verifier logs and six Fable-read logs in
`verify/`. For each ruling, "reopened" means I opened the local source myself and matched the words; "on" a
card, verifier or Fable row means I rely on another's match without reopening. Every source is a file on local disk
(under `~/iit-playground/berthon_ethics_local/` or in the repo) or one of the four Crossref records listed at the
end; nothing here comes from memory.*

*A conflict sets a statement in one file (statement 1) against a challenge from another (statement 2).
**Upheld**: the challenge stands. **Overruled**: the challenge fails, or the two statements do not conflict.
**Narrowed**: statement 1 survives in a narrower form, given under Effect. **Left for the author**: the matter
belongs to the thesis or the structure; the row gives the evidence on each side and decides nothing.*

*`STRUCTURE.md` and `ARGUMENT_AND_OUTLINE.md` are Claude's drafting. Where a row touches the author's own wording
(his definition, his 04 table), it flags the fact with its source and changes nothing. I ran no git command, wrote
nothing for the paper and changed no card.*

Totals: 54 conflicts ruled. Upheld 29; Narrowed 15; Overruled 6; Left for the author 4.

## Rates

Counted row by row from `VERIFY_V-*.md` and `FABLE_READ_*.md` (65 verifier rows, 65 Fable rows, 65 cards; the card
frontmatter agrees with the Fable column on every card).

| Verifier (facets) | Cards | Verifier's verdicts: VERIFIED / FIX / OVERSTATED / REJECT | Fable read set: true / corrected / pending | VERIFIED, then corrected | Fable read corrected something the row had not flagged | Fable read found the row itself wrong |
|---|---|---|---|---|---|---|
| V-A-1 (A1, A3, A5) | 21 | 11 / 7 / 3 / 0 | 2 / 16 / 3 | 9 of 11 (82%) | 17 of 21 (81%) | 1 of 21 (5%) |
| V-A-2 (A2, A4) | 17 | 8 / 7 / 2 / 0 | 3 / 14 / 0 | 5 of 8 (63%) | 13 of 17 (76%) | 1 of 17 (6%) |
| V-B-1 (B1, B2, B5) | 15 | 7 / 3 / 5 / 0 (one of the five is FIX + OVERSTATED) | 0 / 15 / 0 | 7 of 7 (100%) | 15 of 15 (100%) | 4 of 15 (27%) |
| V-B-2 (B3, B4) | 12 | 5 / 5 / 2 / 0 | 0 / 12 / 0 | 5 of 5 (100%) | 12 of 12 (100%) | 5 of 12 (42%) |
| All | 65 | 31 / 22 / 12 / 0 | 5 / 57 / 3 | 26 of 31 (84%) | 57 of 65 (88%) | 11 of 65 (17%) |

How I counted the last three columns.

- **VERIFIED, then corrected** is a plain count: the verifier's verdict cell begins VERIFIED and the Fable read set
  `corrected`. The five that stayed `true`: andriano2019causal, bulger2018promises (V-A-1); lyons2014power,
  spencer1973signature, uscongress1982voting (V-A-2).
- **Corrected something the row had not flagged**: the Fable row's "what I changed" cell lists at least one
  correction to a statement in the card that the verifier's row had neither made nor flagged for the lead. Added
  facts and the verifier's own notes, once applied, do not count. The eight cards outside this column:
  andriano2019causal, bulger2018promises, rasmussen2010attended, yilmaz2011learning (V-A-1); lyons2014power,
  spencer1973signature, uscongress1982voting, yannakakis2021interpreters (V-A-2). The count is by my reading of the
  two cells for each card; a stricter or looser reader would move a few of the 57.
- **Found the row itself wrong**: the Fable row names a statement in the verifier's row as wrong, declines wording
  the verifier proposed, or reverses an item the row had expressly checked and passed. V-A-1: balaj2021parental
  ("they make no causal claim" declined; the article speaks of a "protective effect"). V-A-2: hewitt2013dawn
  ("rejected the radical terminology" stands at para. 3, where the row said the review lacks it). V-B-1:
  acp2026agentic (a Summary sentence the row said "holds" was replaced), imda2026agentic (the p. 47 paraphrase
  the row passed), microsoft2026services (eight of nine §14(s)(ix) restrictions name a person, not nine),
  visa2025trusted (line 98, not 89). V-B-2:
  bayamlioglu2021contest ("individually enforceable" not taken), creel2022leviathan (pages 35 and 39, not 36 and
  40), edpb2023deceptive (the scope note the row said "holds" was too absolute), hoeksema2025republican (the row
  repeated the card's wrong negative on the exit objection; I reopened p. 131 n. 70 and the Fable read is right),
  sparrow2026slaves (the customers sentence does not hold for the pages read; the passage is on p. 6).
- Outside that column, six verifier rows passed the Summary in general terms ("Summary ... fair") and the Fable read
  then corrected it: davis1949davis, guinn1915guinn, louisiana1965louisiana, radin2013boilerplate,
  saunders1971anglia (V-A-2); tang2025darkgui (V-B-2).

What the rates mean. No verifier passed a fabricated or misworded quotation: by the verifiers' own tallies they
checked 430 quotations in Key facts (117, 104, 135, 74) and found none wrong in wording, and the Fable sittings and
my reopenings below found none either. The verifiers caught four quotations cut so as to change or hide meaning
(guinn p. 365, saunders p. 7, yorta para 143, susser p. 7). The Fable read caught three more that a verifier had
passed (guinn p. 357, the dropped proviso; hoeksema p. 130, "If all goes well"; narayanan Part II, "In most
scenarios") and one Summary quotation with a word dropped (vieira p. 28). The errors the verifiers missed sat where
they looked least: in Summaries, Critical notes and bearing lines, and on pages the drafter had not read. A
`VERIFIED` verdict in this run certifies the record and the quotations at the cited pages. It does not certify the
Summary, the bearing line or a negative ("the source does not address X"). One reason for the higher Phase B
figures shows in the logs: the Phase B Fable readers read seven sources whole where the drafter had read a part
(burrell, susser, tang, wachter, narayanan, olghamm, google2025secure_agents), and the verifiers had checked the
drafter's pages.

Conflicts below that exist only because the Fable read went past the verifier's row: CONF-53 (graff2022new,
V-A-1), CONF-25 (fujiwara2015voting, V-A-1), CONF-18 (uscongress1975voting, V-A-2), CONF-30 and CONF-54
(imda2026agentic, V-B-1), CONF-13 and CONF-33 (hoeksema2025republican, V-B-2), CONF-22 and CONF-52
(tang2025darkgui, V-B-2), CONF-2 (wachter2017right, V-B-2).

Where my reopening goes beyond the Fable read: the Copilot terms carry an express indemnity that the library card
and Fable V-B-1 do not record (ruling 5); *L'Estrange* itself names *non est factum* (ruling 24); the Newland
treaty counts are of differently worded sets (CONF-24); the Jakkal post uses "an intrusion" once, generically
(CONF-34); OLG Hamm para 104 does not speak of a duty (ruling 4); Kousser p. 59 does carry the spokesmen's
prediction (CONF-20); and Hoeksema himself doubts McCammon's criterion (ruling 11).

Three Phase A cards stay `pending` and nothing below relies on them: levine1982functional, sandiford1994nicaraguan,
yilmaz2011learning (no saved source). All other run cards read `true` (5) or `corrected` (57).

## Rulings that change the argument

Nadella's post is cited by paragraph (P1–P21) from the local text; quotations are kept to a sentence or less.

| # | Item | Ruling | Evidence | Effect |
|---|---|---|---|---|
| 1 | **CONF-1: AI Act arts. 26(11), 85 and 86 as present rights** (STRUCTURE §4.2; A8) | Upheld | Reopened Reg. (EU) 2026/1744 (OJ L, 24.7.2026), art. 1 point (40)(b), replacing art. 113, third paragraph, point (c): "Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III; and (ii) 2 August 2028 ..."; recital 40 gives the reason. Reopened Reg. (EU) 2024/1689: art. 26 stands in Chapter III, Section 3; art. 26(11) binds "deployers of high-risk AI systems referred to in Annex III"; arts. 85–86 stand in Chapter IX, Section 4, which the Omnibus does not touch (text search: no amendment to arts. 26, 85 or 86); art. 85 complaints "shall be taken into account for the purpose of conducting market surveillance activities"; art. 86(1) attaches to "a high-risk AI system listed in Annex III"; Annex III point 5 lists public benefits, creditworthiness, life and health insurance pricing and emergency triage. SB cites the recital; the operative text is point (40)(b). Art. 26(11) is in `pages_read` of the course-folder card (bec/eu2024aiact), not of bep's | On 19 Nov 2026 art. 26(11) does not apply; it applies from 2 Dec 2027. Art. 85 applies and gives a complaint that feeds market surveillance, not a personal remedy. Art. 86 sits in a chapter whose date did not move, but its trigger is an Annex III high-risk system and the rule that classifies one (art. 6(2)) applies from 2 Dec 2027; no text read says how art. 86 works in between, and B5's "affected in practice" is B5's reading. A refund agent is outside Annex III on either date. §4.2 and A8 must date the three provisions or drop 26(11) and 86 from the present rights. The correction cuts for the paper: the law gives less today than A8 credits. Limit: I read the two OJ texts on disk and did not search for an act later than 24 July 2026; B5 §3 states the law as of 18 Nov 2026 and names none |
| 2 | **CONF-2: GDPR art. 22 as "narrow, after-the-fact rights"** (STRUCTURE §4.2) | Narrowed | Reopened GDPR art. 22(1) ("the right not to be subject to a decision based solely on automated processing"); art. 22(3) ("at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision"); art. 13(1)–(2) ("at the time when personal data are obtained"); arts. 13(2)(f), 14(2)(g), 15(1)(h) ("meaningful information about the logic involved"). Reopened *SCHUFA* para 52: art. 22(1) "lays down a prohibition in principle, the infringement of which does not need to be invoked individually". Reopened Wachter, Mittelstadt and Floridi, manuscript p. 15: "only an ex ante explanation of system functionality is explicitly required by Articles 13(2)f and 14(2)g. These notification duties precede decision-making." | "After the fact" fits art. 22(3) alone. The information duties come before the decision, access is on request, and art. 22(1) is a prohibition in principle, which ARGUMENT's own D02 row already uses. §4.2 should state three layers: notice before, a prohibition with a contract exception, safeguards after. The narrowed safeguards claim ("no independent, binding check at the point of decision") is untouched. Wachter's page numbers are manuscript pages (the journal runs 76–99), and the paper is a 2017 forecast to set against *SCHUFA* and *Dun & Bradstreet* (on Fable V-B-2) |
| 3 | **CONF-40: "necessary, not sufficient: Berthon, Pitt and Campbell 2019, p. 457"** (STRUCTURE §4.2) | Upheld | Reopened p. 457, left column, on Apple's and Google's screen-time tools: "Indeed, empirical research suggests that information is necessary, but not sufficient to change behavior (e.g., Worsley 2002)." The passage calls the tools "a minimum first step" and concludes "that public policy solutions are required to address digital addiction". Text search of the article: no "literacy" | p. 457 carries "information alone does not change behaviour", reported from Worsley 2002, in a passage on digital addiction. It says nothing on disclosure as a legal remedy or on AI-literacy training, and no card in either phase tests "necessary". The cite can stay for the narrow point. The sentence in STRUCTURE §4.2 is Claude's, not the author's. How the paper speaks of Berthon's scheme is call 6 |
| 4 | **CONF-7: "none of it reaches a refund"** (A8) | Narrowed | Reopened *Moffatt v. Air Canada*, 2024 BCCRT 149: para 1 ("This dispute is about a refund for a bereavement fare"); para 27 (the chatbot "is still just a part of Air Canada's website"); para 28 (the airline "does not explain why customers should have to double-check information found in one part of its website on another part of its website"); para 44 ($650.88 in damages, $812.02 in all). Reopened OLG Hamm, 12 May 2026, 4 UKl 3/25: para 73 (a chatbot's conduct counts as "geschäftliche Handlungen seines Betreibers"); para 104 (no rule of experience that consumers know its answers "stets eines Faktenchecks bedürfen"; most trust a machine's answer). On ADJUDICATION_R ruling 1: a refund decision falls under GDPR art. 22(2)(a) with 22(3)'s safeguards. On B5 §3: the California and Colorado rules reach "significant" or "consequential" decisions from 2027 (cards pending) | A8's sentence holds for the AI Act and the US rules. It fails as a statement about the law. Negligent misrepresentation reached a chatbot's statement about claiming a refund, in a small-claims tribunal, on the customer's own suit, after the loss; and whether GDPR art. 22 reaches a refused refund turns on "similarly significantly affects", which no card settles. Both decisions concern what a chatbot said. No decision read concerns what an agent decided or did (B5 §3). Para 104 denies that consumers are known to distrust chatbot answers; it speaks of no duty, so the map's gloss "no duty to fact-check" (L-3, CE-4.4) should follow the card's wording. The Hamm case is an association's action over a clinic's chatbot and names no misled consumer (on Fable V-B-1) |
| 5 | **CONF-4: the loss row, "Terms that make the user 'solely responsible'"** (STRUCTURE §4.4, row 5) | Narrowed | Reopened Copilot Terms of Use (effective 18 Aug 2026), "Important disclosures & warnings": "When you request that Copilot take Actions on your behalf, you are solely responsible for those Actions and any results or consequences"; same section: "You agree to indemnify us and hold us harmless ... from and against any claims, losses, and expenses (including attorneys' fees) arising from or relating to your use of Copilot". Reopened Microsoft Services Agreement (published 30 July 2026, effective 30 Sept 2026): §14(s)(viii), "You are solely responsible for responding to any third-party claims regarding Your use of the AI services"; §16, the Terms "are solely for your and our benefit; they aren't for the benefit of any other person". Reopened P3: "A model provider's assurances do not relieve us of that responsibility." | (a) Upheld: "the user" in these terms is the account holder, the agent's principal. (b) Upheld for §14(s)(viii), a duty to respond and no indemnity. Overruled for Microsoft's consumer terms as a whole: the Copilot terms carry an express indemnity in Microsoft's favour. The library card (bep/microsoft2026copilot; same file by sha256) omits that sentence, and Fable V-B-1's "neither an indemnity in terms" and CE-4.5's heading are true of the two "solely responsible" clauses only. (c) Upheld: P3 keeps responsibility with the deployer and belongs on no loss row; STRUCTURE's row 5 does not cite it. The row should say whose terms and which user: the principal is "solely responsible" and indemnifies Microsoft; the person acted on is not mentioned, and §16 gives her nothing under the terms. Her loss rests on silence, as ARGUMENT's ruling-10 line has it |
| 6 | **CONF-43: "All four vendors put responsibility for actions on the user"** (`COVERAGE_PREMISES.md`, round 1, A4) | Narrowed | Reopened Smith and Nowbar, 7 Sept 2023: para 3 ("we will defend the customer and pay the amount of any adverse judgments or settlements"); para 5 ("we should make this our problem rather than our customers' problem"); para 8 ("specifically for paid versions of Microsoft commercial Copilot services and Bing Chat Enterprise"). The round-1 finding itself: on facet N1, not reopened | The round-1 sentence stands for actions under the consumer terms. Microsoft carries one loss for one class: copyright claims over Copilot output against paying commercial customers who kept the filters on. Beside ruling 5, the same firm defends the paying customer and takes an indemnity from the consumer; neither document mentions the person acted on. Where the commitment is written into contract is not established (on Fable V-B-1) |
| 7 | **CONF-3: row 1 pairs P3, P5, P11, P17 with "Monopoly; custody by an interested party"** (STRUCTURE §4.4) | Narrowed | Reopened P5 ("we need to separate the supply of intelligence from the authority over it"); P14 ("No one model should become the sole dependency for an important outcome"); P17 ("Orgs should be able to independently determine what a model can access"); P11 (controls "must sit outside the model"). Reopened Positive Sum (15 Nov 2025), para 10: every firm should "have control of their own destiny and sovereignty" | The essay argues against a single supplier, and "monopoly" describes no move in it. "Custody by an interested party" does describe P17: the deploying organisation holds the controls and the envelope. The pairing holds for the deployer's custody toward outsiders and for nothing wider. Whether the row keeps the label "Monopoly" is call 4 |
| 8 | **CONF-5: record row, "evidence for the deployer (P15)"** (STRUCTURE §4.4, row 2; A4) | Narrowed | Reopened P15: "Every meaningful model action must leave tamper-proof human readable evidence." It names no reader. Reopened Microsoft Learn, "Audit logs for Copilot and AI applications": "If your organization enables auditing ..."; "Access Copilot audit logs by using the Microsoft Purview portal" | "For the deployer" is the products' allocation, not P15's words. Cite P15 for the demand and the Purview page for the reader: the tenant organisation, through its own portal. The page read names no access for anyone outside the tenant |
| 9 | **CONF-44 and CONF-51: stop row, "Brake held by 'an authorized person' (P19)"; "No brake"** (STRUCTURE §4.4, row 3) | Narrowed (44); Overruled (51) | Reopened P19: "An authorized person should always be able to pause or shut down a model mid-task." It does not say who authorises. Reopened Roadmap item 570434 (archive capture; published 1 Sep 2026; status "In development"; "GA date: September CY2026"): "Approval requests appear inline in the channel where the agent is deployed, including Microsoft Teams and Microsoft 365 Copilot" | 44: the sentence leaves the holder open; "the deployer" comes from P17 and the products. 51: the item names two workplace channels and no customer-facing one. The card's "whoever is chatting with the agent" is its inference, and SB's step to a customer is a second inference the source does not carry. "No brake" should read "no brake she is shown to hold". The row still has to argue gate versus brake (ADJUDICATION_R ruling 6) |
| 10 | **CONF-54 and CONF-30: envelope row, "No sight of the envelope"; IMDA as "voluntary"** | Narrowed (54); Upheld (30) | Reopened IMDA, *Model AI Governance Framework for Agentic AI*, cover: "Version 1.5 \| Published 20 May 2026 (Updated 5 June 2026)". p. 46, 2.4.2: users who deal with agents "that act on behalf of the organisation e.g. customer service or sales agents". p. 47: "Inform the users on the range of actions and decisions that the agent is authorised to perform and make"; "Provide users with the respective human contact points ... whom the users can alert if the agents malfunction or if they are dissatisfied with a decision"; "Where appropriate, allow users to set their own approval thresholds and boundaries". p. 28: users should get "sufficient information to hold the organisation accountable". p. 46: "Organisations should consider". Text search of the 53 pages: no "voluntar" | 54: the row stands as a statement about the essay and the Microsoft documents read (B5 §4 found none that gives the person sight of the envelope). A wider "no design gives her this" fails: a public body asks deployers to tell the customer the agent's range of action and whom to reach. 30: "voluntary" is not in the text; use the framework's own "should consider", or cite IMDA's page for its status (not captured). The framework names no remedy (text search on Fable V-B-1). Its use in the paper is call 9 |
| 11 | **CONF-13, CONF-33, CONF-32, CONF-14, CONF-12: domination and the one-off dealing** (A7(ii); ARGUMENT call 2; B4 facet; ledger N04, N05, L04) | Upheld (33, 32); Overruled (14); Left for the author (13, 12) | Reopened Gädeke 2020: p. 199, "Domination, I maintain, is a structurally constituted form of power"; p. 200, "Purely interactional forms of power, which are based on an opportunistic capacity to interfere, however, are not instances of domination", and the mugger dominates only if his power "is structurally enabled and thus serves as the basis of a persisting status asymmetry" (card still `pending`). Reopened Hoeksema 2025: p. 28, "I remain agnostic towards this question", and "I agree with Gädeke that excluding episodic power from the concept of domination would bring more conceptual clarity"; p. 30, the candy clerk, "There is no impositional power in play", because "reasonable alternatives likely exist", and "it is doubtful whether McCammon succeeds"; p. 31, micro-domination, instances "of little consequence by themselves" that "amount to a significant level of domination in aggregate"; p. 33, "calling this impositional power pushes the example too far"; p. 130, on Pettit and Taylor, "If all goes well, they will never be subject to arbitrary power by virtue of competition and exit mechanisms"; p. 131 n. 70, "There are two responses to this challenge." Reopened his 2023 article as reprinted (ch. 2, p. 67): "republicans cannot rely on the idea of exit options or of rationally consenting citizens". Reopened Creel and Hellman 2022, p. 34: the charge "has no obvious moral force"; an inefficient screen "does not wrong others" unless the firm "made commitments" or "invited reliance". Reopened Burrell 2024: no "Pettit" and no "republican" anywhere in the text; "Drawing especially from philosopher Iris Marion Young's work" (§1). Sparrow 2026, p. 6: the VPN and plane-ticket sentence stands there (found by search; the reading is on Fable V-B-2) | 33: B4's "reports the exit objection and does not settle it" and "No source read gives a test for a one-off dealing" are overruled; Hoeksema gives two answers and reports McCammon's test on a one-off sale. 32: Burrell supports "automated decision-making as domination" on Young's account, in public-sector cases; she carries no republican test and no customer dealing. 14: no conflict; in 2023 and in 2025 Hoeksema reports the Pettit–Taylor case for exit and argues against relying on it. Ledger N05's "exit and consent fail" is stronger than his "cannot rely on". 13 and 12 are calls 1 and 2. What the sources fix for call 1: Gädeke's test needs a persisting status asymmetry; the clerk example fails for want of dependence, the condition the paper's "no alternative route" must supply; Creel and Hellman's "arbitrary" means ill-fitted to the firm's own ends, not uncontrolled, so they do not answer the republican claim; Hoeksema's own route for small harms is aggregation; McCammon, O'Shea and Lazar's micro-domination paper reach the run through him alone (on Fable V-B-2) |
| 12 | **CONF-22 and CONF-52: Tang et al. 2025** | Upheld (both) | Reopened Table 3 (p. 12) and tallied it: avoidance under oversight is higher for 10 of 16 pattern types, equal at 100.0% for 4 (Adding Steps, Choice Overload, Urgency, Shaming) and lower for 2 (Social Proof 100.0 → 90.9; Forced Registration 40.0 → 25.0). p. 13: "in 14 of 16 tasks, participants were less likely to fall for dark patterns when supervising the agent (Table 3)". p. 16: responsibility "defaults to end users least able to manage the risk". p. 18: "AI safety literacy education should therefore extend beyond identifying manipulative design" | Cite the table: no worse in 14 of 16, better in 10. Sample and test limits on Fable V-B-2 (22 participants, no significance test). The paper both supports the responsibilization point and prescribes a user literacy; its use is call 12. The person at risk is the agent's own user on the authors' test sites, not a person a firm's agent acts on (on Fable V-B-2). An arXiv v1 preprint |
| 13 | **CONF-41: "The intermediary adapts to the person as the page never did (Yeung 2016)"** (STRUCTURE §5) | Narrowed | Reopened Yeung, accepted manuscript. Abstract: the paper "focuses on algorithmic decision-guidance techniques"; such nudges are "networked, continuously updated, dynamic and pervasive". AM p. 4: automated decision-making processes "constitute a form of action-forcing (or coercive) design". AM p. 5: "this paper focuses on Big Data driven decision guidance techniques". AM p. 6: "a highly personalised choice environment". Dates on the card's Crossref check: online 22 May 2016; issue 20(1), 118–136, 2 Jan 2017 | Yeung carries adaptivity for guidance, the hypernudge, and sets deciding systems aside. That an agent which decides also adapts to the person, and so adds to her burden, is the paper's inference; it needs its own source or to be stated as inference. Year: 2016 online, 2017 in the issue. The index says 2017; make the text and the reference agree |
| 14 | **CONF-15: disanalogy "intent (the 1901 tests) versus position (agents)"** (STRUCTURE §5; A6) | Narrowed | Reopened *Davis v. Schnell*, 81 F. Supp. at 878: the board "is given the arbitrary power to accept or reject any prospective elector that may apply"; "Such arbitrary power amounts to a denial of equal protection of the law within the meaning of the Fourteenth Amendment". At 876: "The States have a right to prescribe a literacy test for electors" (OCR mark in the file). Reopened USCCR 1961, Finding 12, p. 138: "Whether or not they are clearly racially discriminatory, such practices are arbitrary". The separate Fifteenth Amendment holding (pp. 880–881): on Fable V-A-2-1 | The record condemned the test on position alone as well as on intent, so the disanalogy is weaker than §5 states and can be shown non-critical from these two sources. They also fix the property the gate pairing must share: power to accept or reject with no standard, record or review. The courts kept literacy as a qualification (ADJUDICATION_R ruling 6 stands) |
| 15 | **CONF-45: "the 1901 convention on registrars' discretion"** (A3) | Narrowed | Reopened *Official Proceedings*, vol. 1, p. 11, Knox's opening address of 22 May 1901, on Mississippi's plan: "the objection has been urged with force that it perpetuates the very form of abuse which we are seeking to escape. Elections by managers or registrars is not what we want". The card's pages read: pp. 6–17 and p. 129 | The objection is the convention president's report, in his opening address, of an objection to another state's clause. It is no act of the convention, and what the convention adopted (§181) is on no page read. A3 should name Knox and the page. ADJUDICATION_R ruling 6's "the 1901 convention's own objection" takes the same narrowing |
| 16 | **CONF-18: the 1975 Act as a "permanent ban on tests or devices"** (A2 facet §3) | Upheld | Reopened 89 Stat. 400: long title, "to make permanent the ban against certain prerequisites to voting"; s. 102 amends s. 201(a) of the 1965 Act by striking "Prior to August 6, 1975, no" and inserting "No". The print does not reprint s. 201 | The page supports "Congress made permanent 'the ban against certain prerequisites to voting'". That this ban is the test-or-device ban is on no page read. §3.2 and D02 cannot say Congress banned literacy tests for good until s. 201 as it stood in 1975 is read |
| 17 | **CONF-42: the oversold promise as "Jomtien and Dakar"** (STRUCTURE §3.6) | Upheld | Reopened the Jomtien Framework for Action, para 8 (OCR text): "Countries may wish to set their own" targets "in terms of the following proposed dimensions", among them "Reduction of the adult illiteracy rate ... to, say, one-half its 1990 level by the year 2000". Reopened the Dakar Framework, para 7: "We hereby collectively commit ourselves to the attainment of the following goals", with "(iv) achieving a 50 per cent improvement in levels of adult literacy by 2015" | The commitment is Dakar's. Jomtien proposed a dimension countries "may wish" to adopt. §3.6 should rest the broken promise on Dakar and cite Jomtien as the proposal |
| 18 | **CONF-10: "Writing demanded a new competence of everyone it reached"** (STRUCTURE §1.1) | Narrowed | Reopened the author's draft 04, line 40: "Distinguishes between literacy as an optional, rewarding capability and literacy as a mandatory institutional gate." Ledger H17. On run cards: oral voting in Peru (ragas p. 131); an electorate "85 per cent illiterate" (shani p. 12, no footnote) | The sentence is Claude's, in STRUCTURE §1.1. It says more than the author's own distinction and the record allow. Restate §1.1 in §2.1's terms: a competence demanded at the gates institutions built. The present question then becomes where agents are made gates |
| 19 | **CONF-6: AP2 "shows the alternative can be built"** (A5) | Narrowed | Reopened the AP2 specification v0.2, "Modes": in the autonomous case trust rests on "open Mandates that are signed by the User"; "Constraints in these Mandates allow the verifier to verify that the Checkout and Payment match the User's intent. Only constraints relevant to the closed Mandates are shared with the verifier." The text has no "Intent Mandate" and no "binds both". Reopened Visa's Trusted Agent Protocol README: "a standardized, cryptographic method for an AI agent to prove its identity and associated authorization directly to merchants"; release (14 Oct 2025): "these initial specifications apply to the Visa network in this phase" | (a) Upheld: AP2 is not the only published design. Visa's is a second, a specification with sample code and no use shown (on Fable V-B-1). (b) `COVERAGE_PREMISES` v2's "partial counter-instance" stands; round 1's "Intent Mandate, which binds both sides" is not the v0.2 text. Both designs let a merchant check an agent, and in payments the party acted on is the merchant. D03's precedent therefore runs toward the merchant: call 11 |
| 20 | **CONF-16 and CONF-17: the correction's two forms; D04's precedents** (A2; duty table) | Narrowed (16); Upheld (17) | Reopened the Election Commission's report, ch. IX (p. 80 on the card): a law "requiring the polling officers to help illiterate voters ... would have meant the virtual abandonment of the vitally important principle of the secret ballot"; the Commission then gave each candidate a box with a mark. Reopened Pub. L. 97-205, s. 5 (96 Stat. 134–135), adding s. 208 "Effective January 1, 1984": a voter unable to read or write "may be given assistance by a person of the voter's choice, other than the voter's employer or agent of that employer or officer or agent of the voter's union" | 16: A2 stands ("the artifact or a party owed to the weaker side"). The helper the Commission refused was the state's own officer, and it chose the artifact. The two forms are not interchangeable where secrecy or capture is at stake: D04's reader must be the person's own choice and independent of the deployer. 17: s. 208 is a working precedent the D04 row omits. It permits a helper and obliges no one to supply one. Adding it is call 10 |
| 21 | **CONF-19: candidate 2 (reading allowed, writing withheld) "UNSUPPORTED"** (A3 facet §4) | Upheld | Reopened *Statutes at Large of South Carolina*, vol. 7, Act No. 670 (1740), s. XLV (p. 413 on the card): whoever "shall hereafter teach, or cause any slave or slaves to be taught, to write, or shall use or employ any slave as a scribe in any manner of writing whatsoever ... shall ... forfeit the sum of one hundred pounds current money". The section does not mention reading | A3 did not consult the library card. The statute supports "teaching to write penalised; reading not mentioned in s. XLV". It does not show reading permitted: I read one section and the card read four pages of the Act (pp. 397, 413–414, 417). GA proposes folding the case into §3.3; that belongs to call 5 |
| 22 | **CONF-9: "'Microsoft's agent-policy specification': UNSUPPORTED"** (B1 facet §3) | Upheld | Reopened the saved post, "Introducing Agent Control Specification: Portable runtime governance for AI Agents" (Command Line, 2 June 2026): "There is no standard mechanism by which a security or compliance team can define, enforce, and audit policy across agents." `CARD_INDEX.md` lists bep/elmergawi2026introducing (full, `true`) | The card exists and B1 missed it. Two flags on STRUCTURE §4.3. The document's name is the Agent Control Specification. And the card records an announcement that "reports no deployment or evaluation", so "already runs in" is not shown for the specification |
| 23 | **CONF-53: who contests Graff** | Upheld | On Fable V-A-1-1 and the card as it stands (reopened the card, not the article): Houston 1982 and Mitch 2003 "were blocked and unread" | The run cannot say who contests Graff. The first draft of the card described two unread works' positions, which is what the first guard forbids; the Fable read removed it. CE-1.1 (the "-acy" label as the literacy myth's own move) is answered by no card, and Graff's target is "X literacy" labels, so its use against "algorithmacy" is inference (on Fable) |
| 24 | **CONF-38: the defences to the signature rule** (ADJUDICATION_R ruling 8) | Upheld | Reopened *L'Estrange v. Graucob* [1934] 2 K.B. at 403 (Scrutton L.J.): "in the absence of fraud, or, I will add, misrepresentation, the party signing it is bound, and it is wholly immaterial whether he has read the document or not" (the OCR prints "T will add"); at 406 (Maugham L.J.): a document "signed in circumstances which made it not her act. That is known as the case of Non est factum." Reopened Spencer's abstract, one sentence: "one of three defences: (a) fraud, (b) misrepresentation, or (c) non est factum" | Three defences. Ruling 8 of the R round quoted Scrutton L.J. alone; *L'Estrange* itself keeps the third in view. §3.4 should state the presumption with its three exits; §5 already lists *non est factum* among the buffers. Spencer's own argument is unread (abstract card) |
| 25 | **CONF-46: §4.1's "the monopoly (compute and model weights)"** | Left for the author | Reopened the author's draft 04, line 109: "Classical monopolies restricted physical printing presses; contemporary monopolies restricted infrastructure and model weights." Ledger E07: "not established as a Stationers-type grant; left an open row" (CMA 2023 and Posada et al. cards, not reopened). No run card on concentration of compute or weights (Part B §B2) | Call 4. The wording is the author's and stays as he wrote it unless he changes it |
| 26 | **CONF-11: which wording of the definition** | Left for the author | Reopened draft 04, line 5, which STRUCTURE §1.1 quotes exactly; reopened draft 05, line 31: "the relational competence demanded when human agents must coordinate with one another through an automated third party that processes, evaluates, and enforces outcomes binding on both sides". The 08 wording ("reads all of them"): on ledger K01 | Call 3. Both wordings are the author's; STRUCTURE quotes the earlier one |

## Lesser rulings

Records, numbers and process. None changes a premise; several change what a sentence may cite.

| Conflict | Ruling | Evidence | Effect |
|---|---|---|---|
| CONF-8: A8 cites Arbel and Becher "(abstract)" | Upheld | Reopened Arbel and Becher 2022, 90 Geo. Wash. L. Rev. 83 (pages confirmed by running heads): p. 121, "adversarial attacks by interested firms"; pp. 135–136, smart readers "do not necessarily portend the end of pro-consumer legal measures"; pp. 138–139, "standard doctrines would allocate the entirety of the risk of smart reader error to the consumer"; p. 141, "regressive cross-subsidies that exacerbate inequalities" | "(abstract)" is now true of the 2025 chapter alone (bep/arbel2025how, pending). The 2022 article, read in part (about 18 of 64 pages, on Fable V-B-1), supports the reply "who runs the reader" |
| CONF-20: Kousser p. 59 and the predicted humiliation | Narrowed | Reopened p. 59: "As spokesmen for the lower strata of whites had predicted, poor, illiterate men were often too humiliated to register under these provisions"; the Mississippi evidence is Frank Johnston's 1902 count of "about a dozen whites" | The page carries the prediction, so A3 was nearer the source than the card's short bullet. "Mississippi" for the spokesmen is A3's addition; Kousser does not place them |
| CONF-31: X07 and "the empirical case against disclosure (E08)" | Overruled | Reopened `../consolidation/CONFLICTS.md`, X07: "The empirical case against disclosure (E08) and the autonomy defence (O07) sit on either side." | No conflict. E08 rests on existing library cards (Bakos; Ben-Shahar; McDonald; Obar; not reopened). B3 adds no measurement of disclosure, as it says |
| CONF-34: logs widened "after CISA pressure" | Upheld | Reopened Jakkal, 19 July 2023, para 7: "Today's news comes as a result of our close partnership with CISA, which has called for the industry to take action" | `NADELLA_MOVES.md` row 8 should take the post's wording. The post uses "an intrusion" once, generically, and names none; the Fable row's "never mentions an intrusion" should read "names no intrusion". The page was modified in June 2025 (on Fable V-B-1) |
| CONF-29: whose DOI is 10.1017/9781009279079.019 | Upheld | Crossref, fetched 19 Nov 2026: Arbel and Becher, "How Smart Are Smart Readers? LLMs and the Future of the No-Reading Problem", book chapter, pp. 336–374, issued 31 Mar 2025 | Scout B's "Elvy and Kim" is wrong; bep/arbel2025how has the record right |
| CONF-36: Lund and Teel's names | Upheld | Reopened the saved text's title block: "Brady D. Lund and Zoë Abbie Teel", University of North Texas | The scout row is wrong; the card is right |
| CONF-39: stale notes in `references.bib` | Upheld | Reopened `../literature/references.bib`: guinn1915guinn, "Read in part: pp. 357 and 366"; saunders1971anglia, "Not accessible ... second-hand" | Both notes are out of date. The run cards rest on the whole *Guinn* opinion and on an Internet Archive capture of BAILII for *Saunders* (on Fable V-A-2-1). Cite *Saunders* by its AC page, which the capture does not give |
| CONF-23: Kleinberg et al., 24.8% and 42.0% or 24.7% and 41.8% | Upheld | Reopened NBER WP 23180: p. 2, "up to 24.8%" and "42.0%"; p. 6, "24.7% fewer crimes" and "41.8% fewer people" | Cite p. 6's figures as the working paper's; the abstract's "up to" marks a maximum. "Crime" there is failure to appear, and the QJE text is unread (on Fable V-B-1) |
| CONF-24: Newland, 127 or 171 treaties | Overruled | Reopened vol. II: p. 5, "127 different Treaties ... that implicate the Federal Indian boarding school system"; p. 93, finding 7, "the 171 Treaties ... that implicate the Federal Indian boarding school system or education generally" | The two counts are worded as different sets. The report is not shown to contradict itself. The card uses neither number |
| CONF-25: Fujiwara, blank and null shares | Upheld | Reopened the supplement: p. 3, "(13.8% of voters left their paper ballots blank and 9.3% cast a null vote)", in a sentence that explains the larger effect on null votes by their "higher prevalence"; Table A-I, p. 4, Null Votes/Turnout 0.136 and 0.134, Blank Votes/Turnout 0.109 and 0.093 | The parenthesis contradicts its own sentence and the table. Do not cite the split from the supplement. The article is unread |
| CONF-26: Johnes's title | Upheld | Reopened the PDF's title page: "Elementary Education and the Anglicisation of Wales". Crossref, fetched 19 Nov 2026: "... the Anglicisation of Nineteenth-Century Wales" | Follow the cover and Crossref, as the card does |
| CONF-27: Shani, 2017 or 2018 | Upheld | Crossref, fetched 19 Nov 2026: online 24 Nov 2017, print 1 Dec 2017 | Year 2017. The key keeps "2018" as a label. The saved file is the Introduction and shows no copyright page |
| CONF-28: Heckelman, issue 1 or 1–2 | Upheld | Crossref, fetched 19 Nov 2026: vol. 82, issue 1-2, pp. 107–124, January 1995. The page's meta tag: on Fable V-A-1-1 | Follow Crossref: 82(1–2) |
| CONF-37: IMDA, 22 Jan or 20 May 2026 | Overruled | Reopened the PDF cover (version 1.5, 20 May 2026, updated 5 June 2026) and the saved press page (heading dated 22 Jan 2026; no body text saved) | No conflict: January is the launch and the text read is version 1.5. Cite the version read. Nothing read shows what the January version said on the points of p. 47, so no sentence may date those points to January |
| CONF-47: OLG Hamm, final or open to appeal | Overruled | Reopened the database page: header "Rechtskraft: rechtskräftig"; Tenor, "Die Revision wird zugelassen"; para 118, leave granted "wegen grundsätzlicher Bedeutung" | The two are compatible: the court granted leave on 12 May 2026 and the database now marks the judgment final. No saved source gives the date or says whether an appeal was lodged. Cite it as final on the database header as captured |
| CONF-48: which ACP version | Upheld | Reopened the saved text: RFC header "Version: 2026-01-16"; README, `spec/2026-04-17/` "for the latest stable version" | The RFC read is the repository head. Cite it by fetch date with its header version; the 2026-04-17 snapshot is unread |
| CONF-49: Narayanan and Kapoor, 14 or 15 April 2025 | Upheld | Reopened the page: header "April 15, 2025"; "Cite as: ... 25-09 Knight First Amend. Inst. (Apr. 14, 2025)"; `datePublished` 2025-04-15 | Use the publisher's "Cite as" form in the reference; 15 April is the posting date |
| CONF-50: "01.05.2024" | Upheld | Reopened the note: "01.05.2024 Update: On November 15, 2023, Microsoft announced the expansion of the Copilot Copyright Commitment" | Ambiguous as printed. Cite "update note dated 01.05.2024" and do not convert it |
| CONF-21: `STATUS.md` on seven Phase B cards | Upheld | Counted from frontmatter: narayanan, olghamm, smith, tang, susser, wachter and visa all read `verified: corrected` | `STATUS.md` is stale on this line and on SB and X, both of which have since run (`INDEX_DELTA.md`, 19 Nov: 62 cards copied, 3 held back) |
| CONF-35: Brief X's log names | Upheld | PLAN Brief X, step 1, names `FABLE_READ_A.md` and `FABLE_READ_B.md`; `verify/` holds six logs split by sitting | Settled in practice: X selected on the six logs. No card was held back on this ground |

## Calls for the author

Each is his to decide. The evidence is stated for both sides where there are two; the default named is the one
the files already carry.

1. **Retail domination** (ARGUMENT call 2; CONF-13; CE-2.3). The default argues structural enablement on Gädeke's
   test and says "The refund case stands or falls on this." For keeping it: Gädeke's test turns on power that is
   "structurally enabled" (p. 200), which terms of service, an operator-run channel and no other route can
   supply; Hoeksema holds that republicans "cannot rely on" exit (2023, reprint p. 67) and answers the escape
   objection twice (2025, p. 131 n. 70). Against it: the same sentence of Gädeke requires "a persisting status
   asymmetry", and a single refund is an episode; Hoeksema is "agnostic" on her test (p. 28) and writes that a
   clerk who refuses a sale holds "no impositional power" where alternatives exist (p. 30); Pettit and Taylor
   hold that competition and exit keep consumers from arbitrary power ("If all goes well", reported at p. 130);
   the Gädeke card is still `pending`, and McCammon, O'Shea and Pettit 1997 are second-hand. Options the sources
   leave open: keep the default and show dependence case by case; retreat to standing relations (bank, insurer,
   employer, platform); argue aggregation across many small agent decisions (Hoeksema pp. 31–33); or rest the
   retail case on route (i) alone.
2. **Non-domination: describe or judge** (CONF-12; ARGUMENT call 4). A7(ii) makes domination a ground of
   wrongness. Ledger N04 and L04 record the earlier position: it describes positions, and internal critique
   judges. ADJUDICATION_R ruling 14 put the verdict on two present routes; `COVERAGE_PREMISES` v2 marks A7
   "author's ruling needed". Lazar's cards, the converging route, are still `pending`.
3. **The definition** (CONF-11). STRUCTURE §1.1 quotes draft 04, line 5 ("two human parties ... an opaque
   algorithmic intermediary that observes both and commits binding outcomes"). Draft 05, line 31, reads "human
   agents ... an automated third party that processes, evaluates, and enforces outcomes binding on both sides".
   Bearing on the choice: in payment protocols the party acted on is a merchant, not a consumer (CE-1.8; ruling 19).
4. **The monopoly rows** (CONF-46; ruling 7). §4.1 keeps the author's "contemporary monopolies restricted
   infrastructure and model weights" (04, line 109). Ledger E07 left that row open, the run adds no card on
   concentration, and Nadella's P5 and P14 argue against dependence on one supplier. §4.4 row 1 can keep
   "custody by an interested party" on P17 and the products; whether either row keeps the word "monopoly" is his.
5. **Five failures or six** (STRUCTURE call 2; Part A §3). GA proposes no sixth: fold candidates 1, 2, 4, 6, 7
   and 8, drop 3 and 5. Candidate 2 now has a primary source (ruling 21). If a sixth is wanted, GA names candidate
   7, capture by intermediaries, as the best supported; CE-1.7 puts the same point as a sixth question (who
   appoints and instructs the party that acts for her). Phase B ran on the default of no sixth.
6. **The Berthon sentence in §4.2** (ruling 3; consolidation X07). Page 457 supports "information is necessary,
   but not sufficient to change behavior", from Worsley, on digital addiction. Whether to keep the cite for that
   narrow point, and how the paper states its relation to Berthon, Pitt and Campbell's scheme, X07 already holds
   open.
7. **Where the allocation is charged** (rulings 5, 8, 9; CE-4.2). P15, P19 and P20 exclude no one in terms: P15
   names no reader, P19 no authoriser, and P20 asks for "timely disclosure to those affected". The exclusion
   stands in the products and terms read: the tenant's audit portal, the maker's approval toggle, a "security or
   compliance team" writing policy, and terms "for the benefit of" no other person. The author's instruction is
   that Nadella's solutions would repeat literacy's mistakes. The sources support that claim for the
   architecture as his firm builds it, and do not support it for the essay's sentences read alone.
8. **How §4.2 and A8 list the law** (rulings 1, 2, 4). The facts are fixed above. The choice left is between a
   dated list (art. 26(11) from 2 Dec 2027; art. 86 tied to Annex III; art. 85 as a surveillance complaint) and a
   list cut to what applies in November 2026.
9. **IMDA** (ruling 10). It can stand as a counter-instance (a public body does ask for the envelope and a human
   contact to be given to the customer) or as evidence that the other course is on offer in 2026, or both. It is
   worded as what organisations "should consider", and about 22 of its 53 pages were read (on Fable V-B-1).
10. **D04's precedents** (ruling 20). Add s. 208 of the Voting Rights Act (a helper of the voter's choice, not her
    employer or union), and decide how D04 meets the Election Commission's objection that an official helper ends
    secrecy.
11. **D03's precedent** (ruling 19; CE-7.1). AP2 and Visa's protocol let a merchant verify an agent. ARGUMENT
    rates D03's precedent "working". Whether a design that protects the merchant counts as precedent for a duty
    owed to the person acted on, or only as proof that a verifiable envelope can be built, is his.
12. **Tang et al.** (ruling 12). Use it for the responsibilization point (p. 16), as an instance of the remedy
    the paper criticises (p. 18), or as both; the second use makes it evidence for CE-6.4.
13. **Three bearing values the Fable reader changed and asked him to confirm.** narayanan2025ai: standing from
    partial to no, loss cover from no to partial (on Fable V-B-1; I did not reopen Part IV). visa2025trusted:
    envelope from yes to partial. The README lines I reopened give the merchant proof that the agent is authorised
    "for the specific action it is taking (browsing or payment)" and state no limit set by the user, which fits
    "partial".
14. **Smaller points for his eye.** The Positive Sum post says "Bill" (para 2); "Gates" is an inference. §4.3's
    "the most explicit design for governing agents" rests on no comparison (Part B §B2), and the two vendor
    frameworks read, Anthropic's and Google's, make the same allocation (CE-4.3). The OLG Hamm quotations carry
    the drafter's translations (on Fable V-B-1).
15. **Carried and untouched by this run**: the title; how much platform material §4.1 holds; the drafting method
    (STRUCTURE calls 1, 3, 4); Lazar as a converging route (ARGUMENT call 3).

## Card and file work still to do (lead)

- Save the records for levine1982functional, sandiford1994nicaraguan and yilmaz2011learning, then give each its
  Fable read. Until then they stay out of the index.
- Write an upgrade card for the Copilot Terms of Use that carries the indemnity sentence (ruling 5); correct the
  map's L-1 row and CE-4.5's heading to match.
- Put art. 26(11)'s text and Omnibus art. 1 point (40)(b) on a card in the paper's folder, and bring A8 into line
  with ADJUDICATION_R ruling 9 and ruling 1 here.
- Clear gadeke2020mugger, which carries call 1. Other pending library cards that sections lean on are listed in
  Part B §B1.2 (Lassiter, the Lazar lectures, CPPA, Colorado, arbel2025how).
- Read s. 201 of the Voting Rights Act as it stood in 1975 before §3.2 or D02 speaks of a permanent ban.
- Update `STATUS.md` (CONF-21) and the two `references.bib` notes (CONF-39). Bring `NADELLA_MOVES.md` row 8 to
  the post's wording (CONF-34).
- Carry three narrowings into the files that hold the older wording: ADJUDICATION_R rulings 6 and 8 (rulings 15
  and 24 here), ledger N05's "exit and consent fail" (ruling 11), and the map's "no duty to fact-check"
  (ruling 4).
- Check against the version of record before any page is printed: Wachter et al. (IDPL 7(2), 76–99), Yeung
  (ICS 20(1), 118–136), *Saunders* ([1971] AC 1004), Kleinberg et al. (QJE 133(1)).

## What I fetched

Four Crossref records by DOI, on 19 Nov 2026, with the client name `research-fetch/1.0` and no e-mail or other
identifier: 10.1017/9781009279079.019, 10.16922/welshnot, 10.1017/9781107705722, 10.1007/bf01047732. I filtered
each response to title, authors, dates, volume, issue and pages, and saved nothing in the repo. I made no web
fetch for the legal dates: the two Official Journal texts already on disk settle them.

## Erratum (Fable read F, 2026-11-19)

*Agent-drafted (Fable reader, sitting F, 2026-11-19); appended, with nothing above changed. A working note for the
author, not paper prose; none of the text is his.*

Ruling 1 dates art. 26(11) too simply. Its Effect column says the paragraph "applies from 2 Dec 2027", and call 8
repeats the date. Art. 111(2) of Regulation (EU) 2024/1689 limits that date, and the ruling does not cite it. I
opened it in both Official Journal texts on disk while reading `cards/euaiact2026dates.md`, and the verifier's
point (`verify/VERIFY_V-F.md`) holds.

- **The text.** Reg. (EU) 2026/1744, art. 1 point (39)(a), replaces art. 111(2): "this Regulation shall apply to
  operators of high-risk AI systems, other than the systems referred to in paragraph 1 of this Article, that have
  been placed on the market or put into service before the date of application of Chapter III referred to in
  Article 113, only if, as from that date, those systems are subject to significant changes in their designs. In
  any case, the providers and deployers of high-risk AI systems intended to be used by public authorities shall
  take the necessary steps to comply with the requirements and obligations laid down in this Regulation by
  2 August 2030." A deployer is an operator (2024/1689, art. 3 point (8)). The rule is older than the Omnibus:
  art. 111(2) as enacted carried it with the date 2 August 2026, and point (39)(a) moved the cut-off and kept 2030.
- **Ruling 1, narrowed.** On 19 Nov 2026 art. 26(11) does not apply; that stands. From 2 Dec 2027 (art. 113, third
  paragraph, point (c)(i), as replaced by 2026/1744, art. 1 point (40)(b)) it binds deployers of Annex III systems
  placed on the market or put into service on or after that date. For a system placed on the market or put into
  service before that date, it binds the deployer only once the system's design changes significantly. Where such
  a system is intended to be used by public authorities, its provider and deployer must comply by 2 Aug 2030 in any
  case. The texts set no date by which a private deployer of an unchanged earlier system must give the notice.
- **How far the earlier systems reach.** Recital 39 of 2026/1744 reads the grace period by type and model: once
  one unit is lawfully on the market or in service before the date, further units of that type and model follow
  it "as long as the design of that high-risk AI system remains unchanged". Recital 177 of 2024/1689 treats a
  significant change as "equivalent in substance to the notion of substantial modification" (defined in art. 3
  point (23)).
- **Arts. 85 and 86.** Art. 111(2) says "this Regulation", so on its words the same limit reaches what a deployer
  of such a system owes under art. 86, and leaves an art. 85 complaint about that deployer without an infringement
  to rest on. No text read says either in terms. The rest of ruling 1 on arts. 85 and 86 stands.
- **Where the unqualified date stands.** Ruling 1 (Effect) and call 8 ("art. 26(11) from 2 Dec 2027"). The lead's
  item to card art. 26(11) with point (40)(b) is met by `cards/euaiact2026dates.md`, which now carries point
  (39)(a) as well. The direction of ruling 1 holds and gains force: on these texts the art. 26(11) notice is owed
  only for systems placed on the market or put into service from 2 Dec 2027, for earlier systems once their design
  changes significantly, and for systems intended for public authorities by 2 Aug 2030.
- **Limits.** I read recitals 39 and 40, art. 1 points (39) and (40) and art. 4 of 2026/1744, and recital 177 and
  art. 3 points (8) and (23) and arts. 26, 85, 86, 111 and 113 of 2024/1689. Two readings are mine. The paragraph names no date for "the date
  of application of Chapter III referred to in Article 113"; I take it as 2 Dec 2027 for Annex III systems and
  2 Aug 2028 for Annex I systems, from point (c) and recital 40. Recital 39 speaks of providers, and neither text
  says in terms whether a deployer who takes up, after the date, a unit of an earlier type and model owes the
  notice. I searched for no act later than 24 July 2026 and read no consolidated text, guidance or case law.
