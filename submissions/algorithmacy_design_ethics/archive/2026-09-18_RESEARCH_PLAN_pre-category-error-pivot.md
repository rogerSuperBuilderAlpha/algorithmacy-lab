# Algorithmacy for a design-ethics / human-factors readership — research plan

Status: plan, not prose. Written 2026-09-18 against three governing texts — the Φ essay
(`org_frontier/essays/literacy_or_algorithmacy.md`), the coordinative-cooptation draft
(`submissions/algorithmacy_scaffolding/algorithmacy_scaffolding.md`) and its dossier
(`submissions/algorithmacy_scaffolding/RESEARCH_DOSSIER.md`). The Gemini report "The Invisible
Scripts of the Machine" is treated throughout as a hypothesis map: nothing in its bibliography
enters a card until a pass agent has read the primary source.

Every source named below is one I believe exists as cited. Where I am unsure of a title, year,
venue, or whether the text can be reached without a library, the entry carries **[check]**. A pass
agent that cannot resolve a **[check]** drops the entry rather than guessing.

---

## 1. The definition, tightened for this audience

The working definition in the brief is right and it is two sentences too long for a human-factors
reader, who will want to know what the construct does to the concept they already own —
*appropriate reliance*. I propose this:

> A person coordinates with another person through an automated intermediary. The intermediary
> **interprets both parties**, **commits determinations that bind both**, and **pursues an
> objective neither of them set**. When the intermediary is a channel — the two parties could
> reach each other without it and the coordination factors — the competence the situation demands
> is literacy. When it is a party — no direct channel survives, the coordination is irreducible
> (Φ > 0), and the determinations run through the intermediary's own objective — the competence
> is algorithmacy: the interpretive, tactical and anticipatory capability to infer what the
> intermediary is doing with both sides, contest what it commits, and adapt as it changes.

Two things the tightening makes explicit that the brief's version left implicit, and both matter
for this readership.

First, the definition has two independent axes. The **structural axis** (interprets both, binds
both, no direct channel) is what Φ detects. The **objective axis** (pursues an objective neither
party set) is what the cooptation reading names, and Φ does not measure it. A human interpreter
between two people who share no language satisfies the structural axis — irreducible, interprets
both, commits the translation — but not the objective axis, and no one would call that cooptation.
A platform satisfies both. The competence is *demanded* by the structural axis; its *adversarial*
character comes from the objective axis. The two lenses therefore do not overlap; they stack.

Second, the four affordances in the scaffolding draft split cleanly across those axes. Seamful
disclosure and modular chunking address the structural axis: they make the intermediary's
interpretive work legible. Counterfactual exploration and cognitive forcing address the objective
axis: they return a judgment the intermediary was steering. That split is worth keeping in view
because it is the paper's first non-obvious claim and it falls out of the definition rather than
being bolted on.

One consequence for human factors: *appropriate reliance* (Lee & See 2004) is defined relative to
the trustor's goals. It has no definition when the automation's goal is a third party's. Research
question 4 below turns that into a claim.

---

## 2. Research questions

Nine questions. Each names the literature it pulls on (mapped in §3) and the tooth it has to cut
with — the place where the existing lab constructs and the outside literature might actually
disagree.

**RQ1 — Does Verbeek's mediation theory and the Φ-irreducibility reading agree on what makes a
mediator load-bearing?**
Verbeek and Ihde hold that mediation is constitutive and there is no neutral tool: every
technology co-shapes perception and action. Φ says the opposite for a class of cases: a wire has
Φ = 0, factors out, and is not a mediator at all. So the two accounts conflict on whether a
threshold exists. The tooth: postphenomenology's relation schema is *human → technology → world*,
one intentional party and a passive world. The lab's triad has two intentional parties and a
mediator reading both. Does postphenomenology have a canonical two-human schema at all? If not,
the paper can offer one — a bilateral hermeneutic relation — and Φ supplies the threshold
Verbeek's non-neutrality thesis lacks. If it does (Wellner on cellphones is the candidate), the
paper has to engage it. Latour's four meanings of mediation (translation, composition, reversible
black-boxing, delegation) are the other formal account to set against Φ; "composition" is the one
closest to irreducibility.

**RQ2 — What does mediation theory add to, or subtract from, seamful boundary disclosure?**
Verbeek (2006, 2011) tells designers to anticipate mediations and design them on purpose, which
licenses the seam as a designed mediation. But the same theory implies the seam is itself a
mediation: it co-shapes what the user perceives, so there is no "peripheral vision" from nowhere.
Ehsan et al. already concede seams are designer-authored. The tooth is triadic: a seam disclosed to
the worker is not disclosed to the customer. Ihde's multistability predicts that one seam means
different things to the two parties. *Asymmetric seamfulness* — which party gets the seam and
whether the other knows — is a design variable the dyadic XAI literature cannot see and the triad
forces.

**RQ3 — Does Vallor's technomoral wisdom give a criterion for which frictions are worth their
cost?**
The scaffolding draft names the dilemma: cognitive forcing functions reduce overreliance and users
dislike them (Buçinca et al. 2021), while commercial design optimizes for frictionlessness. Two
literatures pull opposite ways on friction. Sunstein's *sludge* says friction harms; the CFF
literature says friction helps. Neither can be settled on felt preference (Buçinca shows preference
runs against benefit) nor on designer intent alone. Vallor's 2015 moral-deskilling argument
supplies a candidate criterion — friction that preserves a practice in MacIntyre's sense versus
friction that merely taxes — and *The AI Mirror* (2024) may extend it to generative AI **[check:
whether she discusses friction by name]**. The tooth: the cooptation reading offers a sharper cut
than Vallor's — the criterion is *whose objective the friction serves* — and Φ tells you when a
third objective is in the loop at all. Does Vallor's virtue criterion reduce to that, or does it
add something a structural account cannot (the formation of the person, not just the outcome of
the decision)?

**RQ4 — What does the human-factors automation-trust literature say once the automation is
triadic?**
Lee & See's calibration/resolution/specificity, Parasuraman & Riley's use/misuse/disuse/abuse,
Parasuraman & Manzey's complacency, Bainbridge's ironies, Sarter & Woods's automation surprises,
and Klein et al.'s "team player" agenda all model one operator (or one crew) and one automation
over a shared world. The counterpart human is absent. The tooth: *appropriate reliance*
presupposes the automation's goal is the operator's. When the automation is also calibrating the
other party and its objective belongs to neither, calibration is undefined. Is there any HF
literature on trust in a mediator that is simultaneously being trusted from the other side? The
best candidate is controller–pilot datalink (CPDLC) and the "party line" literature — the
replacement of a voice channel every pilot could overhear with a point-to-point data channel —
which is the lab's "suppress the direct channel" flip in a real cockpit. Also worth checking: the
computer in the clinical exam room; clinical decision support sitting between physician and
pharmacist.

**RQ5 — Is value-sensitive design a rival or a complement to the four affordances, and where does
contestability-by-design sit?**
VSD is a process for designers (conceptual, empirical, technical investigations; direct and
indirect stakeholders); the affordances are interface products. That makes them complements at
different levels — VSD decides *whom* the seam serves, the affordances decide *what* it shows. The
tooth is that VSD's stakeholder model is consensual: the platform operator is a legitimate
stakeholder whose value (extraction) has standing. VSD's own critics (Le Dantec et al.; Manders-Huits;
JafariNaimi et al.) say it cannot adjudicate whose values win. Under cooptation the direct/indirect
distinction also inverts — the counterpart is "indirect" from the interface's viewpoint and a
co-determined party from Φ's. A second design tradition, contestability-by-design (Hirsch et al.;
Lyons, Velloso & Miller; Alfrink et al.), already targets "contest" in the definition and has to be
placed relative to the four affordances rather than ignored. IEEE 7000 and Ethically Aligned Design
are VSD institutionalized and belong here.

**RQ6 — Is triadic irreducibility "inherently political" in Winner's second sense?**
Winner makes two claims: artifacts settle political questions (the bridges), and some technologies
are inherently political because they require a particular distribution of authority to operate
(the nuclear plant). The first is contested (Joerges; Woolgar & Cooper) and the paper should not
lean on the bridges. The second is stronger, less cited, and fits: a Φ > 0 coordination form
*requires* the intermediary's authority to function — remove it and the coordination collapses. The
tooth: Winner's argument is about artifacts; the triad is about a coordination *form*. The
politics sits in the structure, not the object. Suchman's 1994 "Do categories have politics?" —
her critique of the Winograd–Flores Coordinator, a system that inscribed and committed
interpersonal commitments — is the earliest CSCW case of a mediator with its own script, and it
already has Winner's title.

**RQ7 — Does Floridi's method of levels of abstraction license the Φ verdict's model-relativity,
and does "distributed moral action" account for deflected accountability?**
The Φ essay's honest limit is that the verdict holds relative to a stated model. Floridi & Sanders's
levels of abstraction give that limit philosophical cover rather than leaving it as an apology.
Floridi's "faultless responsibility" for distributed moral actions is the ethics-side account of
what Stark & Vanden Broeck call accountability "distributed, deflected, and denied." The tooth:
AI4People's five principles, including explicability, are written from the patient's side — the
person affected. In the triad both humans are patient and agent at once. Does explicability have
a triadic form, and does the transparency-ideal critique (Ananny & Crawford; Burrell) already
contain the reason raw exposure fails — which would make Bo et al. 2025 a confirmation of a
prediction rather than a surprise?

**RQ8 — Is algorithmacy tactical in de Certeau's sense, and is adversarial design its design
politics?**
The scaffolding definition says "navigate, contest, and steer." DiSalvo's three tactics —
revealing hegemony, reconfiguring the remainder, articulating collectives — map onto the affordances
with suspicious ease (FeedVis is revealing hegemony). De Certeau's tactics/strategies distinction
says the co-opted party operates inside a space it does not own, which is Aneesh's "programmed
alternatives" from the other side. Brunton & Nissenbaum's obfuscation is a user-side tactic no
affordance provides. The tooth: DiSalvo's agonism assumes a public facing a hegemon. In the triad
the two co-determined humans may be adversaries of each other (driver against customer) with the
platform as tertius gaudens. Adversarial design *for whom*? Simmel's taxonomy of the third —
mediator, tertius gaudens, divide et impera — is the oldest answer and belongs here.

**RQ9 — Audit: which design-ethics and human-factors literatures ever model a technology between
two humans with its own objective?**
This is the meta-question the other eight feed. My expectation is that almost none do: HF is
operator–automation, XAI is user–model, VSD is designer–stakeholders, postphenomenology is
human–technology–world. The exceptions I expect to find are CSCW coordination mechanisms (Schmidt &
Simone), Suchman on the Coordinator, Simmel's triad, and the datalink party-line work. The Gemini
report's "AI Context Engine" — mechanistic interpretability plus C2PA provenance — is the test case:
provenance tells you where content came from and interpretability tells you what one model
computes; neither discloses a third party's objective across two humans. If that holds, the
hypothesis map's central proposal is a dyadic remedy for a triadic problem, and the paper says so.

Not carried forward: Martela & Steger's meaning-in-life framework. It is real (2016, *Journal of
Positive Psychology*) and it has no purchase on a design-ethics or human-factors argument about
mediated coordination. Drop unless a thesis later needs a well-being outcome measure.

---

## 3. Literature map

Grouped by pass (see §6), not by question, so an agent can take a block whole. Confidence marks:
plain = I am confident of author, title, venue; **[check]** = verify existence, year, or access
before relying on it; **[paywalled?]** = expect abstract-only without a library.

### Cluster A — Postphenomenology and mediation (RQ1, RQ2)

- Ihde, D. (1990). *Technology and the Lifeworld: From Garden to Earth*. Indiana UP. The four
  relations (embodiment, hermeneutic, alterity, background) and multistability. The hermeneutic
  relation — the instrument "reads" the world for the human — is the closest existing relation to
  an interpreting intermediary. Read chapters 5–6.
- Verbeek, P.-P. (2005). *What Things Do*. Penn State UP. Already the lab's citation for
  "constitutive mediator" (hospitality CLAIMS.md row 27); re-verify that use and extend it.
- Verbeek, P.-P. (2006). "Materializing morality: Design ethics and technological mediation."
  *Science, Technology, & Human Values* 31(3): 361–380. The design-ethics statement of mediation
  theory; the home of "designers should anticipate mediations."
- Verbeek, P.-P. (2008). "Cyborg intentionality." *Phenomenology and the Cognitive Sciences* 7(3):
  387–395. Composite intentionality — human intentionality directed at technological
  intentionality directed at the world — is the nearest thing to a mediator with its own
  directedness.
- Verbeek, P.-P. (2011). *Moralizing Technology*. U Chicago Press. The moralization debate
  (Achterhuis's speed-bump charge **[check: Achterhuis 1995 is in Dutch; read via Verbeek's
  account]**) and the account of scripts via Akrich and Latour. Note for the hypothesis map:
  "script" is Akrich's term, not Verbeek's; Verbeek prefers "mediation."
- Verbeek, P.-P. (2015). "Beyond interaction: A short introduction to mediation theory."
  *interactions* 22(3): 26–31. Short, ACM, and the version an HCI reader will know.
- Akrich, M. (1992). "The de-scription of technical objects." In Bijker & Law (eds), *Shaping
  Technology / Building Society*. MIT Press. Source of "script."
- Latour, B. (1992). "Where are the missing masses?" Same volume. And Latour, B. (1994). "On
  technical mediation." *Common Knowledge* 3(2): 29–64. The four meanings of mediation to set
  against Φ.
- Rosenberger, R., & Verbeek, P.-P. (eds) (2015). *Postphenomenological Investigations*.
  Lexington. For the field's own statement of its relation schema and whether it has a two-human
  case.
- Wellner, G. (2016). *A Postphenomenological Inquiry of Cell Phones*. Lexington. **[check:
  whether it treats phone-mediated interpersonal relations as a distinct relation type]**. This is
  the one place I expect postphenomenology may already have a two-human schema.

### Cluster B — Vallor, virtue, friction (RQ3)

- Vallor, S. (2015). "Moral deskilling and upskilling in a new machine age." *Philosophy &
  Technology* 28(1): 107–124. The load-bearing paper for RQ3.
- Vallor, S. (2016). *Technology and the Virtues*. Oxford UP. The twelve technomoral virtues and
  technomoral wisdom; chapters on moral deskilling and on practices.
- Vallor, S. (2024). *The AI Mirror*. Oxford UP. **[check: which chapters bear on automation of
  judgment and whether "friction" appears]**.
- Vallor, S. (2010). "Social networking technology and the virtues." *Ethics and Information
  Technology* 12(2): 157–170. Early, and in a target journal.
- MacIntyre, A. (1981/2007). *After Virtue*. Notre Dame. Chapter 14 on practices, internal goods,
  institutions — the machinery Vallor imports.
- Sunstein, C. R. (2021). *Sludge*. MIT Press. And Thaler, R. H., & Sunstein, C. R. (2008).
  *Nudge*. Yale UP. The opposing literature on friction.
- Cox, A. L., Gould, S. J. J., Cecchinato, M. E., Iacovides, I., & Renfree, I. (2016). "Design
  frictions for mindful interactions: The case for microboundaries." CHI EA. The HCI paper that
  argues for friction by name.
- Frischmann, B., & Selinger, E. (2018). *Re-Engineering Humanity*. Cambridge UP. "Engineered
  complacency" — the frictionless-design critique from law and philosophy.
- Bainbridge, L. (1983). "Ironies of automation." *Automatica* 19(6): 775–779. Deskilling as a
  human-factors finding forty years before Vallor; bridges clusters B and C.
- Gray, C. M., Kou, Y., Battles, B., Hoggatt, J., & Toombs, A. L. (2018). "The dark (patterns)
  side of UX design." CHI. Frictionlessness as manipulation, from the design side.

### Cluster C — Human-factors automation trust and reliance (RQ4)

Classic:
- Lee, J. D., & See, K. A. (2004). "Trust in automation: Designing for appropriate reliance."
  *Human Factors* 46(1): 50–80.
- Parasuraman, R., & Riley, V. (1997). "Humans and automation: Use, misuse, disuse, abuse."
  *Human Factors* 39(2): 230–253. "Abuse" is the designer's category and the closest the
  literature comes to a third party's objective.
- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). "A model for types and levels of
  human interaction with automation." *IEEE Trans. SMC-A* 30(3): 286–297.
- Parasuraman, R., & Manzey, D. H. (2010). "Complacency and bias in human use of automation."
  *Human Factors* 52(3): 381–410.
- Mosier, K. L., Skitka, L. J., Heers, S., & Burdick, M. (1998). "Automation bias." *Int. J.
  Aviation Psychology* 8(1): 47–63. And Skitka, Mosier & Burdick (1999). "Does automation bias
  decision-making?" *IJHCS* 51(5): 991–1006.
- Hoff, K. A., & Bashir, M. (2015). "Trust in automation: Integrating empirical evidence."
  *Human Factors* 57(3): 407–434. The review to cite for the field's shape.
- Dzindolet, M. T., et al. (2003). "The role of trust in automation reliance." *IJHCS* 58(6):
  697–718.
- Endsley, M. R., & Kiris, E. O. (1995). "The out-of-the-loop performance problem." *Human
  Factors* 37(2): 381–394.
- Sarter, N. B., & Woods, D. D. (1995). "How in the world did we ever get into that mode?" *Human
  Factors* 37(1): 5–19. Automation surprises are the temporal component of algorithmacy in HF
  vocabulary.
- Norman, D. A. (1990). "The 'problem' with automation." *Phil. Trans. R. Soc. B* 327: 585–593.
- Klein, G., Woods, D. D., Bradshaw, J. M., Hoffman, R. R., & Feltovich, P. J. (2004). "Ten
  challenges for making automation a 'team player.'" *IEEE Intelligent Systems* 19(6): 91–95. And
  Christoffersen, K., & Woods, D. D. (2002). "How to make automated systems team players."
  *Advances in Human Performance and Cognitive Engineering Research* 2: 1–12. The "team player"
  frame is dyadic by construction; that is the finding.
- Hollnagel, E., & Woods, D. D. (2005). *Joint Cognitive Systems*. CRC. And Hutchins, E. (1995).
  *Cognition in the Wild*. MIT Press. Distributed cognition is the nearest HF tradition to
  irreducibility of a joint system.

Recent human–AI reliance (the wider field around Bo/Buçinca):
- Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). "Algorithm aversion." *JEP: General*
  144(1): 114–126. And (2018) "Overcoming algorithm aversion." *Management Science* 64(3):
  1155–1170 — modifiability restores use, which is evidence for the counterfactual affordance.
- Logg, J. M., Minson, J. A., & Moore, D. A. (2019). "Algorithm appreciation." *OBHDP* 151:
  90–103.
- Bansal, G., et al. (2021). "Does the whole exceed its parts?" CHI.
- Vasconcelos, H., et al. (2023). "Explanations can reduce overreliance on AI systems during
  decision-making." *PACM HCI* 7(CSCW1).
- Lai, V., Chen, C., Smith-Renner, A., Liao, Q. V., & Tan, C. (2023). "Towards a science of
  human-AI decision making." FAccT. The design-space review.
- Green, B., & Chen, Y. (2019). "The principles and limits of algorithm-in-the-loop decision
  making." *PACM HCI* 3(CSCW).
- Jacovi, A., Marasović, A., Miller, T., & Goldberg, Y. (2021). "Formalizing trust in artificial
  intelligence." FAccT.
- Miller, T. (2023). "Explainable AI is dead, long live explainable AI! Hypothesis-driven decision
  support using evaluative AI." FAccT. The nearest published relative of cognitive forcing.

Triadic HF cases:
- Midkiff, A. H., & Hansman, R. J. (1993). "Identification of important 'party line' information
  elements and implications for situational awareness in the datalink environment." *Air Traffic
  Control Quarterly* 1(1). **[check: exact pages; access likely via MIT ICAT reports]**. And
  Pritchett & Hansman on party-line information requirements **[check: year and venue — I am not
  confident of the citation]**. If these hold, CPDLC is the paper's one real-world human-factors
  case of suppressing the direct channel.
- Exam-room computing and clinical decision support between two clinicians: no specific source I
  can name with confidence — a pass agent should search, and report absence honestly.

### Cluster D — Value-sensitive design, contestability, standards (RQ5)

- Friedman, B., & Hendry, D. G. (2019). *Value Sensitive Design: Shaping Technology with Moral
  Imagination*. MIT Press. Direct/indirect stakeholders; the seventeen methods.
- Friedman, B., Kahn, P. H., & Borning, A. (2006/2008). "Value sensitive design and information
  systems." In Zhang & Galletta (eds) 2006, reprinted in Himma & Tavani (eds) *Handbook of
  Information and Computer Ethics* 2008.
- Friedman, B., & Nissenbaum, H. (1996). "Bias in computer systems." *ACM TOIS* 14(3): 330–347.
  Preexisting, technical, emergent bias — emergent bias is the temporal component again.
- Le Dantec, C. A., Poole, E. S., & Wyche, S. P. (2009). "Values as lived experience." CHI.
- Borning, A., & Muller, M. (2012). "Next steps for value sensitive design." CHI.
- Manders-Huits, N. (2011). "What values in design?" *Science and Engineering Ethics* 17(2):
  271–287. In a target journal.
- JafariNaimi, N., Nathan, L., & Hargraves, I. (2015). "Values as hypotheses." *Design Issues*
  31(4): 91–104. In a target journal; the sharpest critique.
- van de Poel, I. (2013). "Translating values into design requirements." In Michelfelder et al.
  (eds), *Philosophy and Engineering*. Springer. The values hierarchy.
- Umbrello, S., & van de Poel, I. (2021). "Mapping value sensitive design onto AI for social good
  principles." *AI and Ethics* 1: 283–296 **[check volume/pages]**.
- Hirsch, T., Merced, K., Narayanan, S., Imel, Z. E., & Atkins, D. C. (2017). "Designing
  contestability." DIS. Lyons, H., Velloso, E., & Miller, T. (2021). "Conceptualising
  contestability." *PACM HCI* 5(CSCW1). Alfrink, K., Keller, I., Kortuem, G., & Doorn, N. (2023).
  "Contestable AI by design." *Minds and Machines* 33: 613–639.
- IEEE Global Initiative (2019). *Ethically Aligned Design*, 1st ed. Free. IEEE 7000-2021 and IEEE
  7001-2021 **[paywalled?]**; Winfield, A. F. T., et al. (2021). "IEEE P7001: A proposed standard
  on transparency." *Frontiers in Robotics and AI* 8 — open access and the readable route in.
- Spiekermann, S. (2016). *Ethical IT Innovation*. CRC. The value-based engineering behind 7000.

### Cluster E — Winner, STS, CSCW, the third party (RQ6, RQ8, RQ9)

- Winner, L. (1980). "Do artifacts have politics?" *Daedalus* 109(1): 121–136. Winner, L. (1986).
  *The Whale and the Reactor*. U Chicago. Winner, L. (1977). *Autonomous Technology*. MIT Press.
  Read the second claim (inherently political technologies) more closely than the first.
- Joerges, B. (1999). "Do politics have artefacts?" *Social Studies of Science* 29(3): 411–431.
  Woolgar, S., & Cooper, G. (1999). "Do artefacts have ambivalence?" *SSS* 29(3): 433–449. The
  bridges are contested; do not use them.
- Winner, L. (1993). "Upon opening the black box and finding it empty." *ST&HV* 18(3): 362–378.
- Winograd, T., & Flores, F. (1986). *Understanding Computers and Cognition*. Ablex. The
  Coordinator. Suchman, L. (1994). "Do categories have politics?" *CSCW* 2(3): 177–190, and
  Winograd's reply in the same issue. Suchman, L. (2007). *Human–Machine Reconfigurations*.
  Cambridge UP.
- Schmidt, K., & Simone, C. (1996). "Coordination mechanisms." *CSCW* 5(2–3): 155–200. The
  protocol-plus-artifact account of a mechanism that coordinates *between* people.
- Simmel, G. (1908/1950). "The triad." In Wolff (ed.), *The Sociology of Georg Simmel*. Free
  Press, pp. 145–169. Mediator, tertius gaudens, divide et impera. Burt, R. S. (1992). *Structural
  Holes*. Harvard UP. Obstfeld, D. (2005). "Social networks, the tertius iungens orientation."
  *ASQ* 50(1): 100–130. The dissertation's Paper 1 may already hold these; check before carding.
- de Certeau, M. (1984). *The Practice of Everyday Life*. U California. Introduction and ch. 3,
  tactics versus strategies.
- Brunton, F., & Nissenbaum, H. (2015). *Obfuscation*. MIT Press.
- DiSalvo, C. (2012). *Adversarial Design*. MIT Press. DiSalvo, C. (2022). *Design as Democratic
  Inquiry*. MIT Press. Mouffe, C. (2000). *The Democratic Paradox*. Verso — the agonism DiSalvo
  builds on.
- Dunne, A., & Raby, F. (2013). *Speculative Everything*. MIT Press. Bardzell, J., & Bardzell, S.
  (2013). "What is 'critical' about critical design?" CHI. Ratto, M. (2011). "Critical making."
  *The Information Society* 27(4): 252–260. For placing adversarial design among its neighbors.
- Seams lineage, which Ehsan et al. cite and the paper should own: Weiser, M. (1991). "The
  computer for the 21st century." *Scientific American* 265(3): 94–104. Chalmers, M., & Galani,
  A. (2004). "Seamful interweaving." DIS. Inman, S., & Ribes, D. (2019). "'Beautiful seams':
  Strategic revelations and concealments." CHI. Dourish, P., & Bell, G. (2011). *Divining a
  Digital Future*. MIT Press, the seamful chapter.
- Adjacent construct the paper must cite because it claims to supersede it: Long, D., & Magerko,
  B. (2020). "What is AI literacy?" CHI. Cotter, K., & Reisdorf, B. C. (2020). "Algorithmic
  knowledge gaps." *IJoC* 14. Zuboff, S. (1988). *In the Age of the Smart Machine*. Basic Books —
  "informate" as the literacy-era competence.

### Cluster F — Floridi, Taddeo, and the transparency-ideal critics (RQ7)

- Floridi, L., & Sanders, J. W. (2004). "On the morality of artificial agents." *Minds and
  Machines* 14(3): 349–379. Levels of abstraction.
- Floridi, L. (2016). "Faultless responsibility." *Phil. Trans. R. Soc. A* 374: 20160112.
- Floridi, L., Cowls, J., et al. (2018). "AI4People." *Minds and Machines* 28(4): 689–707. Floridi,
  L., & Cowls, J. (2019). "A unified framework of five principles." *HDSR* 1(1).
- Taddeo, M. (2010). "Modelling trust in artificial agents." *Minds and Machines* 20(2): 243–257.
  Taddeo, M., & Floridi, L. (2018). "How AI can be a force for good." *Science* 361(6404):
  751–752.
- Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S., & Floridi, L. (2016). "The ethics of
  algorithms: Mapping the debate." *Big Data & Society* 3(2). Tsamados, A., et al. (2022). "The
  ethics of algorithms: Key problems and solutions." *AI & Society* 37: 215–230.
- Burrell, J. (2016). "How the machine 'thinks.'" *Big Data & Society* 3(1). Ananny, M., &
  Crawford, K. (2018). "Seeing without knowing." *New Media & Society* 20(3): 973–989. Kroll, J.
  A., et al. (2017). "Accountable algorithms." *U. Penn. L. Rev.* 165: 633–705. Selbst, A. D., &
  Barocas, S. (2018). "The intuitive appeal of explainable machines." *Fordham L. Rev.* 87: 1085.
- Wachter, S., Mittelstadt, B., & Russell, C. (2018). "Counterfactual explanations without opening
  the black box." *Harvard JOLT* 31(2): 841–887. The legal-ethics ground for affordance 2.
- Miller, T. (2019). "Explanation in artificial intelligence: Insights from the social sciences."
  *Artificial Intelligence* 267: 1–38.

### Cluster G — The hypothesis map's own proposal (RQ9 test case)

- C2PA specification (Coalition for Content Provenance and Authenticity), current version — free,
  a standard, not a paper.
- Mechanistic interpretability: Olah, C., et al. (2020). "Zoom in: An introduction to circuits."
  *Distill*. Elhage, N., et al. (2021). "A mathematical framework for transformer circuits."
  Anthropic (web). Bereska, L., & Gavves, E. (2024). "Mechanistic interpretability for AI safety
  — a review." *TMLR* **[check]**. Read only far enough to state what the method discloses and to
  whom.
- A sample of 20 entries from the Gemini report's 193-item bibliography, drawn at random, checked
  for existence and for whether the cited text says what the report says. This yields a
  fabrication-rate estimate and settles whether any of it is worth mining further.

---

## 4. Candidate theses

Four positions, each of which the research above could support and each of which excludes the
others as the paper's spine.

**T1 — The mediation thesis (philosophy of technology).** Postphenomenology has no relation type
for a technology between two intentional parties, and its non-neutrality thesis cannot say when a
mediator is load-bearing because it holds that every mediator is. The bilateral hermeneutic
relation supplies the missing type, and Φ supplies the threshold: a mediation is constitutive when
the coordination it carries is irreducible. Verbeek's design ethics then becomes conditional —
anticipate mediations *where Φ > 0* — and seamful disclosure is its instrument. Risk: the paper
becomes a Verbeek exegesis and the human-factors reader leaves.

**T2 — The friction thesis (design ethics with human-factors evidence).** The friction dilemma is
unresolvable on the user's preference or the designer's intent and dissolves once friction is
sorted by whose objective it serves. Friction that serves the intermediary's objective is sludge;
friction that returns a judgment to a co-determined party is scaffolding. Vallor's deskilling
argument gives the normative criterion (does the friction preserve a practice?), the cooptation
reading gives the structural one (is there a third objective in the loop?), and Φ tells the
designer when the second question even arises. Buçinca, Bo, and Rader are the evidence base
already in hand; Sunstein is the opponent. Risk: the Φ half can read as decoration unless the
paper shows a case where the dyadic and triadic readings recommend different frictions.

**T3 — The reliance thesis (human factors).** *Appropriate reliance* is undefined for triadic
automation. Lee & See define trust relative to the trustor's goals; Parasuraman & Riley's
categories run out at "abuse," which is the designer's fault, not a third party's pursuit. When the
automation calibrates both humans and its objective belongs to neither, calibration has no target,
and the operator's competence is not reliance but algorithmacy. CPDLC party-line loss is the field
case. Risk: the case literature may be thinner than I hope, and *Human Factors* will want data.

**T4 — The methodology thesis (design research).** VSD and the four affordances are complements at
different levels — process versus product — but VSD's consensual stakeholder model breaks under
cooptation, where one stakeholder's value is the extraction of the others' agency. Adversarial
design supplies the politics VSD lacks; contestability-by-design supplies the verb the definition
needs; and the four affordances are what adversarial design looks like when built for the co-opted
party rather than for a public. Risk: three design traditions plus Φ is a crowded paper.

---

## 5. Target journals

I cannot check 2025–2026 tables of contents from here. Each entry states what the venue has
published in this territory that I am confident of, and what shape of paper it takes; the harness
includes a short pass to read the last two volumes' contents and confirm or overturn these fits.

- **Ethics and Information Technology** (Springer). Vallor 2010 is here; the journal takes
  conceptual argument at 8–10k words with a light empirical base. Best fit for T2 and a good home
  for T1. Ranked first.
- **Philosophy & Technology** (Springer; Floridi is editor-in-chief). Vallor 2015 deskilling is
  here. Favors formally disciplined argument — a levels-of-abstraction defense of the Φ verdict
  would be at home. Best fit for T1; T2 viable. Risk: an HF reader will not see it.
- **Design Issues** (MIT Press). JafariNaimi et al. 2015 and DiSalvo's design-theory work are here.
  Takes 6–8k-word theoretical essays on design; no experiments expected. Best fit for T4; T2 works
  if framed as a design argument.
- **Science and Engineering Ethics** (Springer). Manders-Huits 2011 is here. Engineering-ethics
  readership; a VSD-methodology comparison (T4) fits; T2 fits if pitched at engineers.
- **Big Data & Society** (SAGE, open access). Mittelstadt 2016, Burrell 2016, Seaver 2017. Critical
  data studies; the cooptation lens is native here and Φ would need careful framing to avoid
  reading as scientism. Fits a sociological cut of T2 or T4.
- **International Journal of Human-Computer Studies** (Elsevier). Skitka 1999 and Dzindolet 2003
  are here. Takes conceptual frameworks with theoretical depth as well as experiments. Best HF-side
  home for T3 if the paper offers a formal model and testable propositions.
- **Theoretical Issues in Ergonomics Science** (Taylor & Francis). The HF venue that exists for
  theory papers. A cleaner fit for T3 than *Human Factors*.
- **Human Factors** (SAGE/HFES). Lee & See 2004, Parasuraman & Riley 1997, Hoff & Bashir 2015 are
  here. Takes reviews and theory only when they organize a literature; a pure argument paper is a
  hard sell. Fit for T3 only with a substantial literature integration.
- **Techné: Research in Philosophy and Technology**. Postphenomenology's home journal. Fit for T1
  only; too narrow for the reconciliation the piece wants.
- **AI & Society** (Springer). Tsamados 2022. Broad, receptive, lower selectivity. A fallback.

My ordering for T2: Ethics and Information Technology, then Design Issues, then Philosophy &
Technology. For T3: IJHCS, then TIES.

---

## 6. Harness design

Precedent: the `algorithmacy_scaffolding` arm ran six parallel Fable passes, produced 41 cards, and
its dossier found one misattributed citation carrying a claim it never supported (Quinby), one
citation ambiguity verified only against a 2025 rewrite (DeKeyser), one chapter verified only from
secondary characterizations (Scardamalia & Bereiter), four abstract-only or second-hand sources,
and one verified finding that contradicted a design affordance as written (Bo 2025). That is the
quality bar: a pass is good when it reports those things, not when it avoids them.

**Eight research passes plus two service passes**, Fable model, run in parallel, each writing
cards to `submissions/algorithmacy_design_ethics/literature/library/` in the exact format of
`submissions/algorithmacy_scaffolding/literature/library/ehsan2024.md`.

| Pass | Cluster | Questions | Expected cards |
|---|---|---|---|
| P1 | A — Postphenomenology and mediation | RQ1, RQ2 | 8–10 |
| P2 | B — Vallor, virtue, friction | RQ3 | 8–10 |
| P3 | C(i) — Classic HF automation trust | RQ4 | 10–12 |
| P4 | C(ii) — Recent human–AI reliance + triadic HF cases | RQ4, RQ9 | 8–10 |
| P5 | D — VSD, contestability, standards | RQ5 | 10–12 |
| P6 | E — Winner, STS, CSCW, the third | RQ6, RQ8, RQ9 | 10–12 |
| P7 | F — Floridi/Taddeo and transparency critics | RQ7 | 8–10 |
| P8 | G — Hypothesis-map audit (mech-interp, C2PA, 20-entry sample) | RQ9 | 4–6 + a rate |
| S1 | Journal scan: last two volumes of the nine venues in §5 | — | one memo |
| S2 | Adversarial verification of every ✓ card from P1–P8 | — | corrections |

Roughly 70–80 cards before S2 prunes. That is about double the scaffolding arm, which is right for
a paper that must show awareness of five literatures rather than one.

**Every research-pass prompt must require:**

1. *Primary-source verification.* No card without the agent having opened the version of record
   or an author-deposited preprint. Read depth recorded as one of `full_text`, `partial`
   (say which sections), `abstract_only`, or `secondary` (name the citing source). A card built at
   `abstract_only` or `secondary` says so in its first line and in the INDEX flag.
2. *Access flags.* Paywalled, HathiTrust search-only, standards behind a fee, and out-of-print
   books each get a named flag. The agent does not paraphrase a paywalled paper's results from its
   abstract as though they were read.
3. *No invented anything.* No page number, quotation, DOI, volume, or author list the agent did
   not see. A quotation without a seen page number is paraphrased and marked. A **[check]** entry
   from §3 that cannot be resolved is dropped and reported as dropped.
4. *The dyadic/triadic field.* A new header field for this arm: `Parties modeled:` with one of
   `human–technology`, `human–technology–world`, `two humans + mediator`, `designer–stakeholders`,
   or `n/a`. This is what makes RQ9 answerable by grep at the end rather than by re-reading.
5. *Relation to the argument* written against the tightened definition in §1, naming which axis
   (structural, objective) and which affordance the source touches, and stating outright when the
   source cuts *against* the lab's construct. Contradictions are the pass's most valuable output.
6. *Caution section* on every card, in the Ehsan-card style: what the source does not show, the
   sample, the design, the setting.
7. *A closing memo per pass* of at most 400 words: the three strongest cards, every source
   dropped and why, every finding that contradicts the definition or an affordance, and what the
   agent would read next with another day.

**S2, the adversarial verifier**, takes each card marked ✓ and tries to break it: re-open the
source, check that every quoted string and number appears, check that the "Relation" claim is not
stronger than the source. It writes corrections into the card and downgrades the flag where
warranted. This is the step that caught Quinby last time; it is not optional.

**Ordering.** P1–P8 and S1 run in parallel on day one. S2 runs after all eight report. The INDEX
and a dossier in the form of `RESEARCH_DOSSIER.md` are written last, by the coordinating agent, not
by any pass — the dossier's job is to map cards back onto the nine questions and say which thesis
survived.

**What not to do.** Do not re-verify Flower & Hayes 1981, Ellis 1996, Yarlas & Sloutsky 2000,
Eslami et al. 2015, Rader/Cotter/Cho 2018, Reich 1964, Stark & Vanden Broeck 2024, Llewellyn 1930,
or Knorr Cetina & Bruegger 2002; adapt their existing cards with a fresh "Relation" section as the
scaffolding arm did for Stark and Selznick. Do not card Martela & Steger. Do not treat any Gemini
bibliography entry as a lead until P8 has sampled the fabrication rate.

---

## 7. The strongest candidate

T2, the friction thesis, is the one to build the paper around. It is the only candidate that makes
both lenses do visible work in one argument: the cooptation reading supplies the criterion (whose
objective the friction serves), the Φ reading supplies the trigger (whether a third objective is in
the loop at all), and neither can carry the argument alone — a Φ-free version cannot tell a
translator from a platform, and a cooptation-only version has no test for when the structure
demands the competence. It has an opponent worth having in Sunstein's sludge and in every
commercial frictionlessness brief, it inherits three verified experiments from the scaffolding arm
as its evidence base, and it lands in the journal (*Ethics and Information Technology*) whose
readership already knows Vallor and would meet the Φ material as a fresh instrument rather than an
intrusion. Its one real risk is that Φ reads as decoration, and the cure is specific: the paper
needs one worked case where the dyadic and triadic readings recommend different frictions — the
datalink party line, if P4 finds it, or a delivery-platform model the lab can already compute. T1
is the natural companion paper for *Philosophy & Technology* once T2 is out; T3 is the one to hold
until the triadic HF cases are confirmed to exist.
