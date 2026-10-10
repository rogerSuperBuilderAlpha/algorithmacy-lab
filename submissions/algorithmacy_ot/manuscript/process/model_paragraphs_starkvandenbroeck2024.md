# Stark & Vanden Broeck (2024): what each body paragraph does

**Date:** 2026-10-08 · **Written by:** Claude (agent read; nothing here is the author's text)
**Source:** Stark, D., & Vanden Broeck, P. (2024). Principles of algorithmic management. *Organization Theory, 5*(2), 1–24. DOI 10.1177/26317877241257213.
**Read from:** version of record, `pyphi-experiments/submissions/lima_pdw/literature/pdfs/starkvandenbroeck2024.pdf`. I read the body (printed pp. 2–16) in full, from the first paragraph of the Introduction to the last paragraph of "Out of Bounds". Abstract, notes, acknowledgements and references are outside the map.

**How the counts were made.**

- *Paragraph boundaries.* I took them from the typesetting, not from the text flow: `pdftotext -bbox-layout` gives each line's left edge, and a paragraph starts where a line sits 12 points inside its column margin or directly follows a heading. That yields 79 indented starts plus 10 paragraphs that follow a heading, 89 in all. Column and page breaks do not split a paragraph; paragraph 76 runs from the foot of p. 13 across Table 1 onto p. 14.
- *Words* are whitespace tokens with footnote numerals removed. Treat them as good to within two or three words (line-break hyphens are the main source of error).
- *Sentences* were split by script and spot-checked by hand. Quoted speech stays inside its host sentence; I corrected paragraphs 59 and 63 by hand for that reason.
- *Cites* counts author-year references, one per year cited, so a string of three years by one author counts three and a source cited twice in a paragraph counts twice. I removed one false hit by hand (a date in paragraph 68).
- *Job* and *Device* are my readings. The first three columns after the section name are measurements.

## 1. Paragraph table

| # | Section | Words | Sentences | Cites | Opens with | Job | Device |
|---|---|---|---|---|---|---|---|
| 1 | Introduction | 105 | 4 | 1 | "The opening decades of the 20th century marked" | Sets a historical scene: scientific management as the knowledge claim of a new class of engineers standing between capital and labor. | historical analogy (scene-setting) |
| 2 | Introduction | 108 | 5 | 3 | "The opening decades of the 21st century now" | Repeats the scene for the present with software engineers and algorithmic management, and says a capital-versus-labor lens will miss things again. | parallel case + claim |
| 3 | Introduction | 78 | 2 | 6 | "Our opening premise, therefore, departs from the widespread" | Names the view the paper departs from (algorithmic management as amplified Taylorism) and lists four labels other analysts use for it. | contrast with prior work |
| 4 | Introduction | 41 | 1 | 0 | "Despite some similarities, algorithmic management should not be" | States the counter-thesis in a single sentence: the two managements rest on different worldviews. | claim (one-sentence thesis) |
| 5 | Introduction | 25 | 2 | 1 | "Our title harks back, of course, to Taylor’s" | Explains the title and disclaims advocacy. | hedge/boundary |
| 6 | Introduction | 97 | 2 | 0 | "Instead, our task in this essay is to" | States the task of the essay: theorize algorithmic management against changes in the shape of organization and in the roles of many kinds of user. | purpose statement |
| 7 | Introduction | 86 | 3 | 0 | "As we elaborate in more detail below, we" | Narrows to the special focus (eroding boundaries) and introduces co-optation as what algorithmic management attempts. | claim + first use of key term |
| 8 | Introduction | 59 | 3 | 0 | "Our project is less restricted than a new" | Sets the scope: narrower than a theory of society, wider than a theory of the firm, pitched at the organizational level. | hedge/boundary |
| 9 | Introduction | 83 | 4 | 0 | "In the pages that follow, we briefly diagnose" | Lays out the order of the paper and names the method (dimensions of comparison). | roadmap |
| 10 | Introduction | 91 | 2 | 4 | "The study of algorithmic management will be distorted" | Justifies adding a second comparator, collaborative management, and states the three-way comparison. | claim+support (method rationale) |
| 11 | Introduction | 30 | 1 | 0 | "As we shall see, algorithmic management operates within" | Previews the result in one sentence that lists the five ways algorithmic management differs. | roadmap (preview of findings) |
| 12 | Current approaches | 150 | 6 | 6 | "Within just a few years, the study of" | Announces three limitations in current work and gives the first: it confines algorithmic management to the workplace. | contrast with prior work |
| 13 | Current approaches | 77 | 2 | 4 | "Kellogg et al. (2020) go beyond this singular" | Credits Kellogg and colleagues with going further, then shows that they stay inside the same workplace frame. | contrast with prior work (concede, then limit) |
| 14 | Current approaches | 76 | 3 | 4 | "To be clear: bringing labor process theory into" | Concedes what labor process theory contributes before insisting the topic must not become a branch of labor studies. | hedge/boundary (concession) |
| 15 | Current approaches | 71 | 2 | 0 | "For reasons we elaborate in greater detail in" | Says why the first limitation matters: the workplace frame narrows the concept and the supervision frame hides tasks other than surveillance. | claim+support |
| 16 | Current approaches | 99 | 4 | 4 | "A second strand of thinking defines algorithmic management" | Gives the second strand, algorithmic management as automated managerial decisions, in two quoted definitions. | contrast with prior work (quotation) |
| 17 | Current approaches | 205 | 9 | 5 | "Our major problem with this perspective is the" | Rebuts the second strand on two grounds (action is spread across humans and machines; many functions were never managerial) and gives the paper’s own definition. | claim+support + definition |
| 18 | Current approaches | 86 | 3 | 1 | "A third limitation of existing research is that" | Gives the third limitation, calling algorithmic management bureaucratic, and shows it in one named study. | contrast with prior work (named study) |
| 19 | Current approaches | 74 | 4 | 2 | "But not all research is captive to this" | Names a study that escapes the third limitation and sides with it. | contrast with prior work (ally) |
| 20 | Current approaches | 114 | 5 | 3 | "Bureaucracy is hierarchical—in its conceptual as well as" | Explains why the bureaucracy label fails: bureaucracy is hierarchical in structure and in categories, and algorithmic orderings need not be. | definition + contrast |
| 21 | Organizing beyond boundaries | 100 | 2 | 0 | "The limitations of the dominant perspectives can be" | Compresses the three limitations into one two-part formula and sets the paper’s own view against it. | transition (summary + pivot) |
| 22 | Organizing beyond boundaries | 103 | 4 | 0 | "In analyzing the basic organizing principles of algorithmic" | States the paper’s positive starting point: tie algorithmic management to changes in the topology of organization. | claim |
| 23 | Organizing beyond boundaries | 183 | 5 | 6 | "Organization theory is familiar with the idea that" | Grants that organization theory already looks beyond the firm, then argues network theory still assumed firms and trust, so it falls short. | contrast with prior work (concede, then limit) |
| 24 | Organizing beyond boundaries | 111 | 2 | 0 | "Take a basic operation: an online purchase by" | Walks through a single online purchase to show one click acting across many organizations, by a user employed by none of them. | example/illustration |
| 25 | Organizing beyond boundaries | 95 | 2 | 2 | "Whereas in the past, organization was generally understood" | Generalizes from the example: platform organization is better read as unbounded than as porous, and supplies the Möbius image. | claim + metaphor |
| 26 | Organizing beyond boundaries | 95 | 2 | 4 | "This Möbius topology and its corresponding basic operation" | Sets the platform beside hierarchy, market and network, names its verb (co-opted) and states the management challenge that follows. | contrast (four-term formula) + problem statement |
| 27 | Organizing beyond boundaries | 74 | 2 | 0 | "Our diagnosis is that this challenge cannot be" | Argues that none of the three familiar forms can meet the challenge and hands the task to algorithmic management. | claim+support (elimination) |
| 28 | The Principles of Algorithmic Management | 40 | 1 | 0 | "To identify and analyze the distinctive principles of" | Names the five dimensions of comparison in one sentence. | roadmap |
| 29 | Organizational form | 100 | 3 | 8 | "Although some scientific managers addressed the office" | Gives the organizational form of scientific management (factory) and of collaborative management (project), with sources for each. | contrast (two baselines) |
| 30 | Organizational form | 70 | 3 | 0 | "The organizational form most corresponding to algorithmic management" | States the form for algorithmic management: the platform, whose resources are neither inside nor outside. | claim (states the principle) |
| 31 | Organizational form | 104 | 5 | 0 | "Identifying the platform as the organizational form most" | Qualifies the claim: the platform is typical, not exclusive, and firm-internal AI tools still borrow its vocabulary. | hedge/boundary |
| 32 | Organizational form | 220 | 8 | 5 | "Moreover, as our reference to algorithmic-assisted decision-making indicates," | Widens the meaning of platform beyond social media with one extended case, MyJohnDeere. | example/illustration (named platform) |
| 33 | Organizational form | 69 | 2 | 3 | "Thus, when we write about the platform as" | Restates what the authors mean by platform as form: spreading platformization, more than the growth of consumer platforms. | definition (restatement) |
| 34 | Organizational form | 100 | 3 | 1 | "Although scientific, collaborative, and algorithmic management emerged in" | Notes that the three styles coexist today and shows all three inside Amazon. | hedge/boundary + named example |
| 35 | Object of management | 102 | 4 | 2 | "As the previous section suggests, the three management" | Links back to the previous subsection, then gives the object of scientific management (supervising labor) and of collaborative management (coordinating specialists). | contrast (two baselines) |
| 36 | Object of management | 243 | 12 | 8 | "The notion of post-industrialism as a new stage" | Develops collaborative management at length: recombinant innovation, simultaneous engineering, self-directed coordination and what project managers did. | claim+support (extended exposition) |
| 37 | Object of management | 104 | 4 | 5 | "Certainly never explicitly voiced as workers’ self-management, collaborative" | Adds that collaborative management was a kind of self-management and traces its cultural sources. | claim+support |
| 38 | Object of management | 28 | 1 | 0 | "If scientific management is about managing the relationship" | Asks, in one sentence, what relation algorithmic management addresses, given the first two answers. | transition (question pivot) |
| 39 | Object of management | 60 | 2 | 3 | "Algorithmic management is frequently about managing labor; and" | Answers: it can manage labor and specialists, and also actors outside the organization. | claim (states the principle, part one) |
| 40 | Object of management | 40 | 1 | 0 | "It is characteristic of algorithmic management that—whether as" | Adds the key term: whatever their role, the actors are configured as users. | claim (one-sentence key term) |
| 41 | Object of management | 89 | 5 | 0 | "The language of “the user” is so familiar" | Defends treating the everyday word user as an analytic category and raises three questions about it. | problematization (questions) |
| 42 | Object of management | 152 | 7 | 2 | "Consider, for example, an ordinary consumer on a" | Takes a consumer on a streaming platform, agrees with two prior accounts and pushes past them: such people use the platform. | example + contrast with prior work |
| 43 | Object of management | 72 | 4 | 0 | "If I buy a ticket to a concert," | Makes the point with a homely first-person analogy between a concert hall and Spotify. | example/illustration (analogy) |
| 44 | Object of management | 141 | 8 | 5 | "“The user” is, doubtless, socially constructed" | Concedes that the user is socially constructed, then lists what streaming users actually do to show how varied they are. | hedge/concession + enumeration |
| 45 | Object of management | 96 | 6 | 1 | "These heterogeneous users are managed algorithmically. Algorithms co-opt" | States the mechanism: algorithms co-opt and organize users, first by categorizing them, and all the handling is algorithmic. | claim+support (mechanism) |
| 46 | Object of management | 127 | 4 | 7 | "Moreover, the user—as nothing more than an ensemble" | Adds that the user is a bundle of shifting profiles and distinguishes this from the built-in user of science and technology studies. | contrast with prior work |
| 47 | Object of management | 36 | 2 | 0 | "Stated simply, our argument here is that algorithmic" | Restates the subsection’s argument in two sentences. | summary restatement |
| 48 | Object of management | 85 | 4 | 3 | "Specialists are also those for whom platform software" | Extends the user category to specialists and marks the point at which tools become communication partners. | claim+support (extension) |
| 49 | Object of management | 75 | 2 | 11 | "Algorithmic management also shapes and is shaped by" | Extends it to professionals with a run of fields, one citation per field. | list/enumeration (citation list) |
| 50 | Object of management | 138 | 6 | 1 | "The study of the dynamics of the relations" | Calls the study of professionals and algorithms young, poses two questions, and argues the jurisdiction frame cannot cover it. | problematization + contrast with prior work |
| 51 | Object of management | 86 | 3 | 4 | "If in its infancy, the study of algorithmic" | Credits Christin’s comparative work, states what can be said on that basis and calls for more comparative studies. | hedge/boundary + research call |
| 52 | Ideology | 91 | 4 | 0 | "For Frederick Winslow Taylor and his followers, scientific" | Gives the ideology of scientific management: efficiency, with the stopwatch and the one best way. | claim+support (baseline one) |
| 53 | Ideology | 98 | 3 | 4 | "By contrast, not efficiency but flexibility was the" | Gives the ideology of collaborative management: flexibility, argued against locking resources into one best way. | contrast (baseline two) |
| 54 | Ideology | 131 | 4 | 1 | "The chorus of flexibility was sung in many" | Shows the varieties of flexibility talk and names the theme they share, empowerment. | list/enumeration + claim |
| 55 | Ideology | 145 | 7 | 1 | "The ideology of algorithmic management plays with and" | Places algorithmic ideology against that theme: some flexibility, no empowerment, no necessary tie to markets. | claim+support (differentiation) |
| 56 | Ideology | 124 | 3 | 2 | "To the extent that it has an emancipatory" | Says what its emancipatory strain promises (freedom from rules and from choices) and sets this against three positions that reduce algorithms to bureaucracy or markets. | claim + contrast with prior work |
| 57 | Ideology | 47 | 2 | 0 | "The recommender system—paradigmatic in online cultural forms but" | Illustrates with the recommender system in two sentences. | example/illustration |
| 58 | Ideology | 158 | 8 | 0 | "Instead of efficiency or flexibility, we characterize the" | Names the principle, immediacy, and develops its first sense (speed) against the time horizons of the other two styles. | definition + three-way contrast |
| 59 | Ideology | 99 | 5 | 0 | "Similarly, algorithmic logic is one of ceaseless ubiquity," | Adds ubiquity, convenience and abundance to the first sense and ends on an invented chant. | claim+support (elaboration) |
| 60 | Ideology | 137 | 6 | 2 | "Second, immediacy is unmediated. In the ideology of" | Gives the second sense of immediacy (unmediated access) for senior management and calls it a fantasy. | definition + critique |
| 61 | Ideology | 150 | 7 | 2 | "Meanwhile, to the regular user algorithmic management promises" | Applies the second sense to end users and professionals, with mental-health services as the case. | claim+support + example |
| 62 | Ideology | 52 | 2 | 0 | "If immediacy characterizes the ideology of algorithmic management" | Turns to a second strand of the ideology, totalizing knowledge claims, and lays out the three steps to come. | transition + roadmap |
| 63 | Ideology | 75 | 3 | 0 | "More than a century ago, the scientific managers" | Step one, managers: recounts the old pact between engineers and managers and says it is unraveling. | claim+support (invented dialogue) |
| 64 | Ideology | 78 | 7 | 0 | "More broadly, the ideology and practices of algorithmic" | Step two, professionals: defines professional expertise as contextual judgment. | definition + contrast |
| 65 | Ideology | 81 | 4 | 1 | "The knowledge of algorithmic management is also a" | Defines algorithmic knowledge as specialized yet claimed to apply in any field, and so a challenge to professional expertise. | definition + contrast |
| 66 | Ideology | 135 | 6 | 0 | "The ideology of the new class projects in" | Step three, society: ranks the knowledge claims of Taylorism, Leninism and the present in rising order of reach. | historical comparison (escalating series) |
| 67 | Modality | 82 | 3 | 1 | "As a third dimension along which we outline" | Introduces and defines the dimension itself, modality, by way of Elias. | definition |
| 68 | Modality | 97 | 3 | 2 | "Considered in these terms, the modality of scientific" | Gives the modality of scientific management: standardization, with Taylor’s own words. | claim+support (baseline one, quotation) |
| 69 | Modality | 46 | 2 | 1 | "Opposed to standardization, the modus operandi of collaborative" | Gives the modality of collaborative management: diversification. | contrast (baseline two) |
| 70 | Modality | 104 | 4 | 1 | "In much of the scholarly literature, algorithmic management" | Lists three positions in the literature, rejects all three and names the paper’s term, synthetic. | contrast with prior work (enumerated) + claim |
| 71 | Modality | 104 | 5 | 1 | "Take first, for example, recent developments in generative" | Illustrates with generative AI and recommender systems. | example/illustration (named products) |
| 72 | Modality | 155 | 3 | 7 | "The resulting classifications in the algorithmic mode are" | Explains that algorithmic classifications are not human categories, using one concrete data scenario and a quoted source. | claim+support (quotation) |
| 73 | Modality | 107 | 3 | 3 | "That algorithmic classifications can depart from conventional categorizations" | Draws the consequence for professionals: departing from routine categories can prompt new thinking, as one study shows. | implication + named study |
| 74 | Accountability | 112 | 6 | 2 | "In the frame of scientific management, accountability is" | Gives accountability under scientific management: vertical, replacing personal authority. | claim+support (baseline one) |
| 75 | Accountability | 83 | 5 | 4 | "By contrast, in the post-bureaucratic, collaborative frame, accountability" | Gives accountability under collaborative management: lateral and heterarchical, with an informant’s line. | contrast (baseline two, quotation) |
| 76 | Accountability | 165 | 7 | 5 | "Neither vertical nor horizontal, accountability in algorithmic management" | States the principle (twisted) and explains it by a triangular structure of ratings, with eBay as the case. | claim+support + named example |
| 77 | Accountability | 85 | 3 | 4 | "If the cybernetic feedback loops of algorithmic management" | Shows that the feedback loops are neither vertical nor horizontal and that this lets operators deflect accountability. | claim+support (neither/nor) |
| 78 | Accountability | 146 | 6 | 5 | "Heterarchical forms already provided opportunities for deflection: one" | Traces earlier openings for deflection, asks who is accountable when an algorithm decides, and ends on a six-word verdict. | claim+support + question |
| 79 | Accountability | 104 | 5 | 0 | "Table 1 presents a summary view of algorithmic" | Presents Table 1 and defends the simplification of putting the argument in cells. | hedge/boundary (table gloss) |
| 80 | Accountability | 112 | 4 | 0 | "Whichever route taken in making those connections, we" | Draws the dimensions together: algorithmic management reaches past the organization to co-opt the wider world. | synthesis claim |
| 81 | Accountability | 132 | 4 | 0 | "Scientific management displaced the personal authority of the" | Recaps the three styles once more by scope and closes on a question about contradictions. | contrast (three styles) + question hand-off |
| 82 | Out of Bounds | 146 | 7 | 3 | "During the middle of the 20th century, Robert" | Tells how Merton and Lazarsfeld studied organization and communication on parallel tracks. | historical analogy (scene-setting) |
| 83 | Out of Bounds | 104 | 5 | 2 | "Like our Columbia predecessors, the research agenda that" | Positions the authors’ agenda as like theirs and unlike it: organization and communication are now joined. | contrast with prior work (like/unlike) |
| 84 | Out of Bounds | 121 | 5 | 1 | "Our research agenda is also shaped by and" | Brings in Yates, who studied bureaucratic organization as communication, and summarizes her book. | prior-work exposition |
| 85 | Out of Bounds | 125 | 5 | 1 | "Like Yates, we study how organization and communication" | States how the agenda follows Yates and where it departs: technologies as communication partners. | contrast with prior work (like/unlike) + research direction |
| 86 | Out of Bounds | 134 | 3 | 1 | "The notion of technology as a communication partner" | Gives the idea of a communication partner a longer history and current examples. | claim+support + named examples |
| 87 | Out of Bounds | 101 | 5 | 0 | "Yates’ work offers a further jumping off point:" | Proposes a further step, treating technology as organization, and ends on a question. | speculative proposal (question) |
| 88 | Out of Bounds | 139 | 5 | 3 | "As we have argued in this paper, algorithmic" | Restates the paper’s argument and closes on the claim about topology: organizing without boundaries. | summary + closing claim |
| 89 | Out of Bounds | 132 | 8 | 0 | "To close, we turn to the field of" | Ends with a field anecdote from a megachurch whose last line is a quotation. | example/illustration (closing anecdote) |
Two things in the table are the source's, not extraction errors. Paragraph 67 calls modality the third dimension, although it is fourth in the list the authors give in paragraph 28. Paragraph 89 switches from *we* to *I* for the anecdote.

## 2. Sections and subsections

Headings are verbatim. "First sentence" is the mean length of the paragraphs' opening sentences.

| Section / subsection | Level | Paragraphs | Words | Mean words | Range | First sentence | Cites |
|---|---|---|---|---|---|---|---|
| Introduction | 1 | 11 | 803 | 73 | 25–108 | 27 | 15 |
| New Problems and New Answers for a New Era | 1 | 16 | 1,713 | 107 | 71–205 | 33 | 41 |
| — Current approaches | 2 | 9 | 952 | 106 | 71–205 | 24 | 29 |
| — Organizing beyond boundaries | 2 | 7 | 761 | 109 | 74–183 | 44 | 12 |
| The Principles of Algorithmic Management | 1 | 54 | 5,612 | 104 | 28–243 | 23 | 118 |
| — (lead-in, no subheading) | — | 1 | 40 | 40 | — | 40 | 0 |
| — Organizational form | 2 | 6 | 663 | 110 | 69–220 | 26 | 17 |
| — Object of management | 2 | 17 | 1,674 | 98 | 28–243 | 22 | 52 |
| — Ideology | 2 | 15 | 1,601 | 107 | 47–158 | 22 | 13 |
| — Modality | 2 | 7 | 695 | 99 | 46–155 | 23 | 16 |
| — Accountability | 2 | 8 | 939 | 117 | 83–165 | 20 | 20 |
| Out of Bounds | 1 | 8 | 1,002 | 125 | 101–146 | 23 | 11 |
| **Body** | | **89** | **9,130** | **103** | **25–243** | **25** | **185** |

The level-1 heading "New Problems and New Answers for a New Era" has no text of its own; its first subheading follows it directly.

**Introduction (paragraphs 1–11).** These are the shortest paragraphs in the paper. Two matched historical paragraphs open it, each about 105 words, with the same first five words and only the century changed; the second ends by saying what a two-class lens will miss, and the third picks that up as the premise the paper rejects. From paragraph 3 on the paragraphs shrink and turn procedural: seven of the eleven open on *our* or *we*, and two are single sentences (4, the thesis; 11, the preview). Citations appear in five paragraphs only, and six of the fifteen sit in paragraph 3, where each borrowed label for the rejected view carries its source.

**Current approaches (12–20).** One sentence counts the limitations (three) and the subsection then spends four, two and three paragraphs on them. Inside each block the criticized view comes first, in its holders' own quoted words and with their names (12, 16, 18); the authors' reply comes in a separate paragraph that carries few citations or none (15, 17, 20); and a concession sits between the two (13, 14, 19). Topic sentences here are ordinal labels of nine to fifteen words (*A second strand*, *A third limitation*), and the longest paragraph of the subsection, 17 at 205 words, is the one that states the authors' own definition of the construct.

**Organizing beyond boundaries (21–27).** The first paragraph compresses the whole previous subsection into one 71-word sentence and then turns to the authors' view. The order after that is: own starting point (22), the nearest existing theory conceded and then limited (23, the longest at 183 words and six citations), one worked example with no citation (24), the generalization and its metaphor (25), the four-term formula and the problem it poses (26), and the elimination of the three familiar forms (27). Opening sentences are the longest in the paper (mean 44 words) and four of the seven paragraphs have only two sentences; the last sentence of 27 names algorithmic management as the answer, which the next heading takes up.

**The Principles of Algorithmic Management, lead-in (28).** One 40-word sentence that lists the five dimensions in the order the subsections follow.

**Organizational form (29–34).** The two baselines share the first paragraph, which front-loads its citations (eight, four of them inside the opening concession). The principle follows in a 70-word paragraph with no citation at all. Three paragraphs of qualification and widening come next, each opening on a connective (*Identifying…*, *Moreover*, *Thus*); the named platform, MyJohnDeere, gets the longest paragraph (220 words) and all five of its sources are gathered into one closing parenthesis. The subsection ends on a second named case, Amazon, used to show the three styles side by side.

**Object of management (35–51).** The longest subsection runs in four movements. Baselines take 449 words (35–37), and collaborative management gets most of them. A one-sentence question (38) pivots to the answer, given in two short paragraphs (39, 40) that end on the key term. The user is then built up over seven paragraphs (41–47, 713 words) in the order problem, example, analogy, concession, mechanism, refinement, two-sentence restatement. The last four paragraphs (48–51) extend the category to specialists and professionals and end on a call for comparative studies. Paragraph length swings most here, from 28 to 243 words, and the short paragraphs (38, 40, 47) mark the turns. Eleven of the 52 citations sit in paragraph 49, one per professional field.

**Ideology (52–66).** Baselines take three paragraphs (52–54, 320 words: one for scientific management, two for collaborative). Paragraphs 55–57 separate algorithmic ideology from the shared baseline theme and give one example. Paragraphs 58–61 name the principle and work through its two senses, two paragraphs each, the second announced by *Second*. Paragraph 62 is a hinge that announces a further strand and its three steps, which 63–66 then walk. This is the least-cited stretch of the paper: 13 citations in 1,601 words and eight paragraphs with none. Invented slogans and dialogue (55, 59, 63) do the work that named platforms do elsewhere, and three paragraphs end on a sentence of twelve words or fewer (58, 61, 65).

**Modality (67–73).** The only subsection that opens by defining its dimension, because the word is not self-explanatory (67). One paragraph per baseline follows (97 and 46 words). Paragraph 70 numbers three positions in the literature, rejects them in a seven-word sentence and names the authors' term in the sentence after. Then come an example paragraph (71), a deepening paragraph built around one quoted source (72), and a consequence for professionals shown through one study (73). Every paragraph carries at least one citation, and the subsection ends on a borrowed quotation.

**Accountability (74–81).** The comparison is at its strictest: three consecutive paragraphs for the three styles, each opening on a sentence of nine or ten words that contains the defining term. Paragraphs 77 and 78 develop the third, and 78 ends on a six-word verdict. The last three paragraphs (79–81, 348 words) serve the whole Principles section and sit under this subheading only because no new heading intervenes: a gloss on Table 1, a synthesis, and a last three-style recap that ends on a question. None of the three carries a citation.

**Out of Bounds (82–89).** The most even paragraphs in the paper (101–146 words). The section is built from two like/unlike pairs: a paragraph that expounds a predecessor (82 on Merton and Lazarsfeld, 84 on Yates) and then a paragraph that opens *Like…* and turns on *But whereas* (83, 85). Paragraph 86 gives the central idea a history and current examples, 87 proposes a further step and ends on a question, 88 restates the argument, and 89 is an anecdote. The section contains no paragraph of limitations and no list of contributions.

## 3. Whole-paper patterns

**Length.** The body has 89 paragraphs and 9,130 words. The mean paragraph is 103 words, the median 100, the range 25–243 and the standard deviation 40. The paper has 363 sentences, 4.1 per paragraph, at a mean of 25 words. Nine paragraphs run 50 words or fewer (4, 5, 11, 28, 38, 40, 47, 57, 69) and ten run 150 or more (12, 17, 23, 32, 36, 42, 58, 61, 72, 76). Twenty-three paragraphs (26%) have one or two sentences.

**How paragraphs open.** I sorted each opening sentence by its grammatical subject and its first move.

| Opens on | Paragraphs | Share |
|---|---|---|
| A claim about the phenomenon (management style, platform, user) | 33 | 37% |
| An authorial move in *we*/*our* (premise, task, diagnosis, agenda) | 21 | 24% |
| A transition or backward hook (*By contrast*, *Moreover*, *Thus*, *Second*, *If X…*) | 19 | 21% |
| The literature or a named scholar | 10 | 11% |
| An example cue (*Take*, *Consider*, *If I buy*) | 5 | 6% |
| A question | 1 | 1% |

Claims and authorial moves together open 61% of paragraphs. A citation almost never does. Two paragraphs open with a named scholar as grammatical subject (13 and 87), and eight more open on a body of work (*A second strand of thinking*, *Organization theory*). Twenty paragraphs have a citation somewhere in their first sentence, nearly always trailing in a parenthesis. The opening sentence averages 25 words (median 23, range 4–71). Fifteen openers run twelve words or fewer and ten run forty or more, and the long ones cluster in the framing sections, where an opener often restates the previous paragraph in a subordinate clause before it moves.

**Where citations sit.** The paper has 185 author-year references. Thirty-two paragraphs (36%) carry none, and fourteen paragraphs (16%) carry 89 of them (48%). Only 15 of the 185 are narrative citations with the scholar as subject; they cluster where the authors agree or disagree with a specific study (13, 16, 18–20, 67, 72–76, 84). The rest trail in parentheses, and 20 paragraphs end on a citation parenthesis. Paragraphs that state the authors' own principle are usually uncited (4, 30, 40, 45 with one, 58, 80).

**How the introduction is built.** Eleven paragraphs, in this order: (1) a historical scene a century back; (2) the same scene now, and the lens that will not do; (3) the view the paper rejects, with its labels and their sources; (4) the counter-thesis in one sentence; (5) a note on the title that disclaims advocacy; (6) the task; (7) the special focus and the key term; (8) the scope, set between two larger projects the paper declines; (9) the roadmap; (10) the reason for a second comparator; (11) a one-sentence preview of the five findings. The construct the paper will build is not defined here. Paragraph 7 says what it attempts, and the definition waits for paragraph 17.

**How the critique of current approaches is run.** The authors count the limitations before they give them, then take each as a block: state the view in its holders' words, concede what it gets right or who escapes it, reply in the authors' own voice. They name the scholars they disagree with and credit them in the same breath, and they mark agreement as flatly as disagreement: "We agree." (p. 4). The reply paragraphs argue from the nature of the thing criticized (what bureaucracy is, what managers did) and lean on few citations. The next subsection opens by folding all three limitations into a single formula, so the critique leaves the reader with one portable sentence.

**How each "principles" subsection is run.** The internal order repeats in all five:

1. Scientific management first, in one paragraph or the first half of one, with its term stated in the opening sentence.
2. Collaborative management second, opened by *By contrast* or *Opposed to*, in the same paragraph (Organizational form, Object) or the next (Ideology, Modality, Accountability). In Object and Ideology it then gets one or two paragraphs more.
3. A pivot: a question (38), a literature paragraph that lists the wrong answers (70), a paragraph that plays the new style against the baseline theme (55), or none.
4. Algorithmic management third, named by one word or phrase that the table later reuses, usually through a *not X or Y but Z* or *neither… nor* sentence (30, 58, 70, 76).
5. A named example beside the term, in the paragraph that states it or the one that follows (in Ideology, one paragraph before): MyJohnDeere (32), a streaming consumer and Spotify (42–43), the recommender system and a web search (57–58), ChatGPT and other generators (71), eBay and Talkspace (76–77).
6. Qualification and consequence: where the principle stops, what it does to specialists and professionals, what remains unknown.

Subsections do not share an ending. Organizational form ends on a second named case; Object on a call for research; Ideology on an escalating three-step historical series; Modality on a borrowed quotation; Accountability on a verdict of six words, before the three paragraphs that close the whole section. Three of the five return to professionals near the end (Object 49–51, Ideology 61 and 64–65, Modality 73). The baselines are not hurried: across the five subsections the two older styles receive about a fifth of the words before the focal style is named.

**How the paper ends.** The closing section does not summarize first. It opens with a new historical scene (82), as the introduction did, and uses two predecessors to say what the authors' research agenda keeps and what it changes. A speculative question follows (87). The summary comes second to last (88) and returns to the image from the framing section. The last paragraph is a field anecdote that moves to a setting the paper has not discussed, and its final words are an informant's: "we have a database" (p. 16).

**Habits of construction worth checking a draft against.**

- *Contrast carries the paragraphs.* Forty-five of 89 contain an explicit contrast marker (*whereas*, *by contrast*, *neither*, *rather than*, *instead*, *not simply*), and the new term nearly always arrives as the third member after two rejected ones.
- *Short paragraphs are hinges.* The one- and two-sentence paragraphs sit at turns: thesis (4), preview (11), pivot question (38), key term (40), restatement (47), example (57), new strand (62).
- *The authors speak in their own person at every joint.* Fifty paragraphs contain *we* or *our*, 28 in the first sentence. Disagreement is announced, not implied: "As you will now expect, we disagree." (p. 12).
- *An example gets its own paragraph and a name.* Example paragraphs open on an imperative and stay with one case long enough to reach a detail, then compress it: "John Deere harvests data" (p. 6).
- *Paragraphs that state a principle end short.* The dense build stops on a sentence of a dozen words or fewer that the reader can carry: "The platform operator leverages rather than delegates." (p. 14).
- *Em-dashes weld glosses onto terms.* The body has 35, about 3.8 per 1,000 words, in 24 paragraphs.
- *Questions are used sparingly and structurally.* Fourteen question marks in the body; five paragraphs end on one (38, 41, 43, 81, 87), and one of those (81) hands off to the next section.

**Where a plain first draft would most likely differ.**

- It would make paragraphs the same size. This paper's run from 25 to 243 words, and the variation is doing the structural work.
- It would cite in every paragraph. Here a third of the paragraphs carry no citation, the authors' own claims stand uncited, and half of all references are packed into fourteen paragraphs that review or enumerate.
- It would open paragraphs with short topic sentences. The median opener here is 23 words and often begins with a subordinate clause that carries the previous point (*Although…*, *If…*, *Whereas…*) before the main clause states the new one.
- It would state the focal claim first and treat the comparison cases as background. This paper gives each baseline a full, sourced paragraph before the focal term appears, so the term arrives as the answer to a set-up question.
- It would give examples as generic clauses inside claim paragraphs. This paper names the platform, gives it a paragraph, and places it next to the claim it serves.
- It would end with a summary and a contributions list. This paper puts its summary second to last and ends on a scene.
