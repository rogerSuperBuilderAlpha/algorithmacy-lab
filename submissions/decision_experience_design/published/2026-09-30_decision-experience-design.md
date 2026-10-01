---
title: "Decision Experience Design"
subtitle: "Yes, another XD"
author: Roger Hunt
published: 2026-09-30
url: https://rogerhuntphdcand.substack.com/p/decision-experience-design
source: Substack API body_html, converted with pandoc (gfm) on 2026-10-01
note: Final published text. The live post is authoritative; REVIEW.md is the earlier Claude draft.
---

# Decision Experience Design

*Yes, another XD*

*This is 61% AI written according to Pangram, but I assure you it is 100% AI produced.\
Claude researched and wrote a terrible draft. Then Grokbot took forever to fix it so I put it in Gemini, and got a 39% human score!*\
\
Practitioners across product strategy and design consultancies have recently rallied around a new moniker: decision experience design, or DXD. In trade posts, white papers, and agency manifestos, the label is heralded as the natural successor to user experience (UX) design, promising a disciplined approach to how software guides, accelerates, or automates human choice. Yet academic databases reveal an utter void. Across OpenAlex, Crossref, arXiv, and Semantic Scholar, the term has virtually no scholarly footprint. The trade vocabulary has outpaced its theoretical foundations.

This absence does not mean the underlying work is novel. For over seven decades, human factors engineers, cognitive scientists, and behavioral economists have systematically designed the environments in which people decide. They simply did so under different banners: choice architecture, decision support systems, cognitive systems engineering, and human-AI decision research. Bridging this divide requires examining both the history of interaction design and the shifting nature of computational mediation. User experience design became an established cognitive profession by importing empirical findings from psychology—motor limits, visual saccades, working-memory thresholds—and translating them into ergonomic design rules. At each historical juncture, the field reorganized as its core unit of analysis expanded, migrating from the physical keystroke to the visual glance, the structured task, and the organizational workspace.

When human choices are mediated by opaque, adaptive algorithms that coordinate multiple parties and commit binding outcomes, the unit of analysis moves once more: from the task to the decision itself. The cognitive demands of this environment cannot be solved through the traditional UX toolkit of legibility, visual layout, and cognitive load reduction. Deciding through an adaptive intermediary requires a distinct competence: algorithmacy. Two foundational premises govern this inquiry. First, algorithmacy is not legibility; merely exposing an algorithm’s inner workings or appending post-hoc explanations fosters user awareness without conferring agency. Second, the transition from literacy to algorithmacy follows the psychometric model of numeracy, not the cultural ontology of Walter Ong. The claim is not that algorithmic interfaces fundamentally rewire human consciousness. Rather, like numeracy, algorithmacy represents a measurable, domain-specific competence that predicts decision quality over and above general cognitive ability. Decision experience design can emerge as a legitimate discipline only if it grounds itself in this competence, acting as the custodian of human agency within algorithmic coordination.

## The Practitioner Vernacular and Its Academic Neighbors

The phrase began surfacing in industry discussions in late 2023. In Jakarta, product designer Ajeng Restu Putri confronted an activation rate stalled at 14.8% on an educational platform for teachers. When her team eliminated the free trial and lowered the upfront entry fee, activation jumped to 50.6%. Putri (2025) framed the breakthrough not as an interface overhaul, but as an exercise in decision experience design. Around the same time, Matthew Wilkinson (2023), CEO of streaming infrastructure firm Magine Pro, invoked Decision Experience (DX) to address choice paralysis in content catalogs, arguing that an excess of options paralyzes viewers unless interfaces actively scaffold the decision moment. Similar formulations quickly appeared in industry commentary (Pastagia, 2026) and executive forums (Danish-Swiss Chamber of Commerce, 2026).

These practitioner framings split along two operational axes. On one side are outward-facing conversions, where practitioners focus on consumer choice, friction reduction, catalog filtering, and sales funnels (Putri, 2025; Wilkinson, 2023; Pastagia, 2026). On the other lies an inward-facing enterprise logic oriented toward workflow architecture. Andrew Audry (n.d.) describes DX as structuring internal organizational decisions to make them “system-ready,” while the Chilean consultancy Itera (2025) defines DX as the deliberate design of the decision moment, quantified primarily through time-to-decision. Itera acknowledges the core limitation: the practice still lacks an empirical framework comparable to UX.

Scholarly literature has long analyzed the decision as a primary design unit, albeit through distinct lenses. Decision-Centered Design, originating in cognitive engineering (Wolf, Klein, & Thordsen, 1991; O’Hare et al., 1998; Hutton, Miller, & Thordsen, 2003; Militello & Klein, 2013), extracts requirements from experienced operators via Critical Decision Method interviews to build interfaces supporting high-stakes operational choices. Its user is the domain expert managing complex physical systems. Choice architecture and digital nudging, developed by behavioral economists and information systems researchers, frame the interface designer as an architect structuring choice environments to guide behavior without restricting options (Thaler & Sunstein, 2008; Johnson et al., 2012; Weinmann, Schneider, & vom Brocke, 2016; Schneider, Weinmann, & vom Brocke, 2018). Within enterprise engineering and applied data science, decision intelligence integrates process modeling with machine learning to systematize commercial pipelines (Pratt, 2019; Hasić, De Smedt, & Vanthienen, 2018). Marketing research tracks the consumer decision journey across touchpoints from brand awareness to post-purchase evaluation, though its classical models struggle when confronted with autonomous algorithms (Santos & Gonçalves, 2021). Meanwhile, experimental decision psychology isolates the subjective experience of choosing—evaluating perceived difficulty, regret, and satisfaction under conditions of “hyperchoice”—and demonstrates that subjective friction is heavily moderated by numeric competence (Peterson & Cheng, 2022).

The closest conceptual neighbor in human-computer interaction is algorithmic experience, or AX. Oscar Alvarado Rodríguez (2017) and Alvarado and Waern (2018) introduced AX to capture how non-human computational actors alter user experience, proposing design dimensions around algorithmic awareness, profiling transparency, and user control. Shin, Zhong, and Biocca (2020) subsequently positioned AX as operating beyond user experience. Yet AX remains centered on a single user confronting an isolated system. The remedies it offers—preference sliders, transparency toggles, and profile management—are designed to make an automated system legible to an individual.

Decision experience design departs from these precursors at a fundamental structural boundary: the triadic intermediary. In decision-centered design, the system is an instrument commanded by an expert. In choice architecture, the environment is arranged by an identifiable human designer. In algorithmic experience, a lone user interacts with a platform feed. DXD, by contrast, must address situations where choices are brokered through an adaptive, opaque algorithmic intermediary that reads multiple parties simultaneously and commits binding determinations that neither party fully controls.

## Choice Architecture and Its Algorithmic Turn

The intellectual foundation that practitioner DXD casually borrows is choice architecture. Herbert Simon (1956) observed that human rationality is shaped by a pair of scissors, with the cognitive capabilities of the actor forming one blade and the structure of the task environment forming the other. Tversky and Kahneman (1981) demonstrated that subtle variations in how options are framed systematically invert human preferences. Thaler and Sunstein (2008) converted these cognitive biases into an active organizational role—the choice architect—and Johnson et al. (2012) codified the architect’s levers into structural tools, such as defaults and option sequencing, alongside descriptive tools like framing and attribute partitioning.

When software designers migrated this toolkit online, digital nudging was born (Weinmann et al., 2016; Schneider et al., 2018). Every time an interface sets a pre-selected checkbox, spotlights a subscription tier, or sorts a catalog by margin, it engages in choice architecture. Yet this lineage carries an ethical shadow. Practitioner tactics easily slide into dark patterns—interface mechanisms intentionally engineered to subvert user intent for commercial extraction (Gray et al., 2018). Large-scale audits by Mathur et al. (2019) revealed thousands of manipulative patterns across e-commerce platforms, sold as turnkey commercial widgets. Mathur, Kshirsagar, and Mayer (2021) subsequently demonstrated how these patterns systematically exploit cognitive limitations to impair user autonomy.

Where classic choice architecture features an identifiable human designer deploying a fixed interface or default menu to steer an isolated chooser, modern algorithmic environments alter the entire topology. A platform objective governs an adaptive intermediary, which continually ingests behavioral telemetry from multiple sides of an ecosystem—such as workers and consumers on an on-demand labor platform—and issues policy-bound determinations that govern both parties at once.

Worse still for a nascent design discipline, the empirical foundation of behavioral nudging has shown signs of structural fragility. Mertens et al. (2022) published a meta-analysis claiming a robust average nudge effect size (\$d = 0.43\$). Subsequent re-analyses correcting for severe publication bias found the true effect to be statistically indistinguishable from zero (Maier et al., 2022) or hovering at negligible magnitudes between \$d = 0.01\$ and \$d = 0.08\$ (Szaszi et al., 2022). DellaVigna and Linos (2022) compared academic trials against 126 interventions deployed by professional government nudge units, finding that academic effect sizes of 8.7 percentage points shrank to 1.4 points in field deployments. Foundational heuristics show similar volatility: choice overload effects frequently wash out in large replications (Scheibehenne, Greifeneder, & Todd, 2010; Chernev, Böckenholt, & Goodman, 2015), and the canonical default effect replicates at substantially lower rates than originally claimed (Chandrashekar et al., 2023).

The consensus among decision scientists is that heterogeneity—not the aggregate mean—is the primary finding. Nudge efficacy depends on domain complexity, baseline individual competencies, and local environmental friction. Any version of DXD that markets itself as a collection of plug-and-play nudge heuristics builds on shaky ground.

Contemporary computing has dismantled the classical premises of choice architecture: a visible human designer, a static menu, and a single chooser. Karen Yeung (2017) identified this transformation in the hypernudge, an algorithmic environment dynamically assembled in real time from personal behavioral tracking and population-level predictive models. Mills and Sætra (2024) take this further with the concept of the autonomous choice architect, where automated optimizers run continuous multi-armed bandits to select interface configurations that maximize platform-level engagement metrics. In this environment, the human designer is obscured behind an optimization objective (Mills, 2022). The menu ceases to be an inspectable list; it becomes a dynamic, personalized stream. Classic choice architecture universally assumes an isolated actor facing an isolated display. It offers no model for multi-party algorithmic coordination—such as ride-hailing networks or labor marketplaces—where an intermediary digests data from multiple actors and assigns tasks or compensation under proprietary objective functions (Calo & Rosenblat, 2016; Mathur et al., 2021).

The most viable behavioral alternative to nudging is boosting (Hertwig & Grüne-Yanoff, 2017). Rather than exploiting heuristic vulnerabilities to steer behavior, boosts build procedural competencies that persist after the intervention is withdrawn. Researchers have adapted boosting to online spaces through interventions that foster deliberative reflection and lateral reading (Kozyreva, Lewandowsky, & Hertwig, 2020; Callaway et al., 2022). Yet digital boosting remains framed primarily around information literacy—teaching users to interrogate sources and assess claims. It does not address the operational realities of algorithmacy: how an actor formulates intent through constrained interface channels, audits an opaque mediator, and anticipates rule changes in an adaptive system.

## Cognitive Systems Engineering and the Breakdown of the Joint System

Long before graphical operating systems existed, engineers designed systems to support complex organizational and industrial choices. Gorry and Scott Morton (1971) established that where decision logic cannot be mathematically formalized, computational tools must support human judgment rather than supplant it. This realization spawned Decision Support Systems (DSS) as an enterprise discipline (Keen & Scott Morton, 1978; Sprague, 1980; Arnott & Pervan, 2005, 2014).

Cognitive Systems Engineering (CSE) subsequently introduced a rigorous model of human operators managing high-stakes, safety-critical environments. Gary Klein’s Naturalistic Decision Making framework established that experts rely on rapid pattern matching—formalized in the Recognition-Primed Decision (RPD) model—rather than exhaustive calculation (Klein, 1993, 2008). Applied Cognitive Task Analysis and decision-centered methods emerged to map these perceptual cues directly into interface layouts (Militello & Hutton, 1998; Crandall, Klein, & Hoffman, 2006). Ecological Interface Design (EID) took the concept to its logical conclusion, translating the invariant physical laws of complex systems, such as thermodynamic boundaries in power plants, directly into visual geometry so that visual perception could navigate abstract constraints (Vicente & Rasmussen, 1992).

Three foundational principles from CSE apply directly to decision experience design. First, the unit of analysis is the decision, not the screen. Second, evaluation must measure the performance of the joint cognitive system, not the software in isolation (Hollnagel & Woods, 1983; Woods & Hollnagel, 2006). Third, computational tools must aid the process of deliberation rather than simply prescribing a solution (Woods, 1985). David Woods (1985) issued an early warning about systems that bypass deliberation: when an automated agent gathers data invisibly and offers a take-it-or-leave-it conclusion, the human operator is demoted to a passive “solution filter.” Stripped of situational awareness yet carrying institutional accountability, the human is caught in an unsustainable responsibility-authority double-bind.

The core challenge for modern interface design is that algorithmic mediation invalidates the foundational premises of Cognitive Systems Engineering across four distinct dimensions. Where classical CSE domains rely on highly trained expert operators working in dedicated task spaces governed by transparent physical laws and symmetric goal alignment, modern algorithmic environments deploy proprietary, statistical rules over multi-sided platforms to govern untrained, everyday users whose objectives conflict with the platform’s bottom line.

Vicente and Rasmussen (1992) built EID explicitly for highly trained operators. Today’s algorithmic intermediaries govern everyday citizens navigating gig work, e-commerce, and algorithmic social spaces (Janssen et al., 2019; Carsten & Martens, 2019). When systems present complex recommendations to non-experts, users frequently swing between extreme automation bias—rubber-stamping bad automated advice (Banker & Khetani, 2019)—and knee-jerk algorithm aversion (Allen & Choudhury, 2022). Furthermore, EID assumes the system’s operational constraints are governed by immutable physical laws known to the designer. Modern machine-learning intermediaries, by contrast, are stochastic, high-dimensional, and continuously retrained on moving distributions.

This instability undermines the designer’s own footing. EID operates only to the extent that designers understand the system they are building (Vicente & Rasmussen, 1992). In modern software environments, product designers rarely comprehend the complex policies running inside an optimization model. Worse still is the breakdown of goal alignment. Classic engineering assumes the machine and the operator share operational goals. Klein et al. (2004) characterized joint activity as requiring a “Basic Compact” of mutual commitment and goal alignment, while Lee and See (2004) indexed appropriate trust directly to how well automation serves user goals. An algorithmic intermediary deployed by an on-demand labor platform or ad-driven network does not share its users’ goals; it optimizes for platform-level objective functions (Herath Pathirannehelage, Shrestha, & von Krogh, 2025).

This structural misalignment undermines the conditions necessary to develop genuine decision-making expertise. Kahneman and Klein (2009) established that intuitive decision-making skill can develop only when two environmental conditions are met: the task environment must possess high validity and predictability, and the decision maker must receive rapid, unequivocal feedback to learn those regularities. An adaptive algorithmic intermediary systematically disrupts both requirements. Its underlying policies drift across retrainings, and its feedback is partial, delayed, and mediated through platform metrics. Decades earlier, Lisanne Bainbridge (1983) noted that operational competence erodes when systems obscure system states, because process knowledge develops solely through continuous, transparent feedback. Donald Norman (1990) added that automated systems routinely discard this feedback loop simply because the automation does not require it for its own mathematical operation.

Operating inside an adaptive, low-validity platform environment creates an illusion of competence: users gain superficial familiarity with an interface without developing calibrated decision accuracy. Bainbridge’s (1983) proposed remedy in “Ironies of Automation” provides the foundational insight for an ethical approach to DXD. When a computational system uses more parameters and more rapid criteria than a human can process, monitoring becomes impossible. The remedy is not to demand that the user study harder or read more complex displays. The system itself must be constrained to operate within parameters, criteria, and cadences that human perception can track, and it must be built to fail conspicuously.

## The Ergonomic Genealogy: How Interaction Design Built Its Science

The emergence of UX design as a recognized profession provides an operational blueprint for DXD. Human-Computer Interaction (HCI) did not establish itself through generalized creative intuition. It systematically imported targeted findings from cognitive science and human factors, converting psychomotor measurements into interface rules.

This importation unfolded across three distinct operational layers. At the level of physical motor movement, Paul Fitts (1954) modeled the information capacity of human motor systems, showing that movement time is a function of target distance and width. Hick (1952) and Hyman (1953) demonstrated that decision reaction time scales logarithmically with the number of available alternatives. MacKenzie (1992) leveraged these laws to optimize pointing devices, and Card, Moran, and Newell (1980, 1983) synthesized them into the Keystroke-Level Model and the Model Human Processor, inaugurating the information-processing paradigm of HCI (Harrison, Tatar, & Sengers, 2007).

At the visual level, vision science transformed screen typography and information layouts. Healey and Enns (2012) mapped pre-attentive visual features to interface design, Buscher, Cutrell, and Morris (2009) utilized eye tracking to predict visual saliency across web layouts, Dyson (2004) established optimal line lengths for reading performance, and MacLean (2008) extended these perceptual principles to haptic feedback.

At the level of the task, cognitive psychology restructured interface workflows around human processing limits. Hutchins, Hollan, and Norman (1985) modeled direct manipulation through two operational divides: the gulf of execution, which captures the cognitive effort required to translate internal intent into system actions, and the gulf of evaluation, which reflects the effort required to assess system state from interface cues. Hollender et al. (2010) integrated cognitive load theory directly into interface architecture, framing clunky navigational layouts as extraneous cognitive load that exhausts working-memory bandwidth.

Jonathan Grudin (1990) documented the structural logic of this historical evolution, showing that the computer interface continually moves outward from the physical hardware. The discipline began at the hardware level in microseconds, anchored by ergonomics and electrical engineering, before moving to software systems in milliseconds, display terminals in seconds via psychomotor factors and Fitts’s Law, dialogue and structured tasks in minutes via cognitive psychology, and broad work settings over days or months through social psychology and distributed cognition. The decision moment, spanning days to quarters within algorithmic coordination, marks the sixth level of this historical outward expansion.

At every shift, the field required new specialist disciplines, distinct evaluative methodologies, and an expanded unit of analysis. Hollan, Hutchins, and Kirsh (2000) framed this trajectory through distributed cognition, arguing that the proper unit of analysis is never the isolated user or the static screen, but the functional relationships binding tools, actors, and representational media. This progression confirms an early human factors forecast: in a 1951 analysis on function allocation, Paul Fitts predicted that as machines assumed routine mechanical and computational labor, the study of human performance would center on reasoning, judgment, planning, and decision making (de Winter & Dodou, 2014). The emergence of the decision as the core unit of interface design fulfills this trajectory.

Two caveats must qualify this history. The first is the perpetual risk of empirical distortion into design folklore. Scientific principles frequently degraded into dogmatic folklore when untethered from their empirical boundary conditions. George Miller’s (1956) classic paper on short-term memory limits was flattened into an industry mandate that web navigation menus should never exceed seven items—a claim Miller never made and one that empirical research proved counterproductive for deep menu structures (Cowan, 2001, 2015; Doumont, 2002; Commarford et al., 2008). Similarly, Pernice (2017) demonstrated that the vaunted “F-shaped reading pattern” is an artifact of poorly formatted, wall-to-wall text scanned by hurried readers, not an innate physiological scanning law. Decision experience design faces an identical hazard: reifying fragile early nudge heuristics into unbending interface dogmas.

The second caveat concerns the actual distribution of expertise. UX practitioners were rarely trained cognitive psychologists. Job analyses reveal that the market prioritized visual craft, prototyping tools, and front-end code (González, Ghazizadeh, & Smith, 2014; Lallemand, Gronier, & Koenig, 2015). Scientific knowledge lived in the field’s research centers, specialist handbooks, and design systems, trickling into daily workflows as design patterns and heuristic checklists. DXD requires a comparable structure: a grounded academic foundation in decision science and intermediary dynamics, translated into operational tools for working designers.

Theoretical discussions around the post-AI interface remain fractured. Chignell et al. (2023) suggest HCI must merge with classic human factors under a paradigm of human augmentation, while Forlizzi (2018) advocates for stakeholder-centered design, acknowledging that systems coordinate webs of individuals rather than serving isolated users. Yet neither framing establishes the user’s competence in navigating an intermediary as the primary design target. Both preserve the classical assumption of the gulf of evaluation: that the system’s state can be legibly represented to a passive reader. The empirical realities of modern algorithmic mediation reveal the breakdown of that assumption.

## The Triadic Intermediary: Three Cognitive Operations of Algorithmacy

Deciding through an algorithmic system imposes cognitive demands that research on reading, visual layout, and cognitive load cannot resolve. The scale of this dysfunction is documented in recent empirical meta-analyses. Vaccaro, Almaatouq, and Malone (2024) synthesized 370 effect sizes across 106 experiments evaluating human-AI collaboration. They discovered that across empirical trials, hybrid human-AI teams performed significantly worse than the best solo performer, whether human or machine alone (\$g = -0.23\$). This collaborative penalty was most pronounced in decision-making tasks (\$g = -0.27\$). Neither post-hoc explanations nor confidence scores alleviated the penalty; the deciding factor was task structure and relative baseline capability.

Navigating this friction requires three core operations: interpreting, specifying intent, and keeping track. Interpreting demands inferring operational boundaries and counterpart intent from partial, composite system feedback. Specifying intent requires projecting authentic goals through constrained, standardized, and indirect interface channels. Keeping track involves detecting model drift, policy updates, and behavioral shifts across time in an evolving intermediary.

When users encounter an algorithm, their interpretation relies on intuitive explanatory models—what Logg, Minson, and Moore (2019) identify as a “theory of machine.” These representations develop largely outside the interface. Eslami et al. (2015) revealed that 62.5% of surveyed social media users were completely unaware that an automated curation algorithm controlled their feeds. In the absence of clear cues, users formulate idiosyncratic “folk theories” (Eslami et al., 2016; DeVito et al., 2018; Bucher, 2017). These mental models feed back into the system: users alter their behavior to fit imagined rules, and the algorithm adapts to those altered behaviors.

Bansal et al. (2019) demonstrated that effective mental models do not mirror mathematical architecture; they map error boundaries. What matters to the decider is knowing when the system will fail. When an error boundary is parsimonious and predictable, human users calibrate trust effectively. When that boundary is stochastic or jagged, calibration collapses. Dell’Acqua et al. (2026) verified this dynamic in field experiments with professional consultants: within the system’s capability boundaries, output quality and speed surged by double digits, but on tasks lying outside that jagged frontier, reliance persisted and error rates spiked by 19%.

The standard response to misinterpretation—Explainable AI (XAI)—has repeatedly misfired. Rather than improving decision quality, post-hoc explanations typically inflate uncritical acceptance. Explaining why an automated aid might fail increases user reliance regardless of whether the system’s output is correct (Dzindolet et al., 2003). Bansal et al. (2021) demonstrated that local feature explanations, such as SHAP or LIME visualizations, raise human acceptance of incorrect AI recommendations, with no explanation design outperforming a simple, unadorned confidence metric. Poursabzi-Sangdeh et al. (2021) showed that exposing internal model mechanics induces cognitive overload, degrading the user’s capacity to spot obvious errors.

Exceptions exist, but only under narrow conditions. Vasconcelos et al. (2023) showed that explanations reduced overreliance only when reviewing the explanation required less cognitive effort than verifying the underlying task. Calibrated trust improves when system confidence is expressed clearly and testing is inexpensive (Zhang, Liao, & Bellamy, 2020; Kulesza et al., 2012). Yet these boundary conditions reflect classic cognitive load principles that succeed only in static, dyadic interactions where the user is the sole beneficiary and verification costs are near zero.

The second operational hurdle is formulating intent through restrictive input channels. When an automated model errs, users routinely abandon it for human judgment, even when the model significantly outperforms them—a bias known as algorithm aversion (Dietvorst, Simmons, & Massey, 2015). Yet Dietvorst, Simmons, and Massey (2018) discovered that giving users the ability to modify an algorithmic output by as little as 2% to 5% largely eliminated algorithm aversion. System utilization rose from 47% to nearly 70%. What restored trust was not complete control, but the mere existence of a dedicated channel through which intent could be registered.

Buçinca, Malaya, and Gajos (2021) engineered cognitive forcing functions, such as requiring users to commit to an independent judgment before seeing algorithmic advice or imposing deliberate friction before accepting a recommendation. These structural interventions curbed uncritical acceptance far more effectively than explanatory text, even though users rated these demanding interfaces less enjoyable. In platforms lacking explicit channels for intent, users resort to indirect maneuvering: digital creators and gig workers reverse-engineer engagement rules, adapting their language and schedules to manipulate the algorithm’s hidden thresholds (Cotter, 2019).

The third operational challenge is monitoring an intermediary whose underlying policy changes over time. Classic human factors literature notes that human vigilance degrades when monitoring systems with uniform reliability: Parasuraman, Molloy, and Singh (1993) observed that operators caught 82% of automation failures when reliability fluctuated, but only 33% when reliability remained constant. Paradoxically, sustained baseline reliability dulls the human capacity to detect unexpected failures (Parasuraman & Manzey, 2010). Modern adaptive software exacerbates this vulnerability through model drift and unannounced backend updates. Bansal, Nushi, et al. (2019) showed that updating an AI classifier to achieve higher aggregate statistical accuracy paradoxically reduced joint human-AI team performance whenever the update changed the pattern of errors the user had learned to expect. A more accurate but incompatible model produced worse operational outcomes than an inferior, stable model.

Everyday users are poorly equipped to notice these shifts. Mohanty, Lim, and Luther (2025) found that individuals using an updated AI model detected changes at a rate of 48.87%—indistinguishable from chance. Glickman and Sharot (2025) found that human actors in iterative feedback loops were frequently oblivious to how computational recommendations shaped their personal beliefs, and Fernandes et al. (2026) revealed that users consistently overestimated their performance when aided by AI, with higher self-reported AI literacy correlating with worse metacognitive accuracy. Lee et al. (2025) observed that elevated confidence in AI systems was associated with a marked drop in critical thinking among knowledge workers. Conventional guidelines that blithely instruct systems to “notify users about changes” (Amershi et al., 2019) assume an ideal user with unlimited cognitive bandwidth to parse complex engineering updates.

Almost every study in the current literature isolates a single user facing a machine advisor. As Lai et al. (2023) emphasize in their broad review of empirical human-AI research, the literature lacks frameworks that incorporate the perspectives and outcomes of multiple stakeholders. The triadic structure—where the intermediary simultaneously reads, predicts, and binds both a principal and a counterpart—remains unmodeled in laboratory research.

## Algorithmacy on the Numeracy Model

When Andrew Wilkinson (1965) coined the term oracy, he was not offering a linguistic novelty. He was asserting that the spoken capacities of speaking and listening deserved the same institutional legitimacy that educational systems accorded to reading (literacy) and counting (numeracy). Algorithmacy follows this structural lineage. Where literacy enables participation in communication mediated by text, numeracy enables decision-making mediated by numbers, and oracy enables communication mediated by speech, algorithmacy enables participation in coordination mediated by an opaque, adaptive intermediary that reads multiple parties and commits binding decisions.

This lineage reveals a categorical difference in the mediating substrate. Acoustic speech is dyadic, co-present, and ephemeral. Written text is dyadic and asynchronous, but fundamentally passive. Symbolic quantification is abstract, invariant, and formal. An adaptive intermediary, by contrast, is triadic, dynamic, and binding. Literacy, numeracy, and oracy are competencies for engaging a medium; algorithmacy is a competence for engaging a coordination. Its three operations are direct consequences of the intermediary’s structural properties: opacity prevents direct observation of internal rules, requiring interpretation; mutual bindingness commits choices for multiple parties at once, requiring precise intent specification; and adaptivity means rules drift across retraining cycles, requiring continuous tracking. Traditional media hold still; an algorithmic intermediary does not.

This distinction must be protected against theoretical overreach. Walter Ong (1982/2002) and early communication theorists (Goody & Watt, 1963) posited a “Great Divide,” arguing that the invention of writing fundamentally rewired the neurological architecture of the human mind. Brian Street (1984) dismantled this autonomous model, showing that the cognitive consequences of literacy are shaped by the social institutions through which it is acquired and exercised. Claims that algorithmic interfaces rewire human consciousness fall into the same trap.

The defensible foundation for algorithmacy comes from numeracy. Decision researchers do not claim that numbers rewired the human brain. Instead, they demonstrate psychometric incremental validity. Peters et al. (2006) proved that objective numeracy predicts resistance to cognitive framing effects, an advantage that persists after controlling for general intelligence. Sobkow, Olszewska, and Traczyk (2020) confirmed across large representative samples that numeric competencies uniquely predict decision quality beyond fluid intelligence (\$g\$) and cognitive reflection. Reyna and Brainerd (2023) synthesized decades of findings showing that numeracy predicts real-world decision outcomes in health management, financial planning, and legal adjudication.

Numeracy earns its scientific standing because it can be operationalized, psychometrically validated, and demonstrated to predict decision outcomes beyond general intelligence. Algorithmacy must meet this exact empirical standard: it must predict the quality of decisions made through algorithmic intermediaries over and above fluid intelligence, working-memory capacity, and general digital literacy.

Reyna and Brainerd (2023) supply an additional insight: mature numeracy is not rote arithmetic or literal number crunching. It is gist extraction—the capacity to grasp bottom-line qualitative relationships within a decision context. Skilled algorithmacy will mirror this architecture. It is not reverse-engineering Python code or mentalizing neural-network weights; it is extracting the functional boundaries, behavioral tendencies, and incentives governing the intermediary.

This formulation separates algorithmacy from adjacent constructs. Algorithmic literacy is frequently defined as factual awareness of algorithms paired with perceived tactical use (DeVito, 2021; Dogruel, Masur, & Joeckel, 2022), yet comprehensive audits reveal that existing scales measure fragmented attitudinal dimensions rather than a coherent cognitive competence (Oeldorf-Hirsch & Neubaum, 2025; Gagrčin, Naab, & Grub, 2026). Algorithmic awareness is often reduced to single-item self-reports indicating whether a user knows a feed is curated (Gran, Booth, & Bucher, 2021). AI literacy encompasses broad pedagogical taxonomies for using and critiquing consumer AI tools (Long & Magerko, 2020; Ng et al., 2021). Algorithmic skills capture tactical maneuvers deployed to work around specific platform constraints, such as optimizing marketplace hashtags (Hargittai et al., 2020; Klawitter & Hargittai, 2018). While recent scales examining the algorithmic competency of gig workers analyze compliance and resistance behaviors (Zhou et al., 2025), they leave the cognitive demands of multi-sided mediation unaddressed.

All these frameworks retain a dyadic lens: a single user facing a single piece of software. When Kalantzis and Cope (2024) assert that generative AI is primarily an evolution of textual literacy, their argument holds only as long as the system operates as a passive communicative conduit. It collapses the moment the system operates as an active, binding intermediary.

Information theory clarifies this distinction. An interface coordination system can be modeled through integrated information (\$\Phi\$). When an interaction between two humans across a digital channel can be mathematically factored into independent, uncoupled subsystems (\$\Phi = 0\$), the technology acts as a moderator—a passive conduit where traditional literacy suffices. When the intermediary dynamically processes data from both sides, enforces its own optimization function, and binds both parties into an outcome that neither can unilaterally alter, the system cannot be factored (\$\Phi \> 0\$). It acts as a strict mediator. Literacy cannot govern a strict mediator; that environment demands algorithmacy.

## Structural Intervention Over Visual Legibility

The default instinct of computer science and regulatory policy is to treat algorithmic mediation as a problem of visibility. If the user cannot make sound decisions, the remedy is assumed to be explainability: open the black box, expose the decision trees, visualize the weights. The empirical record demonstrates that this approach is flawed. Providing explanations increases user awareness of an algorithm’s presence while leaving user agency flat or diminished.

Eslami et al. (2015) deployed FeedVis to reveal hidden feed filtering, and Fouquaert and Mechant (2022) used the Instawareness tool to expose Instagram curation; both interventions raised users’ passive cognitive awareness, but neither cultivated critical evaluation or meaningful agency. Rader, Cotter, and Cho (2018) presented Facebook users with four architectural explanations of feed curation; all four increased user recognition that the platform shaped their content, but none altered the belief that their own actions remained in control. Cheng et al. (2019) improved non-expert comprehension of a university admissions algorithm, yet found that neither increased comprehension nor interactive interfaces improved subjective trust or decision confidence. Vaccaro, Sandvig, and Karahalios (2020) demonstrated that introducing appeals processes for contested algorithmic decisions yielded zero improvement in user perceptions of fairness, accountability, or autonomy compared to an outright refusal. Moon et al. (2025) found that algorithmic literacy did not benefit users unless both explainability and direct control mechanisms were present simultaneously; absent control, explainability widened the perception gap between sophisticated and unsophisticated users. Fernandes et al. (2026) observed that higher self-reported AI literacy correlated with worse metacognitive calibration, fostering an unjustified confidence in algorithmic suggestions.

Telling an individual that an algorithmic intermediary is shaping their options does not change the mathematical structure of the mediation. A transparent triad remains a triad.

Decision experience design must abandon the pursuit of turning users into visual decoders of complex models. Disclosing model weights, visualizing post-hoc feature saliency, drafting explanatory text, and issuing change alerts address legibility without shifting structural dynamics. Expertise in DXD centers instead on structural interventions that reshape the coordination environment: counter-delegation, structural refusal, bounded operational envelopes, and backward-compatible behavioral updates.

Counter-delegation equips the human party with their own representative software agents to negotiate on their behalf. This provides an algorithmic counterweight to the platform’s optimizer, operationalizing the relational data governance models proposed by Viljoen (2021) and Delacroix and Lawrence (2019). Its minimal psychological footprint is visible in Dietvorst et al.’s (2018) modification right: giving users even a narrow channel to assert intent fundamentally restores their willingness to decide through an algorithmic system. It resolves the classic Woods (1985) double-bind by providing operational authority alongside responsibility.

Structural refusal ensures the decision maker can reject algorithmic mediation on their own terms. Zong and Matias (2024) warn that superficial opt-outs that impose crippling functional penalties are placation mechanisms rather than genuine choices. In information-theoretic terms, offering a costless exit path makes the parties substitutable, collapsing an irreducible triadic mediator back into a separable, manageable dyad.

Bounded operational envelopes establish explicit bounds on algorithmic behavior rather than explaining black-box logic after the fact. This operationalizes Bainbridge’s (1983) core principle: designing systems that decide using criteria and rates human perception can track, engineered to fail conspicuously. It is realized through backward-compatible model updates that safeguard what human users have already learned (Bansal, Nushi, et al., 2019), and by maintaining steady operational envelopes to prevent the vigilance degradation that follows silent updates (Parasuraman & Manzey, 2010). It creates the environmental predictability that Kahneman and Klein (2009) established as mandatory for developing valid judgment.

A persistent debate in human-computer interaction centers on whether UX designers must retrain as machine learning engineers (Dove et al., 2017; Flechtner & Stankowski, 2023; Szlachta, 2024; Li et al., 2024; Alvarez, 2026; Shalamova, Richards, & Miller, 2026). Yang et al. (2018) found that experienced designers working with machine learning did not view technical ML expertise as a prerequisite for good design, finding their value instead in cross-disciplinary collaboration. The historical parallel holds: UX designers did not become vision scientists; they became experts in what human vision perceives, parses, and retains. Decision experience designers do not need to build neural networks; they need expertise in the cognitive limits of human decision-making, the structural dynamics of algorithmic mediation, and the design of channels that safeguard human agency.

Several intermediate design literatures attempt to bridge this divide. Rather than presenting an illusion of seamless automation, seamful design reveals the gaps, joints, and transitions in a computational system, allowing users to understand its limits (Chalmers & Galani, 2004; Ehsan et al., 2024). Contestability by design formulates architectural principles that allow users to interrogate, challenge, and overturn algorithmic decisions (Alfrink et al., 2023). Algorithmic experience frames systems through dimensions of user awareness and adjustment (Alvarado & Waern, 2018). These frameworks advance beyond classic nudging by treating user competence as an explicit design objective. Yet they retain a critical blind spot: none models a triadic coordination environment where an intermediary simultaneously balances and binds a counterpart. Designing seams that help an individual read a system is helpful; designing environments that protect human agency when an intermediary coordinates multiple competing parties is the unmapped frontier of decision experience design.

## Five Unresolved Gaps and a Falsifiable Research Agenda

An audit of the scholarly record reveals five empirical and theoretical gaps. First, the term lacks an academic footprint: the phrase “decision experience design” exists almost entirely within practitioner writing from late 2023 onward, and psychometric repositories contain no validated scales indexing algorithmacy as a triadic decision competence. Second, design competence is misdirected toward upskilling designers in technical machine learning tools, leaving unaddressed how designers should understand, preserve, and scaffold users’ cognitive competencies within algorithmic mediation. Third, multi-party algorithmic decisions remain unmodeled in design, as decision-centered design addresses expert operators running non-adaptive machinery, choice architecture assumes an identifiable human architect, and decision intelligence serves enterprise analytics. Fourth, empirical human-AI decision research remains dyadic, overwhelmingly isolating a single human user evaluating algorithmic advice without modeling the second party of a coordination. Fifth, the cognitive expertise of working designers remains unmeasured; empirical surveys of UX practitioners measure tools and visual craft, meaning the discipline’s historical ties to cognitive science rest on published theoretical frameworks rather than practitioner training.

To transition from an industry catchphrase into an empirical discipline, decision experience design must test a sequence of falsifiable propositions.

The first proposition concerns incremental validity: a psychometrically validated measure of algorithmacy will predict the quality of decisions made through an adaptive algorithmic intermediary after controlling for fluid intelligence (\$g\$), cognitive reflection, and existing scales of general algorithmic literacy. If the construct fails to demonstrate incremental predictive validity over baseline scales, the term is a redundant label, and the discipline should anchor itself in existing literatures of literacy and cognitive reflection.

The second proposition posits a triadic penalty: the cognitive burden of interpreting, specifying intent, and tracking will be significantly higher—and post-hoc explanations will provide significantly less utility—when an intermediary reads and binds a counterpart than when it operates as an isolated dyadic advisor. This proposition directly targets the empirical gap in two-party experimentation, testing the boundary between simple moderation and strict mediation.

The third proposition argues that bounding beats explaining: bounding system behavior through declared operating envelopes and backward-compatible updates will produce higher decision accuracy and better trust calibration over time than exposing internal model mechanics or dispatching passive change notifications. This contrasts structural human factors engineering directly against the explainable AI paradigm.

The fourth proposition asserts that channel existence outweighs bandwidth: introducing an explicit, low-friction channel for intent will improve willingness to decide through an intermediary and enhance overall decision quality, with marginal gains tapering off rapidly as the channel’s bandwidth expands. If decision quality does not improve alongside adoption, the input channel operates merely as a placation mechanism.

These propositions can be measured using established constructs: decision difficulty and subjective satisfaction (Peterson & Cheng, 2022), choice regret, deferral, and switching behavior (Chernev et al., 2015), performance comparisons against the best solo performer (Vaccaro et al., 2024), and joint welfare outcomes across both parties in a coordination. These metrics provide an empirical standard that superficial measures like time-to-decision and click-through activation cannot match.

Several limitations bound this review. Scholarly databases reflect records available through late 2026, and the absence of indexed citations for practitioner terms may shift as trade concepts enter graduate curricula and conference proceedings. Practitioner citations rely on web records, industry essays, and white papers that remain vulnerable to link decay or editorial revision. Furthermore, while the historical analysis identifies Grudin’s outward trajectory and Fitts’s early allocations, the application of the Kahneman-Klein learning criteria to algorithmic drift, the mapping of numeracy’s gist extraction to intermediary rules, and the integration of information theory to separate moderation from strict mediation represent theoretical syntheses that require empirical testing across live organizational platforms.

## References

Alfrink, K., Keller, I., Kortuem, G., & Doorn, N. (2023). Contestable AI by Design: Towards a Framework. *Minds and Machines*, 33(4), 613–639. <https://doi.org/10.1007/s11023-022-09611-z>

Allen, R., & Choudhury, P. (2022). Algorithm-Augmented Work and Domain Experience: The Countervailing Forces of Ability and Aversion. *Organization Science*, 33(1), 149–169. <https://doi.org/10.1287/orsc.2021.1554>

Alvarado, O., & Waern, A. (2018). Towards algorithmic experience: Initial efforts for social media contexts. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. <https://doi.org/10.1145/3173574.3173860>

Alvarado Rodríguez, O. L. (2017). *Towards Algorithmic Experience: Redesigning Facebook’s News Feed* (Master’s thesis, Uppsala University).

Alvarez, I. (2026). Upskilling UX designers for AI-native work: A pedagogical framework and empirical evaluation. In *Proceedings of the 5th Annual Symposium on Human-Computer Interaction for Work* (pp. 1–19). ACM. <https://doi.org/10.1145/3808045.3808059>

Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for Human-AI Interaction. In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. <https://doi.org/10.1145/3290605.3300233>

Aneesh, A. (2009). Global Labor: Algocratic Modes of Organization. *Sociological Theory*, 27(4), 347–370. <https://doi.org/10.1111/j.1467-9558.2009.01352.x>

Arnott, D., & Pervan, G. (2005). A Critical Analysis of Decision Support Systems Research. *Journal of Information Technology*, 20(2), 67–87. <https://doi.org/10.1057/palgrave.jit.2000035>

Arnott, D., & Pervan, G. (2014). A Critical Analysis of Decision Support Systems Research Revisited: The Rise of Design Science. *Journal of Information Technology*, 29(4), 269–293. <https://doi.org/10.1057/jit.2014.16>

Audry, A. (n.d.). *Decision Experience Design*. Retrieved September 30, 2026, from <https://www.andrewaudry.com/dxdesign>

Bainbridge, L. (1983). Ironies of Automation. *Automatica*, 19(6), 775–779. <https://doi.org/10.1016/0005-1098(83)90046-8>

Banker, S., & Khetani, S. (2019). Algorithm Overdependence: How the Use of Algorithmic Recommendation Systems Can Increase Risks to Consumer Well-Being. *Journal of Public Policy & Marketing*, 38(4), 500–515. <https://doi.org/10.1177/0743915619858057>

Bansal, G., Nushi, B., Kamar, E., Lasecki, W. S., Weld, D. S., & Horvitz, E. (2019). Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance. In *Proceedings of the AAAI Conference on Human Computation and Crowdsourcing*, 7(1), 2–11. <https://doi.org/10.1609/hcomp.v7i1.5285>

Bansal, G., Nushi, B., Kamar, E., Weld, D. S., Lasecki, W. S., & Horvitz, E. (2019). Updates in Human-AI Teams: Understanding and Addressing the Performance/Compatibility Tradeoff. In *Proceedings of the AAAI Conference on Artificial Intelligence*, 33(1), 2429–2437. <https://doi.org/10.1609/aaai.v33i01.33012429>

Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., & Weld, D. (2021). Does the Whole Exceed Its Parts? The Effect of AI Explanations on Complementary Team Performance. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. <https://doi.org/10.1145/3411764.3445717>

Bucher, T. (2017). The Algorithmic Imaginary: Exploring the Ordinary Affects of Facebook Algorithms. *Information, Communication & Society*, 20(1), 30–44. <https://doi.org/10.1080/1369118X.2016.1154086>

Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1), 188:1–188:21. <https://doi.org/10.1145/3449287>

Buscher, G., Cutrell, E., & Morris, M. R. (2009). What do you see when you’re surfing? Using eye tracking to predict salient regions of web pages. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 21–30). ACM. <https://doi.org/10.1145/1518701.1518705>

Callaway, F., Jain, Y. R., van Opheusden, B., Das, P., Iwama, G., Gul, S., Krueger, P. M., Becker, F., Griffiths, T. L., & Lieder, F. (2022). Leveraging Artificial Intelligence to Improve People’s Planning Strategies. *Proceedings of the National Academy of Sciences*, 119(12), e2117432119. <https://doi.org/10.1073/pnas.2117432119>

Calo, R., & Rosenblat, A. (2016). The Taking Economy: Uber, Information, and Power. *Columbia Law Review*, 117, 1623–1690.

Card, S. K., Moran, T. P., & Newell, A. (1980). The keystroke-level model for user performance time with interactive systems. *Communications of the ACM*, 23(7), 396–410. <https://doi.org/10.1145/358886.358895>

Card, S. K., Moran, T. P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction*. Lawrence Erlbaum Associates.

Carsten, O., & Martens, M. H. (2019). How Can Humans Understand Their Automated Cars? HMI Principles, Problems and Solutions. *Cognition, Technology & Work*, 21(1), 3–20. <https://doi.org/10.1007/s10111-018-0484-0>

Chalmers, M., & Galani, A. (2004). Seamful Interweaving: Heterogeneity in the Theory and Design of Interactive Systems. In *Proceedings of the 5th Conference on Designing Interactive Systems* (pp. 243–252). ACM. <https://doi.org/10.1145/1013115.1013149>

Chandrashekar, S. P., Adelina, N., Zeng, S., Chiu, Y. Y. E., Leung, G. Y. S., Henne, P., Cheng, B. L., & Feldman, G. (2023). Defaults versus Framing: Revisiting Default Effect and Framing Effect with Replications and Extensions. *Meta-Psychology*, 7. <https://doi.org/10.15626/MP.2022.3108>

Cheng, H.-F., Wang, R., Zhang, Z., O’Connell, F., Gray, T., Harper, F. M., & Zhu, H. (2019). Explaining Decision-Making Algorithms through UI: Strategies to Help Non-Expert Stakeholders. In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. <https://doi.org/10.1145/3290605.3300789>

Chernev, A., Böckenholt, U., & Goodman, J. (2015). Choice Overload: A Conceptual Review and Meta-Analysis. *Journal of Consumer Psychology*, 25(2), 333–358. <https://doi.org/10.1016/j.jcps.2014.08.002>

Chignell, M., Wang, L., Zare, A., & Li, J. J. (2023). The Evolution of HCI and Human Factors: Integrating Human and Artificial Intelligence. *ACM Transactions on Computer-Human Interaction*, 30(2), 1–30. <https://doi.org/10.1145/3557891>

Commarford, P. M., Lewis, J. R., Smither, J. A.-A., & Gentzler, M. D. (2008). A Comparison of Broad Versus Deep Auditory Menu Structures. *Human Factors*, 50(1), 77–89. <https://doi.org/10.1518/001872008x250665>

Cotter, K. (2019). Playing the Visibility Game: How Digital Influencers and Algorithms Negotiate Influence on Instagram. *New Media & Society*, 21(4), 895–913. <https://doi.org/10.1177/1461444818815684>

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87–114. <https://doi.org/10.1017/s0140525x01003922>

Cowan, N. (2015). George Miller’s magical number of immediate memory in retrospect. *Psychological Review*, 122(3), 536–541. <https://doi.org/10.1037/a0039035>

Crandall, B., Klein, G., & Hoffman, R. R. (2006). *Working Minds: A Practitioner’s Guide to Cognitive Task Analysis*. MIT Press. <https://doi.org/10.7551/mitpress/7304.001.0001>

Danish-Swiss Chamber of Commerce. (2026). *@Saxo Bank HQ: The Future of Decision Making*. Event announcement. <https://dshk.ch/events/at-saxo-bank-hq-denmark/>

de Winter, J. C. F., & Dodou, D. (2014). Why the Fitts list has persisted throughout the history of function allocation. *Cognition, Technology & Work*, 16(1), 1–11. <https://doi.org/10.1007/s10111-011-0188-1>

Delacroix, S., & Lawrence, N. D. (2019). Bottom-up data trusts: Disturbing the ‘one size fits all’ approach to data governance. *International Data Privacy Law*, 9(4), 236–252. <https://doi.org/10.1093/idpl/ipz014>

Dell’Acqua, F., McFowland, E., Mollick, E., Lifshitz, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. *Organization Science*, 37(2), 403–423. <https://doi.org/10.1287/orsc.2025.21838>

DellaVigna, S., & Linos, E. (2022). RCTs to Scale: Comprehensive Evidence from Two Nudge Units. *Econometrica*, 90(1), 81–116. <https://doi.org/10.3982/ECTA18709>

DeVito, M. A. (2021). Adaptive Folk Theorization as a Path to Algorithmic Literacy on Changing Platforms. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW2), 339:1–339:38. <https://doi.org/10.1145/3476080>

DeVito, M. A., Birnholtz, J., Hancock, J. T., French, M., & Liu, S. (2018). How People Form Folk Theories of Social Media Feeds. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–12). ACM. <https://doi.org/10.1145/3173574.3173694>

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm Aversion: People Erroneously Avoid Algorithms after Seeing Them Err. *Journal of Experimental Psychology: General*, 144(1), 114–126. <https://doi.org/10.1037/xge0000033>

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them. *Management Science*, 64(3), 1155–1170. <https://doi.org/10.1287/mnsc.2016.2643>

Dogruel, L., Masur, P., & Joeckel, S. (2022). Development and Validation of an Algorithm Literacy Scale for Internet Users. *Communication Methods and Measures*, 16(2), 115–133. <https://doi.org/10.1080/19312458.2021.1968361>

Doumont, J.-L. (2002). Magical numbers: The seven-plus-or-minus-two myth. *IEEE Transactions on Professional Communication*, 45(2), 123–127. <https://doi.org/10.1109/tpc.2002.1003695>

Dove, G., Halskov, K., Forlizzi, J., & Zimmerman, J. (2017). UX design innovation: Challenges for working with machine learning as a design material. In *Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems* (pp. 278–288). ACM. <https://doi.org/10.1145/3025453.3025739>

Dyson, M. C. (2004). How physical text layout affects reading from screen. *Behaviour & Information Technology*, 23(6), 377–393. <https://doi.org/10.1080/01449290410001715714>

Dzindolet, M. T., Peterson, S. A., Pomranky, R. A., Pierce, L. G., & Beck, H. P. (2003). The Role of Trust in Automation Reliance. *International Journal of Human-Computer Studies*, 58(6), 697–718. <https://doi.org/10.1016/S1071-5819(03)00038-7>

Ehsan, U., Liao, Q. V., Passi, S., Riedl, M. O., & Daumé III, H. (2024). Seamful XAI: Operationalizing Seamful Design in Explainable AI. *Proceedings of the ACM on Human-Computer Interaction*, 8(CSCW1), 119:1–119:29. <https://doi.org/10.1145/3637396>

Eslami, M., Karahalios, K., Sandvig, C., Vaccaro, K., Rickman, A., Hamilton, K., & Kirlik, A. (2016). First I “Like” It, Then I Hide It: Folk Theories of Social Feeds. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 2371–2382). ACM. <https://doi.org/10.1145/2858036.2858494>

Eslami, M., Rickman, A., Vaccaro, K., Aleyasen, A., Vuong, A., Karahalios, K., Hamilton, K., & Sandvig, C. (2015). “I Always Assumed That I Wasn’t Really That Close to Her”: Reasoning about Invisible Algorithms in News Feeds. In *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems* (pp. 153–162). ACM. <https://doi.org/10.1145/2702123.2702556>

Fernandes, D., Villa, S., Nicholls, S., Haavisto, O., Buschek, D., Schmidt, A., Kosch, T., Shen, C., & Welsch, R. (2026). AI Makes You Smarter but None the Wiser: The Disconnect between Performance and Metacognition. *Computers in Human Behavior*, 175, 108779. <https://doi.org/10.1016/j.chb.2025.108779>

Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. *Journal of Experimental Psychology*, 47(6), 381–391. <https://doi.org/10.1037/h0055392>

Flechtner, R., & Stankowski, A. (2023). AI is not a wildcard: Challenges for integrating AI into the design curriculum. In *Proceedings of the 5th Annual Symposium on HCI Education* (pp. 72–77). ACM. <https://doi.org/10.1145/3587399.3587410>

Forlizzi, J. (2018). Moving beyond user-centered design. *Interactions*, 25(5), 22–23. <https://doi.org/10.1145/3239558>

Fouquaert, T., & Mechant, P. (2022). Making Curation Algorithms Apparent: A Case Study of ‘Instawareness’. *Information, Communication & Society*, 25(12), 1769–1789. <https://doi.org/10.1080/1369118X.2021.1883707>

Gagrčin, E., Naab, T. K., & Grub, M. F. (2026). Algorithmic Media Use and Algorithm Literacy: An Integrative Literature Review. *New Media & Society*, 28(1), 423–447. <https://doi.org/10.1177/14614448241291137>

Glickman, M., & Sharot, T. (2025). How Human–AI Feedback Loops Alter Human Perceptual, Emotional and Social Judgements. *Nature Human Behaviour*, 9(2), 345–359. <https://doi.org/10.1038/s41562-024-02077-2>

González, C. A., Ghazizadeh, M., & Smith, M. (2014). Perspectives on the Training of Human Factors Students for the User Experience Industry. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting*, 58(1), 1807–1811. <https://doi.org/10.1177/1541931214581378>

Goody, J., & Watt, I. (1963). The Consequences of Literacy. *Comparative Studies in Society and History*, 5(3), 304–345. <https://doi.org/10.1017/S0010417500001730>

Gorry, G. A., & Scott Morton, M. S. (1971). *A Framework for Management Information Systems* (Working Paper No. 510-71). Sloan School of Management, MIT.

Gran, A.-B., Booth, P., & Bucher, T. (2021). To Be or Not to Be Algorithm Aware: A Question of a New Digital Divide? *Information, Communication & Society*, 24(12), 1779–1796. <https://doi.org/10.1080/1369118X.2020.1736124>

Gray, C. M., Kou, Y., Battles, B., Hoggatt, J., & Toombs, A. L. (2018). The Dark (Patterns) Side of UX Design. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–14). ACM. <https://doi.org/10.1145/3173574.3174108>

Grudin, J. (1990). The computer reaches out: The historical continuity of interface design. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 261–268). ACM. <https://doi.org/10.1145/97243.97284>

Hargittai, E., Gruber, J., Djukaric, T., Fuchs, J., & Brombach, L. (2020). Black Box Measures? How to Study People’s Algorithm Skills. *Information, Communication & Society*, 23(5), 764–775. <https://doi.org/10.1080/1369118X.2020.1713846>

Harrison, S., Tatar, D., & Sengers, P. (2007). The Three Paradigms of HCI. In *alt.chi, CHI 2007 Conference on Human Factors in Computing Systems*. ACM.

Hasić, F., De Smedt, J., & Vanthienen, J. (2018). Augmenting processes with decision intelligence: Principles for integrated modelling. *Decision Support Systems*, 107, 1–12. <https://doi.org/10.1016/j.dss.2017.12.008>

Healey, C. G., & Enns, J. T. (2012). Attention and Visual Memory in Visualization and Computer Graphics. *IEEE Transactions on Visualization and Computer Graphics*, 18(7), 1170–1188. <https://doi.org/10.1109/tvcg.2011.127>

Herath Pathirannehelage, S., Shrestha, Y. R., & von Krogh, G. (2025). Design Principles for Artificial Intelligence-Augmented Decision Making: An Action Design Research Study. *European Journal of Information Systems*, 34(2), 207–229. <https://doi.org/10.1080/0960085X.2024.2330402>

Hertwig, R., & Grüne-Yanoff, T. (2017). Nudging and Boosting: Steering or Empowering Good Decisions. *Perspectives on Psychological Science*, 12(6), 973–986. <https://doi.org/10.1177/1745691617702496>

Hick, W. E. (1952). On the Rate of Gain of Information. *Quarterly Journal of Experimental Psychology*, 4(1), 11–26. <https://doi.org/10.1080/17470215208416600>

Hollan, J., Hutchins, E., & Kirsh, D. (2000). Distributed cognition: Toward a new foundation for human-computer interaction research. *ACM Transactions on Computer-Human Interaction*, 7(2), 174–196. <https://doi.org/10.1145/353485.353487>

Hollender, N., Hofmann, C., Deneke, M., & Schmitz, B. (2010). Integrating cognitive load theory and concepts of human–computer interaction. *Computers in Human Behavior*, 26(6), 1278–1288. <https://doi.org/10.1016/j.chb.2010.05.031>

Hollnagel, E., & Woods, D. D. (1983). Cognitive Systems Engineering: New Wine in New Bottles. *International Journal of Man-Machine Studies*, 18(6), 583–600. <https://doi.org/10.1016/S0020-7373(83)80034-0>

Hutchins, E. L., Hollan, J. D., & Norman, D. A. (1985). Direct Manipulation Interfaces. *Human–Computer Interaction*, 1(4), 311–338. <https://doi.org/10.1207/s15327051hci0104_2>

Hutton, R. J. B., Miller, T. E., & Thordsen, M. L. (2003). Decision-centered design: Leveraging cognitive task analysis in design. In E. Hollnagel (Ed.), *Handbook of Cognitive Task Design* (pp. 383–416). Lawrence Erlbaum Associates. <https://doi.org/10.1201/9781410607775.ch17>

Hyman, R. (1953). Stimulus information as a determinant of reaction time. *Journal of Experimental Psychology*, 45(3), 188–196. <https://doi.org/10.1037/h0056940>

Itera. (2025). *La era post-BI: bienvenidos al DX (Decision Experience)*. <https://itera.cl/2025/07/04/la-era-post-bi-bienvenidos-al-dx-decision-experience/>

Janssen, C. P., Donker, S. F., Brumby, D. P., & Kun, A. L. (2019). History and Future of Human-Automation Interaction. *International Journal of Human-Computer Studies*, 131, 99–107. <https://doi.org/10.1016/j.ijhcs.2019.05.006>

Johnson, E. J., Shu, S. B., Dellaert, B. G. C., Fox, C., Goldstein, D. G., Häubl, G., Larrick, R. P., Payne, J. W., Peters, E., Schkade, D., Wansink, B., & Weber, E. U. (2012). Beyond nudges: Tools of a choice architecture. *Marketing Letters*, 23(2), 487–504. <https://doi.org/10.1007/s11002-012-9186-1>

Kahneman, D., & Klein, G. (2009). Conditions for Intuitive Expertise: A Failure to Disagree. *American Psychologist*, 64(6), 515–526. <https://doi.org/10.1037/a0016755>

Kalantzis, M., & Cope, B. (2024). Literacy in the Time of Artificial Intelligence. *Reading Research Quarterly*, 60(1), e591. <https://doi.org/10.1002/rrq.591>

Keen, P. G. W., & Scott Morton, M. S. (1978). *Decision Support Systems: An Organizational Perspective*. Addison-Wesley.

Klawitter, E., & Hargittai, E. (2018). “It’s Like Learning a Whole Other Language”: The Role of Algorithmic Skills in the Curation of Creative Goods. *International Journal of Communication*, 12, 3490–3510.

Klein, G. (2008). Naturalistic Decision Making. *Human Factors*, 50(3), 456–460. <https://doi.org/10.1518/001872008X288385>

Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). Ten Challenges for Making Automation a “Team Player” in Joint Human-Agent Activity. *IEEE Intelligent Systems*, 19(6), 91–95. <https://doi.org/10.1109/MIS.2004.74>

Klein, G. A. (1993). A Recognition-Primed Decision (RPD) Model of Rapid Decision Making. In G. A. Klein, J. Orasanu, R. Calderwood, & C. E. Zsambok (Eds.), *Decision Making in Action: Models and Methods*. Ablex.

Klumbytė, G., Lücking, P., & Draude, C. (2020). Reframing AX with critical design: The potentials and limits of algorithmic experience as a critical design concept. In *Proceedings of the 11th Nordic Conference on Human-Computer Interaction* (pp. 1–12). ACM. <https://doi.org/10.1145/3419249.3420120>

Kozyreva, A., Lewandowsky, S., & Hertwig, R. (2020). Citizens Versus the Internet: Confronting Digital Challenges With Cognitive Tools. *Psychological Science in the Public Interest*, 21(3), 103–156. <https://doi.org/10.1177/1529100620946707>

Kulesza, T., Stumpf, S., Burnett, M., & Kwan, I. (2012). Tell Me More? The Effects of Mental Model Soundness on Personalizing an Intelligent Agent. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*(pp. 1–10). ACM. <https://doi.org/10.1145/2207676.2207678>

Lai, V., Chen, C., Smith-Renner, A., Liao, Q. V., & Tan, C. (2023). Towards a science of human-AI decision making: An overview of design space in empirical human-subject studies. In *Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1369–1385). ACM. <https://doi.org/10.1145/3593013.3594087>

Lallemand, C., Gronier, G., & Koenig, V. (2015). User experience: A concept without consensus? Exploring practitioners’ perspectives through an international survey. *Computers in Human Behavior*, 43, 35–48. <https://doi.org/10.1016/j.chb.2014.10.048>

Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–22). ACM. <https://doi.org/10.1145/3706598.3713778>

Lee, J. D., & See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*, 46(1), 50–80. <https://doi.org/10.1518/hfes.46.1.50_30392>

Li, J., Cao, H., Lin, L., Hou, Y., Zhu, R., & El Ali, A. (2024). User experience design professionals’ perceptions of generative artificial intelligence. In *Proceedings of the CHI Conference on Human Factors in Computing Systems* (pp. 1–18). ACM. <https://doi.org/10.1145/3613904.3642114>

Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm Appreciation: People Prefer Algorithmic to Human Judgment. *Organizational Behavior and Human Decision Processes*, 151, 90–103. <https://doi.org/10.1016/j.obhdp.2018.12.005>

Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. <https://doi.org/10.1145/3313831.3376727>

MacKenzie, I. S. (1992). Fitts’ law as a research and design tool in human-computer interaction. *Human-Computer Interaction*, 7(1), 91–139. <https://doi.org/10.1207/s15327051hci0701_3>

MacLean, K. E. (2008). Haptic Interaction Design for Everyday Interfaces. *Reviews of Human Factors and Ergonomics*, 4(1), 149–194. <https://doi.org/10.1518/155723408x342826>

Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No Evidence for Nudging after Adjusting for Publication Bias. *Proceedings of the National Academy of Sciences*, 119(31), e2200300119. <https://doi.org/10.1073/pnas.2200300119>

Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. *Proceedings of the ACM on Human-Computer Interaction*, 3(CSCW), 1–32. <https://doi.org/10.1145/3359183>

Mathur, A., Kshirsagar, M., & Mayer, J. (2021). What Makes a Dark Pattern... Dark? Design Attributes, Normative Considerations, and Measurement Methods. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–18). ACM. <https://doi.org/10.1145/3411764.3445610>

Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The Effectiveness of Nudging: A Meta-Analysis of Choice Architecture Interventions across Behavioral Domains. *Proceedings of the National Academy of Sciences*, 119(1), e2107346118. <https://doi.org/10.1073/pnas.2107346118>

Militello, L. G., & Hutton, R. J. B. (1998). Applied Cognitive Task Analysis (ACTA): A Practitioner’s Toolkit for Understanding Cognitive Task Demands. *Ergonomics*, 41(11), 1618–1641. <https://doi.org/10.1080/001401398186108>

Militello, L. G., & Klein, G. (2013). Decision-centered design. In J. D. Lee & A. Kirlik (Eds.), *The Oxford Handbook of Cognitive Engineering*. Oxford University Press. <https://doi.org/10.1093/oxfordhb/9780199757183.013.0016>

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81–97. <https://doi.org/10.1037/h0043158>

Mills, S. (2022). Finding the ‘Nudge’ in Hypernudge. *Technology in Society*, 71, 102117. <https://doi.org/10.1016/j.techsoc.2022.102117>

Mills, S., & Sætra, H. S. (2024). The Autonomous Choice Architect. *AI & Society*, 39(2), 583–595. <https://doi.org/10.1007/s00146-022-01486-z>

Mohanty, V., Lim, J., & Luther, K. (2025). What Lies Beneath? Exploring the Impact of Underlying AI Model Updates in AI-Infused Systems. In *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems* (pp. 1–21). ACM. <https://doi.org/10.1145/3706598.3713751>

Moon, J. H., Kim, S., Jung, Y., Bang, J., & Sung, Y. (2025). The Effects of Explainability and User Control on Algorithmic Transparency: The Moderating Role of Algorithmic Literacy. *Cyberpsychology, Behavior, and Social Networking*, 28(7), 497–504. <https://doi.org/10.1089/cyber.2024.0525>

Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI Literacy: An Exploratory Review. *Computers and Education: Artificial Intelligence*, 2, 100041. <https://doi.org/10.1016/j.caeai.2021.100041>

Norman, D. A. (1990). The ‘Problem’ with Automation: Inappropriate Feedback and Interaction, Not ‘Over-Automation’. *Philosophical Transactions of the Royal Society of London. Series B, Biological Sciences*, 327(1241), 585–593. <https://doi.org/10.1098/rstb.1990.0101>

Oeldorf-Hirsch, A., & Neubaum, G. (2025). What do we know about algorithmic literacy? The status quo and a research agenda for a growing field. *New Media & Society*, 27(2), 681–701. <https://doi.org/10.1177/14614448231182662>

O’Hare, D., Wiggins, M., Williams, A., & Wong, W. (1998). Cognitive task analyses for decision centred design and training. *Ergonomics*, 41(11), 1698–1718. <https://doi.org/10.1080/001401398186144>

Ong, W. J. (2002). *Orality and Literacy: The Technologizing of the Word*. Routledge. (Original work published 1982).

Parasuraman, R., & Manzey, D. H. (2010). Complacency and Bias in Human Use of Automation: An Attentional Integration. *Human Factors*, 52(3), 381–410. <https://doi.org/10.1177/0018720810376055>

Parasuraman, R., Molloy, R., & Singh, I. L. (1993). Performance consequences of automation-induced ‘complacency’. *The International Journal of Aviation Psychology*, 3(1), 1–23. <https://doi.org/10.1207/s15327108ijap0301_1>

Pastagia, K. (2026). *UX is Dead. Decision Experience (DX) is the Future*. LinkedIn. <https://www.linkedin.com/posts/keyurpastagia_ux-is-dead-decision-experience-dx-is-the-activity-7476958776173060096-52kW>

Pernice, K. (2017). *F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant (Even on Mobile)*. Nielsen Norman Group. <https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/>

Peters, E., Västfjäll, D., Slovic, P., Mertz, C. K., Mazzocco, K., & Dickert, S. (2006). Numeracy and Decision Making. *Psychological Science*, 17(5), 407–413. <https://doi.org/10.1111/j.1467-9280.2006.01720.x>

Peterson, N., & Cheng, J. (2022). Decision experience in hyperchoice: The role of numeracy and age differences. *Current Psychology*, 41(8), 5399–5411. <https://doi.org/10.1007/s12144-020-01041-3>

Poursabzi-Sangdeh, F., Goldstein, D. G., Hofman, J. M., Wortman Vaughan, J., & Wallach, H. (2021). Manipulating and Measuring Model Interpretability. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*(pp. 1–52). ACM. <https://doi.org/10.1145/3411764.3445315>

Pratt, L. (2019). *Link: How Decision Intelligence Connects Data, Actions, and Outcomes for a Better World*. Emerald Publishing. <https://doi.org/10.1108/9781787696532>

Putri, A. R. (2025). *How We Improved Activation by 242% by Redesigning Our Membership Decision Flow*. Medium. <https://medium.com/@ajengerp/how-we-improved-activation-by-242-by-redesigning-our-membership-decision-flow-7dd46911b194>

Rader, E., Cotter, K., & Cho, J. (2018). Explanations as Mechanisms for Supporting Algorithmic Transparency. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. <https://doi.org/10.1145/3173574.3173677>

Reyna, V. F., & Brainerd, C. J. (2023). Numeracy, gist, literal thinking and the value of nothing in decision making. *Nature Reviews Psychology*, 2(7), 421–439. <https://doi.org/10.1038/s44159-023-00188-7>

Rupashree. (2026). *Organizational Design Is Just Decision Design*. Medium. <https://rupashree.medium.com/organizational-design-is-just-decision-design-9d8e9a59d418>

Santos, S., & Gonçalves, H. M. (2021). The consumer decision journey: A literature review of the foundational models and theories and a future perspective. *Technological Forecasting and Social Change*, 173, 121117. <https://doi.org/10.1016/j.techfore.2021.121117>

Scheibehenne, B., Greifeneder, R., & Todd, P. M. (2010). Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload. *Journal of Consumer Research*, 37(3), 409–425. <https://doi.org/10.1086/651235>

Schneider, C., Weinmann, M., & vom Brocke, J. (2018). Digital nudging: Guiding online user choices through interface design. *Communications of the ACM*, 61(7), 67–73. <https://doi.org/10.1145/3213765>

Shalamova, N., Richards, K., & Miller, C. (2026). AI is here. Is UX ready? A four-dimension framework for curriculum design. In *Proceedings of the 8th Annual Symposium on HCI Education* (pp. 1–7). ACM. <https://doi.org/10.1145/3803869.3803888>

Shin, D., Zhong, B., & Biocca, F. A. (2020). Beyond user experience: What constitutes algorithmic experiences? *International Journal of Information Management*, 52, 102061. <https://doi.org/10.1016/j.ijinfomgt.2019.102061>

Simon, H. A. (1956). Rational Choice and the Structure of the Environment. *Psychological Review*, 63(2), 129–138. <https://doi.org/10.1037/h0042769>

Sobkow, A., Olszewska, A., & Traczyk, J. (2020). Multiple numeric competencies predict decision outcomes beyond fluid intelligence and cognitive reflection. *Intelligence*, 80, 101452. <https://doi.org/10.1016/j.intell.2020.101452>

Sprague, R. H., Jr. (1980). A Framework for the Development of Decision Support Systems. *MIS Quarterly*, 4(4), 1–26. <https://doi.org/10.2307/248957>

Street, B. V. (1984). *Literacy in Theory and Practice*. Cambridge University Press.

Szaszi, B., Higney, A., Charlton, A., Gelman, A., Ziano, I., Aczel, B., Goldstein, D. G., Yeager, D. S., & Tipton, E. (2022). No Reason to Expect Large and Consistent Effects of Nudge Interventions. *Proceedings of the National Academy of Sciences*, 119(31), e2200732119. <https://doi.org/10.1073/pnas.2200732119>

Szlachta, A. M. (2024). Nawigowanie wśród złożoności sztucznej inteligencji. Kluczowe kompetencje techniczne projektantów UX \[Navigating the AI complexity: Key technical competency of UX designers\]. *Formy*, (22). <https://doi.org/10.52652/fxyz.22.24.5>

Thaler, R. H., & Sunstein, C. R. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness*. Yale University Press.

Tversky, A., & Kahneman, D. (1981). The Framing of Decisions and the Psychology of Choice. *Science*, 211(4481), 453–458. <https://doi.org/10.1126/science.7455683>

Vaccaro, K., Sandvig, C., & Karahalios, K. (2020). “At the End of the Day Facebook Does What It Wants”: How Users Experience Contesting Algorithmic Content Moderation. *Proceedings of the ACM on Human-Computer Interaction*, 4(CSCW2), 167:1–167:22. <https://doi.org/10.1145/3415238>

Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When Combinations of Humans and AI Are Useful: A Systematic Review and Meta-Analysis. *Nature Human Behaviour*, 8(12), 2293–2303. <https://doi.org/10.1038/s41562-024-02024-1>

Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations Can Reduce Overreliance on AI Systems During Decision-Making. *Proceedings of the ACM on Human-Computer Interaction*, 7(CSCW1), 129:1–129:38. <https://doi.org/10.1145/3579605>

Vicente, K. J., & Rasmussen, J. (1992). Ecological Interface Design: Theoretical Foundations. *IEEE Transactions on Systems, Man, and Cybernetics*, 22(4), 589–606. <https://doi.org/10.1109/21.156574>

Viljoen, S. (2021). A relational theory of data governance. *Yale Law Journal*, 131(2), 573–654.

Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital nudging. *Business & Information Systems Engineering*, 58(6), 433–436. <https://doi.org/10.1007/s12599-016-0453-1>

Wilkinson, A. (1965). The Concept of Oracy. *Educational Review*, 17(4), 11–15. <https://doi.org/10.1080/0013191770170401a>

Wilkinson, M. (2023). *Enhancing Decision Experience (DX): A Path to Resolving Video Consumption’s Paradox*. Magine Pro blog. <https://www.maginepro.com/enhancing-decision-experience-dx-a-path-to-resolving-video-consumptions-paradox/>

Wolf, S. P., Klein, G. A., & Thordsen, M. L. (1991). Decision-centered design requirements. In *Proceedings of the IEEE 1991 National Aerospace and Electronics Conference* (pp. 800–805). IEEE. <https://doi.org/10.1109/naecon.1991.165845>

Woods, D. D. (1985). Cognitive Technologies: The Design of Joint Human-Machine Cognitive Systems. *AI Magazine*, 6(4), 86–92. <https://doi.org/10.1609/aimag.v6i4.511>

Woods, D. D., & Hollnagel, E. (2006). *Joint Cognitive Systems: Patterns in Cognitive Systems Engineering*. CRC Press. <https://doi.org/10.1201/9781420005684>

Yang, Q., Scuito, A., Zimmerman, J., Forlizzi, J., & Steinfeld, A. (2018). Investigating how experienced UX designers effectively work with machine learning. In *Proceedings of the 2018 Designing Interactive Systems Conference* (pp. 585–596). ACM. <https://doi.org/10.1145/3196709.3196730>

Yeung, K. (2017). ‘Hypernudge’: Big Data as a Mode of Regulation by Design. *Information, Communication & Society*, 20(1), 118–136. <https://doi.org/10.1080/1369118X.2016.1186713>

Zhang, Y., Liao, Q. V., & Bellamy, R. K. E. (2020). Effect of Confidence and Explanation on Accuracy and Trust Calibration in AI-Assisted Decision Making. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency* (pp. 295–305). ACM. <https://doi.org/10.1145/3351095.3372852>

Zhou, L., Lei, X., Liu, M., Huang, X., & Hou, R. (2025). Algorithmic Competency of On-Demand Labor Platform Workers: Scale Development, Antecedents, and Consequences. *Asia Pacific Journal of Human Resources*, 63(2), e70004. <https://doi.org/10.1111/1744-7941.70004>

Zong, J., & Matias, J. N. (2024). Data refusal from below: A framework for understanding, evaluating, and envisioning refusal as design. *ACM Journal on Responsible Computing*, 1(1), Article 10, 1–23. <https://doi.org/10.1145/3630107>
