<!--
COMPLETE VERSION (course), assembled by Claude (Opus 5.5) on 2026-11-12 from COURSE_v1.md.
- Roger's sentences (SOURCE.md, Pass 2) appear unmarked, verbatim and in his order.
- Every passage Claude wrote sits between [DRAFTED] and [/DRAFTED].
- Fact flags on Roger's text, open checks and adopted defaults are numbered [Note n] in the body
  and written out under 'Notes for the author' at the end. Nothing in Roger's text was changed.
-->

# Animate the Decision, Not the Character: Decision Experience Design for Opaque, Co-optive, Triadic Environments

Roger B. Hunt III

Bentley University

PHD1750-3 Independent Research Project (mapped to HF700-1 Foundations in Human Factors)

Professor Ericson [Note 1]

December 15, 2026 [Note 2]

---

## Introduction

Online retailers and their customers used to agree on the goal. If a shopper wanted a raincoat, the retailer built a simple, low-friction website to sell them that raincoat. Designer and buyer both knew the end goal before the interaction started.

That agreement breaks down when people solve problems using conversational agents like Claude or Grok. Suppose it is pouring outside and a commuter needs to figure out how to get to work dry. They might start out searching for raincoats, talk through the commute with an agent, and realize halfway through that an umbrella is what they actually need. If they land on a retail site engineered to push raincoat conversions, digital nudging tools (Weinmann, Schneider, & vom Brocke, 2016) collide with a shifting goal, and neither the site nor the user gets what they wanted.

[DRAFTED] Now suppose the agent does the shopping as well: it searches retailers for the commuter, ranks their offers by rules that weigh what each retailer pays and what the agent's operator prefers, and places the order. The agent then evaluates and binds both parties—the commuter's money and the retailer's terms—under a rule that neither of them wrote. [/DRAFTED]

The metrics that built modern web design—conversion rates, page stickiness, and dark patterns—fail when the destination is moving. Choice architecture proves that how options are presented systematically shapes what people decide (Johnson et al., 2012). But the design problem today is not how to push someone toward a fixed finish line. Decision Experience Design (DXD) is the practice of building interfaces that help a user figure out what decision to make when the finish line is still being worked out.

[Note 3]

Current chat and AI interfaces fall well short of supporting this work. Although models and interfaces change rapidly, three baseline conditions of the problem remain constant:

First, the user is a human being: biological, cognitive, and emotional. A separate body of research examines machine-to-machine agent experience; we bracket that literature here to focus on the human decider.

Second, the user environment is a platform that is opaque, co-optive, and triadic. Platforms coordinate activity by co-opting external actors, assets, and behaviors into organizational processes via algorithmic management (Stark & Vanden Broeck, 2024), while operating with an opacity rooted in corporate secrecy, technical specialization, and the scale of machine learning itself (Burrell, 2016). Demanding transparency does little to help the user decide, because peering inside a black box is not the same as understanding how a system exercises power across a relational environment (Ananny & Crawford, 2018).

[Note 4]

Third, the design move required is an aesthetic shift: recognizing that when we engage large language models, we are engaging animations. Building on Teri Silvio’s (2019) theory of animation as the projection of human agency and persona onto non-human objects, Luke Stark (2024) demonstrates that LLM chatbots function as animated characters that rely on stereotypes, obscure human labor, and manipulate emotion.

[Note 5]

Understanding LLM interfaces as animation clarifies why platform environments behave the way they do:

* Animation is constitutively opaque. There are literal missing frames. As Norman McLaren (1968) observed, animation is not the art of drawings that move, but the art of movements that are drawn; what happens between each frame is more consequential than what exists on the frame itself. Animation is the craft of manipulating the invisible interstices between frames.
* Animation is co-optive. At a certain threshold in an animated sequence, the viewer "locks in" and the perceptual gaps disappear, enlisting the viewer's own perception to supply continuity where none exists.
* Animation is triadic. Watching a stage actor is a dyadic encounter between an audience member ("I") and a performer ("Actor"). Watching animation introduces a third term: "I" am watching a "character" manipulated by an unseen "animator."

[Note 6]

To build interfaces suited for Decision Experience Design, researchers and designers must learn and apply the core methodologies of the animator (Chevalier et al., 2016; Silvio, 2019; Stark, 2024)—working deliberately with the missing frames rather than pretending the gaps do not exist.

[Note 7]

[DRAFTED]
This paper builds that claim into a model and maps it onto the four headings of the course. The three conditions say what the setting is; they do not yet say what the person must do in it, or which of the animator's methods a designer should take. I take the first from algorithmacy, which shows in three competencies—idempotent interpretation, intent specification and intuitive governance tracking—each naming work the intermediary leaves to the person. I take the second from the craft as animators codified it (Lasseter, 1987) and as interface designers borrowed it (Chang & Ungar, 1993; Thomas & Calder, 2001). Each competency, and the technique that answers it, falls under one course heading: what the decider can see (Perception), where the decider acts (Action), and how the decider keeps up with a rule that moves (Cognition). The last section, Human factors and design, states the model as a whole, its propositions and its limits.

The paper is a conceptual analysis, not a study. I built it from sources read in full wherever they could be obtained: the animator's principles as Lasseter (1987) set them out for computer animation, the interface work that borrowed them (Chang & Ungar, 1993; Thomas & Calder, 2001; Gonzalez, 1996), and the robot and chatbot studies that tested or applied them. Thomas and Johnston's (1981) book, the source most of these papers cite, was not read; I cite it only as others quote it. Every quotation in the sections that follow the introduction was checked against its source; the bracketed flags in the introduction mark what could not be.
[/DRAFTED]

## The Setting and the Person

[DRAFTED]
Algorithmacy belongs to a sequence. Oracy is the sensibility to navigate a direct dyad through speaking and hearing; literacy, the sensibility to read and write the texts that moderate a dyad; and algorithmacy, the sensibility to navigate an irreducible triad, in which an algorithm creates "an in-principle opaque, dynamic, mediated triad" (Hunt, 2026c). Hunt (2026c) puts the in-principle claim plainly: "I can tell you everything about the algorithm and you would not be any better off, while people who know nothing about it successfully navigate it."

The three conditions of the introduction name properties of the setting, and each is easy to see once the agent does the commuter's shopping. The setting is **opaque**: the rule that produces a determination is hidden from the people it binds, and Burrell (2016) traces such opacity to "intentional corporate or state secrecy", "technical illiteracy", and "the characteristics of machine learning algorithms and the scale required to apply them usefully" (p. 1). It is **co-optive**: "whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted" (D. Stark & Vanden Broeck, 2024, p. 1), and Hunt (2026c) glosses co-optation as "evaluate and bind". It is **triadic**: the two parties and the intermediary form one unit, and the third seat—the operator—sets the rule and changes it for reasons of its own. These line up with the properties from which Hunt (2026a) derives the competencies: opacity "withholds the rule", bindingness "turns every message into evidence before a verdict", and adaptivity "unsettles whatever the actor has learned".

Each competency is work the person does because the setting withholds something. One response is to teach people to read the system. Hunt (2026b) rejects that response for DXD: its expertise "centers instead on structural interventions that reshape the coordination environment". If knowing everything about the algorithm leaves a person no better off, explanation cannot be the design move. The design move is to take the work into the interface. Animators have done this for viewers since the 1930s, and the next three sections take one competency each.
[/DRAFTED]

## Perception: What the Decider Can See

[DRAFTED]
The opaque setting withholds the source of a determination: one output, several possible causes. The competency it asks of the person is **idempotent interpretation**—reaching, from an output that looks the same whatever produced it, a reading of which party produced it (the counterpart, the rule or one's own input) that a second look, or a regenerated reply, would not change. Hunt (2026c) states the problem as interpreting "idempotent outputs to determine the variable inputs". In computing, an operation is idempotent when doing it twice gives the result of doing it once; the term here describes the reading the person needs, not the output. The same umbrella could come first because the commuter asked for something cheap, because the retailer paid for the placement, or because the operator changed its ranking the day before.

What the commuter sees is already animated. L. Stark (2024) argues that ChatGPT and similar chatbots "can be best understood as animated characters" (p. 1663), and in a streamed reply the frames are literal. Wu and Masson (2026) call the word-by-word animation of model output "a happy accident resulting from the underlying technology" and such animations "glorified progress bars" (pp. 1–2); in their study, crafted and slower transitions helped 16 participants track and review the elements of a response. Bhat (2025) found that a reply typed out in real time raised perceived competence, warmth and trustworthiness, with "no significant differences" in perceived effectiveness (p. 846). Tan et al. (2026) treat latency as "a tunable design variable with ethical implications" (p. 1); their participants rated longer waits as more thoughtful while their logged behaviour did not change. Platforms already set the frames, and they set them for how the character seems.

Animators set frames for a different purpose: so that a viewer understands an action without seeing how it was made. Lasseter (1987) reports that the effect an object gives depends "entirely on the spacing of the poses and not on the poses themselves" (p. 37), and quotes Thomas and Johnston's demonstration that the same two drawings of a head read as a blow, a twitch, a crisp order or an appraisal depending on how many drawings lie between them. A film viewer sees those in-betweens. The user of an agent sees only the extremes—what was asked and what came back—and the same two extremes fit different meanings. That is the perceptual form of the problem. The animator's answer is staging: "the presentation of an idea so it is completely and unmistakably clear", with "only one idea" seen at a time (Lasseter, 1987, p. 38).

Interface designers carried this into screens. Chang and Ungar (1993) began from the observation that when a screen jumps, "the causal connection between the old state of the screen and the new state of the screen is not immediately clear" (p. 45), and argued that animation offloads "some of the cognitive burden of interpreting the change to the perceptual system" (p. 46). Thomas and Calder (2001) noted that for changes a user did not make directly, "if the initial and final state of the screen are similar, it may not be obvious just what has changed or how the change came about" (p. 209). Gonzalez (1996) supplies the one test against decisions: with 89 undergraduates, transitions that involved "the change of only one element in each display frame" (p. 29) produced more accurate decisions than abrupt ones, F(1,78) = 5.84, p < .05 (p. 32); her tasks had one correct answer and one user. The other experiments are less encouraging. Thomas and Calder found "no significant difference in execution time between the four feedback conditions" with 17 participants, who preferred any feedback to none and rated animation alone no better than plain selection handles (p. 215), and 13 others rated the animation "fun to use" but "were ambivalent about whether it improved productivity (mean = 4.3, sd = 2.0)" (p. 219). Dragicevic et al. (2011), after testing slow in and slow out on object tracking, warned that interface work "has largely been dominated by design principles from general animation that may not necessarily transfer to interaction design" (p. 2017). The craft helps a viewer see a change; whether it helps a decider is a separate question.

Perception also limits what showing more can do. Hoerl (2015) argues that the motion seen in film at normal speed is real, and that its vanishing when the projector slows "does nothing to show that the appearance of it at normal speed must be illusory" (p. 690). Slowing down does show something true—"cinematic motion objectively lacks continuity" (p. 690)—but it loses what the viewer needed. The analogy I draw, which is not Hoerl's, is that inspecting one output of an intermediary, as one would inspect a frame, hides what the decision needs: who moved, and whether the rule moved, are properties of the sequence of determinations.

The design move for perception follows. The interface stages each determination on its own and labels the seat that produced it—the person's own key, the counterpart or the operator's rule. In the commuter's case the agent shows the umbrella offer alone and marks it either as matching the limits the commuter set or as placed because the retailer paid. The label says who moved and leaves the model unexplained, and it is what makes the reading idempotent: asked again, the agent returns the same offer with the same mark, or a different offer with a different mark, and either way the commuter knows which seat changed. Lewis et al. (2026) give the warning: observers of a robot that was calibrating "might interpret its motion as a shrug of apathy" (p. 8). A stable reading can still miss the cause, so the label has to name the seat that actually produced the result.
[/DRAFTED]

## Action: Where the Decider Acts

[DRAFTED]
The co-optive setting takes away the private act. Every input is evidence that two audiences read, and the intermediary draws what lies between the person's words. The competency it asks of the person is **intent specification**—fixing what one means so that those one is coordinated with can trace a result back to it. Hunt (2026c) separates it from prompting: a prompt addresses the system alone, while a specification is read by two audiences at once. Hunt (2026a) calls this "dual-audience encoding" and names its failure "Machine-legible, peer-illegible". When the commuter tells the agent "under thirty dollars, and I need it before nine", the agent parses the words and the retailer receives an order shaped by them; if the retailer never sees "before nine", the order that binds the retailer no longer carries the commuter's intent. The label has other owners—Leveson (2000) uses "intent specifications" for a kind of software specification, and Vaithilingam et al. (2025) for a store of a user's intent kept by an AI system—but here it names a person's competency.

The person is not only a viewer. L. Stark (2024) notes that a chatbot's animators are many and that the last of them is "the individual human user interacting with the system", whose prompts "help populate an instance in the first place" (p. 1667). I therefore treat the animator as a seat several parties fill: in the commuter's case the operator, the retailers whose offers and payments shape what the agent says, and the commuter all animate the agent. Where the person acts, they act as one animator among several.

Animators have a method for sharing that work. In pose-to-pose animation the animator "plans his actions, figures out just what drawings will be needed to animate the business, makes the drawings concentrating on the poses, relates them to each other in size and action, and then draws the inbetweens" (Lasseter, 1987, p. 40), and a "timing chart" drawn beside the drawing tells "his assistant who will be doing the inbetweens later, how he wanted the timing to be and where he wanted the inbetween drawings placed" (p. 40). When the computer became the in-betweener, it could make a value "shoot in the wrong direction just before (or just after) the large change in value" (p. 41), and Lasseter's fix was more keys that "locked" the spline (p. 41). His conclusion was that keyframe animation cannot be approached "exactly as one would pose-to-pose hand drawn animation" (p. 40). A person who fixes a few commitments and leaves an agent to generate what lies between them stands where Lasseter's animator stood.

The design move for action has three parts. First, content the intermediary generates between keys is shown as provisional, tied to the last key the way Thomas and Calder's (2001) telltale shows an object where it will go "if the change is committed, but with a telltale corner stretched back to its original position" (p. 210), until the person commits or cancels; cancelling costs nothing. Second, where the in-betweens drift, the person adds a key. Third, the key's note travels with the commitment: as the timing chart told the in-betweener what the animator meant, the commuter's "before nine" travels to the retailer with the order. Two precedents built parts of this for one user. Zhang and Davis (2026) let writers "specify different types of narrative constraints at selected moments in a story, then use AI to generate intervening prose" (p. 1), although in their system generated material can rewrite the writer's keys (p. 6); the model asks that the person's keys hold. Pinhanez (2017) applied anticipation to "an important action such as charging a credit card", giving "one more chance for the user to change her mind" (p. 31). He also borrowed from bunraku, in which the puppeteer stays visible: a chatbot shows the user its "alternative understandings of an utterance from the user" (p. 31) and asks which is meant, so that the user settles the system's ambiguity about the user. The model adds the counterpart.

The moving goal of the introduction fits here. Lasseter (1987) distinguishes straight-ahead animation, which "is used for wild, scrambling actions where spontaneity is important", from pose-to-pose animation, which "is used for animation that requires good acting, where the poses and timing are all important" (p. 40). The commuter needs both. The umbrella is found straight-ahead, by talking the commute through; the purchase is made pose-to-pose. The action move applies only to the second.
[/DRAFTED]

## Cognition: Keeping Up With a Moving Rule

[DRAFTED]
The triadic setting takes away a rule that holds still: the operator changes the rule for reasons neither party sees. The competency it asks of the person is **intuitive governance tracking**—sensing that the rules governing a coordination are changing while they change, from the feel of results rather than from announcements. Hunt (2026c) calls it "less documenting them than sensing them as dynamic flows". *Intuitive* carries a condition. Kahneman and Klein (2009) hold that intuitions earn trust only in "an environment of sufficiently high validity and adequate opportunity to practice the skill" (p. 520), with "feedback that is both rapid and unequivocal" (p. 524), and they warn that "high subjective confidence is not a good indication of validity" (p. 522). An intermediary whose rule drifts without notice lowers the validity of the very cues the person learns from, so intuitive tracking is the competency that silent drift defeats. DeVito (2021) comes closest among prior accounts: users of changing platforms keep re-theorising how the platform works and decide whether to adapt, limit their use or leave. Her users face a platform and an audience; no counterpart shares the binding determination with them.

The craft has a technique for change. Anticipation leads the audience "to expect it before it actually occurs"; it "may not show why he is doing something, but there is no question about what he is going to do next" (Lasseter, 1987, p. 38). And a change made during a major movement "will go unnoticed": "The change must come before, or after, the move" (p. 42). Chang and Ungar (1993) proposed anticipation for collaborative software, where "remote users often will initiate actions, so the user may not even have the advantage of expecting something to happen" (p. 54).

The evidence on anticipation is a caution. Takayama, Dooley and Ju (2011) found, with 273 participants, that a robot's forethought "was not found to be a significant predictor of keyword match in the participant's descriptions of robot activity", yet viewers were surer of their readings (5.69 against 5.20 on a 1–7 scale) (p. 74). Szafir, Mutlu and Fong (2014) "found no manipulation that significantly improved accuracy over the baseline for any individual primitive" when a flying robot used arcs, easing and anticipation, and anticipation, which lengthened each flight by a third, "significantly lowered composite scores for several primitives" (pp. 361–362); in a separate study, 24 participants nonetheless preferred the robot that flew with the manipulations (p. 363). Anticipation spent on the character raised confidence without raising accuracy—the gap Kahneman and Klein warn about. Dragan, Holladay and Srinivasa (2014) approach the same gap from the other side: in their model of deceptive robot motion, the observer "will not only be wrong, but will be confidently wrong" (p. 4).

The design move for cognition takes anticipation's function, not its form as motion. The interface cues a change of rule before it lands, as an explicit statement about the rule, and lands it between decisions, never inside one. In the commuter's case the agent says, before it starts ranking paid placements differently, that the ranking is about to change, and it never changes the rule in the middle of a purchase. The cue must also be reliable: changes made only inside a declared envelope, and always cued, because intuition learns only from valid cues. Hunt (2026b) argues for such envelopes and for updates that preserve what users have learned; this move supplies the craft for their timing. Here the remote party Chang and Ungar had in mind is the operator, and the action is a change of rule.
[/DRAFTED]

## Human Factors and Design: The Model

[DRAFTED]
The three moves make a model with two rules (Table 1; Figure 1). The **selection rule** carries an animation technique into a decision interface only if, at home, it does work the viewer would otherwise do—reading a change, expecting the next action, seeing the one idea that matters—and, in the interface, it does the work of one of the three competencies. The **placement rule** puts the technique on the decision—its commitments, its sources, its changes of rule—and not on the character's voice, warmth or apparent thought. Squash and stretch, appeal and the exaggeration of a persona fail the selection rule, because their home work is to give a character life; the robot studies show that in an interface they raise appeal and confidence. Robotics borrowed the craft for exactly that end. Schulz, Torresen and Herstad (2019) reviewed 27 robot studies, noted that the principles "were not verified scientifically" (p. 12:2), and found timing, staging, solid drawing and appeal tested in none of them; Lewis et al. (2026) argue that Disney's principles are "inherently limited" for embodied characters and turn to puppetry instead (p. 1).

The warrant for borrowing comes from May, Dean and Barnard (2003), who argued that a craft reaches interface design "economically" only through "an intermediate psychological account" of what it does to the receiver (p. 332). Their own account was tested on one film with four viewers and never on an interface. I take their form, not their account: here the account of the receiver is algorithmacy, and it is proposed, not validated. Gonzalez's (1996) decision accuracy and Kurian's (2025) developmental stages are other accounts of the receiver; Kurian chose Disney techniques through what children can perceive at each stage of development.

The animation frame also says what a designer must not do. "The appeal and charisma of the animated character itself often pushes the actual living labor of their animators into the background or offstage" (L. Stark, 2024, p. 1666), and Maeda and L. Stark (2025) add that "animation disguises—or at least distracts from—this fact" (p. 1663). Neither paper draws a design method from the frame; Stark's remedies are governance, and Maeda and Stark hold that "technical guardrails are needed to prevent excessive animation in high-risk contexts" (p. 1670). A paper that tells designers to animate better has to answer them. The answer here is selection and placement: the competencies say which techniques serve the person's decision, and the rest stay off it.

Each part of the model has a precedent. Pinhanez (2017) drew chatbot design methods from puppetry and animation, Zhang and Davis (2026) put keyframes and model-generated in-betweens into a writing tool, and Kurian (2025) chose techniques through an account of the user. I found no work that selects professional animation techniques through the competencies a person needs to decide through an opaque, binding, adaptive intermediary; the searches are reported with the journal version of this paper.
[/DRAFTED]

**Table 1.** The animator's model of DXD, by course heading. [DRAFTED]

| | Perception | Action | Cognition |
|---|---|---|---|
| Setting | opaque | co-optive | triadic |
| What it withholds | the source of a determination | a private act | a rule that holds still |
| Competency | idempotent interpretation | intent specification | intuitive governance tracking |
| Craft at home | staging; visible passage between states | pose-to-pose; timing chart; extra keys | anticipation; change before or after the move |
| Design move | stage each determination; label the seat that produced it | the person sets keys; in-betweens provisional until commit or cancel; the key's note travels to the counterpart | cue the rule change before it lands; land it between decisions, inside an envelope |
| Held back | exaggeration of the persona; appeal | straight-ahead generation for commitments | the surprise gag; the character's visible "thinking" |
[/DRAFTED]

**Figure 1.** The animator's model of DXD (file `figures/figure1_model.svg`). [DRAFTED] Each row runs from what the setting withholds, through the competency, to the animator's technique and the design move; the character layer is held back. [/DRAFTED]

[DRAFTED]
**Not legibility.** Each move passes the test Hunt (2026b) set for DXD: the perception move labels who moved and leaves the model unexplained, the action move gives the person a channel and a way to refuse, and the cognition move changes when and how the rule changes rather than asking the person to read change logs. Robotics uses "legible" for motion that is "intent-expressive" (Dragan, Lee, & Srinivasa, 2013); the moves are legible in that sense, not in the sense of reading the algorithm.

**Propositions.** Each can fail, and each names a measure. (P1) Techniques that pass the selection rule improve decision outcomes more than techniques that fail it, at equal liking; measured as decision quality against a criterion the parties set in advance. (P2) Staging one determination at a time with its seat labelled makes attributions more stable across regenerated replies, and more accurate, than an explanation of the model; measured as agreement of attributions across regenerations and accuracy against the known source. (P3) Letting a person fix binding commitments, with the output between them provisional, raises decision quality and the counterpart's ability to trace a result back to the person's intent; measured as decision quality and whether the counterpart can state the intent behind the order. (P4) A rule change cued before it lands and landed between decisions is detected more often, with better-calibrated confidence, than a silent or mid-decision change; measured as detection rate and the match between confidence and accuracy. (P5) Craft spent on the character raises liking and confidence without raising decision quality; craft spent on the decision raises decision quality without that rise in confidence. (P6) These gains are larger when the intermediary binds a counterpart than when it advises one person. (P7) Designers given the three competencies place techniques better than designers given a list of principles. P5 has the most support so far, all from single users (Takayama et al., 2011; Bhat, 2025). P4 has none yet: neither read test of an anticipatory cue found one that raised accuracy, so P4 bets that an explicit cue about the rule does what motion cues did not.

**The surprise gag.** The craft can deceive. Chang and Ungar (1993) warned that anticipation can suggest one action and deliver another (p. 53); Tan et al. (2026) write that "deliberately manipulating response speed sits uneasily between positive friction and potential deception" (§5.5); and Dragan, Holladay and Srinivasa (2014) built robot motion that "tricks the observer into believing that the robot is not moving towards its actual goal" (p. 1). The placement rule is this paper's answer: a label that says who produced a result, a preview that can be cancelled and a cue that a rule will change are true statements about the coordination, while a thinking indicator and a warm voice are statements about a character. The rule does not make the craft safe. The model assumes that seat labels and cues are accurate, and the accountability for that accuracy lies with the operator.

**Where the analogy breaks, and limits.** An animated film has many hands and binds no one: nothing a viewer does is evaluated, and no viewer's choice binds another, so the triad belongs to the interface, not to the cartoon. A cartoon is passive and an interface interactive (Chang & Ungar, 1993), and an agent draws its in-betweens live, while a film is finished before anyone sees it. Lasseter's computer in-betweener, which overshoots between keys, is the nearest case in the craft, and puppetry, which animates live, may be closer still (Lewis et al., 2026). The animator's first goal is to entertain (Lasseter, 1987, p. 43), while the goal of DXD is the person's decision; the selection rule exists because the two goals differ. No study has tested the model, no instrument yet measures algorithmacy, and the craft is read through Lasseter (1987), Chang and Ungar (1993) and Thomas and Calder (2001) rather than through Thomas and Johnston's (1981) book. The paper brackets agent experience and works one case.
[/DRAFTED]

## Conclusion

[DRAFTED]
The commuter ends with an umbrella and a purchase, and between them is an agent that ranked, chose and committed on behalf of the commuter and of the retailer. The introduction asked designers to learn the animator's methods. The model says which methods, and where: for perception, staging and labelled seats; for action, key poses with provisional in-betweens; for cognition, anticipated change between moves. None of them asks the commuter to read the algorithm. The propositions say how to find out whether they work.
[/DRAFTED]

## Statement on generative AI use

[DRAFTED] The author used Claude (Anthropic; Claude Code, models Fable 5.2 and Opus 5.5, November 2026) to search for and retrieve sources, to write notes on them, to check every citation, quotation and number against the source texts, and to draft the sections that follow the introduction. The argument and wording of the introduction are the author's own. The author reviewed and revised all drafted text and takes full responsibility for the content of this paper. [/DRAFTED] [Note 8]


## Notes for the author

[DRAFTED]
1. VERIFY: instructor's name and title as the course lists them
2. VERIFY: due date
3. FLAG F5: "proves" — Johnson et al. (2012) is a review; "shows" fits.
4. FLAG F7–F10: Burrell's term is "technical illiteracy"; D. Stark and Vanden Broeck write "activities"; give initials for the two Starks; Ananny and Crawford's argument concerns accountability (abstract read only).
5. FLAG F2–F3: Stark argues rather than demonstrates; Silvio's definition reaches the lab only through Stark.
6. FLAG F1, F4, F12: no 1968 McLaren source exists; Silvio concedes performance and animation are hard to separate; the perceptual account of "locks in" is disputed (Hoerl, 2015).
7. FLAG F11: Chevalier et al. review interface animation, not the animator's craft; Lasseter (1987) states the craft.
8. FLAG: the sentence "The author reviewed and revised all drafted text" is true only after your revision; edit the declaration to match what you did before submission.
9. Defaults adopted in this complete version (MODEL.md §8), open to your objection: D-c, the animator is a seat several parties fill (after L. Stark); D-d, the competencies belong to the person and the designer's expertise is knowing them; D-e, apparent motion is dropped as the mechanism of 'locking in'; D-f, 'intuitive' is grounded in Kahneman and Klein's conditions; D-h, the working DXD definition; D-i, the working title and the model's name; D-j, the Lima derivation rather than either coordination-condition mapping; D-k, Lasseter's eleven principles, not 'twelve'.
[/DRAFTED]

## References

[DRAFTED]

Ananny, M., & Crawford, K. (2018). Seeing without knowing: Limitations of the transparency ideal and its application to algorithmic accountability. *New Media & Society*, *20*(3), 973–989. https://doi.org/10.1177/1461444816676645

Bhat, M. (2025). How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces (IUI '25)* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131

Burrell, J. (2016). How the machine 'thinks': Understanding opacity in machine learning algorithms. *Big Data & Society*, *3*(1), Article 2053951715622512. https://doi.org/10.1177/2053951715622512

Chang, B.-W., & Ungar, D. (1993). Animation: From cartoons to the user interface. In *Proceedings of the 6th Annual ACM Symposium on User Interface Software and Technology* (pp. 45–55). ACM. https://doi.org/10.1145/168642.168647

Chevalier, F., Henry Riche, N., Plaisant, C., Chalbi, A., & Hurter, C. (2016). Animations 25 years later: New roles and opportunities. In *Proceedings of the International Working Conference on Advanced Visual Interfaces (AVI '16)* (pp. 280–287). ACM. https://doi.org/10.1145/2909132.2909255

DeVito, M. A. (2021). Adaptive folk theorization as a path to algorithmic literacy on changing platforms. *Proceedings of the ACM on Human-Computer Interaction*, *5*(CSCW2), Article 339, 1–38. https://doi.org/10.1145/3476080

Dragan, A., Holladay, R., & Srinivasa, S. (2014). An analysis of deceptive robot motion. In *Robotics: Science and Systems X*. https://doi.org/10.15607/rss.2014.x.010

Dragan, A. D., Lee, K. C. T., & Srinivasa, S. S. (2013). Legibility and predictability of robot motion. In *2013 8th ACM/IEEE International Conference on Human-Robot Interaction (HRI)* (pp. 301–308). IEEE. https://doi.org/10.1109/hri.2013.6483603

Dragicevic, P., Bezerianos, A., Javed, W., Elmqvist, N., & Fekete, J.-D. (2011). Temporal distortion for animated transitions. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '11)* (pp. 2009–2018). ACM. https://doi.org/10.1145/1978942.1979233

Gonzalez, C. (1996). Does animation in user interfaces improve decision making? In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems: Common Ground (CHI '96)* (pp. 27–34). ACM Press. https://doi.org/10.1145/238386.238396

Hoerl, C. (2015). Seeing motion and apparent motion. *European Journal of Philosophy*, *23*(3), 676–702. https://doi.org/10.1111/j.1468-0378.2012.00565.x

Hunt, R. B., III. (2026a). *Algorithmacy: A competency for coordinative co-optation* [Paper presentation]. Organization Studies / Organization Theory Paper Development Workshop, Universidad de Piura, Lima, Peru.

Hunt, R. B., III. (2026b, September 30). *Decision experience design* [Substack post]. https://rogerhuntphdcand.substack.com/p/decision-experience-design

Hunt, R. B., III. (2026c). *Toward an account of algorithmacy: A triadic view of working through algorithms* [Manuscript in preparation].

Johnson, E. J., Shu, S. B., Dellaert, B. G. C., Fox, C., Goldstein, D. G., Häubl, G., Larrick, R. P., Payne, J. W., Peters, E., Schkade, D., Wansink, B., & Weber, E. U. (2012). Beyond nudges: Tools of a choice architecture. *Marketing Letters*, *23*(2), 487–504. https://doi.org/10.1007/s11002-012-9186-1

Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist*, *64*(6), 515–526. https://doi.org/10.1037/a0016755

Kurian, N. (2025). Once upon an AI: Six scaffolds for child-AI interaction design, inspired by Disney. *International Journal of Child-Computer Interaction*, *46*, Article 100788. https://doi.org/10.1016/j.ijcci.2025.100788

Lasseter, J. (1987). Principles of traditional animation applied to 3D computer animation. In *Proceedings of the 14th Annual Conference on Computer Graphics and Interactive Techniques* (pp. 35–44). ACM. https://doi.org/10.1145/37401.37407

Leveson, N. G. (2000). Intent specifications: An approach to building human-centered specifications. *IEEE Transactions on Software Engineering*, *26*(1), 15–35. https://doi.org/10.1109/32.825764

Lewis, C., Collins, S., Hanson, A., Smith, J., & Williams, T. (2026). *Invisible strings: Deriving puppetry principles and their hidden connections to robot behavior design* (arXiv:2607.03289). arXiv. https://doi.org/10.48550/arxiv.2607.03289

Maeda, T., & Stark, L. (2025). Anthropomorphism as social affordance: Charting the co-animation of chatbots into social "agents." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, *8*(2), 1661–1673. https://doi.org/10.1609/aies.v8i2.36664

May, J., Dean, M. P., & Barnard, P. J. (2003). Using film cutting techniques in interface design. *Human–Computer Interaction*, *18*(4), 325–372. https://doi.org/10.1207/s15327051hci1804_1

McLaren, N. (1968). [No source found; see the Notes for the author.]

Pinhanez, C. S. (2017). Design methods for personified interfaces. In *Proceedings of the International Conference on Computer-Human Interaction Research and Applications (CHIRA 2017)* (pp. 27–38). SciTePress. https://doi.org/10.5220/0006487500270038

Schulz, T., Torresen, J., & Herstad, J. (2019). Animation techniques in human-robot interaction user studies: A systematic literature review. *ACM Transactions on Human-Robot Interaction*, *8*(2), Article 12, 1–22. https://doi.org/10.1145/3317325

Silvio, T. J. (2019). *Puppets, gods, and brands: Theorizing the age of animation from Taiwan*. University of Hawaii Press. https://doi.org/10.1515/9780824880989

Stark, D., & Vanden Broeck, P. (2024). Principles of algorithmic management. *Organization Theory*, *5*(2), Article 26317877241257213. https://doi.org/10.1177/26317877241257213

Stark, L. (2024). Animation and artificial intelligence. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1663–1671). ACM. https://doi.org/10.1145/3630106.3658995

Szafir, D., Mutlu, B., & Fong, T. (2014). Communication of intent in assistive free flyers. In *Proceedings of the 2014 ACM/IEEE International Conference on Human-Robot Interaction (HRI '14)* (pp. 358–365). ACM. https://doi.org/10.1145/2559636.2559672

Takayama, L., Dooley, D., & Ju, W. (2011). Expressing thought: Improving robot readability with animation principles. In *Proceedings of the 6th International Conference on Human-Robot Interaction (HRI '11)* (pp. 69–76). ACM. https://doi.org/10.1145/1957656.1957674

Tan, F. F.-Y., Messerschmidt, M. A., Yin, W., & Nov, O. (2026). The impact of response latency and task type on human-LLM interaction and perception. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26)* (pp. 1–17). ACM. https://doi.org/10.1145/3772318.3790716

Thomas, B. H., & Calder, P. (2001). Applying cartoon animation techniques to graphical user interfaces. *ACM Transactions on Computer-Human Interaction*, *8*(3), 198–222. https://doi.org/10.1145/502907.502909

Thomas, F., & Johnston, O. (1981). *Disney animation: The illusion of life*. Abbeville Press.

Vaithilingam, P., Kim, M., Acosta-Parenteau, F.-C., Lee, D., Mhedhbi, A., Glassman, E. L., & Arawjo, I. (2025). *Semantic Commit: Helping users update intent specifications for AI memory at scale* (arXiv:2504.09283). arXiv.

Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital nudging. *Business & Information Systems Engineering*, *58*(6), 433–436. https://doi.org/10.1007/s12599-016-0453-1

Wu, J., & Masson, D. (2026). *AInimation: Animating from prompt to AI-generated responses* (arXiv:2607.18507). arXiv. https://doi.org/10.48550/arxiv.2607.18507

Zhang, C., & Davis, A. (2026). Narrative keyframing for generative creative writing. In *Proceedings of the 39th Annual ACM Symposium on User Interface Software and Technology (UIST '26)* (pp. 1–19). ACM. https://doi.org/10.1145/3830398.3830586
[/DRAFTED]