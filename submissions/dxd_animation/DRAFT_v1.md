<!--
DRAFT v1 — written by Claude (Opus 5.5) on 2026-11-11 for Roger's read-aloud.
How to read it:
- Roger's own sentences (SOURCE.md, Pass 2) appear unmarked and verbatim, in his order, in Section 1.
- Every passage Claude wrote sits between [DRAFTED] and [/DRAFTED].
- [FLAG Fn …] notes a fact in Roger's text that a read source contradicts or does not support (CHECK.md numbering); his sentence is left as written.
- [DECISION D-x] marks a default taken from MODEL.md §8 that Roger may overrule.
- [VERIFY …] marks something not yet checked against a source.
- Every citation resolves to a card in library/cards/ (key in the reference notes) or to one of Roger's own manuscripts.
- The draft keeps American spelling and double quotation marks so that Roger's sentences stay verbatim. TIES requires British -ise spelling and single quotation marks; convert at submission.
- Self-citations (Hunt 2026a–d) must be anonymised for TIES's double-anonymous review.
- Page numbers: where a PDF prints no page numbers (Takayama et al.; Pinhanez; Dragicevic et al., HAL copy with a cover page; Hoerl, Early View layout), the page is inferred from Crossref's range and the PDF's page count, which match in each case (checked 2026-11-12).
- Target: TIES "no more than 10000 words, inclusive of" tables, references and captions (venue/TIES.md).
-->

# Animate the Decision, Not the Character: An Animator's Model of Decision Experience Design

[DECISION D-i: working title and model name.]

## Abstract

[DRAFTED]
Conversational agents change what an interface has to do. A commuter who sets out to buy a raincoat may, after talking the commute through with an agent, find that an umbrella is what they need—and the agent that found it may also rank the retailers who sell it and place the order. Interfaces for such agents are opaque, co-optive and triadic: two parties coordinate through an intermediary that evaluates and binds both under rules neither can see. I propose a model of decision experience design (DXD) for this setting. Algorithmacy, the sensibility such settings demand, shows in three competencies—idempotent interpretation, intent specification and intuitive governance tracking—and each names work the intermediary leaves to the person. Professional animators have a codified craft for doing a viewer's work without showing the frames: staging, key poses with in-betweens drawn by other hands, timing charts, anticipation, and placing a change between moves. The model uses the competencies to choose which techniques to carry into a decision interface, and it places them on the decision rather than on the character. It is stated as three rows, two rules and seven propositions that a study could refute. The evidence so far is indirect and comes from single-user interface and robot studies.
[/DRAFTED]

**Relevance to human factors / ergonomics theory**

[DRAFTED]
Human–AI decision research mostly studies one person facing one machine advisor (Hunt, 2026b). Agent interfaces put an intermediary with interests of its own between two parties who must coordinate. This paper derives, from the structure of that setting, the work a person must do in it, and uses that account to select and place techniques from animation craft. It offers designers a theory-led basis for borrowing from a neighbouring craft and gives researchers seven propositions to test.
[/DRAFTED]

**Keywords:** decision experience design; algorithmacy; animation principles; human–AI interaction; intermediaries; interface design

---

## 1. Introduction

Online retailers and their customers used to agree on the goal. If a shopper wanted a raincoat, the retailer built a simple, low-friction website to sell them that raincoat. Designer and buyer both knew the end goal before the interaction started.

That agreement breaks down when people solve problems using conversational agents like Claude or Grok. Suppose it is pouring outside and a commuter needs to figure out how to get to work dry. They might start out searching for raincoats, talk through the commute with an agent, and realize halfway through that an umbrella is what they actually need. If they land on a retail site engineered to push raincoat conversions, digital nudging tools (Weinmann, Schneider, & vom Brocke, 2016) collide with a shifting goal, and neither the site nor the user gets what they wanted.

[DRAFTED] Now suppose the agent does the shopping as well: it searches retailers for the commuter, ranks their offers by rules that weigh what each retailer pays and what the agent's operator prefers, and places the order. The agent then evaluates and binds both parties—the commuter's money and the retailer's terms—under a rule that neither of them wrote. [/DRAFTED] [DECISION D-b: this sentence makes the case triadic; without it the case reads as a dyad plus an owner (library/CRITIC.md, cut 6).]

The metrics that built modern web design—conversion rates, page stickiness, and dark patterns—fail when the destination is moving. Choice architecture proves that how options are presented systematically shapes what people decide (Johnson et al., 2012). But the design problem today is not how to push someone toward a fixed finish line. Decision Experience Design (DXD) is the practice of building interfaces that help a user figure out what decision to make when the finish line is still being worked out.

[FLAG F5: Johnson et al. (2012), read in full (`johnson2012beyond`), is a review of choice-architecture tools; it supports "shows", not "proves". Jachimowicz et al. (2019) carry the meta-analytic evidence (`jachimowicz2019when`). Your call.]

Current chat and AI interfaces fall well short of supporting this work. Although models and interfaces change rapidly, three baseline conditions of the problem remain constant:

First, the user is a human being: biological, cognitive, and emotional. A separate body of research examines machine-to-machine agent experience; we bracket that literature here to focus on the human decider.

[FLAG: the paper is single-authored and the rest of the draft uses "I"; "we" here is yours to keep or change. The library found no source for "biological" and "emotional" (library/CRITIC.md, §3.1).]

Second, the user environment is a platform that is opaque, co-optive, and triadic. Platforms coordinate activity by co-opting external actors, assets, and behaviors into organizational processes via algorithmic management (Stark & Vanden Broeck, 2024), while operating with an opacity rooted in corporate secrecy, technical specialization, and the scale of machine learning itself (Burrell, 2016). Demanding transparency does little to help the user decide, because peering inside a black box is not the same as understanding how a system exercises power across a relational environment (Ananny & Crawford, 2018).

[FLAG F8: APA asks for initials when two first authors share a surname: "D. Stark & Vanden Broeck, 2024" here and "L. Stark, 2024" below.]
[FLAG F9: D. Stark and Vanden Broeck write "actors, assets, and activities", not "behaviors".]
[FLAG F7: Burrell's second source of opacity is "technical illiteracy", not "technical specialization".]
[FLAG F10: Ananny and Crawford's argument concerns accountability; the step to "help the user decide" is yours. The library holds their abstract only, so "across a relational environment" is unconfirmed.]

Third, the design move required is an aesthetic shift: recognizing that when we engage large language models, we are engaging animations. Building on Teri Silvio’s (2019) theory of animation as the projection of human agency and persona onto non-human objects, Luke Stark (2024) demonstrates that LLM chatbots function as animated characters that rely on stereotypes, obscure human labor, and manipulate emotion.

[FLAG F2: Stark (2024) argues; the paper is conceptual and runs no test. Stark's own words are "to demonstrate the utility of such a frame".]
[FLAG F3: Silvio's definition, as Stark quotes it, projects qualities "outside of the self, and into the sensory environment" and lists "personality", not "persona"; Stark dates it 2019, p. 52, and Maeda and L. Stark (2025) date the same words 2010. Neither Silvio text is read.]

Understanding LLM interfaces as animation clarifies why platform environments behave the way they do:

* Animation is constitutively opaque. There are literal missing frames. As Norman McLaren (1968) observed, animation is not the art of drawings that move, but the art of movements that are drawn; what happens between each frame is more consequential than what exists on the frame itself. Animation is the craft of manipulating the invisible interstices between frames.
* Animation is co-optive. At a certain threshold in an animated sequence, the viewer "locks in" and the perceptual gaps disappear, enlisting the viewer's own perception to supply continuity where none exists.
* Animation is triadic. Watching a stage actor is a dyadic encounter between an audience member ("I") and a performer ("Actor"). Watching animation introduces a third term: "I" am watching a "character" manipulated by an unseen "animator."

[FLAG F1: no 1968 source for McLaren has been found; the earliest traced is his letter printed in Sifianos (1995), not held. A read source states the timing point in citable form: weight "depend[s] entirely on the spacing of the poses and not on the poses themselves" (Lasseter, 1987, p. 37). Noted, not substituted.]
[FLAG F12 / DECISION D-e: the perceptual account of "locks in" is disputed. Hoerl (2015), now read in full, argues that cinematic motion is not Wertheimer-type apparent motion and that the motion seen at normal speed is real, not supplied by the viewer. Section 3 handles this; your bullet stands as written.]
[FLAG F4: Silvio contrasts introjection (performance) with projection (animation), and concedes that "in practice, performance and animation are [hard] to separate" (as quoted in L. Stark, 2024, p. 1668). Stark's animators are many, and he names the user as one (p. 1667). Section 3 treats "animator" as a seat several parties fill.]

To build interfaces suited for Decision Experience Design, researchers and designers must learn and apply the core methodologies of the animator (Chevalier et al., 2016; Silvio, 2019; Stark, 2024)—working deliberately with the missing frames rather than pretending the gaps do not exist.

[FLAG F11: Chevalier et al. (2016), read in full, review interface animation and do not describe the animator's methods. Lasseter (1987) states the methods and is read in full.]

[DRAFTED]
This paper builds that claim into a model. The three conditions say what the setting is. They do not yet say what the person must do in it, or which of the animator's methods a designer should take. I take the first from algorithmacy, the sensibility to navigate opaque, triadic, coordinative co-optation (Hunt, 2026c). It shows in three competencies—idempotent interpretation, intent specification and intuitive governance tracking—and each names work the intermediary leaves to the person: settling which party produced a result, fixing what one means so that others can trace it, and sensing that the rules have moved. I take the second from the craft as animators codified it (Lasseter, 1987) and as interface designers borrowed it (Chang & Ungar, 1993; Thomas & Calder, 2001). The competencies then select the techniques. A technique enters a decision interface when, at home, it does work a viewer would otherwise do and, here, it does one competency's work; and it goes on the decision, not on the character.

Each part of this has a precedent. Pinhanez (2017) drew chatbot design methods from puppetry and animation, Zhang and Davis (2026) put keyframes and model-generated in-betweens into a writing tool, and Kurian (2025) chose Disney techniques through what children can perceive at each stage of development. I found no work that selects professional animation techniques through the competencies a person needs to decide through an opaque, binding, adaptive intermediary, in the searches reported in Section 7.3. Section 2 defines the setting and the competencies. Section 3 reads the interface as an animation. Section 4 reviews what animators know and what happened when designers borrowed it. Section 5 states the model, Section 6 its propositions, and Section 7 its ethics and limits.
[/DRAFTED]

## 2. The setting and the person

### 2.1 Algorithmacy

[DRAFTED]
Algorithmacy belongs to a sequence. Oracy is the sensibility to navigate a direct dyad through speaking and hearing; literacy, the sensibility to read and write the texts that moderate a dyad; and algorithmacy, the sensibility to navigate an irreducible triad, in which an algorithm creates "an in-principle opaque, dynamic, mediated triad" (Hunt, 2026c). The phrase *in principle* carries the weight. Hunt (2026c) puts it this way: "I can tell you everything about the algorithm and you would not be any better off, while people who know nothing about it successfully navigate it." Knowing the system is neither what a person needs nor enough. What a person needs is a set of practised competencies, and what a designer needs is to know what those competencies are for.
[/DRAFTED]

### 2.2 Opaque, co-optive, triadic

[DRAFTED]
The three conditions of the introduction name properties of the setting, and each is easy to see once the agent does the commuter's shopping.

The setting is **opaque**: the rule that produces a determination is hidden from the people it binds. Burrell (2016) separates three sources of such opacity—"intentional corporate or state secrecy", "technical illiteracy", and opacity that comes from "the characteristics of machine learning algorithms and the scale required to apply them usefully" (p. 1). The commuter cannot see why the agent put one umbrella first, and neither can the retailer that lost the sale.

The setting is **co-optive**: the intermediary enrols both parties on terms it sets. D. Stark and Vanden Broeck (2024) mark the difference in one sentence: "whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted" (p. 1). Hunt (2026c) glosses co-optation as "evaluate and bind". The agent scores each retailer's offer and commits the commuter's money to one of them.

The setting is **triadic**: the two parties and the intermediary form one unit, and the third seat—the operator—sets the rule and changes it for reasons of its own. Hunt (2026c) describes rules "that update constantly and unpredictably".

These three properties line up with the three from which Hunt (2026a) derives the competencies. Opacity "withholds the rule". Bindingness "turns every message into evidence before a verdict". Adaptivity "unsettles whatever the actor has learned". I read *co-optive* through bindingness and *triadic* through adaptivity, because in a triad the rule's author is a party with interests the other two cannot see.
[/DRAFTED] [DECISION D-a: rows on your triple, glossed by the generating properties; the alternative is to keep adaptivity as a fourth property.]

### 2.3 Three competencies

[DRAFTED]
**Idempotent interpretation** is the competency of reaching, from an output that looks the same whatever produced it, a reading of which party produced it—the counterpart, the rule or one's own input—that a second look, or a regenerated reply, would not change. Hunt (2026c) states the problem as interpreting "idempotent outputs to determine the variable inputs". In computing, an operation is idempotent when doing it twice gives the result of doing it once; the term here describes the reading the person needs, not the output. The agent's recommendation is the case. The same umbrella could come first because the commuter asked for something cheap, because the retailer paid for the placement, or because the operator changed its ranking the day before. Hunt (2026a) calls this having "one signal from which to infer two minds". A reading that flips each time the commuter asks again is not yet an interpretation. [DECISION D-m: the label is also used once in mathematical logic, for something else; kept per your ruling R1.]

**Intent specification** is the competency of fixing what one means so that those one is coordinated with can trace a result back to it. Hunt (2026c) separates it from prompting: a prompt addresses the system alone, while a specification is read by two audiences at once. Hunt (2026a) calls the requirement "dual-audience encoding" and names its failure "Machine-legible, peer-illegible". When the commuter tells the agent "under thirty dollars, and I need it before nine", the agent parses the words and the retailer receives an order shaped by them. If the retailer never sees "before nine", the order that binds the retailer no longer carries the commuter's intent. The label has other owners. Leveson (2000) uses "intent specifications" for a kind of software specification, and Vaithilingam et al. (2025) for a store of a user's intent kept by an AI system; here the term names a person's competency. [DECISION D-l]

**Intuitive governance tracking** is the competency of sensing that the rules governing a coordination are changing while they change, from the feel of results rather than from announcements. Hunt (2026c) calls it "less documenting them than sensing them as dynamic flows". *Intuitive* carries a condition. Kahneman and Klein (2009) hold that intuitions earn trust only in "an environment of sufficiently high validity and adequate opportunity to practice the skill" (p. 520), with "feedback that is both rapid and unequivocal" (p. 524), and they warn that "high subjective confidence is not a good indication of validity" (p. 522). An intermediary whose rule drifts without notice lowers the validity of the very cues the person learns from. Intuitive tracking is therefore the competency that silent drift defeats, and a person who feels on top of the changes may not be. DeVito (2021) comes closest among prior accounts: users of changing platforms keep re-theorising how the platform works and decide whether to adapt to it, limit their use or leave. Her users face a platform and an audience; no counterpart shares the binding determination with them.
[/DRAFTED]

### 2.4 Why reading the algorithm does not help

[DRAFTED]
Each competency is work the person does because the setting withholds something: the source of a result, a private channel for meaning, a rule that holds still. One response is to teach people to read the system. Hunt (2026b) rejects that response for DXD: "Decision experience design must abandon the pursuit of turning users into visual decoders of complex models", and its expertise "centers instead on structural interventions that reshape the coordination environment". The in-principle opacity of Section 2.1 says why. If knowing everything about the algorithm leaves a person no better off, explanation cannot be the design move. The design move is to take the work into the interface, so that the person no longer supplies by sensibility what the design could supply by construction. Animators have done this for viewers since the 1930s.
[/DRAFTED]

## 3. The interface as an animation

[DRAFTED]
L. Stark (2024) argues that ChatGPT and similar chatbots "can be best understood as animated characters" (p. 1663). Two parts of his argument matter here.

The first is that an animated character has many hands. "Animated characters (be they Chinese dragon puppets, Disney films, or chatbots) are typified by the distributed agency of their creation and enlivenment" (p. 1666). A chatbot's animators include the company's staff and the people who rate its outputs, and the last of them is "the individual human user interacting with the system", whose prompts "help populate an instance in the first place" (p. 1667). I therefore treat the animator as a seat that several parties fill, not as a person. In the commuter's case the operator, the retailers whose offers and payments shape what the agent says, and the commuter all animate the agent. The triad of the introduction holds in the algorithmacy sense when two of those hands are the two parties to a coordination and the character's output binds both. [DECISION D-c]

The second is what the animation hides. "The appeal and charisma of the animated character itself often pushes the actual living labor of their animators into the background or offstage" (L. Stark, 2024, p. 1666). Maeda and L. Stark (2025) put it more strongly: "animation disguises—or at least distracts from—this fact", the fact being the network of agents behind a system's apparent agency (p. 1663). Neither paper draws a design method from the frame. Stark's remedies are governance, and Maeda and Stark hold that "technical guardrails are needed to prevent excessive animation in high-risk contexts" (p. 1670). A paper that tells designers to animate better has to answer them. My answer is selection: the competencies say which techniques serve the person's decision, and the rest stay off it.

In a streamed reply the frames are literal. Wu and Masson (2026) note that the word-by-word animation of model output is "a happy accident resulting from the underlying technology" and call such animations "glorified progress bars" (pp. 1–2); in their study, crafted and slower transitions helped 16 participants track and review response elements. Tan et al. (2026) treat latency as "a tunable design variable with ethical implications" (p. 1); their participants rated longer waits as more thoughtful while their logged behaviour did not change. Bhat (2025) found that a reply typed out in real time raised perceived competence, warmth and trustworthiness, with "no significant differences" in perceived effectiveness (p. 846). Platforms already set the frames, and they set them for how the character seems. The stream itself, and where in it a decision lies, is the subject of a companion paper (Hunt, 2026d).

One perceptual claim needs care. The introduction says the viewer "locks in" and that perception supplies continuity. Hoerl (2015) argues that cinematic motion is not the apparent motion of Wertheimer's experiments. The motion seen at normal speed is real, and "The fact that cinematic motion becomes invisible when we slow down the projector does nothing to show that the appearance of it at normal speed must be illusory" (p. 690). Slowing down does show something true: "cinematic motion objectively lacks continuity" (p. 690). It also loses what the viewer needed. The analogy I draw, which is not Hoerl's, is that inspecting one output of an intermediary, as one would inspect a frame, shows something true about it and hides what the decision needs. Who moved, and whether the rule moved, are properties of the sequence of determinations, not of any one of them. [DECISION D-e]
[/DRAFTED]

## 4. What animators know

### 4.1 Principles, keys and other hands

[DRAFTED]
Lasseter (1987) wrote the craft down for a new medium. Disney's animators, he reports, analysed action in drawing classes until "procedures were isolated and named, analyzed and perfected, and new artists were taught these practices as rules of the trade" (p. 36). He lists eleven: squash and stretch, timing, anticipation, staging, follow through and overlapping action, straight ahead and pose-to-pose action, slow in and out, arcs, exaggeration, secondary action, and appeal (p. 36). He addressed the designers of animation systems as well as animators (p. 35). Four of his points carry the model. [DECISION D-k: other sources say twelve, citing Thomas and Johnston (1981), whose book has not been read; the paper uses Lasseter's count.]

The first is that meaning lives between the poses. The weight an object shows depends "entirely on the spacing of the poses and not on the poses themselves" (p. 37). Lasseter quotes Thomas and Johnston's demonstration: two drawings of a head, one leaning toward the right shoulder and one to the left, read as a blow, a nervous twitch, a crisp order or a thoughtful appraisal depending on how many drawings lie between them. "Each inbetween drawing added between these two 'extremes' gives a new meaning to the action" (p. 37). The film viewer sees the in-betweens. The user of an agent sees only the extremes—what was asked and what came back—and the same two extremes are compatible with different meanings. That is the form of the problem idempotent interpretation faces.

The second is a division of labour. In pose-to-pose animation the animator "plans his actions, figures out just what drawings will be needed to animate the business, makes the drawings concentrating on the poses, relates them to each other in size and action, and then draws the inbetweens" (p. 40). The in-betweens need not be the animator's own: a "timing chart" drawn beside the drawing tells "his assistant who will be doing the inbetweens later, how he wanted the timing to be and where he wanted the inbetween drawings placed" (p. 40). Keyframe animation made the computer the in-betweener, and the computer misbehaved. Its spline interpolation could make a value "shoot in the wrong direction just before (or just after) the large change in value" (p. 41). Lasseter's fix was more keys, extra extremes that "locked" the spline (p. 41), and his conclusion was that keyframe animation cannot be approached "exactly as one would pose-to-pose hand drawn animation" (p. 40). A person who fixes a few commitments and leaves an agent to generate what lies between them stands where Lasseter's animator stood.

The third is that the craft directs a viewer without explaining itself. Staging is "the presentation of an idea so it is completely and unmistakably clear", and "only one idea" should be seen at a time (p. 38). Anticipation leads the audience "to expect it before it actually occurs"; it "may not show why he is doing something, but there is no question about what he is going to do next" (p. 38, citing Thomas and Johnston).

The fourth concerns change. A change of facial expression made during a major body movement "will go unnoticed, and value intended will be lost"; "The change must come before, or after, the move" (p. 42).

Lasseter also says what the craft is for. "Without a thought process, the actions of a character are just a series of unrelated motions" (p. 43), and "the first goal of the animator is to entertain" (p. 43). The principles exist to make a character seem to think and to hold an audience. That is their value to an animator, and their risk in an interface where someone has to decide.
[/DRAFTED]

### 4.2 The craft carried into interfaces

[DRAFTED]
Chang and Ungar (1993) carried the principles, as they read them in Thomas and Johnston, into the interface of the Self programming environment. They began from an interpretation problem. When a screen jumps from one state to the next, "the causal connection between the old state of the screen and the new state of the screen is not immediately clear" (p. 45), and the user must work out which changes their own action caused. Animation, they argued, offloads "some of the cognitive burden of interpreting the change to the perceptual system" (p. 46). They used anticipation as "a cue about the main action to follow" (p. 50) and proposed it for collaborative software, in which "remote users often will initiate actions, so the user may not even have the advantage of expecting something to happen" (p. 54). They also said what does not transfer. A cartoon is passive and an interface interactive, and a cartoon's surprise gag—an anticipation that suggests one action and delivers another—would disturb the user of a tool (p. 53). Their evidence was informal user testing (p. 53).

Thomas and Calder (2001) added principles for direct manipulation and ran two experiments. One passage states the interpretation problem for changes the user did not make directly: "if the initial and final state of the screen are similar, it may not be obvious just what has changed or how the change came about" (p. 209). Their remedy for trial operations shows an object in the position it will take "if the change is committed, but with a telltale corner stretched back to its original position" (p. 210), so that committing and cancelling are both in view. Their experiments did not show the animation improving performance. With 17 participants, an analysis "showed no significant difference in execution time between the four feedback conditions"; participants preferred any feedback to none, and rated animation alone no better than plain selection handles (p. 215). Thirteen others rated the animation "fun to use" (mean 6.3 on a 7-point scale) but "were ambivalent about whether it improved productivity (mean = 4.3, sd = 2.0)", a self-rating rather than a measure of performance (p. 219).

Gonzalez (1996) supplies the one test against decisions. Eighty-nine undergraduates made choices through eight interface treatments, and transitions that involved "the change of only one element in each display frame" (p. 29) produced more accurate decisions than abrupt ones, F(1,78) = 5.84, p < .05 (p. 32). Her tasks had one correct answer and one user. Dragicevic et al. (2011) tested a single principle, slow in and slow out, on object tracking, and still warned that interface work "has largely been dominated by design principles from general animation that may not necessarily transfer to interaction design" (p. 2017).
[/DRAFTED]

### 4.3 The craft carried into robots, chatbots and language models

[DRAFTED]
Robotics borrowed the same craft for a different end: to make a machine seem alive. Schulz, Torresen and Herstad (2019) reviewed 27 robot studies and noted that the principles "were not verified scientifically" (p. 12:2) and that timing, staging, solid drawing and appeal were tested in none of them. Takayama, Dooley and Ju (2011) give the clearest test. In an online experiment with 273 participants, a robot that showed forethought before acting was no easier to read: forethought "was not found to be a significant predictor of keyword match in the participant's descriptions of robot activity" (p. 74). Viewers of the forethought robot were nonetheless surer of their readings (5.69 against 5.20 on a 1–7 scale) and found the robot more appealing (p. 74). Anticipation spent on the character raised confidence without raising accuracy. Szafir, Mutlu and Fong (2014) found the same for a flying robot whose paths used arcs, easing and anticipation. With 85 online viewers they "found no manipulation that significantly improved accuracy over the baseline for any individual primitive", and anticipation, which lengthened each flight by a third, "significantly lowered composite scores for several primitives" (pp. 361–362); in a separate study, 24 participants preferred the robot that flew with the manipulations, F(1, 23) = 13.39 (p. 363). Lewis et al. (2026) argue that Disney's principles are "inherently limited" for embodied interactive characters and derive puppetry principles instead. One of their cases is a robot that is calibrating; "observers might interpret its motion as a shrug of apathy" (p. 8). A viewer can settle on a reading of a character's motion that does not match its cause. Dragan, Holladay and Srinivasa (2014) made that happen on purpose. They built motion that "tricks the observer into believing that the robot is not moving towards its actual goal" (p. 1); in their model such an observer "will not only be wrong, but will be confidently wrong" (p. 4). Their 12 users also disagreed about who was behind the motion: seven thought the robot was intentionally deceiving them, and two thought a programmer had made the motion by hand (p. 8).
[/DRAFTED]

[DRAFTED]
Conversational and generative interfaces have drawn on the craft as well. Pinhanez (2017) drew design methods for chatbots from puppetry and animation and applied anticipation to a binding act: "an important action such as charging a credit card is clearly anticipated by actions which potentially could be stopped by the user", so that there is "one more chance for the user to change her mind" (p. 31). He left the other principles unexplored "due to space restrictions" and offered his workshops as illustration, "not as validation" (p. 34). Kurian (2025) derived six design scaffolds for children's AI from 52 Disney films, choosing techniques through what children can perceive at each stage of development; she proposes animated-sidekick personas as "a route to selective anthropomorphism, a design strategy that maintains engagement while signalling the AI's non-human nature" (p. 14). Zhang and Davis (2026) took keyframing into a writing tool in which writers "specify different types of narrative constraints at selected moments in a story, then use AI to generate intervening prose" (p. 1), and one of their design goals was tracing "how characterization decisions propagate into generated story text" (p. 4).

Two things follow from these studies. Craft spent on making a character seem alive raises appeal, attributed competence and confidence, and has not been shown to raise accuracy (Bhat, 2025; Takayama et al., 2011); and interface animation that users enjoy has not been shown to improve their performance (Thomas & Calder, 2001). The techniques that help a person read a change or hold to a commitment—one change at a time, a preview that can be cancelled, anticipation before a binding act, keys the machine must pass through—appear in these studies only with one user and a system, never with a counterpart bound by the same determination.
[/DRAFTED] [VERIFY: Kurian's page numbers are those of the arXiv submitted version. The version of record (CC BY) is on ScienceDirect, which showed a CAPTCHA to the automated browser on 2026-11-12; open it yourself and map the pages.]

### 4.4 The warrant for borrowing

[DRAFTED]
Borrowing a craft needs a warrant. May, Dean and Barnard (2003) argued that film editors' craft could reach interface design "economically" only through "an intermediate psychological account" of what the craft does to a viewer (p. 332). Their account, Interacting Cognitive Subsystems, predicted where viewers' eyes would move after a cut. They tested it on one film with four viewers and never on an interface, and two of its predictions went "clearly in the wrong direction" (p. 363). I take their form, not their account. Gonzalez's decision accuracy and Kurian's developmental stages are other accounts of the receiver. The account here is algorithmacy: the three competencies say what the person must do, and so what a technique must do if it is to help. That account is proposed, not validated, and the bridge is only as strong as the construct.
[/DRAFTED]

## 5. The model

### 5.1 Two rules

[DRAFTED]
The model has two rules and three rows (Table 1; Figure 1). The **selection rule** carries an animation technique into a decision interface only if, at home, it does work the viewer would otherwise do—reading a change, expecting the next action, seeing the one idea that matters—and, in the interface, it does the work of one of the three competencies. The **placement rule** puts the technique on the decision—its commitments, its sources, its changes of rule—and not on the character's voice, warmth or apparent thought. Squash and stretch, appeal and the exaggeration of a persona fail the selection rule, because their home work is to give a character life. The robot studies show what such techniques do in an interface: they raise appeal and confidence.
[/DRAFTED]

### 5.2 Row 1: opaque → idempotent interpretation → staging and labelled seats

[DRAFTED]
The opaque setting withholds the source of a determination: one output, several possible causes. The craft that answers it is staging—one idea at a time, unmistakably clear—together with the animator's habit of making the passage from one state to the next visible, which Chang and Ungar (1993) used to keep "the causal connection" between screens. The design move is to stage each determination on its own and label the seat that produced it: the person's own key, the counterpart or the operator's rule. The label says who moved; it does not explain the model. In the commuter's case the agent shows the umbrella offer alone and marks it either as matching the limits the commuter set or as placed because the retailer paid. The label is what makes the reading idempotent. Asked again, the agent returns the same offer with the same mark, or a different offer with a different mark, and either way the commuter knows which seat changed. Gonzalez's (1996) result—one change per frame, more accurate decisions—is the nearest evidence, from a single user. Lewis et al.'s (2026) calibrating robot, read as shrugging, is the warning: a reading can be stable and still miss the cause, so the label has to name the seat that actually produced the result.
[/DRAFTED]

### 5.3 Row 2: co-optive → intent specification → key poses and provisional in-betweens

[DRAFTED]
The co-optive setting takes away the private act. Every input is evidence that two audiences read, and the intermediary draws what lies between the person's words. The craft that answers it is pose-to-pose animation with in-betweens drawn by other hands. The person sets a few key poses—the commitments that matter—and the intermediary generates everything between them. The design move has three parts. First, generated content between keys is shown as provisional, tied to the last key the way Thomas and Calder's (2001) telltale ties a trial position to the original, until the person commits or cancels; cancelling costs nothing. Second, where the in-betweens drift, the person adds a key, as Lasseter added extremes to lock an overshooting spline. Third, the key's note travels with the commitment. As the timing chart told the in-betweener what the animator meant, the commuter's "before nine" travels to the retailer with the order, so that the counterpart can trace the result back to the intent. Zhang and Davis (2026) built keys with generated in-betweens for a writer working alone, although in their system generated material can rewrite the writer's keys: editing a perspective keyframe "triggers an update to the corresponding character keyframe" (p. 6). The model asks the reverse, that the person's keys hold. Pinhanez (2017) built the commit-or-cancel moment for a credit-card charge. The model adds the counterpart and derives the move from intent specification. In Hunt's (2026b) terms, the move is a channel for intent and a refusal that costs nothing.

The moving goal of the introduction fits here. Lasseter distinguishes straight-ahead animation, in which the animator "does one drawing after another, getting new ideas as he goes along" and which "is used for wild, scrambling actions where spontaneity is important", from pose-to-pose animation, which "is used for animation that requires good acting, where the poses and timing are all important" (p. 40). The commuter needs both. The umbrella is found straight-ahead, by talking the commute through; the purchase is made pose-to-pose. Row 2 applies only to the second. Zhang and Davis name the same tension as a limit of their system, which "may feel restrictive for writers who prefer to develop stories in a more fluid or improvisational way" (p. 11).
[/DRAFTED]

### 5.4 Row 3: triadic → intuitive governance tracking → anticipation and change between moves

[DRAFTED]
The triadic setting takes away a rule that holds still: the operator changes the rule for reasons neither party sees. The craft that answers it is anticipation, together with Lasseter's rule that a change must come "before, or after, the move" (p. 42). The design move is to cue a change of rule before it lands and to land it between decisions, never inside one. In the commuter's case the agent says, before it starts ranking paid placements differently, that the ranking is about to change, and it never changes the rule in the middle of a purchase. Two conditions keep the cue honest. It must announce the rule, not show the character deliberating: Takayama et al. (2011) found that a robot's forethought made viewers surer of their readings without making them more accurate, which is the opposite of what tracking needs, and Szafir et al. (2014) found no anticipatory flight path that made viewers more accurate. The row therefore takes anticipation's function—saying what will happen before it happens—and not its form as a motion: the cue is an explicit statement about the rule. And the cue must be reliable—changes made only inside a declared envelope, and always cued—because intuition learns only from valid cues (Kahneman & Klein, 2009). Hunt (2026b) argues for such envelopes and for updates that preserve what users have learned; the row supplies the craft for their timing. Chang and Ungar (1993) proposed anticipation for actions that remote users start. Here the remote party is the operator, and the action is a change of rule.
[/DRAFTED]

**Table 1.** The animator's model of DXD. [DRAFTED]

| | Row 1 | Row 2 | Row 3 |
|---|---|---|---|
| Setting | opaque | co-optive | triadic |
| What it withholds | the source of a determination | a private act | a rule that holds still |
| Competency (the person's work) | idempotent interpretation | intent specification | intuitive governance tracking |
| Craft at home | staging; visible passage between states | pose-to-pose; timing chart; extra keys | anticipation; change before or after the move |
| Design move | stage each determination; label the seat that produced it | the person sets keys; in-betweens provisional until commit or cancel; the key's note travels to the counterpart | cue the rule change before it lands; land it between decisions, inside an envelope |
| In the commuter's case | the umbrella offer, marked "matches your limits" or "placed by the retailer" | "arrive dry", "under thirty dollars", "before nine" fixed as keys; the order carries them | "ranking changes after this purchase"; never mid-purchase |
| Held back | exaggeration of the persona; appeal | straight-ahead generation for commitments | the surprise gag; the character's visible "thinking" |
[/DRAFTED]

**Figure 1.** The animator's model of DXD. [DRAFTED] Each row runs from what the setting withholds, through the competency that names the person's work, to the animator's technique that does that work for a viewer and the design move that does it for a decider. The selection rule admits a technique only if it does a competency's work; the placement rule keeps the character layer out of the decision. (File: `figures/figure1_model.svg`.) [/DRAFTED]

*Image description (alt text) for TIES:* [DRAFTED] A diagram with three rows and four columns: setting, competency, animator's technique, design move. Row 1: opaque, idempotent interpretation, staging, stage each determination and label the party that produced it. Row 2: co-optive, intent specification, pose-to-pose with a timing chart, the person sets key commitments and the agent's in-between output stays provisional until commit or cancel. Row 3: triadic, intuitive governance tracking, anticipation and change between moves, cue a rule change before it lands and land it between decisions. Below, a struck-through dashed box labelled "character layer, held back" lists persona exaggeration, appeal, visible thinking and the surprise gag. [/DRAFTED]

### 5.5 Not a legibility model

[DRAFTED]
Each row passes the test Hunt (2026b) set for DXD. Row 1 labels who moved and leaves the model unexplained. Row 2 gives the person a channel and a way to refuse, not a view inside. Row 3 changes when and how the rule changes rather than asking the person to read change logs. Hunt (2026b) rejects "dispatching passive change notifications"; the row's cue differs because it is timed against the person's decisions and bounded by an envelope, as an anticipation is timed against an action. Pinhanez's (2017) borrowing from bunraku, in which a chatbot shows the user its "alternative understandings of an utterance from the user" (p. 31) and asks which is meant, sits close to the line. It asks the user to settle the system's ambiguity about the user, which can serve intent specification, and it is not an explanation of the model. Robotics uses the word differently again: Dragan, Lee and Srinivasa (2013) call a collaborative robot's motion legible when it is "intent-expressive", so that a watcher can infer its goal. Rows 1 and 3 are legible in that sense; the ruling concerns legibility as reading the algorithm.
[/DRAFTED]

## 6. Propositions

[DRAFTED]
Each proposition can fail, and the measure that would show it is named.

- **P1 (Selection).** Techniques that pass the selection rule improve decision outcomes through an intermediary more than techniques that fail it, at equal liking. It fails if techniques chosen by the rule do no better than a list of principles applied wholesale. Measures: decision quality against a criterion the parties set in advance; liking.
- **P2 (Staged seats).** Staging one determination at a time, with the producing seat labelled, makes a person's attribution of a result more stable across regenerated replies and more accurate than an explanation of the model. It fails if labelled staging is no more stable or accurate than explanation, or than no aid. Measures: agreement of attributions across regenerations; accuracy against the known source.
- **P3 (Key poses).** Letting a person fix a few binding commitments, with the intermediary's output between them shown as provisional, raises decision quality and the counterpart's ability to trace a result back to the person's intent, compared with free prompting. It fails if neither outcome improves. Measures: decision quality; whether the counterpart can state the intent behind the order.
- **P4 (Anticipated change).** A rule change cued before it lands and landed between decisions is detected more often, and with better-calibrated confidence, than a silent or mid-decision change. It fails if detection does not rise, or if the cue raises confidence without raising detection. Measures: detection rate; the match between confidence and accuracy.
- **P5 (Dissociation).** Craft spent on the character raises liking, attributed competence and confidence without raising decision quality; craft spent on the decision raises decision quality without that rise in confidence. It fails if character craft raises decision quality, or if decision craft raises confidence as much as character craft does.
- **P6 (Boundary).** The gains in P2–P4 are larger when the intermediary binds a counterpart than when it advises one person. It fails if the gains are the same with a dyadic advisor.
- **P7 (Designers).** Designers given the three competencies choose and place animation techniques that satisfy P1–P4 more often than designers given a list of principles.

P2–P4 restate, in craft terms, claims Hunt (2026b) made for structural interventions, and P6 restates his triadic penalty; the craft is what they add. P1, P5 and P7 are new. P5 has the most support so far, all of it from single users (Section 4.3). P4 has none yet: neither read test of an anticipatory cue found one that raised accuracy (Szafir et al., 2014; Takayama et al., 2011), so P4 bets on an explicit cue about the rule doing what motion cues did not.
[/DRAFTED]

## 7. Discussion

### 7.1 The surprise gag

[DRAFTED]
The craft can deceive, and its own literature says so. Chang and Ungar (1993) warned that anticipation can suggest one action and deliver another (p. 53). Tan et al. (2026) write that "deliberately manipulating response speed sits uneasily between positive friction and potential deception" (§5.5). Dragan et al. (2014) showed that the techniques that make a robot's intent readable can be inverted to mislead, and their model predicts that the misled will be confident. L. Stark (2024) and Maeda and L. Stark (2025) answer with governance and less animation. The placement rule is this paper's answer. A cue that says a rule will change, a label that says who produced a result, and a preview that can be cancelled are true statements about the coordination. A thinking indicator, a warm voice and a pause timed to suggest deliberation are statements about a character. The rule does not make the craft safe. An operator can mark a paid placement as a match, or cue only the changes it wants noticed. The model assumes that seat labels and cues are accurate; the accountability for that accuracy lies with the operator, not with the person deciding.
[/DRAFTED]

### 7.2 Where the analogy breaks

[DRAFTED]
An animated film has many hands and binds no one. Nothing a viewer does is evaluated, and no viewer's choice binds another; the triad belongs to the interface, not to the cartoon. A cartoon is passive and an interface interactive (Chang & Ungar, 1993), and an agent draws its in-betweens live, while a film is finished before anyone sees it. Lasseter's computer in-betweener, which overshoots between keys, is the nearest case in the craft, and puppetry, which animates live, may be closer still (Lewis et al., 2026). Lasseter (1987) also says the animator's first goal is to entertain. The goal of DXD is the person's decision, and the selection rule exists because the two goals differ.
[/DRAFTED]

### 7.3 Limits

[DRAFTED]
No study has tested the model. No instrument yet measures algorithmacy, and its three competencies are proposed, not validated, so the bridge between craft and interface is only as strong as that construct. The craft is read through Lasseter (1987), Chang and Ungar (1993) and Thomas and Calder (2001); Thomas and Johnston's (1981) book was not read, and the paper cites it only as others quote it. The search for prior work covered Consensus, arXiv, Crossref, Zenodo, OpenAlex and the web, with citation searches on Chang and Ungar, Thomas and Calder, Lasseter, Takayama et al., L. Stark and Pinhanez; searches of Scholar Gateway and Semantic Scholar failed (access denied; rate-limited) and should be rerun. The paper brackets agent experience, as the introduction does, and works one case.
[/DRAFTED] [VERIFY: Scholar Gateway and Semantic Scholar still failed on 2026-11-12 (library/GAP_CHECK_2.md, rerun section); rerun before submission.]

## 8. Conclusion

[DRAFTED]
The commuter ends with an umbrella and a purchase, and between them is an agent that ranked, chose and committed on behalf of the commuter and of the retailer. The introduction asked designers to learn the animator's methods. The model says which methods, and where: staging and labelled seats for what the commuter must interpret, key poses with provisional in-betweens for what the commuter must specify, and anticipated change between moves for what the commuter must track. None of them asks the commuter to read the algorithm. Section 6 says how to find out whether they work.
[/DRAFTED]

---

## Declaration of generative AI use

[DRAFTED] [DECISION: Roger's to write. TIES requires "a statement disclosing whether and how generative AI has been used in the research and manuscript preparation process" (venue/TIES.md). This draft, its library cards and its dossier were produced with Claude; the statement must say so.] [/DRAFTED]

## References

[DRAFTED — every entry is taken from the card named in brackets; entries for Roger's own works are from the files named.]

Ananny, M., & Crawford, K. (2018). Seeing without knowing: Limitations of the transparency ideal and its application to algorithmic accountability. *New Media & Society*, *20*(3), 973–989. https://doi.org/10.1177/1461444816676645 [ananny2018seeing; abstract only]

Bhat, M. (2025). How dynamic vs. static presentation shapes user perception and emotional connection to text-based AI. In *Proceedings of the 30th International Conference on Intelligent User Interfaces (IUI '25)* (pp. 846–860). ACM. https://doi.org/10.1145/3708359.3712131 [bhat2025dynamic]

Burrell, J. (2016). How the machine 'thinks': Understanding opacity in machine learning algorithms. *Big Data & Society*, *3*(1), Article 2053951715622512. https://doi.org/10.1177/2053951715622512 [pointer: monograph library burrell2016how; full text]

Chang, B.-W., & Ungar, D. (1993). Animation: From cartoons to the user interface. In *Proceedings of the 6th Annual ACM Symposium on User Interface Software and Technology* (pp. 45–55). ACM. https://doi.org/10.1145/168642.168647 [chang1993animation]

Chevalier, F., Henry Riche, N., Plaisant, C., Chalbi, A., & Hurter, C. (2016). Animations 25 years later: New roles and opportunities. In *Proceedings of the International Working Conference on Advanced Visual Interfaces (AVI '16)* (pp. 280–287). ACM. https://doi.org/10.1145/2909132.2909255 [chevalier2016animations]

DeVito, M. A. (2021). Adaptive folk theorization as a path to algorithmic literacy on changing platforms. *Proceedings of the ACM on Human-Computer Interaction*, *5*(CSCW2), Article 339, 1–38. https://doi.org/10.1145/3476080 [pointer: lima_pdw devito2021; extended preview]

Dragan, A., Holladay, R., & Srinivasa, S. (2014). An analysis of deceptive robot motion. In *Robotics: Science and Systems X*. https://doi.org/10.15607/rss.2014.x.010 [dragan2014analysis; locators are PDF pages]

Dragan, A. D., Lee, K. C. T., & Srinivasa, S. S. (2013). Legibility and predictability of robot motion. In *2013 8th ACM/IEEE International Conference on Human-Robot Interaction (HRI)* (pp. 301–308). IEEE. https://doi.org/10.1109/hri.2013.6483603 [dragan2013legibility; abstract only]

Dragicevic, P., Bezerianos, A., Javed, W., Elmqvist, N., & Fekete, J.-D. (2011). Temporal distortion for animated transitions. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '11)* (pp. 2009–2018). ACM. https://doi.org/10.1145/1978942.1979233 [dragicevic2011temporal]

Gonzalez, C. (1996). Does animation in user interfaces improve decision making? In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems: Common Ground (CHI '96)* (pp. 27–34). ACM Press. https://doi.org/10.1145/238386.238396 [gonzalez1996does]

Hoerl, C. (2015). Seeing motion and apparent motion. *European Journal of Philosophy*, *23*(3), 676–702. https://doi.org/10.1111/j.1468-0378.2012.00565.x [hoerl2015seeing]

Hunt, R. B., III. (2026a). *Algorithmacy: A competency for coordinative co-optation* [Paper presentation]. Organization Studies / Organization Theory Paper Development Workshop, Universidad de Piura, Lima, Peru. [lima_pdw/manuscript/PAPER.md; anonymise for review]

Hunt, R. B., III. (2026b, September 30). *Decision experience design* [Substack post]. https://rogerhuntphdcand.substack.com/p/decision-experience-design [decision_experience_design/published/; anonymise for review]

Hunt, R. B., III. (2026c). *Toward an account of algorithmacy: A triadic view of working through algorithms* [Manuscript in preparation]. [algorithmacy_ot/manuscript/sbs_schoeneborn2026/ASSEMBLED_2026-10-10.md, the author's introduction; anonymise for review]

Hunt, R. B., III. (2026d). *Spaces in the stream: Algorithmacy and the perception of decision spaces* [Manuscript in preparation]. [phd1750_spaces_in_stream; anonymise for review]

Johnson, E. J., Shu, S. B., Dellaert, B. G. C., Fox, C., Goldstein, D. G., Häubl, G., Larrick, R. P., Payne, J. W., Peters, E., Schkade, D., Wansink, B., & Weber, E. U. (2012). Beyond nudges: Tools of a choice architecture. *Marketing Letters*, *23*(2), 487–504. https://doi.org/10.1007/s11002-012-9186-1 [johnson2012beyond]

Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist*, *64*(6), 515–526. https://doi.org/10.1037/a0016755 [pointer: dxd_foundation kahneman2009conditions; full text]

Kurian, N. (2025). Once upon an AI: Six scaffolds for child-AI interaction design, inspired by Disney. *International Journal of Child-Computer Interaction*, *46*, Article 100788. https://doi.org/10.1016/j.ijcci.2025.100788 [kurian2025once]

Lasseter, J. (1987). Principles of traditional animation applied to 3D computer animation. In *Proceedings of the 14th Annual Conference on Computer Graphics and Interactive Techniques* (pp. 35–44). ACM. https://doi.org/10.1145/37401.37407 [lasseter1987principles]

Leveson, N. G. (2000). Intent specifications: An approach to building human-centered specifications. *IEEE Transactions on Software Engineering*, *26*(1), 15–35. https://doi.org/10.1109/32.825764 [leveson2000intent; abstract only]

Lewis, C., Collins, S., Hanson, A., Smith, J., & Williams, T. (2026). *Invisible strings: Deriving puppetry principles and their hidden connections to robot behavior design* (arXiv:2607.03289). arXiv. https://doi.org/10.48550/arxiv.2607.03289 [lewis2026invisible]

Maeda, T., & Stark, L. (2025). Anthropomorphism as social affordance: Charting the co-animation of chatbots into social "agents." *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, *8*(2), 1661–1673. https://doi.org/10.1609/aies.v8i2.36664 [maeda2025anthropomorphism]

May, J., Dean, M. P., & Barnard, P. J. (2003). Using film cutting techniques in interface design. *Human–Computer Interaction*, *18*(4), 325–372. https://doi.org/10.1207/s15327051hci1804_1 [may2003using]

McLaren, N. (1968). [FLAG F1: no source found for a 1968 publication; Pass 2 cites it. The earliest traced printing is in Sifianos (1995), not held.]

Pinhanez, C. S. (2017). Design methods for personified interfaces. In *Proceedings of the International Conference on Computer-Human Interaction Research and Applications (CHIRA 2017)* (pp. 27–38). SciTePress. https://doi.org/10.5220/0006487500270038 [pinhanez2017design]

Schulz, T., Torresen, J., & Herstad, J. (2019). Animation techniques in human-robot interaction user studies: A systematic literature review. *ACM Transactions on Human-Robot Interaction*, *8*(2), Article 12, 1–22. https://doi.org/10.1145/3317325 [schulz2019animation]

Silvio, T. J. (2019). *Puppets, gods, and brands: Theorizing the age of animation from Taiwan*. University of Hawaii Press. https://doi.org/10.1515/9780824880989 [silvio2019puppets; metadata only]

Stark, D., & Vanden Broeck, P. (2024). Principles of algorithmic management. *Organization Theory*, *5*(2), Article 26317877241257213. https://doi.org/10.1177/26317877241257213 [pointer: monograph library stark2024principles; full text]

Stark, L. (2024). Animation and artificial intelligence. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1663–1671). ACM. https://doi.org/10.1145/3630106.3658995 [stark2024animation]

Szafir, D., Mutlu, B., & Fong, T. (2014). Communication of intent in assistive free flyers. In *Proceedings of the 2014 ACM/IEEE International Conference on Human-Robot Interaction (HRI '14)* (pp. 358–365). ACM. https://doi.org/10.1145/2559636.2559672 [szafir2014communication]

Takayama, L., Dooley, D., & Ju, W. (2011). Expressing thought: Improving robot readability with animation principles. In *Proceedings of the 6th International Conference on Human-Robot Interaction (HRI '11)* (pp. 69–76). ACM. https://doi.org/10.1145/1957656.1957674 [takayama2011expressing]

Tan, F. F.-Y., Messerschmidt, M. A., Yin, W., & Nov, O. (2026). The impact of response latency and task type on human-LLM interaction and perception. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26)* (pp. 1–17). ACM. https://doi.org/10.1145/3772318.3790716 [tan2026impact; locators are the arXiv v1 copy's]

Thomas, B. H., & Calder, P. (2001). Applying cartoon animation techniques to graphical user interfaces. *ACM Transactions on Computer-Human Interaction*, *8*(3), 198–222. https://doi.org/10.1145/502907.502909 [thomas2001applying]

Thomas, F., & Johnston, O. (1981). *Disney animation: The illusion of life*. Abbeville Press. [thomas1981illusion; metadata only; 1981 Abbeville edition, 575 pp., confirmed by Open Library edition OL4266737M (sibling library record); the book is not read]

Vaithilingam, P., Kim, M., Acosta-Parenteau, F.-C., Lee, D., Mhedhbi, A., Glassman, E. L., & Arawjo, I. (2025). *Semantic Commit: Helping users update intent specifications for AI memory at scale* (arXiv:2504.09283). arXiv. [vaithilingam2025semantic; abstract only]

Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital nudging. *Business & Information Systems Engineering*, *58*(6), 433–436. https://doi.org/10.1007/s12599-016-0453-1 [weinmann2016digital]

Wu, J., & Masson, D. (2026). *AInimation: Animating from prompt to AI-generated responses* (arXiv:2607.18507). arXiv. https://doi.org/10.48550/arxiv.2607.18507 [wu2026ainimation]

Zhang, C., & Davis, A. (2026). Narrative keyframing for generative creative writing. In *Proceedings of the 39th Annual ACM Symposium on User Interface Software and Technology (UIST '26)* (pp. 1–19). ACM. https://doi.org/10.1145/3830398.3830586 [zhang2026narrative]
[/DRAFTED]
