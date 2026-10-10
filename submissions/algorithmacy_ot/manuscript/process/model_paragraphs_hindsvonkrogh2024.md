# Paragraph map: Hinds & von Krogh (2024)

Hinds, P., & von Krogh, G. (2024). Generative AI, emerging technology, and organizing: Towards a theory of progressive encapsulation. *Organization Theory*, 5(4), 1–14. Theory Article.

Source read: `pyphi-experiments/submissions/lima_pdw/literature/pdfs/hindsvonkrogh2024.pdf`, all 14 pages (body runs pp. 1–12). Read 2026-10-08.

## How I counted

- **Paragraph boundaries.** I cropped each page into its two columns with `pdftotext -layout` and took every indented line, plus the first line under each heading, as a paragraph start. Column and page breaks do not split a paragraph. That yields 35 body paragraphs.
- **One boundary to know about.** The neutrality statement in the Introduction ("Importantly, our stance toward GenAI is neutral…") starts at the top of a column with no indent, so I count it as the tail of paragraph 2, not as its own paragraph. It reads like a separate move; the typesetting says otherwise.
- **Words** are whitespace tokens from the reading-order extraction, running heads and page numbers removed. Treat them as good to about ±3.
- **Sentences** are counted by terminal punctuation, with "et al.", "e.g.", "i.e." and page locators excluded. Treat as ±1 in the long paragraphs.
- **Cites** counts each dated reference to a work, parenthetical or narrative; a string of three works in one parenthesis counts three. Undated back-references ("as Weick and Roberts show") are not counted; I note them in the Job column where they matter. Page locators for quotations are not counted separately.
- The paper has one footnote (attached to paragraph 25, pointing to Waardenburg et al., 2022). It is outside the counts.

## 1. Paragraph table

| # | Section | Words | Sentences | Cites | Opens with | Job | Device |
|---|---|---|---|---|---|---|---|
| 1 | Introduction | 128 | 4 | 4 | "Emerging technologies, especially AI, have been heralded as" | States the occasion (AI tests whether existing organization theory suffices), narrows to GenAI, and announces that the paper builds on Bailey et al.'s relational perspective. | claim+support, with purpose statement |
| 2 | Introduction | 315 | 10 | 0 | "A relational view fundamentally argues for a move" | Glosses the borrowed perspective in one sentence, argues why GenAI makes it more necessary (hidden learning leaves the technology illegible to users), names the coined construct for the first time in its last argued sentence, then closes on a three-sentence statement that the authors take no normative side. | claim+support, ending in hedge/boundary |
| 3 | Introduction | 96 | 3 | 0 | "The relational perspective has to date not considered" | Names the gap in the borrowed perspective and introduces the construct as the answer to it, with a one-clause working definition. | gap + construct introduction |
| 4 | Introduction | 83 | 3 | 0 | "We use examples of team coordination and team" | Announces the illustration (teams and team coordination, as "illustration and thought experiment") and says it will ground wider implications. | roadmap |
| 5 | Generative AI | 182 | 7 | 5 | "“Generative AI” (GenAI) is a broad term denoting" | Defines the technology, separates it from earlier AI by what it can do, and reports findings on output quality and user performance. | definition |
| 6 | Generative AI | 116 | 5 | 0 | "A prominent example of GenAI is the use" | Describes large language models as the leading instance and how they learn with little supervision. | example/illustration |
| 7 | Generative AI | 188 | 5 | 2 | "LLMs, diffusion models, and related approaches can summarize" | Lists what these systems now do across kinds of work, then adds learning through feedback and two headline achievements (science, the medical licensing exam). | list/enumeration |
| 8 | A Relational Perspective on Generative AI | 55 | 2 | 1 | "In this paper, we focus on how GenAI" | Restates the paper's purpose and names the perspective it will use and whose it is. | transition (purpose restated) |
| 9 | A Relational Perspective on Generative AI | 315 | 10 | 4 | "A relational approach is particularly relevant with GenAI," | Summarizes Bailey et al.'s relational view with three direct quotations and its lineage, endorses it for GenAI, and ends by saying that applying it exposes a need to extend it. | exposition of prior work, ending on a turn |
| 10 | A Relational Perspective on Generative AI | 426 | 16 | 2 | "Fundamental to the relational view of emerging technology" | Takes two terms from the source theory (relational dynamics, relational cascades), illustrates each with small hypothetical cases, and marks where GenAI departs from the source: relations now form inside the technology and keep changing as it learns. | example/illustration + contrast with prior work |
| 11 | A Relational Perspective on Generative AI | 305 | 7 | 0 | "Note that this obscuring visibility is a process," | Asserts the need for a process theory, then works one mundane case (an AI summarizing meetings) through the vocabulary step by step, tagging each new function and relation in parentheses. | example/illustration (worked case) |
| 12 | A Relational Perspective on Generative AI | 122 | 4 | 1 | "Constellations of relations, as described by Bailey et" | Draws the section's conclusion: GenAI multiplies relational complexity while cutting users' and researchers' view of it, which sets up the construct. | claim + handoff |
| 13 | Generative AI and Progressive Encapsulation | 70 | 3 | 0 | "The basic function of GenAI systems today is" | Grounds the construct in the technical architecture and poses the section's question of how GenAI comes to encapsulate functions and relations. | technical premise + framing question |
| 14 | Generative AI and Progressive Encapsulation | 228 | 9 | 2 | "Our concept of “encapsulation” is inspired by the" | Gives the term's source in computer science, says what the authors borrow it to mean (an expanding black box around relations and functions), and argues why the process is progressive. | definition (by borrowing) |
| 15 | Generative AI and Progressive Encapsulation | 265 | 10 | 0 | "The architectures, capacities, and flexibility of GenAI raise" | States the theoretical claim proper (more functions and relations get collapsed and encased; inputs and outputs can be studied, the process cannot), runs one hypothetical (a manager hiring with GenAI), and restates the claim with its two linked effects. | claim+support with one worked hypothetical |
| 16 | Generative AI and Progressive Encapsulation | 167 | 6 | 0 | "To keep track of such progressive encapsulation, we" | Specifies what a theory of the construct must do: where to look (the site of work), what to describe, and what to explain. | theory specification / agenda |
| 17 | Implications for Theory through the Illustration Team Coordination | 181 | 7 | 1 | "To ground our understanding of a relational view" | Frames the illustration as illustration and thought experiment about "as yet unknown" relations, and justifies the choice of team coordination. | roadmap + case justification |
| 18 | Team coordination | 161 | 5 | 2 | "The mechanisms and processes of coordination, that is," | Defines coordination and its formal and informal sides, then states what earlier digital tools did for formal coordination and what they did not do. | definition + baseline from prior work |
| 19 | Team coordination | 210 | 7 | 4 | "A novel capacity of GenAI is learning about" | Claims GenAI can enter informal coordination, anchors that in one empirical study of drug discovery teams, and conjectures how GenAI could take over the practice that study found. | claim + empirical anchor + conjecture |
| 20 | Team coordination | 155 | 6 | 1 | "To theorize about the changes in team coordination" | Applies the perspective to the same study, pushes the conjecture to its limit (GenAI absorbs informal coordination outright), and ends on a question about knock-on team dynamics. | application ending in research question |
| 21 | Team coordination | 141 | 6 | 1 | "In her study of medical teams in a" | Takes a second empirical study (Mayo's hospital teams), asks two opposed questions about what GenAI would do to its finding, and says what a relational analysis would supply. | example/illustration + research questions |
| 22 | Team coordination | 198 | 7 | 0 | "GenAI challenges us to rethink our theories and" | Generalizes from the two studies to a call for processual theorizing, adds the digital twin as a further possibility, and names the question it raises. | claim + research direction |
| 23 | Team coordination | 221 | 6 | 2 | "Another pertinent question relates to teams’ ability to" | Brings in Weick and Roberts's heedful interrelating and asks two questions about what hidden coordination does to a team's and an organization's capacity to respond to crisis. | research questions anchored in a classic |
| 24 | Team coordination | 149 | 5 | 3 | "We also speculate that GenAI may affect the" | Opens a second topic (team boundaries), reviews the literature on fluid boundaries and multi-team systems, and ends on the conjecture that GenAI makes boundaries more porous. | prior work, then conjecture |
| 25 | Team coordination | 214 | 10 | 1 | "This conjecture on team boundaries raises important questions" | Develops the boundary conjecture: GenAI guides movement between teams, may propose team compositions, and may assemble what Mortensen and Haas call participation hubs. | claim+support (elaborated conjecture) |
| 26 | Team coordination | 338 | 13 | 3 | "In arguing for a more flexible and dynamic" | Takes Mortensen and Haas's resource brokerage, casts GenAI as the broker, weighs the gain (less conflict) against the costs (disempowerment, weaker ties, surveillance), and closes on how scholars can study this without access to the models. | claim+support, trade-off, method note |
| 27 | Discussion | 261 | 7 | 1 | "We began this article by noting that the" | Recaps the paper in order (gap, background, construct, illustration, positive and negative effects) and restates the neutral stance. | recap |
| 28 | Discussion | 328 | 13 | 2 | "The theory of progressive encapsulation needs refinement in" | Concedes the theory is unfinished, names three kinds of force that speed or stop encapsulation, announces five domains of inquiry, and gives the first (power) as seven questions. | hedge/boundary, then research questions |
| 29 | Discussion | 187 | 7 | 4 | "Second, connecting to an old debate on the" | Second domain: division of labor, tied to the automation debate, posed as two named alternatives and a third question. | research questions |
| 30 | Discussion | 135 | 4 | 1 | "Third, foundation models built on vast and diverse" | Third domain: creativity in teams; grants GenAI's idea generation, then asks what happens to the secondary functions of creative work. | research questions |
| 31 | Discussion | 96 | 5 | 0 | "Fourth, GenAI is able to be simultaneously present" | Fourth domain: knowledge sharing across teams; states the benefit, concedes the ideas are thin, asks two questions. | research questions |
| 32 | Discussion | 93 | 4 | 0 | "Fifth, there are many micro-related questions that follow" | Fifth domain: individual psychological responses and loss of meaning at work, posed as three questions. | research questions |
| 33 | Discussion | 184 | 6 | 1 | "As these five areas of inquiry indicate, we" | Converts the five domains into a methodological call: process theories alongside variance theories, a named style of process theorizing, and a recommended focus on inputs, outputs and forces. | call for a kind of theory |
| 34 | Discussion | 232 | 8 | 1 | "Since ChatGPT-4 was launched late in 2022, most" | Answers the objection that AI moves too fast to theorize, argues for prospective theorizing, and places the paper as one modest attempt at it. | contrast with an opposing position |
| 35 | Discussion | 100 | 4 | 1 | "Like most disruptive innovations there is of course" | Concedes uncertainty about uptake, then argues organizations are already prepared to deploy GenAI at scale. | closing claim on the phenomenon |

**Totals.** 35 paragraphs, about 6,645 words, 50 dated citations. Eleven paragraphs (2, 3, 4, 6, 11, 13, 15, 16, 22, 31, 32) carry no citation.

## 2. Section by section

### Introduction — 4 paragraphs, 622 words, mean 156

The four paragraphs run occasion-and-purpose, perspective-and-rationale, gap-and-construct, illustration. Each opens by picking up a term the previous one closed on: paragraph 1 ends by naming the relational perspective and paragraph 2 opens "A relational view"; paragraph 2 ends its argument on progressive encapsulation and paragraph 3 defines it. Citations sit only in paragraph 1 (four of them, three bunched in the first sentence); the other three paragraphs are the authors arguing in their own voice, with "we argue", "we contend" and "we advocate" doing the work a citation would otherwise do. Topic sentences are long, 30 to 49 words, and the one long paragraph (315 words) is where the rationale gets argued.

### Generative AI — 3 paragraphs, 486 words, mean 162

A plain background section in three steps: define the class, give the leading instance, list the uses. The authors write it almost without first person (none in any of the three paragraphs) and place citations at sentence ends as support for factual claims. Paragraph 7 is the paper's one catalogue paragraph, with a single 60-word sentence that lists some fifteen uses. Nothing in the section mentions organizations theoretically; it only establishes that the technology learns and adapts, which the next two sections need.

### A Relational Perspective on Generative AI — 5 paragraphs, 1,223 words, mean 245

This is the longest-paragraphed section and the most exemplified. It opens with a 55-word paragraph that restates purpose, spends a 315-word paragraph expounding the source theory through three direct quotations, and then gives two paragraphs of 426 and 305 words to hypothetical cases. Examples arrive in the second or third sentence of a paragraph, signalled by "for example" (eight times in paragraphs 10 and 11 together), and each is closed by a sentence that translates it back into the vocabulary of functions and relations. Paragraphs 9 and 12 both end on the limit of the borrowed view, so the section closes by handing the reader the problem that the construct will answer.

### Generative AI and Progressive Encapsulation — 4 paragraphs, 730 words, mean 183

Four paragraphs define the construct: technical premise, origin and meaning of the term, the theoretical claim with one hypothetical, and what a theory of it must cover. Topic sentences are the shortest in the paper here (14 to 23 words). The section has only two citations, both in paragraph 14, one to the computer-science source and one to the second author's earlier work; the claim paragraph (15) cites nobody. Two sentences recur nearly word for word: the architecture sentence appears in paragraphs 13 and 14, and the closing question of paragraph 13 reopens paragraph 15. Whether that is deliberate restatement or a copyediting leftover, it is how the published section reads.

### Implications for Theory through the Illustration Team Coordination — 10 paragraphs, 1,968 words, mean 197

One framing paragraph sits under the section heading (181 words); nine sit under the subheading "Team coordination" (1,787 words, mean 199). The nine split into two runs: coordination (18–23) and team boundaries (24–26). The recurring unit is anchor-then-conjecture: a paragraph takes one published finding (Ben-Menahem et al., Mayo, Weick and Roberts, Mortensen and Haas), states it in a sentence or two, and then asks what GenAI would do to it. Paragraphs 20, 21 and 23 end on direct questions, and the boundary run is handed over by back-reference ("This conjecture on team boundaries"). The final paragraph is the longest in the section and ends on method, not on a finding.

### Discussion — 9 paragraphs, 1,616 words, mean 180

The Discussion has no subheadings and four parts: a recap (27), a five-item research agenda (28–32), a methodological call (33), and a two-paragraph close (34–35). The agenda items are numbered "First" to "Fifth" inside running prose, each a short setup followed by a string of questions; the five paragraphs hold 17 of the paper's 23 question marks, and they shrink from 328 words to 93. "First" is buried mid-paragraph in 28, after the admission that the theory needs refinement, so the limitation and the agenda are one move. The paper ends on a claim about organizations' readiness for GenAI; there is no "Conclusion" heading and no restatement of the contribution in the last paragraph.

## 3. Whole-paper patterns

### Paragraph length

Mean 190 words; median 182; range 55 (paragraph 8) to 426 (paragraph 10). Nine paragraphs exceed 250 words and seven fall at or under 100. Mean sentence count is about 6.7 per paragraph, so sentences average 28 words. First sentences average 28 words too (range 10 to 53): this paper does not open paragraphs on short topic sentences. Short paragraphs are signposts or agenda items (4, 8, 13, 31, 32); long ones are where an example is worked or a source expounded (2, 9, 10, 11, 26, 28).

### How paragraphs open

My classification of the 35 opening sentences:

- **Claim (19, about 54%)**: 1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 14, 15, 18, 19, 22, 24, 28, 34, 35. Several of these are claims with the authors as subject ("We also speculate that…", "Our concept of…").
- **Transition, back-reference or signpost (14, 40%)**: 4, 8, 11, 16, 17, 20, 23, 25, 27, 29, 30, 31, 32, 33. Four of these are the ordinals "Second" to "Fifth"; three open on a purpose clause ("To ground…", "To keep track…", "To theorize…").
- **Citation-led (2, 6%)**: 21 and 26, both narrative citations that put the scholars in subject position.

Four further openers carry a citation inside or at the end of the first sentence (1, 5, 12, 29), but the sentence's subject is the phenomenon or the authors. No paragraph opens on a parenthetical-citation string or on "Research has shown".

### How the Introduction is built

1. **Occasion and purpose (128 words).** Phenomenon and the challenge to theory, with three citations; then "In this article, we consider"; then the base perspective by name and author.
2. **Perspective and rationale (315 words).** One-sentence gloss of the relational view; why GenAI raises the stakes; what is lost by treating AI as an entity; first naming of the construct; neutrality statement.
3. **Gap and construct (96 words).** What the perspective has not considered; the construct introduced to meet it; a claim that it is key.
4. **Illustration and payoff (83 words).** The example domain and what it will be used for.

Three things are absent. The Introduction has no section-by-section roadmap ("the paper proceeds as follows"), no numbered list of contributions, and no literature review beyond the one base paper. The gap is stated once, in a single sentence, and it is a gap in one named perspective, not in "the literature".

### How the construct is defined

Four paragraphs, 730 words, after a full section that sets up the perspective being extended.

1. **Technical premise (70 words).** What the technology does at the level of architecture, and the question that follows.
2. **Term (228 words).** Where the word comes from, what the authors borrow it to mean, and why the adjective "progressive" applies. The definition is introduced with "We borrow the term", a first-person act, and is given as a description of a process, not as a formal "X is defined as" sentence.
3. **Claim (265 words).** What the construct predicts, including the short declarative "Encapsulation is a relational accomplishment"; one hypothetical (hiring); restatement.
4. **Theory specification (167 words).** What a theory of the construct should observe, describe and explain.

The construct gets no table, figure, propositions, dimensions, or boundary conditions, and the authors never contrast it with neighbouring constructs (opacity, black-boxing, automation, delegation). They signal the modesty openly: the title says "towards a theory", the claim verbs are "conjecture" and "theorize", and the Discussion says the theory needs refinement.

### How the central illustration is run

Ten paragraphs, 1,968 words, about 30% of the body.

1. **Frame (17).** Illustration plus thought experiment; why this domain.
2. **Baseline (18).** Define coordination; what older technology did and did not do.
3. **First anchor and conjecture (19).** A capability claim, one empirical study, what GenAI would do to its finding.
4. **Apply the perspective, extreme case, question (20).**
5. **Second anchor, paired questions, what the perspective adds (21).**
6. **Generalize; a further scenario; a question (22).**
7. **Classic anchor; two questions about crisis (23).**
8. **Second topic opened via literature, ending in a conjecture (24).**
9. **Conjecture elaborated (25).**
10. **Third anchor; trade-offs; how to study it (26).**

The illustration contains no data, no vignette of a real organization using GenAI, and no single running case. It is a sequence of published findings from the pre-GenAI teams literature, each re-read through the construct. Hedging is carried by modal verbs (may, might, could, likely: 36 in these ten paragraphs) and by ending paragraphs on questions.

### How the discussion and ending are built

- **Recap first.** Paragraph 27 walks the paper in order in past tense ("We began…", "we proposed…", "We pointed to…") and restates neutrality.
- **Limitation folded into agenda.** A nine-word sentence admits the theory needs refinement; the rest of the Discussion's middle is five domains of questions, each tied where possible to an existing debate (power, division of labor, creativity, knowledge sharing, individual responses).
- **Methodological call.** Process theories to complement variance theories, with one cited style of process theorizing.
- **Defence of the genre.** The second-to-last paragraph voices the sceptic ("so why bother?"), answers with a case for prospective theorizing, and sizes the paper as "just one such attempt".
- **Last paragraph on the phenomenon.** A hedge, then a claim about organizational readiness, ending on a "see also" citation. No summary sentence, no epigram.

There are no sections titled Limitations, Contributions, Implications for Practice, or Conclusion.

### Other habits worth knowing

- **First person carries the argument.** "We argue", "we contend", "we posit", "we conjecture", "we theorize", "we speculate" and similar verbs appear about 22 times, concentrated in the Introduction, the construct section, and the recap. The Generative AI background section has none.
- **Citation density is low and uneven.** Fifty citations in about 6,650 words is 7.5 per thousand. One source, Bailey et al. (2022), accounts for seven of them and is the only work quoted at length. The construct's claim paragraph and three of four Introduction paragraphs cite nothing.
- **Examples are small, hypothetical and many.** Theme park, robot apple picker, meeting summaries, hiring, a manager's message to staff. Each takes two to five sentences and each is marked "for example" (13 times in the paper, 8 of them in two paragraphs).
- **Restatement is tolerated.** The purpose statement appears in paragraphs 1 and 8; the neutral stance in 2 and 27; the architecture sentence in 13 and 14; the framing question in 13 and 15.
- **Two small errors in the published text**, for anyone quoting it: "Hass" for Haas in paragraph 25, and "bult" for built in paragraph 23.
