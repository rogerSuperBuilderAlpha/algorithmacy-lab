# Outline: Decision Experience Design and the animated interface

[DRAFTED by Claude, 2026-11-05.] This is a structure, not prose. Quoted lines are Roger's (from
`SOURCE.md`, Pass 2) and carry no marker. Everything else is Claude's scaffolding, for Roger to
replace. Citation flags (F1–F13) are in `CHECK.md`.

**Course.** PHD1750-3 Independent Research Project (Ericson), mapped to HF700-1 Foundations in Human
Factors, Bentley, Fall 2026. **Course headings, carried from the accepted proposal
(`../phd1750_ericson/proposal.md`):** Perception, Action, Cognition, Human factors and design.

**Read-depth key.** *full*: whole text read by the lab. *part*: sections read. *abs*: abstract only.
*rec*: record only, not read. *fetch*: not held.

---

## The thesis (Roger's words)

> "Decision Experience Design (DXD) is the practice of building interfaces that help a user figure out
> what decision to make when the finish line is still being worked out."

> "To build interfaces suited for Decision Experience Design, researchers and designers must learn and
> apply the core methodologies of the animator … working deliberately with the missing frames rather
> than pretending the gaps do not exist."

**The argument in four moves** [DRAFTED]:
1. Conversion-era design assumed that designer and user share a fixed goal. Agent-mediated
   decisions break that assumption: the goal moves (raincoat → umbrella).
2. Three conditions hold whatever the interface: the user is human; the environment is a platform
   that is opaque, co-optive and triadic; the needed design move is aesthetic.
3. An LLM interface is an animation (L. Stark, 2024). Animation has the same three properties:
   opaque (missing frames), co-optive (the viewer locks in) and triadic (viewer, character,
   animator). So animation explains why the platform behaves as it does.
4. The design consequence: DXD should use the animator's craft and surface decisions in the
   missing frames, rather than hide those frames or expose the backend.

**How it maps to the course** [DRAFTED]: the three animation properties fall onto three course
headings, and the design move falls onto the fourth.

| Animation property | Course heading | The HF question it answers |
|---|---|---|
| Opaque: missing frames | **Perception** | What does the user actually receive, and at what rate? |
| Co-optive: locking in | **Perception → Cognition** | How does the user's own processing fill the gaps, and what does that do to a decision? |
| Triadic: character, animator, viewer | **Action** | Where can the user act, and on whom: the character or the animator? |
| Working with the missing frames | **Human factors and design** | What should the designer build? |

---

## Section plan

### 1. Introduction: the raincoat and the umbrella

- **Claim:** Pass 2, ¶1–3, as written. They end on the DXD definition.
- **Keep:** the commuter case. It is the concrete anchor, so return to it in every section.
- **Flags:** F5 (Johnson "proves"), F6 (Weinmann not read).
- **Roadmap** [DRAFTED]: one sentence in the first person naming sections 2–6.

### 2. Why conversion-era design fails a moving goal — *Human factors and design*

- **Claim** (Roger): "The metrics that built modern web design—conversion rates, page stickiness, and
  dark patterns—fail when the destination is moving."
- **What to show** [DRAFTED]: classic HF and UX models give the goal first. Norman's seven stages
  of action begin with forming a goal, and the designer bridges the gulfs of execution and
  evaluation *after* it. Choice architecture shapes which option a user picks once the options are
  set. DXD starts a step earlier, at goal formation.
- **Sources:**
  - Norman (1988): `dxd_foundation/literature/library/norman1988psychology.md`. Read through
    secondaries; hold the book before quoting.
  - Hutchins, Hollan and Norman (1985), the gulfs: `…/library/hutchins1985direct.md` (*full*).
  - Jachimowicz et al. (2019), defaults *d* = 0.68 with endorsement as a channel:
    `decision_experience_design/literature/facets/F2_choice_architecture.md` B4 (*part*).
    Endorsement means the user reads a default as the architect's advice, which is the inference an
    opaque platform makes hard.
  - Gray et al. (2018), dark patterns: `…/library/gray2018dark.md`. Nouwens et al. (2020): removing
    the first-page opt-out raised consent by 22–23 points (`…/library/nouwens2020dark.md`, *full*).
  - Johnson et al. (2012) *rec*, and Weinmann et al. (2016) *rec*. Both need a library copy.
  - Simon (1997), bounded rationality, if you want the satisficing frame:
    `lima_pdw/literature/cards/simon1997.md`.

### 3. Three conditions that do not change

#### 3.1 The user is human — *Cognition*

- **Claim** (Roger): "the user is a human being: biological, cognitive, and emotional … we bracket
  that literature [agent experience] here to focus on the human decider."
- **What to show** [DRAFTED]: users work through external representations, and an interface's
  representation changes the task. When an agent conversation carries part of the decision, that is
  cognitive offloading.
- **Sources:**
  - Zhang and Norman (1994): `…/library/zhang1994representations.md` (*full*).
  - Scaife and Rogers (1996), computational offloading and re-representation:
    `…/library/scaife1996external.md` (*full*).
  - Risko and Gilbert (2016): `…/library/risko2016cognitive.md`.
  - **Carried from the proposal:** Eslami et al. (2016). Folk theories are working models built
    from outputs, and they show the human decider forming a picture of a mediator it cannot see
    (`coordinative_sovereignty/literature/library/cards/eslami2016first.md`).

#### 3.2 The environment is a platform — *Human factors and design*

- **Claim** (Roger): Pass 2, "Second…" paragraph, as written.
- **[FLAG, Claude, 2026-11-05 — the next bullet overstates; see `library/triage/F7-F8.md`.]** The lab's
  own cards contradict "two-node loop": `parasuraman2000types` records the phrase as an earlier draft's,
  not the source's, and O'Neill et al. (2022) count 22 of 76 human–autonomy-teaming studies with two or
  more humans. Cameron et al. (2024, Social Triad Model) already propose a user–robot–deployer triad.
  A softer claim for Roger to judge: HF's canonical models take one operator and one aid as the unit;
  where HF admits more parties they share a goal; a third party with interests of its own has entered
  HRI and trust research only recently.
- **What to show** [DRAFTED, superseded by the flag above]: HF's automation models are dyads. Parasuraman, Sheridan and Wickens
  (2000) model the operator and the aid as a two-node loop. Lee and See (2004) and Bainbridge (1983)
  study one human supervising one machine. A platform adds a third party with interests of its own.
  This is the gap the triad fills.
- **Sources:**
  - D. Stark and Vanden Broeck (2024), co-optation: `lima_pdw/literature/cards/starkvandenbroeck2024.md`
    (*full*). See flags F8 and F9.
  - Burrell (2016) *abs*: F7.
  - **Carried from the proposal:** Ananny and Crawford (2018), F10. The proposal's point carries too:
    raw backend access overloads working memory, and abstracting the surface hides the user's part.
  - Parasuraman et al. (2000): `…/library/parasuraman2000types.md`. Its card already notes the
    "two-node loop" reading. Lee and See (2004): `…/library/lee2004trust.md`. Bainbridge (1983):
    `…/library/bainbridge1983ironies.md`. Simkute et al. (2024) apply Bainbridge's ironies to
    generative AI: `…/library/simkute2024ironies.md`.

#### 3.3 The design move is aesthetic

- **Claim** (Roger): Pass 2, "Third…" paragraph.
- **Sources:** L. Stark (2024), *full*: F2, F3. Silvio (2019; 2010) is cited through Stark, so get
  the book for p. 52.
- **Hook to §4** [DRAFTED]: Stark establishes *that* the chatbot is an animated character. §4
  argues from what animation is *made of*.

### 4. What animation is made of

#### 4.1 Opaque: the missing frames — *Perception*

- **Claim** (Roger): "Animation is constitutively opaque. There are literal missing frames."
- **What to show** [DRAFTED]: in a streamed LLM reply the frames are real. Platforms set the token
  rate, pace it to reading speed, and decide what appears between updates. The designer controls
  the interstices, as McLaren said the animator does.
- **Sources:**
  - McLaren, via Sifianos (1995): **fetch**, F1.
  - Liu et al. (2024, *Andes*, preprint): a 4.8 tokens/s target and a client-side "token pacer"
    (`spaces/research/notes/andes2024.md`, *part*).
  - Xiao and Yang (2025): segments paced by cognitive load (`…/notes/xiaoyang2025.md`, *full*).
  - Zhu et al. (2026), *Just-in-Time Tokens*: `…/notes/hzhu2026.md`.
  - Gnewuch et al. (2022), typing delays in chatbots. The PDF is in
    `spaces/notebook_sources/A1_review_agents_streams/`, but there is **no card yet**.
  - **Carried from the proposal:** Dehaene and Cohen (2007). Designed signs already reshape the
    perceptual system (the visual word form area), so a change in the frames is a change in
    perception, not decoration. The PDF is in `spaces/notebook_sources/B_theory/`.

#### 4.2 Co-optive: locking in — *Perception → Cognition*

- **Claim** (Roger): "At a certain threshold in an animated sequence, the viewer 'locks in' and the
  perceptual gaps disappear, enlisting the viewer's own perception to supply continuity where none
  exists."
- **What to show** [DRAFTED]: (a) The perceptual mechanism is apparent motion, not persistence of
  vision (F12). (b) Continuity is cut into events at boundaries, and boundaries change decisions:
  they limit anchoring. (c) Stark adds a second layer: the user's prompts animate the character, so
  the user is co-opted as an animator as well as a viewer (L. Stark, 2024, p. 1667).
- **Sources:**
  - Wertheimer (1912): **fetch**. The lead is `…/library/wagemans2012century.md`. Anderson and
    Anderson (1993) *rec*.
  - Zacks, Speer and Reynolds (2009): `spaces/research/notes/zacks2009.md` (*part*).
  - Pitts et al. (2023), cueing boundaries: `…/notes/pitts2023.md`.
  - Ongchoco et al. (2023): `…/notes/ongchoco2023.md` (*abs*).
  - L. Stark (2024) on the ELIZA effect and the user as "the final uncompensated animator"
    (p. 1667), *full*.

#### 4.3 Triadic: character, animator, viewer — *Action*

- **Claim** (Roger): "Watching animation introduces a third term: 'I' am watching a 'character'
  manipulated by an unseen 'animator.'"
- **What to show** [DRAFTED]: in a triad, the user's action can land on the character (the reply)
  or on the animator (the platform's commitments). Current chat interfaces offer only the first.
  The proposal's Action section carries here: its read/write acts on the mediator become acts on
  the animator.
- **Sources:**
  - Silvio, through L. Stark (2024, p. 1664): projection versus introjection, the "numerical
    disjunct", and the "hard to separate" concession (F4).
  - Where users intervene in agent runs: Huq et al. (2026, preprint, *abs/§1*),
    `…/notes/huq2026.md`; Zhou et al. (2026), confirmation points, `…/notes/zhou2026check.md`;
    Chen et al. (2026), oversight of computer-use agents, `…/notes/chen2026cua.md`.
  - **Carried from the proposal:** the Action paragraph (sanctioned and subversive writes), with
    Belousov's corpus dropped.

### 5. The animator's methods for DXD — *Human factors and design*

- **Claim** (Roger): the closing sentence of Pass 2.
- **What to show** [DRAFTED]: name two or three animator methods and translate each into a DXD
  move. For example: *timing* becomes pacing the stream to the decision; *staging* becomes putting
  the decision point where the eye goes; *the key pose* becomes the frame where the user commits.
  Set these against the two failed options: hiding the frames (a seamless product) and exposing the
  backend (transparency, per Ananny & Crawford).
- **Sources:**
  - Thomas and Johnston (1981), *The Illusion of Life*: **fetch**, F11.
  - Chevalier et al. (2016), interface animation roles *rec*: F11.
  - Design friction: Cox et al. (2016), `…/library/cox2016design.md`. Buçinca et al. (2021),
    cognitive forcing, `spaces/research/notes/bucinca2021.md`.
  - **Carried from the proposal:** the engagement layer, recast as the layer where decisions are
    surfaced.

### 6. Limits and next steps

- **Limits** [DRAFTED]: the paper brackets agent experience by design. It tests nothing. And
  "animation" is an analysis of the interface, not a claim about the model.
- **Next step:** the Spaces eye-tracking study (`spaces/paperC_experiment/`) is the empirical test
  of decision marks in a stream. Cite it as planned work only.

### 7. Conclusion

Return to the commuter, and end on the umbrella.

---

## What carries from the accepted proposal

| Proposal element | Status here |
|---|---|
| Four course headings | **Carry**, as section tags (table above) |
| Eslami et al. (2016) | **Carry**: §3.1 |
| Ananny and Crawford (2018), and the load claim | **Carry**: §3.2, §5 |
| Dehaene and Cohen (2007) | **Carry**: §4.1 |
| Action: reads and writes on the mediator | **Carry, reframed**: §4.3 |
| Engagement layer | **Carry, reframed**: §5 |
| Belousov et al. (2027), the DIAL corpus and re-coding method | **Drop**. The new thesis does not need it. Decision D2 |
| Albantakis et al. (2023), IIT as the altered-state criterion | **Out of scope**, because the thesis no longer argues about altered states. Decision D2 |

## Decisions for Roger

- **D1.** Is Pass 2 the governing text? (The outline assumes it is.)
- **D2.** Belousov and IIT. Drop both, or keep one paragraph that places the new thesis after the
  approved one? The instructor approved a DIAL paper, so a single "this paper develops the
  proposal's design claim" paragraph may help.
- **D3.** Overlap with *Spaces in the Stream* (`phd1750_spaces_in_stream/`). That paper also treats
  streamed output as a perceptual problem for decisions. Should this course paper stay the short HF
  statement of the animation thesis, with Spaces as the long HCI paper, or merge into it?
- **D4.** Instructor sign-off on the change of topic.
- **D5.** Length, due date and rubric. None is in the repo.

## To fetch before drafting

1. Sifianos (1995), *Animation Journal* 3(2): McLaren's letter (F1)
2. Thomas and Johnston (1981), *The Illusion of Life* (F11)
3. Silvio (2019), p. 52, and Silvio (2010), pp. 422–432 (F3, F4)
4. Johnson et al. (2012); Weinmann et al. (2016) (F5, F6)
5. Burrell (2016), to confirm the wording in a browser (F7)
6. Wertheimer (1912), or a review of apparent motion (F12)
7. Card Gnewuch et al. (2022) from the PDF already held
