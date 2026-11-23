[Written by Fable (claude-fable-5-2), stage S13a, 2026-11-23]

# Stacks of open questions in *Organization Theory*, 2023–2026 (analyst F)

Run `ot-oq-2026-11`, stage S13a. I read all 605 open questions in `OPEN_QUESTIONS_BY_DATE.md`, line by line, and grouped them by hand into 14 stacks. I worked blind: I did not open the brief, the report, the fit, critic, pickup or hand-check material, the earlier synthesis files, or the other analyst's `STACKS_O` files that sit in the same folder. Every claim below rests on the input's quotations and reader's paraphrases, and nothing comes from memory of the papers.

## Counting rules

1. **Periods.** A piece belongs to 2025–26 or to 2023–24 by its published-online date in the input headers, which match `published_online` in `QUESTIONS.tsv`. The input holds 65 pieces: 24 from 2025–26 with 221 questions, and 41 from 2023–24 with 384 questions. The earlier period is the larger one, so raw piece counts across periods do not compare; the table gives shares of each period's questions beside the counts.
2. **Assignment.** Each question sits in one stack, in two, or in the residual list. Of the 605, 391 sit in one stack, 207 in two and 7 in the residual, which gives 812 rows in `STACKS_F.tsv`. I gave a second stack only where the question asks that stack's question, not where it merely mentions the theme.
3. **Pieces asking.** A piece asks a stack's concern in a period if at least one of its questions sits in the stack. The status rule and the ranking use this count.
4. **Depth, reported beside it.** One stray question then weighs as much as a whole paper, so I add two columns that the status rule does not use: the number of questions, and the number of *core* pieces, meaning pieces with at least three questions in the stack or at least half of their questions there.
5. **First authors.** No first author has two pieces among the 65, so distinct first authors equal distinct pieces across both periods.
6. **Last ask.** The latest published-online date among the stack's pieces.
7. **Editorial.** Whether `cornelissen2024` or `hollerer2026` has a question in the stack.
8. **Status.** The author's rule, applied mechanically: *prevailing* with three or more pieces in 2025–26, *persistent* when asked in both periods, *fading* with no piece since 2024, *new* with no piece before 2025.
9. **Rank.** Number of 2025–26 pieces first; persistent stacks before the rest; then the more recent last ask.
10. **Quotations.** A script copied every anchor and context quotation from the input and checked each at 40 words or fewer. One, OQ-dion2025-04, is a contiguous excerpt because the input quotation runs longer; the entry says so.
11. **What the script did.** I assigned every question by reading it. A script then tallied my assignments, built the tables and ledgers below, wrote the TSV and copied the quotations. I wrote the prose by hand.
12. **Technology.** I sized it as I sized every other topic, by the pieces and questions that ask about it.

## Ranked stacks

| Rank | Stack | Pieces 2025–26 | of which core | Questions 2025–26 (share) | Pieces 2023–24 | of which core | Questions 2023–24 (share) | First authors | Last ask | Editorial | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | F01 Theory and contribution | 9 | 5 | 30 (14%) | 15 | 9 | 56 (15%) | 24 | 2026-09-19 (`schoeneborn2026`) | `hollerer2026`; `cornelissen2024` | prevailing + persistent |
| 2 | F02 Time and history | 6 | 4 | 33 (15%) | 9 | 0 | 11 (3%) | 15 | 2026-09-19 (`schoeneborn2026`) | none | prevailing + persistent |
| 3 | F03 Productive tension | 6 | 3 | 11 (5%) | 4 | 3 | 31 (8%) | 10 | 2026-07-28 (`corver2026`) | none | prevailing + persistent |
| 4 | F04 Institutions and logics | 6 | 6 | 44 (20%) | 7 | 7 | 51 (13%) | 13 | 2025-12-23 (`wedlin2025`) | none | prevailing + persistent |
| 5 | F05 Moral standard and responsibility | 5 | 4 | 23 (10%) | 8 | 1 | 12 (3%) | 13 | 2026-09-19 (`schoeneborn2026`) | none | prevailing + persistent |
| 6 | F06 Shared emergencies | 5 | 3 | 31 (14%) | 2 | 1 | 5 (1%) | 7 | 2026-07-28 (`corver2026`) | none | prevailing + persistent |
| 7 | F07 Inequality and exclusion | 4 | 1 | 7 (3%) | 17 | 7 | 61 (16%) | 21 | 2026-06-19 (`pavlisa2026`) | none | prevailing + persistent |
| 8 | F08 Digital technology | 4 | 1 | 8 (4%) | 14 | 11 | 123 (32%) | 18 | 2026-04-01 (`friedrich2026`) | `cornelissen2024` | prevailing + persistent |
| 9 | F09 Public contestation | 4 | 2 | 18 (8%) | 5 | 2 | 50 (13%) | 9 | 2026-03-31 (`mena2026`) | none | prevailing + persistent |
| 10 | F10 Futures and imagination | 3 | 2 | 14 (6%) | 3 | 1 | 14 (4%) | 6 | 2026-09-21 (`porsfelt2026`) | none | prevailing + persistent |
| 11 | F11 Organization as actor | 3 | 2 | 24 (11%) | 5 | 1 | 7 (2%) | 8 | 2026-09-19 (`schoeneborn2026`) | none | prevailing + persistent |
| 12 | F12 Democracy | 3 | 2 | 29 (13%) | 6 | 3 | 21 (5%) | 9 | 2026-07-28 (`corver2026`) | none | prevailing + persistent |
| 13 | F13 Coordination and capability | 3 | 2 | 14 (6%) | 9 | 6 | 50 (13%) | 12 | 2026-03-31 (`mena2026`) | none | prevailing + persistent |
| 14 | F14 Affect and the self | 1 | 0 | 2 (1%) | 12 | 3 | 25 (7%) | 13 | 2026-04-01 (`friedrich2026`) | none | persistent (near-fading; see text) |

Shares are of the period's questions (221 and 384). A question in two stacks counts in both, so the shares add to more than 100%. Long lists from single pieces drive the question counts: `leitzinger2023` contributes 33 questions, `hinds2024` 25, `mena2026` 23, `brennecke2025` 21.

## The prevailing concerns now

The status rule alone does not separate the stacks. Thirteen of the fourteen clear the bar of three pieces in 2025–26, and all thirteen were also asked in 2023–24, because a single line in a paper's closing section is enough to count that paper. Pieces, core pieces and questions read together do separate them. Five concerns prevail now.

1. **F01 Theory and contribution.** Nine of the 24 pieces from 2025–26 ask it, five of them at length, and the 2026 editorial asks it too. What counts as theory, and who polices that, is the journal's standing question.
2. **F04 Institutions and logics.** Six pieces, every one of them core, 44 questions. The rank formula places it fourth only because its last ask dates from December 2025. A whole exchange asks whether a person can be an institution, and Schildt and Kodeih ask outright what counts as a logic.
3. **F02 Time and history.** Six pieces, four core, 33 questions. It is the clearest case of a rider turning into an object: nine pieces in 2023–24 asked for more attention to time in a line or two each, and in 2025 two papers ask about little else.
4. **F05 Moral standard and responsibility.** Five pieces, four core, 23 questions, all from 2026.
5. **F06 Shared emergencies.** Five pieces, three core, 31 questions, against two pieces and five questions in 2023–24. It is the nearest thing in the set to a new concern.

Three qualifications belong beside that list. **F03 Productive tension** is wide and shallow: six pieces, eleven questions. **F12 Democracy** and **F11 Organization as actor** are narrow, deep and recent: three pieces each, 29 and 24 questions, nearly all from two papers apiece, with last asks in July and September 2026. They sit exactly on the bar and I would watch them as rising. **F07 Inequality and exclusion** and **F08 Digital technology** clear the bar on seven and eight questions after 61 and 123 in 2023–24; the rule calls them prevailing, and the evidence shows them receding from object to qualifier. **F14 Affect and the self** survives on one 2026 piece and I report it as near-fading, outside the live ranking.

## The stacks

Each ledger lists the pieces behind the counts. A star marks a core piece. Question numbers are the two-digit suffixes of the ids, so `mena2026 · 08` is OQ-mena2026-08.

### F01 Theory and contribution

**Concern.** What should count as theory, and as a contribution, in organization studies, and how should scholars and the journal's gatekeepers go about producing it?

**Now (2025–26).** The askers turn the question on the field's own conventions. The editors want themed sections that look beyond existing conventions and submissions that say what kind of contribution they make (OQ-hollerer2026-02, -06). Ernst, Lassalle, Kerr and Robinson ask how orthodoxies define good theory, and they call on editors and reviewers to counteract field biases (OQ-ernst2026-03, -06). Giovannoni and Quattrone ask for a theory founded on the unknowable, for methods that study absences without filling them, and for reviewers who accept open-ended work (OQ-giovannoni2025-03, -10, -07). Keller, Berti and Smith apply paradox to the theorist's own work (OQ-keller2025-01). Corver and Filler ask how a model, as distinct from other impactful theory, reaches practice (OQ-corver2026-07, -09). The organizationality authors ask for agreed foundations and for explicit ontological postures (OQ-schoeneborn2026-02; OQ-dion2025-13).

**Before (2023–24).** The askers argued over the word itself and over a new tool. Abend, Suddaby and Prasad debated who decides what "theory" means and what it is for (OQ-abend2024-03, -04; OQ-suddaby2024-04; OQ-prasad2024-06). The editors asked whether large language models can theorize and how authors must disclose them (OQ-cornelissen2024-04, -06, -08). Gümüsay and Reinecke asked how the academic system must change to admit imagination and values (OQ-gumusay2024-11). Lantela asked whose voice has counted as theory (OQ-lantela2024-09). Wright and colleagues, and Petriglieri and Ashford, asked what the researcher's self does to theorizing (OQ-wright2023-06; OQ-petriglieri2023-02).

**Movement.** The object moved from the definition of theory to the conventions that police it. The 2025–26 askers address editors and reviewers by role, and the 2026 editorial itself asks for convention-breaking work. The 2024 editorial question about machine theorizing has no asker in 2025–26.

**Anchors (2025–26).**

- **OQ-hollerer2026-02** "Proposals for–and the resulting special themed sections–should, as mentioned, explicitly look beyond existing conventions and push beyond the boundaries of theoretical knowledge in our domain of scholarly inquiry." (p. 5, "'Catalysing & Crystallizing'")
- **OQ-ernst2026-03** "scholars could, as part of their reflexive research practices, benefit from paying attention to how orthodoxies in the field define what is currently considered good theory" (p. 15, "Theory generation in OS")
- **OQ-giovannoni2025-03** "To further develop these approaches, we call for a shift from placing knowledge at the heart of organization theory to making the unknowable its foundation." (p. 4, "Unknowability in a Mysterious World")
- **OQ-corver2026-07** "This invites further theorizing on how modeling generates its own distinct pathways to impact" (p. 17, "Discussion")

**Context (2023–24).**

- **OQ-abend2024-04** "Fellow community members! Which aims should be served by our key words and distinctions? Which aims are more important to us, when, and where?" (p. 7, "5. Democracy, Unfreedom, Usefulness")
- **OQ-gumusay2024-11** "help shed light on the many questions that are still unanswered, such as how our academic ecosystem might change to enable and encourage the role of imagination and values in the theorizing process." (p. 19, "A New Purpose for Theorizing")
- **OQ-cornelissen2024-04** "Rather, it is imperative that we engage in a debate about the implications of this potentially disruptive technology for our theorizing and for the kinds of knowledge that we in turn create about our various phenomena of interest." (p. 3, untitled introduction)

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `schoeneborn2026` | 2026-09-19 | 1 / 10 | 02 |
| 2025–26 | `corver2026` | 2026-07-28 | 2 / 12 | 07, 09 |
| 2025–26 | `hollerer2026` ★ | 2026-07-26 | 6 / 6 | 01, 02, 03, 04, 05, 06 |
| 2025–26 | `ernst2026` ★ | 2026-04-07 | 8 / 8 | 01, 02, 03, 04, 05, 06, 07, 08 |
| 2025–26 | `friedrich2026` | 2026-04-01 | 2 / 17 | 02, 18 |
| 2025–26 | `dion2025` ★ | 2025-12-26 | 3 / 13 | 04, 05, 13 |
| 2025–26 | `hawbaker2025` | 2025-12-01 | 1 / 4 | 04 |
| 2025–26 | `giovannoni2025` ★ | 2025-08-22 | 5 / 7 | 03, 06, 07, 09, 10 |
| 2025–26 | `keller2025` ★ | 2025-07-15 | 2 / 2 | 01, 02 |
| 2023–24 | `suddaby2024` ★ | 2024-10-28 | 5 / 5 | 01, 03, 04, 05, 06 |
| 2023–24 | `prasad2024` ★ | 2024-10-28 | 4 / 4 | 03, 04, 06, 07 |
| 2023–24 | `abend2024` ★ | 2024-10-28 | 7 / 7 | 02, 03, 04, 05, 06, 07, 08 |
| 2023–24 | `langenmayr2024` | 2024-09-18 | 1 / 11 | 09 |
| 2023–24 | `phillips2024` | 2024-09-13 | 2 / 12 | 12, 13 |
| 2023–24 | `lantela2024` ★ | 2024-06-10 | 8 / 8 | 03, 04, 05, 06, 08, 09, 10, 11 |
| 2023–24 | `gumusay2024` ★ | 2024-03-28 | 5 / 12 | 01, 09, 11, 12, 13 |
| 2023–24 | `cornelissen2024` ★ | 2024-03-26 | 7 / 7 | 04, 05, 06, 07, 08, 09, 10 |
| 2023–24 | `wright2023` ★ | 2023-12-21 | 5 / 5 | 02, 03, 04, 05, 06 |
| 2023–24 | `powell2023` | 2023-12-21 | 1 / 14 | 14 |
| 2023–24 | `jorgensen2023` | 2023-12-21 | 2 / 5 | 03, 06 |
| 2023–24 | `orlikowski2023` | 2023-06-16 | 1 / 7 | 05 |
| 2023–24 | `fotaki2023` | 2023-03-11 | 1 / 5 | 05 |
| 2023–24 | `petriglieri2023` ★ | 2023-02-20 | 4 / 4 | 01, 02, 04, 05 |
| 2023–24 | `laine2023` ★ | 2023-02-18 | 3 / 7 | 04, 07, 09 |

### F02 Time and history

**Concern.** How does what came before (the history of a tie, the order of events, an earlier crisis) shape organizing now, and how can theories built on snapshots take it in?

**Now (2025–26).** Two 2025 pieces make time their object. Brennecke, Carnabuci and Ertug ask 21 questions about the history of network ties: which features of a tie's past are retained and when its narrative hardens, which trajectories make a tie brittle, how dyadic histories build network structure (OQ-brennecke2025-12, -10, -15). Garud, Turunen and Karunakaran ask how organizing for innovation runs on several times at once (OQ-garud2025-05, -03). Four other pieces attach a temporal question to another agenda: whether charging collectives with actorhood follows typical temporal patterns (OQ-schoeneborn2026-05), whether person-institutionalization can run in reverse (OQ-derekrobinson2025-12), how past justifications shape later responses (OQ-patriotta2025-07), whether process data reflect the temporality of organizing (OQ-dion2025-07).

**Before (2023–24).** Time arrives only as a closing rider. Nine pieces each add a line or two: embrace process (OQ-suddaby2024-01), build process theories of emerging technologies (OQ-hinds2024-23), add a temporal perspective (OQ-justesen2024-02), study long-term effects (OQ-seidemann2024-12), run longitudinal diffusion studies (OQ-powell2023-04), trace imprinting (OQ-ocasio2023-03). No 2023–24 piece is core to the stack.

**Movement.** The question sharpened. A generic call to add time became a specified object: the biography of a relationship, the memory of a crisis, the sequence of stages.

**Anchors (2025–26).**

- **OQ-brennecke2025-12** "Which features of relational history are retained, which decay over time? When do narratives about a tie crystallize into dominant accounts that guide behaviour? Under what conditions do memories of key events become shared across both parties" (p. 19, "Cognitive and narrative construction of relational history")
- **OQ-garud2025-05** "There have been fewer efforts to theorize organizing for innovation as multi-temporal distributed processes." (p. 13, "Implications")
- **OQ-schoeneborn2026-05** "The second question is whether there are any typical temporal patterns related to charging collectives with or discharging them of actorhood." (p. 14, "Conclusion and Research Agenda")
- **OQ-patriotta2025-07** "Studying recurrent or cyclical crises, such as repeated food safety scandals or recurring privacy controversies in the technology sector, could reveal how past justifications shape the repertoire of responses available to organizations in the future" (p. 18, "Future research directions: Legitimacy in a changing world")

**Context (2023–24).**

- **OQ-suddaby2024-01** "Our profession could indeed still embrace processes more fully. Doing so would help us better incorporate notions of “is” and “was” into our theoretical frames." (p. 5, "Construct Clarity or Construct Clarification?")
- **OQ-justesen2024-02** "we suggest that future research could supplement this approach with a temporal perspective, conceptualization and metaphors" (p. 21, "Future research: Some suggestions")
- **OQ-seidemann2024-12** "temporal and spatial scales, capturing long-term effects as well as cascading or spatially remote effects of paradox management." (p. 18, "Developing a more granular perspective")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `schoeneborn2026` | 2026-09-19 | 1 / 10 | 05 |
| 2025–26 | `dion2025` | 2025-12-26 | 1 / 13 | 07 |
| 2025–26 | `derekrobinson2025` ★ | 2025-12-23 | 4 / 15 | 08, 10, 11, 12 |
| 2025–26 | `patriotta2025` ★ | 2025-11 | 3 / 11 | 02, 06, 07 |
| 2025–26 | `brennecke2025` ★ | 2025-09-28 | 21 / 21 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 |
| 2025–26 | `garud2025` ★ | 2025-07-11 | 3 / 8 | 03, 04, 05 |
| 2023–24 | `hinds2024` | 2024-10-29 | 2 / 25 | 01, 23 |
| 2023–24 | `suddaby2024` | 2024-10-28 | 1 / 5 | 01 |
| 2023–24 | `seidemann2024` | 2024-10-18 | 1 / 16 | 12 |
| 2023–24 | `stevenson2024` | 2024-06-14 | 1 / 5 | 01 |
| 2023–24 | `lantela2024` | 2024-06-10 | 1 / 8 | 03 |
| 2023–24 | `justesen2024` | 2024-03-15 | 2 / 17 | 02, 03 |
| 2023–24 | `sasaki2024` | 2024-01-18 | 1 / 6 | 05 |
| 2023–24 | `powell2023` | 2023-12-21 | 1 / 14 | 04 |
| 2023–24 | `ocasio2023` | 2023-08-04 | 1 / 4 | 03 |

### F03 Productive tension

**Concern.** When are contradiction, paradox and disagreement productive, and when should they be settled, chosen between or refused?

**Now (2025–26).** Six pieces ask, each briefly, and five of them outside paradox theory's home ground. Mena, Mair and Bruder ask when dissent stays productive and when consensus can be dispensed with (OQ-mena2026-08, -07, -22). Corver and Filler ask how disagreement enables modeling (OQ-corver2026-16). Skade asks how divergent futures create productive tensions (OQ-skade2025-01). Schildt and Kodeih ask about contradiction within a single logic (OQ-schildt2025-06). Winkler and Schoeneborn ask that dis/organization be read as escalation as well as equilibrium (OQ-winkler2025-05). Only Keller, Berti and Smith stay inside paradox theory, and they turn it on theorists (OQ-keller2025-01, -02).

**Before (2023–24).** Two 2024 pieces carry the stack. Krautzberger and Tuckermann ask how organizations steer a portfolio of both/and and either/or responses, and how that fails (OQ-krautzberger2024-03, -12). Seidemann asks where both/and stops working, why organizations breed paradoxes, and how responses should be judged (OQ-seidemann2024-11, -02, -08). Georgiou and Arenas, and Stark and Vanden Broeck, add conflict between logics and contradiction within algorithmic management (OQ-georgiou2023-08; OQ-stark2024-05).

**Movement.** The object changed. The 2024 askers questioned a research programme about its own concepts. The 2025–26 askers borrow its question (is this tension productive?) for democracy, modeling, futures and logics. Width grew from four pieces to six while depth fell from 31 questions to 11.

**Anchors (2025–26).**

- **OQ-mena2026-08** "How can we ensure that dissent remains continuously productive and does not become destructive, for example, by deepening fractures among organizational members or even leading to organizational death?" (p. 12, "Agonistic internal focus")
- **OQ-keller2025-01** "We invite future scholarship to continue to explore how paradox theory applies to our own work as scholars and theorists." (p. 16, "Discussion")
- **OQ-skade2025-01** "future research could clarify how these divergent futures inform strategic decisions and create productive tensions within organizations." (p. 18, "Tensions between futures")
- **OQ-corver2026-16** "How such disagreement and the conditions surrounding them, both within and across these groups, feeds into, and perhaps even enables, productive modeling deserves further attention in future research." (p. 18, "Discussion")

**Context (2023–24).**

- **OQ-seidemann2024-11** "I recommend that paradox scholars empirically explore the boundary conditions of both/and for different classes of phenomena at different levels of analysis and the potential negative ramifications of embracing tensions." (p. 18, "Developing a more granular perspective")
- **OQ-krautzberger2024-03** "First, future research could investigate how to effectively navigate a portfolio of both/and and either/or approaches to paradoxes in various contexts." (p. 19, "Directions for future research")
- **OQ-seidemann2024-02** "Understanding paradoxes as inherent organizing features prompts the question of why organizations are “rife with paradoxes”" (p. 15, "Leveraging ontological perspectives")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `corver2026` | 2026-07-28 | 1 / 12 | 16 |
| 2025–26 | `mena2026` ★ | 2026-03-31 | 3 / 23 | 07, 08, 22 |
| 2025–26 | `winkler2025` | 2025-11-11 | 1 / 5 | 05 |
| 2025–26 | `skade2025` ★ | 2025-09-27 | 3 / 7 | 01, 06, 07 |
| 2025–26 | `keller2025` ★ | 2025-07-15 | 2 / 2 | 01, 02 |
| 2025–26 | `schildt2025` | 2025-02-24 | 1 / 6 | 06 |
| 2023–24 | `krautzberger2024` ★ | 2024-11-08 | 11 / 11 | 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13 |
| 2023–24 | `seidemann2024` ★ | 2024-10-18 | 16 / 16 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16 |
| 2023–24 | `stark2024` | 2024-06-18 | 1 / 9 | 05 |
| 2023–24 | `georgiou2023` ★ | 2023-03-11 | 3 / 11 | 05, 06, 08 |

### F04 Institutions and logics

**Concern.** How do institutions and logics come to exist, hold and change, and what may count as one?

**Now (2025–26).** The askers test the edges of the concept. Nigam, Amis and Logue ask why, how, when and for how long a person can become an institution (OQ-nigam2025-11). Derek Robinson and Atanasova ask what conditions make a person-brand institutional and whether the process reverses (OQ-derekrobinson2025-07, -12). Hawbaker and Hallett answer that persons should be kept apart from institutions so that the relation between them can be studied (OQ-hawbaker2025-03). Schildt and Kodeih ask what counts as a logic and how macro ideology arises from local practice (OQ-schildt2025-02, -03). Mutch asks how practices pass between law and organizations (OQ-mutch2025-03). Wedlin and Weinryb ask how hype disrupts institutions (OQ-wedlin2025-03).

**Before (2023–24).** The askers asked how forms spread and who changes them. Powell and DiMaggio ask how new practices enter and stick, and which parts of organizations yield to isomorphic pressure (OQ-powell2023-09, -01). Jackwerth-Rice, Koehrsen and Mattes ask whether the sufficiency of an entrepreneur's resources can be known in advance (OQ-jackwerthrice2023-09). Georgiou and Arenas, Stevenson and colleagues, and Godart and Wittman ask about the community logic, the centrality of logics and purity (OQ-georgiou2023-04; OQ-stevenson2024-01; OQ-godart2024-02). Ocasio warns that institutional explanations may be overused (OQ-ocasio2023-04).

**Movement.** The question shifted from process to unit. Emergence and persistence remain the verbs, but the 2025–26 subject is a candidate unit (a person, a hype, a body of law, a constellation of practices) whose standing as institution or logic is itself in doubt. All six pieces from 2025–26 and all seven from 2023–24 are core.

**Anchors (2025–26).**

- **OQ-nigam2025-11** "We hope that others will take on these ideas and push forward why, how, when and for how long individuals can become institutions." (p. 9, "Conclusion")
- **OQ-hawbaker2025-03** "If we can identify individuals as something other than institutions we can more cogently examine the relationships between those things and institutions, without making every(one) an institution." (p. 9, "Discussion")
- **OQ-schildt2025-02** "what exactly counts as a logic?" and "how do we draw the boundaries of an institutional logic?" (p. 16, "Towards a more dynamic and local view")
- **OQ-wedlin2025-03** "We hope that our model of hype as a process of translation will spur a variety of empirical investigations, further exploring the institutional dynamics of hype and its potentially disruptive institutional consequences." (p. 17, "Concluding Discussion")

**Context (2023–24).**

- **OQ-powell2023-09** "How do new ideas and practices enter organizations and stick? Why do new kinds of institutions emerge, take root, and persist? When are organizations more vulnerable to changes in the wider environment and when are they resisted?" (p. 15, "Institutional change")
- **OQ-ocasio2023-04** "institutional explanations may be overused, and other factors such as power, status, demography, resource dependencies, cognition, emotions, identity, and meaning have effects that are not reducible to institutions" (p. 15, "The ubiquity of institutions and their limits")
- **OQ-jackwerthrice2023-02** "This raises the question of whether changing existing institutions might be easier than building entirely new ones" (p. 9, "A Review of 40 Case Studies of Institutional Entrepreneurship")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `wedlin2025` ★ | 2025-12-23 | 2 / 2 | 03, 04 |
| 2025–26 | `derekrobinson2025` ★ | 2025-12-23 | 15 / 15 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15 |
| 2025–26 | `nigam2025` ★ | 2025-12-06 | 11 / 11 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11 |
| 2025–26 | `hawbaker2025` ★ | 2025-12-01 | 4 / 4 | 01, 02, 03, 04 |
| 2025–26 | `mutch2025` ★ | 2025-04-25 | 6 / 6 | 01, 02, 03, 04, 05, 06 |
| 2025–26 | `schildt2025` ★ | 2025-02-24 | 6 / 6 | 02, 03, 04, 05, 06, 07 |
| 2023–24 | `godart2024` ★ | 2024-09-03 | 5 / 5 | 02, 03, 04, 05, 06 |
| 2023–24 | `stevenson2024` ★ | 2024-06-14 | 5 / 5 | 01, 02, 03, 04, 05 |
| 2023–24 | `powell2023` ★ | 2023-12-21 | 13 / 14 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13 |
| 2023–24 | `ocasio2023` ★ | 2023-08-04 | 4 / 4 | 01, 02, 03, 04 |
| 2023–24 | `jackwerthrice2023` ★ | 2023-06-22 | 10 / 10 | 02, 03, 04, 05, 06, 07, 08, 09, 10, 11 |
| 2023–24 | `orlikowski2023` ★ | 2023-06-16 | 3 / 7 | 01, 06, 09 |
| 2023–24 | `georgiou2023` ★ | 2023-03-11 | 11 / 11 | 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12 |

### F05 Moral standard and responsibility

**Concern.** By what moral standard should organizations act and be judged, and who answers for what they do?

**Now (2025–26).** Three 2026 pieces make it their object. Werner, Cornelissen and Turkenburg ask how an organization's moral reasoning beyond its institutional obligations can be judged case by case, and whether organizations differ in moral scope (OQ-werner2026-10, -03). Kalkman proposes care as the purpose of crisis management, invites rival normative purposes and asks what a care-based purpose produces (OQ-kalkman2026-01, -06). Pavlisa, Harvey and Doh admit that they lack criteria for which stakeholders fall outside a firm's responsibility (OQ-pavlisa2026-03). Schoeneborn, Dobusch and Seidl ask what shifting actorhood does to individual and collective responsibility (OQ-schoeneborn2026-06). Friedrich asks how care for more-than-human others secures resources (OQ-friedrich2026-10).

**Before (2023–24).** Only Fotaki's 2023 piece on care is core (OQ-fotaki2023-03, -07). Seven others raise the question in passing, usually as a charge against another programme. Seidemann asks how paradox responses are to be judged normatively (OQ-seidemann2024-08). Stark and Vanden Broeck ask who is accountable for algorithmic decisions (OQ-stark2024-04). Langenmayr and colleagues ask whether a societal orientation can be reconciled with the business case (OQ-langenmayr2024-08).

**Movement.** From rider to object. The 2023–24 askers demanded that someone bring norms in. The 2026 askers bring them in and then ask for the criteria (of judgment, of scope, of responsibility) that their own proposals lack.

**Anchors (2025–26).**

- **OQ-werner2026-10** "Another question that further normative research might explore is how, when organizations deliberate beyond institutionally prescribed norms and obligations, this can be ethically judged in specific instances and cases." (pp. 21–22, "Theoretical and research implications")
- **OQ-kalkman2026-01** "Scholars can propose other normative approaches to continue the debate or provide an ethical defense of current approaches." (p. 14, "Theoretical Implications")
- **OQ-pavlisa2026-03** "As a limitation, our theorisation inherits the boundary conditions of stakeholder governance literature, lacking robust criteria for determining which stakeholders are beyond the scope of a firm’s responsibility" (p. 18, "Discussion")
- **OQ-schoeneborn2026-06** "What does the recurrent charging or discharging of a collective social address with actorhood imply for individual as opposed to collective responsibility?" (p. 14, "Conclusion and Research Agenda")

**Context (2023–24).**

- **OQ-seidemann2024-08** "Expanding on the predominantly strategic perspective of paradox management, the question of how responses to paradoxes are evaluated from a normative standpoint becomes central." (p. 17, "Purposefully integrating normative approaches")
- **OQ-fotaki2023-03** "it is vital to theorize how power asymmetries among genders, races, ethnicities and social classes within and across geographical locales shape care relations, forms of care, and experiences of caring and being cared for in fundamental ways" (p. 14, "Discussion")
- **OQ-stark2024-04** "But who or what is accountable when an algorithm exercises decisions that occur faster and with a vastly larger number of inputs than a human can physiologically comprehend and react to (Vesa & Tienari, 2022, p. 1137)?" (p. 14, "Accountability")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `schoeneborn2026` | 2026-09-19 | 1 / 10 | 06 |
| 2025–26 | `kalkman2026` ★ | 2026-07-21 | 8 / 8 | 01, 02, 03, 04, 05, 06, 07, 08 |
| 2025–26 | `pavlisa2026` ★ | 2026-06-19 | 3 / 5 | 03, 04, 06 |
| 2025–26 | `werner2026` ★ | 2026-04-01 | 8 / 8 | 03, 04, 05, 06, 07, 08, 09, 10 |
| 2025–26 | `friedrich2026` ★ | 2026-04-01 | 3 / 17 | 09, 10, 13 |
| 2023–24 | `seidemann2024` | 2024-10-18 | 2 / 16 | 08, 09 |
| 2023–24 | `langenmayr2024` | 2024-09-18 | 1 / 11 | 08 |
| 2023–24 | `stark2024` | 2024-06-18 | 1 / 9 | 04 |
| 2023–24 | `gumusay2024` | 2024-03-28 | 1 / 12 | 08 |
| 2023–24 | `jaser2024` | 2024-03-19 | 1 / 10 | 04 |
| 2023–24 | `scherer2023` | 2023-10-18 | 1 / 10 | 06 |
| 2023–24 | `orlikowski2023` | 2023-06-16 | 1 / 7 | 08 |
| 2023–24 | `fotaki2023` ★ | 2023-03-11 | 4 / 5 | 03, 04, 06, 07 |

### F06 Shared emergencies

**Concern.** How do organizations act, and how should they, when the problem is a shared emergency: a sustainability problem, ecological dependence, a crisis?

**Now (2025–26).** Three 2026 pieces carry it, each from a different side. Corver and Filler ask which modeling actions support sustainability problem-solving, and whether problems move from discrete to interconnected (OQ-corver2026-10, -06). Friedrich asks how organizing can keep its dependencies on ecological others in view (OQ-friedrich2026-03, -05). Kalkman asks how organizations change their crisis management and who is vulnerable (OQ-kalkman2026-07, -05). Skade, and Giovannoni and Quattrone, each add a line on grand challenges (OQ-skade2025-02; OQ-giovannoni2025-05).

**Before (2023–24).** Two pieces. Gümüsay and Reinecke ask how climate pathways would change organizing and which outcomes other than growth a theory could serve (OQ-gumusay2024-02, -05). du Gay and Lopdrup Hjorth ask whether anti-formal reforms weakened states that now face perilous circumstances (OQ-dugay2024-06).

**Movement.** Close to new. The question went from prospective (theorize a desirable climate future) to operational (how organizations model, attune and change). I joined three sub-threads here: corporate sustainability change, ecological dependence and crisis response. Each rests mainly on one piece.

**Anchors (2025–26).**

- **OQ-corver2026-10** "Future work also could more systematically map how particular modeling actions relate to concrete results, retrospectively identifying which of these actions in fact support successful sustainability problem-solving processes" (p. 17, "Discussion")
- **OQ-friedrich2026-03** "How can organizing continually acknowledge and investigate material interstices and dependencies with ecological and social others" (p. 12, "Acknowledging assembled becoming")
- **OQ-kalkman2026-07** "Empirical research therefore can help us understand how organizations can effectively change their crisis management approaches." (p. 15, "Implications for Empirical Research")
- **OQ-skade2025-02** "to enable researchers to better understand how actors perceive and manage tensions between organizational futures linked to grand challenges." (p. 18, "Tensions within contexts: Grand challenges")

**Context (2023–24).**

- **OQ-gumusay2024-02** "For instance, how would different climate pathways impact organizing differently, including the behaviour of people and institutions?" (p. 9, "Four modes of theorizing the future")
- **OQ-dugay2024-06** "Time will tell whether they have undermined the capacities of states to deal with the perilous circumstances they now find themselves facing both internationally and domestically." (p. 14, "Implications for political administration research and practice")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `corver2026` ★ | 2026-07-28 | 11 / 12 | 05, 06, 08, 09, 10, 11, 12, 13, 14, 15, 16 |
| 2025–26 | `kalkman2026` ★ | 2026-07-21 | 5 / 8 | 03, 05, 06, 07, 08 |
| 2025–26 | `friedrich2026` ★ | 2026-04-01 | 13 / 17 | 03, 04, 05, 06, 07, 08, 09, 10, 12, 13, 14, 15, 16 |
| 2025–26 | `skade2025` | 2025-09-27 | 1 / 7 | 02 |
| 2025–26 | `giovannoni2025` | 2025-08-22 | 1 / 7 | 05 |
| 2023–24 | `gumusay2024` ★ | 2024-03-28 | 4 / 12 | 02, 04, 05, 06 |
| 2023–24 | `dugay2024` | 2024-03-19 | 1 / 5 | 06 |

### F07 Inequality and exclusion

**Concern.** How does organizing produce, reproduce or reduce inequality and exclusion, and how do the excluded gain voice?

**Now (2025–26).** One piece makes it central. Pavlisa, Harvey and Doh ask how firms mitigate their contribution to inequality and how industry structures reinforce it (OQ-pavlisa2026-06, -05). Three others use it as a qualifier on another debate: race, gender, class and geography in institutional mythologies (OQ-hawbaker2025-02), class and gender in person-institutions (OQ-derekrobinson2025-13), DEI measures as a check on managerial authority (OQ-mena2026-04).

**Before (2023–24).** Seventeen pieces, seven of them core. Arnold and Costas ask how subjects gain a speaking position (OQ-arnold2023-06). Langenmayr and colleagues ask how control over inclusion reproduces inequality in open strategy (OQ-langenmayr2024-01). Sasaki and Baba ask how cultural margins are made and resisted (OQ-sasaki2024-02, -03). Lantela asks whose voice the canon omits (OQ-lantela2024-04). Bacq and colleagues ask about the illegitimate and the underdog (OQ-bacq2023-10). The technology pieces ask who gains and who loses power (OQ-hinds2024-15; OQ-jaser2024-03; OQ-grodal2024-06).

**Movement.** The concern receded and changed object. The 2023–24 question was recognition and voice for the marginalized. The one core piece of 2026 asks about economic inequality through stakeholder governance. Questions fell from 61 to 7.

**Anchors (2025–26).**

- **OQ-pavlisa2026-06** "A critical area of inquiry surrounds how firms and their leaders leverage a stakeholder approach (Doh & Quigley, 2014) and implement strategies to mitigate their contributions to widening economic and social inequalities (Bapuji et al., 2018)." (p. 19, "Managerial implications")
- **OQ-pavlisa2026-05** "extending the analysis toward how organisational and industry-level structures of competing organisations and networks of cooperating organisations imbued with their own internal power structures, create systems of advantage and disadvantage that reinforce inequalities." (p. 19, "Discussion")
- **OQ-hawbaker2025-02** "Race, gender, class, and geography are heavily implicated in the creation of institutional mythologies." (p. 9, "Discussion")
- **OQ-mena2026-04** "Do DEI measures reduce managerial authority over minorities? Do they increase solidarity among the workforce?" (p. 11, "Republican internal focus")

**Context (2023–24).**

- **OQ-arnold2023-06** "we call for future research to look at the struggles of subjects to acquire a speaking position to begin with." (p. 16, "Implications for future research")
- **OQ-langenmayr2024-01** "Adopting an equity-based approach would thus allow open strategy scholars to explore the relation between traditional actors’ dominance and control over inclusion and the reproduction of inequalities." (p. 6, "Normalizing through traditional strategy actors’ control over inclusion")
- **OQ-lantela2024-04** "Whose voice is missing or ill-presented in certain records? How have existing conceptualizations, theories and the canon of privileged voices organized our understanding of proper knowledge and theory?" (p. 9, "A Feminist Reading of Microhistory")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `pavlisa2026` ★ | 2026-06-19 | 4 / 5 | 02, 04, 05, 06 |
| 2025–26 | `mena2026` | 2026-03-31 | 1 / 23 | 04 |
| 2025–26 | `derekrobinson2025` | 2025-12-23 | 1 / 15 | 13 |
| 2025–26 | `hawbaker2025` | 2025-12-01 | 1 / 4 | 02 |
| 2023–24 | `hinds2024` ★ | 2024-10-29 | 3 / 25 | 13, 14, 15 |
| 2023–24 | `seidemann2024` | 2024-10-18 | 1 / 16 | 10 |
| 2023–24 | `grodal2024` | 2024-10-05 | 2 / 8 | 06, 07 |
| 2023–24 | `langenmayr2024` ★ | 2024-09-18 | 11 / 11 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11 |
| 2023–24 | `lantela2024` ★ | 2024-06-10 | 5 / 8 | 04, 05, 06, 09, 11 |
| 2023–24 | `jaser2024` ★ | 2024-03-19 | 4 / 10 | 03, 07, 09, 11 |
| 2023–24 | `justesen2024` | 2024-03-15 | 2 / 17 | 06, 14 |
| 2023–24 | `sasaki2024` ★ | 2024-01-18 | 6 / 6 | 01, 02, 03, 04, 05, 06 |
| 2023–24 | `whyte2023` | 2023-12-21 | 1 / 13 | 11 |
| 2023–24 | `scherer2023` | 2023-10-18 | 1 / 10 | 04 |
| 2023–24 | `arnold2023` ★ | 2023-09-30 | 12 / 12 | 01, 02, 03, 04, 05, 06, 07, 08, 10, 11, 12, 13 |
| 2023–24 | `friesl2023` | 2023-06-25 | 1 / 7 | 04 |
| 2023–24 | `leitzinger2023` | 2023-06-23 | 2 / 33 | 30, 31 |
| 2023–24 | `jackwerthrice2023` | 2023-06-22 | 1 / 10 | 10 |
| 2023–24 | `orlikowski2023` | 2023-06-16 | 1 / 7 | 08 |
| 2023–24 | `fotaki2023` | 2023-03-11 | 2 / 5 | 03, 04 |
| 2023–24 | `bacq2023` ★ | 2023-02-18 | 6 / 10 | 01, 02, 06, 07, 08, 10 |

### F08 Digital technology

**Concern.** What do digital technologies, generative AI among them, do to organizing, and should organization theory treat technology as part of organization and not as a tool?

**Now (2025–26).** Four pieces ask, each as a sub-question of another agenda. Patriotta, Augustine and Voronov ask how technological actors and platforms co-produce legitimacy tests (OQ-patriotta2025-10, -08). Mena, Mair and Bruder ask how social media and AI shape deliberation (OQ-mena2026-12). Garud, Turunen and Karunakaran ask how to organize innovation given the new technologies (OQ-garud2025-08, -10). Friedrich asks how technology can extend attunement and warns that it sits in power-laden assemblages (OQ-friedrich2026-08, -17). No piece from 2025–26 takes technology as its main question. The 2026 editorial names AI only in the reader's paraphrase of OQ-hollerer2026-04, as an example of an emerging issue, and I did not count it here.

**Before (2023–24).** Fourteen pieces, eleven core, 123 questions. Hinds and von Krogh ask what generative AI does to coordination and the division of labour (OQ-hinds2024-05, -16). Phillips, Hsu, Grodal and their co-authors ask what it does to categories and to the human–machine boundary (OQ-phillips2024-09; OQ-hsu2024-06; OQ-grodal2024-08). Stark and Vanden Broeck ask whether technology is organizational structure (OQ-stark2024-08). The editors ask about language models in theorizing (OQ-cornelissen2024-04). Five further pieces ask about surveillance, hidden digital work, online meetings and institutional displacement (OQ-jaser2024-03; OQ-justesen2024-01; OQ-whyte2023-14; OQ-scherer2023-02; OQ-orlikowski2023-01).

**Movement.** Technology went from object to condition. In 2023–24 authors asked what the technology does. In 2025–26 they ask what legitimacy, democracy or innovation become once it is present. The stack clears the three-piece bar on eight questions.

**Anchors (2025–26).**

- **OQ-patriotta2025-10** "suggesting the need to examine how legitimacy tests are co-produced by both human and technological actors in the contemporary digital landscape." (p. 19, "Future research directions: Legitimacy in a changing world")
- **OQ-mena2026-12** "How do new technologies, such as social media and AI, shape deliberations outside and, in turn, within organizations?" (p. 14, "Deliberative outside-in focus")
- **OQ-garud2025-08** "The challenge moving forward is to develop more nuanced approaches to organizing for innovation, recognizing the complex, interdependent relationship between exploration and exploitation given the pitfalls and possibilities offered by these new technologies." (p. 16, "Future research on innovation at work in the age of digital technologies and Gen AI")
- **OQ-friedrich2026-17** "This dual role demands the utmost critical scrutiny in future research, as technological instruments—biotech, AI, military applications, green tech, and so on—are themselves entangled in power-laden assemblages." (p. 19, "Posthuman feminism for organization theory")

**Context (2023–24).**

- **OQ-stark2024-08** "What if, instead of thinking about technology as organizational infrastructure, we considered technology as synonymous with organizational structure?" (p. 16, "Out of Bounds")
- **OQ-phillips2024-15** "we still have a lot more to do to really take technology seriously in many research streams of organization theory." (p. 16, "Conclusions")
- **OQ-orlikowski2023-02** "So, there is little attention focused on the undertow, and thus limited knowledge of the corollary effects that are being generated by digitalization or their consequences." (p. 5, "The Digital Undertow")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `friedrich2026` | 2026-04-01 | 2 / 17 | 08, 17 |
| 2025–26 | `mena2026` | 2026-03-31 | 1 / 23 | 12 |
| 2025–26 | `patriotta2025` | 2025-11 | 2 / 11 | 08, 10 |
| 2025–26 | `garud2025` ★ | 2025-07-11 | 3 / 8 | 06, 08, 10 |
| 2023–24 | `hinds2024` ★ | 2024-10-29 | 25 / 25 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 |
| 2023–24 | `suddaby2024` | 2024-10-28 | 2 / 5 | 05, 06 |
| 2023–24 | `grodal2024` ★ | 2024-10-05 | 8 / 8 | 02, 03, 04, 05, 06, 07, 08, 09 |
| 2023–24 | `hsu2024` ★ | 2024-10-04 | 6 / 6 | 01, 02, 04, 05, 06, 08 |
| 2023–24 | `phillips2024` ★ | 2024-09-13 | 12 / 12 | 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16 |
| 2023–24 | `stark2024` ★ | 2024-06-18 | 9 / 9 | 01, 02, 03, 04, 05, 06, 07, 08, 09 |
| 2023–24 | `cornelissen2024` ★ | 2024-03-26 | 7 / 7 | 04, 05, 06, 07, 08, 09, 10 |
| 2023–24 | `jaser2024` ★ | 2024-03-19 | 10 / 10 | 02, 03, 04, 05, 06, 07, 08, 09, 10, 11 |
| 2023–24 | `justesen2024` ★ | 2024-03-15 | 17 / 17 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| 2023–24 | `whyte2023` ★ | 2023-12-21 | 13 / 13 | 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14 |
| 2023–24 | `scherer2023` ★ | 2023-10-18 | 5 / 10 | 02, 05, 07, 08, 09 |
| 2023–24 | `pozner2023` | 2023-09-30 | 1 / 12 | 15 |
| 2023–24 | `leitzinger2023` | 2023-06-23 | 2 / 33 | 09, 10 |
| 2023–24 | `orlikowski2023` ★ | 2023-06-16 | 6 / 7 | 01, 02, 05, 06, 07, 09 |

### F09 Public contestation

**Concern.** How do publics, media and movements contest organizations, and how do such contests form, escalate and settle?

**Now (2025–26).** Patriotta, Augustine and Voronov ask about the contest itself: what signals that an issue will escalate, how influencers and activists amplify a test, what happens when the contenders' values are irreconcilable (OQ-patriotta2025-05, -09, -12). Winkler and Schoeneborn ask organization scholars to take post-truth communication seriously, and they bound their model at total takeover (OQ-winkler2025-02, -03). Giovannoni and Quattrone ask how rhetoric swings between logic and non-logic under populism (OQ-giovannoni2025-08). Mena, Mair and Bruder ask how organizations themselves challenge the status quo (OQ-mena2026-19).

**Before (2023–24).** The 2023 askers studied the challengers. Leitzinger and Waeger ask 33 questions about social movements that target markets: how they form, when they are co-opted, whether they fade as markets mature (OQ-leitzinger2023-01, -16, -24). Pozner and Hannigan ask how publics become scandal audiences (OQ-pozner2023-04, -09). Godart and Wittman, and Powell and DiMaggio, ask which audiences an organization must satisfy and when a practice becomes mandatory for legitimacy (OQ-godart2024-03; OQ-powell2023-06).

**Movement.** The object changed from who contests to how a contest runs when audiences are polarized and facts disputed. The movements-and-markets agenda has no asker in 2025–26.

**Anchors (2025–26).**

- **OQ-patriotta2025-11** "this paper provides a foundation for future research on how organizations and societies co-create the boundaries of legitimacy in an increasingly complex and contested world." (p. 19, "Conclusion")
- **OQ-patriotta2025-05** "While our theory highlights that legitimacy tests are dynamic and processual, we know little about the early warning signs that indicate when an issue may escalate into a full-blown controversy versus blowing over." (p. 18, "Future research directions: Legitimacy in a changing world")
- **OQ-winkler2025-02** "In this article we argue that PTC should be a topic of serious concern for organizational scholarship." (p. 2, introduction)
- **OQ-mena2026-19** "it would be interesting to examine the opposite process: how organizations challenge the hegemonic status quo, for instance through CEO sociopolitical activism." (p. 16, "Agonistic inside-out focus")

**Context (2023–24).**

- **OQ-pozner2023-04** "we follow the recent prompt from Jourdan (2023) and invite the examination of scandal as a social process centered around the audience." (p. 5, "Moving beyond the media")
- **OQ-leitzinger2023-01** "Key questions remain as to how social movements that target markets and their actors form or, if already established, become mobilized to address new issues." (p. 7, "Phase 1: Emergence")
- **OQ-leitzinger2023-16** "raises questions as to the inevitability of cooptation in creation movement-led markets, which stages of market development are most vulnerable to cooptation" (p. 17, "Phase 3: Interaction")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `mena2026` | 2026-03-31 | 1 / 23 | 19 |
| 2025–26 | `winkler2025` ★ | 2025-11-11 | 5 / 5 | 02, 03, 04, 05, 06 |
| 2025–26 | `patriotta2025` ★ | 2025-11 | 11 / 11 | 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12 |
| 2025–26 | `giovannoni2025` | 2025-08-22 | 1 / 7 | 08 |
| 2023–24 | `godart2024` | 2024-09-03 | 2 / 5 | 03, 04 |
| 2023–24 | `powell2023` | 2023-12-21 | 2 / 14 | 06, 07 |
| 2023–24 | `pozner2023` ★ | 2023-09-30 | 12 / 12 | 04, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16 |
| 2023–24 | `leitzinger2023` ★ | 2023-06-23 | 33 / 33 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33 |
| 2023–24 | `bacq2023` | 2023-02-18 | 1 / 10 | 01 |

### F10 Futures and imagination

**Concern.** How do people in and around organizations imagine and make futures, and what does imagining do before it produces anything?

**Now (2025–26).** Skade asks which future-making practices exist and how actors enact futures from day to day (OQ-skade2025-04, -05). Porsfelt, Vestergaard and Hjorth ask how moments of shared imagining are triggered and how they matter without leaving durable structures, and they ask that imagination be studied apart from creative output (OQ-porsfelt2026-07, -05). Friedrich asks how meetings can invite collective imagination (OQ-friedrich2026-11).

**Before (2023–24).** Gümüsay and Reinecke carry it with twelve questions on how scholars should theorize desirable and undesirable futures and what infrastructure that takes (OQ-gumusay2024-12, -09). Hinds and von Krogh, and Lantela, each echo it once (OQ-hinds2024-24; OQ-lantela2024-08).

**Movement.** The imaginer changed. In 2024 the scholar imagines futures. In 2025–26 organizational actors do, and the scholar studies them. The stack sits on the bar: three pieces, one of them a single question.

**Anchors (2025–26).**

- **OQ-skade2025-05** "Examining how and why social actors enact their futures on a daily basis opens various opportunities to study the creation of better futures within and beyond organizations." (p. 17, "Advancing a dialectical perspective")
- **OQ-porsfelt2026-07** "For organisation studies, this raises questions about how such moments are triggered, how they draw on and reconfigure existing images and cultural resources, and how they can be consequential without forming durable meaning structures." (p. 24, "Moving Forward")
- **OQ-porsfelt2026-05** "it becomes important to extract it from its current conflation with creative outcomes and to examine and explore it as distinct in its own right without being defined by productive ends." (p. 24, "Moving Forward")
- **OQ-friedrich2026-11** "In what ways should organizational meetings be structured to invite collective imagination and creative, poetic, and aesthetic experimentation in envisioning desirable futures?" (p. 14, "Affirmative ethical responsiveness")

**Context (2023–24).**

- **OQ-gumusay2024-12** "We encourage future scholarship to work on the imagination infrastructure that will underpin the kinds of prospective theorizing that we have outlined here, such as by developing future labs and other methodological avenues to actively co-create desirable futures." (p. 19, "A New Purpose for Theorizing")
- **OQ-gumusay2024-09** "There is even value in theorizing undesirable futures – whether to prepare for or caution against such alternative (un-)desirable ideas or practices that may exist at the fringe of society or in the minds of people." (p. 18, "Plausible desirability")
- **OQ-hinds2024-24** "we need 'prospective theorizing' with speculative vigor (e.g., Gümüsay & Reinecke, 2024)" (p. 12, "Discussion")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `porsfelt2026` ★ | 2026-09-21 | 6 / 6 | 04, 05, 06, 07, 08, 09 |
| 2025–26 | `friedrich2026` | 2026-04-01 | 1 / 17 | 11 |
| 2025–26 | `skade2025` ★ | 2025-09-27 | 7 / 7 | 01, 02, 03, 04, 05, 06, 07 |
| 2023–24 | `hinds2024` | 2024-10-29 | 1 / 25 | 24 |
| 2023–24 | `lantela2024` | 2024-06-10 | 1 / 8 | 08 |
| 2023–24 | `gumusay2024` ★ | 2024-03-28 | 12 / 12 | 01, 02, 03, 04, 05, 06, 08, 09, 10, 11, 12, 13 |

### F11 Organization as actor

**Concern.** What makes a collective an organization, an actor in its own right, and should organization studies follow organizing beyond formal organizations?

**Now (2025–26).** The exchange on organizationality supplies almost all of it. Schoeneborn, Dobusch and Seidl ask how loose collectives persist with little organizationality, which practices attribute actorhood, and whether the perspective explains anything beyond formal organizations (OQ-schoeneborn2026-03, -07, -10). Dion, Cooren and Dupuis ask what organizationality is a property of, what evidence would show organizations to be distinct, and whether the discipline should centre formal organizations at all (OQ-dion2025-14, -02, -04). Winkler and Schoeneborn add one invitation to look beyond single organizations (OQ-winkler2025-04).

**Before (2023–24).** Five pieces, mostly single asks. Laine and Kibler ask whether an organization can exist while doing nothing (OQ-laine2023-02). Phillips and colleagues ask what organizations are once artificial persons join them (OQ-phillips2024-09). Stark and Vanden Broeck propose technology as structure (OQ-stark2024-08). Georgiou and Arenas ask when communities become formal organizations (OQ-georgiou2023-09). du Gay and Lopdrup Hjorth pull the other way, toward formal organization (OQ-dugay2024-05, -04).

**Movement.** Scattered provocations became a programme with 24 questions. The programme is narrow: two pieces and one stray line. The counter-position, the return to formal organization, has no voice in 2025–26.

**Anchors (2025–26).**

- **OQ-dion2025-04** "[…] whether the said discipline should step forward and study organizationality unbound by liberal preoccupations for legally recognized 'moral agents' is another question." (p. 11, "A Fourth Tension") [contiguous excerpt; the input quotation runs to 48 words]
- **OQ-schoeneborn2026-03** "Our framework then raises follow-up questions, for instance, how loose and fluid social phenomena can sustain their existence despite a rather low degree of organizationality." (p. 13, "Dynamizing Organizationality")
- **OQ-schoeneborn2026-10** "An important task of future organizational scholarship will then be to demonstrate the extent to which this perspective on organizationality can yield explanatory value" (p. 14, "Conclusion and Research Agenda")

**Context (2023–24).**

- **OQ-laine2023-02** "Is it unthinkable for organization theory that different relational effects at a different time and in a different place still yield the same organization? Is it not possible for an organization to “not do” anything at all?" (p. 11, "For whom objects matter")
- **OQ-phillips2024-09** "How does the introduction of artificial persons into an organization change how we think about what organizations are, how they are constructed and how they function?" (p. 11, "The implications of generative AI in organizations")
- **OQ-dugay2024-05** "But perhaps our contemporary circumstances require the return of the categories and intellectual frameworks that for too long have been consigned to the dustbin of defunct and old-fashioned organizational devices." (p. 12, "Theoretical implications for organization theory")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `schoeneborn2026` ★ | 2026-09-19 | 10 / 10 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10 |
| 2025–26 | `dion2025` ★ | 2025-12-26 | 13 / 13 | 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14 |
| 2025–26 | `winkler2025` | 2025-11-11 | 1 / 5 | 04 |
| 2023–24 | `phillips2024` | 2024-09-13 | 1 / 12 | 09 |
| 2023–24 | `stark2024` | 2024-06-18 | 1 / 9 | 08 |
| 2023–24 | `dugay2024` ★ | 2024-03-19 | 3 / 5 | 04, 05, 07 |
| 2023–24 | `georgiou2023` | 2023-03-11 | 1 / 11 | 09 |
| 2023–24 | `laine2023` | 2023-02-18 | 1 / 7 | 02 |

### F12 Democracy

**Concern.** How can organizing be democratic (who takes part, and on what terms), and what do organizations do to, and under, democracy in society?

**Now (2025–26).** Mena, Mair and Bruder ask 23 questions: who the demos is, whether workplace experiments scale, how right-wing tendencies and democratic backsliding bear on organizations (OQ-mena2026-01, -23, -21, -17). Friedrich asks how democratic organizing resists co-optation and extends voice to ecological others (OQ-friedrich2026-16, -12). Corver and Filler ask how co-creative modeling meets participatory governance (OQ-corver2026-05).

**Before (2023–24).** Six pieces asked about participation without always naming democracy. Friesl, Brielmaier and Dobusch ask why some actors join open strategy and others abstain (OQ-friesl2023-03). Langenmayr and colleagues ask who is represented (OQ-langenmayr2024-11). Scherer and Neesham ask how organizing can foster mature citizens (OQ-scherer2023-13). Jaser and Tourish call for democratic oversight of surveillance (OQ-jaser2024-06). Sasaki and Baba point to rising authoritarianism (OQ-sasaki2024-06).

**Movement.** The question sharpened. Democracy became the named object, and the link between the organization and the polity, in both directions, became the question.

**Anchors (2025–26).**

- **OQ-mena2026-01** "who qualifies as the people (or demos; Koenig-Archibugi, 2022): employees, a larger set of organizational members and/or stakeholders, or a broader demos?" (p. 3, introduction)
- **OQ-mena2026-21** "How do right-wing tendencies at the country level shape democracy within organizations in this country, and how might organizational democracy influence such right-wing take-up?" (p. 19, "Cross-focal dynamics and spillover effects")
- **OQ-friedrich2026-16** "Little research has explored how democratic organizing can mitigate its vulnerabilities to ideological co-optation and, especially, how it might connect with ecological others while sustaining its power-sensitive and egalitarian potential." (p. 5, "Organizational Democracy’s Disconnects")
- **OQ-corver2026-05** "One open conceptual question, for instance, is how a more open, co-creative approach to modeling interacts with more democratic decision-making processes and participatory governance structures" (p. 17, "Discussion")

**Context (2023–24).**

- **OQ-scherer2023-13** "Organization theory and business ethics have a crucial role to play in advancing our understanding of how individual and collective human action can be further organized to foster the communicative conditions needed for mature citizens" (p. 21, "Conclusion")
- **OQ-friesl2023-03** "Unveiling the social processes underpinning self-selection allows future research to study why certain actors participate in open strategy or why they abstain from doing so." (p. 13, "Discussion and Theoretical Implications")
- **OQ-jaser2024-06** "The need to exercise democratic oversight and restraint must be reasserted, through collective action, ideological struggle against the managerialist tenets of neoliberalism and, where necessary, legislative fiat." (p. 16, "Discussion")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `corver2026` | 2026-07-28 | 1 / 12 | 05 |
| 2025–26 | `friedrich2026` ★ | 2026-04-01 | 5 / 17 | 02, 12, 14, 15, 16 |
| 2025–26 | `mena2026` ★ | 2026-03-31 | 23 / 23 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 |
| 2023–24 | `langenmayr2024` ★ | 2024-09-18 | 3 / 11 | 01, 02, 11 |
| 2023–24 | `gumusay2024` | 2024-03-28 | 1 / 12 | 03 |
| 2023–24 | `jaser2024` | 2024-03-19 | 1 / 10 | 06 |
| 2023–24 | `sasaki2024` | 2024-01-18 | 1 / 6 | 06 |
| 2023–24 | `scherer2023` ★ | 2023-10-18 | 8 / 10 | 04, 06, 07, 08, 09, 10, 11, 13 |
| 2023–24 | `friesl2023` ★ | 2023-06-25 | 7 / 7 | 03, 04, 05, 06, 07, 08, 09 |

### F13 Coordination and capability

**Concern.** How is collective work put together and capability built: by which designs, spaces, routines, ties and learning?

**Now (2025–26).** Garud, Turunen and Karunakaran ask which arrangements serve innovation at work, and they invite experiments with alternatives to the dominant structuring themes (OQ-garud2025-03, -09). Brennecke and colleagues ask how a tie's path affects brokerage and creative exchange (OQ-brennecke2025-02, -17). Mena and colleagues ask whether novel governance structures prevent managerial authority (OQ-mena2026-05).

**Before (2023–24).** Nine pieces, six core. Räcker, Geiger and Seidl ask how space coordinates and how coordinating mechanisms interact (OQ-racker2024-08, -10). du Gay and Lopdrup Hjorth ask which formalization each purpose needs (OQ-dugay2024-02). Guercini and Lechner ask how competence is learned and lost (OQ-guercini2023-08). Three technology pieces ask what happens to coordination, maintenance work and meetings (OQ-hinds2024-05; OQ-justesen2024-01; OQ-whyte2023-14).

**Movement.** The concern narrowed. Coordinating mechanisms as such (physical space, formal design, competence) have no asker in 2025–26. What remains is arrangement for innovation and the working of ties.

**Anchors (2025–26).**

- **OQ-garud2025-09** "we propose that organizations can experiment with alternatives to the main dominant themes that structure organizations and work practices." (p. 17, note 22)
- **OQ-mena2026-05** "How do novel organizational governance structures prevent the type of hierarchical and managerial authority that is prevalent in traditional organizational structures such as bureaucracies?" (p. 11, "Republican internal focus")
- **OQ-brennecke2025-02** "Research has shown that the relational activation of bridging ties evolves (Quintane & Carnabuci, 2016), yet we know little about how the longitudinal path of these ties affects brokerage behaviour." (p. 12, "Relational history and brokerage")

**Context (2023–24).**

- **OQ-racker2024-10** "Thus, we need to better understand how different coordinating mechanisms (here: roles, space, routines) interact in achieving successful integration." (p. 13, "Interrelations")
- **OQ-dugay2024-02** "the crucial question remains which kinds of formalization are necessary for each of them to pursue their respective, and very different, purposes in the most requisite manner." (p. 10, "Formality and Authority")
- **OQ-guercini2023-09** "learning is often assumed rather than directly studied, and is theorized, similar to what we have done here, in rather stylized terms (as associative learning, deliberate learning, etc.)." (p. 17, "Implications for further research")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `mena2026` | 2026-03-31 | 1 / 23 | 05 |
| 2025–26 | `brennecke2025` ★ | 2025-09-28 | 5 / 21 | 02, 03, 17, 18, 19 |
| 2025–26 | `garud2025` ★ | 2025-07-11 | 8 / 8 | 03, 04, 05, 06, 07, 08, 09, 10 |
| 2023–24 | `hinds2024` ★ | 2024-10-29 | 13 / 25 | 03, 04, 05, 06, 07, 08, 09, 16, 17, 18, 19, 20, 25 |
| 2023–24 | `hsu2024` | 2024-10-04 | 1 / 6 | 08 |
| 2023–24 | `phillips2024` | 2024-09-13 | 1 / 12 | 07 |
| 2023–24 | `racker2024` ★ | 2024-08-27 | 12 / 12 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12 |
| 2023–24 | `stark2024` | 2024-06-18 | 1 / 9 | 06 |
| 2023–24 | `dugay2024` ★ | 2024-03-19 | 5 / 5 | 02, 04, 05, 06, 07 |
| 2023–24 | `justesen2024` ★ | 2024-03-15 | 3 / 17 | 01, 04, 16 |
| 2023–24 | `whyte2023` ★ | 2023-12-21 | 5 / 13 | 02, 09, 12, 13, 14 |
| 2023–24 | `guercini2023` ★ | 2023-06-07 | 9 / 9 | 04, 05, 06, 07, 08, 09, 10, 11, 12 |

### F14 Affect and the self (near-fading)

**Concern.** What do emotion, affect, atmosphere and the self do in organizing and in research?

**Now (2025–26).** One piece, two questions. Friedrich asks how affective connection to more-than-human life can be cultivated and how routines can engage the senses (OQ-friedrich2026-07, -06).

**Before (2023–24).** Twelve pieces. Bacq and colleagues ask what shame and other negative emotions do to entrepreneurship (OQ-bacq2023-03, -04). Arnold and Costas ask otherness research to turn to affect (OQ-arnold2023-10). Jørgensen and Beyes ask for a politics of atmosphere (OQ-jorgensen2023-05). Ocasio leaves emotions untheorized in institutions (OQ-ocasio2023-01). Petriglieri and Ashford, and Wright and colleagues, ask what the researcher's self does (OQ-petriglieri2023-02; OQ-wright2023-05).

**Movement.** The rule calls the stack persistent because one 2026 piece asks it. I report it as near-fading and keep it out of the live ranking: twelve pieces before 2025, one since, and that one asks about affect toward the non-human, not about emotion among people at work.

**Anchors (2025–26).** The stack holds only these two questions from 2025–26.

- **OQ-friedrich2026-07** "How can affective connections to life forces (zoe) be cultivated as the organization fosters proximity and entanglement with more-than-human others" (p. 13, "Attuning to zoe/geo/techno spheres")
- **OQ-friedrich2026-06** "Which spaces, moments, and routines can be created to slow down or de-focus and extend the rational mind while activating multiple bodily senses" (p. 13, "Attuning to zoe/geo/techno spheres")

**Context (2023–24).**

- **OQ-arnold2023-10** "it is tantamount for otherness research to focus much more strongly on the realm of affect. Only in this way can we understand how a specific social order casts certain people as Other." (p. 15, "An agenda for otherness research")
- **OQ-ocasio2023-01** "Despite its complexity, the theory is not comprehensive, and important phenomena such as values and emotions have received less attention here." (pp. 16–17, "Conclusion")
- **OQ-bacq2023-03** "Future research could also explore how other negative emotions (e.g., guilt or pity, instead of shame) might have an energizing impact on entrepreneurship" (p. 16, "Stigma, shame, and entrepreneurship: The promise for social change")

**Ledger.**

| Period | Piece | Online | In stack / in piece | Question numbers |
|---|---|---|---|---|
| 2025–26 | `friedrich2026` | 2026-04-01 | 2 / 17 | 06, 07 |
| 2023–24 | `hinds2024` | 2024-10-29 | 2 / 25 | 21, 22 |
| 2023–24 | `paca2024` | 2024-07-26 | 1 / 4 | 05 |
| 2023–24 | `jaser2024` | 2024-03-19 | 1 / 10 | 02 |
| 2023–24 | `justesen2024` | 2024-03-15 | 1 / 17 | 13 |
| 2023–24 | `wright2023` | 2023-12-21 | 2 / 5 | 05, 06 |
| 2023–24 | `jorgensen2023` ★ | 2023-12-21 | 5 / 5 | 03, 04, 05, 06, 07 |
| 2023–24 | `arnold2023` | 2023-09-30 | 2 / 12 | 07, 10 |
| 2023–24 | `ocasio2023` | 2023-08-04 | 1 / 4 | 01 |
| 2023–24 | `leitzinger2023` | 2023-06-23 | 1 / 33 | 02 |
| 2023–24 | `fotaki2023` | 2023-03-11 | 2 / 5 | 05, 07 |
| 2023–24 | `petriglieri2023` ★ | 2023-02-20 | 2 / 4 | 02, 05 |
| 2023–24 | `bacq2023` ★ | 2023-02-18 | 5 / 10 | 02, 03, 04, 05, 09 |

## Fading threads inside live stacks

No whole stack meets the strict test for fading, which is no piece since 2024. Five narrower threads do meet it. Each sits inside a stack that stays live on other questions, so the stack's status hides the loss.

1. **Machine theorizing** (in F01 and F08). The 2024 editorial asked whether language models can theorize and how authors must disclose them (all seven questions of `cornelissen2024`), and Suddaby asked what algorithmic science does to theory (OQ-suddaby2024-05, -06). No question from 2025–26 asks about machines in theorizing.
2. **Social movements and markets** (in F09). All 33 questions of `leitzinger2023`, with OQ-bacq2023-01 and OQ-pozner2023-10. No question from 2025–26 asks how movements form or how they shape markets; activists appear as one actor among several in legitimacy tests (OQ-patriotta2025-09), and firms appear as challengers themselves (OQ-mena2026-19).
3. **Surveillance and hidden digital work** (in F08). All ten questions of `jaser2024` and all seventeen of `justesen2024`, with OQ-scherer2023-02, -05, -09. No question from 2025–26 asks about either.
4. **Participation in open strategy** (in F12 and F07). All seven questions of `friesl2023` and all eleven of `langenmayr2024`. The 2026 democracy papers do not take up open strategy.
5. **Coordinating mechanisms as such** (in F13). All twelve questions of `racker2024` on space, all nine of `guercini2023` on competence, and the formal-design questions OQ-dugay2024-02, -04.

## Cross-cutting notes

**1. The cross-level problem.** Authors in almost every stack ask how what they theorized at one level adds up at another, and they leave the bridge to later work. Schildt and Kodeih ask how macro ideology arises from local practice (OQ-schildt2025-03); Mena and colleagues ask whether workplace democracy scales to society (OQ-mena2026-23); Brennecke and colleagues ask how dyadic histories become network structure (OQ-brennecke2025-15, -14); Nigam and colleagues place person-institutions in a multi-level system (OQ-nigam2025-03); Pavlisa and colleagues ask to move from firm to industry (OQ-pavlisa2026-05); Patriotta and colleagues ask how crises migrate across fields (OQ-patriotta2025-02); the organization-as-actor pieces ask to look past the single organization (OQ-winkler2025-04; OQ-dion2025-06). The worry is old: OQ-powell2023-13, OQ-whyte2023-04, OQ-guercini2023-11, OQ-pozner2023-13, OQ-stevenson2024-03, OQ-hsu2024-04.

**2. Where a concept stops.** A shared worry in 2025–26 is that the field's core terms now cover so much that nobody can say what falls outside them. The questions take one form: what counts as an organization (OQ-dion2025-14, -02), an institution (OQ-hawbaker2025-03; OQ-derekrobinson2025-07), a logic (OQ-schildt2025-02), the demos (OQ-mena2026-01), a stakeholder to whom the firm answers (OQ-pavlisa2026-03); and what foundations a programme must agree on first (OQ-schoeneborn2026-02). Earlier forms of the same worry: a paradox (OQ-seidemann2024-16), a team (OQ-hinds2024-09), the human–machine boundary (OQ-grodal2024-08), an extreme context (OQ-wright2023-04), one practice or several (OQ-whyte2023-13), the reach of institutional explanation (OQ-ocasio2023-04), and the criteria for settling such disputes at all (OQ-abend2024-02).

**3. Theory handed over untested.** The journal publishes theory, and its authors close by passing the empirical test to someone else. The presupposition is that someone will take it up. Recent instances: OQ-derekrobinson2025-09, OQ-werner2026-07, OQ-corver2026-13, OQ-nigam2025-09, OQ-wedlin2025-03, OQ-schoeneborn2026-10, OQ-pavlisa2026-02. Earlier: OQ-guercini2023-04, -05, OQ-jackwerthrice2023-03, OQ-georgiou2023-03, OQ-sasaki2024-01, OQ-whyte2023-08, OQ-hsu2024-02, OQ-phillips2024-06, OQ-laine2023-09. The demand for evidence recurs in the closing sections of pieces in every ranked stack.

**4. An unsettled political order as backdrop.** Across four stacks (F12, F09, F04, F01) the 2025–26 askers write against the same background: democratic backsliding and right-wing tendencies (OQ-mena2026-17, -21), truth-bending autocrats and populism (OQ-giovannoni2025-08), post-truth communication and total takeover (OQ-winkler2025-02, -03), polarized environments (OQ-patriotta2025-04), political struggles over versions of logics (OQ-schildt2025-05), unsettled times in which traditional institutions deteriorate (OQ-nigam2025-10), and the question whether inquiry can stand apart from political crisis (OQ-ernst2026-07). The background was already present in OQ-sasaki2024-06, OQ-dugay2024-06, OQ-scherer2023-10, OQ-pozner2023-16 and OQ-jaser2024-10. It is not a stack, because the pieces ask different questions against it.

## Residual

Seven questions fit no stack. All date from 2023–24.

- **OQ-paca2024-02, OQ-paca2024-03, OQ-paca2024-04.** Organizational mythology and archetypes as a guide to change. No other piece asks about myth-making as such. Hawbaker and Hallett use "mythologies" for the stories around institutional persons, and I placed that question in F04. OQ-paca2024-05, on members' psychic needs, sits in F14.
- **OQ-chia2023-03.** A plea to strategy theorists to admit practice, situation and potential beside means–ends reasoning. No stack concerns strategy as such.
- **OQ-laine2023-05, OQ-laine2023-06, OQ-laine2023-08.** Whether non-human objects can bear entrepreneurial qualities. The questions border F11 and the more-than-human thread in F06 and ask neither stack's question.

## What I was unsure about

1. **The three-piece bar turns on single riders.** F10, F11, F12 and F13 sit exactly at three pieces, and in each the third piece contributes one question (OQ-friedrich2026-11, OQ-winkler2025-04, OQ-corver2026-05, OQ-mena2026-05). Without those four tags the four stacks would read persistent, not prevailing. I kept each tag on its merits and flag the dependence.
2. **F06 joins three sub-threads** (sustainability change, ecological dependence, crisis response). Split, none would reach three pieces.
3. **F09 joins legitimacy contests with social movements.** The join gives the stack its 2023 depth. A reader who separates the two would find movements-and-markets fading and legitimacy contests carried by two papers from 2025.
4. **F03 is the widest and shallowest ranked stack.** Its 2025–26 questions share a form (is this disagreement productive?) more than an object.
5. **F14 is not fading by the letter of the rule.** I report it as near-fading on the evidence.
6. **Second tags.** 207 questions carry a second stack. A stricter hand would thin F07 and F08 in 2025–26 further and would take rider pieces from F02 and F05.
7. **Three placements could go either way:** `gumusay2024` between F10 and F01 (I gave most questions both), the five brokerage and creativity questions of `brennecke2025` in F13 as well as F02, and OQ-winkler2025-05 between F03 and F09 (I gave it both).
8. **OQ-hollerer2026-04.** The reader's paraphrase names AI and sustainability as examples; the quotation does not. I counted the question in F01 only.
