# Beyond the Literacy Trap: Toward a Critical Design Ethics for Algorithmacy

**Status:** working spine. Terminology reconciled 2026-09-19 (`DRAFT_AUDIT.md`,
`RESEARCH_PLAN_TERMINOLOGY.md`); "Prevailing Frameworks" restructured and a new "Protection Without
Promotion" section added 2026-09-19 (`RESEARCH_PLAN_FLOURISHING.md`, `RESEARCH_DOSSIER.md` §11).
Every claim below traces to a verified card in `literature/library/`.

### Abstract

Shannon Vallor's most recent book calls for "a new collective agreement on what technologies are for" and admits she cannot say where such an agreement would be built. This paper takes that admission as its starting point and asks a more technical question: structurally, where would the promotive work of design ethics — not just protecting people from a technology but helping them thrive through it — have to live for it to reach the people a technology actually affects? Reading five of the field's key accounts on their own terms — Langdon Winner's politics of artifacts, Vallor's technomoral virtue ethics, Peter-Paul Verbeek's postphenomenology, Value Sensitive Design, and Helen Nissenbaum's contextual integrity — shows that each is more sophisticated, and in several cases more promotive in its stated aims, than a caricatured harm-reduction critique would allow. Yet none assigns the promotive work it wants to the design of the relation between the two people a technology mediates: Winner assigns it to no one, Vallor to a cultivated subject and a future political settlement, Verbeek to a designer-user-artefact alliance built for one user, VSD to values borrowed from outside the method, and Nissenbaum to the historical ends of an institution. The paper traces this shared gap to a category error: algorithmacy — the competency of coordinating with other people through an interpreting, binding, algorithmic third party — is being treated as literacy extended to a new medium, when the two are as categorically distinct as literacy once was from the oracy it displaced. A moderator carries a message between two people; a mediator interprets both and commits determinations that bind both. Design ethics has built an extensive apparatus for teaching people to read the mediator. It has not yet built the apparatus for letting two people mediated by it negotiate, contest, and flourish through their coordination — and that, this paper argues, is exactly where Vallor's collective agreement would have to be built.

### Opening: A Question Vallor Cannot Answer

In her most recent book, Shannon Vallor — one of the field's own leading voices — reaches the edge of what design ethics currently has to offer and names the gap herself. After cataloguing the "low-hanging fruit" available to us — contestability, redress, clear accountability for AI-driven harms, funding of global AI risk observatories, and enforcing people's existing legal protections — she writes: "We also need to govern AI systems in more ambitious ways that don't just seek to mitigate their current harms, but that redirect their power to new and better ends. We need a new collective agreement on what technologies are for" (Vallor, 2024, p. 196).

That is the right question. It is also, on her own account, a question she can point toward but not answer with a design. The "collective agreement" she calls for has no address — no artifact, no interface, no relation it is built into. It waits on politics. This is not a failure specific to Vallor; it recurs, in different forms, across every serious account this paper examines. Design ethics knows how to protect people from a technology. It does not yet know how to build, into the technology itself, the thing that would let two people mediated by it actually thrive.

This paper takes Vallor's question seriously enough to make it more technical. Not: *should* design promote flourishing rather than merely avoid harm? The answer to that is not contested — Vallor, and every account examined below, already says yes. The harder, more specific question is: **where, structurally, would that promotive work have to live for it to reach the people it is meant to serve?** Answering that requires a vocabulary none of the five accounts we examine currently has: a way of naming, precisely, when a technology has stopped being a channel between two people and become a party to their coordination in its own right. Building that vocabulary — and using it to show that the promotive work these accounts already want has nowhere to live except in the relation between the two people a technology mediates — is this paper's task.

### The Architectural Question: Mediation, Power, and the Good Life

Every technical system embodies a silent proposition about how human beings ought to live, who holds authority, and what forms of life are deemed permissible. In mainstream engineering discourse, design ethics is routinely reduced to a negative mandate — *does this system avoid harm?* — and the reduction can be counted. Jobin, Ienca and Vayena (2019) reviewed 84 AI-ethics guidelines and found non-maleficence named in 60 of them against beneficence in 41; the documents, in their own words, "focus primarily on how to preserve privacy, dignity, autonomy and individual freedom in spite of advances in AI, while largely neglecting whether these principles could be promoted" (p. 15). A rigorous design ethics must confront that neglected half, and ask a more demanding question than harm-avoidance: **how do the material architectures of our technological systems actively mediate human behavior, shape political power, and ultimately either support or undermine our capacity to live a meaningful, self-directed life?**

When technological systems reach planetary scale, they cease to function as neutral instruments of convenience; they become the mandatory social terrain through which all human coordination occurs. The five accounts that follow are the field's own best attempts to answer the architectural question. Each earns a hearing on its own terms before this paper says where it runs out.

---

### The Prevailing Frameworks: Diagnostic Brilliance and Prescriptive Collapse

Contemporary philosophy of technology and applied ethics have developed sophisticated tools to analyze this terrain. Yet when confronted with modern deep learning and generative artificial intelligence, each canonical framework reaches a decisive theoretical limit.

#### Langdon Winner: Technological Politics Without Micro-Agency

* **The Steel-Man:** In "Do Artifacts Have Politics?", Langdon Winner dismantles the myth of technological neutrality. He distinguishes two ways an artifact can be political: the contested case, where a specific design choice settles an argument some group would rather have had (his own bridges example belongs here, and its facts are disputed — see Joerges 1999; Woolgar & Cooper 1999 — so this paper leans on it only as illustration, not proof), and the stronger, less-cited claim: certain technologies are *inherently political* because they require a particular distribution of authority simply to operate. Nuclear power is his clean case — a system demanding extreme capital concentration, centralized management, and strict physical security cannot be run any other way, "there is no other way" (Winner, 1980, p. 131). This second claim is the one this paper builds on.
* **The Prescriptive Limit:** Winner's own summary of his claim is blunt: "the initial choice about whether or not to adopt something is decisive in regard to its consequences" (1980, p. 134) — a yes-or-no lever, pulled once, at the point of adoption. Once an inherently political infrastructure is widely deployed and institutionalized, that lever is spent, and in the platform case it was never the enrolled person's to pull in the first place; Winner has no competence claim at all for the citizen already inside the system. His own later work names the mechanism by which enrollment costs a person something: *reverse adaptation*, "the adjustment of human ends to match the character of the available means" (Winner, 1977, p. 229). Winner already rejects cultivating the subject as an adequate remedy — a generation before virtue-ethics answers to this problem were proposed (Winner, 1977, pp. 304–305) — but he never says what an enrolled person should do instead.

#### Shannon Vallor: Technomoral Virtue as an Asymmetric Burden

* **The Steel-Man:** Shannon Vallor recognizes that modern data practices and emerging technologies operate at an unprecedented speed, scale, and pervasiveness that completely outpace traditional legislative handrails and regulatory frameworks. Because reactive laws cannot keep pace with algorithmic evolution, Vallor argues for proactive ethical design anchored in the rigorous cultivation of "technomoral virtues" — particularly *moral attention*, *prudence*, and *technomoral wisdom* — which depend on occasions for practice and repetition (Vallor, 2016). Vallor names the cost of losing those occasions directly: in a section titled "Communicative Friction," she calls "frictionless interactions" a "dubious ideal" (2016, pp. 161–164) and gives the case of an aunt whose calls go unanswered until she "will soon question why she's bothering ... and stop caring" — disenfranchisement by unreturned attention, not by force. Her aim throughout is not merely protective: "virtue just is the activity of living well" (2016, p. 19), the "flourishing that Aristotle called eudaimonia" (p. 160).
* **The Prescriptive Limit:** Yet when Vallor turns from what a good life requires to what design or policy should *do*, the demands she makes are protective ones: values-by-design and participatory design "will not take us all the way" (2015, p. 122), and the concrete programme she endorses is "contestability, and redress, clear accountability for AI-driven harms, funding of global AI risk observatories, and above all, the low-hanging fruit of enforcing people's existing legal protections and human rights" (2024, p. 196). She sees the gap herself and names it — the passage above continues, "we also need to govern AI systems in more ambitious ways... a new collective agreement on what technologies are for" — but locates the promotive work in the cultivated person and in a future political settlement, never in a design. A mediator that sets the tempo of interaction — a dispatch algorithm deciding in seconds, a generative model producing at reading speed — removes the *occasions* for practice that cultivation itself depends on, and no collective agreement yet built reaches that tempo.

#### Peter-Paul Verbeek: A Promotive Ethics for One

* **The Steel-Man:** Grounded in postphenomenology — the view that a person's experience of the world is never unmediated, but always already shaped by the artifacts through which it happens — Peter-Paul Verbeek's theory of technological mediation rejects the Cartesian separation between human subjects and technical objects, and rejects, explicitly, a "humanist" ethics whose job is merely to defend an autonomous subject against technology. Verbeek wants more than protection: "designers materialize morality" (Verbeek, 2009, p. 254), and the aim is not harm-avoidance but "the good life" itself, restored to a central place once philosophy stops treating technology as external to it (2009, p. 241). His remedy borrows constructive technology assessment from Dutch STS, augmented so that stakeholders anticipate *mediations* as well as impacts, in what he calls "a democratization of the designing process" (Verbeek, 2006, p. 23) — a genuinely promotive, participatory design ethics, not merely a protective one.
* **The Prescriptive Limit:** But look closely at who does the promoting, and for whom. Verbeek's own account names the agents: "the designer ... the user ... and the artefact itself" (2009, p. 256) — always one user, never two people bound by the same mediation. "Moral self-practices," his term for the promotive work, aim at "the technological mediation of *their* subjectivity" (2009, p. 260) — a single person's relation to a single artifact. Even his one case involving two people — expecting parents and an ultrasound — resolves to a single decision-maker facing one machine (2009, p. 253). Schot and Rip, whose method he augments, already named the weak point their own tradition never secured: feedback from stakeholders into a design remains "hoping that technology actors will respond" (1997, p. 255), and proprietary, continuously optimized AI removes that hope altogether — the user is neither in the room nor able to read the artifact under assessment. Verbeek's promotive design ethics is real. What it has never had occasion to ask is what happens when the artifact stands between *two* people it mediates at once, each moralized differently, neither able to negotiate with the other through it.

#### Value Sensitive Design: An Honest Floor, a Borrowed Ceiling

* **The Steel-Man:** Batya Friedman and colleagues' Value Sensitive Design is the field's own most-cited answer to "how do we build ethics into design," and its founding case already anticipates this paper's construct almost thirty years early. Friedman and Nissenbaum's 1996 analysis of the National Resident Matching Program describes an algorithm that interprets both residents' and hospitals' ranked preferences, commits a determination that binds both, and whose operator defended the arrangement as neutral "passive facilitation" — a defense the paper does not accept, since "biased systems offer no equivalent means for appeal" (Friedman & Nissenbaum, 1996, p. 331). VSD's later heuristic explicitly lists "Human Welfare — people's physical, material, and psychological well-being" as a value to design for (Friedman, Kahn & Borning, 2006, Table 1) — a promotive commitment on the page, not an afterthought.
* **The Prescriptive Limit:** VSD's own critics, writing inside the tradition, find no methodology behind the promotive half of that list. Manders-Huits (2011) finds VSD "offers no methodological account for distinguishing genuine moral values from mere preferences." Borning and Muller (2012), a VSD co-founder among them, concede the method commits only to "pluralism ... openness and transparency," with power "orthogonal" to its own stakeholder distinction. JafariNaimi and colleagues (2015) go further: on VSD's own definition, "self-interest is a value" too, so an operator's extraction interest enters with the same standing as a user's autonomy. The tradition's own most recent statement concedes the gap directly: Umbrello and van de Poel (2021) distinguish values a design must *respect* — a protective floor, "constraints or boundary conditions" that make a design "(minimally) acceptable" — from values a design should *promote*, and admit that for AI specifically, "an explicit orientation toward socially desirable ends... is still missing in current proposals," borrowed instead from the UN's Sustainable Development Goals. VSD names its own ceiling and confesses the ceiling was imported, not built by the method.

#### Helen Nissenbaum: Contextual Integrity Without a Counterpart

* **The Steel-Man:** Helen Nissenbaum's contextual integrity holds that an information flow is appropriate only when it conforms to the norms of the specific context it occurs in — who is sending and receiving, what type of information is moving, and under what principle it moves (2011, p. 33). On that standard, contextual integrity does not make the individual the remedy — "burdening individuals with the full weight of protecting their privacy online through notice-and-choice is unlikely to yield success" (Nissenbaum, 2011, p. 43) — nor let the mediator name the game: the Net "does not constitute ... a discrete context" (p. 38), and a platform calling itself "a shoe store, a church" thereby "invites evaluation against respective norms" (p. 44), so a dispatch algorithm answers to employment's norms, not its own. Her Walzer passage is this paper's own mechanism stated in different words: it is "a form of tyranny when goods of one sphere intrude into, or become dominant in, not only one sphere but many" (2004, p. 145), and her remedy is a "presumption in favor of the status quo" under which "we initially resist breaches" (2004, p. 145). A platform mediating employment, credit, housing, and speech at once possesses exactly that dominant good: information, "the raw materials of their industry" (2011, p. 44).
* **The Prescriptive Limit:** The benchmark is a benchmark for flows. Its three parameters — actors, attributes, transmission principles — name none of them a *determination*, a match or a rank, that binds a second person. The residency match she analyzed with Friedman in 1996 is two information flows and one binding determination; contextual integrity sees the flows and has nothing to say about the determination that follows. Determinations appear in her 2019 work only as "differential attention, be it decision, action, reward, or punishment" (p. 242) — a harm to the data subject, never a relation between two people one output binds. Her own decision heuristic — "locate contexts, explicate entrenched informational norms, identify disruptive flows, and evaluate" (2011, p. 38) — is run by "the evaluator" (2019, p. 232), never by the person inside the flow, and Nissenbaum concedes, in her own words, that technologies now "outpace the capacity to proceed according to the discrete steps of the CI heuristic" (2019, p. 248). Her promotive term is institutional, not personal: "the ends, purposes, and values of respective contexts" (2011, p. 40), which she acknowledges "sometimes may disfavor the data subject's interests" (2019, p. 233). Tellingly, the user-side instrument this account lacks, Nissenbaum built elsewhere, in a different book: obfuscation (Brunton & Nissenbaum, 2015) is one author's second answer to the same asymmetry her first theory cannot reach.

---

### Protection Without Promotion

Set the five accounts beside each other and a pattern holds that no single critique above fully names: each names a different beneficiary for its promotive ambitions, and none of them is a relation between two coordinated people.

| Account | Telos | Design instrument | Who delivers the promotive part |
| --- | --- | --- | --- |
| Winner | protective | protective | no one — the 1977 book uses "flourish" once, descriptively, and "the good life" not once |
| Vallor | promotive | protective (plus one promotive criterion) | the cultivated person, and a future "collective agreement" she names but does not design |
| Verbeek | promotive | promotive | the designer–user–artefact alliance, for one user at a time |
| VSD | protective founding | procedural core | an import — welfare is listed as a value, but the substantive account of what it requires is borrowed from outside the method |
| Nissenbaum | institutional | a benchmark for flows, not determinations | the historical ends of the context, never the person inside the flow |

**None of the five — whatever their stated aim — assigns the promotive work to the design of the relation between the two people a mediator binds.** That is not five separate complaints; it is the same finding this paper's own construct already makes checkable elsewhere (the census below), arrived at independently, from the inside, by reading what design ethics's own best accounts say about themselves.

Jobin, Ienca and Vayena's review of AI ethics guidance found the same asymmetry at the level of practice: guidelines "focus primarily on how to preserve privacy, dignity, autonomy and individual freedom in spite of advances in AI, while largely neglecting whether these principles could be promoted" (2019, p. 15). Mittelstadt (2019) supplies part of the reason: medicine's ethics rests on a "fiduciary duty" running from a professional to a named patient; AI development has no equivalent relation, since a developer's "principal fiduciary duties" run to shareholders, not to whoever the system mediates (pp. 2–3). Beneficence goes undefined in guideline after guideline not from oversight but because nothing in the field's structure obligates anyone to define it. Even the one school that puts beneficence first among its principles cashes it out downstream in adoption advocacy, not design: of AI4People's twenty recommendations, most operationalize non-maleficence, autonomy, and explicability — court scrutiny, the right to redress — and beneficence appears mainly as a case for building AI at all, not as an instruction about what a given interface should do (Floridi et al., 2018).

What would it mean to actually deliver the promotive half, rather than gesture at it? Martela and Steger's (2016) account of meaning in life supplies the vocabulary this paper needs, because it names what a design would have to produce, not just permit. Meaning resolves into coherence (comprehensibility, already established elsewhere in this paper as a matter of *predictability*, not mechanistic transparency), purpose (self-directed goals that organize action), and significance (the conviction that a life counts). An environment can be need-satisfying at one level while need-frustrating at another — Peters, Calvo and Ryan's own definition of an addictive design (2018, p. 4) — engaging at the interface while crowding out the autonomy, competence, and relatedness a person needs across a life, not just a session. Some interactive technologies are built to *afford the experience of meaning*; most are left, by default, to foreclose it (Mekler & Hornbæk, 2019, p. 2). Coherence, purpose, and significance are not properties an artifact can simply disclose, the way a model card discloses a training set. They are properties two coordinated people either can or cannot build together through what stands between them — which is exactly the site every account above declines to design for.

---

### The Historical Mirror: Print, Power, and the Social Construction of Authority

To understand why these contemporary frameworks fall short, we must examine the historical precedent of the Gutenberg revolution. Popular narratives, exemplified by Elizabeth Eisenstein's *The Printing Press as an Agent of Change* (1979), characterize the advent of movable type as an inherently democratizing event that naturally dispersed knowledge and fostered rational discourse.

Critical historians provide a necessary corrective, at a register this paper can actually defend. Adrian Johns demonstrates in *The Nature of the Book* that the authority and standardized "fixity" of print were not intrinsic technological properties of the press itself, but "as much a product of social actions as of the inherent properties of the press" (Johns, 2002, p. 121) — an achievement of institutions, trust conventions, and credit, not a gift of the machine. Harold Innis supplies the institutional register directly: media are held by classes and organizations, and print did not end monopoly control over knowledge so much as install a new one — a "monopoly of knowledge" realigned, not abolished, by the new medium (Innis, 1951). Michael Clanchy (2013) documents the more modest, better-evidenced claim this paper actually needs: in England between 1066 and 1307, trust migrated from persons to documents, a change in institutional competence, not in cognition. And the binding constraint print's advocates rarely name is supply, not desire — "the supply of readers," which depends on schooling, which lags the technology by generations (Havelock, 1963).

One qualification the paper must state plainly, not concede reluctantly: the strong "great divide" thesis — that literacy itself restructures cognition — is contested (Street, 1984; Finnegan, 1988; Scribner & Cole, 1981; Halverson, 1992) and this paper does not need it. The claim that survives the concession is institutional, not cognitive: societies came to *require* literacy for civic, legal, and economic standing; nothing here claims literacy *rewarded* the literate, which is the narrower, defensible half of a distinction Graff's *Literacy Myth* (1991) insists on and does not contest.

---

### The Category Error: Algorithmacy is Not Literacy

Today, society stands at the exact same historical precipice, yet tech theorists, policymakers, and designers are committing a profound ontological category error: they are treating algorithmacy as if it were merely an advanced extension of literacy.

When the printing press emerged, early modern thinkers initially attempted to govern and authenticate the new medium using the oral paradigms of spoken testimony, dialectical memory, and personal sworn oaths. That strategy failed because print operated on a completely different epistemic plane. Today, we are repeating this error in reverse. We treat generative AI and deep learning systems as complex "texts" to be decoded, analyzed, and critiqued using the traditional tools of literacy. Mainstream AI ethics promotes prompt engineering, mechanistic interpretability, model cards (Mitchell et al., 2019), data nutrition labels (Holland et al., 2018), and digital provenance standards (such as C2PA cryptographic attestations) on the assumption that if users are simply taught how to "read" the black box, human agency will be preserved. Each of these interventions, however, discloses to a downstream reader — never to a coordinated second party whose interests the same system is also determining.

This literacy-based paradigm collapses because of the fundamental nature of algorithmic mediation. **Algorithmacy** is formally defined as:

> The communication competency through which a human worker or citizen navigates, negotiates, and coordinates with other human parties through an algorithmic, automated third party.

Algorithmacy and literacy operate on diametrically opposed ontological foundations:

| Structural Dimension | The Literacy Paradigm (Static Symbolic Decoding) | The Algorithmacy Paradigm (Dynamic Agentic Mediation) |
| --- | --- | --- |
| **Nature of the Medium** | **Static and Passive:** Text is fixed once printed or displayed; it cannot observe, react to, or anticipate the reader. | **Dynamic and Probabilistic:** AI architectures are generative, non-linear, and adapt in real time to behavioral inputs. |
| **Interaction Dynamic** | **Unidirectional Hermeneutics:** The human decodes, interprets, and critiques an inert artifact. | **Adversarial Negotiation:** The human interacts with an active third party that models, predicts, and steers user behavior. |
| **Locus of Mediation** | **Direct Human-to-Human:** Text bridges human minds across time and space via a passive conduit. | **Automated Third-Party Gatekeeping:** Algorithms unilaterally rank, filter, summarize, approve, or deny human interactions. |
| **Comprehension vs. Power** | **Comprehension Yields Agency:** In Enlightenment literacy, decoding the text grants access to civic standing. | **Comprehension is Decoupled from Power:** Mechanistic understanding of an algorithm does not grant leverage over its deployment. |

Designing for algorithmacy cannot mean teaching users to "read" algorithmic systems more effectively. Giving an ordinary citizen an interpretability dashboard or a cryptographic provenance tag to combat proprietary, hyper-scale models is the contemporary equivalent of handing a peasant a dictionary to defend himself against a licensing regime.

---

### The Moral Hazards of Algorithmacy Today

Because design frameworks continue to treat algorithmic systems as communicative texts rather than authoritarian architectures, real, measured harms are accumulating in their place:

* **Infrastructural Enclosure.** Foundational generative AI infrastructure is monopolized by a narrow corporate oligopoly. The capital required for hyper-scale data centers, high-performance GPU clusters, and large proprietary datasets keeps foundational models under the exclusive control of a small number of firms. Proprietary black-box APIs grant conditional, monitored access while denying the public any control over internal weights, system prompts, or architectural logic.
* **Cognitive Deskilling and Epistemic Surrender.** Because generative interfaces remove the necessary cognitive friction from intellectual synthesis, users suffer from "automation bias" — the tendency to uncritically trust algorithmic outputs over contradictory evidence and professional intuition. As cognitive labor is offloaded onto predictive systems, human persistence, problem-solving capacity, and critical discernment atrophy.
* **Standardized Linguistic and Representational Erasure.** Large language models enforce a statistically averaged vernacular. Word embeddings trained on ordinary web text reproduce the same race and gender associations the Implicit Association Test finds in people (Caliskan, Bryson & Narayanan, 2017); toxicity classifiers trained on crowd-labeled corpora flag tweets written in African American English as offensive up to twice as often as otherwise-similar tweets, "suppressing already-marginalized voices" (Sap et al., 2019, p. 1668); and language models asked to judge a speaker from dialect alone assign speakers of African American English less prestigious jobs, convict them more often, and sentence them to death more often than speakers of Standardized American English — a covert prejudice that alignment training conceals rather than removes (Hofmann, Kalluri, Jurafsky & King, 2024). This last finding covers employment and criminal-justice decisions specifically; the parallel claim for educational grading, while plausible, does not yet have a citable study behind it and should not be asserted past what these three sources show.
* **Algorithmic Profiling and Inevitability Rhetoric.** Commercial face-classification systems misclassify darker-skinned women at error rates up to 34.7%, against at most 0.8% for lighter-skinned men — and the same vendors' technology sits inside law-enforcement face-recognition networks that already search Black faces disproportionately (Buolamwini & Gebru, 2018). A Stanford study that trained a classifier to infer sexual orientation from dating-site photographs closes not with a design remedy but with a forecast: "in the long term, the further erosion of privacy seems inevitable," so that the safety of gay people "will hinge on the tolerance of societies and governments" (Wang & Kosinski, 2018, pp. 255–256) — a warning the study's own authors pair with an appeal to "urgently work toward policies and technologies aimed at protecting privacy" (p. 255), not, as sometimes read, a justification for the technology itself. In both cases the affected party is handed a finding to read; no design ever proposes to give her standing over the classification made of her.
* **Mandatory Structural Complicity.** Engagement with algorithmic infrastructure is no longer voluntary. Automated screening systems filter job applications, algorithmic credit scoring gates financial security, predictive management software dictates labor schedules, and automated diagnostics steer healthcare. Pierre Berthon's own account of the attention economy names the mechanism directly: "our attention is not under our own control. Choices are made for us not necessarily in our interest but in the interest of social media companies and the advertisers they serve. In short, business models are designed to make us mindless" (Berthon & Pitt, 2019, p. 136) — and James Williams, writing in the same territory, refuses the subject-side remedy by name, calling employee mindfulness programs in tech "as dangerous as it is futile" (Williams, 2018, pp. 101–102). Citizens cannot exercise individual refusal or step back into mindfulness without facing severe economic marginalization — the condition Zuboff names when she observes that surveillance capitalism's architectures are built not to coerce outright but to "nudge, coax, tune, and herd behavior toward profitable outcomes" (Zuboff, 2019, p. 8). Expecting personal mindfulness and ethical discernment to neutralize architectures built to tune and herd behavior toward the firm's ends leaves the underlying corporate incentives untouched. *(Note: Berthon holds an appointment at the author's own institution; his work is cited here for the argument it makes, not on the strength of that affiliation.)*

---

### The Design Challenge Ahead

The prevailing design ethics tradition has failed this transition because it remains trapped in the assumptions of print literacy. It presumes a contemplative reader with the luxury of reflection, confronting an inert text within an egalitarian public sphere.

Modern algorithmic mediation, however, constitutes an active, asymmetric, and compulsory architecture of governance. We cannot resolve the crises of algorithmacy with literacy-based solutions: transparent dashboards, explainability labels, and individual virtue cultivation are structurally outmatched. If we are to design ethical infrastructure for algorithmacy, we must abandon the ambition of creating "better readers" of automated systems and instead build mechanisms of **counter-delegation** — a party's own agent acting inside the coordination, the micro-instrument of collectively won standing (Viljoen, 2021; Delacroix & Lawrence, 2019) rather than an individual, reactive tactic (the kind of one-user-against-one-algorithm "algorithmic resistance" that Velkova & Kaun (2021) show can succeed only by feeding the system what it already rewards) — **structural refusal** (Zong & Matias, 2024), and **bounded outputs**: predictable, declared operating envelopes in place of black-box legibility. This is where Vallor's own question finally gets an address. A collective agreement on what technologies are for does not have to remain a political abstraction waiting on legislatures; it can be built, one relation at a time, into the coordination itself.

---

### References

Berthon, P. R., & Pitt, L. F. (2019). Types of mindfulness in an age of digital distraction. *Business Horizons*, 62(2), 131–137.

Borning, A., & Muller, M. (2012). Next steps for value sensitive design. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI 2012)*, 1125–1134.

Brunton, F., & Nissenbaum, H. (2015). *Obfuscation: A User's Guide for Privacy and Protest*. MIT Press.

Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. *Proceedings of the 1st Conference on Fairness, Accountability and Transparency*, PMLR 81, 77–91.

Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. *Science*, 356(6334), 183–186.

Clanchy, M. T. (2013). *From Memory to Written Record: England 1066–1307* (3rd ed.). Wiley-Blackwell. (1st ed. Edward Arnold, 1979; 2nd ed. Blackwell, 1993.)

Delacroix, S., & Lawrence, N. D. (2019). Bottom-up data trusts: Disturbing the "one size fits all" approach to data governance. *International Data Privacy Law*, 9(4), 236–252.

Eisenstein, E. L. (1979). *The Printing Press as an Agent of Change: Communications and Cultural Transformations in Early-Modern Europe* (2 vols.). Cambridge University Press.

Finnegan, R. (1988). *Literacy and Orality: Studies in the Technology of Communication*. Blackwell.

Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Luetge, C., Madelin, R., Pagallo, U., Rossi, F., Schafer, B., Valcke, P., & Vayena, E. (2018). AI4People — An ethical framework for a good AI society: Opportunities, risks, principles, and recommendations. *Minds and Machines*, 28(4), 689–707.

Friedman, B., Kahn, P. H., Jr., & Borning, A. (2006). Value sensitive design and information systems. In P. Zhang & D. Galletta (Eds.), *Human-Computer Interaction and Management Information Systems: Foundations* (pp. 348–372). M.E. Sharpe.

Friedman, B., & Nissenbaum, H. (1996). Bias in computer systems. *ACM Transactions on Information Systems*, 14(3), 330–347.

Graff, H. J. (1991). *The Literacy Myth: Cultural Integration and Social Structure in the Nineteenth Century*. Transaction. (Original: *The Literacy Myth: Literacy and Social Structure in the Nineteenth-Century City*, Academic Press, 1979.)

Halverson, J. (1992). Goody and the implosion of the literacy thesis. *Man* (N.S.), 27(2), 301–317.

Havelock, E. A. (1963). *Preface to Plato*. Belknap Press of Harvard University Press.

Hofmann, V., Kalluri, P. R., Jurafsky, D., & King, S. (2024). AI generates covertly racist decisions about people based on their dialect. *Nature*, 633(8028), 147–154.

Holland, S., Hosny, A., Newman, J., Joseph, J., & Chmielinski, K. (2018). The Dataset Nutrition Label: A framework to drive higher data quality standards. *arXiv:1805.03677*.

Innis, H. A. (1951). *The Bias of Communication*. University of Toronto Press.

JafariNaimi, N., Nathan, L., & Hargraves, I. (2015). Values as hypotheses: Design, inquiry, and the service of values. *Design Issues*, 31(4), 91–104.

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, 1(9), 389–399.

Joerges, B. (1999). Do politics have artefacts? *Social Studies of Science*, 29(3), 411–431.

Johns, A. (2002). How to acknowledge a revolution. *American Historical Review*, 107(1), 106–125.

Manders-Huits, N. (2011). What values in design? The challenge of incorporating moral values into design. *Science and Engineering Ethics*, 17(2), 271–287.

Martela, F., & Steger, M. F. (2016). The three meanings of meaning in life: Distinguishing coherence, purpose, and significance. *The Journal of Positive Psychology*, 11(5), 531–545.

Mekler, E. D., & Hornbæk, K. (2019). A framework for the experience of meaning in human-computer interaction. *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI '19)*, Paper 225, 1–15.

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\* '19)*, 220–229.

Mittelstadt, B. (2019). Principles alone cannot guarantee ethical AI. *Nature Machine Intelligence*, 1(11), 501–507.

Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review*, 79(1), 119–157.

Nissenbaum, H. (2011). A contextual approach to privacy online. *Daedalus*, 140(4), 32–48.

Nissenbaum, H. (2019). Contextual integrity up and down the data food chain. *Theoretical Inquiries in Law*, 20(1), 221–256.

Peters, D., Calvo, R. A., & Ryan, R. M. (2018). Designing for motivation, engagement and wellbeing in digital experience. *Frontiers in Psychology*, 9, Article 797.

Sap, M., Card, D., Gabriel, S., Choi, Y., & Smith, N. A. (2019). The risk of racial bias in hate speech detection. *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 1668–1678.

Schot, J., & Rip, A. (1997). The past and future of constructive technology assessment. *Technological Forecasting and Social Change*, 54(2–3), 251–268.

Scribner, S., & Cole, M. (1981). *The Psychology of Literacy*. Harvard University Press.

Street, B. V. (1984). *Literacy in Theory and Practice*. Cambridge University Press.

Umbrello, S., & van de Poel, I. (2021). Mapping value sensitive design onto AI for social good principles. *AI and Ethics*, 1(3), 283–296.

Vallor, S. (2015). Moral deskilling and upskilling in a new machine age: Reflections on the ambiguous future of character. *Philosophy & Technology*, 28(1), 107–124.

Vallor, S. (2016). *Technology and the Virtues: A Philosophical Guide to a Future Worth Wanting*. Oxford University Press.

Vallor, S. (2024). *The AI Mirror: How to Reclaim Our Humanity in an Age of Machine Thinking*. Oxford University Press.

Velkova, J., & Kaun, A. (2021). Algorithmic resistance: Media practices and the politics of repair. *Information, Communication & Society*, 24(4), 523–540.

Verbeek, P.-P. (2006). Materializing morality: Design ethics and technological mediation. *Science, Technology, & Human Values*, 31(3), 361–380.

Verbeek, P.-P. (2009). Cultivating humanity: Towards a non-humanist ethics of technology. In J. K. B. Olsen, E. Selinger, & S. Riis (Eds.), *New Waves in Philosophy of Technology* (pp. 241–263). Palgrave Macmillan.

Viljoen, S. (2021). A relational theory of data governance. *Yale Law Journal*, 131(2), 573–654.

Wang, Y., & Kosinski, M. (2018). Deep neural networks are more accurate than humans at detecting sexual orientation from facial images. *Journal of Personality and Social Psychology*, 114(2), 246–257.

Williams, J. (2018). *Stand Out of Our Light: Freedom and Resistance in the Attention Economy*. Cambridge University Press.

Winner, L. (1977). *Autonomous Technology: Technics-out-of-Control as a Theme in Political Thought*. MIT Press.

Winner, L. (1980). Do artifacts have politics? *Daedalus*, 109(1), 121–136.

Woolgar, S., & Cooper, G. (1999). Do artefacts have ambivalence? Moses' bridges, Winner's bridges and other urban legends in S&TS. *Social Studies of Science*, 29(3), 433–449.

Zong, J., & Matias, J. N. (2024). Data refusal from below: A framework for understanding, evaluating, and envisioning refusal as design. *ACM Journal on Responsible Computing*, 1(1), Article 10, 1–23.

Zuboff, S. (2019). *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power*. PublicAffairs.
