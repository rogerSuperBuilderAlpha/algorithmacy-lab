# Draft — abstract, introduction and section outline

> **Snapshot of the author's Google Doc "Human Factors Paper", taken 2026-10-13.** The Google Doc is the
> governing text; this file is a copy for the repo and may fall behind it. Gemini wrote the diagnostic,
> abstract, introduction and outline as a refactoring of Claude's earlier draft (in this file's git
> history, commit `5b4a7dc`), and the author adopted it. Claude then made 37 word-level edits in the doc
> at the author's instruction ("your judgement is fine"; "if you think the changes are necessary make
> them"): 22 factual corrections and 15 changes following the third research round. Bullets that begin
> "Key citations (added by Claude…)" or "Literature to add (Claude…)" are Claude's. Everything else is
> the adopted text. The evidence behind the edits is in `literature/facets/T_adjudication.md` §9–§10 and
> `literature/audit/AUDIT_07`–`11.md`.

# The Space Between Decisions: Word Separation as a Guide to Designing for Algorithmacy

# Part I: Critical Diagnostic Review of Prior Draft

## 1. Core Structural and Stylistic Deficiencies

- **Defensive Hedging vs. Theoretical Authority:** The previous draft operated defensively, repeatedly undercutting assertions with self-invalidating meta-disclaimers ("A guide is all the history can be," "The paper does not say in its own voice"). Academic theory papers in venues like *Organization Theory* require assertive, conceptually grounded arguments rather than anxious literature ledgering.
- **Mechanical "5C" Execution:** Lange and Pfarrer's (2017) 5C structure was treated as isolated bureaucratic boxes rather than a cumulative cognitive escalation. The narrative leap from medieval scribes to algorithmic mediation lacked the connective conceptual bridge: the distribution and locus of cognitive burden.
- **The Disclosure Category Error:** Prior drafts treated disclosure's inconsistent empirical outcomes as a laundry list of conflicting studies. In truth, disclosure fails because it commits a category error: deploying a literacy-based intervention (demanding passive textual reading) into an interactive, triadic coordination problem.
- **Subjugation of Core Theory:** Algorithmacy was introduced as an aside rather than developed as a primary theoretical construct. The foil—enterprise compliance models treating algorithms as insider risks—was summarized passively rather than dismantled as the institutional zenith of literacy dogma.

# Part II: Refactored Abstract and Introduction

## Abstract

Human factors engineering traditionally resolves cognitively demanding tasks not by re-educating the operator, but by re-representing the task environment. The foundational historical precedent is medieval word separation: inserting spaces between words introduced no semantic data to the page, yet it offloaded lexical boundary-detection costs from inference to perception. Today, human coordination increasingly occurs through algorithmic third parties that mediate exchanges between independent actors while optimizing for distinct, proprietary objectives. Regulators and enterprise architects routinely address algorithmic opacity through disclosure: explainability dashboards, published rules, and audit logs.

This paper argues that disclosure represents a fundamental category error: it applies a literacy-based intervention (demanding textual decoding) to an interactive coordination problem. Navigating irreducible algorithmic triads demands not literacy, but *algorithmacy*—the behavioral capacity to infer, test, and anticipate mediator dynamics through continuous, direct action. Drawing on distributed cognition, epistemic action, and mechanism design, I formulate Decision Experience Design (DXD) and articulate two candidate structural conventions: strategic offloading (eliminating tactical posturing) and radical feedback immediacy (returning valid, plain results of an action with minimal latency). Examining the institutional architectures of courts, dealer foreign-exchange markets, and digital platforms, I analyze who holds the power to enforce these conventions and specify the behavioral conditions required to test them experimentally.

## Introduction: The 5Cs Structural Arc

### Common Ground: The Representational Effect

Human factors engineering has long recognized that when a task exceeds human cognitive capacity, the most robust solution is not to retrain the person, but to transform the representation of the task environment. Zhang and Norman (1994) formalized this principle as the representational effect: isomorphic representations of an identical formal structure evoke radically divergent cognitive behaviors. Hutchins (1995) demonstrated this dynamic within cockpit cognitive architectures, where physical speed bugs placed along the airspeed indicator allow pilots to substitute complex numerical comparisons with immediate judgments of spatial proximity.

The most profound historical instantiation of this principle is the written page. Antiquity and early medieval manuscripts recorded language in continuous script (scriptio continua). Irish scribes initiated word separation by the late seventh century, Continental scribes adopted the practice in the tenth, and by the eleventh century the convention was universal (Saenger, 1997). The space introduced zero semantic information; every grapheme was already present. Yet by introducing visual white space, scribes transformed lexical boundary identification from an arduous phonological parsing task into automated visual pattern recognition, cutting cognitive overhead and easing rapid, silent reading (Saenger, 1997; cf. Rayner, Fischer, & Pollatsek, 1998).

### Complication: The Irreducible Algorithmic Triad

This foundational human-factors insight has failed to reach the systems through which contemporary economic and social life is coordinated. Riders and drivers, buyers and sellers, patients and providers, job applicants and employers increasingly transact across an algorithmic third party that evaluates both sides and enforces outcomes that neither participant directly controls.

Confronted with opaque intermediaries, designers, corporate leaders, and regulatory bodies reflexively default to disclosure: publish model architectures, mandate explainability statements, and maintain immutable audit trails. Yet empirical evaluations of disclosure reveal profound systemic dysfunction:

- **Delinquency and Confusion:** Credit card disclosure messages detailing repayment horizons increased delinquency among some borrowers rather than improving financial health (Seira, Elizondo, & Laguna-Müggenburg, 2017).
- **Illusion of Comprehension:** High-interpretability models with reduced feature counts impair users' ability to catch algorithmic errors during anomalous edge cases (Poursabzi-Sangdeh et al., 2021).
- **Paradoxical Perceptions:** Reading the posted rules in content moderation environments was associated with lower perceived procedural fairness among affected participants (Jhaver et al., 2019).
- **Dyadic Misalignment:** Studies demonstrating positive disclosure outcomes—such as driver intervention alerts in automated driving simulators (Matsuo et al., 2026)—occur in dyadic human-machine settings lacking an active, strategic third-party mediator.

### Concern: The Literacy Category Error

The persistent failure of disclosure stems from a foundational category error. Disclosure presents the human operator with a text—a rulebook, an explanation, a post-hoc audit log—and therefore demands a reader. It is fundamentally a literacy-based intervention.

Coordinating through an adaptive algorithmic intermediary, however, is not a reading task. It is an interactive, multi-agent navigation problem within an irreducible triad. Solving a navigation problem requires algorithmacy: the active behavioral sensibility to probe, anticipate, and respond to mediated algorithmic dynamics.

A remedy tailored for readers merely increases the cognitive tax on the people it purports to protect, leaving their underlying strategic decision paralyzed. Furthermore, disclosure tacitly consolidates institutional power. Satya Nadella's (2026) proposal to treat frontier models as "insider risks" exemplifies this dogma. By demanding tamper-proof human-readable records, model halt switches, and organizational separation between intelligence supply and authority, the framework serves the enterprise principal seeking internal operational defense. To the human transacting through the system, it offers only an autopsy record after failure has occurred. While medieval scribes answered to a church and court that ordered books made correct for their readers, digital platforms possess independent extraction objectives, maintaining terms of service that preserve unfettered corporate discretion (Suzor, 2018).

### Course of Action: Decision Experience Design and Algorithmacy

To escape the literacy trap, human-system design must return to the scribal page and re-examine word separation not as a cultural artifact, but as a cognitive design guide. Understanding an algorithmic intermediary does not come from passive inspection of its documentation; it is enacted through direct, iterative decision-making where feedback is rapid, unequivocal, and causally coupled (Kahneman & Klein, 2009; Weick, 1988).

I term this paradigm Decision Experience Design (DXD). Rather than outputting descriptive explanations, DXD re-engineers the decision interface itself. I identify two primary candidate conventions:

1. **Strategic Offloading:** Designing mechanism representations that structurally eliminate the need for tactical manipulation and visually signal that strategic gaming is obsolete.
2. **Radical Feedback Immediacy:** Collapsing the temporal and cognitive latency between user actions and intermediary state adjustments to enable rapid naturalistic calibration, where the feedback is valid.

### Contribution: Advancing Human Factors and Organizational Coordination

This paper makes three primary contributions:

1. **Establishes the Historical Mechanics of Re-Representation:** Demonstrates how word separation functioned as cognitive offloading without overclaiming historical literacy leaps.
2. **Identifies the Literacy vs. Algorithmacy Boundary:** Provides an analytical framework that sorts regulatory and design remedies by cognitive mode, explaining why disclosure mechanisms so often falter.
3. **Articulates Decision Experience Design (DXD):** Defines the operational conventions of DXD, analyzes the political economy of institutional enforcement across courts, financial markets, and platforms, and establishes the precise behavioral protocol required to test triadic systems experimentally.

# Part III: Complete Reconstructed Manuscript Outline

## Section 1: Introduction: The Space Between Decisions

- **Conceptual Narrative:** The 5Cs structural arc establishing the progression from representational human factors to algorithmic mediation.
- **Core Argument:** The shift from dyadic tools to triadic systems necessitates replacing passive literacy interventions with active algorithmacy frameworks.
- Key citations (added by Claude, from the verified card library): Zhang & Norman (1994, p. 88); Hutchins (1995, pp. 282–283); Saenger (1997, pp. 83, 85, 100, 176–177); Rayner, Fischer, & Pollatsek (1998; abstract only); Kahneman & Klein (2009, p. 524); Nadella (2026); Suzor (2018); Hunt (2026, Part 1 of the DXD series).

## Section 2: The Scribal Precedent: Word Separation as Cognitive Offloading

- **The Historical Shift:** Detailed examination of *scriptio continua* in Greco-Roman antiquity, early Insular innovations (7th century), Continental adoption (10th century), and standardization (11th century) (Saenger, 1997; Parkes, 1992).
- **Information Neutrality:** Proof that word spacing introduced zero semantic information; letters remained identical while cognitive access mechanisms transformed.
- **Historiographical Boundaries:** Rejection of naive democratization narratives; spacing did not replace formal instruction, but provided cognitive shortcuts for lexical processing.
- **The Saccadic Shift:** Transition from acoustic, subvocalized decoding to silent, automated visual boundary detection (Saenger, 1997; disputed by Knox, 1968, and Vatri, 2012; modern eye-movement evidence in Rayner et al., 1998; Mirault et al., 2019).
- Key citations (added by Claude, from the verified card library): Saenger (1997, pp. x, 8, 11, 83, 85, 100, 176–177; wording confirmed, pages need a print check); Parkes (1992; library copy needed); Knox (1968, p. 435); Heilmann (2020, pp. 181–182); Vatri (2012; known through Heilmann); Svenbro (1999, in Cavallo & Chartier); O'Donnell (2000); Tunbridge (1992); Cribiore (1996, p. 48; library copy needed); Johnson (2000, 2010); Clanchy (1993) and Cressy (1980) on what drove literacy.
- Literature to add (Claude; third-round research, audited): who enforced the conventions of the page. Charlemagne, De litteris colendis (letter to Baugulf); Admonitio generalis (789), c. 72; Alcuin, carm. XCIV; Westwell (2018). These show ruler and church ordering correct books, and none of them mentions word separation. They would replace the unsourced claim that scribes and readers shared interests, here and in Section 7.

## Section 3: The Human Factors of Re-Representation

- **Distributed Cognition Foundations:** Zhang and Norman's (1994) representational effect; converting internal search and memory storage into external perceptual cues.
- **Perceptual Substitution:** How external spatial configurations substitute perceptual recognition for logical inference (Hutchins, 1995; Larkin & Simon, 1987).
- **Cognitive Offloading Mechanics:** Risko and Gilbert (2016) on environmental offloading; Kirsh (1995) on the intelligent use of space.
- **Cross-Orthographic Asymmetries:** The directional asymmetry of conventions—removing spaces cripples fluent readers, but adding spaces to non-spaced writing systems (e.g., Chinese, Thai) yields complex, non-linear effects (Bai et al., 2008; Winskel et al., 2009).
- **The Fundamental Divergence:** A manuscript page is passive, static, and cooperative; an algorithmic mediator is dynamic, adaptive, and possesses private extraction incentives.
- Key citations (added by Claude, from the verified card library): Zhang & Norman (1994, p. 88); Larkin & Simon (1987); Hutchins (1995, pp. 282–283); Kirsh & Maglio (1994, p. 513); Kirsh (1995); Risko & Gilbert (2016, Box 3); Scaife & Rogers (1996, p. 210); Vicente & Rasmussen (1992). Removing spaces: Rayner, Fischer, & Pollatsek (1998; abstract only); Mirault et al. (2019). Adding spaces: Bai et al. (2008); Winskel et al. (2009); Kohsom & Gobet (1997); Chantavarin & Leung (2025); Wang et al. (2024); Bassetti & Masterson (2012).
- Literature to add (Claude; third-round research, audited): display-design principles the outline has not used. The proximity compatibility principle (Wickens & Carswell, 1995); the split-attention effect from cognitive load theory (effect size not yet verified); Norman's gulfs of execution and evaluation (his texts not yet read), under which Convention A narrows the gulf of execution and Convention B the gulf of evaluation. Caution from the nudge literature: Mertens et al. (2022, as corrected) class re-representing information ("translation") with informational interventions, the weaker category.

## Section 4: The Failure of Disclosure: A Literacy Intervention in an Algorithmic Arena

- **The Literacy Fallacy:** Explainable AI (XAI) and disclosure mandates treat transacting agents as literary critics analyzing post-hoc prose rather than actors navigating live systems (Ben-Shahar & Schneider, 2011; Schemmer et al., 2022; Vaccaro, Almaatouq, & Malone, 2024).
- **Empirical Failure Synthesis:**
  - Regulatory disclosure backfiring in finance (Seira et al., 2017).
  - Interpretability paradoxes in algorithmic edge cases (Poursabzi-Sangdeh et al., 2021).
  - Procedural fairness paradoxes in platform moderation (Jhaver et al., 2019).
  - Dyadic vs. triadic boundary conditions (Matsuo et al., 2026).
- **Critique of the Enterprise Paradigm:** Close reading of Satya Nadella's (2026) "Models as Insider Risks":
  - Recognition of "neuralese" and the insufficiency of chain-of-thought visibility.
  - Diagnosis of the enterprise solution: audit logs, brake switches, and human verification (CERT, 2022).
  - Theoretical flaw: Resolves principal-agent compliance for the firm while abandoning the external user to post-hoc autopsy notices.
- Key citations (added by Claude, from the verified card library): Seira, Elizondo, & Laguna-Müggenburg (2017, pp. 292, 295); Poursabzi-Sangdeh et al. (2021); Jhaver et al. (2019); Cabrera et al. (2023); Buçinca et al. (2021); Ananny & Crawford (2018). Where disclosure helped: Matsuo et al. (2026); Vasconcelos et al. (2023). Where the field stops short of disclosure: Korbak et al. (2025, p. 7); Regulation (EU) 2019/1150, Art. 5(6). On the insider post: Nadella (2026); CERT (2022, practice 12); Chan et al. (2025); Kutasov et al. (2025); Parasuraman & Manzey (2010); Green (2022); Rieder & Hofmann (2020).
- Literature to add (Claude; third-round research, audited): (1) The law-and-economics critique of mandated disclosure states the paper's mechanism: people do not read, understand or use disclosures (Ben-Shahar & Schneider, 2011, p. 665; Loewenstein, Sunstein, & Golman, 2014; Fung, Graham, & Weil, 2007). Disclosures that work are simple signals and often act on the discloser, not the reader (Ben-Shahar & Schneider, 2011, pp. 743–748). (2) Explanations do not improve decisions on average: Schemmer et al. (2022; SMD 0.07, 95% CI −0.15 to 0.30); Vaccaro, Almaatouq, & Malone (2024; 370 effect sizes). (3) Layout moves consent while the information stays fixed (Nouwens et al., 2020). (4) The nearest rival position is nudging against boosting (Hertwig & Grüne-Yanoff, 2017, pp. 977, 981); the measured case for structure over information is modest (Mertens et al., 2022, as corrected; Maier et al., 2022). (5) Disclosure often changes behaviour without improving outcomes, so the claim should be about performance: a one-line statement that a mechanism is strategy-proof raised sincere bidding from 20.6% to 46.9% and efficiency by about one point (Masuda et al., 2022). Split "disclosure" into presence of an algorithm, its objective, a property of its rule, and the rule's text.

## Section 5: From Literacy to Algorithmacy: Epistemic Action in Triadic Systems

- **Sensemaking Through Probing:** Karl Weick's (1988) enacting sensemaking—understanding opaque systems requires action before comprehension.
- **Epistemic Actions:** Kirsh and Maglio (1994) on actions executed to uncover latent system states rather than advance pragmatic task completion (by extension, gig workers probing surge boundaries; Lee et al., 2015).
- **Conditions for High-Validity Learning:** Kahneman and Klein (2009) and Rahmandad & Gary (2023) on ecological validity, unambiguous feedback, and temporal latency.
- **The Mediated Distortion:** How platforms withhold their rules, by their own account to prevent gaming and on Rahman's (2019) reading to keep control, while noise and delayed payoffs, whatever their cause, cripple human learning loops (Chen, Mislove, & Wilson, 2015; Lee et al., 2015).
- Key citations (added by Claude, from the verified card library): Weick (1988, pp. 305–307); Kirsh & Maglio (1994, pp. 513–515); Kahneman & Klein (2009, p. 524); Rahmandad & Gary (2023, pp. 13, 17); Brehmer & Nählinder (2004); Smith & Hancock (1995, p. 141). Learning on platforms: Cook et al. (2021; working-paper version); Heiland (2023); Rosenblat & Stark (2016). Monitoring against acting: Hutchins (1995, pp. 283, 285); Dismukes & Berman (2010).
- Literature to add (Claude; third-round research, audited): (1) Intent. Platforms withhold their rules; the stated reason is to prevent gaming, and Rahman (2019 dissertation, pp. 128–129; the 2021 ASQ article not yet read) also reads the secrecy as keeping control with the platform. No source shows intent behind noise or delay: the one traced case, the jitter in Uber's surge prices, was a bug by Uber's account (Chen, Mislove, & Wilson, 2015). The "Mediated Distortion" bullet should be split accordingly. (2) Strategic classification models people adapting to a decision rule (Hardt et al., 2016); where the rule is hidden, people infer it from other people's outcomes (Ghalme et al., 2021; Bechavod et al., 2022), so learning is social as well as enacted. (3) Recourse: Ustun, Spangher, & Liu (2019); Karimi et al. (2022). (4) What drivers could and could not learn by acting (Lee et al., 2015); collective sensemaking and resistance (Kellogg, Valentine, & Christin, 2020; Cameron & Rahman, 2022). (5) The counter-literature: people do learn markets by experience (List, 2003; Cook et al., 2021), subject to attrition (Seru, Shumway, & Stoffman, 2010).

## Section 6: Decision Experience Design (DXD): Candidate Structural Conventions

- **Convention A: Strategic Offloading:**
  - *Mechanism:* Making strategic manipulation structurally unnecessary via interface-level obvious strategy-proofness (Li, 2017; Rees-Jones & Skowronek, 2018).
  - *Implementation:* The interface visually proves dominant-strategy truthfulness, reducing game-theoretic second-guessing.
  - *Limitations:* User inertia and residual suspicion in high-stakes environments; about four in ten participants still deviate under the best presentation tested (Gonczarowski, Heffetz, Ishai, & Thomas, 2024).
- **Convention B: Radical Feedback Immediacy:**
  - *Mechanism:* Collapsing the temporal and causal gap between choice and mediator state response.
  - *Implementation:* Real-time visual heatmaps, dynamic constraint curves, and immediate micro-signals replacing terminal logs.
  - *Limitations:* Platform resistance to surrendering tactical information rents; frequent feedback on noisy outcomes lowers performance (Larson, List, & Metcalfe, 2016; Kluger & DeNisi, 1996), so validity comes before speed.
- **Functional Separation:** Convention A governs market clearing and allocation matching; Convention B governs real-time execution and dispatch environments.
- Key citations (added by Claude, from the verified card library): Convention A: Li (2017, §5.3; working-paper version); Rees-Jones & Skowronek (2018); Ashlagi & Gonczarowski (2018); Gonczarowski, Heffetz, & Thomas (2023; theory only in the version read); Arteaga et al. (2022) on where the removed task goes; Kling et al. (2012). Convention B has no tested intervention behind it yet: Kahneman & Klein (2009, p. 524) for the condition; Shneiderman (1983); Harper et al. (2015); Kuhl et al. (2023), which did not replicate its own gain. Against bounded control beating free control: Dietvorst et al. (2018).
- Literature to add (Claude; third-round research, audited): Convention A. Gonczarowski, Heffetz, Ishai, & Thomas (2024; N = 542) is the experiment on presentation: a menu description raised understanding (71% against 58% and 56%) more than it raised straightforward play (59%, against 56% for the traditional description and 48% for the control), so about four in ten still deviate under the best presentation tested. Masuda et al. (2022): stating that the mechanism is strategy-proof raised sincere bidding from 20.6% to 46.9%. Convention B. The evidence puts validity before speed. Real-time feedback helps on a steady quantity the person controls (Tiefenbeck et al., 2018). On noisy, revisable choices it harms: traders given frequent price feedback invested about 25% less in the risky asset and earned about 35% less (Larson, List, & Metcalfe, 2016), and more than a third of feedback interventions lower performance (Kluger & DeNisi, 1996, 1998). "Radical feedback immediacy" should be restated as valid and plain first, then quick. Platform-run tests exist: a driver leaderboard (Ye et al., 2022; +1.66% weekly revenue) and a seller dashboard (Bar-Gill, Brynjolfsson, & Hak, 2024; +3.6% revenue). No controlled test of upfront fares, destination displays or surge maps was found.

## Section 7: Institutional Custody: Who Enforces the Convention?

| Institutional Realm | Primary Enforcement Authority | Historical / Structural Mechanism | Core Structural Vulnerability |
| --- | --- | --- | --- |
| **Courts** | Statutory mandates & judicial oversight | Procedural rules; judge disqualification under conflicts (*Tumey v. Ohio*) | High procedural friction; systematic bias toward repeat players (Galanter, 1974) |
| **Dealer FX Markets** | Voluntary industry coalitions | Conduct codes (FX Global Code) | Absence of binding statutory force; vulnerable to benchmark manipulation (FCA, 2014) |
| **Digital Platforms** | Private corporate governance | Unilateral terms of service (ToS); proprietary algorithms | Direct profit extraction conflicts; broad proprietor discretion (Suzor, 2018) |

- **Theoretical Conclusion on Enforcement: The conventions of the written page were enforced by ruler and church, institutions with standing over the scribe. Algorithmic platforms operate with extractive objectives. DXD conventions are unlikely to emerge through voluntary corporate self-regulation; they require statutory mandates (e.g., EU Digital Services Act, Platform-to-Business Regulation, Platform Work Directive 2024/2831) or collective bargaining pressure.**
- Key citations (added by Claude, from the verified card library): Courts: Tumey v. Ohio (1927); Mathews v. Eldridge (1976); 28 U.S.C. § 2073; Galanter (1974, pp. 97–103); Tyler (1988, p. 131); Colvin (2011). Dealer FX: Global Foreign Exchange Committee (2024), Principles 7, 9, 36, 39, 40; FCA (2014); FSB (2014); NYDFS (2015). Platforms: Suzor (2018); Klonick (2018, pp. 1664–1665); Regulation (EU) 2019/1150, Art. 3; Regulation (EU) 2022/2065, Arts. 17, 20, 53–54; Seattle Office of Labor Standards (2024); Oversight Board (2022, p. 9); Douek (2024); Nagaraj Rao et al. (2026). Interested owner: Jensen & Meckling (1976; source copy needs a check).
- Literature to add (Claude; third-round research, audited): (1) Statute that goes beyond disclosure. Directive (EU) 2024/2831 on platform work, in force since 1 December 2024 with transposition due by 2 December 2026: a human must take suspension and termination decisions (Art. 10(5)); a decision that infringes a worker's rights must be rectified within two weeks or compensated (Art. 11(3)); a discriminating system is to be modified or discontinued if appropriate (Art. 10(3)); some data processing is banned (Art. 7); worker representatives are consulted with an expert (Art. 13). It gives no veto. (2) Co-determination: BetrVG §87(1) no. 6 binds the employer through arbitration. (3) Standards bodies bind no implementer (IAB, RFC 8890). (4) Governance models and their limits: Gorwa (2019); Balkin (2016); Khan & Pozen (2019). (5) The Carolingian sources listed under Section 2 show the page's conventions were enforced by ruler and church, which supports this section and replaces the first sentence of the conclusion. (6) A test the section could adopt, which is Claude's inference and not a finding: can the owner change the convention alone?

## Section 8: Testing the Irreducible Triad: Experimental Boundary Conditions

- **Formalizing Irreducibility:** Measuring system coordination through Integrated Information (Phi) to gauge triadic non-decomposability into isolated dyadic pairs, with the measure, state coding, lag and partition fixed in advance and validated on the lab's Boolean models.
- **Multi-Agent Laboratory Architecture:** Two interacting human participants (Party A and Party B) coordinating exchange through an algorithmic mediator (M) optimizing a distinct objective function (cf. Casella, Friedman, & Perez Archila, 2024, whose mediator maximises agreement and shows its rule).
- **Experimental Treatments:**
  - *Control:* Baseline black-box matching with terminal payout.
  - *Treatment 1 (Literacy / Disclosure):* Complete textual disclosure of matching heuristics, rules, and historical audit logs.
  - *Treatment 2 (DXD / Strategic Offloading):* Interface providing structural strategy-proof representations.
  - *Treatment 3 (DXD / Radical Feedback Immediacy):* Continuous real-time visual constraint signaling, with a discrete-time arm carrying the same information.
- **Measured Dependent Variables:** Pareto coordination efficiency, error-correction latency, surplus distribution, and strategic manipulation rates.
- Key citations (added by Claude, from the verified card library): Nearest existing designs: Li (2017); Rees-Jones & Skowronek (2018); Hohenstein et al. (2023); Terrucha et al. (2025); Zhu et al. (2026); Liu (2026). Disclosure arm: Matsuo et al. (2026); Poursabzi-Sangdeh et al. (2021). Feedback arm: Rahmandad & Gary (2023). Irreducibility: the lab's own integrated-information results (dissertation Papers 2 and 3), which are computed on Boolean models and have not yet been run on human participants. No experiment in the library tests any convention in a triad with a behavioural outcome.
- Literature to add (Claude; third-round research, audited): (1) The closest precedent is Casella, Friedman, & Perez Archila (working paper, 2024): two people bargain through a computer mediator that maximises the chance of agreement, with its rule shown on screen every round and no condition that varies what is shown. No study found gives the mediator an objective of its own or varies what participants are told about it. (2) Related results: Normann & Sternberg on an algorithm among human firms; Ishowo-Oloko et al. (2019) on disclosing a bot's identity; Masuda et al. (2022). (3) Integrated information on human groups: Engel & Malone (2018; 68 groups, a proxy measure, r = .37 with collective intelligence, no mediator). Barrett et al. (2026, preprint) write that Phi "has not been computed on any real physical system", only proxies. The section should name the measure, the coding of behaviour into states, the lag, the partition, and the lab's Boolean models as the validation set. (4) Design additions: a discrete-time arm with the same information as the continuous-feedback arm; a decision on whether participants are told the mediator's payoffs; the deception norm that an undescribed rule is acceptable and a false statement is not (Charness, Samek, & van de Ven, 2022); power at the level of the triad; joint surplus preregistered as the primary outcome.

## Section 9: Boundary Conditions, Limitations, and Research Agenda

- **Historical Scope Limits:** Distinguishing static orthographic reform from dynamic algorithmic learning models.
- **Conceptual Disambiguation:** Differentiating sociological algorithmacy (triadic sociotechnical navigation) from an earlier, undefined use in informatics teaching (e.g., Oberschelp, 1995).
- **Future Empirical Horizons:** Extending DXD beyond commercial matching platforms to clinical decision triage, algorithmic bail systems, and autonomous multi-agent networks.
- Key citations (added by Claude, from the verified card library): Limits of the precedent: Vicente & Rasmussen (1992); Scaife & Rogers (1996); Street (2003); Scribner & Cole (1981; pages unconfirmed). Earlier printed use of the word: Oberschelp (1995, p. 121). Unread and needed from a library: Saenger (1997) and Parkes (1992) beyond the confirmed passages; Vatri (2012); Gavrilov (1997); Burnyeat (1997).
- Literature to add (Claude; third-round research, audited): limits the new research adds. Integrated information is untested on human triads. The nudge literature classes re-representation with informational interventions (Mertens et al., 2022, as corrected). The claim that working disclosures are re-representations is the paper's argument and no source states it. Two reviews of human-algorithm strategic interaction were not opened (March, 2021; Chugunova & Sele, 2020), so the statement that no triadic disclosure experiment exists is limited to the sources searched.

# Part IV: Immediate Manuscript Execution Checklist

- **Archival Verification:** Verify physical page references and exact effect sizes in Saenger (1997) and Rayner et al. (1998).
- **Theoretical Drafting:** Draft Section 4 focusing on the category error of disclosure and the critique of enterprise insider-risk compliance models.
- **Formal Parameterization:** Define the explicit payoff matrices and Integrated Information (Phi) boundary metrics for the triadic laboratory experiment in Section 8.
