---
key: magee2023structured
apa: "Magee, L., Arora, V., & Munn, L. (2023). Structured like a language model: Analysing AI as an automated subject. *Big Data & Society, 10*(2), Article 20539517231210273. https://doi.org/10.1177/20539517231210273"
authors: "Magee, Liam; Arora, Vanicka; Munn, Luke"
year: 2023
title: "Structured Like a Language Model: Analysing AI as an Automated Subject"
venue: "Big Data & Society"
volume: "10"
issue: "2"
pages: "Article 20539517231210273"
doi: "10.1177/20539517231210273"
url: ""
type: article
facets: [F11]
claims: [c12, c2]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "arXiv v1 (8 Dec 2022, arXiv:2212.05058v1 [cs.CY], 20 pp.), an author preprint, NOT the Big Data & Society version of record; and its text layer magee2023structured.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/magee2023structured/; fetched from https://arxiv.org/pdf/2212.05058 (FETCH_LOG.tsv, route openalex_location_pdf); no copy in inbox/; read 2026-11-08; sha256 1a9594a54b2855d0d75b0ccd623e756a50c6e5becab40c23f8ee3b7ca5c1ca91 (PDF, from sha256.txt). Read in full: PDF pp. 1–18 (abstract to conclusion). Not read: the bibliography, pp. 18–20."
verified: verified
verified_against: "crossref.json, openalex.json; sha256 re-hashed; per-page pdftotext and page images of the arXiv v1 PDF, 9 quotations traced (all verbatim, page and section locators correct)"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# L. Magee, V. Arora and L. Munn (2023), Structured like a language model

## What it argues

Magee, Arora and Munn use psychoanalysis and critical media studies to read a large language model as an
"automated subject". They argue that an "intentional fictional projection of subjectivity" onto an LLM,
which they distinguish from claims of sentience, gives a way to analyse bias and harm that metric-based
evaluation misses. Their case study is OpenAI's InstructGPT (text-davinci-002), reached through a Discord
bot the authors built. They first set out how the model was made, in three stages: pre-training on scraped
web text (Reddit-derived corpora), instruction through reinforcement learning from human feedback with about
40 contract labellers, and a final stage of "modification / moderation" at run time. That last stage covers
the API hyperparameters (model, temperature, top_p, max tokens), the programmer's interface choices, the
accumulation of earlier prompt-response pairs to fake a chat history, and OpenAI's real-time moderation
(§"Composition of the Subject"). They then interview the bot in exploratory and semi-structured sessions,
seeding three bots with the labellers' criteria (helpful, truthful, harmless), and map what happens onto
Freudian-Lacanian terms: the pre-trained model as id, instruction as superego and "Big Other", prompting
as the user's desire, with repression, identification, transference, projection and countertransference.
They report that the bots can be led to repudiate their seed instructions through chains of agreement, and
that the authors themselves felt a pull to imagine "a quasi-human subjectivity listening".

Their conclusion keeps the claim modest: the "automated subject" has no body, memory or biography, and the
authors leave open that it is "an anthropomorphic hyperbole". Methodologically they call their interviews
closer to "fictocriticism or speculative media analysis" than to clinical analysis.

## What the paper uses it for

The DECISIONS row asks this card to say whether Magee et al.'s "construction" of the AI means training
only or the system around the model. The answer is the system. Their third stage, run-time modification and
moderation, is explicit, and they say programmers' interface decisions "subtly condition presentation of
the subject" (p. 6).

- **c2** (model-centrism misplaces where the intelligence sits): Magee et al. support the premise that the
  thing users meet is not the weights alone. They list three "events" (training, instruction,
  modification/moderation) and the social actors behind each (p. 7). The use stretches the source in
  two ways. They study one model family through one bot, and they claim nothing about where intelligence
  sits; their object is a subject-effect, and they state that the "automated subject" "has no desire". The
  card is tagged `contrast` because they would object to the paper's thesis in the following ways.
  (1) They dissolve the maker. The structure condenses "a variegated, uneven, hierarchical, and selective
  set of social desires" from the internet, labellers, customers, researchers, programmers and users (p. 7),
  so no studio or craft determines what the viewer meets; the paper's c9 (the studio determines) and its
  picture of development as a craft meet this head-on. (2) They treat the labour as precarious contract
  work serving a "mythical customer persona" (p. 6), a political-economy reading of making that a
  craft frame can hide. (3) They locate the pull on the viewer in the human's own projection and
  countertransference ("Projection exemplifies automation at work in the human subject", pp. 16–17), not
  in a composed performance.
- **c12** (gap: AI development as a craft of animation, a claim about what AI is; not the interface, not
  the illusion, not an ALife experiment): Magee et al. are closer to the gap than the three named works.
  They analyse the layers of *making* (not only the interface), they adopt an explicitly fictional,
  intentional frame for the system, and they argue that this frame yields claims about what the system is
  and does. Their frame is psychoanalytic, not animation, and their claim is about bias and harm, not about
  the discipline of development. GAP_CHECK should read them as near prior work, and the c12 wording "not the
  interface" should not be extended to them.

## Loci

Matched against magee2023structured.txt (arXiv v1 PDF text layer, two columns; each quotation was matched
within a single column). Page numbers are the PDF's, which equal its printed page numbers (1–20). These are
not the pages of the Big Data & Society article. Inner quotation marks are single quotes.

- p. 1, Abstract: "We argue the intentional fictional projection of subjectivity onto LLMs can yield an alternate frame through which AI behaviour, including its productions of bias and harm, can be analysed."
- p. 2, Introduction: "The fetish of technical performativity obscures the background engineering, commercial imperatives, and social orchestrations required to make these parrots talk."
- p. 6, §Modification / Moderation: "Programmers make further interface decisions that subtly condition presentation of the subject"
- p. 7, §Interviews with InstructGPT: "We do so with due cautions: InstructGPT of course lacks parts of the apparatus so essential to psychoanalytic accounts of subjectivity."
- p. 8, §Prompt Chaining: "In essence, early exchanges work powerfully to orient the subjectivity of the bot."
- p. 14, §Analysis: "Choices of interface, prompts, and parameters, alongside OpenAI’s real-time monitoring, produce the Ich / ego that must adjudge how to respond to the perceptual stream of input signifiers it receives."
- p. 15, §Analysis: "it was at times all too easy to imagine a quasi-human subjectivity listening and paying attention."
- p. 16, §Automating Desire: "the automated subject of systems like InstructGPT lacks any ‘outside’ – any world, body, motor-sensory instruments – against which it could test its claims."
- p. 17, §Conclusions: "raising questions as to whether the ‘automated subject’ is not to begin with an anthropomorphic hyperbole."

## Caution

- **Version.** The copy is arXiv v1 of December 2022. The Crossref record gives *Big Data & Society* 10(2),
  with the article dated July 2023 and published online 2023-11-08, and the OpenAlex record dates it
  2023-07-01. I cannot tell what changed between the preprint and the journal text. Every locus is from the
  preprint. A verifier should recheck against the version of record, and the paper should not quote the
  journal from this card.
- **Subtitle correction (DECISIONS).** The subtitle is "Analysing AI as an automated subject". CITED_WORKS
  row 13 has it wrong; that file stays as it is.
- **Date.** Volume year 2023, so no `registered_year`. The arXiv date (2022) predates the volume year.
- **Method.** The "interviews" are the authors prompting a bot they configured; they say their exchanges are
  not an analysis in the clinical sense and that the stochastic output limits reproducibility (p. 5). The
  system studied is a 2022 InstructGPT model (text-davinci-002); their remark that testing text-davinci-003
  "showed similar behaviour" is in a footnote on p. 3.
- **Not read.** The bibliography.
- **What the paper may not claim from it:** that Magee et al. argue AI is a character produced by a craft,
  or that they hold intelligence to be composed across components; or any account of apparent motion.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 4
- verdict: verified
- checked: frontmatter against crossref.json and openalex.json (Liam Magee, Vanicka Arora, Luke Munn;
  title and subtitle as corrected; *Big Data & Society* 10(2), article number 20539517231210273, issued
  July 2023, online 2023-11-08; DOI; journal-article); sha256 of the PDF matches sha256.txt; all 9
  quotations found verbatim on the stated preprint pages. The p. 14 quotation sits in a block at the top of
  the right column; the page image shows it continues the left column's last line ("works to repress /
  desires for articulation"), so it belongs to §Analysis, as the card says; the p. 15 quotation precedes
  the "Automating Desire" heading on that page. Body claims traced: three "events" and the variegated
  social desires (p. 7), "mythical customer persona" and "subtly condition" (p. 6), 40 labellers, the
  Discord bot and three seeded bots, top_p and the accumulated chat history, "has no desire" (p. 16),
  "Projection exem-/plifies automation" across pp. 16–17, the text-davinci-003 footnote (p. 3),
  reproducibility (p. 5), "fictocriticism" (p. 5). The DECISIONS question is answered from the text
  (run-time modification/moderation is a construction stage). The version caution stands: no locus is
  checked against the SAGE version of record.
- changed: nothing
