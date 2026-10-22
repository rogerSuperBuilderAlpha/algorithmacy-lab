# Spaces in the Stream: Literature Review

> **Drafted by Claude (Opus 5.5) for Roger Hunt, 20 October 2026. Every sentence below is my draft, not
> your text.** Citations are APA 7, matching your proposal. Each claim rests on a source I read in full or
> on its database abstract; `notes/` and `../LITERATURE_REVIEW.md` hold the locators. Where a claim comes
> from your proposal and I could not check it against the source, it carries a **[flag]**. Read-aloud is
> yours; I ran no AI-review loop on this prose.

---

A reader who watches a chatbot answer does something none of the reading studies I review was designed to test: they read
a text that a machine is still writing. The words arrive at the machine's pace, the page scrolls without
the reader's hand, and the reader must decide, while the text is still moving, whether to accept it, look
back at it, check it, or stop it. Four literatures bear on that situation, and none of them addresses it
directly. The reading studies show how the eyes find words, follow moving text, and look back to repair understanding. The event-cognition studies show how people divide continuous experience into units and when they update what they know. Ecological and sensorimotor accounts explain why a reader's control over the text matters to what the reader sees. The automation studies show why people supervising a fluent system stop checking it. I take these in turn, then show what each implies for the decision spaces
proposed in this paper and what none of them has yet tested.

## The space as an instrument of reading

The history of the written page frames the problem. Saenger (1997) traces the separation of words to Irish
and English scribes of the seventh and eighth centuries and ties the change to the physiology of reading:
once spaces marked word boundaries, readers could find words by eye rather than by voice **[flag: your
summary; I did not read Saenger this session]**. Modern eye-movement research measures what the space does.
Rayner, Fischer and Pollatsek (1998) found that removing or filling the spaces in English text slowed
reading and altered where the eyes first landed in words: reading rate fell by 54% for sentences and 44%
for passages, and regressions rose from 9.7% to 17.3% of eye movements (pp. 1132, 1141) **[checked
2026-10-20 against the full text; the proposal's "about half" matches the abstract's "approx. 50%"]**. Drieghe, Fitzsimmons and Liversedge (2017)
replicated the cost of unspaced text and found "rather limited evidence" that readers spread processing
across neighbouring words: the reading system, they conclude, "prefers narrowly focused processing of a
single word" when spaces make segmentation easy. McDonald (2006) adds a constraint that matters for a
stream: readers gain preview benefit only from the word they are about to land on.

A chatbot, however, prints spaces. If the analogy to *scriptura continua* stopped at the word, a critic
could answer that AI text already has what the Insular scribes supplied. Parkes (1992) offers the second
half of the history. *Pause and Effect*, his history of punctuation in the West, gives its third chapter
the title "Grammar of Legibility," and the book treats punctuation as a means of resolving structural
uncertainty rather than marking breath **[flag: chapter title and book record verified; Parkes's specific
claims need checking against the book]**. Read together, Saenger and Parkes describe two layers of
segmentation: the space that tells the eye where a word ends, and the mark that tells the reader where a
unit of sense ends. Streaming AI interfaces supply the first layer and remove the second. They print words
in order but deliver every clause, claim and inference at the same steady rate, so that nothing in the
display tells the reader where one decision ends and the next begins. The decision space proposed here
belongs to Parkes's layer, not Saenger's.

## Reading text that moves

Moving text costs readers integration while sparing word recognition. Harvey, Godwin, Fitzsimmons,
Liversedge and Walker (2017) tracked readers through horizontally scrolling text and found fewer and
longer fixations with shorter forward and backward saccades; word-length and word-frequency effects
survived, but the early benefit of predictable words disappeared. Harvey and Walker (2018) then found that
literal comprehension held up under scrolling while inference questions suffered, and they named the
mechanism: in a scrolling format, returning to earlier text is harder. Valsecchi, Gegenfurtner and Schütz
(2013) showed what the eyes do instead. Readers follow drifting text with an alternation of smooth pursuit
and saccades, the gain of pursuit rises after each saccade, and the familiar landmarks of static reading —
the preferred viewing location, the optimal viewing position — carry over to the moving page. Following the "automated cursor" of a chatbot turns part of reading into tracking.

Readers also lose the strategic movement through text that static pages allow. Haverkamp, Bråten, Latini
and Salmerón (2023) gave 145 students a 1,492-word text on a phone or tablet, by scrolling or paging.
Paging produced more backtracking (3.53 vs 2.49 instances, *p* = .012); scrolling produced fewer but
longer, less controlled backtracks; integrated understanding favoured paging only as a trend
(*p* = .066). Öquist and Lundin (2007) found earlier that phone readers got through paged text faster than
scrolled or serially presented text with no loss of comprehension.

Two research programmes come closer to the chatbot case than any scrolling study. Sharmin, Špakov and
Räihä (2015) eye-tracked 20 participants reading text that a print interpreter typed live for
hard-of-hearing clients. Text that appeared word by word produced significantly more rereading and
regressions than text that appeared letter by letter, regressions started more often at sentence-final
words, and readers reread mistyped or abbreviated words more often; 18 hard-of-hearing participants showed
the same trend. Sharmin and colleagues (2016) then analysed where regressions landed in letter-by-letter
text: 90.8% of first and second landing points were content words, against 57.1% of words in the text,
and nouns were the likeliest targets. 

Park and Lee (2024) carried the question into generative chatbots. Thirty-six participants watched four
generation styles copied from 2023 interfaces. Text generated at the bottom of the screen — ChatGPT's
auto-scrolling follow-up turn, Bing's upward growth — drew more fixations, longer total fixation time and
larger saccades than Bard's whole-text display, and fixation starts piled up in the lowest screen regions,
where new words appeared. The study measured no comprehension, regression or error detection. The pace
of that new text, meanwhile, belongs to the server. Liu et al. (2024) estimate average reading consumption
at 4.8 tokens per second and observed one serving system delivering 11.2 tokens per second on a real
request trace. Xiao and Yang (2025) found that 99% of their crowdsourced readers were comfortable at or
below 21.2 words per second on easy text and 12.0 on hard text, against roughly 45 words per second from a
commercial API; streaming, they write, "transforms text from a static payload into a dynamic, time-based
medium." Bhat (2025) supplies the cost on the trust side: 103 participants rated a typing-simulation
display as more competent, warm and trustworthy than the same text shown whole, with no change in
perceived effectiveness.

## Looking back

Streaming threatens the regression most. Booth and Weger (2013) note that regressions make
up 15%–25% of eye movements in normal reading and ask what they are for. When they made a just-read
sentence illegible while preserving every word's position, readers regressed less, landed less
accurately, and gained nothing in comprehension from the regressions they still made; when they swapped a
word during a regression, readers adopted the new word's meaning without noticing. Readers look back to
reread, not to cue memory by location. Booth and Weger even foresaw the present case, predicting that
readers "of scrollable text on small screens" face situations in which "rereading is often impossible."
Schotter, Tran and Rayner (2014) reached the same conclusion from the other side: masking each word after
the eyes left it, so that regressions found nothing, reduced comprehension for 40 readers of single
sentences, ambiguous or not (b = −0.92, z = 5.09; p. 1221) **[checked 2026-10-20 against the full text]**.
Metzner, von der Malsburg, Vasishth and Rösler (2017) found that free reading beat word-by-word
presentation only on trials in which the eyes regressed to an anomaly, and Benedetto et al. (2015) found
that a commercial serial-presentation app, by suppressing regressions and preview, hurt literal
comprehension.

Timkey et al. (2026) explain what regressions do that forward reading cannot. In a study of 368 readers
and 409 language-model surprisal estimates, early reading of syntactically ambiguous sentences tracked
surprisal, but disambiguation added a rereading cost that surprisal did not explain. Their conclusion
divides the labour: surprisal "can capture routine structure-building, but not the cost of detecting or
correcting errors in the structure-building process." Detecting and correcting errors is what a supervisor of AI output must do, and readers do it by looking back.

## Where the break falls

A break in the text helps only if it lands on a unit the reader is already parsing. Tsoukala, Vogelzang and
Tsimpli (2025) placed line breaks so that they either coincided with clause boundaries or cut clauses
across lines, and tested 39 readers with self-paced reading and 29 with eye tracking. Aligned breaks sped
the disambiguating region; repeated misaligned breaks slowed it (first-pass *d* = 0.32, total time
*d* = 0.41) and, in self-paced reading, lowered comprehension in the critical condition (OR = 0.38). The
readers also learned: after several misaligned lines they stopped treating line ends as cues to closure.
Tsoukala and colleagues call line breaks "good" or "bad" cues to structure, and their eye-tracking display
revealed text one line at a time — closer to a stream than most reading studies get.

The text-signalling literature reaches the same point through headings. Hyönä and Lorch (2004) found that
topic headings sped first-pass reading of topic sentences and steered later look-backs to them, and Lorch
(1989) reviewed the general pattern: signals improve memory for what they cue. Segmentation is not free,
though. Keenan (1984) found that one phrase per line slowed reading, which he traced to uneven line
lengths, and Koornneef (2024) found that sentence-by-sentence presentation helped beginning readers
comprehend without the extra wrap-up time explaining the gain. The lesson for decision spaces is double:
place the break where the unit ends, and expect a misplaced break to cost more than no break.

## New text captures the eyes

Every streamed word is an abrupt onset. Yantis and Jonides (1984) showed that an item appearing abruptly in
a display captures attention in visual search, and Wolfe's (2021) Guided Search model folds such salience
into a priority map alongside goals, history and value. Both papers limit the claim. Yantis and Jonides
found capture "only when the visual field contains but one such event" (p. 617), and Wolfe calls
bottom-up salience "short-lived" (p. 1069) **[checked 2026-10-20 against the full texts]**.
Park and Lee's (2024) fixation starts, clustered where new text appeared, fit onset capture. A stream
therefore pulls the eyes forward at the same moment a doubt pulls them back, and a pause that stops new
onsets removes the forward pull for as long as it lasts.

## Events and boundaries

Event segmentation theory supplies the second function of a decision space. Zacks, Speer and Reynolds
(2009) summarise the theory: perceivers maintain event models that predict what comes next; when
predictions fail, the model updates and the moment registers as an event boundary. Kurby and Zacks (2008)
add that people segment at several timescales at once, that activity in posterior temporal, parietal and
lateral frontal cortex rises transiently at boundaries in observed activity, and that segmentation relates
to working-memory updating and long-term memory. Zacks and colleagues (2009) carried the theory into
reading. Readers slowed at clauses that other readers marked as event boundaries — about 108 ms for each
10% rise in boundary agreement — and changes in characters, goals, causes and objects partly mediated the
slowdown. Their first experiment already contained a stream: one group read clauses at a software-set pace,
3.35 words per second, with no way to review earlier clauses, and still segmented the narrative
hierarchically.

Kurby and Zacks (2012) showed what happens at a boundary. Readers who typed their thoughts while reading
mentioned a situation dimension more when it changed, which is incremental updating, and mentioned goals
more at fine boundaries even when goals had not changed (OR = 2.29, *z*(926) = 2.87), which is global
updating. Kumar et al. (2023) linked boundaries to a language model directly: human boundaries in story
listening tracked Bayesian surprise computed from GPT-2.

The interruption literature tests the same structure from the outside. Bailey and Konstan (2006) found
that peripheral tasks arriving during a primary task, rather than between tasks, cost 3%–27% more time,
doubled errors, and raised annoyance by 31%–106%. Powers and Scerbo (2023) tied the effect to event
segmentation: interruptions at coarse breakpoints were no worse than none, while interruptions at fine
breakpoints lengthened resumption and raised workload. Together these studies predict that a pause landing
on a boundary costs little, and a pause landing mid-unit costs something.

## Perception, action and the place of text

The third function of a decision space, aiding regression, depends on text staying where the reader left
it. O'Regan and Noë (2001) hold that "seeing is a way of acting": visual experience consists in mastery of
the laws that link movement to sensory change. O'Regan (2011) develops the account, and Gibson (1979)
grounds perception in what the environment affords **[flag: both books from your proposal; not read this
session]**. Mangen, Olivier and Velay (2019) carry these ideas into reading media. Citing Gibson and
O'Regan and Noë, they compared 50 readers of a 28-page story on a Kindle or in print. Most measures did
not differ, but print readers reconstructed the plot's chronology better (*t*(48) = 2.03), and the
ability to locate events in the text predicted that reconstruction; fixed text, they argue, provides
"material placeholders" that off-load memory. They chose a Kindle precisely because scrolling, in work
they cite, impairs readers' mental map of a text. Mangen, Walgermo and Brønnick (2013) found that 72 tenth
graders comprehended long texts better on paper than as PDFs on screen, and Delgado and colleagues' (2018)
meta-analysis of 54 experiments, as Mangen and colleagues summarise it, found a paper advantage that was
stronger when reading was time-constrained. A stream is both screen-based and paced by someone else. It
removes the reader's control over when text moves, and with it the stable location a regression needs.

## Supervising fluent automation

The automation studies explain why supervisors stop looking back at all. Lee and See (2004) placed trust
at the centre of reliance when a system is too complex to understand fully, and Endsley (2017) named the
"automation conundrum": as automation grows more reliable and autonomous, operators' situation awareness
and capacity to take over decline. Parasuraman and Manzey (2010) integrated complacency and automation bias
under attention — complacency, they found, arises "under conditions of multiple-task load, when manual
tasks compete with the automated task for the operator's attention" — and documented a
"looking-but-not-seeing" effect: some operators sampled every parameter needed to catch an automation
error and still accepted it. A fixation, then, does not prove a check.

 Kim et al. (2025) found, with 308 participants, that
explanations raised agreement with correct and incorrect answers alike, while clickable sources and
visible inconsistencies reduced agreement with wrong ones; 189 participants never clicked a source.
Steyvers et al. (2025) found that longer explanations raised users' confidence without raising accuracy.
Zhu et al. (2026) measured whether justifications help raters tell right answers from wrong ones and found
that post-training raised accuracy without raising that verifiability; in one model, preference
optimisation made the justifications of wrong answers harder to flag, and only methods that added outside
information helped. Liu et al. (2026) traced overreliance in behaviour: heavy over-reliers copied whole
responses and navigated coarsely to prominent parts of the screen. Cho and Lim (2026) eye-tracked 23
participants viewing four source-attribution layouts on static, non-clickable chatbot screens. The fastest
layout drew a first fixation on its sources in 0.96 s and the slowest in 15.65 s, yet no self-report
measure differed and gaze did not track trust: "Attention moved without moving judgment." Prajod et al.
(2026) found that a terse AI-use label raised fixation duration and saccade counts relative to a detailed
one, with no change in workload ratings — a cue that signals a problem without resolving it sends the eyes
searching.

Interface interventions can restore some checking, at a price. Buçinca, Malaya and Gajos (2021) tested
cognitive forcing functions with 199 participants: deciding before seeing the AI, requesting its advice on
demand, or waiting 30 seconds while "the AI is processing." On incorrect AI suggestions, forcing reduced
overreliance (48% vs 64% followed the wrong advice in carb-source detection, *d* = .36), but participants
liked these designs least. The waiting condition matters here, because a bare pause, with no structure,
already helped. Ghosh, Sarkar, Lindley and Poelitz (2026) found, with 214 participants reviewing AI-written
plans, that a prompt to identify the plan's assumptions reduced overreliance without raising workload.

## Supervising agents: when judgment arrives

Oversight of AI agents turns the timing of a check into the main variable. Chen et al. (2026) ran 48
participants through 192 live sessions with a computer-use agent. Users blocked 29 of 138 problematic
actions that reached execution, and 56% of failures arose because the interface asked for judgment before
or after the risky moment. They conclude that oversight "depends less on maximizing control than on
aligning authority, timing, and attention with decision-critical moments." Grunde-McLaughlin et al. (2026)
found that redesigned agent traces cut the time people took to find errors without improving accuracy.
Zhou et al. (2026) let users edit a finished chain of reasoning in place and reported correction gains of
more than 25% with about 40% fewer tokens, though most of their results come from an automated agent
simulating human edits. Gaze can track these judgments: Wu, Wang, Langer and Feit (2025) distinguished
over-, under- and appropriate reliance from verification-related gaze, and Cao and Huang (2022) found that
the share of gaze on an AI suggestion correlated with agreement.

## From algorithmic literacy to algorithmacy

Ridley and Pawlick-Potts (2021) name the competence at stake but not its perceptual form. They define algorithmic literacy as "the skill, expertise, and awareness" to understand
algorithms, recognise their use, apply algorithmic tools, assess their social effects, and "position the
individual as a co-constituent in algorithmic decision-making." Their definition describes what a person
knows. It says nothing about what a person must do with the eyes, in real time, while an algorithm speaks.
The studies above describe that second competence piece by piece: tracking a moving text, holding a place
to return to, recognising where one unit of sense ends, and resisting a fluent source. Algorithmacy, in the
sense this paper uses, names their combination.

## What remains untested

The literatures converge on a design without testing it. Reading research shows that moving text costs
integration, that readers regress to repair meaning, and that breaks aligned with linguistic units help
while misaligned breaks hurt. Event cognition shows that readers update at boundaries and slow down to do
so. Interruption research shows that breakpoints placed at coarse boundaries cost little. Automation
research shows that fluent output suppresses checking and that well-timed friction restores some of it.
I searched Consensus, OpenAlex, arXiv and the web on 20 October 2026 for a study that segments a
streaming language-model response at decision units and measures fixations, regressions and error
detection against a continuous stream and an arbitrarily interrupted one. I found none. Park and Lee
(2024) is the only eye-tracking study of chatbot text generation I found, and it measures neither
comprehension nor error detection. Resulbegoviq et al.'s (2026) systematic review of 23 eye-tracking
studies of AI-generated content describes no comparison of streamed with static text, though its
eligibility rules would have excluded some designs. The experiment proposed here is that comparison.

---

## References

Bailey, B. P., & Konstan, J. A. (2006). On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state. *Computers in Human Behavior, 22*(4), 685–708. https://doi.org/10.1016/j.chb.2005.12.009

Benedetto, S., Carbone, A., Pedrotti, M., Le Fevre, K., Bey, L. A. Y., & Baccino, T. (2015). Rapid serial visual presentation in reading: The case of Spritz. *Computers in Human Behavior, 45*, 352–358. https://doi.org/10.1016/j.chb.2014.12.043

Bhat, M. (2025). How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131

Booth, R. W., & Weger, U. W. (2013). The function of regressions in reading: Backward eye movements allow rereading. *Memory & Cognition, 41*(1), 82–97. https://doi.org/10.3758/s13421-012-0244-y

Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287

Cao, S., & Huang, C.-M. (2022). Understanding user reliance on AI in assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 6*(CSCW2), 1–23. https://doi.org/10.1145/3555572

Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026). *Comparing human oversight strategies for computer-use agents* [Preprint]. arXiv. https://arxiv.org/abs/2604.04918

Cho, J., & Lim, D. (2026). How source attribution visualization shapes user attention and preference: An eye-tracking study of four AI chatbot layouts. *Journal of Eye Movement Research, 19*(4), Article 89. https://doi.org/10.3390/jemr19040089

Delgado, P., Vargas, C., Ackerman, R., & Salmerón, L. (2018). Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. *Educational Research Review, 25*, 23–38. https://doi.org/10.1016/j.edurev.2018.09.003

Drieghe, D., Fitzsimmons, G., & Liversedge, S. P. (2017). Parafoveal preview effects in reading unspaced text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(10), 1701–1716. https://doi.org/10.1037/xhp0000441

Endsley, M. R. (2017). From here to autonomy. *Human Factors, 59*(1), 5–27. https://doi.org/10.1177/0018720816681350

Ghosh, A., Sarkar, A., Lindley, S., & Poelitz, C. (2026). *An experimental comparison of cognitive forcing functions for execution plans in AI-assisted writing: Effects on trust, overreliance, and perceived critical thinking* [Preprint]. arXiv. https://arxiv.org/abs/2601.18033

Gibson, J. J. (1979). *The ecological approach to visual perception*. Houghton Mifflin.

Grunde-McLaughlin, M., Mozannar, H., Murad, M., Chen, J., Amershi, S., & Fourney, A. (2026). *Overseeing agents without constant oversight: Challenges and opportunities* [Preprint]. arXiv. https://arxiv.org/abs/2602.16844

Harvey, H., Godwin, H. J., Fitzsimmons, G., Liversedge, S. P., & Walker, R. (2017). Oculomotor and linguistic processing effects in reading dynamic horizontally scrolling text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(3), 518–536. https://doi.org/10.1037/xhp0000329

Harvey, H., & Walker, R. (2018). Reading comprehension and its relationship with working memory capacity when reading horizontally scrolling text. *Quarterly Journal of Experimental Psychology, 71*(9), 1887–1897. https://doi.org/10.1080/17470218.2017.1363258

Haverkamp, Y. E., Bråten, I., Latini, N., & Salmerón, L. (2023). Is it the size, the movement, or both? Investigating effects of screen size and text movement on processing, understanding, and motivation when students read informational text. *Reading and Writing, 36*(7), 1589–1608. https://doi.org/10.1007/s11145-022-10328-9

Hyönä, J., & Lorch, R. F. (2004). Effects of topic headings on text processing: Evidence from adult readers' eye fixation patterns. *Learning and Instruction, 14*(2), 131–152. https://doi.org/10.1016/j.learninstruc.2004.01.001

Keenan, S. A. (1984). Effects of chunking and line length on reading efficiency. *Visible Language*. *[volume and pages not verified]*

Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025). Fostering appropriate reliance on large language models: The role of explanations, sources, and inconsistencies. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–19). ACM. https://doi.org/10.1145/3706598.3714020

Koornneef, A. (2024). On the readability of texts presented in sentence-by-sentence segments to beginner readers: Evidence from self-paced reading and eye tracking. *Reading and Writing, 37*(1), 69–87. https://doi.org/10.1007/s11145-023-10423-5

Kumar, M., Goldstein, A., Michelmann, S., Zacks, J. M., Hasson, U., & Norman, K. A. (2023). Bayesian surprise predicts human event segmentation in story listening. *Cognitive Science, 47*(10), e13343. https://doi.org/10.1111/cogs.13343

Kurby, C. A., & Zacks, J. M. (2008). Segmentation in the perception and memory of events. *Trends in Cognitive Sciences, 12*(2), 72–79. https://doi.org/10.1016/j.tics.2007.11.004

Kurby, C. A., & Zacks, J. M. (2012). Starting from scratch and building brick by brick in comprehension. *Memory & Cognition, 40*(5), 812–826. https://doi.org/10.3758/s13421-011-0179-8

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392

Liu, C., Zhou, Q., Shen, X., Liu, X. B., Wu, T., & Chen, X. A. (2026). Behavioral indicators of overreliance during interaction with conversational language models. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–23). ACM. https://doi.org/10.1145/3772318.3790332

Liu, J., Chung, J.-W., Wu, Z., Lai, F., Lee, M., & Chowdhury, M. (2024). *Andes: Defining and enhancing quality-of-experience in LLM-based text streaming services* [Preprint]. arXiv. https://arxiv.org/abs/2404.16283

Lorch, R. F. (1989). Text-signaling devices and their effects on reading and memory processes. *Educational Psychology Review, 1*(3), 209–234. https://doi.org/10.1007/BF01320135

Mangen, A., Olivier, G., & Velay, J.-L. (2019). Comparing comprehension of a long text read in print book and on Kindle: Where in the text and when in the story? *Frontiers in Psychology, 10*, Article 38. https://doi.org/10.3389/fpsyg.2019.00038

Mangen, A., Walgermo, B. R., & Brønnick, K. (2013). Reading linear texts on paper versus computer screen: Effects on reading comprehension. *International Journal of Educational Research, 58*, 61–68. https://doi.org/10.1016/j.ijer.2012.12.002

McDonald, S. A. (2006). Parafoveal preview benefit in reading is only obtained from the saccade goal. *Vision Research, 46*(26), 4416–4424. https://doi.org/10.1016/j.visres.2006.08.027

Metzner, P., von der Malsburg, T., Vasishth, S., & Rösler, F. (2017). The importance of reading naturally: Evidence from combined recordings of eye movements and electric brain potentials. *Cognitive Science, 41*(S6), 1232–1263. https://doi.org/10.1111/cogs.12384

O'Regan, J. K. (2011). *Why red doesn't sound like a bell: Understanding the feel of consciousness*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199775224.001.0001

O'Regan, J. K., & Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973. https://doi.org/10.1017/S0140525X01000115

Öquist, G., & Lundin, K. (2007). Eye movement study of reading text on a mobile phone using paging, scrolling, leading, and RSVP. In *Proceedings of the 6th International Conference on Mobile and Ubiquitous Multimedia* (pp. 176–183). ACM. https://doi.org/10.1145/1329469.1329493

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055

Park, H., & Lee, Y. (2024). The effect of text movement on eye movements in generative AI chatbots. *Archives of Design Research, 37*(4), 181–197. https://doi.org/10.15187/adr.2024.08.37.4.181

Parkes, M. B. (1992). *Pause and effect: An introduction to the history of punctuation in the West*. Scolar Press. *[verify edition; Routledge reissue 2016]*

Powers, S. A., & Scerbo, M. W. (2023). Examining the effect of interruptions at different breakpoints and frequencies within a task. *Human Factors, 65*(1), 22–36. https://doi.org/10.1177/00187208211009010

Prajod, P., Cools, H., Röggla, T., Cesar, P., & El Ali, A. (2026). *Towards gaze-informed AI disclosure interfaces: Eye-tracking attentional and cognitive load while reading AI-assisted news* [Preprint]. arXiv. https://arxiv.org/abs/2605.14999

Rayner, K., Fischer, M. H., & Pollatsek, A. (1998). Unspaced text interferes with both word identification and eye movement control. *Vision Research, 38*(8), 1129–1144. https://doi.org/10.1016/S0042-6989(97)00274-5

Resulbegoviq, H., Hlebec, V., Pejić Bach, M., & Stamatović, I. (2026). Eye tracking and AI-generated content: A systematic literature review of visual attention, cognitive processing, and user engagement. *Journal of Eye Movement Research, 19*(5), Article 97. https://doi.org/10.3390/jemr19050097

Ridley, M., & Pawlick-Potts, D. (2021). Algorithmic literacy and the role for libraries. *Information Technology and Libraries, 40*(2). https://doi.org/10.6017/ital.v40i2.12963

Saenger, P. (1997). *Space between words: The origins of silent reading*. Stanford University Press. https://doi.org/10.1515/9781503619081

Schotter, E. R., Tran, R., & Rayner, K. (2014). Don't believe what you read (only once): Comprehension is supported by regressions during reading. *Psychological Science, 25*(6), 1218–1226. https://doi.org/10.1177/0956797614531148

Sharmin, S., et al. *[co-authors and pages: verify]* (2016). The reading process of dynamic text – A linguistic approach to an eye movement study. *SKY Journal of Linguistics, 29*.

Sharmin, S., Špakov, O., & Räihä, K.-J. (2015). Dynamic text presentation in print interpreting – An eye movement study of reading behaviour. *International Journal of Human-Computer Studies, 78*, 17–30. https://doi.org/10.1016/j.ijhcs.2015.01.010

Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X., Mayer, L. W., & Smyth, P. (2025). What large language models know and what people think they know. *Nature Machine Intelligence, 7*(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7

Timkey, W., Huang, K.-J., Oh, B.-D., Prasad, G., Arehalli, S., Linzen, T., & Dillon, B. (2026). Eye movements reveal a dissociation between prediction and structural processing difficulty in language comprehension. *Proceedings of the National Academy of Sciences, 123*(32), e2532230123. https://doi.org/10.1073/pnas.2532230123

Tsoukala, A., Vogelzang, M., & Tsimpli, I. M. (2025). The influence of text segmentation on garden path processing: Evidence from self-paced reading and eye-tracking. *Language and Cognition, 17*, e58. https://doi.org/10.1017/langcog.2025.10009

Valsecchi, M., Gegenfurtner, K. R., & Schütz, A. C. (2013). Saccadic and smooth-pursuit eye movements during reading of drifting texts. *Journal of Vision, 13*(10), 8. https://doi.org/10.1167/13.10.8

Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review, 28*(4), 1060–1092. https://doi.org/10.3758/s13423-020-01859-9

Wu, Z., Wang, Y., Langer, M., & Feit, A. M. (2025). RelEYEance: Gaze-based assessment of users' AI-reliance at run-time. *Proceedings of the ACM on Human-Computer Interaction, 9*(3), 1–18. https://doi.org/10.1145/3725841

Xiao, C., & Yang, B. Z. (2025). Streaming, fast and slow: Cognitive load-aware streaming for efficient LLM serving. In *Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology* (pp. 1–13). ACM. https://doi.org/10.1145/3746059.3747721

Yantis, S., & Jonides, J. (1984). Abrupt visual onsets and selective attention: Evidence from visual search. *Journal of Experimental Psychology: Human Perception and Performance, 10*(5), 601–621. https://doi.org/10.1037/0096-1523.10.5.601

Zacks, J. M., Speer, N. K., & Reynolds, J. R. (2009). Segmentation in reading and film comprehension. *Journal of Experimental Psychology: General, 138*(2), 307–327. https://doi.org/10.1037/a0015305

Zacks, J. M., Speer, N. K., Swallow, K. M., Braver, T. S., & Reynolds, J. R. (2007). Event perception: A mind-brain perspective. *Psychological Bulletin, 133*(2), 273–293. https://doi.org/10.1037/0033-2909.133.2.273

Zhou, H., Zhang, J., Lou, J., Liu, Y., Lu, C., Qu, J., & Li, J. (2026). *Deep interaction: An efficient human-AI interaction method for large reasoning models* [Preprint]. arXiv. https://arxiv.org/abs/2607.14049

Zhu, X., Le Truong, K., Fogliato, R., Swamy, G., Zhang, W., Yang, M., Ye, L., Liu, B., Liu, M., Ilyas, A., & Wu, Z. S. (2026). *Justified or just convincing? Error verifiability as a dimension of LLM quality* [Preprint]. arXiv. https://arxiv.org/abs/2604.04418
