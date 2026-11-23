[Written by Fable (claude-fable-5-2), stage S13b, 2026-11-23]

# The concerns of *Organization Theory*'s authors, 2023–2026: reconciled stacks

Run `ot-oq-2026-11`, stage S13b. This file reconciles two blind groupings of the 605 open questions that authors left in *Organization Theory* between 2023 and September 2026: analyst F's fourteen stacks (`STACKS_F.md`) and analyst O's fourteen (`STACKS_O.md`). The result is one map of twelve stacks ranked on the 2025–26 evidence, with four cross-cutting threads and a residual of fifteen questions. Membership is in `STACKS.tsv`.

I read both analysts' files and membership tables, `QUESTIONS.tsv`, and all 605 questions in `OPEN_QUESTIONS_BY_DATE.md`: the 221 from 2025–26 first, then the 384 from 2023–24. I did not open the brief, the report, the conversation files, or the fit, critic and pickup folders. I did open `DECISIONS.md` for the run's rulings on question forms. Its S13 entry carries one sentence that summarizes fit scores by year; I read it and did not use it, and no grouping or rank below depends on it.

## Rules

1. **Periods.** 2025–26 holds 24 pieces and 221 questions (2025: 14 pieces, 118 questions; 2026: 10 pieces, 103 questions, the last published online on 21 September 2026). 2023–24 holds 41 pieces and 384 questions (2023: 19 and 179; 2024: 22 and 205). The earlier period has about 1.7 times as many questions, so every count below comes with its share of the period.
2. **Evidence.** Following the author's rule, the 2025–26 questions are the primary evidence and the 2023–24 questions are context. Rank and status rest on 2025–26.
3. **Membership.** I mapped each analyst's stacks onto the twelve and compared the filings question by question. On 445 questions the filings agree, and I kept them. On 148 they differ, and I ruled each one by reading the question. Eleven more questions lost their only stack when Affect stopped being a stack. Appendix A lists all 159 rulings with what F filed, what O filed and what I kept.
4. **At most two stacks.** 456 questions sit in one stack, 134 in two and 15 in the residual, which gives 739 rows in `STACKS.tsv`. A question takes a second stack only when its quotation, or the main clause of the reader's paraphrase, asks that stack's question. A setting, a rider or a call for better methods does not earn one.
5. **Core piece.** A piece is core to a stack when at least three of its questions sit there, or at least half of its questions.
6. **Counts.** `tools/stack_counts.py`, run on `STACKS.tsv`, produced every count in the ranking table and in the stacks' count tables: pieces, core pieces, questions in 2025–26, first authors, last ask, editorial signal and the bar. Its output is in Appendix B. Questions in 2023–24 are the script's total minus its 2025–26 figure. A second script of mine added what the first does not print: questions per year, shares of each period, the number of questions that sit in a stack alone, and the lists of backing pieces. I also ran the count script on side groupings (Time, Affect, the merges I rejected) so that each ruling shows its cost.
7. **Status.** *Prevailing*: three or more core pieces in 2025–26. *Persistent*: asked in both periods with at least one core piece in each. *Fading in effect*: at most one core piece in 2025–26 and fewer than a quarter as many questions as in 2023–24. *New*: no piece before 2025. The bar both analysts applied, three or more pieces in 2025–26, stays as a column. All twelve stacks meet it, which is why it cannot rank them.
8. **Rank.** Core pieces in 2025–26; then questions in 2025–26; then core pieces in both periods; then last ask.
9. **Quotations.** A script copied every anchor and context quotation, with its locator, from the pool file and checked each at 40 words or fewer. One anchor, OQ-dion2025-04, is a contiguous excerpt of a 48-word quotation and says so.
10. **Technology.** I sized it as I sized every other topic, by the pieces and questions that ask about it.

## Crosswalk

Each cell gives pieces / core pieces / questions in 2025–26, from the count script run on that analyst's table.

| Reconciled | From F | From O | F | O | Reconciled |
|---|---|---|---|---|---|
| R01 Institutions and logics | F04 | B, plus the person-institution and logic questions of A | 6 / 6 / 44 | B 6 / 6 / 41; A 7 / 4 / 33 | 6 / 6 / 44 |
| R02 Theory and theorizing | F01 | K | 9 / 5 / 30 | 9 / 4 / 27 | 8 / 4 / 27 |
| R03 Moral standard and responsibility | F05 | F | 5 / 4 / 23 | 6 / 4 / 24 | 5 / 4 / 23 |
| R04 Productive tension | F03 | I | 6 / 3 / 11 | 6 / 3 / 12 | 7 / 3 / 13 |
| R05 Ties, coordination and capability | F13, plus Brennecke et al. from F02 | M | 3 / 2 / 14 | 2 / 1 / 22 | 4 / 2 / 31 |
| R06 Democracy and participation | F12 | D | 3 / 2 / 29 | 4 / 2 / 31 | 3 / 2 / 29 |
| R07 Sustainability and ecological dependence | F06 without crisis response | the sustainability half of G | 5 / 3 / 31 | G 5 / 4 / 36 | 3 / 2 / 26 |
| R08 Organization as actor | F11 | the organizationality half of A | 3 / 2 / 24 | A 7 / 4 / 33 | 3 / 2 / 24 |
| R09 Legitimacy and public contestation | F09 | C and L | 4 / 2 / 18 | C 6 / 3 / 20; L 3 / 0 / 3 | 4 / 2 / 18 |
| R10 Futures and imagination | F10 | the futures half of G | 3 / 2 / 14 | G 5 / 4 / 36 | 3 / 2 / 14 |
| R11 Digital technology | F08 | J | 4 / 1 / 8 | 4 / 1 / 8 | 4 / 1 / 8 |
| R12 Inequality and exclusion | F07 | E | 4 / 1 / 7 | 6 / 1 / 8 | 4 / 1 / 7 |
| Thread T1, Time and history | F02 | H | 6 / 4 / 33 | 9 / 5 / 33 | not a stack |
| Residual group, Affect and the self | F14 | N | 1 / 0 / 2 | 1 / 0 / 2 | not a stack |

## Disagreements and rulings

Triples give pieces / core pieces / questions, for 2025–26 first and for 2023–24 after the semicolon where both are given.

| # | Disagreement | What F did | What O did | What I kept | Why |
|---|---|---|---|---|---|
| 1 | Is time a stack? | Stack F02, Time and history (6 / 4 / 33 in 2025–26; 9 / 0 / 11 in 2023–24). Sixteen of Brennecke et al.'s 21 questions sit there alone. Named it the third prevailing concern. | Stack H, Time and trajectory (9 / 5 / 33; 11 / 0 / 13), with 41 of its 46 questions also filed elsewhere. Ranked it first by the rule and then set it aside as "the shared dimension of A and B". | A cross-cutting thread, T1. Brennecke et al.'s questions go to R05, where O had them. | All 57 questions that either analyst flagged as temporal also ask about an object that has its own stack: a tie, an institution, a legitimacy test, a collective's actorhood. None falls to the residual. No piece before 2025 is core to it in either analyst's table. A stack defined by a dimension would count the same papers twice near the top of the ranking. The cost is stated under T1: as a stack it would rank fourth on the 33 questions both analysts flagged (6 / 3 / 22) and level with R01 on the 57 either flagged (9 / 6 / 44). |
| 2 | One unit question or two? | Two stacks: F04 keeps the whole person-institution exchange with institutions and logics; F11 holds organization as actor. | Stack A joins organizationality, "can a person be an institution" and "what counts as a logic" (7 / 4 / 33); stack B holds institutional dynamics (6 / 6 / 41). Most person-institution questions sit in both. | F's two stacks, R01 and R08. | The two exchanges run in different literatures and share no piece. What O saw across them is a shared form of question, "what counts as an X", which also covers the demos and the stakeholder. I report it as thread T2. |
| 3 | Contestation: one stack or two? | One stack, F09, joining legitimacy tests, scandal and social movements (4 / 2 / 18; 5 / 2 / 50). | Two: C, Legitimacy under contestation (6 / 3 / 20; 4 / 2 / 18), and L, Activism and resistance (3 / 0 / 3; 9 / 2 / 44). L clears the bar on three single questions. | One stack, R09, with the movements agenda reported inside it as fading. | L has no core piece and three questions in 2025–26, and two of the three are asked by the legitimacy and democracy papers. Within R09 the questions O filed under L number 36 in 2023 and two since (side run: 2 / 0 / 2 in 2025–26). I did not carry O's L filings for resistance at work (Jaser and Tourish, Stark and Vanden Broeck, Hinds and von Krogh, Justesen and Plesner), which ask about technology. |
| 4 | Futures, sustainability, crisis | Two stacks: F10, Futures and imagination (3 / 2 / 14), and F06, Shared emergencies (5 / 3 / 31), which joins sustainability change, ecological dependence and crisis response. | One stack, G, Imagined and sustainable futures (5 / 4 / 36). No crisis thread; Kalkman's questions sit in the moral stack only. O doubted the placement of Corver and Filler. | Two stacks, R10 and R07. Kalkman's five crisis-management questions stay in R03 only. | Porsfelt et al. and Skade ask nothing about sustainability, and Corver and Filler ask nothing about futures. Two questions link the halves in 2025–26 (OQ-skade2025-02, OQ-friedrich2026-11). Merged, the stack would hold 5 / 4 / 40 and rank second as a composite of four single-paper threads. With Kalkman's five questions R07 would hold 4 / 3 / 31. |
| 5 | Affect and the self | Stack F14 (1 / 0 / 2; 12 / 3 / 25), reported as near-fading and kept out of the live ranking. | Stack N (1 / 0 / 2; 16 / 4 / 33), "fading in effect". | No stack. Of the 38 questions either analyst filed there, 27 keep the other stack they already had and 11 go to the residual. | Two questions since 2024, both from Friedrich and both about attunement to more-than-human life, which is R07's question. The ceiling of twelve stacks forced a choice, and this stack has no 2025–26 support of its own. |
| 6 | What the coordination stack holds | F13, Coordination and capability (3 / 2 / 14; 9 / 6 / 50): Guercini and Lechner on competence, du Gay and Lopdrup Hjorth on formal design, all eight of Garud et al., five of Brennecke et al. | M, Coordination and relations (2 / 1 / 22; 4 / 3 / 28): all 21 of Brennecke et al., none of Garud et al., Guercini and Lechner residual, du Gay and Lopdrup Hjorth under A. | One stack, R05: Brennecke et al. whole (from O); Garud et al., Guercini and Lechner, du Gay and Lopdrup Hjorth (from F). | Each analyst's filing fits the stack's question, which asks how collective work is put together through ties, designs and skills. Row 1 settles where Brennecke et al. sit. |
| 7 | How freely to file a second stack | 207 questions in two stacks. Filed questions about power under inequality. | 223 in two stacks. Filed method calls under theory and any resistance under activism. | 134 in two stacks. | Rule 4. Where one analyst alone added a second stack I kept it 36 times and dropped it 51 times; where the two added different second stacks I kept the shared one (14 cases, four of them together with the one second filing that the quotation plainly supports). |
| 8 | Residual | Seven questions. | Eleven, among them all nine of Guercini and Lechner and OQ-garud2025-09. | Fifteen, all from 2023–24. | F's seven stay. Guercini and Lechner and OQ-garud2025-09 go to R05. Eleven questions are what remains of Affect, and three of those were already in F's residual. |
| 9 | Status and rank | Applied the three-piece bar and found 13 of 14 stacks prevailing. Ranked by pieces. | Same bar, 12 of 14 prevailing. Ranked by pieces, then judged by deep pieces. | Rank by core pieces, then questions. The bar stays as a column. | Both analysts said the bar cannot separate the stacks, because one rider line counts a piece. |

The analysts agree on the size of technology: F08 and J each hold 4 / 1 / 8 in 2025–26 against 11 core pieces before, with 123 questions in F's table and 125 in O's. R11 keeps the same eight recent questions.

**Question-level rulings.** The 159 rulings fall into five kinds. Thirty-seven follow from a stack-level ruling above (code a). Thirty-six keep one analyst's second filing (b) and 51 drop it (c). Fourteen are cases where the analysts' second filings differ (d). Twenty-one are cases where their filings do not overlap at all and I ruled by reading (e). Fifty-four of the rulings concern 2025–26 questions; 26 of those only move Brennecke et al., Garud et al., Kalkman and OQ-dion2025-07 as rows 1, 4 and 6 require.

## Ranked map

| Rank | Stack | Core pieces 2025–26 | Questions 2025–26 (share) | In this stack only | Pieces 2025–26 | Core pieces 2023–24 | Questions 2023–24 (share) | Pieces 2023–24 | First authors | Last ask | Editorial | Bar: ≥3 pieces 2025–26 | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | R01 Institutions and logics | 6 | 44 (20%) | 41 | 6 | 7 | 51 (13%) | 7 | 13 | 2025-12-23 | none | met | prevailing; persistent |
| 2 | R02 Theory and theorizing | 4 | 27 (12%) | 21 | 8 | 9 | 54 (14%) | 14 | 22 | 2026-09-19 | `hollerer2026`, `cornelissen2024` | met | prevailing; persistent |
| 3 | R03 Moral standard and responsibility | 4 | 23 (10%) | 17 | 5 | 1 | 9 (2%) | 5 | 10 | 2026-09-19 | none | met | prevailing; persistent on one earlier core piece |
| 4 | R04 Productive tension | 3 | 13 (6%) | 0 | 7 | 3 | 31 (8%) | 4 | 11 | 2026-07-28 | none | met | prevailing by the count, with no question of its own; persistent |
| 5 | R05 Ties, coordination and capability | 2 | 31 (14%) | 26 | 4 | 5 | 46 (12%) | 7 | 11 | 2026-07-28 | none | met | persistent |
| 6 | R06 Democracy and participation | 2 | 29 (13%) | 16 | 3 | 3 | 23 (6%) | 5 | 8 | 2026-07-28 | none | met | persistent |
| 7 | R07 Sustainability and ecological dependence | 2 | 26 (12%) | 13 | 3 | 1 | 3 (1%) | 1 | 4 | 2026-07-28 | none | met | persistent by the letter; nearest to new |
| 8 | R08 Organization as actor | 2 | 24 (11%) | 19 | 3 | 1 | 7 (2%) | 5 | 8 | 2026-09-19 | none | met | persistent; rising |
| 9 | R09 Legitimacy and public contestation | 2 | 18 (8%) | 12 | 4 | 2 | 50 (13%) | 5 | 9 | 2026-03-31 | none | met | persistent |
| 10 | R10 Futures and imagination | 2 | 14 (6%) | 10 | 3 | 1 | 13 (3%) | 3 | 6 | 2026-09-21 | none | met | persistent |
| 11 | R11 Digital technology | 1 | 8 (4%) | 1 | 4 | 11 | 123 (32%) | 14 | 18 | 2026-04-01 | `cornelissen2024` | met | fading in effect |
| 12 | R12 Inequality and exclusion | 1 | 7 (3%) | 2 | 4 | 5 | 50 (13%) | 13 | 17 | 2026-06-19 | none | met | fading in effect |
| – | T1 Time and history (thread; the questions both analysts flagged) | 3 | 22 (10%) | – | 6 | 0 | 11 (3%) | 9 | 15 | 2026-09-19 | none | – | thread, not ranked |

Shares are of the period's questions (221 and 384). A question in two stacks counts in both. "In this stack only" counts the 2025–26 questions that have no second stack. The thread row comes from the side run described under T1 and has no rank.

## What prevails, what persists, what fades

**Prevailing now.** Three concerns prevail without qualification, and they are the three that both analysts named.

1. **R01 Institutions and logics.** Six pieces, every one core, and 44 questions, a fifth of the period, 41 of them asked nowhere else. Two limits apply. Three of the six pieces are one exchange about whether a person can be an institution, and it supplies 30 of the 44 questions. All six pieces date from 2025, the last from 23 December; no 2026 piece asks this question.
2. **R02 Theory and theorizing.** Eight pieces, four core, 27 questions. The 2026 editorial is one of the four, and the stack is the only one that an editorial asks in both periods.
3. **R03 Moral standard and responsibility.** Five pieces, four core, 23 questions, every one from 2026. In 2023–24 it had one core piece and nine questions.

A fourth clears the threshold with a qualification. **R04 Productive tension** has three core pieces among seven and 13 questions, and not one of the 13 sits in this stack alone. Papers on democracy, futures, modeling, logics and legitimacy borrow its question; only Keller, Berti and Smith still ask it inside paradox theory.

Below these sit six concerns with two core pieces each: R05 (31 questions), R06 (29), R07 (26), R08 (24), R09 (18) and R10 (14). Each is two papers deep. In R05 and R06 one paper supplies most of the questions (Brennecke et al. 21 of 31; Mena et al. 23 of 29). Three of the six grew: R07 from 3 questions to 26, R08 from 7 to 24, and R06 from 23 to 29 in a smaller period.

Time and history is the strongest thread and would be a prevailing stack under either analyst's filing. T1 gives its counts and the reason I did not rank it.

**Persistent, 2023 to 2026.** All twelve stacks have at least one core piece in each period. Six have two or more in both: R01 (6 now, 7 before), R02 (4, 9), R04 (3, 3), R05 (2, 5), R06 (2, 3) and R09 (2, 2). Four rest on a single earlier core piece and have deepened since: R03 (4, 1), R07 (2, 1), R08 (2, 1) and R10 (2, 1). Persistence of the stack does not mean persistence of the object. In R04, R05, R09 and R10 the 2025–26 askers ask about something else than the 2023–24 askers did, as the entries show.

**Fading in effect.** Two stacks meet the test. **R11 Digital technology** went from 14 pieces, 11 of them core, and 123 questions (32% of the period) to four pieces, one core, and 8 questions (4%); one of the eight sits in the stack alone. **R12 Inequality and exclusion** went from 13 pieces, 5 core, and 50 questions to four pieces, one core, and 7 questions. Both still clear the three-piece bar, on riders. Affect and the self has faded further, to two questions, and is no longer a stack (ruling 5).

**New.** No stack is new by the letter. R07 comes nearest: one earlier piece gave it three questions, and 25 of its 26 recent questions date from 2026.

## Time paths

Questions per year, by the piece's published-online date. The base row gives all questions and pieces, so that a fall from 2024 to 2026 can be read against a journal that published 205 questions in 2024 and 103 in the first nine months of 2026.

| Stack | 2023 | 2024 | 2025 | 2026 | Reading |
|---|---|---|---|---|---|
| R01 Institutions and logics | 41 | 10 | 44 | 0 | every recent question dates from 2025 |
| R02 Theory and theorizing | 17 | 37 | 9 | 18 | asked in all four years |
| R03 Moral standard and responsibility | 5 | 4 | 0 | 23 | every recent question dates from 2026 |
| R04 Productive tension | 3 | 28 | 9 | 4 | peaked in 2024 with the paradox pieces |
| R05 Ties, coordination and capability | 14 | 32 | 29 | 2 | 29 of 31 recent questions from 2025 |
| R06 Democracy and participation | 15 | 8 | 0 | 29 | every recent question dates from 2026 |
| R07 Sustainability and ecological dependence | 0 | 3 | 1 | 25 | 25 of 26 recent questions from 2026 |
| R08 Organization as actor | 2 | 5 | 14 | 10 | both recent years |
| R09 Legitimacy and public contestation | 48 | 2 | 17 | 1 | 2023 is the movements review; 2025 is legitimacy and post-truth |
| R10 Futures and imagination | 0 | 13 | 7 | 7 | both recent years |
| R11 Digital technology | 27 | 96 | 5 | 3 | 96 questions in 2024, 8 since |
| R12 Inequality and exclusion | 25 | 25 | 2 | 5 | 50 questions in 2023–24, 7 since |
| T1 Time and history (thread) | 2 | 9 | 21 | 1 | a 2025 event |
| *All questions* | 179 | 205 | 118 | 103 | base |
| *All pieces* | 19 | 22 | 14 | 10 | base |

## The stacks

Question numbers are the two-digit suffixes of the ids, so `mena2026` 08 is OQ-mena2026-08. A star marks a core piece. Each count table comes from the scripts named in rule 6.

### R01 Institutions and logics

**Concern.** How do institutions and logics come to exist, hold and change, and what may count as one?

**Now (2025–26).** The askers test the unit. Nigam, Amis and Logue ask why, how, when and for how long a person can become an institution, and how such an institution outlives its person or a formal office (OQ-nigam2025-11, -06, -07). Derek Robinson and Atanasova ask which conditions make a person-brand institutional, which criteria mark its stages and whether the process can reverse (OQ-derekrobinson2025-07, -10, -12). Hawbaker and Hallett answer that persons should stay distinct from institutions so that the relation between the two can be studied (OQ-hawbaker2025-03). Schildt and Kodeih ask what counts as a logic and how stable macro ideology arises from local practice (OQ-schildt2025-02, -03). Mutch asks how practices pass between law and organizations, and Wedlin and Weinryb ask what hype does to institutions (OQ-mutch2025-03; OQ-wedlin2025-03).

**Before (2023–24).** The askers asked about process and mechanism. Powell and DiMaggio asked how new practices enter organizations and stick, what exactly diffuses, and which parts of organizations yield to isomorphic pressure (OQ-powell2023-09, -02, -01). Jackwerth-Rice, Koehrsen and Mattes asked whether the sufficiency of an entrepreneur's resources can be known in advance (OQ-jackwerthrice2023-09). Georgiou and Arenas, Stevenson and colleagues, and Godart and Wittman asked about the community logic, the centrality of logics and purity (OQ-georgiou2023-04; OQ-stevenson2024-01; OQ-godart2024-02). Orlikowski and Scott asked how digitalization displaces institutions, and Ocasio warned that institutional explanations may be overused (OQ-orlikowski2023-01; OQ-ocasio2023-04).

**Has the object moved?** Yes, from process to unit. The verbs are the same in both periods: emerge, persist, change. The 2025–26 subject is a candidate whose standing is itself in doubt, whether a person, a body of law, a hype or a constellation of practices.

**Anchors (2025–26).**

- **OQ-nigam2025-11** "We hope that others will take on these ideas and push forward why, how, when and for how long individuals can become institutions." (p. 9, "Conclusion")
- **OQ-hawbaker2025-03** "If we can identify individuals as something other than institutions we can more cogently examine the relationships between those things and institutions, without making every(one) an institution." (p. 9, "Discussion")
- **OQ-schildt2025-02** "what exactly counts as a logic?" and "how do we draw the boundaries of an institutional logic?" (p. 16, "Towards a more dynamic and local view")
- **OQ-mutch2025-03** "Recognizing law as a central institutional logic directs our attention to the possibility for practices to be transferred from the legal to the organizational domain (and vice versa)." (p. 13, "Conclusion")

**Context (2023–24).**

- **OQ-powell2023-09** "How do new ideas and practices enter organizations and stick? Why do new kinds of institutions emerge, take root, and persist? When are organizations more vulnerable to changes in the wider environment and when are they resisted?" (p. 15, "Institutional change")
- **OQ-ocasio2023-04** "institutional explanations may be overused, and other factors such as power, status, demography, resource dependencies, cognition, emotions, identity, and meaning have effects that are not reducible to institutions" (p. 15, "The ubiquity of institutions and their limits")
- **OQ-jackwerthrice2023-09** "the sufficiency of resources is still a theoretical black box: can it be known ex ante or only in retrospect which actors dispose of sufficient resources for institutional entrepreneurship?" (p. 15, "Discussion and Conclusion")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 6 | 7 |
| Core pieces | 6 | 7 |
| Questions (share of the period) | 44 (20%) | 51 (13%) |
| Questions in this stack only | 41 | 39 |

First authors: 13. Last ask: 2025-12-23 (`derekrobinson2025`, `wedlin2025`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `wedlin2025`★ 2/2; `derekrobinson2025`★ 15/15; `nigam2025`★ 11/11; `hawbaker2025`★ 4/4; `mutch2025`★ 6/6; `schildt2025`★ 6/6.

Backing pieces, 2023–24: `godart2024`★ 5/5; `stevenson2024`★ 5/5; `powell2023`★ 13/14; `ocasio2023`★ 4/4; `jackwerthrice2023`★ 10/10; `orlikowski2023`★ 3/7; `georgiou2023`★ 11/11.

**Status.** Prevailing and persistent, with core pieces in both periods (6 and 7). No ask since December 2025.

### R02 Theory and theorizing

**Concern.** What should count as theory and as a contribution in organization studies, and how should scholars, editors and reviewers go about producing it?

**Now (2025–26).** The askers turn on the conventions that police theory. The editors want themed sections that look beyond existing conventions and submissions that state what kind of contribution they make (OQ-hollerer2026-02, -06). Ernst, Lassalle, Kerr and Robinson ask how field orthodoxies define good theory, call on editors and reviewers to counteract field biases, and ask whether inquiry can stay apart from political and economic crisis (OQ-ernst2026-03, -06, -07). Giovannoni and Quattrone ask for a theory founded on the unknowable, for reviewers who accept open-ended work, and for methods that study absences without filling them (OQ-giovannoni2025-03, -07, -10). Keller, Berti and Smith apply paradox theory to the theorist's own work (OQ-keller2025-01). Four more pieces add a line or two each, among them questions on how a model reaches practice, on agreed foundations and on explicit ontological postures (OQ-corver2026-07; OQ-schoeneborn2026-02; OQ-dion2025-13).

**Before (2023–24).** The askers argued over the word and over a new tool. Abend, Suddaby and Prasad debated who decides what "theory" means and what it is for (OQ-abend2024-03, -04; OQ-suddaby2024-03; OQ-prasad2024-06). The editors asked whether large language models can theorize and required authors to disclose them (OQ-cornelissen2024-04, -06, -08). Gümüsay and Reinecke asked how the academic system must change to admit imagination and values (OQ-gumusay2024-11). Lantela asked whose voice has counted as theory (OQ-lantela2024-09). Wright and colleagues, and Petriglieri and Ashford, asked what the researcher's self does to theorizing (OQ-wright2023-06; OQ-petriglieri2023-02).

**Has the object moved?** Yes, from the definition of theory to the gatekeeping of it. The 2025–26 askers address editors and reviewers by role, and the 2026 editorial itself asks for work that breaks convention. The 2024 editorial's question about machine theorizing has no asker in 2025–26.

**Anchors (2025–26).**

- **OQ-hollerer2026-02** "Proposals for–and the resulting special themed sections–should, as mentioned, explicitly look beyond existing conventions and push beyond the boundaries of theoretical knowledge in our domain of scholarly inquiry." (p. 5, "'Catalysing & Crystallizing'")
- **OQ-ernst2026-03** "scholars could, as part of their reflexive research practices, benefit from paying attention to how orthodoxies in the field define what is currently considered good theory" (p. 15, "Theory generation in OS")
- **OQ-giovannoni2025-07** "And, of course, the institutional environment, comprising editors, reviewers and readers, would have to support and accept the integrity and fruitfulness of such efforts (rather than asking for them to be reframed in specific substantial terms, i.e. as ‘thing’)." (p. 15, "Discussion")
- **OQ-keller2025-01** "We invite future scholarship to continue to explore how paradox theory applies to our own work as scholars and theorists." (p. 16, "Discussion")

**Context (2023–24).**

- **OQ-abend2024-04** "Fellow community members! Which aims should be served by our key words and distinctions? Which aims are more important to us, when, and where?" (p. 7, "5. Democracy, Unfreedom, Usefulness")
- **OQ-cornelissen2024-04** "Rather, it is imperative that we engage in a debate about the implications of this potentially disruptive technology for our theorizing and for the kinds of knowledge that we in turn create about our various phenomena of interest." (p. 3, untitled introduction)
- **OQ-lantela2024-09** "who has been the legitimate theoretical voice within a specific sub-field, and why? What kind of bodies have been able to theorize?" (p. 12, "Conclusion")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 8 | 14 |
| Core pieces | 4 | 9 |
| Questions (share of the period) | 27 (12%) | 54 (14%) |
| Questions in this stack only | 21 | 33 |

First authors: 22. Last ask: 2026-09-19 (`schoeneborn2026`). Editorial: `hollerer2026`, `cornelissen2024`. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `schoeneborn2026` 1/10; `corver2026` 2/12; `hollerer2026`★ 6/6; `ernst2026`★ 8/8; `friedrich2026` 1/17; `dion2025` 2/13; `giovannoni2025`★ 5/7; `keller2025`★ 2/2.

Backing pieces, 2023–24: `suddaby2024`★ 5/5; `prasad2024`★ 4/4; `abend2024`★ 7/7; `phillips2024` 2/12; `lantela2024`★ 8/8; `gumusay2024`★ 4/12; `cornelissen2024`★ 7/7; `wright2023`★ 5/5; `powell2023` 1/14; `jorgensen2023` 2/5; `orlikowski2023` 1/7; `fotaki2023` 1/5; `petriglieri2023`★ 4/4; `laine2023`★ 3/7.

**Status.** Prevailing and persistent, with core pieces in both periods (4 and 9) and an editorial in each.

### R03 Moral standard and responsibility

**Concern.** By what moral standard should organizations act and be judged, and who answers for what they do?

**Now (2025–26).** Three 2026 pieces make it their object, and a fourth gives it three questions. Werner, Cornelissen and Turkenburg ask how an organization's reasoning beyond its prescribed obligations can be judged case by case, whether organizations differ in moral scope, and whether some hold a calling (OQ-werner2026-10, -03, -04). Kalkman proposes care as the purpose of crisis management, invites rival normative purposes, and asks what a care-based purpose produces and when a crisis prompts moral reflection (OQ-kalkman2026-01, -06, -03). Pavlisa, Harvey and Doh admit that they lack criteria for which stakeholders fall outside a firm's responsibility (OQ-pavlisa2026-03). Friedrich asks how care for more-than-human others is attended to and resourced (OQ-friedrich2026-13, -10). Schoeneborn, Dobusch and Seidl ask what shifting actorhood does to individual and collective responsibility (OQ-schoeneborn2026-06).

**Before (2023–24).** The question came as a rider on other programmes. Only Fotaki's piece on care is core (OQ-fotaki2023-03, -06). Seidemann asked how responses to paradox are to be judged normatively (OQ-seidemann2024-08). Stark and Vanden Broeck asked who is accountable for algorithmic decisions (OQ-stark2024-04). Jaser and Tourish asked what kind of managers and workers people want to be, and Scherer and Neesham proposed revising the MBA oath (OQ-jaser2024-04; OQ-scherer2023-06).

**Has the object moved?** Yes, from rider to object. The 2023–24 askers demanded that norms be brought in. The 2026 askers bring them in and then ask for the criteria of judgment, scope and responsibility that their own proposals lack, and for empirical tests.

**Anchors (2025–26).**

- **OQ-werner2026-10** "Another question that further normative research might explore is how, when organizations deliberate beyond institutionally prescribed norms and obligations, this can be ethically judged in specific instances and cases." (pp. 21–22, "Theoretical and research implications")
- **OQ-kalkman2026-01** "Scholars can propose other normative approaches to continue the debate or provide an ethical defense of current approaches." (p. 14, "Theoretical Implications")
- **OQ-pavlisa2026-03** "As a limitation, our theorisation inherits the boundary conditions of stakeholder governance literature, lacking robust criteria for determining which stakeholders are beyond the scope of a firm’s responsibility" (p. 18, "Discussion")
- **OQ-schoeneborn2026-06** "What does the recurrent charging or discharging of a collective social address with actorhood imply for individual as opposed to collective responsibility?" (p. 14, "Conclusion and Research Agenda")

**Context (2023–24).**

- **OQ-seidemann2024-08** "Expanding on the predominantly strategic perspective of paradox management, the question of how responses to paradoxes are evaluated from a normative standpoint becomes central." (p. 17, "Purposefully integrating normative approaches")
- **OQ-fotaki2023-03** "it is vital to theorize how power asymmetries among genders, races, ethnicities and social classes within and across geographical locales shape care relations, forms of care, and experiences of caring and being cared for in fundamental ways" (p. 14, "Discussion")
- **OQ-stark2024-04** "But who or what is accountable when an algorithm exercises decisions that occur faster and with a vastly larger number of inputs than a human can physiologically comprehend and react to (Vesa & Tienari, 2022, p. 1137)?" (p. 14, "Accountability")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 5 | 5 |
| Core pieces | 4 | 1 |
| Questions (share of the period) | 23 (10%) | 9 (2%) |
| Questions in this stack only | 17 | 2 |

First authors: 10. Last ask: 2026-09-19 (`schoeneborn2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `schoeneborn2026` 1/10; `kalkman2026`★ 8/8; `pavlisa2026`★ 3/5; `werner2026`★ 8/8; `friedrich2026`★ 3/17.

Backing pieces, 2023–24: `seidemann2024` 2/16; `stark2024` 1/9; `jaser2024` 1/10; `scherer2023` 1/10; `fotaki2023`★ 4/5.

**Status.** Prevailing. Persistent on one earlier core piece. Every recent question dates from 2026.

### R04 Productive tension

**Concern.** When are contradiction, paradox and disagreement productive, and when should they be settled, chosen between or refused?

**Now (2025–26).** Seven pieces ask, each briefly, and six of them outside paradox theory. Mena, Mair and Bruder ask when dissent stays productive and when consensus or dissensus can be dispensed with (OQ-mena2026-08, -07, -22). Skade asks how divergent futures create productive tensions (OQ-skade2025-01, -02). Corver and Filler ask how disagreement enables modeling (OQ-corver2026-16). Schildt and Kodeih ask about contradiction within a single logic (OQ-schildt2025-06). Winkler and Schoeneborn ask that dis/organization be read as escalation as well as equilibrium, and Patriotta, Augustine and Voronov mark where irreconcilable values block settlement (OQ-winkler2025-05; OQ-patriotta2025-12). Only Keller, Berti and Smith stay inside paradox theory, and they turn it on theorists (OQ-keller2025-01, -02).

**Before (2023–24).** Two 2024 pieces carried a research programme's questions about itself. Krautzberger and Tuckermann asked how organizations steer a portfolio of both/and and either/or responses and how that fails (OQ-krautzberger2024-03, -12). Seidemann asked where both/and stops working, why organizations breed paradoxes, and whether a weak paradox is still one (OQ-seidemann2024-11, -02, -16). Georgiou and Arenas, and Stark and Vanden Broeck, added conflict between logics and contradiction within algorithmic management (OQ-georgiou2023-08; OQ-stark2024-05).

**Has the object moved?** Yes, from a programme to a borrowed question. Width grew from four pieces to seven while depth fell from 31 questions to 13, and none of the 13 has this stack as its only home.

**Anchors (2025–26).**

- **OQ-mena2026-08** "How can we ensure that dissent remains continuously productive and does not become destructive, for example, by deepening fractures among organizational members or even leading to organizational death?" (p. 12, "Agonistic internal focus")
- **OQ-skade2025-01** "future research could clarify how these divergent futures inform strategic decisions and create productive tensions within organizations." (p. 18, "Tensions between futures")
- **OQ-corver2026-16** "How such disagreement and the conditions surrounding them, both within and across these groups, feeds into, and perhaps even enables, productive modeling deserves further attention in future research." (p. 18, "Discussion")
- **OQ-schildt2025-06** "We hope our practice-centric perspective on institutional logics can inspire scholars to study contradictions, variations, and change also within a single institutional logic." (p. 17, "Concluding remarks")

**Context (2023–24).**

- **OQ-seidemann2024-11** "I recommend that paradox scholars empirically explore the boundary conditions of both/and for different classes of phenomena at different levels of analysis and the potential negative ramifications of embracing tensions." (p. 18, "Developing a more granular perspective")
- **OQ-krautzberger2024-03** "First, future research could investigate how to effectively navigate a portfolio of both/and and either/or approaches to paradoxes in various contexts." (p. 19, "Directions for future research")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 7 | 4 |
| Core pieces | 3 | 3 |
| Questions (share of the period) | 13 (6%) | 31 (8%) |
| Questions in this stack only | 0 | 24 |

First authors: 11. Last ask: 2026-07-28 (`corver2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `corver2026` 1/12; `mena2026`★ 3/23; `winkler2025` 1/5; `patriotta2025` 1/11; `skade2025`★ 4/7; `keller2025`★ 2/2; `schildt2025` 1/6.

Backing pieces, 2023–24: `krautzberger2024`★ 11/11; `seidemann2024`★ 16/16; `stark2024` 1/9; `georgiou2023`★ 3/11.

**Status.** Prevailing by the count of core pieces, persistent with three core pieces in each period. It is wide and shallow: it works in 2025–26 as a question other concerns ask, close to a thread.

### R05 Ties, coordination and capability

**Concern.** How is collective work put together and held together: through which ties, designs, spaces, routines and skills?

**Now (2025–26).** Two 2025 pieces carry the stack, and both ask through time. Brennecke, Carnabuci and Ertug ask 21 questions about the history of network ties: which features of a tie's past are retained, which trajectories make a tie brittle, how a tie's path affects brokerage and creative exchange, and how dyadic histories build network structure (OQ-brennecke2025-12, -10, -02, -17, -15). Garud, Turunen and Karunakaran ask which arrangements trigger which notion of time, how organizing for innovation runs as a multi-temporal distributed process, and what alternatives to the dominant structuring themes organizations might try (OQ-garud2025-03, -05, -09). Two papers add a line each on design: whether novel governance structures prevent managerial authority, and how modeling capacities are spread across roles (OQ-mena2026-05; OQ-corver2026-11).

**Before (2023–24).** The askers asked about coordinating mechanisms as such. Räcker, Geiger and Seidl asked which spatial configurations occur and how space, roles and routines interact (OQ-racker2024-08, -10). du Gay and Lopdrup Hjorth asked which formalization each purpose needs and put formal design back at the centre (OQ-dugay2024-02, -04). Guercini and Lechner asked how competence is learned and lost (OQ-guercini2023-08, -09). Hinds and von Krogh asked what generative AI does to coordination and to the division of labour, and Whyte, Comi and Mosca asked how coherence is made across online and offline practices (OQ-hinds2024-05, -16; OQ-whyte2023-14).

**Has the object moved?** Yes, from mechanism to history. Space, formal design and competence have no asker in 2025–26. What the recent pieces ask is how the past of a tie or the timing of an arrangement shapes joint work, and 29 of the 31 recent questions date from 2025.

**Anchors (2025–26).**

- **OQ-brennecke2025-12** "Which features of relational history are retained, which decay over time? When do narratives about a tie crystallize into dominant accounts that guide behaviour? Under what conditions do memories of key events become shared across both parties" (p. 19, "Cognitive and narrative construction of relational history")
- **OQ-brennecke2025-15** "Hence, future work should pursue designs that link historical features of dyadic ties to enduring properties of network structure." (p. 20, "Relational history and broader network structures")
- **OQ-garud2025-03** "they illustrate how different kinds of organizational arrangements can trigger different notions of time, a topic worthy of further investigation." (p. 12, "Organizing for Ongoing Innovation at Work")
- **OQ-mena2026-05** "How do novel organizational governance structures prevent the type of hierarchical and managerial authority that is prevalent in traditional organizational structures such as bureaucracies?" (p. 11, "Republican internal focus")

**Context (2023–24).**

- **OQ-racker2024-10** "Thus, we need to better understand how different coordinating mechanisms (here: roles, space, routines) interact in achieving successful integration." (p. 13, "Interrelations")
- **OQ-dugay2024-02** "the crucial question remains which kinds of formalization are necessary for each of them to pursue their respective, and very different, purposes in the most requisite manner." (p. 10, "Formality and Authority")
- **OQ-hinds2024-16** "as progressive encapsulation evolves across levels and functions in organizations, how does the process shape the division of labor?" (p. 10, "Discussion")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 4 | 7 |
| Core pieces | 2 | 5 |
| Questions (share of the period) | 31 (14%) | 46 (12%) |
| Questions in this stack only | 26 | 23 |

First authors: 11. Last ask: 2026-07-28 (`corver2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `corver2026` 1/12; `mena2026` 1/23; `brennecke2025`★ 21/21; `garud2025`★ 8/8.

Backing pieces, 2023–24: `hinds2024`★ 13/25; `hsu2024` 1/6; `phillips2024` 1/12; `racker2024`★ 12/12; `dugay2024`★ 5/5; `whyte2023`★ 5/13; `guercini2023`★ 9/9.

**Status.** Persistent, with core pieces in both periods (2 and 5). The stack is the home of most of thread T1.

### R06 Democracy and participation

**Concern.** How can organizing be democratic (who takes part, and on what terms), and what do organizations do to, and under, democracy in society?

**Now (2025–26).** Mena, Mair and Bruder ask 23 questions: who the demos is, whether workplace experiments scale to society, how right-wing tendencies and democratic backsliding bear on organizations, and how social media and AI shape deliberation (OQ-mena2026-01, -23, -21, -17, -12). Friedrich asks how democratic organizing can resist co-optation and extend to ecological others (OQ-friedrich2026-16, -15). Corver and Filler ask how co-creative modeling meets participatory governance (OQ-corver2026-05). All 29 questions date from 2026.

**Before (2023–24).** The askers asked about participation, often without naming democracy. Friesl, Brielmaier and Dobusch asked why some actors join open strategy and others abstain (OQ-friesl2023-03). Langenmayr and colleagues asked who is represented in strategy making (OQ-langenmayr2024-11, -01). Scherer and Neesham asked how organizing can foster mature citizens and named working organizations as sites for it (OQ-scherer2023-13, -11). Jaser and Tourish called for democratic oversight of surveillance (OQ-jaser2024-06).

**Has the object moved?** It sharpened. Democracy became the named object, and the link between the organization and the polity, in both directions, became the question. The 2026 papers do not take up participation in open strategy.

**Anchors (2025–26).**

- **OQ-mena2026-01** "who qualifies as the people (or demos; Koenig-Archibugi, 2022): employees, a larger set of organizational members and/or stakeholders, or a broader demos?" (p. 3, introduction)
- **OQ-mena2026-21** "How do right-wing tendencies at the country level shape democracy within organizations in this country, and how might organizational democracy influence such right-wing take-up?" (p. 19, "Cross-focal dynamics and spillover effects")
- **OQ-friedrich2026-16** "Little research has explored how democratic organizing can mitigate its vulnerabilities to ideological co-optation and, especially, how it might connect with ecological others while sustaining its power-sensitive and egalitarian potential." (p. 5, "Organizational Democracy’s Disconnects")
- **OQ-corver2026-05** "One open conceptual question, for instance, is how a more open, co-creative approach to modeling interacts with more democratic decision-making processes and participatory governance structures" (p. 17, "Discussion")

**Context (2023–24).**

- **OQ-scherer2023-13** "Organization theory and business ethics have a crucial role to play in advancing our understanding of how individual and collective human action can be further organized to foster the communicative conditions needed for mature citizens" (p. 21, "Conclusion")
- **OQ-friesl2023-03** "Unveiling the social processes underpinning self-selection allows future research to study why certain actors participate in open strategy or why they abstain from doing so." (p. 13, "Discussion and Theoretical Implications")
- **OQ-jaser2024-06** "The need to exercise democratic oversight and restraint must be reasserted, through collective action, ideological struggle against the managerialist tenets of neoliberalism and, where necessary, legislative fiat." (p. 16, "Discussion")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 3 | 5 |
| Core pieces | 2 | 3 |
| Questions (share of the period) | 29 (13%) | 23 (6%) |
| Questions in this stack only | 16 | 11 |

First authors: 8. Last ask: 2026-07-28 (`corver2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `corver2026` 1/12; `friedrich2026`★ 5/17; `mena2026`★ 23/23.

Backing pieces, 2023–24: `langenmayr2024`★ 6/11; `gumusay2024` 1/12; `jaser2024` 1/10; `scherer2023`★ 8/10; `friesl2023`★ 7/7.

**Status.** Persistent, with core pieces in both periods (2 and 3). One paper supplies 23 of the 29 recent questions.

### R07 Sustainability and ecological dependence

**Concern.** How do organizations act on sustainability problems and on their dependence on ecological others?

**Now (2025–26).** Two 2026 pieces carry it from different sides. Corver and Filler ask which modeling actions support successful sustainability problem-solving, whether problems move from discrete to interconnected, and whether their account carries to public and third-sector settings (OQ-corver2026-10, -06, -13). Friedrich asks how organizing can keep its dependencies on ecological others in view, how it can learn its own vulnerabilities, and how democratic organizing can connect with ecological others (OQ-friedrich2026-03, -05, -16). Giovannoni and Quattrone add one line on grand challenges beyond the SDGs (OQ-giovannoni2025-05).

**Before (2023–24).** One piece. Gümüsay and Reinecke asked how climate pathways would change organizing, how new methods of valuation would work, and which outcomes other than growth a theory could serve (OQ-gumusay2024-02, -04, -05).

**Has the object moved?** The question went from prospective to operational: from theorizing a desirable climate future to how organizations model, attune and change. Twenty-five of the 26 recent questions date from 2026.

**Anchors (2025–26).**

- **OQ-corver2026-10** "Future work also could more systematically map how particular modeling actions relate to concrete results, retrospectively identifying which of these actions in fact support successful sustainability problem-solving processes" (p. 17, "Discussion")
- **OQ-corver2026-06** "Do organizations typically move from addressing discrete, separate sustainability problems toward recognizing and managing increasingly interconnected ones" (p. 17, "Discussion")
- **OQ-friedrich2026-03** "How can organizing continually acknowledge and investigate material interstices and dependencies with ecological and social others" (p. 12, "Acknowledging assembled becoming")
- **OQ-friedrich2026-05** "What organizational measures can foster learning and recognition of the organization’s, members’, and stakeholders’ vulnerabilities to these natural, cultural, and technological dependencies" (p. 12, "Acknowledging assembled becoming")

**Context (2023–24).**

- **OQ-gumusay2024-02** "For instance, how would different climate pathways impact organizing differently, including the behaviour of people and institutions?" (p. 9, "Four modes of theorizing the future")
- **OQ-gumusay2024-05** "we could theorize practices and business models that maximize the conservation of scarce resources, reduction of GHG emissions, attainment of social impact or regeneration." (p. 13, "Theorizing Practices for the Double Leap into the Future")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 3 | 1 |
| Core pieces | 2 | 1 |
| Questions (share of the period) | 26 (12%) | 3 (1%) |
| Questions in this stack only | 13 | 0 |

First authors: 4. Last ask: 2026-07-28 (`corver2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `corver2026`★ 11/12; `friedrich2026`★ 14/17; `giovannoni2025` 1/7.

Backing pieces, 2023–24: `gumusay2024`★ 3/12.

**Status.** Persistent by the letter and the nearest thing in the set to a new concern. It rests on two papers. Under F's wider definition, which adds Kalkman's crisis-management questions, it would hold 4 / 3 / 31 (ruling 4).

### R08 Organization as actor

**Concern.** What makes a collective an organization, an actor in its own right, and should organization studies follow organizing beyond the formal organization?

**Now (2025–26).** One exchange supplies almost all of it. Schoeneborn, Dobusch and Seidl ask how loose collectives persist with little organizationality, which practices attribute actorhood and with what temporal pattern, and whether the perspective explains anything beyond formal organizations (OQ-schoeneborn2026-03, -07, -05, -10). Dion, Cooren and Dupuis ask what organizationality is a property of, what evidence would show organizations to be distinct, and whether the discipline should centre formal organizations at all (OQ-dion2025-14, -02, -04). Winkler and Schoeneborn add one invitation to look beyond the single organization (OQ-winkler2025-04).

**Before (2023–24).** Five pieces, mostly single provocations. Laine and Kibler asked whether an organization can exist while doing nothing (OQ-laine2023-02). Phillips, Kalvapalle and Kennedy asked what organizations are once artificial persons join them (OQ-phillips2024-09). Stark and Vanden Broeck proposed technology as organizational structure (OQ-stark2024-08). Georgiou and Arenas asked when communities become formal organizations (OQ-georgiou2023-09). du Gay and Lopdrup Hjorth pulled the other way, toward formal organization (OQ-dugay2024-04, -05, -07).

**Has the object moved?** Scattered provocations became a programme of 24 questions that asks for its own foundations. The counter-position, a return to formal organization, has no voice in 2025–26.

**Anchors (2025–26).**

- **OQ-dion2025-14** "When discussing organizationality, the following question should be asked: The organizationality of what?" (p. 16, "Conclusion")
- **OQ-dion2025-04** "[…] whether the said discipline should step forward and study organizationality unbound by liberal preoccupations for legally recognized 'moral agents' is another question." (p. 11, "A Fourth Tension") [contiguous excerpt; the input quotation runs to 48 words]
- **OQ-schoeneborn2026-03** "Our framework then raises follow-up questions, for instance, how loose and fluid social phenomena can sustain their existence despite a rather low degree of organizationality." (p. 13, "Dynamizing Organizationality")
- **OQ-schoeneborn2026-10** "An important task of future organizational scholarship will then be to demonstrate the extent to which this perspective on organizationality can yield explanatory value" (p. 14, "Conclusion and Research Agenda")

**Context (2023–24).**

- **OQ-laine2023-02** "Is it unthinkable for organization theory that different relational effects at a different time and in a different place still yield the same organization? Is it not possible for an organization to “not do” anything at all?" (p. 11, "For whom objects matter")
- **OQ-phillips2024-09** "How does the introduction of artificial persons into an organization change how we think about what organizations are, how they are constructed and how they function?" (p. 11, "The implications of generative AI in organizations")
- **OQ-dugay2024-05** "But perhaps our contemporary circumstances require the return of the categories and intellectual frameworks that for too long have been consigned to the dustbin of defunct and old-fashioned organizational devices." (p. 12, "Theoretical implications for organization theory")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 3 | 5 |
| Core pieces | 2 | 1 |
| Questions (share of the period) | 24 (11%) | 7 (2%) |
| Questions in this stack only | 19 | 1 |

First authors: 8. Last ask: 2026-09-19 (`schoeneborn2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `schoeneborn2026`★ 10/10; `dion2025`★ 13/13; `winkler2025` 1/5.

Backing pieces, 2023–24: `phillips2024` 1/12; `stark2024` 1/9; `dugay2024`★ 3/5; `georgiou2023` 1/11; `laine2023` 1/7.

**Status.** Persistent on one earlier core piece, and rising: 7 questions before 2025, 24 since.

### R09 Legitimacy and public contestation

**Concern.** How do publics, media and movements test and contest organizations, and how do such contests form, escalate and settle?

**Now (2025–26).** The askers study the contest itself. Patriotta, Augustine and Voronov ask what signals that an issue will escalate, how organizations pre-empt a test, how influencers, activists and platforms amplify one, and what happens in polarized settings (OQ-patriotta2025-05, -06, -09, -08, -04). Winkler and Schoeneborn ask organization scholars to take post-truth communication seriously, and they stop their model short of total takeover (OQ-winkler2025-02, -03). Giovannoni and Quattrone ask how rhetoric swings between logic and non-logic under populism (OQ-giovannoni2025-08). Mena, Mair and Bruder ask how organizations themselves challenge the status quo (OQ-mena2026-19).

**Before (2023–24).** The 2023 askers studied the challengers and the audiences. Leitzinger and Waeger asked 33 questions about social movements that target markets: how they form, when they are co-opted, whether they fade as markets mature (OQ-leitzinger2023-01, -16, -24). Pozner and Hannigan asked how publics become scandal audiences (OQ-pozner2023-04, -09). Godart and Wittman, and Powell and DiMaggio, asked which audiences an organization must satisfy and when a practice becomes mandatory for legitimacy (OQ-godart2024-03; OQ-powell2023-06).

**Has the object moved?** Yes, from who contests to how a contest runs when audiences are polarized and facts disputed. The movements-and-markets agenda has no asker in 2025–26: activists appear as one actor among several in a legitimacy test, and firms appear as challengers themselves.

**Anchors (2025–26).**

- **OQ-patriotta2025-05** "While our theory highlights that legitimacy tests are dynamic and processual, we know little about the early warning signs that indicate when an issue may escalate into a full-blown controversy versus blowing over." (p. 18, "Future research directions: Legitimacy in a changing world")
- **OQ-patriotta2025-09** "it is worth exploring how non-traditional actors, such as social media influencers, activists and whistleblowers, increasingly shape and amplify legitimacy tests by rapidly mobilizing audiences." (p. 19, "Future research directions: Legitimacy in a changing world")
- **OQ-winkler2025-02** "In this article we argue that PTC should be a topic of serious concern for organizational scholarship." (p. 2, introduction)
- **OQ-mena2026-19** "it would be interesting to examine the opposite process: how organizations challenge the hegemonic status quo, for instance through CEO sociopolitical activism." (p. 16, "Agonistic inside-out focus")

**Context (2023–24).**

- **OQ-pozner2023-04** "we follow the recent prompt from Jourdan (2023) and invite the examination of scandal as a social process centered around the audience." (p. 5, "Moving beyond the media")
- **OQ-leitzinger2023-01** "Key questions remain as to how social movements that target markets and their actors form or, if already established, become mobilized to address new issues." (p. 7, "Phase 1: Emergence")
- **OQ-leitzinger2023-24** "do all social movements diminish in importance to the markets they facilitate over time" (p. 20, "Phase 4: Settlement")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 4 | 5 |
| Core pieces | 2 | 2 |
| Questions (share of the period) | 18 (8%) | 50 (13%) |
| Questions in this stack only | 12 | 40 |

First authors: 9. Last ask: 2026-03-31 (`mena2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `mena2026` 1/23; `winkler2025`★ 5/5; `patriotta2025`★ 11/11; `giovannoni2025` 1/7.

Backing pieces, 2023–24: `godart2024` 2/5; `powell2023` 2/14; `pozner2023`★ 12/12; `leitzinger2023`★ 33/33; `bacq2023` 1/10.

**Status.** Persistent, with two core pieces in each period. Seventeen of the 18 recent questions date from 2025.

### R10 Futures and imagination

**Concern.** How do people in and around organizations imagine and make futures, and what does imagining do before it produces anything?

**Now (2025–26).** Skade asks which future-making practices exist, how actors enact futures from day to day, what utopias and dystopias mean for organizations, and how divergent futures inform strategy (OQ-skade2025-04, -05, -03, -01). Porsfelt, Vestergaard and Hjorth ask how moments of shared imagining are triggered and how they matter without leaving durable structures, and they ask that imagination be studied apart from creative output (OQ-porsfelt2026-07, -06, -05). Friedrich asks how meetings can invite collective imagination (OQ-friedrich2026-11).

**Before (2023–24).** Gümüsay and Reinecke carried it with eleven questions on how scholars should theorize desirable and undesirable futures and what infrastructure that takes (OQ-gumusay2024-12, -09, -10). Hinds and von Krogh, and Lantela, each echoed it once (OQ-hinds2024-24; OQ-lantela2024-08).

**Has the object moved?** The imaginer changed. In 2024 the scholar imagines futures. In 2025–26 organizational actors do, and the scholar studies them.

**Anchors (2025–26).**

- **OQ-porsfelt2026-07** "For organisation studies, this raises questions about how such moments are triggered, how they draw on and reconfigure existing images and cultural resources, and how they can be consequential without forming durable meaning structures." (p. 24, "Moving Forward")
- **OQ-porsfelt2026-05** "it becomes important to extract it from its current conflation with creative outcomes and to examine and explore it as distinct in its own right without being defined by productive ends." (p. 24, "Moving Forward")
- **OQ-skade2025-05** "Examining how and why social actors enact their futures on a daily basis opens various opportunities to study the creation of better futures within and beyond organizations." (p. 17, "Advancing a dialectical perspective")
- **OQ-friedrich2026-11** "In what ways should organizational meetings be structured to invite collective imagination and creative, poetic, and aesthetic experimentation in envisioning desirable futures?" (p. 14, "Affirmative ethical responsiveness")

**Context (2023–24).**

- **OQ-gumusay2024-12** "We encourage future scholarship to work on the imagination infrastructure that will underpin the kinds of prospective theorizing that we have outlined here, such as by developing future labs and other methodological avenues to actively co-create desirable futures." (p. 19, "A New Purpose for Theorizing")
- **OQ-gumusay2024-09** "There is even value in theorizing undesirable futures – whether to prepare for or caution against such alternative (un-)desirable ideas or practices that may exist at the fringe of society or in the minds of people." (p. 18, "Plausible desirability")
- **OQ-hinds2024-24** "we need 'prospective theorizing' with speculative vigor (e.g., Gümüsay & Reinecke, 2024)" (p. 12, "Discussion")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 3 | 3 |
| Core pieces | 2 | 1 |
| Questions (share of the period) | 14 (6%) | 13 (3%) |
| Questions in this stack only | 10 | 4 |

First authors: 6. Last ask: 2026-09-21 (`porsfelt2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `porsfelt2026`★ 6/6; `friedrich2026` 1/17; `skade2025`★ 7/7.

Backing pieces, 2023–24: `hinds2024` 1/25; `lantela2024` 1/8; `gumusay2024`★ 11/12.

**Status.** Persistent on one earlier core piece. Two papers deep, with the latest last ask in the set (21 September 2026).

### R11 Digital technology

**Concern.** What do digital technologies, generative AI among them, do to organizing, and should organization theory treat technology as part of organization?

**Now (2025–26).** Four pieces ask, each as a sub-question of another agenda. Patriotta, Augustine and Voronov ask how technological actors and platforms co-produce legitimacy tests (OQ-patriotta2025-10, -08). Mena, Mair and Bruder ask how social media and AI shape deliberation (OQ-mena2026-12). Garud, Turunen and Karunakaran ask how to organize innovation with platform architectures, generative AI and digital repositories (OQ-garud2025-06, -08, -10). Friedrich asks how technology can extend attunement and warns that it sits in power-laden assemblages (OQ-friedrich2026-08, -17). Seven of the eight questions also sit in the stack of the agenda they serve. Garud et al. give technology a section of their research agenda and are the one core piece; no 2025–26 piece takes technology as its main question. The 2026 editorial names AI only in the reader's paraphrase of OQ-hollerer2026-04, as an example of an emerging issue, and neither analyst nor I counted it here.

**Before (2023–24).** Fourteen pieces, eleven of them core, and 123 questions, a third of the period. Hinds and von Krogh asked what generative AI does to coordination and the division of labour (OQ-hinds2024-05, -16). Phillips and colleagues, Hsu and Bechky, and Grodal and colleagues asked what it does to categories and to the boundary between human and machine (OQ-phillips2024-09; OQ-hsu2024-06; OQ-grodal2024-08). Stark and Vanden Broeck asked whether technology is organizational structure (OQ-stark2024-08). The editors asked about language models in theorizing (OQ-cornelissen2024-04). Five further pieces asked about surveillance, hidden digital work, online meetings and institutional displacement (OQ-jaser2024-03; OQ-justesen2024-01; OQ-whyte2023-14; OQ-scherer2023-02; OQ-orlikowski2023-02).

**Has the object moved?** Technology went from object to condition. In 2023–24 authors asked what the technology does. In 2025–26 they ask what legitimacy, democracy or innovation become once it is present. The year counts show how fast: 96 questions in 2024, 5 in 2025, 3 in 2026.

**Anchors (2025–26).**

- **OQ-patriotta2025-10** "suggesting the need to examine how legitimacy tests are co-produced by both human and technological actors in the contemporary digital landscape." (p. 19, "Future research directions: Legitimacy in a changing world")
- **OQ-mena2026-12** "How do new technologies, such as social media and AI, shape deliberations outside and, in turn, within organizations?" (p. 14, "Deliberative outside-in focus")
- **OQ-garud2025-08** "The challenge moving forward is to develop more nuanced approaches to organizing for innovation, recognizing the complex, interdependent relationship between exploration and exploitation given the pitfalls and possibilities offered by these new technologies." (p. 16, "Future research on innovation at work in the age of digital technologies and Gen AI")
- **OQ-friedrich2026-17** "This dual role demands the utmost critical scrutiny in future research, as technological instruments—biotech, AI, military applications, green tech, and so on—are themselves entangled in power-laden assemblages." (p. 19, "Posthuman feminism for organization theory")

**Context (2023–24).**

- **OQ-stark2024-08** "What if, instead of thinking about technology as organizational infrastructure, we considered technology as synonymous with organizational structure?" (p. 16, "Out of Bounds")
- **OQ-phillips2024-15** "we still have a lot more to do to really take technology seriously in many research streams of organization theory." (p. 16, "Conclusions")
- **OQ-hinds2024-05** "it inspires us to ask what part of formal and informal management of interdependencies may become subject to progressive encapsulation." (p. 8, "Team coordination")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 4 | 14 |
| Core pieces | 1 | 11 |
| Questions (share of the period) | 8 (4%) | 123 (32%) |
| Questions in this stack only | 1 | 72 |

First authors: 18. Last ask: 2026-04-01 (`friedrich2026`). Editorial: `cornelissen2024`. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `friedrich2026` 2/17; `mena2026` 1/23; `patriotta2025` 2/11; `garud2025`★ 3/8.

Backing pieces, 2023–24: `hinds2024`★ 25/25; `suddaby2024` 2/5; `grodal2024`★ 8/8; `hsu2024`★ 6/6; `phillips2024`★ 12/12; `stark2024`★ 9/9; `cornelissen2024`★ 7/7; `jaser2024`★ 10/10; `justesen2024`★ 17/17; `whyte2023`★ 13/13; `scherer2023`★ 5/10; `pozner2023` 1/12; `leitzinger2023` 2/33; `orlikowski2023`★ 6/7.

**Status.** Fading in effect: one core piece, and 8 questions against 123.

### R12 Inequality and exclusion

**Concern.** How does organizing produce, reproduce or reduce inequality and exclusion, and how do the excluded gain voice?

**Now (2025–26).** One piece makes it central. Pavlisa, Harvey and Doh ask how firms mitigate their contribution to inequality and how industry structures reinforce it (OQ-pavlisa2026-06, -05). Three others use it to qualify another debate: race, gender, class and geography in institutional mythologies, class and gender in person-institutions, and DEI measures as a check on managerial authority (OQ-hawbaker2025-02; OQ-derekrobinson2025-13; OQ-mena2026-04).

**Before (2023–24).** Thirteen pieces, five of them core. Arnold and Costas asked how subjects gain a speaking position at all (OQ-arnold2023-06, -01). Sasaki and Baba asked how cultural margins are made and resisted (OQ-sasaki2024-02, -03). Langenmayr and colleagues asked how control over inclusion reproduces inequality in open strategy (OQ-langenmayr2024-01). Lantela asked whose voice the canon omits (OQ-lantela2024-04). Bacq and colleagues asked about the illegitimate and the underdog, and Fotaki about the asymmetries that shape care (OQ-bacq2023-10; OQ-fotaki2023-03).

**Has the object moved?** It receded and changed. The 2023–24 question was recognition and voice for the marginalized. The one core piece of 2026 asks about economic inequality through stakeholder governance, and elsewhere inequality has become a moderator that authors name in a closing line.

**Anchors (2025–26).**

- **OQ-pavlisa2026-06** "A critical area of inquiry surrounds how firms and their leaders leverage a stakeholder approach (Doh & Quigley, 2014) and implement strategies to mitigate their contributions to widening economic and social inequalities (Bapuji et al., 2018)." (p. 19, "Managerial implications")
- **OQ-pavlisa2026-05** "extending the analysis toward how organisational and industry-level structures of competing organisations and networks of cooperating organisations imbued with their own internal power structures, create systems of advantage and disadvantage that reinforce inequalities." (p. 19, "Discussion")
- **OQ-hawbaker2025-02** "Race, gender, class, and geography are heavily implicated in the creation of institutional mythologies." (p. 9, "Discussion")
- **OQ-mena2026-04** "Do DEI measures reduce managerial authority over minorities? Do they increase solidarity among the workforce?" (p. 11, "Republican internal focus")

**Context (2023–24).**

- **OQ-arnold2023-06** "we call for future research to look at the struggles of subjects to acquire a speaking position to begin with." (p. 16, "Implications for future research")
- **OQ-langenmayr2024-01** "Adopting an equity-based approach would thus allow open strategy scholars to explore the relation between traditional actors’ dominance and control over inclusion and the reproduction of inequalities." (p. 6, "Normalizing through traditional strategy actors’ control over inclusion")
- **OQ-lantela2024-04** "Whose voice is missing or ill-presented in certain records? How have existing conceptualizations, theories and the canon of privileged voices organized our understanding of proper knowledge and theory?" (p. 9, "A Feminist Reading of Microhistory")

**Counts.**

| | 2025–26 | 2023–24 |
|---|---|---|
| Pieces asking | 4 | 13 |
| Core pieces | 1 | 5 |
| Questions (share of the period) | 7 (3%) | 50 (13%) |
| Questions in this stack only | 2 | 29 |

First authors: 17. Last ask: 2026-06-19 (`pavlisa2026`). Editorial: none. Bar of three pieces in 2025–26: met.

Backing pieces, 2025–26: `pavlisa2026`★ 4/5; `mena2026` 1/23; `derekrobinson2025` 1/15; `hawbaker2025` 1/4.

Backing pieces, 2023–24: `hinds2024` 1/25; `seidemann2024` 1/16; `langenmayr2024`★ 11/11; `lantela2024`★ 5/8; `jaser2024` 1/10; `sasaki2024`★ 6/6; `whyte2023` 1/13; `arnold2023`★ 12/12; `leitzinger2023` 2/33; `jackwerthrice2023` 1/10; `orlikowski2023` 1/7; `fotaki2023` 2/5; `bacq2023`★ 6/10.

**Status.** Fading in effect: one core piece, and 7 questions against 50.

## Cross-cutting threads

A thread is a concern whose every question also asks about an object that has its own stack. I list four, with the ids that carry each.

**T1. Time and history.** Authors across six stacks ask how what came before shapes organizing now, and how an organizational thing lasts, changes stage, reverses and ends. Both analysts made this a stack, and ruling 1 explains why it is a thread here. I ran the count script on two versions of it. On the 33 questions that both analysts flagged it has, as pieces / core pieces / questions, 6 / 3 / 22 in 2025–26 and 9 / 0 / 11 in 2023–24, with Brennecke et al., Derek Robinson and Atanasova, and Garud et al. as core pieces. On the 57 that either flagged it has 9 / 6 / 44 and 11 / 0 / 13, and Nigam et al., Patriotta et al. and Schoeneborn et al. join the core. Ranked as a stack it would stand fourth on the first version and level with R01 on the second. By year the both-flagged questions run 2, 9, 21 and 1: the thread is a 2025 event, and one 2026 question carries it on (OQ-schoeneborn2026-05). Its history matches F's reading. Nine pieces in 2023–24 asked for more attention to time in a line or two each, none of them core, and in 2025 two papers asked about little else. The 2025–26 questions sit in R05 (25 of the 44), R01 (9), R08 (4), R09 (3), R10 (2) and R03 (1).

*Ids.* Both analysts flagged, 2025–26: OQ-brennecke2025-02, -04, -08, -10, -11, -12, -15, -16, -19, -20, -21; OQ-derekrobinson2025-08, -10, -11, -12; OQ-garud2025-03, -04, -05; OQ-patriotta2025-02, -07; OQ-dion2025-07; OQ-schoeneborn2026-05. Both analysts flagged, 2023–24: OQ-hinds2024-01, -23; OQ-justesen2024-02, -03; OQ-suddaby2024-01; OQ-seidemann2024-12; OQ-stevenson2024-01; OQ-lantela2024-03; OQ-sasaki2024-05; OQ-powell2023-04; OQ-ocasio2023-03. One analyst flagged, 2025–26, among others: OQ-nigam2025-06, -07, -11; OQ-patriotta2025-06; OQ-schoeneborn2026-01, -03; OQ-derekrobinson2025-02, -09.

**T2. Where a concept stops.** Authors in five stacks ask what falls outside one of the field's core terms. The form is the same each time: what counts as an organization (OQ-dion2025-14, -02, -04), an institution (OQ-hawbaker2025-03; OQ-derekrobinson2025-07), a logic (OQ-schildt2025-02), the demos (OQ-mena2026-01), a stakeholder to whom the firm answers (OQ-pavlisa2026-03), imagination as distinct from creative output (OQ-porsfelt2026-05), and which foundations a programme must settle first (OQ-schoeneborn2026-02). This is what O's stack A caught across two exchanges. Earlier forms of the worry: a paradox (OQ-seidemann2024-16), a team (OQ-hinds2024-09), the boundary between human and machine (OQ-grodal2024-08), an extreme context (OQ-wright2023-04), one practice or several (OQ-whyte2023-13), the reach of institutional explanation (OQ-ocasio2023-04), and the criteria for settling such disputes at all (OQ-abend2024-02).

**T3. An unsettled political order as the backdrop.** Both analysts found it. Across R06, R09, R01 and R02 the 2025–26 askers write against the same setting: democratic backsliding and right-wing tendencies (OQ-mena2026-17, -21, -14), truth-bending autocrats and populism (OQ-giovannoni2025-08), post-truth communication and total takeover (OQ-winkler2025-02, -03), polarized environments (OQ-patriotta2025-04), political struggle over versions of logics (OQ-schildt2025-05), unsettled times in which traditional institutions deteriorate (OQ-nigam2025-10), and the question whether inquiry can stand apart from political crisis (OQ-ernst2026-07). The setting was already present in OQ-sasaki2024-06, OQ-dugay2024-06, OQ-scherer2023-10, OQ-pozner2023-16 and OQ-jaser2024-10. It is a backdrop and not a stack because the pieces ask different questions against it.

**T4. The cross-level problem.** Authors theorize at one level and leave the bridge to another level to later work. Schildt and Kodeih ask how macro ideology arises from local practice (OQ-schildt2025-03). Mena and colleagues ask whether workplace democracy scales to society (OQ-mena2026-23, -20). Brennecke and colleagues ask how dyadic histories become network structure (OQ-brennecke2025-15, -14). Nigam and colleagues place person-institutions in a multi-level system, and Derek Robinson and Atanasova ask whether persons are institutionalized in small settings (OQ-nigam2025-03; OQ-derekrobinson2025-15). Pavlisa and colleagues move from firm to industry, Patriotta and colleagues ask how crises migrate across fields, and the organizationality pieces look past the single organization (OQ-pavlisa2026-05; OQ-patriotta2025-02; OQ-winkler2025-04; OQ-dion2025-06). The worry is old: OQ-powell2023-13, OQ-whyte2023-04, OQ-guercini2023-11, OQ-pozner2023-13, OQ-stevenson2024-03, OQ-hsu2024-04.

Three of the analysts' threads are not listed. O's "scholars are expected to take a normative stance" is what R03 and R02 now hold. O's "power: whose interests a structure serves" sits in R12 and R06. F's "theory handed over untested" is a feature of the genre and recurs in the closing section of nearly every piece.

## Fading inside live stacks

Five narrower agendas from 2023–24 have no asker in 2025–26, although the stack around each stays live. F listed them, and my reading of the 221 recent questions confirms each.

1. **Machine theorizing** (in R02 and R11): all seven questions of `cornelissen2024`, with OQ-suddaby2024-05 and -06.
2. **Social movements and markets** (in R09): all 33 questions of `leitzinger2023`, with OQ-pozner2023-10, -12 and OQ-bacq2023-01.
3. **Surveillance and hidden digital work** (in R11): all ten questions of `jaser2024` and all seventeen of `justesen2024`, with OQ-scherer2023-02, -05 and -09.
4. **Participation in open strategy** (in R06 and R12): all seven questions of `friesl2023` and all eleven of `langenmayr2024`.
5. **Coordinating mechanisms as such** (in R05): all twelve questions of `racker2024` on space, all nine of `guercini2023` on competence, and OQ-dugay2024-02 and -04 on formal design.

## Residual

Fifteen questions fit no stack. All date from 2023–24.

- **What remains of Affect and the self (11).** OQ-bacq2023-03, -04, -05, -09: what shame, other negative emotions and collective identity do to entrepreneurship. OQ-jorgensen2023-04, -05, -07: the politics and the dark side of organizational atmospheres. OQ-paca2024-02, -03, -04, -05: organizational mythology, archetypes and members' psychic needs. No 2025–26 piece asks about emotion among people at work. Friedrich's two questions on affective and sensory attunement (OQ-friedrich2026-06, -07) sit in R07. The side run on the 38 questions either analyst filed under Affect gives, as pieces / core pieces / questions, 16 / 5 / 36 in 2023–24 and 1 / 0 / 2 in 2025–26.
- **OQ-chia2023-03.** A plea to strategy theorists to admit practice, situation and potential beside means–ends reasoning. No stack concerns strategy as such. Both analysts left it residual.
- **OQ-laine2023-05, -06, -08.** Whether non-human objects can bear entrepreneurial qualities. O filed them under "what an organization is"; they ask a different question.

## What I was unsure about

1. **Time as a thread.** This is the ruling most likely to be reversed, because both analysts made time a stack and it would rank near the top. The counts under T1 let a reader reverse it without recounting. Reversing it moves Brennecke et al.'s 21 questions out of R05, which would then hold 2 core pieces only if five brokerage and creativity questions stay double-filed, as F had them.
2. **R04 has no question of its own in 2025–26.** By the test I applied to time it behaves as a thread in the recent period. I kept it as a stack because 24 of its 31 earlier questions have no other home and because one 2025 piece still asks from inside paradox theory.
3. **R05 is two different papers.** Network ties and innovation arrangements share a stack because both ask how joint work is held together, and both happen to ask through time. A reader may prefer to see Brennecke et al. as a stack of one.
4. **R07 and R10 were split against O.** Merged they would rank second. Split, each is two papers deep. I chose the split because the merged concern cannot be stated as one plain question that all four papers ask.
5. **The core-piece rule has edges.** `mena2026` is core to R04 on 3 of its 23 questions. `keller2025` is core to two stacks on two questions. `wedlin2025` is core to R01 on two. Without the first, R04 would have two core pieces and drop out of the prevailing group.
6. **My second-filing rule is stricter than either analyst's.** Its effect falls mostly on 2023–24: R12 holds 50 earlier questions here against 61 in F's table, and R02 holds 54 against 60 in O's. In 2025–26 it changes one core count against F's table, in R02, where `dion2025` drops from three questions to two. (R07 has one core piece fewer than F06 because of ruling 4.) The technology and inequality counts for 2025–26 are the same as F's.
7. **The thresholds are mine.** "Three core pieces" for prevailing and "under a quarter" for fading in effect are readings of the ranking, set after seeing it. A threshold of two core pieces would make ten stacks prevailing; a threshold of four would leave three.
8. **Shares need the base.** 2026 covers nine months and ten pieces. A stack with no 2026 question (R01) may simply have had no piece in press.
9. **OQ-hollerer2026-04.** The reader's paraphrase names AI and sustainability as examples of emerging issues; the quotation does not. I counted the question in R02 only.

## Appendix A: question-level rulings

Codes: **a** follows from a stack-level ruling; **b** one analyst's second filing kept; **c** one analyst's second filing not kept; **d** the analysts' second filings differ, so the shared stack is kept, plus one of the two only where the note says so; **e** the analysts' filings do not overlap, ruled by reading. F's and O's columns give their own stack ids.

| Period | Questions | F filed | O filed | Kept | Code | Why |
|---|---|---|---|---|---|---|
| 2025–26 | `garud2025` 03, 04, 05 | F02, F13 | H | R05 | a | O filed them under Time only |
| 2025–26 | `garud2025` 07 | F13 | H | R05 | a | O filed it under Time only |
| 2025–26 | `garud2025` 09 | F13 | residual | R05 | e | alternatives to the themes that structure organizations; O left it residual |
| 2025–26 | `garud2025` 06, 08, 10 | F08, F13 | J | R05 + R11 | b | organizing for innovation with platforms, GenAI and repositories |
| 2025–26 | `keller2025` 02 | F01, F03 | I | R02 + R04 | b | a condition on a method of theorizing |
| 2025–26 | `schildt2025` 05 | F04 | B, L | R01 | c | political struggle is the setting of a question about logics |
| 2025–26 | `brennecke2025` 01, 05, 06, 09, 13, 14 | F02 | M | R05 | a | F filed them under Time only |
| 2025–26 | `brennecke2025` 04, 08, 10, 11, 12, 15, 16, 20, 21 | F02 | H, M | R05 | a | F filed them under Time only; O under Time and M |
| 2025–26 | `brennecke2025` 07 | F02 | K, M | R05 | a | F filed it under Time only; a method call inside a topic |
| 2025–26 | `skade2025` 02 | F06, F10 | G, I | R10 + R04 | d | tensions between futures, kept from O; grand challenges are the setting |
| 2025–26 | `skade2025` 06 | F03, F10 | I | R10 + R04 | b | a limit on the piece's account of tensions between futures |
| 2025–26 | `derekrobinson2025` 06 | F04 | B, C | R01 | c | tensions inside a person-brand |
| 2025–26 | `dion2025` 04 | F01, F11 | A | R08 | c | the scope of the discipline is this stack's own question |
| 2025–26 | `dion2025` 07 | F02, F11 | H | R08 | a | O filed it under Time only |
| 2025–26 | `hawbaker2025` 01 | F04 | B, C | R01 | c | who co-creates institutional mythologies |
| 2025–26 | `hawbaker2025` 04 | F01, F04 | A | R01 | c | the reach of institutional theory |
| 2025–26 | `patriotta2025` 04 | F09 | C, F | R09 | c | polarized settings of legitimacy tests |
| 2025–26 | `patriotta2025` 12 | F09 | C, I | R09 + R04 | b | when irreconcilable values block settlement |
| 2025–26 | `wedlin2025` 03, 04 | F04 | B, C | R01 | c | hype and institutions; no contest or legitimacy in the quotations |
| 2025–26 | `winkler2025` 04 | F09, F11 | A | R09 + R08 | b | dis/organization beyond the single organization |
| 2025–26 | `winkler2025` 05 | F03, F09 | A, C | R09 + R04 | d | equilibrium against escalation; F second filing kept |
| 2025–26 | `friedrich2026` 02 | F01, F12 | G | R07 + R06 | e | an invitation that covers the piece's two agendas |
| 2025–26 | `friedrich2026` 04 | F06 | E, G | R07 | c | inequity appears only in the paraphrase |
| 2025–26 | `friedrich2026` 11 | F10 | D, G | R10 | c | collective imagination in meetings; O filed it under G, read here as futures; democracy not kept |
| 2025–26 | `friedrich2026` 17 | F08 | D, J | R11 | c | technology in power-laden assemblages |
| 2025–26 | `mena2026` 05 | F12, F13 | D | R06 + R05 | b | governance structures as organizational design |
| 2025–26 | `corver2026` 09 | F01, F06 | K | R02 + R07 | b | theorists and practitioners building the capacity to use sustainability models |
| 2025–26 | `corver2026` 11 | F06 | M | R07 + R05 | e | which roles hold which modeling capacity; both filings kept |
| 2025–26 | `corver2026` 16 | F03, F06 | I | R07 + R04 | b | disagreement inside the modeling process |
| 2025–26 | `kalkman2026` 03, 06, 07, 08 | F05, F06 | F | R03 | a | crisis management is not filed under sustainability |
| 2025–26 | `kalkman2026` 05 | F05, F06 | E, F | R03 | a | as above; vulnerability to a crisis is not the inequality question |
| 2025–26 | `pavlisa2026` 02 | F07 | D, E | R12 | c | stakeholder governance, not democracy |
| 2025–26 | `pavlisa2026` 04 | F05, F07 | F | R03 + R12 | b | a limit on the piece's account of inequality |
| 2023–24 | `georgiou2023` 03, 10 | F04 | A | R01 | e | typology and types of the community logic |
| 2023–24 | `georgiou2023` 04 | F04 | B, I | R01 | c | institutional complexity and hybridity, not tension as such |
| 2023–24 | `georgiou2023` 05 | F03, F04 | I, N | R01 + R04 | b | variants of the logic as a source of tensions and paradoxes |
| 2023–24 | `georgiou2023` 09 | F04, F11 | A | R01 + R08 | b | asks both when communities become formal organizations and whether the logic survives |
| 2023–24 | `georgiou2023` 11 | F04 | A, B | R01 | c | practices that keep the basis of a logic |
| 2023–24 | `laine2023` 04, 07, 09 | F01 | A, K | R02 | c | calls about how to build object-oriented theory |
| 2023–24 | `laine2023` 05, 06, 08 | residual | A | residual | e | entrepreneurial quality of objects; not the organization-as-actor question |
| 2023–24 | `friesl2023` 04 | F07, F12 | D | R06 | c | self-selection into strategy; inequality is not asked |
| 2023–24 | `friesl2023` 08 | F12 | D, K | R06 | c | method call inside a topic |
| 2023–24 | `guercini2023` 04, 05, 06, 07, 08, 09, 10, 11, 12 | F13 | residual | R05 | e | competence and learning fall under capability; O left them residual |
| 2023–24 | `orlikowski2023` 08 | F05, F07 | E, J | R12 | d | constitutive exclusions |
| 2023–24 | `orlikowski2023` 09 | F04, F08 | J | R11 + R01 | b | the quotation names the institutional shifts under way |
| 2023–24 | `arnold2023` 04 | F07 | A, E | R12 | c | otherness, voice and equality; organizationality and democracy are only named |
| 2023–24 | `arnold2023` 06, 13 | F07 | D, E | R12 | c | otherness, voice and equality; organizationality and democracy are only named |
| 2023–24 | `scherer2023` 04 | F07, F12 | D, F | R06 | d | maturity as public reason |
| 2023–24 | `scherer2023` 07 | F08, F12 | J | R11 + R06 | b | regulating language models as part of the maturity project |
| 2023–24 | `scherer2023` 13 | F12 | D, J | R06 | c | no technology in the quotation |
| 2023–24 | `powell2023` 08 | F04 | B, C | R01 | c | conformity versus distinctiveness; legitimacy is not named |
| 2023–24 | `powell2023` 11 | F04 | B, K | R01 | c | method call inside a topic |
| 2023–24 | `whyte2023` 05 | F08 | G, J | R11 | c | futures appear only in the paraphrase |
| 2023–24 | `whyte2023` 08 | F08 | J, M | R11 | c | a boundary condition on the setting |
| 2023–24 | `dugay2024` 02 | F13 | A | R05 | e | which formalization a purpose needs |
| 2023–24 | `dugay2024` 06 | F06, F13 | A | R05 | e | what de-formalizing did to state capacity |
| 2023–24 | `dugay2024` 04, 05, 07 | F11, F13 | A | R05 + R08 | b | formal design, and the place of formal organization in the field |
| 2023–24 | `gumusay2024` 02, 04, 05 | F06, F10 | G | R10 + R07 | b | climate pathways, valuation of nature, low-emission business models |
| 2023–24 | `gumusay2024` 06 | F06, F10 | G, K | R10 | d | metaphors for prospective theorizing; F added sustainability, O theory |
| 2023–24 | `gumusay2024` 08 | F05, F10 | D, G | R10 | d | who judges a future desirable; F added the moral stack, O democracy |
| 2023–24 | `gumusay2024` 09 | F01, F10 | G | R10 | c | theorizing undesirable futures |
| 2023–24 | `gumusay2024` 13 | F01, F10 | K | R02 | c | collaborative theorizing; no future in the question |
| 2023–24 | `jaser2024` 07, 09, 11 | F07, F08 | J, L | R11 | d | resistance to surveillance at work; F filed it as power, O as activism |
| 2023–24 | `justesen2024` 01, 04, 16 | F08, F13 | J | R11 | c | maintenance work; coordination is not asked |
| 2023–24 | `justesen2024` 05, 07, 08, 10 | F08 | J, K | R11 | c | method calls inside a topic |
| 2023–24 | `justesen2024` 06 | F07, F08 | J, K | R11 | d | methods for unseen and devalued work |
| 2023–24 | `justesen2024` 12 | F08 | J, L | R11 | c | collective action is a rider |
| 2023–24 | `justesen2024` 14 | F07, F08 | J | R11 | c | devaluation of work; inequality is not asked |
| 2023–24 | `sasaki2024` 03 | F07 | E, L | R12 | c | resistance by the marginalized, not public contestation of organizations |
| 2023–24 | `sasaki2024` 06 | F07, F12 | E | R12 | c | authoritarianism is the setting of a marginalization question |
| 2023–24 | `godart2024` 03 | F04, F09 | C | R01 + R09 | b | audiences an organization must please, within an inter-institutional environment |
| 2023–24 | `lantela2024` 05, 06, 11 | F01, F07 | E | R02 + R12 | b | theorizing from the margins |
| 2023–24 | `stark2024` 02 | F08 | J, L | R11 | c | professional resistance to algorithms, not public contestation |
| 2023–24 | `stark2024` 06 | F08, F13 | J | R11 | c | organization and communication as one field; coordination is not asked |
| 2023–24 | `grodal2024` 02 | F08 | C, J | R11 | c | audience attention to a technology |
| 2023–24 | `grodal2024` 06, 07 | F07, F08 | J | R11 | c | power in technological emergence; inequality is not asked |
| 2023–24 | `hsu2024` 08 | F08, F13 | J | R11 + R05 | b | retaining expertise is a capability question |
| 2023–24 | `langenmayr2024` 02, 11 | F07, F12 | D | R12 + R06 | b | who is represented in strategy making |
| 2023–24 | `langenmayr2024` 04, 05, 07 | F07 | D, E | R12 + R06 | b | who is represented in strategy making |
| 2023–24 | `langenmayr2024` 08 | F05, F07 | D | R12 | e | the equity agenda against the business case |
| 2023–24 | `langenmayr2024` 10 | F07 | D | R12 | e | the equity agenda against the business case |
| 2023–24 | `langenmayr2024` 09 | F01, F07 | D, E | R12 | d | scholars as critics or activists for equal opportunity |
| 2023–24 | `phillips2024` 12, 13 | F01, F08 | J | R11 + R02 | b | a call for a symbolic turn in how the field theorizes |
| 2023–24 | `hinds2024` 09 | F08, F13 | A, J | R11 + R05 | d | what a team is, in a passage on team coordination; F second filing kept |
| 2023–24 | `hinds2024` 16, 17, 20 | F08, F13 | J | R11 + R05 | b | division of labour and multi-team systems |
| 2023–24 | `hinds2024` 11 | F08 | J, K | R11 | c | method call inside a topic |
| 2023–24 | `hinds2024` 13 | F07, F08 | J | R11 | c | power holders; inequality is not asked |
| 2023–24 | `hinds2024` 14 | F07, F08 | J, L | R11 | d | resistance to GenAI; F filed it as power, O as activism |
| 2023–24 | `hinds2024` 24 | F08, F10 | J, K | R11 + R10 | d | the quotation names prospective theorizing and cites its source; F second filing kept |
| 2023–24 | `seidemann2024` 03 | F03 | I, K | R04 | c | method call inside a topic |
| 2023–24 | `seidemann2024` 06 | F03 | I, L | R04 | c | resistance to paradox, not public contestation |
| 2023–24 | `seidemann2024` 15 | F03 | F, I | R04 | c | "normative" here means prescriptive |
| 2023–24 | `suddaby2024` 04 | F01 | F, K | R02 | c | what kind of knowledge theory should be |
| 2023–24 | `bacq2023` 03, 04, 05, 09 | F14 | N | residual | a | filed only under Affect by both analysts |
| 2023–24 | `jorgensen2023` 04, 05, 07 | F14 | N | residual | a | filed only under Affect by both analysts |
| 2023–24 | `paca2024` 05 | F14 | N | residual | a | filed only under Affect by both analysts |
| 2023–24 | `paca2024` 02, 03, 04 | residual | N | residual | a | F residual; O filed under Affect |

## Appendix B: count script output

`python3 tools/stack_counts.py synthesis/stacks/STACKS.tsv`, run on 23 November 2026. The script's status column applies the three-piece bar.

```
rows 739; unknown ids 0 []; missing 0 []; in >2 stacks []
stack	n_oq	pieces_25_26	pieces_23_24	first_authors	last_ask	core_25_26	core_23_24	q_25_26	editorial	status
R02	81	8	14	22	2026-09-19	4	9	27	y	prevailing+persistent
R04	44	7	4	11	2026-07-28	3	3	13	n	prevailing+persistent
R01	95	6	7	13	2025-12-23	6	7	44	n	prevailing+persistent
R03	32	5	5	10	2026-09-19	4	1	23	n	prevailing+persistent
R05	77	4	7	11	2026-07-28	2	5	31	n	prevailing+persistent
R12	57	4	13	17	2026-06-19	1	5	7	n	prevailing+persistent
R11	131	4	14	18	2026-04-01	1	11	8	y	prevailing+persistent
R09	68	4	5	9	2026-03-31	2	2	18	n	prevailing+persistent
R10	27	3	3	6	2026-09-21	2	1	14	n	prevailing+persistent
R08	31	3	5	8	2026-09-19	2	1	24	n	prevailing+persistent
R07	29	3	1	4	2026-07-28	2	1	26	n	prevailing+persistent
R06	52	3	5	8	2026-07-28	2	3	29	n	prevailing+persistent
```
