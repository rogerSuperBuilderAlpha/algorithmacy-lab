# MODEL — the concept dossier for the DXD model paper

> **[DRAFTED by Claude (Opus 5.5), 2026-11-11. Version 1.]** This file defines every construct the
> paper uses, gives the history of its wording in Roger's texts with locators, states the model and
> its propositions, maps the evidence by read depth, and lists the decisions that are his. Quotations
> of Roger's texts are verbatim and carry their file and line. Everything else here is mine. Sources
> are cited by library key (`library/cards/<key>.md`) with the page the card gives. Items marked
> **[DECISION]** wait on his ruling; **[FLAG]** marks a problem I found and did not fix; **[PENDING]**
> marks evidence a run-2 card has not yet delivered.
>
> Path prefixes: `L/` = `submissions/` in this repository; `D/` = the private dissertation repo
> (`dissertation/`), cited by path only.

---

## 0. The brief and what this file settles

Roger's direction of 11 Nov 2026 (`SOURCE.md`, Pass 3), verbatim:

> "this paper is supposed to build a model for decision experience design using insights from
> profressiona animation technique and built upon the insights from algorithmacy. We need to design
> like animators and consider the new skillsets and competencies for naviagting opaque, cooptive,
> triadic environments. intent specification, idempotent interpretation, and intuitive governance
> tracking."

His rulings the same day (`library/triage/DECISIONS.md`, "Run 2"): "idempotent interpretation" means
many causes, one stable reading (R1); the craft texts come through his browser (R2); the first full
version is a journal article (R3, *Theoretical Issues in Ergonomics Science*); this pass delivers this
dossier, an outline and a full draft (R4).

**The contribution, in one sentence (mine, for his ruling):** algorithmacy's three competencies name
the work an opaque, co-optive, triadic environment leaves to the person, and they tell a designer
which of the animator's techniques to carry into a decision interface so that the interface, not the
person, does that work.

---

## 1. The constructs

### 1.1 Decision Experience Design (DXD)

**Roger's wordings, in order.**

| Date | Wording | Locator |
|---|---|---|
| 30 Sep 2026 (thesis) | "Decision Experience Design (DXD) is where the practice is going and should go, and its practitioners should become experts in algorithmacy the way UX designers became experts in reading and perception." | `L/decision_experience_design/README.md:17–22` |
| 30 Sep 2026 (published Part 1) | "DXD, by contrast, must address situations where choices are brokered through an adaptive, opaque algorithmic intermediary that reads multiple parties simultaneously and commits binding determinations that neither party fully controls." | `L/decision_experience_design/published/2026-09-30_decision-experience-design.md:34` |
| 5 Nov 2026 (Pass 2) | "Decision Experience Design (DXD) is the practice of building interfaces that help a user figure out what decision to make when the finish line is still being worked out." | `SOURCE.md`, Pass 2, ¶3 |

The two definitions do different work. Part 1 fixes the **setting** (a binding, adaptive, opaque
intermediary between parties). Pass 2 fixes the **task** (a decision whose goal is still forming).
Run 1's critic found that Pass 2's raincoat case, as written, reads as "a dyad plus an owner"
(`library/CRITIC.md`, cut 6), so Pass 2 alone loses the setting the other nine lab definitions keep.

**Working definition for the model [DRAFTED; DECISION D-h]:** *Decision Experience Design is the
practice of designing how a person forms and commits to a decision through an intermediary that is
opaque, co-optive and triadic, so that the interface carries the coordinative work the intermediary
would otherwise leave to the person.* It keeps Pass 2's task ("figure out what decision to make") and
Part 1's setting, and it takes its aim — moving work from the person into the design — from the
monograph's chapter 5 (`D/current/monograph/draft/MONOGRAPH_v1.md`, §5.1, Claude-drafted there) and
from Part 1's ruling that DXD is "Structural Intervention Over Visual Legibility" (Part 1, heading
at line 134).

### 1.2 Algorithmacy

**Roger's wordings.**

| Date | Wording | Locator |
|---|---|---|
| 10 Sep 2026 (Lima, unmarked) | "Algorithmacy names the sensibility required to interpret an opaque, adaptive intermediary …, to specify intent through the channels that intermediary permits, and to track its rule as that rule shifts." (elided) | `L/lima_pdw/manuscript/PAPER.md:151` |
| 10 Oct 2026 (author's introduction and rulings) | "We heap algorithmic management systems on people who lack algorithmacy, or the sensibility to navigate opaque triadic coordinative cooptation." | `L/algorithmacy_ot/manuscript/sbs_schoeneborn2026/ASSEMBLED_2026-10-10.md:15` |
| 10 Oct 2026 | "Algorithmacy is the sensibility to navigate irreducible triads. The algorithm creates an in-principle opaque, dynamic, mediated triad: I can tell you everything about the algorithm and you would not be any better off, while people who know nothing about it successfully navigate it." | same file, `:17` |
| 16 Oct 2026 (monograph, author ¶) | "a construct I call algorithmacy, or the sensibility to coordinate through an opaque, adaptive intermediary." | `D/current/monograph/draft/MONOGRAPH_v1.md:68` |
| 22 Oct 2026 (Spaces, Google Doc) | algorithmacy as "the competency required to navigate, evaluate, and steer triadic, opaque, and co-optive algorithmic environments" | `L/phd1750_spaces_in_stream/paper/gdoc_2026-10-22_orig.txt:3` |

The paper uses the 10 Oct wording, his newest and the one his brief echoes ("opaque, cooptive,
triadic"). It also inherits the sentence that matters most for design: knowing everything about the
algorithm leaves a person no better off. That sentence is why the model cannot be a legibility model
(§1.6, §3).

**[FLAG] Sensibility or competency.** The 10 Oct text calls algorithmacy a sensibility that "operates
through the competencies"; the Spaces doc calls it a competency. `L/algorithmacy_ot/AGENDA.md:10`
lists this as open. The paper follows 10 Oct: a sensibility, shown in three competencies.

### 1.3 The environment: opaque, co-optive, triadic

Roger's brief names the environment by three adjectives. The Lima derivation, which generates the
competencies, uses a different triple: "Opacity withholds the rule, so the actor must reconstruct it.
Bindingness turns every message into evidence before a verdict, so the actor must encode for judge and
counterpart at once. Adaptivity unsettles whatever the actor has learned, so the reconstruction has to
be maintained rather than achieved once." (`L/lima_pdw/manuscript/PAPER.md:161`).

**Reconciliation [DRAFTED; DECISION D-a].** The model keeps the brief's triple as its rows and glosses
each by the property that generates its competency.

| Row | Brief's adjective | Gloss | Generating property (Lima :161) | Source for the adjective |
|---|---|---|---|---|
| 1 | **opaque** | the rule producing a determination is hidden from the people it binds, in principle | opacity | Burrell 2016 (pointer `burrell2016how`, full text; her term is "technical illiteracy", CHECK F7); Roger's "in-principle opaque" (`ASSEMBLED…:17`) |
| 2 | **co-optive** | the intermediary enrols both parties on terms it sets — "co-opt …, i.e., evaluate and bind" | bindingness | D. Stark & Vanden Broeck 2024 (pointer `stark2024principles`, full text): "on platforms they are co-opted"; Roger's gloss, `ASSEMBLED…:15` |
| 3 | **triadic** | two parties and an intermediary form one unit; the third seat moves the rule | adaptivity | Roger's "irreducible triads" (`ASSEMBLED…:17`); the "does not hold still" property (Part 1 `:118`) |

The pairing of row 3 with adaptivity is the weakest of the three. A triad need not change, and
change is not triadic in itself. The defence is that in a triad the rule's author is a party with
interests of its own, so the rule moves for reasons neither party sees (Part 1 `:118`: "Traditional
media hold still; an algorithmic intermediary does not."). The alternative is to make adaptivity a
fourth adjective [DECISION D-a].

### 1.4 The three competencies

Roger's brief names them **intent specification, idempotent interpretation, intuitive governance
tracking**. The table gives their earlier wordings.

| Brief (11 Nov) | 10 Oct ruling (`ASSEMBLED…:17`) | Lima (`PAPER.md:163–165`) | Monograph (`D/…:68`) | Part 1 (`:94`) |
|---|---|---|---|---|
| idempotent interpretation | "interpret idempotent outputs to determine the variable inputs" | Interpreting | asymmetric interpretation | interpreting |
| intent specification | "specify intent so that those one is coordinated with have an easier time tracing back, which is distinct from prompting" | Specifying intent | intent specification | specifying intent |
| intuitive governance tracking | "keep track of rules that update constantly and unpredictably, which is less documenting them than sensing them as dynamic flows" | Keeping track | temporal tracking | keeping track |

**Idempotent interpretation [DRAFTED, per R1].** *The competency of reaching, from an output that
looks the same whatever produced it, a reading of which seat produced it — the counterpart, the rule,
or one's own input — that a second look, or a regenerated reply, would not change.* In computing an
operation is idempotent when applying it twice gives the result of applying it once; here the
person's reading is what should be idempotent. The problem it answers is Roger's 10 Oct wording: one
output, many possible inputs. Lima states the same problem as "one signal from which to infer two
minds" (`PAPER.md:169`).
- **[FLAG]** "Idempotent" carries two other senses in Roger's texts: "idempotent conversational
  content" for routine, non-committing generation (`L/phd1750_spaces_in_stream/paper/gdoc_2026-10-22_orig.txt:9`),
  and an input that leaves the trajectory where the system set it
  (`L/phd1750_spaces_in_stream/paper/DOC_EDITS_2026-10-22.md:13`). The paper uses only the R1 sense
  and says so once, with the computing definition.

**Intent specification.** *The competency of fixing what one means so that the intermediary and the
counterpart can trace a result back to it.* It is "distinct from prompting" (10 Oct) because a prompt
addresses the system alone, while the specification is read by two audiences at once: Lima's
"dual-audience encoding" (`PAPER.md:169`), whose failure mode is "Machine-legible, peer-illegible".

**Intuitive governance tracking [DRAFTED].** *The competency of sensing that the rules governing a
coordination are changing while they change, from the feel of results rather than from
announcements.* "Governance" names what is tracked (the rules that govern and bind both parties, Lima
`:165`). "Intuitive" names how: Roger's "less documenting them than sensing them as dynamic flows" (10
Oct) and his ruling D7, "we understand THROUGH deciding and quickly ingesting the results"
(`L/dxd_foundation/SOURCE.md:39`).
- **What the source allows.** Kahneman and Klein (2009) hold that intuition earns trust only in "an
  environment of sufficiently high validity and adequate opportunity to practice the skill" (p. 520),
  with "feedback that is both rapid and unequivocal" (p. 524), and that "high subjective confidence is
  not a good indication of validity" (p. 522). Source: the lab's full-text, verified card
  `L/dxd_foundation/literature/library/kahneman2009conditions.md` (pointer). An intermediary whose
  rule drifts silently lowers the validity of the very cues intuition learns from. So intuitive
  tracking is the competency silent drift defeats, and a person who feels on top of the changes may
  not be. That is the design opening for row 3.
- **[FLAG]** D7's claim that pilots "dont spend time reading the situation" needs the aviation
  literature, which treats monitoring as much of the pilot's work (`L/dxd_foundation/SOURCE.md:39`,
  flag recorded there). The paper does not use the pilot example.

**[FLAG] Which coordination condition each restores.** Two Claude-drafted texts disagree. The OT
draft maps interpreting → accountability, specifying intent → common understanding, keeping track →
predictability (`ASSEMBLED…:99`); the monograph maps interpretation and intent specification to the
inbound and outbound halves of common understanding and tracking to predictability, with
accountability answered by no facet (`D/…`, §2.5). The model does not need either mapping; it uses
the Lima derivation (what each property withholds). If the paper invokes Okhuysen and Bechky (2009),
Roger must pick one [DECISION D-j].

### 1.5 The animation frame: character, animator, viewer

L. Stark (2024) argues that LLM chatbots "can be best understood as animated characters" (p. 1663,
`stark2024animation`, full text). Three of his points shape the model.
- **The animator is a seat, not a person.** "Animated characters … are typified by the distributed
  agency of their creation and enlivenment" (p. 1666); a chatbot's animators include company staff,
  raters and moderators (p. 1667), and the user is "the final uncompensated animator" (p. 1667). The
  model therefore treats "animator" as a seat several parties fill (DECISION D-c, default).
- **What the animation hides is labour.** "The appeal and charisma of the animated character itself
  often pushes the actual living labor of their animators into the background or offstage" (p. 1666).
- **His remedy is governance, and Maeda and L. Stark (2025) want less animation in high-risk settings**
  (`maeda2025anthropomorphism`, full text, p. 1670). The model must say why its craft does not deepen
  the projection both papers warn against (§3, P5).

**The triad in the frame [DRAFTED].** Viewer = the person deciding. Character = the intermediary's
surface (the chat persona, the agent). Animator = the seat that produces the character's behaviour:
the operator, the counterpart whose inputs shape it (a merchant's bid, a seller's listing), and the
person. The frame is triadic in the algorithmacy sense only when two of the hands are the two parties
and the character's output binds both. A cartoon has seats but no binding; that is where the analogy
stops (§4).

**The anchor case, restated [DRAFTED; DECISION D-b].** Pass 2's commuter starts out searching for a
raincoat, "talk[s] through the commute with an agent, and realize[s] halfway through that an umbrella
is what they actually need" (`SOURCE.md`, Pass 2, ¶2). As written, the commuter then lands on a retail
site, and the site and the commuter form a dyad with an owner. The case becomes the model's case when
**the agent does the shopping**: it searches retailers for the commuter, ranks their offers by rules
that weigh the retailers' bids and the platform's own policy, and can place the order. Then the agent
evaluates and binds both parties (the commuter's money, the retailer's listing and delivery terms),
the retailer's inputs animate what the commuter sees, and the commuter's words animate what the
retailer is asked for. One added sentence in the paper, marked as mine, makes this explicit; Roger's
sentences stay as written.

### 1.6 The animator's craft (what is read)

The craft column rests on three full-text sources (run 2) and one tested principle.

| Source | Read | What it gives the model |
|---|---|---|
| Lasseter 1987 (`lasseter1987principles`) | full | Eleven named principles (p. 36); timing lives "on the spacing of the poses and not on the poses themselves" (p. 37); anticipation tells *what* comes next, not *why* (p. 38); staging, one idea at a time (p. 38); straight-ahead versus pose-to-pose, with in-betweens drawn by an assistant from a "timing chart" (p. 40); the computer as in-betweener overshoots and is "locked" by added keys (pp. 40–41); "The change must come before, or after, the move" (p. 42); character as thought process (p. 43); "the first goal of the animator is to entertain" (p. 43) |
| Chang & Ungar 1993 (`chang1993animation`) | full | The interface problem as interpretation of change (p. 45); animation "offloading some of the cognitive burden of interpreting the change to the perceptual system" (p. 46); anticipation as a cue (p. 50); effects that work below awareness (pp. 50, 52); §4 on what does not transfer (p. 53); anticipation for "remotely initiated actions" (p. 54) |
| Thomas & Calder 2001 (`thomas2001applying`) | full | Indirect changes whose before and after look alike (p. 209); the telltale preview of a trial operation, commit or cancel (p. 210); liking without performance gains, N = 17 and N = 13 (pp. 215, 219) |
| Dragicevic et al. 2011 (`dragicevic2011temporal`) | full | The one animator's principle tested in an interface (slow-in/slow-out); it helped object tracking; animation principles "may not necessarily transfer to interaction design" |
| Gonzalez 1996 (`gonzalez1996does`) | full | The one test of interface animation against **decision accuracy**: N = 89; gradual transitions — in which only one element changed in each frame — gave more accurate decisions than abrupt ones (F(1,78) = 5.84, p < .05), with no effect on time; transparent tasks with one right answer; dyadic |
| Schulz et al. 2019 (`schulz2019animation`) | full | Review of 27 HRI studies: key frames "define important (key) points in a movement. Then, the software or other animators interpolate the frames between the key frames" (p. 12:3); timing, staging, solid drawing and appeal tested in none; principles "were not verified scientifically" |
| Takayama et al. 2011 (`takayama2011expressing`) | full | N = 273 online video experiment: a robot's **forethought** (anticipation) did **not** predict correct readings of what it was doing (F(1,271) = 0.65, n.s.) but made viewers **more sure** (5.69 vs 5.20, F(1,255) = 15.95) and raised appeal |
| Ribeiro & Paiva 2012; Lewis et al. 2026; Kurian 2025 (cards) | full (Kurian: arXiv submitted version) | Craft carried into robots and child–AI design for life-likeness and persona; Lewis: Disney principles are "inherently limited" for embodied characters, puppetry principles instead, and an observer may read a calibrating robot's motion as "a shrug of apathy"; Kurian: six scaffolds from 52 Disney films, with persona craft offered as a route to "selective anthropomorphism" |

**What is not read.** Thomas and Johnston (1981), Williams (2001), and Whitaker and Halas (1981) are
book-length craft sources needing a library loan (DECISIONS, "What the browser reached"). The paper
cites Thomas and Johnston only as quoted in Lasseter or Chang and Ungar. No production source on model
sheets is read, so "keeping a character on model" is struck from row 1. **[FLAG]** Lasseter numbers
eleven principles, not twelve; the paper must not say "the twelve principles" on his authority.

**Why the craft fits DXD and not legibility [DRAFTED].** Animators never show the viewer the frames
or the rig. They decide what is staged, where the keys fall, how the in-betweens are spaced, and what
the audience is led to expect, so that the viewer understands the action without inspecting its
mechanism. Chang and Ungar say this outright for interfaces: animation moves the work of interpreting
change "to the perceptual system" (p. 46). Lasseter's anticipation settles "what he is going to do
next" while it "may not show why" (p. 38). That is the shape of DXD after Part 1 and the 30 Sep
ruling: do not teach the person to read the algorithm; build the reading into the interface. Roger's
"I can tell you everything about the algorithm and you would not be any better off" (`ASSEMBLED…:17`)
has a perceptual counterpart in Hoerl (2015; `hoerl2015seeing`, full text, Early View pages): at
slower projection speeds the motion seen at normal speed becomes invisible, which "does nothing to show
that the appearance of it at normal speed must be illusory" (EV p. 15). Slowing down does show
something true — that cinematic motion "objectively lacks continuity" (EV p. 15) — but it loses what
the viewer needed. The paper's analogy, which is mine and not Hoerl's: inspecting a single output of an
intermediary, as one would a frame, shows something true about it and hides what the decision needs,
which is a property of the sequence of determinations (who moved, whether the rule moved). Hoerl says
nothing about interfaces or AI and does not say the viewer is fooled.

**What the robot studies add [DRAFTED].** Takayama, Dooley and Ju (2011) give the model its sharpest
datum. Their robot's anticipatory "forethought" did not help viewers read what it was doing, yet made
them surer of their readings and liked the robot more. Craft spent on the character raised confidence
without raising accuracy — the dissociation of P5, and Kahneman and Klein's warning that confidence is
not validity. Lewis et al. (2026) supply the other half: a robot that is calibrating may be read as
shrugging, so a designer who animates a character chooses which of several readings the viewer
reaches, and may choose a false one. Both bear on idempotent interpretation: craft can make a reading
stable without making it true.

**Why the craft is also the danger [DRAFTED].** The same craft gives a character a mind ("Without a
thought process, the actions of a character are just a series of unrelated motions", Lasseter p. 43),
works below awareness ("The audience is not consciously aware of these effects", Chang and Ungar p. 50),
and can be used to suggest one action and deliver another (the surprise gag, Chang and Ungar p. 53).
Applied to an AI persona, it is the projection Stark and Maeda and Stark warn against. The competencies
are the selection rule that keeps the craft on the decision and off the character (P1, P5).

---

## 2. The model

**Working name: the animator's model of DXD [DECISION D-i].** One line: *animate the decision, not
the character.*

The model has three rows and two rules. Each row runs from what the environment withholds, to the
work it leaves the person (a competency), to the craft technique that does that work for a viewer at
home, to the design move that does it for the person in a decision interface. The rows' moves realize
interventions Part 1 and the monograph already argue for; the model's addition is the craft that says
*how* to build them and the competency that says *which* technique to choose.

### 2.1 The three rows

| | Row 1 — opaque | Row 2 — co-optive | Row 3 — triadic |
|---|---|---|---|
| **The environment withholds** | the rule and the source: one output, many possible causes | a private act: every input is evidence for two readers, and the system draws what lies between the person's words | a rule that holds still: an unseen seat changes it for its own reasons |
| **Work left to the person (competency)** | **idempotent interpretation** — a stable reading of which seat produced a determination | **intent specification** — fixing what one means so that others can trace results back to it | **intuitive governance tracking** — sensing rule changes as they happen |
| **The craft at home (read source)** | **Staging**: one idea at a time, "completely and unmistakably clear" (Lasseter p. 38). **The in-between table**: the same two extremes read as different actions by what lies between them (Lasseter p. 37, quoting Thomas and Johnston). **Transitions that keep the causal connection** between old and new states (Chang and Ungar pp. 45–46) | **Pose-to-pose**: the animator fixes the key poses and an assistant draws the in-betweens from a written **timing chart** (Lasseter p. 40). **The machine in-betweener overshoots**; the fix is added keys that "locked" the spline (pp. 40–41). **The telltale preview**: the trial result shown with a corner stretched back to the prior state, until commit or cancel (Thomas and Calder p. 210) | **Anticipation**: a cue that leads the audience "to expect it before it actually occurs" and settles *what*, not *why* (Lasseter p. 38; Chang and Ungar p. 50). **Change between moves**: "The change must come before, or after, the move" (Lasseter p. 42). **Remotely initiated actions** announced by anticipation (Chang and Ungar p. 54) |
| **The DXD move** | Stage each determination on its own and **label the seat that produced it** (your key / the counterpart / the platform's rule), without explaining the model; show how the new state follows from the old | Let the person **set a few key poses** — the commitments that matter — and show everything the intermediary generates between them as **provisional**, tethered to the last key, until the person commits; let the person **add a key** where the in-betweens drift; pass the key's note to the counterpart so they can trace the result back | **Cue a governance change before it lands**, and **land it between decisions**, never inside one; keep changes within a declared envelope so the cues stay valid for intuition |
| **Realizes (prior lab argument)** | the source tag (`D/…`, §5.1) | the channel for intent and structural refusal (Part 1 `:142–146`; Proposition 4, `:166`) | bounded envelopes and backward-compatible updates (Part 1 `:148`; Proposition 3, `:164`) |
| **In the anchor case** | The agent shows the umbrella offer alone, tagged "matches your 'arrive dry, under $30'" or "sponsored by Retailer B" | The commuter fixes "arrive dry", "under $30", "pick up on the way"; the agent's search and chat between them stay provisional; the order is the committed key, and the retailer sees the keys it was chosen against | The agent says before it starts ranking sponsored offers differently, and never changes the policy in the middle of a purchase |
| **Craft held back** | exaggeration of the persona; appeal | straight-ahead generation for commitments (keep it for exploration, below) | the surprise gag: an anticipation that misleads |

**The moving goal, in craft terms [DRAFTED].** Lasseter describes two approaches. Straight-ahead
action, where the animator "does one drawing after another, getting new ideas as he goes along", is
"used for wild, scrambling actions where spontaneity is important"; pose-to-pose "is used for animation
that requires good acting, where the poses and timing are all important" (p. 40). Pass 2's commuter
needs both: the goal is found straight-ahead (talking through the commute until the umbrella appears),
and then fixed pose-to-pose (the commitments that bind). The model's row 2 applies only to the second.
This gives the moving goal a design handle without a source claiming that goals move (run 1 found
none; `library/CRITIC.md`, §1–2).

### 2.2 The two rules

- **The selection rule (m4).** Carry an animation technique into a decision interface only if (a) at
  home it does work the viewer would otherwise do — reading a change, expecting the next action,
  seeing the one idea that matters — and (b) in the decision interface it does the work of one of
  the three competencies. Techniques whose home job is to give the character life — personality,
  appeal, exaggeration of the persona — fail (b) and stay out of the decision layer.
  **What is not new [FLAG].** Selecting animation techniques for a purpose, through an account of
  the receiver, has precedents: Gonzalez (1996) chose animation features by their effect on decision
  accuracy; Kurian (2025) chose Disney techniques through children's developmental stages; May, Dean
  and Barnard (2003) argued that film craft transfers only through a psychological account of the
  viewer. What the model adds is the receiver account itself — the three competencies an opaque,
  co-optive, triadic intermediary demands — and the placement rule, which runs against Kurian's use of
  persona craft to manage reliance.
- **The placement rule.** Craft goes on the decision (its keys, its sources, its changes), not on the
  character (its voice, its apparent thinking, its warmth).

### 2.3 Propositions

Each proposition can fail. The disconfirming result is given with it.

| # | Proposition | Disconfirmed if | Evidence now |
|---|---|---|---|
| **P1 Selection** | Techniques that pass the selection rule improve decision outcomes through an intermediary more than techniques that fail it, at equal liking. | Techniques chosen by the rule do no better on decision outcomes than a principle list applied wholesale. | Indirect: Dragicevic et al. (one principle, tested; warns against wholesale transfer); Chang and Ungar §4 (argued selection). No test. |
| **P2 Staged sources** | Staging one determination at a time with the producing seat labelled makes a person's attribution of a result more stable across regenerations and more accurate than an explanation of the model. | Labelled staging yields attributions no more stable or accurate than explanation, or no better than nothing. | Chang and Ungar p. 45 and Thomas and Calder p. 209 state the problem; Gonzalez 1996 (one change per frame raised decision accuracy, dyadic, transparent tasks); Part 1's XAI findings (`:100–102`) suggest explanation fails; Lewis et al. 2026 (a stable reading can be false). No test of labelled staging in a triad. |
| **P3 Key poses** | Letting a person set a few binding commitments, with the intermediary's in-between output shown as provisional, raises decision quality and the counterpart's ability to trace results back, compared with free prompting. | Key-pose interfaces do no better than free prompting on either outcome. | Lasseter p. 40 (division of labour); Thomas and Calder p. 210 (telltale; recall effect cited, not read); Dietvorst et al. 2018 via Part 1 `:104` (a narrow channel restored use). No triadic test. |
| **P4 Anticipated change** | A governance change cued before it lands and landed between decisions is detected more often than a silent or mid-decision change, and the person's confidence tracks the change better. The cue must announce the change to the rule, not show the character deliberating. | Cued, between-move changes are detected no better than silent ones; or the cue raises confidence without raising detection. | Lasseter p. 42; Chang and Ungar p. 54 (proposed); Kahneman and Klein pp. 520–524 (why silent drift defeats intuition); Takayama et al. 2011 (anticipation in the character raised sureness, not accuracy — the failure P4 must avoid); Part 1 `:110` reports chance-level detection of updates (Mohanty et al., not carded here). |
| **P5 Dissociation** | Craft spent on the character raises liking, attributed competence and confidence without raising decision quality; craft spent on the decision raises decision quality without that rise in confidence. | Character craft raises decision quality, or decision craft raises confidence as much as character craft does. | Takayama et al. 2011 (forethought: sureness and appeal up, correct readings unchanged); Thomas and Calder pp. 215, 219 (liked, no performance gain); Bhat 2025 (streaming raised perceived competence, trustworthiness and more; "no significant differences" in perceived effectiveness, p. 846); Tan et al. 2026 (longer latency read as more "thoughtful"; behaviour robust to latency). Against: Gonzalez 1996 (accuracy and enjoyment rose together, but her animation was of the decision display, not a character); Kurian 2025 proposes persona craft as a remedy for over-reliance. |
| **P6 Boundary** | The gains in P2–P4 are larger when the intermediary binds a counterpart than when it advises one person. | The gains are the same with a dyadic advisor. | Part 1 Proposition 2 (`:162`), untested. |
| **P7 Designers** | Designers given the three competencies choose and place animation techniques that meet P1–P4 more often than designers given the principle list. | No difference. | None. |

P2–P4 restate, in craft terms, claims Part 1 and the monograph already make; P1, P5 and P7 are new
to the lab. The paper should say so.

---

## 3. Why the model is not a legibility model

The 30 Sep ruling: "Algorithmacy is not legibility … not for a user who reads the algorithm more
skilfully" (`L/decision_experience_design/README.md:39–43`). Each row passes that test.
- Row 1 labels the seat that produced a determination and leaves the model unexplained, as the
  monograph's source tag does. Lasseter's anticipation settles what happens without showing why.
- Row 2 gives the person a channel and a way to refuse, not a view inside.
- Row 3 changes when and how the rule changes; it does not ask the person to read change logs.
  Part 1 already rejects "passive change notifications" (`:164`); row 3's cue differs because it is
  timed against the person's decisions and bounded by an envelope, as an anticipation is timed
  against the action.

**[FLAG] Chang and Ungar's "legibility"** means how readable a motion is (p. 53). The paper should
gloss the word or avoid it.

---

## 4. Where the analogy breaks

- **Cartoons are passive, interfaces interactive** (Chang and Ungar p. 53). The model keeps this: the
  person is also an animator (Stark p. 1667), which is why row 2 exists.
- **A cartoon has no binding.** Its seats are many, but nothing the audience does is evaluated and
  nothing binds two viewers. The triad is the interface's, not the cartoon's.
- **The animator's first goal is to entertain** (Lasseter p. 43). DXD's goal is the person's
  decision. The selection rule exists because these goals differ.
- **Live, not rendered.** An animated film is finished before it is seen; an agent draws its
  in-betweens live. Lasseter's machine in-betweener that overshoots (pp. 40–41) is the nearest craft
  case, and puppetry may be closer still [PENDING `lewis2026invisible`].
- **The perceptual mechanism.** The run-1 outline rested "locking in" on apparent motion, which the
  library found disputed (CHECK F12; `library/CRITIC.md`, §4.2). The model does not need a perceptual
  mechanism for lock-in; it needs only that viewers follow craft they do not notice (Chang and Ungar
  p. 50) [PENDING Hoerl; DECISION D-e].

---

## 5. The method warrant

May, Dean and Barnard (2003; `may2003using`, full text in run 2) argue that film craft transfers to
interface design "economically" only through "an intermediate psychological account" (p. 332). Their
account is Interacting Cognitive Subsystems; they tested it against one film (*The Mask of Zorro*,
1,916 cuts, 1,731 analysed, four viewers) and never against an interface, and two of their predictions
went "clearly in the wrong direction" (p. 363). The model takes their form only: craft → an account of
the receiver → design guidance. Kurian (2025) is a second precedent for the form, with child
development as the receiver account.
Its bridge has two spans.
1. **Why the craft works on viewers** — Chang and Ungar's offloading to perception (p. 46); Lasseter's
   practitioner account of anticipation and staging (p. 38). These are practitioners' claims, not
   tested perception science.
2. **What the decision setting needs from the person** — algorithmacy's three competencies, which
   say what work the intermediary leaves.

May and colleagues checked their account against craft practice (one film); the competencies have not
been validated (the Algorithmacy Competence Scale is unfielded; Lima Table B1 is a protocol). The
paper must say that the second span is a proposed construct.

---

## 6. Evidence by read depth

| Model element | Full text | Partial / abstract | Not held |
|---|---|---|---|
| Craft principles | Lasseter; Chang & Ungar; Thomas & Calder; Dragicevic | — | Thomas & Johnston; Williams; Whitaker & Halas (loan) |
| Craft in robots and agents | [PENDING Takayama 2011; Ribeiro & Paiva 2012; Schulz 2019; Lewis 2026; Kurian 2025 (submitted version)] | — | — |
| LLM as animation | L. Stark 2024; Maeda & L. Stark 2025; Jones 2026; Wu & Masson 2026 | Silvio 2010 (abstract) | Silvio 2019 (book) |
| Stream as frames | Gnewuch 2022; Tan 2026; Anderl 2024; Bhat 2025 | — | — |
| Environment properties | Burrell 2016; D. Stark & Vanden Broeck 2024 (pointers) | Ananny & Crawford 2018 (abstract) | — |
| Competencies | Roger's texts; Kahneman & Klein 2009 (pointer, full) | — | no validated measure |
| Method warrant | May et al. 2003 (partial → [PENDING] full) | — | May & Barnard 1995 |
| Perception | [PENDING Hoerl 2015 re-card]; Scholl & Tremoulet 2000 (sibling library, full) | Wertheimer; Anderson & Anderson; Steinman | — |
| Novelty | run-1 gap check (`library/GAP_CHECK.md`) | — | [PENDING `library/GAP_CHECK_2.md`] |

---

## 7. What belongs to the sibling papers

- ***Spaces in the Stream*** owns decision spaces, their marking in the token stream, the formula
  G = F × MI × (1 − O), stream pacing, event boundaries and the *scriptio continua* analogy. This
  paper cites them. Its own rows act on the coordination (keys, seats, rule changes), not on where a
  decision sits in the stream.
- **The *Philosophy & Technology* paper** (`wt-pt-animation`) owns AI development as animation
  production (the pipeline mapping) and the life/intelligence argument. Same three traits; the paper
  discloses the overlap.
- **Monograph and Part 1** own the full argument for the design moves (source tag, envelope, channel,
  accountability), word separation, and Φ. This paper cites them and adds the craft and the selection.
- **Lima / OT** own the construct's validation.

---

## 8. Decisions for Roger

| # | Question | My default |
|---|---|---|
| D-a | Rows on the brief's triple (opaque, co-optive, triadic) with generating properties as glosses, or rows on opacity, bindingness, adaptivity? | Brief's triple; adaptivity carried by row 3 |
| D-b | Restate the raincoat case so the agent shops across retailers? | Yes, one marked sentence |
| D-c | "Animator" as a seat several parties fill (after Stark)? | Yes |
| D-d | The competencies belong to the person; the designer's expertise is knowing them (30 Sep thesis)? | Yes |
| D-e | Drop apparent motion as the lock-in mechanism? | Yes, pending the Hoerl re-card |
| D-f | "Intuitive" grounded in Kahneman and Klein's conditions? | Yes, with the confidence caveat |
| D-g | Each CHECK flag F1–F13 closed or carried? | Carried where unread (F1 McLaren, F3–F4 Silvio, F10 Ananny & Crawford) |
| D-h | The working DXD definition (§1.1)? | As drafted |
| D-i | The model's name? | "the animator's model of DXD"; alternatives: "key-pose model", "decision animation" |
| D-j | Which coordination-condition mapping, if the paper uses Okhuysen and Bechky? | Neither; the Lima derivation |
| D-k | Use "twelve principles" anywhere? | No; Lasseter's eleven |
