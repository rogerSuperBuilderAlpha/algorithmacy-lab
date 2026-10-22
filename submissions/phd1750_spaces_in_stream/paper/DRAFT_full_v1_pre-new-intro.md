# Spaces in the Stream: Algorithmacy and the Perception of Decision Spaces in Streaming AI Output — A Theory and Research Agenda [D1]

> **Full draft, version 1. Drafted by Claude (Opus 5.5) for Roger Hunt, 20 October 2026, from Roger's restructured outline.**
>
> **How to read this file:**
> - **Everything in this file is Claude's drafting, except text inside `[ROGER] … [/ROGER]`.** ROGER text is your wording, copied unchanged from your outline or from `abstract_intro_edit.md`. Your earlier flags (F1–F17) stay attached to it.
> - **`[D#]`** points to a discrepancy listed at the end of the file. Each one gives what the outline says, what the source says (with a locator), and what the draft does. The decision on each is yours.
> - **`[NEEDS: …]`** marks a claim that rests on a source not read this session (Saenger, Parkes, Gibson, O'Regan & Noë, Oberschelp) or on a decision only you can make.
> - Sources marked [A] in the outline were read as abstract only. The draft cites them only for what their abstracts state.
> - I wrote every sentence by hand, paragraph by paragraph. There is no AI-review or rewrite pass; your read-aloud is the last gate.
> - **Person.** Your outline's abstract says "we." The body uses "I", because you are the sole author and your style guide says solo work uses "I" [D2].

---

## Abstract

[ROGER] This theoretical article addresses a paradox in human oversight of generative artificial intelligence: streaming conversational interfaces accelerate perceived authority and trust while systematically degrading supervisory scrutiny and error detection. [D3] We propose that this failure is structural. Natural reading depends on three perceptual invariants: stable visual targets, event boundaries that trigger situation-model updating, and unconstrained regressive saccades for structural repair. Streaming interfaces eliminate all three, pulling visual attention to an autonomously advancing leading edge and co-opting judgment points into an unbroken performance of textual fluency. Drawing on the historical transition from continuous script (scriptio continua) to word separation, we formulate the perceptual layer of algorithmacy theory. We define decision spaces as the opaque, co-opted junctures in an automated process where judgment is required, and marking as the interface intervention that renders them perceptible. We model supervisory navigation as the product of decision-space perception and the reader's mental model of the intermediary (G = F × MI), articulate six formal propositions, derive thirteen directional predictions, specify an empirical eye-tracking testing agenda, and outline design implications for stateful generative interfaces. [/ROGER]

**Keywords:** algorithmacy; decision spaces; text streaming; large language models; eye movements; event segmentation; automation supervision; overreliance

---

## 1. INTRODUCTION

[ROGER] When users watch a chatbot responding to a query/prompt, their eyes track the text as it appears. Words stream incrementally, expanding and scrolling, forcing the user to track the text as if following an automated cursor. In eye-tracking evaluations of streaming interfaces, this dynamic display fundamentally alters oculomotor routines: bottom-generated scrolling text increases total fixation counts, prolongs cumulative gaze duration, and expands saccade amplitudes, with initial fixations tightly clustered at the leading visual edge where new tokens emerge (Park & Lee, 2024). [F3] Under these conditions, the stream is paced by the server, not the reader. [/ROGER]

The evidence on what this does to supervision points in different directions. Bhat (2025) showed 103 participants the same kind of GPT-3.5 answers typed out sentence by sentence or displayed whole. The typed display raised ratings of the AI's competence, trustworthiness and persuasiveness, yet left ratings of its effectiveness unchanged (F = 0.16, p = .69). Kim et al. (2025) found that explanations raised agreement with a language model's answers whether those answers were right or wrong: when the model's answer was wrong, participants' accuracy was 17.2% with an explanation and 21.8% without one. Meanwhile the pace of the stream answers to the server. Xiao and Yang (2025) measured the fastest streaming speed that 99% of readers found comfortable at 21.20 words per second for an easy passage and 11.97 for a complex one, against roughly 45 words per second from a commercial API. [D4] So readers credit streamed text with more authority, they agree more with fluent answers whether right or wrong, and they read at a pace set by compute. None of these studies varied where, inside the stream, a reader has a place to stop.

That variable is the subject of this paper. I argue that supervising streamed AI output means navigating decision spaces: the opaque, co-opted points in an automated process where a judgment is required — accept, check, reject, redirect — but the process does not present them as such. Streaming hides decision spaces by removing the boundaries and look-backs on which reading relies. Marking them makes them perceptible, and navigating them is what I call algorithmacy.

The claim rests on two bodies of evidence. The first is basic research on reading, visual attention and event perception: how the eyes find targets in text, how readers segment what they read into events, and why they look back (Section 2). The second is applied research on the supervision of automation and of language models: complacency, recommendation framing, overreliance and the friction designed to counter it (Section 3). Neither literature, on its own, addresses the internal structure of a stream. Together they predict what that structure should do.

The paper's scope is narrow by design. It treats the *perceptual* layer of algorithmacy: how a reader comes to see a decision space inside a streamed response, and what happens to the eyes and to supervision when the interface marks it. I set aside the organizational and political layers of algorithmacy, which my dissertation treats, along with model architecture, prompting technique and user training. One limit deserves stating at the outset. Marking is necessary for navigation in an unmarked stream, but it is not sufficient. A mark makes a decision space perceptible; the reader still has to fill it, just as the written space between words never made anyone literate.

Current accounts change the stream around its edges. Pacing research changes the rate at which tokens arrive (Xiao & Yang, 2025; Zhu et al., 2026). Friction research places obstacles before an interaction (Cox et al., 2016), before or around access to a model (Arun et al., 2026; Collins et al., 2024), or inside the model itself (Disley & Khan, 2026). Automation research studies recommendations and transparency displays that arrive as discrete events (Gegoff et al., 2025; Tatasciore et al., 2026). I searched arXiv, Consensus and the web on 20 October 2026 and found no work that marks decision points inside a streamed AI response, or that places interface boundaries inside one.

The theory can be stated in six points, which Section 4 develops as formal propositions:

1. Literacy fills the gap between written marks and linguistic meaning. Algorithmacy fills the gap at an automated process's decision spaces.
2. In streamed AI output, decision spaces arrive inside a reading task that the reader does not pace.
3. Reading depends on stable spatial targets, units of sense and the freedom to look back. Streaming removes all three at the moments decision spaces occur, and renews a forward pull at the leading edge.
4. Continuous generation therefore conceals decision spaces, and surface fluency co-opts them by making a point of judgment read as a finished answer.
5. Marking a decision space restores a saccade target, an event boundary and an unhurried window for looking back. How much it restores depends on where the mark falls, how long it lasts and what form it takes.
6. Marking makes a decision space perceptible but does not resolve it. Supervisory navigation requires both perception of the decision space and a working model of the intermediary that produced it (G = F × MI).

[ROGER] This question sits at the center of my dissertation, which examines how individuals navigate opaque and cooptive environments, a phenomenon I call algorithmacy. [/ROGER] The paper proceeds as follows. Section 2 introduces the foundations: the historical shift from continuous script to word separation (2.1), eye movements and regressions in reading (2.2), onsets and priority maps in visual search (2.3), event segmentation (2.4), and the ecological view of text as a stable material object (2.5). Section 3 reviews four literatures that touch streaming — pacing (3.1), automation supervision (3.2), language-model overreliance and friction (3.3), and gaze as evidence of supervision (3.4) — and states the gap they share (3.5). Section 4 presents algorithmacy theory: its foundations among the older competences (4.1), a nomological network (4.2), six propositions (4.3), thirteen predictions (4.4), a rule for locating decision spaces (4.5), three perceptual mechanisms (4.6–4.8), moderators (4.9), the distinction between gaze and navigation (4.10), and what marking is not (4.11). Section 5 sets out a testing agenda, design implications, the reach of algorithmacy beyond text, and two counterpoints. Section 6 concludes.

---

## 2. FOUNDATIONAL CONCEPTS: SCRIPTIO CONTINUA, READING, ATTENTION AND EVENTS

This section introduces the science on which the theory rests, for readers in HCI who do not work on reading or attention. It begins with a historical case, because the case states the problem in its simplest form, and then turns to four bodies of research. Each subsection ends by naming the mechanism it hands to the theory in Section 4.

### 2.1 The historical precedent: scriptio continua and word separation

[ROGER] An informative historical parallel exists in the evolution of written language: Latin manuscripts were originally composed in scriptura continua, [F16] with letters joined together without word boundaries, forcing readers to read aloud or subvocalize to determine lexical units through phonological inference (Saenger, 1997). Beginning in the seventh century, Insular scribes introduced blank spaces between words, a structural innovation that offloaded lexical segmentation from internal working memory to pre-attentive visual processing, enabling silent, reflective reading (Parkes, 1992; Saenger, 1997). [F17] [/ROGER] [NEEDS: page locators for both claims; Saenger and Parkes not read this session.]

The psychophysics bears out what the space does for the eye. Rayner, Fischer and Pollatsek (1998) removed the spaces from English text and recorded the eye movements of skilled adult readers. Reading rate fell by 54% for single sentences and 44% for passages in their first experiment, and by 58% in their second. Regressions in sentence reading rose from 9.7% to 17.3% of eye movements, and in passages from 11.2% to 16.4%. Readers no longer landed just left of a word's centre, where the eyes usually land, but near its start. Rayner and colleagues concluded that missing spaces disrupt both word identification and the programming of saccades, and word identification more. Spaces, they wrote, enhance upcoming words "as 'targets' for an eye movement" (p. 1129). Drieghe, Fitzsimmons and Liversedge (2017) found that unspaced text slowed reading with "rather limited evidence" that readers spread their processing across several words to compensate. The fluent adult reader does not outgrow the space. He or she relies on it without noticing.

An obvious objection follows. Chat interfaces already print spaces between words, so a streamed answer is not scriptio continua. The objection is right about the word and wrong about the stream. A streamed response keeps word-level typography, but while it forms it lacks the units above the word that a finished page supplies: a paragraph that stays put, a section break, a pause that marks where one claim ends and the next judgment begins. [D5] The space problem returns one level up. Words are separated; decisions are not.

The analogy has limits, and they shape the theory. Medieval readers set their own pace, whereas the reader of a stream does not. Silent reading also predates word separation in some classical settings (Knox, 1968) [NEEDS: Knox not read; cite only for the general claim], so the space did not create the capacity to read silently. It made that reading easier by moving a task from memory to the eye. The claim here is the same in kind: marking decision spaces should make supervision easier, not make it possible for the first time.

The case also shows the triad on which the theory rests. The space made word boundaries perceptible, but it did not make anyone literate. A person who cannot read sees the marks and the gaps and still cannot cross from marks to meaning. Three things were in play: the written text, the space that marks its units, and the literacy that fills the gap between marks and meaning. Streamed AI output presents the same three: the output, the decision space that a mark can make visible, and the competence to fill it. [ROGER] I theorize that observing AI in operation today is analogous to reading scriptura continua, which requires oral reading to discern each word's function, thereby merging oracy with emerging literacy. Similarly, interacting with AI now combines users' literacy with their developing algorithmacy. [/ROGER] Section 4.1 takes up that competence.

### 2.2 Eye movements in reading: targets, regressions and repair

Reading alternates fixations, during which the eyes are nearly still and take in text, with saccades, rapid jumps between fixations. In Rayner et al.'s (1998) spaced conditions, fixations averaged about 250 ms and forward saccades about 7 to 8 characters (Table 1). [D6] Not every saccade goes forward. Regressions, saccades back to earlier text, make up 10–15% of eye movements by one estimate (Schotter, Tran, & Rayner, 2014, p. 1225) and 15–25% by another (Booth & Weger, 2013, citing Rayner & Pollatsek, 1989).

Regressions serve rereading. Booth and Weger (2013) tested whether readers look back to reread or merely to cue their memory for where a word was. Across three experiments they found the first: when the earlier text was made illegible, regressions fell and stopped predicting comprehension. They also foresaw the case of this paper, noting that readers "of scrollable text on small screens" may find that "rereading is often impossible" (General Discussion).

[ROGER] Crucially, reading comprehension is not a strictly feedforward perceptual process; it requires regressions—backward eye movements launched to reread ambiguous clauses, integrate syntactic structures, and repair comprehension failures (Schotter et al., 2014). When word masking prevents readers from executing regressions, reading comprehension deteriorates significantly (Schotter et al., 2014). [F8] [/ROGER] Schotter and colleagues used a trailing mask, which turned each word into a row of x's once the eyes had passed it, and tested 40 readers on single-line sentences. The mask lowered comprehension (b = −0.92, z = 5.09, p < .001), and not only for garden-path sentences. Comprehension stood at 78% in normal reading when readers did not regress and at 71% under the mask (p. 1223).

Rereading carries a repair that forward reading does not. Timkey et al. (2026) recorded 368 readers and found that language-model surprisal explained early reading effects but not the cost of rereading at the point where a sentence's structure was disambiguated. They read that rereading cost as "the cost of detecting or correcting errors in the structure-building process." The repair, in other words, happens on the way back.

Displays that remove the way back lose it. Rapid serial visual presentation shows one word at a time in a fixed place, which suppresses both regressions and preview of the next word; Benedetto et al. (2015) found that it hurt literal comprehension. Metzner et al. (2017) found that free reading beat word-by-word presentation only on trials where readers regressed to the anomaly. These are the conditions a stream approaches when it moves earlier text out of view.

This subsection hands one function to the theory: marking should open a window in which looking back is possible and unhurried (Section 4.8).

### 2.3 Visual search, abrupt onsets and priority maps

New things draw the eye, under conditions. Yantis and Jonides (1984) showed that an item appearing abruptly in a visual search display is identified first. They also limited the claim: capture of this kind occurs "only when the visual field contains but one such event" (p. 617). A token stream meets that condition when one new word appears against static text. It meets it less well when several words arrive together.

Wolfe's (2021) Guided Search 6.0 places such effects inside a larger model. Five sources of guidance — top-down and bottom-up feature guidance, prior history, reward, and scene syntax and semantics (p. 1060) — feed a priority map, which attention visits about 20 times per second. Wolfe treats bottom-up salience as "a very powerful but short-lived form of guidance" and suggests that "attention capture" may be a misnomer for a bump in that map. He adds that "if there is enough of a break in the action, the map may get reset," and asks whether event boundaries do the resetting (p. 1069). [D7] That suggestion, which Wolfe does not test, is the strongest single anchor for why a pause might help: a stream that never breaks keeps refreshing the bottom-up bump at its leading edge.

This subsection hands a second function to the theory: marking should provide a stable visual target that competes with the leading edge (Section 4.6).

### 2.4 Event segmentation and situation-model updating

People parse continuous activity into events. Event Segmentation Theory holds that perceivers maintain a model of the current event and update it when their predictions about what comes next begin to fail; the moment of updating is perceived as a boundary between events (Kurby & Zacks, 2008; Zacks et al., 2007). [NEEDS: Zacks et al. 2007 unread; the paraphrase follows Kurby & Zacks 2008 and Zacks et al. 2009.]

Readers segment text the same way. Zacks, Speer and Reynolds (2009) found that changes in the narrative situation — a new character, goal, cause, place or time — predicted where readers placed event boundaries. Each additional situation change added 92.8 ms of reading time, and each 10% rise in the probability of a boundary added about 108 ms. Segmentation survived pacing that the reader did not control: in a visual-sequential condition, software showed one clause at a time at about 3.35 words per second, with no way back, and readers still placed boundaries above chance. That condition is the closest precedent in the literature to a stream.

Boundaries do work. Kurby and Zacks (2012) found that readers updated their situation models both globally, rebuilding at boundaries, and incrementally, adding detail as they went; goals were mentioned more often at fine-grained boundaries even when no goal had changed (OR = 2.29). [D8] And boundaries can be computed from text. Kumar et al. (2023) showed that Bayesian surprise computed with the GPT-2 language model tracked where listeners placed event boundaries in spoken stories. [D9]

This subsection hands a third function to the theory: a mark at a decision space should act as an event boundary and prompt updating (Section 4.7).

### 2.5 Ecological and sensorimotor perception: text as a stable object

[NEEDS: this subsection's first paragraph rests on Gibson (1979) and O'Regan & Noë (2001), both deferred and unread. The sentences below state their positions only at the level of their abstracts and titles; check the wording against the texts before submission.] Gibson (1979) treated perception as the pickup of affordances, the possibilities for action that an environment offers an animal. O'Regan and Noë (2001) treated seeing as the exercise of mastery over sensorimotor contingencies: the lawful ways sensory input changes as the perceiver moves (see also O'Regan, 2011). On both views, reading is something done with a stable object. The eye moves and the page answers the same way each time.

Printed text supplies that stability, and the evidence suggests readers use it. Mangen, Olivier and Velay (2019) gave 50 readers a 28-page story in print or on a Kindle. Print readers reconstructed the plot's chronology better (t(48) = 2.03, η² = .08), and the authors tied the advantage to the "material placeholders" a physical book provides, citing Gibson and O'Regan and Noë. Delgado et al.'s (2018) meta-analysis found a paper advantage that grew under time constraint. Neither study tested scrolling or streaming; Mangen et al. compared page-turning devices. [D10] The inference to a stream is mine: a stream offers fewer placeholders than a screen of fixed text, because the text is still arriving and the earlier part is moving away.

This subsection hands the framing of the theory, reading as action on a stable object, to Section 4.1.

---

## 3. STREAMING IN CURRENT HCI, AUTOMATION AND LLM-RELIANCE ACCOUNTS

Given what Section 2 shows about reading, one would expect the structure of a stream — where it offers targets, boundaries and a way back — to figure in current accounts of how people supervise AI. It does not. This section reviews four literatures that come closest. Each studies something real about streamed or automated output, and each leaves out the same variable.

### 3.1 Streaming and pacing in generative interfaces

Streams change where people look. Park and Lee (2024) tracked the eyes of 36 participants reading Korean expository text in four chatbot display types. When text was generated at the bottom of the screen, participants made more fixation starts, spent more total time fixating and made larger saccades than when text appeared whole at the top, and their fixation starts clustered where new text appeared (Tables 9, 11–12). It is the only eye-tracking study of chatbot text movement I found. Topic was confounded with condition, and Park and Lee measured no comprehension. [F3]

Streams also change what people think of the source. In Bhat's (2025) within-subjects study, simulated typing at two to three seconds per sentence raised perceived competence (F = 40.89), trustworthiness (F = 35.21) and persuasiveness (F = 76.89), all p < .0001, relative to the same kind of response shown whole. Perceived effectiveness did not change (F = 0.16, p = .69). [D11] Every measure was a rating. Bhat measured no accuracy, and simulated typing is not token streaming. The finding is nonetheless the cleanest evidence that the manner of delivery, apart from content, changes the authority a reader grants.

The pace of a stream is set by compute. Liu et al. (2024) estimated an average reading speed of 4.8 tokens per second by converting a words-per-minute table at about 1.3 tokens per word, and used it as a delivery target; one serving system they studied delivered 11.2 tokens per second on a real trace. Xiao and Yang (2025) measured comfortable streaming speed directly with an adaptive procedure: the 99th-percentile comfortable speed was 21.20 words per second for an easy passage and 11.97 for a complex one, against about 45 words per second from the GPT-4o API. [D4] Comfort is not comprehension, and neither paper measured comprehension. Both papers, and Zhu et al.'s (2026) adaptive token pacing [NEEDS: Zhu et al. 2026 unread beyond its record], treat the problem as one of rate.

Moving text changes rereading. Sharmin, Špakov and Räihä (2015) found that text emerging word by word, as in live captioning, produced more rereading and more regressions than text emerging letter by letter. A follow-up found that 90.8% of regression landings in dynamic text fell on content words, against a base rate of 57.1% (Sharmin et al., 2016). Harvey et al. (2017) found that horizontally scrolling text preserved word-level effects but lost the benefit of sentence-level predictability, and Harvey and Walker (2018) found that literal comprehension held under scrolling while inference suffered. Haverkamp et al. (2023) compared reader-controlled scrolling with paging through a PDF (N = 145): scrollers backtracked less often (2.49 vs 3.53 times) but farther, and the comprehension advantage for paging was only a trend (p = .066). [D12] None of these displays was an AI stream, but each removes some of the stability that reading uses.

What this work omits is placement. Pacing research adjusts how fast tokens arrive. It does not ask where, inside a response, a reader could stop.

### 3.2 Automation supervision and trust

Human-factors research on automation explains failures of supervision as failures of attention. Parasuraman and Manzey (2010) located complacency in the allocation of attention under multiple-task load, and used "looking-but-not-seeing" (p. 403) to explain commission errors, in which operators follow wrong automated advice. Their evidence came from information sampling rather than fixations: in a study by Manzey and colleagues, about half of those who missed a wrong diagnosis had sampled all the information needed to catch it (p. 402). [F15] Lee and See (2004) framed the design goal as appropriate reliance, trust calibrated to what the automation can actually do.

Advice that arrives as a recommendation changes scrutiny, slightly. Gegoff et al. (2025) gave 142 participants an uninhabited-vehicle management task with or without decision recommendations. Recommendations raised accuracy (.89 vs .85) but slightly lowered participants' discrimination of accurate from inaccurate system information (.93 vs .94; ηp² = .05) (pp. 785–787). [D13] A streamed answer arrives in recommendation form: complete, confident and ready to accept.

Giving operators control over transparency does not fix this. Tatasciore et al. (2026) let operators choose their own level of automation transparency across two experiments (N = 73 and 88). Operators chose high transparency on 39% and 43% of adaptable trials, and adaptable transparency did not improve the accuracy of automation use (p. 22). [D14] Across six studies, high transparency raised hit rates and sensitivity but also a bias toward agreeing with the automation, with no gain in correct rejections (p. 21).

Supervision of agents fails on timing. Chen et al. (2026) observed 48 participants overseeing 192 live sessions of a computer-use agent. Users blocked 29 of 138 problematic actions, and 61 of 109 failures (56%) involved a timing mismatch between the user's intervention and the moment that mattered. Oversight, they concluded, depends on "aligning authority, timing, and attention with decision-critical moments." That phrase comes close to naming decision spaces.

Expertise changes the relationship. Lamb et al. (2026) followed defence intelligence analysts adopting an object-detection overlay on live video. Over the study, seven of nine stopped treating the tool as an "advisor" (McNemar p = .023), and analysts wanted to learn the tool's "boundary conditions." Endsley (2017) frames the larger problem as a conundrum: the more capable and reliable the automation, the less likely its supervisors are to catch its failures. [D15]

What this work omits is continuity. It models advice that arrives as discrete events — an alert, a diagnosis, a recommendation on a screen. A stream is not an event but a performance that unfolds while the reader reads it.

### 3.3 LLM overreliance, fluency and friction

Fluent explanation raises reliance on language models whether or not the answer is right. Kim et al. (2025) combined a think-aloud study (N = 16) with a pre-registered experiment (N = 308) on hard binary factual questions. Explanations raised agreement with both correct and incorrect answers; sources and inconsistencies lowered agreement with incorrect ones. Few participants checked: 189 of 308 never clicked a source. Kim et al. observe that "the properties that make such explanations intelligible and compelling may be precisely those that lead to overreliance" (§5.1). Steyvers et al. (2025) found that longer explanations raised users' confidence in a model's answers without raising accuracy.

Fluency can be trained in without verifiability. Zhu et al. (2026) found that post-training raised accuracy without raising how verifiable a model's errors were, and that rephrasing without new information did not help. For one model on one benchmark (Tulu3.1-8B on GSM8K), their false-positive verifiability score fell from 0.717 to 0.602 after preference optimisation (§7.1). [D16] Most of their raters were language models.

Overreliance leaves traces in behaviour. Liu et al. (2026) logged the mouse and keyboard of 77 participants working with a GPT-4 platform into which misinformation had been injected. High overreliance went with copying whole texts, coarse navigation, and accepting despite hesitation (Table 3).

Interventions that force a pause reduce overreliance, at a price. Buçinca, Malaya and Gajos (2021) tested three cognitive forcing functions with 199 participants, one of them a 30-second wait before the AI's prediction appeared. On incorrect predictions, the forcing functions cut overreliance (0.48 vs 0.64, d = .36). Participants preferred them less and trusted the system less. Ghosh et al. (2026) compared forcing functions for execution plans in AI-assisted writing (n = 214) and found that an "Assumptions" function reduced overreliance most, without raising cognitive load (abstract only). [D17]

Friction designs place their obstacles around the stream, never inside it. Cox et al. (2016) defined a microboundary as "a small obstacle prior to an interaction" that imposes a short time cost and shifts behaviour from automatic to deliberate; they listed user control over such boundaries as an open question. Collins et al. (2024) tested "selective frictions," such as a button that impedes access to a model, which reduced click-through with little effect on accuracy but spilled over to other topics (abstract only). Arun et al. (2026) found that preparatory friction raised mental demand and trust without reducing self-reported reliance (N = 40; abstract only). Disley and Khan (2026) built friction into the model itself by suppressing a concept during ideation (N = 37). The unmodified model lowered effort and ownership (ownership 6.38, against 9.16 with suppression and 11.49 unaided). They contrasted this model-level friction with interface-level friction — "an added step, a delay" (§2.3) — and called for comparisons between the two (§7.9). [D18]

Asking users to reflect has its own cost. Forshaw, Hale and Longmire (2026) gave eight managers coaching from a human and from an AI agent built on the same protocol. All eight preferred the human coach and resisted the AI's probing questions, yet the coached behaviours appeared after both sessions (§6.1). [D19] What users say about friction and what friction does can diverge.

What this work omits is placement by meaning. Friction sits before an action, before access, or inside the model. None of it sits inside the generated response, at points set by what the response says.

### 3.4 Gaze as an insufficient proxy for supervision

Gaze tracks reliance. Wu et al. (2025) used gaze to distinguish over-, under- and appropriate reliance at run time, and Cao and Huang (2022) found that the share of gaze on an AI's suggestion correlated with agreement with it (both abstract only).

But attention can move without judgment moving. Cho and Lim (2026) varied how four chatbot layouts attributed sources (N = 23). Time to first fixation on the source ranged from 0.96 s to 15.65 s across layouts, yet gaze did not predict trust: "Attention moved without moving judgment" (§3.4). Their screens were static.

Fixation duration is ambiguous. Yang et al. (2027) found that augmented-reality cues shortened pedestrians' fixations on approaching automated vehicles (d = −0.80) and brought crossings earlier, and they warned that the shorter fixations "may also indicate overreliance" (§5). Resulbegoviq et al. (2026) reviewed 23 eye-tracking studies of AI-generated content and found that "no modality-independent gaze pattern emerged"; longer viewing more often reflected difficulty or checking than preference.

What this work omits is a normative account: where gaze should land during a stream, and when a fixation counts as checking.

### 3.5 Summary: the missing variable

The four literatures share a blind spot. Pacing research studies the rate of the stream, automation research the advice it carries, friction research the obstacles around it, and gaze research where the eyes go. None examines the stream's internal structure — where in a forming response judgment is required, and whether the reader can see that it is. Algorithmacy theory, at its perceptual layer, supplies that variable.

---

## 4. ALGORITHMACY THEORY: DECISION SPACES AND THEIR MARKING

The gap that Section 3 identified is a gap in what current accounts look at: they study the stream's rate, its advice, its surroundings and the reader's gaze, but not the points inside it where judgment is required. This section states a theory of those points. It defines algorithmacy and places it among the older competences (4.1), draws the theory as a network of constructs (4.2), states six propositions (4.3) and thirteen predictions (4.4), and gives a rule for locating decision spaces (4.5). Subsections 4.6 to 4.8 treat the three perceptual mechanisms that marking restores, each in the same four steps: the evidence from Section 2, how the mechanism shows up in streams, how streams differ from static text, and what the theory predicts. Subsections 4.9 to 4.11 treat moderators, the distinction between gaze and navigation, and what marking is not.

### 4.1 Foundations: algorithmacy, triadic coordination and the competence models

**Definition.** Algorithmacy is the competency of navigating triadic coordination. This paper treats its perceptual layer: the capacity to detect, evaluate and act on decision spaces in an intermediary's output.

**The triad.** Reading a printed text is dyadic. A writer and a reader meet through a text that does not change while it is read. A streamed AI response is triadic. The user meets the task through an intermediary that is opaque, that optimizes for objectives of its own, and that sets the timing of delivery. Each property has an anchor in Section 3. The pace of the stream is set by the provider's compute (Liu et al., 2024; Xiao & Yang, 2025). Its manner of delivery raises the authority readers grant it (Bhat, 2025). Post-training can make its output more convincing without making its errors easier to catch (Zhu et al., 2026).

**Co-optation.** Stark and Vanden Broeck (2024) distinguish organizational forms by how they enrol the people within them: "Whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted." Co-optation is enrolment through the design of the system rather than through prior competence or agreement. A streamed answer co-opts in this sense. Its fluency, its pace and its form as a finished recommendation make a point that calls for judgment read as a point that calls only for acceptance.

**The comparative lineage.** Algorithmacy belongs to a family of named competences. Table 2 sets the perceptual layer of algorithmacy beside literacy, oracy and numeracy. [D20]

*Table 2. Algorithmacy among the older competences.*

| Dimension | Literacy | Oracy | Numeracy | Algorithmacy (perceptual layer) |
|---|---|---|---|---|
| What is given | Written marks on a static page | A spoken stream [D20] | Mathematical symbols and notation [D20] | A stream of output from an opaque process |
| The gap | Between marks and linguistic meaning | Between sound and meaning in context [D20] | Between notation and the relations it states [D20] | Decision spaces: hidden points where judgment is required |
| What can make the gap perceptible | Word spaces, punctuation, layout | Prosody, pauses, turn-taking [D20] | Layout of working and proof [D20] | Marking: visual and temporal boundaries in the stream |
| What fills the gap | Literacy | Oracy | Numeracy | Algorithmacy |
| Failure state | Illiteracy | Non-fluency [D20] | Innumeracy | Co-optation; uncritical overreliance |

The older competences share four properties that carry over to algorithmacy. First, each name claims parity. Andrew Wilkinson coined "oracy" in 1965 "to try to give spoken language skills comparable status" with reading and writing (Mercer, Warwick, & Ahmed, 2017, p. 2), and Gal et al. (2020) argue that "numeracy should have a similar standing to that of literacy." Algorithmacy makes the same claim for the competence of navigating an intermediary. Second, the competence multiplies a code-handling component by a meaning component. Hoover and Gough (1990) state reading comprehension as the product of decoding and linguistic comprehension; each is necessary, and the product predicted better than either alone (abstract). Third, each competence has several components. Gal et al. (2020) include knowledge, skills and dispositions in numeracy, and Duke and Cartwright (2021) add active, self-regulatory processes to the simple view of reading (abstract). Fourth, functional and critical uses are intertwined. Gal et al. (2020) describe functional and critical numeracy with "no hierarchy and no dichotomy," and note that one can be critical "even without fully understanding the mathematical part first."

The second property gives the theory its central claim:

> **Supervisory navigation (G) = perception of decision spaces (F) × the reader's model of the intermediary (MI).**

Both factors are necessary and neither is sufficient. A reader who perceives a decision space but has no model of what the intermediary is likely to get wrong there sees the point and does nothing with it. A reader with a rich model who never perceives the decision space has nothing to apply the model to. This paper treats the first factor, the algorithmacy analogue of decoding. Duke and Cartwright's (2021) amendment to the simple view applies here too: the product is a simplification, and the two factors will overlap in practice.

Algorithmacy also differs from the older competences in four ways. First, the code is hidden, proprietary and changing. Gal et al. (2020) note that the algorithmic processes of machine learning "are black boxes, even for those who produce them," and that mathematics "disappears within technological systems." Second, the gaps are unmarked by default. Writing developed spaces and punctuation for its units; no older competence model has a component for locating judgment points that the medium hides. Third, participation precedes competence. Children are taught to read before they are asked to read contracts, but users are co-opted into streamed AI before anyone teaches them to supervise it (Stark & Vanden Broeck, 2024). Fourth, fluency can be capture rather than mastery, a difference Section 4.9 develops.

One further guard is needed. Literacy studies spent decades dismantling the claim that literacy is a neutral technical skill with built-in cognitive effects. Street (2003) called that claim the "autonomous" model and argued that it "disguises the cultural and ideological assumptions that underpin it," and Scribner and Cole (1978) found that literacy's cognitive consequences among the Vai were tied to specific practices rather than general (abstract). This paper therefore claims specific perceptual consequences of one practice, supervising streamed text, and no general transformation of cognition. Dehaene et al. (2015) show the form a defensible consequences claim takes: learning to read reorganizes specific visual and phonological systems, which can be measured (abstract). Section 5.4 returns to the critique.

**Prior use of the term.** OpenAlex records one earlier use of "algorithmacy": Oberschelp (1995), in a chapter on developing analytical competency through informatics teaching. [NEEDS: read the chapter and state how Oberschelp uses the word before characterizing it.] [D21] The term also needs distinguishing from algorithmic literacy, which Ridley and Pawlick-Potts (2021) define as "the skill, expertise, and awareness" to understand, recognise, create, apply and assess algorithms (p. 3). Algorithmic literacy is knowledge *about* algorithms. Algorithmacy is the competence of navigating *through* an intermediary, and its perceptual layer concerns what the reader sees while doing so.

**Decision spaces.** Decision spaces are the opaque, co-opted points in an automated process where a human judgment — accept, verify, reject, redirect — is required but the process does not present it as such. They are *opaque* because the process does not show them, and *co-opted* because fluency, pace and recommendation framing make a judgment point read as a finished answer. Decision spaces exist in the process whether or not the interface shows them.

**Marking.** Marking is the interface operation that makes a decision space perceptible in the stream: a pause, a space, a rule, a label. Marking does not create decision spaces, and it does not navigate them.

### 4.2 The nomological network

Figure 1 draws the theory's constructs and the causal arrows between them. Following Cutting and Deterding (2022), each construct has a letter and each prediction in Table 1 names the arrow it tests.

```
                    ┌──────────────────────────────────────────────┐
                    │  DS: Decision Spaces (Latent in the Process) │
                    └──────────────────────────────────────────────┘
                         │ Hidden by                    │ Rendered Perceptible by
                         ▼                              ▼
A: Stream Properties ──(+)──▶ C: Forward Pull      M: Marking (Placement, Duration, Form)
   (Pace, Onsets,                at Leading Edge      │ (−)→C   (+)→D   (+)→E
    Auto-Scroll)                 │ (−)                ▼
                                 ▼              D: Event Boundary / Updating
H: Co-optation: Fluency &    E: Look-Back Window      │
   Recommendation Framing        │                    ▼
        │ (−)                    └──────────▶   F: Fixations & Regressions at DS
        ▼                                             │ (Necessary, Not Sufficient)
   G: Supervisory Navigation: Detect, Reject, Steer ◀─┘
        ▲
        │ Multiplicative Moderation (G = F × MI)
   MI: Reader's Model of the Intermediary (Interpretive Factor)
```

*Figure 1. Nomological network of the perceptual layer of algorithmacy. [ROGER: diagram copied from your outline.]*

Read from the top, the figure says that decision spaces (DS) exist in the process and that two things act on whether a reader sees them. Stream properties (A) — the server's pace, the onset of each new token, automatic scrolling — create a forward pull at the leading edge (C), which shrinks the window in which the reader can look back (E). Marking (M) works against the pull, creates an event boundary (D) and widens the look-back window. Boundary and window together bring fixations and regressions to the decision space (F). Those fixations are necessary for navigation (G) but not sufficient: what the reader does with them depends on the reader's model of the intermediary (MI), and co-optation (H) works against navigation directly, whatever the eyes do.

### 4.3 Formal propositions

[ROGER]
- **Proposition 1 (Representation of Process):** An automated text stream contains latent decision spaces that exist independently of interface representation.
- **Proposition 2 (Perceptual Suppression):** Continuous token generation exerts stimulus-driven attentional capture toward the leading edge, suppressing regressive saccades and situation-model updating.
- **Proposition 3 (Co-optation via Fluency):** Syntactic fluency and recommendation framing co-opt supervisory scrutiny, biasing users toward passive compliance.
- **Proposition 4 (Perceptual Restoration via Marking):** Introducing structural marks at decision spaces restores visual targets, triggers cognitive event segmentation, and opens look-back windows.
- **Proposition 5 (Multiplicative Competency):** Fixating upon a marked decision space is an oculomotor prerequisite, but successful navigation depends multiplicatively on the user's mental model of the intermediary (G = F × MI).
- **Proposition 6 (Alignment Sensitivity):** Marking efficacy is non-linearly sensitive to structural placement, temporal duration, and visual form; misaligned marks induce cognitive fragmentation.
[/ROGER]

Proposition 1 makes decision spaces a property of the process rather than of the display, which is what allows an interface to mark them correctly or incorrectly. Proposition 2 rests on the onset and priority-map evidence (Section 2.3) and on Park and Lee's (2024) finding that fixation starts cluster where new text appears; "capture" here should be read with Wolfe's (2021) caution that it may be a bump in a priority map rather than a seizure of attention. [D7] Proposition 3 rests on Kim et al. (2025), Gegoff et al. (2025) and Bhat (2025). Proposition 4 gathers the three mechanisms of Sections 4.6 to 4.8. Proposition 5 is the product claim of Section 4.1. Proposition 6 rests on the evidence on misaligned breaks and lockout duration reviewed in Section 4.9.

### 4.4 Directional predictions

Table 1 states thirteen predictions. Each names the arrow in Figure 1 it tests and, where it corresponds to one, a research question for the study outlined in Section 5.1.

*Table 1. Directional predictions. [ROGER: prediction wording copied from your outline.]*

| # | Prediction | Arrow | Research question |
|---|---|---|---|
| P1 | Higher streaming speeds and unmasked token onsets will increase dwell at the leading edge and reduce regressive saccades to preceding text. | A → C → E | Baseline validation |
| P2 | Introducing interface marking will truncate forward attentional capture for the duration of the mark. | M → C | Baseline validation |
| P3 | Marking will increase the availability of earlier text within the unconstrained regression window. | M → E | Baseline validation |
| P4 | Marks placed at decision spaces will evoke cognitive event segmentation and induce working-memory situation updating. | M → D | Baseline validation |
| P5 | Marks aligned with semantic decision spaces will elicit significantly higher fixation counts and regressive landings than identical marks placed at arbitrary intervals. | M → F (via D, E) | RQ1 |
| P6 | Marks aligned with decision spaces will yield higher error detection and intervention accuracy than continuous streams or arbitrary periodic breaks. | M → G (via F) | RQ2 |
| P7 | Marks placed at arbitrary intervals will impose significant costs in detection latency, subjective workload (NASA-TLX), and local refixations relative to an unbroken stream. | M (misaligned) → D (disrupted) | RQ3 |
| P8 | High textual fluency and recommendation framing will suppress supervisory intervention independently of ocular fixation dwell. | H → G | Foils validation |
| P9 | Elevated fixation counts at decision spaces without corresponding error interception (F ↛ G) will identify visual inspection without cognitive verification. | F ↛ G | RQ1 vs. RQ2 |
| P10 | Mark duration will display an inverted-U relationship with navigation: brief pauses fail to break forward pull, while excessive pauses prompt task switching. | M (duration) → G | Design-space validation |
| P11 | A richer user model of the intermediary (MI) will accelerate the transition from ocular fixation (F) to intervention (G) via targeted regressions rather than prolonged dwell. | MI × F → G | Algorithmacy moderation |
| P12 | Marking will reduce performance variance between users with high and low MI, acting as an equalizing perceptual scaffold. | M × MI → G | Ergonomic equity |
| P13 | Supervisory navigation requires both perceptual detection and an active model of the intermediary (G = F × MI); neither factor in isolation will yield calibrated intervention. | F × MI → G | Simple-view pattern |

Predictions P11 to P13 require a measure of the reader's model of the intermediary. Section 5.3 proposes a route to one; until it exists, these three are a research agenda rather than testable predictions. [NEEDS: your decision on whether to keep P11–P13 in the table or move them to Section 5.3.]

### 4.5 Locating decision spaces: the operational rule

The theory is only as testable as its rule for finding decision spaces. Two failures threaten it. If the rule is vague, any pause can be said to fall at a decision space after the fact. If the rule is simply "where the experimenter put the pause," the theory reduces to a claim about pauses. The rule must therefore identify decision spaces in a response's content, before any interface acts on it, and independently of the outcome measures.

I propose four criteria. A point in a response is a candidate decision space if it meets any of them:

1. **The end of a verifiable assertion.** A factual claim, a figure or a citation has just been completed, and the reader could check it against something outside the response.
2. **A branching action point.** The response introduces a course of action, a piece of code or a recommendation that the user would have to authorize before going on. This is the criterion closest to the term itself, and closest to Chen et al.'s (2026) "decision-critical moments."
3. **An event or sub-goal shift.** The response changes goal, cause or entity, the situation changes that Zacks et al. (2009) found predict event boundaries in reading.
4. **A peak in model-derived surprise.** Kumar et al. (2023) showed that Bayesian surprise computed from a language model tracks where people perceive event boundaries, so peaks can serve as an automatic, content-based detector. [D9]

The criteria differ in kind. The first two are about what the reader might have to *do*, the second two about how the reader is likely to *segment*. A study can test them separately, and the theory predicts that the first two matter most for navigation (P6) and the second two most for segmentation (P4). [NEEDS: this is the paper's central contribution. Confirm the four criteria, their order, and whether any combination rule applies.]

### 4.6 Mechanism 1: restoring a stable visual target

*Evidence.* Word spaces make upcoming words targets for saccades: without them, readers land at the start of words rather than near their centres, and reading slows by about half (Rayner et al., 1998). [D22] An abrupt onset is selected first when it is the only one in view (Yantis & Jonides, 1984), and bottom-up salience is powerful but short-lived (Wolfe, 2021).

*In streams.* The newest token is an onset, and it appears at the leading edge. Park and Lee (2024) found that fixation starts clustered where new text appeared, at the bottom of the screen.

*How streams differ from static text.* On a static page the targets stay where they are, and the reader decides which to visit next. In a stream the most salient target is the one that keeps moving, and every new token renews its salience. A decision space that has just scrolled past competes with an onset that has just appeared, and on Wolfe's account the onset wins the bump in the priority map.

*Formally*, the theory predicts that pace and onsets will hold the eyes at the leading edge and reduce regressions (P1), and that a mark will interrupt this pull while it lasts (P2).

### 4.7 Mechanism 2: establishing an event boundary and prompting updating

*Evidence.* Readers place event boundaries at changes in the narrative situation and slow down there (Zacks et al., 2009), update their situation models both globally and incrementally at boundaries (Kurby & Zacks, 2012), and may have their priority maps reset by a sufficient break in the action (Wolfe, 2021, as a suggestion).

*In streams.* Segmentation does not need a reviewable page. In Zacks et al.'s (2009) visual-sequential condition, readers who saw one clause at a time at a pace set by software still placed boundaries above chance. A stream therefore supplies the material for segmentation.

*How streams differ from static text.* A finished text shows its segmentation: paragraph breaks, headings and white space tell the reader where the writer thought one unit ended. While a response streams, it shows none of this. The reader must segment it unaided, at a pace not of the reader's choosing, while the leading edge keeps drawing the eyes forward.

*Formally*, the theory predicts that marks placed at decision spaces will act as event boundaries and prompt updating (P4).

### 4.8 Mechanism 3: opening an unhurried look-back window

*Evidence.* Readers look back to reread, not to cue memory (Booth & Weger, 2013); preventing regressions with a trailing mask lowered comprehension from 78% to 71% (Schotter et al., 2014) [D23]; and rereading carries the cost of repairing the structure of a sentence (Timkey et al., 2026).

*In streams.* Text emerging word by word produced more rereading and more regressions than text emerging letter by letter (Sharmin et al., 2015), and scrolling text cost inference while sparing literal comprehension (Harvey & Walker, 2018). When readers controlled scrolling themselves, they backtracked less often but farther (Haverkamp et al., 2023). [ROGER] In streaming AI interfaces, auto-scrolling text continuously displaces preceding lines beyond the functional regression window, forcing users to choose between manually scrolling up to review earlier claims or trailing the moving cursor (Haverkamp et al., 2023). [F9] [/ROGER]

*How streams differ from static text.* A static page waits for the reader's eye. A stream moves on, and a regression to earlier text costs the reader the newest text.

*Formally*, the theory predicts that marking will increase the availability of earlier text (P3) and, when placed at decision spaces, will draw more fixations and regressions there than the same number of arbitrary marks (P5).

### 4.9 Moderators: properties of the mark and the reader's algorithmacy

Marks are not equal. Their effect depends on where they fall, how long they last and what they look like, and on who is reading.

**Placement.** Breaks aligned with units of meaning help, and misaligned breaks hurt. Tsoukala, Vogelzang and Tsimpli (2025) found that line breaks cutting across clauses raised first-pass reading time (d = 0.32) and total time (d = 0.41), although the interaction did not survive correction for multiple comparisons and readers recalibrated after repeated misaligned breaks. Koornneef (2024) found that presenting text in sentence-sized segments raised comprehension (abstract). Research on interruptions points the same way. Bailey and Konstan (2006) found that interruptions during a task, rather than between tasks, cost more time and doubled errors, and Powers and Scerbo (2023) found that interruptions at coarse breakpoints cost about as little as no interruption, while fine ones were costly (both abstract only).

**Duration.** Gould et al. (2016) found that brief task lockouts encouraged checking in the lab, while longer lockouts on a crowdsourcing platform induced task switching, and concluded that duration "needs to be carefully calibrated" (abstract). [D24] The theory predicts an inverted U (P10).

**Form.** A mark must signal without demanding to be read. Prajod et al. (2026) found that a one-line AI-disclosure label drew more total fixation time than a detailed label (58.70 vs 49.46, d = 0.34) among 30 readers of static news. [D25] Hyönä and Lorch (2004) found that topic headings sped first-pass reading and steered where readers looked back (abstract), and Lorch (1989) reviews the wider family of text signals. [NEEDS: your view on mark form — pause only, white space, rule, or label.]

**The reader's algorithmacy, and the problem of fluency.** Here algorithmacy departs most sharply from literacy. In reading, fluency is a plain good: the fluent reader decodes without effort and attends to meaning. In supervising an intermediary, fluency can be capture. The algorithmate user fits to the regularities of the system, and some of those regularities are the system's own engineering — its pace, its confident form, its finished recommendations. In an unmarked stream, fluency fits the co-optation. The fluent user accepts at speed and is navigated rather than navigating.

Marking resolves the tension without demanding slow, deliberate checking from everyone. It gives fluency something legitimate to fit to. Reading shows the pattern. Fluent adults do not outgrow word spaces; they rely on them without noticing, and when the spaces are removed they read about half as fast and regress almost twice as often (Rayner et al., 1998). In a marked stream, the fluent user can orient to marks in the same way: quick fixations and targeted regressions at the decision spaces, navigation that is fast without being blind. For the novice, a mark prompts the slow, effortful decoding with which any competence begins.

The resolution changes what counts as evidence of algorithmacy. Navigation (G) means acting on a decision space, not deliberating at length. Long dwell at a mark is evidence of decoding, not of mastery, which is why P11 predicts faster and better-targeted conversion of fixations into action rather than longer dwell. Whether marking matters more for novices than for experts is a hypothesis; I found no source that tests the parallel claim about word spacing and reading skill. [NEEDS: a source, or keep it stated as a hypothesis.]

### 4.10 Dissociating attention from navigation

The theory separates two things that eye-tracking studies often merge. Fixations and regressions at a decision space (F) are evidence that the reader perceived it. Supervisory navigation (G) is what the reader then does: accept, verify, reject or redirect. The separation has empirical warrant. Cho and Lim (2026) found that layouts moved first fixations on a source by up to fifteen seconds without moving trust. Parasuraman and Manzey (2010) explained commission errors as looking without seeing, on evidence that operators who missed a wrong diagnosis had often sampled everything needed to catch it. Yang et al. (2027) warned that shorter fixations on a hazard may signal overreliance rather than efficiency.

The separation also makes the theory falsifiable in a particular way. If marks at decision spaces raise F but not G, the theory's perceptual claim survives and its claim about navigation fails, or the failure lies with the reader's model of the intermediary (P9, P13). If marks raise G without raising F, something other than perception is doing the work.

### 4.11 What marking decision spaces is not

Marking resembles four neighbouring interventions, and differs from each. A cognitive forcing function imposes a delay or a task that the task itself does not require (Buçinca et al., 2021); marking reveals a boundary that the task already contains. A microboundary is "a small obstacle prior to an interaction" (Cox et al., 2016); marking structures the perception of output that is already under way. Selective friction impedes access to a model (Collins et al., 2024); marking acts inside the generated content. Concept suppression changes what the model produces (Disley & Khan, 2026); marking leaves the output unchanged and changes only how it is presented. In each comparison the difference is the same. Marking adds no obstacle. It makes visible a point that is already in the process, and it is placed by what the response says rather than by when the response arrives.

---

## 5. DISCUSSION: IMPLICATIONS AND RESEARCH AGENDA

The theory extends prior accounts in three ways. It moves the question of competence from knowledge *about* algorithms, the concern of algorithmic literacy, to navigation *through* an opaque intermediary, and it begins that move at the level of perception. It treats the structure of a stream — where its decision spaces fall — and not only its rate or its content. And it separates seeing a decision space from navigating it, which makes the gap between the two something a study can measure. This section sets out how to test the theory (5.1), what it implies for interface design (5.2), how far algorithmacy reaches beyond the text stream (5.3), and two counterpoints that a sceptical reader should press (5.4).

### 5.1 Severe testing: an evaluation strategy

No one has yet tested any of the thirteen predictions. Cutting and Deterding (2022) put "the severe testing" of their own theory first among the work it called for (§5.1) [NEEDS: page number; the copy I read is paginated 19 at that point, not in journal pages], and the same comes first here. The decisive test is simple to state. If pauses placed at decision spaces help supervision no more than the same number of pauses placed at arbitrary points, the benefit comes from delay, not from structure, and the theory is wrong about placement.

The design that follows from this is a three-condition, within-subjects eye-tracking experiment. [D26] In the first condition, participants supervise a continuous stream at a fixed rate. In the second, the stream pauses at arbitrary intervals, yoked so that each response has exactly as many pauses as in the third condition. In the third, the stream pauses at decision spaces located by the rule in Section 4.5. Responses are generated in advance and replayed, so that content is identical across conditions and only the presentation varies. Each response contains seeded errors of two kinds: local, clause-level factual distortions, and contradictions that span paragraphs. Stimulus domains are counterbalanced across conditions with a Latin square.

[ROGER] To evaluate whether structural boundaries restore supervisory vigilance, this paper specifies an empirical eye-tracking study (N = 42) [F2] comparing user supervision of streaming text containing seeded factual and inferential errors across three conditions: a continuous stream, a stream paused at arbitrary periodic intervals, and a stream paused at semantic decision units. The experiment investigates three formal research questions:

⚬ RQ1: Do breaks placed at decision units draw fixations and regressions to those points more than breaks placed at arbitrary intervals?
⚬ RQ2: Do decision-unit breaks improve detection of seeded errors relative to a continuous stream and to arbitrary breaks?
⚬ RQ3: Do arbitrary breaks impose a cost relative to a continuous stream in terms of detection latency, subjective workload, or local refixations? [/ROGER]

Gaze and outcome must be measured together, because the theory predicts that they can come apart (P9). The process measures are first-pass fixation duration, total dwell and the density of regression landings in areas of interest drawn around each decision space and each seeded error. The outcome measures are error detections and false alarms, detection latency, workload on the NASA-TLX, and calibrated trust. A high sampling rate eye tracker with velocity-based fixation classification will serve. [D26] Gaze alone cannot settle the question: shorter fixations can mean either efficient checking or overreliance (Yang et al., 2027), and only the outcome measures tell them apart.

The streaming rate needs care. Xiao and Yang's (2025) 99th-percentile comfortable speed for complex text was 11.97 words per second; a rate above that confounds the manipulation with discomfort. [D26]

Two caveats bound what such a study can show. Most of the evidence on which the theory rests comes from static or experimenter-paced text. Only Park and Lee (2024) and Bhat (2025) studied chatbot streaming, and only Park and Lee measured gaze. And a laboratory replay removes the interactivity of real use, where the reader can interrupt, scroll and ask again.

### 5.2 Design implications: interfaces that mark decision spaces

Current chat interfaces stream continuously by default. Continuous streaming is a design choice, made for the sake of perceived responsiveness, and an interface that marks decision spaces is a different choice. Four dimensions define it, each a trade-off.

*Placement.* Marks belong at decision spaces, located by the content of the response, and never at the points where network packets happen to fall. A mark at the wrong place is worse than none, because misaligned breaks cost reading time (Tsoukala et al., 2025) and interruptions in the middle of a task cost more than those between tasks (Bailey & Konstan, 2006).

*Form.* A mark should orient the eye without asking to be read. White space, a change in line spacing or a faint rule can provide a landmark in the parafovea; a label adds text that must itself be processed, and Prajod et al. (2026) found that even a one-line label drew substantial fixation. [D25] [NEEDS: your view; the specific values in your outline (a 0.5 pt rule) are design proposals with no source.]

*Duration.* A pause must be long enough to let the eyes leave the leading edge and short enough not to invite a switch to another task. Gould et al. (2016) found both failure modes in task lockouts. The right duration is an empirical question that P10 poses. [D24]

*Initiative.* The system places the marks, and the user may extend a pause, for instance by scrolling back or selecting text. Leaving placement to the user is unlikely to work: operators who could choose their own transparency did not use it to improve their decisions (Tatasciore et al., 2026). Cox et al. (2016) list user control over microboundaries as an open question, and the same question applies here.

The case for marking grows with autonomy. An agent that browses, writes and runs code produces a stream of actions rather than of words, and Chen et al. (2026) found that more than half of supervisory failures with a computer-use agent involved a mismatch of timing. Marking the decision spaces in an agent's run — before an irreversible action, after a claim that later steps depend on — turns a continuous run into stages a person can inspect. Kazemitabaar et al. (2024) found that decomposing an AI data analysis into steps made intervention, correction and verification easier than a conversational baseline (abstract), and Zhou et al. (2026) found that letting users edit a completed chain of reasoning raised correction success, mostly with simulated correctors.

### 5.3 Algorithmacy beyond the text stream

The perceptual layer is one layer of a wider competence. Decision spaces occur wherever an opaque process makes a judgment on someone's behalf or leaves one to them without saying so. A platform's ranking decides which seller a buyer sees. A dispatch algorithm decides which driver gets which trip, and at what price. A screening system decides which applicant a recruiter never reads. [NEEDS: your dissertation cases, with sources.] In none of these is there text to mark, but the structure is the same: a judgment point hidden in a process, and a person who must navigate it without seeing it.

Expert supervision of live visual streams shows what algorithmacy acquired over time looks like. The intelligence analysts in Lamb et al.'s (2026) study stopped treating an object-detection overlay as an advisor and wanted to learn its "boundary conditions": where, in effect, its decision spaces lay. That is the reader's model of the intermediary, built through use. Najjar and Nasir (2026) found that the structure of a human–AI exchange changed its outcome: across 244 participants, iterative critique produced more task-appropriate creative work than exchanges led by the AI's proposals (abstract only). [D27]

Predictions P11 to P13 need a measure of algorithmacy. The older competences show how such measures are built. Watson and Callingham (2003) validated a six-level hierarchy of statistical literacy, from idiosyncratic to critical-mathematical, with Australian school students; Mercer et al. (2017) assessed oracy through profiles across several tasks; and the OECD's adult skills survey pairs proficiency tasks with items on how often people use numeracy (Gal et al., 2020). Following Watson and Callingham's form, and Sharma's (2017) review of statistical-literacy models, I propose six levels of algorithmacy for later validation:

1. *Unaware or co-opted:* the user accepts output as given and relies on its fluency.
2. *Tacitly fitted:* the user moves fluently and quickly, fitted to the platform's regularities, but without reflection and easily misled.
3. *Aware but inconsistent:* the user knows the system can err but has no systematic way to check it.
4. *Consistent but non-critical:* the user follows explicit checking rules, often supplied from outside.
5. *Critical:* the user navigates decision spaces unprompted, with targeted regressions and checks of the system's boundary conditions.
6. *Critical-systemic:* the user models what the intermediary is optimizing and redirects or contests its course.

The levels are a proposal, built by analogy, and untested. Following Gal et al.'s (2020) five domains of numeracy, algorithmacy may also vary by domain — work and gig platforms, search and information, generative AI, civic and administrative systems, and social feeds. This paper sits in the generative-AI domain.

### 5.4 Two counterpoints

**Counterpoint 1: users resist friction, and any benefit may come from the pause alone.** The objection has strong support. Users resist systems that ask them to reflect: Forshaw et al.'s (2026) managers resisted an AI coach's probing questions. Users prefer cognitive forcing functions less and trust them less (Buçinca et al., 2021). Preparatory friction did not reduce reliance (Arun et al., 2026). [D28] Users may simply switch the marks off to get their flow back. And if marks help at all, the help might come from slowing the reader down, which any pause would do.

The theory has three answers. First, marking adds no task. It reveals a point already in the process, as a word space asks nothing of a reader, and the fluency resolution in Section 4.9 predicts that fluent users will pass through marks quickly rather than stall at them. Second, the pause-alone explanation is exactly what the arbitrary-pause condition tests. P6 predicts that marks at decision spaces will outperform the same number of arbitrary marks; if they do not, the theory is wrong about placement, and the study will have shown it. Third, stated dislike is a poor guide to effect. Forshaw et al. found that the coached behaviours appeared after both coaching sessions, whatever the managers said about the AI.

Some questions the theory cannot yet answer: whether users will tolerate marks in everyday use, whether the effects hold for expert users, and whether decision spaces can be located reliably in real, unplanned responses.

**Counterpoint 2: a laboratory measure of a perceptual skill repeats the autonomous model.** This objection comes from literacy studies, and an HCI reader may not anticipate it. Street (2003) argued that treating literacy as a neutral technical skill "disguises the cultural and ideological assumptions that underpin it." Scribner and Cole (1978) separated literacy from schooling among the Vai and found its cognitive consequences tied to particular practices (abstract). A critic could say that defining algorithmacy as an individual perceptual capacity, and measuring it with an eye tracker, makes the same error for a new medium.

The answer begins with scope. The paper claims one factor of algorithmacy, perception of decision spaces, tied to one practice, supervising streamed text. It claims no general change in cognition. The interpretive factor, the reader's model of the intermediary, is where practice, context and power enter, and my dissertation treats it at that level. Where the paper does claim consequences, it claims them in the specific and measurable form that Dehaene et al. (2015) show for reading.

The critique is also partly right, and the theory should concede it. Decision spaces are not neutral. Whether an interface marks them, hides them or places them is a design choice with interests behind it. A provider that streams continuously because continuous streaming feels responsive has chosen, whether it meant to or not, to leave its decision spaces unmarked. That is Street's point applied to interfaces, and it is why the perceptual layer cannot be the whole of algorithmacy.

---

## 6. CONCLUSION

Human oversight of AI will not be secured by asking for more literacy: more explanations, more disclosures, more training in how models work. Each of these treats the user as the reader of a finished text. A streamed response is not a finished text while it is being read. It is a performance by an opaque intermediary, delivered at a pace set by compute, and it takes from the reader three things that reading relies on: a stable target, a boundary between units, and a way back. In that performance the points that call for judgment arrive looking like points that call only for acceptance.

Algorithmacy theory names those points decision spaces and the competence of navigating them algorithmacy. At its perceptual layer it predicts that marking decision spaces will restore the target, the boundary and the way back, that the gain will depend on placing the marks where judgment is actually required, and that perception will help only as far as the reader's model of the intermediary allows. It also explains the puzzle with which the paper began. Readers grant streamed text more authority and agree with fluent answers whether right or wrong, because nothing in the stream shows them where to stop.

[ROGER] For years, human–computer interaction has asked whether users can comprehend what artificial intelligence writes; algorithmacy theory asks whether interfaces allow them to see where it leaves them a decision. [/ROGER]

---

## REFERENCES

Entries follow the verified master list in `FINAL_OUTLINE_HCI.md`. † marks an entry that still needs completing or checking. Three entries in your new outline are not cited in this draft and are left out: Keenan (1984) [D28], Mangen et al. (2013) and McDonald (2006). Cutting and Deterding (2022) is cited once, in §4.2 and §5.1. Secondary citations (Rayner & Pollatsek, 1989; Manzey et al., 2008; Wilkinson, 1965; Michael & Lupton, 2016) are attributed in the text through the source that cites them and get no entry; in APA 7 form they should read "as cited in".

- Arun, S., et al. (2026). Encouraging thought before completion: The role of task-specific selective friction in AI-assisted knowledge work. In *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work*. ACM. https://doi.org/10.1145/3808045.3808049 †authors, pages
- Bailey, B. P., & Konstan, J. A. (2006). On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state. *Computers in Human Behavior, 22*(4), 685–708. https://doi.org/10.1016/j.chb.2005.12.009
- Benedetto, S., Carbone, A., Pedrotti, M., Le Fevre, K., Bey, L. A. Y., & Baccino, T. (2015). Rapid serial visual presentation in reading: The case of Spritz. *Computers in Human Behavior, 45*, 352–358. https://doi.org/10.1016/j.chb.2014.12.043
- Bhat, M. (2025). How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131
- Booth, R. W., & Weger, U. W. (2013). The function of regressions in reading: Backward eye movements allow rereading. *Memory & Cognition, 41*(1), 82–97. https://doi.org/10.3758/s13421-012-0244-y
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287
- Cao, S., & Huang, C.-M. (2022). Understanding user reliance on AI in assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 6*(CSCW2), 1–23. https://doi.org/10.1145/3555572
- Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026). *Comparing human oversight strategies for computer-use agents* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2604.04918
- Cho, J., & Lim, D. (2026). How source attribution visualization shapes user attention and preference: An eye-tracking study of four AI chatbot layouts. *Journal of Eye Movement Research, 19*(4), Article 89. https://doi.org/10.3390/jemr19040089
- Collins, K. M., et al. (2024). *Modulating language model experiences through frictions* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2407.12804 †authors
- Cox, A. L., Gould, S. J. J., Cecchinato, M. E., Iacovides, I., & Renfree, I. (2016). Design frictions for mindful interactions: The case for microboundaries. In *Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems* (pp. 1389–1397). ACM. https://doi.org/10.1145/2851581.2892410
- Cutting, J., & Deterding, S. (2022). The task-attention theory of game learning: A theory and research agenda. *Human–Computer Interaction, 39*(5–6), 257–287. https://doi.org/10.1080/07370024.2022.2047971
- Dehaene, S., Cohen, L., Morais, J., & Kolinsky, R. (2015). Illiterate to literate: Behavioural and cerebral changes induced by reading acquisition. *Nature Reviews Neuroscience, 16*(4), 234–244. https://doi.org/10.1038/nrn3924
- Delgado, P., Vargas, C., Ackerman, R., & Salmerón, L. (2018). Don't throw away your printed books: A meta-analysis on the effects of reading media on reading comprehension. *Educational Research Review, 25*, 23–38. https://doi.org/10.1016/j.edurev.2018.09.003
- Disley, M., & Khan, M. (2026). Designing cognitive friction with concept suppression in large language models. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2708617
- Drieghe, D., Fitzsimmons, G., & Liversedge, S. P. (2017). Parafoveal preview effects in reading unspaced text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(10), 1701–1716. https://doi.org/10.1037/xhp0000441
- Duke, N. K., & Cartwright, K. B. (2021). The science of reading progresses: Communicating advances beyond the simple view of reading. *Reading Research Quarterly, 56*(S1), S25–S44. https://doi.org/10.1002/rrq.411 †pages taken from your outline; I could not verify them (Crossref lists none)
- Endsley, M. R. (2017). From here to autonomy. *Human Factors, 59*(1), 5–27. https://doi.org/10.1177/0018720816681350
- Forshaw, T., Hale, J., & Longmire, M. (2026). The Reflection Penalty: When managers accept leadership coaching from a human but not an AI agent. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2744236
- Gal, I., Grotlüschen, A., Tout, D., & Kaiser, G. (2020). Numeracy, adult education, and vulnerable adults: A critical view of a neglected field. *ZDM Mathematics Education, 52*(3), 377–394. https://doi.org/10.1007/s11858-020-01155-9
- Gegoff, I., Tatasciore, M., Bowden, V. K., & Loft, S. (2025). Deciphering automation transparency: Do the benefits of transparency differ based on whether decision recommendations are provided? *Human Factors, 67*(8), 776–794. https://doi.org/10.1177/00187208251318465
- Ghosh, A., Sarkar, A., Lindley, S., & Poelitz, C. (2026). *An experimental comparison of cognitive forcing functions for execution plans in AI-assisted writing: Effects on trust, overreliance, and perceived critical thinking* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2601.18033
- Gibson, J. J. (1979). *The ecological approach to visual perception*. Houghton Mifflin. †unread
- Gould, S. J. J., Cox, A. L., Brumby, D. P., & Wickersham, A. (2016). Now check your input: Brief task lockouts encourage checking, longer lockouts encourage task switching. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 3311–3323). ACM. https://doi.org/10.1145/2858036.2858067
- Harvey, H., Godwin, H. J., Fitzsimmons, G., Liversedge, S. P., & Walker, R. (2017). Oculomotor and linguistic processing effects in reading dynamic horizontally scrolling text. *Journal of Experimental Psychology: Human Perception and Performance, 43*(3), 518–536. https://doi.org/10.1037/xhp0000329
- Harvey, H., & Walker, R. (2018). Reading comprehension and its relationship with working memory capacity when reading horizontally scrolling text. *Quarterly Journal of Experimental Psychology, 71*(9), 1887–1897. https://doi.org/10.1080/17470218.2017.1363258
- Haverkamp, Y. E., Bråten, I., Latini, N., & Salmerón, L. (2023). Is it the size, the movement, or both? Investigating effects of screen size and text movement on processing, understanding, and motivation when students read informational text. *Reading and Writing, 36*(7), 1589–1608. https://doi.org/10.1007/s11145-022-10328-9
- Hoover, W. A., & Gough, P. B. (1990). The simple view of reading. *Reading and Writing, 2*(2), 127–160. https://doi.org/10.1007/BF00401799
- Hyönä, J., & Lorch, R. F. (2004). Effects of topic headings on text processing: Evidence from adult readers' eye fixation patterns. *Learning and Instruction, 14*(2), 131–152. https://doi.org/10.1016/j.learninstruc.2004.01.001
- Kazemitabaar, M., et al. (2024). Improving steering and verification in AI-assisted data analysis with interactive task decomposition. In *Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology*. ACM. https://doi.org/10.1145/3654777.3676345 †authors, pages
- Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025). Fostering appropriate reliance on large language models: The role of explanations, sources, and inconsistencies. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–19). ACM. https://doi.org/10.1145/3706598.3714020
- Knox, B. M. W. (1968). Silent reading in antiquity. *Greek, Roman and Byzantine Studies, 9*(4), 421–435. †unread
- Koornneef, A. (2024). On the readability of texts presented in sentence-by-sentence segments to beginner readers: Evidence from self-paced reading and eye tracking. *Reading and Writing, 37*(1), 69–87. https://doi.org/10.1007/s11145-023-10423-5
- Kumar, M., Goldstein, A., Michelmann, S., Zacks, J. M., Hasson, U., & Norman, K. A. (2023). Bayesian surprise predicts human event segmentation in story listening. *Cognitive Science, 47*(10), e13343. https://doi.org/10.1111/cogs.13343
- Kurby, C. A., & Zacks, J. M. (2008). Segmentation in the perception and memory of events. *Trends in Cognitive Sciences, 12*(2), 72–79. https://doi.org/10.1016/j.tics.2007.11.004
- Kurby, C. A., & Zacks, J. M. (2012). Starting from scratch and building brick by brick in comprehension. *Memory & Cognition, 40*(5), 812–826. https://doi.org/10.3758/s13421-011-0179-8
- Lamb, S. C., Byrne, M., Norman, T. J., Ramchurn, S. D., & Naiseh, M. (2026). What's informing trust and adoption? Can current cognitive models support expert adoption of AI? *Journal of Cognitive Engineering and Decision Making, 20*(2), 158–175. https://doi.org/10.1177/15553434261430550
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392
- Liu, C., Zhou, Q., Shen, X., Liu, X. B., Wu, T., & Chen, X. A. (2026). Behavioral indicators of overreliance during interaction with conversational language models. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–23). ACM. https://doi.org/10.1145/3772318.3790332
- Liu, J., Chung, J.-W., Wu, Z., Lai, F., Lee, M., & Chowdhury, M. (2024). *Andes: Defining and enhancing quality-of-experience in LLM-based text streaming services* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2404.16283
- Lorch, R. F. (1989). Text-signaling devices and their effects on reading and memory processes. *Educational Psychology Review, 1*(3), 209–234. https://doi.org/10.1007/BF01320135
- Mangen, A., Olivier, G., & Velay, J.-L. (2019). Comparing comprehension of a long text read in print book and on Kindle: Where in the text and when in the story? *Frontiers in Psychology, 10*, Article 38. https://doi.org/10.3389/fpsyg.2019.00038
- Mercer, N., Warwick, P., & Ahmed, A. (2017). An oracy assessment toolkit: Linking research and development in the assessment of students' spoken language skills at age 11–12. *Learning and Instruction, 48*, 51–60. https://doi.org/10.1016/j.learninstruc.2016.10.005
- Metzner, P., von der Malsburg, T., Vasishth, S., & Rösler, F. (2017). The importance of reading naturally: Evidence from combined recordings of eye movements and electric brain potentials. *Cognitive Science, 41*(S6), 1232–1263. https://doi.org/10.1111/cogs.12384
- Najjar, M. S., & Nasir, M. (2026). Dialogue patterns in human-AI co-creation: How interaction structure shapes output and process. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2717534
- Oberschelp, W. (1995). Developing analytical competency through informatics teaching. In *Integrating information technology into education* (IFIP Advances in Information and Communication Technology, pp. 115–126). Springer US. https://doi.org/10.1007/978-0-387-34842-1_12 †unread
- O'Regan, J. K. (2011). *Why red doesn't sound like a bell: Understanding the feel of consciousness*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199775224.001.0001 †unread
- O'Regan, J. K., & Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973. https://doi.org/10.1017/S0140525X01000115 †abstract only
- Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055
- Park, H., & Lee, Y. (2024). The effect of text movement on eye movements in generative AI chatbots. *Archives of Design Research, 37*(4), 181–197. https://doi.org/10.15187/adr.2024.08.37.4.181
- Parkes, M. B. (1992). *Pause and effect: An introduction to the history of punctuation in the West*. Scolar Press. †edition; unread
- Powers, S. A., & Scerbo, M. W. (2023). Examining the effect of interruptions at different breakpoints and frequencies within a task. *Human Factors, 65*(1), 22–36. https://doi.org/10.1177/00187208211009010
- Prajod, P., Cools, H., Röggla, T., Cesar, P., & El Ali, A. (2026). *Towards gaze-informed AI disclosure interfaces: Eye-tracking attentional and cognitive load while reading AI-assisted news* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2605.14999
- Rayner, K., Fischer, M. H., & Pollatsek, A. (1998). Unspaced text interferes with both word identification and eye movement control. *Vision Research, 38*(8), 1129–1144. https://doi.org/10.1016/S0042-6989(97)00274-5
- Resulbegoviq, H., Hlebec, V., Pejić Bach, M., & Stamatović, I. (2026). Eye tracking and AI-generated content: A systematic literature review of visual attention, cognitive processing, and user engagement. *Journal of Eye Movement Research, 19*(5), Article 97. https://doi.org/10.3390/jemr19050097
- Ridley, M., & Pawlick-Potts, D. (2021). Algorithmic literacy and the role for libraries. *Information Technology and Libraries, 40*(2). https://doi.org/10.6017/ital.v40i2.12963 †your outline adds pages 1–15; unverified
- Saenger, P. (1997). *Space between words: The origins of silent reading*. Stanford University Press. https://doi.org/10.1515/9781503619081 †unread
- Schotter, E. R., Tran, R., & Rayner, K. (2014). Don't believe what you read (only once): Comprehension is supported by regressions during reading. *Psychological Science, 25*(6), 1218–1226. https://doi.org/10.1177/0956797614531148
- Scribner, S., & Cole, M. (1978). Literacy without schooling: Testing for intellectual effects. *Harvard Educational Review, 48*(4), 448–461. https://doi.org/10.17763/haer.48.4.f44403u05l72x375
- Sharma, S. (2017). Definitions and models of statistical literacy: A literature review. *Open Review of Educational Research, 4*(1), 118–133. https://doi.org/10.1080/23265507.2017.1354313
- Sharmin, S., Špakov, O., & Räihä, K.-J. (2015). Dynamic text presentation in print interpreting – An eye movement study of reading behaviour. *International Journal of Human-Computer Studies, 78*, 17–30. https://doi.org/10.1016/j.ijhcs.2015.01.010
- Sharmin, S., et al. (2016). The reading process of dynamic text – A linguistic approach to an eye movement study. *SKY Journal of Linguistics, 29*. †your outline gives "Sharmin, Špakov, Räihä, & Lehtinen" and pages 35–60; unverified
- Stark, D., & Vanden Broeck, P. (2024). Principles of algorithmic management. *Organization Theory, 5*(2). https://doi.org/10.1177/26317877241257213 †your outline adds pages 1–28; unverified
- Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X., Mayer, L. W., & Smyth, P. (2025). What large language models know and what people think they know. *Nature Machine Intelligence, 7*(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7
- Street, B. (2003). What's "new" in New Literacy Studies? Critical approaches to literacy in theory and practice. *Current Issues in Comparative Education, 5*(2), 77–91. https://doi.org/10.52214/cice.v5i2.11369
- Tatasciore, M., Bennett, L., Bowden, V. K., Bell, J., Visser, T. A. W., McAnally, K., McCarley, J. S., Thompson, M. B., Shanahan, C., Morris, R., & Loft, S. (2026). Adaptable automation transparency: Should humans be provided flexibility to self-select transparency information? *Human Factors, 68*(1), 5–27. https://doi.org/10.1177/00187208251349269
- Timkey, W., Huang, K.-J., Oh, B.-D., Prasad, G., Arehalli, S., Linzen, T., & Dillon, B. (2026). Eye movements reveal a dissociation between prediction and structural processing difficulty in language comprehension. *Proceedings of the National Academy of Sciences, 123*(32), e2532230123. https://doi.org/10.1073/pnas.2532230123
- Tsoukala, A., Vogelzang, M., & Tsimpli, I. M. (2025). The influence of text segmentation on garden path processing: Evidence from self-paced reading and eye-tracking. *Language and Cognition, 17*, e58. https://doi.org/10.1017/langcog.2025.10009
- Watson, J. M., & Callingham, R. (2003). Statistical literacy: A complex hierarchical construct. *Statistics Education Research Journal, 2*(2), 3–46. https://doi.org/10.52041/serj.v2i2.553
- Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review, 28*(4), 1060–1092. https://doi.org/10.3758/s13423-020-01859-9
- Wu, Z., Wang, Y., Langer, M., & Feit, A. M. (2025). RelEYEance: Gaze-based assessment of users' AI-reliance at run-time. *Proceedings of the ACM on Human-Computer Interaction, 9*(3), 1–18. https://doi.org/10.1145/3725841
- Xiao, C., & Yang, B. Z. (2025). Streaming, fast and slow: Cognitive load-aware streaming for efficient LLM serving. In *Proceedings of the 38th Annual ACM Symposium on User Interface Software and Technology* (pp. 1–13). ACM. https://doi.org/10.1145/3746059.3747721
- Yang, Y., Lee, Y. M., Tabone, W., García de Pedro, J., Happee, R., & Merat, N. (2027). The effect of augmented reality on pedestrians' gaze patterns and crossing probability while interacting with automated vehicles. *International Journal of Human-Computer Studies, 217*, Article 103920. https://doi.org/10.1016/j.ijhcs.2026.103920
- Yantis, S., & Jonides, J. (1984). Abrupt visual onsets and selective attention: Evidence from visual search. *Journal of Experimental Psychology: Human Perception and Performance, 10*(5), 601–621. https://doi.org/10.1037/0096-1523.10.5.601
- Zacks, J. M., Speer, N. K., & Reynolds, J. R. (2009). Segmentation in reading and film comprehension. *Journal of Experimental Psychology: General, 138*(2), 307–327. https://doi.org/10.1037/a0015305
- Zacks, J. M., Speer, N. K., Swallow, K. M., Braver, T. S., & Reynolds, J. R. (2007). Event perception: A mind-brain perspective. *Psychological Bulletin, 133*(2), 273–293. https://doi.org/10.1037/0033-2909.133.2.273 †unread
- Zhou, H., Zhang, J., Lou, J., Liu, Y., Lu, C., Qu, J., & Li, J. (2026). *Deep interaction: An efficient human-AI interaction method for large reasoning models* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2607.14049
- Zhu, H., Wang, J., Xie, L., Ma, R., Sun, Y., Liu, F., Zheng, C., & Li, Q. (2026). Just-in-time tokens: Adaptive token pacing for cognitive-friendly LLM streaming. In *Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–8). ACM. https://doi.org/10.1145/3772363.3798936 †unread
- Zhu, X., Le Truong, K., Fogliato, R., Swamy, G., Zhang, W., Yang, M., Ye, L., Liu, B., Liu, M., Ilyas, A., & Wu, Z. S. (2026). *Justified or just convincing? Error verifiability as a dimension of LLM quality* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2604.04418

---

## DISCREPANCIES BETWEEN YOUR NEW OUTLINE AND THE SOURCES (your decision on each)

Each item gives what the outline says, what the source says with its locator, and what the draft does. Locators and values come from my notes in `FINAL_OUTLINE_HCI.md`, `abstract_intro_edit.md` (flags F1–F17) and the source texts in `debate/texts/` and `algorithmacy/texts/`.

**D1 — title.** The outline's title has two colons ("Spaces in the Stream: … Output: A Theory and Research Agenda"). The draft uses an em-dash before the subtitle. The model paper has one colon. Your call on wording.

**D2 — "we" for a sole author.** Your outline uses "we." Your style guide says solo-authored work uses "I." The body uses "I"; your abstract, which is your wording, still says "we."

**D3 — abstract claim stated as finding (same as F1).** "Systematically degrading supervisory scrutiny and error detection": no study I read shows that streaming lowers error detection. Bhat (2025) measured perceptions only; Park & Lee (2024) measured gaze, not detection. That is what the proposed study (RQ2, P6) would test. Possible fix: "may degrade".

**D4 — streaming speeds.** The outline says "Commercial LLM delivery speeds (~15–45 words/second) dramatically outpace comfortable human reading ingestion thresholds (~12–21 words/second)." Xiao & Yang (2025, §3.2) report a 99th-percentile *comfortable streaming speed* of 21.20 WPS (easy) and 11.97 WPS (complex), against about 45 WPS from the GPT-4o API. I found no source for "15." These are streaming-comfort percentiles, not reading or "ingestion" thresholds, and the paper did not measure comprehension (F6). Liu et al.'s 4.8 tokens/s is an estimate converted from a words-per-minute table (F4). The draft uses Xiao & Yang's values with those limits stated.

**D5 — "an unspaced grammar of legibility at the level of the stream."** "The Grammar of Legibility" is Parkes's chapter 3 title, and the chapter is unread. The draft states the idea without the phrase. Restore the phrase only if you adopt Parkes's frame after reading him.

**D6 — fixation and saccade values.** The outline gives "fixations (200–250 ms) and saccadic jumps (7–9 letter spaces)" with no source given. Rayner et al. (1998, Table 1) report spaced-text fixations of 253 and 250 ms and forward saccades of 7.3 and 7.9 characters. The draft uses those.

**D7 — Wolfe's reset.** The outline says that "absent a … 'break in the action,' top-down supervisory search cannot reset the priority map." Wolfe (2021, p. 1069) *suggests* that "if there is enough of a break in the action, the map may get reset," and asks whether event boundaries do it. It is a suggestion, not a finding, and he says nothing about what cannot happen. The draft keeps it as a suggestion. Proposition 2's "stimulus-driven attentional capture" is your wording; Wolfe suggests "attention capture" may be a misnomer.

**D8 — Kurby & Zacks "purge."** The outline says boundaries "trigger working memory to purge obsolete representations." Kurby & Zacks (2012) found global *and* incremental updating, with information carried across boundaries (goals mentioned more at fine boundaries without a goal change, OR = 2.29). "Purge" overstates it. The draft reports global and incremental updating.

**D9 — surprise vs surprisal.** The outline's §2.4 and §4.5 say "Bayesian surprisal." Kumar et al. (2023) use Bayesian *surprise*, computed with GPT-2. Surprise (the change in belief) and surprisal (negative log probability) are different measures; Timkey et al. (2026) use surprisal. The draft says "surprise" for Kumar.

**D10 — Mangen and scrolling.** The outline says material placeholders are "an affordance systematically crippled by scrolling digital displays (Mangen et al., 2013, 2019; Delgado et al., 2018)." Mangen et al. (2019) compared print with a Kindle, a page-turning device; scrolling was not tested. The draft says so and marks the step to streams as an inference.

**D11 — Bhat "objective effectiveness."** The outline says streaming raised ratings "without improving objective effectiveness." Bhat (2025, Table 2) measured *perceived* effectiveness, a self-report rating (F = 0.16, p = .69). There was no objective measure. The draft says "perceived."

**D12 — dynamic text and working memory.** The outline attributes "increases working-memory load during inferential processing" to five studies together. Harvey & Walker (2018) relate comprehension of scrolling text to working-memory capacity and found inference suffered (abstract); the others show different things. Haverkamp et al. (2023) studied reader-controlled scrolling of a PDF, not dynamic text (F9). The draft gives each study its own finding.

**D13 — Gegoff overstated.** The outline says recommendation framing "systematically suppresses critical discrimination and inflates agreement bias." Gegoff et al. (2025, pp. 785–787): discrimination .93 vs .94, ηp² = .05, while accuracy *rose* (.89 vs .85). "Agreement bias" is Tatasciore et al.'s (2026) finding about high transparency, not Gegoff's about recommendations. The draft reports the small effect.

**D14 — Tatasciore "rarely."** The outline says users "rarely opt to inspect complex rationales." Operators chose high transparency on 39% and 43% of adaptable trials (two experiments). The finding is that the choice did not improve accuracy (p. 22). The draft says so.

**D15 — Endsley (abstract only).** The draft paraphrases Endsley's (2017) "automation conundrum." I read it at abstract level only; check the wording against the article.

**D16 — Zhu et al. (2026) direction.** I recorded the change in the false-positive score (0.717 to 0.602) but not with certainty which direction is worse. The draft reports the numbers without interpreting them. Check §7.1 before you characterize it.

**D17 — Ghosh.** The outline groups Ghosh et al. (2026) with interventions users dislike. Its abstract reports that the "Assumptions" forcing function reduced overreliance most *without raising cognitive load*. The draft reports that.

**D18 — friction taxonomy.** (a) The outline says microboundaries are placed "prior to model access." Cox et al. (2016) define a microboundary as "a small obstacle prior to an interaction," for any interaction, not model access. (b) The outline says concept suppression "alter[s] underlying model weights." My notes say Disley & Khan suppress a concept at the model level; I did not record that weights are changed. The draft says the method "changes what the model produces."

**D19 — Forshaw "strong psychological reactance."** N = 8. All eight preferred the human coach and resisted the AI's questions, but the coached behaviours appeared after both (§6.1). "Strong reactance" overstates the measure, and the behavioural result cuts the other way. The draft reports both.

**D20 — Table 2 (comparative matrix) cells without sources.** The outline's column is "Oracy & SLA." I read nothing on second-language acquisition, so the draft drops "SLA." The oracy cells ("spoken stream," "prosody, pauses, turn-taking," "non-fluency") and the numeracy cells ("notation and the relations it states," "layout of working and proof") are reasonable but come from no source I read. Mercer et al. (2017) give oracy's four skill areas (physical, linguistic, cognitive, social and emotional); Gal et al. (2020) give numeracy's definition and domains. Either source the cells or cut the oracy and numeracy columns to what those papers say.

**D21 — Oberschelp.** The outline says Oberschelp used the word "in German school informatics." That is my earlier inference from the chapter's reference list, not a reading. The draft names the chapter and stops there until you read it.

**D22 — "low-spatial-frequency visual targets" (same as F7).** The outline's §4.6 says word spacing "establishes low-spatial-frequency visual targets (Rayner et al., 1998)." Rayner et al. say nothing about spatial frequency; they say spaces enhance words "as 'targets' for an eye movement" (p. 1129). The draft uses their wording.

**D23 — Schotter "7–10%."** The outline says eliminating regressions "drops comprehension by ~7–10%." Schotter et al. (2014, p. 1223) report 78% vs 71%, a 7-point difference. The draft gives those figures.

**D24 — Gould lockout durations.** The outline gives "~500–1000 ms" for brief lockouts and ">3000 ms" for long ones, and §5.2 proposes "~750 ms." I read Gould et al. (2016) at abstract level only and recorded no millisecond values. The draft gives no durations. Read the paper (open-access copy at the University of Birmingham repository) before stating any.

**D25 — Prajod reversed.** The outline says "subtle spatial rests and low-contrast rules orient visual attention without adding linguistic cognitive load; verbose disclosure labels increase extraneous processing (Prajod et al., 2026 …)." Prajod et al. found the opposite about labels: the *one-line* label drew more total fixation than the *detailed* label (58.70 vs 49.46, d = 0.34) and more saccades. They did not test spatial rests or rules. The draft reports the finding as it is.

**D26 — study parameters.** (a) N = 42 has no stated justification (F2). (b) "18 words/s / 24 tokens/s" exceeds Xiao & Yang's (2025) 99th-percentile comfortable speed for complex text (11.97 WPS), so the rate itself may cause discomfort; the draft leaves the rate open and says why. (c) "≥ 250 Hz, I-VT" is reasonable but unsourced; the draft says "high sampling rate" and "velocity-based." (d) The draft keeps your RQ paragraph verbatim, including N = 42.

**D27 — Najjar & Nasir "directly dictates."** The outline says interaction structure "directly dictates co-creative quality and critical steering." The abstract (all I read) reports that iterative critique produced more task-appropriate creativity than AI-led proposals, N = 244. The draft says that.

**D28 — Keenan (1984) misused.** The outline cites Keenan for users resisting friction and disliking delays. Keenan is about chunking and line length: chunked text was read more slowly, which the author attributes to variable line length. It says nothing about users' attitudes to friction. The draft drops it from Counterpoint 1. If you want it, it supports "segmented text can slow reading," not resistance. Its volume and pages (18(1), 61–80 in your outline) are unverified.

