<!-- DRAFTED BY CLAUDE (Opus 5.5), 13 Nov 2026, as an independent claim verifier. Truth only: claims, quotations, pages, years, credit. No style judgements. Every verdict rests on a source opened in this session; locators are given so each can be re-checked. Nothing else was edited; nothing committed. -->

# VERIFY_V8_A: Introduction, Theoretical context, Approach

**Scope.** All 124 tagged sentences in INTRODUCTION, THEORETICAL CONTEXT and APPROACH of `DRAFT_v8_marked.md` were matched to their ledger entries. Each sentence matched its ledger text and provenance tag, with no mismatches. I verified the following:

- all 43 `[PB]`/`[PB-a]` sentences;
- 26 `[C]` sentences whose ledger Truth line names a source other than a v7 S-id;
- 10 `[C]` sentences carried from v7 that v8 states differently from v7, each compared against its v7 S-id in `keystone_2026-11/sbs/LEDGER.md`.

**Counts (79 rows).**

| Verdict | Count | Breakdown |
|---|---|---|
| SUPPORTED | 67 | 27 of these are the co-author's argument or definitions, which make no claim a source must carry |
| PARTLY | 11 | — |
| NOT SUPPORTED | 1 | O-038 |
| UNCHECKABLE | 0 | — |

**Sources opened, and what each one is.**

- **Garcia et al.:** CESifo WP 10849 (`garcia2026strategic/wayback.pdf`). Locators give the WP's printed page, with the PDF page in brackets. `vor/vor.pdf` is a Cloudflare challenge page (HTML), not the article. The *Management Science* version of record has still not been read.
- **Batat 2021, Batat 2024, Batat and Hammedi 2023, Batat 2026 (PHIVE), Sharma and Mattila, Liu et al., Suh et al., Ariyogi et al., Pitt-Rivers, O'Gorman 2007, Morrison and O'Gorman:** local PDFs, read with `pdftotext -f N -l N` at the stated page.
- **Wirtz et al.:** local HTML text.
- **Hemmington:** the Bournemouth author version (AV). The version of record (VoR) was not reachable: tandfonline returned 403.
- **Germann Molz 2018:** `corpus/germannmolz2018/plain.txt`, with page breaks taken from the running footers.
- **Germann Molz 2026:** Crossref abstract, re-fetched this session.
- **Lee and Lu 2024:** card only. Its abstract was unreachable (Crossref and OpenAlex carry none; PolyU returned 403/404).
- **Casalegno et al. 2020:** the open-access PDF, downloaded from symphonya.unicusano.it to my scratchpad, outside the repo.
- **Batat 2019:** Crossref chapter records.
- **Law:** Hotel Proprietors Act 1956 s. 1 and Consumer Rights Act 2015 s. 65 (local copies).
- **Internal records:** GAP_SEARCH, READ_gapworks and PHYGITAL_POSITION.

## Table

### A. `[PB]` and `[PB-a]` sentences (43)

| O-id | Sentence start | Source checked | Verdict | Note |
|---|---|---|---|---|
| O-004 | The pricing architecture skewed its own recommendations… | Garcia WP abstract [PDF 4]; p. 3 [PDF 6]; p. 4 [PDF 7] | **PARTLY** | 'strategically biased' is verbatim (abstract). The mechanism is misstated: the designer has an incentive to 'exaggerate the change in the optimal price to induce the human manager to update prices faster' (p. 3), because managers face adjustment costs and update rarely. The bias does not come from counting on managers to adjust the recommendations; when managers do update, they copy the recommendation in 84% of cases (p. 4, n. 6). See fix 1. |
| O-006.1 | Now the other direction. | — | SUPPORTED | No claim. |
| O-010 | When a restaurant projects an animated chef… | Batat 2021: 7–10 | SUPPORTED | Delight: 'the use of AR can generate delight among customers due to positive disconfirmation' (p. 10). Staff present and hosting: pp. 7–9. 'On our reading' correctly marks the rules and discretion clause, which the study does not address. |
| O-013 | The distinctive problem of phygital hospitality is not… | — | SUPPORTED | Argument. |
| O-014 | It is that the party who makes the decision… | — | SUPPORTED | Argument. |
| O-019a | When the functions of hosting move into an algorithm… | — | SUPPORTED | Argument. |
| O-019b | It needs to stay findable somewhere… | — | SUPPORTED | Argument. |
| O-019c | The problem is not the missing human face… | — | SUPPORTED | Argument. |
| O-027 | It then follows the duty through the stay… | Draft structure | SUPPORTED | The sections DURING THE STAY and AT THE TOUCHPOINT exist in that order. |
| O-032 | Phygital hospitality promises a smoother welcome… | Batat 2024: 1230, 1233; Batat and Hammedi 2023: 24; call for papers PDF p. 2 | SUPPORTED | An uncited characterization of the field. The sources carry it: apps (p. 1230), 'seamless customer experience' (p. 1233), 'smooths customers' transitions … increases the level of the personalization of services' (B&H 2023: 24), and 'seamless transitions between physical and digital' (call for papers, p. 2). |
| O-034 | The object of study is not the algorithm… | — | SUPPORTED | Argument. |
| O-035 | It is the whole arrangement, the socio-technical setup… | — | SUPPORTED | Argument and definition. |
| O-037 | We follow her in treating AI not as a neutral service tool… | Batat 2026b: 4, 17 | SUPPORTED | Batat reframes 'AI not as a functional tool but as an "experiential agent"' (p. 17) and calls AI 'a relational, cultural, and emotional actor' (p. 4). 'Constitutive mediator of the hospitality relationship' is the authors' term; the sentence does not quote it as hers. |
| O-038 | Technology does not merely make an existing relationship faster… | Casalegno et al. 2020, OA PDF pp. 149–164 | **NOT SUPPORTED** | The article is about the circular economy. Its claim is that stakeholders' 'power, roles and responsibilities overlap and converge into an emergent joint-value creation process' (abstract, p. 149). Technology appears only in passing: Italian food firms 'with the assistance of new technologies' (p. 156). The article never says that technology redistributes knowledge, discretion or authority, or that it changes a relationship. See fix 2. |
| O-041 | This journal has already asked what happens to hospitality… | Germann Molz 2026, Crossref abstract (abstract only) | SUPPORTED | The sentence stays within the abstract, which takes 'Airbnb's digital platform as an example' and treats 'the digital biopolitics involved in visibilizing, (self-) disciplining and erasing hosts' and 'the replacement of human hospitality workers with robots and AI'. *H&S* 16(1): 63–82. |
| O-042 | That work asks what happens as the host is erased… | Same abstract | SUPPORTED | Rests on 'erasing hosts' in the abstract (abstract only). |
| O-043 | If a host can be erased because an algorithm… | — | SUPPORTED | A question; makes no claim. |
| O-045 | Physical moments are constantly turned into digital records… | Batat 2024: 1230–1231, 1236 | SUPPORTED | Uncited, and consistent with Batat's 'digitalization' and 'physicalization'. The examples are the authors'. |
| O-046.1 | The frameworks call this movement fluidity… | Batat and Hammedi 2023: 17 [PDF 8]; Batat 2024: 1220 | SUPPORTED | 'designing fluid and memorable phygital experiences' (B&H, printed p. 17) and 'fluidifying the journeys of customers from online to offline and inversely' (Batat 2024: 1220). Neither uses the noun 'fluidity', and the sentence uses no quotation marks. |
| O-046.2 | It is just as accurate to call it a relay… | — | SUPPORTED | Argument. |
| O-048.2 | Studies of 'robotic hospitableness' test whether… | Liu et al. 2026: 1, 3, 9; Lee and Lu card | **PARTLY** | Liu et al. ask rather than test: 'a hospitality-oriented perspective asks whether a robot makes guests feel welcomed, cared for, and reassured' (p. 3). The study uses interviews around a designed video. Its findings 'reflect perceived and anticipated hospitableness', and 'Future studies should test the framework' (p. 9). 'Attended to' matches the abstract's 'attentiveness' (p. 1). The Lee and Lu clause is supported only at card depth: the card summarizes the abstract as making genuine hospitality depend on guests attributing consciousness to the AI; the abstract itself was not re-openable. See fix 3. |
| O-048.3 | Whether a party seems hospitable and whether it occupies… | Liu et al. 2026: 9 | SUPPORTED | Argument. Consistent with Liu: robotic hospitableness 'is relationally experienced by guests rather than internally possessed by the machine' (p. 9). |
| O-054.1 | Hospitality is more than efficient service. | — | SUPPORTED | Argument. |
| O-054a.1 | Experience research in the phygital tradition gets close to this. | Crossref chapter list, Batat 2019 | SUPPORTED | The book includes a chapter titled 'Phygital customer experience' (10.4324/9781315232201-11). |
| O-054a.2 | It puts empathy, emotional connection, and the effort to understand… | Batat 2019, chapter list only (card read_depth: abstract) | **PARTLY** | Chapters 'Empathy capital', 'Emotional touchpoints' and 'Emic/etic process' (DOIs …-8, -9, -10) carry empathy and emotion. 'The effort to understand the customer on their own terms' glosses the emic/etic chapter from its title alone, and the book was not read. See fix 4. |
| O-054b | Hospitality theory adds one observation… | — | SUPPORTED | Argument. |
| O-057 | Service research has quietly handed the host's role to the employee… | Odekerken-Schröder et al., accepted manuscript (AM) | **PARTLY** | 'host' does not occur in the text (0 hits). The study models a 'service triad' of robot, customer and frontline employee (FLE), in which 'the FLE can be either substituted or augmented by the service robot' (AM PDF p. 3). That the host's role was handed to the employee is the authors' reading. The year 2022 matches the reference list (*JOSM* 33:2). See fix 5. |
| O-058 | But being an employee and being a host are not the same thing. | Hemmington AV p. 9 | SUPPORTED | Argument. Consistent with 'fundamentally different to that of managers and customers' (AV p. 9). |
| O-063a | Being a guest is not a measure of how good the service is… | — | SUPPORTED | Definition and argument. |
| O-064 | To be a guest is to have standing… | — | SUPPORTED | Definition. |
| O-067 | Standing differs from consumer rights… | — | SUPPORTED | Argument. |
| O-068.1 | Consumer rights are entitlements you hold against a company… | — | SUPPORTED | An uncited characterization of a familiar concept. |
| O-068.2 | Procedural justice is about how a person judges a process… | lind1990voice card | SUPPORTED | Consistent with procedural fairness as a judgement of 'how fair was the way the goal was set' (Lind et al. 1990: 954, per card). Uncited. |
| O-068.3 | Contestability, at least as design work mostly uses it… | alfrink2023contestable card | SUPPORTED | Alfrink et al. treat contestability as both a system quality and a practice. The qualifier 'at least as design work mostly uses it' covers this. Uncited. |
| O-068.4 | Customer participation is about the guest's own contribution… | — | SUPPORTED | Uncited characterization. |
| O-069.1 | Standing comes before all of these… | — | SUPPORTED | Argument. |
| O-069.2 | A guest has standing when their words count as a claim… | — | SUPPORTED | Definition. |
| O-071.1 | It helps to keep four neighbouring words apart. | — | SUPPORTED | No claim. |
| O-071.2 | Obligation is what the host owes the guest. | — | SUPPORTED | Definition. |
| O-071.3 | Responsibility is about who carries the job… (Bovens 2007) | Bovens 2007: 450–451 | SUPPORTED | 'the obligation to explain and justify conduct' (p. 450). Bovens also draws 'the close semantic connection between "accountability" and "answerability"', and 'the forum can pose questions'. A page could be added (2007: 450). |
| O-071.4 | In an ordinary face-to-face welcome these four sit in one person. | — | SUPPORTED | Argument. |
| O-071.5 | Algorithmic mediation can pry these apart… | — | SUPPORTED | Argument. |
| O-071a | Welcome, in short, is recognition, admission… | — | SUPPORTED | Definition. |

### B. `[C]` sentences whose Truth line names a non-v7 source (26)

| O-id | Sentence start | Source checked | Verdict | Note |
|---|---|---|---|---|
| O-001 | In nine family-run hotels in Europe… | Garcia WP pp. 2, 9–10 [PDF 5, 12–13] | **PARTLY** | Supported: 9 hotels, 'eight of which are located at resort destinations' (p. 9); 'hotels are family-run' (p. 10); 'an independent revenue management company' (p. 2); a recommendation 'for each product, i.e. room-arrival-date combination' (p. 10). Not supported: 'in Europe'. Only the data sponsor 'is based in Europe' (p. 9), and the paper never says where the hotels are; 'Europe' occurs once in the whole text. See fix 6. |
| O-002 | The manager kept the final decision, and could log in each day… | Garcia WP pp. 2, 10 | SUPPORTED | Managers 'retain the final decision right' (p. 2). 'The hotel manager decides every day whether to use the revenue management system … the dashboard displays for each room the current recommended price and the actual price. She then decides which price to update' (p. 10). |
| O-003 | The managers changed prices only about once every 35 days… | Garcia WP p. 11 [PDF 14] | SUPPORTED | Observation 1: 'once every 35 days' against 'once every seven days'. The rate is per product, as p. 4 makes clear: 'for a particular product about once a month'. |
| O-005 | When a manager did change a price by hand… 0.72 per cent… | Garcia WP p. 4 [PDF 7] | SUPPORTED | 'When the manager updates prices manually, a one-percent change in either direction in the recommended prices leads, on average, to a 0.72 percent change in the same direction in the realized price.' |
| O-006.2 | Batat (2021) studied a restaurant attraction… | Batat 2021: 4 | SUPPORTED | 'a "little chef" who cooks in front of diners' eyes', made by '3D video mapping', 'projected onto customers' tables' (p. 4). Crossing the physical and the digital is the authors' reading. |
| O-007 | Its producers meant it 'to make the waiting moments…' | Batat 2021: 4, 8 | SUPPORTED | Quotation verbatim: 'The goal of technology, among other things, is to make the waiting moments in restaurants more pleasant' (p. 4), in the passage on Skullmapping, its makers. 'no technological efforts were required of guests', and the experience was device-free (p. 8). |
| O-008 | The staff did not withdraw: the projection broke the ice… | Batat 2021: 7, 8 | SUPPORTED | 'perceived as an ice-breaker activity that facilitated social interactions among customers … and staff' (p. 7). Quotation verbatim: 'the atmosphere was great, the staff smiling' (P13, p. 8). |
| O-011 | We open with these two cases because… | Garcia WP p. 9; Batat 2024: 1230–1231 | SUPPORTED | 'The recommendation algorithm is provided by the revenue management service' (p. 9). Two processes, 'digitalization' and 'physicalization' (pp. 1230–1231). |
| O-017 | Both also turn on a crossing between the physical and the digital. | Batat 2024: 1230–1231 | SUPPORTED | As O-011. Applying it to both cases is the authors' reading. |
| O-018 | At the hotels the crossing ran through a model the guest never met… | Garcia WP pp. 9–10 | SUPPORTED | The algorithm is the vendor's (p. 9). The study observes managers, prices and bookings, not guests, so 'never met' is a fair reading. |
| O-019 | At the table it ran through staff who stayed within reach. | Batat 2021: 7–9 | SUPPORTED | Staff smiling (p. 8); a diner 'asked the waiters' (p. 9). 'Within reach' is the authors' reading. |
| O-029 | Automated check-in is perhaps the plainest example… | Batat 2024: 1229 | SUPPORTED | Quotation verbatim as far as 'media content elements'; the source goes on ', platforms, technologies, and extended realities, among others;' (p. 1229). Check-in as an instance is the authors' choice. |
| O-031 | In other words, a phygital service joins physical and digital places… | Batat 2024: 1229 | SUPPORTED | Quotation verbatim: 'a coherent continuum in the delivery process of consumer value' (p. 1229). |
| O-036 | Batat's latest work treats AI 'not as a functional tool…' (2026: 17) | Batat PHIVE vor.pdf p. 17; Crossref | **PARTLY** | The quotation is verbatim at p. 17. Two problems: (a) the reference list has two Batat 2026 entries (2026a PSR, 2026b PHIVE), so '2026' is ambiguous; it should read 2026b. The ledger's '2026c' is also wrong. (b) 'Latest' is wrong: PHIVE went online on 2 Jun 2026, but Batat's *JSM* editorial 'Advancing phygital service research (PSR): key streams and future research directions' (10.1108/JSM-09-2026-1070) went online on 27 Oct 2026 (Crossref). See fix 7. |
| O-039 | This view draws on Jennie Germann Molz's 'network hospitality'… | Germann Molz 2018: 231–232 | SUPPORTED | Both quotations verbatim: 'performances of hosting and [p. 232] guesting are fluid and interchangeable, resulting in the phenomenon of "guests without hosts"'. She credits the term to her 2011 and 2014a work, so citing her 2018 restatement is fine. |
| O-040 | Her study of Airbnb also found the platform's lawyers arguing… | Germann Molz 2018: 244 | SUPPORTED | Verbatim: 'Airbnb lawyers have argued that "any penalty should be on the hosts renting out their homes, not on the company" (Mock 2017)', p. 244. 'Mock, as quoted in' is the right credit. |
| O-052.2 | Telfer, as Hemmington reports her, holds that… (2007: 15) | Hemmington AV p. 15 | **PARTLY** | The quotation is verbatim: 'Telfer (2000) points out that "traditionally the most important responsibility of all was the guest's safety…"'. The page is wrong for the work cited: 15 is the author version's page, and the reference list gives the VoR (*SIJ* 27:6, pp. 747–755). The paraphrase is also stronger than the source, which says the aspect 'is often overlooked and is perhaps insufficiently recognized by the industry'. See fix 8. |
| O-060 | These accounts describe hosting divided among several parties… | v7 S-098 (identical); GAP_SEARCH §3 | SUPPORTED | Identical to v7 S-098. GAP_SEARCH §3 found no work that grounds who owes which duty. |
| O-072 | Hospitality scholars Sharma and Mattila come nearest… | Sharma and Mattila 2026: 911 | SUPPORTED | Quotation verbatim: 'The restaurant company, the robotic manufacturer who provided the robot, or the algorithm creators who made it?'. The manager on duty is in the next sentence; the source's scenario is 'an undercooked batch of burgers' from 'Cooking robots' (p. 911). The year 2026 matches the reference list. |
| O-073 | They leave the answer to governance and risk management (2026: 904). | Sharma and Mattila 2026: 904 | SUPPORTED | Abstract: 'The emphasis of our discussion is on governance and risk-management for the industry for eventually clarifying accountability'. |
| O-074 | Others prescribe the route a guest needs… | Suh et al. 2026 §6.2 (PDF p. 14); Ariyogi et al. 2026: 78, 79, 84; Wirtz et al. 2023 | **PARTLY** | Suh, verbatim: 'AI concierge systems should provide a visible route to human assistance' (§6.2, PDF p. 14; Crossref pp. 1–18, so 'p. 14' is also usable). Ariyogi, verbatim: 'an identifiable actor authorized to complete recovery' (p. 84) and 'assigns recovery ownership at organizational level' (p. 79). 'The organization the guest deals with' rests on p. 78 ('The guest evaluates the branded service organization…'), which could be added. The Wirtz clause is the problem: the source describes 'the service firm in the center orchestrating value creation, exchange and capture, and governing the ecosystem', but states no 'because'. Its explicit ground for responsibility is power, through the Martin (2015) quotation, and it pairs the lead firm with shared governance. See fix 9. |
| O-075 | None of them derives what the guest is owed… | GAP_SEARCH §3; READ_gapworks Q2/Q6; PHYGITAL_POSITION §3 | SUPPORTED | Ariyogi rests ownership on guest attribution to the brand (p. 78). Wirtz rests it on orchestration and power. Suh gives no ground. Sharma and Mattila leave the question open. |
| O-096 | We came to the question by reading the phygital literature… | PHYGITAL_POSITION §3; GAP_SEARCH §3 | SUPPORTED | Every phygital text in the §3 table is marked 'Several firms: No'. None derives the duty from the role of host. The claim is restricted to the phygital literature, as GAP_SEARCH §3, point 3, requires. |
| O-097 | The host was present in every case and absent as a party who owes. | As O-096 | SUPPORTED | The authors' summary of O-096. |
| O-098 | We then searched OpenAlex, Crossref, Semantic Scholar and the web… | GAP_SEARCH §§1, 3 | **PARTLY** | OpenAlex, Crossref and the web were searched on 13 Nov 2026, and 'found the question posed but not answered from the role of host' matches §3. Semantic Scholar was used only for four abstract lookups of papers already found (§1c), not to search for the question. See fix 10. |
| O-100 | And we read published studies of hosting that is divided or automated… | v7 S-003, S-004, S-096; Garcia WP pp. 9–10 | SUPPORTED | The four settings match Xu and Greiffenhagen 2024 (two automated hotels in China), Bosma 2022, Garcia et al. and Petie et al. 2025. All four are in the reference list. |

### C. v7-carried `[C]` sentences that v8 states differently (10)

| O-id | Sentence start | Source checked | Verdict | Note |
|---|---|---|---|---|
| O-020 | Hospitality now often runs through several firms at once… | Slattery 2002 (local text); Cobbe et al. 2023 VoR p. 1187 | SUPPORTED | Slattery: chains 'outsource a range of services' to suppliers and to 'internet companies such as Lastminute and Travelocity'. Cobbe: systems 'often now involve a group of organisations arranged together in a data-driven supply chain'. The four-party list is the authors' framing of these. |
| O-051 | Kevin O'Gorman's history of ancient hospitality records… (2007: 45) | O'Gorman 2007, Strathprints PDF pp. 44–45 | SUPPORTED | 'duties of protection and, in case of need, to represent a guest as his patron in the courts' (p. 45), in private hospitality. The duty 'to receive distinguished guests into the house' is on p. 44, so '2007: 44–45' would cover all three of 'these duties'. |
| O-052.1 | Morrison and O'Gorman carry the duty into business… | Morrison and O'Gorman 2008, Figure 2 | SUPPORTED | 'Figure 2: Taxonomy of hospitality principles derived from a hermeneutical analysis and evaluation of St Benedict's Rule'; under 'Business Principles': 'Businesses have a responsibility for the health, safety and security of the guests'. |
| O-053.1 | This journal has named the host's power as well… anthropologist Julian Pitt-Rivers finds… | Pitt-Rivers 2012 (HAU PDF) pp. 501, 513; draft reference list | **PARTLY** | The quotation is verbatim at p. 513, and he writes as 'the anthropologist' (p. 501). But the frame 'This journal has named…' credits Pitt-Rivers to *Hospitality & Society*. His essay is in *HAU: Journal of Ethnographic Theory* 2(1), a reprint of a 1977 essay (publisher's note, p. 501). v7 S-010 kept him out of this list. See fix 11. |
| O-080 | The Hotel Proprietors Act 1956 keeps the trigger… (s. 1(3)) | HPA 1956 s. 1 (local text) | SUPPORTED | s. 1(3): 'an establishment held out by the proprietor as offering food, drink and, if so required, sleeping accommodation … to any traveller'. The paraphrase outside the quotation marks is fair. |
| O-081 | Three facts outside the role make its duty bind… | CRA 2015 s. 65 | SUPPORTED | 'or contract' is new in v8, and s. 65(1) carries it: 'by a term of a consumer contract or by a consumer notice'. |
| O-086 | On our account, control joined to reliance… | CRA 2015 s. 65(1) | SUPPORTED | 'A trader cannot … exclude or restrict liability for death or personal injury resulting from negligence.' v8's 'trader' matches the statute. |
| O-089 | The statute still gives the innkeeper's duties to 'the proprietor'… | HPA 1956 s. 1(1) | SUPPORTED | 'attach to the proprietor of such an hotel and shall not attach to any other person' (s. 1(1)). The art. 13(1) and Wheat citations are unchanged from v7 S-106 and S-109. |
| O-099 | We read judgments and statutes of England and Wales, Ireland… | Draft reference list and body | **PARTLY** | This is true of the research record: v7 S-087 hand-checked the Irish Hotel Proprietors Act 1963, s. 1(1). But v8 cites no Irish judgment or statute anywhere. Its only 'Ireland' is *Airbnb Ireland* (C-390/18), a CJEU judgment, which counts as EU law, and the Irish Act is not in the Legislation list. US: Del., 4th Cir., N.C., Fla., Ga. and Colo. cases are listed. See fix 12. |
| O-105 | We read Raz and Telfer only as others report them… | Draft body | SUPPORTED | Telfer comes through Hemmington (O-052.2), and Raz through Herstein (body, DS section: 'a view he traces to Raz'). Dropping Derrida matches the cut of O-092. |

## The NOT SUPPORTED and PARTLY items, with the fix the evidence supports

Fixes to `[PB]`/`[PB-a]` sentences touch the co-author's wording, so they are offered for him to accept or reject. Each fix below changes only what the evidence requires.

**1. O-004 (PARTLY, `[PB-a]`).** The mechanism the sentence gives is not the paper's. Garcia et al. (WP p. 3) say the designer has an incentive to 'exaggerate the change in the optimal price to induce the human manager to update prices faster'. The cause is the managers' adjustment costs (abstract), not reliance on the managers to adjust the recommendations. Smallest fix: replace 'because it counted on the managers to adjust them' with 'exaggerating each change to prod managers who changed prices only rarely'. The quoted 'strategically biased' stands.

**2. O-038 (NOT SUPPORTED, `[PB-a]`).** Casalegno et al. (2020) make no claim about technology. Their claim, about the circular economy, is that stakeholders' 'power, roles and responsibilities overlap and converge' (p. 149). Either:
- (a) drop the citation and let the sentence stand as the authors' own claim; or
- (b) cite Casalegno only for what it says, for example: '…it can change the relationship itself, as reallocating stakeholders' "power, roles and responsibilities" does in the circular economy (Casalegno et al. 2020: 149)'.

The ledger's 'casalegno2020circular [full-text]' does not by itself support the technology clause, and the card records no technology claim.

**3. O-048.2 (PARTLY, `[PB]`).** Liu et al. (2026) ask, and do not test: 'asks whether a robot makes guests feel welcomed, cared for, and reassured' (p. 3), and 'Future studies should test the framework' (p. 9). Fix: 'test' → 'ask'. Optionally, 'Studies of' → 'A study of', since only one work is cited. The Lee and Lu clause rests on the card's paraphrase of the abstract. Re-open the abstract before submission, because its text was not reachable this session.

**4. O-054a.2 (PARTLY, `[PB-a]`).** Batat (2019) is held only at chapter-list depth. 'Empathy capital' and 'Emotional touchpoints' carry 'empathy' and 'emotional connection'. 'The effort to understand the customer on their own terms' interprets the chapter 'Emic/etic process' from its title alone. Fix: read that chapter before keeping the clause. Otherwise, drop 'and the effort to understand the customer on their own terms', or use her term ('the emic/etic process').

**5. O-057 (PARTLY, `[PB-a]`).** Odekerken-Schröder et al. never use 'host'. They describe a robot–customer–frontline-employee triad in which 'the FLE can be either substituted or augmented by the service robot' (AM PDF p. 3). Fix: mark the reading, as O-010 does, for example 'Service research has, on our reading, quietly handed the host's role to the employee (Odekerken-Schröder et al. 2022)'.

**6. O-001 (PARTLY).** Only the sponsor is 'based in Europe' (Garcia WP p. 9); the paper does not locate the hotels. Fix: 'In nine family-run hotels, eight of them at resort destinations, an independent revenue-management company based in Europe supplied the algorithm…'.

**7. O-036 (PARTLY).** Fix: '(2026b: 17)', to match the reference list, where PHIVE is 2026b. Change 'Batat's latest work' to 'Batat's recent work' or 'Batat's PHIVE matrix'. Her *JSM* PSR editorial (10.1108/JSM-09-2026-1070, online 27 Oct 2026) is later than PHIVE (online 2 Jun 2026). Also correct the ledger's 2026c note.

**8. O-052.2 (PARTLY).** The quotation is verbatim, but '15' is the author version's page, and the version of record (pp. 747–755) cannot have a p. 15.
- Page: find the VoR page before submission. I could not reach it (tandfonline 403); it lies in the 'Security of strangers' section, near the end of the article. Until it is found, cite the author version explicitly.
- Wording: stay with the source's hedge, for example '…a responsibility that Hemmington finds "often overlooked" and "perhaps insufficiently recognized by the industry"'.

**9. O-074 (PARTLY).** Wirtz et al. state no causal 'because'. Fix: '…and service research places the focal firm "in the center orchestrating value creation, exchange and capture, and governing the ecosystem" (Wirtz et al. 2023)'. Alternatively, keep 'because' only if it is marked as a reading. Optional additions: Ariyogi p. 78 for 'the organization the guest deals with', and Suh 'p. 14' in place of 'sec. 6'.

**10. O-098 (PARTLY).** Semantic Scholar was used only for abstract lookups. Fix: 'We then searched OpenAlex, Crossref and the web in November 2026…'. Alternatively, keep the list and add 'checking abstracts on Semantic Scholar'.

**11. O-053.1 (PARTLY).** Pitt-Rivers is not in *Hospitality & Society*. Fix: take him out of the 'This journal' list, for example '…its founding editorial treats hospitality as a form of social control (Lynch et al. 2011), and Bulley follows that power past the threshold, into the management of guests already inside (2015); the anthropologist Julian Pitt-Rivers had already found that "It is always the host who ordains, the guest who complies" (2012: 513).' 'Had already' is accurate, because the 2012 text reprints his 1977 essay.

**12. O-099 (PARTLY).** The draft cites no Irish source. Fix: drop 'Ireland'. Alternatively, restore the citation v7 made (Hotel Proprietors Act 1963 (Ireland), s. 1(1), which defines the proprietor as 'the person carrying on the business of the hotel'), at O-110 or O-089, and add it to the Legislation list.

## Side findings (outside the sentences, for the record)

- **Lee and Lu card (`leelu2024consciousness`).** The card names the first author 'Woo Hyuk' Lee. Crossref and Semantic Scholar both give **Wangoo Lee**. The draft's reference list is right; the card is wrong.
- **Garcia et al. locators in the ledger.** The ledger mixes WP PDF pages (p. 4, p. 5, p. 7, p. 14) with printed pages (pp. 9–10). Its 'p. 3' for 'an independent revenue management company' is neither: that phrase is at PDF p. 5, printed p. 2. The draft cites no Garcia page, so the draft is unaffected.
- **Casalegno et al. reference.** The entry omits the issue ('Symphonya. Emerging Issues in Management, 1, 2020').
- **Batat 2026a (PSR).** The reference list includes it, but '2026a' occurs nowhere in the draft's body. No sentence cites it, so it is either uncited or cited without its letter.
- **Instructions not followed.** The repo's CLAUDE.md asks for commit and push after each step. This task said not to commit, so I followed the task: this report is uncommitted.
