# R5: Novelty and the counter-case since N6; the strongest objection to each duty

*Run R5, 2026-10-24. Agent-drafted. The author has not reviewed it. None of the text is the author's.*

## Scope

- Ledger rows D02, D03, D04, D06, D07, D08 (the six duties of CB) and O01–O08 (the objections), with D01, D05 where a
  duty's enforcement is at issue.
- Premises A4, A5, A7, A8, B1, CB, and the novelty claim that the opening makes for CA.
- Draft passages (`../manuscript/DRAFT_v1.md`): lines 26–34 (the post and its reception), 36–42 (its "we"), 54–70
  (what is new; prior uses of the print analogy; the gap sentence), 279–283 (teach-back and the grade card as
  corrections), 442–510 (§4 objections), 512–552 (§5 duties).
- Inputs read first: `../facets/N6_counter_case_and_gap_search.md` (its search log rows 1–61 were not repeated),
  `../ARGUMENT_AND_OUTLINE.md` v2, `../../consolidation/CONCEPT_LEDGER.md` rows D01–D10 and O01–O08,
  `../../literature/CARD_INDEX.md` (grepped for every candidate before carding).

Three questions. (1) Since N6, has anyone argued that AI or LLM vendor or enterprise governance repeats print, scribal
practice, press licensing, notaries, the duty to read or the history of literacy? (2) What was the post's reception
from 20 to 24 October 2026? (3) For each duty, what is the strongest published objection or failed precedent, and what
implementation shows it feasible?

## Search log

Blocks are marked **B**. No paywall, bot-wall or CAPTCHA was circumvented; no email address was sent anywhere.

| # | Source | Exact query or URL | Hits | Notes |
|---|---|---|---|---|
| 1 | Consensus | three queries (print-press analogy for LLM governance; duty to read and LLM agents; notary/scribe analogy for agent accountability) | — | **B** "You've used all 500 included searches this month; resets on November 1st" (all three) |
| 2 | Scholar Gateway | one natural-language query on print/licensing/scribal/notary/duty-to-read/literacy analogies for AI governance, 2020– | — | **B** `ACCESS_DENIED` |
| 3 | Google Scholar | `"printing press" "AI agents" governance history`, as_ylo=2020 (one curl) | HTTP 200 | Response not parsed (Scholar serves no API; HTML not read to avoid scraping). Logged as attempted once |
| 4 | OpenAlex t&a | `"duty to read" AND ("artificial intelligence" OR "large language model" OR chatbot)`, 2020–2026 | 1 | Medical essay; no hit |
| 5 | OpenAlex t&a | `"history of the book" AND ("artificial intelligence" OR "large language model")` | 12 | Library-science and review items; one Sapienza 2026 item on paper devices as "cognitive machines" (not opened) |
| 6 | OpenAlex t&a | `"print culture" AND ("large language model" OR "generative AI")` | 8 | Critical AI 2024 sociolinguistics; nothing on governance |
| 7 | OpenAlex t&a | `"cultural technologies" AND "large language models"` and `"cultural and social technologies"` | 12; 5 | **Farrell, Gopnik, Shalizi, Evans (2025, Science)** |
| 8 | OpenAlex t&a | `"Gutenberg" AND ("large language model" OR "generative AI") AND (ethics OR governance OR regulation)` | 3 | Mahardhika (N6); two unrelated |
| 9 | OpenAlex t&a | `"Gutenberg parenthesis"` | 43 | Jarvis 2023 (book) and reviews; a 2024 Journal of Cyber Policy review (closed) |
| 10 | OpenAlex t&a | `"literacy" AND "history" AND ("AI agents" OR "agentic AI") AND (governance OR ethics)` | 7 | None on point |
| 11 | OpenAlex t&a | `"scriptorium" OR "scribes" AND "generative AI"` | 70 | Clinical "AI scribes"; one 2026 philosophy-of-engineering chapter "Author and Scribe" (closed, not opened) |
| 12 | OpenAlex t&a | `"insider risk" OR "insider threat" AND "Nadella"` | 0 | |
| 13 | OpenAlex t&a | `"smart readers" AND contracts`; `"no-reading problem" AND ("artificial intelligence" OR "language model")` | 3; 7 | **Arbel and Becher (2025)**; Arbel and Becher 2022 located via WebSearch |
| 14 | OpenAlex t&a | `"Areopagitica" AND ("artificial intelligence" OR "AI")`; `"imprimatur" AND (...)`; `"licensing" AND "press" AND "seventeenth century" AND (...)` | 0; 0; 0 | |
| 15 | OpenAlex t&a | `"literacy test" AND (algorithm OR "artificial intelligence") AND (analogy OR history)`; `"mass literacy" AND (...)`; `"Eisenstein" AND "printing" AND (...)` | 32; 2; 1 | OECD skills reports; nothing on point |
| 16 | OpenAlex t&a | `"agentic AI" AND ("business ethics" OR "third parties") AND (accountability OR duties)`, 2025–2026 | 27 | Agency-law and provenance preprints; no historical analogy |
| 17 | OpenAlex t&a | `"AI agents" AND "history" AND (analogy OR precedent) AND (governance OR regulation) AND (print OR literacy OR telegraph OR corporation)` | 0 | |
| 18 | WebSearch | `"duty to read" large language models AI agents contracts consumers 2024 2025 law review` | 9 | Arbel and Becher 2022; Ashkenazi 2025 (BETR); Kolt 2022 (BTLJ) |
| 19 | WebSearch (extended) | `"AI agents" history "scribes" OR "notaries" OR "printing press" OR "literacy" essay governance accountability "people affected" 2026` | 9 | A blog ("The Scribe and the Agent"), arXiv governance preprints; none on point |
| 20 | WebSearch | `Jeff Jarvis AI "printing press" OR Gutenberg regulation agents ... 2025 OR 2026` | 10 | WEF interview 2024 on the book; no agent-governance essay |
| 21 | WebSearch | `Farrell Gopnik Shalizi Evans ... pdf preprint` | 10 | Author's version at henryfarrell.net (downloaded) |
| 22 | WebSearch | `Arbel Becher "Contracts in the Age of Smart Readers" ... gwlr.org` | 10 | Journal abstract page; SSRN; a third-party mirror (not used) |
| 23 | figshare API | `articles/21078382` (Wellington repository record of Arbel and Becher 2022) | 1 | Record points back to SSRN; no file |
| 24 | Crossref | `works/10.1017/9781009279079` and `.019`; OpenAlex abstract for `.019` | 1; 1 | Cambridge Handbook (ed. Elvy), pp. 336–374, 2025 |
| 25 | WebFetch | scholarship.law.missouri.edu/betr/vol9/iss2/4 (Ashkenazi landing page) | 200 | Relayed abstract; PDF URL |
| 26 | curl / WebFetch | Ashkenazi PDF (`viewcontent.cgi?article=1238&context=betr`) | 403; 403 | **B** |
| 27 | WebSearch (extended) | `Nadella "insider risks" AI models essay response critique October 2026` | 9 | Above/Security Boulevard; Digit; TheStreet; FourWeekMBA; blogs |
| 28 | WebSearch (extended) | `Nadella "Models as Insider Risks" Anthropic OR OpenAI OR Google OR Suleyman response ...` | 9 | Suleyman and Levie support (Business Standard); no vendor statement found |
| 29 | WebSearch (extended) | `Nadella insider risk essay commentary Stratechery OR Platformer OR "The Information" OR Fortune OR "Wall Street Journal" OR Lawfare OR Substack` | 9 | None from those outlets; DTEX; **SiliconANGLE 19 Oct** |
| 30 | WebSearch (extended) | `Nadella "insider" AI essay LinkedIn OR blog "disagree" OR "wrong" OR "misses" OR "pushback" ... October 21 OR 22 OR 23 2026` | 9 | No pushback found; Crowdfund Insider (blocked, row 36) |
| 31 | HN Algolia | `search_by_date` for `Nadella insider`, `insider risks super intelligence`, `models as insider risks`, `Nadella emergency brake`, created after 20 Oct 2026 | 10/4/91/1 | No new submission or comment after 13 Oct; Bloomberg 10 Oct story (8 points, 0 comments) |
| 32 | WebFetch | siliconangle.com/2026/10/19/... | 200 | Downloaded; carded `riley2026microsoft` |
| 33 | WebFetch + curl | dtex.ai blog (Koo, 12 Oct); above.security (10 Oct); cellcog.ai (Garg, 11 Oct); securityboulevard.com | 200 ×4 | Downloaded and carded (`koo2026insider`, `above2026satya`, `garg2026nadella`) |
| 34 | WebFetch | getscuttlebutt.substack.com (23 Oct summary of a Semafor interview) | 200 | Relayed; names no essay; led to row 35 |
| 35 | WebSearch (semafor.com) + WebFetch | Albergotti author page; `article/10/21/2026/microsofts-nadella-is-back-in-business`; `article/10/23/2026/human-complacency...` | 2 | Both downloaded; neither mentions the post or insider risk |
| 36 | curl / WebFetch | crowdfundinsider.com/2026/10/317713-... | 403; 403 | **B** (reported by WebSearch snippet as arguing the essay shifts responsibility to deployers "which benefits Microsoft commercially"; unverified) |
| 37 | WebSearch ×2 + curl | `Hayete Gallot "agentic insider" ...`; `"Securing the agentic insider" Gallot Microsoft`; blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/ | 9; 9; 200 | Microsoft's own post downloaded; carded `gallot2026securing` |
| 38 | OpenAlex t&a | `"Local Law 144" AND (compliance OR audit)` | 43 | **Wright et al. 2024**; Groves et al. 2024 |
| 39 | OpenAlex t&a | `"right to human intervention" OR "human alternative" AND "automated decision" AND (empirical OR effectiveness OR practice)`; `"Article 22" GDPR ... (effectiveness OR practice OR empirical)` | 1; 28 | Binns and Veale 2021 (OUP, not opened) |
| 40 | OpenAlex t&a | `"human oversight" AND "AI Act" AND (ineffective OR limits OR critique)` | 59 | Preprints; nothing stronger than `green2022flaws` |
| 41 | OpenAlex t&a | `"platform-to-business" regulation AND (evaluation OR review OR effectiveness)` | 51 | No evaluation study surfaced |
| 42 | WebSearch ×2 | P2B Regulation 2019/1150 Commission review 2025; digital omnibus 19 Nov 2025 repeal of P2B | 10; 9 | COM(2023) 525 preliminary review; repeal proposal in the Digital Omnibus (law-firm summaries) |
| 43 | curl | EUR-Lex `CELEX:52023DC0525` PDF; EUR-Lex procedure `2022_303`; digital-strategy.ec.europa.eu P2B page | 202 empty ×2; 403 | **B** (EUR-Lex returns a 202 shell to scripted requests; Commission page CloudFront 403) |
| 44 | OpenAlex t&a | `"model cards" AND (analysis OR practice OR adoption) AND documentation` | 108 | **Liang et al. 2024** (NMI closed; arXiv read) |
| 45 | OpenAlex t&a | `"data trusts" AND (failure OR adoption OR critique)` | 107 | **Austin and Lie 2021** |
| 46 | OpenAlex t&a | `"out-of-court dispute settlement" AND "Digital Services Act"` | 19 | "The last duel?" (ICTL 2026, T&F, not opened); Appeals Centre found via WebSearch |
| 47 | WebSearch | Appeals Centre Europe transparency report 2025 ... Article 21 DSA | 9 | Reports of Sept 2025 and May 2026 downloaded; May 2026 carded |
| 48 | OpenAlex t&a | `"teach-back" AND (systematic review OR meta-analysis)` | 85 | **Talevski et al. 2020** (PLoS, read); JGIM 2026 meta-analysis (not opened) |
| 49 | OpenAlex t&a | `"informed consent" AND comprehension AND interventions AND "systematic review"` | 29 | Glaser et al. 2020 (MDM) |
| 50 | curl | SAGE PDF; europepmc.org PMC7079202 render; pmc.ncbi.nlm.nih.gov PMC7079202 | 403; 403; HTML | **B** Glaser not opened |
| 51 | OpenAlex t&a | `"restaurant" AND "grade" AND (hygiene OR sanitation) AND (manipulation OR inflation OR "Fudging")` | 3 | Food Policy 2020; JEBO 2020 (both closed) |
| 52 | Crossref | `query.bibliographic=Fudging the Nudge ...` | 3 | Led to Ho, Ashwood, Handan-Nader 2019 and the Jin–Leslie reply |
| 53 | WebSearch ×2 | Ho "Fudging the Nudge" pdf; Ho Ashwood Handan-Nader AEJ pdf Stanford | 10; 10 | yalelawjournal.org PDF; dho.stanford.edu published PDF (both downloaded) |
| 54 | curl | aeaweb.org PDF of the Jin–Leslie reply (10.1257/pol.20180543) | HTML | **B** Abstract via Crossref only |
| 55 | OpenAlex t&a | `"privacy nutrition labels" OR "privacy labels" AND (iOS OR accuracy OR usable)` | 88 | **Zhang et al. 2022** (read); Kollnig 2022; Li 2022 (not opened) |
| 56 | OpenAlex t&a | `"cookie banners" OR "consent banners" AND (dark patterns OR nudging) AND (empirical OR field)` | 6 | Theses; nothing opened |
| 57 | WebSearch + curl | Felt et al. "Improving SSL Warnings" CHI 2015 pdf | 9; 200 | Downloaded from research.google.com |
| 58 | OpenAlex t&a | `"financial literacy" AND "meta-analysis" AND (education OR interventions)` | 57 | Fernandes 2014 and Kaiser 2022 already carded (course library); NBER w27057 downloaded, not carded |
| 59 | OpenAlex t&a | `"generative AI" AND "harm learning" OR "without guardrails"` | — | Bastani et al. 2025 (PNAS) |
| 60 | curl | PNAS PDF; europepmc PMC12232635; pmc.ncbi.nlm.nih.gov PMC12232635 | 403; 403; HTML | **B** Bastani not opened |
| 61 | OpenAlex t&a | `"AI literacy" AND responsibilization`; `"plain language" AND (mandate OR law OR regulation) AND (effect OR evaluation OR comprehension) AND (contracts OR disclosure)` | 1; 47 | Nothing usable |
| 62 | WebSearch ×2 | AI Liability Directive withdrawn 2025; OJ notice COM(2022) 496 | 10; 10 | EAPIL (downloaded, carded); Bird & Bird (downloaded) |
| 63 | curl | arXiv 2406.01399 (Wright); arXiv 2402.05160 (Liang); dl.acm.org PDFs for 3630106.3658998 and 3630106.3658959 | 200; 200; 403; 403 | **B** ACM DL; Groves 2024 has no arXiv copy |
| 64 | Semantic Scholar API | OA-PDF lookups for Wright, Groves, Fernandes, Binns–Veale, Arbel 2025, Kaiser, Jin–Leslie | 7 | Only Wright's arXiv ID returned |
| 65 | Crossref | DOI checks for every carded work (titles, venues, years, pages matched) | 17 | Recorded in each card |
| 66 | Local | Card index greps for every candidate key; `simon2005impact` card; N3 Q9; ADJUDICATION A2 row; AUDIT_N7a N3-21/22 | — | Simon 2005 is the draft's D07 figure |

## Entries

### E1. The novelty claim (draft lines 54–70; CA; outline "Opening")

**What the draft says.** Lines 63–70 name four prior uses of the press analogy (Lastowka, Cedillo-Lazcano, Cinar,
Mahardhika), then: "In the databases and journals I searched, I found no work that turns the record of print and mass
literacy on the people a deploying organization's agents act on".

**What the literature holds.** Two works the draft does not cite reach the same ground from different sides.

- Farrell, Gopnik, Shalizi and Evans (2025, Science; `farrell2025large`, author's version read in full): large models
  are "cultural and social technologies" in the line of writing and print, which "allow people to access information
  that other people have created"; and "In the case of earlier social and cultural technologies, a range of further
  institutions, including normative and regulatory institutions, emerged to temper their effects. These ranged from
  editors, peer review, and libel laws for print". It is the most-cited recent print analogy for LLMs (73 citations in
  OpenAlex) and it argues against treating models as agents, the frame Nadella's "insider" presupposes.
- Arbel and Becher (2022 GWLR; 2025 Cambridge Handbook chapter, `arbel2025how`, abstract only) put LLMs and the duty
  to read together before the draft, with the opposite conclusion: LLM "smart readers" cut contract length by about
  two-thirds and bring college-level text to a fifth-grade level, so the no-reading problem is one the medium can now
  relieve on the consumer's side. Ashkenazi (2025) proposes mandatory links to certified AI readers (landing page only;
  PDF blocked).

**Gap.** Neither turns the record on the people an organisation's agents act on, and neither discusses custody of the
record or the brake. The draft's gap sentence survives in its exact words. Its framing sentence ("Scholars have reached
for the press before, in two directions", producers and regulators) does not: Farrell et al. reach for print as a
cultural technology, a third direction, and the smart-reader literature reaches for the duty to read, which is the
draft's own third moment.

**Verdict.** **Narrower.** The gap statement at lines 68–70 holds; the survey at lines 63–68 is incomplete and must
add Farrell et al. and Arbel and Becher, and must meet the smart-reader claim (E4 below).

Gap statements, in the form the research rules require:

> I found no work that argues that AI or LLM vendor or enterprise governance repeats the print era, scribal practice,
> press licensing, notaries, the duty to read or the history of literacy, for the people the deploying organisation's
> agents act on, in OpenAlex title-and-abstract search (rows 4–17, 38–61), Crossref (rows 24, 52, 65), the Semantic
> Scholar API (row 64), WebSearch (rows 18–22, 27–30) and Hacker News (row 31), 2020–2026. The nearest works are
> Farrell et al. (2025), print as a cultural technology with its "countervailing" institutions; Arbel and Becher (2022,
> 2025) and Ashkenazi (2025), LLMs as the consumer's reader under the duty to read; and the four N6 found (Lastowka,
> Cedillo-Lazcano, Cinar, Mahardhika). Consensus (quota) and Scholar Gateway (access denied) were unavailable; Google
> Scholar was attempted once and not parsed.

> I found no scholarly or expert critique of "Models as Insider Risks in the Super Intelligence Era" published between
> 20 and 24 October 2026 in WebSearch (rows 27–30, 35–37), Hacker News (row 31) or OpenAlex (row 12). In that window
> the only new items found are Microsoft's own: Gallot's post of 19 October and its trade coverage, and a Semafor
> profile of 21 October that does not mention the post. Practitioner commentary of 10–13 October (Above, Garg, Koo,
> Pillitteri per N6) is supportive and names standards, tests and Microsoft's interest, never the people acted on.

### E2. The reception claim (draft lines 26–27, 69–70; A4)

**What the draft says.** Thirteen million views in two days (line 27); "the essay's reception has so far been largely
descriptive" (lines 69–70).

**What the sources hold.**
- Microsoft, 19 October: Gallot's "Securing the agentic insider" (`gallot2026securing`): "Unfortunately, frontier
  models, regardless of their origin, cannot be trusted."; "They are agentic insiders."; "Model transparency will not
  replace containment." Riley (`riley2026microsoft`): the controls "require verified human approval" at higher risk,
  cap an agent's authority at that of "the person it works for", and have no date or price; detail promised at Ignite
  on 17 November. The words customer, applicant, affected do not occur in Gallot's post.
- Vendors, 10–12 October: Above (`above2026satya`): "one of the most important perspectives I've read on securing AI in
  the enterprise", with the caveat that a checking model "introduces a second model whose judgments can also be
  imperfect". Koo (`koo2026insider`): "His reasoning is hard to dispute."; "A tamper-proof log tells you what an agent
  did. It can’t tell you whether that matched what anyone asked for."; and of a compromised agent's user, "The person
  is affected, not responsible." Garg (`garg2026nadella`): "It names no Microsoft product, no standard and no date."
- Semafor, 21 and 23 October: nothing on the post (local captures). Hacker News: no new submission or comment after 13
  October. Crowdfund Insider (blocked) is reported by a search snippet as saying the essay shifts responsibility to
  deployers to Microsoft's commercial benefit; unverified.
- View count: Garg gives 8.9 million in a day; the draft's thirteen million in two days has no card.

**Gap.** "Largely descriptive" holds and is now too weak: the decisive response is Microsoft's own product move, which
confirms A4's allocation in a second document and adds a profession for A7 ("transparency will not replace
containment"). The view count is unsupported in the library.

**Verdict.** Lines 69–70 **hold**; line 27's figure **unsupported** (give the source or drop it). Fix to the argument:
the reception section should report Gallot (19 Oct) as the architecture built, and use it under A4/A5/A7.

### E3. "This isn't new!" and the insider frame (draft lines 54–55; A4)

The draft lets Nadella concede that the insider frame is old. Koo's "the insider risk playbook ... already exists" and
Above's recital of insider-risk controls confirm the trade sees it so; Farrell et al. reject the agent frame outright.
No damage; one addition: the insider frame has an owner (enterprise security), and that owner's vocabulary has no word
for the person acted on. **Holds.**

### E4. The burden of reading meets the smart reader (draft lines 48–50, 59, 371–408; A4, A6; D04, D07)

**What the draft says.** The architecture "leaves her the reading" (line 50); the third moment is "courts that bound
the signer to whatever she signed" (line 59).

**What the literature holds.** Arbel and Becher (`arbel2025how`, abstract): LLMs reduce contract length by 66.9 percent
and reading time by about fifteen minutes, and convert college-level text to fifth-grade readability, with occasional
misstatement of legal terms (paraphrase). The duty-to-read literature therefore already has an answer to "leaves her
the reading": the medium can now do the reading for her.

**Gap.** The pairing of M8 (the burden of reading) with L'Estrange holds only if the draft says who runs the reader. A
smart reader supplied by the drafter or the deploying organisation is the Requerimiento's own interpreter (the draft's
second moment); a smart reader the person brings is D04's "bring her own reader". The draft does not make the
distinction, and the vendor's reply writes itself.

**Verdict.** **Contested.** Fix: state the pairing as "the reading is done by a reader the organisation supplies and
controls", and move the smart reader into D04 and D07 as feasible but operator-dependent.

### E5. D02, structural refusal (draft lines 520–521, 535–536)

**What the draft says.** "a route to the same outcome that does not pass through the agent, at no penalty".

**Strongest objection and failed precedent.** The nearest statutory precedent for operator duties toward applicants is
NYC Local Law 144. Wright et al. (`wright2024null`, arXiv p. 1): "Among these employers, 18 posted audit reports and 13
posted transparency notices" of 391 checked; "a null result cannot be said to indicate non-compliance, a condition we
call "null compliance""; "the benefit of LL 144 to ordinary job seekers is limited due to shortcomings in accessibility
and usability". The law has no alternative-route requirement (ledger D02 already says so); this adds that its weaker
duties were met by a small minority because the operator decides scope. The published objection in the library remains
Hoeksema (`hoeksema2023digital`, O04: the second track priced so no one uses it) and Green (`green2022flaws`: the human
may be no fairer).

**Feasibility.** I found no implementation at scale of a no-penalty human route for people acted on by LLM agents
(rows 39–40). The ledger's Bhargava and Assadi (`bhargava2023hiring`) remains the argument that interviews matter, not
evidence that a parallel route exists at comparable speed.

**Verdict.** **Holds as a duty; unsupported as "with a working precedent"** (line 517–518 promises one for each). Fix:
either name a precedent (the draft's own history gives the 1883 jurat rule a different duty, not this one) or drop the
"working precedent" claim for D02 and rest it on D05's point that a duty is worth its enforcement.

### E6. D03, a declared envelope binding toward the people acted on (draft lines 521–524)

**Failed precedent.** Liang et al. (`liang2024whats`, arXiv pp. 2–3): "more than half of the models lacking a model
card"; Limitations filled in 17.4 percent of cards, Evaluation 15.4 percent, Training 74.3 percent. The declaring
instrument in practice describes inputs, not limits. Ho (`ho2012fudging`, p. 612): the San Diego grade could be
re-earned for a fee within thirty days, a redeclarable envelope. P2B (ledger D03's "15 days") is proposed for repeal
in the Commission's Digital Omnibus of November 2025 (law-firm summaries only; Commission page blocked, row 43).

**Feasibility.** AP2 (`google2026agentic`, `parikh2025powering`) remains the one implementation in which the person
signs the constraint; Gallot's Dynamic Permissions cap an agent at "the person it works for" (Riley ¶5), an envelope
toward the enterprise.

**Verdict.** **Holds, narrower.** The duty's precedent is AP2 alone; model cards and grades are failed precedents for
the declaring half unless a party other than the operator fixes and checks the declaration. Fix: state the condition
("fixed by or checkable by someone the operator does not control") inside D03, as O05 already implies.

### E7. D04, counter-delegation (draft lines 524–526, 537–538)

**Failed precedent.** Austin and Lie (`austin2021data`, pp. 255, 257): Sidewalk Labs' Urban Data Trust "was a failed
model because it lacked clarity regarding the nature of the problem(s) to which it is a solution, how accountability
and oversight are secured, and its relation to existing data protection law"; de-identification "actually reduced
accountability and oversight". An operator-designed steward is the configuration D04 excludes.

**Feasibility and its limit.** Appeals Centre Europe (`appealscentre2026transparency`): over 24,000 disputes in a
year; "on average we disagreed with the platform’s decision 59% of the time" where it could review the content (p. 4);
but "a large number of default decisions, where a platform does not provide the content" (p. 5), "In the vast majority
of account suspension disputes, platforms failed to provide us with the content" (p. 11), and "We are still not
receiving consistent data about whether platforms have implemented our decisions" (p. 11); "our decisions are
non-binding" (p. 3).

**Verdict.** **Holds, narrower.** An independent reader exists at scale and mostly overturns the operator; it is
hollow where the operator keeps the record and reports nothing back. The two halves of D04 (her own record; a body the
operator does not control) are one duty, not two, and the draft asserts this without arguing it. Fix: argue the
dependence from the Appeals Centre's default decisions, and keep Easton 1757 as the precedent in which both halves were
present.

### E8. D06, check understanding and carry the risk (draft lines 279–281, 527–530)

**Check understanding.** Talevski et al. (`talevski2020teach`, pp. 11, 14): "19 studies (95%) reported positive
findings for primary outcome measures"; "Teach-back is effective across a wide range of settings, populations and
outcome measures, although implementation techniques are not well described." Feasible at the bedside. Glaser et al.
(2020), the updated review of consent-comprehension interventions, was blocked (row 50); it is the source a referee
would cite for comprehension remaining low after interventions. The strongest objection stays Kolt's (N6 rank 6): no
encounter exists at agent speed in which to check anyone.

**Carry the risk.** The EU's AI Liability Directive, the one legislative attempt to move the burden of proof for AI
harms toward the operator, was listed for withdrawal on 11 February 2025 and withdrawn by OJ notice on 6 October 2025
"for lack of a foreseeable agreement" (`eapil2025european`, ¶¶2–3; Bird & Bird adds Parliament supporters' view that
industry pressure for simplification was the main reason). Microsoft's Copyright Commitment (N6) carries one class of
output risk for the enterprise, conditioned on using Microsoft's filters; nothing carries risk for the person acted on.

**Verdict.** **Holds, narrower.** The checking half has a working precedent for encounters, none for populations; the
risk-carrying half has historical precedents (the 1883 rule, Jones v. Meehan) and a withdrawn modern one. Fix: state
D06 so that the risk half governs wherever no encounter occurs, and cite the AILD withdrawal under O02 as evidence the
law provides less than in 2022.

### E9. D07, change the medium at the point of use (draft lines 281–283, 530–532, 541–542)

**What the draft says.** Los Angeles grade cards "put an inspector's judgment in a letter on the door, and their
introduction was associated with a 13.1 percent fall in foodborne-disease hospitalizations (Simon et al. 2005, 32)";
D07's precedent is the grade card.

**What the literature holds.** Ho, Ashwood and Handan-Nader (`ho2019new`, p. 404): "we show that this finding does not
hold up under improvements to the original data and methodology. The largest salmonella outbreak in state history hit
Southern California before Los Angeles implemented grading."; n. 1 (p. 405): "A different version of the foodborne
illness analysis was also published as Simon et al. (2005). Online Appendix A shows that the same issues identified
here affect that analysis."; p. 425: "there is little credible evidence for the impact of restaurant grading—what many
regard as the archetypal disclosure—on foodborne illness." Jin and Leslie's reply (abstract) defends the result as
"pronounced against central and Northern CA, but insignificant when compared with the rest of Southern CA". Ho
(`ho2012fudging`, pp. 574, 611, 645): San Diego, "Nearly all restaurants receive ‘A’s" (99.9 percent); New York's
grading "has not discernably reduced manifestations of foodborne illness"; "the system perversely shifts inspection
resources away from higher health hazards to resolve grade disputes." Zhang et al. (`zhang2022how`, pp. 204, 218):
Apple's privacy labels, the privacy field's grade card, "still fail to fully support user comprehension" and have low
discoverability "even for participants who said they were concerned".

**What shows feasibility.** Felt et al. (`felt2015improving`, pp. 2893, 2900): "We ultimately failed at our goal of a
well-understood warning. However, nearly 30% more total users chose to remain safe after seeing our warning."
Adherence rose from 30.9 to 58.3 percent by design, not text, and shipped in Chrome 37. The marker's author and the
person protected share an interest there; the adverse case (operator marks its own agent's denial) is untested.

**Verdict.** Simon 2005 figure: **contested** (and the N3/ADJUDICATION claim that it is "the one disclosure regime with
a measured protective effect" falls with it). D07: **narrower**: it holds for markers that need no reading and are
issued or fixed by a party the operator does not control (Jin and Leslie's unrefuted hygiene-score and demand findings;
Felt's warning); it fails for operator-authored summaries (privacy labels) and for grades the graded can buy back.
Fix: cite the grade card as a device that moved the inspector's reading to the door, not as a measured health effect;
add Felt as the precedent; state the independence condition.

### E10. D08, scaffold inside the system (draft lines 503–510, 532–533, 542–543)

**Objection.** O08 (responsibilization) and D10 are already the ledger's strongest; the financial-literacy record is
**contested** in the library's own cards (`fernandes2014financial`: about a tenth of a standard deviation, decaying;
`kaiser2022financial`: effects "at least three times as large" as Fernandes', NBER w27057 abstract, local copy
downloaded). The draft's four conditions (built in, owed, withdrawn, paired with the check) are the right answer to
Fernandes and Willis, but line 509–510's "The skilling promises of Section 3 report reach" relies on N4, not on new
evidence. Bastani et al. (2025, PNAS), the field experiment in which an unscaffolded tutor harmed learning and a
scaffolded one did not, is the implementation evidence D08 needs; it could not be opened (row 60).

**Verdict.** **Holds, contested evidence base.** Fix: name both meta-analyses, and fetch Bastani through the library.

### E11. Objections O02, O07, O08 in §4 (draft lines 472–510)

- **O02.** New evidence cuts both ways: the AILD withdrawal (E8) and LL 144's null compliance (E5) show the law
  providing less than the objection supposes; the Appeals Centre (E7) shows a provided remedy without standing. The
  draft's reply (lines 478–481) **holds** and can be sharpened.
- **O07.** Calo's outsider-reader defence (N6) now has a present instance: Gallot's "accountability and traceability"
  are for practitioners (`gallot2026securing` ¶15). **Holds** as N6 left it.
- **O08.** No stronger published form than Docherty (N6). **Holds.**

### E12. CB's promise, "each with a working precedent" (draft lines 517–518, 552)

Across E5–E10: D03 (AP2), D04 (Easton; Appeals Centre as a partial modern instance), D06's checking half (teach-back),
D07 (Felt; the grade card as device) and D08 (Belland, Kulesza) have precedents; D02 has none in the AI setting, and
D06's risk half has a withdrawn one. **Narrower.** Fix: "each with a precedent, four of them working today" or an
equivalent that does not promise six.

## Damage ranking (what remains after the cheapest repair)

| Rank | Finding | Hits | Damage after cheapest repair | Cheapest repair |
|---|---|---|---|---|
| 1 | The grade-card health effect is contested on replication (Ho et al. 2019; Ho 2012) | D07; A2 (N3 Q9, ADJUDICATION A2 row); draft 281–283, 530–532 | **Medium-high on CB** (the clearest "working precedent" loses its measured outcome); low on CA | Cite the card as device, not outcome; add Felt 2015; state the independence condition |
| 2 | The smart reader answers "leaves her the reading" (Arbel and Becher 2022, 2025) | A4 (M8 pairing); A6; D04, D07 | **Medium on CA** | Pair M8 with "a reader the organisation supplies and controls"; put user-run readers under D04 |
| 3 | "Carry the risk" has no live legal precedent for AI (AILD withdrawn 2025); "check understanding" has none at population scale | D06; CB | **Medium on CB** | Make the risk half govern wherever no encounter occurs; cite AILD under O02 |
| 4 | The statutory duties nearest D02/D03 were met by a minority and self-scoped (LL 144); model cards declare inputs, not limits | D02, D03, D05 | **Medium on CB's feasibility**; none on the duties as duties | Drop "working precedent" for D02; add the fix-and-check condition to D03 |
| 5 | Prior print and duty-to-read analogies not cited (Farrell et al. 2025; Arbel and Becher) | Opening 63–70 | **Low-medium** (survey incomplete; gap sentence intact) | Add both; recast "two directions" as three |
| 6 | Independent readers are hollow where the operator keeps the record (Appeals Centre 2026; Austin and Lie 2021) | D04 | **Low-medium**; strengthens the two-halves link | Argue the dependence; keep Easton |
| 7 | Reception: Microsoft built the architecture on 19 Oct and professed "transparency will not replace containment" | A4, A5, A7 (gain, not damage) | **None**; a gain | Add Gallot to §3 and to the A7 profession route |
| 8 | View count unsourced (13 million vs Garg's 8.9 million in a day) | Line 27 | **Low** | Source or drop |
| 9 | Financial-literacy evidence contested (Fernandes vs Kaiser) | D08, O08 | **Low** | Name both; fetch Bastani |

## Verdict table

| ID | Concept / claim | Draft lines | Verdict | Evidence (card + locator) | Fix to the argument |
|---|---|---|---|---|---|
| R5-01 | Gap sentence: no work turns the print/literacy record on the people acted on | 68–70 | holds | gap statements above (rows 4–31, 38–65) | none |
| R5-02 | Survey of prior press analogies ("two directions") | 63–68 | narrower | `farrell2025large` (paras. "The new technology"; "In the case of earlier"); `arbel2025how` (abstract) | add Farrell et al. (print as cultural technology) and Arbel–Becher (LLM as the consumer's reader); three directions |
| R5-03 | Reception "largely descriptive" | 69–70 | holds | `gallot2026securing` ¶3, ¶15; `riley2026microsoft` ¶2, ¶9; `above2026satya` ¶10; `koo2026insider` ¶10, ¶13; `garg2026nadella` ¶2 | report Gallot (19 Oct) as the architecture built; no critique names the people acted on |
| R5-04 | "Thirteen million" views in two days | 27 | unsupported | `garg2026nadella` ¶ (8.9 million in a day); no card carries 13 million | source or drop |
| R5-05 | "This isn't new!": insider frame conceded old | 54–55 | holds | `koo2026insider` ¶5; `above2026satya` ¶1; `farrell2025large` (rejects agent frame) | note the frame's owner (enterprise security) has no word for the person acted on |
| R5-06 | "Leaves her the reading" (M8 pairing with L'Estrange) | 48–50, 59 | contested | `arbel2025how` (abstract: 66.9 percent shorter, fifth-grade readability) | pair with "a reader the organisation supplies and controls"; user-run readers go to D04/D07 |
| R5-07 | D02 structural refusal | 520–521, 535–536 | holds as duty; unsupported as working precedent | `wright2024null` arXiv p. 1 (18 audits, 13 notices of 391; null compliance); `hoeksema2023digital`, `green2022flaws` (existing) | drop "working precedent" for D02 or name one; rest on D05 |
| R5-08 | D03 declared envelope | 521–524 | holds, narrower | `liang2024whats` arXiv pp. 2–3 (Limitations 17.4 percent); `ho2012fudging` p. 612 (regrade fee); `google2026agentic` (existing) | add "fixed or checkable by a party the operator does not control"; precedent is AP2 alone |
| R5-09 | D04 counter-delegation | 524–526, 537–538 | holds, narrower | `austin2021data` pp. 255, 257; `appealscentre2026transparency` pp. 3–5, 11 | argue that record and body are one duty (default decisions when the operator withholds the record) |
| R5-10 | D06 check understanding | 279–281, 527–529 | holds, narrower | `talevski2020teach` pp. 11, 14; Kolt (N6) | precedent for encounters, not populations; risk half governs where no encounter occurs |
| R5-11 | D06 carry the risk | 529–530 | holds as duty; unsupported as working AI-law precedent | `eapil2025european` ¶¶2–3 (AILD withdrawn 6 Oct 2025); Copilot Copyright Commitment (N6, relayed) | keep the 1883 rule and Jones v. Meehan; cite AILD under O02 |
| R5-12 | Simon 2005 "13.1 percent fall" as D07's precedent | 281–283, 530–532 | contested | `ho2019new` pp. 404, 405 n. 1, 418, 425; Jin–Leslie reply (abstract) | cite the grade card as a device that moved the inspector's reading to the door, not as a measured health effect |
| R5-13 | D07 change the medium | 530–532, 541–542 | narrower | `ho2012fudging` pp. 574, 611, 645; `zhang2022how` pp. 204, 218; `felt2015improving` pp. 2893, 2900 | holds for no-reading markers issued independently of the operator; add Felt as precedent; state the condition |
| R5-14 | D08 scaffold inside the system | 503–510, 532–533 | holds; evidence contested | `fernandes2014financial`, `kaiser2022financial` (existing); Bastani 2025 blocked | name both meta-analyses; fetch Bastani |
| R5-15 | O02 "the law already provides" and the reply | 472–481 | holds | `eapil2025european`; `wright2024null`; `appealscentre2026transparency` p. 11 | sharpen: the law provides less than in 2022 and gives readers without standing |
| R5-16 | O07, O08 replies | 483–510 | holds | `gallot2026securing` ¶15 (traceability for practitioners); Docherty (existing) | none |
| R5-17 | CB "each with a working precedent" | 517–518, 552 | narrower | E5–E10 | promise precedents for the six and working ones for four |
| R5-18 | A4/A5/A7 restated for the second party | 36–42, 123–139 | holds (strengthened) | `gallot2026securing` ¶¶3–5, 14–15; `riley2026microsoft` ¶¶5, 8 | add Gallot's "Model transparency will not replace containment" to the profession route |

## Gaps and blocks

| Item | Block | Where a Bentley library user would find it |
|---|---|---|
| Consensus (three queries, row 1) | Monthly quota exhausted until 1 Nov 2026 | Rerun rows 4–17 as Consensus queries after 1 Nov |
| Scholar Gateway (row 2) | `ACCESS_DENIED` | Reconnect the connector; rerun the row 2 query |
| Google Scholar (row 3) | Attempted once; HTML not parsed | Run `"printing press" "AI agents" governance` and `"duty to read" "large language model"` in a browser |
| Arbel and Becher (2025), Cambridge Handbook ch. 19, doi 10.1017/9781009279079.019; SSRN 4491043 | Chapter closed; SSRN blocked | Cambridge Core via Bentley; SSRN in a browser |
| Arbel and Becher (2022), GWLR 90(1): 83–146 | Journal page gives abstract only; SSRN 3740356 blocked; third-party mirror not used | HeinOnline; SSRN in a browser |
| Ashkenazi (2025), BETR 9(2) art. 4 | Repository PDF 403 (curl and WebFetch) | scholarship.law.missouri.edu in a browser |
| Jin and Leslie (2019), AEJ:EP 11(4): 429–443, doi 10.1257/pol.20180543 | AEA PDF served HTML | AEA via Bentley; JSTOR |
| Glaser et al. (2020), MDM 40(2), doi 10.1177/0272989X19896348 | SAGE 403; Europe PMC and PMC 403/HTML | SAGE via Bentley; PMC7079202 in a browser |
| Bastani et al. (2025), PNAS 122(26), doi 10.1073/pnas.2422633122 | PNAS 403; PMC12232635 403/HTML | PNAS (open access) in a browser |
| Groves et al. (2024), "Auditing Work", FAccT, doi 10.1145/3630106.3658959 | ACM DL 403; no arXiv copy | ACM DL in a browser (open access) |
| Wright et al. (2024) version of record, pp. 1701–1713 | ACM DL 403 (arXiv read instead) | ACM DL in a browser |
| Liang et al. (2024), NMI 6: 744–753 | Closed (arXiv read instead) | Nature via Bentley |
| Farrell et al. (2025), Science 387(6739): 1153–1156 | Closed (author's version read) | Science via Bentley; confirm quotations against the version of record |
| Binns and Veale (2021), IDPL 11(4): 319–332, doi 10.1093/idpl/ipab020 | Not attempted (OUP Cloudflare per N6) | Oxford Academic via Bentley |
| "The last duel?" (2026), ICTL, doi 10.1080/13600834.2026.2728403 | Not attempted (T&F) | Taylor & Francis via Bentley |
| EUR-Lex: COM(2023) 525 (P2B preliminary review); procedure 2022/0303(COD) (AILD withdrawal) | 202 empty shell to scripted requests | eur-lex.europa.eu in a browser |
| Commission P2B policy page; Digital Omnibus repeal of Regulation 2019/1150 (19 Nov 2025) | CloudFront 403; only law-firm summaries read | digital-strategy.ec.europa.eu in a browser; the Omnibus proposal text |
| Crowdfund Insider (Oct 2026) on the essay | 403 (curl and WebFetch) | Browser; save a copy if its "benefits Microsoft commercially" line is to be cited |
| Semafor "Future Proof" interview with Nadella (recorded about 14 Oct 2026) | Only the 21 Oct profile found; the interview itself (video) not located | semafor.com in a browser; the Scuttlebutt summary (23 Oct) claims it discusses insider risk |
| Microsoft materials on Dynamic Agent Risk / Conditional Access / Permissions | Only Riley's report and Gallot's post located | Microsoft Security blog or Tech Community in a browser |
| Kaiser et al. (2022) version of record, JFE 145(2): 255–272 | Closed (NBER w27057 downloaded to `R5/kaiser2020/`, not carded; course card exists) | ScienceDirect via Bentley |
| Ho (2012) Online Appendix; Ho et al. (2019) Online Appendix A (the Simon 2005 reanalysis) | Not fetched | AEA site (topcat.aeaweb.org materials 11743) |
