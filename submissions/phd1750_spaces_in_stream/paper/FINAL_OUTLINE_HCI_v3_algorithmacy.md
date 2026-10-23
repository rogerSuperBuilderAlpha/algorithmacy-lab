# Spaces in the Stream: Algorithmacy and the Perception of Decision Spaces in Streaming AI Output

### Final outline for a theory article in *Human–Computer Interaction* (Taylor & Francis), version 3, reframed around algorithmacy theory

> **Drafted by Claude (Opus 5.5) for Roger Hunt, 20 October 2026.** This is a map of moves and the sources each one rests on, not prose; you write the sentences. **ROGER** marks text you have already written (`abstract_intro_edit.md`, your proposal, and your Substack posts). **[NEEDS]** marks a decision only you can make.
>
> Earlier versions:
> - version 1: `FINAL_OUTLINE_HCI_v1_pre-model.md`
> - version 2 (the "stream-legibility" account): `FINAL_OUTLINE_HCI_v2_stream-legibility.md`
>
> **The reframing in version 3, following your instruction of 20 October:**
> - **Decision spaces** are the opaque, co-opted points in an AI's process where a judgment is required but the process does not show it.
> - **Navigating them is algorithmacy.** As text creates meaning from marks, and literacy fills the gap between marks and meaning, the stream presents output, and algorithmacy fills the gap at its decision spaces.
> - **The interface intervention is marking.** Making a decision space perceptible is what the interface can do; marking it does not create it.
> - **This paper** is the perceptual layer of **algorithmacy theory**.
>
> **Resolved on 20 October at your instruction ("use your best judgement"):**
> 1. **Your three "implementing decision spaces" sentences** now say *marking*. They are in the abstract and the [Claim] paragraph of `abstract_intro_edit.md`, tagged `[EDITED]`, with your originals kept beside them.
> 2. **Fluency versus deliberate checking** is resolved in §5.5 move 4.
> 3. **The "decision space" term collision** is resolved in §5.0 move 4.
> 4. **The definition** is resolved in §5.0 move 1.
>
> **Structural model:** Cutting, J., & Deterding, S. (2022). The task-attention theory of game learning: A theory and research agenda. *Human–Computer Interaction, 39*(5–6), 257–287. https://doi.org/10.1080/07370024.2022.2047971. I read it in full or in its substantive sections; the analysis is in `../models/MODEL_cutting2022.md`. Each section below names the move it borrows, with the model's section number in brackets.
>
> **Layout of each section:**
> - the job of the section and the model move it borrows;
> - the moves, numbered;
> - a **section bibliography**, with each source annotated for that section: what it is, what it shows (with locator), how it is used here, and its limits.
>
> Full annotations sit in the section where a source does most of its work; other sections cross-reference them. A master APA 7 list closes the file.
>
> **Status codes:** **[F]** read in full or in substantive sections; **[A]** abstract only; **[M]** metadata only; **[P]** preprint. You deferred Saenger, Parkes, Gibson, and O'Regan & Noë; they stay flagged.

---

## Word budget (scaled to the model)

The model's body runs about 14,900 words, and its theory section is 45% of that.

| § | Section | Model analogue | Words |
|---|---|---|---|
| 1 | Introduction | C&D §1 | 1,500 |
| 2 | Streaming output as a new scriptio continua | none (your distinctive move) | 1,300 |
| 3 | A brief introduction to reading, attention and events | C&D §2 (primer) | 1,600 |
| 4 | Streaming in current HCI, automation and LLM-reliance accounts | C&D §3 (mini-review) | 2,000 |
| 5 | Algorithmacy theory: decision spaces and their marking | C&D §4 (theory) | 5,000 |
| 6 | Discussion: implications and future work | C&D §5 | 3,000 |
| 7 | Conclusion | C&D §6 | 300 |
| | **Total body** | | **about 14,700** |

The journal sets no word limit (checked 20 October 2026). In the model paper, *HCI* printed about 14,900 body words over 31 pages.

---

## Front matter

- **Title.** "Spaces in the Stream: Algorithmacy and the Perception of Decision Spaces in Streaming AI Output" (suggested). **[NEEDS: your wording]**
- **Abstract (about 200 words).** The model's published version opens without one, but *HCI*'s style guide asks the abstract to state "the nature of the paper (theoretical, empirical, or methodological)", so write one. Moves:
  1. This is a theoretical article.
  2. The puzzle in the evidence.
  3. The claim: streamed AI output hides its decision spaces, and navigating them is algorithmacy.
  4. The scriptio continua parallel: marks, gap, competence.
  5. The three perceptual mechanisms that marking restores.
  6. What the paper delivers: propositions, formal predictions, design implications.
- **Keywords.** The model lists eight. Suggested: algorithmacy; decision spaces; streaming; large language models; eye movements; event segmentation; automation supervision; overreliance.

---

## 1. INTRODUCTION (about 1,500 words)

**Job:** move from a puzzle in the evidence, to a one-sentence claim, to the whole theory in numbered points. Borrowed from C&D §1.

### Moves

1. **The puzzle in the evidence** (C&D open on "mixed and contradictory" findings). Evidence on streamed AI output points in different directions, and nobody has tested the variable that would reconcile it:
   - Streaming changes where people look (Park & Lee, 2024).
   - Streaming raises perceived competence and trust but not perceived effectiveness (Bhat, 2025).
   - Fluent explanations raise reliance on wrong answers (Kim et al., 2025).
   - Pacing is set by the server, not the reader (Liu et al., 2024; Xiao & Yang, 2025).
   - The untested variable: where, in the stream, the reader has a place to stop.

   **ROGER:** your [Context] paragraph supplies most of this (resolve flags F3–F6).

2. **The claim, in one sentence** (C&D: "we propose that task-based attention is ... [a] moderator"). Supervising streamed AI output means navigating decision spaces: the opaque, co-opted points in the process where judgment is required. Streaming hides them by removing the boundaries and look-backs that reading relies on. Marking them makes them perceptible, and navigating them is algorithmacy.
   - **ROGER:** your [Claim] paragraph's decision-spaces sentence, reworded from "implementing" to "marking" (see the conflict note at the top).

3. **Two bases of evidence** (C&D cite attention research plus their own game studies):
   - reading and event research (§3);
   - supervision and reliance research (§4).

4. **Scope bracketing** (C&D: "not ... the sole or primary mechanism ... we analytically bracket").
   - **What this paper covers:** the *perceptual* layer of algorithmacy, meaning how a reader comes to see a decision space in a stream.
   - **What it brackets:**
     - the organizational and political layers of algorithmacy, which your dissertation treats;
     - model accuracy;
     - explanation design;
     - user training.
   - **What it does not claim:** that marking is sufficient for navigation. Marking makes a decision space perceptible; algorithmacy still has to fill it, just as a written space does not make a reader literate.

5. **What current accounts miss** (one paragraph previewing §4). Pacing work changes the *rate* of the stream. Friction work places obstacles *before or around* model access. Automation research studies recommendations and transparency. None of them places structure *inside* the stream.

   **Gap sentence:** "I found no work that marks decision points inside a streamed AI response, or that places interface boundaries inside one" (searches of arXiv, Consensus and the web, 20 October 2026; `search-log.md` rows 23–34 and 51–55).

6. **The theory as numbered points** (C&D give six). Draft for you to accept or rewrite:
   - (i) Literacy fills the gap between marks and meaning. Algorithmacy fills the gap at a process's decision spaces: the opaque, co-opted points where judgment is required.
   - (ii) In streamed AI output, decision spaces arrive inside a reading task the reader does not pace.
   - (iii) Reading depends on stable targets, units of sense and the freedom to look back. Streaming removes all three at the moments decision spaces occur, and renews a forward pull at the leading edge.
   - (iv) Streaming therefore hides decision spaces. Fluency and recommendation framing co-opt them by making a judgment point read as a finished answer.
   - (v) Marking a decision space restores a target, an event boundary and a look-back window. The effect depends on where the mark falls, how long it lasts and what form it takes.
   - (vi) Marking makes a decision space perceptible but does not fill it. Gaze at a marked decision space is necessary, not sufficient, evidence of navigation, and the reader's algorithmacy moderates what follows.

7. **ROGER:** the algorithmacy sentence, then a roadmap that names each section and subsection (C&D's roadmap names subsections).

### Section bibliography

No new full annotations here; the sources are previewed and annotated where they do their work.
- Park & Lee (2024), Bhat (2025), Liu et al. (2024), Xiao & Yang (2025): see §4.1.
- Kim et al. (2025): see §4.3.

---

## 2. STREAMING OUTPUT AS A NEW SCRIPTIO CONTINUA (about 1,300 words)

**Job:** make the historical argument that motivates the theory. The model has no equivalent; keep this section because the analogy is your contribution (C1). It can be shortened to a long motivating section if length requires.

### Moves

1. **What word spacing did.** **ROGER:** your Saenger and Parkes paragraph. Pick one term, *scriptio* or *scriptura continua* (flag F16). **[Deferred: page locators; flag F17 stays]**
2. **What the space does for the eye.** Missing spaces slow reading by about half, roughly double regressions in sentence reading, and shift where the eyes land in a word.
3. **Spacing permits narrow focus on one word at a time.**
4. **The objection that chatbots already print spaces.** **[NEEDS: your wording]**
5. **The answer: a second layer of legibility, above the word.** **[NEEDS: adopt Parkes's "grammar of legibility" or not; chapter unread]**
6. **What streams keep and what they remove.** **ROGER:** "Alternatively, is the current experience of interacting with AI already optimal?"
7. **Where the analogy breaks.** Medieval readers set their own pace; stream readers do not. Silent reading predates spacing (Knox, 1968), so the claim concerns the *ease* of reading, not its invention. This move moves the old limits section here, following C&D's practice of placing caveats where they bite.
8. **From the space to the competence (the hand-off to §5.0).**
   - The space made word boundaries perceptible, but it did not make anyone literate. A non-literate person sees the marks and the gaps and still cannot fill the gap between marks and meaning.
   - The same triad holds for streams: output, a decision space, and the competence to fill it.
   - **ROGER:** "I theorize that observing AI in operation today is analogous to reading scriptura continua, which requires oral reading to discern each word's function, thereby merging oracy with emerging literacy. Similarly, interacting with AI now combines users' literacy with their developing algorithmacy."

### Section bibliography

**Saenger, P. (1997).** *Space between words: The origins of silent reading*. Stanford University Press. https://doi.org/10.1515/9781503619081 **[M, deferred]**
- *What it is:* the standard history linking word separation to silent reading.
- *Used here:* the historical claims in move 1.
- *Limits:* not read this session. Every claim needs a page locator before submission.

**Parkes, M. B. (1992).** *Pause and effect: An introduction to the history of punctuation in the West*. Scolar Press (reissued Routledge, 2016). **[M, deferred]**
- *What it is:* a history of punctuation. Chapter 3 is titled "The Grammar of Legibility" (title verified).
- *Used here:* a possible name for the second layer (move 5).
- *Limits:* contents unread; confirm which edition you cite.

**Rayner, K., Fischer, M. H., & Pollatsek, A. (1998).** Unspaced text interferes with both word identification and eye movement control. *Vision Research, 38*(8), 1129–1144. https://doi.org/10.1016/S0042-6989(97)00274-5 **[F]**
- *What it is:* two eye-tracking experiments (N = 12 and N = 10) comparing spaced, unspaced, filled, wide-spaced and flanked text.
- *What it shows:*
  - Reading rate fell 54% for sentences and 44% for passages without spaces (p. 1132), and 58% in Experiment 2 (p. 1138).
  - Regressions in sentence reading rose from 9.7% to 17.3% (Table 1).
  - Landing positions moved from just left of a word's centre to its start (pp. 1136, 1141).
  - Missing spaces disrupt both word identification and saccade programming, word identification more (p. 1143).
  - Spaces enhance upcoming words "as 'targets' for an eye movement" (p. 1129).
- *Used here:* move 2. It also grounds Function 1 in §5.2.
- *Limits:* the paper says nothing about "low-spatial-frequency boundaries" (flag F7).

**Drieghe, D., Fitzsimmons, G., & Liversedge, S. P. (2017).** Parafoveal preview effects in reading unspaced text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(10), 1701–1716. https://doi.org/10.1037/xhp0000441 **[A]**
- *What it shows:* unspaced text slowed reading, with "rather limited evidence" that readers spread processing across words.
- *Used here:* move 3.

**McDonald, S. A. (2006).** Parafoveal preview benefit in reading is only obtained from the saccade goal. *Vision Research, 46*(26), 4416–4424. https://doi.org/10.1016/j.visres.2006.08.027 **[M]**
- *Used here:* optional, in move 3. Preview comes only from the word the eye is aimed at.
- *Limits:* unread; cite lightly or drop.

**Knox, B. M. W. (1968).** Silent reading in antiquity. *Greek, Roman and Byzantine Studies, 9*(4), 421–435. **[M]**
- *Used here:* move 7. Silent reading predates spacing.
- *Limits:* unread.

---

## 3. A BRIEF INTRODUCTION TO READING, ATTENTION AND EVENTS (about 1,600 words)

**Job:** a primer on the underlying science for HCI readers, borrowed from C&D §2. Define the terms and mechanisms the theory rests on, and keep it short; claims about streaming wait for §§4–5. Each subsection ends by naming the mechanism it hands to §5.

### 3.1 Regressions and rereading (hands Function 3 to §5.4)

1. **Key terms:** fixation, saccade, regression.
   - Regressions are 10–15% of eye movements by one estimate (Schotter et al., 2014, p. 1225) and 15–25% by another (Booth & Weger, 2013, citing Rayner & Pollatsek, 1989).
2. **Regressions serve rereading,** so the text must stay available.
3. **Preventing regressions lowers comprehension.**
4. **Rereading carries the structural repair** that forward reading does not.

**ROGER:** "Schotter, Tran, and Rayner (2014) found that masking each word after it was read..." Change "word masking" to "trailing mask".

### 3.2 Onsets, salience and the priority map (hands Function 1 to §5.2)

1. **Abrupt onsets** are selected first, but only when the onset is the only such event.
2. **Bottom-up salience** is powerful but short-lived. The priority map can reset after "a break in the action."

**ROGER:** your Wolfe and Yantis sentence (flag F10).

### 3.3 Event segmentation (hands Function 2 to §5.3)

1. **Event Segmentation Theory:** activity is parsed into events, and updating happens at event boundaries.
2. **In reading,** situation changes predict boundaries, and readers slow down at them, even in a software-paced, non-reviewable display.
3. **Boundaries trigger global and incremental updating.**
4. **Boundaries track surprise computed from text.**

**ROGER:** your Zacks et al. (2007) sentence.

### 3.4 Perception as action (hands the framing to §5.0)

1. **Seeing as mastery of sensorimotor contingencies.** **ROGER:** your Gibson and O'Regan sentences (flag F11, deferred).
2. **Fixed text gives readers material placeholders** that support a map of the text.

### Section bibliography

#### 3.1

**Schotter, E. R., Tran, R., & Rayner, K. (2014).** Don't believe what you read (only once): Comprehension is supported by regressions during reading. *Psychological Science, 25*(6), 1218–1226. https://doi.org/10.1177/0956797614531148 **[F]**
- *What it is:* N = 40; single one-line sentences, garden-path and unambiguous; a trailing mask turned each word to x's once the eyes passed it.
- *What it shows:*
  - The mask lowered comprehension (b = −0.92, z = 5.09, p < .001), and not only for garden-path sentences (interaction p = .06) (p. 1221).
  - Comprehension was 78% in normal reading without a regression versus 71% under the mask (p. 1223).
  - Readers regress 10–15% of the time (p. 1225).
- *Used here:* the causal anchor for move 3.
- *Limits:* single sentences only.

**Booth, R. W., & Weger, U. W. (2013).** The function of regressions in reading: Backward eye movements allow rereading. *Memory & Cognition, 41*(1), 82–97. https://doi.org/10.3758/s13421-012-0244-y **[F]**
- *What it is:* three experiments (N = 22, 32, 19).
- *What it shows:*
  - Readers regress to reread, not to cue memory by location.
  - When the text was made illegible, regressions fell (F(1, 851) = 65.34) and stopped predicting comprehension.
  - The authors foresaw that readers "of scrollable text on small screens" may find "rereading is often impossible" (General Discussion).
- *Used here:* move 2.

**Timkey, W., Huang, K.-J., Oh, B.-D., Prasad, G., Arehalli, S., Linzen, T., & Dillon, B. (2026).** Eye movements reveal a dissociation between prediction and structural processing difficulty in language comprehension. *Proceedings of the National Academy of Sciences, 123*(32), e2532230123. https://doi.org/10.1073/pnas.2532230123 **[A + preprint in part]**
- *What it shows:* across 368 readers, language-model surprisal explained early reading effects but not a rereading cost at the point of disambiguation, which reflects "the cost of detecting or correcting errors in the structure-building process."
- *Used here:* move 4.
- *Limits:* garden-path syntax; applying it to auditing AI output is your inference.

**Metzner, P., von der Malsburg, T., Vasishth, S., & Rösler, F. (2017).** The importance of reading naturally: Evidence from combined recordings of eye movements and electric brain potentials. *Cognitive Science, 41*(S6), 1232–1263. https://doi.org/10.1111/cogs.12384 **[A]**
- *What it shows:* free reading beat word-by-word presentation only on trials where readers regressed to the anomaly.
- *Used here:* move 3, converging evidence.

**Benedetto, S., Carbone, A., Pedrotti, M., Le Fevre, K., Bey, L. A. Y., & Baccino, T. (2015).** Rapid serial visual presentation in reading: The case of Spritz. *Computers in Human Behavior, 45*, 352–358. https://doi.org/10.1016/j.chb.2014.12.043 **[A]**
- *What it shows:* rapid serial visual presentation (RSVP), which suppresses regressions and preview, hurt literal comprehension.
- *Used here:* move 3.

#### 3.2

**Yantis, S., & Jonides, J. (1984).** Abrupt visual onsets and selective attention: Evidence from visual search. *Journal of Experimental Psychology: Human Perception and Performance, 10*(5), 601–621. https://doi.org/10.1037/0096-1523.10.5.601 **[F: introduction, Exp. 1, General Discussion]**
- *What it shows:* an abrupt-onset item is identified first in visual search (N = 18 in Exp. 1). Capture occurs "only when the visual field contains but one such event" (p. 617).
- *Used here:* move 1, with its limit stated.

**Wolfe, J. M. (2021).** Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review, 28*(4), 1060–1092. https://doi.org/10.3758/s13423-020-01859-9 **[F pp. 1060–1071]**
- *What it is:* five sources of guidance feed a priority map, which attention visits about 20 times per second.
- *What it shows (p. 1069):*
  - Bottom-up salience is "a very powerful but short-lived form of guidance."
  - "Attention capture" may be a misnomer.
  - "If there is enough of a break in the action, the map may get reset"; Wolfe asks whether event boundaries reset it.
- *Used here:* move 2. It is the strongest single anchor for why a pause might help.
- *Limits:* the reset is Wolfe's suggestion, not a finding.

#### 3.3

**Zacks, J. M., Speer, N. K., Swallow, K. M., Braver, T. S., & Reynolds, J. R. (2007).** Event perception: A mind-brain perspective. *Psychological Bulletin, 133*(2), 273–293. https://doi.org/10.1037/0033-2909.133.2.273 **[M]**
- *Used here:* move 1, as the theory citation.
- *Limits:* unread; paraphrase the theory as it is stated in Zacks et al. (2009) and Kurby & Zacks (2008).

**Kurby, C. A., & Zacks, J. M. (2008).** Segmentation in the perception and memory of events. *Trends in Cognitive Sciences, 12*(2), 72–79. https://doi.org/10.1016/j.tics.2007.11.004 **[A]**
- *Used here:* move 1, a short review.

**Zacks, J. M., Speer, N. K., & Reynolds, J. R. (2009).** Segmentation in reading and film comprehension. *Journal of Experimental Psychology: General, 138*(2), 307–327. https://doi.org/10.1037/a0015305 **[F]**
- *What it shows:*
  - Situation changes predict event boundaries.
  - Each additional situation change added 92.8 ms of reading time (Exp. 3).
  - Each 10% rise in the probability of a boundary added about 108 ms.
  - Boundaries aligned above chance even in a *visual-sequential* condition: one clause at a time, paced by software at about 3.35 words per second, not reviewable (Exp. 1).
- *Used here:* move 2. It is the closest precedent to a stream.

**Kurby, C. A., & Zacks, J. M. (2012).** Starting from scratch and building brick by brick in comprehension. *Memory & Cognition, 40*(5), 812–826. https://doi.org/10.3758/s13421-011-0179-8 **[F results]**
- *What it shows:* readers updated their situation model both globally and incrementally. Goals were mentioned more at fine-grained boundaries even without a goal change (OR = 2.29, z(926) = 2.87).
- *Used here:* move 3.

**Kumar, M., Goldstein, A., Michelmann, S., Zacks, J. M., Hasson, U., & Norman, K. A. (2023).** Bayesian surprise predicts human event segmentation in story listening. *Cognitive Science, 47*(10), e13343. https://doi.org/10.1111/cogs.13343 **[A]**
- *What it shows:* Bayesian surprise computed from GPT-2 tracks where humans place event boundaries.
- *Used here:* move 4. Boundaries can be computed from text, which matters for the placement rule in §5.1.

#### 3.4

**Gibson, J. J. (1979).** *The ecological approach to visual perception*. Houghton Mifflin. **[M, deferred]**
- *Used here:* affordances.
- *Limits:* unread (flag F11).

**O'Regan, J. K., & Noë, A. (2001).** A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973. https://doi.org/10.1017/S0140525X01000115 **[A, deferred]**
- *Used here:* sensorimotor contingencies.
- *Limits:* abstract only.

**O'Regan, J. K. (2011).** *Why red doesn't sound like a bell: Understanding the feel of consciousness*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199775224.001.0001 **[M, deferred]**
- *Used here:* optional; the book-length statement.

**Mangen, A., Olivier, G., & Velay, J.-L. (2019).** Comparing comprehension of a long text read in print book and on Kindle: Where in the text and when in the story? *Frontiers in Psychology, 10*, Article 38. https://doi.org/10.3389/fpsyg.2019.00038 **[F]**
- *What it is:* N = 50; a 28-page story read on Kindle or in print.
- *What it shows:* print readers reconstructed the plot's chronology better (t(48) = 2.03, η² = .08). The authors tie this to "material placeholders," citing Gibson and O'Regan & Noë.
- *Used here:* move 2.
- *Limits:* page-turning devices only; scrolling was not tested.

**Mangen, A., Walgermo, B. R., & Brønnick, K. (2013).** Reading linear texts on paper versus computer screen: Effects on reading comprehension. *International Journal of Educational Research, 58*, 61–68. https://doi.org/10.1016/j.ijer.2012.12.002 **[A]**
- *Used here:* optional.

**Delgado, P., Vargas, C., Ackerman, R., & Salmerón, L. (2018).** Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. *Educational Research Review, 25*, 23–38. https://doi.org/10.1016/j.edurev.2018.09.003 **[A, via Mangen et al. 2019]**
- *Used here:* optional. The paper advantage was larger under time constraint.

---

## 4. STREAMING IN CURRENT HCI, AUTOMATION AND LLM-RELIANCE ACCOUNTS (about 2,000 words)

**Job:** a mini-review of competing accounts, borrowed from C&D §3. Each subsection ends by naming what its account leaves out; a summary paragraph then states the gap. Open with one sentence: given what §3 shows about reading, one would expect the structure of a stream to figure in current accounts, and it does not. This mirrors C&D's opening of §3.

### 4.1 Work on streaming and pacing

**Moves:**
1. Streams change gaze.
2. Streaming display raises perceived authority.
3. Delivery pacing is set by compute, and recent work adapts the rate.
4. The text still forming changes rereading.

**Omits:** *where* in the stream a reader can stop. Pacing work changes speed, not structure.

**ROGER:** your [Context] sentences on rates (flags F4–F6).

### 4.2 Automation supervision and trust

**Moves:**
1. Complacency and bias are failures of attention allocation. Looking is not seeing.
2. Recommendations lower scrutiny.
3. Transparency raises agreement bias, and transparency the user chooses does not help.
4. Oversight of agents fails on timing.
5. Experts learn a tool's "boundary conditions" over time.

**Omits:** the presentation of output that arrives continuously. These accounts model discrete advice.

**ROGER:** your Parasuraman and Manzey sentence (flag F15).

### 4.3 LLM overreliance and friction

**Moves:**
1. Fluent explanations raise reliance; sources and inconsistencies lower it.
2. Fluency can make wrong answers more convincing.
3. Overreliance leaves traces in behaviour.
4. Cognitive forcing functions reduce overreliance, partly by delay alone.
5. Friction designs place obstacles *before* an action (microboundaries), *before or around* access to the model (selective and preparatory friction), or *inside* the model (concept suppression).
6. Asking users to reflect has a price.

**Omits:** friction placed *inside the streamed response*, at points set by its meaning.

**ROGER:** your Kim and Bhat sentences (flags F12–F14).

### 4.4 Gaze as evidence of supervision

**Moves:**
1. Gaze tracks reliance.
2. But attention can move without judgment moving.
3. Shorter fixations can signal overreliance rather than ease.

**Omits:** a theory of *where* gaze should go during a stream, and of when gaze counts as checking.

### 4.5 Summary: the gap

In one paragraph, as C&D close their §3: current accounts treat the stream's speed, the advice it carries and the friction around it, but not its decision spaces: where judgment is required, and whether the reader can see it. Algorithmacy theory, at its perceptual layer, fills that gap.

### Section bibliography

#### 4.1

**Park, H., & Lee, Y. (2024).** The effect of text movement on eye movements in generative AI chatbots. *Archives of Design Research, 37*(4), 181–197. https://doi.org/10.15187/adr.2024.08.37.4.181 **[F]**
- *What it is:* the only eye-tracking study I found of chatbot text movement. N = 36, Korean expository text, four movement types, Tobii eye tracker.
- *What it shows:*
  - Text generated at the bottom of the screen produced more fixation starts, more total fixation time and larger saccade amplitudes than text appearing whole at the top.
  - Fixation starts clustered where new text appeared (Tables 9, 11–12).
- *Used here:* move 1.
- *Limits:* one study; topic confounded with condition; no comprehension measure (flag F3).

**Bhat, M. (2025).** How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131 **[F]**
- *What it is:* within-subjects, N = 103, GPT-3.5 Turbo; simulated typing at 2–3 s per sentence versus a static display.
- *What it shows:*
  - Typing raised perceived competence (F = 40.89), trustworthiness (F = 35.21) and persuasiveness (F = 76.89), all p < .0001.
  - Perceived effectiveness did not change (F = 0.16, p = .69) (Table 2).
- *Used here:* move 2, and the puzzle in §1.
- *Limits:* self-report only; simulated typing, not token streaming; responses may have differed across conditions (§5.5).

**Liu, J., Chung, J.-W., Wu, Z., Lai, F., Lee, M., & Chowdhury, M. (2024).** *Andes: Defining and enhancing quality-of-experience in LLM-based text streaming services* [Preprint]. arXiv:2404.16283. **[F §1–2][P]**
- *What it shows:*
  - Reading consumption estimated at 4.8 tokens/s, converted from an age table at about 1.3 tokens per word (v1 §2.1).
  - One server delivered 11.2 tokens/s on a real trace (v2 §2.2).
- *Used here:* move 3.
- *Limits:* 4.8 is an estimate, not a measurement (F4). Nothing in the paper supports "11–25 tokens/s" (F5).

**Xiao, C., & Yang, B. Z. (2025).** Streaming, fast and slow: Cognitive load-aware streaming for efficient LLM serving. In *Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology* (pp. 1–13). ACM. https://doi.org/10.1145/3746059.3747721 **[F]**
- *What it shows:* the 99th-percentile comfortable streaming speed was 21.20 words/s for an easy passage and 11.97 for a complex one, against about 45 words/s from the GPT-4o API (PEST procedure, 79 valid participants; §3.2).
- *Used here:* move 3.
- *Limits:* measures comfortable speed, not comprehension (F6).

**Zhu, H., Wang, J., Xie, L., Ma, R., Sun, Y., Liu, F., Zheng, C., & Li, Q. (2026).** Just-in-time tokens: Adaptive token pacing for cognitive-friendly LLM streaming. In *Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–8). ACM. https://doi.org/10.1145/3772363.3798936 **[M]**
- *Used here:* move 3. Shows HCI work adapting the *rate* of streaming.
- *Limits:* unread; read it before relying on it.

**Sharmin, S., Špakov, O., & Räihä, K.-J. (2015).** Dynamic text presentation in print interpreting – An eye movement study of reading behaviour. *International Journal of Human-Computer Studies, 78*, 17–30. https://doi.org/10.1016/j.ijhcs.2015.01.010 **[A]**
- *What it shows:* text emerging word by word produced more rereading and regressions than text emerging letter by letter (N = 20).
- *Used here:* move 4. The closest precedent to token streaming.

**Sharmin, S., et al. (2016).** The reading process of dynamic text – A linguistic approach to an eye movement study. *SKY Journal of Linguistics, 29*. **[A; authors and pages unverified]**
- *What it shows:* 90.8% of regression landings fell on content words, against a base rate of 57.1%.
- *Used here:* optional, in move 4.

**Harvey, H., Godwin, H. J., Fitzsimmons, G., Liversedge, S. P., & Walker, R. (2017).** Oculomotor and linguistic processing effects in reading dynamic horizontally scrolling text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(3), 518–536. https://doi.org/10.1037/xhp0000329 **[A]**
- *What it shows:* under horizontal scrolling, word-level effects were preserved but the benefit of sentence-level predictability was lost.
- *Used here:* move 4.

**Harvey, H., & Walker, R. (2018).** Reading comprehension and its relationship with working memory capacity when reading horizontally scrolling text. *Quarterly Journal of Experimental Psychology, 71*(9), 1887–1897. https://doi.org/10.1080/17470218.2017.1363258 **[A]**
- *What it shows:* literal comprehension held, but inference suffered; returning to earlier text was harder.
- *Used here:* move 4.

**Haverkamp, Y. E., Bråten, I., Latini, N., & Salmerón, L. (2023).** Is it the size, the movement, or both? Investigating effects of screen size and text movement on processing, understanding, and motivation when students read informational text. *Reading and Writing, 36*(7), 1589–1608. https://doi.org/10.1007/s11145-022-10328-9 **[F]**
- *What it is:* N = 145; reader-controlled scrolling versus paging of a PDF.
- *What it shows:* scrollers backtracked less often (2.49 vs 3.53, p = .012) but farther. The comprehension advantage for paging was only a trend (p = .066).
- *Used here:* move 4.
- *Limits:* reader-controlled, with no auto-scroll (F9).

#### 4.2

**Parasuraman, R., & Manzey, D. H. (2010).** Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055 **[F core sections]**
- *What it shows:*
  - Complacency arises under multiple-task load (p. 381).
  - "Looking-but-not-seeing" is used to explain commission errors (p. 403).
  - In Manzey et al. (2008), about half of those who missed a wrong diagnosis had sampled all the information they needed (p. 402).
- *Used here:* move 1.
- *Limits:* the evidence is information sampling, not fixations (F15).

**Lee, J. D., & See, K. A. (2004).** Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392 **[A]**
- *Used here:* move 1 (appropriate reliance) and move 5 (origin of "boundary conditions").

**Gegoff, I., Tatasciore, M., Bowden, V. K., & Loft, S. (2025).** Deciphering automation transparency: Do the benefits of transparency differ based on whether decision recommendations are provided? *Human Factors, 67*(8), 776–794. https://doi.org/10.1177/00187208251318465 **[F]**
- *What it is:* N = 142; an uninhabited-vehicle management task.
- *What it shows:*
  - Recommendations raised accuracy (.89 vs .85, ηp² = .16).
  - Recommendations slightly lowered discrimination of accurate from inaccurate system information (.93 vs .94, ηp² = .05) (pp. 785–787).
  - The authors call for eye tracking (p. 790).
- *Used here:* move 2. A streamed answer arrives as a recommendation.
- *Limits:* small effect; novices.

**Tatasciore, M., Bennett, L., Bowden, V. K., Bell, J., Visser, T. A. W., McAnally, K., McCarley, J. S., Thompson, M. B., Shanahan, C., Morris, R., & Loft, S. (2026).** Adaptable automation transparency: Should humans be provided flexibility to self-select transparency information? *Human Factors, 68*(1), 5–27. https://doi.org/10.1177/00187208251349269 **[F]**
- *What it is:* two experiments (N = 73 and 88).
- *What it shows:*
  - Participants chose high transparency on 39% and 43% of adaptable trials.
  - Adaptable transparency did not improve accuracy of automation use (p. 22).
  - Across six studies, high transparency raised hit rate and sensitivity but also bias toward agreeing, with no gain in correct rejections (p. 21).
- *Used here:* move 3. Reused in §6.2.

**Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026).** *Comparing human oversight strategies for computer-use agents* [Preprint]. arXiv:2604.04918. **[F][P]**
- *What it is:* N = 48, 192 live agent sessions.
- *What it shows:*
  - Users blocked 29 of 138 problematic actions.
  - 61 of 109 failures (56%) involved a timing mismatch.
  - Oversight depends on "aligning authority, timing, and attention with decision-critical moments."
- *Used here:* move 4. Reused in §5.1.
- *Limits:* preprint; no eye tracking.

**Lamb, S. C., Byrne, M., Norman, T. J., Ramchurn, S. D., & Naiseh, M. (2026).** What's informing trust and adoption? Can current cognitive models support expert adoption of AI? *Journal of Cognitive Engineering and Decision Making, 20*(2), 158–175. https://doi.org/10.1177/15553434261430550 **[F]**
- *What it is:* a longitudinal naturalistic study; 12 defence intelligence analysts, then 9, adopting an object-detection overlay on live video.
- *What it shows:*
  - Seven of nine stopped seeing the tool as an "advisor" (McNemar p = .023).
  - Analysts wanted to learn the tool's "boundary conditions."
  - The authors argue for interdependence over task allocation.
- *Used here:* move 5. Reused in §6.3.

**Endsley, M. R. (2017).** From here to autonomy. *Human Factors, 59*(1), 5–27. https://doi.org/10.1177/0018720816681350 **[A]**
- *Used here:* optional, for move 1: the automation conundrum.

#### 4.3

**Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025).** Fostering appropriate reliance on large language models: The role of explanations, sources, and inconsistencies. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–19). ACM. https://doi.org/10.1145/3706598.3714020 **[F]**
- *What it is:* N = 16 think-aloud plus N = 308 pre-registered experiment; hard binary factual questions.
- *What it shows:*
  - Explanations raised agreement with both correct and incorrect answers.
  - Sources and inconsistencies lowered agreement with incorrect answers.
  - With an incorrect answer, accuracy was 17.2% with an explanation versus 21.8% without (Table 1).
  - 189 of 308 participants never clicked a source.
- *Used here:* move 1, and the puzzle in §1.
- *Limits:* responses were shown whole, not streamed; the task was objective QA (F13).

**Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X., Mayer, L. W., & Smyth, P. (2025).** What large language models know and what people think they know. *Nature Machine Intelligence, 7*(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7 **[A]**
- *What it shows:* longer explanations raised users' confidence without raising accuracy.
- *Used here:* move 1.

**Zhu, X., Le Truong, K., Fogliato, R., Swamy, G., Zhang, W., Yang, M., Ye, L., Liu, B., Liu, M., Ilyas, A., & Wu, Z. S. (2026).** *Justified or just convincing? Error verifiability as a dimension of LLM quality* [Preprint]. arXiv:2604.04418. **[F §1–7.1][P]**
- *What it shows:*
  - Post-training raised accuracy without raising how verifiable errors were.
  - Rephrasing without new information did not help.
  - For one model on one benchmark (Tulu3.1-8B, GSM8K), the false-positive score fell from 0.717 to 0.602 after preference optimisation (§7.1).
- *Used here:* move 2.
- *Limits:* preprint; most raters were LLMs.

**Liu, C., Zhou, Q., Shen, X., Liu, X. B., Wu, T., & Chen, X. A. (2026).** Behavioral indicators of overreliance during interaction with conversational language models. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–23). ACM. https://doi.org/10.1145/3772318.3790332 **[F]**
- *What it is:* N = 77; a GPT-4 platform with injected misinformation; mouse and keyboard logs.
- *What it shows:* high overreliance went with whole-text copy-paste, coarse navigation, and accepting despite hesitation (Table 3).
- *Used here:* move 3.
- *Limits:* no eye tracking.

**Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021).** To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287 **[F §1–4]**
- *What it is:* N = 199; three cognitive forcing functions, including a 30-second wait.
- *What it shows:* on incorrect AI predictions, the forcing functions cut overreliance (0.48 vs 0.64, d = .36). Participants preferred and trusted them less.
- *Used here:* move 4. Reused in P2, §5.6.

**Ghosh, A., Sarkar, A., Lindley, S., & Poelitz, C. (2026).** *An experimental comparison of cognitive forcing functions for execution plans in AI-assisted writing: Effects on trust, overreliance, and perceived critical thinking* [Preprint]. arXiv:2601.18033. **[A][P]**
- *What it shows:* with n = 214, an "Assumptions" forcing function reduced overreliance most, without raising cognitive load.
- *Used here:* move 4.

**Cox, A. L., Gould, S. J. J., Cecchinato, M. E., Iacovides, I., & Renfree, I. (2016).** Design frictions for mindful interactions: The case for microboundaries. In *Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems* (pp. 1389–1397). ACM. https://doi.org/10.1145/2851581.2892410 **[F]**
- *What it is:* a position paper with no data.
- *What it shows:*
  - A microboundary is "a small obstacle prior to an interaction," imposed through a short time cost, that shifts behaviour from automatic to deliberate.
  - It lists user autonomy over microboundaries as an open question.
- *Used here:* move 5. The nearest design precedent. Contrasted in §5.7.

**Collins, K. M., et al. (2024).** *Modulating language model experiences through frictions* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2407.12804 **[A][P]**
- *What it shows:* "selective frictions," such as a button that impedes model access, reduced click-through with little effect on accuracy, but spilled over to other topics.
- *Used here:* move 5. Friction placed before access.
- *Limits:* complete the author list.

**Arun, S., et al. (2026).** Encouraging thought before completion: The role of task-specific selective friction in AI-assisted knowledge work. In *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work*. ACM. https://doi.org/10.1145/3808045.3808049 **[A]**
- *What it shows:* N = 40. Preparatory friction raised mental demand and trust but did not reduce self-reported reliance.
- *Used here:* move 5.
- *Limits:* complete the authors and pages.

**Disley, M., & Khan, M. (2026).** Designing cognitive friction with concept suppression in large language models. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2708617 **[F]**
- *What it is:* N = 37; within-subjects ideation unaided, with Llama3.2:3b, or with the concept "chair" suppressed.
- *What it shows:*
  - The unmodified model lowered effort and ownership (ownership 6.38 vs 9.16 suppressed vs 11.49 unaided; ηp² = .251).
  - The authors contrast their model-level friction with interface-level friction ("an added step, a delay"; §2.3) and call for interface-level comparisons (§7.9).
- *Used here:* move 5.
- *Limits:* an ideation task, not verification.

**Forshaw, T., Hale, J., & Longmire, M. (2026).** The Reflection Penalty: When managers accept leadership coaching from a human but not an AI agent. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2744236 **[F]**
- *What it is:* N = 8 managers; design-based research comparing human and AI coaching built on the same protocol.
- *What it shows:* all eight preferred the human coach and resisted the AI's questions, yet the coached behaviours appeared after both (§6.1).
- *Used here:* move 6. Reused in §6.4.
- *Limits:* order unbalanced; the media differed.

#### 4.4

**Cho, J., & Lim, D. (2026).** How source attribution visualization shapes user attention and preference: An eye-tracking study of four AI chatbot layouts. *Journal of Eye Movement Research, 19*(4), Article 89. https://doi.org/10.3390/jemr19040089 **[F]**
- *What it is:* N = 23; four source layouts on static screens.
- *What it shows:* time to first fixation on the source ranged from 0.96 s to 15.65 s by layout, yet gaze did not predict trust: "Attention moved without moving judgment" (§3.4).
- *Used here:* move 2.
- *Limits:* static screens, not streams.

**Wu, Z., Wang, Y., Langer, M., & Feit, A. M. (2025).** RelEYEance: Gaze-based assessment of users' AI-reliance at run-time. *Proceedings of the ACM on Human-Computer Interaction, 9*(3), 1–18. https://doi.org/10.1145/3725841 **[A]**
- *What it shows:* gaze distinguished over-, under- and appropriate reliance.
- *Used here:* move 1.

**Cao, S., & Huang, C.-M. (2022).** Understanding user reliance on AI in assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 6*(CSCW2), 1–23. https://doi.org/10.1145/3555572 **[A]**
- *What it shows:* the share of gaze on the AI's suggestion correlated with agreeing with it.
- *Used here:* move 1.

**Yang, Y., Lee, Y. M., Tabone, W., García de Pedro, J., Happee, R., & Merat, N. (2027).** The effect of augmented reality on pedestrians' gaze patterns and crossing probability while interacting with automated vehicles. *International Journal of Human-Computer Studies, 217*, Article 103920. https://doi.org/10.1016/j.ijhcs.2026.103920 **[F]**
- *What it is:* 27 participants analysed; a pedestrian simulator.
- *What it shows:*
  - AR cut fixation time on the vehicle and the cue (heads-up and crossing-path placements, d = −0.80 each), and crossings came earlier.
  - The authors warn this "may also indicate overreliance" and name gaze-only evaluation as a limitation (§5).
- *Used here:* move 3.

**Resulbegoviq, H., Hlebec, V., Pejić Bach, M., & Stamatović, I. (2026).** Eye tracking and AI-generated content: A systematic literature review of visual attention, cognitive processing, and user engagement. *Journal of Eye Movement Research, 19*(5), Article 97. https://doi.org/10.3390/jemr19050097 **[F in part]**
- *What it shows:* across 23 studies, "no modality-independent gaze pattern emerged." Longer viewing more often reflected difficulty or checking than preference.
- *Used here:* summary of the move.
- *Limits:* inclusion required a human comparator, so the review's silence on streaming is weak evidence.

---

## 5. ALGORITHMACY THEORY: DECISION SPACES AND THEIR MARKING (about 5,000 words)

**Job:** the theory, borrowed from C&D §4. Open by restating the gap, state the theory and its terms, show it as a figure, list the propositions, and tabulate the formal predictions. Then give one subsection per construct in a uniform pattern:
- evidence (§3);
- how it shows up in streams (§4);
- how streams differ from static text;
- "Formally, the theory predicts ...".

### 5.0 Algorithmacy, decision spaces and marking

1. **Algorithmacy: your definitions.** Use the version you want in this paper. **[NEEDS: choose one or merge]** Your current public formulations, from your Substack:
   - *"Algorithmacy is the competency of navigating triadic coordination."* (Literacy derives from "a dyadic structure: a writer and a reader mediated by a static text"; the present structure is "triadic: users mediated by an opaque, optimizing, and recursive intermediary.") Source: "Algorithmacy and the Co-optation of the Subject" (v22).
   - Algorithmacy as a developmental competence like learning to read: the novice "decod[es]" effortfully, while the "algorithmate" user moves "with fluent, unreflective automaticity." Source: "Cognitive Science Implications of Algorithmacy."

   **Decision:** use the first as the paper's definition, and add one clause naming this paper's layer: "Algorithmacy is the competency of navigating triadic coordination; this paper treats its perceptual layer, the capacity to see and act on decision spaces in an intermediary's output."
   - Restate it in the paper without citing the Substack posts. Citing your own blog would break an anonymised review, and the definition is yours to state.
   - Use the developmental account in §5.5, also restated.

2. **The triad in a chatbot stream.** State in one paragraph why a streamed AI response is triadic and not a dyad of user and tool:
   - the output comes from an opaque, optimizing intermediary;
   - its pace is set by the provider's compute (§4.1);
   - its framing is tuned to persuade (Bhat, 2025; Zhu et al., 2026).
   - Co-optation, in the platform sense, means enrolment through the system's design rather than through prior competence. Stark and Vanden Broeck (2024) put it this way: "on platforms they are co-opted."

3. **The literacy parallel, stated as a table in the paper:**

   | | Literacy | Algorithmacy (this paper's layer) |
   |---|---|---|
   | What is given | marks on a page | a stream of output from an opaque process |
   | The gap | between marks and meaning | **decision spaces**: points where judgment is required but the process does not show it |
   | What can make the gap perceptible | the written space, punctuation, layout | **marking** the decision space in the stream |
   | What fills the gap | literacy | algorithmacy |
   | Who cannot fill it | the non-literate reader | the reader without algorithmacy |

4. **Decision spaces, defined.** They are the opaque, co-opted points in an AI's process where a judgment is required (accept, check, reject, redirect) but the process does not present them as such.
   - *Opaque:* the process does not show them.
   - *Co-opted:* fluency, pace and recommendation framing make a judgment point read as a finished answer.
   - **Term decision:** keep "decision spaces." It is your term, and it carries the word-space analogy that a substitute would lose.
     - Define it in one sentence at first use (§1 move 2) and hold the definition fixed.
     - Do not mention the health-policy "decision space" literature. It is unrelated, an *HCI* reviewer is unlikely to raise it, and mentioning it would need a source I have not read. If a reviewer does raise it, one sentence of distinction in the revision will do.

5. **Marking, defined.** Marking is the interface operation that makes a decision space perceptible in the stream: a pause, a space, a rule, a label. Marking does not create decision spaces and does not navigate them.

6. **Prior use of the word "algorithmacy" (context).**
   - OpenAlex records one earlier use: Oberschelp, W. (1995), "Developing analytical competency through informatics teaching", a chapter in an IFIP volume on integrating information technology into education (pp. 115–126).
   - I could not read how the word is used there (Springer bot check). The title and reference list suggest a German informatics-education setting, probably algorithmic competence as a school subject. **That is my inference, not a reading.**
   - Your Substack has been summarised as saying the word "has never appeared in a published academic text." Read the chapter, then position it, for example: "Oberschelp (1995) used *algorithmacy* for ...; I use it for ...". **[NEEDS: the chapter text; it is marked free to read, so it should open in a normal browser]**

7. **Algorithmic literacy, by contrast.** Ridley and Pawlick-Potts (2021) define algorithmic literacy as skill, expertise and awareness concerning algorithms. That is knowledge *about* the intermediary. Algorithmacy is the competence of navigating *through* it, here at the perceptual level.

8. **Figure 1: a nomological network**, a diagram of the theory's constructs and the causal arrows between them. Version 3 draft for you to redraw:

```
                    ┌─────────────────────────────────────────────┐
                    │  DS  Decision spaces (latent, in the process) │
                    └─────────────────────────────────────────────┘
                         │ hidden by                    │ made perceptible by
                         ▼                              ▼
A  Stream properties ──(+)──▶ C  Forward pull     M  Marking (placement, duration, form)
   (server pace, onsets,           at leading edge       │ (−)→C   (+)→D   (+)→E
    auto-scroll, packet gaps)      │ (−)                 ▼
                                   ▼              D  Event boundary / updating
H  Co-optation: fluency and   E  Look-back window         │
   recommendation framing           │                      ▼
        │ (−)                       └──────────▶  F  Fixations and regressions at DS
        ▼                                                  │ (necessary, not sufficient)
   G  Navigation of DS: detection, check, reject, redirect ◀┘
        ▲
        │ moderates F→G
   ALG  Reader's algorithmacy
```

9. **Propositions (i)–(vi)**, matching §1 move 6. Give each a bold line and a short paragraph, as C&D do.

10. **Table 1: formal predictions**, each tied to an arrow (C&D's "1→C" convention). Version 3 draft:

| # | Prediction | Arrow | From your RQs |
|---|---|---|---|
| 1 | Faster pace and leading-edge onsets will increase forward pull and reduce regressions to earlier text | A→C→E | — |
| 2 | Marking will reduce forward pull while the mark lasts | M→C | — |
| 3 | Marking will increase look-back availability | M→E | — |
| 4 | Marks placed at decision spaces will act as event boundaries and prompt updating | M→D | — |
| 5 | Marks at decision spaces will draw more fixations and regressions to those points than the same number of arbitrary marks | M→F (via D, E) | **RQ1 → P1** |
| 6 | Marks at decision spaces will raise navigation (error detection, intervention) over an unmarked stream and over the same number of arbitrary marks | M→G (via F) | **RQ2 → P2** |
| 7 | Arbitrary marks will cost detection latency, workload or local refixations relative to an unmarked stream | M (misplaced)→D (disrupted) | **RQ3 → P3** |
| 8 | Co-optation (fluency, recommendation framing) will lower navigation independently of gaze | H→G | — |
| 9 | Changes in F without changes in G will indicate attention without navigation | F⇸G | **P4** |
| 10 | Mark duration will have an inverted-U effect on navigation | M (duration)→G | — |
| 11 | **New:** algorithmacy will moderate F→G. Readers with more algorithmacy will convert fixations at marked decision spaces into navigation faster and with better-targeted regressions, not with longer dwell | ALG × F→G | — |
| 12 | **New:** marking will narrow the gap in navigation between readers with more and less algorithmacy, as written spacing eased reading without creating literacy | M × ALG→G | — |

**[NEEDS: accept, cut or rewrite. Predictions 11–12 need a way to measure algorithmacy; if you have none yet, state them as a research agenda in §6.1 rather than as formal predictions.]**

### 5.1 Locating decision spaces

1. **ROGER:** your theory sentence ("analogous to reading scriptura continua ... algorithmacy").
2. **[NEEDS: the operational rule for locating decision spaces in a process. This is the contribution.]** The task is identifying where judgment is hidden, not choosing where to insert pauses. Candidates, which can be combined:
   - (a) the end of a checkable claim;
   - (b) a change of goal, cause or entity (Zacks et al., 2009);
   - (c) a peak in model surprisal (Kumar et al., 2023);
   - (d) a point where the user could accept, reject or redirect (Chen et al., 2026). This one fits "decision space" most literally.
3. **Uniform pattern applied.**
   - *Evidence:* boundaries regulate reading (§3.3).
   - *In streams:* gaps fall where packets fall, not where decision spaces are (§4.1).
   - *Difference from static text:* static text carries paragraph and section boundaries; a stream has none while it forms.
   - *Formally:* Table 1, #4.

### 5.2 What marking restores, 1: a stable visual target

**ROGER:** "1) providing a visual target."

**Uniform pattern:**
- *Evidence:* spaces make words targets for saccades (Rayner et al., 1998); onsets capture attention when they are unique (Yantis & Jonides, 1984).
- *In streams:* fixation starts cluster at the leading edge (Park & Lee, 2024).
- *Difference:* in static text the targets stay put; in a stream the newest target keeps moving.
- *Formally:* Table 1, #1–2.

### 5.3 What marking restores, 2: an event boundary

**ROGER:** "2) establishing event boundaries."

**Uniform pattern:**
- *Evidence:* Zacks et al. (2009); Kurby & Zacks (2012); and Wolfe's (2021) suggestion that event boundaries reset the priority map.
- *In streams:* clause-paced display still yields segmentation (Zacks et al., 2009, visual-sequential condition).
- *Difference:* a stream supplies the material for segmentation but no marked boundaries.
- *Formally:* Table 1, #4.

### 5.4 What marking restores, 3: a look-back window

**ROGER:** "3) facilitating efficient regression." **ROGER:** "auto-scrolling interfaces may move previous lines beyond the regression window..." (correct per F9).

**Uniform pattern:**
- *Evidence:* Schotter et al. (2014); Booth & Weger (2013); Timkey et al. (2026).
- *In streams:* rereading changes for text still emerging (Sharmin et al., 2015), and moving text costs integration (Harvey & Walker, 2018).
- *Difference:* static text waits for the reader; a stream moves on.
- *Formally:* Table 1, #3 and #5.

### 5.5 Moderators: properties of the mark and the reader's algorithmacy (C&D's "demands")

1. **Placement.** Marks aligned with meaningful units help and misaligned marks hurt. Interruptions at coarse breakpoints cost little.
2. **Duration.** Brief lockouts encourage checking; long ones induce switching.
3. **Form.** A terse cue that signals without resolving raises visual search; headings steer where readers look back.
4. **The reader's algorithmacy.**
   - On your developmental account, novices decode effortfully and algorithmate users navigate fluently.
   - Hypothesis: marking should matter most for novices. **[No source checked for a parallel claim about spacing and reading skill. Do not assert one without a citation.]**
   - What is supported: fluent adult readers still rely on spaces (Rayner et al., 1998, tested fluent adult readers).
   - **Resolution of the fluency tension (decided):** marking does not require deliberate checking; it gives fluency something legitimate to fit to.
     - *The reading parallel (supported):* fluent reading does not dispense with spaces; it relies on them without noticing. Remove the spaces and fluent adults read 44–58% more slowly, regress more often (9.7% to 17.3% of eye movements in sentences; 11.2% to 16.4% in passages), and lose their usual landing positions (Rayner et al., 1998, pp. 1132–1141).
     - *Applied to algorithmacy:* algorithmate fluency is fit to a system's regularities, but your own account says that fit can be fit to "hidden regularities" (your phrase) the platform has engineered. In an unmarked stream, fluency fits the co-optation. The fluent user accepts at speed and is navigated rather than navigating.
     - *In a marked stream:* fluency can fit the decision spaces themselves. The fluent user orients to marks automatically: fast fixations and targeted regressions. Navigation can be quick without being blind.
     - *For novices:* marks prompt slow, deliberate decoding. That is the stage your developmental account describes, and it is where marking should matter most (hypothesis; see the note below).
     - *What this changes in the theory:*
       - "navigation" (node G) means acting on a decision space, not slow deliberation;
       - Table 1 #11 is restated: algorithmacy should show as *faster and better-targeted* conversion of fixations into navigation, not as more dwell time;
       - long dwell at a mark is evidence of decoding (novices), not of mastery.
     - Put this resolution in the paper as one paragraph in §5.5. It also answers the counterpoint in §6.4: marks need not slow fluent users down.
5. *Formally:* Table 1, #7, #10, #11 and #12.

### 5.6 Gaze and navigation

1. Attention can move without judgment (Cho & Lim, 2026). Looking is not seeing (Parasuraman & Manzey, 2010).
2. Shorter fixations can signal overreliance (Yang et al., 2026).
3. Fluency and recommendation framing work on detection directly (Gegoff et al., 2025; Kim et al., 2025; Zhu et al., 2026).
4. A pause alone can reduce overreliance (Buçinca et al., 2021), so the theory must beat equally many arbitrary marks.
5. *Formally:* Table 1, #6, #8 and #9.

### 5.7 What marking decision spaces is not

One short paragraph contrasting marking with four neighbouring ideas, using the §4.3 sources:
- cognitive forcing functions (delay alone);
- microboundaries (an obstacle *before* the user's action, with a time cost);
- friction around access to the model;
- friction inside the model.

What distinguishes marking:
- it reveals a point already in the process instead of adding an obstacle;
- it sits inside the output and is placed by meaning;
- it works through perception and asks nothing of the user.

### Section bibliography

Sources annotated in §§2–4 are reused here and not repeated. New to this section:

**Stark, D., & Vanden Broeck, P. (2024).** Principles of algorithmic management. *Organization Theory, 5*(2). https://doi.org/10.1177/26317877241257213 **[F, per the close reading recorded in your writing-skill notes; not reread this session]**
- *What it shows:* a theory essay contrasting organizational forms: "Whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted."
- *Used here:* §5.0 move 2, the meaning of "co-opted." Your Substack already uses this quote.
- *Limits:* about platforms and organizations, not streamed text. The step to decision spaces is yours.

**Ridley, M., & Pawlick-Potts, D. (2021).** Moved here from §6. Full annotation below in §6's bibliography. *Used here:* §5.0 move 7, the contrast with algorithmic literacy.

**Oberschelp, W. (1995).** Developing analytical competency through informatics teaching. In *Integrating Information Technology into Education* (IFIP Advances in Information and Communication Technology, pp. 115–126). Springer US. https://doi.org/10.1007/978-0-387-34842-1_12 **[M]**
- *What it is:* the only prior record of the word "algorithmacy" that OpenAlex returns. Crossref shows 16 references, mostly German school-informatics recommendations and the author's own teaching materials.
- *Used here:* §5.0 move 6, as context on prior use.
- *Limits:* unread (Springer bot check). How it uses the word is unknown. Do not characterize it until you have read it.

**Roger Hunt's working papers (Substack).** "Algorithmacy and the Co-optation of the Subject" (v22) and "Cognitive Science Implications of Algorithmacy," rogerhuntphdcand.substack.com. **[F, the relevant passages only]**
- *Used here:* §5.0 move 1, the definitions, and §5.5 move 4, the developmental account.
- *Limits:* self-published. Decide whether to cite them or restate the definition directly.

**Tsoukala, A., Vogelzang, M., & Tsimpli, I. M. (2025).** The influence of text segmentation on garden path processing: Evidence from self-paced reading and eye-tracking. *Language and Cognition, 17*, e58. https://doi.org/10.1017/langcog.2025.10009 **[F]**
- *What it is:* self-paced reading (N = 39) and eye tracking (N = 29); line breaks aligned with or cutting across clauses; lines appeared cumulatively in the eye-tracking study.
- *What it shows:*
  - Misaligned breaks raised first-pass time (d = 0.32) and total time (d = 0.41).
  - Accuracy fell in one misaligned condition (OR = 0.38).
  - Readers recalibrated after repeated misaligned breaks.
  - The interaction did not survive FDR correction; power was 52%.
- *Used here:* §5.5 move 1, and Table 1 #5 and #7.

**Bailey, B. P., & Konstan, J. A. (2006).** On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state. *Computers in Human Behavior, 22*(4), 685–708. https://doi.org/10.1016/j.chb.2005.12.009 **[A]**
- *What it shows:* interruptions during a task, rather than between tasks, cost more time and doubled errors.
- *Used here:* §5.5 move 1; Table 1 #7.

**Powers, S. A., & Scerbo, M. W. (2023).** Examining the effect of interruptions at different breakpoints and frequencies within a task. *Human Factors, 65*(1), 22–36. https://doi.org/10.1177/00187208211009010 **[A]**
- *What it shows:* coarse breakpoints cost about as little as no interruption; fine ones were costly.
- *Used here:* §5.5 move 1.

**Gould, S. J. J., Cox, A. L., Brumby, D. P., & Wickersham, A. (2016).** Now check your input: Brief task lockouts encourage checking, longer lockouts encourage task switching. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 3311–3323). ACM. https://doi.org/10.1145/2858036.2858067 **[A]**
- *What it shows:*
  - In the lab, lockouts encouraged checking, and longer ones made checking more likely.
  - On a crowdsourcing platform, longer lockouts induced task switching.
  - Duration "needs to be carefully calibrated."
- *Used here:* §5.5 move 2; Table 1 #10.
- *Limits:* abstract only. An open-access copy is at the University of Birmingham repository.

**Prajod, P., Cools, H., Röggla, T., Cesar, P., & El Ali, A. (2026).** *Towards gaze-informed AI disclosure interfaces: Eye-tracking attentional and cognitive load while reading AI-assisted news* [Preprint]. arXiv:2605.14999. **[F §1–4.2][P]**
- *What it shows:* a one-line AI-use label drew more total fixation (58.70 vs 49.46, d = 0.34) and more saccades than a detailed label (30 eye-tracked readers of static news).
- *Used here:* §5.5 move 3.
- *Limits:* static text; disclosure labels, not decision boundaries.

**Hyönä, J., & Lorch, R. F. (2004).** Effects of topic headings on text processing: Evidence from adult readers' eye fixation patterns. *Learning and Instruction, 14*(2), 131–152. https://doi.org/10.1016/j.learninstruc.2004.01.001 **[A]**
- *What it shows:* headings sped first-pass reading and steered look-backs.
- *Used here:* §5.5 move 3.

**Lorch, R. F. (1989).** Text-signaling devices and their effects on reading and memory processes. *Educational Psychology Review, 1*(3), 209–234. https://doi.org/10.1007/BF01320135 **[A]**
- *Used here:* §5.5 move 3, a review of text signals.

**Koornneef, A. (2024).** On the readability of texts presented in sentence-by-sentence segments to beginner readers: Evidence from self-paced reading and eye tracking. *Reading and Writing, 37*(1), 69–87. https://doi.org/10.1007/s11145-023-10423-5 **[A]**
- *What it shows:* presenting text in sentence segments raised comprehension, and the gain was not explained by wrap-up time.
- *Used here:* §5.5 move 1, as support that segmentation can help.

---

## 6. DISCUSSION: IMPLICATIONS AND FUTURE WORK (about 3,000 words)

**Job:** borrowed from C&D §5. Open with the ways the account extends prior accounts, then give implications by audience. Testing the account comes first. End on the strongest counterpoint, argued, in place of a limitations list.

**Opening paragraph.** The theory extends prior work in three ways (C&D list three extensions):
1. It moves the competence question from knowledge *about* algorithms (algorithmic literacy) to navigating *through* an opaque intermediary, beginning at the perceptual level.
2. It treats the stream's *structure*, meaning where its decision spaces fall, and not only its rate or content.
3. It separates seeing a decision space from navigating it, and makes that separation testable.

### 6.1 Testing the theory (C&D §5.1: "severe testing ... itself")

1. **State plainly that the predictions are untested.** Then give the test logic in one or two paragraphs:
   - three conditions: a continuous stream, arbitrary breaks, and breaks at decision units;
   - equal break counts in the two break conditions;
   - embedded errors;
   - gaze, detection and workload measured together;
   - pre-generated responses replayed at a fixed rate.

   **ROGER:** your experimental-design sentence and your "something other than segmentation" line.
2. **Measurement advice** (C&D §5.1.4). Pair gaze with outcomes, and mark regions of interest at decision loci.
3. **Moderators to manipulate** later: placement, pause length, marker form (Table 1 #7 and #10).
4. **Caveat in C&D's manner:** most of the evidence comes from static or experimenter-paced text. Only Park & Lee (2024) and Bhat (2025) study chatbot streaming, and only Park & Lee measured gaze.

### 6.2 Design implications: interfaces that mark decision spaces or hide them

**Framing sentence:** current chat interfaces hide decision spaces by default; designing them is a choice to mark them or not.

Four dimensions, each a trade-off ending in a principle:
1. **Placement:** mark decision spaces where they are, never where packets fall.
2. **Marker form:** **[NEEDS: your view]**.
3. **Pause length:** calibrate it, because too brief and too long both fail (Gould et al., 2016).
4. **Who triggers it:** the system places decision spaces and users may extend them. User-chosen transparency did not help (Tatasciore et al., 2026), and user autonomy is an open question in the microboundaries literature (Cox et al., 2016).

**Extension to agents:** Chen et al. (2026). Optional: once a pause prompts a correction, segment-level editing is one way to act on it (Zhou et al., 2026). Structure the output into units to support steering (Kazemitabaar et al., 2024).

### 6.3 Algorithmacy theory beyond the stream (C&D §5.3)

1. **ROGER:** literacy merged with oracy; literacy now merges with algorithmacy, including your "opacity of AI systems and the influence of other users" sentence.
2. **The perceptual layer is one layer.** Decision spaces also occur where no text streams:
   - ranking (who sees which seller);
   - dispatch (which driver gets which trip);
   - screening (which applicant is filtered out).

   In each, a judgment point is hidden in an opaque process. **[NEEDS: your dissertation cases]**
3. **Expert supervision of live visual streams.** Analysts watching video with an AI overlay learned the tool's "boundary conditions" (Lamb et al., 2026). That is algorithmacy acquired over time at a system's decision spaces.
4. **The structure of an exchange shapes what people do** (Najjar & Nasir, 2026, abstract only).
5. **Measuring algorithmacy.** Your posts claim the theory "generates predictions measurable by instrument." Predictions 11–12 in Table 1 need such a measure. **[NEEDS: your measure, or treat the predictions as an agenda]**

### 6.4 The strongest counterpoint: friction is disliked, and pauses may work only by slowing things down (C&D §5.4)

1. **State the counterpoint fairly:**
   - Users resist systems that ask them to reflect (Forshaw et al., 2026).
   - Users prefer and trust forcing functions less (Buçinca et al., 2021).
   - Preparatory friction did not reduce reliance (Arun et al., 2026).
   - Chunked text can slow reading (Keenan, 1984).
   - Any gain might come from the pause, not the placement.
2. **Answer it from the theory:**
   - Marking asks nothing of the user. It reveals a point already in the process, as a written space asks nothing of a reader.
   - Their benefit is predicted to exceed that of equally many arbitrary pauses (P2). If it does not, the theory is wrong about placement, and that result would itself be informative.
   - Forshaw et al. found that behaviour diverged from stated dislike.
3. **Say what the theory cannot answer yet:**
   - whether users will tolerate pauses in everyday use;
   - whether the effects hold for expert users;
   - whether decision units can be located reliably in real responses (§5.1).

### Section bibliography

Most sources are annotated in §§3–5. New to this section:

**Ridley, M., & Pawlick-Potts, D. (2021).** Algorithmic literacy and the role for libraries. *Information Technology and Libraries, 40*(2). https://doi.org/10.6017/ital.v40i2.12963 **[F pp. 1–4]**
- *What it shows:* defines algorithmic literacy as "the skill, expertise, and awareness" to understand, recognise, create, apply and assess algorithms, and to "position the individual as a co-constituent in algorithmic decision-making" (p. 3).
- *Used here:* §5.0 move 7, the contrast with algorithmacy.
- *Limits:* reading it as lacking a perceptual component is your interpretation.

**Najjar, M. S., & Nasir, M. (2026).** Dialogue patterns in human-AI co-creation: How interaction structure shapes output and process. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2717534 **[A]**
- *What it shows:* N = 244; iterative critique produced more task-appropriate creativity than AI-led proposals.
- *Used here:* §6.3 move 4.

**Zhou, H., Zhang, J., Lou, J., Liu, Y., Lu, C., Qu, J., & Li, J. (2026).** *Deep interaction: An efficient human-AI interaction method for large reasoning models* [Preprint]. arXiv:2607.14049. **[F method/evaluation][P]**
- *What it shows:* editing a completed chain of thought raised correction success by more than 25% and cut tokens by about 40%, mostly with simulated correctors.
- *Used here:* optional, in §6.2.

**Kazemitabaar, M., et al. (2024).** Improving steering and verification in AI-assisted data analysis with interactive task decomposition. In *Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology*. ACM. https://doi.org/10.1145/3654777.3676345 **[A]**
- *What it shows:* with n = 18, stepwise and phasewise decomposition made intervention, correction and verification easier than a conversational baseline.
- *Used here:* §6.2.
- *Limits:* complete the author list.

**Keenan, S. A. (1984).** Effects of chunking and line length on reading efficiency. *Visible Language*. **[A; volume and pages unverified]**
- *What it shows:* chunked text was read more slowly, which the author attributes to variable line length.
- *Used here:* §6.4, as counter-evidence.
- *Limits:* verify or drop.

---

## 7. CONCLUSION (about 300 words)

**Job:** borrowed from C&D §6.
1. Give the synthesis in two paragraphs: what the theory proposes, and what it explains in the puzzle from §1.
2. End on an inversion, as C&D do ("We have studied what players are looking at for a long time; task-attention theory may help us understand what they have been seeing"). One shape to adapt in your words: we have asked whether people can read what AI writes; algorithmacy asks whether they can see where it leaves them a decision.

**[NEEDS: your line.]** No new citations.

---

## Master reference list (APA 7)

Same as version 1, plus Endsley (2017) and the structural model (added in version 2), and Oberschelp (1995) and Stark & Vanden Broeck (2024) (added in version 3). Your Substack working papers are listed separately below the main list. Each entry's status code appears in the section bibliographies above. Entries marked † need completion before submission.

- Arun, S., et al. (2026). Encouraging thought before completion: The role of task-specific selective friction in AI-assisted knowledge work. In *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work*. ACM. https://doi.org/10.1145/3808045.3808049 †
- Bailey, B. P., & Konstan, J. A. (2006). On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state. *Computers in Human Behavior, 22*(4), 685–708. https://doi.org/10.1016/j.chb.2005.12.009
- Benedetto, S., Carbone, A., Pedrotti, M., Le Fevre, K., Bey, L. A. Y., & Baccino, T. (2015). Rapid serial visual presentation in reading: The case of Spritz. *Computers in Human Behavior, 45*, 352–358. https://doi.org/10.1016/j.chb.2014.12.043
- Bhat, M. (2025). How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131
- Booth, R. W., & Weger, U. W. (2013). The function of regressions in reading: Backward eye movements allow rereading. *Memory & Cognition, 41*(1), 82–97. https://doi.org/10.3758/s13421-012-0244-y
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287
- Cao, S., & Huang, C.-M. (2022). Understanding user reliance on AI in assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 6*(CSCW2), 1–23. https://doi.org/10.1145/3555572
- Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026). *Comparing human oversight strategies for computer-use agents* [Preprint]. arXiv. https://arxiv.org/abs/2604.04918
- Cho, J., & Lim, D. (2026). How source attribution visualization shapes user attention and preference: An eye-tracking study of four AI chatbot layouts. *Journal of Eye Movement Research, 19*(4), Article 89. https://doi.org/10.3390/jemr19040089
- Collins, K. M., et al. (2024). *Modulating language model experiences through frictions* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2407.12804 †
- Cox, A. L., Gould, S. J. J., Cecchinato, M. E., Iacovides, I., & Renfree, I. (2016). Design frictions for mindful interactions: The case for microboundaries. In *Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems* (pp. 1389–1397). ACM. https://doi.org/10.1145/2851581.2892410
- Cutting, J., & Deterding, S. (2022). The task-attention theory of game learning: A theory and research agenda. *Human–Computer Interaction, 39*(5–6), 257–287. https://doi.org/10.1080/07370024.2022.2047971 *(structural model; cite only if you mention it)*
- Delgado, P., Vargas, C., Ackerman, R., & Salmerón, L. (2018). Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. *Educational Research Review, 25*, 23–38. https://doi.org/10.1016/j.edurev.2018.09.003
- Disley, M., & Khan, M. (2026). Designing cognitive friction with concept suppression in large language models. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2708617
- Drieghe, D., Fitzsimmons, G., & Liversedge, S. P. (2017). Parafoveal preview effects in reading unspaced text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(10), 1701–1716. https://doi.org/10.1037/xhp0000441
- Endsley, M. R. (2017). From here to autonomy. *Human Factors, 59*(1), 5–27. https://doi.org/10.1177/0018720816681350
- Forshaw, T., Hale, J., & Longmire, M. (2026). The Reflection Penalty: When managers accept leadership coaching from a human but not an AI agent. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2744236
- Gegoff, I., Tatasciore, M., Bowden, V. K., & Loft, S. (2025). Deciphering automation transparency: Do the benefits of transparency differ based on whether decision recommendations are provided? *Human Factors, 67*(8), 776–794. https://doi.org/10.1177/00187208251318465
- Ghosh, A., Sarkar, A., Lindley, S., & Poelitz, C. (2026). *An experimental comparison of cognitive forcing functions for execution plans in AI-assisted writing: Effects on trust, overreliance, and perceived critical thinking* [Preprint]. arXiv. https://arxiv.org/abs/2601.18033
- Gibson, J. J. (1979). *The ecological approach to visual perception*. Houghton Mifflin.
- Gould, S. J. J., Cox, A. L., Brumby, D. P., & Wickersham, A. (2016). Now check your input: Brief task lockouts encourage checking, longer lockouts encourage task switching. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 3311–3323). ACM. https://doi.org/10.1145/2858036.2858067
- Harvey, H., Godwin, H. J., Fitzsimmons, G., Liversedge, S. P., & Walker, R. (2017). Oculomotor and linguistic processing effects in reading dynamic horizontally scrolling text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(3), 518–536. https://doi.org/10.1037/xhp0000329
- Harvey, H., & Walker, R. (2018). Reading comprehension and its relationship with working memory capacity when reading horizontally scrolling text. *Quarterly Journal of Experimental Psychology, 71*(9), 1887–1897. https://doi.org/10.1080/17470218.2017.1363258
- Haverkamp, Y. E., Bråten, I., Latini, N., & Salmerón, L. (2023). Is it the size, the movement, or both? Investigating effects of screen size and text movement on processing, understanding, and motivation when students read informational text. *Reading and Writing, 36*(7), 1589–1608. https://doi.org/10.1007/s11145-022-10328-9
- Hyönä, J., & Lorch, R. F. (2004). Effects of topic headings on text processing: Evidence from adult readers' eye fixation patterns. *Learning and Instruction, 14*(2), 131–152. https://doi.org/10.1016/j.learninstruc.2004.01.001
- Kazemitabaar, M., et al. (2024). Improving steering and verification in AI-assisted data analysis with interactive task decomposition. In *Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology*. ACM. https://doi.org/10.1145/3654777.3676345 †
- Keenan, S. A. (1984). Effects of chunking and line length on reading efficiency. *Visible Language*. †
- Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025). Fostering appropriate reliance on large language models: The role of explanations, sources, and inconsistencies. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–19). ACM. https://doi.org/10.1145/3706598.3714020
- Knox, B. M. W. (1968). Silent reading in antiquity. *Greek, Roman and Byzantine Studies, 9*(4), 421–435.
- Koornneef, A. (2024). On the readability of texts presented in sentence-by-sentence segments to beginner readers: Evidence from self-paced reading and eye tracking. *Reading and Writing, 37*(1), 69–87. https://doi.org/10.1007/s11145-023-10423-5
- Kumar, M., Goldstein, A., Michelmann, S., Zacks, J. M., Hasson, U., & Norman, K. A. (2023). Bayesian surprise predicts human event segmentation in story listening. *Cognitive Science, 47*(10), e13343. https://doi.org/10.1111/cogs.13343
- Kurby, C. A., & Zacks, J. M. (2008). Segmentation in the perception and memory of events. *Trends in Cognitive Sciences, 12*(2), 72–79. https://doi.org/10.1016/j.tics.2007.11.004
- Kurby, C. A., & Zacks, J. M. (2012). Starting from scratch and building brick by brick in comprehension. *Memory & Cognition, 40*(5), 812–826. https://doi.org/10.3758/s13421-011-0179-8
- Lamb, S. C., Byrne, M., Norman, T. J., Ramchurn, S. D., & Naiseh, M. (2026). What's informing trust and adoption? Can current cognitive models support expert adoption of AI? *Journal of Cognitive Engineering and Decision Making, 20*(2), 158–175. https://doi.org/10.1177/15553434261430550
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392
- Liu, C., Zhou, Q., Shen, X., Liu, X. B., Wu, T., & Chen, X. A. (2026). Behavioral indicators of overreliance during interaction with conversational language models. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–23). ACM. https://doi.org/10.1145/3772318.3790332
- Liu, J., Chung, J.-W., Wu, Z., Lai, F., Lee, M., & Chowdhury, M. (2024). *Andes: Defining and enhancing quality-of-experience in LLM-based text streaming services* [Preprint]. arXiv. https://arxiv.org/abs/2404.16283
- Lorch, R. F. (1989). Text-signaling devices and their effects on reading and memory processes. *Educational Psychology Review, 1*(3), 209–234. https://doi.org/10.1007/BF01320135
- Mangen, A., Olivier, G., & Velay, J.-L. (2019). Comparing comprehension of a long text read in print book and on Kindle: Where in the text and when in the story? *Frontiers in Psychology, 10*, Article 38. https://doi.org/10.3389/fpsyg.2019.00038
- Mangen, A., Walgermo, B. R., & Brønnick, K. (2013). Reading linear texts on paper versus computer screen: Effects on reading comprehension. *International Journal of Educational Research, 58*, 61–68. https://doi.org/10.1016/j.ijer.2012.12.002
- McDonald, S. A. (2006). Parafoveal preview benefit in reading is only obtained from the saccade goal. *Vision Research, 46*(26), 4416–4424. https://doi.org/10.1016/j.visres.2006.08.027
- Metzner, P., von der Malsburg, T., Vasishth, S., & Rösler, F. (2017). The importance of reading naturally: Evidence from combined recordings of eye movements and electric brain potentials. *Cognitive Science, 41*(S6), 1232–1263. https://doi.org/10.1111/cogs.12384
- Najjar, M. S., & Nasir, M. (2026). Dialogue patterns in human-AI co-creation: How interaction structure shapes output and process. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2717534
- Oberschelp, W. (1995). Developing analytical competency through informatics teaching. In *Integrating Information Technology into Education* (IFIP Advances in Information and Communication Technology, pp. 115–126). Springer US. https://doi.org/10.1007/978-0-387-34842-1_12 [M; read before citing]
- O'Regan, J. K. (2011). *Why red doesn't sound like a bell: Understanding the feel of consciousness*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199775224.001.0001
- O'Regan, J. K., & Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973. https://doi.org/10.1017/S0140525X01000115
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055
- Park, H., & Lee, Y. (2024). The effect of text movement on eye movements in generative AI chatbots. *Archives of Design Research, 37*(4), 181–197. https://doi.org/10.15187/adr.2024.08.37.4.181
- Parkes, M. B. (1992). *Pause and effect: An introduction to the history of punctuation in the West*. Scolar Press. †edition
- Powers, S. A., & Scerbo, M. W. (2023). Examining the effect of interruptions at different breakpoints and frequencies within a task. *Human Factors, 65*(1), 22–36. https://doi.org/10.1177/00187208211009010
- Prajod, P., Cools, H., Röggla, T., Cesar, P., & El Ali, A. (2026). *Towards gaze-informed AI disclosure interfaces: Eye-tracking attentional and cognitive load while reading AI-assisted news* [Preprint]. arXiv. https://arxiv.org/abs/2605.14999
- Rayner, K., Fischer, M. H., & Pollatsek, A. (1998). Unspaced text interferes with both word identification and eye movement control. *Vision Research, 38*(8), 1129–1144. https://doi.org/10.1016/S0042-6989(97)00274-5
- Resulbegoviq, H., Hlebec, V., Pejić Bach, M., & Stamatović, I. (2026). Eye tracking and AI-generated content: A systematic literature review of visual attention, cognitive processing, and user engagement. *Journal of Eye Movement Research, 19*(5), Article 97. https://doi.org/10.3390/jemr19050097
- Ridley, M., & Pawlick-Potts, D. (2021). Algorithmic literacy and the role for libraries. *Information Technology and Libraries, 40*(2). https://doi.org/10.6017/ital.v40i2.12963
- Saenger, P. (1997). *Space between words: The origins of silent reading*. Stanford University Press. https://doi.org/10.1515/9781503619081
- Schotter, E. R., Tran, R., & Rayner, K. (2014). Don't believe what you read (only once): Comprehension is supported by regressions during reading. *Psychological Science, 25*(6), 1218–1226. https://doi.org/10.1177/0956797614531148
- Sharmin, S., Špakov, O., & Räihä, K.-J. (2015). Dynamic text presentation in print interpreting – An eye movement study of reading behaviour. *International Journal of Human-Computer Studies, 78*, 17–30. https://doi.org/10.1016/j.ijhcs.2015.01.010
- Sharmin, S., et al. (2016). The reading process of dynamic text – A linguistic approach to an eye movement study. *SKY Journal of Linguistics, 29*. †
- Stark, D., & Vanden Broeck, P. (2024). Principles of algorithmic management. *Organization Theory, 5*(2). https://doi.org/10.1177/26317877241257213
- Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X., Mayer, L. W., & Smyth, P. (2025). What large language models know and what people think they know. *Nature Machine Intelligence, 7*(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7
- Tatasciore, M., Bennett, L., Bowden, V. K., Bell, J., Visser, T. A. W., McAnally, K., McCarley, J. S., Thompson, M. B., Shanahan, C., Morris, R., & Loft, S. (2026). Adaptable automation transparency: Should humans be provided flexibility to self-select transparency information? *Human Factors, 68*(1), 5–27. https://doi.org/10.1177/00187208251349269
- Timkey, W., Huang, K.-J., Oh, B.-D., Prasad, G., Arehalli, S., Linzen, T., & Dillon, B. (2026). Eye movements reveal a dissociation between prediction and structural processing difficulty in language comprehension. *Proceedings of the National Academy of Sciences, 123*(32), e2532230123. https://doi.org/10.1073/pnas.2532230123
- Tsoukala, A., Vogelzang, M., & Tsimpli, I. M. (2025). The influence of text segmentation on garden path processing: Evidence from self-paced reading and eye-tracking. *Language and Cognition, 17*, e58. https://doi.org/10.1017/langcog.2025.10009
- Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review, 28*(4), 1060–1092. https://doi.org/10.3758/s13423-020-01859-9
- Wu, Z., Wang, Y., Langer, M., & Feit, A. M. (2025). RelEYEance: Gaze-based assessment of users' AI-reliance at run-time. *Proceedings of the ACM on Human-Computer Interaction, 9*(3), 1–18. https://doi.org/10.1145/3725841
- Xiao, C., & Yang, B. Z. (2025). Streaming, fast and slow: Cognitive load-aware streaming for efficient LLM serving. In *Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology* (pp. 1–13). ACM. https://doi.org/10.1145/3746059.3747721
- Yang, Y., Lee, Y. M., Tabone, W., García de Pedro, J., Happee, R., & Merat, N. (2027). The effect of augmented reality on pedestrians' gaze patterns and crossing probability while interacting with automated vehicles. *International Journal of Human-Computer Studies, 217*, Article 103920. https://doi.org/10.1016/j.ijhcs.2026.103920
- Yantis, S., & Jonides, J. (1984). Abrupt visual onsets and selective attention: Evidence from visual search. *Journal of Experimental Psychology: Human Perception and Performance, 10*(5), 601–621. https://doi.org/10.1037/0096-1523.10.5.601
- Zacks, J. M., Speer, N. K., & Reynolds, J. R. (2009). Segmentation in reading and film comprehension. *Journal of Experimental Psychology: General, 138*(2), 307–327. https://doi.org/10.1037/a0015305
- Zacks, J. M., Speer, N. K., Swallow, K. M., Braver, T. S., & Reynolds, J. R. (2007). Event perception: A mind-brain perspective. *Psychological Bulletin, 133*(2), 273–293. https://doi.org/10.1037/0033-2909.133.2.273
- Zhou, H., Zhang, J., Lou, J., Liu, Y., Lu, C., Qu, J., & Li, J. (2026). *Deep interaction: An efficient human-AI interaction method for large reasoning models* [Preprint]. arXiv. https://arxiv.org/abs/2607.14049
- Zhu, H., Wang, J., Xie, L., Ma, R., Sun, Y., Liu, F., Zheng, C., & Li, Q. (2026). Just-in-time tokens: Adaptive token pacing for cognitive-friendly LLM streaming. In *Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–8). ACM. https://doi.org/10.1145/3772363.3798936
- Zhu, X., Le Truong, K., Fogliato, R., Swamy, G., Zhang, W., Yang, M., Ye, L., Liu, B., Liu, M., Ilyas, A., & Wu, Z. S. (2026). *Justified or just convincing? Error verifiability as a dimension of LLM quality* [Preprint]. arXiv. https://arxiv.org/abs/2604.04418

**Count:** 72 cited sources (33 [F], 30 [A], 9 [M]; 7 are preprints), plus the structural model and your two working papers.

**Your working papers (cite only if you choose to; §5.0 move 1):**
- Hunt, R. (n.d.). *Algorithmacy and the co-optation of the subject* (v22) [Substack post]. https://rogerhuntphdcand.substack.com/p/algorithmacy-and-the-co-optation-a81 †date
- Hunt, R. (n.d.). *Cognitive science implications of algorithmacy* [Substack post]. https://rogerhuntphdcand.substack.com/p/cognitive-science-implications-of †date

---

## Decisions that remain yours

Resolved on 20 October (my judgement, at your instruction): the [Claim] wording; the fluency tension (§5.5 move 4); the term collision (§5.0 move 4); and the definition (§5.0 move 1). Reverse any of them freely.

Still yours:
1. **The rule for locating decision spaces (§5.1).** This remains the paper's central contribution.
2. **Oberschelp (1995):** read the chapter (marked free to read), then position your use of the word against it (§5.0 move 6).
3. **Figure 1 and Table 1:** accept, cut or rewrite. Predictions 11–12 need a measure of algorithmacy, or they become research agenda.
4. **The numbered points in §1 move 6.**
5. **Whether to adopt Parkes's frame (§2).**
6. **Mark form (§6.2).**
7. **Abstract, roadmap and conclusion inversion,** in your words.
8. **Flags F1 and F3–F17** in `abstract_intro_edit.md`.
9. **The six † references.**
