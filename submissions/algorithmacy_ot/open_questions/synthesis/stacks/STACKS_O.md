[Written by Opus (claude-opus-5-5), stage S13a, 2026-11-23]

# Stacks of open questions in *Organization Theory*, 2023–2026 (analyst O)

Run `ot-oq-2026-11`, stage S13a. I read all 605 open questions in `ot_open_questions_local/work/stacks/OPEN_QUESTIONS_BY_DATE.md` (65 pieces) and grouped them blind to the brief, the report, the earlier clustering and every fit or hand-check section. The ids match the 605 non-`own_research_question` rows of `QUESTIONS.tsv` exactly. The companion file `STACKS_O.tsv` holds one row per (question, stack).

## Counting rules

- **Band.** A piece belongs to 2025–26 if its "published online" date in the input starts with 2025 or 2026, and to 2023–24 otherwise. That puts 24 pieces in 2025–26 and 41 in 2023–24. Schildt & Kodeih (2025-02-24) and Patriotta et al. (dated "2025-11") fall in 2025–26.
- **Membership.** I assigned every question by reading its quotation and paraphrase. A question sits in one stack, or in two when it plainly asks two things. Of the 605 questions, 371 sit in one stack, 223 in two, and 11 are residual.
- **Pieces.** "Pieces asking" counts distinct articles with at least one member question in the band. Under each stack I list the backing pieces with their question numbers (for example, `mena2026 (19, 04)` means OQ-mena2026-19 and OQ-mena2026-04).
- **First authors.** I counted first authors as distinct surnames from the record key. All 65 pieces have different first authors, so this column equals the total number of pieces.
- **Editorial.** This column says whether `cornelissen2024` or `hollerer2026` has a member question.
- **Status** follows the brief: **prevailing** means three or more pieces in 2025–26, **persistent** means asked in both bands, **fading** means no piece since 2024, and **new** means 2025–26 only.
- **Ranking.** Stacks are ranked by 2025–26 pieces, then persistence, then most recent ask date, then (my tie-break) 2025–26 question count.
- **Extra columns, never summed.** I also report question counts per band and the "deep" 2025–26 pieces, those with three or more questions in the stack. These columns show whether a concern is a piece's agenda or a passing ask.
- **Quotations.** Anchors and context quotations are copied verbatim from the input, with their locators, and none exceeds 40 words.

## Ranked stacks

| Rank | Stack | Pieces 2025–26 | Pieces 2023–24 | Distinct first authors | Most recent ask | Editorial asks | Status | Qs 2025–26 | Qs 2023–24 | Deep pieces 2025–26 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | H. Time and trajectory | 9 | 11 | 20 | 2026-09-21 | no | prevailing + persistent | 33 | 13 | 5 |
| 2 | K. How organization theory theorizes | 9 | 17 | 26 | 2026-09-19 | hollerer2026, cornelissen2024 | prevailing + persistent | 27 | 60 | 3 |
| 3 | A. What an organization (or institution) is | 7 | 7 | 14 | 2026-09-19 | no | prevailing + persistent | 33 | 20 | 3 |
| 4 | F. The moral organization | 6 | 6 | 12 | 2026-09-19 | no | prevailing + persistent | 24 | 12 | 4 |
| 5 | I. Living with contradiction | 6 | 4 | 10 | 2026-07-28 | no | prevailing + persistent | 12 | 32 | 2 |
| 6 | E. Inequality and exclusion | 6 | 13 | 19 | 2026-07-21 | no | prevailing + persistent | 8 | 46 | 1 |
| 7 | B. How institutions arise, persist and change | 6 | 7 | 13 | 2025-12-23 | no | prevailing + persistent | 41 | 45 | 4 |
| 8 | C. Legitimacy under contestation | 6 | 4 | 10 | 2025-12-23 | no | prevailing + persistent | 20 | 18 | 2 |
| 9 | G. Imagined and sustainable futures | 5 | 3 | 8 | 2026-09-21 | no | prevailing + persistent | 36 | 13 | 4 |
| 10 | D. Democracy and voice | 4 | 6 | 10 | 2026-07-28 | no | prevailing + persistent | 31 | 28 | 2 |
| 11 | J. Technology and organizing | 4 | 14 | 18 | 2026-04-01 | cornelissen2024 | prevailing + persistent | 8 | 125 | 1 |
| 12 | L. Activism and resistance | 3 | 9 | 12 | 2026-03-31 | no | prevailing + persistent | 3 | 44 | 0 |
| 13 | M. Coordination and relations | 2 | 4 | 6 | 2026-07-28 | no | persistent | 22 | 28 | 1 |
| 14 | N. Affect and lived experience | 1 | 16 | 17 | 2026-04-01 | no | persistent | 2 | 33 | 0 |

### Which concerns prevail now

The table says every stack except M and N is "prevailing", because the brief's threshold of three pieces is low against 24 recent pieces. Depth separates them. Four concerns hold several deep 2025–26 pieces each, and I judge them the community's prevailing concerns now:

1. **A. What an organization (or institution) is.** Seven recent pieces ask it, three of them deep (schoeneborn2026, dion2025, derekrobinson2025), with 33 recent questions, and it is asked directly rather than as a side issue.
2. **B. How institutions arise, persist and change.** Six recent pieces ask it, four of them deep (nigam2025, derekrobinson2025, mutch2025, schildt2025), with 41 recent questions, the most of any stack.
3. **F. The moral organization.** Six recent pieces ask it, four of them deep (werner2026, kalkman2026, pavlisa2026, friedrich2026), and authors were still asking it in September 2026.
4. **K. How organization theory theorizes.** Nine recent pieces ask it, including the 2026 editorial, and it also has the longest history (17 pieces in 2023–24).

**H. Time and trajectory** ranks first under the rule and could count as a fifth. Almost all its questions also belong to another stack, though, so I treat it as the shared dimension of A and B (stages, persistence, reversal), not as a separate concern. **G. Imagined and sustainable futures** comes close: it has five recent pieces, four of them deep.

The other stacks are weaker than their status suggests. E (inequality) and J (technology) reach four to six recent pieces but hold only eight recent questions each, against 46 and 125 earlier: both have moved from agenda to aside. L (activism) clears the threshold on three one-question asks. Almost all of M's recent weight sits in one piece (brennecke2025), N persists through a single recent piece (friedrich2026), and N is fading in effect.

## 1. Stack H: Time and trajectory

**Concern.** How do organizational phenomena (ties, institutions, collective actorhood, crises) unfold, persist, reverse and end over time, and how can theory and data capture that?

**How 2025–26 askers put it.** Askers in 2025–26 put the question to specific objects. They ask which features of a tie's history are kept and which decay (brennecke2025), what criteria mark the stages of a person-institution and whether the process can run in reverse (derekrobinson2025, nigam2025), whether charging and discharging actorhood follows typical temporal patterns (schoeneborn2026), how arrangements trigger different notions of time (garud2025), and how past justifications shape responses to recurring crises (patriotta2025).

**How 2023–24 askers put it.** In 2023–24 the ask was mostly a general plea for process theory (hinds2024-01/-23, suddaby2024-01) or a temporal add-on to another framework (justesen2024-02/-03, stevenson2024-01). The question has moved from 'we need process theory' to object-specific questions about decay, reversal and stage criteria.

**Caution.** 41 of its 46 questions also sit in another stack. Time works more as a dimension of other concerns than as a concern of its own, and the ranking rule lifts it to first place on breadth.

**Counts.** Pieces in 2025–26: 9. Pieces in 2023–24: 11. Distinct first authors: 20. Most recent ask: 2026-09-21. Editorial: no. Status: prevailing + persistent. Questions: 33 in 2025–26 and 13 in 2023–24.

- 2025–26 pieces (question numbers): brennecke2025 (21, 20, 19, 16, 15, 12, 11, 10, 08, 04, 02); derekrobinson2025 (12, 11, 10, 09, 08, 02); dion2025 (07); garud2025 (07, 05, 04, 03); nigam2025 (11, 07, 06); patriotta2025 (07, 02); porsfelt2026 (08, 07); schoeneborn2026 (05, 03, 01); werner2026 (06)
- 2023–24 pieces (question numbers): hinds2024 (23, 01); justesen2024 (03, 02); krautzberger2024 (04); laine2023 (02); lantela2024 (03); ocasio2023 (03); powell2023 (04); sasaki2024 (05); seidemann2024 (12); stevenson2024 (01); suddaby2024 (01)

**Anchor questions (2025–26)**

- OQ-schoeneborn2026-05 [2026-09-19]: "The second question is whether there are any typical temporal patterns related to charging collectives with or discharging them of actorhood." (p. 14, "Conclusion and Research Agenda")
- OQ-derekrobinson2025-11 [2025-12-23]: "Under what conditions are transitions smooth or discrete?" (p. 9, "Conclusion")
- OQ-brennecke2025-12 [2025-09-28]: "Which features of relational history are retained, which decay over time? When do narratives about a tie crystallize into dominant accounts that guide behaviour? Under what conditions do memories of key events become shared across both parties" (p. 19, "Cognitive and narrative construction of relational history")
- OQ-patriotta2025-07 [2025-11]: "Studying recurrent or cyclical crises, such as repeated food safety scandals or recurring privacy controversies in the technology sector, could reveal how past justifications shape the repertoire of responses available to organizations in the future" (p. 18, "Future research directions: Legitimacy in a changing world")

**Context questions (2023–24)**

- OQ-hinds2024-01 [2024-10-29]: "we need a process theory that maps relations and functions at the outset and at the output stage" (p. 4, "A Relational Perspective on Generative AI")
- OQ-suddaby2024-01 [2024-10-28]: "Our profession could indeed still embrace processes more fully. Doing so would help us better incorporate notions of “is” and “was” into our theoretical frames." (p. 5, "Construct Clarity or Construct Clarification?")

## 2. Stack K: How organization theory theorizes

**Concern.** What counts as a good theory and a contribution in organization theory, who gets to produce it, and what reflexivity, methods and institutional support does it need?

**How 2025–26 askers put it.** In 2025–26 the 2026 editorial asks every submission to state its theoretical contribution and asks themed sections to go beyond the field's conventions (hollerer2026). Ernst et al. (2026) ask how field orthodoxies define good theory and whether inquiry can stay apart from political crisis. Giovannoni and Quattrone (2025) ask editors and reviewers to accept open-ended inquiry, and ask for methods that study absence. Schoeneborn et al. (2026) want shared foundations for a cumulative programme.

**How 2023–24 askers put it.** In 2023–24 the asks were about what theory is and who settles its words (suddaby2024, abend2024, prasad2024), whether LLMs can theorize and how authors must disclose their use (cornelissen2024), the place of imagination and values (gumusay2024), whose voices count (lantela2024), and the scholar's self (wright2023, petriglieri2023). The object has moved from defining theory, and from the disruption that LLMs might bring, to the institutional conditions (editors, reviewers, orthodoxies) that govern contribution. No 2025–26 piece repeats the LLM-in-theorizing questions.

**Counts.** Pieces in 2025–26: 9. Pieces in 2023–24: 17. Distinct first authors: 26. Most recent ask: 2026-09-19. Editorial: hollerer2026, cornelissen2024. Status: prevailing + persistent. Questions: 27 in 2025–26 and 60 in 2023–24.

- 2025–26 pieces (question numbers): brennecke2025 (07); corver2026 (09, 07); dion2025 (13, 05); ernst2026 (08, 07, 06, 05, 04, 03, 02, 01); friedrich2026 (18); giovannoni2025 (10, 09, 07, 06, 03); hollerer2026 (06, 05, 04, 03, 02, 01); keller2025 (01); schoeneborn2026 (02)
- 2023–24 pieces (question numbers): abend2024 (08, 07, 06, 05, 04, 03, 02); cornelissen2024 (10, 09, 08, 07, 06, 05, 04); fotaki2023 (05); friesl2023 (08); gumusay2024 (13, 12, 11, 06, 01); hinds2024 (24, 11); jorgensen2023 (06, 03); justesen2024 (10, 08, 07, 06, 05); laine2023 (09, 07, 04); lantela2024 (10, 09, 08, 04, 03); orlikowski2023 (05); petriglieri2023 (05, 04, 02, 01); powell2023 (14, 11); prasad2024 (07, 06, 04, 03); seidemann2024 (03); suddaby2024 (06, 05, 04, 03, 01); wright2023 (06, 05, 04, 03, 02)

**Anchor questions (2025–26)**

- OQ-hollerer2026-06 [2026-07-26]: "Submissions therefore also should clearly signal and communicate the nature of their theoretical contribution in relation to the existing literature." (p. 5, "What We Are Looking For")
- OQ-ernst2026-03 [2026-04-07]: "scholars could, as part of their reflexive research practices, benefit from paying attention to how orthodoxies in the field define what is currently considered good theory" (p. 15, "Theory generation in OS")
- OQ-giovannoni2025-07 [2025-08-22]: "And, of course, the institutional environment, comprising editors, reviewers and readers, would have to support and accept the integrity and fruitfulness of such efforts (rather than asking for them to be reframed in specific substantial terms, i.e. as ‘thing’)." (p. 15, "Discussion")
- OQ-ernst2026-07 [2026-04-07]: "Can we afford to divorce inquiry in academia from crisis at the political and geopolitical levels or from economic forces?" (p. 17, "Conclusions")

**Context questions (2023–24)**

- OQ-gumusay2024-11 [2024-03-28]: "help shed light on the many questions that are still unanswered, such as how our academic ecosystem might change to enable and encourage the role of imagination and values in the theorizing process." (p. 19, "A New Purpose for Theorizing")
- OQ-cornelissen2024-04 [2024-03-26]: "Rather, it is imperative that we engage in a debate about the implications of this potentially disruptive technology for our theorizing and for the kinds of knowledge that we in turn create about our various phenomena of interest." (p. 3, untitled introduction)
- OQ-abend2024-04 [2024-10-28]: "Fellow community members! Which aims should be served by our key words and distinctions? Which aims are more important to us, when, and where?" (p. 7, "5. Democracy, Unfreedom, Usefulness")

## 3. Stack A: What an organization (or institution) is

**Concern.** What makes something an organization or an institution, as distinct from other collectives and from persons, and where does organization theory's object end?

**How 2025–26 askers put it.** In 2025–26 the question is asked head-on. Organizationality is treated as graded and attributed: how do weakly organized collectives persist, and what is organizationality predicated of (schoeneborn2026, dion2025)? Three linked pieces argue over whether persons can be institutions (nigam2025, derekrobinson2025, hawbaker2025). Others ask what counts as a logic (schildt2025-02) and what dis/organization looks like beyond single organizations (winkler2025-04).

**How 2023–24 askers put it.** In 2023–24 new entrants put the object under strain. Askers wanted to know what organizations are once artificial persons join them (phillips2024-09) and what a team is under GenAI (hinds2024-09). Others asked whether an organization can exist while doing nothing (laine2023-02), when communities become organizations (georgiou2023-09), and whether formal organization still matters (dugay2024). The question has sharpened: the field once asked whether newcomers fit, and it now asks directly what the category is.

**Counts.** Pieces in 2025–26: 7. Pieces in 2023–24: 7. Distinct first authors: 14. Most recent ask: 2026-09-19. Editorial: no. Status: prevailing + persistent. Questions: 33 in 2025–26 and 20 in 2023–24.

- 2025–26 pieces (question numbers): derekrobinson2025 (15, 07, 03, 01); dion2025 (14, 13, 12, 11, 10, 09, 08, 06, 05, 04, 03, 02); hawbaker2025 (04, 03); nigam2025 (03, 01); schildt2025 (02); schoeneborn2026 (10, 09, 08, 07, 06, 05, 04, 03, 02, 01); winkler2025 (05, 04)
- 2023–24 pieces (question numbers): arnold2023 (04); dugay2024 (07, 06, 05, 04, 02); georgiou2023 (11, 10, 09, 03); hinds2024 (09); laine2023 (09, 08, 07, 06, 05, 04, 02); phillips2024 (09); stark2024 (08)

**Anchor questions (2025–26)**

- OQ-schoeneborn2026-09 [2026-09-19]: "our theory invites researchers in this field to trace and identify the emergence and maintenance of organizationality in various parts of society, including but not limited to markets, communities, movements, and families" (p. 14, "Conclusion and Research Agenda")
- OQ-schoeneborn2026-03 [2026-09-19]: "Our framework then raises follow-up questions, for instance, how loose and fluid social phenomena can sustain their existence despite a rather low degree of organizationality." (p. 13, "Dynamizing Organizationality")
- OQ-dion2025-14 [2025-12-26]: "When discussing organizationality, the following question should be asked: The organizationality of what?" (p. 16, "Conclusion")
- OQ-hawbaker2025-03 [2025-12-01]: "If we can identify individuals as something other than institutions we can more cogently examine the relationships between those things and institutions, without making every(one) an institution." (p. 9, "Discussion")

**Context questions (2023–24)**

- OQ-phillips2024-09 [2024-09-13]: "How does the introduction of artificial persons into an organization change how we think about what organizations are, how they are constructed and how they function?" (p. 11, "The implications of generative AI in organizations")
- OQ-laine2023-02 [2023-02-18]: "Is it unthinkable for organization theory that different relational effects at a different time and in a different place still yield the same organization? Is it not possible for an organization to “not do” anything at all?" (p. 11, "For whom objects matter")
- OQ-hinds2024-09 [2024-10-29]: "We may even need to ask what it means to be a team in the world of GenAI." (p. 9, "Team coordination")

## 4. Stack F: The moral organization

**Concern.** What makes an organization moral: how are its character, purpose, care and responsibility formed, and by what standard should they be judged?

**How 2025–26 askers put it.** In 2025–26 askers build positive normative theory and ask for its empirical test. Werner et al. (2026) ask about moral scope, character change and how to judge reasoning beyond prescribed norms. Kalkman (2026) asks about a care-based purpose for crisis management. Pavlisa et al. (2026) ask which stakeholders a firm answers to. Schoeneborn et al. (2026) ask what shifting actorhood means for individual and collective responsibility, and Friedrich (2026) asks about care for more-than-human others.

**How 2023–24 askers put it.** In 2023–24 the ask was mostly a critique: paradox research should judge responses normatively (seidemann2024), theory should be syncretic and normative (suddaby2024-04), care is shaped by power (fotaki2023), and someone must answer who is accountable for algorithmic decisions (stark2024-04). The question has moved from 'admit normativity' to 'theorize the organization as a moral agent and test it'.

**Counts.** Pieces in 2025–26: 6. Pieces in 2023–24: 6. Distinct first authors: 12. Most recent ask: 2026-09-19. Editorial: no. Status: prevailing + persistent. Questions: 24 in 2025–26 and 12 in 2023–24.

- 2025–26 pieces (question numbers): friedrich2026 (13, 10, 09); kalkman2026 (08, 07, 06, 05, 04, 03, 02, 01); patriotta2025 (04); pavlisa2026 (06, 04, 03); schoeneborn2026 (06); werner2026 (10, 09, 08, 07, 06, 05, 04, 03)
- 2023–24 pieces (question numbers): fotaki2023 (07, 06, 04, 03); jaser2024 (04); scherer2023 (06, 04); seidemann2024 (15, 09, 08); stark2024 (04); suddaby2024 (04)

**Anchor questions (2025–26)**

- OQ-werner2026-10 [2026-04-01]: "Another question that further normative research might explore is how, when organizations deliberate beyond institutionally prescribed norms and obligations, this can be ethically judged in specific instances and cases." (pp. 21–22, "Theoretical and research implications")
- OQ-werner2026-09 [2026-04-01]: "one question that further research might pursue is whether the depth and breadth of an organization’s moral reasoning is connected to specific legitimate ethical positions, content-wise, that organizations take up in society (Selznick, 2008)." (p. 21, "Theoretical and research implications")
- OQ-schoeneborn2026-06 [2026-09-19]: "What does the recurrent charging or discharging of a collective social address with actorhood imply for individual as opposed to collective responsibility?" (p. 14, "Conclusion and Research Agenda")
- OQ-kalkman2026-03 [2026-07-21]: "a crisis can trigger moral self-reflection on the organization’s role and functioning, and it would be interesting to learn more about the conditions that facilitate such reflection." (p. 15, "Implications for Empirical Research")

**Context questions (2023–24)**

- OQ-seidemann2024-08 [2024-10-18]: "Expanding on the predominantly strategic perspective of paradox management, the question of how responses to paradoxes are evaluated from a normative standpoint becomes central." (p. 17, "Purposefully integrating normative approaches")
- OQ-fotaki2023-03 [2023-03-11]: "it is vital to theorize how power asymmetries among genders, races, ethnicities and social classes within and across geographical locales shape care relations, forms of care, and experiences of caring and being cared for in fundamental ways" (p. 14, "Discussion")
- OQ-jaser2024-04 [2024-03-19]: "What kind of managers and workers do people want to be? What value do we attribute to humanity in the workplace, to the human moments that comes with human workers (such as speaking to a customer when delivering mail)?" (p. 17, "Conclusion")

## 5. Stack I: Living with contradiction

**Concern.** When are contradiction, dissent and paradox productive rather than destructive, and how do organizations navigate them?

**How 2025–26 askers put it.** In 2025–26 the question appears outside paradox theory. Mena et al. (2026) ask when dissent stays productive and when consensus is unnecessary. Skade (2025) asks how actors handle tensions between futures, Schildt and Kodeih (2025) ask about contradiction within a single logic, Patriotta et al. (2025) consider incommensurable values, and Corver and Filler (2026) consider disagreement in modelling. Paradox theory proper appears only in Keller et al. (2025).

**How 2023–24 askers put it.** In 2023–24 the asks came from paradox theory's own agenda: portfolios of both/and and either/or responses (krautzberger2024), and the boundary conditions, normativity and ontology of paradox (seidemann2024). Community-logic tensions came up as well (georgiou2023). The object has moved from paradox as a theory to dissent and contestation as conditions of organizing.

**Counts.** Pieces in 2025–26: 6. Pieces in 2023–24: 4. Distinct first authors: 10. Most recent ask: 2026-07-28. Editorial: no. Status: prevailing + persistent. Questions: 12 in 2025–26 and 32 in 2023–24.

- 2025–26 pieces (question numbers): corver2026 (16); keller2025 (02, 01); mena2026 (22, 08, 07); patriotta2025 (12); schildt2025 (06); skade2025 (07, 06, 02, 01)
- 2023–24 pieces (question numbers): georgiou2023 (08, 06, 05, 04); krautzberger2024 (13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03); seidemann2024 (16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); stark2024 (05)

**Anchor questions (2025–26)**

- OQ-mena2026-08 [2026-03-31]: "How can we ensure that dissent remains continuously productive and does not become destructive, for example, by deepening fractures among organizational members or even leading to organizational death?" (p. 12, "Agonistic internal focus")
- OQ-mena2026-22 [2026-03-31]: "Under what conditions may dissensus be nonessential, and for what types of outcomes?" (p. 20, "Comparative analysis across perspectives")
- OQ-skade2025-02 [2025-09-27]: "to enable researchers to better understand how actors perceive and manage tensions between organizational futures linked to grand challenges." (p. 18, "Tensions within contexts: Grand challenges")
- OQ-schildt2025-06 [2025-02-24]: "We hope our practice-centric perspective on institutional logics can inspire scholars to study contradictions, variations, and change also within a single institutional logic." (p. 17, "Concluding remarks")

**Context questions (2023–24)**

- OQ-seidemann2024-11 [2024-10-18]: "I recommend that paradox scholars empirically explore the boundary conditions of both/and for different classes of phenomena at different levels of analysis and the potential negative ramifications of embracing tensions." (p. 18, "Developing a more granular perspective")
- OQ-krautzberger2024-12 [2024-11-08]: "Fourth, and more broadly, paradox studies could explore the undesired outcomes and failures of organizations in pursuing a meta-both/and approach." (p. 20, "Directions for future research")

## 6. Stack E: Inequality and exclusion

**Concern.** How do organizations and institutions produce, reproduce or reduce inequality, marginalization and otherness?

**How 2025–26 askers put it.** In 2025–26 only Pavlisa et al. (2026) make inequality the object, asking how stakeholder structures create advantage and disadvantage. Elsewhere it enters as a moderator: does the theory vary by race, gender, class and geography (hawbaker2025-02, derekrobinson2025-13)? Who is vulnerable in a crisis (kalkman2026-05)? Do DEI measures reduce domination (mena2026-04)?

**How 2023–24 askers put it.** In 2023–24 it was the central object of several pieces: otherness and denied speaking positions (arnold2023), cultural marginalization (sasaki2024), voices missing from the canon (lantela2024), equity in open strategy (langenmayr2024), and shame and stigma (bacq2023). The concern has moved from central object to boundary condition. It reaches six recent pieces but holds 8 recent questions, against 46 earlier.

**Caution.** It is prevailing by piece count but thin by depth.

**Counts.** Pieces in 2025–26: 6. Pieces in 2023–24: 13. Distinct first authors: 19. Most recent ask: 2026-07-21. Editorial: no. Status: prevailing + persistent. Questions: 8 in 2025–26 and 46 in 2023–24.

- 2025–26 pieces (question numbers): derekrobinson2025 (13); friedrich2026 (04); hawbaker2025 (02); kalkman2026 (05); mena2026 (04); pavlisa2026 (06, 05, 02)
- 2023–24 pieces (question numbers): arnold2023 (13, 12, 11, 10, 08, 07, 06, 05, 04, 03, 02, 01); bacq2023 (10, 08, 07, 06, 02, 01); fotaki2023 (04, 03); hinds2024 (15); jackwerthrice2023 (10); jaser2024 (03); langenmayr2024 (09, 07, 06, 05, 04, 03, 01); lantela2024 (11, 09, 06, 05, 04); leitzinger2023 (31, 30); orlikowski2023 (08); sasaki2024 (06, 05, 04, 03, 02, 01); seidemann2024 (10); whyte2023 (11)

**Anchor questions (2025–26)**

- OQ-pavlisa2026-06 [2026-06-19]: "A critical area of inquiry surrounds how firms and their leaders leverage a stakeholder approach (Doh & Quigley, 2014) and implement strategies to mitigate their contributions to widening economic and social inequalities (Bapuji et al., 2018)." (p. 19, "Managerial implications")
- OQ-pavlisa2026-05 [2026-06-19]: "extending the analysis toward how organisational and industry-level structures of competing organisations and networks of cooperating organisations imbued with their own internal power structures, create systems of advantage and disadvantage that reinforce inequalities." (p. 19, "Discussion")
- OQ-hawbaker2025-02 [2025-12-01]: "Race, gender, class, and geography are heavily implicated in the creation of institutional mythologies." (p. 9, "Discussion")
- OQ-mena2026-04 [2026-03-31]: "Do DEI measures reduce managerial authority over minorities? Do they increase solidarity among the workforce?" (p. 11, "Republican internal focus")

**Context questions (2023–24)**

- OQ-arnold2023-01 [2023-09-30]: "We call for research to draw more attention to the most under-privileged and excluded people in societies – people whose status as a speaking being is denied." (p. 14, "An agenda for otherness research")
- OQ-langenmayr2024-04 [2024-09-18]: "we know little about the reproduction of power relations through traditional strategy actors’ control and management of diversity" (p. 10, "Reproducing power relations through managing diversity")

## 7. Stack B: How institutions arise, persist and change

**Concern.** How do institutions and logics arise, persist, travel and change, and how does stable macro order come out of local practice, persons, law and hype?

**How 2025–26 askers put it.** Askers in 2025–26 locate institutions in particular carriers. Schildt and Kodeih (2025) ask how stable macro logics arise from local practice, and Mutch (2025) asks how practices move between law and organizations. Nigam et al. (2025) and Derek Robinson and Atanasova (2025) ask why, when and for how long persons become institutions, and what happens at their death. Wedlin and Weinryb (2025) ask how hype acts on institutions.

**How 2023–24 askers put it.** In 2023–24 the asks were about classic mechanisms: what diffuses and why some practices stick (powell2023), the cross-level construction of institutions (ocasio2023), the centrality and purity of logics (stevenson2024, godart2024), the resources of institutional entrepreneurs (jackwerthrice2023), and displacement by digitalization (orlikowski2023). The question has moved from mechanisms of diffusion and entrepreneurship to the carriers that make institutions last.

**Counts.** Pieces in 2025–26: 6. Pieces in 2023–24: 7. Distinct first authors: 13. Most recent ask: 2025-12-23. Editorial: no. Status: prevailing + persistent. Questions: 41 in 2025–26 and 45 in 2023–24.

- 2025–26 pieces (question numbers): derekrobinson2025 (15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 02, 01); hawbaker2025 (02, 01); mutch2025 (06, 05, 04, 03, 02, 01); nigam2025 (11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); schildt2025 (07, 06, 05, 04, 03, 02); wedlin2025 (04, 03)
- 2023–24 pieces (question numbers): georgiou2023 (12, 11, 08, 07, 06, 04, 02); godart2024 (06, 05, 04, 02); jackwerthrice2023 (11, 10, 09, 08, 07, 06, 05, 04, 03, 02); ocasio2023 (04, 03, 02, 01); orlikowski2023 (06, 01); powell2023 (13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); stevenson2024 (05, 04, 03, 02, 01)

**Anchor questions (2025–26)**

- OQ-schildt2025-03 [2025-02-24]: "We thus call for future research to examine how diverse aspects of institutional logics that, from afar, look like macro-level ideology and tradition with significant stability may arise from local dynamic processes." (p. 16, "Towards a more dynamic and local view")
- OQ-nigam2025-11 [2025-12-06]: "We hope that others will take on these ideas and push forward why, how, when and for how long individuals can become institutions." (p. 9, "Conclusion")
- OQ-derekrobinson2025-12 [2025-12-23]: "Is the process always uni-directional or can it run in reverse?" (p. 9, "Conclusion")
- OQ-mutch2025-03 [2025-04-25]: "Recognizing law as a central institutional logic directs our attention to the possibility for practices to be transferred from the legal to the organizational domain (and vice versa)." (p. 13, "Conclusion")

**Context questions (2023–24)**

- OQ-powell2023-09 [2023-12-21]: "How do new ideas and practices enter organizations and stick? Why do new kinds of institutions emerge, take root, and persist? When are organizations more vulnerable to changes in the wider environment and when are they resisted?" (p. 15, "Institutional change")
- OQ-stevenson2024-01 [2024-06-14]: "Scholars could, for instance, study the stability of the centrality of one logic over time, space and actors." (p. 12, "Discussion and Conclusion")

## 8. Stack C: Legitimacy under contestation

**Concern.** How do audiences, media and platforms make, test and unmake legitimacy? When does an issue escalate into controversy, scandal or hype, and how does a polarized, post-truth environment change this?

**How 2025–26 askers put it.** In 2025–26 the asks set legitimacy in a contested environment: early warning signs of escalation, and pre-emptive justification (patriotta2025), the escalating dis/organization of post-truth communication (winkler2025), hype (wedlin2025), and rhetoric under truth-bending autocrats (giovannoni2025-08).

**How 2023–24 askers put it.** In 2023–24 the asks were about how audiences construct scandal (pozner2023), how many audiences an organization must please to survive (godart2024-03), and how firms differ while keeping legitimacy (powell2023-07). The question has moved from audience-centred scandal to contestation under polarization and post-truth.

**Counts.** Pieces in 2025–26: 6. Pieces in 2023–24: 4. Distinct first authors: 10. Most recent ask: 2025-12-23. Editorial: no. Status: prevailing + persistent. Questions: 20 in 2025–26 and 18 in 2023–24.

- 2025–26 pieces (question numbers): derekrobinson2025 (06); giovannoni2025 (08); hawbaker2025 (01); patriotta2025 (12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02); wedlin2025 (04, 03); winkler2025 (06, 05, 03, 02)
- 2023–24 pieces (question numbers): godart2024 (04, 03); grodal2024 (02); powell2023 (08, 07, 06); pozner2023 (16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 04)

**Anchor questions (2025–26)**

- OQ-patriotta2025-05 [2025-11]: "While our theory highlights that legitimacy tests are dynamic and processual, we know little about the early warning signs that indicate when an issue may escalate into a full-blown controversy versus blowing over." (p. 18, "Future research directions: Legitimacy in a changing world")
- OQ-patriotta2025-11 [2025-11]: "this paper provides a foundation for future research on how organizations and societies co-create the boundaries of legitimacy in an increasingly complex and contested world." (p. 19, "Conclusion")
- OQ-winkler2025-02 [2025-11-11]: "In this article we argue that PTC should be a topic of serious concern for organizational scholarship." (p. 2, introduction)
- OQ-wedlin2025-03 [2025-12-23]: "We hope that our model of hype as a process of translation will spur a variety of empirical investigations, further exploring the institutional dynamics of hype and its potentially disruptive institutional consequences." (p. 17, "Concluding Discussion")

**Context questions (2023–24)**

- OQ-pozner2023-06 [2023-09-30]: "we know little about the dynamics through which social groups make sense of the information—good or bad—that informs their evaluations." (p. 13, "Discussion")
- OQ-pozner2023-15 [2023-09-30]: "Empirical work might explicitly consider social media’s role in social evaluation (Etter et al., 2019; Seidel et al., 2020) and compare scandal construction before and after the widespread adoption of social media." (p. 16, "Future directions")

## 9. Stack G: Imagined and sustainable futures

**Concern.** How do organizations and their members imagine and enact futures, including desirable and sustainable ones under grand challenges, and with what effect on present decisions?

**How 2025–26 askers put it.** In 2025–26 the asks concern actors' own future-making. Porsfelt et al. (2026) ask what triggers in-situ collective imagination, Skade (2025) asks how divergent futures shape strategy, Corver and Filler (2026) ask how sustainability problems are modelled, and Friedrich (2026) asks how organizing can attune to ecological interdependence.

**How 2023–24 askers put it.** In 2023–24 the ask was mostly that scholars themselves theorize desirable futures (gumusay2024), which Lantela (2024-08) and Whyte et al. (2023-05) echo. The object has moved from the scholar's prospective theorizing to how organizations imagine and enact futures.

**Caution.** It has five recent pieces and four of them are deep (36 recent questions), so it runs close behind the prevailing group.

**Counts.** Pieces in 2025–26: 5. Pieces in 2023–24: 3. Distinct first authors: 8. Most recent ask: 2026-09-21. Editorial: no. Status: prevailing + persistent. Questions: 36 in 2025–26 and 13 in 2023–24.

- 2025–26 pieces (question numbers): corver2026 (15, 14, 13, 12, 10, 08, 06, 05); friedrich2026 (16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02); giovannoni2025 (05); porsfelt2026 (09, 08, 07, 06, 05, 04); skade2025 (07, 05, 04, 03, 02, 01)
- 2023–24 pieces (question numbers): gumusay2024 (12, 11, 10, 09, 08, 06, 05, 04, 03, 02, 01); lantela2024 (08); whyte2023 (05)

**Anchor questions (2025–26)**

- OQ-porsfelt2026-07 [2026-09-21]: "For organisation studies, this raises questions about how such moments are triggered, how they draw on and reconfigure existing images and cultural resources, and how they can be consequential without forming durable meaning structures." (p. 24, "Moving Forward")
- OQ-skade2025-01 [2025-09-27]: "future research could clarify how these divergent futures inform strategic decisions and create productive tensions within organizations." (p. 18, "Tensions between futures")
- OQ-friedrich2026-11 [2026-04-01]: "In what ways should organizational meetings be structured to invite collective imagination and creative, poetic, and aesthetic experimentation in envisioning desirable futures?" (p. 14, "Affirmative ethical responsiveness")
- OQ-corver2026-06 [2026-07-28]: "Do organizations typically move from addressing discrete, separate sustainability problems toward recognizing and managing increasingly interconnected ones" (p. 17, "Discussion")

**Context questions (2023–24)**

- OQ-gumusay2024-02 [2024-03-28]: "For instance, how would different climate pathways impact organizing differently, including the behaviour of people and institutions?" (p. 9, "Four modes of theorizing the future")
- OQ-gumusay2024-11 [2024-03-28]: "help shed light on the many questions that are still unanswered, such as how our academic ecosystem might change to enable and encourage the role of imagination and values in the theorizing process." (p. 19, "A New Purpose for Theorizing")

## 10. Stack D: Democracy and voice

**Concern.** Who governs and who has a voice: how can organizations be democratic and inclusive, and how does organizational democracy connect to democracy in society?

**How 2025–26 askers put it.** In 2025–26 Mena et al. (2026) pose 23 questions: who counts as the demos, when consensus is needed, and how right-wing politics and democratic backsliding interact with workplace democracy. Friedrich (2026) asks how democratic organizing can resist co-optation and include ecological others. Corver and Filler (2026) ask about participatory governance.

**How 2023–24 askers put it.** In 2023–24 the asks were about inclusion and self-selection in open strategy (langenmayr2024, friesl2023), organized maturity and digital civic spaces (scherer2023), and democratic oversight of surveillance (jaser2024-06). The question has moved from participation in strategy-making to democracy as a concept with society-level spillovers. Its recent weight rests mostly on one piece.

**Counts.** Pieces in 2025–26: 4. Pieces in 2023–24: 6. Distinct first authors: 10. Most recent ask: 2026-07-28. Editorial: no. Status: prevailing + persistent. Questions: 31 in 2025–26 and 28 in 2023–24.

- 2025–26 pieces (question numbers): corver2026 (05); friedrich2026 (17, 16, 15, 14, 12, 11); mena2026 (23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); pavlisa2026 (02)
- 2023–24 pieces (question numbers): arnold2023 (13, 06); friesl2023 (09, 08, 07, 06, 05, 04, 03); gumusay2024 (08, 03); jaser2024 (06); langenmayr2024 (11, 10, 09, 08, 07, 05, 04, 02, 01); scherer2023 (13, 11, 10, 09, 08, 06, 04)

**Anchor questions (2025–26)**

- OQ-mena2026-01 [2026-03-31]: "who qualifies as the people (or demos; Koenig-Archibugi, 2022): employees, a larger set of organizational members and/or stakeholders, or a broader demos?" (p. 3, introduction)
- OQ-mena2026-07 [2026-03-31]: "more inquiry into the preconditions of consensus is required, as well as consideration regarding when sub-optimal (or non-consensual) decisions can be sufficient without hindering organizational democracy" (p. 12, "Deliberative internal focus")
- OQ-friedrich2026-16 [2026-04-01]: "Little research has explored how democratic organizing can mitigate its vulnerabilities to ideological co-optation and, especially, how it might connect with ecological others while sustaining its power-sensitive and egalitarian potential." (p. 5, "Organizational Democracy’s Disconnects")
- OQ-corver2026-05 [2026-07-28]: "One open conceptual question, for instance, is how a more open, co-creative approach to modeling interacts with more democratic decision-making processes and participatory governance structures" (p. 17, "Discussion")

**Context questions (2023–24)**

- OQ-langenmayr2024-01 [2024-09-18]: "Adopting an equity-based approach would thus allow open strategy scholars to explore the relation between traditional actors’ dominance and control over inclusion and the reproduction of inequalities." (p. 6, "Normalizing through traditional strategy actors’ control over inclusion")
- OQ-friesl2023-03 [2023-06-25]: "Unveiling the social processes underpinning self-selection allows future research to study why certain actors participate in open strategy or why they abstain from doing so." (p. 13, "Discussion and Theoretical Implications")

## 11. Stack J: Technology and organizing

**Concern.** How do digital technologies, generative AI and algorithms among them, change organizing, work, coordination, and the social construction of categories and legitimacy?

**How 2025–26 askers put it.** In 2025–26 the stack holds four pieces and 8 questions, each a side ask inside another concern: technology co-producing legitimacy tests (patriotta2025), social media and AI in deliberation (mena2026-12), innovation under GenAI (garud2025), and technology in power-laden assemblages (friedrich2026-17).

**How 2023–24 askers put it.** In 2023–24, 14 pieces asked 125 questions. GenAI encapsulating coordination (hinds2024), the human–machine boundary (grodal2024), categories (phillips2024, hsu2024), algorithmic management (stark2024), LLMs in theorizing (cornelissen2024), surveillance (jaser2024, scherer2023), invisible digi-work (justesen2024), online/offline work (whyte2023) and digital undertow (orlikowski2023) each drew questions. Technology has moved from a dedicated topic to an environmental condition inside other concerns.

**Caution.** No 2025–26 piece re-asks the workplace-surveillance strand (jaser2024, scherer2023) or the GenAI-in-teams strand (hinds2024, phillips2024-07). Both strands are fading.

**Counts.** Pieces in 2025–26: 4. Pieces in 2023–24: 14. Distinct first authors: 18. Most recent ask: 2026-04-01. Editorial: cornelissen2024. Status: prevailing + persistent. Questions: 8 in 2025–26 and 125 in 2023–24.

- 2025–26 pieces (question numbers): friedrich2026 (17, 08); garud2025 (10, 08, 06); mena2026 (12); patriotta2025 (10, 08)
- 2023–24 pieces (question numbers): cornelissen2024 (10, 09, 08, 07, 06, 05, 04); grodal2024 (09, 08, 07, 06, 05, 04, 03, 02); hinds2024 (25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); hsu2024 (08, 06, 05, 04, 02, 01); jaser2024 (11, 10, 09, 08, 07, 06, 05, 04, 03, 02); justesen2024 (17, 16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); leitzinger2023 (10, 09); orlikowski2023 (09, 08, 07, 06, 05, 02, 01); phillips2024 (16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05); pozner2023 (15); scherer2023 (13, 09, 08, 07, 05, 02); stark2024 (09, 08, 07, 06, 05, 04, 03, 02, 01); suddaby2024 (06, 05); whyte2023 (14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02)

**Anchor questions (2025–26)**

- OQ-patriotta2025-10 [2025-11]: "suggesting the need to examine how legitimacy tests are co-produced by both human and technological actors in the contemporary digital landscape." (p. 19, "Future research directions: Legitimacy in a changing world")
- OQ-mena2026-12 [2026-03-31]: "How do new technologies, such as social media and AI, shape deliberations outside and, in turn, within organizations?" (p. 14, "Deliberative outside-in focus")
- OQ-garud2025-08 [2025-07-11]: "The challenge moving forward is to develop more nuanced approaches to organizing for innovation, recognizing the complex, interdependent relationship between exploration and exploitation given the pitfalls and possibilities offered by these new technologies." (p. 16, "Future research on innovation at work in the age of digital technologies and Gen AI")
- OQ-friedrich2026-17 [2026-04-01]: "This dual role demands the utmost critical scrutiny in future research, as technological instruments—biotech, AI, military applications, green tech, and so on—are themselves entangled in power-laden assemblages." (p. 19, "Posthuman feminism for organization theory")

**Context questions (2023–24)**

- OQ-phillips2024-15 [2024-09-13]: "we still have a lot more to do to really take technology seriously in many research streams of organization theory." (p. 16, "Conclusions")
- OQ-stark2024-04 [2024-06-18]: "But who or what is accountable when an algorithm exercises decisions that occur faster and with a vastly larger number of inputs than a human can physiologically comprehend and react to (Vesa & Tienari, 2022, p. 1137)?" (p. 14, "Accountability")
- OQ-hinds2024-16 [2024-10-29]: "as progressive encapsulation evolves across levels and functions in organizations, how does the process shape the division of labor?" (p. 10, "Discussion")

## 12. Stack L: Activism and resistance

**Concern.** When and how do activism, social movements and resistance emerge, and what do they do to firms, markets and institutions?

**How 2025–26 askers put it.** In 2025–26 the stack holds three single asks: CEO sociopolitical activism (mena2026-19), activists and whistleblowers shaping legitimacy tests (patriotta2025-09), and political contestation over versions of logics (schildt2025-05).

**How 2023–24 askers put it.** In 2023–24 Leitzinger and Waeger (2023) set out a 33-question agenda on market-targeting movements. Other pieces asked about resistance to surveillance (jaser2024), professionals resisting algorithms (stark2024-02), and scandal and movements (pozner2023-10/-12). Activism now survives only as an input to legitimacy and democracy questions.

**Caution.** It meets the prevailing rule only on three one-question asks. The market-movement agenda has not been re-asked since 2023 and is fading.

**Counts.** Pieces in 2025–26: 3. Pieces in 2023–24: 9. Distinct first authors: 12. Most recent ask: 2026-03-31. Editorial: no. Status: prevailing + persistent. Questions: 3 in 2025–26 and 44 in 2023–24.

- 2025–26 pieces (question numbers): mena2026 (19); patriotta2025 (09); schildt2025 (05)
- 2023–24 pieces (question numbers): bacq2023 (01); hinds2024 (14); jaser2024 (11, 09, 07); justesen2024 (12); leitzinger2023 (33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); pozner2023 (12, 10); sasaki2024 (03); seidemann2024 (06); stark2024 (02)

**Anchor questions (2025–26)**

- OQ-mena2026-19 [2026-03-31]: "it would be interesting to examine the opposite process: how organizations challenge the hegemonic status quo, for instance through CEO sociopolitical activism." (p. 16, "Agonistic inside-out focus")
- OQ-patriotta2025-09 [2025-11]: "it is worth exploring how non-traditional actors, such as social media influencers, activists and whistleblowers, increasingly shape and amplify legitimacy tests by rapidly mobilizing audiences." (p. 19, "Future research directions: Legitimacy in a changing world")
- OQ-schildt2025-05 [2025-02-24]: "We focus particularly on the study of contemporary political efforts to advocate and advance competing versions of societal and field-level institutional logics" (p. 15, "Discussion and Conclusion")

**Context questions (2023–24)**

- OQ-leitzinger2023-01 [2023-06-23]: "Key questions remain as to how social movements that target markets and their actors form or, if already established, become mobilized to address new issues." (p. 7, "Phase 1: Emergence")
- OQ-stark2024-02 [2024-06-18]: "The study of the dynamics of the relations between professional expertise and algorithmic practices is in its infancy. Under what conditions can we expect resistance by professionals to incursions by algorithmic practices? When are compromises likely?" (p. 9, "Object of management")

## 13. Stack M: Coordination and relations

**Concern.** How are coordination and collaboration accomplished through relations, roles, space and interaction?

**How 2025–26 askers put it.** In 2025–26 the stack holds Brennecke et al. (2025), with 21 questions on tie histories, brokerage and multiplexity, and one question on roles (corver2026-11).

**How 2023–24 askers put it.** In 2023–24 the asks were about coordinating through space (racker2024), GenAI and team coordination (hinds2024), presence across online and offline settings (whyte2023), and AI teammates (phillips2024-07). The stack persists below the prevailing threshold, and nearly all its recent weight sits in one piece.

**Counts.** Pieces in 2025–26: 2. Pieces in 2023–24: 4. Distinct first authors: 6. Most recent ask: 2026-07-28. Editorial: no. Status: persistent. Questions: 22 in 2025–26 and 28 in 2023–24.

- 2025–26 pieces (question numbers): brennecke2025 (21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); corver2026 (11)
- 2023–24 pieces (question numbers): hinds2024 (25, 19, 18, 08, 07, 06, 05, 04, 03); phillips2024 (07); racker2024 (12, 11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01); whyte2023 (14, 13, 12, 09, 08, 02)

**Anchor questions (2025–26)**

- OQ-brennecke2025-14 [2025-09-28]: "future research can explore how the biographies of individual ties interact with structural properties such as brokerage, centrality, constraint, network status" (p. 19, "Relational history and broader network structures")
- OQ-brennecke2025-03 [2025-09-28]: "Future research might explore how brokers interpret and narrate these tie histories as part of their behavioural repertoire, and how actors' awareness of tie histories influences the perceived appropriateness and success of brokerage efforts." (p. 13, "Relational history and brokerage")
- OQ-corver2026-11 [2026-07-28]: "Is the capacity for problem reframing, for instance, distributed differently across organizational roles than the capacity for reflexive evaluation" (p. 17, "Discussion")

**Context questions (2023–24)**

- OQ-racker2024-10 [2024-08-27]: "Thus, we need to better understand how different coordinating mechanisms (here: roles, space, routines) interact in achieving successful integration." (p. 13, "Interrelations")
- OQ-hinds2024-25 [2024-10-29]: "We need theorizing that captures what shapes team participants' dynamic relations with AI to coordinate their work." (p. 8, "Team coordination")

## 14. Stack N: Affect and lived experience

**Concern.** How do emotion, affect, identity and lived experience shape organizing and its exclusions?

**How 2025–26 askers put it.** In 2025–26 only Friedrich (2026-06/-07) asks this, about affective and sensory attunement to more-than-human life.

**How 2023–24 askers put it.** In 2023–24, 16 pieces asked it: shame and other emotions (bacq2023), affect and otherness (arnold2023), care (fotaki2023), atmospheres (jorgensen2023), myths and psychic needs (paca2024), lived experience of digital work (justesen2024), psychological responses to GenAI (hinds2024-21/-22), and scholars' selves (wright2023, petriglieri2023).

**Caution.** It is persistent on a single recent piece and is fading in effect.

**Counts.** Pieces in 2025–26: 1. Pieces in 2023–24: 16. Distinct first authors: 17. Most recent ask: 2026-04-01. Editorial: no. Status: persistent. Questions: 2 in 2025–26 and 33 in 2023–24.

- 2025–26 pieces (question numbers): friedrich2026 (07, 06)
- 2023–24 pieces (question numbers): arnold2023 (12, 10, 07); bacq2023 (09, 06, 05, 04, 03); fotaki2023 (07, 05); georgiou2023 (05); godart2024 (06); hinds2024 (22, 21); jaser2024 (02); jorgensen2023 (07, 06, 05, 04, 03); justesen2024 (13, 11); krautzberger2024 (11); leitzinger2023 (13, 02); ocasio2023 (01); paca2024 (05, 04, 03, 02); petriglieri2023 (05); powell2023 (10); wright2023 (05)

**Anchor questions (2025–26)**

- OQ-friedrich2026-07 [2026-04-01]: "How can affective connections to life forces (zoe) be cultivated as the organization fosters proximity and entanglement with more-than-human others" (p. 13, "Attuning to zoe/geo/techno spheres")
- OQ-friedrich2026-06 [2026-04-01]: "Which spaces, moments, and routines can be created to slow down or de-focus and extend the rational mind while activating multiple bodily senses" (p. 13, "Attuning to zoe/geo/techno spheres")

**Context questions (2023–24)**

- OQ-arnold2023-10 [2023-09-30]: "it is tantamount for otherness research to focus much more strongly on the realm of affect. Only in this way can we understand how a specific social order casts certain people as Other." (p. 15, "An agenda for otherness research")
- OQ-fotaki2023-07 [2023-03-11]: "This requires delving into the relationship between the business models neoliberalism propagates, how these are affectively appropriated and how they impact different bodies." (p. 13, "Discussion")
- OQ-bacq2023-05 [2023-02-18]: "Future research may therefore helpfully explore the effects of different emotional antecedents on necessity entrepreneurship and on opportunity recognition and exploitation." (p. 17, "Necessity entrepreneurship and its emancipatory potential")

## Cross-cutting notes

1. **Organization theory's object is widening beyond the formal organization (A, B, D, G).** Several stacks share one presupposition: the field's object now reaches persons, communities, markets, movements, families and more-than-human assemblages, and the asks are about what holds that wider object together. Examples: OQ-schoeneborn2026-09, OQ-dion2025-04, OQ-nigam2025-04, OQ-friedrich2026-15, OQ-mena2026-01, OQ-georgiou2023-09, OQ-laine2023-05.
2. **Scholars are expected to take a normative stance (F, K, G, I, E).** Authors ask scholars to state and defend values instead of only describing. The 2023–24 askers made it a call (suddaby2024-04, seidemann2024-09, gumusay2024-08, langenmayr2024-09). By 2025–26 it has become a premise (kalkman2026-01, werner2026-10, ernst2026-07). Examples: OQ-suddaby2024-04, OQ-seidemann2024-09, OQ-gumusay2024-08, OQ-langenmayr2024-09, OQ-kalkman2026-01, OQ-werner2026-10, OQ-ernst2026-07.
3. **Power: whose interests a structure serves (E, D, J, L).** Many questions end on the same worry about who gains and who loses. Examples: OQ-jaser2024-03, OQ-langenmayr2024-04, OQ-hinds2024-15, OQ-grodal2024-06, OQ-pavlisa2026-05, OQ-friedrich2026-04, OQ-mena2026-05.
4. **A deteriorating political environment (C, D, E, K).** Polarization, post-truth communication, authoritarianism and democratic backsliding recur as the setting for questions in several stacks. The concern grows sharper in 2025–26. Examples: OQ-giovannoni2025-08, OQ-winkler2025-02, OQ-patriotta2025-04, OQ-mena2026-21, OQ-mena2026-17, OQ-ernst2026-07; earlier, OQ-sasaki2024-06, OQ-scherer2023-10, OQ-jaser2024-10.

## Residual (11 questions)

- OQ-guercini2023-12, -11, -10, -09, -08, -07, -06, -05, -04: these ask about competence attrition and learning processes. No other piece asks about them, so I left them out of every stack.
- OQ-chia2023-03: a call for strategy theorists to admit practice, situation and potential as logics of intention. It is a single strategy-theory ask.
- OQ-garud2025-09: an invitation for organizations to experiment with alternatives to dominant organizing themes. It is too general to place.

## What I was unsure about

- **H as a stack.** Time could be a cross-cutting note instead. I kept it as a stack because brennecke2025, derekrobinson2025, nigam2025, schoeneborn2026 and garud2025 each ask three or more temporal questions. The rule then ranks it first.
- **A versus B for the person-institution debate.** I put the conceptual asks (can a person be an institution?) in A and the dynamics (emergence, stages, death) in B. Many questions sit in both, so A and B share pieces.
- **Corver & Filler (2026) in G.** Their sustainability-modelling questions could equally form a "pragmatist tool-use" or "theory–practice" concern, and the paper's own vocabulary is modelling.
- **E and J piece counts.** Both rest on single side-questions in 2025–26. I counted them as the rule requires, and the question columns show how thin they are.
- **Wedlin & Weinryb (2025)** do not say what the hype is about in the quoted text, so I did not place it under J.
