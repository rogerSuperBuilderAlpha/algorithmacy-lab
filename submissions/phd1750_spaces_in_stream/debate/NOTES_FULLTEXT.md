# Full-text reading notes (2026-10-20)

PDFs from Roger's Downloads, copied to `debate/pdfs/`; text extracted to `debate/texts/` with pdftotext. I read each one myself. Each entry gives its depth of reading. Locators refer to journal page numbers, or to section numbers where a PDF has no page numbers.

Not supplied, so still abstract only or unread: Najjar & Nasir (2026), Khan et al. (2026), Kula & Avcı (2026), Gill (2026), Zhang et al. (2026), O'Regan & Noë (2001), Powers & Scerbo (2023), Saenger (1997), Parkes (1992), Gibson (1979).

---

## Sources your intro cites

### Rayner, Fischer & Pollatsek (1998). Vision Research 38(8), 1129–1144. Read in full.
- Design: Exp. 1, N = 12, sentences and passages, spaced vs unspaced. Exp. 2, N = 10, five spacing conditions (normal, wide, flanker, filled, none).
- Reading rate fell by 54% (sentences) and 44% (passages) without spaces (Exp. 1, p. 1132; Table 1). In Exp. 2 the fall was 58% (p. 1138). The abstract says "approx. 50%".
- Regressions rose without spaces: 9.7% → 17.3% (sentences) and 11.2% → 16.4% (passages) (Table 1).
- Landing position: with spaces, readers landed a bit left of the word's centre; without them, at the word's beginning (pp. 1136, 1141).
- Conclusion: removing spaces interferes with both word identification and eye-movement control. The authors think interference with word identification is "the larger contributor" (p. 1143).
- **Not in the paper:** "low-spatial-frequency boundaries" and any claim about parafoveal vision guiding targeting in those terms. Spaces "enhance them as 'targets' for an eye movement" (p. 1129) is the nearest sentence.

### Schotter, Tran & Rayner (2014). Psychological Science 25(6), 1218–1226. Read in full (JSTOR scan; some text garbled).
- N = 40 UCSD undergraduates; 40 garden-path sentences plus unambiguous versions; single sentences, one line each.
- Trailing mask: each word turned to x's once the reader's eyes moved past it.
- Comprehension fell under the trailing mask: b = −0.92, z = 5.09, p < .001. The effect held for unambiguous sentences too (interaction p = .06) (p. 1221).
- Comprehension by trial type: 84% after a regression in normal reading, 78% with no regression in normal reading, and 71% under the mask with no regression (p. 1223).
- Readers regress 10–15% of the time (p. 1225).

### Bhat (2025). IUI '25, 846–860. Read in full.
- N = 103 non-technical adults; within-subjects; GPT-3.5 Turbo. "Dynamic" means simulated typing at 2–3 s per sentence; "static" means the whole reply at once (§3.1).
- Higher with dynamic display: competence F = 40.89, trustworthiness F = 35.21, persuasiveness F = 76.89, accountability F = 88.91, and others, all p < .0001 (Table 2).
- No difference in perceived effectiveness (F = 0.16, p = .69), bias, or learning support. The author reads the effectiveness null as users "differentiate between how information is presented and its actual utility" (§5.1.1).
- Limitations: all measures are self-report Likert items; there is no accuracy task. GPT-3.5 may have given different responses in the two conditions (§5.5). The method says "In the first session ... dynamic" but also says order was counterbalanced (§3.1).

### Yantis & Jonides (1984). JEP:HPP 10(5), 601–621. Read: abstract, introduction, Exp. 1 method, General Discussion.
- An abrupt-onset item is identified first in visual search (Exps. 1 and 3; N = 18 in Exp. 1).
- Key limit (p. 617): "the occurrence of an abrupt onset does not by itself constitute a sufficient stimulus for capturing attention ... Apparently only when the visual field contains but one such event ... can attention be engaged in the manner illustrated by these experiments."
- The paper does not study motion transients.

### Wolfe (2021). Psychonomic Bulletin & Review 28(4), 1060–1092. Read: abstract, introduction, guidance sections (pp. 1060–1071). The simulation sections were not read.
- Guided Search 6.0 has five sources of guidance; attention goes to the peak of a "priority map" about 20 times per second (abstract).
- Bottom-up salience "may be a very powerful but short-lived form of guidance" (p. 1069).
- "'attention capture' may be a misnomer ... stimuli for attention capture create bumps in the priority map" (p. 1069, citing Lamy et al., 2020).
- **For decision spaces (p. 1069):** "If there is enough of a break in the action, the map may get reset ... it would be interesting to see if the maps are reset by event boundaries (Zacks & Swallow, 2007)."

---

## Debate papers to cite

### Gegoff, Tatasciore, Bowden & Loft (2025). Human Factors 67(8), 776–794. Read in full.
- N = 142 students; UV management task; additional information (none, medium, high) between subjects; recommendation (absent, present) within subjects; 120 trials; recommender 82.5% correct.
- Recommendations raised accuracy (.89 vs .85, F(1,139) = 27.0, ηp² = .16) and sped decisions (p. 785).
- Recommendations lowered information-accuracy discrimination: .93 with vs .94 without, F(1,94) = 4.55, p = .04, ηp² = .05 (p. 787). The effect is small.
- Additional information improved accuracy only when recommendations were present. The core predicted interaction was not supported (pp. 790–791).
- The authors call for eye tracking to see what operators attend to (p. 790).

### Tatasciore et al. (2026). Human Factors 68(1), 5–27. Read: introduction, both experiments, aggregated analysis, general discussion.
- Exp. 1: N = 73 (a priori power: d = .43, power .95, minimum 73). Exp. 2: N = 88.
- High transparency was chosen on 39% (Exp. 1) and 43% (Exp. 2) of adaptable trials; 41% averaged (pp. 13, 18, 23). In Exp. 1, 16.4% of participants never chose it.
- Adaptable transparency did not improve accuracy of automation use in either experiment (p. 22).
- Across six studies, fixed high transparency raised hit rate and sensitivity and also raised bias toward agreeing with advice. Correct rejections did not improve (p. 21).
- The authors call for eye tracking to examine strategy (p. 15).

### Disley & Khan (2026). Human–Computer Interaction, online first, 1–42. Read: §§1–2.3, 5–7.
- N = 37 design students and academics (47 recruited); within-subjects; three 15-minute ideation sessions: unaided, Llama3.2:3b, and "Unlearning to Rest" (the concept "chair" suppressed).
- Ownership: 6.38 (unmodified model), 9.16 (suppressed), 11.49 (unaided); F(2,72) = 12.43, ηp² = .251; all pairwise differences significant (Tables 1–3).
- Mental demand and effort were lowest with the unmodified model; the suppressed model did not differ from unaided (§6.1).
- §2.3 cites Cox et al. (2016) "microboundaries — small, deliberate frictions placed before an action." The authors contrast their own model-level friction with interface-level friction, "an added step, a delay." **Decision spaces are interface-level friction of this kind.**
- §7.9 calls for comparing interface-level interventions.
- Limitations: one ownership item; the task was creative ideation, not verification (§7.8).

### Forshaw, Hale & Longmire (2026). Human–Computer Interaction, online first, 1–26. Read: §§1–6.1.
- Fourth cycle of design-based research at a consulting firm. Eight managers each had one human coaching session (Zoom) and one text-based AI coaching session built on the same protocol.
- All eight preferred the human coach. Six of eight expected answers from the AI and were frustrated by its questions (Table 11).
- Despite the stated dislike, the coached behaviours were "observed, to at least some degree," after both formats (§6.1; Table 11 note). Said and did diverged.
- Confounds: order was not balanced (5 AI-first, 3 human-first), and the two formats differed in mode (video vs text) (§4.3–4.4).

### Yang, Lee, Tabone, García de Pedro, Happee & Merat (2026/2027). IJHCS 217, 103920. Read in full (CC-BY).
- N = 30 recruited; three excluded for missing gaze data. Secondary analysis of the Tabone et al. (2024) CAVE dataset; Tobii Pro Glasses 2 at 50 Hz.
- AR conditions reduced total fixation duration on the vehicle plus the AR interface relative to baseline: HUD M = −283 ms, Crossing Path M = −282 ms (d = −0.80 each), Car Path M = −76 ms (d = −0.32) (§3.3.1).
- More intuitive interfaces and repeated encounters reduced fixation duration further (§3.3.1).
- The authors' caution (§5): "Evaluating visual load in isolation without considering these safety-critical outcomes is a limitation of the current study."

---

## Debate papers judged not useful (verdicts now from full text)

| Paper | Read | Confirms abstract-based verdict? |
|---|---|---|
| Lamb et al. (2026), JCEDM | In full | Yes for the intro. Twelve analysts before deployment and nine after; machine-vision overlay on live video. Seven of nine stopped seeing it as an "advisor" (McNemar p = .023). Analysts wanted to learn the tool's "boundary conditions" (Lee & See, 2004). **Possible for Section 7:** live visual stream, AI overlay, trust learned from failures. |
| Haghighi & Wong (2026), JCEDM | Abstract and method | Yes. Six participants, no automated aid. |
| Xu et al. (2025), TOCHI | Abstract, method, findings §4.2, discussion | Yes. Observation and interviews; "attentional tunneling" noted from video, with no eye tracking. |
| Kot et al. (2026), TOCHI | Abstract and method | Yes. Qualitative workshops and interviews with people with dementia or MCI. |
| Cetinkaya & Krämer (2026), BIT | Method, results, discussion | Yes. N = 315 German Prolific participants; conjoint in a healthcare scenario; no layout or attention measure; pseudo-R² .01–.02. The text contradicts itself on which cluster had higher AI acceptance (§4.4.4 vs §5.1). |
| Horvers et al. (2026), BIT | Abstract, method, cross-case results, limitations | Yes. One teacher per case; no inter-rater reliability. One line worth noting: transformation was likelier when AI output came in planning or reflection "rather than during lesson execution," because those phases give teachers "more opportunities to critically interpret AI-generated output" (§3.2.3). |
| Tafesse & Mamo (2026), BIT | Abstract, method, discussion | Yes. A 3-minute MTurk recall survey (192 retained; the abstract says 191), two items per construct, no stimuli. |

## Read later the same day

### Cox, Gould, Cecchinato, Iacovides & Renfree (2016). CHI EA '16, 1389–1397. Read in full (White Rose accepted version).
- A position paper (late-breaking work) with no new data.
- Definition: "A microboundary is an intervention that provides a small obstacle prior to an interaction that prevents us rushing from one context to another." It is implemented "via a short time cost" and prompts a switch from System 1 to System 2.
- Evidence it cites:
  - Soboczenski et al. (2013): a less legible font raised transcription accuracy with no measurable speed cost.
  - Task lockouts stop mindless clicking through dialogs, but if lockouts are too long people switch to other tasks.
- Future work: habituation, and "the level of autonomy a user has over the introduction of the microboundary."

### Gould, Cox, Brumby & Wickersham (2016). CHI '16, 3311–3323. https://doi.org/10.1145/2858036.2858067. Abstract only (OpenAlex).
- Lab experiment: lockouts before confirming data entry encouraged checking, and longer lockouts made checking more likely.
- Crowdsourced experiment: longer lockouts induced switching to other activities.
- The authors conclude that duration "needs to be carefully calibrated." An open-access copy exists in the University of Birmingham repository; I did not fetch it.
