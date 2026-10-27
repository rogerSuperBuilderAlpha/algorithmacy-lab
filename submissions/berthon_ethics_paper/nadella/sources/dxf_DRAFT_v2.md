# The Space Between Decisions: Word Separation as a Guide to Designing for Algorithmacy

> **Version 2, 2026-10-13.** This is the author's full draft of 2026-10-13, repaired by Claude at his
> instruction ("rehab it and create a new file for the updated version"). The author's wording is kept
> wherever the sources carry it. Claude changed sentences only where a source contradicted them, where a
> citation did not match the published record, or where the review (`REVIEW_v2_2026-10-13.md`) found an
> argument that would not survive a referee. The reference list is rebuilt from the project's verified
> bibliography and from Crossref. Two sections at the end are Claude's and are not part of the paper:
> "Changes from version 1" and "Still unverified". The author's read-aloud is the last gate.

## Abstract

Human factors engineering has a standing answer to a task that only the trained can perform: change the representation of the task environment and leave the person as they are. This paper takes the oldest case of that principle, the medieval scribes' move from continuous script (*scriptio continua*) to spaces between words, as a guide to designing for algorithmic mediation. People increasingly coordinate through algorithmic third parties—in ride-hailing, labor markets, commerce, and content governance—that read both sides of an exchange and commit outcomes neither side controls. The prevailing design and regulatory remedy is disclosure: explanations, published rules, and audit logs, exemplified by a recent proposal to govern frontier models as "insider risks." I argue that disclosing rules and rationales commits a category error by applying a literacy-based intervention—handing the person a text and asking for a reader—to an interactive coordination problem. Navigating irreducible triads draws instead on algorithmacy, a sensibility exercised in deciding and taking in what returns. Integrating distributed cognition, visual search, and mechanism design, I formulate Decision Experience Design (DXD), specify two structural conventions—strategic offloading and ecological feedback immediacy—examine what institutions can enforce them, and set out a four-claim research agenda.

## 1. Introduction

Human factors has a standing answer to a task that only the trained can do: change the representation of the task and leave the person as they are. Zhang and Norman (1994) gave the principle its name—the representational effect, in which "different isomorphic representations of a common formal structure can cause dramatically different cognitive behaviors" (p. 88)—and Hutchins (1995) showed it at work in a cockpit, where movable markers on the airspeed indicator let pilots reach "the same results" by "judgments of spatial proximity" (p. 282) that they would otherwise reach by reading, remembering, and comparing numbers. The oldest instantiation of this principle sits on the written page. Antiquity and early medieval manuscripts recorded text in continuous script (*scriptio continua*), which on Saenger's (1997) account left readers to find the boundaries between words by sounding the text out. Beginning with Irish scribes in the late seventh century and spreading across Continental scriptoria by the eleventh, copyists inserted blank spaces between words (Saenger, 1997). The space added no semantic information, since every letter was already on the page, yet it changed what a reader had to do with the letters; modern readers deprived of word spacing lose roughly half their reading rate (Rayner, Fischer, & Pollatsek, 1998).

That representational answer has not reached the decisions people now make through algorithmic intermediaries. Riders and drivers, buyers and sellers, applicants and employers, and creators and audiences increasingly coordinate across a third-party system that evaluates both sides and commits outcomes that neither party directly controls. When these intermediaries are opaque, regulatory mandates and HCI design interventions alike default to disclosure: publishing rules, generating post-hoc explanations, and logging decisions for inspection. Yet across empirical evaluations, disclosure often fails to improve human decision-making and sometimes degrades it. A repayment disclosure on credit-card statements increased delinquency among some borrowers (Seira, Elizondo, & Laguna-Müggenburg, 2017); a clear model with few features left users less able to detect and correct the model's mistake on an unusual case (Poursabzi-Sangdeh et al., 2021); and having read a community's posted rules went with lower perceived fairness among users whose posts were removed (Jhaver, Appling, Gilbert, & Bruckman, 2019). Explanations do not improve decision performance on average (Schemmer et al., 2022), and across 370 effect sizes in human–AI studies the presence of an explanation made no significant difference (Vaccaro, Almaatouq, & Malone, 2024). Where explanations or alerts do help—as in automated driving takeovers (Matsuo, Liu, Hiraoka, & Wada, 2026) or cognitive forcing interfaces (Buçinca, Malaya, & Gajos, 2021)—they operate inside dyadic human–machine loops. In neither of those settings does the algorithm issue a determination binding two parties before either acts.

The failure is not an empirical anomaly; it is a category error. A disclosure of rules and rationales hands the person a text—a rule, a rationale, a record—and so asks for a reader, making it an intervention in literacy. Deciding through an adaptive third party draws on something else: algorithmacy, which I define as the sensibility to navigate irreducible triads, as literacy is the sensibility that reading and writing require. A remedy built for readers adds to the reading of the people it means to help and leaves their decision where it was. It also settles, without argument, who holds the remedy. Satya Nadella's (2026) proposal to govern frontier models as "insider risks" illustrates the enterprise endpoint of this logic, asking that every meaningful model action leave "tamper-proof human readable evidence," that an authorized person be able to halt a model in mid-task, and that organizations "separate the supply of intelligence from the authority over it." Each provision serves the deploying organization's internal control, whereas the people on whom the model acts enter the framework only once, as recipients of a disclosure after something has failed. Unlike medieval scribes, who answered to a church and court that ordered books made correct for their readers, a digital platform that owns the interface between two parties optimizes for objectives of its own under terms of service that reserve "broad, unfettered discretion to platform owners" (Suzor, 2018).

The focus and contribution of this paper is to shift the design of mediated decision environments from literacy-based disclosure to algorithmacy-based re-representation. Treating the history of word separation as an analytic guide rather than a general history of literacy (Saenger, 1997, p. x), I restate the scribes' move in the vocabulary of distributed cognition and visual search, distinguishing structural re-representation from both disclosure and training. I then argue that in triadic systems, people come to understand a mediator not by reading about it, but by acting through it and taking in what returns—a process of enacted sensemaking and epistemic action (Kirsh & Maglio, 1994; Weick, 1988) that succeeds only where a valid environment supplies "feedback that is both rapid and unequivocal" (Kahneman & Klein, 2009, p. 524). From that premise, I formulate Decision Experience Design (DXD) and specify two candidate conventions that do for mediated decisions what word spacing did for the line of text: strategic offloading, which removes a tactical calculation from the mechanism and makes its removal plain on the interface, and ecological feedback immediacy, which returns valid, low-latency state changes as the person acts.

The remainder of the paper proceeds in eight sections. I first review HCI and CSCW scholarship on transparency, trust calibration, and "revealing design" (§2), restate the scribal precedent in human-factors terms (§3), and show why disclosures of rules and rationales fail when transplanted from dyadic tools to triadic mediators (§4). I then define algorithmacy as enacted sensemaking in irreducible triads (§5) and articulate the two DXD conventions, each paired with a design opening (§6). Finally, I introduce a unilateral-modification test to compare convention enforcement across courts, dealer foreign-exchange markets, and platforms (§7), set out a four-claim research agenda anchored by a multi-agent experimental protocol (§8), and state the framework's scope (§9).

## 2. Background: Transparency, Explanation, and Legibility in HCI

### 2.1 The Transparency and Trust-Calibration Turn in HCI and CSCW

HCI has spent three decades operating under the assumption that opacity is an informational defect to be repaired by exposure. When early collaborative filtering algorithms began making recommendations, researchers observed that users resisted suggestions whose origin they could not discern. The initial remedy was straightforward: attach an explanation showing neighboring user ratings or item similarities (Herlocker, Konstan, & Riedl, 2000; Knijnenburg et al., 2012). As statistical learning models grew more complex, this logic expanded into explainable artificial intelligence (XAI), producing feature-attribution summaries, counterfactual explanations, descriptions of model behavior, and content-moderation notices (Wischnewski, Krämer, & Müller, 2023; Cabrera, Perer, & Hong, 2023; Jhaver et al., 2019; Ehsan et al., 2021). The implicit cognitive model was classical: if an interface can render the internal state, training weights, or decision boundaries of an automated system visible, the human operator will form an accurate mental model, calibrate their trust appropriately, and make better decisions (Lee & See, 2004; Körber, 2018).

Empirical reality has repeatedly unsettled this optimism. Instead of calibration, transparency interventions often produce a paradox: exposing internal system mechanics increases what the user must process without improving decision quality, and can induce misplaced reliance (Parasuraman & Manzey, 2010). When people are shown explanations for automated recommendations, the explanations can raise acceptance of the recommendation whether or not it is correct (Bansal et al., 2021; Chen, Liao, Wortman Vaughan, & Bansal, 2023), and explanations reduce overreliance only under particular conditions, such as a hard task with an explanation that is cheap to check (Vasconcelos et al., 2023). Prolonged reliance on automated aids shifts the human operator from active control toward passive monitoring, with costs to vigilance and to manual skill (Metzger & Parasuraman, 2001; Casner, Geven, Recker, & Schooler, 2014).

Recent investigations into human collaboration with large language models and generative agents report related problems. Text-generation tools impose an output-inspection cost (Mozannar, Bansal, Fourney, & Horvitz, 2024; Simkute et al., 2024). Operators must read through fluent, probabilistically generated text to catch subtle errors or misalignment, and knowledge workers report reduced critical engagement when they do (Lee et al., 2025). The interface presents an uninterrupted token stream, leaving the user to check for errors after the fact.

### 2.2 Situated Rationale vs. Post-Hoc Audit Trails and "Revealing Design"

Recognizing that post-hoc textual explanations fail to support real-time execution, contemporary interaction design has begun exploring in-flow friction and situated scaffolding. Buçinca, Malaya, and Gajos (2021) showed that cognitive forcing functions—such as requiring users to formulate an independent choice before viewing an AI recommendation—reduced overreliance compared with simple explanations on the questions where the AI was wrong. Similarly, Disley and Khan (2026) reframe system representations as an active "design surface," showing that selectively suppressing a concept in a model can introduce productive cognitive friction. In software development environments, annotation made at the point of use preserves context that is hard to reconstruct afterward (Horvath et al., 2022). Dialogue systems similarly depend on economy in interaction and discoverable error-correction rather than lengthy explanatory turns (Pucci, Piro, & Matera, 2027).

Critical scholars in CSCW and HCI have taken this critique a step further, interrogating the structural relations embedded in commercial platforms. Özçetin and Wiltse (2023) critique how Terms of Service (ToS) rely on static, legalistic text to govern dynamic, asymmetric relations. They advocate for "revealing design," an approach aimed at making platform entanglements "legible" to participants.

Yet revealing design, for all its critical insight, stops short of escaping the literacy paradigm. To make an entanglement legible is still to treat the user as a critical reader. It presumes that if we give a gig worker or digital consumer an expressive visual diagram or a richer conceptual breakdown of their position, we have equipped them to act. But understanding that one is entangled does not change the actions required to accept a dispatch, price a product, or contest a penalty. A person sitting at an interface does not need a more transparent picture of their subordination; they need an interaction surface whose mechanics alter what they have to calculate to coordinate their lives.

### 2.3 From Human–Machine Dyads to Irreducible Algorithmic Triads

The deeper reason why transparency paradigms fail is structural: research on transparency and explanation remains oriented around dyadic interaction. In the classic cognitive engineering literature, interaction is modeled as a two-node loop: a human operator paired with a machine aid (Sheridan & Verplank, 1978; Parasuraman, Sheridan, & Wickens, 2000). The pilot monitors the autopilot; the clinician reviews a diagnostic classifier; the driver takes over from an automated steering system (Matsuo et al., 2026). In a dyad, the machine's role is auxiliary. Its explicit functional purpose is to support, inform, or substitute for the human operator in executing an external task.

```
Classic HCI Dyad:
[Human Operator] <====== Interaction Loop ======> [Machine / Tool]
```

Coordination across contemporary digital platforms does not fit this schema. In ride-hailing, digital labor platforms, electronic financial markets, and content clearinghouses, the architecture is triadic. Two human counterparts—a rider and a driver, a freelance specialist and an employer, a buyer and a seller—coordinate through a third node: an active algorithmic mediator (M). HCI and CSCW have studied settings with more than one person and a system, including AI-mediated communication, where suggested replies change how two correspondents write and regard each other (Hohenstein et al., 2023). The transparency literature has not taken the same step.

```
Irreducible Algorithmic Triad:
                   ┌─────────────────────────────┐
                   │    Algorithmic Mediator     │
                   │ (Optimizing Objective J_M)  │
                   └──────────────┬──────────────┘
                                 ▲ ▲
                  Mediation Probe│ │Boundary Reaction
                                 │ │
            ┌────────────────────┴─┴────────────────────┐
            │                                           │
  ┌─────────┴─────────┐                       ┌─────────┴─────────┐
  │      Party A      │◄──Coordination Move──►│      Party B      │
  │ (Worker / Driver) │                       │ (Client / Rider)  │
  └───────────────────┘                       └───────────────────┘
```

This mediator is not an advisory instrument assisting one party. It reads inputs from both sides, filters information symmetrically or asymmetrically, applies an independent objective function (J_M)—such as platform profit maximization, throughput balancing, or dispute minimization—and commits a binding allocation that neither party directly controls (Lee, Kusbit, Metsky, & Dabbish, 2015). Party A's payoff depends directly on Party B's move, yet Party A can only perceive, probe, or influence Party B through the transformation imposed by M; in that sense the triad does not decompose into two independent dyads. Transplanting dyadic transparency tools into a triadic mediator yields incoherence: explaining to Party A why the algorithm made an allocation does not eliminate the tactical necessity for Party A to second-guess what Party B will do through that same mediator.

## 3. Re-Representation: The Scribal Precedent in Human-Factors Terms

### 3.1 The Page Before and After Word Separation

To understand how an interaction surface can be transformed without changing the underlying information, we can look to the history of the written page. For more than a millennium across Greco-Roman antiquity and the early Middle Ages, texts were transcribed in *scriptio continua*. Words were strung together in unbroken lines without spaces between them.

Because *scriptio continua* provided no spatial demarcations between lexical units, Saenger (1997) argues, reading was laborious: a reader identified words by pronouncing or subvocalizing the characters, relying on sound to reconstruct lexical boundaries. Classicists dispute how heavy that burden was for trained readers (Heilmann, 2020), and the argument here does not depend on settling it.

Between the late seventh and eleventh centuries, an uncoordinated ergonomic change unfolded across monastic scriptoria. Scribes in Ireland and Anglo-Saxon Britain learned Latin as a foreign language, not as a spoken one, and Insular copyists began inserting gaps between words (Saenger, 1997; Parkes, 1992). Over the next three centuries, this spatial convention reached Continental scriptoria, becoming standard by the eleventh century alongside developments in punctuation and layout (Parkes, 1992; Saenger, 1997).

Before drawing human-factors conclusions from this shift, we must set strict historiographical boundaries. Spacing did not single-handedly generate modern literacy. Mass literacy required centuries of institutional change, legal documentation, administrative centralization, and the invention of movable type (Clanchy, 1993; Cressy, 1980; Eisenstein, 1969). Nor was silent reading impossible in the ancient world: classical accounts show that skilled readers could and did read silently long before word spacing appeared (Knox, 1968; Gavrilov, 1997; Burnyeat, 1997; Heilmann, 2020).

The scribal convention did something more specific: it altered the sensory mechanics of the task. The space between words added no semantic data. Every letter on the page remained unchanged. Yet by altering the visual layout of the page, scribes altered what a reader had to do to extract meaning. Saenger's own statement of the effect is that word separation and related devices in Insular books "provided shortcuts for achieving the reading skills that an elite among the ancients had mastered only through a prolonged and arduous grammatical apprenticeship" (1997, p. 85).

### 3.2 Cognitive Offloading, Visual Search, and Perceptual Substitution

In the language of cognitive engineering, the introduction of inter-word spacing was an act of environmental cognitive offloading (Risko & Gilbert, 2016; Kirsh, 1995) that exploited the representational effect (Zhang & Norman, 1994). Zhang and Norman demonstrated that across formally isomorphic tasks—such as variations of the Tower of Hanoi—the external representation dictates the cognitive rules of engagement. When constraints are embedded directly into physical space, they do not need to be held in working memory or checked through conscious mental inference.

Hutchins (1995) documented the same principle on the flight deck: pilots set movable speed bugs on the rim of the airspeed indicator, and the comparison of speeds is externalized into the spatial proximity between a needle and a marker.

```
Representational Shift on the Page:

Scriptio Continua:
[L][E][X][I][C][A][L][B][O][U][N][D][A][R][Y]
▲                                           ▲
└──────── Working Memory / Phonological ────┘
          Reconstruction Overhead

Word Spacing:
[L][E][X][I][C][A][L]   [B][O][U][N][D][A][R][Y]
          ▲          ▲          ▲
          └── Visual ┴── Eye ───┘
              Saccade Targeting
```

On this reading, *scriptio continua* left boundary detection to the reader, who had to hold ambiguous strings of sound while testing competing segmentations, and word spacing substituted visual segmentation for that inference. The interpretation is this paper's; no study has measured it for medieval readers.

The visual system processes spatial structure across the field in parallel. Under Wolfe's (2021) Guided Search model, bottom-up feature salience guides the allocation of focal attention. By carving white channels between character clusters, spacing gives the oculomotor system targets for the next saccade, and removing the spaces changes where the eyes land as well as how fast words are identified (Rayner et al., 1998). Deprived of these spatial markers, modern readers lose roughly half their reading rate (Rayner et al., 1998). Spacing let the geometry of the page do the work of lexical segmentation.

### 3.3 Cross-Orthographic Asymmetries and the Structural Disanalogy

The interaction between orthography and human vision reveals that representational offloading is not a simple, universal trick. Cross-linguistic reading experiments uncover a directional asymmetry. When spaces are removed from an alphabetic script like English, reading performance drops sharply. Yet when spaces are inserted into scripts that are normally written without them—such as Chinese or Thai—the effect is mixed (Bai et al., 2008; Winskel, Radach, & Luksaneeyanawin, 2009; Chantavarin & Leung, 2025).

Skilled readers of Chinese read word-spaced text no faster than normal unspaced text, 5,239 against 5,221 milliseconds a sentence (Bai et al., 2008). Thai readers fixate a spaced word for less time and take longer over the sentence (Winskel et al., 2009; Chantavarin & Leung, 2025). Learners do not reliably gain: child learners of Chinese read spaced text more slowly and less accurately (Bassetti & Masterson, 2012), and for adult second-language learners the difference between spaced and unspaced text was not significant (Cui, 2023). A convention pays once readers have come to depend on it. An ergonomic intervention is not an abstract virtue; it must match the visual search affordances of the medium to the cognitive tasks of the user.

Here lies the decisive structural disanalogy between the medieval page and the modern platform. A manuscript page is passive, static, and cooperative. Once ink dries on parchment, the page has no agency. It does not reorder its words, change its layout when the reader blinks, or extract behavioral surplus from the reader's gaze. Furthermore, the scribes who made it worked under institutional discipline.

Carolingian rulers and church authorities ordered scriptoria to produce correct books: Charlemagne's letter *De litteris colendis* measures monasteries' writing against a standard of correctness, the *Admonitio generalis* of 789 (c. 72) orders books corrected and copied with care, and Alcuin's *Carmen* XCIV instructs scribes to mark sense units for the lector. Westwell (2018) cautions that uniformity imposed from above can be overstated. None of these texts concerns word separation, which the Insular scribes had adopted earlier. What they show is who stood behind the page: an authority with standing over the scribe.

An algorithmic intermediary is dynamic, adaptive, and governed by the commercial incentives of its owner. The platform controls the interface, observes user probes, and can rewrite its ranking rules, pricing multipliers, and allocation weights. Where the medieval page was a stable, cooperative surface held in check by institutional authority, the platform interface is an active, contested site.

## 4. Disclosure as a Literacy-Based Intervention

### 4.1 Taxonomizing Disclosure and the Law-and-Economics Critique

When algorithmic mediation produces unfair or exploitative outcomes, public regulators, legal bodies, and design standards routinely fall back on disclosure. Mandating that platforms explain themselves has become the universal compromise. To understand why this fails, we must disaggregate "disclosure" into four distinct targets:

```
               ┌────────────────────────────────────────────────────────┐
               │              Target 1: Presence Disclosure             │
               │         ("An automated algorithm is in use")           │
               └───────────────────────────┬────────────────────────────┘
                                           │
               ┌───────────────────────────▼────────────────────────────┐
               │         Target 2: Objective Function Disclosure        │
               │   ("System maximizes driver utilization and margin")   │
               └───────────────────────────┬────────────────────────────┘
                                           │
               ┌───────────────────────────▼────────────────────────────┐
               │        Target 3: Formal Rule Property Disclosure       │
               │         ("Mechanism is obviously strategy-proof")      │
               └───────────────────────────┬────────────────────────────┘
                                           │
               ┌───────────────────────────▼────────────────────────────┐
               │       Target 4: Full Textual Rule & Rationale          │
               │  (Terms of Service, XAI feature cards, audit logs)     │
               └────────────────────────────────────────────────────────┘
```

1. Target 1 (Presence): Notifying users that an algorithm or bot is active (Ishowo-Oloko et al., 2019).
2. Target 2 (Objective Function): Stating the objective the mediator is optimizing (e.g., platform margin maximization vs. wait-time minimization).
3. Target 3 (Formal Rule Property): Informing users of an actionable structural property of the mechanism (e.g., that an auction is strategy-proof; Masuda et al., 2022).
4. Target 4 (Full Textual Rule and Rationale): Providing full terms of service, technical documentation, or post-hoc feature-attribution scores explaining an individual allocation.

The category error named in this paper lies in Target 4. Target 3 behaves differently: a one-line statement of a property changes what people do (§6.2), and it does so as a signal that a calculation is unnecessary, with nothing to study.

The legal and behavioral critique of mandated disclosure explains why Target 4 repeatedly fails. Ben-Shahar and Schneider (2011) reviewed disclosure regimes across finance, healthcare, and consumer contracts and concluded that mandated disclosure, among the most common regulatory techniques, regularly fails because the people it addresses do not read disclosures, do not understand them when they do, and do not use them when they understand (p. 665). Psychology explains much of the gap between what is disclosed and what is done with it (Loewenstein, Sunstein, & Golman, 2014), and disclosure works only where it is embedded in the routines of users and disclosers alike (Fung, Graham, & Weil, 2007).

The disclosures that do alter outcomes tend to be simple, low-cost signals, such as letter grades for hygiene posted in restaurant windows, and they act in good part on the discloser, who changes its conduct to avoid publishing a poor grade (Ben-Shahar & Schneider, 2011, pp. 743–748; Loewenstein et al., 2014, p. 403). Ben-Shahar and Schneider hedge even this case.

### 4.2 The Empirical Record Across Finance, XAI, and Platform Governance

The failure of disclosure is documented across empirical human–AI interaction. In a meta-analysis of XAI interventions, explanations yielded no reliable improvement in human decision performance (Schemmer et al., 2022, reporting a pooled standardized mean difference of 0.07, 95% CI [−0.15, 0.30]), and across 370 effect sizes the presence of an explanation was not a significant moderator of human–AI performance (Vaccaro et al., 2024).

Field experiments in consumer finance show that disclosure can backfire. When a Mexican bank added messages to credit-card statements, a message stating the interest rate changed nothing, and a message stating how many months the balance would take to repay raised delinquency among two groups of clients by 0.011 points, 7.4% of the mean (Seira et al., 2017, pp. 292, 295).

In machine learning interfaces, Poursabzi-Sangdeh et al. (2021) showed that presenting users with a clear model with few features reduced their ability to detect and correct the model's mistake on an unusual case, in three of four experiments. The authors conjecture that the visible detail overloaded participants.

In platform governance, Jhaver et al. (2019) surveyed 907 Reddit users whose posts had been removed. Users who had read the community's rules beforehand judged the removal as less fair (β = −.314), while users who received an explanation of the removal judged it fairer (β = .384). The rulebook and the situated reason pulled in opposite directions.

Furthermore, Nouwens et al. (2020) demonstrated in cookie consent interfaces that layout alone moves behavior: removing the opt-out button from the first page raised consent by 22 to 23 percentage points. Users respond to the spatial architecture of the interface.

### 4.3 Enterprise Compliance as the Zenith of Literacy Dogma

The apex of literacy-based governance is on display in modern enterprise AI proposals. Satya Nadella's (2026) post, "Models as Insider Risks in the Super Intelligence Era," provides a case study. Confronted with the unpredictability of autonomous frontier agents, Nadella proposes treating AI systems like insiders who may be mistaken or compromised, and sets out seven principles. Three bear on what a person is given:

1. Auditability: every meaningful model action must leave "tamper-proof human readable evidence."
2. Interruption: an authorized person must be able to pause or shut down a model in mid-task, which he likens to an emergency brake.
3. Separation: organizations must "separate the supply of intelligence from the authority over it."

This framework addresses internal principal–agent control for the deploying organization, in the tradition of insider-threat practice (CERT National Insider Threat Center, 2022). Its other principles—model diversity, independent controls, independent auditability—are likewise held by the organization.

```
Enterprise Insider Risk Architecture:
┌────────────────────────────────────────────────────────┐
│                   Deploying Firm                       │
│  ┌──────────────────┐           ┌───────────────────┐  │
│  │ Intelligence     │           │ Executive         │  │
│  │ Provider (Model) │           │ Authority / Halt  │  │
│  └────────┬─────────┘           └─────────▲─────────┘  │
│           │                               │            │
│           └──────► Human-Readable ────────┘            │
│                    Audit Logs                          │
└───────────────────────────┬────────────────────────────┘
                            │ Binding Triadic Allocation
                            ▼
┌────────────────────────────────────────────────────────┐
│               External Transacting Parties             │
│        (Gig Worker / Consumer / Displaced User)        │
│                                                        │
│   Status: Receive disclosure of an incident after      │
│           an adverse determination has occurred        │
└────────────────────────────────────────────────────────┘
```

For the external humans transacting across the model, Nadella's framework changes little. The gig worker who is deactivated, the small business whose account is suspended, or the consumer denied a transaction does not hold the brake. They cannot interrupt the model in mid-inference. The framework promises them "timely disclosure" when the system fails or is compromised.

For the person on the receiving end of an algorithmic determination, a disclosure after the fact is an autopsy report. It asks them to read the record of what happened to them and leaves them unable to reshape the interaction.

## 5. Algorithmacy: Epistemic Action in Irreducible Triads

### 5.1 Defining Algorithmacy

I define algorithmacy as the behavioral sensibility required to navigate irreducible algorithmic triads: the capacity to coordinate with a counterpart through an active, optimizing mediator whose internal rules shift dynamically.

```
                                 ┌─────────────────────────────┐
                                 │    Historical Transition    │
                                 └──────────────┬──────────────┘
                                                │
         ┌──────────────────────────────────────┴──────────────────────────────────────┐
         ▼                                                                             ▼
┌─────────────────────────────────┐                                           ┌─────────────────────────────────┐
│            Literacy             │                                           │          Algorithmacy           │
├─────────────────────────────────┤                                           ├─────────────────────────────────┤
│ Mode: Evaluative, textual,      │                                           │ Mode: Enacted, exploratory,     │
│       reflective                │                                           │       epistemic                 │
│ Medium: Static pages, documents,│                                           │ Medium: Dynamic, optimizing,    │
│         post-hoc logs           │                                           │         triadic interfaces      │
│ Cognitive Demands: Working      │                                           │ Cognitive Demands: Dynamic      │
│   memory, phonological loop,    │                                           │   calibration, boundary         │
│   semantic parsing              │                                           │   probing, feedback integration │
│ Stance: Reader                  │                                           │ Stance: Decision-maker          │
└─────────────────────────────────┘                                           └─────────────────────────────────┘
```

Algorithmacy is distinct from dyadic "AI literacy." The latter typically refers to conceptual knowledge: understanding what neural networks are, how training data shapes bias, or how to compose structured text prompts in chat windows.

Nor does it match the one earlier printed use of the word that I have found. Oberschelp (1995), writing on informatics teaching, urges that "we have to preserve logicacy and algorithmacy by continuously training simple mental activities without artificial tools" (p. 121). He does not define the term; in context it names the skill of carrying out algorithmic steps by hand.

Algorithmacy as I use it is an active coordination competency. Just as literacy allows a reader to traverse an author's text without demanding that the reader build a printing press, algorithmacy allows an individual to formulate choices, infer hidden constraints, and protect their welfare across an algorithmic intermediary without requiring them to inspect its source code.

### 5.2 Enacted Sensemaking and Epistemic Action

In an irreducible triad, people do not come to understand a mediator by reading about it. They understand it by acting through it and observing what happens. This process is grounded in Weick's (1988) account of enacted sensemaking: in ambiguous, dynamic environments, "people think by acting" (p. 305). Actors take action, create consequences in the environment, and then look at the results to infer what kind of system they are dealing with. Weick adds a warning that belongs in any design that relies on this: action that clarifies a situation can also intensify it.

In cognitive science, exploratory moves of this kind are known as epistemic actions (Kirsh & Maglio, 1994). Kirsh and Maglio showed that in Tetris, players do not rotate and translate falling pieces only to place them (pragmatic action). They also move them to learn something sooner than they could work it out in the head. Epistemic actions are "physical actions that make mental computation easier, faster, or more reliable" (p. 513).

```
Triadic Epistemic Probing:
[Worker / User] ──── (1) Epistemic Probe: Move / Micro-bid ────► [Algorithmic Mediator]
                                                                        │
                                                                 (2) Evaluates Probe
                                                                 Against Objective J_M
                                                                        │
[Worker / User] ◄─── (3) Boundary Reaction / State Update ──────────────┘
       │
(4) Dynamic Recalibration of Strategy
```

Transacting workers and consumers engage in epistemic actions every day, and extending Kirsh and Maglio's concept to them is this paper's move. Ride-hail drivers do not learn dispatch and surge behavior from company documentation. They form working theories from what the system does in response to their own moves, and they trade those theories in online forums (Lee et al., 2015; Kellogg, Valentine, & Christin, 2020). Workers pool what they observe and push back together (Cameron & Rahman, 2022). Formal models of strategic classification under opacity describe the same situation: when a decision rule is hidden, people infer it from the observed outcomes of others (Ghalme et al., 2021). Learning a mediator is social as well as enacted.

These probes are epistemic actions designed to extract information from an opaque mediator. Transacting parties navigate algorithmic environments through continuous behavioral experimentation.

### 5.3 High-Validity Learning Environments vs. Mediated Distortion

For enacted sensemaking to succeed, the environment must meet the two conditions Kahneman and Klein (2009) set for skilled intuition: an environment regular enough to be learned, and an opportunity to learn it through "feedback that is both rapid and unequivocal" (p. 524).

When feedback is delayed or noisy, calibration suffers, and in different ways. Rahmandad and Gary (2023) found that delay pushes decision-makers toward options that pay off quickly and can drive convergence to inefficient strategies, while noise does not produce that bias and instead pulls choices toward the middle of the strategy space.

Algorithmic intermediaries often fail these conditions. To analyze mediated distortion, we must separate two distinct drivers:

1. Strategic Rule Secrecy: Platforms conceal evaluation criteria, ranking parameters, and matching formulas. Platform operators justify this secrecy as necessary to prevent "gaming," and Rahman (2019) reads it as also keeping control of a stratified workforce with the platform.
2. Technical Noise and Latency: Algorithmic mediators introduce jitter, batching delays, and stochastic allocations. Not all distortion is intended. The rapid fluctuation in Uber's surge multipliers measured by Chen, Mislove, and Wilson (2015) was, by Uber's own account, a bug. No source I have found shows that a platform introduces noise or delay on purpose.

Regardless of whether distortion originates in corporate strategy or system architecture, its cognitive result is the same. When an intermediary combines hidden rules with noisy, delayed feedback, it removes the conditions for learning by acting. The user probes the system, receives an ambiguous response later, and cannot distinguish whether their action failed, the market shifted, or the algorithm penalized them.

Under these conditions, algorithmacy cannot flourish. The user is left relying on folk theories and defensive gaming.

## 6. Decision Experience Design (DXD): Two Candidate Conventions

### 6.1 Architectural Framing via Norman's Gulfs of Action

Decision Experience Design (DXD) shifts the design agenda from writing textual explanations to restructuring the decision interface. DXD grounds its interventions in Norman's (1988) framework of action:

```
                     ┌─────────────────────────────────────────┐
                     │          The Transacting Human          │
                     └──────────────┬──────────────────▲───────┘
                                    │                  │
                Formulate Intent    │                  │ Evaluate State
                                    │                  │
                   ┌────────────────▼┐                ┌┴────────────────┐
                   │     Gulf of     │                │     Gulf of     │
                   │    Execution    │                │   Evaluation    │
                   └────────────────┬┘                └▲────────────────┘
                                    │                  │
                     Bridged by:    │                  │ Bridged by:
                     Strategic      │                  │ Ecological
                     Offloading     │                  │ Feedback
                     (Convention A) │                  │ Immediacy
                                    │                  │ (Convention B)
                                    │                  │
                     ┌──────────────▼──────────────────┴───────┐
                     │          Algorithmic Mediator           │
                     └─────────────────────────────────────────┘
```

1. The Gulf of Execution: The cognitive distance between a user's goal and the actions permitted by the interface. Convention A (Strategic Offloading) narrows the Gulf of Execution by eliminating tactical gaming calculations from the transaction mechanism and showing on the display that they have been eliminated.
2. The Gulf of Evaluation: The cognitive distance between the system's state and the user's ability to assess that state. Convention B (Ecological Feedback Immediacy) narrows the Gulf of Evaluation by delivering valid, noise-filtered, low-latency feedback as the user formulates their choice.

### 6.2 Convention A: Strategic Offloading (Removing a Tactical Task and Showing It Is Gone)

In classical mechanism design, an allocation mechanism is strategy-proof if reporting one's true valuation or preference is a dominant strategy: no participant can gain by lying, shading their bid, or misrepresenting their constraints. Yet theoretical strategy-proofness rarely translates into sincere human behavior. In a laboratory Vickrey auction, only about a fifth of bids were sincere without advice (Masuda et al., 2022).

To address this, Li (2017) formalized obviously strategy-proof (OSP) mechanisms. A mechanism is obviously strategy-proof if, for any deviating strategy, the best possible outcome under the deviation is no better than the worst possible outcome under the truth. OSP mechanisms can be recognized as safe by agents who lack contingent reasoning capabilities, and in Li's experiments far fewer games ended off the dominant-strategy outcome under the obviously strategy-proof version of the same rule.

Convention A embeds this property in the visual interface. It removes the tactical calculation—eliminating the need to second-guess what other participants are doing—and uses the interface to make that removal obvious.

Recent experimental economics calibrates the convention and its limit. Gonczarowski, Heffetz, Ishai, and Thomas (2024; N = 542) tested whether describing a matching mechanism as a personalized menu, in place of the traditional description of its algorithm, increased understanding and straightforward play. Understanding of strategy-proofness rose to 71%, against 58% and 56% under the other descriptions. Straightforward play reached 59% under the menu description, against 56% under the traditional description, a difference that is not significant, and 48% under a control that conveyed almost nothing.

The boundary is plain: under the best description tested, about four in ten participants still did not play straightforwardly, and better understanding moved play only a little.

This is why Masuda et al. (2022) matter: a plain statement that sincere bidding is a dominant strategy raised sincere bids from 20.6% to 46.9%, while efficiency rose by about one percentage point. Convention A must therefore pair the structural elimination of the tactical task with an interface that visibly confirms the task is gone, and its designers should expect behavior to change more than outcomes.

```
Convention A Interface Transformation:

Old Gaming Interface:
┌────────────────────────────────────────────────────────┐
│ Enter Your Hourly Rate Bid: [ $ 45.00 / hr           ] │
│                                                        │
│ [ Warning: Other workers may undercut your bid.      ] │
│ [ Consider platform commission (20%) and surge index. ]│
└────────────────────────────────────────────────────────┘
Result: Tactical anxiety; complex shade calculation.

DXD Strategic Offloading Interface:
┌────────────────────────────────────────────────────────┐
│ Guaranteed Clearing Menu:                              │
│                                                        │
│   ● [ $ 52.00 / hr ] ── Guaranteed Dispatch in Tier 1  │
│   ○ [ $ 48.00 / hr ] ── Guaranteed Dispatch in Tier 2  │
│                                                        │
│ [ Strategy Notice: Ascending Clock Active.             ]│
│ [ Sincere preference revelation is dominant. No worker ]│
│ [ can undercut your allocated tier.                    ]│
└────────────────────────────────────────────────────────┘
Result: Tactical calculations offloaded to mechanism display.
```

**Design Opening: What if...?**
What if freelance labor dispatch and procurement platforms abandoned open-ended bid-entry boxes—which force workers to calculate speculative price-shading—and replaced them with ascending-clock menus that display clearing tiers where compensation is guaranteed and tactical undercutting is made impossible by design?

### 6.3 Convention B: Ecological Feedback Immediacy (Valid and Plain First, Rapid Second)

Convention B addresses the Gulf of Evaluation by shortening the temporal and causal distance between an actor's exploratory probe and the mediator's response. In classical graphical user interfaces, direct manipulation relies on immediate visual feedback: when a user drags a file, the icon tracks the cursor in real time (Shneiderman, 1983). In algorithmic mediation, that immediate coupling is routinely broken. A user submits a bid, posts a job, or positions a car, and waits in an informational vacuum while backend algorithms batch, calculate, and commit.

However, in designing Convention B, ecological validity strictly precedes speed. Exposing high-frequency feedback on noisy or volatile data can damage human decision-making. Larson, List, and Metcalfe (2016) found that professional traders shown prices second by second invested about 25% less in the risky asset and earned about 35% less than traders shown prices every four hours, a pattern they attribute to myopic loss aversion.

Similarly, Kluger and DeNisi (1996, 1998) showed in a meta-analysis that more than one-third of feedback interventions reduce performance. Providing uncurated, rapid feedback on a volatile algorithm hands the user a stream of noise.

Therefore, Convention B specifies feedback that is valid and noise-filtered first, plain second, and low-latency third. It provides pre-commit sandboxes and boundary contours that let participants test how the mediator will treat a move before committing to an irreversible choice. No experiment has yet tested this convention in a mediated triad; it follows from the conditions in §5.3 and is offered as a hypothesis.

```
Convention B: Pre-Commit Boundary Feedback

Opaque Batched Flow:
[ Formulate Move ] ──► [ Commit Action ] ──► [ Silent Batching Delay ] ──► [ Irreversible Outcome ]
                                              (Zero visibility)             (Post-hoc shock)

DXD Pre-Commit Sandbox Flow:
[ Formulate Move ] 
       │
       ▼ (Exploratory Probe)
┌────────────────────────────────────────────────────────┐
│ Pre-Commit Counterfactual Contour Sandbox              │
│                                                        │
│   Candidate Parameter: [ X = 42 ]                      │
│   Mediator Boundary Reaction: [ Cleared: P(Match) = 88%│
│   Noise-Filtered Confidence Band: [ ± 3% ]             │
│                                                        │
│   [ Visual contour shows parameter boundary line ]     │
└────────────────────────────────────────────────────────┘
       │
       ▼ (Informed Commitment)
[ Commit Final Action ] ──► [ Deterministic Execution ]
```

**Design Opening: What if...?**
What if gig drivers and marketplace sellers were provided with noise-filtered contour maps that showed, as they dragged a price or radius slider, how the platform's clearing mechanism would allocate orders across candidate locations before they committed to a shift or contract?

## 7. Institutional Custody: Who Can Hold a Convention?

### 7.1 The Unilateral-Modification Custody Test

A representational convention is not an abstract piece of interface code; it is a promise between the mediator and the transacting parties. For a convention to hold, participants must trust that the interface will not deceive them. This introduces the problem of custody: who ensures that the interface remains faithful?

To evaluate institutional stability, I formulate the Unilateral-Modification Custody Test:

*Can the party that operates the intermediary unilaterally alter, suspend, or distort the representational convention without the informed consent of the transacting parties?*

This test is grounded in the economic theory of agency costs (Jensen & Meckling, 1976). When an intermediary has an independent financial interest in the transaction, its operator faces continuing incentives to alter the representation to capture surplus from transacting users.

### 7.2 Comparative Analysis Across Three Institutional Realms

To evaluate how custody functions in practice, I examine three institutional environments:

| Institutional Realm | Primary Enforcement Authority | Structural & Procedural Mechanism | Unilateral-Modification Vulnerability |
| --- | --- | --- | --- |
| Courts of Law | Constitutional oversight & statutory civil procedure | Rules Enabling Act (28 U.S.C. § 2073); judicial disqualification (*Tumey v. Ohio*, 1927); procedural due process (*Mathews v. Eldridge*, 1976) | Low (rule-bound): a judge cannot alter evidentiary or procedural rules mid-trial to advantage one party |
| Dealer FX Markets | Voluntary industry code; regulators after the fact | FX Global Code (GFXC, 2024): Principle 17 on last look; Principles 9, 36, and 39 on what is disclosed to clients; Principle 40 on agreeing changes to terms | Moderate (soft law): the Code is voluntary; benchmark manipulation was punished by regulators (FCA, 2014; NYDFS, 2015) |
| Digital Platforms | Private corporate ownership | Unilateral Terms of Service (Suzor, 2018; Klonick, 2018); proprietary interface updates; advisory boards (Oversight Board, 2022) | High (unilateral): the owner sets and changes rankings, algorithms, and interface conventions, subject to statute where one applies |

In judicial systems, procedural conventions are insulated from unilateral tampering. Under the Rules Enabling Act (28 U.S.C. § 2073), federal procedural rules are prescribed through committees whose meetings are noticed to the public. The Supreme Court ruled in *Tumey v. Ohio* (1927) that a judge who has a direct pecuniary interest in the outcome violates due process. Repeat litigants hold systemic advantages (Galanter, 1974), and employees fare worse in arbitration than in court (Colvin, 2011), but the judge cannot rewrite procedural conventions during closing arguments.

In foreign-exchange dealer markets, banks act as both liquidity providers and counterparties on their own platforms. "Last look" lets a dealer hold a client's order briefly and decide whether to accept it; the recitals of a 2015 consent order state that one bank used the practice to reject trades that had moved against it and did not tell clients why (NYDFS, 2015).

Regulators fined five banks £1.1 billion in 2014 for manipulating benchmark rates (FCA, 2014; FSB, 2014). The industry's code followed. The FX Global Code asks dealers to disclose their last-look practice and to agree substantial changes to terms before a transaction (GFXC, 2024, Principles 17 and 40), and adherence to it is voluntary. A soft-law convention holds as far as reputation and the threat of a regulator carry it.

Digital platforms fare worst on the custody test. In all fourteen sets of platform terms that Suzor (2018) examined, the terms "provided broad, unfettered discretion to platform owners," and appeals were thin when Klonick (2018) studied them. Bodies such as the Meta Oversight Board (2022) have narrow remits that do not reach matching algorithms, dynamic pricing, or dispatch interfaces.

Technical standards bodies cannot fill the gap: adoption of their standards is voluntary, and end users take little part in writing them (Nottingham, 2020). If a platform can rewrite its matching conventions with a software update, a designer's promise of "strategic offloading" can be withdrawn whenever margins compress.

### 7.3 External Compulsion and Statutes Beyond Disclosure

Because platforms fail the custody test, Decision Experience Design conventions cannot survive through voluntary designer ethics alone. They require external legal compulsion.

First-generation platform regulations relied largely on disclosure and procedure. The EU Platform-to-Business Regulation (Regulation (EU) 2019/1150) requires fifteen days' notice of changes to terms (Art. 3) and a description of the main ranking parameters (Art. 5), and it states that providers are not required to disclose their algorithms (Art. 5(6)). The Digital Services Act (Regulation (EU) 2022/2065) requires a statement of reasons for restrictions (Art. 17) and an internal complaint-handling system (Art. 20), and gives users a complaint to a regulator and a claim for damages (Arts. 53–54). These measures give notice, reasons, and recourse. They leave the owner free to set the convention.

Recent statutory frameworks are beginning to move beyond disclosure toward structural intervention:

1. The EU Platform Work Directive (Directive (EU) 2024/2831; in force since 1 December 2024; transposition due by 2 December 2026): bans certain processing of personal data (Art. 7); requires a system found to discriminate to be modified or discontinued where appropriate (Art. 10(3)); requires that decisions to restrict, suspend, or terminate an account be taken by a human (Art. 10(5)); requires rectification within two weeks, or compensation, where a decision infringes a worker's rights (Art. 11(3)); and establishes consultation of worker representatives, assisted by an expert (Art. 13). It gives workers no veto.
2. German Works Constitution Act (BetrVG § 87(1) no. 6): grants works councils co-determination over technical systems designed to monitor employee behavior or performance. An employer cannot introduce or modify such a system without works-council agreement or a binding decision of the conciliation committee (§ 87(2)).

These statutes provide the institutional framework needed to sustain DXD conventions. Just as Carolingian scriptoria were directed by royal and ecclesiastical authority to produce correct books, digital platforms will maintain honest representational conventions only when external law removes their power to alter them at will.

## 8. A Research Agenda for Triadic Decision Design

### 8.1 Four Falsifiable Claims

In the manner of a framework and research agenda (Terveen & McDonald, 2005), I set out four claims, each stated so that data could count against it:

- **Claim 1 (Irreducibility).** In a triad comprising Party A, Party B, and Mediator M, a proxy measure of integrated information computed on the joint behavior of all three will exceed the same measure computed on each person–mediator pair, and the excess will shrink when M's determinations are made independent of one party's moves.
  - *Operationalization.* Integrated information (Φ) has so far been applied to human groups only by proxy: Engel and Malone (2018) computed a proxy on who was active when in 68 groups and found it correlated with collective intelligence (r = .37), in groups with no mediator, and Barrett et al. (2026) note that Φ itself has not been computed on a real physical system. I therefore fix the measure, the coding of behavior into discrete states, the time lag, and the partition in advance, validate them on small Boolean models where exact values can be computed, and treat the application to human triads as untested.
- **Claim 2 (Representational conventions outperform textual disclosure).** In a triadic allocation game where Mediator M optimizes an independent objective (J_M ≠ J_A, J_B), representing the system through Convention A (menu-based strategic offloading) produces higher joint surplus and less tactical distortion than full textual rule disclosure.
  - *Operationalization.* The closest precedent is Casella, Friedman, and Perez Archila (2026), where two participants bargain through a computer mediator that maximizes the chance of agreement and shows its rule every round. I give M a margin of its own and compare joint surplus between rulebook arms and menu arms.
- **Claim 3 (Validity governs the sign of feedback immediacy).** The effect of feedback immediacy on error correction depends on mediator noise. Under low noise, continuous feedback speeds convergence; under high noise, continuous feedback degrades choices, and discrete filtered feedback yields higher joint surplus.
  - *Operationalization.* I test the boundary conditions of Larson, List, and Metcalfe (2016) by comparing continuous boundary feedback against discrete-round filtered feedback across high-jitter and low-jitter mediator regimes.
- **Claim 4 (Custodial drift degrades sincere play).** Conventions subject to unannounced mediator parameter drift decay into defensive, manipulative play, whereas conventions the mediator has committed not to change within a session sustain sincere coordination over repeated rounds.

### 8.2 Five-Arm Multi-Agent Experimental Protocol

To test these claims, I specify a controlled laboratory experiment. The protocol follows experimental-economics norms: no false statements to participants (Charness, Samek, & van de Ven, 2022), power calculated at the triad level (the independent unit of observation is the three-node triad, not the individual participant), and joint surplus preregistered as the primary outcome variable.

```
Experimental Architecture (5-Arm Triadic Protocol):

    [ Participant A ] <═══════> [ Mediator M ] <═══════> [ Participant B ]
                                     ║
               Varying Interface / Representation Condition:
    ═════════════════════════════════╬═════════════════════════════════
    Arm 1: Control (Black-Box Interface; Terminal Payout Only)
    Arm 2: Disclosure (Full Written Rulebook, Margin Formulas, Audit Logs)
    Arm 3: DXD Convention A (Ascending Clock / Strategic Offloading Menus)
    Arm 4a: DXD Convention B (Continuous Low-Latency Boundary Contours)
    Arm 4b: Discrete Control (Identical Filtered Feedback Between Rounds)
```

1. Arm 1 (Control — Black-Box): Participants submit raw bids or demands through an unadorned interface, receiving only terminal round payoffs with no explanatory rules.
2. Arm 2 (Literacy — Full Disclosure): Participants receive complete documentation of M's objective function, matching formulas, and an itemized post-round audit log explaining how both inputs were scored.
3. Arm 3 (DXD Convention A — Strategic Offloading): Participants interact with personalized menus where dominant strategies are pre-cleared, visually confirming that strategic undercutting has been removed.
4. Arm 4a (DXD Convention B — Continuous Immediacy): Participants receive real-time, pre-commit visual boundary contours that update as they adjust their sliders, showing clearing odds before commitment.
5. Arm 4b (Discrete Control for Convention B): Participants receive identical noise-filtered boundary data, delivered only at discrete intervals between rounds, isolating the effect of temporal immediacy from informational content.

## 9. Conclusion and Scope Boundaries

### 9.1 Synthesis

Human factors engineering established long ago that when an interface demands heroic human performance, the solution is not to train the person or hand them an instruction manual; the solution is to re-represent the task environment. The scribes of the early Middle Ages demonstrated this on the manuscript page. By replacing continuous script with spaces between words, they changed what a reader had to do with the same letters. They did not alter human biology; they altered the visual geometry of the page.

Today, human–computer interaction and algorithmic regulation stand where reading stood before word separation. Faced with opaque, complex algorithmic intermediaries, our default response has been to demand more literacy: more documentation, more transparency dashboards, more explainability cards, and more post-hoc audit logs.

This is a category error. Rulebooks and rationales treat human beings as readers of algorithms rather than deciders within mediated environments. Navigating irreducible triads requires algorithmacy—an enacted sensibility that operates through epistemic probing and the integration of valid feedback.

Decision Experience Design (DXD) provides an alternative path. By embedding strategic offloading and ecological feedback immediacy directly into the interaction surface, DXD looks for the modern equivalent of the space between words: an interaction architecture that lets people coordinate across algorithms with clarity, autonomy, and agency.

### 9.2 Explicit Scope Boundaries

To ensure theoretical precision, this framework establishes five explicit scope boundaries:

1. Analytical Guide, Not Historical Determinism: Word separation is used strictly as an ergonomic guide for distributed cognition, not as a monocausal explanation of historical literacy or intellectual development (Street, 2003; Scribner & Cole, 1981).
2. Asymmetric Empirical Maturity: Convention A rests on experiments in mechanism design that show a real but partial effect (Li, 2017; Gonczarowski et al., 2024). Convention B and the measurement of triadic integrated information remain hypotheses awaiting the five-arm protocol.
3. Choice Architecture Boundary: DXD is a neighbor of nudging and boosting and must be placed against them (Hertwig & Grüne-Yanoff, 2017). A nudge alters how choices are presented within an unchanged game; DXD changes what the mechanism requires a person to calculate and shows that it has. The nudge literature classes re-presentation of information with informational interventions, the weaker kind (Mertens, Herberz, Hahnel, & Brosch, 2022), and DXD's claim to differ rests on Claim 2.
4. Theoretical Status of Working Disclosures: The argument that working disclosures succeed insofar as they function as simple perceptual signals is this paper's theoretical claim, not an established consensus in prior literature.
5. Institutional Boundary: Interaction conventions cannot withstand commercial pressure without external institutional anchors. Where the Carolingian page was sustained by church and court, modern algorithmic conventions will require statutory co-determination and enforceable legal mandates.

## References

Bai, X., Yan, G., Liversedge, S. P., Zang, C., & Rayner, K. (2008). Reading spaced and unspaced Chinese text: Evidence from eye movements. *Journal of Experimental Psychology: Human Perception and Performance, 34*(5), 1277–1287. https://doi.org/10.1037/0096-1523.34.5.1277

Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., & Weld, D. (2021). Does the whole exceed its parts? The effect of AI explanations on complementary team performance. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. https://doi.org/10.1145/3411764.3445717

Barrett, A. B., Milinkovic, B., Mediano, P. A. M., Rosas, F. E., Bor, D., Barnett, L., & Seth, A. K. (2026). *Integrated information theory: The good, the bad and the misunderstood* [Preprint].

Bassetti, B., & Masterson, J. (2012). Effects of removing morphemic information and adding interword spacing on reading in Chinese experienced and inexperienced readers. *Reading and Writing, 25*(9), 2291–2314. https://doi.org/10.1007/s11145-012-9358-7

Ben-Shahar, O., & Schneider, C. E. (2011). The failure of mandated disclosure. *University of Pennsylvania Law Review, 159*, 647–749.

Bundesministerium der Justiz. (n.d.). *Betriebsverfassungsgesetz (BetrVG)* [Works Constitution Act], § 87.

Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287

Burnyeat, M. F. (1997). Postscript on silent reading. *The Classical Quarterly, 47*(1), 74–76. https://doi.org/10.1093/cq/47.1.74

Cabrera, Á. A., Perer, A., & Hong, J. I. (2023). Improving human-AI collaboration with descriptions of AI behavior. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW1), 1–21. https://doi.org/10.1145/3579612

Cameron, L. D., & Rahman, H. (2022). Expanding the locus of resistance: Understanding the co-constitution of control and resistance in the gig economy. *Organization Science, 33*(1), 38–58. https://doi.org/10.1287/orsc.2021.1557

Casella, A., Friedman, E., & Perez Archila, M. (2026). On the fragility of mediation: Theory and experimental evidence. *Journal of the European Economic Association, 24*(3), 801–850. https://doi.org/10.1093/jeea/jvaf049

Casner, S. M., Geven, R. W., Recker, M. P., & Schooler, J. W. (2014). The retention of manual flying skills in the automated cockpit. *Human Factors, 56*(8), 1506–1516. https://doi.org/10.1177/0018720814535628

CERT National Insider Threat Center. (2022). *Common sense guide to mitigating insider threats* (7th ed.). Software Engineering Institute, Carnegie Mellon University.

Chantavarin, S., & Leung, T. T.-C. (2025). The effects of interword spacing and morphological complexity in reading Thai: An eye-tracking study. *Language and Cognition, 17*. https://doi.org/10.1017/langcog.2025.10028

Charness, G., Samek, A., & van de Ven, J. (2022). What is considered deception in experimental economics? *Experimental Economics, 25*(2), 385–412. https://doi.org/10.1007/s10683-021-09726-7

Chen, L., Mislove, A., & Wilson, C. (2015). Peeking beneath the hood of Uber. In *Proceedings of the 2015 Internet Measurement Conference* (pp. 495–508). ACM. https://doi.org/10.1145/2815675.2815681

Chen, V., Liao, Q. V., Wortman Vaughan, J., & Bansal, G. (2023). Understanding the role of human intuition on reliance in human-AI decision-making with explanations. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW2), 1–32. https://doi.org/10.1145/3610219

Clanchy, M. T. (1993). *From memory to written record: England 1066–1307* (2nd ed.). Blackwell.

Colvin, A. J. S. (2011). An empirical study of employment arbitration: Case outcomes and processes. *Journal of Empirical Legal Studies, 8*(1), 1–23. https://doi.org/10.1111/j.1740-1461.2010.01200.x

Cressy, D. (1980). *Literacy and the social order: Reading and writing in Tudor and Stuart England*. Cambridge University Press.

Cui, Y. (2023). Eye movements of second language learners when reading spaced and unspaced Chinese texts. *Frontiers in Psychology, 14*, Article 783960. https://doi.org/10.3389/fpsyg.2023.783960

Directive (EU) 2024/2831 of the European Parliament and of the Council of 23 October 2024 on improving working conditions in platform work. *Official Journal of the European Union*.

Disley, S., & Khan, H. (2026). Designing cognitive friction with concept suppression in large language models. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2708617

Ehsan, U., Liao, Q. V., Muller, M., Riedl, M. O., & Weisz, J. D. (2021). Expanding explainability: Towards social transparency in AI systems. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–19). ACM. https://doi.org/10.1145/3411764.3445188

Eisenstein, E. L. (1969). The advent of printing and the problem of the Renaissance. *Past & Present, 45*(1), 19–89. https://doi.org/10.1093/past/45.1.19

Engel, D., & Malone, T. W. (2018). Integrated information as a metric for group interaction. *PLOS ONE, 13*(10), Article e0205335. https://doi.org/10.1371/journal.pone.0205335

Financial Conduct Authority. (2014, November 12). *FCA fines five banks £1.1 billion for FX failings and announces industry-wide remediation programme* [Press release].

Financial Stability Board. (2014). *Foreign exchange benchmarks: Final report*.

Fung, A., Graham, M., & Weil, D. (2007). *Full disclosure: The perils and promise of transparency*. Cambridge University Press.

Galanter, M. (1974). Why the "haves" come out ahead: Speculations on the limits of legal change. *Law & Society Review, 9*(1), 95–160. https://doi.org/10.2307/3053023

Gavrilov, A. K. (1997). Techniques of reading in classical antiquity. *The Classical Quarterly, 47*(1), 56–73. https://doi.org/10.1093/cq/47.1.56

Ghalme, G., Nair, V., Eilat, I., Talgam-Cohen, I., & Rosenfeld, N. (2021). *Strategic classification in the dark* [Preprint]. arXiv.

Global Foreign Exchange Committee. (2024). *FX Global Code: A set of global principles of good practice in the foreign exchange market* (December 2024 update).

Gonczarowski, Y. A., Heffetz, O., Ishai, G., & Thomas, C. (2024). *Describing deferred acceptance and strategyproofness to participants: Experimental analysis* (Working Paper No. 33020). National Bureau of Economic Research. https://doi.org/10.3386/w33020

Heilmann, J. (2020). Reading early New Testament manuscripts: Scriptio continua, "reading aids", and other characteristic features. In *Material aspects of reading in ancient and medieval cultures* (pp. 177–196). De Gruyter. https://doi.org/10.1515/9783110639247-011

Herlocker, J. L., Konstan, J. A., & Riedl, J. (2000). Explaining collaborative filtering recommendations. In *Proceedings of the 2000 ACM Conference on Computer Supported Cooperative Work* (pp. 241–250). ACM. https://doi.org/10.1145/358916.358995

Hertwig, R., & Grüne-Yanoff, T. (2017). Nudging and boosting: Steering or empowering good decisions. *Perspectives on Psychological Science, 12*(6), 973–986. https://doi.org/10.1177/1745691617702496

Hohenstein, J., Kizilcec, R. F., DiFranzo, D., Aghajari, Z., Mieczkowski, H., Levy, K., Naaman, M., Hancock, J., & Jung, M. F. (2023). Artificial intelligence in communication impacts language and social relationships. *Scientific Reports, 13*, Article 5487. https://doi.org/10.1038/s41598-023-30938-9

Horvath, A., Liu, M. X., Hendriksen, R., Shannon, C., Paterson, E., Jawad, K., Macvean, A., & Myers, B. A. (2022). Understanding how programmers can use annotations on documentation. In *CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. https://doi.org/10.1145/3491102.3502095

Hutchins, E. (1995). How a cockpit remembers its speeds. *Cognitive Science, 19*(3), 265–288. https://doi.org/10.1207/s15516709cog1903_1

Ishowo-Oloko, F., Bonnefon, J.-F., Soroye, Z., Crandall, J., Rahwan, I., & Rahwan, T. (2019). Behavioural evidence for a transparency–efficiency tradeoff in human–machine cooperation. *Nature Machine Intelligence, 1*(11), 517–521. https://doi.org/10.1038/s42256-019-0113-5

Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. *Journal of Financial Economics, 3*(4), 305–360. https://doi.org/10.1016/0304-405X(76)90026-X

Jhaver, S., Appling, D. S., Gilbert, E., & Bruckman, A. (2019). "Did you suspect the post would be removed?": Understanding user reactions to content removals on Reddit. *Proceedings of the ACM on Human-Computer Interaction, 3*(CSCW), Article 192. https://doi.org/10.1145/3359294

Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist, 64*(6), 515–526. https://doi.org/10.1037/a0016755

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested terrain of control. *Academy of Management Annals, 14*(1), 366–410. https://doi.org/10.5465/annals.2018.0174

Kirsh, D. (1995). The intelligent use of space. *Artificial Intelligence, 73*(1–2), 31–68. https://doi.org/10.1016/0004-3702(94)00017-U

Kirsh, D., & Maglio, P. (1994). On distinguishing epistemic from pragmatic action. *Cognitive Science, 18*(4), 513–549. https://doi.org/10.1207/s15516709cog1804_1

Klonick, K. (2018). The new governors: The people, rules, and processes governing online speech. *Harvard Law Review, 131*, 1598–1670.

Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284. https://doi.org/10.1037/0033-2909.119.2.254

Kluger, A. N., & DeNisi, A. (1998). Feedback interventions: Toward the understanding of a double-edged sword. *Current Directions in Psychological Science, 7*(3), 67–72. https://doi.org/10.1111/1467-8721.ep10772989

Knijnenburg, B. P., Willemsen, M. C., Gantner, Z., Soncu, H., & Newell, C. (2012). Explaining the user experience of recommender systems. *User Modeling and User-Adapted Interaction, 22*(4–5), 441–504. https://doi.org/10.1007/s11257-011-9118-4

Knox, B. M. W. (1968). Silent reading in antiquity. *Greek, Roman, and Byzantine Studies, 9*(4), 421–435.

Körber, M. (2018). *Theoretical considerations and development of a questionnaire to measure trust in automation* [Preprint]. PsyArXiv. https://doi.org/10.31234/osf.io/nfc45

Larson, F., List, J. A., & Metcalfe, R. D. (2016). *Can myopic loss aversion explain the equity premium puzzle? Evidence from a natural field experiment with professional traders* (Working Paper No. 22605). National Bureau of Economic Research. https://doi.org/10.3386/w22605

Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–22). ACM. https://doi.org/10.1145/3706598.3713778

Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50–80. https://doi.org/10.1518/hfes.46.1.50.30392

Lee, M. K., Kusbit, D., Metsky, E., & Dabbish, L. (2015). Working with machines: The impact of algorithmic and data-driven management on human workers. In *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems* (pp. 1603–1612). ACM. https://doi.org/10.1145/2702123.2702548

Li, S. (2017). Obviously strategy-proof mechanisms. *American Economic Review, 107*(11), 3257–3287. https://doi.org/10.1257/aer.20160425

Loewenstein, G., Sunstein, C. R., & Golman, R. (2014). Disclosure: Psychology changes everything. *Annual Review of Economics, 6*, 391–419. https://doi.org/10.1146/annurev-economics-080213-041341

Masuda, T., Mikami, R., Sakai, T., Serizawa, S., & Wakayama, T. (2022). The net effect of advice on strategy-proof mechanisms: An experiment for the Vickrey auction. *Experimental Economics, 25*(3), 902–941. https://doi.org/10.1007/s10683-021-09736-5

*Mathews v. Eldridge*, 424 U.S. 319 (1976).

Matsuo, R., Liu, H., Hiraoka, T., & Wada, T. (2026). An educational human machine interface providing request-to-intervene trigger and reason explanation for enhancing the driver's comprehension of ADS's system limitations. *IEEE Transactions on Human-Machine Systems, 56*(3), 650–661. https://doi.org/10.1109/thms.2026.3679748

Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. *Proceedings of the National Academy of Sciences, 119*(1), Article e2107346118. https://doi.org/10.1073/pnas.2107346118 (Correction published 2022.)

Metzger, U., & Parasuraman, R. (2001). The role of the air traffic controller in future air traffic management: An empirical study of active control versus passive monitoring. *Human Factors, 43*(4), 519–528. https://doi.org/10.1518/001872001775870421

Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E. (2024). Reading between the lines: Modeling user behavior and costs in AI-assisted programming. In *Proceedings of the CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. https://doi.org/10.1145/3613904.3641936

Nadella, S. (2026, October 10). *Models as insider risks in the super intelligence era* [Post]. X. https://x.com/satyanadella/status/2108931348857827686

New York State Department of Financial Services. (2015, November 17). *In the matter of Barclays Bank PLC, Barclays Bank PLC, New York Branch: Consent order under New York Banking Law § 44*.

Norman, D. A. (1988). *The psychology of everyday things*. Basic Books.

Nottingham, M. (2020). *The Internet is for end users* (RFC 8890). Internet Architecture Board.

Nouwens, M., Liccardi, I., Veale, M., Karger, D., & Kagal, L. (2020). Dark patterns after the GDPR: Scraping consent pop-ups and demonstrating their influence. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. https://doi.org/10.1145/3313831.3376321

Oberschelp, W. (1995). Developing analytical competency through informatics teaching. In D. Watson & D. Tinsley (Eds.), *Integrating information technology into education* (pp. 115–126). Springer. https://doi.org/10.1007/978-0-387-34842-1_12

Oversight Board. (2022). *Q1 2022 transparency report*.

Özçetin, S., & Wiltse, H. (2023). Terms of entanglement: A posthumanist reading of Terms of Service. *Human–Computer Interaction, 40*(1–4), 171–194. https://doi.org/10.1080/07370024.2023.2281928

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors, 52*(3), 381–410. https://doi.org/10.1177/0018720810376055

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics—Part A: Systems and Humans, 30*(3), 286–297. https://doi.org/10.1109/3468.844354

Parkes, M. B. (1992). *Pause and effect: An introduction to the history of punctuation in the West*. Scolar Press.

Poursabzi-Sangdeh, F., Goldstein, D. G., Hofman, J. M., Wortman Vaughan, J., & Wallach, H. (2021). Manipulating and measuring model interpretability. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (Article 237). ACM. https://doi.org/10.1145/3411764.3445315

Pucci, E., Piro, L., & Matera, M. (2027). From tabbing to talking: LLM-driven conversational agents for web form interaction. *International Journal of Human-Computer Studies, 218*, Article 103925. https://doi.org/10.1016/j.ijhcs.2026.103925

Rahman, H. A. (2019). *Invisible cages: Algorithmic evaluations in online labor markets* [Doctoral dissertation, Stanford University].

Rahmandad, H., & Gary, M. S. (2023). Delays impair learning and can drive convergence to inefficient strategies. *Organization Science, 34*(6), 2392–2414. https://doi.org/10.1287/orsc.2020.1405

Rayner, K., Fischer, M. H., & Pollatsek, A. (1998). Unspaced text interferes with both word identification and eye movement control. *Vision Research, 38*(8), 1129–1144. https://doi.org/10.1016/S0042-6989(97)00274-5

Regulation (EU) 2019/1150 of the European Parliament and of the Council of 20 June 2019 on promoting fairness and transparency for business users of online intermediation services. *Official Journal of the European Union*.

Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 on a Single Market For Digital Services (Digital Services Act). *Official Journal of the European Union*.

Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences, 20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002

Rules Enabling Act, 28 U.S.C. § 2073.

Saenger, P. (1997). *Space between words: The origins of silent reading*. Stanford University Press.

Schemmer, M., Hemmer, P., Nitsche, M., Kühl, N., & Vössing, M. (2022). A meta-analysis of the utility of explainable artificial intelligence in human-AI decision-making. In *Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society* (pp. 617–626). ACM. https://doi.org/10.1145/3514094.3534128

Scribner, S., & Cole, M. (1981). *The psychology of literacy*. Harvard University Press.

Seira, E., Elizondo, A., & Laguna-Müggenburg, E. (2017). Are information disclosures effective? Evidence from the credit card market. *American Economic Journal: Economic Policy, 9*(1), 277–307. https://doi.org/10.1257/pol.20140404

Sheridan, T. B., & Verplank, W. L. (1978). *Human and computer control of undersea teleoperators* [Technical report]. Massachusetts Institute of Technology, Man-Machine Systems Laboratory. https://doi.org/10.21236/ada057655

Shneiderman, B. (1983). Direct manipulation: A step beyond programming languages. *Computer, 16*(8), 57–69. https://doi.org/10.1109/mc.1983.1654471

Simkute, A., Tankelevitch, L., Kewenig, V., Scott, A. E., Sellen, A., & Rintel, S. (2024). Ironies of generative AI: Understanding and mitigating productivity loss in human-AI interaction. *International Journal of Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2024.2405782

Street, B. V. (2003). What's "new" in New Literacy Studies? Critical approaches to literacy in theory and practice. *Current Issues in Comparative Education, 5*(2), 77–91.

Suzor, N. (2018). Digital constitutionalism: Using the rule of law to evaluate the legitimacy of governance by platforms. *Social Media + Society, 4*(3). https://doi.org/10.1177/2056305118787812

Terveen, L., & McDonald, D. W. (2005). Social matching: A framework and research agenda. *ACM Transactions on Computer-Human Interaction, 12*(3), 401–434. https://doi.org/10.1145/1096737.1096740

*Tumey v. Ohio*, 273 U.S. 510 (1927).

Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour, 8*(12), 2293–2303. https://doi.org/10.1038/s41562-024-02024-1

Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations can reduce overreliance on AI systems during decision-making. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW1), Article 129. https://doi.org/10.1145/3579605

Weick, K. E. (1988). Enacted sensemaking in crisis situations. *Journal of Management Studies, 25*(4), 305–317. https://doi.org/10.1111/j.1467-6486.1988.tb00039.x

Westwell, A. (2018). *The dissemination and reception of the Ordines Romani in the Carolingian church, c. 750–900* [Doctoral dissertation, University of Cambridge]. https://doi.org/10.17863/cam.23255

Winskel, H., Radach, R., & Luksaneeyanawin, S. (2009). Eye movements when reading spaced and unspaced Thai and English: A comparison of Thai–English bilinguals and English monolinguals. *Journal of Memory and Language, 61*(3), 339–351. https://doi.org/10.1016/j.jml.2009.07.002

Wischnewski, M., Krämer, N., & Müller, E. (2023). Measuring and understanding trust calibrations for automated systems: A survey of the state-of-the-art and future directions. In *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems*. ACM.

Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review, 28*(4), 1060–1092. https://doi.org/10.3758/s13423-020-01859-9

Zhang, J., & Norman, D. A. (1994). Representations in distributed cognitive tasks. *Cognitive Science, 18*(1), 87–122. https://doi.org/10.1207/s15516709cog1801_3

---

## Changes from version 1 (Claude's notes; not part of the paper)

**Reference list.** Rebuilt. Thirty-nine entries were replaced with the published record (the full table
is in `REVIEW_v2_2026-10-13.md` §2a). Entries the text never cited were removed (Arteaga et al.; Ashlagi
& Gonczarowski; Balkin; Bar-Gill et al.; Bechavod et al.; Brehmer & Nählinder; Crabtree; Dietvorst et
al.; Dix; Douek; Hardt et al.; Lee & Moray; Rees-Jones & Skowronek; Scaife & Rogers; Thorgeirsson et al.;
Vicente & Rasmussen; Wickens & Carswell). Entries were added for every work the text cites. Three
citations were removed because no record could be found or the record did not match the claim:
Kosmyna et al. (2025), Thorgeirsson et al. (2026), and Sáenz & De Russis (2027), whose only Crossref
match is a paper with a different title.

**Statements corrected against their sources.**

| Section | Version 1 | Version 2 |
| --- | --- | --- |
| 1, 4.2 | Repayment disclosures "increased delinquency among borrowers"; "Mexican credit card companies"; "made the debt feel insurmountable" | One bank's messages; delinquency rose for two client groups by 0.011 points (7.4% of the mean); the invented mechanism is removed |
| 1, 4.2 | "High-interpretability models impaired users' ability to correct anomalous model mistakes"; "an illusion of competence" | A clear model left users less able to correct the mistake on an unusual case, in three of four experiments; the authors' own conjecture (overload) is given |
| 4.2 | Explained removals judged less fair than unexplained ones | Rule-readers judged removal less fair (β = −.314); those given an explanation judged it fairer (β = .384) |
| 4.2 | Layout shifted consent "by orders of magnitude"; text "produced no detectable effect" | Removing the opt-out button raised consent by 22 to 23 points; the claim about text is removed |
| 1, 4.2 | "Explanations do not improve decision performance on average (Vaccaro…)" | Schemmer et al. for the average effect; Vaccaro et al. for explanation not moderating performance |
| 3.1 | Reading "confined to an elite, highly trained scribal caste"; Insular languages "shared no linguistic roots with Latin"; distinctiones and "codex page indexing" standardized by the eleventh century | Saenger's claims attributed to him and marked as disputed; Insular scribes learned Latin as a foreign language; the unsourced details are removed; his p. 85 sentence is quoted |
| 3.2 | Boundary detection in "the phonological loop"; saccade claims unsourced | Marked as this paper's interpretation; landing-position effect cited to Rayner et al. |
| 3.3 | Spaces help children and learners; spaces slow skilled Chinese readers (Bai) | Bai: no difference; Thai: faster words, slower sentences; child learners worse (Bassetti & Masterson); adult learners not significant (Cui) |
| 3.3, 7.3 | Carolingian edicts cited to Westwell; scribes "held accountable to readers" | The three primary texts named; Westwell's caution added; a sentence states that none concerns word separation |
| 4.1 | A quotation from Ben-Shahar & Schneider not found at p. 665; "a bright caloric label" | Their mechanism paraphrased from p. 665; their own example (restaurant grades) with its hedge |
| 4.1 | Only Target 4 said to fail, while the thesis condemned all disclosure | The abstract, introduction and 4.1 now locate the category error in Target 4 and say why Target 3 differs |
| 4.3 | "Three pillars"; "halt switches" in quotation marks; affected people "handed the… audit log" | Seven principles, three of which bear on a person; his emergency-brake image; affected people are promised "timely disclosure" |
| 5.1 | Oberschelp "treated algorithmacy as elementary procedural programming literacy" | His one sentence quoted (p. 121); undefined; a hand-computation skill |
| 5.2 | Drivers with a second phone driving "two blocks north"; Ghalme et al. cited for sharing screenshots | What Lee et al. and Kellogg et al. report; Ghalme et al. cited for inferring a hidden rule from others' outcomes |
| 5.3 | Kahneman & Klein quoted beyond the verified words; platforms "deliberately disrupt ecological validity"; "an engineering synchronization bug in their geospatial grid" | Only "feedback that is both rapid and unequivocal" is quoted; intent is claimed for secrecy and denied for noise; the bug is Uber's own account |
| 5.3 | Rahmandad & Gary: failure "even after hundreds of trials… superstitious heuristics" | Delay and noise have different effects, as the paper reports |
| 6.2 | "Comprehension from 56% to 71%. Sincere play increased from 48% to 59%" | Understanding 71% against 58% and 56%; play 59% against 56% (not significant) and 48% (control) |
| 6.2 | Masuda et al. "pairing a structural representation with a clear confirmation" | A statement that sincere bidding is dominant; 20.6% to 46.9%; efficiency up about one point |
| 6.3 | Larson et al. in the *Journal of Finance*; "financial traders… real-time price telemetry" | An NBER working paper on professional traders; second-by-second against four-hourly prices |
| 7.2 | Code followed by fines; Principles 7, 9, 36, 39, 40 "governing last-look and pre-hedging" | Fines in 2014–15, Code afterward; Principle 17 for last look and the others for what they cover |
| 7.2 | RFC 8890 "explicitly declare[s]" standards do not bind platforms | Standards are voluntary and end users take little part; cited to Nottingham (2020) |
| 7.3 | P2B and DSA "merely" require plain-language description, "changing nothing" | Their notice, reasons, complaint and damages provisions stated; P2B's no-algorithm-disclosure clause added |
| 7.3 | Directive article summaries without their qualifiers | "Where appropriate" (Art. 10(3)); rights infringed (Art. 11(3)); no veto |
| 8.1 | Claim 1: "strictly positive integrated information (Φ > 0) that cannot be factored" | A comparison the data could fail, with the proxy status of the measure stated |
| 8.1 | Claim 4: "verifiable cryptographic or co-governance lock-in" | A commitment not to change the convention within a session |
| 9.1 | "where reading stood before the eighth century" | "before word separation" |
| 9.2 | Convention A "rests on established empirical mechanism design"; one sentence on nudging | "A real but partial effect"; nudge and boost named as the neighbor, with Mertens et al.'s classification |

**Structure and voice.** The roadmap is prose. Where "we" meant the author it is now "I"; the inclusive "we" that addresses the reader is kept. Convention B is "ecological
feedback immediacy" everywhere. The claim that HCI is dyadic is narrowed to transparency research, with
AI-mediated communication acknowledged. "Importantly," and "Notably," are removed. The diagrams are kept
as they were, inside code blocks; they still need redrawing as figures.

**Not done.** The paper is not lengthened. The body runs to about 7,600 words excluding diagrams and references, against 9,000 to 17,000 in the four recent articles read from the journal. Sections
2, 5 and 7 are the ones to grow.

## Still unverified (Claude's notes; not part of the paper)

- **Records confirmed at Crossref, texts not read.** The sentences that cite these rest on the earlier
  draft's description of them: Herlocker et al. (2000); Knijnenburg et al. (2012); Wischnewski et al.
  (2023; Crossref shows the preprint, and the CHI venue is from the draft); Ehsan et al. (2021); Lee &
  See (2004); Körber (2018); Bansal et al. (2021); Chen et al. (2023); Metzger & Parasuraman (2001);
  Casner et al. (2014); Mozannar et al. (2024); Simkute et al. (2024); Lee et al. (2025); Horvath et al.
  (2022); Pucci et al. (2027); Sheridan & Verplank (1978); Wolfe (2021); Hohenstein et al. (2023, carded
  for a different point); Eisenstein (1969).
- **Terveen & McDonald (2005)** is cited as the form the agenda follows and has not been read.
- **Norman (1988)** is cited for the gulfs of execution and evaluation and has not been opened.
- **Rayner et al. (1998)** was read as an abstract only.
- **Saenger (1997) and Parkes (1992).** Saenger's quoted wording is confirmed; his pages need a print
  check. Parkes is known from snippets.
- **Rahman (2019)** is the dissertation; the published article (2021) was not opened.
- **Gonczarowski et al. (2024), Larson et al. (2016)** were read as working papers.
- **Barrett et al. (2026)** is a preprint; the bibliography holds no DOI or archive number for it.
- **The interface mock-ups and their numbers** (rates, tiers, "P(Match) = 88%") are illustrations.
