# Conversations in *Organization Theory* 4(1)–7(3): clusterer O

Run `ot-oq-2026-11`, stage S9a. Clusterer O worked independently and did not open the other clusterer's files, `ALGORITHMACY_BRIEF.md`, `BASELINES.md`, `fit/` or `manuscript/`. The `fit_A`/`fit_B` columns of `QUESTIONS.tsv` were not used.

## How the counts were made

- **Pool.** 619 open OQs from 65 articles (all rows of `QUESTIONS.tsv` except `own_research_question`). `bartunek2025` has a record but no OQ rows, so it asks nothing here; it is mentioned only where its argument bears on a conversation.
- **Membership.** Each OQ sits in at most two conversations. 600 of the 619 OQs are placed; the other 19 are singletons (listed below).
- **Recurring.** Every conversation below has at least two asking articles with different first authors, counting only askers with at least one non-boundary OQ. Three also carry the editorial signal: O08, O32, O45.
- **Boundary conditions** are marked **(BC)** in member lists. An article whose only OQs in a conversation are boundary conditions counts 0.5 in the article counts.
- **Support line.** "Theory/review articles" counts `theory`, `review` and `essay` items (the two essays are Petriglieri & Ashford 2023 and Powell & DiMaggio 2023). "Commentary or exchange pieces" counts `controversies_conversations` items. Editorial items (Cornelissen et al. 2024; Höllerer et al. 2026) are not counted as articles. They set **editorial signal = y**, as does any OQ with form `editor_call` (Giovannoni & Quattrone 2025-07; Ernst et al. 2026-06).
- **Citation edges.** `EDGES.tsv` is not present. In its place I counted directed citations among the askers, using the records' "OT articles it cites" field (51 within-corpus edges in all, after removing false matches by hand; e.g. Hawbaker & Hallett cite Ocasio's 2023 *book*, not the OT article, and Suddaby cites Abend 2008/2023, not abend2024). Treat these counts as provisional until `EDGES.tsv` exists.
- **Order.** Conversations are ordered by support: the weighted count of asking articles (theory/review plus commentary), then editorial signal, then distinct volumes, then the most recent ask. Order does not measure depth. Several high-ranked conversations are *cross-cutting* (marked so): they gather one or two OQs from many articles on different topics, whereas topical ones gather many OQs from fewer articles.
- **Level** is my reading of where the conversation sits; the modal OQ level from `QUESTIONS.tsv` is given beside it.

## Index

| id | kind | question | askers (theory+comm.) | ed. | vols | last asked |
|---|---|---|---|---|---|---|
| O01 | cross-cutting | How does the history and temporal path of a tie, practice, institution or collective shape what it does now? | 12 | n | 4 | 2026-09-19 |
| O02 | cross-cutting | What exactly counts as an instance of the field's core constructs (a logic, a paradox, an organization, an institution, an imaginary), and where are their boundaries? | 11 | n | 4 | 2026-09-21 |
| O03 | cross-cutting | Which methods can capture what is hidden, absent, sociomaterial or changing in organizing? | 11 | n | 3 | 2025-09-28 |
| O04 | topical | How does organizing produce, reproduce or reduce exclusion and inequality? | 10.5 | n | 4 | 2026-06-19 |
| O05 | cross-cutting | What makes a collective organizational, and how do loose collectives, movements and non-human agents gain, hold or lose organizational actorhood? | 9 | n | 4 | 2026-09-19 |
| O06 | cross-cutting | What place do non-human things (technologies, objects, nature, atmospheres) have as actors in organizing? | 9 | n | 4 | 2026-04-01 |
| O07 | cross-cutting | What happens to organizational and professional competence and expertise when new knowledge or technology arrives: is it lost, kept or rebuilt? | 9 | n | 3 | 2026-07-28 |
| O08 | topical | Who decides which words, concepts and standards of good theory a scholarly community uses, and by what procedure? | 8 | y | 4 | 2026-09-19 |
| O09 | topical | How do organizations act, and how does organizing itself change, amid polarization, post-truth politics and democratic backsliding? | 8 | n | 4 | 2026-04-07 |
| O10 | cross-cutting | How do emotions and affect drive organizing, entrepreneurship and mobilization? | 8 | n | 3 | 2026-04-01 |
| O11 | topical | How do scholars' own selves, careers and positions enter their theorizing, and how should they reflect on that? | 7 | n | 4 | 2026-04-07 |
| O12 | topical | How can organization theory theorize what does not yet exist or cannot be known (futures, possibilities, absences) with rigour? | 7 | n | 4 | 2026-04-01 |
| O13 | cross-cutting | Who is answerable when decisions are made by algorithms, platforms or loosely bounded collectives rather than by an identifiable office-holder? | 7 | n | 3 | 2026-09-19 |
| O14 | cross-cutting | What are the failures and dark sides of organizing practices that the field usually treats as good? | 7 | n | 3 | 2025-11-11 |
| O15 | topical | What slow, indirect effects do digital technologies have on institutions, work and society beyond their visible uses? | 7 | n | 3 | 2025-07-11 |
| O16 | topical | How do new institutions and organizational forms emerge, take root or displace old ones, and what makes a field ready for them? | 7 | n | 2 | 2025-12-23 |
| O17 | topical | How do marginalized and excluded people gain a speaking position, a voice or cultural autonomy? | 6.5 | n | 2 | 2024-09-18 |
| O18 | cross-cutting | Who counts as a member (of a community, a demos, an organization, a stakeholder set), and who decides? | 6 | n | 4 | 2026-09-19 |
| O19 | topical | How do organizations and their members imagine and enact futures, and how is imagination practised together? | 6 | n | 3 | 2026-09-21 |
| O20 | cross-cutting | Should organization scholars act as critics or activists in the struggles they study, and what does inquiry owe to its political moment? | 6 | n | 3 | 2026-04-07 |
| O21 | cross-cutting | How do collective, organizational and personal identities form, and how do they shape what actors do? | 6 | n | 3 | 2026-04-01 |
| O22 | topical | Does generative AI take part in constructing categories, legitimacy and other social objects, and how should theory treat technology as an actor in that construction? | 6 | n | 3 | 2025-11 |
| O23 | topical | What makes an organization hold to its values under pressure, and how should its moral conduct be judged? | 5.5 | n | 3 | 2026-07-21 |
| O24 | topical | How do social movements and collective action form, shape markets and organizations, and what becomes of them after success or cooptation? | 5.5 | n | 3 | 2026-03-31 |
| O25 | topical | How do law, regulation and the state shape organizations, and can they restrain new technologies? | 5 | n | 4 | 2026-03-31 |
| O26 | topical | How does generative AI change coordination, teamwork and the division of labour inside organizations? | 5 | n | 3 | 2026-03-31 |
| O27 | topical | Which formal structures do organizations need for their purposes, and what can replace hierarchy? | 5 | n | 3 | 2026-03-31 |
| O28 | topical | How do organizations, communities and actors hold, rank or combine several institutional logics over time? | 5 | n | 3 | 2025-02-24 |
| O29 | cross-cutting | When is disagreement or dissent productive rather than destructive, for organizations and for scholarly communities? | 5 | n | 2 | 2026-07-28 |
| O30 | cross-cutting | What does digital technology at work demand of, and do to, the individual worker: hidden labour, consent, autonomy, meaning? | 5 | n | 2 | 2024-10-29 |
| O31 | cross-cutting | When and why do people resist control and new technology, and can resistance itself be productive? | 4.5 | n | 1 | 2024-10-29 |
| O32 | topical | Whose voices, bodies and standpoints count as legitimate sources of theory, and who is left out of the record? | 4 | y | 3 | 2026-07-26 |
| O33 | topical | Who takes part in organizational decision-making (strategy, governance, modeling), on whose terms, and with what effect? | 4 | n | 3 | 2026-07-28 |
| O34 | topical | How do organizations anticipate, respond to and learn from crises, and what should crisis response aim at? | 4 | n | 3 | 2026-07-21 |
| O35 | topical | How do physical space and the material settings of online and offline work shape coordination and presence? | 4 | n | 3 | 2026-04-01 |
| O36 | topical | How do organizations strengthen or erode democracy and citizens' capacity for public reason, inside and beyond their walls? | 4 | n | 3 | 2026-04-01 |
| O37 | topical | How do audiences, media and activists turn events into scandals and legitimacy tests, and how do digital platforms change that process? | 4 | n | 3 | 2025-11 |
| O38 | topical | How should organizations and their members respond to paradoxes (both/and, either/or, or neither), and how should those responses be judged? | 4 | n | 3 | 2025-09-27 |
| O39 | topical | What are institutional logics made of (beliefs, practices, law), where do they come from, and how do practices travel between them? | 4 | n | 3 | 2025-04-25 |
| O40 | topical | How can organizations take up and sustain care as an organizing value against the pull of control and efficiency? | 4 | n | 2 | 2026-07-21 |
| O41 | topical | How does neoliberal ideology shape what organizations and states treat as legitimate, from care to surveillance to public administration? | 4 | n | 2 | 2024-03-19 |
| O42 | topical | How does brokerage work, and what happens to brokers and resource holders when tie histories accumulate or technology takes over brokering? | 3 | n | 3 | 2025-09-28 |
| O43 | topical | What do practices actually do inside organizations once they have spread or been adopted: change conduct, or stay symbolic? | 3 | n | 2 | 2026-07-28 |
| O44 | topical | Can a person become an institution, and under what conditions does such an institution form, endure, or outlive the person? | 3 | n | 1 | 2025-12-23 |
| O45 | topical | What will large language models do to theorizing, and what expertise must scholars keep to judge them? | 2 | y | 1 | 2024-10-28 |
| O46 | topical | How do hype and attention around new technologies form, and with what institutional and power consequences? | 2 | n | 2 | 2025-12-23 |
| O47 | topical | How do stories and images around organizations and people become myths with sacred or binding force? | 2 | n | 2 | 2025-12-01 |
| O48 | topical | When are organizations rewarded for conforming, and when for staying distinct or 'pure', and before which audiences? | 2 | n | 2 | 2024-09-03 |

## Conversations

### O01. How does the history and temporal path of a tie, practice, institution or collective shape what it does now?

*Kind:* cross-cutting. *Key:* `time_history`.

**Members** (32 OQs from 12 articles):

- Brennecke 2025 (`brennecke2025`, theory): OQ-brennecke2025-02, OQ-brennecke2025-03, OQ-brennecke2025-04, OQ-brennecke2025-05, OQ-brennecke2025-06, OQ-brennecke2025-09, OQ-brennecke2025-10, OQ-brennecke2025-11, OQ-brennecke2025-12, OQ-brennecke2025-13, OQ-brennecke2025-14, OQ-brennecke2025-15, OQ-brennecke2025-17, OQ-brennecke2025-18, OQ-brennecke2025-19, OQ-brennecke2025-20, OQ-brennecke2025-21
- Garud 2025 (`garud2025`, theory): OQ-garud2025-03, OQ-garud2025-05, OQ-garud2025-07
- Justesen 2024 (`justesen2024`, theory): OQ-justesen2024-02, OQ-justesen2024-03
- Lantela 2024 (`lantela2024`, theory): OQ-lantela2024-03
- Suddaby 2024 (`suddaby2024`, controversies_conversations): OQ-suddaby2024-01
- Dion 2025 (`dion2025`, theory): OQ-dion2025-07
- Patriotta 2025 (`patriotta2025`, theory): OQ-patriotta2025-02, OQ-patriotta2025-07
- Schoeneborn 2026 (`schoeneborn2026`, theory): OQ-schoeneborn2026-05
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-12
- Sasaki 2024 (`sasaki2024`, theory): OQ-sasaki2024-05
- Derek Robinson 2025 (`derekrobinson2025`, controversies_conversations): OQ-derekrobinson2025-08
- Leitzinger 2023 (`leitzinger2023`, review): OQ-leitzinger2023-27

**Representative quotation** (OQ-brennecke2025-12, Brennecke 2025): “Which features of relational history are retained, which decay over time? When do narratives about a tie crystallize into dominant accounts that guide behaviour? Under what conditions do memories of key events become shared across both parties” (p. 19, "Cognitive and narrative construction of relational history")

**Support:** theory/review articles 10; commentary or exchange pieces 2; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 1; most recent ask 2026-09-19.

**Level of analysis:** multi-level (dyad and interaction to institution) (modal OQ level: interaction).

**What remains unanswered, and where the askers disagree.** Twelve askers want to know how the past of a thing acts on its present, but they ask it of different things. Brennecke et al. ask it of the dyadic tie (which features of a tie's history are retained, which decay, and when narratives about a tie crystallize); Patriotta et al. of an organization's earlier crises; Schoeneborn et al. of a collective's actorhood; Sasaki and Baba of marginalization that escalates; Leitzinger and Waeger of movements that shift goal types; Derek Robinson and Atanasova of a person-institution's ruptures. Garud et al., Suddaby, Justesen and Plesner, Lantela and Dion et al. ask the prior question of which notion of time theory should use. What remains open is whether history works as a variable (Brennecke's founding conditions, trajectories and critical events) or as a different kind of time altogether (Garud's Kairos and Aion, Suddaby's 'is' and 'was'). No asker reconciles the two, and none says how the measured history of a tie relates to the narrated history its parties carry.

### O02. What exactly counts as an instance of the field's core constructs (a logic, a paradox, an organization, an institution, an imaginary), and where are their boundaries?

*Kind:* cross-cutting. *Key:* `what_counts`.

**Members** (18 OQs from 11 articles):

- Schildt 2025 (`schildt2025`, theory): OQ-schildt2025-02, OQ-schildt2025-07 (BC)
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-01
- Dion 2025 (`dion2025`, theory): OQ-dion2025-02, OQ-dion2025-04, OQ-dion2025-05, OQ-dion2025-13, OQ-dion2025-14
- Schoeneborn 2026 (`schoeneborn2026`, theory): OQ-schoeneborn2026-10
- Porsfelt 2026 (`porsfelt2026`, theory): OQ-porsfelt2026-01, OQ-porsfelt2026-03
- Georgiou 2023 (`georgiou2023`, review): OQ-georgiou2023-01
- Hawbaker 2025 (`hawbaker2025`, controversies_conversations): OQ-hawbaker2025-03
- Derek Robinson 2025 (`derekrobinson2025`, controversies_conversations): OQ-derekrobinson2025-03 (BC), OQ-derekrobinson2025-07
- Laine 2023 (`laine2023`, theory): OQ-laine2023-02
- Mena 2026 (`mena2026`, theory): OQ-mena2026-02
- Wright 2023 (`wright2023`, theory): OQ-wright2023-04

**Representative quotation** (OQ-schildt2025-02, Schildt 2025): “what exactly counts as a logic?" and "how do we draw the boundaries of an institutional logic?” (p. 16, "Towards a more dynamic and local view")

**Support:** theory/review articles 9; commentary or exchange pieces 2; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 2; most recent ask 2026-09-21.

**Level of analysis:** field (the discipline's concepts) (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** These askers want to know where the edges of the field's working concepts lie. Schildt and Kodeih ask what counts as a logic and how to draw its boundary; Seidemann asks what contradiction, interrelation and persistence signify once paradox is grounded in an ontology; Dion et al. ask 'the organizationality of what?'; Porsfelt et al. ask whether 'imaginaries' enriches the vocabulary at all; Georgiou and Arenas ask whether a community logic exists; the person-institution exchange asks what boundary makes a person-brand an institution; Wright et al. ask how the definition of an extreme context is reshaped by use. The askers disagree on the remedy. Schoeneborn et al. want the field to agree on foundations so that a cumulative programme can form; Dion et al. warn that an umbrella concept conceals incompatible onto-epistemic postures and would rather ask when entities take part in organizing than whether they are organizations; Laine and Kibler ask whether an organization could do nothing at all and still be the same organization. The open question is who settles such boundaries, which joins this conversation to the one on words and standards.

### O03. Which methods can capture what is hidden, absent, sociomaterial or changing in organizing?

*Kind:* cross-cutting. *Key:* `methods_hidden`.

**Members** (18 OQs from 11 articles):

- Orlikowski 2023 (`orlikowski2023`, theory): OQ-orlikowski2023-05, OQ-orlikowski2023-09
- Justesen 2024 (`justesen2024`, theory): OQ-justesen2024-05, OQ-justesen2024-06, OQ-justesen2024-07, OQ-justesen2024-08, OQ-justesen2024-10
- Jørgensen 2023 (`jorgensen2023`, theory): OQ-jorgensen2023-03
- Giovannoni 2025 (`giovannoni2025`, theory): OQ-giovannoni2025-10
- Brennecke 2025 (`brennecke2025`, theory): OQ-brennecke2025-07, OQ-brennecke2025-08, OQ-brennecke2025-16
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-11
- Whyte 2023 (`whyte2023`, theory): OQ-whyte2023-07
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-14
- Räcker 2024 (`racker2024`, theory): OQ-racker2024-03
- Pozner 2023 (`pozner2023`, theory): OQ-pozner2023-08
- Powell 2023 (`powell2023`, essay): OQ-powell2023-11

**Representative quotation** (OQ-justesen2024-06, Justesen 2024): “So, what methods will be appropriate to study work that is out of sight as well as devalued?” (p. 21, "Future research: Some suggestions")

**Support:** theory/review articles 11; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 1; most recent ask 2025-09-28.

**Level of analysis:** multi-level (methodological) (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** Eleven askers want methods for what ordinary designs miss: invisible and devalued work (Justesen and Plesner), corollary effects 'below the water line' (Orlikowski and Scott), atmospheres that are easier to reflect on than to study (Jørgensen and Beyes), absences that should not be filled (Giovannoni and Quattrone), the within-tie variation that static network analysis flattens (Brennecke et al.), foundation models to which researchers lack access (Hinds and von Krogh), and hidden material interactions across devices (Whyte et al.). Pozner and Hannigan and Powell and DiMaggio look to computational text analysis. The disagreement is between capture and restraint: the computational askers want better detection of what is already there, while Giovannoni and Quattrone, and in part Jørgensen and Beyes, want methods that keep the absent absent. Hinds and von Krogh name the hardest practical gap: theory about algorithms may need access to the algorithms, and that access may be refused.

### O04. How does organizing produce, reproduce or reduce exclusion and inequality?

*Kind:* topical. *Key:* `inequality`.

**Members** (21 OQs from 11 articles):

- Arnold 2023 (`arnold2023`, theory): OQ-arnold2023-03, OQ-arnold2023-05, OQ-arnold2023-11
- Sasaki 2024 (`sasaki2024`, theory): OQ-sasaki2024-06
- Langenmayr 2024 (`langenmayr2024`, theory): OQ-langenmayr2024-01, OQ-langenmayr2024-03, OQ-langenmayr2024-04, OQ-langenmayr2024-06, OQ-langenmayr2024-07
- Pavlisa 2026 (`pavlisa2026`, theory): OQ-pavlisa2026-01, OQ-pavlisa2026-02, OQ-pavlisa2026-04 (BC), OQ-pavlisa2026-05, OQ-pavlisa2026-06
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-15
- Whyte 2023 (`whyte2023`, theory): OQ-whyte2023-11
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-10
- Fotaki 2023 (`fotaki2023`, theory): OQ-fotaki2023-03
- Mena 2026 (`mena2026`, theory): OQ-mena2026-04
- Hawbaker 2025 (`hawbaker2025`, controversies_conversations): OQ-hawbaker2025-02 (BC)
- Derek Robinson 2025 (`derekrobinson2025`, controversies_conversations): OQ-derekrobinson2025-13

**Representative quotation** (OQ-langenmayr2024-01, Langenmayr 2024): “Adopting an equity-based approach would thus allow open strategy scholars to explore the relation between traditional actors’ dominance and control over inclusion and the reproduction of inequalities.” (p. 6, "Normalizing through traditional strategy actors’ control over inclusion")

**Support:** theory/review articles 9; commentary or exchange pieces 1.5; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 0; most recent ask 2026-06-19.

**Level of analysis:** organization to society (multi-level) (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers want to know how organizing makes and keeps inequality, and whether the organizational remedies on offer reduce it. Langenmayr et al. ask whether open strategy's control over inclusion reproduces inequality; Pavlisa et al. ask why stakeholder governance fails to reduce societal inequality; Arnold and Costas ask how organizations produce some people as unintelligible 'noise'; Hinds and von Krogh ask whether GenAI's progressive encapsulation includes or excludes marginalized groups; Whyte et al. ask whether hybrid work reproduces inequality; Seidemann asks how paradoxes reflect gender inequities; Mena et al. ask whether DEI measures reduce managerial domination. The two person-institution replies add race, gender, class and geography as conditions on whose mythology travels. The unresolved split is between a business-case reading, in which inclusion is valued for its effect on outcomes, and an equity reading, in which inclusion is judged by what it does for those included (Langenmayr et al.'s contrast). No asker has shown which organizational mechanism actually narrows inequality rather than relabelling it.

### O05. What makes a collective organizational, and how do loose collectives, movements and non-human agents gain, hold or lose organizational actorhood?

*Kind:* cross-cutting. *Key:* `organizationality`.

**Members** (26 OQs from 9 articles):

- Dion 2025 (`dion2025`, theory): OQ-dion2025-03, OQ-dion2025-06, OQ-dion2025-08, OQ-dion2025-09, OQ-dion2025-10, OQ-dion2025-11, OQ-dion2025-12
- Schoeneborn 2026 (`schoeneborn2026`, theory): OQ-schoeneborn2026-01, OQ-schoeneborn2026-03, OQ-schoeneborn2026-05, OQ-schoeneborn2026-07, OQ-schoeneborn2026-08, OQ-schoeneborn2026-09
- Winkler 2025 (`winkler2025`, theory): OQ-winkler2025-01, OQ-winkler2025-04, OQ-winkler2025-05, OQ-winkler2025-06
- Phillips 2024 (`phillips2024`, controversies_conversations): OQ-phillips2024-09
- Stark 2024 (`stark2024`, theory): OQ-stark2024-06, OQ-stark2024-08, OQ-stark2024-09
- Arnold 2023 (`arnold2023`, theory): OQ-arnold2023-04
- Georgiou 2023 (`georgiou2023`, review): OQ-georgiou2023-09
- Laine 2023 (`laine2023`, theory): OQ-laine2023-06 (BC), OQ-laine2023-08
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-09

**Representative quotation** (OQ-schoeneborn2026-03, Schoeneborn 2026): “Our framework then raises follow-up questions, for instance, how loose and fluid social phenomena can sustain their existence despite a rather low degree of organizationality.” (p. 13, "Dynamizing Organizationality")

**Support:** theory/review articles 8; commentary or exchange pieces 1; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 4; most recent ask 2026-09-19.

**Level of analysis:** multi-level (collective actor) (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** This conversation asks what makes a collective organizational, and its askers reply to one another inside the corpus. Schoeneborn et al. treat organizationality as a matter of degree and ask how loose phenomena survive with little of it, why collectives are charged with or discharged of actorhood, and in what temporal patterns. Dion et al. ask how communication's organizing property explains social agents and propose that organizationality may be stronger or weaker by Ahrne and Brunsson's criteria. Winkler and Schoeneborn ask how post-truth communication organizes while attacking the organizations it imitates. Phillips et al. ask how 'artificial persons' change what organizations are; Stark and Vanden Broeck ask whether technology is organizational structure; Hinds and von Krogh ask what a team is under GenAI; Laine and Kibler ask whether any object can be entrepreneurial. The disagreement is explicit: Dion et al. deny that organizationality can serve as an umbrella between entitative and processual views, and Schoeneborn et al. answer by building it into a theory of gradual actorhood. Open across all of them is what evidence would show a collective has crossed into actorhood.

### O06. What place do non-human things (technologies, objects, nature, atmospheres) have as actors in organizing?

*Kind:* cross-cutting. *Key:* `nonhuman`.

**Members** (24 OQs from 9 articles):

- Laine 2023 (`laine2023`, theory): OQ-laine2023-04, OQ-laine2023-05, OQ-laine2023-06 (BC), OQ-laine2023-08
- Orlikowski 2023 (`orlikowski2023`, theory): OQ-orlikowski2023-07
- Friedrich 2026 (`friedrich2026`, theory): OQ-friedrich2026-03, OQ-friedrich2026-04, OQ-friedrich2026-05, OQ-friedrich2026-07, OQ-friedrich2026-08, OQ-friedrich2026-09, OQ-friedrich2026-12, OQ-friedrich2026-14, OQ-friedrich2026-15, OQ-friedrich2026-17
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-05
- Jørgensen 2023 (`jorgensen2023`, theory): OQ-jorgensen2023-04, OQ-jorgensen2023-05, OQ-jorgensen2023-07
- Hsu 2024 (`hsu2024`, controversies_conversations): OQ-hsu2024-06
- Phillips 2024 (`phillips2024`, controversies_conversations): OQ-phillips2024-13, OQ-phillips2024-15
- Patriotta 2025 (`patriotta2025`, theory): OQ-patriotta2025-10
- Whyte 2023 (`whyte2023`, theory): OQ-whyte2023-07

**Representative quotation** (OQ-laine2023-05, Laine 2023): “while it may be customary to think of humans as more suitable to being characterized as entrepreneurial than, for instance, broken pencils, ultimately this distinction needs to be shown rather than assumed.” (p. 19, "OOOT in Action: Sun Ra")

**Support:** theory/review articles 7; commentary or exchange pieces 2; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 3; most recent ask 2026-04-01.

**Level of analysis:** multi-level (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** The askers ask whether things other than people act in organizing, and what theory must change if they do. Laine and Kibler say the distinction between entrepreneurial humans and 'broken pencils' must be shown, not assumed; Friedrich asks how organizing can attend to air, water, minerals, animals and data flows; Jørgensen and Beyes ask how to respond to atmospheres; Seidemann asks what sociomateriality does to paradox; Orlikowski and Scott, Hsu and Bechky and Phillips et al. ask how far digital technology is an actor in its own right; Patriotta et al. ask how legitimacy tests are co-produced by human and technological actors. They disagree on what sort of actor the thing is: an object with real qualities (Laine and Kibler), a more-than-human other owed care (Friedrich), a symbolic participant in category work (Phillips et al.), or one force among others in a relational network (Hsu and Bechky). None of them says how a researcher would tell an actor from an affordance in data.

### O07. What happens to organizational and professional competence and expertise when new knowledge or technology arrives: is it lost, kept or rebuilt?

*Kind:* cross-cutting. *Key:* `competence`.

**Members** (19 OQs from 9 articles):

- Guercini 2023 (`guercini2023`, theory): OQ-guercini2023-04, OQ-guercini2023-05, OQ-guercini2023-06, OQ-guercini2023-07, OQ-guercini2023-08, OQ-guercini2023-09, OQ-guercini2023-10, OQ-guercini2023-11, OQ-guercini2023-12
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-17
- Hsu 2024 (`hsu2024`, controversies_conversations): OQ-hsu2024-08
- Stark 2024 (`stark2024`, theory): OQ-stark2024-02, OQ-stark2024-03
- Corver 2026 (`corver2026`, theory): OQ-corver2026-09, OQ-corver2026-11
- Jackwerth-Rice 2023 (`jackwerthrice2023`, theory): OQ-jackwerthrice2023-08
- Powell 2023 (`powell2023`, essay): OQ-powell2023-10
- Fotaki 2023 (`fotaki2023`, theory): OQ-fotaki2023-06
- Scherer 2023 (`scherer2023`, theory): OQ-scherer2023-06

**Representative quotation** (OQ-hinds2024-17, Hinds 2024): “Or will we see the onset of 'hyper-generalization' in which such specialized tasks are performed by GenAI and are no longer available or visible to organizational members” (p. 11, "Discussion")

**Support:** theory/review articles 8; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-07-28.

**Level of analysis:** organization and profession (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** These askers ask what happens to what organizations and professionals know how to do when something new arrives. Guercini and Lechner propose that acquiring a competence can erode an existing one, and leave open which kinds and timings of competence produce attrition. Hinds and von Krogh ask whether GenAI produces 'hyper-generalization', with specialist tasks no longer visible to members; Hsu and Bechky ask how to keep the expertise needed to question the technology; Stark and Vanden Broeck ask when professionals resist algorithmic incursion and when they compromise; Corver and Filler ask how organizations become good 'tool users'. Powell and DiMaggio, Jackwerth-Rice et al., Fotaki and Scherer and Neesham ask how routines, skills and capabilities such as care or civic maturity are formed and taught. The unanswered question is the mechanism of loss: Guercini and Lechner theorize it as interference between competences, Hinds and von Krogh as encapsulation inside a system. No asker tests either.

### O08. Who decides which words, concepts and standards of good theory a scholarly community uses, and by what procedure?

*Kind:* topical. *Key:* `words_standards`.

**Members** (25 OQs from 9 articles):

- Abend 2024 (`abend2024`, controversies_conversations): OQ-abend2024-02, OQ-abend2024-03, OQ-abend2024-04, OQ-abend2024-05, OQ-abend2024-06, OQ-abend2024-07, OQ-abend2024-08 (BC)
- Prasad 2024 (`prasad2024`, controversies_conversations): OQ-prasad2024-03 (BC), OQ-prasad2024-04 (BC), OQ-prasad2024-06, OQ-prasad2024-07
- Suddaby 2024 (`suddaby2024`, controversies_conversations): OQ-suddaby2024-03 (BC), OQ-suddaby2024-04
- Schoeneborn 2026 (`schoeneborn2026`, theory): OQ-schoeneborn2026-02
- Höllerer 2026 (`hollerer2026`, editorial): OQ-hollerer2026-01, OQ-hollerer2026-02, OQ-hollerer2026-03, OQ-hollerer2026-04, OQ-hollerer2026-06
- Giovannoni 2025 (`giovannoni2025`, theory): OQ-giovannoni2025-06, OQ-giovannoni2025-07
- Ernst 2026 (`ernst2026`, theory): OQ-ernst2026-03, OQ-ernst2026-06
- Gümüsay 2024 (`gumusay2024`, theory): OQ-gumusay2024-11
- Powell 2023 (`powell2023`, essay): OQ-powell2023-14

**Representative quotation** (OQ-abend2024-02, Abend 2024): “In both cases, word ‘w’ and distinction d, adjudicating a dispute necessitates secondorder criteria: what makes a good proposal good, goodness according to which principles and aims, and who gets to establish these.” (p. 4, "3. What’s At Stake")

**Support:** theory/review articles 5; commentary or exchange pieces 3; editorial signal y; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 7; most recent ask 2026-09-19.

**Level of analysis:** field (scholarly community) (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** The journal's editors join this conversation in Höllerer et al.'s editorial, and two authors address editors directly. Abend asks who should decide a community's key words and distinctions, by which second-order criteria, and at whose cost, and he answers with democratic deliberation. Prasad asks how such deliberation would begin or bind anyone, and offers problem-solving communities instead; Suddaby argues the call is not new and asks for theory that is (syncretic, combining objective and normative views). Schoeneborn et al. want agreed foundations for organizationality; Ernst et al. ask how orthodoxies define good theory and call on editors and reviewers to counteract field biases; Giovannoni and Quattrone say editors, reviewers and readers would have to accept work that refuses to name its 'thing'. Höllerer et al.'s editorial invites proposals that 'push beyond the boundaries' of convention, while also requiring contributions to be signalled against existing literature. The open disagreement is the procedure. Abend's is deliberative, Prasad's is problem-led, Suddaby's is the field's long swing between grand theory and empiricism, and the editorial position is curated exchange. None of them says who counts as a member of the deciding community, a point Abend himself leaves as 'a can of worms'.

### O09. How do organizations act, and how does organizing itself change, amid polarization, post-truth politics and democratic backsliding?

*Kind:* topical. *Key:* `polarization`.

**Members** (13 OQs from 8 articles):

- Winkler 2025 (`winkler2025`, theory): OQ-winkler2025-01, OQ-winkler2025-02, OQ-winkler2025-03 (BC), OQ-winkler2025-07
- Mena 2026 (`mena2026`, theory): OQ-mena2026-14, OQ-mena2026-17, OQ-mena2026-21
- Werner 2026 (`werner2026`, theory): OQ-werner2026-01
- Patriotta 2025 (`patriotta2025`, theory): OQ-patriotta2025-04
- Giovannoni 2025 (`giovannoni2025`, theory): OQ-giovannoni2025-08
- Ernst 2026 (`ernst2026`, theory): OQ-ernst2026-07
- du Gay 2024 (`dugay2024`, theory): OQ-dugay2024-06
- Pozner 2023 (`pozner2023`, theory): OQ-pozner2023-16

**Representative quotation** (OQ-mena2026-17, Mena 2026): “future research could examine how organizations can strengthen civic engagement and solidarity in contexts that are not fully democratic, in which democratic backsliding is occurring, or where the regime is hybrid or altogether nondemocratic” (p. 15, "Republican inside-out focus")

**Support:** theory/review articles 8; commentary or exchange pieces 0; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 1; most recent ask 2026-04-07.

**Level of analysis:** organization in society (multi-level) (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** These askers want to know how organizations act when the political ground under them shifts. Winkler and Schoeneborn ask how post-truth communication organizes itself and how established organizations can de-escalate it; Mena et al. ask how right-wing tendencies and democratic backsliding shape democracy inside organizations; Werner et al. ask why some firms hold to ESG and DEI commitments under political attack; Patriotta et al. offer legitimacy tests as a tool for polarized environments; Giovannoni and Quattrone ask about rhetoric as 'irrationality and nonlogic' under autocrats; Ernst et al. ask whether inquiry can be divorced from geopolitical crisis; du Gay and Lopdrup Hjorth ask whether anti-formal reforms have weakened state capacity. The askers differ on direction: most ask how the political environment acts on organizations, while Mena et al. and Winkler and Schoeneborn also ask how organizations act back on it. All of the asks fall in 2024-2026, and none is yet answered empirically.

### O10. How do emotions and affect drive organizing, entrepreneurship and mobilization?

*Kind:* cross-cutting. *Key:* `emotion`.

**Members** (12 OQs from 8 articles):

- Bacq 2023 (`bacq2023`, theory): OQ-bacq2023-03, OQ-bacq2023-04, OQ-bacq2023-05, OQ-bacq2023-06
- Arnold 2023 (`arnold2023`, theory): OQ-arnold2023-07, OQ-arnold2023-10
- Ocasio 2023 (`ocasio2023`, theory): OQ-ocasio2023-01
- Leitzinger 2023 (`leitzinger2023`, review): OQ-leitzinger2023-02
- Friedrich 2026 (`friedrich2026`, theory): OQ-friedrich2026-07
- Jørgensen 2023 (`jorgensen2023`, theory): OQ-jorgensen2023-05
- Pozner 2023 (`pozner2023`, theory): OQ-pozner2023-12
- Paca 2024 (`paca2024`, theory): OQ-paca2024-05

**Representative quotation** (OQ-bacq2023-03, Bacq 2023): “Future research could also explore how other negative emotions (e.g., guilt or pity, instead of shame) might have an energizing impact on entrepreneurship” (p. 16, "Stigma, shame, and entrepreneurship: The promise for social change")

**Support:** theory/review articles 8; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-04-01.

**Level of analysis:** individual and interaction (modal OQ level: individual).

**What remains unanswered, and where the askers disagree.** The askers ask how emotion and affect move organizing. Bacq et al. ask whether guilt or pity energizes entrepreneurship as shame does, and whether shame leads to replicating existing business models; Arnold and Costas ask how affect and discourse clash in struggles over who is heard; Leitzinger and Waeger ask when emotions change mobilization; Pozner and Hannigan ask how frames activate values; Friedrich asks how affective ties to life forces can be cultivated; Jørgensen and Beyes ask about the politics of atmosphere; Paca and Rozuel ask about members' psychic needs. Ocasio flags values and emotions as under-treated in his own cross-level theory. The open question is level: some askers treat emotion as individual experience (Bacq et al.), others as an affective order that precedes subjects (Arnold and Costas, Jørgensen and Beyes). Nobody connects the two.

### O11. How do scholars' own selves, careers and positions enter their theorizing, and how should they reflect on that?

*Kind:* topical. *Key:* `reflexivity`.

**Members** (18 OQs from 7 articles):

- Petriglieri 2023 (`petriglieri2023`, essay): OQ-petriglieri2023-01, OQ-petriglieri2023-02, OQ-petriglieri2023-04 (BC), OQ-petriglieri2023-05
- Wright 2023 (`wright2023`, theory): OQ-wright2023-01, OQ-wright2023-02, OQ-wright2023-03, OQ-wright2023-05, OQ-wright2023-06
- Ernst 2026 (`ernst2026`, theory): OQ-ernst2026-01, OQ-ernst2026-02, OQ-ernst2026-04, OQ-ernst2026-05, OQ-ernst2026-08
- Keller 2025 (`keller2025`, theory): OQ-keller2025-01
- Lantela 2024 (`lantela2024`, theory): OQ-lantela2024-10
- Jørgensen 2023 (`jorgensen2023`, theory): OQ-jorgensen2023-06
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-03

**Representative quotation** (OQ-wright2023-06, Wright 2023): “We invite future research to draw on our theoretical framework and explore how, when, where and for whom a meaningful sense of self operates in research in extreme as well as non-extreme contexts.” (p. 20, "Discussion")

**Support:** theory/review articles 7; commentary or exchange pieces 0; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 1; most recent ask 2026-04-07.

**Level of analysis:** individual (the scholar) (modal OQ level: individual).

**What remains unanswered, and where the askers disagree.** These askers turn the field's questions on the scholar. Petriglieri and Ashford ask for new chronicles of academic working lives and for what productivity stands in for; Wright et al. ask how a researcher's self operates in theorizing, whether selves can switch, and what restricting one's modes of engagement does to a career; Ernst et al. ask how reflexivity relates to theorizing and what a researcher owes the field; Keller et al. ask how paradox applies to scholars' own work; Lantela asks about the researcher's embodied position; Seidemann asks how researcher involvement matters in action research. They disagree on what reflexivity is for. For Ernst et al. it is epistemic, a break with pre-constructed objects; for Petriglieri and Ashford it is existential; for Wright et al. it is a resource for theorizing. Petriglieri and Ashford also bound their own claim: the parallels are not true of every academic.

### O12. How can organization theory theorize what does not yet exist or cannot be known (futures, possibilities, absences) with rigour?

*Kind:* topical. *Key:* `theorize_future`.

**Members** (17 OQs from 7 articles):

- Gümüsay 2024 (`gumusay2024`, theory): OQ-gumusay2024-01, OQ-gumusay2024-06, OQ-gumusay2024-07, OQ-gumusay2024-08, OQ-gumusay2024-09, OQ-gumusay2024-12
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-24
- Lantela 2024 (`lantela2024`, theory): OQ-lantela2024-08
- Giovannoni 2025 (`giovannoni2025`, theory): OQ-giovannoni2025-01, OQ-giovannoni2025-02, OQ-giovannoni2025-03, OQ-giovannoni2025-04, OQ-giovannoni2025-09
- Laine 2023 (`laine2023`, theory): OQ-laine2023-07, OQ-laine2023-09
- Friedrich 2026 (`friedrich2026`, theory): OQ-friedrich2026-02
- Suddaby 2024 (`suddaby2024`, controversies_conversations): OQ-suddaby2024-01

**Representative quotation** (OQ-giovannoni2025-01, Giovannoni 2025): “But what does it mean to develop a theory that places unknowability at the heart of theorizing, effectively moving away from an epistemological problem of knowledge towards a pragmatic concern with individual and collective action?” (p. 3, "Introduction")

**Support:** theory/review articles 6; commentary or exchange pieces 1; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 5; most recent ask 2026-04-01.

**Level of analysis:** field (scholarly practice) (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** This conversation asks how theory can reach beyond the empirical past. Gümüsay and Reinecke ask how prospective theorizing can be rigorous, and who besides scholars judges what is desirable; Hinds and von Krogh want 'speculative vigor' for a technology that moves faster than studies; Lantela proposes microhistory for theorizing 'what does not exist'; Laine and Kibler plead for aesthetics-driven theory; Friedrich offers imaginative questions as co-creation. Giovannoni and Quattrone ask what theory would look like if its 'substances' (values, ends, purpose) are unknowable. Suddaby wants 'is' and 'was' in theoretical frames. The disagreement is over knowledge itself. Gümüsay and Reinecke seek criteria of speculative rigour, while Giovannoni and Quattrone call for theory that keeps the unknowable unknown rather than making it present. No one has yet said how a speculative theory would be judged wrong.

### O13. Who is answerable when decisions are made by algorithms, platforms or loosely bounded collectives rather than by an identifiable office-holder?

*Kind:* cross-cutting. *Key:* `accountability`.

**Members** (9 OQs from 7 articles):

- Stark 2024 (`stark2024`, theory): OQ-stark2024-04
- Schoeneborn 2026 (`schoeneborn2026`, theory): OQ-schoeneborn2026-04, OQ-schoeneborn2026-06
- Mena 2026 (`mena2026`, theory): OQ-mena2026-03, OQ-mena2026-15
- Scherer 2023 (`scherer2023`, theory): OQ-scherer2023-07
- Pavlisa 2026 (`pavlisa2026`, theory): OQ-pavlisa2026-03
- Jaser 2024 (`jaser2024`, theory): OQ-jaser2024-03
- Friedrich 2026 (`friedrich2026`, theory): OQ-friedrich2026-17

**Representative quotation** (OQ-stark2024-04, Stark 2024): “But who or what is accountable when an algorithm exercises decisions that occur faster and with a vastly larger number of inputs than a human can physiologically comprehend and react to (Vesa & Tienari, 2022, p. 1137)?” (p. 14, "Accountability")

**Support:** theory/review articles 7; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-09-19.

**Level of analysis:** multi-level (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** The askers ask who answers when no one is plainly in charge. Stark and Vanden Broeck ask who or what is accountable when an algorithm decides faster than a person can follow; Schoeneborn et al. ask what charging and discharging collectives with actorhood implies for individual as against collective responsibility, and why actors do it; Mena et al. ask about transparency and accountability in organizational democracy and how organizations can engage more transparently in democratic processes; Scherer and Neesham call for strict regulation of LLM applications; Pavlisa et al. note that stakeholder governance lacks criteria for which stakeholders fall outside a firm's responsibility; Jaser and Tourish ask whose interests surveillance serves; Friedrich asks for scrutiny of power-laden technology. They agree on the gap and differ on the locus: the algorithm (Stark and Vanden Broeck), the attribution practice (Schoeneborn et al.), or law (Scherer and Neesham). None proposes how responsibility would be traced across all three.

### O14. What are the failures and dark sides of organizing practices that the field usually treats as good?

*Kind:* cross-cutting. *Key:* `dark_side`.

**Members** (7 OQs from 7 articles):

- Jørgensen 2023 (`jorgensen2023`, theory): OQ-jorgensen2023-04
- Krautzberger 2024 (`krautzberger2024`, theory): OQ-krautzberger2024-12
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-11
- Sasaki 2024 (`sasaki2024`, theory): OQ-sasaki2024-06
- Winkler 2025 (`winkler2025`, theory): OQ-winkler2025-06
- Gümüsay 2024 (`gumusay2024`, theory): OQ-gumusay2024-09
- Leitzinger 2023 (`leitzinger2023`, review): OQ-leitzinger2023-20

**Representative quotation** (OQ-seidemann2024-11, Seidemann 2024): “I recommend that paradox scholars empirically explore the boundary conditions of both/and for different classes of phenomena at different levels of analysis and the potential negative ramifications of embracing tensions.” (p. 18, "Developing a more granular perspective")

**Support:** theory/review articles 7; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 0; most recent ask 2025-11-11.

**Level of analysis:** organization and multi-level (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** These askers say the field studies the bright side of its favourite constructs and ask about the other side. Jørgensen and Beyes call the dark side of atmospheres a lacuna; Krautzberger and Tuckermann ask about failures of a meta-both/and approach; Seidemann asks about the negative ramifications of embracing tensions; Sasaki and Baba ask about organizations' role in eradicating cultures under rising authoritarianism; Winkler and Schoeneborn extend dis/organization to terrorism, hacktivism and misconduct; Gümüsay and Reinecke see value in theorizing undesirable futures; Leitzinger and Waeger ask whether mission drift can be productive. The askers share a diagnosis of affirmative bias but not a programme: some want failure cases (Krautzberger and Tuckermann), others a politics (Jørgensen and Beyes). How a dark side would be recognized before the harm is done remains open.

### O15. What slow, indirect effects do digital technologies have on institutions, work and society beyond their visible uses?

*Kind:* topical. *Key:* `undertow`.

**Members** (12 OQs from 7 articles):

- Orlikowski 2023 (`orlikowski2023`, theory): OQ-orlikowski2023-01, OQ-orlikowski2023-02, OQ-orlikowski2023-06, OQ-orlikowski2023-09
- Hsu 2024 (`hsu2024`, controversies_conversations): OQ-hsu2024-04, OQ-hsu2024-05
- Phillips 2024 (`phillips2024`, controversies_conversations): OQ-phillips2024-05, OQ-phillips2024-06
- Scherer 2023 (`scherer2023`, theory): OQ-scherer2023-05
- Justesen 2024 (`justesen2024`, theory): OQ-justesen2024-12
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-12
- Garud 2025 (`garud2025`, theory): OQ-garud2025-10

**Representative quotation** (OQ-orlikowski2023-02, Orlikowski 2023): “So, there is little attention focused on the undertow, and thus limited knowledge of the corollary effects that are being generated by digitalization or their consequences.” (p. 5, "The Digital Undertow")

**Support:** theory/review articles 5; commentary or exchange pieces 2; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 4; most recent ask 2025-07-11.

**Level of analysis:** field and institution (multi-level) (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** The askers ask what digital technology does to institutions slowly and indirectly. Orlikowski and Scott ask about corollary effects distant from the visible programme of digital change, and about other industry-structuring mechanisms that may be displaced; Hsu and Bechky ask how to trace the vectors of successive waves of change; Phillips et al. ask what passive use of GenAI does to categorization; Scherer and Neesham ask about reductionism induced by technology; Justesen and Plesner ask what digitalization does to employment relations; Hinds and von Krogh ask what forces accelerate or arrest encapsulation. Inside the GenAI exchange the askers disagree: Phillips et al. treat GenAI as different in kind, while Hsu and Bechky place it in a long line of category-restructuring technologies whose main effects are gradual. Neither side has data over a span long enough to tell.

### O16. How do new institutions and organizational forms emerge, take root or displace old ones, and what makes a field ready for them?

*Kind:* topical. *Key:* `inst_emerge`.

**Members** (22 OQs from 7 articles):

- Powell 2023 (`powell2023`, essay): OQ-powell2023-05, OQ-powell2023-06, OQ-powell2023-09, OQ-powell2023-12, OQ-powell2023-13
- Jackwerth-Rice 2023 (`jackwerthrice2023`, theory): OQ-jackwerthrice2023-02, OQ-jackwerthrice2023-03, OQ-jackwerthrice2023-04, OQ-jackwerthrice2023-05, OQ-jackwerthrice2023-06, OQ-jackwerthrice2023-07, OQ-jackwerthrice2023-09, OQ-jackwerthrice2023-11
- Ocasio 2023 (`ocasio2023`, theory): OQ-ocasio2023-01, OQ-ocasio2023-02 (BC), OQ-ocasio2023-03
- Wedlin 2025 (`wedlin2025`, theory): OQ-wedlin2025-03, OQ-wedlin2025-04
- Nigam 2025 (`nigam2025`, controversies_conversations): OQ-nigam2025-05, OQ-nigam2025-10
- Schildt 2025 (`schildt2025`, theory): OQ-schildt2025-03
- Orlikowski 2023 (`orlikowski2023`, theory): OQ-orlikowski2023-01

**Representative quotation** (OQ-powell2023-09, Powell 2023): “How do new ideas and practices enter organizations and stick? Why do new kinds of institutions emerge, take root, and persist? When are organizations more vulnerable to changes in the wider environment and when are they resisted?” (p. 15, "Institutional change")

**Support:** theory/review articles 6; commentary or exchange pieces 1; editorial signal n; distinct volumes 2 (4, 6); citation edges among askers 1; most recent ask 2025-12-23.

**Level of analysis:** field (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** The askers ask how new institutions and forms appear, take hold or displace older ones. Powell and DiMaggio ask how new ideas enter organizations and stick, why some social worlds are more 'poised' for novelty, how thresholds make a practice mandatory, and how meso-level resources help or thwart individual organizers; Jackwerth-Rice et al. ask whether changing institutions is easier than building them, whether imported resources are as valuable as local ones, and whether resource sufficiency can be known in advance; Ocasio asks about the functional origins of institutions; Wedlin and Weinryb ask how hype disrupts institutional orders; Nigam et al. ask whether persons become institutions in unsettled times; Schildt and Kodeih ask how macro-level logics arise from local processes. The askers disagree about agency: Powell and DiMaggio warn that work on change agents makes them too 'muscular', while Jackwerth-Rice et al. build a resource account of institutional entrepreneurs. Neither says how to tell an entrepreneur's success from a field's readiness.

### O17. How do marginalized and excluded people gain a speaking position, a voice or cultural autonomy?

*Kind:* topical. *Key:* `voice_margins`.

**Members** (20 OQs from 7 articles):

- Arnold 2023 (`arnold2023`, theory): OQ-arnold2023-02, OQ-arnold2023-04, OQ-arnold2023-06, OQ-arnold2023-07, OQ-arnold2023-08, OQ-arnold2023-10, OQ-arnold2023-12, OQ-arnold2023-13
- Sasaki 2024 (`sasaki2024`, theory): OQ-sasaki2024-01, OQ-sasaki2024-02, OQ-sasaki2024-03, OQ-sasaki2024-04, OQ-sasaki2024-05
- Lantela 2024 (`lantela2024`, theory): OQ-lantela2024-06 (BC)
- Langenmayr 2024 (`langenmayr2024`, theory): OQ-langenmayr2024-02, OQ-langenmayr2024-05, OQ-langenmayr2024-11
- Bacq 2023 (`bacq2023`, theory): OQ-bacq2023-10
- Fotaki 2023 (`fotaki2023`, theory): OQ-fotaki2023-04
- Leitzinger 2023 (`leitzinger2023`, review): OQ-leitzinger2023-31

**Representative quotation** (OQ-arnold2023-06, Arnold 2023): “we call for future research to look at the struggles of subjects to acquire a speaking position to begin with.” (p. 16, "Implications for future research")

**Support:** theory/review articles 6.5; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 5); citation edges among askers 1; most recent ask 2024-09-18.

**Level of analysis:** interaction and field (modal OQ level: interaction).

**What remains unanswered, and where the askers disagree.** These askers ask how people who are excluded come to be heard. Arnold and Costas ask about the struggle to gain a speaking position at all, practices that produce or unsettle otherness, and enacted forms of equality; Sasaki and Baba ask how marginalized groups survive culturally and gain autonomy, through what means of resistance, and with what internal effects; Langenmayr et al. ask how newly included strategy actors could contribute on their own terms; Lantela treats the subjugated as an open, situated question; Bacq et al., Fotaki and Leitzinger and Waeger call for research on the underdog, the deprived and non-Western movements. The live disagreement is Arnold and Costas's claim that the struggle is over subjectivity, not identity, which runs against identity-based work on equality. None of the askers says what organizational form keeps a newly gained voice from being re-silenced.

### O18. Who counts as a member (of a community, a demos, an organization, a stakeholder set), and who decides?

*Kind:* cross-cutting. *Key:* `membership`.

**Members** (6 OQs from 6 articles):

- Abend 2024 (`abend2024`, controversies_conversations): OQ-abend2024-07
- Mena 2026 (`mena2026`, theory): OQ-mena2026-01
- Schoeneborn 2026 (`schoeneborn2026`, theory): OQ-schoeneborn2026-08
- Derek Robinson 2025 (`derekrobinson2025`, controversies_conversations): OQ-derekrobinson2025-04
- Pavlisa 2026 (`pavlisa2026`, theory): OQ-pavlisa2026-03
- Georgiou 2023 (`georgiou2023`, review): OQ-georgiou2023-11

**Representative quotation** (OQ-mena2026-01, Mena 2026): “who qualifies as the people (or demos; Koenig-Archibugi, 2022): employees, a larger set of organizational members and/or stakeholders, or a broader demos?” (p. 3, introduction)

**Support:** theory/review articles 4; commentary or exchange pieces 2; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 0; most recent ask 2026-09-19.

**Level of analysis:** organization and community (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** Six askers, writing on different topics, stop at the same question: who is inside? Abend leaves 'who's a community member, how to decide who's a community member' as a can of worms; Mena et al. ask whether the demos is employees, members, stakeholders or a broader public; Schoeneborn et al. ask whether attributing membership charges a collective differently from attributing contributorship; Derek Robinson and Atanasova ask how fan-community membership is enacted; Pavlisa et al. note that stakeholder theory lacks criteria for who is beyond a firm's responsibility; Georgiou and Arenas ask what practices preserve a community's common boundary. No asker answers it, and the answers would differ in kind: a political choice (Abend, Mena et al.), a communicative attribution (Schoeneborn et al.) or a boundary practice (Georgiou and Arenas).

### O19. How do organizations and their members imagine and enact futures, and how is imagination practised together?

*Kind:* topical. *Key:* `org_futures`.

**Members** (20 OQs from 6 articles):

- Gümüsay 2024 (`gumusay2024`, theory): OQ-gumusay2024-02, OQ-gumusay2024-03, OQ-gumusay2024-05, OQ-gumusay2024-10
- Skade 2025 (`skade2025`, theory): OQ-skade2025-01, OQ-skade2025-02, OQ-skade2025-03, OQ-skade2025-04, OQ-skade2025-05, OQ-skade2025-07 (BC)
- Friedrich 2026 (`friedrich2026`, theory): OQ-friedrich2026-11
- Corver 2026 (`corver2026`, theory): OQ-corver2026-06
- Porsfelt 2026 (`porsfelt2026`, theory): OQ-porsfelt2026-02, OQ-porsfelt2026-04, OQ-porsfelt2026-05, OQ-porsfelt2026-06, OQ-porsfelt2026-07, OQ-porsfelt2026-08, OQ-porsfelt2026-09
- Garud 2025 (`garud2025`, theory): OQ-garud2025-03

**Representative quotation** (OQ-porsfelt2026-07, Porsfelt 2026): “For organisation studies, this raises questions about how such moments are triggered, how they draw on and reconfigure existing images and cultural resources, and how they can be consequential without forming durable meaning structures.” (p. 24, "Moving Forward")

**Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (5, 6, 7); citation edges among askers 3; most recent ask 2026-09-21.

**Level of analysis:** organization and interaction (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask how organizations and their members imagine and act toward futures. Skade asks how divergent futures inform strategy, which future-making practices exist, and what utopias and dystopias mean for organizations; Gümüsay and Reinecke ask how climate pathways would affect organizing and how present-day prefigurative settings work; Friedrich asks how meetings can invite collective imagination; Corver and Filler ask whether organizations move from discrete to interconnected sustainability problems; Porsfelt et al. ask how shared moments of imagination are triggered and coordinated, and whether imagination should be studied apart from creativity. The disagreement is Porsfelt et al.'s: they want imagination extracted from its conflation with creative or productive ends, whereas Skade and Gümüsay and Reinecke tie it to strategy and desirable futures. How imagined futures bind present decisions is not yet shown.

### O20. Should organization scholars act as critics or activists in the struggles they study, and what does inquiry owe to its political moment?

*Kind:* cross-cutting. *Key:* `scholar_activism`.

**Members** (6 OQs from 6 articles):

- Langenmayr 2024 (`langenmayr2024`, theory): OQ-langenmayr2024-09
- Fotaki 2023 (`fotaki2023`, theory): OQ-fotaki2023-04
- Ernst 2026 (`ernst2026`, theory): OQ-ernst2026-07
- Prasad 2024 (`prasad2024`, controversies_conversations): OQ-prasad2024-07
- Orlikowski 2023 (`orlikowski2023`, theory): OQ-orlikowski2023-08
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-09

**Representative quotation** (OQ-ernst2026-07, Ernst 2026): “Can we afford to divorce inquiry in academia from crisis at the political and geopolitical levels or from economic forces?” (pp. 16-17, "Conclusions")

**Support:** theory/review articles 5; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-04-07.

**Level of analysis:** field (scholarly community) (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** This conversation asks whether organization scholars should take sides. Langenmayr et al. suggest open strategy scholars act as critics or activists; Fotaki calls scholars to academic activism on the distribution of care; Ernst et al. ask whether inquiry can be divorced from political and economic crisis; Prasad invites scholars to problem-solving research that 'tries to change the world'; Orlikowski and Scott make ethical inquiry into constitutive exclusions part of the agenda; Seidemann asks the paradox community to examine the normative quality of responses. The askers agree that neutrality is not available; they differ on the vehicle (critique, activism, problem-solving communities, ethics within research). Suddaby, in the same exchange as Prasad, wants syncretic knowledge that combines objective and normative worldviews, and is wary of a hyper-pragmatic science.

### O21. How do collective, organizational and personal identities form, and how do they shape what actors do?

*Kind:* cross-cutting. *Key:* `identity`.

**Members** (11 OQs from 6 articles):

- Bacq 2023 (`bacq2023`, theory): OQ-bacq2023-07 (BC), OQ-bacq2023-08, OQ-bacq2023-09
- Godart 2024 (`godart2024`, theory): OQ-godart2024-04, OQ-godart2024-06
- Wright 2023 (`wright2023`, theory): OQ-wright2023-05, OQ-wright2023-06
- Werner 2026 (`werner2026`, theory): OQ-werner2026-02, OQ-werner2026-06
- Petriglieri 2023 (`petriglieri2023`, essay): OQ-petriglieri2023-02
- Arnold 2023 (`arnold2023`, theory): OQ-arnold2023-12

**Representative quotation** (OQ-werner2026-02, Werner 2026): “How is organizational character constituted, what might be variations in types of organizational characters, and under what conditions and how might organizations evolve their character over time?” (p. 2, "Introduction")

**Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-04-01.

**Level of analysis:** individual and organization (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask how identities form and what they make actors do. Bacq et al. ask how collective identity shapes founder identity and how entrepreneurs escape victimization or resilience narratives; Godart and Wittman ask about the identity work in adhering to a logic, at organizational level; Wright et al. ask how pliable a researcher's self-concept is; Werner et al. ask how organizational character is constituted and changes; Petriglieri and Ashford ask how a field mirrors its researchers' selves. Arnold and Costas dissent: the struggle they describe is over subjectivity, not identity. Open between them is whether organizations have identities or characters in the sense persons do, which Werner et al. assert and others leave aside.

### O22. Does generative AI take part in constructing categories, legitimacy and other social objects, and how should theory treat technology as an actor in that construction?

*Kind:* topical. *Key:* `ai_construct`.

**Members** (19 OQs from 6 articles):

- Phillips 2024 (`phillips2024`, controversies_conversations): OQ-phillips2024-08, OQ-phillips2024-10, OQ-phillips2024-11, OQ-phillips2024-12, OQ-phillips2024-13, OQ-phillips2024-14, OQ-phillips2024-15, OQ-phillips2024-16 (BC)
- Grodal 2024 (`grodal2024`, controversies_conversations): OQ-grodal2024-03, OQ-grodal2024-04, OQ-grodal2024-05, OQ-grodal2024-08, OQ-grodal2024-09
- Hsu 2024 (`hsu2024`, controversies_conversations): OQ-hsu2024-06
- Patriotta 2025 (`patriotta2025`, theory): OQ-patriotta2025-10
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-01, OQ-hinds2024-02, OQ-hinds2024-23
- Orlikowski 2023 (`orlikowski2023`, theory): OQ-orlikowski2023-07

**Representative quotation** (OQ-phillips2024-08, Phillips 2024): “much work remains to be done to understand how engaging with generative AI affects human interaction and therefore affects category construction and category work at these different levels of analysis.” (p. 11, "The implications of generative AI in organizations")

**Support:** theory/review articles 3; commentary or exchange pieces 3; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 7; most recent ask 2025-11.

**Level of analysis:** multi-level (category and institution) (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** This conversation is the core of the 5(3) exchange. Phillips et al. ask how engaging with GenAI affects category construction across levels, and call for a 'symbolic turn' that takes technology seriously; Grodal et al. ask whether perceived crossing of the human-machine boundary generates attention, when customers accept it, and whether we will come to see GenAI as a machine; Hsu and Bechky ask for technology to be treated as one force in the relational network that constructs categories; Hinds and von Krogh ask for process theory of how GenAI absorbs relations and functions; Patriotta et al. ask how legitimacy tests are co-produced by technological actors. The disagreement is whether GenAI is new in kind (Phillips et al.) or one more technology that shapes categories (Grodal et al., Hsu and Bechky). Phillips et al. concede the target is moving, and they leave GenAI's part in constructing other social-symbolic objects 'for another time'.

### O23. What makes an organization hold to its values under pressure, and how should its moral conduct be judged?

*Kind:* topical. *Key:* `moral_character`.

**Members** (17 OQs from 6 articles):

- Werner 2026 (`werner2026`, theory): OQ-werner2026-01, OQ-werner2026-02, OQ-werner2026-03, OQ-werner2026-04, OQ-werner2026-05, OQ-werner2026-06, OQ-werner2026-07 (BC), OQ-werner2026-08, OQ-werner2026-09, OQ-werner2026-10
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-08, OQ-seidemann2024-09
- Kalkman 2026 (`kalkman2026`, theory): OQ-kalkman2026-01, OQ-kalkman2026-03
- Godart 2024 (`godart2024`, theory): OQ-godart2024-02
- Patriotta 2025 (`patriotta2025`, theory): OQ-patriotta2025-12 (BC)
- Jaser 2024 (`jaser2024`, theory): OQ-jaser2024-04

**Representative quotation** (OQ-werner2026-01, Werner 2026): “raising not only the question of what might explain such differences in response, but also more specifically, what drives an organization to be unwavering in the face of political pressures?” (p. 2, "Introduction")

**Support:** theory/review articles 5.5; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (5, 6, 7); citation edges among askers 1; most recent ask 2026-07-21.

**Level of analysis:** organization (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask what keeps organizations to their values and how their conduct should be judged. Werner et al. ask what drives an organization to stay unwavering under political pressure, how character is constituted and changes, whether a 'calling' exists, and how deliberation beyond prescribed norms can be ethically judged; Seidemann asks how responses to paradox are evaluated normatively; Kalkman invites other normative accounts of crisis management and asks what triggers moral self-reflection; Godart and Wittman ask how purity in intention relates to purity in action; Jaser and Tourish ask what kind of managers and workers people want to be. Patriotta et al. bound their own theory: settlement fails if values are incommensurable. The askers differ on the source of steadiness. Werner et al. place it in character, Godart and Wittman in identity work. Empirical work on how values survive pressure has not yet been done.

### O24. How do social movements and collective action form, shape markets and organizations, and what becomes of them after success or cooptation?

*Kind:* topical. *Key:* `movements`.

**Members** (32 OQs from 6 articles):

- Leitzinger 2023 (`leitzinger2023`, review): OQ-leitzinger2023-01, OQ-leitzinger2023-03, OQ-leitzinger2023-04, OQ-leitzinger2023-05, OQ-leitzinger2023-06, OQ-leitzinger2023-07, OQ-leitzinger2023-08, OQ-leitzinger2023-11, OQ-leitzinger2023-12, OQ-leitzinger2023-13, OQ-leitzinger2023-14, OQ-leitzinger2023-15, OQ-leitzinger2023-16, OQ-leitzinger2023-17, OQ-leitzinger2023-18, OQ-leitzinger2023-19, OQ-leitzinger2023-21, OQ-leitzinger2023-22, OQ-leitzinger2023-23, OQ-leitzinger2023-24, OQ-leitzinger2023-25, OQ-leitzinger2023-26, OQ-leitzinger2023-28, OQ-leitzinger2023-29, OQ-leitzinger2023-30, OQ-leitzinger2023-32 (BC), OQ-leitzinger2023-33
- Bacq 2023 (`bacq2023`, theory): OQ-bacq2023-01
- Pozner 2023 (`pozner2023`, theory): OQ-pozner2023-10
- Jaser 2024 (`jaser2024`, theory): OQ-jaser2024-07
- Scherer 2023 (`scherer2023`, theory): OQ-scherer2023-10 (BC)
- Mena 2026 (`mena2026`, theory): OQ-mena2026-19

**Representative quotation** (OQ-leitzinger2023-01, Leitzinger 2023): “Key questions remain as to how social movements that target markets and their actors form or, if already established, become mobilized to address new issues.” (p. 7, "Phase 1: Emergence")

**Support:** theory/review articles 5.5; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-03-31.

**Level of analysis:** field (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** Leitzinger and Waeger carry most of this conversation's questions. They ask how market-oriented movements form, which events spur them, when spin-offs start, whether cooptation is inevitable, what outcomes matter for movements themselves, and whether movements fade as markets mature. Bacq et al. ask when entrepreneurial processes give rise to collective action; Pozner and Hannigan ask about scandal as an instrument of social movements; Jaser and Tourish say resistance to surveillance needs more than individual resistance, forums, exit or unions; Scherer and Neesham note that organized citizens' struggle is harder where states are not rule-of-law democracies; Mena et al. ask how organizations challenge hegemony through CEO activism. Unanswered across the askers is who the movement is when firms, CEOs and entrepreneurs act like movements. The support here is narrower than the number of OQs suggests, since one review supplies 27 of the 32.

### O25. How do law, regulation and the state shape organizations, and can they restrain new technologies?

*Kind:* topical. *Key:* `law_state`.

**Members** (12 OQs from 5 articles):

- Mutch 2025 (`mutch2025`, theory): OQ-mutch2025-01, OQ-mutch2025-02, OQ-mutch2025-03, OQ-mutch2025-06
- du Gay 2024 (`dugay2024`, theory): OQ-dugay2024-04, OQ-dugay2024-06, OQ-dugay2024-07
- Mena 2026 (`mena2026`, theory): OQ-mena2026-09, OQ-mena2026-10
- Scherer 2023 (`scherer2023`, theory): OQ-scherer2023-07, OQ-scherer2023-10 (BC)
- Jaser 2024 (`jaser2024`, theory): OQ-jaser2024-06

**Representative quotation** (OQ-mutch2025-06, Mutch 2025): “This article has sought to argue that organizational scholars need to take the law seriously as a key influence on organizational life.” (p. 13, "Conclusion")

**Support:** theory/review articles 5; commentary or exchange pieces 0; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 0; most recent ask 2026-03-31.

**Level of analysis:** field and society (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** The askers ask how law and the state act on organizations. Mutch asks organization scholars to take law seriously as a logic and to study practice transfer between legal and organizational domains, across legal systems; du Gay and Lopdrup Hjorth want formal organizational design back at the centre of scholarship and ask whether anti-formal reforms have undermined state capacity; Mena et al. ask how labour law can strengthen workers' rights and how citizen rights compare with members' rights; Scherer and Neesham call for strict regulation of LLMs and note that most states are not rule-of-law democracies; Jaser and Tourish call for democratic oversight 'where necessary' by legislative fiat. The askers disagree on whether law is a constitutive logic (Mutch) or an external restraint (Scherer and Neesham, Jaser and Tourish). How organizations change law, rather than only being changed by it, is left open.

### O26. How does generative AI change coordination, teamwork and the division of labour inside organizations?

*Kind:* topical. *Key:* `ai_coord`.

**Members** (18 OQs from 5 articles):

- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-03, OQ-hinds2024-04, OQ-hinds2024-05, OQ-hinds2024-06, OQ-hinds2024-07, OQ-hinds2024-08, OQ-hinds2024-09, OQ-hinds2024-16, OQ-hinds2024-17, OQ-hinds2024-18, OQ-hinds2024-19, OQ-hinds2024-20
- Phillips 2024 (`phillips2024`, controversies_conversations): OQ-phillips2024-07, OQ-phillips2024-09
- Stark 2024 (`stark2024`, theory): OQ-stark2024-05, OQ-stark2024-07
- Mena 2026 (`mena2026`, theory): OQ-mena2026-12
- Garud 2025 (`garud2025`, theory): OQ-garud2025-08

**Representative quotation** (OQ-phillips2024-07, Phillips 2024): “at the team level many questions remain outstanding regarding how an AI system as a teammate affects team dynamics and performance (Seeber et al., 2020).” (p. 11, "The implications of generative AI in organizations")

**Support:** theory/review articles 4; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (5, 6, 7); citation edges among askers 1; most recent ask 2026-03-31.

**Level of analysis:** interaction (team) and organization (modal OQ level: interaction).

**What remains unanswered, and where the askers disagree.** The askers ask what happens inside organizations when GenAI and algorithms take over coordinating work. Hinds and von Krogh ask what encapsulation does to cohesion, psychological safety, conflict, emergent interdependence, team evolution, the division of labour and multi-team systems, and whether team members will 'blindly follow' the AI; Phillips et al. ask how an AI teammate affects team dynamics and how 'artificial persons' change organizations; Stark and Vanden Broeck ask what sociality arises when the communicating partner is an algorithm and what contradictions the system generates; Mena et al. ask how AI shapes deliberation inside organizations; Garud et al. ask how to organize for innovation given these technologies. The askers start from different units: the team (Hinds and von Krogh), the platform topology (Stark and Vanden Broeck) and the organization's membership (Phillips et al.). Almost every question here is still posed rather than studied.

### O27. Which formal structures do organizations need for their purposes, and what can replace hierarchy?

*Kind:* topical. *Key:* `formal_structure`.

**Members** (7 OQs from 5 articles):

- du Gay 2024 (`dugay2024`, theory): OQ-dugay2024-02, OQ-dugay2024-04, OQ-dugay2024-05
- Mena 2026 (`mena2026`, theory): OQ-mena2026-05
- Gümüsay 2024 (`gumusay2024`, theory): OQ-gumusay2024-03
- Stark 2024 (`stark2024`, theory): OQ-stark2024-08
- Powell 2023 (`powell2023`, essay): OQ-powell2023-01

**Representative quotation** (OQ-dugay2024-02, du Gay 2024): “the crucial question remains which kinds of formalization are necessary for each of them to pursue their respective, and very different, purposes in the most requisite manner.” (p. 10, "Formality and Authority")

**Support:** theory/review articles 5; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-03-31.

**Level of analysis:** organization (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** These askers ask what formal structure organizations need, and what could replace hierarchy. Du Gay and Lopdrup Hjorth ask which kinds of formalization different purposes require and want organizational design restored to the centre of the field; Mena et al. ask how novel governance structures prevent managerial authority; Gümüsay and Reinecke ask how decisions unfold without formal hierarchy in prefigurative settings; Stark and Vanden Broeck ask whether technology should be treated as organizational structure; Powell and DiMaggio ask which aspects of organizations are most vulnerable to isomorphic pressure. The disagreement is sharp: du Gay and Lopdrup Hjorth defend formality against its caricature, while Mena et al. and Gümüsay and Reinecke look for structures that avoid hierarchical authority. Nobody asks what formal offices become when the structure is the platform.

### O28. How do organizations, communities and actors hold, rank or combine several institutional logics over time?

*Kind:* topical. *Key:* `logics_plural`.

**Members** (15 OQs from 5 articles):

- Georgiou 2023 (`georgiou2023`, review): OQ-georgiou2023-04, OQ-georgiou2023-05, OQ-georgiou2023-06, OQ-georgiou2023-07, OQ-georgiou2023-08, OQ-georgiou2023-11
- Godart 2024 (`godart2024`, theory): OQ-godart2024-02, OQ-godart2024-05, OQ-godart2024-06
- Stevenson 2024 (`stevenson2024`, theory): OQ-stevenson2024-01, OQ-stevenson2024-02, OQ-stevenson2024-03, OQ-stevenson2024-05
- Schildt 2025 (`schildt2025`, theory): OQ-schildt2025-06
- Jackwerth-Rice 2023 (`jackwerthrice2023`, theory): OQ-jackwerthrice2023-04

**Representative quotation** (OQ-georgiou2023-04, Georgiou 2023): “How do communities respond to institutional complexity (e.g., M. D. P. Lee & Lounsbury, 2015)? Do they become hybrids? If so, how do they manage to maintain their hybrid nature in the long term?” (p. 15, "Future Research")

**Support:** theory/review articles 5; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 0; most recent ask 2025-02-24.

**Level of analysis:** organization and community (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask how actors and organizations live with more than one institutional logic. Georgiou and Arenas ask how communities respond to institutional complexity, whether they become hybrids, how communities and organizations signal convergence, and what lets them work together despite conflict; Godart and Wittman ask about organizations that hold to a single logic ('purity'), and how purity varies; Stevenson et al. ask how stable a logic's centrality is and whether layers within an organization hold the same logic central; Schildt and Kodeih ask about contradictions within a single logic; Jackwerth-Rice et al. ask how dominant field logics shape actors' perceptions. The askers disagree on the default: Georgiou and Arenas assume hybridity under complexity, while Godart and Wittman argue that some organizations ignore survival pressures and stay pure. How centrality and purity relate is not yet asked by either side.

### O29. When is disagreement or dissent productive rather than destructive, for organizations and for scholarly communities?

*Kind:* cross-cutting. *Key:* `dissent`.

**Members** (8 OQs from 6 articles):

- Mena 2026 (`mena2026`, theory): OQ-mena2026-07, OQ-mena2026-08, OQ-mena2026-22
- Corver 2026 (`corver2026`, theory): OQ-corver2026-16
- Prasad 2024 (`prasad2024`, controversies_conversations): OQ-prasad2024-04 (BC)
- Abend 2024 (`abend2024`, controversies_conversations): OQ-abend2024-08 (BC)
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-06
- Krautzberger 2024 (`krautzberger2024`, theory): OQ-krautzberger2024-09

**Representative quotation** (OQ-mena2026-08, Mena 2026): “How can we ensure that dissent remains continuously productive and does not become destructive, for example, by deepening fractures among organizational members or even leading to organizational death?” (p. 12, "Agonistic internal focus")

**Support:** theory/review articles 4; commentary or exchange pieces 1; editorial signal n; distinct volumes 2 (5, 7); citation edges among askers 2; most recent ask 2026-07-28.

**Level of analysis:** organization and interaction (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** These askers ask when disagreement helps. Mena et al. ask how dissent can stay productive rather than splitting members or killing the organization, when consensus is needed, and when dissensus is nonessential; Corver and Filler ask how disagreement within and across groups enables productive modeling; Prasad accepts that problem-solving communities still disagree and may 'disagree their way' out of shared premises; Abend accepts that community decisions are provisional; Seidemann asks about the productive potential of resistance to change; Krautzberger and Tuckermann point to dialogue in reflective episodes. Open across them is a criterion for telling productive from destructive dissent before the outcome is known.

### O30. What does digital technology at work demand of, and do to, the individual worker: hidden labour, consent, autonomy, meaning?

*Kind:* cross-cutting. *Key:* `digital_person`.

**Members** (19 OQs from 5 articles):

- Jaser 2024 (`jaser2024`, theory): OQ-jaser2024-02, OQ-jaser2024-04, OQ-jaser2024-08 (BC)
- Justesen 2024 (`justesen2024`, theory): OQ-justesen2024-01, OQ-justesen2024-03, OQ-justesen2024-04, OQ-justesen2024-09, OQ-justesen2024-11, OQ-justesen2024-13, OQ-justesen2024-14, OQ-justesen2024-15, OQ-justesen2024-16, OQ-justesen2024-17 (BC)
- Scherer 2023 (`scherer2023`, theory): OQ-scherer2023-04, OQ-scherer2023-09 (BC), OQ-scherer2023-13
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-21, OQ-hinds2024-22
- Whyte 2023 (`whyte2023`, theory): OQ-whyte2023-03

**Representative quotation** (OQ-justesen2024-13, Justesen 2024): “Finally, we could account more fully for the emotional costs, mental loads and unintended tasks associated with digitalization.” (p. 22, "Future research: Some suggestions")

**Support:** theory/review articles 5; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 5); citation edges among askers 0; most recent ask 2024-10-29.

**Level of analysis:** individual (modal OQ level: individual).

**What remains unanswered, and where the askers disagree.** This is a conversation about the individual's place inside digitally organized work. Jaser and Tourish ask why workers consent to surveillance, through comfort, indifference or unawareness, and what value we place on human moments at work; Justesen and Plesner ask about the lived experience, emotional costs and mental loads of invisible digi-work, and its biographies; Scherer and Neesham ask how organization research can revive autonomous public reason against 'organized immaturity'; Hinds and von Krogh ask about individuals' psychological responses and loss of orientation as GenAI absorbs tasks; Whyte et al. ask how identities are built across online and offline work. The askers disagree about agency: Jaser and Tourish set resistance aside to theorize consent, while Scherer and Neesham argue that Zuboff's reforms still depend on individuals' capacity to recognize and resist, the very capacity that organized immaturity erodes. How much of the worker's experience is consent and how much is compliance is left 'beyond the scope' by Jaser and Tourish themselves.

### O31. When and why do people resist control and new technology, and can resistance itself be productive?

*Kind:* cross-cutting. *Key:* `resistance`.

**Members** (7 OQs from 5 articles):

- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-06
- Jaser 2024 (`jaser2024`, theory): OQ-jaser2024-09 (BC), OQ-jaser2024-11 (BC)
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-14
- Stark 2024 (`stark2024`, theory): OQ-stark2024-02, OQ-stark2024-03
- Sasaki 2024 (`sasaki2024`, theory): OQ-sasaki2024-03

**Representative quotation** (OQ-stark2024-02, Stark 2024): “The study of the dynamics of the relations between professional expertise and algorithmic practices is in its infancy. Under what conditions can we expect resistance by professionals to incursions by algorithmic practices? When are compromises likely?” (p. 9, "Object of management")

**Support:** theory/review articles 4.5; commentary or exchange pieces 0; editorial signal n; distinct volumes 1 (5); citation edges among askers 0; most recent ask 2024-10-29.

**Level of analysis:** multi-level (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** The askers ask when and why people resist, and what resistance is good for. Seidemann says resistance to change has been treated as something to overcome and asks about its productive potential; Hinds and von Krogh ask whether resistance to GenAI stems from perceived power loss or distrust; Stark and Vanden Broeck ask when professionals resist algorithmic practices and when they compromise; Sasaki and Baba ask through what means of resistance cultural autonomy becomes possible; Jaser and Tourish bound their theory with liminal spaces for resistance and leave aside whether workers' acts are resistance or compliance. Bartunek et al. (2025), in the corpus, argue for generative resistance but contribute no open questions. The open question is the one Jaser and Tourish set aside: how to tell resistance from compliance in practice.

### O32. Whose voices, bodies and standpoints count as legitimate sources of theory, and who is left out of the record?

*Kind:* topical. *Key:* `voices`.

**Members** (9 OQs from 5 articles):

- Lantela 2024 (`lantela2024`, theory): OQ-lantela2024-04, OQ-lantela2024-05, OQ-lantela2024-09, OQ-lantela2024-11
- Fotaki 2023 (`fotaki2023`, theory): OQ-fotaki2023-05
- Gümüsay 2024 (`gumusay2024`, theory): OQ-gumusay2024-08, OQ-gumusay2024-13
- Höllerer 2026 (`hollerer2026`, editorial): OQ-hollerer2026-05
- Arnold 2023 (`arnold2023`, theory): OQ-arnold2023-01

**Representative quotation** (OQ-lantela2024-09, Lantela 2024): “who has been the legitimate theoretical voice within a specific sub-field, and why? What kind of bodies have been able to theorize?” (p. 12, "Conclusion")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal y; distinct volumes 3 (4, 5, 7); citation edges among askers 1; most recent ask 2026-07-26.

**Level of analysis:** field (scholarly community) (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** The askers ask whose voices count in theory itself. Lantela asks whose voice is missing from records, who has been the legitimate theoretical voice in a sub-field, and what bodies have been able to theorize; Fotaki wants research to reflect real people's material and affective lives; Gümüsay and Reinecke say affected communities must join in judging what futures are desirable, and call for larger, more diverse teams; the editorial by Höllerer et al. asks for a diversity of authors and perspectives in each debate; Arnold and Costas call for attention to those whose status as speaking beings is denied. Lantela names the difficulty that remains: to find a basis for similarity of experience without categorizing it in a way that dominates again.

### O33. Who takes part in organizational decision-making (strategy, governance, modeling), on whose terms, and with what effect?

*Kind:* topical. *Key:* `participation`.

**Members** (16 OQs from 4 articles):

- Friesl 2023 (`friesl2023`, theory): OQ-friesl2023-03, OQ-friesl2023-04, OQ-friesl2023-05, OQ-friesl2023-06 (BC), OQ-friesl2023-07, OQ-friesl2023-08, OQ-friesl2023-09
- Langenmayr 2024 (`langenmayr2024`, theory): OQ-langenmayr2024-02, OQ-langenmayr2024-05, OQ-langenmayr2024-11
- Mena 2026 (`mena2026`, theory): OQ-mena2026-01, OQ-mena2026-05, OQ-mena2026-06, OQ-mena2026-13
- Corver 2026 (`corver2026`, theory): OQ-corver2026-05, OQ-corver2026-11

**Representative quotation** (OQ-friesl2023-03, Friesl 2023): “Unveiling the social processes underpinning self-selection allows future research to study why certain actors participate in open strategy or why they abstain from doing so.” (p. 13, "Discussion and Theoretical Implications")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 1; most recent ask 2026-07-28.

**Level of analysis:** organization and interaction (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask who takes part in organizational decisions, and on whose terms. Friesl et al. ask why actors self-select into open strategy or abstain, and how selection contexts shape that choice; Langenmayr et al. ask how newly included actors are misrepresented and whether representativity rests on self-identified heterogeneity; Mena et al. ask who qualifies as the demos, how inclusion and deliberation can be enhanced descriptively, and whether deliberative tools are merely symbolic; Corver and Filler ask how co-creative modeling interacts with democratic governance and how capacities are distributed across roles. The disagreement is over the starting point: Friesl et al. begin from the individual's choice to take part, Langenmayr et al. from incumbents' control over inclusion. The two views meet only in Langenmayr et al.'s citation of Friesl et al.

### O34. How do organizations anticipate, respond to and learn from crises, and what should crisis response aim at?

*Kind:* topical. *Key:* `crisis`.

**Members** (9 OQs from 4 articles):

- Kalkman 2026 (`kalkman2026`, theory): OQ-kalkman2026-03, OQ-kalkman2026-05, OQ-kalkman2026-07, OQ-kalkman2026-08
- Patriotta 2025 (`patriotta2025`, theory): OQ-patriotta2025-05, OQ-patriotta2025-06, OQ-patriotta2025-07
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-06
- Giovannoni 2025 (`giovannoni2025`, theory): OQ-giovannoni2025-05

**Representative quotation** (OQ-patriotta2025-06, Patriotta 2025): “Scholars could explore how organizations attempt to anticipate and preempt legitimacy challenges by crafting proactive justifications before a test crystallizes, and furthermore examine how prior crises constrain or enable subsequent responses.” (p. 18, "Future research directions: Legitimacy in a changing world")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (5, 6, 7); citation edges among askers 0; most recent ask 2026-07-21.

**Level of analysis:** organization (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask what crisis management is for and how organizations learn from crises. Kalkman asks what conditions foster moral self-reflection in a crisis, how relationships are kept in an affected organization, who is most vulnerable, and how organizations change their approaches, while noting how hard causal claims are in crises; Patriotta et al. ask about early warning signs, proactive justification, and how prior crises constrain later responses; Hinds and von Krogh ask how GenAI-built coordination fares when crises demand change; Giovannoni and Quattrone extend their rhetorical approach to extreme contexts. The askers differ on purpose: Kalkman asks for a care-based purpose against the functionalist restoration of order, while Patriotta et al. study how organizations justify themselves to restore legitimacy.

### O35. How do physical space and the material settings of online and offline work shape coordination and presence?

*Kind:* topical. *Key:* `space_hybrid`.

**Members** (23 OQs from 4 articles):

- Whyte 2023 (`whyte2023`, theory): OQ-whyte2023-02, OQ-whyte2023-04, OQ-whyte2023-05, OQ-whyte2023-06, OQ-whyte2023-08 (BC), OQ-whyte2023-09, OQ-whyte2023-10, OQ-whyte2023-12, OQ-whyte2023-13, OQ-whyte2023-14
- Räcker 2024 (`racker2024`, theory): OQ-racker2024-01, OQ-racker2024-02, OQ-racker2024-04, OQ-racker2024-05 (BC), OQ-racker2024-06 (BC), OQ-racker2024-07, OQ-racker2024-08, OQ-racker2024-09, OQ-racker2024-10, OQ-racker2024-11, OQ-racker2024-12 (BC)
- Justesen 2024 (`justesen2024`, theory): OQ-justesen2024-08
- Friedrich 2026 (`friedrich2026`, theory): OQ-friedrich2026-06

**Representative quotation** (OQ-racker2024-01, Räcker 2024): “There is, we believe, a need for systematic empirical research on how different types of coordination practices produce space and how this impacts the outcomes of any integration effort.” (p. 12, "Spatial perspective on coordinating opens up a novel empirical research programme")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-04-01.

**Level of analysis:** interaction and organization (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask how material and spatial settings shape coordination, including the offline settings in which online work happens. Räcker et al. ask how coordination practices produce space, how practitioners use distance, boundaries and movement on purpose, and how spatial configurations interact with roles and routines; Whyte et al. ask how coherence is created across simultaneous online and offline practices, how hybrid work reshapes strategy practices, and whether a video meeting is one practice or many; Justesen and Plesner ask for methods for hybrid presence; Friedrich asks for spaces and routines that slow down and extend the rational mind. Whyte et al. leave open a debate with Uhlin (2022) about whether the online meeting is one practice or multiple. Räcker et al. limit their theory to physical space and expect space-focused coordinating to work best under co-presence. How virtual settings produce space is the gap between the two.

### O36. How do organizations strengthen or erode democracy and citizens' capacity for public reason, inside and beyond their walls?

*Kind:* topical. *Key:* `democracy`.

**Members** (23 OQs from 4 articles):

- Mena 2026 (`mena2026`, theory): OQ-mena2026-09, OQ-mena2026-10, OQ-mena2026-11, OQ-mena2026-12, OQ-mena2026-14, OQ-mena2026-16, OQ-mena2026-17, OQ-mena2026-18, OQ-mena2026-20, OQ-mena2026-21, OQ-mena2026-23
- Scherer 2023 (`scherer2023`, theory): OQ-scherer2023-02, OQ-scherer2023-04, OQ-scherer2023-06, OQ-scherer2023-08, OQ-scherer2023-11, OQ-scherer2023-12 (BC), OQ-scherer2023-13
- Friedrich 2026 (`friedrich2026`, theory): OQ-friedrich2026-01, OQ-friedrich2026-15, OQ-friedrich2026-16
- Jaser 2024 (`jaser2024`, theory): OQ-jaser2024-06, OQ-jaser2024-07

**Representative quotation** (OQ-scherer2023-13, Scherer 2023): “Organization theory and business ethics have a crucial role to play in advancing our understanding of how individual and collective human action can be further organized to foster the communicative conditions needed for mature citizens” (p. 21, "Conclusion")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-04-01.

**Level of analysis:** multi-level (organization and polity) (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** The askers ask how organizations sustain or erode democracy. Mena et al. ask how citizen rights compare with members' rights, how civic engagement passes between personal and organizational life, how platforms shape public deliberation, how organizations act in non-democratic or backsliding contexts, and how organizational democratic innovations scale; Scherer and Neesham ask how organizing can foster the communicative conditions for mature citizens, and propose a Habermas-Kant framework for digital civic spaces; Friedrich asks what organizational democracy becomes when ecological interdependencies are constitutive; Jaser and Tourish call for democratic oversight of surveillance. The disagreement is over the demos itself. Scherer and Neesham ground democracy in human public reason, while Friedrich argues that the humanist subject is the problem.

### O37. How do audiences, media and activists turn events into scandals and legitimacy tests, and how do digital platforms change that process?

*Kind:* topical. *Key:* `scandal_legit`.

**Members** (21 OQs from 4 articles):

- Pozner 2023 (`pozner2023`, theory): OQ-pozner2023-04, OQ-pozner2023-06, OQ-pozner2023-07, OQ-pozner2023-08, OQ-pozner2023-09, OQ-pozner2023-11, OQ-pozner2023-12, OQ-pozner2023-13 (BC), OQ-pozner2023-14, OQ-pozner2023-15, OQ-pozner2023-16
- Patriotta 2025 (`patriotta2025`, theory): OQ-patriotta2025-02, OQ-patriotta2025-03, OQ-patriotta2025-05, OQ-patriotta2025-08, OQ-patriotta2025-09, OQ-patriotta2025-11, OQ-patriotta2025-12 (BC)
- Leitzinger 2023 (`leitzinger2023`, review): OQ-leitzinger2023-09, OQ-leitzinger2023-10
- Grodal 2024 (`grodal2024`, controversies_conversations): OQ-grodal2024-02

**Representative quotation** (OQ-pozner2023-15, Pozner 2023): “Empirical work might explicitly consider social media’s role in social evaluation (Etter et al., 2019; Seidel et al., 2020) and compare scandal construction before and after the widespread adoption of social media.” (p. 16, "Future directions")

**Support:** theory/review articles 3; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 1; most recent ask 2025-11.

**Level of analysis:** field and interaction (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** The askers ask how audiences turn events into scandals and tests of legitimacy. Pozner and Hannigan ask how publics make sense of information, how media, publics and social control agents interact, how non-adjacent publics come into conversation, whether journalists suffice to start a scandal, and how social media change scandal construction; Patriotta et al. ask about early warning signs, the role of media and platforms, influencers, activists and whistleblowers, and comparative and longitudinal patterns; Leitzinger and Waeger ask when online or street protest works better; Grodal et al. ask whether perceived boundary-crossing technology draws more attention. Patriotta et al. cite Pozner and Hannigan, so the conversation is linked inside the corpus. Both theories leave the platform as context rather than as a party to the test, and that is the open point.

### O38. How should organizations and their members respond to paradoxes (both/and, either/or, or neither), and how should those responses be judged?

*Kind:* topical. *Key:* `paradox`.

**Members** (21 OQs from 5 articles):

- Krautzberger 2024 (`krautzberger2024`, theory): OQ-krautzberger2024-03, OQ-krautzberger2024-04, OQ-krautzberger2024-05, OQ-krautzberger2024-06, OQ-krautzberger2024-07, OQ-krautzberger2024-08, OQ-krautzberger2024-10, OQ-krautzberger2024-11, OQ-krautzberger2024-12, OQ-krautzberger2024-13
- Seidemann 2024 (`seidemann2024`, theory): OQ-seidemann2024-02, OQ-seidemann2024-04, OQ-seidemann2024-07, OQ-seidemann2024-08, OQ-seidemann2024-11, OQ-seidemann2024-12, OQ-seidemann2024-13, OQ-seidemann2024-15
- Keller 2025 (`keller2025`, theory): OQ-keller2025-02 (BC)
- Skade 2025 (`skade2025`, theory): OQ-skade2025-06 (BC)
- Georgiou 2023 (`georgiou2023`, review): OQ-georgiou2023-05

**Representative quotation** (OQ-seidemann2024-08, Seidemann 2024): “Expanding on the predominantly strategic perspective of paradox management, the question of how responses to paradoxes are evaluated from a normative standpoint becomes central.” (p. 17, "Purposefully integrating normative approaches")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 2; most recent ask 2025-09-27.

**Level of analysis:** organization and multi-level (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask how paradox should be handled and judged. Krautzberger and Tuckermann ask how to navigate a portfolio of both/and and either/or approaches, how reflective episodes work, and what failures a meta-both/and approach brings; Seidemann asks why organizations are 'rife with paradoxes', how responses are evaluated normatively, and what boundary conditions both/and has; Keller et al. bound their paradoxical theorizing by fixed material and institutional constraints; Skade bounds his futures perspectives as not all-encompassing; Georgiou and Arenas ask whether logic variants create tensions for members. The disagreement is Seidemann's critique of the 'hegemony' of both/and, which Krautzberger and Tuckermann, writing independently, partly answer by giving either/or equal standing. Bartunek et al. (2025, no open questions) add 'neither/nor'. How a response to paradox should be judged good is unresolved.

### O39. What are institutional logics made of (beliefs, practices, law), where do they come from, and how do practices travel between them?

*Kind:* topical. *Key:* `logics_origin`.

**Members** (13 OQs from 4 articles):

- Schildt 2025 (`schildt2025`, theory): OQ-schildt2025-03, OQ-schildt2025-04, OQ-schildt2025-05
- Mutch 2025 (`mutch2025`, theory): OQ-mutch2025-01, OQ-mutch2025-02, OQ-mutch2025-03, OQ-mutch2025-04, OQ-mutch2025-05 (BC), OQ-mutch2025-06
- Georgiou 2023 (`georgiou2023`, review): OQ-georgiou2023-02, OQ-georgiou2023-03, OQ-georgiou2023-12
- Stevenson 2024 (`stevenson2024`, theory): OQ-stevenson2024-04

**Representative quotation** (OQ-mutch2025-03, Mutch 2025): “Recognizing law as a central institutional logic directs our attention to the possibility for practices to be transferred from the legal to the organizational domain (and vice versa).” (p. 13, "Conclusion")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 0; most recent ask 2025-04-25.

**Level of analysis:** field (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** The askers ask what institutional logics are made of and how they come to be. Schildt and Kodeih ask how practice constellations arise and how competing versions of logics are advanced politically; Mutch asks the field to treat law as a logic and to study the transfer of practices between law and organizations, across legal systems; Georgiou and Arenas ask about novel variants of the community logic and how to measure it; Stevenson et al. suggest a mutually constitutive view of logics. The disagreement is substantive: Schildt and Kodeih complement the belief-centred view with practices, Mutch follows Friedland in treating a logic as a substance carried by practices, and Georgiou and Arenas reply to Mutch (2021), who denied a community logic. Which logics belong in the inter-institutional system remains disputed.

### O40. How can organizations take up and sustain care as an organizing value against the pull of control and efficiency?

*Kind:* topical. *Key:* `care`.

**Members** (11 OQs from 4 articles):

- Fotaki 2023 (`fotaki2023`, theory): OQ-fotaki2023-01, OQ-fotaki2023-02, OQ-fotaki2023-03, OQ-fotaki2023-06
- Kalkman 2026 (`kalkman2026`, theory): OQ-kalkman2026-02, OQ-kalkman2026-04, OQ-kalkman2026-05, OQ-kalkman2026-06
- Friedrich 2026 (`friedrich2026`, theory): OQ-friedrich2026-10, OQ-friedrich2026-13
- Bacq 2023 (`bacq2023`, theory): OQ-bacq2023-02

**Representative quotation** (OQ-fotaki2023-01, Fotaki 2023): “We need to consider why the value of care in private life is generally accepted when its importance and role in the public sphere are subject to heated debates and controversies” (p. 2, "Introduction")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 7); citation edges among askers 1; most recent ask 2026-07-21.

**Level of analysis:** organization and society (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** This conversation asks how care can become an organizing value. Fotaki asks why care is valued in private but contested in public, how power asymmetries shape care, and how care can be taught as a capability; Kalkman asks how members negotiate care-based values in crises, whether moral stewards are more open to them, and what a care-based purpose produces; Friedrich asks how posthuman care can secure resources and how care 'calls' can be answered; Bacq et al. ask how shame-reducing ventures should be managed. Kalkman cites Fotaki, so the thread is linked. The askers disagree on whom care is for: humans in political relations (Fotaki), people affected by crises (Kalkman), or multispecies others (Friedrich). Kalkman leaves open whether critics of the ethics of care are right about its results.

### O41. How does neoliberal ideology shape what organizations and states treat as legitimate, from care to surveillance to public administration?

*Kind:* topical. *Key:* `neoliberal`.

**Members** (5 OQs from 4 articles):

- Fotaki 2023 (`fotaki2023`, theory): OQ-fotaki2023-02
- Jaser 2024 (`jaser2024`, theory): OQ-jaser2024-05, OQ-jaser2024-10 (BC)
- du Gay 2024 (`dugay2024`, theory): OQ-dugay2024-07
- Scherer 2023 (`scherer2023`, theory): OQ-scherer2023-02

**Representative quotation** (OQ-jaser2024-05, Jaser 2024): “We need to pay more attention to the neoliberal ideological context in which HS has arisen, and from which it has derived undue legitimacy and power.” (p. 17, "Conclusion")

**Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 5); citation edges among askers 0; most recent ask 2024-03-19.

**Level of analysis:** field and society (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** Four askers ask how neoliberal ideology shapes what organizations take as legitimate. Fotaki, quoting Tronto, asks what it would mean to argue against neoliberalism from the standpoint of care; Jaser and Tourish ask for attention to the neoliberal context that lends surveillance its legitimacy, and bound their theory by that context's durability; du Gay and Lopdrup Hjorth ask for a transformation in views of government, the public good and the state; Scherer and Neesham ask for a critical theory of surveillance capitalism. They agree on the diagnosis and differ on the counter-value: care, democratic oversight, formal state organization, or Enlightenment maturity. None asks what would show the ideology weakening.

### O42. How does brokerage work, and what happens to brokers and resource holders when tie histories accumulate or technology takes over brokering?

*Kind:* topical. *Key:* `brokerage`.

**Members** (5 OQs from 3 articles):

- Brennecke 2025 (`brennecke2025`, theory): OQ-brennecke2025-03, OQ-brennecke2025-14
- Hinds 2024 (`hinds2024`, theory): OQ-hinds2024-10, OQ-hinds2024-13
- Pozner 2023 (`pozner2023`, theory): OQ-pozner2023-09

**Representative quotation** (OQ-hinds2024-13, Hinds 2024): “What are the effects of such changes on power holders and resource brokers, and how do they respond to these changes?” (p. 10, "Discussion")

**Support:** theory/review articles 3; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 0; most recent ask 2025-09-28.

**Level of analysis:** interaction (network) (modal OQ level: interaction).

**What remains unanswered, and where the askers disagree.** The askers ask how brokerage works and what threatens it. Brennecke et al. ask how the history of bridging ties affects brokerage behaviour and how tie biographies interact with brokerage and centrality; Hinds and von Krogh ask how GenAI relates to resource holders, how digital brokerage works, and how power holders and brokers respond; Pozner and Hannigan ask how non-adjacent publics come into conversation during a scandal. Open is whether a technology can hold a brokerage position, which Hinds and von Krogh imply and Brennecke et al.'s dyadic framework does not address.

### O43. What do practices actually do inside organizations once they have spread or been adopted: change conduct, or stay symbolic?

*Kind:* topical. *Key:* `diffusion_effects`.

**Members** (6 OQs from 3 articles):

- Powell 2023 (`powell2023`, essay): OQ-powell2023-02, OQ-powell2023-03, OQ-powell2023-04
- Mena 2026 (`mena2026`, theory): OQ-mena2026-13
- Corver 2026 (`corver2026`, theory): OQ-corver2026-08, OQ-corver2026-10

**Representative quotation** (OQ-powell2023-04, Powell 2023): “The challenge for diffusion studies is to understand better the mechanisms of adoption and how newly adopted practices mesh with existing organizational practices, structures, and values. Longitudinal analyses that examine both the predictors and consequences of adoption, as in the studies of diversity training, are essential.” (p. 14, "Heterogeneous diffusion")

**Support:** theory/review articles 3; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 7); citation edges among askers 0; most recent ask 2026-07-28.

**Level of analysis:** organization (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** The askers ask what adopted practices do. Powell and DiMaggio ask what is diffused, through which channels, how adopted practices mesh with existing structures, and what their effects are, calling for longitudinal studies of predictors and consequences; Mena et al. ask whether deliberative tools lead mostly to symbolic compliance; Corver and Filler ask which decisions modeling has actually improved and which modeling actions support success. The askers share the worry that adoption is measured more often than effect, and none has yet found a design that tracks practices from adoption to consequence.

### O44. Can a person become an institution, and under what conditions does such an institution form, endure, or outlive the person?

*Kind:* topical. *Key:* `person_inst`.

**Members** (28 OQs from 3 articles):

- Nigam 2025 (`nigam2025`, controversies_conversations): OQ-nigam2025-01, OQ-nigam2025-02 (BC), OQ-nigam2025-03, OQ-nigam2025-04, OQ-nigam2025-05, OQ-nigam2025-06, OQ-nigam2025-07, OQ-nigam2025-08, OQ-nigam2025-09, OQ-nigam2025-10, OQ-nigam2025-11
- Derek Robinson 2025 (`derekrobinson2025`, controversies_conversations): OQ-derekrobinson2025-01, OQ-derekrobinson2025-02, OQ-derekrobinson2025-04, OQ-derekrobinson2025-05, OQ-derekrobinson2025-06, OQ-derekrobinson2025-07, OQ-derekrobinson2025-08, OQ-derekrobinson2025-09, OQ-derekrobinson2025-10, OQ-derekrobinson2025-11, OQ-derekrobinson2025-12, OQ-derekrobinson2025-13, OQ-derekrobinson2025-14, OQ-derekrobinson2025-15
- Hawbaker 2025 (`hawbaker2025`, controversies_conversations): OQ-hawbaker2025-01, OQ-hawbaker2025-02 (BC), OQ-hawbaker2025-04

**Representative quotation** (OQ-nigam2025-11, Nigam 2025): “We hope that others will take on these ideas and push forward why, how, when and for how long individuals can become institutions.” (p. 9, "Conclusion")

**Support:** theory/review articles 0; commentary or exchange pieces 3; editorial signal n; distinct volumes 1 (6); citation edges among askers 2; most recent ask 2025-12-23.

**Level of analysis:** multi-level (person to institution) (modal OQ level: multi-level).

**What remains unanswered, and where the askers disagree.** This is the 6(4) exchange. Nigam et al. ask why, how, when and for how long individuals become institutions, how such institutions live on after death or office, and whether they arise more in unsettled times; Derek Robinson and Atanasova ask what criteria mark transitions between stages, whether the process can reverse, how class, gender and generation shape it, and whether micro-institutionalization of personhood happens in workplaces; Hawbaker and Hallett invite theory on key institutional interactants and the co-creation of mythologies. The disagreement is basic. Hawbaker and Hallett deny that any individual can be an institution, Derek Robinson and Atanasova accept it only as an outcome of branding, and Nigam et al. bound their own theory by reciprocity and resonance. Höllerer et al.'s editorial cites all three pieces.

### O45. What will large language models do to theorizing, and what expertise must scholars keep to judge them?

*Kind:* topical. *Key:* `llm_theory`.

**Members** (10 OQs from 3 articles):

- Cornelissen 2024 (`cornelissen2024`, editorial): OQ-cornelissen2024-04, OQ-cornelissen2024-05 (BC), OQ-cornelissen2024-06, OQ-cornelissen2024-07, OQ-cornelissen2024-08, OQ-cornelissen2024-09, OQ-cornelissen2024-10
- Suddaby 2024 (`suddaby2024`, controversies_conversations): OQ-suddaby2024-05 (BC), OQ-suddaby2024-06
- Hsu 2024 (`hsu2024`, controversies_conversations): OQ-hsu2024-08

**Representative quotation** (OQ-cornelissen2024-06, Cornelissen 2024): “In this context, the million-dollar question is whether LLMs can now, or in the near future, be truly creative beyond such basic tasks, and in ways that might capture or mimic human levels of creativity in acts of theorizing. It is perhaps a bit premature here to give a conclusive answer” (p. 7, "Abstract reasoning and creativity")

**Support:** theory/review articles 0; commentary or exchange pieces 2; editorial signal y; distinct volumes 1 (5); citation edges among askers 2; most recent ask 2024-10-28.

**Level of analysis:** field and individual (the scholar) (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** The editors open this conversation. Cornelissen et al. ask whether LLMs can be creative in acts of theorizing beyond basic tasks, call for debate on the technology's implications, and require authors to declare and explain LLM use in their chain of reasoning; Suddaby replies that AI depends on data about what 'was' and will work poorly in dynamic contexts, and suggests that overcoming a hyper-pragmatic science may rest on manipulating how algorithms read past behaviour; Hsu and Bechky ask how to retain the expertise needed to question the technology. Cornelissen et al. bound their stance as provisional, since LLMs may improve quickly. Open is whether LLM-assisted theorizing will become normal practice, which the editors themselves call too early to judge.

### O46. How do hype and attention around new technologies form, and with what institutional and power consequences?

*Kind:* topical. *Key:* `hype`.

**Members** (5 OQs from 2 articles):

- Wedlin 2025 (`wedlin2025`, theory): OQ-wedlin2025-03, OQ-wedlin2025-04
- Grodal 2024 (`grodal2024`, controversies_conversations): OQ-grodal2024-02, OQ-grodal2024-06, OQ-grodal2024-07

**Representative quotation** (OQ-wedlin2025-03, Wedlin 2025): “We hope that our model of hype as a process of translation will spur a variety of empirical investigations, further exploring the institutional dynamics of hype and its potentially disruptive institutional consequences.” (p. 17, "Concluding Discussion")

**Support:** theory/review articles 1; commentary or exchange pieces 1; editorial signal n; distinct volumes 2 (5, 6); citation edges among askers 0; most recent ask 2025-12-23.

**Level of analysis:** field (modal OQ level: field).

**What remains unanswered, and where the askers disagree.** Two askers ask how attention around new technology forms and what it does. Wedlin and Weinryb ask for empirical work on the institutional dynamics of hype and for a broader set of translators and enablers; Grodal et al. ask whether perceived crossing of the human-machine boundary generates audience attention, and for study of power during technological emergence, including around AI. Open is whether hype is a cause of institutional change (Wedlin and Weinryb) or a symptom of a perceived boundary crossing (Grodal et al.).

### O47. How do stories and images around organizations and people become myths with sacred or binding force?

*Kind:* topical. *Key:* `myth`.

**Members** (5 OQs from 2 articles):

- Paca 2024 (`paca2024`, theory): OQ-paca2024-02, OQ-paca2024-03, OQ-paca2024-04, OQ-paca2024-05
- Hawbaker 2025 (`hawbaker2025`, controversies_conversations): OQ-hawbaker2025-01

**Representative quotation** (OQ-hawbaker2025-01, Hawbaker 2025): “We welcome further theorizing about the impact of key institutional interactants, and the contexts and social dimensions that allow some people to leverage interactions to co-create mythologies.” (p. 9, "Discussion")

**Support:** theory/review articles 1; commentary or exchange pieces 1; editorial signal n; distinct volumes 2 (5, 6); citation edges among askers 0; most recent ask 2025-12-01.

**Level of analysis:** organization (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** Two askers ask how myths form around organizations and persons. Paca and Rozuel ask for empirical study of mythological stories and archetypal images across contexts, and for the use of their Jungian model in organizational change; Hawbaker and Hallett, replying to Nigam et al., invite theory on how some people use interactions to co-create institutional mythologies. They differ on the source: psychic archetypes in Paca and Rozuel, and interaction in Hawbaker and Hallett.

### O48. When are organizations rewarded for conforming, and when for staying distinct or 'pure', and before which audiences?

*Kind:* topical. *Key:* `conform_distinct`.

**Members** (5 OQs from 2 articles):

- Powell 2023 (`powell2023`, essay): OQ-powell2023-01, OQ-powell2023-07, OQ-powell2023-08
- Godart 2024 (`godart2024`, theory): OQ-godart2024-03, OQ-godart2024-04

**Representative quotation** (OQ-powell2023-08, Powell 2023): “But constructive engagement with these literatures may help institutional theorists to clarify the features of organizations (and the types of organizations) for which conformity or distinctiveness, respectively, are rewarded, and the scope conditions governing such generalizations.” (p. 15, "Heterogeneous diffusion")

**Support:** theory/review articles 2; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 5); citation edges among askers 0; most recent ask 2024-09-03.

**Level of analysis:** organization and field (modal OQ level: organization).

**What remains unanswered, and where the askers disagree.** Two askers ask when organizations gain from conforming and when from standing apart. Powell and DiMaggio ask which aspects of organizations are most vulnerable to isomorphic pressure and what rules let organizations differentiate while gaining legitimacy (the punk example); Godart and Wittman ask which and how many audiences an organization must please to survive, and how shared identities foster categories. The gap is the scope condition Powell and DiMaggio name: for which organizations conformity, and for which distinctiveness, is rewarded.

## Singletons

These 19 OQs are asked by one article only and fit no conversation above. Most are limitations or scope notes tied to a single model. The rest are agenda items no other author picks up: Garud et al. on exploring through existing architectures, Chia and Holt on strategy theory's logics, Gümüsay and Reinecke on prospective theories of valuation, Corver and Filler on carrying modeling actions to other settings.

- OQ-georgiou2023-10 (Georgiou 2023; limitation): “Although this list of communities may not be comprehensive, it encompasses the most frequently discussed types in the organization and management field.” (p. 6, "Research on Communities of Place, Practice, Users, and Firms")
- OQ-jackwerthrice2023-10 (Jackwerth-Rice 2023; limitation): “more research would be needed to corroborate this assumption.” (p. 16, "Discussion and Conclusion")
- OQ-chia2023-03 (Chia 2023; invitation): “What we urge, however, is for those strategy theorists,tied to a means–ends logic to admit the force of both practice and situation, and even to further admit a fourth.” (p. 17, "Discussion: What Next for Strategy?")
- OQ-gumusay2024-04 (Gümüsay 2024; future_research_call): “This is a missed opportunity; organization theorists could develop prospective theories of different valuation methods, convening stakeholders and offering a critical voice in these debates.” (p. 13, "Theorizing Practices for the Double Leap into the Future")
- OQ-stark2024-01 (Stark 2024; explicit_question): “What does this mean? How could it become so taken-for-granted? And how does that familiarity indicate some fundamental similarities across dissimilar contexts while masking other important differences?” (p. 8, "Object of management")
- OQ-hsu2024-01 (Hsu 2024; limitation): “While this is early-stage, non-peer-reviewed work, the findings point to a number of consistent patterns across these diverse contexts” (p. 6, "The Case of Creative Work: Professional gatekeepers and creative producers")
- OQ-hsu2024-02 (Hsu 2024; limitation): “Our ideas are therefore speculative, but rooted in grounded understandings of the creative roles that are vital to this industry.” (p. 7, "A Thought Experiment: Imagined impacts of generative AI in television and film production")
- OQ-langenmayr2024-08 (Langenmayr 2024; future_research_call): “More research is needed to show whether such a re-orientation towards broader societal issues can be reconciled with the prevalent business case approach in (open) strategy research.” (p. 15, "Discussion and Conclusion")
- OQ-langenmayr2024-10 (Langenmayr 2024; limitation): “The list of theories is neither exhaustive nor exclusive as there may be other, equally relevant theories that could be used to study the themes raised by the equity-based research agenda.” (p. 5, "Theorizing Inclusion in Open Strategy Research")
- OQ-garud2025-04 (Garud 2025; future_research_call): “These practices underscore an additional facet of innovation at work worth investigating. Interweaving all three notions of time (Chronos, Kairos, and Aion) generates options value for knowledge assets” (p. 13, "Implications")
- OQ-garud2025-06 (Garud 2025; future_research_call): “How actors may explore new functionalities by exploiting existing architectures is a topic worth further investigation in the context of organizational ambidexterity.” (p. 15, "Future research on innovation at work in the age of digital technologies and Gen AI")
- OQ-garud2025-09 (Garud 2025; invitation): “we propose that organizations can experiment with alternatives to the main dominant themes that structure organizations and work practices.” (p. 17, note 22)
- OQ-brennecke2025-01 (Brennecke 2025; future_research_call): “A way to specify and test these ideas would be to leverage Bensaou et al. (2014) with respect to the distinction these authors make between devoted players, selective players and purists” (p. 11, "Relational history and network agency")
- OQ-friedrich2026-18 (Friedrich 2026; limitation): “A challenge of Braidotti’s critical affirmative theorizing is, however, her eclectic “zigzagging” between various theoretical traditions” (p. 19, "Posthuman feminism for organization theory")
- OQ-corver2026-07 (Corver 2026; future_research_call): “This invites further theorizing on how modeling generates its own distinct pathways to impact” (p. 17, "Discussion")
- OQ-corver2026-12 (Corver 2026; future_research_call): “Further conceptual and empirical work could explore whether additional types of modeling actions become visible once this vocabulary is applied to settings with different problem structures” (p. 18, "Discussion")
- OQ-corver2026-13 (Corver 2026; future_research_call): “Further research could examine whether and how the modeling activity, actions, and consequences we have outlined translate to these contexts” (p. 18, "Discussion")
- OQ-corver2026-14 (Corver 2026; limitation): “we have said comparatively little about how the people involved in that process actually interpret the consequences it produces in any given instance” (p. 18, "Discussion")
- OQ-corver2026-15 (Corver 2026; boundary_condition): “our focus on the modeling process is not meant to suggest that implementation problems in corporate sustainability stem from modeling assumptions alone” (p. 18, "Discussion")

## Cross-cutting questions

Several conversations cut across the journal's topical lines. I group them under the three lenses the brief names, plus three more that the corpus itself throws up. Each line names the conversations that carry the lens and what joins them.

**The individual's place inside new organizational forms.** The person inside an organization that is platform-based, hybrid, digitally mediated or barely bounded appears in six conversations. **O30** asks what digital work demands of the worker (consent, hidden labour, autonomy, meaning). **O33** asks who chooses to take part in opened-up strategy and governance. **O05** asks how collectives gain actorhood, and Schoeneborn et al. turn that into a question about individual as against collective responsibility. **O44** inverts the lens and asks whether a person can become the institution. **O21** and **O11** ask the same of founders, organizations and scholars themselves. Across them the individual is either absorbed into a larger agent (encapsulation, actorhood, institution) or asked to choose (self-selection, consent).

**Accountability when no one is in charge.** **O13** is the direct form: Stark and Vanden Broeck on algorithms, Schoeneborn et al. on attributing actorhood, Mena et al. on transparency, Pavlisa et al. on the stakeholder boundary. **O18** is its precondition, since answerability needs a bounded set of members, and six authors on six topics leave that boundary open. **O05**, **O26** (decisions taken over by GenAI) and **O37** (audiences and platforms that test legitimacy without anyone convening them) supply cases. The askers place responsibility in three different places: the technology, the attribution practice and the law (**O25**).

**Technology standing between people.** Technology as intermediary runs through **O26** (GenAI in teams and coordination), **O22** (GenAI in category work), **O15** (slow institutional effects), **O35** (the video call and its unseen offline settings), **O30** (surveillance and invisible work), **O37** (social media in scandal and legitimacy tests), **O36** (Mena et al. on social media, AI and platforms in deliberation), **O42** (digital brokerage) and **O45** (LLMs between scholars and their theorizing). The shared, unanswered question is whether the technology is a channel, a party or a structure. Hsu and Bechky call it an independent force, Stark and Vanden Broeck call it organizational structure, Phillips et al. call it a participant in category work, and Whyte et al. treat it as one practice among the offline practices it rests on.

**History and time as explanation.** **O01** gathers twelve askers who want the past of a tie, a crisis, a collective or a movement to explain its present, and several more (Garud et al., Suddaby, Justesen and Plesner, Lantela, Dion et al.) who want a different notion of time, such as Kairos and Aion or 'is' and 'was'.

**Concept boundaries and who settles them.** **O02** and **O08** ask, respectively, where the field's concepts end and who decides. **O32** and **O20** ask who is entitled to theorize and whether theorizing can be neutral.

**The underside of favoured constructs.** **O14**, **O31** and **O29** each take a construct the field treats as good or bad by default (both/and, atmospheres, consensus, overcoming resistance) and ask about its other face.

## Conversations that continue outside the corpus

These pieces reply to, extend or argue against work published outside the 66-item window. Their OQs therefore belong to conversations whose earlier turns are not in this corpus.

- **Georgiou & Arenas (2023)** reply to Mutch (2021, *Organization Theory*, before the window), who denied a distinct community logic, and answer Almandoz et al. (2017) on intra-logic heterogeneity. Their OQs sit in **O28** and **O39**. Mutch's in-corpus "Law as logic" (2025) does not return to that dispute.
- **Abend (2024)** presents his book *Words and Distinctions for the Common Good* (2023); **Suddaby (2024)** critiques the book and Abend (2008), not the in-corpus essay. **O08** continues a debate begun in those books and articles.
- **Scherer & Neesham (2023)** and **Jaser & Tourish (2024)** extend and critique Zuboff's program on surveillance capitalism (Zuboff 2022, *Organization Theory* 3(3), before the window). See **O41**, **O36** and **O30**.
- **Dion, Cooren & Dupuis (2025)** challenge Schoeneborn et al. (2019, 2022), outside the window; the conversation re-enters the corpus with **Schoeneborn, Dobusch & Seidl (2026)**, who cite Dion et al. See **O05**.
- **Whyte, Comi & Mosca (2023)** leave open a debate with Uhlin (2022) about whether an online meeting is one practice or several (**O35**).
- **Keller, Berti & Smith (2025)** restart Poole and Van de Ven's (1989) proposal to theorize with paradox; **Bartunek et al. (2025)** dispute Mikel-Hong et al. (2024) on neutralizing resistance (no OQs). See **O38** and **O31**.
- **Powell & DiMaggio (2023)** look back on their 1983 isomorphism paper; their open questions continue a forty-year conversation (**O16**, **O43**, **O48**).
- **Pozner & Hannigan (2023)** take up Jourdan's (2023) prompt to treat scandal as an audience-centred process (**O37**).
- **Hinds & von Krogh (2024)** extend Bailey et al.'s (2022) relational view of technology (**O26**, **O22**).
- **du Gay & Lopdrup Hjorth (2024)** argue against King and colleagues' metatheory of the organization as social actor (**O27**); **Mutch (2025)** answers the absence of law in Thornton et al. (2012) (**O39**, **O25**).
- Smaller replies: Lantela (2024) contests Decker's view of theory (**O32**); Ernst et al. (2026) build on Carter and Spence (2019) (**O11**); Kalkman (2026) extends Alpaslan and Mitroff (2021) (**O34**, **O40**).

## Notes for the lead

- Five conversations rest heavily on one article: **O24** (Leitzinger & Waeger, 27 of 32 OQs), **O07** (Guercini & Lechner, 9 of 19), **O26** (Hinds & von Krogh, 12 of 18), **O36** (Mena et al., 11 of 23) and **O01** (Brennecke et al., 17 of 32). Their recurrence is real but thinner than their OQ counts suggest.
- Three conversations are formal exchanges that the journal convened: **O22**, with **O15**, is the 5(3) GenAI set; **O44** is the 6(4) person-institution set; **O08** is the 5(4) Abend set. The 6(4) organizationality set (Dion et al.) is folded into **O05** and **O02**. The convening inflates commentary counts and citation edges for these conversations.
- Wright et al. (2023)-01 is coded `explicit_question` in the TSV, although its paraphrase calls it the paper's own research question; I kept it as open and placed it in **O11**.
