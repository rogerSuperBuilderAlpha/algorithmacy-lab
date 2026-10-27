# Antonio Scala's revised plan and abstract, 25 Oct 2026

[Filed by Claude, 26 Oct 2026, verbatim from Roger's paste of Antonio's message. Antonio's words throughout; nothing below is Roger's or Claude's. The simulation-parameter symbols were lost in the paste (they appear as blanks); Antonio's `coordinative_sovereignty_sim.py` was not attached. The merged abstract that answers this plan is `ABSTRACT.md` (v5); an independent run of the model is in `model/`.]

Let's identify what works and att doesn't and create a new version of the abstract combining our ideas

Conditions for Coordinative Sovereignty – revised plan

Authors: Roger Hunt, Antonio Scala et al.
Target: Exetasis, special issue "AI and Sovereignty" — https://philevents.org/event/show/154909
Abstract: 300–500 words + short bio and affiliation, to editorial@exetasis.net, subject "CFP — AI and Sovereignty", deadline 20 December 2026
Full paper (if invited): ≈ 8,000 words
Fit with the call: tracks 3 (AI, autonomy and individual sovereignty) and 4 (rethinking sovereignty; "new political concepts")

Possible Abstract

Democratic theory has long tied popular sovereignty to civic competence. In fifth-century Greece, democracy was "from the beginning associated with widespread literacy" (Goody & Watt, 1963, p. 332), and current responses to algorithmic power repeat the premise, calling for technology literacy and civic education to restore epistemic agency (Son, 2022; Coeckelbergh, 2023). The history of literacy shows the premise to be incomplete. Mass schooling expanded largely under nondemocratic regimes that used it to instil obedience (Paglayan, 2022): literate subjects lacked standing, not qualifications. Reading enabled sovereignty only where law, a free press and an enfranchised public could compel authority to account.

Algorithmic coordination reproduces this gap in sharper form. It operates through a triadic structure with the platform operator at the apex (Stark & Vanden Broeck, 2024), resists ordinary forms of literacy (Burrell, 2016), and issues no public decrees, producing no subject to address (Rouvroy & Berns, 2013). Operating within it requires algorithmacy: the competence to infer intermediary evaluations, encode intent and adapt as predictive models evolve. Yet algorithmacy yields positional advantage over peers, not collective standing (Gagrčin et al., 2026), and exit is no remedy when "a choice between awful regimes cannot confer authority on either" (Lazar, 2025, p. 163).

We identify what lies between competence and standing: the formation of the collective that could claim it. Drawing on network science, we argue that the capacity for collective mobilisation is a structural property of relations, not an aggregate of individual competences. Mobilisation that requires social reinforcement crosses between communities only through wide bridges, that is, multiple converging ties (Centola & Macy, 2007). A minimal simulation of threshold contagion on a modular network illustrates the point: individual competence compensates for thin bridges only when it sits at bridge positions, while competence distributed at random leaves mobilisation largely confined to its community of origin. Since recommendation systems shape which ties form and where bridges lie, even without political intent (Santos et al., 2021), the intermediary takes part in producing, or failing to produce, the collective subject that might contest it.

We call the missing condition coordinative sovereignty: a population's capacity to form and sustain the relations through which it can act as a collective subject and hold coordinating authority to account, independently of any single intermediary. Situated in the lineage of constituent power, the concept names a dimension of sovereignty that neither state technological sovereignty nor individual autonomy captures. AI-literacy policies, like literacy campaigns before them, are necessary but cannot by themselves secure self-government: the conditions under which relations form are themselves a question of sovereignty.

The body is 425 words, inside the 300–500 limit.

Changes from Roger's text:

Paragraphs 1–2 are his, compressed.
Paragraph 3 (the network mechanism and the simulation) and paragraph 4 (the definition of coordinative sovereignty) are new.
The Mill quote was cut to make room, and "irreducible mediation" no longer appears.
To check before sending:

The page-cited quotations (Goody & Watt, Lazar).
Whether you want a reference list attached. The call doesn't ask for one; Roger included one.
A bio and affiliation for each author.

## 1. Thesis

A population's capacity to act as a collective subject is a property of the structure of its relations, not of the competence of its members. An intermediary that shapes how those relations form therefore takes part in producing — or in failing to produce — the collective subject of sovereignty, whatever the individual Algorithmacy of its users.
Central concept: coordinative sovereignty — the capacity of a population to form and sustain the relations through which it can act as a collective subject and hold the coordinating authority to account, independently of any single intermediary.

## 2. What we take from Roger's original abstract

Roger's abstract ("Conditions for Coordinative Sovereignty") already provides most of the argument:

Competence ≠ sovereignty. Literacy was historically necessary for democratic sovereignty but never sufficient (Goody & Watt 1963; Paglayan 2022; against Mill 1861).
Triadic, opaque, co-optive coordination (Stark & Vanden Broeck 2024; Burrell 2016; Rouvroy & Berns 2013).
Algorithmacy, defined individually: the competence to infer intermediary evaluations, encode intent and adapt as models evolve. This definition is adopted (replacing the relational one of the earlier battleplan).
Algorithmacy gives positional advantage over peers, not collective standing (Gagrčin et al. 2026).
Exit is not a remedy; collective voice is (Lazar 2025).
Missing step, supplied by the joint paper: Roger moves directly from "competence is insufficient" to "collective standing". He does not ask whether the collective that would hold that standing can form under mediation. Sections 4–5 below fill that gap. "Irreducible mediation" (Roger's phrase) is the hook.

Tension to exploit: Rouvroy & Berns argue that algorithmic governmentality "produces no subjectivation". If no individual subject is addressed, the question becomes whether a collective subject can still be constituted — and who controls the conditions of its formation.

## 3. What we are not claiming

That platforms necessarily fragment societies or suppress collective action.
That fragmentation or community structure is bad in itself (it can protect pluralism).
That network cohesion confers political legitimacy.
That algorithmic feeds determine beliefs (see Guess et al. 2023: small attitudinal effects). Our claim concerns the structure of relations and the capacity to act together, not attitudes.
That the simulation is evidence about real platforms. It is a how-possibly illustration (Schelling 1971; Weisberg 2013).

## 4. Skeleton (≈ 7,300 words main text)

1. Introduction (600, joint)
The AI-and-sovereignty debate splits into two levels. One is state or technological sovereignty (infrastructure, chips, models); the other is individual sovereignty (autonomy, manipulation).
Missing middle: the collective capacity of a people to constitute itself, which belongs to neither level.
Contribution: (i) a historical argument that competence does not amount to sovereignty; (ii) a structural mechanism; (iii) a concept, coordinative sovereignty.

2. Competence is not sovereignty: the case of literacy (1,100, Roger)
Goody & Watt: literacy as the medium of written institutions.
Literate populations remained subordinated. Sovereignty required citizenship, the franchise and collective organisation.
Paglayan: the competence was supplied by the authority it might have been used to contest.
Lesson: competence is a necessary input. It is neither sufficient nor politically neutral as to who provides it.

3. Algorithmacy and the limits of individual remedies (800, Roger)
Algorithmacy defined relationally: competence in coordinating with others under algorithmic mediation, not skill at gaming rankings.
The parallel: AI-literacy and individual-autonomy remedies (the call's track 3) reproduce the literacy mistake.
Bridge to §4: if competence does not suffice, what else is needed? Answer: structure.

4. Collective agency as a structural property (1,400, Antonio)
Simple versus complex contagion. Mobilisation needs reinforcement, which needs wide bridges between communities (Centola–Macy).
Figure (two panels). Compare collective reach when (a) every node's competence is raised and (b) the bridges between communities are thinned.
Claim to be tested by simulation: beyond some point, competence cannot make up for missing bridges.
Rule for this section: no formula in the body text. The model goes in the appendix.

5. Mediation as the production of collective subjects (1,200, joint)
Recommenders shape how networks form. Similarity-based link recommendation produces more separated communities (Santos et al.), with no political intent required.
This links to the call's own framing: power produces subjects. Here, what gets produced or blocked is a collective subject, not an individual one.
Constraint from the Meta 2023 experiments: feed effects on beliefs are small. Our claim concerns structure and the capacity to act together, not attitudes.
One paragraph on fragility: migration or changes to the platform can preserve pairwise contacts while destroying wide bridges. This is where portability survives.

6. Coordinative sovereignty (1,300, Roger lead)
Definition: a population's capacity to form and sustain the relations through which it can act as a collective subject, independently of any single mediator.
Placement against existing concepts:
constituent power (Sieyès, Williams);
Klein's organised collective power;
Cohen–Suzor's "capabilities to organise";
the distinction from state technological sovereignty and from individual sovereignty.
Why sovereignty rather than domination (Aytaç, Hoeksema): our concern is the constitution of the collective subject itself, not only interference with it.

7. Objections (600, joint)
Network communities are not political subjects.
Fragmentation can protect pluralism.
Platforms also enable political movements.
The Meta null results.
Why a new concept is needed at all.

8. Conclusion (300, Roger)
Return to literacy. AI-literacy policy is necessary but cannot secure sovereignty. The conditions under which relations form are themselves a matter of sovereignty.

Appendix (≈500, Antonio)
Model specification: network, contagion rule, how competence and bridge structure are each parametrised.

## 5. The model (§4 figure, appendix)

Purpose. Show, in the simplest possible setting, that (i) collective mobilisation depends on bridge width between communities; (ii) individual competence compensates for thin bridges only when it sits at bridge positions — and bridge positions are what an intermediary shapes.

Ingredients (implemented in coordinative_sovereignty_sim.py):
Network: a ring of [K] communities ("villages"), each a clique of [n] people. Neighbouring communities are joined by [w] random bridge ties — the bridge width.
Contagion: threshold rule (Granovetter 1978; Centola & Macy 2007). A person joins once the active signal from their neighbours reaches [θ] (complex contagion: one contact is not enough).
Seed: one whole community starts active.
Competence: [B] "competent" people; when active, their signal counts [2] instead of 1 (better signalling/credibility).
Three conditions: no competence; competence placed at random; competence placed at bridge endpoints.
Outcome: reach = fraction of the population eventually active, averaged over many network realisations.

Expected picture.
Panel (a): reach vs [w]. Wide bridges → contagion crosses; thin bridges → it stays local. Randomly placed competence shifts the curve little; competence at bridge endpoints shifts it a lot.
Panel (b): at thin bridges, reach vs budget [B]. Targeted competence achieves with few nodes what random competence needs many for.

Modelling choices to defend in the text.
Competence is not modelled as a lower threshold. Lowering [θ] to 1 turns complex contagion into simple contagion, which crosses any bridge. Philosophical justification: understanding the algorithm does not reduce the social reinforcement needed to take part in costly collective action.
Universal competence. If everyone is competent ([B = N]), every tie carries [2] and contagion becomes simple. The claim is therefore about realistic, partial competence and its distribution, not about an idealised population of experts. State this openly in §7.
Cliques. Communities are cliques for transparency; the result depends only on what happens at the bridges. Robustness check (optional): replace cliques with dense random graphs.

[Bracketed symbols above are Claude's reconstruction of the blanks in the paste, from the surrounding text and from the run in `model/`.]

## 6. Open decisions

Mapping of competence in the model (signal weight vs alternatives). Must be consistent with Roger's individual definition of Algorithmacy.
Whether "coordinative sovereignty" is presented as a new concept or as a specification of constituent power. Current choice: new concept, with constituent power as lineage.
Whether the portability paragraph (§5) stays.
Verify all page-cited quotations in Roger's abstract and the editors of Williams (2024).

## 7. Sequence

Run the simulation; check the figure supports the §4 claim. If not, revise the claim before the abstract.
Abstract (300–500 words), starting from Roger's text; add one sentence for the structural mechanism and one for the concept.
Submit by 20 December 2026.
If invited: draft §§4–6 first (the core), then §§2–3, then §§1, 7, 8.

## References (Antonio's list; unverified from this side except where `literature/VERIFICATION.md` already has a row)

Aytaç, U. (2024). Digital domination: Social media and contestatory democracy. Political Studies, 72(1). https://doi.org/10.1177/00323217221096564
Burrell, J. (2016). How the machine "thinks": Understanding opacity in machine learning algorithms. Big Data & Society, 3(1), 1–12. https://doi.org/10.1177/2053951715622512
Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. American Journal of Sociology, 113(3), 702–734. https://doi.org/10.1086/521848
Coeckelbergh, M. (2023). Democracy, epistemic agency, and AI: Political epistemology in times of artificial intelligence. AI and Ethics, 3(4), 1341–1350. https://doi.org/10.1007/s43681-022-00239-4
Cohen, T., & Suzor, N. P. (2024). Contesting the public interest in AI governance. Internet Policy Review, 13(3). https://doi.org/10.14763/2024.3.1794
Gagrčin, E., Naab, T. K., & Grub, M. F. (2026). Algorithmic media use and algorithm literacy: An integrative literature review. New Media & Society, 28(1), 423–447. https://doi.org/10.1177/14614448241291137
Goody, J., & Watt, I. (1963). The consequences of literacy. Comparative Studies in Society and History, 5(3), 304–345. https://doi.org/10.1017/S0010417500001730
Granovetter, M. (1978). Threshold models of collective behavior. American Journal of Sociology, 83(6), 1420–1443. https://doi.org/10.1086/226707
Guess, A. M., et al. (2023). How do social media feed algorithms affect attitudes and behavior in an election campaign? Science, 381(6656), 398–404. https://doi.org/10.1126/science.abp9364
Hoeksema, B. (2023). Digital domination and the promise of radical republicanism. Philosophy & Technology, 36, Article 17. https://doi.org/10.1007/s13347-023-00618-7
Klein, S. (2022). Democracy requires organized collective power. Journal of Political Philosophy, 30(1), 26–47. https://doi.org/10.1111/jopp.12249
Lazar, S. (2025). Governing the algorithmic city. Philosophy & Public Affairs, 53(2), 102–168. https://doi.org/10.1111/papa.12279
Mill, J. S. (1861). Considerations on Representative Government. London: Parker, Son, and Bourn.
Paglayan, A. S. (2022). Education or indoctrination? The violent origins of public school systems in an era of state-building. American Political Science Review, 116(4), 1242–1257. https://doi.org/10.1017/S0003055422000247
Rouvroy, A., & Berns, T. (2013). Gouvernementalité algorithmique et perspectives d'émancipation. Réseaux, 177, 163–196.
Santos, F. P., Lelkes, Y., & Levin, S. A. (2021). Link recommendation algorithms and dynamics of polarization in online social networks. PNAS, 118(50), e2102141118. https://doi.org/10.1073/pnas.2102141118
Schelling, T. C. (1971). Dynamic models of segregation. Journal of Mathematical Sociology, 1(2), 143–186. https://doi.org/10.1080/0022250X.1971.9989794
Sieyès, E.-J. (1789). Qu'est-ce que le tiers état? Paris.
Son, W.-C. (2022). Democracy in the time of "hyperlead": Knowledge acquisition via algorithmic recommendation and its political implication in comparison with orality, literacy, and hyperlink. Philosophy & Technology, 35(3), Article 80. https://doi.org/10.1007/s13347-022-00573-9
Stark, D., & Vanden Broeck, P. (2024). Principles of algorithmic management. Organization Theory, 5(2), 1–24. https://doi.org/10.1177/26317877241257213
Verhulst, S., & González Otero, B. (2026). The triad of tech sovereignty and Europe's package: Dependency, openness, and agency [Preprint]. SSRN. https://doi.org/10.2139/ssrn.6907425
Watts, D. J. (1999). Small Worlds: The Dynamics of Networks between Order and Randomness. Princeton University Press.
Weisberg, M. (2013). Simulation and Similarity: Using Models to Understand the World. Oxford University Press.
Williams, M. S. (2024). Deterritorializing democratic legitimacy. In Empowering Affected Interests. Cambridge University Press. [editors and pages to verify]
