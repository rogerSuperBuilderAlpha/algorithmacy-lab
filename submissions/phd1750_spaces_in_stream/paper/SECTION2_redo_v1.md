# Section 2 — full redo (21 October 2026)

> **Drafted by Claude (Opus 5.5) for Roger Hunt, around the argument and register of your rewrite.** Everything is my drafting except text inside `[ROGER] … [/ROGER]`, which is your wording kept verbatim. `[S#]` points to the check of your rewrite at the end of this file. Each item there says what your text said, what the source says, and what this redo does instead; nothing was corrected silently. `[NEEDS]` marks a claim resting on a source not read (Saenger, Parkes, Knox, Gibson, O'Regan & Noë, Zacks et al. 2007).
>
> **Citation status.** Every citation comes from the project library or from a record I pulled and checked on 21 October. [F] means read in full; [A] means I read the abstract via PubMed or OpenAlex.
> - New in this section, all [A]: Dehaene & Cohen (2007), Risko & Gilbert (2016), Zhang & Norman (1994).
> - The Dehaene et al. (2015), Drieghe et al. (2017), Kurby & Zacks (2008), Kumar et al. (2023) and Metzner et al. (2017) abstracts were re-read today.
>
> **Length.** About 2,900 words, against the outline's 2,800.

---

## 2. FOUNDATIONAL CONCEPTS: SCRIPTIO CONTINUA, READING, ATTENTION AND EVENTS

Reading is a cultural invention running on older equipment. Writing is too recent to have shaped the evolution of the human brain, yet in every literate person reading occupies the same region of cortex. Dehaene and Cohen (2007) explain that regularity with a neuronal recycling hypothesis: cultural inventions "invade evolutionarily older brain circuits and inherit many of their structural constraints." Learning to read reorganizes the ventral visual pathway. Responses to written characters grow in the left occipito-temporal sulcus, and responses to faces shift toward the right hemisphere (Dehaene, Cohen, Morais, & Kolinsky, 2015). [S1] Because reading borrows the visual system rather than owning one, it inherits that system's dependence on the arrangement of what it looks at. A reader takes nothing from a page without moving the eyes: finding targets, landing on them, and going back to earlier ones. Each of these acts depends on how the marks are laid out, and a streaming interface lays them out differently. [S2]

### 2.1 The historical precedent: scriptio continua, word separation and cognitive offloading

For centuries, Latin was written in *scriptio continua*, with letters run together and no spaces between words (Saenger, 1997). [NEEDS: page locators; Saenger and Parkes unread] [S3] Rayner, Fischer and Pollatsek (1998, p. 1129) note in passing that English, too, "was not always written with spaces." On Saenger's account, a reader of unseparated script had to sound the syllables, aloud or under the breath, to find where one word ended and the next began. Writing on this account was a script for voicing, and reading stayed bound to speech. [S4] Some classicists dispute how far ancient readers depended on reading aloud. [NEEDS: Gavrilov (1997) and Johnson (2000); see the track-down list.]

The space came, on Saenger's account, from the edge of the Latin world. Irish and Anglo-Saxon scribes, for whom Latin was a learned and foreign language rather than a spoken one, began separating words, and the practice spread over the following centuries to the Continent (Saenger, 1997). [NEEDS: dates and pages; your rewrite gives "the seventh and eleventh centuries"] [S5] Parkes (1992) traces the punctuation that developed alongside it. [NEEDS: Parkes unread]

The space added no information. Every letter on the page stayed where it was; only the arrangement changed. Zhang and Norman (1994) give the general principle. In a distributed cognitive task, the task is represented partly in the mind and partly in the world, and the external part can be analysed separately from the internal one. Change the external representation and the work the mind must do changes with it. A word space moves the finding of word boundaries out of the reader's phonological working memory and onto the page, where the eye can find them. Risko and Gilbert (2016) call the general move cognitive offloading: "the use of physical action to alter the information processing requirements of a task so as to reduce cognitive demand." The word space is an unusual case of it. The scribe performed the physical action, once, and every later reader received the reduction in demand. [S6]

Rayner, Fischer and Pollatsek (1998) measured what that reduction is worth to a skilled reader. They removed the spaces from English text, or filled them with letters or other characters, and recorded adult readers' eye movements. Reading rate fell by about half: by 54% for single sentences and 44% for passages in their first experiment, and by 58% in their second (pp. 1132, 1138). Regressions in sentence reading rose from 9.7% of eye movements to 17.3%, and in passages from 11.2% to 16.4% (Table 1). Readers stopped landing just left of a word's centre, where the eye usually lands, and landed nearer its beginning. [S7] Rayner and colleagues frame the space as doing two jobs (p. 1129). It aids word identification "by (among other things) making clear where a given word begins and ends." It also guides the eyes: spaces around the words to the right of the one being fixated "enhance them as 'targets' for an eye movement." Their data showed both effects. Removing spaces raised the effect of word frequency on fixation times, which shows interference with word identification, and it shifted landing positions, which shows interference with eye guidance. Word identification suffered more (p. 1143). [S8]

Drieghe, Fitzsimmons and Liversedge (2017) replicated the slowdown in unspaced reading. Using a gaze-contingent preview, they then asked whether readers compensate by spreading their processing across several words at once. They found "rather limited evidence" that they do. Their results point toward "a system that prefers narrowly focused processing of a single word, at least when means for easy word segmentation are available." [S9] The space lets the eye take one word at a time, and skilled readers use it to do exactly that.

Two points follow, and the argument needs both. First, fluent readers do not outgrow the space. Rayner et al.'s participants were skilled adults, and removing spaces still halved their reading rate. Second, the space is an aid, not a precondition. The same participants went on reading unspaced English, more slowly. Rayner et al. also note that written Chinese runs without spaces, because its characters, as morphemes, already mark units of meaning (p. 1129). [S10] Skilled reading leans on the space wherever the script offers one, and reading still survives without it. That is the relation this paper claims between marking and supervision.

[ROGER] A superficial objection immediately presents itself: conversational AI front-ends already print spaces between words. A streaming large language model does not output unspaced orthography; it delivers standard, punctuated text formatted in conventional typeface. Why, then, should ancient scriptio continua serve as an operative framework for generative AI? [/ROGER]

The objection is right about the word and wrong about the stream. A streamed response keeps word-level typography intact, but while it forms it lacks the units above the word that a finished page supplies. A finished page has paragraph breaks that stay where they are, headings, margins and white space, and it holds still. Together these show the reader where one unit of sense ends and the next begins. [S11] A response that is still streaming shows none of this. It arrives as a single, continuously extending run of text that scrolls itself. Nothing in it marks where a checkable claim ends, where the response commits to one course of action over another, or where it changes goal. [S12] The words are separated; the decisions are not. The problem of scriptio continua returns one level up.

The parallel has limits, and stating them sharpens it. Medieval readers set their own pace, whereas a reader of a stream follows a pace set by the provider's compute (Liu et al., 2024; Xiao & Yang, 2025). Silent reading was also not born with the word space: there is evidence of it in classical antiquity, before word separation (Knox, 1968). [NEEDS: Knox unread] Rayner et al.'s data agree from the other side, since skilled readers read unspaced text, if slowly. The space did not create the capacity to read silently. It made silent reading easy enough to become ordinary, by moving the segmentation task from memory to the eye.

The claim this paper makes is the same in kind. Marking a decision space will not make an uncritical user a competent supervisor. It moves the work of finding the point of judgment from the user's memory and vigilance onto the display. [ROGER] Just as the scribal word space did not automatically teach an illiterate person how to read, marking a decision space makes an operational boundary perceptible without dictating how the human supervisor should act. [/ROGER] The space between words supplied the perceptual conditions for literacy without supplying literacy. Marking decision spaces would supply the perceptual conditions for algorithmacy in the same way, and only those.

### 2.2 Oculomotor mechanics: saccade targets, regressions and repair

Reading alternates fixations, brief pauses in which the eyes are nearly still and take in text, with saccades, rapid jumps between fixations. In Rayner et al.'s (1998) spaced conditions, fixations averaged about 250 ms and forward saccades about 7 to 8 characters (Table 1). [S13] The eyes do not only move forward. Regressions, saccades back to text already passed, make up 10–15% of eye movements by one estimate (Schotter, Tran, & Rayner, 2014, p. 1225) and 15–25% by another (Booth & Weger, 2013, citing Rayner & Pollatsek, 1989).

Regressions exist to reread. Booth and Weger (2013) separated two accounts: that readers look back to take in the earlier text again, or that they look back to the place where a word was as a cue to memory, whatever is now there. Across three experiments the evidence favoured rereading. When the earlier text was made illegible, readers regressed less, and their regressions no longer predicted comprehension. Booth and Weger drew the implication for screens themselves: readers "of scrollable text on small screens" may find that "rereading is often impossible" (General Discussion).

Taking the way back away costs comprehension. Schotter, Tran and Rayner (2014) used a trailing mask, which replaced each word with a row of x's once the eyes had passed it, so that a regression found nothing to reread. Forty readers read single-line sentences, some with temporary syntactic ambiguities (garden-path sentences) and some without. The mask lowered comprehension (b = −0.92, z = 5.09, p < .001), and it did so for unambiguous sentences as well as garden-path ones (p. 1221). Comprehension was 78% in normal reading on trials without a regression and 71% under the mask (p. 1223). Readers, the authors conclude, should not believe what they read only once.

Rereading also carries work that forward reading does not. Timkey et al. (2026) recorded the eye movements of 368 readers and compared them with a language model's predictions. Surprisal, the model's measure of how unexpected each word was, explained early reading effects. It did not explain the rereading cost at the point where a sentence's structure was disambiguated, which the authors attribute to "the cost of detecting or correcting errors in the structure-building process." Metzner, von der Malsburg, Vasishth and Rösler (2017) reached the same point with brain potentials. Readers who met a syntactic or semantic violation either regressed, which went with a P600 response and good comprehension, or pressed on with a "good-enough" interpretation and comprehended worse. Free reading beat word-by-word presentation only on trials in which the eyes went back.

Displays that pace the reader remove that option. Rapid serial visual presentation shows one word at a time in a fixed place, so the reader can neither look back nor preview what comes next; Benedetto et al. (2015) found that it hurt literal comprehension (abstract). Metzner et al.'s word-by-word condition is the same kind of display. In each case comprehension depended on a regression that the display either allowed or prevented. A stream that moves earlier text up and out of view, while new text claims the eyes at the bottom, approaches the same condition. [S14]

### 2.3 Visual search, abrupt onsets and priority maps

Something new in the visual field draws the eye, under conditions. Yantis and Jonides (1984) showed that in visual search an item appearing abruptly is identified first, ahead of items present from the start. They also bounded the effect: capture of this kind occurs "only when the visual field contains but one such event" (p. 617).

Wolfe's (2021) Guided Search 6.0 puts such effects inside a general model of where attention goes next. Five sources of guidance feed a single priority map: top-down and bottom-up feature guidance, prior history, reward, and scene syntax and semantics (p. 1060). Attention visits the most active location on the map "approximately 20 times per second." The sources differ in how long they last. Bottom-up salience "may be a very powerful but short-lived form of guidance" (p. 1069). Wolfe endorses Lamy and colleagues' view that "attention capture" may be a misnomer: a salient onset creates "bumps in the priority map," which often win the competition for the next deployment of attention without seizing attention outright. [S15]

Wolfe then makes the point on which this paper's mechanism depends. Priority evolves over time. In "visual marking," people searching a display can deprioritize items they have already previewed and favour items that arrive later (Watson & Humphreys, 1997, as discussed in Wolfe, 2021, p. 1069). [S16] That evolution has a limit: "If there is enough of a break in the action, the map may get reset." Wolfe adds that "it would be interesting to see if the maps are reset by event boundaries" (p. 1069). He proposes the reset; he does not test it. [S17]

Read together, the two papers describe a reader facing a stream. Each new token is an onset, and while it appears alone against static text it meets Yantis and Jonides's condition. Its salience is brief, but the stream renews it many times a second. The map keeps favouring what has just arrived over what has already been seen, which is what visual marking would predict. Nothing in a continuous stream supplies the break that, on Wolfe's suggestion, would let the map reset.

### 2.4 Event segmentation and situation-model updating

People parse continuous activity into events. Kurby and Zacks (2008) summarize the evidence:
- segmentation runs constantly during ordinary perception;
- events are segmented at several timescales at once, and grouped hierarchically;
- activity in posterior temporal, parietal and lateral frontal cortex rises briefly at event boundaries.

Segmentation is tied to updating working memory, to what is later remembered, and to learning new procedures. Event Segmentation Theory explains it as a by-product of prediction: the mind integrates the recent past to predict the near future, and a boundary falls where prediction error rises (Kurby & Zacks, 2008; Zacks et al., 2007). [NEEDS: Zacks et al. 2007 unread; this paraphrase follows Kurby & Zacks 2008 and Kumar et al. 2023]

Readers segment text the same way. Zacks, Speer and Reynolds (2009) found that changes in the situation a narrative describes predicted where readers placed event boundaries: changes in characters, goals, causes, objects or locations. Reading slowed at those changes. Each additional situation change added 92.8 ms of reading time, and each 10% rise in the probability of a boundary added about 108 ms. Segmentation also survived pacing that the reader did not control. In a visual-sequential condition, software presented one clause at a time at about 3.35 words per second, with no way to go back. Readers still segmented the text hierarchically: their coarse and fine boundaries aligned above chance (t(26) = 2.97). [S22] Of the conditions studied in the reading literature, this one comes closest to a stream.

Boundaries are where the reader's model of the situation gets rebuilt. Kurby and Zacks (2012) found two kinds of updating. Readers updated globally, rebuilding the model at boundaries, and incrementally, adding detail as they went. At fine-grained boundaries they mentioned goals more often even when no goal had changed (OR = 2.29). [S18]

Boundaries can also be computed from the text itself. Kumar et al. (2023) used the GPT-2 language model to compute, word by word, the predicted distribution of the next word in three stories, and asked listeners to mark event boundaries. The boundaries went with transient rises in Bayesian surprise, the change in the model's beliefs. They did not go with surprisal, the simpler measure of how unexpected each word was. [S19] The finding supports prediction error as the control signal for segmentation. For this paper it also matters practically: a boundary in a text can be located before anyone reads it.

### 2.5 Ecological and sensorimotor perception: text as a stable object

[NEEDS: the first two sentences of this paragraph rest on Gibson (1979) and O'Regan & Noë (2001), both unread (the latter at abstract level). Check the wording against the texts.] On the ecological view, perception picks up affordances: the possibilities for action that an environment offers the perceiver (Gibson, 1979). On the sensorimotor view, seeing is the exercise of mastery over sensorimotor contingencies, the lawful ways in which sensory input changes as the perceiver moves (O'Regan & Noë, 2001; see also O'Regan, 2011). On both views, reading is an action performed on a stable object. The eyes move, and the page answers each movement in the same way every time. A word read a moment ago is still where it was, and a regression lands on it.

Printed text supplies that stability, and the evidence suggests that readers use it. Mangen, Olivier and Velay (2019) gave 50 readers a 28-page story, in print or on a Kindle. Print readers were better at reconstructing the order of the plot's events (t(48) = 2.03, η² = .08). The authors tie the advantage to the "material placeholders" that a physical book offers the hands and eyes, citing Gibson and O'Regan and Noë. Delgado, Vargas, Ackerman and Salmerón's (2018) meta-analysis found that readers comprehend better on paper than on screens, and that the advantage grew under time pressure (as reported in Mangen et al., 2019). [S20]

Neither study tested scrolling or streaming. Mangen et al. compared print with a page-turning device. The step from their findings to a stream is mine, and it runs as follows. A page and a screen of fixed text both stay put. A scrolling screen keeps text in a fixed order but moves it. A streaming response moves its earlier text while it is still adding new text, in amounts and at times that the reader does not choose. Each step removes some of the stability on which the sensorimotor account says reading depends. A stream, on this account, is the least stable reading surface of the four. [S21]

---

## CHECK OF YOUR REWRITE (your decision on each)

Each item quotes or locates your text, gives the source value, and says what the redo does.

**S0 — your opener contradicts your own analysis of the model.** Your analysis says Cutting & Deterding use no meta-announcements. Your opening paragraph ends on a roadmap ("This section establishes those baselines: tracing how … (2.1) … (2.5)"). C&D's §2 has no lead paragraph at all: it goes from the heading "2. A brief introduction to attention" straight to "2.1. Key terminology" (model text, lines 182–183). Your introduction already carries a roadmap with the same subsections. The redo keeps a short lead paragraph, because your plan asks for one, and drops the roadmap.

**S1 — neuronal recycling overstated.** You wrote that reading "repurposes ancestral visual and motor circuits originally evolved for object recognition, spatial tracking, and tactile manipulation."
- Dehaene & Cohen (2007, abstract) say cultural inventions "invade evolutionarily older brain circuits and inherit many of their structural constraints," and locate letter strings in left occipito-temporal cortex.
- Dehaene et al. (2015, abstract) describe a reorganized ventral occipito-temporal pathway, with face responses shifting rightward.

Neither abstract mentions motor circuits, spatial tracking or tactile manipulation. The redo keeps to the visual pathway. Both papers are new citations, verified at abstract level (Dehaene & Cohen: *Neuron, 56*(2), 384–398).

**S2 — "incapacitate."** "To understand why contemporary streaming interfaces incapacitate human supervision" states as fact what the paper predicts and has not tested. The redo states what the interface does (lays the marks out differently) and leaves the effect to the theory.

**S3 — what scriptio continua lacked.** "An unbroken ribbon of uppercase characters lacking word spaces, punctuation, capitalization, or paragraph divisions … (Parkes, 1992; Saenger, 1997)."
- Both books are unread.
- Parkes's book is a history of punctuation in the West that begins in antiquity, so "lacking punctuation" is the claim most likely to fail against him.
- "Uppercase" and "for more than a millennium" also need page locators.

The redo claims only the missing word spaces, with [NEEDS].

**S4 — "solely" and "interpretive monopoly."**
- "Conceptualized writing *solely* as a passive acoustic script" contradicts your own later sentence citing Knox (1968) for silent reading in antiquity.
- "Preserved an interpretive monopoly for an elite scribal caste" has no source in the library and is a strong social-historical claim.

The redo attributes the oral-reading view to Saenger, notes that classicists dispute it, and drops the monopoly claim. Restore it only with a source.

**S5 — the Insular scribes' languages.** "Whose native Celtic and Old English tongues shared no Romance linguistic roots with Latin" is muddled. Romance languages descend *from* Latin, so Latin has no "Romance roots." Celtic and Old English are both Indo-European, as Latin is, so they do share deep roots. The point you need, on Saenger's account, is that Latin was a *foreign, learned* language for these scribes. The redo says that.

**S6 — offloading citations.** Risko & Gilbert (2016) define offloading as the agent's own physical action reducing the agent's own demand (tilting your head, setting a reminder). The word space is one person acting so that a later person's demand falls. That is closer to Zhang & Norman's (1994) external representations, so the redo leads with them and marks the word space as an unusual case of offloading.

"The representational effect" (your phrase) is not in Zhang & Norman's abstract. It may be in the paper, but check before using the term.

**S7 — landing positions.** "Migrated … to its extreme left boundary": Rayner et al. report that landing positions moved toward the beginning of words. "Extreme" overstates it.

Also: "reading rates plummeted by 44% to 54% in their first experiment" is right, but the abstract summarizes all of it as "approx. 50%." The redo gives both.

**S8 — "low-spatial-frequency optical guides" (same as F7, D22).** Not in the paper (I searched the full text for "spatial frequency"). The quoted phrase is "enhance them as 'targets' for an eye movement" (p. 1129). It sits in the introduction's framing of what spaces do, and it is about words to the right of fixation. The redo quotes it as framing and reports the experiments' two effects separately.

**S9 — Drieghe et al. (2017) characterized wrongly.**
- "Replicating this work" is half right: they replicate the slowdown, but their experiment was a different paradigm (boundary preview).
- "Severely degrades parafoveal preview benefit" is not in the abstract. They found limited evidence that readers spread processing across words, and a system that prefers "narrowly focused processing of a single word."

The redo reports that.

**S10 — "mature literacy depends upon it completely."** Rayner et al.'s own data contradict "completely": the same skilled readers read unspaced text at roughly half speed. Rayner et al. also note that Chinese runs without spaces because its characters delimit units of meaning (p. 1129). This helps your argument. The space is an aid that skilled reading relies on, not a precondition, which is exactly the relation you claim between marking and supervision. The redo makes that move.

**S11 — Parkes's "grammar of legibility" used as his concept.** "What Parkes (1992) terms the 'grammar of legibility' at the macro-level of the stream." That is Parkes's chapter 3 title (verified), but the chapter is unread, so attributing to him the content you give it (paragraph breaks, margins, temporal stillness) is unsupported. The redo describes the finished page's units without the phrase. Read the chapter and the phrase may well fit.

**S12 — "idempotent filler" (same as I15).** The redo describes the three kinds of point (a checkable claim ends, a course of action is chosen, the goal changes) without the term.

**S13 — fixation and saccade values.** Not in your rewrite, but your plan names "Fixation/Saccade Baseline." The redo uses Rayner et al.'s (1998, Table 1) measured values, about 250 ms and 7–8 characters, not the textbook "200–250 ms, 7–9 letters" from the earlier outline. That range probably comes from Rayner's (1998) *Psychological Bulletin* review (see the track-down list).

**S14 — "Why Serial Streams Starve Look-Backs" (your plan).** The basic evidence (trailing mask, RSVP) concerns displays that pace or block the reader, not streams. The redo states the analogy as an approach to a condition, and leaves the stream studies (Sharmin, Harvey, Haverkamp) to §3, where the model paper puts applied work.

**S15 — "Why Continuous Token Onsets Seize the Priority Map" (your plan).** Wolfe endorses the view that capture "may be a misnomer": an onset creates a bump in the map, not a seizure. The redo uses "bump" and "favouring."

**S16 — "visual marking" is an existing term in visual search.** Watson & Humphreys (1997) coined it for deprioritizing previewed items in favour of new ones. Wolfe discusses it on p. 1069, in the same passage as the "break in the action." This matters twice.
- *Mechanism:* visual marking predicts that a reader's priority map will favour new tokens over text already seen, which is your leading-edge pull, with a literature behind it.
- *Term collision:* your intervention is also called "marking," and in this literature the word means nearly the opposite: inhibiting old items rather than highlighting a point of judgment.

Either distinguish the two terms in one sentence, or reconsider the name, which is already open (I19).

**S17 — "The Necessity of a 'Break in the Action'" (your plan).** Wolfe *suggests* that a break "may" reset the map, citing Kunar et al. (2003, 2006), and proposes testing event boundaries. "Necessity" overstates it. The redo keeps it as a proposal.

**S18 — "purge" (same as D8).** The redo reports global and incremental updating.

**S19 — Kumar et al. (2023) on surprisal.** The abstract (re-read today) says boundaries tracked Bayesian surprise "but not … surprisal." This sharpens D9. It also bears on §4.5: the surprise-peak criterion must use Bayesian surprise, and surprisal will not do.

**S20 — Delgado et al. (2018).** Abstract-level, through Mangen et al. (2019). Read the meta-analysis before stating the moderator.

**S21 — "The Sensorimotor Break in Scrolling Streams" (your plan).** No study in the library tests scrolling or streaming against the sensorimotor account. The redo states the four-surface ordering as the paper's own inference.

**S22 — a correction to my own earlier drafts.** Rechecking `notes/zacks2009.md`, I found two errors in what I wrote earlier (outline v4 and `DRAFT_full_v1.md` §2.4 and §4.7).
- Zacks et al. coded changes in characters, goals, causes, objects and locations; I had written "place or time."
- In the visual-sequential condition, the reported result is that coarse and fine boundaries *aligned* above chance (t(26) = 2.97), not that readers "placed boundaries above chance."

I have fixed both in this redo and in `DRAFT_full_v1.md`.

---

## PAPERS TO TRACK DOWN (records checked 21 October; none read)

**To make §2.1 defensible. These are the priority, because the history is the paper's founding analogy:**
1. **Saenger, P. (1997).** *Space between words*. Stanford University Press. Chapters on Irish and Anglo-Saxon word separation, for dates, locators, and the foreign-language argument.
2. **Parkes, M. B. (1992).** *Pause and effect*, chapter 3, "The Grammar of Legibility." Needed before using the phrase.
3. **Knox, B. M. W. (1968).** Silent reading in antiquity. *Greek, Roman and Byzantine Studies, 9*(4), 421–435.
4. **Gavrilov, A. K. (1997).** Techniques of reading in classical antiquity. *The Classical Quarterly, 47*(1), 56–73. https://doi.org/10.1093/cq/47.1.56. Its opening states the received view that Greeks and Romans "always, or nearly always, read aloud." Read it to see how far it challenges that view.
5. **Johnson, W. A. (2000).** Toward a sociology of reading in classical antiquity. *American Journal of Philology, 121*(4), 593–627. https://doi.org/10.1353/ajp.2000.0053. A classicist's account of ancient reading practice. Read it to check how a reviewer from classics would receive the Saenger story.

**To strengthen §§2.2–2.3:**
6. **Rayner, K. (1998).** Eye movements in reading and information processing: 20 years of research. *Psychological Bulletin, 124*(3), 372–422. https://doi.org/10.1037/0033-2909.124.3.372. The standard source for baseline fixation and saccade values.
7. **Rayner, K. (2009).** Eye movements and attention in reading, scene perception, and visual search. *Quarterly Journal of Experimental Psychology, 62*(8), 1457–1506. https://doi.org/10.1080/17470210902816461. Ties reading to visual search, the bridge between §2.2 and §2.3.
8. **Watson, D. G., & Humphreys, G. W. (1997).** Visual marking: Prioritizing selection for new objects by top-down attentional inhibition of old objects. *Psychological Review, 104*(1), 90–122. https://doi.org/10.1037/0033-295X.104.1.90. **The most important new find** (S16): a mechanism for the leading-edge pull, and a term collision.
9. **Kunar, M. A., Humphreys, G. W., Smith, K. J., & Hulleman, J. (2003).** What is "marked" in visual marking? *Perception & Psychophysics, 65*(6), 982–996. https://doi.org/10.3758/BF03194828. Also Kunar, M. A., Shapiro, K. L., & Humphreys, G. W. (2006). Top-up search and the attentional blink: A two-stage account of the preview effect in search. *Visual Cognition, 13*(6), 677–699. https://doi.org/10.1080/13506280500463195 These are the evidence behind Wolfe's "break in the action."
10. **Theeuwes, J. (2010).** Top-down and bottom-up control of visual selection. *Acta Psychologica, 135*(2), 77–99. https://doi.org/10.1016/j.actpsy.2010.02.006. The standard review on capture, if a reviewer presses on onsets.
11. **Chun, M. M., Golomb, J. D., & Turk-Browne, N. B. (2011).** A taxonomy of external and internal attention. *Annual Review of Psychology, 62*, 73–101. https://doi.org/10.1146/annurev.psych.093008.100427. The model paper's opening definition, if you want the same anchor.

**To strengthen §2.4:**
12. **Zacks, J. M., Speer, N. K., Swallow, K. M., Braver, T. S., & Reynolds, J. R. (2007).** *Psychological Bulletin, 133*(2), 273–293. Already cited and still unread.
13. **Zacks, J. M. (2020).** Event perception and memory. *Annual Review of Psychology, 71*, 165–191. https://doi.org/10.1146/annurev-psych-010419-051101. The current review of Event Segmentation Theory, which could replace leaning on the 2007 paper.
14. **Zwaan, R. A., & Radvansky, G. A. (1998).** Situation models in language comprehension and memory. *Psychological Bulletin, 123*(2), 162–185. https://doi.org/10.1037/0033-2909.123.2.162. The standard source for the situation-model dimensions (time, space, causation, protagonist, goal) that Zacks et al. (2009) coded.

**To make §2.5 more than an inference:**
15. **Gibson (1979)**, the chapter on affordances, and **O'Regan & Noë (2001)**, full text. Both are already cited and unread.
16. **Kirsh, D. (1995).** The intelligent use of space. *Artificial Intelligence, 73*(1–2), 31–68. https://doi.org/10.1016/0004-3702(94)00017-U. On how people arrange their surroundings to simplify perception and choice. It would join §2.1's offloading argument to §2.5.

**New references this section adds to the master list (verified records):**
- Dehaene, S., & Cohen, L. (2007). Cultural recycling of cortical maps. *Neuron, 56*(2), 384–398. https://doi.org/10.1016/j.neuron.2007.10.004
- Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences, 20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002
- Zhang, J., & Norman, D. A. (1994). Representations in distributed cognitive tasks. *Cognitive Science, 18*(1), 87–122. https://doi.org/10.1207/s15516709cog1801_3
- Watson, D. G., & Humphreys, G. W. (1997), as above. It is cited in §2.3 through Wolfe (2021); add a full entry only after reading it, otherwise cite it as "as discussed in Wolfe, 2021."
