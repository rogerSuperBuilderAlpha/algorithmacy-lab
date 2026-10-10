<!--
  FULL DRAFT — written by Claude on the author's instruction of 2026-10-07 ("draft the whole paper").
  This is NOT the author's text. The author's text is PAPER.md, untouched.

  Every paragraph carries a tag:
    [A]   the author's prose, copied verbatim by script from the frozen Lima paper
          (lima_pdw/archive/2026-09-10_PAPER_submitted.md); the line number follows.
    [A*]  the author's prose, edited: trimmed, joined, or corrected against a source. What changed is
          listed in DRAFT_NOTES_2026-10-07.md.
    [C]   drafted by Claude.
  Strip the tags for a clean copy:  sed -E 's/^\[(A|A\*|C)[^]]*\] //' DRAFT_2026-10-07_claude.md
-->

# [C] Algorithmacy: Coordinating With Others Through an Intermediary That Binds

## Abstract

[C] Organization theory has shown that platforms coordinate by co-opting the people who use them, and that algorithmic and generative systems are remaking organizing from inside the work. It has not yet said what a person must be able to do when her coordination with another person runs through such a system. I argue that the accounts a reader would reach for each see two of the three parties: the person and the machine, or the two people and a channel. I develop algorithmacy as the missing construct — the sensibility required to interpret an opaque, adaptive intermediary that evaluates and binds both parties and the counterpart reached through it, to specify intent through the channels that intermediary permits, and to track its rule as that rule shifts. I call the arrangement that demands it coordinative co-optation, building on Stark and Vanden Broeck (2024), and I derive the three operations from three properties of the intermediary: opacity, bindingness and adaptivity. Each property withholds something, each operation supplies it, and none of the three works without the other two. The construct moves research on algorithmic management from the mechanisms of control to the mechanics of execution, and it raises a paradox: individual mastery of the arrangement stabilizes the arrangement that burdens individuals. Three propositions state what follows for outcomes, for inequality among participants a platform treats as equivalent, and for transparency as an alternative to capacity.

[C] *Keywords:* algorithmacy; algorithmic management; coordination; co-optation; platforms; triad; generative AI; literacy

## Introduction

[A*] Organizations fail to adopt and understand the tsunami of new platforms and services enabled by generative AI. While global leaders promote these technologies, less visible displacements of institutional values, norms, and rules are also reconfiguring how organizations perform (Orlikowski & Scott, 2023). Focusing on those less visible shifts allows us to recognize how generative AI sits inside the work and reshapes it, functioning more as—but not quite—a "counterpart" in a system of work that includes its design, implementation, and use (Anthony et al., 2023). Hoping to install a plug-and-play intelligence ignores that organizing now depends on relations among human and algorithmic actors (Stelmaszak et al., 2026), relations in which generative AI may expand the black box and reduce visibility and control (Hinds & von Krogh, 2024) while its detailed outputs give those who are shown them an illusion that uncertain outcomes are knowable (Leonardi & Leavell, 2026). While the academic debate has clearly moved past the surface of "tooling," it still leaves open how someone coordinates through a co-optive, opaque, adaptive intermediary.

[A*] If it were only a matter of how, this proposal would be less interesting. The how I propose also requires that we refactor the why.

[A*] Organizations have been doing the equivalent of giving books to people who lack literacy. We heap algorithmic management systems on people who lack algorithmacy, or the sensibility to navigate opaque triadic coordinative co-optation. The intermediaries in question are not neutral software. The platforms behind them hold collective actorhood by degree, and they work to downplay it (Schoeneborn et al., 2026); on them, as Stark and Vanden Broeck (2024, p. 5) put it, actors "are co-opted"—enrolled, evaluated, and bound. Building on the OT/OS discussion and exploring other popular models including Human-Machine Communication and AI Literacy, I argue that we are strapping ourselves to the mast of a "literacy"-based understanding. We do this by either setting aside the third actor, treating the mediator as a passive channel, or reducing the triad to pairs, which leaves us blind to its emergent, binding power.

[A*] Oracy—the term is Wilkinson's (1965)—is the sensibility to navigate direct dyadic forms through speaking and hearing (or feeling and tapping). Literacy is the sensibility necessary for the competency to read and write texts that moderate chained or linked dyads. Algorithmacy is the sensibility to navigate irreducible triads. Porsfelt et al. (2026, p. 1) propose treating imagination as "a situated engagement with the non-present"; algorithmacy can be seen as a situated engagement with what is present and unseen. As a sensibility like literacy and oracy, it operates through the competencies and capacities to: 1) interpret, from an otherwise innocuous output, both the intermediary's rule and a counterpart's intentions; 2) specify intent so meaning survives the opaque, adaptive mediator; and 3) keep track as governance radically, repeatedly, and suddenly shifts. We cannot read our way out of or into this, just as we cannot—or should not—listen to a book.

[C] My approach is theoretical critique followed by construct development, and it ends in three propositions. I first show that existing accounts each see two of the three parties. I then define the arrangement and the construct, and spend the largest part of the article on the mechanics—how each of the three operations answers one property of the intermediary, and why the three depend on one another. The discussion returns to the *why*.

## The Triadic Blind Spot

[A*] Recent work in *Organization Theory* has shown how digitalization displaces established institutional apparatuses in ways that are easy to miss (Orlikowski & Scott, 2023), and how platforms introduce a form of governance the classical archetypes do not describe. Stark and Vanden Broeck (2024, p. 5) state the departure in one line: "whereas actors in hierarchies command, in markets they contract, and in networks collaborate, on platforms they are co-opted." Yet while organization theory has mapped this shift in structural control, its models of how individuals carry out work within these systems keep returning to pairs.

[C] The most advanced relational account shows how near the field has come and where it stops. Stelmaszak et al. (2026, p. 337) relocate AI from the algorithm to "multiple, complex, and multifaceted relations among human and algorithmic actors," and their own example has three kinds of party. The Uber system "includes the drivers (human actors), the riders (human actors), and the platform (algorithmic actors)" (p. 346). The riders are counted. What the account does not theorize is the tie between rider and driver. Every relation it develops runs between a human and an algorithm, so the algorithm never stands as a third between two people. The capability that results belongs to the organization, since "such intelligence is not merely a human trait or skill" (p. 346). The authors note in passing that drivers "learn how to change their behaviours" (p. 350). They do not say what that learning consists of. Hinds and von Krogh (2024, p. 4) reach the same edge from generative AI. When managers use it to evaluate employees, they write, cascades run "between managers, GenAI, and employees," and the system "may ultimately obscure managers' and employees' visibility into the basis on which the AI is making decisions." Both accounts have the three parties in view. Neither asks what the person in the middle of them must be able to do.

[A*] I therefore read each candidate construct for one thing first: the position it assigns the computational intermediary, and where that leaves the human counterpart on the far side of the interaction.

[A] (41) That question carries a classical warrant the comparison would otherwise leave implicit. Simmel (1902) argued that moving from two parties to three changes the sociological form rather than the population: a dyad ends when either member withdraws, while a triad supports positions no dyad can hold — the impartial mediator who reconciles, the *tertius gaudens* who profits from the other two's opposition, and the third who manufactures that opposition in order to profit from it. In each case the relation between the other two is no longer immediate; it is routed, and the router has interests of its own (Simmel, 1950). Which position the third occupies is therefore what determines what the first two can do with each other, and the status a construct accords the intermediary is not a descriptive detail but the thing that fixes the arrangement's form.

[A*] Eight constructs from organization theory, communication studies, and human–computer interaction can be sorted by that status, and they fall into three families. Table 1 sets them side by side.

### The machine as the other party

[A*] Human–machine communication has moved the machine furthest toward the position of a party. Guzman and Lewis (2020) argue that communicative artificial intelligence systems operate as "communicative subjects, instead of mere interactive objects" (p. 71). The relocation is one seat vacated and another taken within a two-position model (Guzman, 2018). An individual may achieve comprehensive mastery within human–machine communication—decoding the system's cues, sustaining rapport with it—and still lack the sensibility required to coordinate interdependent labor through a system that evaluates and binds both parties. AI literacy treats the algorithm as an object of knowledge and reaches the same boundary. Long and Magerko (2020) derive seventeen competencies, and no competency in the seventeen names another person as a party to the interaction; the humans that appear are upstream designers or a comparison baseline.

### The machine as channel or delegate

[A*] A second family keeps both people and thins the machine. Spitzberg's (2006) model of computer-mediated communication competence carries the architecture of interpersonal competence into digital settings intact: the medium enters as a set of parameters conditioning a dyadic exchange, never as a party to it. Walther (1992, 1996) shows communicators learning to convey through a narrow channel what the channel was thought unable to carry, and his adaptation works because the party who receives the message is the party who evaluates it and replies. In the triad, the party that evaluates is not the party whose understanding matters. Walther's communicator adapts to a channel. The triad's participant answers to one. Hancock et al. (2020) restore a computational agent between two people, and confine it to operating "on behalf of a communicator" (p. 90). AI-mediated communication governs symbolic messages, whereas algorithmacy governs binding institutional verdicts. An editor is not a judge.

### The worker facing the system

[A*] The third family comes nearest, because it studies the people platforms co-opt. Zhou, Lei, Liu, et al. (2025) validate a twelve-item scale of algorithmic competency, defined as workers' "understanding of platform algorithms that assign and evaluate their work and their ability to adapt to and navigate those algorithms" (p. 2). The customer appears in it as a source of ratings; every validated dimension is anchored in the worker–platform dyad. Rahman's (2021) "invisible cage" documents the counterpart and leaves her outside the construct: he interviewed 18 clients alongside 80 freelancers (p. 956), and the one adaptation in which his freelancers direct action toward a client is to move the relationship off the platform. Reaching the counterpart requires exiting the apparatus. Sutherland et al. (2020) find the same exit in gig literacies, where rapport is an instrument of disintermediation—a way of extracting the collaboration from the system and restoring a channel in which scoring no longer applies.

**Table 1.** Eight candidate constructs, by the status each accords the algorithm and the human counterpart.

| Construct | Status of the algorithm | Status of the human counterpart |
| :-- | :-- | :-- |
| Human–machine communication (Guzman & Lewis, 2020) | Autonomous communicative partner | Absent; the machine occupies the interlocutor seat |
| AI literacy (Long & Magerko, 2020) | Object of technical and conceptual knowledge | Absent; appears only as an upstream system designer |
| Computer-mediated communication competence (Spitzberg, 2006) | Transmission medium | Present; directly evaluates communicative messages |
| Social information processing and the hyperpersonal model (Walther, 1992, 1996) | Channel whose constraints communicators learn to exceed | Present; receives, evaluates, and replies |
| AI-mediated communication (Hancock et al., 2020) | Delegate acting on one party's behalf | Present; receives a computationally modified message |
| Algorithmic competency (Zhou, Lei, Liu, et al., 2025) | Object of strategic navigation and compliance | Present only as a downstream rating source |
| Reactivity under opaque evaluation (Rahman, 2021) | Object of worker interpretation | Documented in the field site, omitted from the construct |
| Gig literacies (Sutherland et al., 2020) | Infrastructure to circumvent or escape | Present; reached by leaving the system |
| Algorithmacy (this article) | Opaque, adaptive system that evaluates and binds both | Active party reached through the intermediary |

### What the three families share

[A*] One limitation runs through all eight: no extant framework theorizes an active human counterpart and an opaque, consequential intermediary that evaluates and binds both parties. The vacancy does not stem from omitting the second human actor, since AI-mediated communication, social information processing, algorithmic competency, and gig literacies each incorporate a counterpart. The limitation lies in how each framework couples the intermediary to the counterpart. Where a framework admits a human counterpart, it reduces the computational system to a passive conduit, a channel learned and exceeded, a partisan delegate, or an obstacle to circumvent, never an authority rendering binding determinations. Where a framework models the intermediary as opaque and binding, it demotes the counterpart to an exogenous rating source or an outcome variable, never an interdependent actor with whom the focal participant coordinates.

[A*] The triad itself is not new to the field. Curchod et al. (2020) describe an asymmetrical triad sustained by a visibility gap, and Cameron (2024) an "algorithmic labor triangle"; online dispute resolution theorized the infrastructure as an active "fourth party" two decades ago (Katsh & Rifkin, 2001). These accounts explain what the triad is and how platforms enforce discipline within it. They describe the structure from the platform's side, as an institutional design choice, and none asks what capacity the enrolled participant needs to coordinate with the human counterpart the structure still leaves on the other end of the exchange. Fieldwork has already watched that capacity at work. Manky (2025) shows ride-hailing drivers in Lima reading opaque platform metrics to infer whether a passenger is safe to accept. The claim I defend is accordingly narrow: no construct models the individual capacity to coordinate interdependent joint work with a human counterpart through an intermediary that evaluates and binds both parties. The next section builds one.

## Algorithmacy and Coordinative Co-optation

[A] (15) A student submits her code for review. Her classmates read it, comment on it, and vote, all in public where she can watch. An algorithm none of them can inspect then weighs those inputs by a concealed formula and returns a verdict: pass or fail. Her instructor holds no vote and cannot override the outcome, and the weights themselves are retuned as the term runs. To get through, she must coordinate with people she can see through a rule she cannot — reading the verdict for what her peers meant, writing an explanation that a test suite will parse and a person will still understand, and noticing when the hidden rule has moved.

[C] I return to this student throughout. Her situation is small, and its shape is the one the platform literature describes at scale: unchosen parties, a rule none of them can read, and a verdict that binds them all.

### The arrangement

[A*] Mature organization theory defines a coordination form by specifying both its primary operational mechanism and the formal standing of the participants it governs. In a hierarchy, an employee operates within an authority-governed zone of acceptance (Simon, 1997; Weber, 1978). In a market, an autonomous transacting party evaluates a posted price backed by an unrestricted right of refusal (Hayek, 1945). In a network, a partner invests in an elective, revocable relationship grounded in reciprocity and reputation (Granovetter, 1985; Powell, 1990). Platforms break the pairing of mechanism and standing. They deploy algorithms to match unchosen parties, evaluate their ongoing interactions, and unilaterally terminate accounts (Stark & Pais, 2020).

[A*] I call this arrangement *coordinative co-optation*, building the compound term on the mechanism Stark and Vanden Broeck (2024) themselves identify—"on platforms they are co-opted" (p. 5)—and a reader's intuition for co-optation will misfire without a gloss. In Selznick's (1949) classical sense, an organization absorbs an external challenger by conferring a seat on him: opposition becomes participation, and the seat carries a formal standing. The platform confers nothing of the kind. It does not hire you, buy from you, or befriend you—it enrolls you, on terms it sets, scores, and can revoke. Selznick's absorbed challenger at least received a seat; the enrolled participant receives a queue position.

[A*] Three terms carry the structure: opacity, adaptivity, and bindingness. Opacity means the participant cannot observe the governing rule directly; adaptivity means the rule itself moves over time; bindingness means the intermediary's determination binds both the focal actor and her human counterpart at once—the property that seats the other two in a single arrangement, the algorithmic system standing between the focal actor and her counterpart.

[A*] Among the third positions a triad supports, the platform occupies the one Simmel (1950) calls the arbitrator—the third who does not reconcile two parties' positions but decides between them—with one decisive difference. Simmel's arbitrator holds an authority the two parties conferred on him and can withdraw; the platform holds an authority neither party conferred, and the only withdrawal on offer is exit.

[C] The platform's third position has a second peculiarity, and Schoeneborn et al. (2026) supply the terms for it. On their account a collective holds actorhood by degree, as others attribute agency to it or decline to, and digital platforms "rather strategically downplay their collective actorhood status to avoid accountability" (p. 13). The arbitrator in this triad therefore decides between two parties while presenting itself as no party at all—as infrastructure, a marketplace, a tool. The participant must coordinate through a third that binds her and disclaims having done so.

### The construct

[A] (151, first sentence) Algorithmacy names the sensibility required to interpret an opaque, adaptive intermediary that evaluates and binds both parties and the counterpart reached through it, to specify intent through the channels that intermediary permits, and to track its rule as that rule shifts.

[C] The definition has a genus and three operations, and the two should be kept apart. A sensibility, as I use the word, is a standing orientation toward a kind of situation—a readiness to perceive what the situation contains and to treat it as calling for a response. The literate person does not decide, each time, to treat marks on a page as text. A person with algorithmacy treats a verdict as something authored by a rule and by other people together, and treats her own next act as addressed to both. The three operations are the competencies through which that orientation works. I say sensibility for the whole because the operations can each be performed without it. A participant can decode a platform's rule with great skill and never register that a person stood on the other side of the score.

[A*] Algorithmacy is in this sense an individual competency rather than an isolable skill or a firm-level capability. A skill is a procedural routine that can be codified and transmitted through instruction, and the rules of opaque systems remain proprietary and dynamic. A capability resides in routines and assets a firm owns and deploys (Teece et al., 1997), and the firm alone owns the matching algorithms and rating systems. Sandberg (2000), examining engine optimizers at Volvo, demonstrated that competence reflects an actor's qualitative conception of work rather than an inventory of attributes; that finding is what algorithmacy extends to mediated triadic coordination.

[A*] I build algorithmacy as a micro-foundational construct, which requires decoupling an actor's behavioral capacity from her formal institutional standing. Whether an enrolled participant holds the protections of an employee, the exit rights of a market buyer, or the hearing rights of a co-opted stakeholder is a question of governance, and algorithmacy operates independently of how it is resolved, because the operations derive from opacity, adaptivity, and bindingness—properties of the arrangement, not of participant status. A hearing right that leaves the rule undisclosed alters standing without relieving the deficits that demand the capacity. Locating algorithmacy within the individual does not make it individualist: the construct is a micro-foundation with social antecedents (Felin et al., 2015), acquired through peer networks and enacted individually.

[A*] Those same properties fix the scope conditions, and arrangements fall along a continuum according to how strictly they govern rather than switching on or off. Algorithmacy applies where a computational intermediary is opaque, adaptive, and mutually binding, and where the two parties' work is interdependent with the intermediary as the sole channel through which one party's evaluation reaches the other in a form that carries consequence; it ceases to operate under static administrative rules or in open markets where parties negotiate directly. This last condition is what keeps a visible exchange—a public comment, a vote—from disqualifying the arrangement: what must run through the intermediary alone is not the exchange but its consequence, the weight assigned to what was exchanged. Online freelance platforms occupy a hybrid boundary, because participants can negotiate terms or migrate off-platform (Sutherland et al., 2020); dispatch networks, piecework queues, and peer-evaluation systems that conceal scoring rules sit at the core. The conditions pick out configurations of coordination, not industrial sectors.

[C] The two halves of the definition exclude different things. A matchmaking platform that pairs two people and lets them negotiate the rest supplies joint work without a binding verdict. An algorithm that scores a family and binds a caseworker's decision supplies a binding verdict without joint work between the two who are scored. Algorithmacy is the capacity called for when both are present, and the next section shows what it consists of.

## The Mechanics of Algorithmacy

[A] (159) Organization theory has a name for what the participant is short of, and it is not information. Daft and Lengel (1986) separate *uncertainty*, the absence of data, from *equivocality*, the presence of several incompatible readings of the data one already holds, and only the second calls for a rich, feedback-bearing channel. The participant at an opaque gate has ratings, outcomes, and a rejection history; what she lacks is any way to settle which reading is right, and the channel that could settle it is fixed and is also the judge.

[A] (161) Each structural property of the triad imposes one informational deficit, and each deficit demands one operation. Opacity withholds the rule, so the actor must reconstruct it. Bindingness turns every message into evidence before a verdict, so the actor must encode for judge and counterpart at once. Adaptivity unsettles whatever the actor has learned, so the reconstruction has to be maintained rather than achieved once. Three properties, three deficits, three operations:

**Table 2.** From the properties of the intermediary to the operations of algorithmacy.

| Property of the intermediary | What it withholds | Operation it demands | How the operation fails |
| :-- | :-- | :-- | :-- |
| Opacity | The rule, and whose input moved the verdict | Interpreting | A reading of the machine alone, or of the people alone |
| Bindingness | A channel that is not also the judge | Specifying intent | A message the rule can parse and the counterpart cannot use, or the reverse |
| Adaptivity | A rule that stays learned | Keeping track | A working theory that was right last month |

### Interpreting

[A] (163) **Interpreting:** Reconstructing, from ambiguous and fragmented system feedback, the underlying actions, constraints, and intentions of both the algorithmic intermediary and the human counterpart whose evaluation the actor cannot read — was the failed verdict a peer's downvote, or a shifted threshold?

[C] Opacity is usually described as a missing rule. For the participant it is more exactly a missing attribution. The student holds a failed verdict, three comments, and a vote tally she can see. She does not hold the weights, so she cannot tell whether her reviewers disliked the work or liked it and were outvoted by a threshold that moved.

[A*] *Interpreting* requires the intermediary and the counterpart at once: the student at the gate cannot ask the gate what it wanted or ask her reviewers what they meant; she has one signal from which to infer two minds. Communication research has known since Sundar and Nass (2000) that this attribution is supplied by the user and not settled by the interface. Their participants received identical evaluations from a terminal labeled a computer or labeled a person and rated the identical content differently; the authors call the variable *source orientation*—the user's working answer to the question of who is speaking. An actor reading an unexplained outcome at a gate is deciding whether what arrived came from a peer, from a rule, or from the two together, and *interpreting* names the capacity to do it under conditions where no cover story fixes the answer.

[A*] The platform literature shows the same problem and treats it as a property of the metric. In Rahman's (2021) account a freelancer confronted with a score drop cannot discern whether it stems from client dissatisfaction or an unannounced recalibration, and that uncertainty is an epistemic problem about the score. Algorithmacy addresses a different problem: deciphering the expectations of a human counterpart through an opaque intermediary. Manky's (2025) drivers work on that second problem directly when they read platform metrics for what they reveal about the passenger and not about the platform.

[C] The operation fails in two directions, and they mirror the two families of the previous section. A participant who reads only the machine arrives at a theory of the rule and treats her reviewers as noise in it. A participant who reads only the people takes the verdict as their opinion of her, and misses that a formula stood between their opinions and the result. Each reading is coherent. Each discards half of the one signal she has.

### Specifying intent

[A] (164) **Specifying intent:** Structuring and encoding communicative action so that intended meaning survives the narrow, standardized signaling channels the intermediary permits, and reaches the counterpart intact — a pull-request description written so the test suite parses it *and* the peer understands why the change matters, though neither the actor nor the peer can read what weight that understanding carries in the verdict.

[C] Bindingness changes what a message is. In an unmediated exchange the student's explanation is addressed to her reviewer, and its success is the reviewer's understanding. At the gate the same explanation is also an input to a verdict. The channel she writes in is the instrument that judges her, and it judges the reviewer too, whose own standing depends on how the reviewer's assessment squares with the outcome.

[A*] *Specifying intent* therefore works through dual-audience encoding, since a single act must satisfy the intermediary's parsing rules and the counterpart's expectations concurrently. Walther's (1992, 1996) adaptation thesis is the closest thing in the literature to this operation, argued three decades early: his communicators develop, through experience and without instruction, the capacity to convey what a narrow channel was thought unable to carry. The difference sits in the loop's closing condition. The sender in Walther's account learns what carries because the receiver responds, and every adjustment is calibrated against feedback from the addressee herself. At the gate the counterpart replies—her comment is visible, her vote registers—but the intermediary is what issues the assessment, and it returns nothing resembling a reply to either of them. The student can write her pull-request description a hundred ways, and what the failed verdict tells her is that this one did not clear. Which of her two readers the sentence lost, and where, is not in the signal.

[A*] Grounding theory states why the mutual calibration is unavailable rather than merely difficult (Clark & Brennan, 1991): the reviewer's comment is visible and her vote is a next turn, but what the intermediary withholds is the weight her evaluation carries in the verdict it returns. Spitzberg's (2006) criteria survive the move with new referents. An act is effective when it survives the gate *and* the counterpart decodes the meaning the actor intended. An act is appropriate when it fits the counterpart's expectations as the actor has reconstructed them under opacity, which is what *interpreting* produces.

[C] The characteristic failure is a message built for one audience. A participant can route her explanation through a language model tuned for machine parsability, clear the gate, and never address the peer at all. The result is machine-legible and peer-illegible. The opposite failure is the warm, clear note to a colleague that the parser cannot score. Generative tools make the first failure cheap, which is one reason the operation matters more as those tools spread. Hinds and von Krogh (2024) expect such systems to "minimize the relations between team members" (p. 7). A participant who optimizes only for the gate does that minimizing herself.

### Keeping track

[A] (165) **Keeping track:** Detecting temporal shifts, continuous drift, and unannounced recalibrations in the rules that govern and bind both interactants — the commit style that cleared the gate in week four now draws review comments, and nothing was announced.

[C] Adaptivity means that the first two operations never finish. Whatever the student has inferred about the rule and about her reviewers was inferred from past verdicts, and the weights are retuned as the term runs. Hinds and von Krogh (2024, p. 4) mark the same shift for generative systems, whose functions and relations, "rather than being fixed," are "likely to evolve and expand as the AI learns."

[A*] *Keeping track* requires the triad through an evidentiary mechanism: under opacity, rule shifts register through altered counterpart behavior and systematic variation in peer ratings, so an actor who monitors only platform telemetry misses the recalibration entirely. Duran (1983) named the nearest antecedent, communicative adaptability, but his communicator reads a partner and a setting she can see; the triad's actor reads outcomes from a rule that announces nothing, which is why noticing is part of the operation rather than a precondition for it. DeVito (2021) comes closer still. Her *adaptive folk theorization* names users detecting when a feed algorithm's rules have shifted, and shows the capacity acquired through participation and sometimes taught outright. What her design does not include is a counterpart whose intentions must be reconstructed, an intermediary that binds both sides of the exchange, and work the two of them execute together rather than a feed one person manages alone. *Keeping track* has no equivalent in traditional literacy frameworks, because conventional media hold still and this rule does not.

[C] The failure here is a stale theory held with confidence. Rahman (2021) shows where it leads: freelancers who cannot tell what changed either experiment at a cost to their scores or restrict their activity to protect them. A participant who keeps track separates two questions those responses run together—whether the rule moved, and whether the people did.

### The loop

[A*] The three operations function as a recursively linked process, not an inventory of discrete traits: a coordination incident begins with *interpreting* an ambiguous outcome, that reading informs *specifying intent* in the actor's next act, and *keeping track* then evaluates whether the rules have shifted, generating updated priors that feed back into *interpreting* for the next one. Without a grounding loop to join them, inbound and outbound understanding become two unaided inferences rather than two halves of one process (Clark & Brennan, 1991), which is why the model splits *interpreting* from *specifying intent* and then ties them together again.

[C] The dependence can be stated by removal. Take away specifying intent and interpreting becomes a private diagnosis. The student knows why she failed, and nothing she writes next reflects it. Take away interpreting and specifying intent becomes formatting, since she has no reading of either audience to encode for. Take away keeping track and the other two run on a theory of the gate that has quietly expired, and the better she was at them the longer she will defend it. Each operation supplies what another consumes. This is the sense in which the triad is irreducible for the person inside it: no pair of the three parties can be handled and the third added afterward, because the signal she reads, the message she sends, and the rule she follows are each produced by all three together.

[C] **Figure 1.** *Algorithmacy as a recursive coordination process.* [To be drawn: the three operations in a cycle, each labeled with the property that demands it and the deficit it answers, around a triad of actor, counterpart, and intermediary.]

[C] The loop also explains why algorithmacy is acquired the way it is. Jablin and Sias (2001) describe newcomers acquiring communicative competence through participation, inferring what counts as competent from how others respond to them. The participant in the triad learns the same way, except that she reads an outcome from a rule and never a response from the counterpart she is trying to reach. Because operators withhold the decision rules, instruction cannot substitute for that participation. The capacity grows by going round the loop, and whoever has gone round it more often, or with better company, holds more of it.

## Discussion

[C] I began with a debate about why organizations fail to absorb algorithmic and generative systems, and with a promise to refactor the *why*. The construct now permits it.

### From control to execution

[A] (189) Formalizing algorithmacy reorients organizational research on algorithmic management from mechanisms of control to the mechanics of execution. Where labor process theorists conceptualize algorithmic workplaces as contested terrain centered on direction, evaluation, and discipline (Kellogg et al., 2020), algorithmacy isolates the competencies required to coordinate through those constraints. The distinction locates interventions: transparency mandates modify the information environment, whereas cultivating algorithmacy enhances an actor's capacity to act within it whatever its transparency. Online dispute resolution names what the arrangement withholds — transparency, accountability, and informed participation (Wing, 2016) — and algorithmic regimes forfeit each while directing contestation to the platform's own apparatus rather than to the counterpart (Curchod et al., 2020; Katsh & Rabinovich-Einy, 2017). The three operations are the individual-level capacities participants must mobilize because those protections are absent.

### The relational view, from the other side

[C] The relational accounts of AI in organization theory locate capability between humans and algorithms, and they are right to. Stelmaszak et al. (2026) hold that the capability is organizational and Hinds and von Krogh (2024) that generative AI encapsulates more and more of the relations it rests on. Algorithmacy is the view of the same relations from inside one of them. A capability with no individual bearer cannot say why two drivers on one platform in one week fare differently, and encapsulation described from the system's side cannot say what a person does when the relation to her colleague has been encapsulated and the colleague is still there. The construct names what the drivers in Stelmaszak et al.'s example are learning when they "learn how to change their behaviours" (p. 350).

[C] Leonardi and Leavell (2026) show what turns on that learning. In their comparison of two planning organizations using the same AI simulation, the experts are the intermediaries, and where they amplified the tool the model became "the primary arbiter of planning decisions" (p. 533) and stakeholders "treated the outputs as binding forecasts" (p. 537). The interpretive capacity the authors describe—"selecting, sequencing, qualifying, and presenting information so that others can act under uncertainty" (p. 518)—belongs to the expert. Their study says nothing about what the lay party must be able to do, and in coordinative co-optation there is no expert standing between the participant and the system. Algorithmacy is the interpretive work that falls to the person when no one is employed to do it for her.

### The why

[C] The usual account of failed adoption is a deficit on the organization's side: the wrong tool, a poor rollout, too little training in the tool. If the argument here holds, the deficit is of a different kind. An algorithmic system that evaluates and binds changes the form of coordination among the people it touches, and the people are then asked to coordinate in the new form with the sensibility of the old one—to read a verdict as if a colleague had written it, or to write to a colleague as if no verdict were listening. Training in the tool does not reach this, in the way that teaching the alphabet does not reach a person who has never met the idea that marks can stand for speech. The *why* of failed adoption is then less a failure to learn a technology than a change of form that went unnamed.

### A paradox the construct raises rather than resolves

[A*] The paradox is this: individual mastery of the arrangement stabilizes the arrangement that burdens individuals. Capacity and fairness vary independently, so higher competency does not signal greater welfare or legitimacy. Elish's (2019) hazard applies to the construct and not only to the arrangement it describes: a framing that reads variance in outcomes off variance in worker capacity is itself, structurally, a crumple-zone move, and holding capacity and fairness apart is what keeps the construct from re-billing a system's opacity as an individual's deficit. The decoupling also yields an aggregation mechanism: where Cameron (2024) shows workers manufacturing consent through confined choices, an enrolled population's collective competency determines whether frictions trigger visible breakdown or get quietly absorbed (Felin et al., 2015).

[A] (195) Three propositions follow from this tension.

[A] (197) **Proposition 1.** *Higher algorithmacy improves an individual participant's coordination outcomes while leaving the arrangement's procedural justice unchanged; performance gains concentrate in private navigation rather than in institutional disclosures won, formal appeals granted, or rules rendered legible to peers.* It extends to a formalized competency what Rahman (2021) and Sutherland et al. (2020) document for reactivity and informal literacies.

[A] (199) **Proposition 2.** *Because algorithmacy is distributed unevenly across participants whom the platform treats as formally equivalent, that variance introduces a secondary axis of inequality among actors whom the organizational form designates as interchangeable.* It transposes the logic of second-level digital divides (Hargittai, 2002) to triadic coordination.

[A] (201) **Proposition 3.** *Increasing an intermediary's transparency reduces the algorithmacy needed to coordinate through it, establishing the construct's scope conditions as a malleable institutional lever rather than a fixed analytical perimeter.* Disclosure policy is therefore an alternative governance pathway to compensatory competency.

### Boundaries and further work

[A*] Whether the three operations are empirically distinct, whether they separate cleanly from general software literacy and traditional communicative competence, and whether evaluative attribution—deciding whether the platform or the human client drove a score change (Rahman, 2021)—stands as a fourth operation are open questions that measurement must resolve; I house attribution provisionally within *interpreting*. The strongest rival explanation is Rahman's own: if platform dependence and prior evaluation shocks explain the variance in coordination outcomes, algorithmacy explains nothing a labor-process account has not already explained better. Only a design that measures both, in the same participants, can settle that. Advisory decision aids, dyadic software tools, and unmediated peer collaboration fall outside the construct for a common reason: each is missing at least one leg of the triad.

## Conclusion

[A*] Algorithmacy isolates the capacity an individual needs inside the triad: to interpret it, to speak through it, and to track it as it moves. Naming that capacity supplies the micro-foundational engine macro-structural models of platform governance presuppose, and it gives researchers a way to ask how individual competence aggregates to stabilize or disrupt an emerging form of organizational control.

[A*] Naming it matters because its distribution is consequential and currently invisible. For the driver in Lima judging in a few seconds whether a passenger is safe to accept, or the student watching a verdict she cannot appeal, the stakes are not academic—they are the exchange itself. An inequality with no name cannot be measured, taught, or compensated for.

[C] Oracy and literacy were each named long after people had been speaking and reading, and each name made a distribution visible that had been taken for nature. The same is now due for the sensibility that coordination through a binding intermediary demands.

## References

[C] Entries not marked new are copied from the Lima paper's reference list; the eight marked † were added for this version and checked against Crossref on 2026-10-07.

Anthony, C., Bechky, B. A., & Fayard, A.-L. (2023). "Collaborating" with AI: Taking a system view to explore the future of work. *Organization Science, 34*(5), 1672–1694. https://doi.org/10.1287/orsc.2022.1651 †

Cameron, L. D. (2024). The making of the "good bad" job: How algorithmic management manufactures consent through constant and confined choices. *Administrative Science Quarterly, 69*(2), 458–514.

Clark, H. H., & Brennan, S. E. (1991). Grounding in communication. In L. B. Resnick, J. M. Levine, & S. D. Teasley (Eds.), *Perspectives on socially shared cognition* (pp. 127–149). American Psychological Association.

Curchod, C., Patriotta, G., Cohen, L., & Neysen, N. (2020). Working for an algorithm: Power asymmetries and agency in online work settings. *Administrative Science Quarterly, 65*(3), 644–676.

Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. *Management Science, 32*(5), 554–571.

DeVito, M. A. (2021). Adaptive folk theorization as a path to algorithmic literacy on changing platforms. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW2), Article 339, 1–38.

Duran, R. L. (1983). Communicative adaptability: A measure of social communicative competence. *Communication Quarterly, 31*(4), 320–326.

Elish, M. C. (2019). Moral crumple zones: Cautionary tales in human-robot interaction. *Engaging Science, Technology, and Society, 5*, 40–60.

Felin, T., Foss, N. J., & Ployhart, R. E. (2015). The microfoundations movement in strategy and organization theory. *Academy of Management Annals, 9*(1), 575–632.

Granovetter, M. (1985). Economic action and social structure: The problem of embeddedness. *American Journal of Sociology, 91*(3), 481–510.

Guzman, A. L. (Ed.). (2018). *Human-machine communication: Rethinking communication, technology, and ourselves*. Peter Lang.

Guzman, A. L., & Lewis, S. C. (2020). Artificial intelligence and communication: A human–machine communication research agenda. *New Media & Society, 22*(1), 70–86.

Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-mediated communication: Definition, research agenda, and ethical considerations. *Journal of Computer-Mediated Communication, 25*(1), 89–100.

Hargittai, E. (2002). Second-level digital divide: Differences in people's online skills. *First Monday, 7*(4).

Hayek, F. A. (1945). The use of knowledge in society. *American Economic Review, 35*(4), 519–530.

Hinds, P., & von Krogh, G. (2024). Generative AI, emerging technology, and organizing: Towards a theory of progressive encapsulation. *Organization Theory, 5*(4), Article 26317877241293478. https://doi.org/10.1177/26317877241293478 †

Jablin, F. M., & Sias, P. M. (2001). Communication competence. In F. M. Jablin & L. L. Putnam (Eds.), *The new handbook of organizational communication* (pp. 819–864). Sage.

Katsh, E., & Rabinovich-Einy, O. (2017). *Digital justice: Technology and the internet of disputes*. Oxford University Press.

Katsh, E., & Rifkin, J. (2001). *Online dispute resolution: Resolving conflicts in cyberspace*. Jossey-Bass.

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested terrain of control. *Academy of Management Annals, 14*(1), 366–410.

Leonardi, P. M., & Leavell, V. (2026). Knowing enough to be dangerous: The problem of "artificial certainty" for expert authority when using AI for decision making and planning. *Organization Science, 37*(2), 516–543. https://doi.org/10.1287/orsc.2023.18224 †

Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM.

Manky, O. (2025). Reimagining work security in Latin America's platform economy: Workers' strategies amid urban violence. *New Technology, Work and Employment, 41*(1), 33–44.

Orlikowski, W. J., & Scott, S. V. (2023). The digital undertow and institutional displacement: A sociomaterial approach. *Organization Theory, 4*(2), Article 26317877231180898. https://doi.org/10.1177/26317877231180898 †

Porsfelt, R., Vestergaard, A., & Hjorth, D. (2026). Image, imagination, imaginaries: A genealogy of imago-concepts in organisational research. *Organization Theory, 7*(3). https://doi.org/10.1177/26317877261484615 †

Powell, W. W. (1990). Neither market nor hierarchy: Network forms of organization. *Research in Organizational Behavior, 12*, 295–336.

Rahman, H. A. (2021). The invisible cage: Workers' reactivity to opaque algorithmic evaluations. *Administrative Science Quarterly, 66*(4), 945–988.

Sandberg, J. (2000). Understanding human competence at work: An interpretative approach. *Academy of Management Journal, 43*(1), 9–25.

Schoeneborn, D., Dobusch, L., & Seidl, D. (2026). Toward a theory of organizationality: A gradual view on collective actorhood. *Organization Theory, 7*(3). https://doi.org/10.1177/26317877261484616 †

Selznick, P. (1949). *TVA and the grass roots: A study in the sociology of formal organization*. University of California Press.

Simmel, G. (1902). The number of members as determining the sociological form of the group. *American Journal of Sociology, 8*(1), 1–46; *8*(2), 158–196.

Simmel, G. (1950). *The sociology of Georg Simmel* (K. H. Wolff, Ed. & Trans.). Free Press.

Simon, H. A. (1997). *Administrative behavior: A study of decision-making processes in administrative organizations* (4th ed.). Free Press. (Original work published 1947)

Spitzberg, B. H. (2006). Preliminary development of a model and measure of computer-mediated communication (CMC) competence. *Journal of Computer-Mediated Communication, 11*(2), 629–666.

Stark, D., & Pais, I. (2020). Algorithmic management in the platform economy. *Sociologica, 14*(3), 47–72.

Stark, D., & Vanden Broeck, P. (2024). Principles of algorithmic management. *Organization Theory, 5*(2), Article 26317877241257213. https://doi.org/10.1177/26317877241257213 †

Stelmaszak, M., Joshi, M., & Constantiou, I. (2026). Artificial intelligence as an organizing capability arising from human–algorithm relations. *Journal of Management Studies, 63*(2), 335–365. https://doi.org/10.1111/joms.70003 †

Sundar, S. S., & Nass, C. (2000). Source orientation in human-computer interaction: Programmer, networker, or independent social actor? *Communication Research, 27*(6), 683–703.

Sutherland, W., Jarrahi, M. H., Dunn, M., & Nelson, S. B. (2020). Work precarity and gig literacies in online freelancing. *Work, Employment and Society, 34*(3), 457–475.

Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal, 18*(7), 509–533.

Walther, J. B. (1996). Computer-mediated communication: Impersonal, interpersonal, and hyperpersonal interaction. *Communication Research, 23*(1), 3–43.

Walther, J. B. (1992). Interpersonal effects in computer-mediated interaction: A relational perspective. *Communication Research, 19*(1), 52–90.

Weber, M. (1978). *Economy and society: An outline of interpretive sociology* (G. Roth & C. Wittich, Eds.). University of California Press. (Original work published 1922)

Wilkinson, A. (1965). The concept of oracy. *Educational Review, 17*(4), 11–15.

Wing, L. (2016). Ethical principles for online dispute resolution: A GPS device for the field. *International Journal of Online Dispute Resolution, 3*(1), 12–29.

Zhou, L., Lei, X., Liu, M., Huang, X., & Hou, R. (2025). Algorithmic competency of on-demand labor platform workers: Scale development, antecedents, and consequences. *Asia Pacific Journal of Human Resources, 63*(2), e70004.
