# Sketch: AI development as animation (*Philosophy & Technology*)

[DRAFTED by Claude, 2026-11-08. Roger's own words appear in quotation marks and come from `SOURCE.md`.
Citations marked **(unverified)** come from memory or from Consensus abstracts and must be checked
against the version of record before they enter a draft. Citations marked **(lab-checked)** were
verified in `../dxd_animation/CHECK.md`.]

## Thesis

Roger's claim: "creating artificial intelligence is better conceived as creating artificial life," and
"treating the development of AI as a computer science problem is a mistake."

As edited (decision 2026-11-08), the target is **model-centrism**, the view that the model *is* the AI.
"We have the core feature of the LLM but developing AI as we know it now requires so much more around
that LLM": harnesses, virtual machines, efficiencies. That surrounding work is the craft of bringing a
character to life, and animation is the discipline that has practiced it longest.

The edit keeps the claim and removes the easy rebuttal (harnesses and VMs are themselves computer
science). Engineering sources already concede the premise:
- Sculley et al. (2015), "Hidden Technical Debt in Machine Learning Systems," *NeurIPS*: ML code is a
  small fraction of a real ML system. **(unverified)**
- Zaharia et al. (2024), "The Shift from Models to Compound AI Systems," BAIR blog. **(unverified)**

## Working titles (Claude's)

- *Animating Intelligence: Against Model-Centrism in AI Development*
- *The Illusion of Life, Again*, after Thomas & Johnston (1981), *The Illusion of Life: Disney Animation*

## Positioning: what already exists

| Work | What it argues | How this paper differs |
|---|---|---|
| Luke Stark (2024), "Animation and Artificial Intelligence," *FAccT '24*, pp. 1663–1671, doi 10.1145/3630106.3658995 **(lab-checked)** | ChatGPT-style chatbots are best understood as animated characters; animation's traits are "reliance on stereotypes, obfuscation of human labor, and manipulation of an audience's emotions" (p. 1663) | Stark reads the **character the user meets**, critically. This paper reads the **making**: development as an animation production pipeline, framed as life against intelligence, and triadic. |
| Shanahan, McDonell & Reynolds (2023), "Role play with large language models," *Nature* **(unverified)** | Dialogue agents are best described as role-playing characters | Same: user-facing character, not the production of it |
| Bernini (2025), "AI as Character," *Style* 59(3) **(unverified)** | Fictionality and Dennett's intentional stance explain human–AI interaction | Same |
| Berthon, "AI to AL" (lab, PRs #879/#880) | When model lineages become artificial life (reproduction, open-ended evolution) | Berthon asks **whether AI is alive**; this paper asks **what kind of making AI development is**. Keep §2 from becoming a second "is it alive?" argument. |
| Lab: `../dxd_animation/` (HF course paper, PR #878) and `../dxd_animator/` (CFP) | LLM interfaces are animations, so DXD needs the animator's methods; the same three traits (opaque, co-optive, triadic) | Those arms apply the animation lens to **decision-experience design**. This paper applies it to **AI development** and adds the life/intelligence philosophy. The same three traits appear in all three; disclose the overlap. |

## Section plan

### 1. The puzzle

The LLM is "the core feature," yet a working AI needs harnesses, virtual machines and efficiencies
around it. If the model were the AI, that surrounding work would be packaging. It is not packaging:
it decides what the user meets. What kind of making is this?

### 2. Two ways of thinking about the job: intelligence or life

- **Intelligence:** specify, benchmark, defer to the result, hold it to "a rigid standard."
- **Life:** animate, tend, expect failure; treat it as "fallible and requiring nurturing."

The philosophy section lives here. Pass 1 asked to "just lay out the dominant theories"; a
*Philosophy & Technology* reviewer will want a defended position instead, because neither term has
a consensus definition **(all unverified)**:
- Trifonov (2011) collected 123 definitions of life; Machery (2012, *Synthese*) argues the definitional
  project is hopeless; Cleland argues for a theory of life, not a definition.
- Legg & Hutter (2007) collected about 70 definitions of intelligence.

Candidate positions for the deep research to weigh: organizational/autopoietic accounts (Maturana &
Varela; Moreno & Mossio), which fit "so much more around that LLM" (life as maintained organization,
not as a core component); Dennett's intentional stance as the model for a "vital stance." The paper
should state which one it takes. Consciousness (IIT) stays out unless Φ earns a role.

### 3. Animation as a production craft

The pipeline: story, layout, key poses, in-betweening, rigging, cleanup, compositing, rendering;
stop-motion as the contrast case (a person authors every frame). Anchor in Thomas & Johnston (1981)
and Lasseter (1987, "Principles of traditional animation applied to 3D computer animation").

Draft mapping, to be tested against production sources:

| Animation | AI development |
|---|---|
| Character model and rig | Model weights |
| Key poses | System prompts, specifications |
| In-betweening | Decoding and sampling (the model produces its own in-betweens) |
| Animation layers, cleanup | Harness, tools, memory, guardrails |
| Render farm | Inference infrastructure, VMs, efficiencies |
| Animator | Developer, studio, platform |

### 4. Four parallels

**4.1 Composition** (the thesis carrier; implicit in Pass 2). The character is the rig plus every
layer of work on it; the AI is the LLM plus "harnesses, virtual machines, efficiencies."

**4.2 Necessary opacity.** "There will always be missing frames"; in AI, "the in principle black box:
we could have all the information possible about the algorithm but still have opacity."
- Suggested sharpening: what animation lacks is not frames but **motion**. No frame contains the
  motion; the viewer's perception supplies it (apparent motion, Wertheimer 1912). The older
  "persistence of vision" account is a myth among film scholars (Anderson & Anderson 1993)
  **(lab-checked, F12)**. Read this way, intelligence too sits in no single component.
- AI side: Burrell (2016) names three sources of opacity: "intentional corporate or state secrecy",
  "technical illiteracy", and opacity from the characteristics of ML at scale **(lab-checked, F7)**.
  Roger's "in principle" claim matches the third; Humphreys (2009) on essential epistemic opacity
  **(unverified)**.

**4.3 Co-optation.** AI: "like platforms the more you use the more dependencies you require."
Animation: "you ultimately become coopted into the suspended reality of the narrative and screen."
- Strain: Coleridge's phrase is the *willing* suspension of disbelief (1817) **(unverified)**.
  Animation co-opts with consent; AI dependency may not. The gap may be the finding.
- Platform side: co-optation of "actors, assets, and activities" not located within the firm
  **(lab-checked, F9)**.

**4.4 Triadicity.** "There is always an animator between us watching and the final product."
- Strain: the lab's own criterion requires the third party to commit binding determinations, hold
  its own interest and keep the parties apart. An animator may only moderate a dyad (audience ↔ film).
  The argument has to show the studio, not the character, determines what the viewer gets.
- Help: Stark (2024) says a chatbot's animators are **many** (staff, raters, moderators, authors) and
  calls the user the "final uncompensated animator" (p. 1667) **(lab-checked, F4)**. That cuts both
  ways: it multiplies the third party, and it puts the user partly on the animator's side.

### 5. Where the analogy breaks

Animation is rendered in advance; AI is live and answers back. Puppetry and live performance capture
may be the closer case: a performer animates in real time, to an audience. Stop-motion sharpens the
other edge: there a person authors every frame; an LLM produces its own in-betweens.

### 6. Stakes for implementing and evaluating business processes

- Intelligence frame: implementation is procurement; evaluation is benchmarking; failure is a defect.
- Life frame: implementation is casting, rigging, rehearsal; evaluation is believability and
  consistency over time; failure is expected and tended.
- Phygital (Pass 1): "a digital intelligence with a physical form as application layer and dynamic,
  adaptive (living!) text." Optional here; the lab's phygital arms already carry it.

### 7. Conclusion

## Venue: *Philosophy & Technology* (Springer)

Chosen 2026-11-08. Scope, article types, word limit and reference style still to be checked on the
journal's site before outlining in detail. A conceptual-analysis venue means §2 (the defended
position on life and intelligence) and §5 (limits of the analogy) carry the most weight; §6 stays
short.

## Open decisions for Roger

1. Which account of life the paper defends in §2 (to be decided after the deep research).
2. Whether "vital stance" (Dennett-style) is the frame, or the paper makes a stronger,
   organizational claim about what AI is.
3. Whether the triad claim (§4.4) stays central, given the moderated-dyad objection.
4. Whether puppetry enters as a fifth parallel or only as the limit case in §5.

## For the deep research run

Start from what the lab holds, then search:
- `~/iit-playground/dxd_animation_local/` (79 PDFs; Consensus files F2 apparent motion,
  G_F9 animation principles in agents, G_llm_as_animation) and `../dxd_animation/library/` (77 cards).
- Gaps: philosophy of life (definitions, organizational accounts, Machery, Cleland); definitions of
  intelligence; animation production studies (pipeline, stop-motion, puppetry); compound-AI /
  ML-systems engineering; *Philosophy & Technology* papers on AI opacity, anthropomorphism and
  artificial life, to position against the venue's own conversation.
