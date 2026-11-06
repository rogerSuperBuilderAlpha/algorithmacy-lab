---
key: wu2026ainimation
apa: "Wu, J., & Masson, D. (2026). *AInimation: Animating from prompt to AI-generated responses* (arXiv:2607.18507v1). arXiv. https://doi.org/10.48550/arxiv.2607.18507"
authors: "Wu, Jiaqi; Masson, Damien"
year: 2026
title: "AInimation: Animating from Prompt to AI-Generated Responses"
venue: "arXiv"
volume: ""
issue: ""
pages: ""
doi: "10.48550/arxiv.2607.18507"
url: "https://arxiv.org/abs/2607.18507"
type: preprint
facets: [F9, G]
claims: [c5, c8, c9]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "arXiv v1 PDF (12 pp.; p. 1 carries the stamp 'arXiv:2607.18507v1 [cs.HC] 20 Jul 2026') and its text layers wu2026ainimation.txt and wu2026ainimation.readorder.txt, at ~/iit-playground/dxd_animation_local/pdfs/wu2026ainimation/; fetched from https://arxiv.org/pdf/2607.18507 (provenance.txt); read in full 2026-11-06; sha256 99afbd26650775f5ef47ff7e15ebf28c15f1aa5a725e993d264a1c63e6e85f47 (PDF, recomputed with shasum -a 256; matches provenance.txt and sha256.txt)"
verified: corrected
verified_against: "arXiv v1 PDF (sha256 99afbd26650775f5ef47ff7e15ebf28c15f1aa5a725e993d264a1c63e6e85f47, recomputed) via its reading-order text layer (identical to a fresh pdftotext of the PDF); datacite.json, openalex.json, arxiv_abs.xml"
prior_cards: []
status: candidate
added: 2026-11-06
run: dxda-lib-2026-11
---

# Wu & Masson (2026), AInimation

## What it argues

Jiaqi Wu and Damien Masson (Université de Montréal, cs.HC) argue that animating the move from a prompt to
an AI response helps users review that response. They treat animation as a user-interface technique, in the
line of animated transitions in data graphics, document histories and spatial views (they build on
Heer & Robertson, Chevalier et al., Gliimpse and Diffamation). The paper opens by calling the familiar
token-by-token display of an LLM reply an animation, but "a happy accident" of how the model works. They
call such displays "technology-driven animations" and "essentially glorified progress bars" (§2.1). They
then ask whether the reply should arrive as fast as possible, or through slower, crafted animations.

Their method has four parts. (1) They set four design goals, drawn from earlier classifications of the roles
of animation in interfaces: G1 locate elements, G2 estimate changes, G3 verify the interpretation of the
prompt, G4 keep the user engaged (§3). (2) One author reviewed 800 prompt-response pairs from four public
datasets, the authors discussed them, and they built a taxonomy of seven relationships between prompt and
response elements: reuse, alteration, reconceptualization, structural, internal reference, external
reference and extraneous. Each relationship gets an animation, such as translate, morph, highlight, overlay
or fade (§3.1–3.3, Fig. 2). A further 100 pairs per dataset checked the taxonomy. (3) They give timing
rules: minimum durations of about 1.5 to 2 seconds per animation, about 6 seconds in the worst case, and
"slow-in" and "slow-out" easing, which they cite to Dragicevic et al. [17], not to animation craft (§3.4).
(4) They build a React player and a naive GPT 5.4 pipeline that proposes which elements to animate. In ten
runs over ten text-to-text prompt sets (100 specifications), the pipeline did well on most animation types
and worse on alteration and external reference (§4). The table's text layer is jumbled, so I did not map
its six values to rows.

The user study has n = 16 (ages 18 to 26, M = 21.9; 8 female, 8 male), all completing three within-subject
experiments, which the paper says they "completed … in succession" (§5, PDF p. 6) without writing the order out. The baseline was an instant reply shown for the same total time as the animated
one. The authors piloted a word-by-word baseline and dropped it as too weak (§5). Experiment 1: animation
cut click error on tracked elements by 47.5 pixels, which they report as a 43% improvement. Experiment 2:
animation cut estimation error by 3.17, reported as 152% in §5.3.1 and 153% in the abstract, the Introduction and the summary of results (§6.1).
Experiment 3: participants were .62 more confident (on a five-point scale) that the AI had followed the
prompt, reported as 20%; the evidence for external reference was inconclusive. Every response in Experiment 3
had followed the instruction, and participants were told the AI was "imperfect" to prevent over-trust, so
the 20% measures confidence, not correct detection of a failure. All participants preferred the animated
version and found it engaging. One, P2, said it felt like seeing "a bit of behind the scenes". The authors
list their own limits: a young sample, short lab tasks, a pipeline too slow to ship, and no longitudinal
test (§6.3). Their closing claim is that "well-crafted but slower animations might be preferable" to
instant replies.

The paper never uses "animator" or "character" in the animation-theory sense, cites no animation theory, and
never uses the word "decision". Forms of "decide" occur six times, always for designers, the pipeline or
prompt elements, never for the user.

## What the paper uses it for

- **c4** (an LLM interface is an animation): not supported. Wu and Masson do not frame the LLM interface as
  an animation in Stark's or Silvio's sense. They use animation as a presentation technique for responses:
  a sequence of frames that conveys the relation between two display states (§2.2). Their only use of
  "animation" for the unmodified chat display is the token stream, which they call an accident of the
  technology and a progress bar. The words "Stark", "Silvio", "puppet" and "animator" do not occur anywhere in
  the paper or its 62 references. "Characters" occurs only for typed letters (the highlighted added and
  removed characters in text edits).
- **c5** (animation is opaque: missing frames; the interstices are the craft): adjacent, not supporting.
  They do treat the streamed reply as real frames whose pacing is a design choice, which is the premise of
  OUTLINE §4.1. They say the token stream's character came from the model's architecture and from raw speed
  gains, and they ask whether a designer should craft it instead (§1, §2.1). They also cite Xiao & Yang
  (2025) for generation already exceeding reading speed (§2.1, ref. [57]), a source OUTLINE §4.1 already
  holds. But they never say the frames are missing or that the viewer supplies continuity. Their animations
  add frames to make a mapping visible. They do not read the existing interstices as the craft.
- **c6** (animation is co-optive: the viewer locks in; the user also animates): not supported. They have no
  account of apparent motion, thresholds or the viewer's perception filling gaps. Their measure is task
  performance and stated engagement (G4). The user is a reviewer of the reply, not an animator. A single
  line, that the pipeline-made animation gave participants "the impression of seeing how the AI operates
  internally" (§5.5.2), is a user report, not a mechanism.
- **c7** (animation is triadic: viewer, character, animator): not addressed. The nearest roles are the user,
  the AI and the "designers" they advise. No animator stands behind a character, and the user's action never
  lands on the platform's commitments. Their one proposal for acting back is that users could return from
  the response to refine the prompt (§6.4.3), which is an act on the prompt, not on the animator.
- **c8** (DXD must apply the animator's methods, not hide frames or expose the backend): partly relevant
  and the strongest link. They apply a design craft to AI responses: goals, a taxonomy, durations, easing,
  coordination of simultaneous motion. They cite Chevalier et al. (2016) and Baecker & Small (1990) for the
  roles of animation, not Thomas & Johnston, Lasseter or any animator's handbook, and they name no
  animator's method (timing, staging, key pose). Their result that slower, crafted animation beat an instant
  reply of equal duration, with n = 16 and tasks about the prompt-response mapping, is the only empirical
  datum the paper has for "pacing". It is about review, not about pacing a stream to a decision.
  Participant reports of "behind the scenes" bear on c8's "expose the backend" failure. The pipeline pairs
  elements by semantic matching with a GPT model. It does not read the model's internals (§2.3, §3.2, §4),
  so what users see is a reconstruction of the relation, not the mechanism.
- **c9** (gap: no prior work frames LLM interfaces as animation for decision design): this is the nearest
  prior to c9's second half, and it narrows the claim, but only in one respect. Wu and Masson do offer a
  design method that applies animation to AI responses, built on a taxonomy and tested. So c9 cannot say
  that no prior work applies animation to AI responses as a design method. It can still say that no work
  takes the animation reading (Stark, Silvio) as the design frame, and none aims at the user's decision. The
  paper's targets are locating, estimating and verifying, all measured at the level of the reply, with
  accuracy and confidence. The word "decision" does not occur. The closest user-facing concept is "verify
  the interpretation of the prompt" (G3), and the nearest decision-like step is reviewing a reply, which
  they never link to a choice the user makes next. The "I found no work…" sentence in GAP_CHECK.md should
  keep its second clause ("takes the animation reading as a design method for the user's decision") and
  drop any wording that implies Wu and Masson are absent.

## Loci

Locators: the held PDF prints no page numbers, so "PDF p." counts form-feed pages in the reading-order text
layer, and section numbers are those printed in the text layer (some run-in headings print no number; I give
the heading). Every quotation below was matched against `wu2026ainimation.readorder.txt`, the reading-order
text layer of the held PDF (sha256 above), after collapsing whitespace. Where the paper has double quotation
marks inside a quotation, I give them as single quotes.

- "Our work applies to all software that integrates AI and shows that well-crafted, slower animations are preferable to instant AI responses." — PDF p. 1, Abstract; matched against wu2026ainimation.readorder.txt
- "Far from being a design choice, this animation is a happy accident resulting from the underlying technology" — PDF p. 1, §1 Introduction; matched against wu2026ainimation.readorder.txt
- "those technology-driven animations are essentially glorified progress bars" — PDF p. 2, §2.1; matched against wu2026ainimation.readorder.txt
- "Should AI answers be shown as fast as possible using technology-driven animations, or would slower but well-crafted animations be preferable?" — PDF p. 2, §2.1; matched against wu2026ainimation.readorder.txt
- "Animated transitions are a sequence of visual frames (usually temporally interpolated [9]) to smoothly convey the relationship between one display state and another [11, 23]." — PDF p. 2, §2.2; matched against wu2026ainimation.readorder.txt
- "Based on previous classifications of the roles of animations in user interfaces [12, 45], we identified four key design goals" — PDF p. 2, §3; matched against wu2026ainimation.readorder.txt
- "For a mapping between a prompt and a response element to exist, there must be a causal relationship" — PDF p. 3, §3.2; matched against wu2026ainimation.readorder.txt
- "Sixteen participants (18 to 26 years old, M = 21.9; 8 self-identified as female and 8 as male)" — PDF p. 6, §5; matched against wu2026ainimation.readorder.txt
- "Animated transitions reduced the average error of tracked elements by 47.5 pixels" — PDF p. 7, §5.2.1; matched against wu2026ainimation.readorder.txt
- "we told participants that responses were generated by 'an imperfect AI' that might not follow instructions." (inner quotes given as single) — PDF p. 8, §5.4 (Experiment 3); matched against wu2026ainimation.readorder.txt
- "participants were .62 more confident that the AI was correct with animated transitions" — PDF p. 8, §5.4.1; matched against wu2026ainimation.readorder.txt
- "animations helped despite slowing down generation and delaying when users could see the final answer." — PDF p. 9, Discussion; matched against wu2026ainimation.readorder.txt
- "We argue that these improved speeds should be used to develop animated transitions, not to show the response as fast as possible." — PDF p. 9, Discussion; matched against wu2026ainimation.readorder.txt
- "It also gave them the impression of seeing how the AI operates internally." — PDF p. 9, §5.5.2; matched against wu2026ainimation.readorder.txt
- "these tasks might not cover the full range of what interests users" — PDF p. 10, §6.3.2; matched against wu2026ainimation.readorder.txt

## Caution

- **Not Stark's sense of animation.** The word is used for UI motion (transitions), and the cited lineage is
  HCI and information visualisation. This is the paper's whole relation to c4, and a reviewer who confuses
  the two senses would think c9 is taken. Section 6 should say outright that "animation" here means two
  different things.
- **Citations checked in the reference list (62 entries), by name.** Stark, Silvio, Maeda, Thomas & Johnston
  and Lasseter: none appears (searched `wu2026ainimation.txt` and the reading-order layer; zero hits for
  each, and none for "Illusion of Life", "Disney", "puppet", "animator", "principles"). Chevalier: yes. Ref.
  [12] Chevalier, Henry Riche, Plaisant, Chalbi and Hurter (2016), "Animations 25 Years Later: New Roles and
  Opportunities" (AVI '16), is cited in §3 as one of two sources for "previous classifications of the roles of
  animations in user interfaces" (with Baecker & Small 1990, [45]). It is the same work OUTLINE §5 lists as
  "Chevalier et al. (2016), interface animation roles *rec*". Refs. [9]–[11] are other Chevalier works. The
  text layer lists [9] and [10], and [18] and [19], as duplicate entries of one work each; the duplication is
  in the paper's list, not mine. Wu and Masson treat the 2016 paper as UI-animation roles. They do not use it
  for craft.
- **Another quirk of the numbering.** The printed subsection numbers are irregular (the Discussion has 6.3.x
  and 6.4.x subsections that appear in the text layer in a different order, "Applications" and "Future Work"
  headings sit among them, and the Limitations heading comes after its numbered items). I cite the numbers as
  printed and name the heading where a number is unclear.
- **Numbers.** 152% (§5.3.1) against 153% (abstract, Introduction, §6.1 summary of results). The 43% is click error in pixels,
  not a ratio of tasks done. The 20% is a rating difference on a five-point scale (.62), so it is a confidence
  measure on responses that were all correct. The Experiment 2 confidence results (§5.3.1, PDF p. 8) name text-to-image twice in one
  sentence list and omit text-to-text (the second is probably text-to-text); I did not quote it. Section 4 writes "10,0000
  resamples" (sic) for the pipeline's bootstrap. Experiment 1 gives the animation 4 to 6 seconds against an
  instant reply shown for the same total time.
- **Status and version.** arXiv v1, submitted 2026-07-20 (datacite and arXiv records); not peer reviewed as
  far as the folder shows.
  Cite as a preprint. The DOI is the arXiv DOI.
- **Funding and authorship.** The acknowledgments name NSERC RGPIN-2026-06392, IVADO and the Canada First
  Research Excellence Fund. The first author's name appears as "Jiaqi Wu" in the paper and as "Jia-Qi Wu"
  in GAP_CHECK.md; the paper's own spelling is used here. GAP_CHECK.md also says Wu and Masson "do not cite
  animation theory": confirmed, and their abstract also lacks the word "decision": confirmed in the full
  text. GAP_CHECK's reading is therefore right, and now rests on the whole paper, not the abstract alone.
- **Related, not duplicate.** Damien Masson and Fanny Chevalier appear together as authors of ref. [37],
  Textoshop (CHI '25). Masson's own work (DirectGPT, [39]) is also in the list. This is background for a
  reviewer who knows the group, not a claim in the card.
- **What the paper may not claim from it:** that prior work frames the LLM interface as animation; that
  animation in an LLM interface has been tested on decisions; any account of locking in, missing frames or an
  animator; or any support for "pacing the stream to the decision". It may claim that interface animation
  of AI responses is an existing, tested design technique, and that a crafted, slower display beat an
  instant one at review tasks in one lab study (n = 16).

## Verification

2026-11-06 · S6 verifier (opus; not the writer) · verdict: corrected · checked: sha256 recomputed (matches provenance.txt and sha256.txt); the reading-order layer matches a fresh pdftotext of the PDF after whitespace collapse; authors (Jiaqi Wu, Damien Masson), title, year 2026, DOI 10.48550/arxiv.2607.18507, v1 (submitted 2026-07-20), cs.HC and preprint type agree across datacite.json, arxiv_abs.xml, openalex.json (which abbreviates "D Masson") and the PDF title block; loci 15/15 verbatim, each on the PDF page given; 800 pairs (200 per modality from four datasets), seven relationship types, 100 validation pairs per dataset, 1.5 s/2 s minimums and the ~6 s worst case, slow-in/slow-out cited to [17], React player, GPT 5.4 pipeline, 5 tasks × 2 sets × 10 runs = 100 specifications, "10,0000"; n = 16, ages 18–26, M = 21.9, 8/8; 47.5 px = 43% (§5.2.1); 3.17 = 152% (§5.3.1) against 153% in the abstract, Introduction and §6.1; .62 = 20% (§5.4.1), external reference inconclusive (p = .265); all Experiment 3 responses followed the instruction, with the "imperfect AI" framing (§5.4); the equal-duration instant baseline and the dropped word-by-word pilot (§5); all participants preferred animation (§5.5.2) and found it engaging (§6.1); limits in §6.3.1–6.3.3; references: 62 entries, [12] Chevalier, Henry Riche, Plaisant, Chalbi & Hurter 2016 cited with [45] Baecker & Small in §3, [9]/[10] and [18]/[19] duplicates, [57] Xiao & Yang 2025 in §2.1, [37] Textoshop, [39] DirectGPT; zero hits in both text layers for Stark, Silvio, Maeda, Johnston, Lasseter, Disney, puppet, animator and decision/Decision; "character(s)" only for typed letters; OUTLINE §4.1 holds Xiao & Yang and §5 lists Chevalier et al. (2016); the c4–c9 bullets follow from the source and match GAP_CHECK.md · changed: (1) 153% also appears in the Introduction, added in both places it is listed; (2) the duplicated "text-to-image" list is in Experiment 2's confidence results (§5.3.1, PDF p. 7), not Experiment 3 (text-to-text only), and the missing modality is text-to-text, not image-to-text; (3) "experiments in sequence" removed, since the paper does not state their order; (4) "contains no 'decision' in any sense" narrowed to the word itself, with the six "decide" forms noted (designers, pipeline, prompt elements; none for the user).

## Hand-check

- 2026-11-06, Fable (S7). Verdict: **index after fix** (fixed here).
- Checked: 15/15 loci found in the text layer (`wu2026ainimation.readorder.txt`, whitespace collapsed, each on the PDF page the card gives by form-feed count); frontmatter vs record (datacite.json, openalex.json, arxiv_abs.xml and pdfinfo agree on authors, title, year, arXiv 2607.18507 v1, DOI, preprint, 12 pp.; sha256 recomputed, matches provenance.txt and sha256.txt); claim uses c4–c9 read against the full text; zero hits in both text layers for Stark, Silvio, Maeda, Johnston, Lasseter, Disney, puppet, animator, "Illusion of Life", principles, decision/Decision; the six "decid-" forms sit at §3.3 (structural elements), §3.4.3 (designers), §4 (pipeline, three times) and §6.4.2 (designers); "character(s)" occurs at Fig. 1, §2.1 (diffusion LMs) and §3.3 alteration, all typed letters. Table 1 in the reading-order layer lists its six rows and six values in one order (reuse 1.00 … external reference 0.59), so the mapping the writer declined is recoverable; I left the sentence as written.
- Changed: (1) §5 paragraph: "(the paper does not state their order)" replaced by the paper's own words, "completed … in succession" (§5, PDF p. 6; the same page also calls them "three successive experiment[s]"), since the card denied something the paper does say; (2) Caution, "Numbers": the Experiment 2 confidence sentence is on PDF p. 8, not p. 7 (both halves, "Participants rated themselves 1.08 points more confident…" and "by 1.44 for image-to-text…", fall on p. 8 by form-feed count).
- For the author: (a) whether "in succession" fixes the order as Experiments 1→2→3 is a reading; the paper numbers them and calls them successive but never writes the order out. (b) The c4, c6 and c7 bullets record non-support for tags absent from the frontmatter `claims` list; README asks one bullet per claim tag, so keep or cut is a style call. (c) GAP_CHECK.md c9: the verdict and the suggested §6 sentence stand on the full text; four small wording updates are listed in `hand_check/part5.md`.
