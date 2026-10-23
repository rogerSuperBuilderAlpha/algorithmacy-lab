# Spaces in the Stream: Decision Spaces and the Legibility of Streaming AI Output

### Final outline for a theory article in *Human–Computer Interaction* (Taylor & Francis)

> **Drafted by Claude (Opus 5.5) for Roger Hunt, 20 October 2026.**
>
> - This is a map of moves with the sources each move rests on. It is not prose. Following your writing skill's finding, you write the sentences.
> - **ROGER** marks text you have already written; it lives in `abstract_intro_edit.md` and your proposal.
> - **[NEEDS]** marks a decision only you can make.
> - The working title is a suggestion; keep yours if you prefer.
>
> **How each section is laid out:** the section's job, its moves, then a **section bibliography**. Each source is annotated *for that section*: what the source is, what it shows (with its number and locator), how the section uses it, and any limit on that use. A source used in more than one section is annotated in full where it first appears and cross-referenced after that. A master reference list in APA 7 closes the file.
>
> **Status codes** (my reading this session):
> - **[F]** read in full, or in its substantive sections;
> - **[A]** abstract only;
> - **[M]** metadata only, not read;
> - **[P]** preprint, not peer reviewed.
>
> Everything marked [A], [M] or [P] should be described no more strongly than the annotation allows. Sources you have deferred (Saenger, Parkes, Gibson, O'Regan & Noë) stay flagged.

---

## What *HCI* asks of a theory paper, and how this outline meets it

| *HCI* requirement (journal aims and author documents) | Where this outline meets it |
|---|---|
| Theoretical and "framework" papers must give "a rigorous analysis developing new conceptual views ... that imply future research directions" | §2 (the scriptio continua account), §4 (the construct), §5 (falsifiable propositions) |
| Papers need "scientific implications, system design implications, and analyses of how systems are actually used" | §3 (mechanisms), §6 (design space), §1 and §3.2 (how streaming interfaces work today) |
| "Not interested in ... papers reporting only preliminary results" | No pilot data. The study appears only as the test logic in §5.5. |
| The abstract must state "the nature of the paper (theoretical, empirical, or methodological)" | Abstract, move 1 |
| No word limit is stated; the journal "favors substantial papers" | Target about 11,000 words plus references (my estimate; the 2026 *HCI* papers cited here run 26–42 typeset pages) |
| Final style: numbered first-level headings in capitals, a table of contents, APA citations | Applies at acceptance, not at review |

---

## ABSTRACT (about 200 words)

**Moves:**
1. State the nature of the paper: a theoretical article.
2. The phenomenon: people supervise AI text while it is still forming.
3. The problem: reading depends on stable text, units of sense and the freedom to look back, and streaming removes the last two.
4. The account: streamed output is a new scriptio continua.
5. The construct: decision spaces, defined, with their three functions.
6. The deliverables: four propositions and a design space.
7. The consequence for algorithmacy.

**ROGER:** Your current abstract supplies moves 2, 3, 5 and 7. Its sentences on the N = 42 protocol must go, and its causal claim needs hedging (flag F1). **[NEEDS: your rewrite.]**

No citations in the abstract.

---

## 1. INTRODUCTION (about 1,300 words)

**Job:** move from what users see, to why it matters, to the contribution.

### Moves
1. **[Context]** Watching a chatbot answer means reading text that is still being written, paced by the server rather than by the reader. **ROGER:** your [Context] paragraph, with flags F3–F6 resolved your way.
2. **[Complication]** Streaming removes the stable text and the look-backs that reading depends on. **ROGER:** your [Complication] paragraph, with F7–F11 resolved.
3. **[Consequence]** Fluent output that arrives as a recommendation suppresses scrutiny. **ROGER:** your [Consequence] paragraph, with F12–F15 resolved. Keep the drafted Gegoff sentence or cut it.
4. **[Claim]** Perception and action; the historical parallel; decision spaces in one sentence. **ROGER:** your [Claim] paragraph (F16–F17).
5. **Contribution statement**, rewriting your [Course] paragraph:
   - **C1, theoretical:** the scriptio continua account of streaming output.
   - **C2, conceptual:** decision spaces, with three functions and four falsifiable propositions.
   - **C3, design:** a four-dimension design space.
6. **Gap**, stated only as far as the search supports it:
   - "I found no work that places interface friction inside a streamed AI response, or that segments a streamed response at decision units" (searches of arXiv, Consensus and the web, 20 October 2026; `search-log.md` rows 23–34 and 51–55).
   - Define "decision spaces" at first use; the phrase appears elsewhere only in unrelated senses.
7. **ROGER:** the algorithmacy sentence, then the roadmap, rewritten to match §§2–9.

### Section bibliography

**Park, H., & Lee, Y. (2024).** The effect of text movement on eye movements in generative AI chatbots. *Archives of Design Research, 37*(4), 181–197. https://doi.org/10.15187/adr.2024.08.37.4.181. **[F]**
- *What it is:* the only eye-tracking study I found of how chatbot text movement affects gaze. N = 36, Korean expository text, four movement types drawn from 2023 chatbots, Tobii.
- *What it shows:* text generated at the bottom of the screen produced more fixation starts, more total fixation time and larger saccade amplitudes than text appearing whole at the top. Fixation starts clustered where new text appeared (Tables 9, 11–12).
- *Use here:* the opening empirical anchor that streaming changes gaze.
- *Limits:* one study; topic is confounded with condition; no comprehension or decision measure. Write "one eye-tracking study", not "evaluations" (F3).

**Liu, J., Chung, J.-W., Wu, Z., Lai, F., Lee, M., & Chowdhury, M. (2024).** *Andes: Defining and enhancing quality-of-experience in LLM-based text streaming services* [Preprint]. arXiv:2404.16283. **[F §1–2][P]**
- *What it is:* a systems paper proposing a scheduler and token pacer driven by quality of experience.
- *What it shows:* average reading consumption estimated at 4.8 tokens/s, converted from an age table of words per minute at about 1.3 tokens per word (v1 §2.1). One serving system delivered 11.2 tokens/s on a real trace (v2 §2.2).
- *Use here:* pacing is set by servers, not readers.
- *Limits:* 4.8 is an estimate used as a delivery target, not a controlled measurement (F4). Nothing in it supports "11–25 tokens/s" (F5).

**Xiao, C., & Yang, B. Z. (2025).** Streaming, fast and slow: Cognitive load-aware streaming for efficient LLM serving. In *Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology* (pp. 1–13). ACM. https://doi.org/10.1145/3746059.3747721. **[F]**
- *What it is:* a UIST paper that slows streaming on complex segments to save compute.
- *What it shows:* a PEST procedure (79 valid Prolific participants) put the 99th-percentile comfortable streaming speed at 21.20 words/s for an easy passage and 11.97 for a complex one, against about 45 words/s from the GPT-4o API (§3.2).
- *Use here:* delivery speed is a design choice, decoupled from readers.
- *Limits:* the measure is comfortable speed, not comprehension (F6). No eye tracking.

**Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025).** Fostering appropriate reliance on large language models: The role of explanations, sources, and inconsistencies. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–19). ACM. https://doi.org/10.1145/3706598.3714020. **[F]**
- *What it is:* a think-aloud study (N = 16) and a pre-registered experiment (N = 308) on hard binary factual questions.
- *What it shows:*
  - Explanations raised agreement with both correct and incorrect answers.
  - Sources and visible inconsistencies lowered agreement with wrong answers.
  - 189 of 308 participants never clicked a source.
  - With an incorrect answer, accuracy was 17.2% with an explanation and 21.8% without (Table 1).
- *Use here:* fluent explanation drives over-reliance.
- *Limits:* responses were shown whole, not streamed. The task was objective question-answering, not "collaborative decision-making" (F13).

**Bhat, M. (2025).** How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131. **[F]**
- *What it is:* a within-subjects study, N = 103, GPT-3.5 Turbo, comparing a simulated typing display (2–3 s per sentence) with a static display.
- *What it shows:* the typing display raised perceived competence (F = 40.89), trustworthiness (F = 35.21) and persuasiveness (F = 76.89), all p < .0001. Perceived effectiveness did not change (F = 0.16, p = .69) (Table 2).
- *Use here:* the only direct evidence that streaming display raises perceived authority.
- *Limits:* self-report only, with no accuracy task. Simulated typing is not token streaming. Responses may have differed between conditions (§5.5). The effectiveness null argues against "readers conflate fluency with accuracy" (F12).

**Gegoff, I., Tatasciore, M., Bowden, V. K., & Loft, S. (2025).** Deciphering automation transparency: Do the benefits of transparency differ based on whether decision recommendations are provided? *Human Factors, 67*(8), 776–794. https://doi.org/10.1177/00187208251318465. **[F]**
- *What it is:* a Human Factors experiment, N = 142, on an uninhabited-vehicle management task. Additional information varied between subjects; recommendations varied within subjects.
- *What it shows:*
  - Recommendations raised accuracy (.89 vs .85, ηp² = .16) and sped decisions.
  - Recommendations slightly lowered discrimination of accurate from inaccurate system information (.93 vs .94, F(1,94) = 4.55, p = .04, ηp² = .05) (pp. 785–787).
  - The authors call for eye tracking to see what operators attend to (p. 790).
- *Use here:* a streamed answer arrives as a recommendation, and recommendations reduce scrutiny. This is the Human Factors anchor for [Consequence].
- *Limits:* the effect is small; novices; not language-model output.

**Parasuraman, R., & Manzey, D. H. (2010).** Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055. **[F core sections]**
- *What it is:* the standard integrative review of complacency and automation bias.
- *What it shows:*
  - Complacency appears under multiple-task load, when manual tasks compete with the automated task for attention (p. 381).
  - "Looking-but-not-seeing" is used to explain *commission errors*, a form of automation bias (p. 403).
  - In Manzey et al. (2008), about half of those who missed a wrong diagnosis had sampled all the information they needed (p. 402).
- *Use here:* [Consequence]; the main use comes in §3.4.
- *Limits:* the evidence is information *sampling*, not fixations (F15a–b).

**Ridley, M., & Pawlick-Potts, D. (2021).** Algorithmic literacy and the role for libraries. *Information Technology and Libraries, 40*(2). https://doi.org/10.6017/ital.v40i2.12963. **[F pp. 1–4]**
- *Use here:* one sentence placing algorithmacy beside algorithmic literacy. Full annotation in §7.

---

## 2. STREAMING OUTPUT AS A NEW SCRIPTIO CONTINUA (about 1,500 words)

**Job:** build the historical argument that carries the theory, and answer the obvious objection.

### Moves
1. **What word spacing did.** **ROGER:** your Saenger and Parkes paragraph. Pick one term, *scriptio* or *scriptura continua* (F16). **[Deferred: page locators for "seventh century" and "Insular scribes"; F17 stays.]**
2. **What the space does for the eye.** Spaces aid both word identification and eye guidance. Without them, reading slows by about half, regressions roughly double, and landing positions shift to the start of words.
3. **The narrow focus spacing permits.** With spaces, readers process one word at a time; without them, the evidence for spreading processing across words is "rather limited".
4. **The objection.** Chatbots already print spaces. **[NEEDS: state it plainly in your words.]**
5. **The answer: a second layer of legibility, above the word.** Units of sense, not units of form. **[NEEDS: adopt or reject Parkes's "grammar of legibility" as the name for this layer. Chapter contents are unread; the chapter title is verified.]**
6. **What streams keep and what they remove.**
   - They keep word spaces.
   - They remove stable position, units-of-sense boundaries, and the freedom to look back while text is still arriving.
   - **ROGER:** "Alternatively, is the current experience of interacting with AI already optimal?"

### Section bibliography

**Saenger, P. (1997).** *Space between words: The origins of silent reading*. Stanford University Press. https://doi.org/10.1515/9781503619081. **[M, deferred]**
- *What it is:* the standard history linking word separation to silent reading.
- *Use here:* the historical claims in move 1.
- *Limits:* not read this session. Every specific claim (century, scribes, cognitive account) needs a page locator before submission.

**Parkes, M. B. (1992).** *Pause and effect: An introduction to the history of punctuation in the West*. Scolar Press (reissued Routledge, 2016). **[M, deferred]**
- *What it is:* a history of punctuation. Chapter 3 is titled "The Grammar of Legibility" (title verified via Open Library and web records).
- *Use here:* possibly the name for the second layer in move 5.
- *Limits:* contents unread; confirm which edition you cite.

**Rayner, K., Fischer, M. H., & Pollatsek, A. (1998).** Unspaced text interferes with both word identification and eye movement control. *Vision Research, 38*(8), 1129–1144. https://doi.org/10.1016/S0042-6989(97)00274-5. **[F]**
- *What it is:* two eye-tracking experiments (N = 12 and N = 10) comparing spaced, unspaced, filled, wide and flanker text.
- *What it shows:*
  - Reading rate fell 54% for sentences and 44% for passages without spaces (Exp. 1, p. 1132), and 58% in Exp. 2 (p. 1138).
  - Regressions rose from 9.7% to 17.3% for sentences (Table 1).
  - Landing positions moved from just left of a word's centre to its start (pp. 1136, 1141).
  - Missing spaces interfere with both word identification and saccade programming, the first more (p. 1143).
  - Spaces enhance upcoming words "as 'targets' for an eye movement" (p. 1129).
- *Use here:* move 2; it also grounds decision-space function 1 in §4.
- *Limits:* the paper does not discuss "low-spatial-frequency boundaries" (F7).

**Drieghe, D., Fitzsimmons, G., & Liversedge, S. P. (2017).** Parafoveal preview effects in reading unspaced text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(10), 1701–1716. https://doi.org/10.1037/xhp0000441. **[A]**
- *What it shows:* unspaced text slowed reading, with "rather limited evidence" that readers spread processing across neighbouring words.
- *Use here:* move 3. Spacing lets the system focus narrowly; streaming supplies spaces but not higher-level focus points.
- *Limits:* abstract only.

**McDonald, S. A. (2006).** Parafoveal preview benefit in reading is only obtained from the saccade goal. *Vision Research, 46*(26), 4416–4424. https://doi.org/10.1016/j.visres.2006.08.027. **[M]**
- *Use here:* optional support for move 3. Preview comes only from where the eye is aimed, so a stable target matters.
- *Limits:* the title states the claim; the paper is unread. Cite lightly or drop it.

**Knox, B. M. W. (1968).** Silent reading in antiquity. *Greek, Roman and Byzantine Studies, 9*(4), 421–435. **[M]**
- *Use here:* optional. It complicates any simple "unspaced means read aloud" story, and a careful theory paper should acknowledge it.
- *Limits:* unread; metadata from the journal's issue listing.

---

## 3. THREE MECHANISMS STREAMING DISRUPTS (about 2,800 words)

**Job:** turn the literature review into mechanism. Each subsection ends by naming the property of streams it implicates, and the three closers become the three functions of a decision space in §4.

### 3.1 Looking back: regressions repair comprehension, and streams take the text away

**Moves:**
1. Regressions are a normal and functional part of reading, about 10–15% of eye movements by one estimate and 15–25% by another.
2. Readers regress to *reread*, so the text must still be there.
3. Removing the ability to regress lowers comprehension.
4. Rereading does structural repair that forward reading does not.
5. Moving, scrolling and still-forming text change and reduce rereading.
6. **Closer:** streams move text and keep adding to it, so the look-back loses both its target and its time.

**ROGER:** "Schotter, Tran, and Rayner (2014) found that masking each word after it was read..."; and "In the context of streaming AI, auto-scrolling interfaces may move previous lines beyond the regression window..." The second needs F9's correction.

### 3.2 Being pulled forward: onsets, salience and pacing

**Moves:**
1. A single abrupt onset is identified first, but an onset is not enough by itself; capture needs it to be the only such event.
2. Bottom-up salience is powerful but short-lived, and the priority map can reset after "a break in the action".
3. In token streaming, each new word is a fresh onset at the leading edge, which matches Park & Lee's fixation-start clustering.
4. The stream's pace is set by compute, not by the reader.
5. **Closer:** streams keep renewing a forward pull, and nothing in them marks where a pause would let the map reset.

**ROGER:** your Wolfe and Yantis sentence (F10).

### 3.3 Segmenting into events: boundaries regulate processing

**Moves:**
1. Event Segmentation Theory: people parse activity into events, and updating happens at boundaries.
2. In reading, situation changes predict boundaries, and readers slow at them, even in a software-paced, clause-by-clause display that could not be reviewed.
3. Boundaries trigger both global and incremental updating.
4. Boundaries track model-derived surprise, so they are computable from text.
5. Where a break falls matters more than whether it falls:
   - breaks aligned with clauses help and misaligned breaks disrupt;
   - interruptions at coarse breakpoints cost little and at fine breakpoints a lot.
6. **Closer:** streams deliver continuous activity with no boundary marks, and any pauses they do have fall where packets fall, not where meaning breaks.

**ROGER:** your Zacks et al. (2007) sentence; "An AI agent's operation constitutes such continuous activity..."

### 3.4 Supervising fluent automation: attention, reliance and the limits of gaze

**Moves:**
1. Complacency and automation bias are failures of attention allocation, and "looking-but-not-seeing" separates fixation from detection.
2. Recommendations lower scrutiny; transparency raises bias toward agreement; fluent explanations raise reliance.
3. Streaming raises perceived competence and trust.
4. Overreliance has process signatures:
   - in interaction logs;
   - in gaze on static layouts, where attention moved "without moving judgment";
   - in pedestrians, where shorter fixations may signal over-reliance rather than easier perception.
5. **Closer:** gaze is necessary but not sufficient evidence of supervision. This sets up P4 in §5.

### 3.5 Perception as action

**Moves:**
1. Seeing as the mastery of sensorimotor contingencies.
2. Fixed text gives readers material placeholders that support a cognitive map; when those placeholders move or never settle, the map degrades.

**ROGER:** your Gibson and O'Regan sentences (F11; deferred).

### Section bibliography

#### §3.1 Looking back

**Schotter, E. R., Tran, R., & Rayner, K. (2014).** Don't believe what you read (only once): Comprehension is supported by regressions during reading. *Psychological Science, 25*(6), 1218–1226. https://doi.org/10.1177/0956797614531148. **[F]**
- *What it is:* N = 40, single one-line sentences (garden-path and unambiguous), with a trailing mask that turned each word to x's once the eyes passed it.
- *What it shows:*
  - The mask lowered comprehension (b = −0.92, z = 5.09, p < .001), and not only for ambiguous sentences (interaction p = .06) (p. 1221).
  - Comprehension was 78% in normal reading without a regression and 71% under the mask (p. 1223).
  - Readers regress 10–15% of the time (p. 1225).
- *Use here:* the causal anchor that regressions support comprehension.
- *Limits:* single sentences. Describe the manipulation as a "trailing mask".

**Booth, R. W., & Weger, U. W. (2013).** The function of regressions in reading: Backward eye movements allow rereading. *Memory & Cognition, 41*(1), 82–97. https://doi.org/10.3758/s13421-012-0244-y. **[F]**
- *What it is:* three experiments (N = 22, 32, 19) testing whether regressions serve to reread or to cue memory by location.
- *What it shows:*
  - Readers regress to reread. When the text was made illegible, regressions fell (F(1, 851) = 65.34) and stopped predicting comprehension.
  - The authors foresaw that for readers "of scrollable text on small screens ... rereading is often impossible" (General Discussion).
- *Use here:* move 2. Look-backs need the text to stay available.

**Timkey, W., Huang, K.-J., Oh, B.-D., Prasad, G., Arehalli, S., Linzen, T., & Dillon, B. (2026).** Eye movements reveal a dissociation between prediction and structural processing difficulty in language comprehension. *Proceedings of the National Academy of Sciences, 123*(32), e2532230123. https://doi.org/10.1073/pnas.2532230123. **[A + preprint in part]**
- *What it shows:* across 368 readers of difficult sentences, language-model surprisal explained early effects but not a rereading cost at disambiguation. Surprisal does not capture "the cost of detecting or correcting errors in the structure-building process."
- *Use here:* move 4. Rereading is where repair happens.
- *Limits:* garden-path syntax; extending it to auditing LLM output is your inference, not theirs.

**Metzner, P., von der Malsburg, T., Vasishth, S., & Rösler, F. (2017).** The importance of reading naturally: Evidence from combined recordings of eye movements and electric brain potentials. *Cognitive Science, 41*(S6), 1232–1263. https://doi.org/10.1111/cogs.12384. **[A]**
- *What it shows:* free reading beat word-by-word presentation only on trials where readers regressed to the anomaly.
- *Use here:* move 3, a converging result.

**Benedetto, S., Carbone, A., Pedrotti, M., Le Fevre, K., Bey, L. A. Y., & Baccino, T. (2015).** Rapid serial visual presentation in reading: The case of Spritz. *Computers in Human Behavior, 45*, 352–358. https://doi.org/10.1016/j.chb.2014.12.043. **[A]**
- *What it shows:* RSVP (rapid serial visual presentation, one word at a time), which suppresses regressions and preview, hurt literal comprehension.
- *Use here:* move 3. Streams share RSVP's forward-only pacing.

**Harvey, H., Godwin, H. J., Fitzsimmons, G., Liversedge, S. P., & Walker, R. (2017).** Oculomotor and linguistic processing effects in reading dynamic horizontally scrolling text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(3), 518–536. https://doi.org/10.1037/xhp0000329. **[A]**
- *What it shows:* word-level effects survived scrolling; the sentence-level predictability benefit was lost.
- *Use here:* move 5. Moving text spares word recognition and costs integration.

**Harvey, H., & Walker, R. (2018).** Reading comprehension and its relationship with working memory capacity when reading horizontally scrolling text. *Quarterly Journal of Experimental Psychology, 71*(9), 1887–1897. https://doi.org/10.1080/17470218.2017.1363258. **[A]**
- *What it shows:* literal comprehension held under scrolling; inference suffered; returning to earlier text was harder.
- *Use here:* move 5.

**Haverkamp, Y. E., Bråten, I., Latini, N., & Salmerón, L. (2023).** Is it the size, the movement, or both? Investigating effects of screen size and text movement on processing, understanding, and motivation when students read informational text. *Reading and Writing, 36*(7), 1589–1608. https://doi.org/10.1007/s11145-022-10328-9. **[F]**
- *What it is:* N = 145, 2 × 2 design (screen size × scrolling vs paging), reader-controlled, with a PDF.
- *What it shows:* scrollers backtracked less often (2.49 vs 3.53, p = .012) but farther. The integrated-understanding advantage for paging was only a trend (p = .066).
- *Use here:* move 5, describing it as *reader-controlled* scrolling.
- *Limits:* no auto-scroll (F9).

**Sharmin, S., Špakov, O., & Räihä, K.-J. (2015).** Dynamic text presentation in print interpreting – An eye movement study of reading behaviour. *International Journal of Human-Computer Studies, 78*, 17–30. https://doi.org/10.1016/j.ijhcs.2015.01.010. **[A]**
- *What it shows:* text that emerges word by word produced more rereading and regressions than text that emerges letter by letter (N = 20).
- *Use here:* move 5. Text still forming changes rereading; this is the closest precedent to token streaming.

**Sharmin, S., et al. (2016).** The reading process of dynamic text – A linguistic approach to an eye movement study. *SKY Journal of Linguistics, 29*. **[A; co-authors and pages unverified]**
- *What it shows:* 90.8% of regression landings fell on content words, against a 57.1% base rate.
- *Use here:* optional; regressions in emerging text target meaning-bearing words.
- *Limits:* the citation is incomplete. Verify it or drop it.

**Mangen, A., Olivier, G., & Velay, J.-L. (2019).** *Use here:* move 6 and §3.5. Full annotation in §3.5.

#### §3.2 Being pulled forward

**Yantis, S., & Jonides, J. (1984).** Abrupt visual onsets and selective attention: Evidence from visual search. *Journal of Experimental Psychology: Human Perception and Performance, 10*(5), 601–621. https://doi.org/10.1037/0096-1523.10.5.601. **[F: introduction, Exp. 1, General Discussion]**
- *What it shows:*
  - In visual search, an abrupt-onset item is identified first (N = 18 in Exp. 1).
  - Onset alone is not sufficient: capture occurs "only when the visual field contains but one such event" (p. 617).
- *Use here:* move 1, with the limit stated. Word-by-word streaming fits it; chunked streaming fits it less well.

**Wolfe, J. M. (2021).** Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review, 28*(4), 1060–1092. https://doi.org/10.3758/s13423-020-01859-9. **[F pp. 1060–1071]**
- *What it is:* the current Guided Search model. Five sources of guidance feed a priority map, and attention is deployed to its peak about 20 times per second.
- *What it shows:*
  - Bottom-up salience is "a very powerful but short-lived form of guidance."
  - "Attention capture" may be a misnomer for a bump in the priority map.
  - "If there is enough of a break in the action, the map may get reset." Wolfe asks whether event boundaries reset it (p. 1069).
- *Use here:* move 2. This is the strongest single anchor for why a pause might help.
- *Limits:* a model of visual search, not of reading; the reset idea is Wolfe's suggestion, not a finding.

**Park & Lee (2024).** See §1. *Use here:* move 3. Fixation starts clustered where new text appeared.

**Liu et al. (2024, Andes)** and **Xiao & Yang (2025).** See §1. *Use here:* move 4.

**Zhu, H., Wang, J., Xie, L., Ma, R., Sun, Y., Liu, F., Zheng, C., & Li, Q. (2026).** Just-in-time tokens: Adaptive token pacing for cognitive-friendly LLM streaming. In *Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–8). ACM. https://doi.org/10.1145/3772363.3798936. **[M]**
- *Use here:* move 4, as evidence that HCI researchers have started adapting the *rate* of streaming. Decision spaces change its *structure*.
- *Limits:* unread; metadata and a search snippet only. Read it before relying on it.

#### §3.3 Segmenting into events

**Zacks, J. M., Speer, N. K., Swallow, K. M., Braver, T. S., & Reynolds, J. R. (2007).** Event perception: A mind-brain perspective. *Psychological Bulletin, 133*(2), 273–293. https://doi.org/10.1037/0033-2909.133.2.273. **[M]**
- *What it is:* the founding statement of Event Segmentation Theory.
- *Use here:* move 1, as the theory citation.
- *Limits:* unread this session. Paraphrase the theory from Zacks et al. (2009) and Kurby & Zacks (2008), which state it, rather than characterising this paper in detail.

**Kurby, C. A., & Zacks, J. M. (2008).** Segmentation in the perception and memory of events. *Trends in Cognitive Sciences, 12*(2), 72–79. https://doi.org/10.1016/j.tics.2007.11.004. **[A]**
- *Use here:* move 1, a short review of segmentation and memory.

**Zacks, J. M., Speer, N. K., & Reynolds, J. R. (2009).** Segmentation in reading and film comprehension. *Journal of Experimental Psychology: General, 138*(2), 307–327. https://doi.org/10.1037/a0015305. **[F]**
- *What it shows:*
  - Situation changes predict event boundaries in text.
  - Each additional situation change added 92.8 ms of reading time (Exp. 3).
  - Each 10% rise in the probability that a clause is a boundary slowed reading by about 108 ms.
  - Boundaries aligned above chance even in a *visual-sequential* condition: one clause at a time, software-paced at about 3.35 words/s, earlier clauses not reviewable (Exp. 1).
- *Use here:* move 2. The visual-sequential condition is the closest precedent to a stream, and segmentation survived it.

**Kurby, C. A., & Zacks, J. M. (2012).** Starting from scratch and building brick by brick in comprehension. *Memory & Cognition, 40*(5), 812–826. https://doi.org/10.3758/s13421-011-0179-8. **[F results]**
- *What it shows:* think-aloud reading showed both global and incremental updating. Goals were mentioned more at fine boundaries even when the goal had not changed (OR = 2.29, z(926) = 2.87).
- *Use here:* move 3. Boundaries trigger updating; this grounds decision-space function 2.

**Kumar, M., Goldstein, A., Michelmann, S., Zacks, J. M., Hasson, U., & Norman, K. A. (2023).** Bayesian surprise predicts human event segmentation in story listening. *Cognitive Science, 47*(10), e13343. https://doi.org/10.1111/cogs.13343. **[A]**
- *What it shows:* Bayesian surprise derived from GPT-2 tracks where humans place event boundaries.
- *Use here:* move 4. Decision units could be computed from the response itself, which feeds the placement rule in §4.2.

**Tsoukala, A., Vogelzang, M., & Tsimpli, I. M. (2025).** The influence of text segmentation on garden path processing: Evidence from self-paced reading and eye-tracking. *Language and Cognition, 17*, e58. https://doi.org/10.1017/langcog.2025.10009. **[F]**
- *What it is:* self-paced reading (N = 39) and eye tracking (N = 29); five-line texts whose line breaks aligned with or cut across clauses. In the eye-tracking study, lines appeared one at a time.
- *What it shows:*
  - Misaligned breaks raised first-pass time (d = 0.32) and total time (d = 0.41) on the disambiguating region.
  - Accuracy fell in one misaligned condition (OR = 0.38).
  - Repeated misaligned breaks retrained readers' expectations.
  - The interaction did not survive FDR correction, and power was 52%.
- *Use here:* move 5. Placement, not number, is the variable. The line-by-line display resembles a stream.

**Bailey, B. P., & Konstan, J. A. (2006).** On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state. *Computers in Human Behavior, 22*(4), 685–708. https://doi.org/10.1016/j.chb.2005.12.009. **[A]**
- *What it shows:* interruptions during a task, rather than between tasks, cost more time and doubled errors.
- *Use here:* move 5. Mistimed breaks hurt; grounds P3.

**Powers, S. A., & Scerbo, M. W. (2023).** Examining the effect of interruptions at different breakpoints and frequencies within a task. *Human Factors, 65*(1), 22–36. https://doi.org/10.1177/00187208211009010. **[A]**
- *What it shows:* interruptions at coarse breakpoints cost about as little as no interruption; fine breakpoints were costly.
- *Use here:* move 5.
- *Limits:* abstract only.

**Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026).** *Comparing human oversight strategies for computer-use agents* [Preprint]. arXiv:2604.04918. **[F][P]**
- *What it is:* within-subjects, N = 48, 192 live sessions of agents performing tasks, each containing one embedded problematic action.
- *What it shows:*
  - Users blocked 29 of 138 problematic actions that reached execution.
  - 61 of 109 failures (56%) involved a timing mismatch, where risk emerged before or without a decision point.
  - The authors: oversight depends on "aligning authority, timing, and attention with decision-critical moments."
- *Use here:* closing move. Agent activity is continuous, and judgment has to land at the right moment.
- *Limits:* preprint; no eye tracking.

#### §3.4 Supervising fluent automation

**Parasuraman & Manzey (2010).** See §1. *Use here:* move 1, as the main citation.

**Lee, J. D., & See, K. A. (2004).** Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392. **[A]**
- *Use here:* move 1, the canonical definition of appropriate reliance. It is also the source of "boundary conditions", which Lamb et al. (2026) use (§7).

**Gegoff et al. (2025).** See §1. *Use here:* move 2. Recommendations lower scrutiny.

**Tatasciore, M., Bennett, L., Bowden, V. K., Bell, J., Visser, T. A. W., McAnally, K., McCarley, J. S., Thompson, M. B., Shanahan, C., Morris, R., & Loft, S. (2026).** Adaptable automation transparency: Should humans be provided flexibility to self-select transparency information? *Human Factors, 68*(1), 5–27. https://doi.org/10.1177/00187208251349269. **[F]**
- *What it shows:* across six studies in their lab (the authors' aggregated analysis), high transparency raised hit rate and sensitivity but also raised bias toward agreeing with automated advice, with no gain in correct rejections (p. 21).
- *Use here:* move 2. Transparency is not a cure for agreement bias. Full annotation in §6.

**Kim et al. (2025).** See §1. *Use here:* move 2.

**Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X., Mayer, L. W., & Smyth, P. (2025).** What large language models know and what people think they know. *Nature Machine Intelligence, 7*(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7. **[A]**
- *What it shows:* users overestimated LLM accuracy with default explanations, and longer explanations raised confidence without raising accuracy.
- *Use here:* move 2.

**Zhu, X., Le Truong, K., Fogliato, R., Swamy, G., Zhang, W., Yang, M., Ye, L., Liu, B., Liu, M., Ilyas, A., & Wu, Z. S. (2026).** *Justified or just convincing? Error verifiability as a dimension of LLM quality* [Preprint]. arXiv:2604.04418. **[F §1–7.1][P]**
- *What it shows:*
  - Post-training and scaling raised accuracy without making errors easier to verify.
  - Rephrasing without new information did not help; adding external information did.
  - One cell: Tulu3.1-8B's false-positive score on GSM8K fell from 0.717 to 0.602 after preference optimization (§7.1).
- *Use here:* move 2. Fluency can make wrong answers *more* convincing, so restyling the output will not fix detection.
- *Limits:* preprint; most raters were LLMs.

**Bhat (2025).** See §1. *Use here:* move 3.

**Liu, C., Zhou, Q., Shen, X., Liu, X. B., Wu, T., & Chen, X. A. (2026).** Behavioral indicators of overreliance during interaction with conversational language models. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–23). ACM. https://doi.org/10.1145/3772318.3790332. **[F]**
- *What it is:* N = 77; a GPT-4 chat platform with injected misinformation; three tasks; mouse and keyboard logs, clustered.
- *What it shows:* high overreliance went with whole-text copy-paste, coarse navigation and accepting despite hesitation; low overreliance with careful early reading and fine-grained locating (Table 3).
- *Use here:* move 4. Process signatures of overreliance exist.
- *Limits:* no eye tracking.

**Cho, J., & Lim, D. (2026).** How source attribution visualization shapes user attention and preference: An eye-tracking study of four AI chatbot layouts. *Journal of Eye Movement Research, 19*(4), Article 89. https://doi.org/10.3390/jemr19040089. **[F]**
- *What it is:* within-subjects, N = 23, four source layouts on static answer screens shown for 60 s, Tobii at 60 Hz.
- *What it shows:*
  - Time to first fixate sources ranged from 0.96 s (card list) to 15.65 s (raw hyperlinks).
  - No self-report measure differed, and gaze did not predict trust. In the authors' words, "Attention moved without moving judgment" (§3.4).
- *Use here:* move 4. Gaze and judgment come apart; this supports P4.
- *Limits:* static screens, not streams.

**Yang, Y., Lee, Y. M., Tabone, W., García de Pedro, J., Happee, R., & Merat, N. (2026/2027).** The effect of augmented reality on pedestrians' gaze patterns and crossing probability while interacting with automated vehicles. *International Journal of Human-Computer Studies, 217*, Article 103920. https://doi.org/10.1016/j.ijhcs.2026.103920. **[F]**
- *What it is:* a secondary analysis of a CAVE pedestrian-simulator study; 30 recruited, 27 analysed.
- *What it shows:*
  - AR cues cut fixation time on the vehicle plus the AR cue (head-up display M = −283 ms and crossing-path cue M = −282 ms, d = −0.80 each).
  - Pedestrians crossed earlier with AR.
  - The authors warn the pattern "may also indicate overreliance" and call evaluating visual load without safety outcomes a limitation (§5).
- *Use here:* move 4. Less looking can mean more trust, not easier perception.

**Wu, Z., Wang, Y., Langer, M., & Feit, A. M. (2025).** RelEYEance: Gaze-based assessment of users' AI-reliance at run-time. *Proceedings of the ACM on Human-Computer Interaction, 9*(3), 1–18. https://doi.org/10.1145/3725841. **[A]**
- *What it shows:* gaze patterns distinguished over-, under- and appropriate reliance.
- *Use here:* move 4. Gaze carries reliance signal, but only alongside outcomes.

**Cao, S., & Huang, C.-M. (2022).** Understanding user reliance on AI in assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 6*(CSCW2), 1–23. https://doi.org/10.1145/3555572. **[A]**
- *What it shows:* the share of gaze on an AI suggestion correlated with agreeing with it.
- *Use here:* move 4.

**Resulbegoviq, H., Hlebec, V., Pejić Bach, M., & Stamatović, I. (2026).** Eye tracking and AI-generated content: A systematic literature review of visual attention, cognitive processing, and user engagement. *Journal of Eye Movement Research, 19*(5), Article 97. https://doi.org/10.3390/jemr19050097. **[F in part]**
- *What it shows:* 23 studies; "no modality-independent gaze pattern emerged." Longer viewing more often reflected difficulty or checking than preference.
- *Use here:* move 4, the current synthesis.
- *Limits:* its eligibility rule required a human or no-AI comparator, so its silence on streaming is weak evidence of a gap.

#### §3.5 Perception as action

**Gibson, J. J. (1979).** *The ecological approach to visual perception*. Houghton Mifflin. **[M, deferred]**
- *Use here:* affordances, and perception for action.
- *Limits:* unread (F11). Keep the claims general.

**O'Regan, J. K., & Noë, A. (2001).** A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973. https://doi.org/10.1017/S0140525X01000115. **[A, deferred]**
- *Use here:* seeing as the mastery of sensorimotor contingencies.
- *Limits:* abstract only (F11).

**O'Regan, J. K. (2011).** *Why red doesn't sound like a bell: Understanding the feel of consciousness*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199775224.001.0001. **[M, deferred]**
- *Use here:* optional, as the book-length statement of the 2001 account.

**Mangen, A., Olivier, G., & Velay, J.-L. (2019).** Comparing comprehension of a long text read in print book and on Kindle: Where in the text and when in the story? *Frontiers in Psychology, 10*, Article 38. https://doi.org/10.3389/fpsyg.2019.00038. **[F]**
- *What it is:* N = 50, a 28-page story read on a Kindle or in print.
- *What it shows:* most measures did not differ, but print readers reconstructed the plot's chronology better (t(48) = 2.03, η² = .08). The authors tie this to "material placeholders", drawing on Gibson and on O'Regan and Noë.
- *Use here:* the empirical bridge from sensorimotor theory to reading media.
- *Limits:* it compares page-turning devices; the authors deliberately did not test scrolling.

**Mangen, A., Walgermo, B. R., & Brønnick, K. (2013).** Reading linear texts on paper versus computer screen: Effects on reading comprehension. *International Journal of Educational Research, 58*, 61–68. https://doi.org/10.1016/j.ijer.2012.12.002. **[A]**
- *Use here:* optional; an earlier screen-versus-paper comprehension difference.

**Delgado, P., Vargas, C., Ackerman, R., & Salmerón, L. (2018).** Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. *Educational Research Review, 25*, 23–38. https://doi.org/10.1016/j.edurev.2018.09.003. **[A, known via Mangen et al. 2019]**
- *Use here:* optional; the paper advantage was stronger under time constraint, which is what streaming imposes.

---

## 4. DECISION SPACES (about 1,700 words)

**Job:** define the construct precisely, tie each function to its mechanism, and set it apart from its nearest neighbours.

### Moves
1. **The theory.** **ROGER:** "I theorize that observing AI in operation today is analogous to reading scriptura continua... interacting with AI now combines users' literacy with their developing algorithmacy."
2. **Definition.** **ROGER:** your decision-spaces sentence.
   - **[NEEDS: the operational rule for locating a decision unit. In a theory paper, this rule is the contribution.]**
   - Candidates, which can be combined:
     - (a) the end of a checkable claim;
     - (b) a change of goal, cause or entity (Zacks et al., 2009);
     - (c) a peak in model surprisal (Kumar et al., 2023);
     - (d) a point where the user could accept, reject or redirect (Chen et al., 2026).
3. **Three functions, each mapped to a mechanism.** **ROGER:** "1) providing a visual target; 2) establishing event boundaries; and 3) facilitating efficient regression."
   - Function 1 maps to §3.2 and Rayner et al. (1998);
   - function 2 to §3.3;
   - function 3 to §3.1.
   - Wolfe's "break in the action" connects functions 1 and 2.
4. **What a decision space is not.**
   - Not a delay alone. Cognitive forcing functions such as a 30-second wait reduce overreliance without any segmentation.
   - Not a microboundary. Microboundaries sit *before* a user action and work through time cost; decision spaces sit *inside* the system's output and work through perception.
   - Not friction around model access, such as selective frictions or preparatory tasks.
   - Not friction inside the model, such as concept suppression.
5. **What a decision space asks of the user: nothing.**
   - This may avoid the "reflection penalty" that greets AI agents asking users to do reflective work.
   - Present this as a conjecture, and connect it to Forshaw et al.'s finding that stated dislike and observed behaviour diverged.

### Section bibliography

**Rayner et al. (1998), Zacks et al. (2009), Kurby & Zacks (2012), Kumar et al. (2023), Schotter et al. (2014), Booth & Weger (2013), Wolfe (2021), Chen et al. (2026).** See §§2–3. *Use here:* moves 2 and 3, as the mechanism behind each function.

**Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021).** To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287. **[F §1–4]**
- *What it is:* N = 199 on MTurk; six conditions, including three cognitive forcing functions: on-demand, update, and a 30-second wait.
- *What it shows:*
  - When the AI was wrong, the forcing functions cut overreliance (0.48 vs 0.64, d = .36).
  - Participants trusted and preferred the forcing-function designs less.
- *Use here:* move 4. A pause alone can work, which is why P2 has to beat equally many arbitrary breaks.

**Ghosh, A., Sarkar, A., Lindley, S., & Poelitz, C. (2026).** *An experimental comparison of cognitive forcing functions for execution plans in AI-assisted writing: Effects on trust, overreliance, and perceived critical thinking* [Preprint]. arXiv:2601.18033. **[A][P]**
- *What it shows:* with n = 214, an "Assumptions" forcing function reduced overreliance most, without raising load.
- *Use here:* move 4, a recent LLM forcing function.

**Cox, A. L., Gould, S. J. J., Cecchinato, M. E., Iacovides, I., & Renfree, I. (2016).** Design frictions for mindful interactions: The case for microboundaries. In *Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems* (pp. 1389–1397). ACM. https://doi.org/10.1145/2851581.2892410. **[F]**
- *What it is:* a position paper with no new data.
- *What it shows:*
  - Defines a microboundary as "a small obstacle prior to an interaction," implemented through a short time cost that shifts behaviour from automatic to deliberate.
  - Cites evidence on lockouts and on a less legible font that raised transcription accuracy.
  - Lists user autonomy over microboundaries as future work.
- *Use here:* move 4. It is the nearest design precedent, and the contrast sharpens decision spaces.

**Collins, K. M., et al. (2024).** *Modulating language model experiences through frictions* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2407.12804. **[A][P]**
- *What it shows:* "selective frictions", such as a button impeding model access, reduced click-through with little effect on accuracy, but spilled over to topics without friction.
- *Use here:* move 4. Friction placed *before* access.
- *Limits:* complete the author list from the record before citing.

**Arun, S., et al. (2026).** Encouraging thought before completion: The role of task-specific selective friction in AI-assisted knowledge work. In *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work*. ACM. https://doi.org/10.1145/3808045.3808049. **[A]**
- *What it shows:* N = 40. Preparatory friction raised mental demand and trust, but did not reduce self-reported reliance or increase critical evaluation.
- *Use here:* move 4. Friction *before* access does not reliably raise scrutiny.
- *Limits:* complete the author list and pages.

**Disley, M., & Khan, M. (2026).** Designing cognitive friction with concept suppression in large language models. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2708617. **[F]**
- *What it is:* N = 37, within-subjects ideation in three conditions: unaided, unmodified Llama3.2:3b, and Llama3.2:3b with the concept "chair" suppressed.
- *What it shows:*
  - The unmodified model lowered mental demand and effort, and also lowered ownership (6.38 vs 9.16 suppressed vs 11.49 unaided; ηp² = .251).
  - The authors contrast their model-level friction with interface-level friction, "an added step, a delay" (§2.3), and call for comparisons with interface-level designs (§7.9).
- *Use here:* move 4. Friction inside the model; decision spaces answer their call for interface-level work.
- *Limits:* the task was creative ideation, not verification.

**Forshaw, T., Hale, J., & Longmire, M. (2026).** The Reflection Penalty: When managers accept leadership coaching from a human but not an AI agent. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2744236. **[F]**
- *What it is:* the fourth cycle of a design-based research programme; eight managers each had human and AI coaching built on the same protocol.
- *What it shows:*
  - All eight preferred the human coach and resisted the AI's probing questions (the "Reflection Penalty").
  - The coached behaviours nonetheless appeared after both formats (§6.1).
- *Use here:* move 5. Asking users to reflect has a cost, and stated cost and behavioural effect can diverge.
- *Limits:* N = 8; order unbalanced; the two formats differed in medium (video vs text).

---

## 5. PROPOSITIONS (about 1,300 words)

**Job:** make the theory falsifiable. Each proposition comes from your RQs and names the result that would count against it. The study appears only as the test logic. **[NEEDS: accept or rewrite P1–P4.]**

### Moves
- **P1 Targeting and regression** (from RQ1). Breaks at decision units draw fixations and regressions to those points more than the same number of breaks at arbitrary intervals.
  - *Against it:* no difference in regressions to break locations.
  - Sources: Rayner et al. (1998); Booth & Weger (2013); Tsoukala et al. (2025).
- **P2 Detection** (from RQ2). Breaks at decision units improve detection of embedded errors over both a continuous stream and arbitrarily broken streams.
  - *Against it:* detection equal to arbitrary breaks. Then pausing, not segmentation, does the work.
  - **ROGER:** "If arbitrary breaks yield similar improvements, the benefit may be attributed to something rather than segmentation" [probably "other than"].
  - Sources: Buçinca et al. (2021); Zacks et al. (2009); Kurby & Zacks (2012).
- **P3 Cost of misplaced breaks** (from RQ3). Arbitrary breaks cost detection latency, workload or local refixations relative to a continuous stream.
  - *Against it:* arbitrary breaks are cost-free or beneficial.
  - Sources: Bailey & Konstan (2006); Powers & Scerbo (2023); Tsoukala et al. (2025); Gould et al. (2016) on duration.
- **P4 Gaze is not verification** (new). Changes in gaze without changes in detection would show attention moving without judgment.
  - *Consequence:* any test must pair gaze with detection outcomes.
  - Sources: Parasuraman & Manzey (2010); Cho & Lim (2026); Yang et al. (2026); Resulbegoviq et al. (2026).
- **5.5 The test that separates them**, in one paragraph:
  - three conditions, with equal break counts in the two broken conditions;
  - embedded errors;
  - gaze plus detection plus workload;
  - pre-generated responses replayed at a fixed rate.
  - **ROGER:** your experimental-design sentence. State that the study is future work, not reported here.

### Section bibliography

All sources above are annotated in §§1–4, except one:

**Gould, S. J. J., Cox, A. L., Brumby, D. P., & Wickersham, A. (2016).** Now check your input: Brief task lockouts encourage checking, longer lockouts encourage task switching. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 3311–3323). ACM. https://doi.org/10.1145/2858036.2858067. **[A]**
- *What it shows:*
  - In the lab, lockouts before confirming data entry encouraged checking, and longer lockouts made checking more likely.
  - In a crowdsourced study, longer lockouts induced switching to other activities.
  - Duration "needs to be carefully calibrated."
- *Use here:* P3. Pause length can tip a break from helpful to costly.
- *Limits:* abstract only. An open-access copy exists in the University of Birmingham repository and is worth reading.

---

## 6. A DESIGN SPACE FOR DECISION SPACES (about 1,300 words)

**Job:** give *HCI* its design implications. There are four dimensions; each is stated as a trade-off with its evidence and ends in a design principle.

### Moves
1. **Placement rule.** Decision unit, time or length.
   - Evidence: Tsoukala et al. (2025); Powers & Scerbo (2023); Chen et al. (2026).
   - *Principle:* place by meaning, never by packet.
2. **Marker form.** Blank space, rule, label or prompt. A terse cue that signals without resolving raises visual search.
   - Evidence: Prajod et al. (2026). Content signals such as headings steer look-backs: Hyönä & Lorch (2004); Lorch (1989).
   - **[NEEDS: your view on the marker.]**
3. **Pause length and pacing.**
   - Brief lockouts encourage checking; long ones invite switching (Gould et al., 2016).
   - Comfortable streaming speed (Xiao & Yang, 2025).
   - Rate adaptation (Zhu et al., 2026, CHI EA).
   - *Principle:* calibrate duration, and keep the stream paused only as long as inspection plausibly lasts.
4. **Who triggers it.** System or user.
   - User-chosen transparency did not improve automation use, and operators chose the higher level on about 41% of missions (Tatasciore et al., 2026).
   - Cox et al. (2016) list user autonomy as an open question.
   - *Principle:* the system places decision spaces; users may extend them.
5. **Extension to agents.** Computer-use agents need judgment placed at decision-critical moments (Chen et al., 2026). Optional: once a pause has prompted a correction, segment-level editing of reasoning is one way to act on it (Zhou et al., 2026).

### Section bibliography

**Tsoukala et al. (2025), Powers & Scerbo (2023), Chen et al. (2026), Xiao & Yang (2025), Gould et al. (2016), Cox et al. (2016).** See §§1–5.

**Tatasciore, M., et al. (2026).** Full reference in §3.4. **[F]**
- *What it is:* two experiments (N = 73 and N = 88) on a UV task, comparing fixed low, fixed high and adaptable transparency.
- *What it shows:*
  - Participants chose high transparency on 39% and 43% of adaptable trials (about 41% overall).
  - Adaptable transparency did not improve accuracy of automation use in either experiment (p. 22).
  - The authors call for eye tracking to study strategy (p. 15).
- *Use here:* move 4. Leaving the boundary to the user does not help, so the system should place it.

**Prajod, P., Cools, H., Röggla, T., Cesar, P., & El Ali, A. (2026).** *Towards gaze-informed AI disclosure interfaces: Eye-tracking attentional and cognitive load while reading AI-assisted news* [Preprint]. arXiv:2605.14999. **[F §1–4.2][P]**
- *What it shows:* with 30 eye-tracked readers of static news articles, a one-line AI-use label drew more total fixation (58.70 vs 49.46, d = 0.34) and more saccades than a detailed label. NASA-TLX and pupil size did not differ.
- *Use here:* move 2. A terse marker may prompt search.
- *Limits:* static text; labels about AI use, not decision boundaries.

**Hyönä, J., & Lorch, R. F. (2004).** Effects of topic headings on text processing: Evidence from adult readers' eye fixation patterns. *Learning and Instruction, 14*(2), 131–152. https://doi.org/10.1016/j.learninstruc.2004.01.001. **[A]**
- *What it shows:* headings sped first-pass reading and steered look-backs.
- *Use here:* move 2. Structural signals guide regressions.

**Lorch, R. F. (1989).** Text-signaling devices and their effects on reading and memory processes. *Educational Psychology Review, 1*(3), 209–234. https://doi.org/10.1007/BF01320135. **[A]**
- *Use here:* move 2, a review of signals such as headings and previews.

**Koornneef, A. (2024).** On the readability of texts presented in sentence-by-sentence segments to beginner readers: Evidence from self-paced reading and eye tracking. *Reading and Writing, 37*(1), 69–87. https://doi.org/10.1007/s11145-023-10423-5. **[A]**
- *What it shows:* presenting text in sentence segments raised comprehension, and wrap-up time did not explain the gain.
- *Use here:* move 1. Segmentation can help readers.

**Zhu, H., et al. (2026).** Just-in-time tokens. See §3.2. **[M]** *Use here:* move 3.

**Zhou, H., Zhang, J., Lou, J., Liu, Y., Lu, C., Qu, J., & Li, J. (2026).** *Deep interaction: An efficient human-AI interaction method for large reasoning models* [Preprint]. arXiv:2607.14049. **[F method/evaluation][P]**
- *What it shows:* letting users edit a *completed* chain of thought improved correction success by more than 25% and cut tokens about 40%, mainly with simulated correctors.
- *Use here:* move 5, optional, as an example of what users can do once a pause prompts them to correct.
- *Limits:* not streaming; the correctors were mostly simulated.

**Kazemitabaar, M., et al. (2024).** Improving steering and verification in AI-assisted data analysis with interactive task decomposition. In *Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology*. ACM. https://doi.org/10.1145/3654777.3676345. **[A]**
- *What it shows:* stepwise and phasewise decomposition (n = 18) made intervention, correction and verification easier than a conversational baseline.
- *Use here:* move 1. Structuring the output into units helps users steer and verify; this is the nearest interaction-level precedent.
- *Limits:* complete the author list; this is task decomposition, not stream segmentation.

---

## 7. ALGORITHMACY (about 1,100 words)

**Job:** state the theoretical consequence beyond interface design.

### Moves
1. **ROGER:** literacy once merged with oracy; literacy now merges with algorithmacy. Include "Users must interpret text while navigating both the opacity of AI systems and the influence of other users, particularly in organizational contexts."
2. Algorithmic literacy describes knowledge and awareness; algorithmacy adds a real-time perceptual skill. Quote Ridley and Pawlick-Potts's five bullets; do not paraphrase them.
3. Trust is learned at a system's edges. Expert analysts watching live video with an AI overlay said they needed to learn its "boundary conditions," and seven of nine stopped seeing it as an advisor. A decision space is a designed place to meet those edges.
4. **[NEEDS: your dissertation material on organizational and cooptive environments.]**

### Section bibliography

**Ridley, M., & Pawlick-Potts, D. (2021).** Algorithmic literacy and the role for libraries. *Information Technology and Libraries, 40*(2). https://doi.org/10.6017/ital.v40i2.12963. **[F pp. 1–4]**
- *What it is:* a definitional paper.
- *What it shows:* algorithmic literacy is "the skill, expertise, and awareness" to understand algorithms, recognise their use, create and apply them, assess their influence, and "position the individual as a co-constituent in algorithmic decision-making" (p. 3).
- *Use here:* move 2. The definition you extend.
- *Limits:* that it lacks a perceptual component is your reading, not the authors'.

**Lamb, S. C., Byrne, M., Norman, T. J., Ramchurn, S. D., & Naiseh, M. (2026).** What's informing trust and adoption? Can current cognitive models support expert adoption of AI? *Journal of Cognitive Engineering and Decision Making, 20*(2), 158–175. https://doi.org/10.1177/15553434261430550. **[F]**
- *What it is:* a longitudinal naturalistic study of defence intelligence analysts (12 before deployment, 9 after) adopting an object-detection overlay on live video.
- *What it shows:*
  - Seven of nine stopped seeing the tool as an "advisor" (McNemar p = .023).
  - Analysts wanted to learn its "boundary conditions"; trust "must be earned."
  - The authors argue for interdependence over task allocation.
- *Use here:* move 3. The nearest case of supervising a live AI-augmented visual stream.

**Lee & See (2004).** See §3.4. *Use here:* move 3, the origin of "boundary conditions".

**Najjar, M. S., & Nasir, M. (2026).** Dialogue patterns in human-AI co-creation: How interaction structure shapes output and process. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2717534. **[A]**
- *What it shows:* N = 244 in four interaction structures. Iterative critique gave higher task-appropriate creativity than AI-led proposals, and participants in that condition saw the AI as a tool and felt ownership.
- *Use here:* optional, in move 2 or §6. The structure of an exchange shapes what people do; algorithmacy includes reading that structure.
- *Limits:* abstract only.

---

## 8. LIMITS OF THE ARGUMENT (about 600 words)

**Job:** state each limit so that it changes the claim.

### Moves
1. **Where the analogy breaks.**
   - Medieval readers controlled their own pace; stream readers do not.
   - Word spaces were added once and for all; decision spaces must be computed for each response.
   - Knox (1968) shows that silent reading predates spacing, so the historical claim should be about *ease* of silent reading, not its invention. **[Unread; deferred.]**
2. **The evidence is indirect.**
   - Most of it concerns static, scrolled or experimenter-paced text.
   - Only Park & Lee (2024) and Bhat (2025) study chatbot streaming, and only Park & Lee measured gaze.
3. **Placement is hard.** If decision units cannot be located reliably, P1–P3 cannot be tested. This makes §4.2 the paper's weakest point and its most important one.
4. **Friction has users' dislike to contend with.** Forshaw et al. (2026); Buçinca et al. (2021); Arun et al. (2026).
5. **Interfaces change fast.** Token rates, layouts and agent designs will date; the mechanisms in §3 should not.

### Section bibliography
All sources are annotated above (Knox in §2; the rest in §§1, 3 and 4).

**Counter-evidence worth one sentence:**

**Keenan, S. A. (1984).** Effects of chunking and line length on reading efficiency. *Visible Language*. **[A; volume and pages unverified]**
- *What it shows:* chunked text was read more slowly, which the author attributed to variable line length.
- *Use here:* segmentation is not free.
- *Limits:* verify the citation or drop it.

---

## 9. CONCLUSION (about 300 words)

**Job:** end on the most specific design consequence: interfaces should break streams where meaning breaks. Write it in your register. No new citations.

---

## Master reference list (APA 7)

Status codes repeat those above. Entries marked † need completion or verification before submission.

- Arun, S., et al. (2026). Encouraging thought before completion: The role of task-specific selective friction in AI-assisted knowledge work. In *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work*. ACM. https://doi.org/10.1145/3808045.3808049 [A] †authors, pages
- Bailey, B. P., & Konstan, J. A. (2006). On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state. *Computers in Human Behavior, 22*(4), 685–708. https://doi.org/10.1016/j.chb.2005.12.009 [A]
- Benedetto, S., Carbone, A., Pedrotti, M., Le Fevre, K., Bey, L. A. Y., & Baccino, T. (2015). Rapid serial visual presentation in reading: The case of Spritz. *Computers in Human Behavior, 45*, 352–358. https://doi.org/10.1016/j.chb.2014.12.043 [A]
- Bhat, M. (2025). How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131 [F]
- Booth, R. W., & Weger, U. W. (2013). The function of regressions in reading: Backward eye movements allow rereading. *Memory & Cognition, 41*(1), 82–97. https://doi.org/10.3758/s13421-012-0244-y [F]
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287 [F]
- Cao, S., & Huang, C.-M. (2022). Understanding user reliance on AI in assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 6*(CSCW2), 1–23. https://doi.org/10.1145/3555572 [A]
- Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026). *Comparing human oversight strategies for computer-use agents* [Preprint]. arXiv. https://arxiv.org/abs/2604.04918 [F][P]
- Cho, J., & Lim, D. (2026). How source attribution visualization shapes user attention and preference: An eye-tracking study of four AI chatbot layouts. *Journal of Eye Movement Research, 19*(4), Article 89. https://doi.org/10.3390/jemr19040089 [F]
- Collins, K. M., et al. (2024). *Modulating language model experiences through frictions* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2407.12804 [A][P] †authors
- Cox, A. L., Gould, S. J. J., Cecchinato, M. E., Iacovides, I., & Renfree, I. (2016). Design frictions for mindful interactions: The case for microboundaries. In *Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems* (pp. 1389–1397). ACM. https://doi.org/10.1145/2851581.2892410 [F]
- Delgado, P., Vargas, C., Ackerman, R., & Salmerón, L. (2018). Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. *Educational Research Review, 25*, 23–38. https://doi.org/10.1016/j.edurev.2018.09.003 [A]
- Disley, M., & Khan, M. (2026). Designing cognitive friction with concept suppression in large language models. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2708617 [F]
- Drieghe, D., Fitzsimmons, G., & Liversedge, S. P. (2017). Parafoveal preview effects in reading unspaced text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(10), 1701–1716. https://doi.org/10.1037/xhp0000441 [A]
- Forshaw, T., Hale, J., & Longmire, M. (2026). The Reflection Penalty: When managers accept leadership coaching from a human but not an AI agent. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2744236 [F]
- Gegoff, I., Tatasciore, M., Bowden, V. K., & Loft, S. (2025). Deciphering automation transparency: Do the benefits of transparency differ based on whether decision recommendations are provided? *Human Factors, 67*(8), 776–794. https://doi.org/10.1177/00187208251318465 [F]
- Ghosh, A., Sarkar, A., Lindley, S., & Poelitz, C. (2026). *An experimental comparison of cognitive forcing functions for execution plans in AI-assisted writing: Effects on trust, overreliance, and perceived critical thinking* [Preprint]. arXiv. https://arxiv.org/abs/2601.18033 [A][P]
- Gibson, J. J. (1979). *The ecological approach to visual perception*. Houghton Mifflin. [M, deferred]
- Gould, S. J. J., Cox, A. L., Brumby, D. P., & Wickersham, A. (2016). Now check your input: Brief task lockouts encourage checking, longer lockouts encourage task switching. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 3311–3323). ACM. https://doi.org/10.1145/2858036.2858067 [A]
- Harvey, H., Godwin, H. J., Fitzsimmons, G., Liversedge, S. P., & Walker, R. (2017). Oculomotor and linguistic processing effects in reading dynamic horizontally scrolling text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(3), 518–536. https://doi.org/10.1037/xhp0000329 [A]
- Harvey, H., & Walker, R. (2018). Reading comprehension and its relationship with working memory capacity when reading horizontally scrolling text. *Quarterly Journal of Experimental Psychology, 71*(9), 1887–1897. https://doi.org/10.1080/17470218.2017.1363258 [A]
- Haverkamp, Y. E., Bråten, I., Latini, N., & Salmerón, L. (2023). Is it the size, the movement, or both? Investigating effects of screen size and text movement on processing, understanding, and motivation when students read informational text. *Reading and Writing, 36*(7), 1589–1608. https://doi.org/10.1007/s11145-022-10328-9 [F]
- Hyönä, J., & Lorch, R. F. (2004). Effects of topic headings on text processing: Evidence from adult readers' eye fixation patterns. *Learning and Instruction, 14*(2), 131–152. https://doi.org/10.1016/j.learninstruc.2004.01.001 [A]
- Kazemitabaar, M., et al. (2024). Improving steering and verification in AI-assisted data analysis with interactive task decomposition. In *Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology*. ACM. https://doi.org/10.1145/3654777.3676345 [A] †authors, pages
- Keenan, S. A. (1984). Effects of chunking and line length on reading efficiency. *Visible Language*. [A] †volume, pages
- Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025). Fostering appropriate reliance on large language models: The role of explanations, sources, and inconsistencies. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–19). ACM. https://doi.org/10.1145/3706598.3714020 [F]
- Knox, B. M. W. (1968). Silent reading in antiquity. *Greek, Roman and Byzantine Studies, 9*(4), 421–435. [M]
- Koornneef, A. (2024). On the readability of texts presented in sentence-by-sentence segments to beginner readers: Evidence from self-paced reading and eye tracking. *Reading and Writing, 37*(1), 69–87. https://doi.org/10.1007/s11145-023-10423-5 [A]
- Kumar, M., Goldstein, A., Michelmann, S., Zacks, J. M., Hasson, U., & Norman, K. A. (2023). Bayesian surprise predicts human event segmentation in story listening. *Cognitive Science, 47*(10), e13343. https://doi.org/10.1111/cogs.13343 [A]
- Kurby, C. A., & Zacks, J. M. (2008). Segmentation in the perception and memory of events. *Trends in Cognitive Sciences, 12*(2), 72–79. https://doi.org/10.1016/j.tics.2007.11.004 [A]
- Kurby, C. A., & Zacks, J. M. (2012). Starting from scratch and building brick by brick in comprehension. *Memory & Cognition, 40*(5), 812–826. https://doi.org/10.3758/s13421-011-0179-8 [F]
- Lamb, S. C., Byrne, M., Norman, T. J., Ramchurn, S. D., & Naiseh, M. (2026). What's informing trust and adoption? Can current cognitive models support expert adoption of AI? *Journal of Cognitive Engineering and Decision Making, 20*(2), 158–175. https://doi.org/10.1177/15553434261430550 [F]
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392 [A]
- Liu, C., Zhou, Q., Shen, X., Liu, X. B., Wu, T., & Chen, X. A. (2026). Behavioral indicators of overreliance during interaction with conversational language models. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–23). ACM. https://doi.org/10.1145/3772318.3790332 [F]
- Liu, J., Chung, J.-W., Wu, Z., Lai, F., Lee, M., & Chowdhury, M. (2024). *Andes: Defining and enhancing quality-of-experience in LLM-based text streaming services* [Preprint]. arXiv. https://arxiv.org/abs/2404.16283 [F][P]
- Lorch, R. F. (1989). Text-signaling devices and their effects on reading and memory processes. *Educational Psychology Review, 1*(3), 209–234. https://doi.org/10.1007/BF01320135 [A]
- Mangen, A., Olivier, G., & Velay, J.-L. (2019). Comparing comprehension of a long text read in print book and on Kindle: Where in the text and when in the story? *Frontiers in Psychology, 10*, Article 38. https://doi.org/10.3389/fpsyg.2019.00038 [F]
- Mangen, A., Walgermo, B. R., & Brønnick, K. (2013). Reading linear texts on paper versus computer screen: Effects on reading comprehension. *International Journal of Educational Research, 58*, 61–68. https://doi.org/10.1016/j.ijer.2012.12.002 [A]
- McDonald, S. A. (2006). Parafoveal preview benefit in reading is only obtained from the saccade goal. *Vision Research, 46*(26), 4416–4424. https://doi.org/10.1016/j.visres.2006.08.027 [M]
- Metzner, P., von der Malsburg, T., Vasishth, S., & Rösler, F. (2017). The importance of reading naturally: Evidence from combined recordings of eye movements and electric brain potentials. *Cognitive Science, 41*(S6), 1232–1263. https://doi.org/10.1111/cogs.12384 [A]
- Najjar, M. S., & Nasir, M. (2026). Dialogue patterns in human-AI co-creation: How interaction structure shapes output and process. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2717534 [A]
- O'Regan, J. K. (2011). *Why red doesn't sound like a bell: Understanding the feel of consciousness*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199775224.001.0001 [M, deferred]
- O'Regan, J. K., & Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973. https://doi.org/10.1017/S0140525X01000115 [A, deferred]
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055 [F]
- Park, H., & Lee, Y. (2024). The effect of text movement on eye movements in generative AI chatbots. *Archives of Design Research, 37*(4), 181–197. https://doi.org/10.15187/adr.2024.08.37.4.181 [F]
- Parkes, M. B. (1992). *Pause and effect: An introduction to the history of punctuation in the West*. Scolar Press. [M, deferred] †edition
- Powers, S. A., & Scerbo, M. W. (2023). Examining the effect of interruptions at different breakpoints and frequencies within a task. *Human Factors, 65*(1), 22–36. https://doi.org/10.1177/00187208211009010 [A]
- Prajod, P., Cools, H., Röggla, T., Cesar, P., & El Ali, A. (2026). *Towards gaze-informed AI disclosure interfaces: Eye-tracking attentional and cognitive load while reading AI-assisted news* [Preprint]. arXiv. https://arxiv.org/abs/2605.14999 [F][P]
- Rayner, K., Fischer, M. H., & Pollatsek, A. (1998). Unspaced text interferes with both word identification and eye movement control. *Vision Research, 38*(8), 1129–1144. https://doi.org/10.1016/S0042-6989(97)00274-5 [F]
- Resulbegoviq, H., Hlebec, V., Pejić Bach, M., & Stamatović, I. (2026). Eye tracking and AI-generated content: A systematic literature review of visual attention, cognitive processing, and user engagement. *Journal of Eye Movement Research, 19*(5), Article 97. https://doi.org/10.3390/jemr19050097 [F in part]
- Ridley, M., & Pawlick-Potts, D. (2021). Algorithmic literacy and the role for libraries. *Information Technology and Libraries, 40*(2). https://doi.org/10.6017/ital.v40i2.12963 [F]
- Saenger, P. (1997). *Space between words: The origins of silent reading*. Stanford University Press. https://doi.org/10.1515/9781503619081 [M, deferred]
- Schotter, E. R., Tran, R., & Rayner, K. (2014). Don't believe what you read (only once): Comprehension is supported by regressions during reading. *Psychological Science, 25*(6), 1218–1226. https://doi.org/10.1177/0956797614531148 [F]
- Sharmin, S., Špakov, O., & Räihä, K.-J. (2015). Dynamic text presentation in print interpreting – An eye movement study of reading behaviour. *International Journal of Human-Computer Studies, 78*, 17–30. https://doi.org/10.1016/j.ijhcs.2015.01.010 [A]
- Sharmin, S., et al. (2016). The reading process of dynamic text – A linguistic approach to an eye movement study. *SKY Journal of Linguistics, 29*. [A] †authors, pages
- Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X., Mayer, L. W., & Smyth, P. (2025). What large language models know and what people think they know. *Nature Machine Intelligence, 7*(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7 [A]
- Tatasciore, M., Bennett, L., Bowden, V. K., Bell, J., Visser, T. A. W., McAnally, K., McCarley, J. S., Thompson, M. B., Shanahan, C., Morris, R., & Loft, S. (2026). Adaptable automation transparency: Should humans be provided flexibility to self-select transparency information? *Human Factors, 68*(1), 5–27. https://doi.org/10.1177/00187208251349269 [F]
- Timkey, W., Huang, K.-J., Oh, B.-D., Prasad, G., Arehalli, S., Linzen, T., & Dillon, B. (2026). Eye movements reveal a dissociation between prediction and structural processing difficulty in language comprehension. *Proceedings of the National Academy of Sciences, 123*(32), e2532230123. https://doi.org/10.1073/pnas.2532230123 [A]
- Tsoukala, A., Vogelzang, M., & Tsimpli, I. M. (2025). The influence of text segmentation on garden path processing: Evidence from self-paced reading and eye-tracking. *Language and Cognition, 17*, e58. https://doi.org/10.1017/langcog.2025.10009 [F]
- Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review, 28*(4), 1060–1092. https://doi.org/10.3758/s13423-020-01859-9 [F]
- Wu, Z., Wang, Y., Langer, M., & Feit, A. M. (2025). RelEYEance: Gaze-based assessment of users' AI-reliance at run-time. *Proceedings of the ACM on Human-Computer Interaction, 9*(3), 1–18. https://doi.org/10.1145/3725841 [A]
- Xiao, C., & Yang, B. Z. (2025). Streaming, fast and slow: Cognitive load-aware streaming for efficient LLM serving. In *Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology* (pp. 1–13). ACM. https://doi.org/10.1145/3746059.3747721 [F]
- Yang, Y., Lee, Y. M., Tabone, W., García de Pedro, J., Happee, R., & Merat, N. (2027). The effect of augmented reality on pedestrians' gaze patterns and crossing probability while interacting with automated vehicles. *International Journal of Human-Computer Studies, 217*, Article 103920. https://doi.org/10.1016/j.ijhcs.2026.103920 [F] (online 2026)
- Yantis, S., & Jonides, J. (1984). Abrupt visual onsets and selective attention: Evidence from visual search. *Journal of Experimental Psychology: Human Perception and Performance, 10*(5), 601–621. https://doi.org/10.1037/0096-1523.10.5.601 [F]
- Zacks, J. M., Speer, N. K., & Reynolds, J. R. (2009). Segmentation in reading and film comprehension. *Journal of Experimental Psychology: General, 138*(2), 307–327. https://doi.org/10.1037/a0015305 [F]
- Zacks, J. M., Speer, N. K., Swallow, K. M., Braver, T. S., & Reynolds, J. R. (2007). Event perception: A mind-brain perspective. *Psychological Bulletin, 133*(2), 273–293. https://doi.org/10.1037/0033-2909.133.2.273 [M]
- Zhou, H., Zhang, J., Lou, J., Liu, Y., Lu, C., Qu, J., & Li, J. (2026). *Deep interaction: An efficient human-AI interaction method for large reasoning models* [Preprint]. arXiv. https://arxiv.org/abs/2607.14049 [F][P]
- Zhu, H., Wang, J., Xie, L., Ma, R., Sun, Y., Liu, F., Zheng, C., & Li, Q. (2026). Just-in-time tokens: Adaptive token pacing for cognitive-friendly LLM streaming. In *Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–8). ACM. https://doi.org/10.1145/3772363.3798936 [M]
- Zhu, X., Le Truong, K., Fogliato, R., Swamy, G., Zhang, W., Yang, M., Ye, L., Liu, B., Liu, M., Ilyas, A., & Wu, Z. S. (2026). *Justified or just convincing? Error verifiability as a dimension of LLM quality* [Preprint]. arXiv. https://arxiv.org/abs/2604.04418 [F][P]

**Count:** 69 entries.
- Read in full or in substantive sections: 32.
- Abstract only: 29.
- Metadata only: 8.
- Preprints: 7, which overlap the categories above.
- Entries marked † need completion before submission: 6.

---

## Decisions that remain yours
1. **The operational rule for a decision unit (§4.2).** Nothing else in the paper is as consequential.
2. Whether to adopt Parkes's "grammar of legibility" frame (§2).
3. Accept or rewrite P1–P4 (§5).
4. Marker form (§6).
5. Rewrite the abstract, the [Course] paragraph and the roadmap.
6. Resolve flags F1 and F3–F17 in `abstract_intro_edit.md`. F2 no longer applies.
7. Complete the † references (author lists for Collins, Arun and Kazemitabaar; Sharmin 2016; Keenan 1984; Parkes edition).
