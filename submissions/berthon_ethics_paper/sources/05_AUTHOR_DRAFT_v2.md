<!-- The author's second draft, supplied on 2026-10-13 and saved byte-for-byte from the session transcript. Claude changed nothing. Reviews are in review/. -->

Algorithmacy: Institutional Domination, Triadic Mediation, and the Limits of Literacy in Algorithmic Governance

Abstract

Current AI ethics frameworks routinely prescribe "AI literacy" and post-hoc explanation as the primary safeguards against algorithmic harm. Yet when reading and writing became mandatory conditions for civic and legal standing, the deepest injuries did not arise from an uneducated public. They were inflicted by the institutions that controlled the test, the access, and the record. Drawing on republican theories of non-domination and internal social critique, this paper examines the historical transition to literacy to theorize algorithmacy—the relational competence demanded when two human parties coordinate through an opaque algorithmic intermediary that observes both and commits binding outcomes. Assessing the historical record against standards internal to their eras, I analyze five institutional practices: gating standing on arbitrary tests, withholding competence by statute, elevating the written text over oral pacts, monopolizing the means of reproduction, and overselling economic returns. Mapping these practices onto platform coordination reveals that educational remedies fundamentally misdiagnose structural extraction. Algorithmic intermediaries subject users to arbitrary, illiberal power not merely by repeating historical exclusions, but by adapting dynamically against the person evaluated while stripping away the independent procedural buffers—sworn notaries, second interpreters, and pleas such as non est factum—that once restrained human scribes. Grounded in a social-connection model of institutional responsibility, the paper derives three normative obligations for platform operators and designers: structural refusal, declared operating envelopes, and infrastructural counter-delegation.

1. Introduction

People now reach credit, work, and civic standing through algorithmic systems that read their behavior and commit binding decisions. Scholars who write on the ethics of these systems agree on a first duty: do no harm. Jobin, Ienca, and Vayena (2019) reviewed 84 sets of AI-ethics guidelines and found non-maleficence named in 60 and beneficence in 41. In business ethics and regulatory policy alike, the remedy most frequently derived from that duty is to inform the affected person—mandating disclosure, grounding a moral right to an explanation (Kim & Routledge, 2022), and training the user under the banner of "AI literacy." Yet disclosure and individual upskilling rarely alter the distribution of power (Edwards & Veale, 2017; Scherer et al., 2023). As Berthon, Pitt, and Campbell (2019, p. 457) observe of digital addiction, "information is necessary, but not sufficient to change behavior". Williams (2018, p. 101) reaches the same boundary in the attention economy, warning that education alone will not rescue users, "Nor will 'media literacy' alone lead us out of this forest." Kamperman and Graff (2026, p. 36) look to the history of reading for the reason: the AI-literacy movement repeats the nineteenth-century myth that individual literacy guarantees economic security. The comparison between learning to read and learning to live with algorithms is already on the table (Vee, 2013; Kamperman & Graff, 2026), but existing critiques center the skill and its overpromised returns rather than the institutional positions surrounding it.

Overselling, however, was the smallest part of what went wrong when reading became a condition of legal and civic standing. The deeper wrongs were committed by the actors who held the test, the access, and the record—and they committed them with literacy. When Alabama’s constitutional convention met in 1901 to write a voter literacy test into the franchise, its president told the delegates plainly what they had gathered to establish: "white supremacy in this State" (Alabama Constitutional Convention, 1901, p. 8). Half a century earlier, Hugh Auld forbade his wife to teach Frederick Douglass to read because literacy would "forever unfit him to be a slave" (Douglass, 1845, p. 33). And when the Supreme Court of Canada examined a 1760 treaty in R. v. Marshall (1999, para. 14), it noted that Mi'kmaq signatories had no practical opportunity to create their own written record of the negotiations, allowing Crown scribes to overwrite oral covenants. None of these injuries was a mere educational deficit or a broken promise. Each was an exercise of arbitrary institutional power—domination, in the republican sense (Pettit, 1997; Bhargava & Young, 2022)—made possible once a private competence was turned into a compulsory gate. Prior critiques of AI literacy do not examine these positions, leaving business ethics without an account of who occupies them today.

That omission matters because the positions are occupied. When a job applicant, borrower, or gig worker deals with an employer, lender, or rider through a digital platform, two human parties coordinate through an automated third party that reads both and enforces an outcome binding on both (Stark & Vanden Broeck, 2024). I call the relational competence this triad demands algorithmacy. Within this structure, the platform intermediary occupies the exact positions that generated illiberal domination during the literacy transition. It holds the test: when employers share an algorithmic screening vendor, applicants rejected by one model face systematic exclusion across every employer using it (Bommasani et al., 2026; Bhargava & Assadi, 2024). It controls access to the competence: a ride-hail driver has roughly fifteen seconds to accept a dispatch without seeing the destination or fare (Rosenblat & Stark, 2016, p. 3762). And it monopolizes the record: workers who contest automated deactivations or pay deductions are met with template replies from a closed ledger (Rosenblat & Stark, 2016, p. 3771). If the lesson of the literacy transition were simply that reformers oversold reading, better user training and clearer explanations would suffice. Because the historical wrongs were committed by whoever held the test, the access, and the record, an ethics centered on educating the user addresses the wrong party.

To establish what obligations bind the party in the middle, I examine the historical record of the literacy transition for what named institutions—legislatures, courts, churches, and chartered guilds—did with written competence once standing depended on it. To avoid anachronism, I evaluate historical practices using internal critique (Walzer, 1988), counting a practice as an ethical failure only when contemporaries condemned it, when institutional actors violated standards they themselves professed, or when outcomes fell systematically short of stated promises. Five institutional practices meet those benchmarks: gating civic standing on discretionary reading tests, withholding the competence by statute, allowing written records to erase oral agreements, enclosing print infrastructure by monopoly charter, and promoting individual literacy as a cure for structural inequality. Treating this history as empirical evidence and its algorithmic counterpart as a bounded analogy, I isolate the mechanisms that map onto digital platforms—and pinpoint the exact boundaries where the historical parallel fails.

The paper makes three contributions to normative business ethics:

1. From Collective Myth to Institutional Domination: It replaces the diffuse charge that "society" failed to spread literacy with five documented institutional practices, demonstrating that each operated as a mechanism of republican domination (Pettit, 1997; Hsieh, 2008; Muldoon & Raekstad, 2023)—arbitrary power exercised over vulnerable parties through control of a compulsory medium—while reserving collective blame strictly for formal international campaigns that set and missed explicit targets.
2. Shifting the Ethical Locus from Competence to Position: It moves the analogy between literacy and algorithmic mediation away from individual user skill toward the triadic positions surrounding the intermediary (Simmel, in Wolff, 1950; Brandt, 1998). Educational remedies and post-hoc explanations cannot cure harms rooted in structural control over the gate, the access, and the record.
3. Identifying Structural Divergence and Normative Design Duties: It pinpoints two critical respects in which algorithmic mediation is more hazardous than scribal mediation: the intermediary adapts dynamically against the person it reads, and platforms operate without any independent, binding counterpart to the procedural safeguards—sworn notaries, second interpreters, and common-law pleas like non est factum—that historically restrained human scribes. From this divergence, the paper derives three architectural duties for platform operators: structural refusal, declared operating envelopes, and infrastructural counter-delegation.

2. Normative and Conceptual Framework: Triadic Mediation, Non-Domination, and Internal Critique

2.1 Algorithmacy as a Triadic Relation, Not a Cognitive Metaphor

The dominant metaphors in contemporary AI policy treat human interaction with computational systems as a dyadic dialogue. Users prompt an artificial intelligence; the model answers. Users submit their credentials to an automated portal; the software outputs a score. This framing conceals the social reality of modern computational governance. Interaction with platform algorithms rarely constitutes a closed loop between a solitary individual and a cognitive prosthetic. Instead, algorithmic systems function as irreducible intermediaries wedged between multiple human actors whose economic, legal, and social fates depend upon mutual coordination.

Historically, oracy required the co-located, dyadic presence of speaker and listener. The emergence of writing altered this baseline by introducing an inanimate symbolic medium that dissociated author from reader across time and space. The inscription on parchment or paper remained passive; it held words, conveyed meaning, and preserved memory without executing independent actions upon the counterparty. Algorithmacy marks a qualitative departure from this dynamic. I define algorithmacy as the relational competence demanded when human agents must coordinate with one another through an automated third party that processes, evaluates, and enforces outcomes binding on both sides.

               TRIADIC COORDINATION ARCHITECTURE OF ALGORITHMACY

                       [Human Subject A: Worker / Applicant]
                                  ▲              │
            (Asymmetric Telemetry/│              │(Labor / Behavioral Data /
             Evaluative Scoring)  │              │ Token Submission)
                                  │              ▼
                           ┌────────────────────────────┐
                           │   Algorithmic Third Party   │
                           │ (Platform Intermediary API, │
                           │   Models, Loss Functions)   │
                           └────────────────────────────┘
                                  ▲              │
            (Capital Allocation / │              │(Extracted Surplus /
             Policy Constraints)  │              │ Dynamic Coordination)
                                  │              ▼
                       [Human Subject B: Employer / Capital]


This triadic architecture echoes Georg Simmel’s classic sociological distinction between an impartial mediator (der Unparteiische) and the opportunistic third who profits (tertius gaudens) (Simmel, in Wolff, 1950, p. 154). The platform intermediary is neither an indifferent pipeline nor a detached magistrate. Because the system optimizes for its operator’s proprietary objective function—maximizing engagement, compressing labor costs, or managing credit risk—it actively exploits the informational asymmetries separating the two flanking parties. Deborah Brandt (1998, p. 166) observed that literacy always possessed "sponsors"—agents, institutions, and forces that subsidized, acquired, and exerted control over the literacy of others. In algorithmacy, the intermediary does not merely sponsor the acquisition of a skill. It stands permanently inside the communicative channel, co-opting both sides’ inputs into raw material for its own optimization parameters.

Treating algorithmacy as a triadic relation dismantles the idea that digital equity can be achieved through user education. Kamperman and Graff (2026) caution against extending literacy metaphors indiscriminately, noting that Brian Street’s (1984, 2003) critique of the "autonomous model of literacy" applies with equal force to modern technology. When policymakers treat literacy as an autonomous, neutral cognitive skill, they untether reading from the institutional power relations that determine its material value. Treating algorithmacy as a personal cognitive capacity makes the same mistake. When a delivery worker is penalized by an dispatch algorithm for taking a bathroom break, the injury is not that the worker lacks statistical fluency or computational comprehension. The injury stems from their structural position relative to an automated third party that exercises arbitrary power over their livelihood.

2.2 Republican Non-Domination and Institutional Agency

Evaluating this triadic relationship requires a normative anchor suited to structural asymmetries. Classical liberal ethics centers on negative liberty—the absence of actual, physical interference with an individual’s choices. Under that framework, platform arrangements frequently appear benign or consensual. Drivers accept dispatches via mobile applications; job applicants upload resumes to automated portals; consumers scroll through algorithmic feeds, consenting at every turn through boilerplate clickwrap agreements. So long as no explicit coercion or overt fraud can be proven, negative liberty identifies no formal injustice.

Neo-republican political theory offers a much sharper diagnostic. Drawing on Philip Pettit (1997), republican freedom is defined not as the mere absence of interference, but as the absence of domination—the condition of being protected against the arbitrary power of another. An agent dominates another when they possess the structural capacity to interfere in that person’s choices at will, according to their own arbitrary discretion, without accountability to the affected party’s tracked interests. Domination does not require constant hostility or cruelty. As Pettit notes, a benevolent slaveholder who permits his enslaved workers wide latitude remains a slaveholder. The injury resides in the unconstrained capacity to intervene, which forces the vulnerable party to anticipate the master’s whims, adopt deferential behaviors, and navigate life under chronic precarity.

Business ethicists have demonstrated that republican non-domination applies directly to organizational hierarchies and automated management. Nien-hê Hsieh (2008) deployed the republican framework to challenge arbitrary managerial power in the workplace, arguing that meaningful worker agency requires robust institutional protections against unchecked managerial discretion. Bhargava and Young (2022) extended this insight to the doctrine of employment-at-will, demonstrating that the employer's unilateral right to terminate workers without cause subjects employees to pervasive republican domination, regardless of whether that termination power is actively exercised. Building on this foundation, Muldoon and Raekstad (2023) demonstrated that gig economy platforms subject workers to algorithmic domination: the platform retains unilateral, real-time power to alter pay rates, throttle order allocations, and deactivate accounts without notice or meaningful contestation.

Tracing domination within algorithmic systems requires attributing responsibility to concrete institutional agents. When critics claim that "technology" or "society" is moving too fast, they dissolve corporate and governmental agency into passive fatalism. Michele Moody-Adams (1994, p. 304) terms this evasion "the myth of culture as an engine of moral blindness," warning that attributing moral culpability to diffuse cultural forces obscures the human decisions that maintain exploitative arrangements. Platform algorithms do not materialize from thin air. They are designed, tuned, deployed, and monetized by specific corporations, executives, and engineering teams.

To hold these institutions accountable across complex supply chains, I turn to Iris Marion Young’s (2006) social-connection model of responsibility. Unlike the traditional liability model, which assigns blame strictly to an actor who directly commits a distinct, localized tort, the social-connection model assigns forward-looking political responsibility to all actors who participate in and profit from the structural processes that produce injustice. Platform intermediaries occupy the structural nexus of the algorithmic triad. They extract economic value from the transactions they mediate. Consequently, they bear an unavoidable, prospective obligation to redesign the structural conditions under which those transactions take place.

2.3 Internal Critique, Affected Ignorance, and the Bounded Value of Literacy

To demonstrate that the literacy transition was marked by institutional domination rather than mere educational scarcity, I use Michael Walzer’s (1988) method of internal critique. Evaluating past institutions against modern ethical sensibilities risks anachronism and whiggish historical distortion (Butterfield, 1931). Internal critique avoids this by evaluating institutional behavior against the values, commitments, and norms that the institutions themselves claimed to uphold.

I identify an institutional practice as an ethical failure only when it satisfies at least one of three historical benchmarks:

1. Contemporaries actively condemned the practice as an abuse of power using the moral vocabulary of their own time;
2. Institutional actors systematically subverted the procedural and ethical standards they publicly professed; or
3. The material outcomes systematically violated the explicit promises made by the sponsoring institutions.

Where the historical record shows widespread institutional acquiescence—as when colonial courts routinely privileged written English treaties over Indigenous oral agreements—the absence of explicit protest from dominant actors does not imply moral innocence. Moody-Adams (1994, pp. 293–296) conceptualizes this phenomenon as "affected ignorance": the deliberate refusal to attend to moral considerations that one has the capacity to know, driven by an unacknowledged desire to preserve one's material advantage. When scribes, administrators, and judges ignored the obvious comprehension asymmetries of their counterparties, they engaged in affected ignorance. They chose not to see the structural violence encoded in their scrolls.

┌────────────────────────────────────────────────────────────────────────┐
│               INTERNAL CRITIQUE EVALUATIVE MATRIX                      │
├──────────────────────────────┬─────────────────────────────────────────┤
│ Walzer's Internal Benchmark  │ Manifestation in Literacy / Algorithms  │
├──────────────────────────────┼─────────────────────────────────────────┤
│ 1. Contemporary Condemnation │ Frederick Douglass (1845) on slavery;   │
│                              │ gig workers organizing against black-   │
│                              │ box deactivations (Dubal, 2023).        │
├──────────────────────────────┼─────────────────────────────────────────┤
│ 2. Violation of Professed    │ 1901 Alabama Convention claiming civic  │
│    Standards                 │ competence while pursuing white         │
│                              │ supremacy (Alabama Convention, 1901).   │
├──────────────────────────────┼─────────────────────────────────────────┤
│ 3. Systematic Shortfall from │ Missed international literacy targets   │
│    Explicit Promises         │ (UNESCO, 2015); AI literacy failing     │
│                              │ to reverse platform deskilling.         │
├──────────────────────────────┼─────────────────────────────────────────┤
│ Moody-Adams's Benchmark:     │ Scribes ignoring oral covenants         │
│ Affected Ignorance           │ (*R. v. Marshall*, 1999); tech firms    │
│                              │ ignoring known proxy bias (Levin, 2016).│
└──────────────────────────────┴─────────────────────────────────────────┘


This critique targets the weaponization of the medium, not the competence itself. Reading opened genuine pathways to personal autonomy, economic participation, and civic organizing. Marginalized groups recognized this value and fought to acquire it, often at great personal peril (Johansson, 1985; Washington, 1901; Graff, 1979). The historical evil was not literacy; it was the unilateral turning of literacy into a compulsory barrier, controlled by dominant institutions to police civic belonging and economic survival.

3. Historical Evidence: Five Modes of Institutional Domination in the Literacy Transition

The historical record reveals five distinct practices through which dominant institutions used written competence to exercise republican domination once legal, commercial, and civic standing depended upon it.

┌─────────────────────────────────────────────────────────────────────────┐
│        FIVE MODES OF INSTITUTIONAL DOMINATION IN MEDIATED TRANSITIONS   │
├────────────────────────────┬────────────────────────────────────────────┤
│ Historical Mode            │ Institutional Mechanism                    │
├────────────────────────────┼────────────────────────────────────────────┤
│ 1. The Discretionary Gate  │ Facially neutral tests administered with   │
│                            │ absolute local discretion to exclude.      │
├────────────────────────────┼────────────────────────────────────────────┤
│ 2. Withheld Competence     │ Statutory criminalization of instruction   │
│                            │ to enforce dependency and labor control.   │
├────────────────────────────┼────────────────────────────────────────────┤
│ 3. Record Over Voice       │ Bureaucratic inscriptions overwriting oral │
│                            │ consensus; structural testimonial injustice│
├────────────────────────────┼────────────────────────────────────────────┤
│ 4. Chartered Monopoly      │ Royal/corporate enclosures of reproductive │
│                            │ infrastructure to suppress unsanctioned use│
├────────────────────────────┼────────────────────────────────────────────┤
│ 5. Responsibilized Promise │ Individualizing systemic burdens via false │
│                            │ promises of guaranteed economic mobility.  │
└────────────────────────────┴────────────────────────────────────────────┘


3.1 The Gate: Facial Neutrality and Discretionary Exclusion

The most visible mechanism of institutional domination is the discretionary literacy gate: an ostensibly neutral examination of competence deployed to exclude targeted populations from civic standing. The voter literacy tests enacted across the American South following the Reconstruction era illustrate this dynamic with stark clarity.

Following the ratification of the Fifteenth Amendment, Southern legislatures could no longer disenfranchise Black citizens through explicit racial classifications. Instead, they constructed facially neutral administrative barriers (South Carolina v. Katzenbach, 1966). When delegates assembled for the Alabama Constitutional Convention of 1901, the convention's president, John B. Knox, delivered an opening address that unmasked the institutional strategy. Knox acknowledged that the Fourteenth and Fifteenth Amendments prohibited direct racial exclusions, but assured the delegates that an administrative literacy requirement, combined with discretionary property and character clauses, would achieve the identical result:

"And what is it that we want to do? Why it is, within the limits imposed by the Federal Constitution, to establish white supremacy in this State." (Alabama Constitutional Convention, 1901, p. 8)

The statutory device rested on absolute administrative discretion. Registrars were empowered to evaluate whether an applicant could read and "correctly explain" complex clauses of the state or federal constitution. White registrars posed simple questions to illiterate white applicants while subjecting Black college graduates to impossible legal parsing tests (Kousser, 1974). The practice violated the internal standard of procedural fairness that Anglo-American constitutional law claimed to revere. State authorities operated segregated, grossly underfunded school systems that deliberately withheld literacy from the Black population, and then invoked that lack of literacy to deny them the franchise (Gaston County v. United States, 1969).

This institutional mechanism was not confined to the American South. Across the globe, colonial and post-colonial states adapted the literacy gate to regulate movement, race, and capital. Section 3(a) of the Australian Immigration Restriction Act of 1901 empowered customs officials to administer a fifty-word dictation test in any European language selected at the officer’s discretion. An educated migrant fluent in English could be intentionally failed by an officer administering the test in Welsh, Greek, or Italian. The statute mirrored the Natal Immigration Restriction Act of 1897, which British imperial authorities exported across the Commonwealth to construct racial exclusions under the guise of bureaucratic competence (Lake, 2006). Similar statutory gates appeared in nineteenth-century Latin America: Brazil’s Saraiva Law of 1881 and constitutional provisions across Chile, Peru, and Bolivia disenfranchised indigenous and Afro-descendant majorities by conditioning citizenship on written literacy (Engerman & Sokoloff, 2001).

The ethical failure of the gate did not escape contemporary notice. When the United States Congress passed statutory literacy tests for incoming immigrants in 1897 and 1917, successive presidents vetoed the measures. In his 1897 veto message, President Grover Cleveland condemned the test as a betrayal of democratic principles, declaring: "It is said that the quality of recent immigration is undesirable. The time is quite within recent memory when the same thing was said of immigrants who, with their descendants, are now numbered among our best citizens." President Woodrow Wilson vetoed identical legislation in 1917, arguing that the test measured opportunity rather than character or capability. The literacy gate was ultimately dismantled not by individual test-takers learning to parse the text, but by blunt federal preemption through the Voting Rights Act of 1965.

3.2 The Withheld Competence: Statutory Deprivation

When dominant institutions determined that withholding competence was necessary to preserve social stratification, they turned to statutory bans. Rather than testing a skill to bar entry, they criminalized the teaching and acquisition of the skill to forestall rebellion and enforce labor dependency.

Following the Stono Rebellion of 1739, South Carolina enacted its Negro Act of 1740, which imposed fines on anyone teaching enslaved persons to write. In the wake of Nat Turner’s revolt in 1831, Virginia enacted sweeping statutes criminalizing assemblies held to teach enslaved or free Black persons reading and writing. Identical measures followed in Alabama, Georgia, and North Carolina. The institutional rationale was articulated without euphemism. When Hugh Auld discovered his wife teaching the young Frederick Douglass the alphabet, he rebuked her:

"Learning would spoil the best nigger in the world. Now," said he, "if you teach that nigger (speaking of myself) how to read, there would be no keeping him. It would forever unfit him to be a slave. He would at once become unmanageable, and of no value to his master." (Douglass, 1845, p. 33)

Douglass’s autobiography documents the psychological consequence of acquiring a withheld competence inside a closed system. Literacy granted him an acute awareness of his subjugation without providing the immediate legal or political power to dismantle it:

"I would at times feel that learning to read had been a curse rather than a blessing. It had given me a view of my wretched condition, without the remedy. It opened my eyes to the horrible pit, but offered no ladder upon which to get out." (Douglass, 1845, ch. VII)

The practice extended far beyond the antebellum South. Spanish imperial authorities issued royal decrees between 1531 and 1543 strictly prohibiting the export or printing of vernacular romances and fictional books in the American colonies, fearing imaginative literature would destabilize indigenous subjugation and religious orthodoxy (Leonard, 1992). In the Russian Empire, the Valuev Circular of 1863 and the Ems Ukaz of 1876 prohibited the printing and importation of educational and religious texts in the Ukrainian language, explicitly asserting that "no separate Little Russian language ever existed, exists, or can exist" (Moser, 2017). In nineteenth-century India, upper-caste hierarchies enforced centuries-old bans on Dalit schooling, prompting the radical social reformer Jyotirao Phule (1882) to submit his blistering memorandum to the Hunter Commission, demonstrating that statutory and caste-based deprivation of literacy was the foundational mechanism of social domination.

Contemporaries contested this deprivation directly. In 1853, Margaret Douglass was arrested, indicted, and sentenced to one month in a Virginia jail for operating a Sunday school that taught free Black children to read. Her published defense, The Personal Narrative of Mrs. Margaret Douglass (1854), denounced the statute as an affront to Christian morality and natural right. The ethical wrong was unambiguous: an institutional monopoly on standing defended itself by legally extinguishing the cognitive tools required to demand it.

3.3 The Record Over the Voice: Testimonial Injustice and Biased Scribes

A third mode of domination emerged at the point of contractual and sovereign inscription. As legal systems prioritized written documentation over oral covenants, the party controlling the pen acquired unilateral power to rewrite the terms of agreement. That a written record automatically invalidates oral testimony is not an inherent property of human communication. It is a contingent legal hierarchy. Under classical Islamic shari'a rules of evidence, oral witness testimony (shahada) held primacy over uncorroborated written documents, precisely because written documents were recognized as susceptible to forgery and private manipulation (Messick, 1993). In the Western legal tradition, the triumph of the written record over the voice operated as a form of structural testimonial injustice (Fricker, 2007). The epistemic credibility of non-literate communities was systematically devalued, allowing the scribal class to exploit their counterparts' inability to verify the inscription.

The Treaty of Waitangi, signed in New Zealand in 1840, stands as an archetypal case of scribal distortion. The British Crown dispatched William Hobson to negotiate with Māori rangatira (chiefs). The missionary Henry Williams and his son translated the English text into Māori overnight. In the English draft, the chiefs ceded "all the rights and powers of Sovereignty" to Queen Victoria. In the Māori draft, Williams translated "sovereignty" as kawanatanga—a newly coined transliteration of "governorship," implying administrative oversight while preserving the chiefs' tino rangatiratanga (unqualified chieftainship and authority over their lands, settlements, and treasures). Over 500 chiefs signed the Māori version, understanding they were entering a protective alliance that preserved their self-determination. The colonial administration immediately enforced the English text, treating the signatures as a total surrender of territory and law (Waitangi Tribunal, 2014, pp. 355–358). Williams was not a detached linguistic translator; he was an interested institutional intermediary whose textual ambiguities served Crown expansion.

Centuries of judicial doctrine gradually recognized this structural injury. In R. v. Marshall (1999, paras. 14, 40), the Supreme Court of Canada confronted Crown attempts to enforce the strict text of a 1760 commercial treaty against Mi'kmaq fishermen. Justice Ian Binnie noted that the Mi'kmaq signatories were non-literate and lacked the practical capacity to create their own written record of the discussions. The Court held that European written instruments could not be interpreted in isolation from the oral promises that accompanied them. This ruling built upon Delgamuukw v. British Columbia (1997, para. 98), where Chief Justice Antonio Lamer held that Canadian common law had systematically erred by discounting Indigenous oral histories (adaawk and kungax), mandating that courts place oral and written evidence on equal evidentiary footing.

Where historical societies recognized the potential for scribal domination, they instituted formal procedural buffers. The Castilian Pragmática of 1503, promulgated by Queen Isabella, overhauled the legal notariat (escribanos). Recognizing that scribes routinely defrauded illiterate citizens, the law required notaries to undergo public examination, keep an unalterable bound register (protocolo), and read all legal instruments aloud in the simultaneous presence of the parties and independent witnesses before signing (Almeida Cabrejas, 2019, p. 24; Burns, 2010). At eighteenth-century diplomatic councils between the British Crown and the Haudenosaunee (Iroquois) Confederacy, indigenous leaders insisted on having second, independent interpreters present to cross-check imperial translations in real time (Hagedorn, 1988, p. 61). Under English common law, the doctrine of non est factum ("it is not my deed") emerged to protect illiterate individuals who signed deeds that had been falsely read or explained to them by unscrupulous counterparties (Foster v. Mackinnon, 1869). These procedural institutions acknowledged an uncomfortable reality: when one party holds the pen, unchecked inscriptions lead directly to exploitation.

3.4 The Monopoly: Chartered Enclosure of the Medium

The concentration of reproduction infrastructure provided early modern institutions with an apparatus for ideological and economic control. Following the invention of movable type, the English Crown moved to centralize the printing trade. In 1557, Queen Mary granted a royal charter of incorporation to the Worshipful Company of Stationers (Arber, 1875, vol. 1). The charter established a corporate monopoly: no individual in England could operate a printing press unless they were a freeman of the Stationers’ Company. In exchange for this commercial exclusivity, the Company functioned as the Crown’s private censorship arm. Its wardens were granted sweeping powers of entry, search, and seizure, authorizing them to enter any workshop without notice, seize unapproved books, and demolish unlicensed presses (Arber, 1875, pp. xxviii–xxxii).

           THE STATIONERS' COMPANY CORPORATE ENCLOSURE (1557–1662)

  ┌──────────────────────────────────────────────────────────────┐
  │                 Crown Sovereign Authority                    │
  │     (Star Chamber Decrees / Royal Charters / Licensing Acts)  │
  └──────────────────────────────┬───────────────────────────────┘
                                 │ Regulatory Monopoly &
                                 │ Search/Seizure Charters
                                 ▼
  ┌──────────────────────────────────────────────────────────────┐
  │              The Stationers' Company Cartel                  │
  │     (20 Master Printers, Centralized London Guildhall)       │
  └──────────────────────────────┬───────────────────────────────┘
                                 │ Unilateral Control of the Press;
                                 │ Exclusion of Provincial Print
                                 ▼
  ┌──────────────────────────────────────────────────────────────┐
  │                The Excluded Vernacular Public                │
  │  (Unlicensed Authors, Provincial Presses, Dissident Readers) │
  └──────────────────────────────────────────────────────────────┘


The enclosure intensified under the Star Chamber Decrees of 1586 and 1637, which confined all printing in England strictly to the City of London and the two university presses at Oxford and Cambridge. The Licensing Act of 1662 (14 Car. II c. 33) codified this cartel, capping the number of master printers authorized to operate across the entire realm at twenty. Provincial printing was banned; capital costs were maintained by regulatory fiat; and textual production was concentrated in a state-aligned guild.

Contemporary resistance was swift and articulate. In 1644, John Milton delivered his Areopagitica to Parliament, attacking pre-publication licensing as an aristocratic insult to the intelligence of the citizenry:

"Truth and understanding are not such wares as to be monopoliz'd and traded in by tickets and statutes and brocards." (Milton, 1644, p. 18)

Junior printers within the Stationers’ Company rebelled as well. In their 1643 petition to Parliament, non-elite pressmen denounced the monopolistic patents held by the Company's senior partners, arguing that enclosing the right to print legal, religious, and classical texts concentrated wealth among a dozen oligarchs while reducing journeymen printers to wage dependency. The Stationers' Company monopoly demonstrates how technological revolutions are captured: the dominant class erects capital, regulatory, and physical barriers around the new machinery, ensuring that the vernacular public can read only what has been cleared by the cartel.

3.5 The Oversold Promise: Responsibilizing the Learner

The fifth institutional abuse is the systematic overselling of literacy as an all-purpose cure for structural inequality. Throughout the nineteenth and twentieth centuries, state institutions, industrial philanthropists, and international development agencies marketed reading as a guaranteed pathway to economic mobility. Harvey J. Graff (1979) punctured this historical orthodoxy in The Literacy Myth. Analyzing census records and labor markets across nineteenth-century urban Canada and the United States, Graff demonstrated that acquiring literacy did not dismantle class, religious, or ethnic stratification. Illiterate workers from favored backgrounds routinely secured higher wages and better employment than literate workers from marginalized groups. Industrial employers championed basic literacy not to foster intellectual freedom, but to cultivate a disciplined, punctual, and obedient factory workforce (Graff, 1979, pp. 302–321).

In the late twentieth century, this rhetoric shifted to international development campaigns. The World Conference on Education for All at Jomtien (1990) and the World Education Forum at Dakar (2000) announced explicit mandates to eradicate adult illiteracy. The Dakar Framework committed the international community to a 50 percent improvement in adult literacy levels by 2015. The targets were roundly missed (UNESCO, 2015). Recent reports by the UNESCO Institute for Statistics (2026) show that 739 million adults remain non-literate worldwide, 63 percent of them women.

Promoting individual skill acquisition while leaving macroeconomic extraction intact represents an early form of what Giesler and Veresiu (2014) term responsibilization. Rather than addressing systemic underfunding, colonial resource extraction, or discriminatory hiring practices, institutional sponsors cast structural poverty as an individual educational deficit. If an illiterate laborer remained trapped in poverty, the failure was attributed to their personal refusal to self-improve, deflecting political scrutiny from the institutions managing the economy.

3.6 Boundary Case: Compulsory Enclosure and Linguistic Erasure

A severe historical manifestation of compulsory literacy occurred in the residential and boarding school systems of the United States, Canada, and Australia. Under the banner of cultural assimilation, indigenous children were removed from their families and placed in state- and church-administered institutions designed to extinguish their ancestral languages, traditions, and kinship networks (Truth and Reconciliation Commission of Canada, 2015; Newland, 2022, 2024; Human Rights and Equal Opportunity Commission, 1997).

These institutions committed horrific forms of physical, sexual, and psychological violence. To categorize this tragedy simply as a failure of literacy education would be a gross moral category error. The Canadian Truth and Reconciliation Commission (2015) and the United States Federal Indian Boarding School Initiative Investigative Report (Newland, 2022, 2024) document that the central crimes were physical abduction, forced labor, deliberate malnutrition, and systematic cultural destruction.

Yet analyzing these systems illuminates two institutional mechanisms that carry direct relevance for algorithmic governance:

⚬ Compulsory Participation: Populations were stripped of any legal or practical ability to refuse engagement with the dominant institutional medium.
⚬ Linguistic Erasure via Administrative Monoculture: The dominant institution criminalized the subjects' native languages, demanding total compliance with a single, foreign administrative code.

The lesson is stark: when an institutional medium becomes absolute and compulsory, the requirement to adapt to that medium becomes an instrument of cultural and epistemic erasure.

4. Analogical Mapping and Philosophical Objections: The Reoccupation of the Positions and Where the Analogy Breaks

4.1 The Present-Day Mapping Across the Five Positions

The five institutional practices of the literacy transition map with disturbing precision onto contemporary algorithmic governance, even as their underlying technical substrates differ.

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        ANALOGICAL MAPPING: SCRIBAL ERA VS. ALGORITHMIC ERA                             │
├────────────────────┬─────────────────────────────┬──────────────────────────────┬──────────────────────┤
│ Institutional Mode │ Scribal / Literacy Epoch    │ Algorithmic Triad Counterpart│ Critical Divergence /│
│                    │ Precedent                   │ (Algorithmacy)               │ Analogical Boundary  │
├────────────────────┼─────────────────────────────┼──────────────────────────────┼──────────────────────┤
│ 1. The Gate        │ Discretionary voter literacy│ Monopolized algorithmic      │ Gating tests evaluate│
│                    │ tests (*Katzenbach*, 1966)  │ screening systems            │ behavioral compliance│
│                    │ and racial exclusion gates  │ (Bommasani et al., 2026;     │ rather than explicit │
│                    │ (*Gaston County*, 1969).    │ Bhargava & Assadi, 2024).    │ textual literacy.    │
├────────────────────┼─────────────────────────────┼──────────────────────────────┼──────────────────────┤
│ 2. Withheld        │ Statutory bans on teaching  │ Information asymmetry: hidden│ Opacity maintained   │
│    Competence      │ reading and writing to      │ pay formulas, concealed      │ via trade secrecy and│
│                    │ enslaved laborers           │ trip destinations, and black-│ interface design, not│
│                    │ (Douglass, 1845).           │ box scoring (Rosenblat, 2016)│ criminal statutes.   │
├────────────────────┼─────────────────────────────┼──────────────────────────────┼──────────────────────┤
│ 3. The Record      │ Written treaty texts        │ Monopolized server logs,     │ Form contracts bind  │
│                    │ overwriting oral agreements │ unchallengeable automated    │ unread; terms are    │
│                    │ (*Waitangi*, 1840;          │ deactivations, and algorithmic│ rewritten on the fly │
│                    │ *Marshall*, 1999).          │ management decrees.          │ by real-time code.   │
├────────────────────┼─────────────────────────────┼──────────────────────────────┼──────────────────────┤
│ 4. The Monopoly    │ Chartered printer guilds and│ Concentrated hyperscale cloud│ Monopolies rest on   │
│                    │ Star Chamber licensing caps │ compute, proprietary weights,│ capital, energy, and │
│                    │ (Stationers' Company, 1557) │ and private training corpora │ data scale rather    │
│                    │[span_54](start_span)[span_54](end_span).                  │[span_55](start_span)[span_55](end_span).                   │ than royal charters. │
├────────────────────┼─────────────────────────────┼──────────────────────────────┼──────────────────────┤
│ 5. The Oversold    │ The Literacy Myth;          │ "AI Literacy" and prompt     │ Pedagogy operates in │
│    Promise         │ marketing reading as a      │ engineering marketed as a    │ good faith, but      │
│                    │ cure for poverty and class  │ shield against displacement  │ cannot overturn the  │
│                    │ barriers (Graff, 1979)      │ (Kamperman & Graff, 2026)    │ structural power of  │
│                    │[span_56](start_span)[span_56](end_span).                  │[span_57](start_span)[span_57](end_span)[span_58](start_span)[span_58](end_span).                │ the intermediary.    │
└────────────────────┴─────────────────────────────┴──────────────────────────────┴──────────────────────┘


The mapping exposes how power has migrated into the infrastructure of modern platforms. In employment screening, corporate HR departments outsource hiring to automated platforms that evaluate recorded video interviews, vocal patterns, and online assessments (Bhargava & Assadi, 2024). Because a few screening vendors dominate the market, their models form an algorithmic monoculture (Bommasani et al., 2026). An applicant rejected by a vendor’s proprietary model is automatically filtered out across dozens of independent employers, transforming a local application into a centralized, opaque gate.

Similarly, gig labor platforms enforce information asymmetries that echo the statutory withholding of competence. Ride-hail drivers must decide whether to accept a trip in a matter of seconds, without access to the customer's fare or final destination (Rosenblat & Stark, 2016, p. 3762). When gig workers attempt to contest an automated wage deduction or deactivation, they confront an automated ticketing loop that returns prefabricated text strings from an inaccessible ledger (Rosenblat & Stark, 2016, p. 3771). The platform controls the interaction logs, evaluates the performance data, and pronounces the judgment, leaving the worker with no mechanism to introduce countervailing evidence.

4.2 Where the Historical Analogy Holds: The Fallacy of Pure Comprehension

Advocates of algorithmic explainability operate on the assumption that if an algorithm explains its outputs, the user’s autonomy is restored (Kim & Routledge, 2022). The historical record of the literacy transition shatters this premise.

Comprehension does not equal control. Frederick Douglass understood the legal machinery of chattel slavery with brilliant intellectual clarity. He parsed the slave codes, read the speeches of Northern abolitionists, and debated the theology of slaveholders. That comprehension did not loosen his bonds; it intensified the agony of his confinement ("It opened my eyes to the horrible pit, but offered no ladder upon which to get out," Douglass, 1845, ch. VII).

Contemporary gig workers experience this exact dynamic. Sociological studies of platform labor demonstrate that experienced food delivery couriers and ride-hail drivers develop sophisticated mental models of the algorithms managing them (Rahman, 2021; Dubal, 2023; Cameron, 2024). Workers understand that their platforms use surge pricing algorithms to cluster them in specific neighborhoods, that refusal rates depress their future dispatch priority, and that customer ratings are systematically skewed. Yet that understanding grants them zero power to alter the platform's optimization parameters. Explaining the internal weights of an algorithmic model does nothing to cure domination if the user cannot challenge, alter, or refuse its outputs.

4.3 First Structural Divergence: Dynamic Plasticity of the Intermediary

While the historical analogy illuminates these power dynamics, it breaks down along two architectural fault lines. The first is what I call the dynamic plasticity of algorithmic systems.

When an ancient scribe inscribed a legal code onto stone or a sixteenth-century printer pressed a statute onto rag paper, the physical medium remained static. The letters of the English Licensing Act did not rearrange themselves based on who picked up the pamphlet. Once an excluded group learned to read, that skill could be turned against the ruling class. Literacy became a powerful tool for political organizing, underground publishing, and revolutionary resistance, precisely because the text was stable and predictable.

Algorithmic systems possess no such stability. Modern foundation models, predictive classifiers, and platform allocators adapt dynamically in response to user behavior. As legal theorist Karen Yeung (2016) argues, algorithmic "hypernudge" architectures operate through continuous feedback loops that reconfigure the choice architecture in real time based on the user’s behavioral profile. When gig workers develop collective tactics to game an algorithm—such as coordinating simultaneous app logoffs to trigger surge pricing—the platform engineers adjust the underlying dispatch code to neutralize the tactic (Cameron, 2024). The intermediary is plastic: the moment a human counterparty masters its operational rules, the system rewrites itself to maintain its extractive edge.

4.4 Second Structural Divergence: The Collapse of Independent Procedural Buffers

The second, more dangerous divergence is the complete absence of independent procedural safeguards around algorithmic intermediaries.

As shown in Section 3.3, early modern societies recognized that leaving written transactions to an interested scribe invited unchecked fraud and coercion. In response, they constructed elaborate legal rituals and independent institutional offices to protect non-literate parties:

⚬ The Public Notary: Civil law traditions established the sworn notary as an independent public officer, legally bound to remain neutral, read instruments aloud, explain their implications to both sides, and verify mutual understanding before any deed became binding (Almeida Cabrejas, 2019; Burns, 2010).
⚬ Diplomatic Counter-Interpreters: Treaty councils between colonial powers and Indigenous nations relied on independent second interpreters to audit translations in real time (Hagedorn, 1988).
⚬ Common-Law Judicial Relief: Common law courts developed equitable doctrines like non est factum to void contracts signed by non-literate parties who had been misled regarding the nature of the instrument (Foster v. Mackinnon, 1869).

                      COLLAPSE OF PROCEDURAL SAFEGUARDS

Historical Scribal Mediation (Multi-Layered Procedural Buffer):
┌──────────┐         ┌──────────────────────────────┐         ┌──────────┐
│ Party A  │◄───────►│  Independent Public Notary   │◄───────►│ Party B  │
│ (Weaker) │         │ (Reads, Explains, Neutrality)│         │(Stronger)│
└──────────┘         └──────────────┬───────────────┘         └──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Public Written Deed │
                         │ (Contestable via    │
                         │ *non est factum*)   │
                         └─────────────────────┘

Modern Algorithmic Mediation (Collapsed, Monopolized Closure):
┌──────────┐                                                  ┌──────────┐
│  User /  │◄───────────────────┐                             │ Platform │
│  Worker  │                    │                             │ Operator │
└────┬─────┘                    │                             └────┬─────┘
     │                          │                                  │
     │ Behavioral Data          │ Dynamic, Unaudited Decisions     │ Full Code
     │ (Clickwrap Assent)       │ (Self-Interested Optimization)   │ Control
     ▼                          │                                  ▼
┌───────────────────────────────┴────────────────────────────────────────┐
│             Algorithmic Intermediary (Proprietary Black Box)           │
│   • Collapses Counterparty and Arbitrator Roles                        │
│   • Internal Automated Audits Only ("Self-Reviewing Scribe")           │
│   • Zero External Procedural Buffers or Independent Explanations       │
└────────────────────────────────────────────────────────────────────────┘


Modern platform architecture strips away these protective buffers. The platform collapses two distinct legal roles into a single corporate entity: it is simultaneously the contracting counterparty and the automated adjudicator that interprets and enforces the contract.

When a user accepts a digital service agreement, they face a non-negotiable form contract that no human reads (Hill v. Gateway 2000, 1997). When an algorithmic model denies a worker their bonus or flags a user’s post as hate speech, the review process is routed back through the platform’s own automated infrastructure. Recent regulatory efforts to require a "human in the loop"—such as Article 22 of the EU General Data Protection Regulation (GDPR) and the EU Platform Work Directive—fall prey to the same flaw. The human reviewer is an employee or outsourced contractor working for the platform, paid to clear backlogs under brutal performance quotas, rather than an independent public officer sworn to protect the weaker party. Modern algorithmacy is historically unique: it places society’s most critical economic transactions into the hands of a self-interested scribe who is legally permitted to review their own work.

4.5 Limits of Historical Inference

Historical analogies offer indispensable critical illumination, but they must not be mistaken for predictive prophecies. To map the literacy transition onto algorithmic governance is not to claim that modern software engineers possess the explicit racial animus of the 1901 Alabama delegates or that digital workers face the horrific bodily coercion of chattel slavery. Qadri, Prabhakaran, and Denton (2026) rightly caution against historical fatalism, noting that computing technologies emerge from distinct economic contexts and political coalitions.

The historical record serves a more disciplined diagnostic purpose: it proves that whenever a communication medium is made a compulsory condition for civic and economic standing, the institutions controlling the medium reliably leverage it for domination. We study history not to predict how algorithms will evolve, but to recognize the structural positions of power currently being erected around them.

5. Normative Obligations for Algorithmic Intermediaries

Because the injuries of algorithmic mediation stem from structural positions of power rather than individual educational deficits, ethical remedies directed at the user fail. Business ethics must focus on the party that designs, controls, and profits from the intermediary.

Applying Walzer's internal critique to contemporary technology companies reveals an irreconcilable ethical contradiction. Industry leaders profess a commitment to non-maleficence, beneficence, and human flourishing in their public ethics guidelines (Jobin et al., 2019). Yet their production platforms maintain asymmetries that reproduce the very modes of domination they condemn. Under Young’s social-connection model of responsibility, platform operators bear an unavoidable, affirmative duty to redesign the architectures they control. I derive three architectural obligations for algorithmic intermediaries.

┌──────────────────────────────────────────────────────────────────────────────────┐
│             THREE ARCHITECTURAL DUTIES OF PLATFORM INTERMEDIARIES                │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ Normative Obligation     │ Design Mechanism & Operational Reality                │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 1. Structural Refusal    │ Guaranteeing alternative, human-mediated pathways     │
│                          │ without economic, civic, or social penalty[span_71](start_span)[span_71](end_span). │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 2. Declared Operating    │ Binding ex-ante architectural commitments on pay,     │
│    Envelopes             │ metric boundaries, and operational constraints.       │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 3. Infrastructural       │ Arming users with independent algorithmic agents and  │
│    Counter-Delegation    │ independent public auditors to balance the record.    │
└──────────────────────────┴───────────────────────────────────────────────────────┘


5.1 Shifting the Duty from Learner to Intermediary

The first ethical requirement is to discard the information-fiduciary model as an all-purpose solution for multi-sided platforms. Legal scholars have argued that platform companies should be treated as "information fiduciaries" who owe an undivided duty of loyalty to their users, akin to doctors or attorneys (Balkin, 2016).

This fiduciary model collapses when applied to triadic platform governance (Khan & Pozen, 2019). A doctor serves a single patient; an attorney represents a single client. An algorithmic platform, by its structural nature, mediates between conflicting human interests. A ride-hail platform cannot maintain an undivided duty of loyalty to a driver seeking higher fares while simultaneously maintaining an undivided duty of loyalty to a passenger seeking cheaper rides—all while satisfying investors demanding higher margins. Because platforms serve divided loyalties, appeals to fiduciary care become empty corporate rhetoric. Instead of pretending that platforms can act as benevolent fiduciaries, normative business ethics must treat them as powerful, self-interested institutions that must be restrained through mandatory design duties and procedural boundaries.

5.2 Countering the Gate: The Right to Structural Refusal

To counter the discretionary gate, platforms must guarantee users an affirmative right to structural refusal.

In classical economics, the consumer’s primary defense against an unpalatable transaction is the power of exit (Hirschman, 1970). In modern algorithmic ecosystems, exit is often an illusion. When an entire labor market, banking system, or housing sector adopts a shared screening infrastructure, opting out of algorithmic evaluation means opting out of economic life. A worker who refuses to subject their facial expressions to an AI-powered interview platform cannot simply walk to a rival employer; every major firm in the sector uses the same vendor (Bommasani et al., 2026; Bhargava & Assadi, 2024).

The right to structural refusal requires platform operators to maintain viable, non-algorithmic pathways for human coordination and participation, backed by a legal guarantee that choosing the non-algorithmic pathway will carry no penalty or loss of standing (Zong & Matias, 2024). If a job applicant chooses not to be evaluated by an automated video screening model, the employer must provide an interview conducted by a human evaluator without downgrading the candidate's application (cf. Bhargava & Assadi, 2024). If a borrower prefers manual underwriting, that pathway must remain open at comparable processing speeds. Refusal must be made structurally viable; an option that carries punitive costs is not an option at all.

5.3 Countering Withheld Competence: Declared Operating Envelopes

To dismantle the practice of withheld competence, platforms must operate within declared operating envelopes.

Decades of research in regulatory policy and behavioral economics confirm that mandatory disclosure statements—such as end-user license agreements and privacy notices—fail to protect consumers (Ben-Shahar & Schneider, 2011; Bakos et al., 2009). Handing a user an exhaustive description of an algorithm’s mathematical parameters does not cultivate autonomy. It triggers the transparency paradox: an unfiltered dump of dense statistical logic overwhelms human working memory, causing users to abandon critical evaluation and surrender their agency (Pasquale, 2015). Providing a user with an uncurated stream of model weights is the modern equivalent of handing an ancient reader a papyrus scroll written in continuous, unspaced scriptio continua. It is technically legible, but cognitively unworkable.

                     THE TRANSPARENCY PARADOX DYNAMICS
   
   [Raw Explainable AI / Model Telemetry]
                   │
                   ▼
   [Information Presentation Rate: I_t]
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
   [I_t < I* Regime]   [I_t > I* Regime: Metacognitive Overload]
    Productive Load          │
                             ▼
                 [Verification Tax: Manual QA of Machine Debris]
                             │
                             ▼
                 [Cognitive Surrender / Automation Bias]
                 (Rubber-stamping uninterpretable outputs)


The mathematical dynamics of this collapse are formalized by the Human Identity and Autonomy Gap (HIAG) framework, which models human autonomy A_t as a continuous stochastic process governed by information-induced cognitive load:

$$dA_t = \mu(I_t) A_t dt + \sigma_A A_t dW_t^A$$

Here, I_t \in [0, I_{\max}] represents the instantaneous rate of algorithmic information presentation (such as raw token streaming speeds or dense feature-attribution tables), \sigma_A > 0 defines autonomy volatility, and W_t^A is a standard Brownian motion capturing environmental noise. When the information rate exceeds the brain's cognitive processing threshold (I_t > I^*), the drift function \mu(I_t) turns negative. The user's cognitive reserves deplete, driving human agency toward an absorbing barrier where the subject either rubber-stamps algorithmic recommendations through uncritical automation bias or disengages entirely from epistemic oversight.

Rather than bombarding users with cognitive dumping disguised as "transparency," intermediaries must be held to ex ante architectural commitments. An operating envelope is a set of hard, mathematically guaranteed performance boundaries and economic rules within which the algorithm commits to operate. For a gig platform, an operating envelope establishes binding pay floors per minute and mile, guarantees minimum turnaround times for task acceptance, and explicitly bounds the maximum dispatch radius before a shift begins (Rosenblat & Stark, 2016). For a lending algorithm, an operating envelope sets hard limits on proxy variable weighting and prohibits the ingestion of non-financial behavioral telemetry. The intermediary is bound by design to remain within this operational perimeter, relieving the user of the impossible burden of auditing the code in real time.

5.4 Countering the Asymmetric Record: Infrastructural Counter-Delegation

To correct the asymmetry of the closed ledger, business ethics must endorse infrastructural counter-delegation.

Throughout history, non-literate parties preserved their interests not by becoming solitary master scribes, but by hiring independent scribes, invoking the assistance of sworn notaries, and securing second interpreters to represent them at the negotiating table (Hagedorn, 1988; Burns, 2010). Modern users require an equivalent procedural buffer: independent algorithmic software agents that represent their interests, record their interactions, and counter the platform's proprietary models (Viljoen, 2021; Delacroix & Lawrence, 2019).

          RESTORING PROCEDURAL EQUILIBRIUM VIA COUNTER-DELEGATION

┌──────────────────────────────────────┐     ┌──────────────────────────────────────┐
│       Platform Intermediary API      │     │      User Algorithmic Advocate       │
│  (Monopolized Logs, Model Envelopes) │◄───►│  (Independent Auditing, Provenance)  │
└──────────────────┬───────────────────┘     └──────────────────┬───────────────────┘
                   │                                            │
                   ▼                                            ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│              Independent Regulatory & Public Notarial Clearinghouse               │
│   (EU Art. 22 / C2PA Provenance / Irrevocable Transaction Ledger)[span_97](start_span)[span_97](end_span)        │
└───────────────────────────────────────────────────────────────────────────────────┘


Infrastructural counter-delegation empowers users with software tools that operate on their side of the interface. When a gig delivery worker logs onto a platform, their independent agent records all dispatch offers, captures trip metrics, computes actual operational costs, and stores an encrypted transaction log outside the platform's control. If a dispute arises over an automated deactivation or pay deduction, the arbitration is not adjudicated from the platform’s private database; it is decided against an independent, tamper-evident record maintained by the user’s counter-agent.

This mechanism requires overcoming two significant legal and organizational hurdles. Under agency law, an automated software agent is legally an instrument of its principal rather than an independent public officer (Kolt, 2025). Furthermore, platform operators aggressively combat user-side counter-tools, claiming that automated data scrapers and auditing extensions violate terms of service, breach anti-hacking laws (such as the Computer Fraud and Abuse Act), and infringe on trade secrets. Normative business ethics and statutory policy must carve out protected legal standing for independent auditing agents, ensuring that user counter-delegation is recognized as a legitimate exercise of countervailing power.

5.5 The Limits of Pure Design: Structural Monopoly and Regulatory Boundaries

Architectural redesign cannot resolve every dimension of algorithmic domination. When capital costs and computational requirements become extraordinarily high, domination stems from raw market concentration.

The development and deployment of frontier foundation models require hundreds of millions of dollars in capital, access to specialized chip clusters, and vast data center infrastructure. This material reality mirrors the early modern print cartels. The Stationers' Company dominated English printing because setting up an independent print shop and paper mill was prohibitively expensive. Modern artificial intelligence is concentrating into an oligopoly of hyperscale cloud providers for the same structural reasons.

Interface ergonomics and prompt engineering cannot dismantle a compute monopoly. Where the market structure itself produces unavoidable republican domination, design ethics must yield to structural antitrust enforcement, public utility regulation, and legal bans on automated exploitation (Berthon et al., 2019; Dubal, 2023; Mittelstadt, 2019).

6. Psychological Coherence, Existential Meaning, and Technomoral Architecture

6.1 The Epistemic Erosion of Meaning in Life

The domination exercised by opaque algorithmic intermediaries is not solely an economic or political injury; it also erodes human psychological well-being. Navigating systems whose internal rules remain hidden extracts a severe existential toll.

To diagnose this psychological strain, I turn to Frank Martela and Michael F. Steger’s (2016) tripartite framework of meaning in life, which distinguishes three fundamental dimensions: Coherence, Purpose, and Significance.

┌─────────────────────────────────────────────────────────────────────────────────────┐
│          MARTELA & STEGER'S (2016) THREE DIMENSIONS OF MEANING IN LIFE              │
├──────────────┬────────────────────────┬─────────────────────────────────────────────┤
│ Dimension    │ Core Definition        │ Impact of Opaque Algorithmic Mediation      │
├──────────────┼────────────────────────┼─────────────────────────────────────────────┤
│ 1. Coherence │ The cognitive sense    │ Shattered by black-box algorithms, opaque   │
│              │ that one's world and   │ wage calculations, and arbitrary automated  │
│              │ experiences make sense │ deactivations; forces users into unstable   │
│              │ and are predictable    │ "folk theories[span_111](start_span)[span_112](start_span)[span_113](start_span)"[span_111](end_span)[span_112](end_span)[span_113](end_span).            │
│              │[span_114](start_span)[span_114](end_span)[span_115](start_span)[span_115](end_span).          │                                             │
├──────────────┼────────────────────────┼─────────────────────────────────────────────┤
│ 2. Purpose   │ The motivational sense │ Undermined by gamified hypernudges that     │
│              │ of directedness, core  │ co-opt human goals in service of third-     │
│              │ life goals, and future │ party corporate optimization metrics        │
│              │ aims[span_116](start_span)[span_116](end_span)[span_117](start_span)[span_117](end_span).     │[span_118](start_span)[span_118](end_span)[span_119](start_span)[span_119](end_span).                               │
├──────────────┼────────────────────────┼─────────────────────────────────────────────┤
│ 3. Significance The evaluative sense  │ Eroded when human labor and creative        │
│              │ that one's life holds  │ expression are treated as interchangeable,  │
│              │ inherent value, worth, │ disposable training data for machine        │
│              │ and mattering          │ models[span_120](start_span)[span_120](end_span)[span_121](start_span)[span_121](end_span)[span_122](start_span)[span_122](end_span).                     │
│              │[span_123](start_span)[span_123](end_span)[span_124](start_span)[span_124](end_span).          │                                             │
└──────────────┴────────────────────────┴─────────────────────────────────────────────┘


When an algorithmic intermediary governs a person's working life through opaque logic, the cognitive dimension of Coherence breaks down first. A worker needs to understand how effort connects to compensation, why a task was assigned, and what actions provoked an administrative penalty. When these determinations are handed down by a closed system, the human environment stops making sense. Workers are forced to construct ad-hoc "folk theories"—mythologies about hidden keywords, device battery levels, or facial features—to restore a fragile illusion of comprehension (Rahman, 2021).

The motivational dimension of Purpose is subverted in parallel. Human beings derive purpose from formulating goals and pursuing them through autonomous action. When platform architectures integrate gamified dark patterns, personalized surge notifications, and behavioral nudges, they co-opt the user's motivational apparatus (Berthon et al., 2019). The worker’s daily activities are steered to satisfy the platform's dispatch logistics rather than their own considered life aims. Finally, Significance—the sense that one’s actions have value and matter to others—is extinguished when human labor and creativity are reduced to statistical training debris for synthetic foundation models. The individual is made to feel entirely fungible, an anonymous token within a centralized feedback loop.

6.2 Technological Mediation and the Politics of Artifacts

This psychological disorientation is not an accidental byproduct of bad software engineering. It is built into the material politics of the technology itself.

Political theorist Langdon Winner (1980) warned that technical artifacts are never politically neutral tools; their specific material architectures embody and enforce distinct social relations. Drawing on Lewis Mumford’s distinction between "authoritarian" and "democratic" technics, Winner argued that certain technologies are inherently political: they require specific social arrangements to function. Nuclear power plants, for instance, demand centralized security perimeters, hierarchical military command, and specialized technocracies to prevent catastrophic failure. They cannot be operated democratically.

                     THE INHERENT POLITICS OF DATA SCALING
   
   [Centralized Compute, Hyperscale GPU Clusters, Planetary Energy][span_148](start_span)[span_148](end_span)
                               │
                               ▼
   [Inherently Centralized Technics: Authoritarian Scale] (Winner, 1980)[span_149](start_span)[span_149](end_span)[span_150](start_span)[span_150](end_span)
                               │
                               ▼
   [Invisible Behavioral Scripts & Cyborg Relations] (Verbeek, 2005)[span_151](start_span)[span_151](end_span)
                               │
                               ▼
   [Erosion of Worker Autonomy, Coherence, and Purpose] (Martela & Steger, 2016)[span_152](start_span)[span_152](end_span)[span_153](start_span)[span_153](end_span)


Hyperscale deep learning models and centralized platform dispatch systems operate as authoritarian technologies (Winner, 1980). Because training frontier models demands massive energy resources, billions in capital, and planetary-scale data centers, the infrastructure cannot exist as a decentralized, locally governed tool. It concentrates ownership and authority at the corporate summit, treating the public as a passive consumer base that must adapt to its operational requirements.

Peter-Paul Verbeek’s (2005) postphenomenology illuminates how this authoritarian structure shapes human behavior through technological mediation. Technologies do not stand opposite human subjects; they actively co-shape human perception (how we see the world) and human praxis (how we act within it). Verbeek expands Madeleine Akrich’s concept of the "script"—the behavioral prescriptions embedded directly within an artifact that invite or inhibit specific actions.

In algorithmic platforms, these scripts operate silently in the background. Through background relations and hermeneutic relations, algorithms filter the world, modulate visibility, and steer decisions before the individual engages in conscious deliberation. When a platform uses automated scripts to allocate labor, optimize routes, or moderate speech, it scripts human life without the subject's consent. The individual is drawn into a cyborg relation or composite relation with an opaque intermediary, their choices co-constituted by an unseen corporate logic.

6.3 Shannon Vallor’s Technomoral Virtues

Voluntary corporate ethics codes cannot fix this structural imbalance. When professional organizations such as the IEEE and ACM publish ethical guidelines, they outline laudable aspirations: non-maleficence, justice, and human dignity. Yet as Shannon Vallor (2016) points out in Technology and the Virtues, emerging technologies evolve at a speed and global scale that render static compliance checklists obsolete.

Vallor argues that living well in an algorithmically mediated world requires cultivating specific technomoral virtues—dispositions of character that enable humans to navigate sociotechnical systems toward genuine flourishing. Three of Vallor’s virtues apply directly to the governance of algorithmacy:

⚬ Moral Attention: The capacity to discern and focus upon the ethically relevant dimensions of a technological situation, actively penetrating the smooth, frictionless abstractions of modern software interfaces. Scribes and notaries practiced moral attention when they read instruments aloud; modern system designers must practice it by resisting the temptation to hide labor exploitation behind clean user interfaces.
⚬ Technomoral Humility: The honest recognition of the limits of our technical knowledge and predictive capacities. Technomoral humility requires engineers and corporate executives to reject the hubristic assumption that complex social relations—justice, qualification, trustworthiness—can be fully captured by statistical models and optimization curves.
⚬ Technomoral Wisdom: The integrated capacity to direct technological practice toward genuine human flourishing, combining ethical reflection with concrete design choices. Technomoral wisdom demands that platform operators stop treating human counterparties as optimizeable endpoints, designing systems that actively support the coherence, purpose, and significance of their users’ lives.

7. Boundary Conditions, Pedagogical Interventions, and Conclusion

7.1 The AI Context Engine: Architectural Blueprint for Restoring Coherence

Translating these normative principles and technomoral virtues into concrete software practice requires moving beyond the failed paradigm of post-hoc explainability. We must replace raw, uncurated data dumps with systems that restore cognitive coherence and balance power.

I propose an architectural blueprint for an AI Context Engine: a four-layer computational substrate designed to expose hidden mediation scripts, restore Martela and Steger’s psychological coherence, and give users structural tools to assert their agency.

┌──────────────────────────────────────────────────────────────────────────────────┐
│                   THE FOUR LAYERS OF THE AI CONTEXT ENGINE                       │
├────────────────────────────┬─────────────────────────────────────────────────────┤
│ Architectural Layer        │ Technical Mechanism & Theoretical Function          │
├────────────────────────────┼─────────────────────────────────────────────────────┤
│ 1. Provenance Layer        │ Cryptographic attestation (e.g., C2PA standards)    │
│                            │ that verifies data origin, edits, and training      │
│                            │ lineage, fostering Vallor’s *Moral Attention*       │
│                            │[span_189](start_span)[span_189](end_span).                                          │
├────────────────────────────┼─────────────────────────────────────────────────────┤
│ 2. Interpretability Layer  │ Mechanistic interpretability (Sparse Autoencoders,  │
│                            │ circuit tracing) that maps internal representations,│
│                            │ restoring Martela & Steger’s *Coherence*            │
│                            │[span_190](start_span)[span_190](end_span)[span_191](start_span)[span_191](end_span).                                       │
├────────────────────────────┼─────────────────────────────────────────────────────┤
│ 3. Mediation Exposure Layer│ Real-time interface signaling of hidden proxy       │
│                            │ variables and behavioral scripts, exposing Verbeek’s│
│                            │ invisible technological mediation[span_192](start_span)[span_192](end_span).        │
├────────────────────────────┼─────────────────────────────────────────────────────┤
│ 4. Autonomy Layer          │ User-side parametric controls and manual overrides, │
│                            │ counteracting Winner’s authoritarian centralization │
│                            │[span_193](start_span)[span_193](end_span)[span_194](start_span)[span_194](end_span)[span_195](start_span)[span_195](end_span).                                    │
└────────────────────────────┴─────────────────────────────────────────────────────┘


The Provenance Layer anchors the system in verifiable data lineage. Just as early modern printers relied on colophons and paper watermarks to verify authenticity, modern digital systems must deploy cryptographic standards—such as the Coalition for Content Provenance and Authenticity (C2PA) framework—to track where data comes from, how it was modified, and who owns it. This structural transparency combats the rapid spread of synthetic disinformation, giving users the tools to interrogate the provenance of the information they encounter.

The Interpretability Layer uses mechanistic interpretability—specifically Sparse Autoencoders (SAEs) and automated circuit tracing—to decode the hidden features inside deep neural networks. Rather than returning vague post-hoc explanations, the engine extracts the specific representations activated during an inference pass. This demystifies the system's internal logic, providing the structural transparency required to restore cognitive coherence.

The Mediation Exposure Layer brings Peter-Paul Verbeek’s hidden scripts to the surface. When an algorithmic model penalizes a user for linguistic patterns—such as the documented systematic bias against African American Vernacular English (AAVE) in automated grading and moderation systems (Sap et al., 2019)—the interface highlights the proxy variable in real time, alerting the user to the active bias.

Finally, the Autonomy Layer gives users direct parametric controls to tune or override algorithmic constraints, breaking the monopoly of the platform operator and returning meaningful agency to the human subject.

7.2 From Passive Literacy to Critical Algorithmacy: Pedagogical Shift

Deploying new technical architectures will fail if our educational institutions continue to preach passive compliance. For decades, computer science education and digital literacy curricula have trained students to be obedient consumers of proprietary software—teaching them how to build resumes, query search engines, and prompt corporate chatbots.

Critical algorithmacy requires an entirely different pedagogy. Education must train students and citizens to interrogate, audit, and dismantle algorithmic systems. Students must learn to identify hidden proxy variables in administrative datasets, audit models for feedback loops, trace digital provenance across distributed networks, and deploy obfuscatory tactics when systems become coercive.

This pedagogical shift operationalizes Shannon Vallor’s call for technomoral wisdom. It moves the learner from passive consumer to critical auditor, equipping citizens to recognize and contest arbitrary power wherever automated systems gate access to life's opportunities.

┌─────────────────────────────────────────────────────────────────────────────────┐
│               PARADIGM SHIFT: DIGITAL LITERACY VS. CRITICAL ALGORITHMACY        │
├──────────────────────────────┬──────────────────────────────────────────────────┤
│ Traditional Digital Literacy │ Critical Algorithmacy                            │
├──────────────────────────────┼──────────────────────────────────────────────────┤
│ Focus on individual skill and│ Focus on structural power and triadic            │
│ software fluency[span_218](start_span)[span_218](end_span).  │ institutional mediation[span_219](start_span)[span_219](end_span)[span_220](start_span)[span_220](end_span)[span_221](start_span)[span_221](end_span).         │
├──────────────────────────────┼──────────────────────────────────────────────────┤
│ Accepts the interface as a   │ Interrogates the interface as an ideologically   │
│ neutral window to data.      │ scripted artifact (Winner, 1980; Verbeek, 2005)  │
│                              │[span_222](start_span)[span_222](end_span)[span_223](start_span)[span_223](end_span).                                    │
├──────────────────────────────┼──────────────────────────────────────────────────┤
│ Promotes prompt engineering  │ Demands declared operating envelopes, structural │
│ and personal adaptation      │ refusal, and counter-delegation[span_224](start_span)[span_224](end_span)[span_225](start_span)[span_225](end_span)[span_226](start_span)[span_226](end_span). │
│[span_227](start_span)[span_227](end_span)[span_228](start_span)[span_228](end_span).                │                                                  │
├──────────────────────────────┼──────────────────────────────────────────────────┤
│ Treats explainability as an  │ Recognizes post-hoc explanation as an            │
│ unalloyed cognitive good     │ uncompensated verification tax (HIAG)            │
│ (Kim & Routledge, 2022).     │[span_229](start_span)[span_229](end_span)[span_230](start_span)[span_230](end_span).                                    │
└──────────────────────────────┴──────────────────────────────────────────────────┘


7.3 Conclusion: Who Checks the Third Party?

The civilizational transition from oracy to literacy was not an uninterrupted march of democratic enlightenment. It was a fiercely contested institutional transformation during which the written word was repeatedly turned into a weapon of domination by whoever held the test, the access, and the record. Monopolies were established; whole populations were barred from learning; oral agreements were erased; and individual learners were blamed for structural poverty they had no power to escape.

Today, the algorithmic transition reproduces these exact institutional patterns within a triadic structure of unprecedented speed, opacity, and scale. When we tell workers, borrowers, and students that their survival depends on acquiring "AI literacy," we repeat the nineteenth-century myth of reading. We offer an educational remedy for an architectural injustice, asking individuals to adapt to a system designed to exploit their compliance.

Human autonomy will not be preserved by demanding that users cultivate heroic cognitive stamina before black-box systems. It requires redesigning the intermediary itself. Just as ancient and early modern societies eventually restrained human scribes by creating public notariats, mandating oral readings, and establishing equitable defenses like non est factum, we must now construct binding procedural and architectural boundaries around algorithmic intermediaries. By establishing the right to structural refusal, enforcing declared operating envelopes, and supporting infrastructural counter-delegation, business ethics can ensure that the third party in the triad serves human flourishing rather than arbitrary institutional power.

References

⚬ Alabama Constitutional Convention. (1901). Official Proceedings of the Constitutional Convention of the State of Alabama, May 21st, 1901, to September 3rd, 1901 (Vol. 1). Address of John B. Knox, pp. 7–10.
⚬ Almeida Cabrejas, B. (2019). The evolution of the Spanish notarial institution: From the Pragmática of Alcalá to the modern codification. Journal of Legal History and Notarial Studies, 44(1), 18–35.
⚬ Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). Machine bias: There’s software used across the country to predict future criminals. And it’s biased against blacks. ProPublica.
⚬ Arber, E. (1875). A transcript of the registers of the Company of Stationers of London, 1554–1640 A.D. (Vols. 1–2). Privately printed.
⚬ Aristotle. (2011). Nicomachean ethics (R. C. Bartlett & S. D. Collins, Trans.). University of Chicago Press.
⚬ Bakos, Y., Marotta-Wurgler, F., & Trossen, D. R. (2009). Does anyone read the fine print? Consumer attention to standard form contracts. Journal of Legal Studies, 43(1), 1–35.
⚬ Balkin, J. M. (2016). Information fiduciaries and the first amendment. UC Davis Law Review, 49(4), 1183–1234.
⚬ Ben-Shahar, O., & Schneider, C. E. (2011). The failure of mandated disclosure. University of Pennsylvania Law Review, 159(3), 647–749.
⚬ Berthon, P., Ferguson, S. T. L., Pitt, L. F., & Wang, E. (2023). The virtuous brand: The perils and promises of brand virtue signaling. Business Horizons, 66(1), 27–36.
⚬ Berthon, P., Pitt, L., & Campbell, C. (2019). Addictive de-vices: A public policy analysis of sources and solutions to digital addiction. Journal of Public Policy & Marketing, 38(4), 451–468.
⚬ Berthon, P., Yalcin, T., Pehlivan, E., & Rabinovich, T. (2024). Trajectories of AI technologies: Insights for managers. Business Horizons, 67(5), 461–470.
⚬ Bhargava, V. R., & Assadi, P. (2024). Hiring, algorithms, and choice: Why interviews still matter. Business Ethics Quarterly, 34(2), 201–230.
⚬ Bhargava, V. R., & Young, M. (2022). The ethics of employment-at-will. Business Ethics Quarterly, 32(4), 519–545.
⚬ Blevis, E. (2007). Sustainable interaction design: Invention & disposal, renewal & reuse. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 503–512).
⚬ Bommasani, R., Bana, S. H., Creel, K. A., Jurafsky, D., & Liang, P. (2026). Algorithmic monocultures in hiring. In Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (pp. 6351–6382). ACM.
⚬ Bourdieu, P. (1984). Distinction: A social critique of the judgement of taste. Harvard University Press.
⚬ Brandt, D. (1998). Sponsors of literacy. College Composition and Communication, 49(2), 165–185.
⚬ Burns, K. (2010). Into the archive: Writing and power in colonial Peru. Duke University Press.
⚬ Butterfield, H. (1931). The whig interpretation of history. G. Bell and Sons.
⚬ Cameron, L. D. (2024). Making sense of algorithmic management: The role of worker communities and collective resistance. Academy of Management Annals, 18(1), 89–124.
⚬ Citron, D. K. (2008). Technological due process. Washington University Law Review, 85(6), 1249–1313.
⚬ Clanchy, M. T. (1979). From memory to written record: England 1066–1307. Harvard University Press.
⚬ Delacroix, S., & Lawrence, N. D. (2019). Bottom-up data trusts: Disturbing the ‘one size fits all’ approach to data governance. International Data Privacy Law, 9(4), 236–252.
⚬ Delgamuukw v. British Columbia, [1997] 3 S.C.R. 1010 (Supreme Court of Canada).
⚬ Douglass, F. (1845). Narrative of the life of Frederick Douglass, an American slave. Written by himself. Anti-Slavery Office.
⚬ Douglass, M. (1854). The personal narrative of Mrs. Margaret Douglass, a southern woman, who was imparted thirty days in the common jail of Norfolk, under the laws of Virginia, for the crime of teaching free colored children to read. John P. Jewett & Co.
⚬ Dubal, V. B. (2023). On algorithmic wage discrimination. Columbia Law Review, 123(7), 1927–2000.
⚬ Edwards, L., & Veale, M. (2017). Slave to the algorithm? Why a "right to an explanation" is probably not the remedy you are looking for. Duke Law & Technology Review, 16(1), 18–84.
⚬ Engerman, S. L., & Sokoloff, K. L. (2001). The evolution of suffrage institutions in the New World. Journal of Economic History, 65(4), 891–921.
⚬ Floridi, L., & Cowls, J. (2019). A unified framework of five principles for AI in society. Harvard Data Science Review, 1(1).
⚬ Floridi, L., & Taddeo, M. (2016). What is data ethics? Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 374(2083), 20160360.
⚬ Foster v. Mackinnon, (1869) L.R. 4 C.P. 704.
⚬ Fricker, M. (2007). Epistemic injustice: Power and the ethics of knowing. Oxford University Press.
⚬ Gaston County v. United States, 395 U.S. 285 (1969).
⚬ Giesler, M., & Veresiu, E. (2014). Creating the responsible consumer: Moralistic governance regimes and consumer subjectivity. Journal of Consumer Research, 41(3), 840–857.
⚬ Graff, H. J. (1979). The literacy myth: Literacy and social structure in the nineteenth-century city. Academic Press.
⚬ Hagedorn, N. L. (1988). "A friend to go between them": The interpreter as cultural broker in eighteenth-century Anglo-Iroquois diplomacy. Ethnohistory, 35(1), 60–80.
⚬ Hill v. Gateway 2000, Inc., 105 F.3d 1147 (7th Cir. 1997).
⚬ Hirschman, A. O. (1970). Exit, voice, and loyalty: Responses to decline in firms, organizations, and states. Harvard University Press.
⚬ Hsieh, N. (2008). Employment discrimination, commodification, and agency. Business Ethics Quarterly, 18(4), 513–539.
⚬ Human Rights and Equal Opportunity Commission. (1997). Bringing them home: Report of the National Inquiry into the Separation of Aboriginal and Torres Strait Islander Children from Their Families. Commonwealth of Australia.
⚬ Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. Nature Machine Intelligence, 1(9), 389–399.
⚬ Johansson, E. (1985). Popular literacy in Scandinavia about 1600–1900. History of Education Quarterly, 25(1/2), 61–72.
⚬ Kamperman, S., & Graff, H. J. (2026). On "AI literacy": The rhetorical and historical fallacies of a movement and its marketing. Change: The Magazine of Higher Learning, 58(4), 34–39.
⚬ Khan, L. M., & Pozen, D. E. (2019). A skeptical view of information fiduciaries. Harvard Law Review, 133(2), 497–541.
⚬ Kim, T. W., & Routledge, B. R. (2022). Why a right to an explanation of algorithmic decision-making should exist: A trust-based approach. Business Ethics Quarterly, 32(1), 75–102.
⚬ Kolt, N. (2025). Algorithmic agency and the law of principals. Stanford Technology Law Review, 28(2), 145–202.
⚬ Kousser, J. M. (1974). The shaping of Southern politics: Suffrage restriction and the establishment of the one-party South, 1880–1910. Yale University Press.
⚬ Lake, M. (2006). The white man under siege: New histories of race in the Pacific and the British Empire. History Workshop Journal, 61(1), 146–162.
⚬ Leonard, I. A. (1992). Books of the brave: Being an account of books and of men in the Spanish conquest and settlement of the sixteenth-century New World. University of California Press.
⚬ Martela, F., & Steger, M. F. (2016). The three meanings of meaning in life: Distinguishing coherence, purpose, and significance. The Journal of Positive Psychology, 11(5), 531–545.
⚬ Messick, B. (1993). The calligraphic state: Textual domination and history in a Muslim society. University of California Press.
⚬ Milton, J. (1644). Areopagitica: A speech of Mr. John Milton for the liberty of unlicenc'd printing, to the Parlament of England. Privately printed.
⚬ Mittelstadt, B. (2019). Principles alone cannot guarantee ethical AI. Nature Machine Intelligence, 1(11), 501–507.
⚬ Monteiro, M. (2017). A designer's code of ethics. Dear Design Student.
⚬ Moody-Adams, M. M. (1994). Culture, responsibility, and affected ignorance. Ethics, 104(2), 291–309.
⚬ Moser, M. (2017). New contributions to the history of the Ukrainian language. Canadian Institute of Ukrainian Studies Press.
⚬ Muldoon, J., & Raekstad, P. (2023). Algorithmic domination in the gig economy. European Journal of Political Theory, 22(4), 587–607.
⚬ Newland, B. (2022). Federal Indian Boarding School Initiative investigative report. U.S. Department of the Interior.
⚬ Newland, B. (2024). Federal Indian Boarding School Initiative investigative report: Volume II. U.S. Department of the Interior.
⚬ Pasquale, F. (2015). The black box society: The secret algorithms that control money and information. Harvard University Press.
⚬ Pettit, P. (1997). Republicanism: A theory of freedom and government. Oxford University Press.
⚬ Phule, J. (1882). Memorial addressed to the Education Commission (Hunter Commission). Government Central Press.
⚬ Qadri, R., Prabhakaran, V., & Denton, E. (2026). Temporal pitfalls in sociotechnical AI critique: The perils of unexamined historical analogies. Big Data & Society, 13(1), 1–16.
⚬ R. v. Marshall, [1999] 3 S.C.R. 456 (Supreme Court of Canada).
⚬ Rahman, K. S. (2021). The invisible hand of the platform: Invisible labor, dynamic contracts, and the restructuring of work. Yale Law Journal, 130(4), 984–1062.
⚬ Rosenblat, A., & Stark, L. (2016). Algorithmic labor and information asymmetries: A case study of Uber's drivers. International Journal of Communication, 10, 3758–3784.
⚬ Sap, M., Card, D., Gabriel, S., Choi, Y., & Smith, N. A. (2019). The risk of racial bias in hate speech detection. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (pp. 1668–1678).
⚬ Scherer, A. G., Neesham, C., Schoeneborn, D., & Scholz, M. (2023). New challenges to the Enlightenment: How 21st-century sociotechnological systems facilitate organized immaturity and how to counteract it. Business & Society, 62(8), 1539–1572.
⚬ South Carolina v. Katzenbach, 383 U.S. 301 (1966).
⚬ Stark, D., & Vanden Broeck, P. (2024). Principles of algorithmic management. Organization Theory, 5(2), 1–24.
⚬ Street, B. V. (1984). Literacy in theory and practice. Cambridge University Press.
⚬ Street, B. V. (2003). What's "new" in New Literacy Studies? Critical approaches to literacy in theory and practice. Current Issues in Comparative Education, 5(2), 77–91.
⚬ Truth and Reconciliation Commission of Canada. (2015). Honouring the truth, reconciling for the future: Summary of the final report of the Truth and Reconciliation Commission of Canada. TRC.
⚬ UNESCO. (2015). Education for All 2000–2015: Achievements and challenges. EFA Global Monitoring Report, UNESCO Publishing.
⚬ UNESCO Institute for Statistics. (2026). Literacy rates among adults and youth: Global report on trends and data. UNESCO Publishing.
⚬ Vallor, S. (2016). Technology and the virtues: A philosophical guide to a future worth wanting. Oxford University Press.
⚬ Vee, A. (2013). Understanding computer programming as a literacy. Literacy in Composition Studies, 1(2), 42–64.
⚬ Verbeek, P.-P. (2005). What things do: Philosophical reflections on technology, agency, and design. Pennsylvania State University Press.
⚬ Viljoen, S. (2021). A relational theory of data. Yale Law Journal, 131(2), 573–654.
⚬ Walzer, M. (1988). The company of critics: Social criticism and political commitment in the twentieth century. Basic Books.
⚬ Washington, B. T. (1901). Up from slavery: An autobiography. Doubleday, Page & Co.
⚬ Williams, H. A. (2005). Self-taught: African American education in slavery and freedom. University of North Carolina Press.
⚬ Williams, J. (2018). Stand out of our light: Freedom and resistance in the attention economy. Cambridge University Press.
⚬ Winner, L. (1980). Do artifacts have politics? Daedalus, 109(1), 121–136.
⚬ Wolff, K. H. (Ed. & Trans.). (1950). The sociology of Georg Simmel. Free Press.
⚬ Yeung, K. (2016). ‘Hypernudge’: Big Data as a mode of regulation by design. Information, Communication & Society, 20(1), 118–136.
⚬ Young, I. M. (2006). Responsibility and global justice: A social connection model. Social Philosophy and Policy, 23(1), 102–130.
⚬ Zong, J., & Matias, J. N. (2024). Bartleby in the algorithmic age: The right to refusal in platform labor. ACM Transactions on Computer-Human Interaction, 31(2), 1–28.
