<!-- DRAFTED BY CLAUDE (Opus 5.5), 11 Nov 2026. The source corrections made to DRAFT_v6 after the reviewer pack, at the authors' instruction ('go'). Facts only: each item makes a sentence say what its source says, marks the authors' own inference as theirs, fixes a locator, or removes a citation that did not support its sentence. Argument and register changes were not made; they wait for the authors' decisions and read-aloud. Each item is also recorded in sbs/LEDGER.md under its sentence. -->

# Source corrections to DRAFT_v6, 11 November 2026

**Basis.** `reviews/2026-11-11/SYNTHESIS.md`, section 5, the source-integrity ledger. Every item was re-checked against its card in `library/cards/` before the edit, and the card or page is named below. Items the synthesis marked VERIFY were not changed (list at the end).

**Effect.** Body 8,385 → 8,775 words (limit 9,000). References 83 → 82: Xu et al. 2021, Möhlmann et al. 2021 and De Vos et al. 2024 removed; Boo and Chua 2022 and Ivanov and Webster 2024 added. Kaniadakis and Farmaki now carries its 2024 issue year and journal page. Seven sentences that the corrections lengthened were split without change of content (recorded in the ledger as 'Split for length').

**Checks after the corrections.** Ledger and manuscript agree sentence by sentence (280 body sentences in order; manuscript body identical to DRAFT_v6). `check_citations.py`: 113 citations, the one known Woodland flag. `preflight.py` on a numbered copy: 20 of 23, the known artefacts. The reviewer letter's 27 quotations of revised text all still match. `build_index.py --check`: OK.

## The corrections

### C01 · S-003 · Introduction

- **Why:** Xu et al. was held at abstract depth and displaced by Boo and Chua in August; Belanche et al. studied vignette respondents, not guests.
- **Source:** cards xu2020facial (superseded_by boochua2022facial), boochua2022facial (abstract), belanche2020 pp. 275-276, 281
- **Was:** Facial-recognition systems verify identity at check-in (Xu et al. 2021), and service robots greet, direct and serve guests, who hold the firm responsible when the robots fail (Belanche et al. 2020).
- **Now:** Facial-recognition systems verify identity at check-in (Boo and Chua 2022), and service robots greet, direct and serve guests; in vignette experiments, respondents held the firm more responsible when a robot rather than an employee failed (Belanche et al. 2020).
- **Words:** +8

### C02 · S-010 · Introduction

- **Why:** Germann Molz calls her method exploratory and illustrative, so 'showed' overstates; Riordan's subjects are delivery workers, not guests.
- **Source:** cards germannmolz2018scale p. 235; riordan2024digitally (abstract)
- **Was:** Germann Molz (2018: 244) showed Airbnb using its status as a platform to evade legal responsibility, and later work describes guests without hosts and algorithmic hostility (Germann Molz 2026; Riordan 2024).
- **Now:** Germann Molz (2018: 244) described Airbnb using its status as a platform to evade legal responsibility, and later work describes guests without hosts and an algorithmic hostility towards food-delivery workers (Germann Molz 2026; Riordan 2024).
- **Words:** +4

### C03 · S-011 · Introduction

- **Why:** Batat 2026 and Brochado et al. said nothing about smoothness; 'tools' came from a dropped source and van Doorn et al. supports 'social presence'; the absence claim was refuted by Shabnam et al. and is narrowed to the gap that survives.
- **Source:** cards batat2026psr (title, abstract), brochado2026phygital (abstract), vandoorn2017domo p. 43, li2021systematic (abstract), xing2026algorithmic (title), shabnam PDF p. 14
- **Was:** The phygital literature presents such systems as means to a smoother and more personal experience (Batat 2024, 2026; Brochado et al. 2026) and describes them by what they do, as tools, mediators, facilitators and co-creators (van Doorn et al. 2017; Li et al. 2021; Xing and Zhang 2026), without saying what the party that deploys them owes the guest.
- **Now:** Phygital operation may now be the normal condition of services (Brochado et al. 2026), and the literature on it presents such systems as means to a smoother and more personal experience (Batat 2024) and describes them by what they do, as social presences, mediators, facilitators and co-creators (van Doorn et al. 2017; Li et al. 2021; Xing and Zhang 2026). Where it turns to governance, it calls for human-first design and contestable rules (Batat 2026; Shabnam et al. 2026), without saying to whom these safeguards are owed or which of the firms behind a system owes them.
- **Words:** +38

### C04 · S-012 · Introduction

- **Why:** Nissenbaum points to designers, expert sources or the deploying organization, not to the delegating party alone.
- **Source:** card nissenbaum1996accountability pdf p. 11
- **Was:** Algorithmic-accountability research keeps answerability with the party that delegates but ties it to harm (Nissenbaum 1996; Kong 2026: 5)
- **Now:** Algorithmic-accountability research looks for answerability among those who design or deploy a system and ties it to harm (Nissenbaum 1996; Kong 2026: 5)
- **Words:** +4

### C05 · S-032 · The host's power and the host's obligation

- **Why:** The 'promise' generalized one uncited sentence in O'Gorman's conclusion; its evidence concerns caravanserais built by rulers and donors.
- **Source:** card ogorman2009origins pdf pp. 9-11
- **Was:** Commercial houses made a similar promise: by O'Gorman's account, a traveller who crossed their threshold was guaranteed protection and refuge (2009).
- **Now:** O'Gorman's history of commercial hospitality ends on the claim, for which it cites no evidence, that crossing a commercial threshold also guaranteed the traveller physical protection (2009).
- **Words:** +6

### C06 · S-048 · The host's power and the host's obligation

- **Why:** The 'externally imposed' obligation is religious obligation, and the same authors state the host's duty to keep guests safe. The paragraph's opening claim that the debate turns on motive is left for the authors (synthesis, finding on the foil).
- **Source:** card blain2014hospitableness pp. 1-2
- **Was:** Blain and Lashley set an obligation that is 'externally imposed' against hospitableness, with which it 'may be at odds', and look to secure the welcome by recruiting people with hospitable motives (2014: 2).
- **Now:** Blain and Lashley hold that the host 'is obliged to make the guests safe' (2014: 1), yet set obligations that are 'externally imposed', such as religious ones, against hospitableness, with which they 'may be at odds', and look to secure the welcome by recruiting people with hospitable motives (2014: 2).
- **Words:** +17

### C07 · S-057 · The host's power and the host's obligation

- **Why:** Bogen's sentence concerns the duty to serve the public, not all the innkeeper's duties.
- **Source:** card bogen1996innkeeper p. 75
- **Was:** finding that it was 'English law, not the innkeeper's express commitment' that imposed them (1996: 75)
- **Now:** finding that it was 'English law, not the innkeeper's express commitment' that imposed the duty to serve the public (1996: 75)
- **Words:** +5

### C08 · S-077 · The host's power and the host's obligation

- **Why:** The paraphrase dropped a defining condition of s. 1(3).
- **Source:** card uk1956hotel s. 1(3)
- **Was:** applies those duties to an establishment 'held out by the proprietor' as offering food, drink and, if required, a bed to 'any traveller presenting himself
- **Now:** applies those duties to an establishment 'held out by the proprietor' as offering food, drink and, if required, a bed, 'without special contract', to 'any traveller presenting himself
- **Words:** +3

### C09 · S-083 · The host's power and the host's obligation

- **Why:** The Act deems a hotel, and only a hotel, an inn, so the denial of any special legal category was wrong.
- **Source:** card uk1956hotel s. 1(1)
- **Was:** To say that the law imposes the duty is not to say that the law explains it, or that it places today's hotels in any special legal category.
- **Now:** To say that the law imposes the duty is not to say that the law explains it, although the 1956 Act does set hotels apart by deeming them, and no other establishment, to be inns (s. 1(1)).
- **Words:** +9

### C10 · S-087 · The host's power and the host's obligation

- **Why:** The sentence is Golubovskaya et al.'s, citing King; it was presented as King's formulation.
- **Source:** card golubovskaya2017meaning p. 1286
- **Was:** In commercial hospitality the guest's duties narrow: in King's formulation, as Golubovskaya et al. report it, the guest's 'only obligation is to pay and behave reasonably' (2017: 1286).
- **Now:** In commercial hospitality the guest's duties narrow: following King (1995), Golubovskaya et al. write that commercial hospitality often empowers the guest, 'whose only obligation is to pay and behave reasonably' (2017: 1286).
- **Words:** +4

### C11 · S-088 · The host's power and the host's obligation

- **Why:** Xiang et al. studied one upscale hotel under state-imposed pandemic rules; the general 'hotels' overstated it.
- **Source:** card xiang2022covid (design; limitations)
- **Was:** and hotels ask guests to leave who will not follow the stay's rules after repeated communications (Xiang et al. 2022)
- **Now:** and in one hotel under pandemic rules, guests who would not follow the stay's rules after repeated communications were asked to leave (Xiang et al. 2022)
- **Words:** +6

### C12 · S-101 · Delegation and standing: Beyond the host in person?

- **Why:** Pages 7-8 are accepted-manuscript pages, not pages of the journal version listed; the journal version is closed, so the paraphrase carries no pinpoint.
- **Source:** card morgan2015liability ('AM page numbers are not journal pages')
- **Was:** (Woodland v. Essex County Council 2013: para 7; Morgan 2015: 7–8)
- **Now:** (Woodland v. Essex County Council 2013: para 7; Morgan 2015)
- **Words:** -1

### C13 · S-108 · Delegation and standing: Beyond the host in person?

- **Why:** Reporter page in place of the copy's paragraph numbers.
- **Source:** card crinkley1988holiday source_basis (paras 7 and 9 at 159)
- **Was:** were all held liable to guests assaulted in their room (1988: paras 7, 9).
- **Now:** were all held liable to guests assaulted in their room (1988: 159).
- **Words:** -2

### C14 · S-109 · Delegation and standing: Beyond the host in person?

- **Why:** Reporter pages; footnote 3 (Hayman v. Ramada Inn), which limits the holding where guests do not choose the brand, had been omitted.
- **Source:** card crinkley1988holiday paras 49-52, fn 3 (pp. 166-67)
- **Was:** though the court called the evidence of reliance 'marginal' (1988: paras 9, 49–52).
- **Now:** though the court called the evidence of reliance 'marginal' and recorded that a North Carolina appeals court had rejected a comparable claim where the guest's employer, not the guest, had chosen the motel (1988: 159, 166–67 and n. 3).
- **Words:** +26

### C15 · S-118 · Delegation and standing: Beyond the host in person?

- **Why:** The quotation carried an accepted-manuscript page; without the closed journal version it becomes a paraphrase.
- **Source:** card morgan2015liability
- **Was:** and Morgan states the principle in a line: 'No duty of care can be delegated, but its performance may well be' (2015: 7).
- **Now:** and Morgan states the principle that no duty of care can be delegated, though its performance may be (2015).
- **Words:** -4

### C16 · S-124 · Delegation and standing: Beyond the host in person?

- **Why:** Nissenbaum names designers, sources or the deploying organization; the deployer-specific claim is Kong's.
- **Source:** cards nissenbaum1996accountability pdf pp. 6, 11; kong2026delegation p. 5
- **Was:** Writers on algorithmic accountability already hold that deploying an autonomous system does not lessen the deployer's responsibility (Nissenbaum 1996; Kong 2026: 5).
- **Now:** Writers on algorithmic accountability already hold that handing a function to a system does not dissolve answerability, which may lie with its designers or with the organization that deploys it (Nissenbaum 1996), and that deploying an autonomous system does not lessen the deployer's responsibility (Kong 2026: 5).
- **Words:** +25

### C17 · S-128 · Delegation and standing: Beyond the host in person?

- **Why:** Kropf et al. name programmers, manufacturers and other humans, not deployers alone.
- **Source:** card kropf2026blame p. 9
- **Was:** and that blame stays with the humans who deploy it (2026: 7, 9–10).
- **Now:** and that accountability stays with human beings, among them its programmers and manufacturers (2026: 7, 9–10).
- **Words:** +3

### C18 · S-131 · Delegation and standing: Beyond the host in person?

- **Why:** The p. 36 gloss concerns second-personal authority in general; pp. 31-32 state the obligee's authority.
- **Source:** card darwall2013bipolar pp. 31-32, 36
- **Was:** Darwall glosses the authority of an obligee as a 'standing to address claims and demands and hold accountable' (2013: 36), so that
- **Now:** Darwall holds that bipolar obligations give obligees a 'distinctive discretionary second-personal authority' to make claims and demands of obligors and hold them personally responsible (2013: 31–32), so that
- **Words:** +6

### C19 · S-132 · Delegation and standing: Beyond the host in person?

- **Why:** Quoted together, the two forms swap the roles of X and Y; only the duty form is needed.
- **Source:** card thompson2004wrong p. 335
- **Was:** Thompson's forms of directed duty, 'X has a duty to Y to do A' and 'X has a right against Y' (2004: 335), fix who owes what to whom without mentioning answering.
- **Now:** Thompson's form of directed duty, 'X has a duty to Y to do A' (2004: 335), fixes who owes what to whom without mentioning answering.
- **Words:** -7

### C20 · S-134 · Delegation and standing: Beyond the host in person?

- **Why:** 'Concedes' overstated; Darwall goes on to tie the right to the obligee's authority (reviewer R2; the authors should read p. 35 in full).
- **Source:** card darwall2013bipolar p. 35
- **Was:** as Darwall himself concedes when he writes
- **Now:** as Darwall allows when he writes
- **Words:** -1

### C21 · S-139 · Delegation and standing: Beyond the host in person?

- **Why:** The quotation concerns commercial-home hosts, not commercial hosts generally.
- **Source:** card didomenico2007host p. 335
- **Was:** since commercial hosts 'must meet the desires and demands of the paying guest' (Di Domenico and Lynch 2007: 335)
- **Now:** since even the hosts of commercial homes 'must meet the desires and demands of the paying guest' (Di Domenico and Lynch 2007: 335)
- **Words:** +4

### C22 · S-150b · Assembled hosts at the touchpoint

- **Why:** The receptionist finding is the inquiries', as the authors read them.
- **Source:** card petie2025exploring MS p. 11
- **Was:** Petie et al. (2025) describe hosting divided by outsourcing
- **Now:** Petie et al. (2025), drawing on an official evaluation and an independent inquiry, describe hosting divided by outsourcing
- **Words:** +9

### C23 · S-151 · Assembled hosts at the touchpoint

- **Why:** As C02.
- **Source:** card germannmolz2018scale p. 235
- **Was:** Germann Molz (2018: 243–244) has shown the other end of the path
- **Now:** Germann Molz (2018: 243–244) has described the other end of the path
- **Words:** +0

### C24 · S-156 · The authority–answerability split

- **Why:** Batat's framework concerns customer experience in general, not hospitality.
- **Source:** card batat2024phcx
- **Was:** Accounts of phygital hospitality describe the movement between physical and digital touchpoints as fluid and make smoothness a goal of design (Batat 2024: 1220, 1233).
- **Now:** Accounts of the phygital customer experience describe the movement between physical and digital touchpoints as fluid and make smoothness a goal of design (Batat 2024: 1220, 1233).
- **Words:** +2

### C25 · S-158 · The authority–answerability split

- **Why:** The relay restates Batat's two processes without credit.
- **Source:** card batat2024phcx pp. 1230-1231
- **Was:** The movement can as accurately be called a relay: physical moments become digital records,
- **Now:** Batat names the two directions of that movement digitalization and physicalization (2024: 1230–1231), and together they can as accurately be called a relay: physical moments become digital records,
- **Words:** +14

### C26 · S-163 · The authority–answerability split

- **Why:** Page 14 was the OnlineFirst PDF's; the open journal version (CC BY, read 11 Nov 2026) prints the quotation on p. 5776 of the 2024 issue.
- **Source:** journal PDF, revision_2026-11/research/sources/kaniadakis2022responsibilisation/vor.pdf, p. 5776
- **Was:** (Kaniadakis and Farmaki 2022: 14)
- **Now:** (Kaniadakis and Farmaki 2024: 5776)
- **Words:** +0

### C27 · S-169 · The authority–answerability split

- **Why:** Reporter page.
- **Source:** card crinkley1988holiday source_basis
- **Was:** among owners, an operating company and a franchisor (1988: para 7)
- **Now:** among owners, an operating company and a franchisor (1988: 159)
- **Words:** -1

### C28 · S-173 · The authority–answerability split

- **Why:** Both sources concern platform workers and participants; the guest-data claim is our application and is now marked as an analogy.
- **Source:** cards rahman2021cage; calorosenblat2017taking (abstract)
- **Was:** alongside the property's inventory and constraints (Rahman 2021; Calo and Rosenblat 2017).
- **Now:** alongside the property's inventory and constraints, much as platforms hold what their workers and users cannot see (Rahman 2021; Calo and Rosenblat 2017).
- **Words:** +11

### C29 · S-174 · The authority–answerability split

- **Why:** Neither source reports a trend in time spent reading decisions; Spektor et al.'s cost is documentation labour.
- **Source:** cards pedersen2022 p. 80; spektor2025working s. 5.3
- **Was:** Discretion splits, because staff keep some freedom to act while more of their day goes to reading decisions made elsewhere and working around categories set elsewhere (Pedersen and Pors 2023; Spektor et al. 2025).
- **Now:** Discretion splits, because staff keep some freedom to act but must work around categories and scripts set elsewhere and record their work for the system (Pedersen and Pors 2023; Spektor et al. 2025).
- **Words:** -1

### C30 · S-181 · Three conditions and six questions

- **Why:** The source's accountability is task responsibility among coordinating parties; the change of sense is now visible.
- **Source:** card okhuysenbechky2009 p. 483
- **Was:** which identifies 'three integrating conditions for coordination: accountability, predictability, and common understanding' (Okhuysen and Bechky 2009: 483).
- **Now:** which identifies 'three integrating conditions for coordination: accountability, predictability, and common understanding', and in which accountability settles 'who is responsible for specific elements of the task' (Okhuysen and Bechky 2009: 483).
- **Words:** +14

### C31 · S-192 · Three conditions and six questions

- **Why:** Garcia et al. say nothing about the desk; managers keep the final decision. 'Moderate' was not the guidance's word.
- **Source:** cards garcia2026strategic (WP p. 5); article292018guidelines p. 22
- **Was:** Neither guest nor staff could anticipate the operative rule and no one at the desk could explain the price, so the touchpoint fails on predictability and on accountability, although its legal weight is moderate unless the price bars a guest from the service (Article 29 Working Party 2018: 22).
- **Now:** The final decision stayed with revenue managers, who could set the advice aside (Garcia et al. 2026). On our reading, neither a guest nor the staff at the desk could anticipate the operative rule or reach the managers who held it, so the touchpoint fails on predictability and on accountability. How much that matters depends on the price, since the regulators' guidance holds that differential pricing could significantly affect a person whom prohibitively high prices bar from a service (Article 29 Working Party 2018: 22).
- **Words:** +36

### C32 · S-193 · Three conditions and six questions

- **Why:** The history-weighing system is our hypothetical, not Xu et al.'s; Xu et al. was displaced.
- **Source:** cards xu2020facial; boochua2022facial (abstract)
- **Was:** At check-in, a facial-recognition system that confirms a guest's identity does a clerical job, while one that weighs the guest's history to decide how they will be received is deciding admission (Xu et al. 2021).
- **Now:** At check-in, a facial-recognition system that confirms a guest's identity does a clerical job (Boo and Chua 2022), while one that weighed the guest's history to decide how they would be received, a case we construct, would be deciding admission.
- **Words:** +5

### C33 · S-195 · Three conditions and six questions

- **Why:** Bosma says nothing about codes failing at night; the night failure is now our hypothetical, and the platform's rule is Bosma's.
- **Source:** card bosma2022platformed p. 605
- **Was:** In a short-term rental with self-check-in the app may answer the first three questions well, yet when a code fails at night no one with authority may be reachable (Bosma 2022: 605).
- **Now:** In short-term rentals Airbnb requires self-check-in for a listing to qualify for business travellers, so that guests can arrive 'without meeting anyone in person' (Bosma 2022: 605); the app may answer the first three questions well, yet if a code failed at night no one with authority might be reachable.
- **Words:** +18

### C34 · S-196 · Three conditions and six questions

- **Why:** Batat says nothing about rules or staff discretion; it reports staff present and social.
- **Source:** card batat2021ar pp. 7-8, and its note that the study is silent on rules and discretion
- **Was:** When a restaurant projects an animated chef onto the table while staff go on hosting the meal, the technology adds to an encounter whose rules stay steady and whose staff keep their discretion (Batat 2021), and the touchpoint passes.
- **Now:** When a restaurant projects an animated chef onto the table, diners describe the staff as still present and sociable (Batat 2021: 7–8); the projection decides nothing about the guest, and the touchpoint passes.
- **Words:** -6

### C35 · S-197 · Three conditions and six questions

- **Why:** No case reports guest satisfaction or the absence of harm. (The Conclusion's matching claim is left for the authors.)
- **Source:** the four cases as now described
- **Was:** Together the cases show that a touchpoint can satisfy guests and harm no one while failing the test.
- **Now:** Together the cases show that the questions separate touchpoints that decide something about the guest from those that decide nothing.
- **Words:** +2

### C36 · S-199 · Three conditions and six questions

- **Why:** Bendoly is a laboratory study of reservation agents' latitude below the system's price; it says nothing about a guest's sense of control.
- **Source:** card bendoly2013realtime (abstract)
- **Was:** Skilled front-desk employees manufacture a guest's sense of control through small acts of discretion, appearing to defer while steering the options (Bendoly 2013).
- **Now:** Hotel reservation agents are often given latitude to accept rate bids below a revenue-management system's prescriptions, and in a laboratory experiment how far they used it depended on how they expected management to view their actions (Bendoly 2013).
- **Words:** +15

### C37 · S-200 · Three conditions and six questions

- **Why:** Jianu et al. is a Delphi forecast, and its translation runs from managers to staff.
- **Source:** card jianu2025 pp. 4, 7, 10
- **Was:** Under algorithmic direction that work becomes translation in both directions, as managers carry the system's decisions to the people they affect (Jianu et al. 2025) and the employee at the desk carries the guest's request into terms the system will accept.
- **Now:** Under algorithmic direction that work becomes translation: experts consulted on hotels expect managers to explain and justify the system's opaque decisions to frontline staff (Jianu et al. 2025: 7, 10), while the employee at the desk carries the guest's request into terms the system will accept.
- **Words:** +5

### C38 · S-201 · Three conditions and six questions

- **Why:** 'Overnight' and 'no one tells' were ours; Hatherley's point is outdated mental models after updates.
- **Source:** card hatherley2025moving p. 7, and its support verdicts
- **Was:** The translation is fragile, because when a system quietly revises its rules the knowledge it rests on loses its value overnight and no one tells the employee or the guest (Hatherley 2025).
- **Now:** The translation is fragile, because when a system is updated the mental models its users have built from experience can become outdated (Hatherley 2025: 7).
- **Words:** -7

### C39 · S-202 · Three conditions and six questions

- **Why:** Neither source concerns producing a sense of control; Fuller and Smith concern management by customers, and Möhlmann et al. was superseded.
- **Source:** cards fuller1991consumers (abstract); mohlmann2021algorithmic (superseded_by jianu2025; Uber drivers)
- **Was:** Staff are asked to produce a sense of control without holding the controls (Fuller and Smith 1991; Möhlmann et al. 2021), employees fall silent
- **Now:** Managers can use guests' reports to monitor and discipline staff (Fuller and Smith 1991), employees fall silent
- **Words:** -7

### C40 · Table 1 · When a person must be reachable (Table 1)

- **Why:** Wilson-Nash et al. count a kept but downgraded route as a trigger of captivity.
- **Source:** card wilsonnash2025captivity p. 978
- **Was:** | A staffed fallback; a reachable person if failure would refuse entry |
- **Now:** | A staffed fallback that is not a downgraded route; a reachable person if failure would refuse entry |
- **Words:** +6

### C41 · S-214 · When a person must be reachable

- **Why:** The prose contradicted Table 1's identity row.
- **Source:** Table 1
- **Was:** Identity checks, room allocation and pricing need a later appeal by default, and a reachable person where failure would refuse entry or leave a room unusable.
- **Now:** Identity checks need a staffed fallback, room allocation and pricing a later appeal by default, and each a reachable person where failure would refuse entry or leave a room unusable.
- **Words:** +4

### C42 · S-215 · When a person must be reachable

- **Why:** The absence claim was refuted by a study held in the library.
- **Source:** card ivanov2024automated (abstract)
- **Was:** The placements are our own reading of the sources cited, and no study makes them for hospitality.
- **Now:** The placements are our own reading of the sources cited; the nearest hospitality study asks hoteliers which of 23 hotel decisions they would leave to artificial intelligence, not what recourse a guest needs (Ivanov and Webster 2024).
- **Words:** +20

### C43 · S-218 · When a person must be reachable

- **Why:** Art. 22(3) applies within the exceptions; outside them art. 22(1) forbids such decisions. The sentence implied the right applied generally.
- **Source:** card gdpr2016art22 arts 22(1)-(3)
- **Was:** Under the General Data Protection Regulation, a person subject to a solely automated decision with legal or similarly significant effects has 'at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision' (Regulation (EU) 2016/679, art. 22(3)).
- **Now:** Under the General Data Protection Regulation, a person has the right not to be subject to a solely automated decision with legal or similarly significant effects (Regulation (EU) 2016/679, art. 22(1)), and where such a decision is allowed because it is necessary to a contract, among other grounds, the controller must provide 'at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision' (art. 22(2)–(3)).
- **Words:** +28

### C44 · S-220 · When a person must be reachable

- **Why:** Follows C43.
- **Source:** card gdpr2016art22
- **Was:** The right states no timing, and many hotel decisions may fall within the exception for decisions necessary to a contract (art. 22(2)(a)).
- **Now:** The right states no timing, and many hotel decisions may fall within that contractual exception (art. 22(2)(a)).
- **Words:** -5

### C45 · S-221 · When a person must be reachable

- **Why:** That the safeguard comes after the decision is a reading, since the article states no timing.
- **Source:** card gdpr2016art22 (the card marks this as inference)
- **Was:** The law therefore secures a later review, not a person at the threshold.
- **Now:** The law can therefore be satisfied by a later review rather than a person at the threshold.
- **Words:** +4

### C46 · S-228 · Designing for interruptible hospitality

- **Why:** The study concerns fashion and luxury production; Mosca 2026 is an editorial, a position rather than a finding.
- **Source:** cards moscalarosa2019; mosca2026ai
- **Was:** One study of luxury production found customers so uneasy about technology that it advised keeping its use hidden to protect a sense of authenticity (Mosca and La Rosa 2019), while more recent work backs transparency and human oversight for high-stakes systems (Mosca 2026).
- **Now:** One study of fashion and luxury production found customers so uneasy about technology that it advised keeping its use undisclosed to protect a sense of authenticity (Mosca and La Rosa 2019), while a more recent editorial endorses transparency and human oversight for high-risk systems (Mosca 2026).
- **Words:** +3

### C47 · S-231 · Designing for interruptible hospitality

- **Why:** The fuller explanation guests wanted comes after the stay, not later in it.
- **Source:** card pigac2026transparency pp. 286, 291
- **Was:** since guests prefer little disclosure at check-in and fuller explanation later in the stay (Pigac et al. 2026: 286)
- **Now:** since guests prefer little disclosure at check-in and fuller, retrospective explanation afterwards, in post-stay feedback and loyalty apps (Pigac et al. 2026: 286, 291)
- **Words:** +5

### C48 · S-231 · Designing for interruptible hospitality

- **Why:** Hatherley doubts that announcing changes reduces the risk; the principle now concedes it.
- **Source:** card hatherley2025moving p. 11
- **Was:** and make significant rule changes visible (Hatherley 2025).
- **Now:** and make significant rule changes visible, though informing users of a change may not by itself reduce the risks it brings (Hatherley 2025: 11).
- **Words:** +16

### C49 · S-235 · Designing for interruptible hospitality

- **Why:** Lyons et al. report submissions' view, hedged 'likely'; Martin and Waldman did not compare five mechanisms on adverse decisions, where only appeal was tested.
- **Source:** cards lyons2021conceptualising pdf p. 12; martinwaldman2022legitimate (Results; Discussion)
- **Was:** The deploying organization is best placed to reverse a decision (Lyons et al. 2021), algorithmic governance in services calls for routes of escalation and human oversight (Shabnam et al. 2026), and of five governance mechanisms only appeal raised the perceived legitimacy of an adverse algorithmic decision (Martin and Waldman 2023).
- **Now:** Submissions to an Australian consultation held that the entity deploying a system is likely to be best placed to reverse its decisions (Lyons et al. 2021), algorithmic governance in services calls for routes of escalation and human oversight (Shabnam et al. 2026), and in vignette studies an appeal to a human decision maker was the only governance mechanism that raised an algorithmic decision's perceived legitimacy, including for adverse decisions (Martin and Waldman 2023).
- **Words:** +23

### C50 · S-261 · Conclusion

- **Why:** Annex III names no hospitality setting, but point 4(b) covers systems that allocate work, which reaches hotels as employers.
- **Source:** card eu2024aiact Annex III
- **Was:** but that requirement is owed to overseers, not guests, and the Act lists no hospitality use as high-risk.
- **Now:** but that requirement is owed to overseers, not guests, and the Act's list of high-risk areas names no hospitality setting, though its rule for systems that allocate work reaches hotel staff (Annex III, point 4(b)).
- **Words:** +17

### C51 · S-265 · Conclusion

- **Why:** Some statutes are United Kingdom or Great Britain law, and Crinkley applied North Carolina law.
- **Source:** Cases and Legislation lists; card crinkley1988holiday
- **Was:** First, its legal sources are English, United States federal and European Union law, with one decision of a United States federal appeals court, so
- **Now:** First, its legal sources are English, British, United States and European Union law, with one decision of a United States federal appeals court applying North Carolina law, so
- **Words:** +4

### C52 · S-274 · Conclusion

- **Why:** Batat 2022 (TLR) asks its well-being question of the luxury ecosystem, not of service systems; it is now attributed to its own field.
- **Source:** card batat2022tlr pp. 609, 618
- **Was:** (Anderson and Ostrom 2015; Batat 2022)
- **Now:** (Anderson and Ostrom 2015), and Batat (2022: 609) asks the same of the luxury ecosystem
- **Words:** +9

### C53 · S-276 · Conclusion

- **Why:** De Vos et al. studied students with disabilities in an online MBA, at abstract depth; it cannot carry a claim about communities.
- **Source:** card devos2024disabilities (abstract)
- **Was:** For communities the evidence suggests a range rather than a verdict, since the same digital mediation can enchant, disenchant or re-enchant a service encounter depending on the arrangements around it (De Vos et al. 2024), and whether the path from the guest to authority survives is one of those arrangements.
- **Now:** For communities we have no evidence to offer, only the expectation that whether the path from the guest to authority survives will be among the arrangements on which their well-being turns.
- **Words:** -19

### C54 · S-278 · Conclusion

- **Why:** 'Address' is Kong's term for the party answerable for an outcome.
- **Source:** card kong2026delegation p. 3
- **Was:** the obligation of hosting still has an address, and whether the guest can reach it.
- **Now:** the obligation of hosting still has an address (Kong 2026: 3), and whether the guest can reach it.
- **Words:** +3

## Also changed

- **Bibliography.** Darwall (2013) gains its place (Oxford; Crossref gives none, so the publisher's seat is used) and Baum and Laux (2026) theirs (Cham, from Crossref), which removes the stray ', :' from both entries. Ivanov and Webster's article number is now rendered.
- **Card.** `kaniadakis2022responsibilisation` records the open journal version and the page of the quotation.
- **Reviewer letter.** It now says that two questions remain in the body, not one; it gives the longest sentence (64 words) instead of 'about fifty'; it says the abstract names the test and its scope; and it carries bracketed notes to the authors on the three bare uses of 'framework' and on the evidence paragraph, which was untrue of the 10 Nov text.
- **Editor note.** Body and reference counts updated.

## Not changed, and why

**VERIFY: the cards cannot settle these.** Read the source, then keep, correct or cut.
- Cheng et al. 2025 and Morrison 2014: abstract only; the silence sentence in 'Three conditions and six questions'.
- Calo and Rosenblat 2017: abstract only; it is now cited only for an asymmetry its abstract states.
- Batat and Hammedi 2023: the 'queues, repetition, uncertainty and wasted effort' list is not on the full-text card.
- Batat 2026, as read by Shabnam et al.: read the PSR article itself.
- Lynch et al. 2011: five attributions are not on its card, including Aramberri and the micro- and macro-hosts. The bibliography's note places micro- and macro-hosts in Lynch 2017, which is held at metadata only.
- Bulley 2015: 'assembled host' is in the saved manuscript but not on the card; it needs the printed page.
- Weaver 2026: 'traced … to large corporations' is not on the card.
- Sandoval-Strausz 2005: 65, and whether it concerns goods or persons.
- Scott and Orlikowski 2012: 'whoever designs, configures' is not on the card.
- AI Act, Annex III 1(a), on check-in biometrics.

**The authors' decisions: changes of argument, not of fact** (`SYNTHESIS.md`, sections 4 and 6).
- **The step from duty to a hearing.**
- **The opening of 'The host's power and the host's obligation', fourth paragraph** ('turns on the host's motive'). Blain and Lashley, as now described, and Lashley (2015: 4) both state a host's duty.
- **Woodland and the adult guest.** Meeting Kong's ground (p. 4).
- **'Real-time' accountability against Bovens.**
- **Lugosi 2009 as support for requests reaching authority.**
- **The Conclusion's sentence on an arrangement that 'harms no one'.**
- **The scope of the role account:** restaurants, and placed or non-paying guests (Petie et al.).
