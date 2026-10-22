# Spaces in the Stream: How People See AI — Full-Paper Outline

> **Drafted by Claude (Opus 5.5) for Roger Hunt, 20 October 2026.** This is a paragraph-by-paragraph map,
> not prose. Lines marked **ROGER** quote your proposal verbatim and show where your sentences already fit.
> **Anchors** list the verified source and number each paragraph can rest on (details and locators in
> `literature_review.md` and `../notes/`). **[NEEDS: …]** marks a decision or material only you can supply.
> Your writing-prose skill records that Claude's sentences cannot be made to read as yours, so the plan is
> for you to write the sentences into this frame.

**Register:** empirical human-factors / HCI journal article (IJHCS / *Human Factors*), APA 7, first person
for your own moves. **Length assumed:** ~7,000 words plus references. **[NEEDS: the assignment's actual
length and required sections — the budgets below scale.]**

**One fact to decide on before drafting:** your proposal's last line reads "If arbitrary breaks yield
similar improvements, the benefit may be attributed to something rather than segmentation." I read
"something rather than" as a slip for "something other than" — your call.

---

## Front matter

- **Title:** Spaces in the Stream: How People See AI (keep).
- **Abstract (≤ 200 words), five moves:** (1) the phenomenon — people supervise AI text as it streams;
  (2) the tension — reading depends on spaces, stable text and look-backs, and streams remove the last two;
  (3) what the paper does — traces the scriptura continua analogy, synthesises four literatures, proposes
  decision spaces; (4) the study — three-condition eye-tracking design with seeded errors; (5) what it
  would show and why it matters for algorithmacy.

## 1. Introduction (~700 words)

| ¶ | Claim / job | Anchors | Your text |
|---|---|---|---|
| 1.1 | Watching a chatbot answer is reading a text that is still being written | Park & Lee (2024): bottom-generated text raised fixations, total fixation time, saccade amplitude; fixation starts clustered where new words appeared | **ROGER:** "When users watch a chatbot responding to a query/prompt, their eyes track the text as it appears. Words stream incrementally, expanding and scrolling, forcing the user to track the text as if following an automated cursor." |
| 1.2 | The stream is paced by the server, not the reader | Liu et al. (2024): average reading consumption 4.8 tokens/s; one server delivered 11.2 tokens/s; Xiao & Yang (2025): 99% comfortable ≤ 21.2 wps (easy) / 12.0 wps (hard) vs ~45 wps API | [NEEDS: your sentence] |
| 1.3 | The research question: perception and action | — | **ROGER:** "I propose to examine this phenomenon as an issue of perception and action: specifically, how users visually process AI-generated output in real time and how this influences subsequent behaviors, such as accepting, disregarding, rereading, consulting sources, or intervening to redirect the AI." |
| 1.4 | Why it matters: fluent output suppresses checking | Kim et al. (2025): explanations raised agreement with wrong answers; Bhat (2025): streamed display rated more trustworthy | [NEEDS: your sentence] |
| 1.5 | Research questions (numbered, each tied to a measure) | — | Draft RQs for you to accept or rewrite: **RQ1** Do breaks placed at decision units draw fixations and regressions to those points more than breaks placed at arbitrary intervals? (fixation and regression counts at break loci) **RQ2** Do decision-unit breaks improve detection of seeded errors relative to a continuous stream and to arbitrary breaks? (hit and false-alarm rates) **RQ3** Do arbitrary breaks cost anything relative to a continuous stream? (detection, workload, local refixations) |
| 1.6 | Link to the dissertation; roadmap in one sentence | — | **ROGER:** "This question sits at the center of my dissertation, which examines how individuals navigate opaque and cooptive environments, a phenomenon I call algorithmacy." |

## 2. From word spaces to a grammar of legibility (~800 words)

| ¶ | Claim / job | Anchors | Your text |
|---|---|---|---|
| 2.1 | Unspaced text forced readers to read aloud; spacing changed visual word finding | Saenger (1997) **[flag: not read this session]**; your earlier scriptio continua passage (dissertation) | **ROGER:** "As literacy expanded, Latin texts were originally composed in scriptura continua, with letters joined together and no spaces between words, forcing "readers" in many cases to either understand how to read in verse or listen to someone read aloud. Paul Saenger (1997) documents how Irish and English scribes began separating words in the seventh and eighth centuries, a practice that later spread to Continental scriptoria. Introducing spacing altered the visual processing required to identify words." |
| 2.2 | Eye-movement evidence for what the space does | Rayner, Fischer & Pollatsek (1998) **[flag: "about half" unchecked]**; Drieghe et al. (2017) replicate the slowing and find processing narrowly focused on one word when spaces allow; McDonald (2006): preview only from the saccade goal | adapt your "Eye movements and reading" paragraph |
| 2.3 | The objection: chatbots already print spaces | — | [NEEDS: your sentence — state the objection plainly] |
| 2.4 | The answer: a second layer, the grammar of legibility | Parkes (1992), ch. 3 "Grammar of Legibility" **[flag: read the chapter before relying on it]** | [NEEDS: your decision to adopt this frame] |
| 2.5 | What streams supply and remove: word spaces yes; unit-of-sense boundaries no | synthesis | **ROGER:** "This raises the question: what analogous structural element could transform our experience of AI-generated text? Alternatively, is the current experience of interacting with AI already optimal?" |

## 3. Course concepts as framework (~2,000 words; your three proposal headings)

### 3.1 Eye movements and reading (~800)

| ¶ | Claim | Anchors |
|---|---|---|
| 3.1.1 | Moving text spares word recognition and costs integration | Harvey et al. (2017): fewer, longer fixations; no early predictability benefit; Harvey & Walker (2018): inference suffers, returning harder |
| 3.1.2 | Readers track drifting text with pursuit plus saccades | Valsecchi et al. (2013) |
| 3.1.3 | Text that is still forming changes where readers look back | Sharmin et al. (2015): word-by-word > letter-by-letter rereading and regressions (N = 20); Sharmin et al. (2016): 90.8% of regression landings on content words vs 57.1% base rate |
| 3.1.4 | Regressions exist to reread and repair | **ROGER:** "Schotter, Tran, and Rayner (2014) found that masking each word after it was read, thereby preventing regressions, led to decreased comprehension."; Booth & Weger (2013); Timkey et al. (2026): rereading cost of disambiguation not explained by surprisal (n = 368) |
| 3.1.5 | Streaming threatens the regression window | **ROGER:** "In the context of streaming AI, auto-scrolling interfaces may move previous lines beyond the regression window, requiring users to choose between scrolling up to review or continuing to follow new text."; Haverkamp et al. (2023): scrolling → fewer backtracks (2.49 vs 3.53) |

### 3.2 Attention, motion and events (~700)

| ¶ | Claim | Anchors |
|---|---|---|
| 3.2.1 | New tokens are abrupt onsets that pull the eyes forward | Yantis & Jonides (1984); **ROGER:** Wolfe (2021) priority-map sentence; **ROGER:** Park & Lee sentence |
| 3.2.2 | Readers segment text into events and slow at boundaries | **ROGER:** Zacks et al. (2007) sentence; Zacks, Speer & Reynolds (2009): ~108 ms per 10% boundary agreement; software-paced clause stream still segmented |
| 3.2.3 | Boundaries trigger global updating | Kurby & Zacks (2012): goals mentioned more at fine boundaries without change (OR = 2.29); Kumar et al. (2023): boundaries track GPT-2 Bayesian surprise |
| 3.2.4 | Where a break falls matters more than whether it falls | Tsoukala et al. (2025): aligned vs scissored line breaks (d = 0.32 / 0.41; OR = 0.38); Bailey & Konstan (2006); Powers & Scerbo (2023): coarse breakpoints ≈ no interruption |
| 3.2.5 | An agent's work is continuous activity; judgment must land at the right moment | **ROGER:** "An AI agent's operation constitutes such continuous activity, compelling users to decide whether to review previous content or continue processing new information."; Chen et al. (2026, preprint): 29 of 138 problematic actions blocked; 56% of failures from mistimed judgment |

### 3.3 Perception and action (~500)

| ¶ | Claim | Anchors |
|---|---|---|
| 3.3.1 | Seeing as mastery of movement–sensation laws | **ROGER:** Gibson (1979) and O'Regan (2011) sentences; O'Regan & Noë (2001) |
| 3.3.2 | Fixed text gives readers placeholders; streams remove them | Mangen et al. (2019): print readers better on chronology, t(48) = 2.03; Mangen et al. (2013); Delgado et al. (2018) via Mangen: paper advantage stronger under time constraint |
| 3.3.3 | Supervising fluent automation: attention, complacency, looking without seeing | **ROGER (revise per flag):** "Parasuraman and Manzey (2010) attribute automation complacency and bias to operators' attention span" → source says *attention* under multitask load; looking-but-not-seeing (p. 403); Zhu et al. (2026, preprint); Prajod et al. (2026, preprint) |
| 3.3.4 | Layout and structure shape what users check | **ROGER (revise per flag):** Cho & Lim sentence → layout changed how quickly users first fixated *sources* (0.96 s vs 15.65 s), on static screens; gaze did not track trust |

## 4. Decision spaces (~600 words)

| ¶ | Claim / job | Anchors / your text |
|---|---|---|
| 4.1 | The theory: AI reading today resembles reading scriptura continua | **ROGER:** "I theorize that observing AI in operation today is analogous to reading scriptura continua, which requires oral reading to discern each word's function, thereby merging oracy with emerging literacy. Similarly, interacting with AI now combines users' literacy with their developing algorithmacy." |
| 4.2 | Definition of a decision space | **ROGER:** "Analogous to the introduction of spaces in written language, I propose implementing perceptual boundaries within AI-generated streams at points where users need to make decisions, or decision spaces." **[NEEDS: an operational rule for locating a decision unit in a response — e.g., the end of a checkable claim; a change of goal or cause (Zacks et al., 2009); a point where the user could accept, reject, or redirect. This rule decides whether the experiment can be replicated.]** |
| 4.3 | Three functions, each tied to its literature | **ROGER:** "These decision spaces would serve three functions: 1) providing a visual target; 2) establishing event boundaries; and 3) facilitating efficient regression." Function 1 → Rayner et al. (1998), McDonald (2006); 2 → Zacks et al. (2009), Kurby & Zacks (2012); 3 → Booth & Weger (2013), Schotter et al. (2014) |
| 4.4 | What a decision space is not: a cognitive forcing function by delay alone | Buçinca et al. (2021): 30-s wait reduced overreliance; Ghosh et al. (2026, preprint) |
| 4.5 | How much the marker should say | Prajod et al. (2026): terse labels raised fixations and saccades vs detailed ones **[NEEDS: your choice — blank space, rule, label, or prompt]** |

## 5. Proposed study (~1,500 words)

**ROGER (base text):** "A possible experimental design would have participants supervise a streaming AI response containing intentional errors under three conditions: a continuous stream, a stream interrupted at arbitrary intervals, and a stream segmented at decision units, with an equal number of breaks in each condition."

| Subsection | Content | Anchors / open decisions |
|---|---|---|
| 5.1 Design | Three conditions; equal break counts in conditions 2 and 3. Within- vs between-subjects | **[NEEDS: within or between.]** Tsoukala et al. (2025) found readers recalibrate after repeated misaligned breaks, so within-subjects needs blocked, counterbalanced order (Latin square, per Cho & Lim's own recommendation §5.2) |
| 5.2 Participants | Sample size and justification | **[NEEDS: N and power basis.]** For scale: Cho & Lim N = 23 (detected large gaze effects only); Park & Lee N = 36; Tsoukala eye tracking N = 29 (52% power for interaction) |
| 5.3 Stimuli | Pre-generated responses replayed at a fixed token rate; auto-scroll and input-bar fold held constant; seeded errors | Liu et al. (2024) and Xiao & Yang (2025) for rate choice; Cho & Lim (2026) for fold. Optional: split errors into local factual errors and cross-paragraph contradictions (an idea from the pasted packet, not a literature finding). **[NEEDS: topic domain, response length, number and kind of errors, token rate, pause length.]** |
| 5.4 Apparatus | Eye tracker, sampling rate, calibration and AOI rules | Cho & Lim report I-VT settings and data-quality thresholds worth matching. **[NEEDS: lab equipment.]** |
| 5.5 Measures | (a) fixations and dwell at break loci; (b) regressions — count, length, landing on content words (Sharmin et al., 2016); (c) error detection — hits and false alarms; (d) intervention latency; (e) workload (NASA-TLX); (f) trust | Liu et al. (2026) and Wu et al. (2025) for process measures; Parasuraman & Manzey for why (a)–(b) need (c) |
| 5.6 Hypotheses | **H1 (ROGER):** "I hypothesize that breaks at decision units will cause fixations and regressions to those points." **H2:** decision-unit breaks raise detection over both other conditions. **H3:** arbitrary breaks cost detection or workload relative to the continuous stream (Bailey & Konstan, 2006; Powers & Scerbo, 2023; Tsoukala et al., 2025) | [NEEDS: accept, revise or drop H2–H3] |
| 5.7 Analysis | Mixed-effects models with participant and item random effects; aggregate AOIs per participant × condition to avoid pseudoreplication (Cho & Lim, §2.6); fix the analysis plan before collecting data and say so in those words (your research rule: not "pre-registered" without a registry) | — |

## 6. Possible outcomes and what each would mean (~500 words)

| Pattern | Reading |
|---|---|
| C3 > C2 > C1 on regressions to break loci and detection | Segmentation at decision units does work beyond pausing — supports the decision-space account |
| C3 ≈ C2 > C1 | Pause or reduced pace explains the gain — **ROGER:** "If arbitrary breaks yield similar improvements, the benefit may be attributed to something rather than segmentation." Link to Buçinca's wait condition |
| C3 > C1 > C2 | Misplaced breaks hurt; placement matters in both directions (Tsoukala et al., 2025) |
| Gaze differs, detection does not | Attention moved without judgment (Cho & Lim, 2026); looking-but-not-seeing (Parasuraman & Manzey, 2010) |

## 7. Discussion: algorithmacy (~800 words)

| ¶ | Claim | Anchors / your text |
|---|---|---|
| 7.1 | Literacy merged with oracy; literacy now merges with algorithmacy | **ROGER:** "Users must interpret text while navigating both the opacity of AI systems and the influence of other users, particularly in organizational contexts." |
| 7.2 | Algorithmic literacy describes knowledge; algorithmacy adds a perceptual skill | Ridley & Pawlick-Potts (2021) definition (five bullets, "co-constituent") |
| 7.3 | Design implications for chat and agent interfaces | Chen et al. (2026): align judgment with decision-critical moments; Cho & Lim: Notice–Attend–Map–Act; Andes / Xiao & Yang: pacing is a design choice |
| 7.4 | Organizational contexts and other users | **[NEEDS: your material on cooptive environments from the dissertation]** |

## 8. Limitations (~400 words; each limit says what it does to the claim)

- Lab replay of pre-generated text is not live interaction; it buys control at the cost of intervention realism.
- Seeded errors may be easier or harder than natural model errors (Zhu et al., 2026, on fluent wrong answers).
- Fixations and regressions show where attention went, not that checking happened.
- Models and interfaces change; the stream rates and layouts tested will date.

## 9. Conclusion (~200 words)

One paragraph: what the paper proposed, what the study would show, and the most specific consequence for
interface design. End flat, in your register (see your scriptio continua passage: "We are in the process
of new UX changes for algorithmacy.").

## References

Use the list at the end of `literature_review.md` (59 entries, APA 7). Three entries still carry flags:
Parkes (edition), Sharmin et al. (2016) (co-authors, pages), Keenan (1984) (volume, pages).

---

## Decisions only you can make (collected)

1. Assignment length and required sections.
2. Adopt or reject the Parkes "grammar of legibility" frame (and read ch. 3 if adopting).
3. Operational rule for locating a decision unit.
4. Marker form at a decision space (blank, rule, label, prompt).
5. Within- vs between-subjects; N; token rate; pause length; error types.
6. Accept, revise, or drop H2–H3 and RQ1–RQ3.
7. Revisions to the two flagged sentences (Cho & Lim; Parasuraman & Manzey) and the "something rather than" slip.
