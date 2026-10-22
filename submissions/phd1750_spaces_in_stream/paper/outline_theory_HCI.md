# Spaces in the Stream: How People See AI — Theory-Paper Outline for *Human–Computer Interaction*

> **Drafted by Claude (Opus 5.5) for Roger Hunt, 20 October 2026.** This replaces `outline.md` for the
> journal version. It is a map of moves, not prose. **ROGER** marks text you have already written and
> where it fits. **[NEEDS]** marks a decision or material only you can supply. The class-paper outline
> stays in `outline.md` unchanged.

## What changes when the study becomes theory

*HCI* welcomes "theoretical papers, 'framework' papers, review papers, and even essays," but expects "a rigorous analysis developing new conceptual views ... that imply future research directions." It also requires "scientific implications, system design implications, and analyses of how systems are actually used" (journal aims, T&F PDF). It is "not interested in ... papers reporting only preliminary results."

So the paper's contribution becomes three things:
1. **A construct.** Streaming AI output as unsegmented text, and decision spaces as its fix.
2. **Falsifiable propositions** derived from four literatures.
3. **A design space** for building decision spaces into interfaces.

The three-condition study shrinks from a methods section to one paragraph that states the test logic. N = 42 and its power problem (flag F2) drop out.

**Consequences for your current abstract and intro** (`abstract_intro_edit.md`). These sentences are yours to rewrite; I have not changed them:
- **Abstract:** "To evaluate this intervention, I present a three-condition eye-tracking protocol (N = 42)..." now describes a study the paper no longer reports. The abstract needs to say what the paper contributes as theory.
- **[Course] paragraph:** "this paper specifies an empirical eye-tracking study (N = 42)..." needs the same change. The RQs become propositions (see §5 below).
- **Roadmap:** "Section 5 details the experimental methodology and statistical model; Section 6 analyzes possible empirical outcomes" needs to match the new sections.

**Length (checked 2026-10-20):** none of *HCI*'s three official documents sets a word limit: the aims PDF, the instructions to authors and the final-submission style guide. The last two are old; they name Thomas Moran as editor and cite APA 4th edition. The live author page sits behind a bot check. The journal "favors substantial papers," and the guide asks the abstract to state "the nature of the paper (theoretical, empirical, or methodological)." For scale, the 2026 *HCI* papers in your debate set run 26 pages (Forshaw et al.), 31 pages (Najjar & Nasir) and 42 pages (Disley & Khan) in typeset form. The style guide also requires numbered all-caps first-level headings and a table of contents. Those apply at final submission, not at review.

---

## Section plan

### Abstract (~200 words)
Moves, in order:
1. People now supervise AI text while it forms.
2. Reading depends on stable text, word-level and sense-level boundaries, and look-backs; streams remove the last two.
3. The paper argues, from the history of word spacing, that streamed output is a new scriptio continua.
4. It defines decision spaces and derives propositions.
5. It maps the design space.
6. What follows for algorithmacy.

**[NEEDS: your sentences; check *HCI*'s abstract rules.]**

### 1. Introduction (~1,200 words)
Keep your [Context], [Complication], [Consequence] and [Claim] paragraphs, with the flagged facts fixed as you decide (F1–F17). Then:
- **[Course] rewritten as the contribution statement.** Use three numbered contributions, matching *HCI*'s request for scientific implications, design implications and how systems are used:
  - **C1** (theoretical): the scriptio continua account of streaming output.
  - **C2** (conceptual): decision spaces, with three functions and falsifiable propositions.
  - **C3** (design): the design space and its trade-offs.
- **Gap sentence, kept to what was searched:** "I found no study ... that segments a streaming LLM response at decision units and measures fixations, regressions and error detection against continuous and arbitrarily interrupted streams." I reran the search on 2026-10-20 in arXiv, Consensus and web search (`search-log.md` rows 51–55), and it still holds. For a theory paper, the claim can be broader: "I found no work that places interface friction inside a streamed AI response; existing friction designs act before or around access to the model (Collins et al., 2024; Arun et al., 2026; Cox et al., 2016)." **[Rerun just before submission.]**
- **Term check:** "decision spaces" appears on arXiv only in unrelated senses (network optimisation, BCI, organisational rules). Define the term at first use.
- **ROGER:** the algorithmacy sentence and the roadmap.

### 2. Streaming output as a new scriptio continua (~1,500 words)
The historical argument carries the theory.
- **2.1 What word spacing did.** **ROGER:** your Saenger/Parkes paragraph. **[flag F17: Saenger and Parkes still unread; page locators needed.]**
- **2.2 What the space does for the eye.** Rayner et al. (1998), read in full:
  - reading rate fell 54% and 44% without spaces;
  - regressions rose from 9.7% to 17.3%;
  - landing positions shifted to the start of words;
  - spaces aid both word identification and eye guidance (pp. 1132–1143).
  - Drieghe et al. (2017) replicate the slowing.
- **2.3 The objection: chatbots already print spaces.** **[NEEDS: state it in your words.]**
- **2.4 The answer: a second layer of legibility, above the word.** Parkes's "grammar of legibility" (ch. 3 title verified; contents unread). **[NEEDS: decide whether to adopt this frame; read ch. 3 if so.]**
- **2.5 What streams supply and remove.** Word spaces remain. Stable position and units-of-sense boundaries are gone. **ROGER:** "Alternatively, is the current experience of interacting with AI already optimal?"

### 3. Three mechanisms streaming disrupts (~2,500 words)
This is your literature review recast as mechanism, not coverage. Each subsection ends with the property of streams that it implicates.
- **3.1 Looking back.**
  - Regressions repair comprehension: Schotter et al. (2014), read in full, N = 40, trailing mask, b = −0.92; Booth & Weger (2013); Timkey et al. (2026).
  - Moving and scrolling text costs integration and backtracking: Harvey et al. (2017); Harvey & Walker (2018); Haverkamp et al. (2023), reader-controlled scrolling.
  - Text still forming changes rereading: Sharmin et al. (2015, 2016).
  - Park & Lee (2024) is the one study of chatbot text movement itself.
- **3.2 Being pulled forward.**
  - Abrupt onsets: Yantis & Jonides (1984), with their limit of a single onset (p. 617).
  - Salience is short-lived and the priority map can reset after "a break in the action" (Wolfe, 2021, p. 1069).
  - Pacing is set by compute: Liu et al. (2024); Xiao & Yang (2025), described as their measures actually were (F4–F6).
- **3.3 Segmenting into events.**
  - Event Segmentation Theory: Zacks et al. (2007, 2009).
  - Boundaries trigger updating: Kurby & Zacks (2012).
  - Where breaks fall matters: Tsoukala et al. (2025); Bailey & Konstan (2006); Powers & Scerbo (2023), abstract only.
- **3.4 Supervising fluent automation.**
  - Parasuraman & Manzey (2010), with F15 fixed.
  - Recommendations reduce scrutiny: Gegoff et al. (2025), effect small, .93 vs .94.
  - Explanations raise reliance: Kim et al. (2025).
  - Streaming raises perceived competence and trust but not perceived effectiveness: Bhat (2025).
  - Process markers of overreliance: Liu et al. (2026); Cho & Lim (2026).
- **3.5 Perception as action.** Gibson (1979) and O'Regan & Noë (2001). **ROGER:** your sentences. **[flag F11: not read.]**

### 4. Decision spaces (~1,500 words)
- **4.1 The theory.** **ROGER:** "I theorize that observing AI in operation today is analogous to reading scriptura continua..."
- **4.2 Definition.** **ROGER:** the decision-spaces sentence. **[NEEDS: the operational rule for locating a decision unit.]** For a theory paper this rule *is* the contribution, so it must be stated precisely. Candidates:
  - the end of a checkable claim;
  - a change of goal or cause (Zacks et al., 2009);
  - a point where the user could accept, reject or redirect.
- **4.3 Three functions, each tied to its mechanism in §3.** **ROGER:** "1) providing a visual target; 2) establishing event boundaries; and 3) facilitating efficient regression." Map them as 1 → §3.2, 2 → §3.3, 3 → §3.1.
- **4.4 Positioning against neighbouring constructs.** This is where the debate papers go:
  - *Cognitive forcing functions:* Buçinca et al. (2021), a delay alone.
  - *Microboundaries:* Cox et al. (2016), read in full. Their definition: "an intervention that provides a small obstacle prior to an interaction," a short time cost that moves the user from automatic to deliberate processing. Decision spaces differ in two ways. They sit inside the system's output rather than before the user's action, and they work through perception rather than a time cost alone. Cox et al. list "the level of autonomy a user has over the introduction of the microboundary" as future work, which links to Tatasciore et al.
  - *Lockout length:* Gould, Cox, Brumby & Wickersham (2016, CHI, abstract only). Brief lockouts encouraged checking; longer lockouts induced task switching, so duration "needs to be carefully calibrated." This feeds the pause-length dimension in §6.
  - *Friction around LLM access* (abstracts only): Collins et al. (2024, arXiv), "selective frictions" before model access reduced click-through; Arun et al. (2026, CHIWORK), preparatory friction (N = 40) raised mental demand but did not reduce self-reported reliance. Both place friction before or around access. None places it inside the streamed response.
  - *Representational friction:* Disley & Khan (2026), friction inside the model rather than at the interface. They call for interface-level comparisons (§7.9).
  - *Adaptable transparency:* Tatasciore et al. (2026). User-chosen information did not help, so the system places decision spaces.
  - What makes decision spaces distinct: they are perceptual, they are placed by event structure, and they ask nothing of the user. That last point is a possible answer to Forshaw et al.'s (2026) reflection penalty.

### 5. Propositions (~1,200 words)
These replace the methods section. Your RQs become falsifiable propositions, each with the result that would count against it. **[NEEDS: accept or rewrite.]**
- **P1 (targeting and regression)**, from RQ1. Breaks at decision units draw fixations and regressions to those points more than equally many arbitrary breaks.
  - *Against it:* no difference in regressions to break loci.
- **P2 (detection)**, from RQ2. Decision-unit breaks improve detection of embedded errors over continuous and arbitrarily broken streams.
  - *Against it:* detection equal to arbitrary breaks. That would mean pausing, not segmentation, does the work. **ROGER:** "If arbitrary breaks yield similar improvements, the benefit may be attributed to something rather than segmentation" ["other than"?].
- **P3 (cost)**, from RQ3. Arbitrary breaks cost detection latency, workload or refixations relative to a continuous stream (Tsoukala et al., 2025; Bailey & Konstan, 2006).
- **P4 (gaze is not verification)**, new. Gaze changes without detection changes would show attention moving without judgment. Sources: Parasuraman & Manzey (2010); Yang et al. (2026), who name gaze-only evaluation as a limitation; Cho & Lim (2026).
- **The test that separates them.** One paragraph: three conditions, equal break counts, embedded errors, gaze plus detection. **ROGER:** your experimental-design sentence. Say that the study is future work, not reported here.

### 6. A design space for decision spaces (~1,200 words)
*HCI* expects design implications. Four dimensions, each stated as a trade-off with its evidence:
1. **Placement rule:** decision unit vs time vs length (§4.2; Tsoukala et al.).
2. **Marker form:** blank space, rule, label or prompt (Prajod et al., 2026, preprint: terse labels raised fixations). **[NEEDS: your view.]**
3. **Pause length and pacing:** Xiao & Yang (2025) on comfortable speed; Buçinca et al. (2021) on waits.
4. **Who triggers it:** system or user (Tatasciore et al., 2026: user selection did not help, and high transparency was chosen on about 41% of missions).

Optional extension: agents and computer-use systems (Chen et al., 2026, preprint: 56% of failures from mistimed judgment).

### 7. Algorithmacy (~1,000 words)
- **7.1** **ROGER:** literacy merged with oracy; literacy now merges with algorithmacy.
- **7.2** Algorithmic literacy describes knowledge; algorithmacy adds a perceptual skill (Ridley & Pawlick-Potts, 2021).
- **7.3** Trust learned at the system's edges. Lamb et al. (2026), read in full: analysts watching live video with an AI overlay said they needed to learn its "boundary conditions." Seven of nine stopped seeing it as an advisor.
- **7.4** Organizational and cooptive contexts. **[NEEDS: your dissertation material.]**

### 8. Limits of the argument (~500 words)
Each limit should say what it does to the claim:
- **The analogy has limits.** Medieval readers controlled their own pace; stream readers do not. Say where the analogy breaks.
- **The evidence is indirect.** Most of it comes from static or experimenter-moved text; only Park & Lee (2024) and Bhat (2025) study chatbot streaming.
- **Interfaces change fast.** Token rates and layouts will date.

### 9. Conclusion (~300 words)
End on the most specific design consequence, in your register.

---

## Decisions only you can make
1. The operational rule for a decision unit (§4.2). This matters most now.
2. Whether to adopt Parkes's frame, and whether to read ch. 3.
3. Accept or rewrite P1–P4.
4. Your view on marker form (§6).
5. Rewrite the abstract's study sentence, the [Course] paragraph and the roadmap.
6. The flagged facts F1–F17 in `abstract_intro_edit.md`. F2 (N = 42) no longer applies.
7. Done 2026-10-20: *HCI* limits checked (none stated), gap search rerun (holds), Cox et al. (2016) read.
8. Deferred by Roger (not available): Saenger, Parkes, Gibson, O'Regan & Noë, and the abstract-only debate papers. Keep their flags in place until full texts are in hand.
