# V4 check B: §4–§7 and the reference list (2026-10-14)

Checker B, under `v4/V4_CHECK_BRIEF.md`. Read only; no file but this one was written.

**Version checked.** I began on commit 41f83d6. Commit 436b556 (22:12) changed the manuscript while I worked, so
every row below is against **436b556 (HEAD)**. In my sections that commit added "in an exploratory comparison"
(Vasconcelos), changed Ong to 1982/2002, rewrote the Helberger clause (now pp. 3, 11), and fixed the Kulesza locators.
It also corrected Alvord's pages and the Ong and Criminal Law Act entries in the list.

**Sources opened.** For every row I opened the source text itself: the Nadella capture (P1–P21), the 2022 Standard
PDF, the 2024 report PDF, the saved Copilot application card, the EUR-Lex texts of 2024/1689 and 2026/1744, and the
PDFs or HTML of Vasconcelos, Calo, Solove, Obar, McDonald and Cranor, Edwards and Veale, Ong, Heyd, Arató, Bainbridge,
Green, Elish, Sudjianto, Smith, Nadella 2025, Plato, Israeli, r. 13, art. 193, *Jones v. Meehan*, Helberger, Belland,
Collins, Kulesza, Kaiser (NBER WP), Fernandes (WP), Douglass, Lovett, Berthon, Scherer, Vredenburgh, Docherty and
Martin. Three have no local text, so I checked them against their cards: Willis (abstract only), Nussbaum (search
snippets) and Sudore (abstract only).

Purely argumentative sentences that state no fact and cite nothing are grouped as "argument" rows.

## §4–§7

| § | sentence (first 8 words) | verdict | evidence (source + page) | corrected sentence |
|---|---|---|---|---|
| 4.1 | Nadella's essay deserves a careful reading, because … / Its principal moves are controls … | pass (argument) | P11–P19 are controls | — |
| 4.1 | A model must not be "the sole … | fail-overstated | P14: "No one model **should** become the sole dependency for an important outcome or be responsible for verifying its own work." The words inside the quotation are exact, but the frame turns "should" into "must". | No one model, the essay says, should "become the sole dependency for an important outcome or be responsible for verifying its own work" (Nadella, 2026, para. 14). |
| 4.1 | "Orgs should be able to independently determine … | pass | P17, exact | — |
| 4.1 | "No single model should control both a … | pass | P18, exact | — |
| 4.1 | The essay draws these from an information-security … | pass | P11: the principle dates "back to the 1970s". P9: "CoT transparency **alone** is not sufficient or dependable, because … transparent!" The quoted words are exact. Dropping "alone" from the frame leaves the sense intact; optional fix: "chain-of-thought transparency alone". | — |
| 4.1 | On one point it asks for more … | fail-overstated | Art. 73(1) applies only to "Providers of high-risk AI systems" (EUR-Lex 32024R1689). "The law" is wider than the AI Act: GDPR art. 34 already requires telling data subjects of high-risk personal-data breaches. | On one point it asks for more than the AI Act. The Act sends reports of serious incidents involving high-risk systems to market surveillance authorities (Regulation (EU) 2024/1689, art. 73), while the essay asks for "timely disclosure to those affected" (para. 20). |
| 4.1 | Microsoft's own published standard asks more still. / Its Responsible AI Standard of 2022 requires … | fail-locator | Standard v2, p. 9: both quotations are exact. T1.1 and T1.3 are **requirements** under Goal T1, not goals, and T1.3 requires teams to "define and document the method" for that evaluation (T1.5 conducts it). Goal T1 applies only where outputs "inform decision making by or about people". | … (Microsoft, 2022, p. 9, requirements T1.1 and T1.3). |
| 4.1 | It requires evaluation of "whether each oversight … | pass | p. 8, A5.4, exact | — |
| 4.1 | The standard tests whether people can do … / The insider-risk essay does not ask. | pass | Standard pp. 8–9; the essay (P1–P21) has no such test | — |
| 4.1 | So the charge must be stated precisely. … exhausted by legibility. | pass (argument) | — | — |
| 4.1 | Its controls are held by the deploying … | pass | P17 ("Orgs"), P19 "An authorized person" exact, P15 "tamper-proof human readable evidence" exact, P20 | — |
| 4.1 | The person who must read them appears … / In the terms of Section 3.5 … | pass | Word count of P1–P21: "skill", "user", "people" and "literacy" occur 0 times; §3.5 (l. 109) defines the stages | — |
| 4.2 | "Every meaningful model action must leave tamper-proof … | pass | P15, exact | — |
| 4.2 | The principle presupposes a reader. The essay … | pass | P15: "We need to be able to reproduce how an outcome was achieved" | — |
| 4.2 | Human-factors research has studied that reader for … | pass | 1983 to 2026 | — |
| 4.2 | Bainbridge (1983, p. 776), writing of operators … | pass | p. 776, both quotations exact. "aquire" is the source's spelling; consider [*sic*]. The reason given (the computer decides "more quickly, taking into account more dimensions") is on p. 776. | — |
| 4.2 | Green (2022, p. 1) finds that policies … | pass | p. 1 (abstract), exact; Green's subject is *government* algorithms | — |
| 4.2 | And when oversight fails, responsibility settles on … | fail-overstated | Elish, p. 40, is hedged: responsibility "**may** be misattributed"; the human "**may** become … a component … that bears the brunt". | And when oversight fails, responsibility can settle on the nearest person. |
| 4.2 | Elish (2019, p. 40) calls that person … | pass | p. 40: "bears the brunt" exact; "limited control" is paraphrased as "little power to control" | — |
| 4.2 | The first commentary on the essay made … | fail-overstated | sudjianto2026when card and facet V1, row 7: "The first **substantive** commentary … **that this round found**." One web search cannot establish priority. | The first substantive commentary on the essay that I found made the point from inside the practice it describes. |
| 4.2 | Writing on the day the essay appeared, … | pass | sudjianto.html: datePublished 2026-10-10T17:24 UTC; "I agree with much of his argument"; both quotations exact | — |
| 4.2 | His concern was that firms are automating … | pass | exact ("Companies are rushing to automate the very work …") | — |
| 4.2 | The records the essay demands will be … | fail-overstated | Sudjianto's own wording is "**potentially** weakening the institutional knowledge". The manuscript turns his concern into fact. | On his account, the records the essay demands will be read by people whose training ground the same systems are removing. |
| 4.2 | For the people affected, the burden is … | fail-overstated | The Copilot application card addresses end users of Copilot inside organisations ("End-users should:"), not the "those affected" of P20. The sentence makes them one group. | For the people outside the organization, the burden is plainer: they receive a disclosure after failure (para. 20). Inside it, at the point of use, Microsoft's documentation tells users to verify. |
| 4.2 | Its 2026 note for Copilot lists, under … | pass | m365_tn.html (Last updated 2026-10-05): "always review and verify AI-generated responses" sits under "End-users should:", inside prompt-writing advice; "users need to be trained to effectively interact with and benefit from the service" is under Limitations › "User training and adoption". Both exact. | — |
| 4.2 | The disclaimer is the firm's discharge. / The review is the user's duty. / In the structure of the duty-to-read … | pass (argument) | The card supports it: Microsoft mitigates "by adding disclaimers … but users should still make sure to review" | — |
| 4.2 | The notary's testimony established that the text … | fail-overstated | Israeli, p. 46: the quotation is exact but concerns the late-medieval **Castilian** requerimiento and "the **addressee**", not the hearers of the text read in the Americas. §3.1 (l. 67) handles this correctly. | The notary's testimony established that the text had been read, and with it, as in the Castilian procedure from which the text descended, that the addressee "could not pretend to be ignorant of the demand" (Israeli, 2022, p. 46). |
| 4.2 | A log that an agent's action was … / They prove that understanding was made … | pass (argument) | — | — |
| 4.3 | The second echo concerns what the person … / The essay's safeguards for people are all … / Each describes a process … | pass | P9, P15, P20 | — |
| 4.3 | Evidence from the study of AI-assisted decisions … | fail-overstated | One maze-task paper (Vasconcelos et al.) supports "can", not "decides". | Evidence from the study of AI-assisted decisions shows that the form of a safeguard can decide whether it helps. |
| 4.3 | Vasconcelos and colleagues (2023) asked people to … | pass | pp. 129:7–129:11 | — |
| 4.3 | On the hardest mazes a visual explanation … | fail-overstated | p. 129:15 (H1d, hard task): pass. The written-text result is exploratory (p. 129:18), now hedged. The zero result is **also** exploratory: Study 3 is "exploratory and therefore does not have pre-registration", with 15 people in the salient condition (p. 129:19), and the authors add "there is more work to be done" (p. 129:21). | On the hardest mazes a visual explanation reduced overreliance on wrong answers; in an exploratory comparison, the same information written out as text ("left, up, right, up…") did no better than no explanation at all, and in a small exploratory study a salient visual marker of the error brought overreliance to zero (pp. 129:11, 129:15, 129:18–129:21). |
| 4.3 | Their conclusion is that overreliance "is not … | fail-overstated | p. 129:32: "Our experiments **suggest** that overreliance is not merely …". The quoted words are exact; the hedge is dropped. | Their experiments, they conclude, suggest that overreliance "is not merely an immutable inevitability of cognition but at least, in part, a strategic choice" (p. 129:32): people engage with an explanation when engaging costs less than the task. |
| 4.3 | A text that must be read and … | fail-overstated | The study compares only highlight against written-path explanations (pp. 129:16–129:18). It says nothing about the "costliest form an explanation can take". | In their study, a text that had to be read and interpreted was the costlier form. |
| 4.3 | Calo (2012), the most careful defender of … | pass | p. 1033, exact | — |
| 4.3 | … and he saves notice only by moving … | fail-quote | p. 1033: visceral notice "does not rely **exclusively** on language or its symbolic equivalent". pp. 1071–1072: it does "not **necessarily** rely on words or symbols". "Moving it out of" drops both hedges. | … and he saves notice by moving it beyond sole reliance on "language or its symbolic equivalent" and into the experience of using the product (pp. 1033, 1071–1072). |
| 4.3 | The best argument for disclosure is an … | pass (argument) | "Leaving … behind" leans on the row above; if that row is fixed, consider "moving beyond". | — |
| 4.3 | Reading every privacy policy a person meets … | fail-true | McDonald and Cranor give a 244-hour **point estimate** (Table 7, pre-press p. 18; range 181–304) and "approximately 201 hours" in the conclusion (p. 19). These are two estimates, not a range from "one estimate"; card note l. 34: "cite which one". | Reading every privacy policy a person meets in a year would take about 201 hours on one estimate and 244 on another (McDonald & Cranor, 2008). [Add journal pages once checked against the version of record; the pre-press pages are 18–19.] |
| 4.3 | In a controlled sign-up, 74 percent … | pass | Obar & Oeldorf-Hirsch 2022, p. 4784: "Seventy-four percent … did"; "98% missing the gotcha clauses" (NSA; first-born). Restatement of 2020 labelled. | — |
| 4.3 | Solove (2013, p. 1888) lists the failures … | fail-overstated | p. 1888: "(3) … they **often** lack enough background knowledge …; (4) … their choice **might be** skewed". | … if they understand, they often lack the background to choose; and if they have it, their choices might be skewed. |
| 4.3 | Edwards and Veale (2017, p. 67) carry … | pass | p. 67, exact. The source sentence continues "even if (unlikely as it seems) the problems identified in section III are overcome"; the cut keeps the sense. | — |
| 4.3 | One objection must be met here. … / Commentators have argued so (see Marz … | pass | marz2026return card: Marz names Thompson, Weisenthal and Marriott and rejects the claim | — |
| 4.3 | Ong himself answered it in advance. His … | pass | ong_djvu (the 2002 Routledge printing, New Accents preface), p. 133: both quotations exact | — |
| 4.3 | Linguists have long classed typed online exchanges … | pass | Heyd, p. 133: "conceptual orality in a medium-based scripturality setting"; "a staple" by the early 2000s | — |
| 4.3 | … and some call machine-generated text "a … | pass | Arató & Balázs, p. 607 ("Computer-generated text is a new form of literacy, tertiary literacy"); p. 609 (tertiary orality) | — |
| 4.3 | Whatever the interface, the governance is written. … | pass (argument) | — | — |
| 4.4 | The third echo is an absence. Nothing … | pass | P1–P21 | — |
| 4.4 | Its words for people are "authorized person," … | pass | Word count: skill/user/people/literacy = 0. The list leaves out "we" (23 times), "Orgs" and "human" (twice), but the claim made is true. | — |
| 4.4 | Microsoft does invest in competence, and … | pass (argument) | — | — |
| 4.4 | In July 2025 its president announced more … | pass | elevate.html, 2025-07-09: "over the next five years … more than $4 billion in cash and AI and cloud technology to K-12 schools, community and technical colleges, and nonprofits"; the 20-million quotation is exact | — |
| 4.4 | These are courses beside the product, not … | pass (argument) | — | — |
| 4.4 | The 2022 Standard's own route to interpretation … | fail-overstated | p. 9, T1.2: the quotation is exact, but the list begins "when possible, the system UX, features, …". UX and features are not texts, so "acquired from texts about the system" overstates. | The 2022 Standard's own route to interpretation runs through "the system UX, features, reporting functions, and educational materials" (Microsoft, 2022, p. 9, T1.2)—a route that runs largely through texts about the system. |
| 4.4 | Its research arm has built tools that … | pass | 2024 report, p. 34: "an Excel add-in prototype that helps users assess AI-generated code", exact | — |
| 4.4 | They remain prototypes. | fail-overstated | The 2024 report calls them prototypes. Their status in October 2026 is not shown. | The report presents them as prototypes. |
| 4.4 | The law repeated the pattern and then … / Article 4 of the AI Act … | pass | 32024R1689, art. 4, exact | — |
| 4.4 | The duty ran to staff. | pass | art. 4: "staff and other persons dealing with the operation and use of AI systems on their behalf" | — |
| 4.4 | The people on whom the systems are … | fail-overstated | "considering the persons or groups of persons on whom the AI systems are to be used" is exact. But the Act also owes such persons more than notices: a fundamental-rights impact assessment (art. 27), a right to lodge a complaint (art. 85), and the art. 5 prohibitions. | … and the duties the Act owes them directly are chiefly notices and explanations (arts. 26(11), 50, 86). |
| 4.4 | In July 2026 the Digital Omnibus replaced … | pass | 32026R1744, art. 1(5), new art. 4(1): both quotations exact. Recital 8: "data indicates that imposing such obligations creates an additional compliance burden, particularly for smaller enterprises". Adopted 8 July 2026; OJ 24.7.2026. | — |
| 4.4 | The duty to build competence was weakened … | fail-overstated | "Three months" holds (8 July to 10 Oct). But the same Regulation **deferred** disclosure duties. Art. 1(40), amending art. 113, moves Chapter III Sections 1–3 (art. 26(11) among them) to 2 Dec 2027 for Annex III systems. Recital 38 and the amended art. 50 timing give art. 50(2) a four-month transition. | The duty to build competence was weakened three months before the essay appeared, and the duties to disclose were left in place, though some were deferred (Regulation (EU) 2026/1744, art. 1(40)). |
| 4.4 | Nadella has used the word himself. In … | fail-quote | nadella2025looking.html, para. 4 (the first of three items under "this is some of what we still need to get right:"): "A new concept that evolves 'bicycles for the mind' **such that** we always think of AI as a scaffolding …". An aspiration listed as still to be achieved is quoted as a statement of practice. | In December 2025 he listed, among what "we still need to get right," "a new concept that evolves 'bicycles for the mind' such that we always think of AI as a scaffolding for human potential vs a substitute," and called it "the product design question we need to debate and answer" (Nadella, 2025, para. 4). |
| 4.4 | The insider-risk essay is where he answered … | pass (argument) | — | — |
| 4.4 | Plato's Thamus described the result of letters … | pass | Perseus Fowler XML, 275a–b: "for they will read many things without instruction and will therefore seem to know many things", exact | — |
| 4.4 | A staff member with a complete log … | pass (argument) | — | — |
| 5.1 | The history in Section 3 does not … (whole paragraph) | pass (argument; internal) | §3.5, l. 109 | — |
| 5.1 | The duties rest on the three benchmarks … / Operators profess a standard … | pass | Standard pp. 9 (T1.3) and 8 (A5.4), exact | — |
| 5.1 | Contemporaries object, from Sudjianto's practitioner's warning … | fail-quote | Green, p. 1: the *policies* "rest on an uninterrogated assumption: that people are able to effectively oversee algorithmic decision-making". Green does not call human oversight itself an assumption. | Contemporaries object, from Sudjianto's practitioner's warning to the scholars who find that human-oversight policies rest on an "uninterrogated assumption" (Green, 2022, p. 1). |
| 5.1 | And the promise falls short: … | pass (argument) | — | — |
| 5.2 | The first duty is to take back … / The operator should check understanding … | pass (argument) | — | — |
| 5.2 | The probate registrar must "satisfy himself" that … | pass | r. 13: "the [district judge or] registrar shall satisfy himself that the testator had such knowledge" (blind or illiterate testator). Art. 193: reading counts as complete when the notary has conveyed "alcance y efectos, atendidas las circunstancias de los comparecientes", exact. | — |
| 5.2 | For AI systems the analogue is the … | pass | Standard pp. 8–9; P1–P21 | — |
| 5.2 | Green (2022) proposes that agencies justify any … | pass | p. 15: "the default assumption should be that human oversight is likely to be ineffective, unless proven otherwise" (initial capital is a permitted change); pre-deployment justification at pp. 14–16 | — |
| 5.2 | Sudore and colleagues' result is the measure … | fail-true | Card (abstract only, checked against PubMed): 28% answered all questions correctly at the first pass (so 72% did not), which holds. But 98% is of participants "who **engaged in** the consent process", not those who completed it, and the abstract gives no denominator. | … and teaching to a stated goal left 2 percent of those who engaged in the process without full understanding (Sudore et al., 2006). |
| 5.2 | Where understanding cannot be secured, the operator … / *Jones v. Meehan* (1899) construed a … | pass | cap_jones_meehan.html, 175 U.S. at 11: "drawn up by them and in their own language"; "the interpreter employed by the United States"; quotation exact. A pin cite (at 11) is advisable. | — |
| 5.2 | Helberger, Pierson, and Poell (2018) put the … | pass | helberger2018.pdf, p. 3 (quotation exact) and p. 11 ("Users can only be expected to take some … responsibility if the necessary conditions have been created by platforms and authorities"). **No card exists** for this work. | — |
| 5.2 | A duty to verify AI output, … | pass (argument) | — | — |
| 5.3 | The second duty is to deliver … / A log written for later … / What can is support … | pass (argument) | — | — |
| 5.3 | The experimental record points the way: salient, … | fail-overstated | Vasconcelos tested no uncertainty markers, and the salient-marker result is exploratory (p. 129:19), as in §4.3. Calo, p. 1033: "not … exclusively" language, as in §4.3. | The experimental record points the way: in a small exploratory study, salient, visual markers of a system's error reduced overreliance where written explanations did not (Vasconcelos et al., 2023), and Calo's (2012) "visceral notice" moves the information into the experience of using the product, not only into language about it. |
| 5.3 | A second form of the duty concerns … / The previous version of this argument … | fail-ref | "(v3, Section 5.3)" cites an unpublished internal draft. It has no reference entry and a reader cannot follow it. v3 §5.3 (l. 209–217) does propose the envelope. | A second form of the duty concerns what a person needs to know to act: a *declared operating envelope*, that is, advance, binding limits on what a system may do to the person, stated in terms the person can act on without understanding the model. |
| 5.3 | A driver need not understand a pricing … / The envelope changes the medium … | pass (argument) | — | — |
| 5.4 | The third duty is to scaffold … / The definition in Section 2.2 … | pass | §2.2, l. 45 | — |
| 5.4 | The support must be interactive, contingent on … | pass | Belland, p. 5 (interactive; PDF 14), p. 18 (contingency; "Support that continues indefinitely does not meet the scaffolding definition"), p. 19 (job aid); fading is at p. 21 | — |
| 5.4 | It must operate where the competence is … / And it must externalize the processes … | fail-overstated (minor) | Collins et al., p. 3: cognitive apprenticeship is for "reading, writing, and mathematics"; p. 4: "render key aspects of expertise invisible"; p. 6: "bring these tacit processes into the open" | … which is the problem cognitive apprenticeship was built to solve for reading, writing, and mathematics (Collins et al., 1987, pp. 3–6). |
| 5.4 | Systems built this way exist, at small … / Kulesza and colleagues (2015) designed a … | fail-true | Author's version, p. 1 (quotation exact) and p. 9 ("52% higher … (W = 259, p < .001)"): both now right. But p. 7 says participants could have no more programming experience than "an introductory-level course"; they were not "without programming experience". | … participants with no more than introductory programming experience who used it scored 52 percent higher on a test of their mental model of the system than a control group (author's version, p. 9). |
| 5.4 | Bainbridge (1983, p. 777) proposed the industrial … | fail-true | p. 777: all three quotations exact, and the ellipsis replaces "which". But "forty years earlier" follows Kulesza (2015): 1983 is 32 years before it. "Forty years" is true only from today (43). | Bainbridge (1983, p. 777) proposed the industrial form more than thirty years earlier: … |
| 5.4 | Sudjianto's (2026) recommendation that firms "redesign junior … | pass | exact ("Second, redesign junior roles …") | — |
| 5.4 | The evidence that such support changes outcomes … / A meta-analysis of 76 randomized … | fail-locator | p. 16 is a page of **NBER Working Paper 27057 (2020)**, which is the copy read (card), not of *JFE* 145(2), 255–272, which is the work cited. The quotation is exact at WP p. 16 (PDF 17). Card l. 66: the comparison uses 64 RCTs, not all 76. "Most-cited" has no source. | … and noted that one of the main findings of an influential earlier review "is not confirmed" (Kaiser et al., 2022, working paper p. 16; on the earlier review, Fernandes et al., 2014). |
| 5.4 | The modesty is itself an argument … / Courses taken once and far from … | fail-overstated | Fernandes WP p. 14: "at delays of 20 months or greater, there is no significant effect of even 24 hours of instruction", which holds. But WP p. 22: "'just-in-time' financial education **may have promise, alone and** embedded in decision support systems". "Recommended" overstates, and the ellipsis cuts out the hedge. | … the earlier review found no significant effect of instruction at delays of twenty months, and its authors suggested that "'just-in-time' financial education may have promise, alone and embedded in decision support systems" (Fernandes et al., 2014, working paper pp. 14, 22). |
| 5.4 | Scaffolding without an avenue to act does … / Nussbaum (2011) distinguishes the internal capability … | cannot-check (card is snippets only) | nussbaum2011creating: one-line search snippets, "two snippets, joined", no page. The card warns "every phrase needs its printed page and context checked before quotation". The quotation has no page. | (Supply the page from the printed book; quoted words to be confirmed.) |
| 5.4 | A worker who has learned how a … | pass | Lovett (SEP): "Just because one is better able to cope with arbitrary power, it does not follow that one's domination is any less". Douglass, p. 40 (DocSouth mark): "It had given me a view of my wretched condition, without the remedy", exact. | — |
| 5.4 | The three duties therefore stand together. … | fail-ref | "(v3, Section 5.4)" again cites an internal draft with no entry. The "independent party" is otherwise undeveloped in v4. | … and the envelope, joined to an independent party able to hear disputes, gives the competence something to act on. |
| 5.5 | *The essay is for enterprises, not consumers.* … | pass | P20 is the one place outsiders appear; Bainbridge, p. 776 | — |
| 5.5 | *Disclosure respects autonomy.* Calo (2012, p. 1049) … | pass | p. 1049, exact (Calo reporting the defence: "the view is") | — |
| 5.5 | Solove (2013, p. 1899) concludes that privacy … | fail-overstated (minor) | p. 1899: "should not be abandoned", exact. The reason he gives there is autonomy ("key to facilitating some autonomy"); at p. 1900, "paternalistic solutions are troubling". "Because the alternative is paternalism" compresses this. | Solove (2013, pp. 1899–1900) concludes that privacy self-management "should not be abandoned" and that paternalistic alternatives are troubling. |
| 5.5 | Disclosure also disciplines the discloser: Solove suggests … | pass | p. 1900: "**perhaps** the greatest practical impact …"; the hedge is kept ("may") | — |
| 5.5 | Nothing here asks operators to stop disclosing. … | pass (argument) | — | — |
| 5.5 | Berthon, Pitt, and Campbell (2019, p. 457) … | pass | p. 457: "empirical research suggests that information is necessary, but not sufficient to change behavior (e.g., Worsley 2002)", quotation exact. p. 452: "informing (educate and disclose)". | — |
| 5.5 | *Scaffolding is responsibilization by another name.* … Willis … | pass (abstract only) | willis2008against: all three quotations exact in the abstract (OpenAlex). No locator is possible. The abstract says "For some consumers … **appears to**"; the manuscript's "can" is acceptable. The card did not confirm the venue from a primary record. | — |
| 5.5 | Docherty and Valderrama Barragán (2026, p. 17) … | fail-locator | Both quotations are exact at **online-first** p. 17 (PDF 18). The entry gives issue pages 555–575, and the online-first page n is issue page 554 + n (21 pages each), so the issue page is 571. | Docherty and Valderrama Barragán (2026, p. 571) find … |
| 5.5 | Martin (2019, p. 845) notes that on … | fail-overstated | p. 845: "if the role of the algorithm in a decision is minimized, by providing tools to allow users to revisit **how the algorithm works**, the firm would have **more of** a traditional handoff of a product with associated (minimal) responsibility". The tools let users revisit how the algorithm works, not "its decisions", and the passage is about the firm's share. Martin's "users" are deployers such as judges (card). The page is inferred, not printed (card). | Martin (2019, p. 845) notes that on her own account, a firm that gives the people who use an algorithm tools to revisit how it works moves toward a traditional product handoff, with "(minimal)" responsibility of its own. |
| 5.5 | And the history in Section 3.3 shows … | pass (internal) | §3.3, l. 95: "the scaffold served the sponsor"; Brandt | — |
| 5.5 | The objection defines the conditions … (to "… while the competence grows.") | pass (argument) | — | — |
| 5.5 | Business ethics has already asked firms to … Scherer … | pass | Scherer et al., p. 428 ("business organizations also have a responsibility to contribute to organizing individual and collective maturity") and p. 429 ("informing and training citizens"), exact | — |
| 5.5 | … and Vredenburgh (2022, accepted manuscript pp. … | fail-overstated (minor) | AAM p. 18: "It is neither realistic nor desirable to expect individuals to use explanations … within all the institutions that affect them, absent support". "Usable only with support" is stronger. The p. 22 quotation is exact (it continues "– human or algorithmic"). | … and Vredenburgh (2022, accepted manuscript pp. 18, 22) argues that people cannot be expected to use explanations across the institutions that affect them "absent support," so that "states and companies may need to invest more resources in providing individuals with free experts." |
| 5.5 | What the history adds is the order … | pass (argument) | — | — |
| 5.5 | *The history is analogy.* … (paragraph) | pass (argument; internal) | §2.1, l. 35 (objects of literacy fixed, of algorithmacy moving); §3.3 native schools | — |
| 6 | The historical cases are narrow. They come … / The burden is documented … | pass | consistent with §3 | — |
| 6 | Several sources are known to me in … | fail-ref / fail-true | Gabel and *Saunders v. Anglia* are cited nowhere in v4 and have no entries (grep). The list also leaves out partial reads that §§4–5 rely on: Willis (abstract), Nussbaum (search snippets), Kaiser and Fernandes (working-paper versions), and Kulesza and Vredenburgh (author's versions, which the text labels). Sudore is the only consent study cited. | Several sources are known to me in part: Clanchy's book through excerpts, the consent study and Willis's article through their abstracts, Nussbaum's book through search snippets, and the financial-education studies through their working papers. |
| 6 | The Requerimiento's Spanish text and its contemporary … | pass | Las Casas 1876, Oviedo 1853, Helps 1855 | — |
| 6 | The present-day evidence is also narrow. … (paragraph) | pass | Vasconcelos and Kulesza both test decision-time use | — |
| 6 | The analogy compares positions and practices. … (paragraph) | pass (argument) | — | — |
| 7 | Nadella's essay ends on a reversal: … | pass | P21; P11, P14, P19 | — |
| 7 | What the essay does not ask … / Its answer to that question is a text. | pass (argument) | — | — |
| 7 | A text read aloud in a language … / A signature bound a buyer … | pass | §3.1 (Requerimiento; *L'Estrange*) | — |
| 7 | A verse chosen by the judge decided … | fail-overstated | §3.1 (Cross, 1917, p. 552): the verse was "usually the opening of the fifty-first Psalm". The judge's choice is one 1640 petition. | A reading test set by the court decided who hanged. |
| 7 | The institutions that did better learned, … (to end) | pass (argument) | — | — |

## Reference list

A fork of this check compared each entry with its card and checked every DOI against Crossref (27 DOIs,
2026-10-14; Johansson through DataCite). I re-scored its rows against HEAD (436b556).

| § | entry | verdict | evidence | corrected entry |
|---|---|---|---|---|
| Ref | Alvord 1905/1866 | pass (fixed in 436b556) | alvord1866report: pp. 143–145; HEAD now reads 143–145 | — |
| Ref | Criminal Law Act 1827 (now "An Act for further improving the Administration of Justice in Criminal Cases in England, 7 & 8 Geo. IV c. 28 (1827)") | cannot-check (no card) | Only facet V2 has it, from a vLex transcription the facet says to re-check against a printed *Statutes at Large* | — |
| Ref | Finnegan 1973 | cannot-check (end page) | The card confirms p. 112 as the start only; 144 is unconfirmed | — |
| Ref | Goody 1987 | cannot-check (no card) | Snippet-only facet record, no pages; the §2.4 quotation has no page | — |
| Ref | Helberger, Pierson & Poell 2018 | pass (no card) | Crossref: 34(1) 1–14, DOI matches; pp. 3 and 11 read in the local PDF. A card should be written. | — |
| Ref | Kaiser et al. 2022 | pass (entry); see §5.4 locator | Crossref: 145(2) 255–272. The locator in the text belongs to the NBER WP. | — |
| Ref | Kulesza et al. 2015 | pass | Crossref: IUI '15, 126–137. The text cites author's-version pages, labelled. | — |
| Ref | Docherty & Valderrama Barragán 2026 | pass (entry); see §5.5 locator | Crossref: 29(4) 555–575 | — |
| Ref | Nussbaum 2011 | pass (entry) | Card is "writer-grounded" (snippets) | — |
| Ref | Ong 2002 (orig. 1982), Routledge | pass (fixed in 436b556) | DOI 10.4324/9780203328064 is the Routledge e-book; the djvu read carries the 2002 New Accents preface; p. 133 confirmed | — |
| Ref | Oviedo 1853 | fail-ref | oviedo1853historia: the author is "Fernández de Oviedo y Valdés, Gonzalo", and "Fernández de Oviedo" is the surname | Fernández de Oviedo y Valdés, G. (1853). *Historia general y natural de las Indias, islas y tierra-firme del mar océano* (J. Amador de los Ríos, Ed.; Vol. 3). Real Academia de la Historia. [In-text: (Fernández de Oviedo, 1853).] |
| Ref | Scherer et al. 2023 | fail-ref | Card and Crossref: the title begins "Guest editors' introduction:" | Scherer, A. G., Neesham, C., Schoeneborn, D., & Scholz, M. (2023). Guest editors' introduction: New challenges to the enlightenment: How twenty-first-century sociotechnological systems facilitate organized immaturity and how to counteract it. *Business Ethics Quarterly, 33*(3), 409–439. https://doi.org/10.1017/beq.2023.7 |
| Ref | Sudore et al. 2006 | pass | Crossref: 21(8) 867–873, DOI matches (erratum at 21(9) 1009) | — |
| Ref | Willis 2008 | pass (entry, writer-grounded) | OpenAlex and Crossref give no venue record; "94 Iowa L. Rev. 197" rests on a secondary citation; OpenAlex title has no hyphen | — |
| Ref | all other 69 entries | pass | Fork table: Almeida, Arató, Bainbridge, Belland, Berthon, Bhola, Brandt, Butterfield, Cal. Civ. Code § 1632, Calo, Clanchy, Collins, Cross, Douglass, Edwards & Veale, Elish, Fernandes, *Foster*, the four General Assembly acts, Green, Hagedorn, Helps, Heyd, Israeli, Johansson, *Jones*, Las Casas, *L'Estrange*, Ley del Notariado, Lovett, Martin, Marz, McDonald & Cranor, Microsoft 2022/2024/2026, MoJ PD 32, Moody-Adams, *Morales*, Morris, Nadella 2025/2026, NCPR 1987, Obar, Plato, *Badger*, *Marshall*, Reglamento, Reg. 2024/1689, Reg. 2026/1744, Roberts (no card; bib and facet agree), Selbst & Barocas, Smith, Solove, South Carolina, Street, Sudjianto, TRC, *Upton*, Vasconcelos, Vredenburgh, Waitangi, Walzer, *Bailey*, Washington, Yeung. Each matches its card, and its Crossref record where a DOI is given. | — |

**Citations against entries (whole manuscript).** Every entry is cited, and every citation has an entry. The one
exception, Pettit (1999, p. 165), is quoted through Lovett, a valid secondary citation. §6 names Gabel and *Saunders*
without citing them (see the §6 row). "(v3, Section 5.3)" and "(v3, Section 5.4)" cite a draft that has no entry (see
the §5.3 and §5.4 rows).

## Rates

**§4–§7: 115 rows** (some rows group several sentences). 78 pass (68%; this includes argument rows and 1 pass at
abstract level), 36 fail (31%), 1 cannot-check.

| verdict | count |
|---|---|
| pass | 78 |
| fail-overstated | 23 |
| fail-true | 4 |
| fail-quote | 3 |
| fail-locator | 3 |
| fail-ref | 2, plus the §6 row scored fail-ref/fail-true (3 in all) |
| cannot-check | 1 (Nussbaum) |

**Reference list: 83 entries.** 78 pass, 2 fail-ref (Oviedo, Scherer), 3 cannot-check (Criminal Law Act 1827,
Goody 1987, Finnegan's end page). Alvord and Ong were fixed by 436b556. Cited works without an entry: 0. Entries never
cited: 0.

**Pattern.** Most fails are hedges dropped when a source's claim is carried into the text: Elish's "may", Vasconcelos's
"suggest" and its exploratory zero result, Calo's "not exclusively", Solove's "might", Fernandes's "may have promise",
Sudjianto's "potentially", and Nadella 2025's aspiration quoted as practice. The Microsoft and EU-law quotations are
all verbatim; their fails are about scope. The Copilot card's users are not the essay's "those affected". Art. 73
applies only to high-risk providers. The Omnibus deferred disclosure duties as well as weakening art. 4.
