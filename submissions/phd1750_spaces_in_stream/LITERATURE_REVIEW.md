# Related literature for "Spaces in the Stream: How People See AI" (PHD1750)

> **Drafted by Claude (Opus 5.5) for Roger Hunt, 20 October 2026.** Every sentence in this file is my
> text, not yours. Your proposal is untouched. I read 13 sources in full or in large part myself
> (notes in `notes/`), triaged the rest by database abstract, and logged every query in `search-log.md`.
> Section 1 lists points in your current text that the sources do not support as written — your call on
> each.

---

## 1. Flags on your current text (for you to decide)

| Your sentence | What the source says | Locator | Status |
|---|---|---|---|
| "Cho and Lim (2026) showed that a chatbot's layout influences how quickly users find information." | Cho and Lim timed the first fixation on the **source-citation elements** (chips, cards, panel, links), not on answer content. Stimuli were **static, non-clickable screens** shown for 60 s; nothing streamed. Card list 0.96 s vs raw links 15.65 s to first fixation. | §2.3, Table 5, §3.2, §4.1 | Narrower than your wording |
| "Parasuraman and Manzey (2010) attribute automation complacency and bias to operators' attention span" | Their term is **attention**, not attention span: complacency "occurs under conditions of multiple-task load, when manual tasks compete with the automated task for the operator's attention"; the two phenomena share an attentional basis, "with attention playing a central role." | p. 381 (abstract) | Wording differs from source |
| "Park and Lee (2024) observed … more fixations and longer saccades when chatbot text appeared incrementally at the bottom of the screen, rather than all at once." | Supported. The "all at once" baseline was Bard-style text appearing whole at the top (Type 4). The study measured no comprehension and reported no regressions. | Tables 11–12; §4.2 | Accurate |
| Rayner, Fischer and Pollatsek (1998): "reduced reading speed by approximately half" | I could not open the full text (ScienceDirect blocked scripted and browser access from here). | — | **Not verified by me** |
| Schotter, Tran and Rayner (2014) | Not open access. The database abstract states that "the inability to regress affected comprehension negatively," which matches your sentence. | abstract only | Consistent; full text unread |
| Zacks et al. (2007); Wolfe (2021); Saenger (1997); Gibson (1979); O'Regan (2011) | Metadata verified (Crossref; Open Library for Gibson). I did not read these texts this session. | — | Metadata only |

All ten references in your list resolve to real records with matching author, title, year, venue,
volume and pages.

---

## 2. Synthesis

I organise the literature around the three functions you assign to a decision space — a visual
target, an event boundary, an aid to regression — and then around the automation problem those
functions are meant to solve.

### 2.1 Text that moves under the reader

Readers handle moving text by giving up integration, not word recognition. Harvey and colleagues
showed this most cleanly with horizontally scrolling text: readers made fewer and longer fixations
with shorter progressive and regressive saccades, kept the usual word-length and word-frequency
effects, but lost the early benefit of predictable words — word-level processing survived while
sentence-level integration did not (Harvey et al., 2017). Harvey and Walker (2018) then found that
literal comprehension held up under scrolling while inference questions suffered, and they named the
mechanism directly: returning to earlier text is harder in this format. Haverkamp, Bråten, Latini and
Salmerón (2023) moved the comparison onto phones and tablets with 145 students. Paging produced more
backtracking than scrolling (3.53 vs 2.49 instances, *p* = .012), scrolling produced longer and
less controlled backtracks, and integrated understanding favoured paging only as a trend
(*p* = .066). Öquist and Lundin (2007) had already found that, on a phone, paged text was read faster
than scrolled or RSVP text with no loss of comprehension.

Chatbot streaming adds one thing these studies lack: the system, not the reader, sets the motion.
Park and Lee (2024) are the only eye-tracking study I found of that condition. With 36 participants
watching four generation styles copied from 2023 chatbots, text generated at the bottom of the
screen — ChatGPT's auto-scrolling follow-up turn, Bing's upward growth — drew more fixations, longer
total fixation time and larger saccades than Bard's whole-text display, and fixation starts piled up
in the lowest screen regions where new words appeared (Tables 9, 11–12). Xiao and Yang (2025) supply
the engineering side of the same fact. Streaming speed tracks the provider's compute budget, not the
reader: GPT-4o's API runs near 45 words per second, while 99% of their Prolific readers were
comfortable at or below 21.2 words per second on easy text and 12.0 on hard text (§3.2). In their
phrase, streaming "transforms text from a static payload into a dynamic, time-based medium" (§1).

### 2.2 Regressions need text that stays where it was

The rereading account of regressions makes streaming's cost concrete. Booth and Weger (2013) made a
just-read sentence illegible while keeping every word's position, length and capitals; readers
regressed less, landed less accurately, and gained nothing in comprehension from the regressions they
still made (*F*(1, 851) = 65.34 for regression rate). When they swapped a word during a regression,
readers adopted the new word's meaning without noticing the change (*d* = 1.87). Readers, in other
words, look back to *reread*, not to cue memory by location. Booth and Weger even anticipated your
problem: readers of "scrollable text on small screens" face a world where "rereading is often
impossible" (General discussion). Schotter, Tran and Rayner's (2014) trailing mask, already in your
proposal, removes the same option by a different route. Metzner, von der Malsburg, Vasishth and Rösler
(2017) add the neural side: free reading beat word-by-word RSVP only on trials where the eyes
regressed to an anomaly, and those regressions travelled with a P600 effect. Benedetto et al. (2015)
found that Spritz, by suppressing regressions and parafoveal preview, hurt literal comprehension.

An auto-scrolling stream sits between these manipulations. It does not mask or delete earlier text,
but it can move that text out of view, and Booth and Weger's results predict that readers will
regress less once the target is no longer where they left it.

### 2.3 Where a break falls matters, not only that it falls

The strongest support for decision-unit breaks over arbitrary ones comes from a 2025 line-break
study. Tsoukala, Vogelzang and Tsimpli (2025) placed line breaks so that they either coincided with
clause boundaries or "scissored" clauses across lines, and ran self-paced reading (N = 39) and eye
tracking (N = 29). Aligned breaks sped the disambiguating region; repeated misaligned breaks slowed it
(eye tracking: first-pass *d* = 0.32, total time *d* = 0.41) and, in self-paced reading, cut
comprehension in the critical condition (OR = 0.38). They frame line breaks as "good" or "bad" cues
and show that readers recalibrate: after several scissored lines, readers stopped trusting line ends
as closure cues (§4.3). Their eye-tracking display also revealed text one line at a time — closer to a
stream than most reading studies get. Tsoukala and colleagues also report, citing LeVasseur et al.
(2006), that only 31% of lines in US second-grade texts ended on an intact syntactic unit (§6; I have
not read LeVasseur et al.).

The text-signalling literature reaches the same conclusion through headings. Hyönä and Lorch (2004)
found that topic headings sped first-pass reading of topic sentences and directed later look-backs to
them, and Lorch (1989) reviewed the general pattern: signalled content is remembered better, while
unsignalled content is mostly unaffected. The evidence runs the other way too. Keenan (1984) found
that one-phrase-per-line chunking slowed reading, which he attributed to uneven line lengths, and
Koornneef (2024) found that sentence-by-sentence segmentation helped beginning readers comprehend
without the longer wrap-up times explaining why. Segmentation, then, is not free; its value depends
on matching units the reader already parses.

### 2.4 New text captures the eyes

Your Guided Search framing gains a sharper mechanism from attentional capture. Yantis and Jonides
(1984) showed that an item appearing abruptly in a display captures attention in visual search. Every
streamed token is such an onset. Park and Lee's fixation starts clustered exactly where new text
appeared, which is what onset capture predicts, and it implies that a stream pulls the eyes forward
against the backward pull of a regression. A decision space that halts new onsets removes that
competitor for a moment.

### 2.5 Events and breakpoints

Event segmentation theory carries into reading and into interrupted work. Zacks, Speer and Reynolds
(2009) showed that readers slow at clauses that other readers mark as event boundaries — roughly
108 ms for each 10% rise in boundary agreement — and that situation changes partly mediate the
slowdown (Exp. 3). Their Experiment 1 already contains a stream: a "visual-sequential" group read
clauses at a software-set pace with no way to review earlier ones, and still segmented hierarchically.
Kumar et al. (2023) linked segmentation to a language model directly: human event boundaries in story
listening tracked Bayesian surprise computed from GPT-2, not simple surprisal.

The interruption literature tests what happens when a system breaks a task at a boundary versus
mid-unit. Bailey and Konstan (2006) found that peripheral tasks arriving *during* a primary task,
rather than between tasks, cost 3%–27% more time, doubled errors and raised annoyance by 31%–106%.
Powers and Scerbo (2023) tied this directly to event segmentation: interruptions at coarse
breakpoints were no more disruptive than no interruption, while fine-breakpoint interruptions
lengthened resumption and raised workload. These two studies give your arbitrary-break condition a
prediction of its own: a break that lands mid-unit should cost something, not merely fail to help.

### 2.6 Fluent output and overreliance

The automation literature you cite has an LLM-era sequel. Lee and See (2004) placed trust at the
centre of reliance when systems are too complex to understand fully, and Endsley (2017) named the
"automation conundrum": as autonomy and reliability rise, operators' situation awareness and capacity
to take over fall. Parasuraman and Manzey's (2010) review supplies the finding most relevant to an
eye-tracking design — a "looking-but-not-seeing" effect, in which operators sampled every parameter
needed to catch an automation error and still accepted it (p. 403). Fixations alone, then, will not
show that a reader checked anything.

Recent LLM studies show how presentation shifts reliance. Kim et al. (2025), with 308 participants,
found that explanations raised agreement with correct and incorrect answers alike, while sources and
visible inconsistencies lowered agreement with wrong ones; 189 participants never clicked a source.
Steyvers et al. (2025) found that users overestimated LLM accuracy with default explanations and that
longer explanations raised confidence without raising accuracy. Bhat (2025) is the closest test of
streaming itself: in a within-subjects study with 103 participants, a typing-simulation display
raised perceived competence, trustworthiness and warmth compared with static text, with no change in
perceived effectiveness. If streaming makes output look more trustworthy, it adds a reliance cost to
the perceptual one. Liu et al. (2026) traced overreliance in behaviour rather than outcomes: heavy
overreliers copied and pasted whole responses and navigated coarsely to "prominent" screen areas.

Buçinca, Malaya and Gajos (2021) tested the interventions closest to a decision space. Their
"cognitive forcing functions" — deciding before seeing the AI, requesting it on demand, or waiting
30 seconds while "the AI is processing" — cut overreliance on wrong suggestions (carb-source
detection: 48% vs 64% followed the wrong AI, *d* = .36), at the price of lower preference and higher
perceived complexity. The wait condition matters for your design: a bare pause, with no structure,
already helped.

### 2.7 Supervising agents: when judgment arrives

Agent oversight research converges on timing. Chen et al. (2026, preprint) ran 48 participants
through 192 live sessions with a computer-use agent. Users blocked only 29 of 138 problematic actions
that reached execution, and 56% of failures arose because the interface asked for judgment before or
after the moment the risk appeared (§5.2.1). Their conclusion reads close to your proposal: oversight
"depends less on maximizing control than on aligning authority, timing, and attention with
decision-critical moments" (Abstract). Grunde-McLaughlin et al. (2026, preprint) found that
redesigned agent traces cut the time people took to find errors without improving their accuracy.

### 2.8 Perception and action

This facet stayed thin in the empirical search. O'Regan and Noë (2001) state the sensorimotor claim
that your proposal builds on — seeing as the exercise of mastered laws linking movement to sensory
change — and the Booth and Weger and Haverkamp results read naturally in those terms: a stream breaks
the lawful link between where the reader looks back and what is there. I did not find an empirical
study that applies sensorimotor theory to dynamic or streamed text.

---

## 3. Gap check

**What I looked for:** studies that (a) eye-track streamed LLM output against static output, or (b)
segment or pause a stream at decision points and measure verification.

**Where:** Consensus (8 queries), OpenAlex (6), arXiv API (4), web search in extended mode (4), plus
the reference lists of Park and Lee (2024), Cho and Lim (2026), Chen et al. (2026), and the 2026
systematic review by Resulbegoviq et al. Scholar Gateway refused access. Dates: 20 October 2026.

**What I found:**
- Park and Lee (2024) is the only eye-tracking study of chatbot text *generation* I found. It
  measures fixations and saccades across generation styles; it has no comprehension, regression, or
  error-detection measure and no segmentation manipulation.
- Bhat (2025) compares streamed and static display, but on self-reported perception, without eye
  tracking or error detection.
- Xiao and Yang (2025) and a CHI 2026 extended abstract ("Just-in-Time Tokens", not read) adjust
  stream *speed* to readers; neither segments the stream at decision points.
- Resulbegoviq et al. (2026) reviewed 23 eye-tracking studies of AI-generated content and described
  none that compares streamed with static text. Their eligibility rule required a human-made or no-AI
  comparator (§3.3), which would exclude a streamed-vs-static study, so their silence is weak evidence.
- Chen et al. (2026) show that judgment timing matters for agent oversight, without eye tracking and
  without text streams.
- Tsoukala et al. (2025) show that break placement relative to linguistic units matters, in static
  poem-like texts.
- Nobody I found applies the *scriptura continua* analogy to AI output.

**Statement you can defend:** I found no study, in the sources and dates above, that segments a
streaming LLM response at decision units and measures fixations, regressions and error detection
against a continuous stream and an arbitrarily interrupted one.

---

## 4. What the literature implies for the proposed experiment (my reading)

1. **Pause vs. structure.** Buçinca et al.'s 30-second "wait" reduced overreliance with no
   segmentation at all, so your equal-number-of-breaks arbitrary condition is the right control. The
   interruption studies (Bailey & Konstan, 2006; Powers & Scerbo, 2023) predict that mid-unit breaks
   may *hurt*, not just fail to help.
2. **Cue reliability drifts.** Tsoukala et al. found that repeated misaligned breaks taught readers to
   stop trusting line ends. Within-subjects arbitrary breaks could therefore contaminate later
   decision-unit trials; block order or a between-subjects factor would guard against that.
3. **Fixation is not verification.** Parasuraman and Manzey's looking-but-not-seeing finding, Cho and
   Lim's dissociation between gaze and trust, and Resulbegoviq et al.'s §5.2.1 all argue for pairing
   gaze with error detection — which your seeded-error design already does.
4. **Reviewable vs. scrolled-away text** is a separable factor. Zacks et al.'s visual-sequential vs
   visual-continuous groups and Booth and Weger's illegibility manipulation suggest holding scroll
   behaviour constant or crossing it with segmentation.
5. **Process measures exist.** Wu et al. (2025) and Cao and Huang (2022) show that gaze on AI output
   tracks reliance; their measures could serve as secondary outcomes.

---

## 5. Annotated bibliography (new sources, by facet)

Status codes: **[F]** read in full or in large part by me this session (notes file named);
**[A]** abstract only, from the database record; **[P]** preprint, not peer reviewed.
Metadata for every entry checked against Crossref unless noted. Co-author initials marked *[verify]*
where Crossref returned family names only and I lost network access before re-querying.

### Reading moving, scrolled and streamed text
- **Park, H., & Lee, Y. (2024).** The effect of text movement on eye movements in generative AI chatbots. *Archives of Design Research, 37*(4), 181–197. https://doi.org/10.15187/adr.2024.08.37.4.181 — **[F]** `notes/parklee2024.md`. N = 36; bottom-anchored generation raised fixations, total fixation time and saccade amplitude vs whole-text display.
- **Harvey, H., Godwin, Fitzsimmons, Liversedge, & Walker *[verify initials]* (2017).** Oculomotor and linguistic processing effects in reading dynamic horizontally scrolling text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(3), 518–536. https://doi.org/10.1037/xhp0000329 — **[A]** Word-level effects preserved; sentence-level predictability benefit lost under scrolling.
- **Harvey, H., & Walker *[verify]* (2018).** Reading comprehension and its relationship with working memory capacity when reading horizontally scrolling text. *Quarterly Journal of Experimental Psychology, 71*(9), 1887–1897. https://doi.org/10.1080/17470218.2017.1363258 — **[A]** Literal comprehension held; inference suffered; returning to earlier text harder.
- **Haverkamp, Y. E., Bråten, I., Latini, N., & Salmerón, L. (2023).** Is it the size, the movement, or both? *Reading and Writing, 36*(7), 1589–1608. https://doi.org/10.1007/s11145-022-10328-9 — **[F]** `notes/haverkamp2023.md`. Paging > scrolling for backtracking; comprehension difference only a trend.
- **Öquist, G., & Lundin *[verify]* (2007).** Eye movement study of reading text on a mobile phone using paging, scrolling, leading, and RSVP. In *Proceedings of the 6th International Conference on Mobile and Ubiquitous Multimedia* (pp. 176–183). https://doi.org/10.1145/1329469.1329493 — **[A]** N = 16; paging read faster than scrolling and RSVP, comprehension equal.
- **Xiao, C., & Yang, B. Z. (2025).** Streaming, fast and slow: Cognitive load-aware streaming for efficient LLM serving. In *Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology (UIST '25)* (pp. 1–13). https://doi.org/10.1145/3746059.3747721 — **[F]** `notes/xiaoyang2025.md`. Comfortable streaming speeds far below API speed; adaptive pacing.
- **Rayner, K. (1998).** Eye movements in reading and information processing: 20 years of research. *Psychological Bulletin, 124*(3), 372–422. https://doi.org/10.1037/0033-2909.124.3.372 — **[A]** Standard review; eye-movement data index moment-to-moment processing.

### Regressions and rereading
- **Booth, R. W., & Weger, U. W. (2013).** The function of regressions in reading: Backward eye movements allow rereading. *Memory & Cognition, 41*(1), 82–97. https://doi.org/10.3758/s13421-012-0244-y — **[F]** `notes/booth2013.md`. Regressions serve rereading, not location-cued memory.
- **Metzner, P., von der Malsburg, Vasishth, & Rösler *[verify]* (2017).** The importance of reading naturally. *Cognitive Science, 41*(S6), 1232–1263. https://doi.org/10.1111/cogs.12384 — **[A]** Free reading beat RSVP only on trials with regressions to the anomaly.
- **Benedetto, S., Carbone, Pedrotti, Le Fevre, Bey, & Baccino *[verify]* (2015).** Rapid serial visual presentation in reading: The case of Spritz. *Computers in Human Behavior, 45*, 352–358. https://doi.org/10.1016/j.chb.2014.12.043 — **[A]** Suppressing regressions and preview hurt literal comprehension.

### Breaks, segmentation and signalling
- **Tsoukala, A., Vogelzang, M., & Tsimpli, I. M. (2025).** The influence of text segmentation on garden path processing. *Language and Cognition, 17*, e58. https://doi.org/10.1017/langcog.2025.10009 — **[F]** `notes/tsoukala2025.md`. Breaks aligned with clause boundaries help; misaligned breaks disrupt and retrain expectations.
- **Hyönä, J., & Lorch, R. F. (2004).** Effects of topic headings on text processing: Evidence from adult readers' eye fixation patterns. *Learning and Instruction, 14*(2), 131–152. https://doi.org/10.1016/j.learninstruc.2004.01.001 — **[A]** Headings sped first-pass reading and steered look-backs.
- **Lorch, R. F. (1989).** Text-signaling devices and their effects on reading and memory processes. *Educational Psychology Review, 1*(3), 209–234. https://doi.org/10.1007/BF01320135 — **[A]** Review of signals.
- **Koornneef, A. (2024).** On the readability of texts presented in sentence-by-sentence segments to beginner readers. *Reading and Writing, 37*(1), 69–87. https://doi.org/10.1007/s11145-023-10423-5 — **[A]** Segmentation raised comprehension; wrap-up time did not explain it.
- **Keenan, S. A. (1984).** Effects of chunking and line length on reading efficiency. *Visible Language.* — **[A]** No DOI; volume and pages not verified. Chunked text read more slowly, attributed to line-length variability. Counter-evidence.

### Attention capture
- **Yantis, S., & Jonides, J. (1984).** Abrupt visual onsets and selective attention: Evidence from visual search. *Journal of Experimental Psychology: Human Perception and Performance, 10*(5), 601–621. https://doi.org/10.1037/0096-1523.10.5.601 — **[A]** Abrupt onsets capture attention.

### Event segmentation and breakpoints
- **Zacks, J. M., Speer, N. K., & Reynolds, J. R. (2009).** Segmentation in reading and film comprehension. *Journal of Experimental Psychology: General, 138*(2), 307–327. https://doi.org/10.1037/a0015305 — **[F]** `notes/zacks2009.md`. Readers slow at event boundaries; includes a software-paced, non-reviewable condition.
- **Kumar, M., Goldstein, Michelmann, Zacks, Hasson, & Norman *[verify]* (2023).** Bayesian surprise predicts human event segmentation in story listening. *Cognitive Science, 47*(10), e13343. https://doi.org/10.1111/cogs.13343 — **[A]** GPT-2–derived Bayesian surprise tracks human boundaries.
- **Bailey, B. P., & Konstan *[verify]* (2006).** On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state. *Computers in Human Behavior, 22*(4), 685–708. https://doi.org/10.1016/j.chb.2005.12.009 — **[A]** Interruptions during vs between tasks: more time, double errors.
- **Powers, S. A., & Scerbo *[verify]* (2023).** Examining the effect of interruptions at different breakpoints and frequencies within a task. *Human Factors, 65*(1), 22–36. https://doi.org/10.1177/00187208211009010 — **[A]** Coarse breakpoints ≈ no interruption; fine breakpoints costly. (Online 2021; the open repository copy is the first author's MS thesis, not the article.)

### Automation, trust and LLM overreliance
- **Lee, J. D., & See *[verify]* (2004).** Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392 — **[A]**
- **Endsley, M. (2017).** From here to autonomy. *Human Factors, 59*(1), 5–27. https://doi.org/10.1177/0018720816681350 — **[A]** The automation conundrum. *[verify middle initial]*
- **Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025).** Fostering appropriate reliance on large language models. In *CHI '25* (pp. 1–19). https://doi.org/10.1145/3706598.3714020 — **[F]** `notes/kim2025.md`.
- **Steyvers, M., Tejeda, Kumar, Belem, Karny, Hu, Mayer, & Smyth *[verify]* (2025).** What large language models know and what people think they know. *Nature Machine Intelligence, 7*(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7 — **[A]** Longer explanations raised confidence, not accuracy.
- **Bhat, M. (2025).** How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces* (pp. 846–860). https://doi.org/10.1145/3708359.3712131 — **[A]** Streamed display raised perceived trustworthiness. (ACM full text behind bot check.)
- **Liu, C., Zhou, Q., Shen, X., Liu, X. B., Wu, T., & Chen, X. A. (2026).** Behavioral indicators of overreliance during interaction with conversational language models. In *CHI '26* (pp. 1–23). https://doi.org/10.1145/3772318.3790332 — **[F]** `notes/liu2026.md`.
- **Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021).** To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287 — **[F]** `notes/bucinca2021.md`.
- **Wu, Z.-K., Wang, Langer, & Feit *[verify]* (2025).** RelEYEance: Gaze-based assessment of users' AI-reliance at run-time. *Proceedings of the ACM on Human-Computer Interaction, 9*(3), 1–18. https://doi.org/10.1145/3725841 — **[A]** Gaze patterns distinguish over-, under- and appropriate reliance.
- **Cao, S., & Huang *[verify]* (2022).** Understanding user reliance on AI in assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 6*(CSCW2), 1–23. https://doi.org/10.1145/3555572 — **[A]** Gaze share on AI suggestion correlated with agreement.
- **Resulbegoviq, H., Hlebec, V., Pejić Bach, M., & Stamatović, I. (2026).** Eye tracking and AI-generated content: A systematic literature review. *Journal of Eye Movement Research, 19*(5), Article 97. https://doi.org/10.3390/jemr19050097 — **[F, in part]** `notes/resulbegoviq2026.md`.

### Agent oversight
- **Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026).** *Comparing human oversight strategies for computer-use agents* [Preprint]. arXiv:2604.04918v2. — **[F][P]** `notes/chen2026cua.md`. Verified against the PDF itself; arXiv API unreachable at audit time.
- **Grunde-McLaughlin, M., Mozannar, H., Murad, M., Chen, J., Amershi, S., & Fourney, A. (2026).** *Overseeing agents without constant oversight: Challenges and opportunities* [Preprint]. arXiv:2602.16844. — **[A][P]** Names from Chen et al.'s reference [24] and the Consensus record.

### Perception and action
- **O'Regan, J. K., & Noë, A. (2001).** A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973. https://doi.org/10.1017/S0140525X01000115 — **[A]**

### Already in your list, re-checked
Cho and Lim (2026) **[F]** `notes/cholim2026.md`; Parasuraman and Manzey (2010) **[F, core sections]**
`notes/parasuraman2010.md`; the other eight: metadata verified, full texts not read this session.

---

## 6. Not read or not reachable

- Full text blocked: Rayner, Fischer & Pollatsek (1998, ScienceDirect); Schotter et al. (2014, SAGE, not OA); Bhat (2025, ACM bot check); Powers & Scerbo (2023, SAGE bot check); Harvey et al. (2017), Harvey & Walker (2018), Metzner et al. (2017), Benedetto et al. (2015), Hyönä & Lorch (2004), Lee & See (2004), Endsley (2017), O'Regan & Noë (2001) — not open access.
- Not attempted for time: Zacks et al. (2007), Wolfe (2021), Saenger (1997), Gibson (1979), O'Regan (2011); "Just-in-Time Tokens" (CHI EA 2026).
- I did not bypass any bot-verification page.

## 7. Citation audit

| Check | Result |
|---|---|
| Metadata vs Crossref | All 38 DOI-bearing entries (29 new + 9 of yours) matched on title, authors' family names, year, venue, volume, pages. Keenan (1984) has no DOI and is unverified. Chen et al. and Grunde-McLaughlin et al. verified against the PDF / a second reference list. |
| Corrections I made to my own working notes | "Bailey et al. (2006)" → **Bailey & Konstan (2006)**; Powers & Scerbo print year **2023**, not 2021; Endsley print year **2017**; Haverkamp et al. print year **2023**; Koornneef print year **2024**; Metzner et al. **2017** (vol. 41, S6). |
| Claim check | Every number in §2 and §4 comes from a source I read [F] (locators in the notes files) or from a database abstract [A]. |
| Retraction / correction search (Crossref `updates` filter) | Cho & Lim, Park & Lee, Schotter et al.: none. Remaining key papers: **not completed** — Crossref stopped responding. |
| Co-author initials | Marked *[verify]* where not confirmed from a record. |

## 8. Files

- `search-log.md` — 36 logged queries and access attempts
- `notes/*.md` — 13 reading notes with locators
- `texts/` — extracted full texts used for reading

---

# ROUND 2 — The pasted research packet ("Perceptual Boundaries in Autonomous Text Streams")

> **Drafted by Claude (Opus 5.5), 20 October 2026.** The packet you pasted reads as machine-generated
> research and cites about 35 sources. Following your rule that every citation and number be verified
> before it enters a draft, I checked each load-bearing source against a record, read eight of them in
> full or in large part, and compared the packet's claims with what the sources say. Notes are in
> `notes/` (andes2024, zhu2026, prajod2026, deepinteraction2026, timkey2026, mangen2019, ridley2021,
> ghosh2026); queries 37–43 in `search-log.md`. I have **not** copied the packet's prose into your review.

## R2.1 Claims in the packet that the sources do not support

| Packet claim | What the source says | Status |
|---|---|---|
| "Aggarwal et al. (2026)": balanced verifiability falls from 0.717 (SFT) to 0.602 (DPO) | First author is **Zhu**; Aggarwal et al. is a separate work cited in it. 0.717→0.602 is the **false-positive cell for one model (Tulu3.1-8B) on one benchmark (GSM8K)**, not overall v_bal; raters were mainly LLMs (Zhu et al. §7.1, App. A) | Misattributed, misdescribed |
| Only structural changes that "alter presentation format" restore verifiability | Zhu et al. find the **opposite**: changing presentation without adding information does not help; only methods that add external information do (§1) | Reversed |
| Liu et al. (Andes) give 238 WPM overall, 200 nonfiction / 260 fiction | Not in either arXiv version. Andes gives age-group WPM (236–175) and the 4.8 tokens/s **average** (v1 §2.1, Table 1). The 32% dropout figure concerns web pages generally, citing a web-statistics source | Partly unsupported |
| 4.8 tokens/s is a "biological ceiling" of human reading | Andes treats it as an average consumption rate used as a delivery target | Overstated |
| Streaming Fast and Slow cut compute 16.79% "while maintaining user satisfaction across 99% of readers" | 16.79% is at a 95% streaming-reading alignment rate; 63.14% was the 99% figure in a pilot simulation; no satisfaction measure (Xiao & Yang Table 1, §3.2) | Conflated |
| Cho & Lim coin the term "commercial chat fold" | They write that occluding the last line "reproduc[es] the fold of commercial chat interfaces" (§2.3) — a description, not a term | Overstated |
| Zacks et al. (2009) and Kurby & Zacks (2008) "established via reading-time paradigms" cortical spikes at boundaries | Zacks et al. (2009) has no imaging. Kurby & Zacks (2008) is a review whose abstract reports transient boundary activity in posterior temporal, parietal and lateral frontal cortex for **observed activity**, not reading | Conflated |
| Buçinca et al. (2021) / Ghosh et al. (2026) formalise CFFs as D₂ = F(D₁) | Neither paper contains this notation | Invented formalism |
| Mangen et al. (2019) show scrolling destroys spatial landmarks, with parietal neuroimaging evidence | Kindle vs print book, N = 50; the authors **deliberately did not test scrolling** and report no imaging; print readers better on chronology (t(48) = 2.03) | Misdescribed |
| Lei et al. (2023) compared five paradigms; Auto-Scrolling had highest NASA-TLX (M = 26.97) | Record: 20 participants, four **gaze-controlled page-scrolling** techniques on a smartphone, sitting and walking; the implicit technique scrolled by reading speed. It is not autonomous streaming. I could not open the full text (ACM bot check) to verify the numbers | Not verified; context differs |
| Sharmin (2016): emerging text gives longer fixations than static text; word-by-word > letter-by-letter regressions; F(1,19) = 78.193; "continuation-checking" saccades | The SKY 2016 abstract concerns **letter-by-letter** print-interpreted text: 90.8% of regression landing points were content words, nouns most often; omissions caused regressions. The word-by-word > letter-by-letter finding is **Sharmin, Špakov & Räihä (2015, IJHCS)**. "Longer than static," the F value, and continuation-checking saccades are not in either abstract | Partly misattributed; rest unverified |
| Drieghe et al. (2017) show degraded boundary cues "severely impair preview benefit" | Abstract: unspaced text slowed reading, with "rather limited evidence for more distributed processing." Sheridan et al. (2016, not in the packet) is the study showing larger preview effects for spaced than unsegmented text | Overstated |
| Valsecchi et al. (2013): pursuit episodes "significantly longer" than fixations; 2.5°/s acuity threshold; tested speeds 3.52/7.05/14.09°/s | Abstract confirms drifting text is read by smooth pursuit plus saccades and that pursuit gain rises after a saccade. The durations, threshold and speeds are not in the abstract; full text not obtained | Partly verified |
| Deep Interaction: human-in-the-loop mid-stream intervention gives >25% correction gain, ~40% fewer tokens | Gains confirmed in the abstract, but users edit a **finished** chain of thought, and large-scale results use an automated agent that simulates human corrections from reference solutions | Context differs |
| PNAS (2026), 409 estimates; regression-inhibiting interfaces "cripple" auditing of LLM logic | Authors are **Timkey et al.**, n = 368, 409 surprisal estimates, syntactic garden paths. The step to auditing LLM output is the packet's inference | Authors missing; extrapolated |
| Prajod et al. (2026): one-line disclosures raised load "compared to both no disclosure and detailed disclosures" | Overall difference significant against detailed disclosures; against no disclosure only within lifestyle articles (§4.2) | Slightly overstated |
| Kurby & Zacks (2012): OR = 2.29, z(926) = 2.87 for goals at fine boundaries | Confirmed in the full text (PMC4190164, retried 20 Oct): fine boundaries raised mention of goals (OR = 2.29, z(926) = 2.87, p = .004) and causes (OR = 1.81) **in the subset of clauses with no change on that dimension**; coarse boundaries raised mention of time (OR = 1.53). Readers typed think-aloud responses while reading | Verified |
| E-Z Reader constants (Q = 7, S_b = 7.3, S_m = 4.5), 125–175 ms saccade programming | Reichle et al. (1998) metadata verified; full text not read | Not verified |

## R2.2 What the packet gets right, and what I add

The packet's strongest contribution is an argument, not a citation: **Parkes's (1992) "grammar of
legibility"** answers the obvious objection to your analogy — that chat text already has word spaces.
"Grammar of Legibility" is the title of Parkes's third chapter, and the book treats punctuation as a
means of resolving structural uncertainty. If you take this route, Saenger supplies word-level
separation and Parkes supplies the discourse-level pause that a decision space would play. I have
verified the chapter title and the book record only; the claims about *positurae* and *per cola et
commata* need checking against the book. The framing is yours to accept or reject.

Several sources survive verification and strengthen the review:

- **Emerging text.** Sharmin, Špakov and Räihä (2015) eye-tracked 20 participants reading text typed
  live by a print interpreter. Word-by-word appearance produced significantly more rereading and
  regressions than letter-by-letter appearance, and regressions started more often at sentence-final
  words. Sharmin and colleagues (2016) found that 90.8% of regression landing points on letter-by-letter
  text were content words, against 57.1% of the text, with nouns the most likely targets. These two
  studies are the closest precedent I have now seen for watching a stream of text form, closer than
  Park and Lee (2024).
- **Drifting text.** Valsecchi, Gegenfurtner and Schütz (2013) showed that readers follow drifting text
  with an alternation of smooth pursuit and saccades, and that pursuit and saccades interact. The
  "automated cursor" in your proposal now has an oculomotor name.
- **Rereading as repair.** Timkey et al. (2026) found, with 368 readers, that language-model surprisal
  predicts early reading on garden-path sentences but not the added rereading cost of disambiguation;
  surprisal "can capture routine structure-building, but not the cost of detecting or correcting
  errors." That line joins Booth and Weger (2013) and Schotter et al. (2014).
- **Updating at boundaries.** Kurby and Zacks (2012) found both incremental updating (readers mention a
  situation dimension more when it changes) and global updating (more mentions at event onsets,
  controlling for change).
- **Delivery speed.** Liu et al. (2024, Andes) estimate average reading consumption at 4.8 tokens/s and
  observed a serving system delivering 11.2 tokens/s on a real trace (v2 §2.2).
- **Fluency hides errors.** Zhu et al. (2026) found that post-training raised accuracy without raising
  error verifiability, and that preference optimization made wrong answers' justifications harder to
  flag in at least one model–benchmark pair.
- **Cue informativeness.** Prajod et al. (2026) found that a terse AI-use label raised fixation duration
  and saccade count relative to a detailed one, with no change in NASA-TLX or pupil size — a design
  warning for how much a decision-space marker should say.
- **Embodied reading.** Mangen, Olivier and Velay (2019) tie Gibson and O'Regan and Noë to reading media
  empirically, and Mangen, Walgermo and Brønnick (2013) found that 72 tenth-graders comprehended better
  on paper than on screen-read PDFs. Delgado et al. (2018) meta-analysed 54 experiments (as summarised
  by Mangen et al., 2019) and found a paper advantage that grew between 2000 and 2017.
- **Algorithmic literacy.** Ridley and Pawlick-Potts (2021) define algorithmic literacy as "skill,
  expertise, and awareness" across five bullets ending with positioning "the individual as a
  co-constituent in algorithmic decision-making." Their definition describes knowledge and awareness
  and names no real-time perceptual skill — the space your term algorithmacy occupies.

## R2.3 The packet's experimental recommendations (for you to weigh)

The packet proposes four design refinements. Each sits on sources whose support I rate here:

1. **Log tokens per second and fix the input-bar fold.** Sound; Cho and Lim standardised the fold, and
   Andes and Xiao and Yang show delivery speed varies by system.
2. **Split seeded errors into local factual errors and global cross-paragraph contradictions.** A good
   design idea; it is the packet's own, not a finding from the cited studies.
3. **Test a passive pause against an active micro-interaction at each decision space.** Reasonable, and
   it echoes Buçinca et al.'s on-demand vs wait conditions; the Lei et al. support is weak (see R2.1).
4. **Aggregate AOIs per participant × condition.** Directly from Cho and Lim §2.6.

The packet's table of predicted outcomes by condition is speculation built partly on the claims in
R2.1; I would not cite it as derived from the literature.

## R2.4 Verified additions to the bibliography

Status codes as in §5. **[F]** read in full or in large part; **[A]** abstract/record only; **[P]** preprint.

- **Delgado, P., Vargas, C., Ackerman, R., & Salmerón, L. (2018).** Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. *Educational Research Review, 25*, 23–38. https://doi.org/10.1016/j.edurev.2018.09.003 — **[A]** via Mangen et al. (2019).
- **Drieghe, D., Fitzsimmons, G., & Liversedge, S. P. (2017).** Parafoveal preview effects in reading unspaced text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(10), 1701–1716. https://doi.org/10.1037/xhp0000441 — **[A]**
- **Ghosh, A., Sarkar, A., Lindley, S., & Poelitz, C. (2026).** *An experimental comparison of cognitive forcing functions for execution plans in AI-assisted writing* [Preprint]. arXiv:2601.18033. — **[A][P]** n = 214.
- **Knox, B. M. W. (1968).** Silent reading in antiquity. *Greek, Roman and Byzantine Studies, 9*(4), 421–435. — **[metadata only]** from the journal's issue listing via web search; not read.
- **Kurby, C. A., & Zacks, J. M. (2008).** Segmentation in the perception and memory of events. *Trends in Cognitive Sciences, 12*(2), 72–79. https://doi.org/10.1016/j.tics.2007.11.004 — **[A]**
- **Kurby, C. A., & Zacks, J. M. (2012).** Starting from scratch and building brick by brick in comprehension. *Memory & Cognition, 40*(5), 812–826. https://doi.org/10.3758/s13421-011-0179-8 — **[F, results]** think-aloud while reading; both incremental and global updating; goal and cause mentions rise at fine boundaries even without a change on that dimension.
- **Lei, Y., Wang, Y., Caslin, T., Wisowaty, A., Zhu, X., Khamis, M., & Ye, J. (2023).** DynamicRead: Exploring robust gaze interaction methods for reading on handheld mobile devices under dynamic conditions. *Proceedings of the ACM on Human-Computer Interaction, 7*(ETRA), 1–17. https://doi.org/10.1145/3591127 — **[A]** gaze-controlled page scrolling, not streaming.
- **Liu, J., Chung, J.-W., Wu, Z., Lai, F., Lee, M., & Chowdhury, M. (2024).** *Andes: Defining and enhancing quality-of-experience in LLM-based text streaming services* [Preprint]. arXiv:2404.16283. — **[F, §1–2][P]**
- **Mangen, A., Olivier, G., & Velay, J.-L. (2019).** Comparing comprehension of a long text read in print book and on Kindle: Where in the text and when in the story? *Frontiers in Psychology, 10*, Article 38. https://doi.org/10.3389/fpsyg.2019.00038 — **[F]**
- **Mangen, A., Walgermo, B. R., & Brønnick, K. (2013).** Reading linear texts on paper versus computer screen: Effects on reading comprehension. *International Journal of Educational Research, 58*, 61–68. https://doi.org/10.1016/j.ijer.2012.12.002 — **[A]**
- **McDonald, S. A. (2006).** Parafoveal preview benefit in reading is only obtained from the saccade goal. *Vision Research, 46*(26), 4416–4424. https://doi.org/10.1016/j.visres.2006.08.027 — **[metadata only]**; the title states the claim.
- **Parkes, M. B. (1992).** *Pause and effect: An introduction to the history of punctuation in the West.* Scolar Press. (Reissued Routledge, 2016.) — **[metadata only]**; chapter 3 titled "Grammar of Legibility." *[verify publisher/city of the edition you use]*
- **Prajod, P., Cools, H., Röggla, T., Cesar, P., & El Ali, A. (2026).** *Towards gaze-informed AI disclosure interfaces: Eye-tracking attentional and cognitive load while reading AI-assisted news* [Preprint]. arXiv:2605.14999. — **[F][P]**
- **Reichle, E. D., Pollatsek, A., Fisher, D. L., & Rayner, K. (1998).** Toward a model of eye movement control in reading. *Psychological Review, 105*(1), 125–157. https://doi.org/10.1037/0033-295X.105.1.125 — **[metadata only]**
- **Ridley, M., & Pawlick-Potts, D. (2021).** Algorithmic literacy and the role for libraries. *Information Technology and Libraries, 40*(2). https://doi.org/10.6017/ital.v40i2.12963 — **[F, pp. 1–4]**
- **Sharmin, S., Špakov, O., & Räihä, K.-J. (2015).** Dynamic text presentation in print interpreting – An eye movement study of reading behaviour. *International Journal of Human-Computer Studies, 78*, 17–30. https://doi.org/10.1016/j.ijhcs.2015.01.010 — **[A]**
- **Sharmin, S., et al. *[co-authors and pages: verify]* (2016).** The reading process of dynamic text – A linguistic approach to an eye movement study. *SKY Journal of Linguistics, 29*. — **[A]** The packet lists Sharmin as sole author; the Consensus record lists more than one author.
- **Timkey, W., Huang, K.-J., Oh, B.-D., Prasad, G., Arehalli, S., Linzen, T., & Dillon, B. (2026).** Eye movements reveal a dissociation between prediction and structural processing difficulty in language comprehension. *Proceedings of the National Academy of Sciences, 123*(32), e2532230123. https://doi.org/10.1073/pnas.2532230123 — **[A + preprint read in part]**
- **Valsecchi, M., Gegenfurtner, K. R., & Schütz, A. C. (2013).** Saccadic and smooth-pursuit eye movements during reading of drifting texts. *Journal of Vision, 13*(10), 8. https://doi.org/10.1167/13.10.8 — **[A]**
- **Zhou, H., Zhang, J., Lou, J., Liu, Y., Lu, C., Qu, J., & Li, J. (2026).** *Deep interaction: An efficient human-AI interaction method for large reasoning models* [Preprint]. arXiv:2607.14049. — **[F, method/eval][P]**
- **Zhu, X., Le Truong, K., Fogliato, R., Swamy, G., Zhang, W., Yang, M., Ye, L., Liu, B., Liu, M., Ilyas, A., & Wu, Z. S. (2026).** *Justified or just convincing? Error verifiability as a dimension of LLM quality* [Preprint]. arXiv:2604.04418. — **[F, §1–7.1][P]**
- **Zhu, H., Wang, J., Xie, L., Ma, R., Sun, Y., Liu, F., Zheng, C., & Li, Q. (2026).** Just-in-time tokens: Adaptive token pacing for cognitive-friendly LLM streaming. In *Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–8). https://doi.org/10.1145/3772363.3798936 — **[metadata + search snippet only]**

Also verified as records, not added (peripheral or already covered): Räihä & Sharmin (2014, NordiCHI, 10.1145/2639189.2639242); Turner, Iqbal & Dumais (2015, UbiComp, 10.1145/2800835.2804331); Tang et al. (2024, VL/HCC, 10.1109/VL/HCC60511.2024.00015); Pang et al. (2025, arXiv:2506.23678); Sharmin, Špakov & Räihä (2013, gaze-based auto-scrolling, 10.1145/2509315.2509319).

## R2.5 Named in the packet, not verified, not added

Bawden (2024) and Hagendorff (2024) — no full reference given; Westheimer & McKee (1975); Buettner et al. (1985); O'Regan (1990, 1992); McConkie et al. (1988); Engbert et al. (SWIFT); Reichle & Reingold (2013); Harvey et al. (2019); Singer Trakhman (2016); Mangen & van der Weel (2016) — record exists in *Literacy*, 10.1111/lit.12086, not read; Zwaan & Radvansky (1998); Radvansky & Zacks (2017); DuBrow et al.; Chen et al. (2025, CFFs); Ashktorab et al. (2024); Fok & Weld (2024); Ibrahim et al. (2025); Aggarwal et al. (2026); Zhou et al. (2026, verifiability); Kosch et al. (2023); Chiossi et al. (2024).
