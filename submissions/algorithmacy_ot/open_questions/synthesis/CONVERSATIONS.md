# Conversations in the open questions of *Organization Theory*, 4(1) 2023 – 7(3) 2026: the reconciled map

[Written by Fable (claude-fable-5-2), stage S9b, 2026-11-22]

Run `ot-oq-2026-11`. This file reconciles the two independent clusterings of stage S9a, `CONVERSATIONS_O.md` (Opus, 48 conversations) and `CONVERSATIONS_F.md` (Fable, 30 conversations and 11 cross-cutting questions), into one map, rebuilds every member list against the final `QUESTIONS.tsv`, and lays the final fit scores of `fit/FIT_FINAL.tsv` over each conversation. `RECURRENCE.tsv` holds the same map as a table. I did not open `manuscript/`; what I say about the three versions of the paper rests on `BASELINES.md` and `ALGORITHMACY_BRIEF.md`.

The map holds 54 recurring conversations. They place 588 of the 605 open questions (OQs); the other 17 are singletons. Fit is concentrated: all 27 OQs with a final score of 2 or 3 come from eight articles published between October 2023 and October 2024, and they sit in 18 of the 54 conversations. The other 36 conversations hold nothing above 1.

## Counting rules

- **Pool.** `QUESTIONS.tsv` has 684 rows. The 79 rows with form `own_research_question` are not open and belong to no conversation. The 605 open OQs come from 65 pieces; the sixty-sixth record, `bartunek2025`, states none.
- **Recurring.** A conversation needs two pieces with different first authors, each with at least one member that is not a boundary condition, or one such piece and an editorial. All 54 meet the first test.
- **Two memberships at most.** No OQ sits in more than two conversations; 308 sit in two and 280 in one.
- **Boundary conditions** are marked (bc) from the final `form` column. A piece that enters a conversation through boundary conditions alone counts ½.
- **Support is reported in separate columns and never summed into a score:** theory/review articles (types `theory`, `review` and `essay`), commentary or exchange pieces (`controversies_conversations`), editorial signal, distinct volumes, citation edges among askers, and the most recent ask with the months elapsed to 22 November 2026.
- **Editorial signal** is "y" only where an OQ from one of the two editorials (`cornelissen2024`, `hollerer2026`) is a member. O had also counted two OQs of form `editor_call` in theory articles (OQ-giovannoni2025-07, OQ-ernst2026-06). Those are calls that authors address to editors, so I follow F and do not count them.
- **Citation edges** are rows of `EDGES.tsv` (55 rows) whose two ends are both askers in the conversation. O had no `EDGES.tsv` and counted from the records; those counts are replaced.
- **Questions put to practitioners.** The lead ruled that OQ-friedrich2026-03 to -11 are put to practitioners and that synthesis should weight them accordingly (DECISIONS, H8). They stay as members. In three conversations Friedrich (2026) enters through them alone (R14 (AI as participant), R06 (emotion and affect), R25 (futures and imagination)), and each of those entries states its support without that article.
- **Order.** Conversations are ordered by the number of asking pieces (theory/review plus commentary), then editorial signal, then distinct volumes, then the most recent ask. The order measures breadth. It does not measure cohesion, and it does not measure fit.
- **Fit line.** Each entry lists its members' final fit scores and names the members at 2 or above. The sentence after "Entry" judges the conversation as a whole against `ALGORITHMACY_BRIEF.md`. Fit 2 means adjacent and citable; fit 3 means the brief answers part of a stated question, or all of it after a reframing. No OQ in the corpus scores 4.

## Reconciliation notes

**Member lists.** I dropped 17 of O's members and 8 of F's that the hand-check reclassified as the paper's own research question (among them OQ-giovannoni2025-01, O's representative quotation for theorizing the unknowable, and OQ-werner2026-01 and -02), and OQ-scherer2023-12, which the hand-check removed. I placed the four OQs the hand-check added: OQ-hinds2024-25, which F had and O did not, and OQ-fotaki2023-07, OQ-ocasio2023-04 and OQ-seidemann2024-16, which neither had. Boundary-condition marks follow the final forms; OQ-scherer2023-09, OQ-jaser2024-08 and OQ-mutch2025-05 are now limitations and OQ-friesl2023-06 is a call.

**Where O and F cut differently.** Each line gives what the two did, what I kept, and why.

| Topic | O | F | Reconciled | Reason |
|---|---|---|---|---|
| Inequality | O04 and O17 | C01 | R02 (inequality) and R33 (voice at the margins) | One set asks how organizations produce inequality; the other asks how an excluded person comes to be heard. F's own paragraph noted that the askers split on the unit. |
| Scholars and theory | O11 and O32 | C08 | R24 (scholars' reflexivity) and R45 (whose voices count) | The 2026 editorial asks for diverse authors. A merge lent that signal to askers who discuss the reflexivity of scholars already inside. |
| Institutional logics | O28 and O39 | C23 | R31 (institutional logics) | Three askers (Georgiou and Arenas, Stevenson et al., Schildt and Kodeih) sit in both of O's halves, and no citation links any asker to another, so the split added a conversation and little independent support. |
| Democracy | O09 and O36 | C06 | R13 (democracy) | Mena et al. supply questions in both directions (3 of O09's 13 members and 11 of O36's 23); splitting by direction cut one article's agenda in two. |
| Dissent and resistance | O29 and O31 | X10 | R41 (dissent) and R36 (resistance) | One set wants a criterion for productive dissent; the other asks when and why people resist. Stark and Vanden Broeck and Hinds and von Krogh ask only the second. |
| Words and constructs | O02, O08 | C04, C12 | R11 (construct boundaries), R12 (words and standards), R23 (openness to other fields) | Where a construct ends, who decides, and which outside fields to admit are three questions. O had filed the 2026 editorial's calls for new topics and vocabularies under "who decides"; they ask for openness, where F put them. |
| Normativity and engagement | O20, part of O23 | C02, C13 | R10 (normative claims) and R15 (scholars and practice) | One concerns ought-claims inside theory; the other concerns the scholar's conduct toward those studied. |
| The individual | O18, O30, O33 | X04, C30, C14 | R26 (membership categories), R48 (the worker's side), R35 (participation), R54 (surveillance and consent) | F's X04 held three questions: which category a person belongs under, what digital work does to the person, and who takes part. O's partition separates them. F's C30 stays because both of its askers take up one earlier article in the journal. |
| Community | spread over O05, O18, O28 | C20 | dissolved | F called it the loosest conversation in its list; its askers mean a logic, a degree of organizing and a set of scholars. Its members sit in R31 (institutional logics), R09 (what an organization is), R26 (membership categories) and R12 (words and standards). |
| Neoliberal ideology | O41 | spread | dissolved | Once OQ-fotaki2023-02 became the paper's own question, what remained was a shared diagnosis among three askers and no shared question. Its members sit in R54 (surveillance and consent), R13 (democracy) and R34 (law and the state). |
| Audiences | O37, O48 | C22, C16 | R40 (audiences and legitimacy), R53 (conformity and distinctiveness), R19 (digital media and publics) | F's C16 gathers seven askers on what digital media do to publics; O had folded the question into scandal, which left out four of them. O's O48 is a separate question on conformity and distinctiveness. |
| Accountability | O13 | X07 | R17 (accountability) | I removed the 2024 editorial's two disclosure rules, which F had included. They concern authors' answerability for using a language model; counting them gave an editorial signal to a question about algorithms that the editors did not ask. |

**Technology, where the two differed most.** O cut by setting: generative AI in teams (O26), AI in category work (O22), slow institutional effects (O15), the worker (O30), space and hybrid work (O35), brokerage (O42). F cut by question: AI as participant (C15), work held together without its usual carriers (C17), expertise and the division of labour (C19), and two cross-cutting questions, technology between people (X06) and what happens to the old competence (X11). I kept F's questions where askers from several settings pose them and O's settings where they isolate one, and I split three clusters.

- O35 joined Räcker et al. and Whyte et al. under space. Räcker et al. ask a coordination question in the line of Okhuysen and Bechky; Whyte et al. ask about presence through a medium. The only bridge is OQ-racker2024-05, a boundary condition. Räcker et al. go to R49 and Whyte et al. to R22.
- O26 mixed Hinds and von Krogh's questions on team coordination with their questions on the division of labour and with Stark and Vanden Broeck's on sociality. The first set goes to R49, the second to R44, the third to R22.
- F's C17 added du Gay and Lopdrup Hjorth, Gümüsay and Reinecke, and Mena et al. to the coordination askers. Their questions concern formal structure and hierarchy, so they go to R43, as in O.
- O07 and X11 are one question about competence and become R18. I returned three of Guercini and Lechner's items to the singletons, since they are limits of that article's own propositions.
- R52 (brokerage), R43 (formal structure), R38 (crisis), R34 (law and the state), R46 (adopted practices), R51 (hype), R53 (conformity and distinctiveness), R29 (dark sides) and R28 (identity) come from O alone, and R05 (micro and macro), R07 (scope conditions), R20 (actor and structure), R19 (digital media and publics), R37 (ecological crisis) and R54 (surveillance and consent) from F alone. Each meets the rule. R29 (dark sides), R28 (identity), R51 (hype), R52 (brokerage), R53 (conformity and distinctiveness) and R26 (membership categories) are thin: about one question per asker, or two askers only.

**The count.** The map has 54 conversations against O's 48 and F's 41, because I kept a split wherever the two halves pose different questions and kept every one-sided conversation that meets the rule. Six of the 54 are flagged thin above.

## The coordination cluster

The run reports the coordination cluster whatever its size. It is R49 (coordination), and it is small.

- **Askers.** Two theory articles, Räcker, Geiger and Seidl (2024) and Hinds and von Krogh (2024), and one question in a commentary (Phillips et al., 2024, on an AI teammate). 23 OQs.
- **Support.** Theory/review articles 2; commentary or exchange pieces 1; editorial signal n; distinct volumes 1 (5); citation edges among askers 0; most recent ask 2024-10-29, 24 months before this run.
- **Under the wider definitions.** O's version (O26, with Stark and Vanden Broeck, Mena et al. and Garud et al.) had 4 theory articles and 1 commentary over 3 volumes. F's version (C17, with Whyte et al., du Gay and Lopdrup Hjorth, Gümüsay and Reinecke, and Mena et al.) had 6 theory articles over 3 volumes. Both reach their size by adding questions about sociality, deliberation, presence or formal structure, in which the askers do not use coordination as their object.
- **Who cites coordination theory.** Seven records score the coordination flag at 2 (du Gay, Friesl, Hinds, Orlikowski, Räcker, Stark, Winkler). By my reading of their open questions, two of the seven (Räcker et al.; Hinds and von Krogh) ask about the coordination of interdependent work. One record in 66 lists Okhuysen and Bechky (2009), the anchor of GDOC's frame, as a named interlocutor: Räcker et al.
- **Fit.** One member at 3, six at 2, twelve at 1, four at 0. Seven members at 2 or above is a count only R22 matches, and Hinds and von Krogh carry it: the 3 and four of the six 2s are theirs. Räcker et al. hold one 2 among twelve members.

The author's hunch holds on the support columns and fails on the fit column. As a conversation in this journal, coordination has two articles and one further question, none of which cites another, one volume, no editorial signal and no ask in two years. As a problem, coordination is where the brief fits best, because Hinds and von Krogh pose their questions about generative AI in its vocabulary. A coordination frame addressed to coordination theory finds one interlocutor in the journal. A coordination problem addressed to the people asking about algorithms and generative AI finds the corpus's best-fitting question (OQ-hinds2024-04). `SHORTLIST.md` ranks the two separately.

## Fit overlay in brief

| Verdict | Conversations |
|---|---|
| A place to enter | R22 (technology between people), with two 3s and five 2s; R49 (coordination) by fit, with thin support; R48 (the worker's side), for positioning at the brief's own level |
| Partial or narrow | R18 (competence and expertise), by reframing the askers' question; R52 (brokerage), through one question about a third who allocates; R21 (the digital undertow), through invisible work only |
| Adjacent, needs a change of level | R44 (division of labour); R09 (what an organization is); R17 (accountability), which also uses the word in another sense |
| A foil or a licence | R14 (AI as participant), whose premise the brief rejects; R23 (openness to other fields), where the editors welcome new vocabularies |
| Rival accounts | R54 (surveillance and consent): consent, and competence outside the systems |
| Single citable members, no entry | R06 (emotion and affect), R13 (democracy), R26 (membership categories), R36 (resistance), R43 (formal structure), R50 (language models in theorizing) |
| Nothing above 1 | the other 36 |

Two patterns hold across the overlay. Every OQ at 2 or above was asked in volume 4(3) or volume 5, so the questions the brief can answer are between 24 and 37 months old at this run, and no piece in volumes 6 or 7 poses one. And the level of analysis sorts the verdicts: the brief's construct is an individual's capacity exercised in an interaction, and the conversations it can enter are the ones posed at that level (R22, R49, R48); those posed at the level of the organization, the profession or the field stay at 2, or reach 3 only with a change of level, as OQ-stark2024-06 does.

## Index

| id | short name | from | kind | question | theory/review | commentary | ed. | vols | edges | last asked | members at 3 / 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | time and history | O01 + X01 | cross-cutting | How does the past of a tie, practice, institution or collective act on its present, and what notion of time should theory use? | 13 | 2 | n | 4 | 2 | 2026-09-19 | 0 / 0 |
| R02 | inequality | O04 + part of C01 | topical | How does organizing produce, reproduce or reduce exclusion and inequality? | 13 | 1.5 | n | 4 | 0 | 2026-06-19 | 0 / 0 |
| R03 | methods for the hidden | O03 + X08 | cross-cutting | Which methods can study what does not show itself: invisible work, atmospheres, absences, black-boxed processes? | 12 | 0 | n | 3 | 1 | 2025-09-28 | 0 / 0 |
| R04 | non-human things | O06 + X02 | cross-cutting | What part do non-human things (objects, spaces, atmospheres, ecologies, technologies) play in organizing, and how should theory give them that part? | 9.5 | 2 | n | 4 | 7 | 2026-09-21 | 0 / 0 |
| R05 | micro and macro | X03 | cross-cutting | How do local practices add up to macro structures, and how do macro conditions reach into local action? | 10 | 1 | n | 4 | 1 | 2026-06-19 | 0 / 0 |
| R06 | emotion and affect | O10 + C05 | cross-cutting | What do emotion and affect do in organizing that accounts built on discourse and cognition miss? | 10 | 0 | n | 3 | 1 | 2026-04-01 | 0 / 2 |
| R07 | scope conditions | X05 | cross-cutting | Do theories built in a few national, democratic, for-profit settings hold in other societies and sectors? | 7.5 | 2 | n | 4 | 3 | 2026-07-28 | 0 / 0 |
| R08 | theorizing the not-yet | O12 + C03 | topical | How can scholars theorize what does not yet exist, or cannot be known, and still be rigorous? | 7 | 2 | y | 4 | 9 | 2026-04-01 | 0 / 0 |
| R09 | what an organization is | O05 + C07 + parts of C20 | topical | What makes a collective an organization, and where does organization end and other sociality begin? | 8 | 1 | n | 4 | 4 | 2026-09-19 | 0 / 2 |
| R10 | normative claims | C02 + parts of O20 and O23 | topical | Should organization theory say what organizations ought to do, and what warrants such claims? | 8 | 1 | n | 3 | 5 | 2026-07-21 | 0 / 0 |
| R11 | construct boundaries | O02 + part of C04 | cross-cutting | Where do the boundaries of the field's working constructs lie: what counts as a logic, a paradox, an organization, an institution? | 6.5 | 2 | n | 4 | 3 | 2026-09-19 | 0 / 0 |
| R12 | words and standards | O08 + C04 | topical | Who decides which words, distinctions and standards of good theory a scholarly community uses, and by what procedure? | 5 | 3 | y | 3 | 8 | 2026-09-19 | 0 / 0 |
| R13 | democracy | O09 + O36 + C06 | topical | What do organizations do, and what do they owe, when democratic institutions weaken, and what do they do to democracy in turn? | 8 | 0 | n | 4 | 0 | 2026-04-07 | 0 / 1 |
| R14 | AI as participant | O22 + C15 | topical | What changes when a generative-AI system or algorithm takes part in organizing (in category work, legitimacy tests, teams) as a participant and not only as a tool? | 5 | 3 | n | 4 | 10 | 2026-04-01 | 0 / 4 |
| R15 | scholars and practice | O20 + C13 | cross-cutting | What should scholars do with and for the people and struggles they study: critic, activist, co-inquirer or adviser? | 7 | 1 | n | 3 | 2 | 2026-07-28 | 0 / 0 |
| R16 | institutional emergence | O16 + C10 | topical | Under what conditions do new practices, forms and institutions emerge, take hold and displace old ones? | 6 | 2 | n | 2 | 3 | 2025-12-23 | 0 / 0 |
| R17 | accountability | O13 + X07 | cross-cutting | Who answers for an outcome when an algorithm, a platform or a loosely bounded collective decides and no office-holder does? | 7 | 0 | n | 3 | 0 | 2026-09-19 | 0 / 1 |
| R18 | competence and expertise | O07 + X11 | cross-cutting | What happens to competence and expertise when new knowledge or technology arrives: is it lost, kept or rebuilt, and what must people still be able to do? | 6 | 1 | n | 3 | 0 | 2026-07-28 | 0 / 3 |
| R19 | digital media and publics | C16 + part of O37 | topical | How do digital media and platforms change how publics form, judge organizations and mobilize? | 5 | 2 | n | 3 | 2 | 2026-03-31 | 0 / 0 |
| R20 | actor and structure | X09 | cross-cutting | How much can one actor do against the structures they sit in, and where do their resources come from? | 7 | 0 | n | 3 | 0 | 2025-09-28 | 0 / 0 |
| R21 | the digital undertow | O15 + C11 | topical | What are the indirect, hidden and delayed consequences of digitalization for institutions and for work? | 5 | 2 | n | 2 | 6 | 2024-10-29 | 0 / 3 |
| R22 | technology between people | X06 + Whyte's part of O35 | cross-cutting | What changes when a technology stands between the people who organize: is it a medium they communicate through or a party they communicate with? | 5.5 | 1 | n | 3 | 1 | 2026-03-31 | 2 / 5 |
| R23 | openness to other fields | C12 | topical | Which neighbouring fields, topics and vocabularies should organization theory open to, and how does it stay cumulative while doing so? | 4 | 2 | y | 4 | 2 | 2026-07-26 | 1 / 0 |
| R24 | scholars' reflexivity | O11 + part of C08 | topical | How do scholars' own selves, careers and positions enter their theorizing, and how should they account for that? | 6 | 0 | n | 4 | 2 | 2026-04-07 | 0 / 0 |
| R25 | futures and imagination | O19 + C24 | topical | How do people in organizations imagine what is not present, futures above all, and what does imagining do to organizing now? | 6 | 0 | n | 3 | 3 | 2026-09-21 | 0 / 0 |
| R26 | membership categories | O18 + part of X04 | cross-cutting | Under which category does a person belong to an organization (member, user, contributor, citizen, stakeholder), and who decides? | 5 | 1 | n | 3 | 0 | 2026-09-19 | 0 / 1 |
| R27 | movements | O24 + C09 | topical | How do movements and collective action form, press on organizations and markets, and survive co-optation? | 6 | 0 | n | 3 | 0 | 2026-04-01 | 0 / 0 |
| R28 | identity | O21 | cross-cutting | How do collective, organizational and personal identities form, and how do they shape what actors do? | 6 | 0 | n | 3 | 0 | 2026-04-01 | 0 / 0 |
| R29 | dark sides | O14 | cross-cutting | What are the failures and dark sides of practices the field usually treats as good? | 6 | 0 | n | 3 | 0 | 2025-11-11 | 0 / 0 |
| R30 | paradox | O38 + C18 | topical | When should organizations hold a contradiction open, choose a side, or refuse both, and how would anyone know the response was good? | 6 | 0 | n | 3 | 2 | 2025-09-27 | 0 / 0 |
| R31 | institutional logics | O28 + O39 + C23 | topical | What is an institutional logic: what is it made of, where are its boundaries, and how do actors hold or combine several? | 6 | 0 | n | 3 | 0 | 2025-04-25 | 0 / 0 |
| R32 | values under pressure | O23 + C21 | topical | What makes an organization hold to its values or purpose under pressure, and how do its commitments change? | 5.5 | 0 | n | 4 | 1 | 2026-07-21 | 0 / 0 |
| R33 | voice at the margins | O17 + part of C01 | topical | How do marginalized and excluded people gain a speaking position, a voice or cultural autonomy? | 5.5 | 0 | n | 2 | 0 | 2024-09-18 | 0 / 0 |
| R34 | law and the state | O25 | topical | How do law, regulation and the state shape organizations, and can they restrain new technologies? | 5 | 0 | n | 4 | 0 | 2026-03-31 | 0 / 0 |
| R35 | participation | O33 + C14 | topical | Who gets to take part in organizational decisions, on whose terms, and does participation deliver what it promises? | 5 | 0 | n | 3 | 1 | 2026-07-28 | 0 / 0 |
| R36 | resistance | O31 + part of X10 | cross-cutting | When and why do people resist control and new technology, and how is resistance told from compliance? | 4.5 | 0 | n | 1 | 0 | 2024-10-29 | 0 / 1 |
| R37 | ecological crisis | C25 | topical | How should organizing change under ecological crisis and other grand challenges whose shape is not settled? | 4 | 0 | n | 3 | 3 | 2026-07-28 | 0 / 0 |
| R38 | crisis | O34 | topical | How do organizations anticipate, respond to and learn from crises, and what should crisis response aim at? | 4 | 0 | n | 3 | 0 | 2026-07-21 | 0 / 0 |
| R39 | myth and narrative | O47 + C26 | topical | How do stories, myths and narratives gain force in and around organizations? | 3 | 1 | n | 3 | 0 | 2025-12-01 | 0 / 0 |
| R40 | audiences and legitimacy | O37 + C22 | topical | How do audiences come to judge an organization as legitimate or scandalous, and how do organizations answer? | 4 | 0 | n | 3 | 1 | 2025-11 | 0 / 0 |
| R41 | dissent | O29 + part of X10 | cross-cutting | When is disagreement or dissent productive, for organizations and for scholarly communities, and when does it destroy? | 3 | 1 | n | 2 | 2 | 2026-07-28 | 0 / 0 |
| R42 | care | O40 + C28 | topical | How can organizations give and sustain care when care is undervalued? | 4 | 0 | n | 2 | 1 | 2026-07-21 | 0 / 0 |
| R43 | formal structure | O27 | topical | Which formal structures do organizations need for their purposes, and what can stand in for hierarchy? | 4 | 0 | n | 2 | 0 | 2026-03-31 | 0 / 1 |
| R44 | division of labour | C19 + part of O26 | topical | What happens to the division of labour and workplace power when algorithms and generative AI take over tasks? | 3 | 1 | n | 1 | 0 | 2024-10-29 | 0 / 4 |
| R45 | whose voices count | O32 + part of C08 | topical | Whose voices, bodies and standpoints count as sources of theory, and who is left out of the record? | 3 | 0 | y | 3 | 1 | 2026-07-26 | 0 / 0 |
| R46 | adopted practices | O43 | topical | What do practices do inside organizations once adopted: change conduct or stay symbolic? | 3 | 0 | n | 2 | 0 | 2026-07-28 | 0 / 0 |
| R47 | person as institution | O44 + C29 | topical | Can a person be an institution, and under what conditions? | 0 | 3 | n | 1 | 2 | 2025-12-23 | 0 / 0 |
| R48 | the worker's side | O30 + part of X04 | cross-cutting | What does digitalized work demand of, and do to, the individual worker: hidden labour, consent, meaning? | 3 | 0 | n | 1 | 0 | 2024-10-29 | 0 / 4 |
| R49 | coordination | Räcker's part of O35 + Hinds's part of O26 + C17 | topical | How is interdependent work coordinated when its usual carriers (co-presence, informal contact, human teammates) are displaced? | 2 | 1 | n | 1 | 0 | 2024-10-29 | 1 / 6 |
| R50 | language models in theorizing | O45 + C27 | topical | What place should language models and computational methods have in scholars' own theorizing? | 1 | 1 | y | 2 | 2 | 2024-10-28 | 0 / 1 |
| R51 | hype | O46 | topical | How do hype and attention around a new technology form, and with what institutional and power consequences? | 1 | 1 | n | 2 | 0 | 2025-12-23 | 0 / 0 |
| R52 | brokerage | O42 | topical | How does brokerage work, and what happens when tie histories accumulate or a technology takes over the brokering? | 2 | 0 | n | 2 | 0 | 2025-09-28 | 0 / 1 |
| R53 | conformity and distinctiveness | O48 | topical | When are organizations rewarded for conforming and when for staying distinct, and before which audiences? | 2 | 0 | n | 2 | 1 | 2024-09-03 | 0 / 0 |
| R54 | surveillance and consent | C30 | topical | Why do people consent to surveillance and data-driven control, and what would restore their autonomy? | 2 | 0 | n | 2 | 0 | 2024-03-19 | 0 / 1 |

## Conversations, ordered by support
### R01. How does the past of a tie, practice, institution or collective act on its present, and what notion of time should theory use?

- **Short name:** time and history.
- **Kind and origin:** cross-cutting; from O01 + X01.
- **Members** (41 OQs from 15 pieces): Leitzinger 2023: OQ-leitzinger2023-27; Ocasio 2023: OQ-ocasio2023-03; Sasaki 2024: OQ-sasaki2024-05; Justesen 2024: OQ-justesen2024-02, -03; Lantela 2024: OQ-lantela2024-03; Stevenson 2024: OQ-stevenson2024-01; Seidemann 2024: OQ-seidemann2024-12; Suddaby 2024: OQ-suddaby2024-01; Hinds 2024: OQ-hinds2024-01, -23; Garud 2025: OQ-garud2025-03, -04, -05, -07; Brennecke 2025: OQ-brennecke2025-02, -03, -04, -05, -06, -07, -08, -09, -10, -11, -12, -13, -14, -15, -17, -18, -19, -20, -21; Patriotta 2025: OQ-patriotta2025-02, -06, -07; Derek Robinson 2025: OQ-derekrobinson2025-01, -08; Dion 2025: OQ-dion2025-07; Schoeneborn 2026: OQ-schoeneborn2026-05.
- **Representative quotation:** OQ-brennecke2025-12: “Which features of relational history are retained, which decay over time? When do narratives about a tie crystallize into dominant accounts that guide behaviour? Under what conditions do memories of key events become shared across both parties” (p. 19, "Cognitive and narrative construction of relational history")
- **Support:** theory/review articles 13; commentary or exchange pieces 2; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 2; most recent ask 2026-09-19 (schoeneborn2026), 2 months before the run.
- **Level:** Multi-level: ties, practices, organizations and institutions, each with a past.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 6; 0 × 35. At 2 or above: none.

Fifteen pieces ask their own literature to stop treating the past as background, and they ask it of different things. Brennecke, Carnabuci and Ertug (2025) ask it of the dyadic tie: which features of a tie's history are retained, which decay, and when a narrative about the tie hardens into the account that guides behaviour. Patriotta, Augustine and Voronov (2025) ask it of an organization's earlier crises, Schoeneborn, Dobusch and Seidl (2026) of a collective's actorhood, and Sasaki and Baba (2024) of marginalization that turns from one type into another. A second group asks which notion of time theory should use. Garud, Turunen and Karunakaran (2025) work with three kinds of time, Suddaby (2024) wants "is" and "was" inside constructs, and Hinds and von Krogh (2024) call for process theory beside variance theory. The two groups do not meet: no asker says whether history works as a variable, as in Brennecke et al.'s founding conditions, trajectories and critical events, or as a different kind of time. Brennecke et al. supply 19 of the 41 questions.

**Entry.** None. Six members score 1 and none higher. The 1s are Hinds and von Krogh's calls for process theory, one of Justesen and Plesner's, and Brennecke et al.'s questions on brokers and third-party audiences, which meet the brief in R52.

### R02. How does organizing produce, reproduce or reduce exclusion and inequality?

- **Short name:** inequality.
- **Kind and origin:** topical; from O04 + part of C01.
- **Members** (26 OQs from 15 pieces): Bacq 2023: OQ-bacq2023-06; Fotaki 2023: OQ-fotaki2023-03; Jackwerth-Rice 2023: OQ-jackwerthrice2023-10; Leitzinger 2023: OQ-leitzinger2023-30; Arnold 2023: OQ-arnold2023-03, -04, -05, -11, -13; Whyte 2023: OQ-whyte2023-10, -11; Sasaki 2024: OQ-sasaki2024-06; Justesen 2024: OQ-justesen2024-14; Langenmayr 2024: OQ-langenmayr2024-01, -03, -04, -05, -06, -07; Seidemann 2024: OQ-seidemann2024-10; Hinds 2024: OQ-hinds2024-15; Hawbaker 2025: OQ-hawbaker2025-02 (bc); Derek Robinson 2025: OQ-derekrobinson2025-13; Mena 2026: OQ-mena2026-04; Pavlisa 2026: OQ-pavlisa2026-05, -06.
- **Representative quotation:** OQ-langenmayr2024-01: “Adopting an equity-based approach would thus allow open strategy scholars to explore the relation between traditional actors’ dominance and control over inclusion and the reproduction of inequalities.” (p. 6, "Normalizing through traditional strategy actors’ control over inclusion")
- **Support:** theory/review articles 13; commentary or exchange pieces 1.5; counted at ½ because they enter through boundary conditions only: Hawbaker 2025; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 0; most recent ask 2026-06-19 (pavlisa2026), 5 months before the run.
- **Level:** Multi-level: organization to society.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 1; 0 × 25. At 2 or above: none.

The askers want to know how organizing makes and keeps inequality, and whether the remedies on offer reduce it. Langenmayr, Splitter, Tienari and Vesa (2024) ask how incumbents' control over inclusion reproduces power in open strategy. Pavlisa, Harvey and Doh (2026) ask how organizational and industry structures reinforce inequality and how firms might reduce their own part in it. Arnold and Costas (2023) ask how organizations produce some people as noise and which forms of organizing make a shift in who counts as Other last. Whyte, Comi and Mosca (2023) and Hinds and von Krogh (2024) put the same question to hybrid work and to generative AI: do the new arrangements reproduce existing patterns or alter them? The unresolved split is the one Langenmayr et al. draw between a business-case reading of inclusion and an equity reading. No asker shows which organizational mechanism narrows inequality, and no citation links any two of the fifteen.

**Entry.** None. One member scores 1 (OQ-hinds2024-15, on whether encapsulation includes or excludes marginalized groups); the rest score 0.

### R03. Which methods can study what does not show itself: invisible work, atmospheres, absences, black-boxed processes?

- **Short name:** methods for the hidden.
- **Kind and origin:** cross-cutting; from O03 + X08.
- **Members** (21 OQs from 12 pieces): Orlikowski 2023: OQ-orlikowski2023-05, -09; Friesl 2023: OQ-friesl2023-08; Pozner 2023: OQ-pozner2023-08; Jørgensen 2023: OQ-jorgensen2023-03; Powell 2023: OQ-powell2023-11; Whyte 2023: OQ-whyte2023-07; Justesen 2024: OQ-justesen2024-05, -06, -07, -08, -09, -10; Lantela 2024: OQ-lantela2024-04; Räcker 2024: OQ-racker2024-03; Hinds 2024: OQ-hinds2024-01, -11; Giovannoni 2025: OQ-giovannoni2025-10; Brennecke 2025: OQ-brennecke2025-07, -08, -16.
- **Representative quotation:** OQ-justesen2024-06: “So, what methods will be appropriate to study work that is out of sight as well as devalued?” (p. 21, "Future research: Some suggestions")
- **Support:** theory/review articles 12; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 1; most recent ask 2025-09-28 (brennecke2025), 13 months before the run.
- **Level:** Multi-level; a question of method.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 4; 0 × 17. At 2 or above: none.

Twelve articles reach a point where the methods at hand cannot observe their object. Justesen and Plesner (2024) ask which methods can study work that is out of sight and devalued. Orlikowski and Scott (2023) ask for research practices that follow effects "below the water line". Jørgensen and Beyes (2023), Giovannoni and Quattrone (2025) and Lantela (2024) ask how to study atmospheres, absences and missing voices; Brennecke et al. (2025) ask for temporal measures that static network analysis lacks; Hinds and von Krogh (2024) note that researchers may be refused access to the models they theorize. The proposals form a list and not a method, since each asker names techniques for its own case and none tests one. Two attitudes divide them. Justesen and Plesner, Whyte et al. (2023) and the computational askers (Pozner and Hannigan, 2023; Powell and DiMaggio, 2023) want the hidden made visible, whereas Jørgensen and Beyes and Giovannoni and Quattrone want its withdrawal respected.

**Entry.** None. Four members score 1. The brief is a theory article that "measures no one", so it brings no method to this conversation; Hinds and von Krogh's access problem (OQ-hinds2024-11) is a limit the paper shares and does not solve.

### R04. What part do non-human things (objects, spaces, atmospheres, ecologies, technologies) play in organizing, and how should theory give them that part?

- **Short name:** non-human things.
- **Kind and origin:** cross-cutting; from O06 + X02.
- **Members** (31 OQs from 12 pieces): Laine 2023: OQ-laine2023-04, -05, -06 (bc), -08; Orlikowski 2023: OQ-orlikowski2023-05; Jørgensen 2023: OQ-jorgensen2023-04, -05, -07; Whyte 2023: OQ-whyte2023-06, -07; Lantela 2024: OQ-lantela2024-03; Räcker 2024: OQ-racker2024-01, -07, -11, -12 (bc); Phillips 2024: OQ-phillips2024-13; Hsu 2024: OQ-hsu2024-06; Seidemann 2024: OQ-seidemann2024-05, -14; Keller 2025: OQ-keller2025-02 (bc); Friedrich 2026: OQ-friedrich2026-03, -04, -05, -07, -08, -09, -12, -14, -15, -17; Porsfelt 2026: OQ-porsfelt2026-08.
- **Representative quotation:** OQ-laine2023-05: “while it may be customary to think of humans as more suitable to being characterized as entrepreneurial than, for instance, broken pencils, ultimately this distinction needs to be shown rather than assumed.” (p. 19, "OOOT in Action: Sun Ra")
- **Support:** theory/review articles 9.5; commentary or exchange pieces 2; counted at ½ because they enter through boundary conditions only: Keller 2025; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 7; most recent ask 2026-09-21 (porsfelt2026), 2 months before the run.
- **Level:** Multi-level; an ontological question each asker works out at its own level.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 7; 0 × 24. At 2 or above: none.

Twelve pieces ask theory to give non-human things a part in organizing. Laine and Kibler (2023) hold that whether humans carry "the entrepreneurial" better than broken pencils must be shown and not assumed. Friedrich (2026) asks how organizing can attend to air, water, minerals and data flows; Räcker, Geiger and Seidl (2024) ask how coordination produces space; Jørgensen and Beyes (2023) ask for the politics of atmospheres. The disagreement is sharpest in the exchange on generative AI, where Hsu and Bechky (2024) want technology treated as an actor in its own right and Phillips, Kalvapalle and Kennedy (2024) call for a "symbolic turn" away from the realist ontology they find in the field's talk about AI. Ontologies differ inside the materialist camp as well: objects that withhold something from their relations (Laine and Kibler) against entanglement (Orlikowski and Scott, 2023; Friedrich). No asker says how a researcher would tell an actor from an affordance in data.

**Entry.** None. Seven members score 1. The brief treats the intermediary as a party that evaluates and binds two people and takes no position on the ontology of things, so it shares this conversation's objects and none of its questions.

### R05. How do local practices add up to macro structures, and how do macro conditions reach into local action?

- **Short name:** micro and macro.
- **Kind and origin:** cross-cutting; from X03.
- **Members** (17 OQs from 12 pieces): Guercini 2023: OQ-guercini2023-11; Ocasio 2023: OQ-ocasio2023-02 (bc); Pozner 2023: OQ-pozner2023-13 (bc); Powell 2023: OQ-powell2023-10, -13; Whyte 2023: OQ-whyte2023-04; Stevenson 2024: OQ-stevenson2024-03; Schildt 2025: OQ-schildt2025-03; Brennecke 2025: OQ-brennecke2025-14, -15; Nigam 2025: OQ-nigam2025-03; Mena 2026: OQ-mena2026-11, -20, -21, -23; Werner 2026: OQ-werner2026-08; Pavlisa 2026: OQ-pavlisa2026-05.
- **Representative quotation:** OQ-powell2023-13: “how are individual efforts at organizing facilitated or thwarted by available meso-level resources, and how are those resources themselves produced and structured by macro-level processes? How do macro-level conditions foster or impede the emergence and success of individual innovators?” (p. 18, "Institutional change")
- **Support:** theory/review articles 10; commentary or exchange pieces 1; counted at ½ because they enter through boundary conditions only: Ocasio 2023, Pozner 2023; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 1; most recent ask 2026-06-19 (pavlisa2026), 5 months before the run.
- **Level:** Multi-level by definition.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 1; 0 × 16. At 2 or above: none.

Twelve pieces, from most of the literatures in the corpus, ask how the micro and the macro connect. Powell and DiMaggio (2023) call it a frontier: how individual organizing depends on meso-level resources that macro-level processes produce. Schildt and Kodeih (2025) ask how seemingly stable macro ideology arises from local practice. Mena, Mair and Bruder (2026) ask about spillover in both directions between workplace democracy and national politics. Brennecke et al. (2025) ask how the histories of dyadic ties connect to network structure, Whyte et al. (2023) how mundane video meetings add up to larger phenomena, and Werner, Cornelissen and Turkenburg (2026) how conversations between leaders and employees form organizational character. The askers assume aggregation and seldom specify it. They differ on direction: emergence from below (Schildt and Kodeih; Whyte et al.) against embedding from above (Ocasio, 2023, who bounds his structure to modern societies), with Mena et al. asking for both.

**Entry.** None. One member scores 1. The brief names its own cross-level claim, an individual capacity exercised under an organizational form, and it gives no account of aggregation; the hand-check makes the same point about OQ-hinds2024-08 in R49.

### R06. What do emotion and affect do in organizing that accounts built on discourse and cognition miss?

- **Short name:** emotion and affect.
- **Kind and origin:** cross-cutting; from O10 + C05.
- **Members** (17 OQs from 10 pieces): Bacq 2023: OQ-bacq2023-03, -04, -05, -06; Fotaki 2023: OQ-fotaki2023-07; Leitzinger 2023: OQ-leitzinger2023-02, -13; Ocasio 2023: OQ-ocasio2023-01; Arnold 2023: OQ-arnold2023-07, -10; Jørgensen 2023: OQ-jorgensen2023-05, -07; Justesen 2024: OQ-justesen2024-13; Paca 2024: OQ-paca2024-05; Hinds 2024: OQ-hinds2024-21; Friedrich 2026: OQ-friedrich2026-06, -07.
- **Representative quotation:** OQ-arnold2023-07: “Future research may explore in greater detail how affect and discourse interrelate, that is clash or reinforce each other in struggles over otherness.” (p. 17, "Implications for future research")
- **Support:** theory/review articles 10; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 1; most recent ask 2026-04-01 (friedrich2026), 7 months before the run.
- **Level:** Interaction, with individual-level questions about felt emotion.
- **Fit (final scores of members):** 3 × 0; 2 × 2; 1 × 0; 0 × 15. At 2 or above: OQ-justesen2024-13 (2), OQ-hinds2024-21 (2).

Ten articles from unrelated literatures arrive at the same gap: their field's account runs through discourse or cognition and leaves affect out. Arnold and Costas (2023) ask when affect and discourse clash or reinforce each other in the making of otherness. Bacq, Toubiana, Ruebottom, Ormiston and Ajunwa (2023) ask whether negative emotions other than shame energize entrepreneurship; Leitzinger and Waeger (2023) ask when anger and positive emotion help or hinder mobilization; Ocasio (2023) records values and emotions as the part of institutions his theory does not cover. Justesen and Plesner (2024) ask for an account of the emotional costs of digitalization, and Hinds and von Krogh (2024) ask how employees respond as generative AI absorbs their tasks. The askers do not share a concept of affect. For Bacq et al. and for Leitzinger and Waeger it is a discrete emotion with effects; for Arnold and Costas and for Jørgensen and Beyes (2023) it is an order or an atmosphere that comes before subjects. No article compares the two. Friedrich (2026) enters through two questions the lead ruled as put to practitioners (DECISIONS, H8); without that article the conversation has 9 theory articles in volumes 4 and 5, and its most recent ask is October 2024.

**Entry.** None at the level of the conversation. Two members score 2 (OQ-justesen2024-13, OQ-hinds2024-21), and both ask what digital systems cost the person who works with them; they belong with R48, where the brief has something to say. The brief makes no claim about affect.

### R07. Do theories built in a few national, democratic, for-profit settings hold in other societies and sectors?

- **Short name:** scope conditions.
- **Kind and origin:** cross-cutting; from X05.
- **Members** (13 OQs from 11 pieces): Leitzinger 2023: OQ-leitzinger2023-06, -31; Ocasio 2023: OQ-ocasio2023-02 (bc); Scherer 2023: OQ-scherer2023-10 (bc); Lantela 2024: OQ-lantela2024-06 (bc); Langenmayr 2024: OQ-langenmayr2024-03; Mutch 2025: OQ-mutch2025-01, -05; Patriotta 2025: OQ-patriotta2025-03; Nigam 2025: OQ-nigam2025-04; Derek Robinson 2025: OQ-derekrobinson2025-14; Mena 2026: OQ-mena2026-17; Corver 2026: OQ-corver2026-13.
- **Representative quotation:** OQ-leitzinger2023-06: “suggests a clear research opportunity to investigate whether similar factors drive the emergence of elimination movements in other national and socio-economic contexts.” (p. 11, "Phase 1: Emergence")
- **Support:** theory/review articles 7.5; commentary or exchange pieces 2; counted at ½ because they enter through boundary conditions only: Ocasio 2023, Scherer 2023, Lantela 2024; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 3; most recent ask 2026-07-28 (corver2026), 3 months before the run.
- **Level:** Field and societal: the scope conditions of theories.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 13. At 2 or above: none.

Eleven pieces ask whether their theory holds outside the setting that produced it. Leitzinger and Waeger (2023) ask whether the same factors drive movements in other national and socio-economic contexts. Patriotta et al. (2025) expect comparative work beyond democratic societies to reveal other orders of worth. Mena et al. (2026) ask what organizations can do where democracy is weak, Mutch (2025) asks about legal systems other than common and civil law, and Corver and Filler (2026) ask about public and third-sector settings. Three boundary conditions say the same from the other side: Ocasio (2023) claims his structure for modern societies only, Scherer and Neesham (2023) note that most states are not rule-of-law democracies, and Lantela (2024) holds that the subjugated must be identified anew for each time and culture. Every item calls for a comparison still to be made.

**Entry.** None. Every member scores 0.

### R08. How can scholars theorize what does not yet exist, or cannot be known, and still be rigorous?

- **Short name:** theorizing the not-yet.
- **Kind and origin:** topical; from O12 + C03.
- **Members** (19 OQs from 10 pieces): Laine 2023: OQ-laine2023-07, -09; Jaser 2024: OQ-jaser2024-08; Cornelissen 2024: OQ-cornelissen2024-05 (bc); Gümüsay 2024: OQ-gumusay2024-01, -06, -09, -11, -12; Lantela 2024: OQ-lantela2024-08; Phillips 2024: OQ-phillips2024-14; Hsu 2024: OQ-hsu2024-02; Hinds 2024: OQ-hinds2024-24; Giovannoni 2025: OQ-giovannoni2025-03, -06, -07, -09, -10; Friedrich 2026: OQ-friedrich2026-02.
- **Representative quotation:** OQ-hinds2024-24: “we need 'prospective theorizing' with speculative vigor (e.g., Gümüsay & Reinecke, 2024)” (p. 12, "Discussion")
- **Support:** theory/review articles 7; commentary or exchange pieces 2; editorial signal y (through a boundary condition only); distinct volumes 4 (4, 5, 6, 7); citation edges among askers 9; most recent ask 2026-04-01 (friedrich2026), 7 months before the run.
- **Level:** Field: the discipline's standards for theory.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 2; 0 × 17. At 2 or above: none.

Gümüsay and Reinecke (2024) pose the question of speculative rigour and answer it in part, with a framework they say leaves much scope for refinement. Others take up the call without settling the standard. Hinds and von Krogh (2024) invite speculative theorizing on generative AI against scholars who would wait for the technology to stabilize. Lantela (2024) suggests microhistory as a way to theorize what does not exist. Giovannoni and Quattrone (2025) ask what methods can study an absence without filling it, and they say editors and reviewers would have to accept open-ended work. The commentaries on generative AI mark their own claims as speculative and their target as moving (Phillips et al., 2024; Hsu and Bechky, 2024), and the 2024 editorial bounds its conclusions to current models. Two questions remain: what separates disciplined speculation from assertion once validation against data is unavailable, and whether the field's institutions will accept it.

**Entry.** None as a question to answer. Two members score 1 (OQ-hinds2024-24, OQ-phillips2024-14). The conversation gives a theory article on a moving technology its warrant, which a paper can cite once; it is no place to position the argument.

### R09. What makes a collective an organization, and where does organization end and other sociality begin?

- **Short name:** what an organization is.
- **Kind and origin:** topical; from O05 + C07 + parts of C20.
- **Members** (34 OQs from 9 pieces): Laine 2023: OQ-laine2023-02, -04, -06 (bc), -08; Georgiou 2023: OQ-georgiou2023-09; du Gay 2024: OQ-dugay2024-04, -05; Stark 2024: OQ-stark2024-08; Phillips 2024: OQ-phillips2024-09; Hinds 2024: OQ-hinds2024-09; Winkler 2025: OQ-winkler2025-04, -05, -06; Dion 2025: OQ-dion2025-02, -03, -04, -05, -06, -08, -09, -10, -11, -12, -14; Schoeneborn 2026: OQ-schoeneborn2026-01, -02, -03, -04, -05, -06, -07, -08, -09, -10.
- **Representative quotation:** OQ-dion2025-02: “How can we support the claim that what we need is a strong notion of what organizations are (that would distinguish them radically from other social collectives), while recognizing that organizations now take so many forms? And which empirical grounds can support this search for the ontological distinctiveness of organizations” (p. 5, "Organizationality: A Critical Review")
- **Support:** theory/review articles 8; commentary or exchange pieces 1; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 4; most recent ask 2026-09-19 (schoeneborn2026), 2 months before the run.
- **Level:** Field, argued through organization-level and interaction-level cases.
- **Fit (final scores of members):** 3 × 0; 2 × 2; 1 × 4; 0 × 28. At 2 or above: OQ-stark2024-08 (2), OQ-phillips2024-09 (2).

The askers agree that "organization" no longer names one kind of thing, and they disagree on what follows. Schoeneborn, Dobusch and Seidl (2026) keep a criterion, collective actorhood held in degrees, and ask how loose collectives persist at low degrees and why actors charge or discharge a collective with actorhood. Dion, Cooren and Dupuis (2025) deny that any cut separates organizations from other collectives and ask a different question: "The organizationality of what?" Du Gay and Lopdrup Hjorth (2024) go the other way and make formal organization the object. Laine and Kibler (2023) ask whether an organization can persist while its relations change. Three askers carry the dispute to technology: Stark and Vanden Broeck (2024) ask whether technology is organizational structure, Phillips et al. (2024) ask what organizations are once artificial persons join them, and Hinds and von Krogh (2024) ask what a team is once the system assembles it. What evidence would settle any of this is the question Dion et al. pose and leave open (OQ-dion2025-02). Schoeneborn et al. answer Dion et al. by name, so the conversation is linked inside the corpus.

**Entry.** Citable, not enterable. Two members score 2 (OQ-stark2024-08, OQ-phillips2024-09) and four score 1. The askers want to know what the organization is; the brief describes what a person inside one arrangement must be able to do, and the hand-check finds that it "adopts the premise and adds nothing about structure at the organizational level". PAPER's organizationality anchor points here, and the level does not match.

### R10. Should organization theory say what organizations ought to do, and what warrants such claims?

- **Short name:** normative claims.
- **Kind and origin:** topical; from C02 + parts of O20 and O23.
- **Members** (14 OQs from 9 pieces): Fotaki 2023: OQ-fotaki2023-04, -05; Orlikowski 2023: OQ-orlikowski2023-08; Gümüsay 2024: OQ-gumusay2024-08; Langenmayr 2024: OQ-langenmayr2024-08; Seidemann 2024: OQ-seidemann2024-08, -09; Suddaby 2024: OQ-suddaby2024-04; Mena 2026: OQ-mena2026-06; Werner 2026: OQ-werner2026-09, -10; Kalkman 2026: OQ-kalkman2026-01, -06, -08.
- **Representative quotation:** OQ-werner2026-10: “Another question that further normative research might explore is how, when organizations deliberate beyond institutionally prescribed norms and obligations, this can be ethically judged in specific instances and cases.” (pp. 21–22, "Theoretical and research implications")
- **Support:** theory/review articles 8; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 5; most recent ask 2026-07-21 (kalkman2026), 4 months before the run.
- **Level:** Field: the standing of normative claims in the discipline.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 14. At 2 or above: none.

Nine pieces ask what place normative claims should have in theory. Kalkman (2026) invites rival normative purposes for crisis management or an ethical defence of the functionalist one. Seidemann (2024) asks by what criteria a response to paradox counts as good. Werner et al. (2026) ask how to judge an organization that reasons beyond its institutional obligations. Gümüsay and Reinecke (2024) hand the judgment of desirable futures to stakeholders beyond academia. The disagreement concerns warrant: Suddaby (2024) wants knowledge that joins objective and normative orientations, Mena et al. (2026) ask deliberation research to move from ideals back to description, and Langenmayr et al. (2024) leave open whether a societal orientation can be reconciled with the business case. Who decides that a normative claim is sound, and by what procedure, stays unanswered.

**Entry.** None. Every member scores 0.

### R11. Where do the boundaries of the field's working constructs lie: what counts as a logic, a paradox, an organization, an institution?

- **Short name:** construct boundaries.
- **Kind and origin:** cross-cutting; from O02 + part of C04.
- **Members** (16 OQs from 9 pieces): Laine 2023: OQ-laine2023-02; Ocasio 2023: OQ-ocasio2023-04 (bc); Wright 2023: OQ-wright2023-04; Seidemann 2024: OQ-seidemann2024-01, -16; Schildt 2025: OQ-schildt2025-02, -07 (bc); Hawbaker 2025: OQ-hawbaker2025-03; Derek Robinson 2025: OQ-derekrobinson2025-03 (bc), -07; Dion 2025: OQ-dion2025-02, -04, -05, -13, -14; Schoeneborn 2026: OQ-schoeneborn2026-10.
- **Representative quotation:** OQ-schildt2025-02: “what exactly counts as a logic?" and "how do we draw the boundaries of an institutional logic?” (p. 16, "Towards a more dynamic and local view")
- **Support:** theory/review articles 6.5; commentary or exchange pieces 2; counted at ½ because they enter through boundary conditions only: Ocasio 2023; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 3; most recent ask 2026-09-19 (schoeneborn2026), 2 months before the run.
- **Level:** Field: the discipline's concepts.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 16. At 2 or above: none.

These askers want to know where the edges of the field's working concepts lie. Schildt and Kodeih (2025) ask what counts as a logic and how to draw its boundary. Seidemann (2024) asks what paradox's markers mean under different ontologies, and whether a tension still counts as a paradox when one feature is weak (OQ-seidemann2024-16, added at hand-check). Dion et al. (2025) ask what organizationality is predicated of; the person-institution exchange asks what makes a person-brand an institution; Wright, Kent, Hällgren and Rouleau (2023) ask how the definition of an extreme context shifts as researchers adopt it. Ocasio (2023) marks where institutional explanation stops (OQ-ocasio2023-04, added at hand-check, a boundary condition). The askers disagree on the remedy: Schoeneborn et al. (2026) want agreed foundations, and Dion et al. warn that an umbrella concept conceals incompatible postures. Who settles such boundaries is the question R12 takes up.

**Entry.** None. Every member scores 0.

### R12. Who decides which words, distinctions and standards of good theory a scholarly community uses, and by what procedure?

- **Short name:** words and standards.
- **Kind and origin:** topical; from O08 + C04.
- **Members** (22 OQs from 9 pieces): Gümüsay 2024: OQ-gumusay2024-11; Abend 2024: OQ-abend2024-02, -03, -04, -05, -06, -07, -08 (bc); Prasad 2024: OQ-prasad2024-03 (bc), -04 (bc), -06, -07; Suddaby 2024: OQ-suddaby2024-01, -03 (bc), -04; Giovannoni 2025: OQ-giovannoni2025-06, -07; Dion 2025: OQ-dion2025-13; Ernst 2026: OQ-ernst2026-03, -06; Höllerer 2026: OQ-hollerer2026-06; Schoeneborn 2026: OQ-schoeneborn2026-02.
- **Representative quotation:** OQ-abend2024-04: “Fellow community members! Which aims should be served by our key words and distinctions? Which aims are more important to us, when, and where?” (p. 7, "5. Democracy, Unfreedom, Usefulness")
- **Support:** theory/review articles 5; commentary or exchange pieces 3; editorial signal y; distinct volumes 3 (5, 6, 7); citation edges among askers 8; most recent ask 2026-09-19 (schoeneborn2026), 2 months before the run.
- **Level:** Field: the scholarly community.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 22. At 2 or above: none.

The Abend exchange is the core. Abend (2024) asks who should decide a community's key words and distinctions, by which second-order criteria and at whose cost, and he answers with democratic deliberation; he sets aside who belongs to the community. Prasad (2024) doubts the mechanism and offers problem-solving communities, whose closure she expects to be temporary. Suddaby (2024) would keep construct clarity and add process. Theory articles meet the same problem in their own programmes: Schoeneborn et al. (2026) want agreed foundations for organizationality, Ernst, Lassalle, Kerr and Robinson (2026) ask how orthodoxies define good research, and Giovannoni and Quattrone (2025) say editors and reviewers would have to accept open-ended work. The 2026 editorial sets one standard itself: every submission must state its contribution relative to existing literature (OQ-hollerer2026-06). The procedure stays in dispute, and no asker says who counts as a member of the deciding community.

**Entry.** None. Every member scores 0. The editorial requirement in OQ-hollerer2026-06 binds any submission, this one included, and that is a condition and not an opening.

### R13. What do organizations do, and what do they owe, when democratic institutions weaken, and what do they do to democracy in turn?

- **Short name:** democracy.
- **Kind and origin:** topical; from O09 + O36 + C06.
- **Members** (22 OQs from 8 pieces): Scherer 2023: OQ-scherer2023-04, -08, -11, -13; Sasaki 2024: OQ-sasaki2024-06; du Gay 2024: OQ-dugay2024-06, -07; Giovannoni 2025: OQ-giovannoni2025-08; Winkler 2025: OQ-winkler2025-02, -03 (bc); Patriotta 2025: OQ-patriotta2025-04; Mena 2026: OQ-mena2026-11, -14, -15, -16, -17, -18, -19, -20, -21, -23; Ernst 2026: OQ-ernst2026-07.
- **Representative quotation:** OQ-mena2026-17: “future research could examine how organizations can strengthen civic engagement and solidarity in contexts that are not fully democratic, in which democratic backsliding is occurring, or where the regime is hybrid or altogether nondemocratic” (p. 15, "Republican inside-out focus")
- **Support:** theory/review articles 8; commentary or exchange pieces 0; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 0; most recent ask 2026-04-07 (ernst2026), 7 months before the run.
- **Level:** Multi-level: the organization in its polity.
- **Fit (final scores of members):** 3 × 0; 2 × 1; 1 × 2; 0 × 19. At 2 or above: OQ-scherer2023-13 (2).

The askers treat liberal democracy as a condition that can fail, and they ask in both directions. Mena, Mair and Bruder (2026) pose most of the questions: how national conflict and right-wing sentiment shape organizations, what organizations can do for civic engagement where democracy is weak, and whether workplace democratic experiments scale to society. Winkler and Schoeneborn (2025) ask organization scholars to treat post-truth communication as a serious topic. Du Gay and Lopdrup Hjorth (2024) ask whether anti-formal reforms have weakened states. Scherer and Neesham (2023) ask how action can be organized to foster the communicative conditions that mature citizens need. The askers place the remedy in different sites: formal state organization (du Gay and Lopdrup Hjorth), working organizations as places to learn democratic norms (Scherer and Neesham; Mena et al.), or established organizations admitting their own disorder (Winkler and Schoeneborn). No citation links any two of the eight.

**Entry.** None. One member scores 2 (OQ-scherer2023-13) and two score 1. Scherer and Neesham's capacity is civic and their remedy lies outside the systems, in skills "independent of digital assistance" (scherer2023 record, Fit, citing p. 18); the brief describes competence inside them.

### R14. What changes when a generative-AI system or algorithm takes part in organizing (in category work, legitimacy tests, teams) as a participant and not only as a tool?

- **Short name:** AI as participant.
- **Kind and origin:** topical; from O22 + C15.
- **Members** (26 OQs from 8 pieces): Orlikowski 2023: OQ-orlikowski2023-07; Stark 2024: OQ-stark2024-07; Phillips 2024: OQ-phillips2024-05, -06, -07, -08, -09, -10, -11, -12, -13, -14, -15, -16 (bc); Hsu 2024: OQ-hsu2024-06; Grodal 2024: OQ-grodal2024-02, -03, -04, -05, -06, -07, -08, -09; Hinds 2024: OQ-hinds2024-18; Patriotta 2025: OQ-patriotta2025-10; Friedrich 2026: OQ-friedrich2026-08.
- **Representative quotation:** OQ-phillips2024-09: “How does the introduction of artificial persons into an organization change how we think about what organizations are, how they are constructed and how they function?” (p. 11, "The implications of generative AI in organizations")
- **Support:** theory/review articles 5; commentary or exchange pieces 3; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 10; most recent ask 2026-04-01 (friedrich2026), 7 months before the run.
- **Level:** Multi-level: interaction, organization and field.
- **Fit (final scores of members):** 3 × 0; 2 × 4; 1 × 20; 0 × 2. At 2 or above: OQ-stark2024-07 (2), OQ-phillips2024-07 (2), OQ-phillips2024-08 (2), OQ-phillips2024-09 (2).

This is the journal's convened exchange on generative AI, with five theory articles around it. Phillips, Kalvapalle and Kennedy (2024) claim that generative AI now takes part in constructing categories, and they ask what organizations are once artificial persons join them and how an AI teammate changes a team. The two replies contest the premise from opposite sides. Grodal, Ha, Hood and Rajunov (2024) hold that participation is a perception, produced when a technology seems to cross the human–machine boundary, and they ask when customers accept the crossing. Hsu and Bechky (2024) hold that technologies have long shaped categories and ask category research to treat technology as an actor. Outside the exchange, Stark and Vanden Broeck (2024) ask about the sociality that arises when the communication partner is an algorithm, Patriotta et al. (2025) ask how algorithms co-produce legitimacy tests, and Friedrich (2026) asks how AI inputs could extend an organization's attunement. Whether AI is a participant, a perceived participant, or one more technology remains undecided. Ten citation edges link the askers, more than in any other conversation. Friedrich's one member here is a question the lead ruled as put to practitioners (DECISIONS, H8); without that article the conversation has 4 theory articles, 3 volumes (4, 5, 6), 9 edges and a most recent ask of November 2025.

**Entry.** As a foil only. Four members score 2 and twenty score 1; no member is answered. Every asker here takes the system as something a person deals with directly (a participant, a teammate, a partner), which the brief calls the direct dyad and lists as its first failure mode. A paper can enter by contesting that premise, and it then argues against the best-connected AI conversation in the journal.

### R15. What should scholars do with and for the people and struggles they study: critic, activist, co-inquirer or adviser?

- **Short name:** scholars and practice.
- **Kind and origin:** cross-cutting; from O20 + C13.
- **Members** (11 OQs from 8 pieces): Fotaki 2023: OQ-fotaki2023-04; Gümüsay 2024: OQ-gumusay2024-08, -12; Paca 2024: OQ-paca2024-04; Langenmayr 2024: OQ-langenmayr2024-09; Prasad 2024: OQ-prasad2024-07; Krautzberger 2024: OQ-krautzberger2024-10; Ernst 2026: OQ-ernst2026-07; Corver 2026: OQ-corver2026-07, -08, -09.
- **Representative quotation:** OQ-corver2026-09: “a richer empirical understanding is needed of how theorists and practitioners can work together to support the development of organizational capacities constitutive of being a good “tool user.”” (p. 17, "Discussion")
- **Support:** theory/review articles 7; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 2; most recent ask 2026-07-28 (corver2026), 3 months before the run.
- **Level:** Field: the relation between scholars and the people their theories concern.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 1; 0 × 10. At 2 or above: none.

The askers want theory made with the people it concerns, and they do not agree on the scholar's role. Corver and Filler (2026) ask how theorists and practitioners can build together the capacities of a good "tool user", and which decisions modeling has in fact aided. Gümüsay and Reinecke (2024) call for future labs and for stakeholders in the judgment of desirability. Fotaki (2023) and Langenmayr et al. (2024) invite academic activism, Prasad (2024) invites readers into an infrastructure for problem-solving research, and Ernst et al. (2026) ask whether inquiry can be divorced from political and economic crisis. Evidence of effect is what stays unanswered: only Corver and Filler and Paca and Rozuel (2024) ask for a check on whether the tool helped. The roles on offer (co-inquirer, activist, convenor, adviser) are not compared in any article.

**Entry.** None. One member scores 1 (OQ-corver2026-09), through the phrase "tool user"; see R18.

### R16. Under what conditions do new practices, forms and institutions emerge, take hold and displace old ones?

- **Short name:** institutional emergence.
- **Kind and origin:** topical; from O16 + C10.
- **Members** (26 OQs from 8 pieces): Orlikowski 2023: OQ-orlikowski2023-01, -06; Jackwerth-Rice 2023: OQ-jackwerthrice2023-02, -03, -04, -05, -06, -07, -09, -11; Ocasio 2023: OQ-ocasio2023-01, -03; Powell 2023: OQ-powell2023-01, -02, -03, -04, -05, -06, -09, -12; Schildt 2025: OQ-schildt2025-04; Nigam 2025: OQ-nigam2025-05, -08; Derek Robinson 2025: OQ-derekrobinson2025-05; Wedlin 2025: OQ-wedlin2025-03, -04.
- **Representative quotation:** OQ-powell2023-09: “How do new ideas and practices enter organizations and stick? Why do new kinds of institutions emerge, take root, and persist? When are organizations more vulnerable to changes in the wider environment and when are they resisted?” (p. 15, "Institutional change")
- **Support:** theory/review articles 6; commentary or exchange pieces 2; editorial signal n; distinct volumes 2 (4, 6); citation edges among askers 3; most recent ask 2025-12-23 (derekrobinson2025), 10 months before the run.
- **Level:** Field, with calls to join micro, meso and macro levels.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 2; 0 × 24. At 2 or above: none.

Powell and DiMaggio (2023) call the entry, persistence and resistance of new practices and institutions perhaps the most vexing questions in organization studies. The other askers each hold a piece. Jackwerth-Rice, Koehrsen and Mattes (2023) ask whether changing an institution is easier than building one and whether the sufficiency of resources can be known before the attempt. Ocasio (2023) asks for the functional origins of institutions. Orlikowski and Scott (2023) ask which further industry-structuring mechanisms digitalization displaces. Wedlin and Weinryb (2025) ask how hype acts on institutions, and the person-institution commentaries ask when persons arise as institutions. The askers disagree about agents. Powell and DiMaggio warn against "muscular" change agents and look to a field's receptivity; Jackwerth-Rice et al. keep the entrepreneur at the centre; Orlikowski and Scott describe a displacement that nobody intends.

**Entry.** None. Two members score 1, both Orlikowski and Scott's; they are discussed under R21.

### R17. Who answers for an outcome when an algorithm, a platform or a loosely bounded collective decides and no office-holder does?

- **Short name:** accountability.
- **Kind and origin:** cross-cutting; from O13 + X07.
- **Members** (10 OQs from 7 pieces): Scherer 2023: OQ-scherer2023-06, -07; Jaser 2024: OQ-jaser2024-03; Stark 2024: OQ-stark2024-04; Mena 2026: OQ-mena2026-03, -15; Friedrich 2026: OQ-friedrich2026-17; Pavlisa 2026: OQ-pavlisa2026-03; Schoeneborn 2026: OQ-schoeneborn2026-04, -06.
- **Representative quotation:** OQ-stark2024-04: “But who or what is accountable when an algorithm exercises decisions that occur faster and with a vastly larger number of inputs than a human can physiologically comprehend and react to (Vesa & Tienari, 2022, p. 1137)?” (p. 14, "Accountability")
- **Support:** theory/review articles 7; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-09-19 (schoeneborn2026), 2 months before the run.
- **Level:** Multi-level: individuals, collectives and the systems that decide between them.
- **Fit (final scores of members):** 3 × 0; 2 × 1; 1 × 4; 0 × 5. At 2 or above: OQ-stark2024-04 (2).

Stark and Vanden Broeck (2024) pose the question directly: who or what is accountable when an algorithm decides faster, and on more inputs, than a human can follow? Schoeneborn et al. (2026) ask how shifting actorhood between a collective and its individuals changes who is held responsible. Mena et al. (2026) ask how decision-makers can be made accountable to all members. Pavlisa et al. (2026) concede that their theory has no criteria for deciding which stakeholders a firm answers to. Jaser and Tourish (2024) ask whose interests surveillance serves, and Scherer and Neesham (2023) propose oaths and regulation. The answers on offer do not agree: Stark and Vanden Broeck report distributed liability as one proposal, Scherer and Neesham put the duty on designers and managers, and Schoeneborn et al. study the act of attribution. No citation links any two of the seven.

**Entry.** Citable, with a caution about the word. One member scores 2 (OQ-stark2024-04) and four score 1. The brief's first part restores accountability in the coordination sense: a person works out whether an outcome came from the system, the counterpart or both. The askers mean liability and responsibility. The hand-check on OQ-stark2024-04 reads the question as legal in context and holds that interpreting "cannot reach decisions too fast for a person to follow". GDOC, which uses the word in Okhuysen and Bechky's sense, is the version most exposed to the equivocation.

### R18. What happens to competence and expertise when new knowledge or technology arrives: is it lost, kept or rebuilt, and what must people still be able to do?

- **Short name:** competence and expertise.
- **Kind and origin:** cross-cutting; from O07 + X11.
- **Members** (14 OQs from 7 pieces): Fotaki 2023: OQ-fotaki2023-06; Guercini 2023: OQ-guercini2023-06, -07, -08, -10, -11, -12; Jackwerth-Rice 2023: OQ-jackwerthrice2023-08; Stark 2024: OQ-stark2024-03; Hsu 2024: OQ-hsu2024-08; Hinds 2024: OQ-hinds2024-07, -17; Corver 2026: OQ-corver2026-09, -11.
- **Representative quotation:** OQ-hsu2024-08: “finding a way to retain the expertise that will be needed to critically analyse, question and channel this powerful technology is a formidable challenge.” (p. 12, "The Deeper Role that Technology Plays in Social Categorization")
- **Support:** theory/review articles 6; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-07-28 (corver2026), 3 months before the run.
- **Level:** Organization and profession, with individual-level questions.
- **Fit (final scores of members):** 3 × 0; 2 × 3; 1 × 4; 0 × 7. At 2 or above: OQ-hsu2024-08 (2), OQ-hinds2024-07 (2), OQ-hinds2024-17 (2).

These askers ask what happens to what organizations and professionals know how to do when something new arrives. Guercini and Lechner (2023) propose that acquiring a competence can erode an existing one, and they leave open which kinds and timings produce attrition. Hinds and von Krogh (2024) ask whether generative AI brings "hyper-generalization", with specialist tasks no longer visible to members, and whether encapsulating some practices weakens a team's capacity to evolve others. Hsu and Bechky (2024) call the retention of expertise able to question the technology a formidable challenge. Stark and Vanden Broeck (2024) want comparative studies of professional expertise under algorithmic management, and Corver and Filler (2026) ask how organizations build the capacities of a good "tool user". The mechanism of loss is unsettled: interference between competences in Guercini and Lechner, encapsulation inside a system in Hinds and von Krogh. No asker tests either, and none of the seven cites another.

**Entry.** Partial, and the nearest home for the construct's genus. Three members score 2 (OQ-hsu2024-08, OQ-hinds2024-07, OQ-hinds2024-17) and four score 1. The askers ask whether existing expertise is lost, kept or rebuilt. The brief adds a fourth possibility they do not consider: demand moves to a different competence, the one needed to work with another person through the system. That is a reframing and not an answer, because the askers mean domain expertise; the hand-check on OQ-hsu2024-08 notes that the brief "names a different competence, says nothing on retaining craft". Scherer and Neesham's civic competence and Patriotta et al.'s "competent agency" are rival competence constructs in the corpus, at other levels.

### R19. How do digital media and platforms change how publics form, judge organizations and mobilize?

- **Short name:** digital media and publics.
- **Kind and origin:** topical; from C16 + part of O37.
- **Members** (12 OQs from 7 pieces): Leitzinger 2023: OQ-leitzinger2023-09, -10; Pozner 2023: OQ-pozner2023-08, -15; Scherer 2023: OQ-scherer2023-08; Patriotta 2025: OQ-patriotta2025-08, -09, -10; Nigam 2025: OQ-nigam2025-10; Derek Robinson 2025: OQ-derekrobinson2025-04; Mena 2026: OQ-mena2026-12, -18.
- **Representative quotation:** OQ-pozner2023-15: “Empirical work might explicitly consider social media’s role in social evaluation (Etter et al., 2019; Seidel et al., 2020) and compare scandal construction before and after the widespread adoption of social media.” (p. 16, "Future directions")
- **Support:** theory/review articles 5; commentary or exchange pieces 2; editorial signal n; distinct volumes 3 (4, 6, 7); citation edges among askers 2; most recent ask 2026-03-31 (mena2026), 7 months before the run.
- **Level:** Field: publics, media and the organizations they evaluate.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 5; 0 × 7. At 2 or above: none.

Five theory and review articles and two commentaries ask what digital media do to the publics that judge organizations and press on them. Leitzinger and Waeger (2023) ask when movements should use social media or traditional news, and when street protest or online protest is more productive. Pozner and Hannigan (2023) propose comparing scandal construction before and after social media. Patriotta et al. (2025) ask how platform affordances shape the spread of competing justifications, and how influencers and algorithms take part. Mena et al. (2026) ask how social media and AI alter public deliberation. Nigam, Amis and Logue (2025) ask whether person-institutions arise more often where digital connection offers new forms of belonging. All of these questions are prospective; no asker has the before-and-after comparison that Pozner and Hannigan propose.

**Entry.** None. Five members score 1 and none higher. The platforms in this conversation carry and curate what audiences see. They evaluate no one's work and bind no pair of people doing interdependent work, so the brief's triad is absent; the hand-check says so of OQ-patriotta2025-08 and OQ-patriotta2025-10.

### R20. How much can one actor do against the structures they sit in, and where do their resources come from?

- **Short name:** actor and structure.
- **Kind and origin:** cross-cutting; from X09.
- **Members** (12 OQs from 7 pieces): Bacq 2023: OQ-bacq2023-08; Jackwerth-Rice 2023: OQ-jackwerthrice2023-05, -08, -09, -10, -11; Friesl 2023: OQ-friesl2023-07; Powell 2023: OQ-powell2023-13; Stevenson 2024: OQ-stevenson2024-02; Seidemann 2024: OQ-seidemann2024-15; Brennecke 2025: OQ-brennecke2025-01, -13.
- **Representative quotation:** OQ-jackwerthrice2023-05: “it remains an open question to what degree IEs’ structural embeddedness influences their ability to mobilize resources during different stages of institutional entrepreneurship” (p. 15, "Discussion and Conclusion")
- **Support:** theory/review articles 7; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 0; most recent ask 2025-09-28 (brennecke2025), 13 months before the run.
- **Level:** Individual within field and network structures.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 12. At 2 or above: none.

Seven articles ask how much to credit the individual. Jackwerth-Rice et al. (2023) ask how embeddedness shapes an institutional entrepreneur's access to resources at each stage, and whether sufficiency can be known before the attempt. Powell and DiMaggio (2023) ask how meso-level resources and macro-level conditions enable or thwart individual innovators. Bacq et al. (2023) ask how individuals break out of narratives that reinforce themselves; Stevenson, Honingh and Brandsen (2024) ask how flexibly actors alter a logic's centrality; Brennecke et al. (2025) ask how agency and the history of a tie shape each other. The askers lean against the heroic actor without agreeing on the alternative. Friesl, Brielmaier and Dobusch (2023) are the only askers who propose a design to estimate the share of an outcome owed to the person.

**Entry.** None. Every member scores 0.

### R21. What are the indirect, hidden and delayed consequences of digitalization for institutions and for work?

- **Short name:** the digital undertow.
- **Kind and origin:** topical; from O15 + C11.
- **Members** (20 OQs from 7 pieces): Orlikowski 2023: OQ-orlikowski2023-01, -02, -06, -07, -09; Scherer 2023: OQ-scherer2023-05; Justesen 2024: OQ-justesen2024-01, -04, -12, -14, -15, -16, -17 (bc); Stark 2024: OQ-stark2024-05; Phillips 2024: OQ-phillips2024-05, -06; Hsu 2024: OQ-hsu2024-04, -05; Hinds 2024: OQ-hinds2024-02, -12.
- **Representative quotation:** OQ-orlikowski2023-02: “So, there is little attention focused on the undertow, and thus limited knowledge of the corollary effects that are being generated by digitalization or their consequences.” (p. 5, "The Digital Undertow")
- **Support:** theory/review articles 5; commentary or exchange pieces 2; editorial signal n; distinct volumes 2 (4, 5); citation edges among askers 6; most recent ask 2024-10-29 (hinds2024), 24 months before the run.
- **Level:** Multi-level: from work practices through organizations to industry-level institutions.
- **Fit (final scores of members):** 3 × 0; 2 × 3; 1 × 14; 0 × 3. At 2 or above: OQ-justesen2024-01 (2), OQ-justesen2024-16 (2), OQ-stark2024-05 (2).

Orlikowski and Scott (2023) name the question: digitalization has corollary effects, distant in space and time from the programme that causes them, and researchers know little about them. The commentaries on generative AI adopt the frame (Hsu and Bechky, 2024; Phillips et al., 2024). Justesen and Plesner (2024), who cite Orlikowski and Scott, ask for systematic knowledge of the invisible work that keeps the automated organization running. Hinds and von Krogh (2024) ask what speeds or halts the absorption of functions into a system its users cannot inspect, Scherer and Neesham (2023) ask how new technologies reduce persons to data, and Stark and Vanden Broeck (2024) ask which contradictions will drive the evolution of algorithmic management. The inventory itself remains open: which institutional apparatuses digitalization displaces, and which kinds of work go unseen. Every asker sits in volume 4 or 5; no article in volumes 6 or 7 has an open question on the undertow.

**Entry.** Adjacent throughout, enterable at one point. Three members score 2 (OQ-justesen2024-01, OQ-justesen2024-16, OQ-stark2024-05) and fourteen score 1. PAPER's opening on quiet displacement belongs to this conversation, but Orlikowski and Scott ask about institutions and industries, and the brief works at the level of a person in an interaction. The one opening is Justesen and Plesner's invisible work: exercising the three parts could be argued to be work of that kind, which the hand-check calls "a new claim for the paper to argue, not an answer the brief already holds".

### R22. What changes when a technology stands between the people who organize: is it a medium they communicate through or a party they communicate with?

- **Short name:** technology between people.
- **Kind and origin:** cross-cutting; from X06 + Whyte's part of O35.
- **Members** (22 OQs from 7 pieces): Whyte 2023: OQ-whyte2023-02, -03, -04, -05, -06, -08 (bc), -09, -10, -11, -12, -13, -14; Justesen 2024: OQ-justesen2024-08; Stark 2024: OQ-stark2024-06, -07, -09; Räcker 2024: OQ-racker2024-05 (bc); Phillips 2024: OQ-phillips2024-08; Hinds 2024: OQ-hinds2024-04, -10, -25; Mena 2026: OQ-mena2026-12.
- **Representative quotation:** OQ-stark2024-07: “This new sociality—when the partner with which we are communicating is an algorithm— will be a critical component of further research on algorithmic management.” (p. 16, "Out of Bounds")
- **Support:** theory/review articles 5.5; commentary or exchange pieces 1; counted at ½ because they enter through boundary conditions only: Räcker 2024; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 1; most recent ask 2026-03-31 (mena2026), 7 months before the run.
- **Level:** Interaction: meetings, teams and platform exchanges carried through a system.
- **Fit (final scores of members):** 3 × 2; 2 × 5; 1 × 5; 0 × 10. At 2 or above: OQ-stark2024-06 (3), OQ-stark2024-07 (2), OQ-stark2024-09 (2), OQ-phillips2024-08 (2), OQ-hinds2024-04 (3), OQ-hinds2024-10 (2), OQ-hinds2024-25 (2).

Seven pieces ask what a technology placed between people does to their organizing, and they split on what the technology is in the relation. For Whyte, Comi and Mosca (2023) it is a medium: they ask how presence and coherence are made when participants are on screen and bodily elsewhere, and they invite debate with Uhlin (2022) on whether an online meeting is one practice or several. For Stark and Vanden Broeck (2024) it is a party: they hold that organizational design and interface design are now inseparable, ask for study of the communication field joined to the platform form, and expect that "This new sociality—when the partner with which we are communicating is an algorithm" will be a component of further research (OQ-stark2024-07). Hinds and von Krogh (2024) stand between the two. Their system guides colleagues' work with one another, and they ask whether members will "blindly follow guidance from the AI" and what shapes members' "dynamic relations with AI to coordinate their work". Phillips et al. (2024) ask how engaging with generative AI affects human interaction, and Mena et al. (2026) how AI shapes deliberation inside organizations. No asker poses the choice between medium and party as a question. The split is my reading of their premises; F's clustering made the same reading before F had seen any fit data (DECISIONS, S9a).

**Entry.** Yes; this is the best entry at the level of a whole conversation. Two members score 3 (OQ-stark2024-06, OQ-hinds2024-04) and five score 2. The split between medium and party is what ASM calls the dyad dilemma, a moderated dyad against a direct dyad, and the brief's answer is a third position: an intermediary that evaluates and binds two people. Three limits apply. The fit sits in Stark's and Hinds's halves; Whyte et al.'s twelve questions score 0 or 1, because a video conference evaluates no one. Stark and Vanden Broeck take the step the brief rejects, so the paper answers their call while disputing their premise. And one citation edge links the askers (Phillips et al. cite Stark and Vanden Broeck).

### R23. Which neighbouring fields, topics and vocabularies should organization theory open to, and how does it stay cumulative while doing so?

- **Short name:** openness to other fields.
- **Kind and origin:** topical; from C12.
- **Members** (12 OQs from 7 pieces): Powell 2023: OQ-powell2023-14; Stark 2024: OQ-stark2024-06; Phillips 2024: OQ-phillips2024-12, -15; Mutch 2025: OQ-mutch2025-06; Hawbaker 2025: OQ-hawbaker2025-04; Mena 2026: OQ-mena2026-02, -10; Höllerer 2026: OQ-hollerer2026-01, -02, -03, -04.
- **Representative quotation:** OQ-hollerer2026-04: “To remain relevant and contribute knowledge and answers to such pressing and complex issues, organizational scholarship must be able to skilfully handle such emerging developments and therefore also be willing to engage with novel, unfamiliar ideas and perspectives.” (p. 5, "'Catalysing & Crystallizing'")
- **Support:** theory/review articles 4; commentary or exchange pieces 2; editorial signal y; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 2; most recent ask 2026-07-26 (hollerer2026), 3 months before the run.
- **Level:** Field: the discipline's boundaries.
- **Fit (final scores of members):** 3 × 1; 2 × 0; 1 × 5; 0 × 6. At 2 or above: OQ-stark2024-06 (3).

The 2026 editorial creates a journal section for emerging topics and asks for proposals that "engage with emerging topics, bridge disciplinary boundaries, introduce new conceptual vocabularies" (OQ-hollerer2026-01); it holds that scholarship must engage unfamiliar ideas to handle emerging developments, among which the record's scope note lists artificial intelligence. Authors had already asked for particular openings. Powell and DiMaggio (2023) urge scholars to belong to two communities. Mutch (2025) asks the field to take law seriously, and Mena et al. (2026) ask it to reconnect with industrial relations. Stark and Vanden Broeck (2024) ask for organization and communication to be studied as one field, and Phillips et al. (2024) ask many research streams to take technology and the symbolic seriously. Hawbaker and Hallett (2025) add a condition: institutional theory should work beside other accounts without absorbing them. No asker says how a field imports without subsuming and still accumulates.

**Entry.** A licence, not a question. One member scores 3 (OQ-stark2024-06, counted under R22) and five score 1, four of them the editorial's. The editors welcome a new vocabulary and name the technology; they ask for themed-section proposals, and the same editorial requires every submission to state its contribution to existing literature. The signal supports coining a term. It does not say which conversation the term should answer.

### R24. How do scholars' own selves, careers and positions enter their theorizing, and how should they account for that?

- **Short name:** scholars' reflexivity.
- **Kind and origin:** topical; from O11 + part of C08.
- **Members** (17 OQs from 6 pieces): Petriglieri 2023: OQ-petriglieri2023-01, -02, -04 (bc), -05; Wright 2023: OQ-wright2023-02, -03, -05, -06; Lantela 2024: OQ-lantela2024-10; Seidemann 2024: OQ-seidemann2024-03; Keller 2025: OQ-keller2025-01; Ernst 2026: OQ-ernst2026-01, -02, -03, -04, -05, -08.
- **Representative quotation:** OQ-wright2023-06: “We invite future research to draw on our theoretical framework and explore how, when, where and for whom a meaningful sense of self operates in research in extreme as well as non-extreme contexts.” (p. 20, "Discussion")
- **Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 2; most recent ask 2026-04-07 (ernst2026), 7 months before the run.
- **Level:** Individual: the scholar.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 17. At 2 or above: none.

These askers turn the field's questions on the scholar. Petriglieri and Ashford (2023) ask for new chronicles of academic working lives. Wright et al. (2023) ask whether researchers can switch between selves across a project or a career, and which modes of engagement combine well in a team. Ernst et al. (2026) ask how reflexivity links to theorizing and what a researcher owes the field. Keller, Berti and Smith (2025) ask scholars to treat the tensions in their own work as material for theory. The proposals pull apart: Ernst et al. want the researcher's position objectified, whereas Wright et al. and Petriglieri and Ashford want it lived and narrated.

**Entry.** None. Every member scores 0.

### R25. How do people in organizations imagine what is not present, futures above all, and what does imagining do to organizing now?

- **Short name:** futures and imagination.
- **Kind and origin:** topical; from O19 + C24.
- **Members** (21 OQs from 6 pieces): Gümüsay 2024: OQ-gumusay2024-02, -03, -04, -05, -10; Garud 2025: OQ-garud2025-03; Skade 2025: OQ-skade2025-01, -02, -03, -04, -05, -06 (bc), -07 (bc); Friedrich 2026: OQ-friedrich2026-11; Corver 2026: OQ-corver2026-06; Porsfelt 2026: OQ-porsfelt2026-04, -05, -06, -07, -08, -09.
- **Representative quotation:** OQ-skade2025-01: “future research could clarify how these divergent futures inform strategic decisions and create productive tensions within organizations.” (p. 18, "Tensions between futures")
- **Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (5, 6, 7); citation edges among askers 3; most recent ask 2026-09-21 (porsfelt2026), 2 months before the run.
- **Level:** Interaction and organization.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 21. At 2 or above: none.

Skade (2025) asks how co-existing futures inform strategic decisions and which future-making practices actors enact. Porsfelt, Vestergaard and Hjorth (2026) widen the object from futures to imagination as engagement with the non-present: what triggers short-lived shared imagining, what it draws on, and how it matters without hardening into structure. Gümüsay and Reinecke (2024) ask how projected climate pathways and new valuation methods would change organizing, and how decisions unfold in prefigurative settings. Friedrich (2026) asks how meetings can invite collective imagination. The disagreement concerns what imagination produces: Skade has actors synthesize tensions, while Porsfelt et al. want imagination studied apart from creative output. Whether imagined futures change present decisions remains an assumption in all of them. Friedrich enters through one question the lead ruled as put to practitioners (DECISIONS, H8); without that article the conversation has 5 askers.

**Entry.** None. Every member scores 0. PAPER quotes Porsfelt et al. for a phrase; their open questions concern imagination and offer the paper no entry.

### R26. Under which category does a person belong to an organization (member, user, contributor, citizen, stakeholder), and who decides?

- **Short name:** membership categories.
- **Kind and origin:** cross-cutting; from O18 + part of X04.
- **Members** (7 OQs from 6 pieces): Georgiou 2023: OQ-georgiou2023-11; Stark 2024: OQ-stark2024-01; Abend 2024: OQ-abend2024-07; Mena 2026: OQ-mena2026-01, -09; Pavlisa 2026: OQ-pavlisa2026-03; Schoeneborn 2026: OQ-schoeneborn2026-08.
- **Representative quotation:** OQ-mena2026-01: “who qualifies as the people (or demos; Koenig-Archibugi, 2022): employees, a larger set of organizational members and/or stakeholders, or a broader demos?” (p. 3, introduction)
- **Support:** theory/review articles 5; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-09-19 (schoeneborn2026), 2 months before the run.
- **Level:** Organization and community.
- **Fit (final scores of members):** 3 × 0; 2 × 1; 1 × 0; 0 × 6. At 2 or above: OQ-stark2024-01 (2).

Six askers, writing on different topics, stop at the same question: under which category is a person inside? Mena et al. (2026) ask whether the demos of a firm is employees, members, stakeholders or a broader public, and how citizens' rights and members' rights connect or conflict. Schoeneborn et al. (2026) ask whether attributing people to a collective as members constitutes it differently from attributing them as contributors. Stark and Vanden Broeck (2024) ask why one category, the user, now covers employees, professionals, consumers and suppliers, and what the label hides. Abend (2024) cannot say who belongs to the deliberating community; Pavlisa et al. (2026) have no criteria for which stakeholders a firm answers to; Georgiou and Arenas (2023) ask which practices keep a community's boundary. No article reconciles the categories, and each asker uses the one its literature supplies. The conversation is thin: seven questions, about one per asker.

**Entry.** None at the level of the conversation. One member scores 2 (OQ-stark2024-01). The brief does not say who counts as a member. It offers one difference the label "user" masks, whether a user faces the system alone or works with a counterpart through it, and the hand-check lowered the score because Stark and Vanden Broeck's users include the streaming listener, who has no counterpart.

### R27. How do movements and collective action form, press on organizations and markets, and survive co-optation?

- **Short name:** movements.
- **Kind and origin:** topical; from O24 + C09.
- **Members** (35 OQs from 6 pieces): Bacq 2023: OQ-bacq2023-01; Leitzinger 2023: OQ-leitzinger2023-01, -02, -03, -04, -05, -06, -07, -08, -09, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -21, -22, -23, -24, -25, -26, -28, -29, -30, -32 (bc), -33; Pozner 2023: OQ-pozner2023-10; Jaser 2024: OQ-jaser2024-07; Mena 2026: OQ-mena2026-19; Friedrich 2026: OQ-friedrich2026-16.
- **Representative quotation:** OQ-leitzinger2023-01: “Key questions remain as to how social movements that target markets and their actors form or, if already established, become mobilized to address new issues.” (p. 7, "Phase 1: Emergence")
- **Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-04-01 (friedrich2026), 7 months before the run.
- **Level:** Field: movements, markets and the organizations they target.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 35. At 2 or above: none.

Leitzinger and Waeger (2023) supply 30 of the 35 questions: how market-targeting movements form, whether co-optation is inevitable and at which stage of market development, when activists leave co-opted movements, and how movements keep members engaged without mission drift. Five articles from other literatures each touch one of these. Bacq et al. (2023) ask when ventures born of shame give rise to collective action. Pozner and Hannigan (2023) ask how movements use scandal. Mena et al. (2026) ask how organizations institutionalize dissent, and Friedrich (2026) how democratic organizing resists ideological co-optation. Jaser and Tourish (2024) ask what collective response to surveillance goes beyond individual resistance or conventional unionism. Co-optation is the shared unknown, and the askers have not joined it across settings.

**Entry.** None. Every member scores 0. The co-optation these askers mean is of movements by markets and firms; Stark and Vanden Broeck's co-optation of users by platforms, which the brief builds on, is a different relation and none of these askers cites it.

### R28. How do collective, organizational and personal identities form, and how do they shape what actors do?

- **Short name:** identity.
- **Kind and origin:** cross-cutting; from O21.
- **Members** (9 OQs from 6 pieces): Bacq 2023: OQ-bacq2023-07 (bc), -09; Petriglieri 2023: OQ-petriglieri2023-02; Arnold 2023: OQ-arnold2023-12; Wright 2023: OQ-wright2023-05, -06; Godart 2024: OQ-godart2024-04, -06; Werner 2026: OQ-werner2026-06.
- **Representative quotation:** OQ-bacq2023-09: “we point to fruitful pathways for future research to consider the ways in which collective identity might shape role or founder identities” (p. 19, "Transcending the self/other dichotomy in entrepreneurial motives")
- **Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 0; most recent ask 2026-04-01 (werner2026), 7 months before the run.
- **Level:** Individual and organization.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 9. At 2 or above: none.

The askers ask how identities form and what they make actors do. Bacq et al. (2023) ask how collective identity shapes founder and role identities. Godart and Wittman (2024) ask about the identity work in adhering to a logic, at the level of the organization. Wright et al. (2023) ask how pliable a researcher's self-concept is; Werner et al. (2026) ask when a firm's moral reasoning shifts toward a different character. Arnold and Costas (2023) dissent: the struggle they describe is over a person's standing as a subject, prior to identity. The conversation is loose. O found it and F did not, each asker contributes one or two questions, and none cites another.

**Entry.** None. Every member scores 0.

### R29. What are the failures and dark sides of practices the field usually treats as good?

- **Short name:** dark sides.
- **Kind and origin:** cross-cutting; from O14.
- **Members** (6 OQs from 6 pieces): Leitzinger 2023: OQ-leitzinger2023-20; Jørgensen 2023: OQ-jorgensen2023-04; Gümüsay 2024: OQ-gumusay2024-09; Seidemann 2024: OQ-seidemann2024-11; Krautzberger 2024: OQ-krautzberger2024-12; Winkler 2025: OQ-winkler2025-06.
- **Representative quotation:** OQ-krautzberger2024-12: “Fourth, and more broadly, paradox studies could explore the undesired outcomes and failures of organizations in pursuing a meta-both/and approach.” (p. 20, "Directions for future research")
- **Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 0; most recent ask 2025-11-11 (winkler2025), 12 months before the run.
- **Level:** Organization and multi-level.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 6. At 2 or above: none.

These askers say the field studies the bright side of its favoured constructs, and each asks about the other side of one. Jørgensen and Beyes (2023) call the dark side of atmospheres a lacuna; Krautzberger and Tuckermann (2024) ask how a meta-both/and approach fails; Seidemann (2024) asks what harm embracing tensions does; Winkler and Schoeneborn (2025) extend their model to terrorism, hacktivism and misconduct; Gümüsay and Reinecke (2024) see value in theorizing undesirable futures; Leitzinger and Waeger (2023) ask whether mission drift can be productive. The askers share a diagnosis and no programme. Each contributes one question, and no citation links them.

**Entry.** None. Every member scores 0.

### R30. When should organizations hold a contradiction open, choose a side, or refuse both, and how would anyone know the response was good?

- **Short name:** paradox.
- **Kind and origin:** topical; from O38 + C18.
- **Members** (34 OQs from 6 pieces): Georgiou 2023: OQ-georgiou2023-08; Seidemann 2024: OQ-seidemann2024-01, -02, -03, -04, -05, -07, -08, -09, -10, -11, -12, -13, -14, -15, -16; Krautzberger 2024: OQ-krautzberger2024-03, -04, -05, -06, -07, -08, -09, -10, -11, -12, -13; Garud 2025: OQ-garud2025-07, -08; Keller 2025: OQ-keller2025-01, -02 (bc); Skade 2025: OQ-skade2025-01, -02, -06 (bc).
- **Representative quotation:** OQ-seidemann2024-11: “I recommend that paradox scholars empirically explore the boundary conditions of both/and for different classes of phenomena at different levels of analysis and the potential negative ramifications of embracing tensions.” (p. 18, "Developing a more granular perspective")
- **Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 2; most recent ask 2025-09-27 (skade2025), 13 months before the run.
- **Level:** Organization.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 1; 0 × 33. At 2 or above: none.

Paradox theory's both/and response is the shared target. Seidemann (2024) asks where both/and works, where it does not and what harm it does, and how responses should be judged on normative grounds. Krautzberger and Tuckermann (2024) ask how organizations run a portfolio of both/and and either/or approaches, how reflective episodes work, and how a meta-approach fails. Skade (2025) asks how actors handle tensions between co-existing futures. Garud et al. (2025) want concepts fitted to exploring while exploiting, and Georgiou and Arenas (2023) ask which mechanisms let communities and organizations work together despite conflicting logics. Keller et al. (2025) turn the theory on scholars' own work. Two positions in the corpus have no open question behind them: Giovannoni and Quattrone (2025) argue that the poles of a tension cannot be known, and Bartunek et al. (2025) argue for a "neither/nor" stance and state no question.

**Entry.** None. One member scores 1 (OQ-garud2025-08, on organizing for innovation with generative AI in daily work).

### R31. What is an institutional logic: what is it made of, where are its boundaries, and how do actors hold or combine several?

- **Short name:** institutional logics.
- **Kind and origin:** topical; from O28 + O39 + C23.
- **Members** (30 OQs from 6 pieces): Georgiou 2023: OQ-georgiou2023-02, -03, -04, -05, -06, -07, -08, -09, -11, -12; Jackwerth-Rice 2023: OQ-jackwerthrice2023-04; Stevenson 2024: OQ-stevenson2024-01, -02, -03, -04, -05; Godart 2024: OQ-godart2024-02, -05, -06; Schildt 2025: OQ-schildt2025-02, -03, -04, -05, -06, -07 (bc); Mutch 2025: OQ-mutch2025-01, -02, -03, -04, -05.
- **Representative quotation:** OQ-georgiou2023-04: “How do communities respond to institutional complexity (e.g., M. D. P. Lee & Lounsbury, 2015)? Do they become hybrids? If so, how do they manage to maintain their hybrid nature in the long term?” (p. 15, "Future Research")
- **Support:** theory/review articles 6; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 0; most recent ask 2025-04-25 (mutch2025), 18 months before the run.
- **Level:** Field, with organization-level questions.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 30. At 2 or above: none.

Five articles reopen the institutional logics perspective from inside, and a sixth touches it. Schildt and Kodeih (2025) ask what counts as a logic and invite study of variation within a single logic. Georgiou and Arenas (2023) find variants of the community logic and ask how communities respond to institutional complexity and keep their boundary. Stevenson et al. (2024) ask how stable a logic's centrality is across time, space and actors. Godart and Wittman (2024) ask about organizations that adhere strictly to one logic. Mutch (2025) argues that law is a missing logic and asks how practices move between the legal and the organizational domain. The askers disagree on the unit: a bundle of connected practices (Schildt and Kodeih), the meaning a logic has for actors (Stevenson et al.), or a substance carried in practices (Mutch). No citation links any two of them.

**Entry.** None. Every member scores 0.

### R32. What makes an organization hold to its values or purpose under pressure, and how do its commitments change?

- **Short name:** values under pressure.
- **Kind and origin:** topical; from O23 + C21.
- **Members** (18 OQs from 6 pieces): Leitzinger 2023: OQ-leitzinger2023-19, -20, -27; Stevenson 2024: OQ-stevenson2024-05; Godart 2024: OQ-godart2024-02, -05; Patriotta 2025: OQ-patriotta2025-12 (bc); Werner 2026: OQ-werner2026-03, -04, -05, -06, -07, -08, -09, -10; Kalkman 2026: OQ-kalkman2026-01, -03, -04.
- **Representative quotation:** OQ-werner2026-06: “Using the process model as a starting point, further theoretical and empirical research may study these processes in more detail; identifying with more precision and detail when and how a for-profit organization may shift in its moral reasoning and be potentially on the way towards forming a different character and purpose.” (p. 21, "Theoretical and research implications")
- **Support:** theory/review articles 5.5; commentary or exchange pieces 0; counted at ½ because they enter through boundary conditions only: Patriotta 2025; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 1; most recent ask 2026-07-21 (kalkman2026), 4 months before the run.
- **Level:** Organization.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 18. At 2 or above: none.

Werner et al. (2026) explain steadfastness under political pressure by organizational character. They leave open whether organizations differ clearly in moral scope, whether a calling exists beyond instrumental and normative commitment, and how a for-profit organization shifts in its moral reasoning. Godart and Wittman (2024) ask how purity in intention relates to purity in action. Kalkman (2026) asks under what conditions a crisis prompts moral self-reflection. Leitzinger and Waeger (2023) ask what keeps a movement from mission drift, and Stevenson et al. (2024) ask whether centrality can be carried into the study of value pluralism. How to tell commitment from rigidity is open across the set. Patriotta et al. (2025) mark the limit from the other side: settlement fails where the contenders' values are irreconcilable.

**Entry.** None. Every member scores 0. PAPER's opening concerns the displacement of institutional values by generative AI; these askers ask how organizations hold to values under political and market pressure, which is a different question.

### R33. How do marginalized and excluded people gain a speaking position, a voice or cultural autonomy?

- **Short name:** voice at the margins.
- **Kind and origin:** topical; from O17 + part of C01.
- **Members** (18 OQs from 6 pieces): Bacq 2023: OQ-bacq2023-10; Leitzinger 2023: OQ-leitzinger2023-31; Arnold 2023: OQ-arnold2023-01, -02, -04, -06, -07, -08, -10, -12, -13; Sasaki 2024: OQ-sasaki2024-01, -02, -03, -04, -05; Lantela 2024: OQ-lantela2024-06 (bc); Langenmayr 2024: OQ-langenmayr2024-02.
- **Representative quotation:** OQ-arnold2023-06: “we call for future research to look at the struggles of subjects to acquire a speaking position to begin with.” (p. 16, "Implications for future research")
- **Support:** theory/review articles 5.5; commentary or exchange pieces 0; counted at ½ because they enter through boundary conditions only: Lantela 2024; editorial signal n; distinct volumes 2 (4, 5); citation edges among askers 0; most recent ask 2024-09-18 (langenmayr2024), 26 months before the run.
- **Level:** Interaction and field.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 18. At 2 or above: none.

These askers ask how people who are excluded come to be heard. Arnold and Costas (2023) ask about the struggle to gain a speaking position at all, the practices that cast people as noise or unsettle that casting, and equality enacted in practice. Sasaki and Baba (2024) ask how cultural margins are made and enforced, by what means marginalized groups resist, and what resistance does inside the group. Langenmayr et al. (2024) ask how newly included strategy actors could contribute on their own terms. Bacq et al. (2023) and Leitzinger and Waeger (2023) call for research at the margins and outside Western settings. Arnold and Costas place the struggle in subjectivity and not in identity, which runs against identity-based work on equality. No asker says what organizational form keeps a newly gained voice from being silenced again. Every ask falls in volume 4 or 5.

**Entry.** None. Every member scores 0.

### R34. How do law, regulation and the state shape organizations, and can they restrain new technologies?

- **Short name:** law and the state.
- **Kind and origin:** topical; from O25.
- **Members** (10 OQs from 5 pieces): Scherer 2023: OQ-scherer2023-07, -10 (bc); du Gay 2024: OQ-dugay2024-06, -07; Jaser 2024: OQ-jaser2024-06; Mutch 2025: OQ-mutch2025-02, -03, -06; Mena 2026: OQ-mena2026-09, -10.
- **Representative quotation:** OQ-mutch2025-06: “This article has sought to argue that organizational scholars need to take the law seriously as a key influence on organizational life.” (p. 13, "Conclusion")
- **Support:** theory/review articles 5; commentary or exchange pieces 0; editorial signal n; distinct volumes 4 (4, 5, 6, 7); citation edges among askers 0; most recent ask 2026-03-31 (mena2026), 7 months before the run.
- **Level:** Field and society.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 1; 0 × 9. At 2 or above: none.

The askers ask how law and the state act on organizations. Mutch (2025) asks organization scholars to take law seriously and to study the transfer of practices between legal and organizational domains. Du Gay and Lopdrup Hjorth (2024) ask whether anti-formal reforms have undermined state capacity. Mena et al. (2026) ask how external law enables workers' non-domination and how citizens' rights compare with members' rights. Scherer and Neesham (2023) call for strict regulation of applications of large language models, and Jaser and Tourish (2024) call for democratic oversight of surveillance by legislative fiat where necessary. The askers disagree on whether law is a constitutive logic (Mutch) or an external restraint (Scherer and Neesham; Jaser and Tourish). O found this conversation and F did not.

**Entry.** None. One member scores 1 (OQ-scherer2023-07).

### R35. Who gets to take part in organizational decisions, on whose terms, and does participation deliver what it promises?

- **Short name:** participation.
- **Kind and origin:** topical; from O33 + C14.
- **Members** (25 OQs from 5 pieces): Friesl 2023: OQ-friesl2023-03, -04, -05, -06, -07, -08, -09; Langenmayr 2024: OQ-langenmayr2024-01, -02, -04, -05, -07, -11; Mena 2026: OQ-mena2026-01, -03, -05, -06, -07, -13; Friedrich 2026: OQ-friedrich2026-12, -14, -15, -16; Corver 2026: OQ-corver2026-05, -11.
- **Representative quotation:** OQ-friesl2023-03: “Unveiling the social processes underpinning self-selection allows future research to study why certain actors participate in open strategy or why they abstain from doing so.” (p. 13, "Discussion and Theoretical Implications")
- **Support:** theory/review articles 5; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 7); citation edges among askers 1; most recent ask 2026-07-28 (corver2026), 3 months before the run.
- **Level:** Organization.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 2; 0 × 23. At 2 or above: none.

Opening a decision to more people does not settle who comes, on whose terms, or to what effect. Friesl et al. (2023) ask why some actors select themselves into open strategy and others abstain, and they note that only realized participation can be observed. Langenmayr et al. (2024) ask how newly included actors must comply with incumbents' norms. Mena et al. (2026) ask who counts as the demos of a firm, whether deliberative tools yield inclusion or symbolic adoption, and under what conditions an organization can be democratic without consensus. Friedrich (2026) extends the demos beyond the human, and Corver and Filler (2026) ask how co-creative modeling relates to participatory governance. The askers disagree on what participation is for: better strategy, equity, non-domination or deliberation, or attunement to ecological dependence. None offers a way to compare outcomes across these purposes.

**Entry.** None. Two members score 1 (OQ-mena2026-03, OQ-mena2026-05).

### R36. When and why do people resist control and new technology, and how is resistance told from compliance?

- **Short name:** resistance.
- **Kind and origin:** cross-cutting; from O31 + part of X10.
- **Members** (7 OQs from 5 pieces): Sasaki 2024: OQ-sasaki2024-03, -04; Jaser 2024: OQ-jaser2024-09 (bc), -11 (bc); Stark 2024: OQ-stark2024-02; Seidemann 2024: OQ-seidemann2024-06; Hinds 2024: OQ-hinds2024-14.
- **Representative quotation:** OQ-stark2024-02: “The study of the dynamics of the relations between professional expertise and algorithmic practices is in its infancy. Under what conditions can we expect resistance by professionals to incursions by algorithmic practices? When are compromises likely?” (p. 9, "Object of management")
- **Support:** theory/review articles 4.5; commentary or exchange pieces 0; counted at ½ because they enter through boundary conditions only: Jaser 2024; editorial signal n; distinct volumes 1 (5); citation edges among askers 0; most recent ask 2024-10-29 (hinds2024), 24 months before the run.
- **Level:** Multi-level.
- **Fit (final scores of members):** 3 × 0; 2 × 1; 1 × 3; 0 × 3. At 2 or above: OQ-stark2024-02 (2).

The askers ask when and why people resist, and how resistance is recognized. Stark and Vanden Broeck (2024) ask under what conditions professionals resist incursions by algorithmic practices and when they compromise. Hinds and von Krogh (2024) ask whether resistance to generative AI stems from perceived power loss or from distrust. Sasaki and Baba (2024) ask by what means marginalized groups resist. Seidemann (2024) asks paradox research to study resistance for what it exposes and achieves. Jaser and Tourish (2024) bound their theory with liminal spaces for resistance and set aside whether covert behaviour counts as resistance or compliance. That last question, how to tell the two apart in practice, is the open one. I kept this conversation apart from R41: these askers want the conditions and causes of resistance, and none of the technology askers asks whether resistance is productive. All five sit in volume 5.

**Entry.** None. One member scores 2 (OQ-stark2024-02), and the hand-check finds that algorithmacy "predicts neither outcome". Jaser and Tourish's set-aside question (OQ-jaser2024-11) stays at 1: scorer A read "pacifying the algorithm" as a third reading of covert behaviour, and the hand-check held that the contact is "vocabulary and no more".

### R37. How should organizing change under ecological crisis and other grand challenges whose shape is not settled?

- **Short name:** ecological crisis.
- **Kind and origin:** topical; from C25.
- **Members** (8 OQs from 4 pieces): Gümüsay 2024: OQ-gumusay2024-02, -05; Giovannoni 2025: OQ-giovannoni2025-05; Friedrich 2026: OQ-friedrich2026-03, -04, -13; Corver 2026: OQ-corver2026-06, -10.
- **Representative quotation:** OQ-gumusay2024-02: “For instance, how would different climate pathways impact organizing differently, including the behaviour of people and institutions?” (p. 9, "Four modes of theorizing the future")
- **Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (5, 6, 7); citation edges among askers 3; most recent ask 2026-07-28 (corver2026), 3 months before the run.
- **Level:** Organization, set within socio-ecological systems.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 8. At 2 or above: none.

Four theory articles ask what organizing looks like under ecological pressure. Gümüsay and Reinecke (2024) ask how different climate pathways would change organizing. Friedrich (2026) asks how organizations can keep mapping their material dependencies beyond sustainability reports. Corver and Filler (2026) ask whether sustainability problems move from discrete to interconnected, and which modeling actions support solving them. Giovannoni and Quattrone (2025) offer their rhetorical approach for other grand challenges. The askers disagree on whether the problem can be specified: worked out together with its solution (Corver and Filler), unknowable in its ends (Giovannoni and Quattrone), or imaginable and assessable (Gümüsay and Reinecke). All three later articles cite Gümüsay and Reinecke.

**Entry.** None. Every member scores 0.

### R38. How do organizations anticipate, respond to and learn from crises, and what should crisis response aim at?

- **Short name:** crisis.
- **Kind and origin:** topical; from O34.
- **Members** (9 OQs from 4 pieces): Hinds 2024: OQ-hinds2024-06; Giovannoni 2025: OQ-giovannoni2025-05; Patriotta 2025: OQ-patriotta2025-05, -06, -07; Kalkman 2026: OQ-kalkman2026-03, -05, -07, -08.
- **Representative quotation:** OQ-patriotta2025-06: “Scholars could explore how organizations attempt to anticipate and preempt legitimacy challenges by crafting proactive justifications before a test crystallizes, and furthermore examine how prior crises constrain or enable subsequent responses.” (p. 18, "Future research directions: Legitimacy in a changing world")
- **Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (5, 6, 7); citation edges among askers 0; most recent ask 2026-07-21 (kalkman2026), 4 months before the run.
- **Level:** Organization.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 1; 0 × 8. At 2 or above: none.

The askers ask what crisis management is for and how organizations learn from crises. Kalkman (2026) asks under what conditions a crisis prompts moral self-reflection, how relationships are kept up in an affected organization, and how organizations move from a functionalist to a care-based approach. Patriotta et al. (2025) ask which early signals predict escalation, whether justifications can be prepared before a test crystallizes, and how earlier crises constrain later answers. Hinds and von Krogh (2024) ask how coordination built by generative AI fares when a crisis demands change. The askers differ on purpose: Kalkman asks for care against the functionalist restoration of order, while Patriotta et al. study how organizations justify themselves to restore legitimacy. O found this conversation; F had filed its members under audiences and under care.

**Entry.** None. One member scores 1 (OQ-hinds2024-06).

### R39. How do stories, myths and narratives gain force in and around organizations?

- **Short name:** myth and narrative.
- **Kind and origin:** topical; from O47 + C26.
- **Members** (8 OQs from 4 pieces): Bacq 2023: OQ-bacq2023-07 (bc), -08; Paca 2024: OQ-paca2024-02, -03, -04, -05; Brennecke 2025: OQ-brennecke2025-12; Hawbaker 2025: OQ-hawbaker2025-01.
- **Representative quotation:** OQ-hawbaker2025-01: “We welcome further theorizing about the impact of key institutional interactants, and the contexts and social dimensions that allow some people to leverage interactions to co-create mythologies.” (p. 9, "Discussion")
- **Support:** theory/review articles 3; commentary or exchange pieces 1; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 0; most recent ask 2025-12-01 (hawbaker2025), 11 months before the run.
- **Level:** Organization and interaction.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 8. At 2 or above: none.

Paca and Rozuel (2024) ask why some organizational stories acquire sacred qualities and others do not. Hawbaker and Hallett (2025) invite theory on how some people use interaction to co-create an institutional mythology. Brennecke et al. (2025) ask when the narrative of a tie hardens into a dominant account. Bacq et al. (2023) ask how individuals escape a narrative that reinforces itself. The four draw on four theories of narrative (Jungian archetypes, interactionism, network cognition, identity) and none cites another. Selection is open in all four: why one story takes hold and another does not.

**Entry.** None. Every member scores 0.

### R40. How do audiences come to judge an organization as legitimate or scandalous, and how do organizations answer?

- **Short name:** audiences and legitimacy.
- **Kind and origin:** topical; from O37 + C22.
- **Members** (21 OQs from 4 pieces): Pozner 2023: OQ-pozner2023-04, -06, -07, -09, -10, -11, -12, -13 (bc), -14, -15, -16; Godart 2024: OQ-godart2024-03; Brennecke 2025: OQ-brennecke2025-05; Patriotta 2025: OQ-patriotta2025-02, -03, -04, -05, -08, -09, -11, -12 (bc).
- **Representative quotation:** OQ-pozner2023-06: “we know little about the dynamics through which social groups make sense of the information—good or bad—that informs their evaluations.” (p. 13, "Discussion")
- **Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 3 (4, 5, 6); citation edges among askers 1; most recent ask 2025-11 (patriotta2025), 11 months before the run.
- **Level:** Field: organizations and their evaluating audiences.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 2; 0 × 19. At 2 or above: none.

Pozner and Hannigan (2023) set out to open "the black box of audiences": how do groups make sense of the information behind their evaluations, and how do unconnected publics come into conversation during a scandal? Patriotta et al. (2025) cite them and move to the organization's side: which early signals predict escalation, how media and platforms shape a legitimacy test, and how different societies shape its course. Godart and Wittman (2024) ask which audiences, and how many, an organization must satisfy to survive, and Brennecke et al. (2025) ask how third parties read a relationship by the way it formed. How audiences divide and combine remains unanswered. Patriotta et al. mark a limit: where the contenders' values are irreconcilable, settlement fails.

**Entry.** None. Two members score 1. Evaluation here is an audience's judgment of an organization. The brief's evaluation is a system's verdict on two people's work, and the two share a word.

### R41. When is disagreement or dissent productive, for organizations and for scholarly communities, and when does it destroy?

- **Short name:** dissent.
- **Kind and origin:** cross-cutting; from O29 + part of X10.
- **Members** (7 OQs from 5 pieces): Seidemann 2024: OQ-seidemann2024-06; Abend 2024: OQ-abend2024-08 (bc); Prasad 2024: OQ-prasad2024-04 (bc); Mena 2026: OQ-mena2026-07, -08, -22; Corver 2026: OQ-corver2026-16.
- **Representative quotation:** OQ-mena2026-08: “How can we ensure that dissent remains continuously productive and does not become destructive, for example, by deepening fractures among organizational members or even leading to organizational death?” (p. 12, "Agonistic internal focus")
- **Support:** theory/review articles 3; commentary or exchange pieces 1; counted at ½ because they enter through boundary conditions only: Abend 2024, Prasad 2024; editorial signal n; distinct volumes 2 (5, 7); citation edges among askers 2; most recent ask 2026-07-28 (corver2026), 3 months before the run.
- **Level:** Organization and interaction.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 7. At 2 or above: none.

These askers ask when disagreement helps. Mena et al. (2026) ask how dissent can stay productive and not split members or kill the organization, when an organization can be democratic without consensus, and for which decisions dissensus matters little. Corver and Filler (2026) ask how disagreement within and across groups feeds productive modeling. Seidemann (2024) asks about the productive potential of resistance to change. In the Abend exchange, Prasad (2024) and Abend (2024) each bound their proposal by the disagreement it will not end. A criterion for telling productive from destructive dissent before the outcome is known is what no asker supplies.

**Entry.** None. Every member scores 0.

### R42. How can organizations give and sustain care when care is undervalued?

- **Short name:** care.
- **Kind and origin:** topical; from O40 + C28.
- **Members** (13 OQs from 4 pieces): Bacq 2023: OQ-bacq2023-02; Fotaki 2023: OQ-fotaki2023-03, -06, -07; Friedrich 2026: OQ-friedrich2026-05, -09, -10, -13; Kalkman 2026: OQ-kalkman2026-02, -04, -05, -06, -07.
- **Representative quotation:** OQ-kalkman2026-02: “empirical research also could examine how organization members negotiate the implementation of care-based values in crises or how they use it to resolve moral dilemmas during the response effort.” (p. 15, "Implications for Empirical Research")
- **Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 7); citation edges among askers 1; most recent ask 2026-07-21 (kalkman2026), 4 months before the run.
- **Level:** Organization and society.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 13. At 2 or above: none.

Fotaki (2023) asks how asymmetries of gender, race and class shape who gives and who receives care, and how care can be taught as a capability. Kalkman (2026), who cites Fotaki, asks how members negotiate care-based values while a crisis is under way, what a care-based purpose produces, and whether critics of the ethics of care are right about it. Friedrich (2026) asks how care for more-than-human others gets resources inside ordinary operations. How care survives contact with operations is open in all three. The scope of care is not agreed: the most deprived people (Fotaki), those a crisis makes vulnerable (Kalkman), or other species (Friedrich).

**Entry.** None. Every member scores 0.

### R43. Which formal structures do organizations need for their purposes, and what can stand in for hierarchy?

- **Short name:** formal structure.
- **Kind and origin:** topical; from O27.
- **Members** (6 OQs from 4 pieces): du Gay 2024: OQ-dugay2024-02, -04, -05; Gümüsay 2024: OQ-gumusay2024-03; Stark 2024: OQ-stark2024-08; Mena 2026: OQ-mena2026-05.
- **Representative quotation:** OQ-dugay2024-02: “the crucial question remains which kinds of formalization are necessary for each of them to pursue their respective, and very different, purposes in the most requisite manner.” (p. 10, "Formality and Authority")
- **Support:** theory/review articles 4; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (5, 7); citation edges among askers 0; most recent ask 2026-03-31 (mena2026), 7 months before the run.
- **Level:** Organization.
- **Fit (final scores of members):** 3 × 0; 2 × 1; 1 × 1; 0 × 4. At 2 or above: OQ-stark2024-08 (2).

These askers ask what formal structure organizations need and what could stand in for hierarchy. Du Gay and Lopdrup Hjorth (2024) ask which kinds of formalization different purposes require and want organizational design restored to the centre of the field. Mena et al. (2026) ask whether novel governance structures prevent managerial authority or move domination elsewhere. Gümüsay and Reinecke (2024) ask how decisions unfold without formal hierarchy in prefigurative settings. Stark and Vanden Broeck (2024) ask whether technology should be treated as organizational structure. The disagreement is sharp: du Gay and Lopdrup Hjorth defend formality, while Mena et al. and Gümüsay and Reinecke look for structures that avoid hierarchical authority. No asker asks what formal offices become when the structure is the platform. Du Gay and Lopdrup Hjorth are the corpus's contrast case for the brief: formalization is the classical answer to rules a person cannot see.

**Entry.** None. One member scores 2 (OQ-stark2024-08), counted under R09.

### R44. What happens to the division of labour and workplace power when algorithms and generative AI take over tasks?

- **Short name:** division of labour.
- **Kind and origin:** topical; from C19 + part of O26.
- **Members** (9 OQs from 4 pieces): Justesen 2024: OQ-justesen2024-12; Stark 2024: OQ-stark2024-02, -03; Hsu 2024: OQ-hsu2024-08; Hinds 2024: OQ-hinds2024-13, -14, -15, -16, -17.
- **Representative quotation:** OQ-hinds2024-16: “as progressive encapsulation evolves across levels and functions in organizations, how does the process shape the division of labor?” (p. 10, "Discussion")
- **Support:** theory/review articles 3; commentary or exchange pieces 1; editorial signal n; distinct volumes 1 (5); citation edges among askers 0; most recent ask 2024-10-29 (hinds2024), 24 months before the run.
- **Level:** Organization, with field-level questions about professions.
- **Fit (final scores of members):** 3 × 0; 2 × 4; 1 × 5; 0 × 0. At 2 or above: OQ-stark2024-02 (2), OQ-hsu2024-08 (2), OQ-hinds2024-16 (2), OQ-hinds2024-17 (2).

The askers expect algorithms and generative AI to rearrange who does what and who holds power, and they ask in which direction. Hinds and von Krogh (2024) ask how progressive encapsulation shapes the division of labour, whether humans keep the specialized tasks or the general ones, how power holders respond when the system takes over coordination, and whether encapsulation includes or excludes marginalized groups. Stark and Vanden Broeck (2024) ask when professionals resist algorithmic incursions and call for comparative studies across countries and professions. Hsu and Bechky (2024) name the retention of expertise as the worrying case, and Justesen and Plesner (2024) ask what digitalization does to employment relations and professions. The evidence base is the limit: Hsu and Bechky rest on early, unreviewed experiments and Hinds and von Krogh on a thought experiment. Stark and Vanden Broeck reject the labour-studies frame that Justesen and Plesner's question retains. All four askers sit in volume 5.

**Entry.** Adjacent on every member and answered on none: four members score 2, five score 1, none scores 0. The brief's account of why task deskilling and rising relational demand go together gives one shape the division of labour could take. The askers ask at the level of organizations and professions which tasks go where and who loses power, and the hand-check on OQ-hinds2024-17 concludes that algorithmacy "changes the axis rather than picking a side" (scorer A's words). An entry here needs a change of level.

### R45. Whose voices, bodies and standpoints count as sources of theory, and who is left out of the record?

- **Short name:** whose voices count.
- **Kind and origin:** topical; from O32 + part of C08.
- **Members** (7 OQs from 4 pieces): Fotaki 2023: OQ-fotaki2023-05; Gümüsay 2024: OQ-gumusay2024-13; Lantela 2024: OQ-lantela2024-04, -05, -09, -11; Höllerer 2026: OQ-hollerer2026-05.
- **Representative quotation:** OQ-lantela2024-09: “who has been the legitimate theoretical voice within a specific sub-field, and why? What kind of bodies have been able to theorize?” (p. 12, "Conclusion")
- **Support:** theory/review articles 3; commentary or exchange pieces 0; editorial signal y; distinct volumes 3 (4, 5, 7); citation edges among askers 1; most recent ask 2026-07-26 (hollerer2026), 3 months before the run.
- **Level:** Field: the scholarly community.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 7. At 2 or above: none.

The askers ask whose voices count in theory itself. Lantela (2024) asks whose voice is missing from the records, who has been the legitimate theoretical voice in a sub-field, and what bodies have been able to theorize. Fotaki (2023) wants research to start from people's lived material and affective experience. Gümüsay and Reinecke (2024) propose larger, more diverse teams. The 2026 editorial asks that each debate set bring diverse authors and perspectives (OQ-hollerer2026-05). Lantela names the difficulty that remains: to find what marginal experiences share without abstracting them into one more dominating category. I kept this apart from R24; the editorial speaks to who is admitted, not to how those inside reflect.

**Entry.** None. Every member scores 0.

### R46. What do practices do inside organizations once adopted: change conduct or stay symbolic?

- **Short name:** adopted practices.
- **Kind and origin:** topical; from O43.
- **Members** (6 OQs from 3 pieces): Powell 2023: OQ-powell2023-02, -03, -04; Mena 2026: OQ-mena2026-13; Corver 2026: OQ-corver2026-08, -10.
- **Representative quotation:** OQ-powell2023-04: “The challenge for diffusion studies is to understand better the mechanisms of adoption and how newly adopted practices mesh with existing organizational practices, structures, and values. Longitudinal analyses that examine both the predictors and consequences of adoption, as in the studies of diversity training, are essential.” (p. 14, "Heterogeneous diffusion")
- **Support:** theory/review articles 3; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 7); citation edges among askers 0; most recent ask 2026-07-28 (corver2026), 3 months before the run.
- **Level:** Organization.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 6. At 2 or above: none.

The askers ask what adopted practices do. Powell and DiMaggio (2023) ask what is diffused, through which channels, how adopted practices mesh with existing structures, and with what effects, and they call for longitudinal studies of predictors and consequences. Mena et al. (2026) ask whether deliberative tools lead mostly to symbolic adoption. Corver and Filler (2026) ask which decisions modeling has improved and which modeling actions support success. The askers share the worry that adoption is measured more often than effect. O found this conversation and F did not.

**Entry.** None. Every member scores 0.

### R47. Can a person be an institution, and under what conditions?

- **Short name:** person as institution.
- **Kind and origin:** topical; from O44 + C29.
- **Members** (30 OQs from 3 pieces): Hawbaker 2025: OQ-hawbaker2025-01, -02 (bc), -03, -04; Nigam 2025: OQ-nigam2025-01, -02 (bc), -03, -04, -05, -06, -07, -08, -09, -10, -11; Derek Robinson 2025: OQ-derekrobinson2025-01, -02, -03 (bc), -04, -05, -06, -07, -08, -09, -10, -11, -12, -13, -14, -15.
- **Representative quotation:** OQ-nigam2025-11: “We hope that others will take on these ideas and push forward why, how, when and for how long individuals can become institutions.” (p. 9, "Conclusion")
- **Support:** theory/review articles 0; commentary or exchange pieces 3; editorial signal n; distinct volumes 1 (6); citation edges among askers 2; most recent ask 2025-12-23 (derekrobinson2025), 10 months before the run.
- **Level:** Multi-level: person to institution.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 30. At 2 or above: none.

This is the 6(4) exchange. Nigam, Amis and Logue (2025) propose that a person can become an institution, and they ask when, where and for how long, and what happens when the person dies. Derek Robinson and Atanasova (2025) accept the possibility and insert a stage: persons are first person-brands, and the open questions are what moves them from stage to stage and whether the process reverses. Hawbaker and Hallett (2025) reject the premise, since institutions are supra-individual, and ask how individuals and mythologies relate. The disagreement is definitional and unresolved: three pieces take one case and arrive at three objects (institution, brand, mythology). The conversation sits in one issue, and the 2026 editorial cites all three pieces.

**Entry.** None. Every member scores 0.

### R48. What does digitalized work demand of, and do to, the individual worker: hidden labour, consent, meaning?

- **Short name:** the worker's side.
- **Kind and origin:** cross-cutting; from O30 + part of X04.
- **Members** (12 OQs from 3 pieces): Justesen 2024: OQ-justesen2024-01, -04, -09, -11, -13, -15, -16, -17 (bc); Jaser 2024: OQ-jaser2024-02, -04; Hinds 2024: OQ-hinds2024-21, -22.
- **Representative quotation:** OQ-hinds2024-21: “what are individuals' psychological responses to the new relational fabric in which they are embedded?” (p. 11, "Discussion")
- **Support:** theory/review articles 3; commentary or exchange pieces 0; editorial signal n; distinct volumes 1 (5); citation edges among askers 0; most recent ask 2024-10-29 (hinds2024), 24 months before the run.
- **Level:** Individual.
- **Fit (final scores of members):** 3 × 0; 2 × 4; 1 × 5; 0 × 3. At 2 or above: OQ-justesen2024-01 (2), OQ-justesen2024-13 (2), OQ-justesen2024-16 (2), OQ-hinds2024-21 (2).

This conversation asks what digitally organized work demands of the person who does it. Justesen and Plesner (2024) ask for the lived experience of people doing invisible digi-work, for a fuller account of "the emotional costs, mental loads and unintended tasks associated with digitalization" (OQ-justesen2024-13), and for an understanding of the invisible as work that is distributed, practical and embodied. Hinds and von Krogh (2024) ask about individuals' psychological responses to "the new relational fabric in which they are embedded" (OQ-hinds2024-21), and when encapsulation strips work of meaning. Jaser and Tourish (2024) ask why workers consent to surveillance and what kind of workers people want to be. The askers disagree about agency. Jaser and Tourish set resistance aside to theorize consent; Justesen and Plesner describe effort that keeps the system running, including work "aimed through direct and indirect practices at pacifying the algorithm" (justesen2024 record, Hand-check, quoting Bucher et al., 2021, at p. 15), which they file as labour the organization depends on. All three askers sit in volume 5, and none cites another.

**Entry.** Yes for positioning; no member is answered. Four members score 2 and five score 1. This is the one technology conversation at the brief's own level, the individual, and its question is close to ASM's gap sentence: what a person inside the arrangement must be able to do. The three parts are a case of Justesen and Plesner's "unintended tasks" and mental loads. Two things hold the scores at 2. The askers ask for empirical accounts and psychological responses, and the brief is a theory article about a capacity. And Justesen and Plesner read "pacifying the algorithm" as work, where the brief reads it as a failure mode; a paper that enters here has to say which reading it takes.

### R49. How is interdependent work coordinated when its usual carriers (co-presence, informal contact, human teammates) are displaced?

- **Short name:** coordination.
- **Kind and origin:** topical; from Räcker's part of O35 + Hinds's part of O26 + C17.
- **Members** (23 OQs from 3 pieces): Räcker 2024: OQ-racker2024-01, -02, -03, -04, -05 (bc), -06 (bc), -07, -08, -09, -10, -11, -12 (bc); Phillips 2024: OQ-phillips2024-07; Hinds 2024: OQ-hinds2024-03, -04, -05, -06, -07, -08, -09, -19, -20, -25.
- **Representative quotation:** OQ-racker2024-10: “Thus, we need to better understand how different coordinating mechanisms (here: roles, space, routines) interact in achieving successful integration.” (p. 13, "Interrelations")
- **Support:** theory/review articles 2; commentary or exchange pieces 1; editorial signal n; distinct volumes 1 (5); citation edges among askers 0; most recent ask 2024-10-29 (hinds2024), 24 months before the run.
- **Level:** Interaction (team) and organization.
- **Fit (final scores of members):** 3 × 1; 2 × 6; 1 × 12; 0 × 4. At 2 or above: OQ-racker2024-10 (2), OQ-phillips2024-07 (2), OQ-hinds2024-03 (2), OQ-hinds2024-04 (3), OQ-hinds2024-07 (2), OQ-hinds2024-08 (2), OQ-hinds2024-25 (2).

This is the coordination cluster, reported whatever its size. Räcker, Geiger and Seidl (2024) write coordination theory proper. They treat space as something coordination produces, and they ask which spatial configurations occur and why, and how "different coordinating mechanisms (here: roles, space, routines) interact in achieving successful integration" (OQ-racker2024-10); they suggest that coordinating through space may be weaker in virtual collaboration (bc). Hinds and von Krogh (2024) use team coordination as a thought experiment for generative AI. If the system absorbs informal coordination, what happens to cohesion and psychological safety, does emergent interdependence break down "because team members blindly follow guidance from the AI" or become unnecessary, which parts of formal and informal coordination will be encapsulated, and can teams still evolve their practices in a crisis? Phillips et al. (2024) add one question, on how an AI teammate affects team dynamics. The two articles do not meet. Räcker et al. name no algorithm, platform or intermediary. Okhuysen and Bechky (2009), whose integrating conditions frame GDOC, are a named interlocutor in Räcker et al.'s record and in no other of the 66. No citation links the three askers, all three sit in volume 5, and no member of this conversation was published after October 2024.

**Entry.** By fit, yes; by support, weak. One member scores 3 (OQ-hinds2024-04), six score 2 and twelve score 1. Seven members at 2 or above is a count only R22 matches. Nearly all of it is one article. Hinds and von Krogh's ten members carry the 3 and four of the 2s; Räcker et al.'s twelve members carry one 2 (OQ-racker2024-10), where the hand-check notes that their article ties coordinating mechanisms to Okhuysen and Bechky's integrating conditions, "the same three the brief's parts restore", and that on the interplay the call asks about "algorithmacy says nothing". So the coordination problem is where the brief fits best, and coordination theory is not who is asking: the open questions come from a technology article that borrows the vocabulary.

### R50. What place should language models and computational methods have in scholars' own theorizing?

- **Short name:** language models in theorizing.
- **Kind and origin:** topical; from O45 + C27.
- **Members** (10 OQs from 3 pieces): Powell 2023: OQ-powell2023-11; Cornelissen 2024: OQ-cornelissen2024-04, -05 (bc), -06, -07, -08, -09, -10; Suddaby 2024: OQ-suddaby2024-05 (bc), -06.
- **Representative quotation:** OQ-cornelissen2024-06: “In this context, the million-dollar question is whether LLMs can now, or in the near future, be truly creative beyond such basic tasks, and in ways that might capture or mimic human levels of creativity in acts of theorizing. It is perhaps a bit premature here to give a conclusive answer” (p. 7, "Abstract reasoning and creativity")
- **Support:** theory/review articles 1; commentary or exchange pieces 1; editorial signal y; distinct volumes 2 (4, 5); citation edges among askers 2; most recent ask 2024-10-28 (suddaby2024), 24 months before the run.
- **Level:** Field, with rules for individual authors.
- **Fit (final scores of members):** 3 × 0; 2 × 1; 1 × 7; 0 × 2. At 2 or above: OQ-suddaby2024-06 (2).

The 2024 editorial asks the field to debate what language models mean for theorizing and sets a disclosure policy. It leaves open whether models can be creative in theorizing and whether augmented theorizing will become normal. Suddaby (2024) answers with a boundary: a science driven by past data works in stable domains and may fail where people know they are studied. Powell and DiMaggio (2023), writing before the editorial, expect computational text methods to detect hybrid and emergent institutional forms. No asker reports a test of model-assisted theorizing.

**Entry.** None. One member scores 2 (OQ-suddaby2024-06), a closing line that sets a person against an algorithm with no counterpart. The conversation is about scholars' own practice. Its disclosure policy applies to any manuscript prepared with a language model's help.

### R51. How do hype and attention around a new technology form, and with what institutional and power consequences?

- **Short name:** hype.
- **Kind and origin:** topical; from O46.
- **Members** (5 OQs from 2 pieces): Grodal 2024: OQ-grodal2024-02, -06, -07; Wedlin 2025: OQ-wedlin2025-03, -04.
- **Representative quotation:** OQ-wedlin2025-03: “We hope that our model of hype as a process of translation will spur a variety of empirical investigations, further exploring the institutional dynamics of hype and its potentially disruptive institutional consequences.” (p. 17, "Concluding Discussion")
- **Support:** theory/review articles 1; commentary or exchange pieces 1; editorial signal n; distinct volumes 2 (5, 6); citation edges among askers 0; most recent ask 2025-12-23 (wedlin2025), 10 months before the run.
- **Level:** Field.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 3; 0 × 2. At 2 or above: none.

Two askers ask how attention around a new technology forms and what it does. Wedlin and Weinryb (2025) ask for empirical work on the institutional dynamics of hype and for a wider set of translators and enablers. Grodal et al. (2024) ask whether perceived crossing of the human–machine boundary draws audience attention, and they call for study of power during technological emergence. Whether hype causes institutional change or signals a perceived boundary crossing is open between them. The conversation is thin: two askers, five questions, no citation between them.

**Entry.** None. Three members score 1 and none higher.

### R52. How does brokerage work, and what happens when tie histories accumulate or a technology takes over the brokering?

- **Short name:** brokerage.
- **Kind and origin:** topical; from O42.
- **Members** (4 OQs from 2 pieces): Hinds 2024: OQ-hinds2024-10, -13; Brennecke 2025: OQ-brennecke2025-02, -03.
- **Representative quotation:** OQ-hinds2024-10: “we need theory on how GenAI relates to resource holders” (p. 9, "Team coordination")
- **Support:** theory/review articles 2; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (5, 6); citation edges among askers 0; most recent ask 2025-09-28 (brennecke2025), 13 months before the run.
- **Level:** Interaction (network).
- **Fit (final scores of members):** 3 × 0; 2 × 1; 1 × 3; 0 × 0. At 2 or above: OQ-hinds2024-10 (2).

Two articles ask about a party that stands between two others and allocates. Brennecke et al. (2025) ask how the trajectory of a bridging tie affects brokerage behaviour, and how brokers interpret and narrate tie histories. Hinds and von Krogh (2024) place generative AI in the broker's seat: "we need theory on how GenAI relates to resource holders" (OQ-hinds2024-10), and they ask how power holders and resource brokers respond when the system takes over. Whether a technology can hold a brokerage position is open; Hinds and von Krogh imply it, and Brennecke et al.'s framework, built on the biography of a dyadic tie, does not address it. O found this conversation and F did not. I dropped Pozner and Hannigan's question on non-adjacent publics from O's list, since it names no broker. The conversation is thin: two askers, four questions, no citation between them.

**Entry.** Narrow. One member scores 2 (OQ-hinds2024-10) and three score 1. This is the only place in the corpus where askers pose an open question about a third party with allocating power between two others, and in Hinds and von Krogh's passage the third is a system. The brief describes the people on either side of such a third. The call asks for theory of the system's relation to resource holders and of power around brokerage, which the brief does not supply.

### R53. When are organizations rewarded for conforming and when for staying distinct, and before which audiences?

- **Short name:** conformity and distinctiveness.
- **Kind and origin:** topical; from O48.
- **Members** (6 OQs from 2 pieces): Powell 2023: OQ-powell2023-01, -06, -07, -08; Godart 2024: OQ-godart2024-03, -04.
- **Representative quotation:** OQ-powell2023-08: “But constructive engagement with these literatures may help institutional theorists to clarify the features of organizations (and the types of organizations) for which conformity or distinctiveness, respectively, are rewarded, and the scope conditions governing such generalizations.” (p. 15, "Heterogeneous diffusion")
- **Support:** theory/review articles 2; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 5); citation edges among askers 1; most recent ask 2024-09-03 (godart2024), 26 months before the run.
- **Level:** Organization and field.
- **Fit (final scores of members):** 3 × 0; 2 × 0; 1 × 0; 0 × 6. At 2 or above: none.

Two askers ask when organizations gain from conforming and when from standing apart. Powell and DiMaggio (2023) ask which aspects of organizations are most vulnerable to isomorphic pressure, when a practice becomes mandatory, and what rules let organizations differ while keeping legitimacy. Godart and Wittman (2024) ask which audiences, and how many, an organization must satisfy to survive. The scope condition Powell and DiMaggio name is the gap: for which organizations conformity is rewarded, and for which distinctiveness.

**Entry.** None. Every member scores 0.

### R54. Why do people consent to surveillance and data-driven control, and what would restore their autonomy?

- **Short name:** surveillance and consent.
- **Kind and origin:** topical; from C30.
- **Members** (17 OQs from 2 pieces): Scherer 2023: OQ-scherer2023-02, -04, -05, -06, -09, -11, -13; Jaser 2024: OQ-jaser2024-02, -03, -04, -05, -06, -07, -08, -09 (bc), -10 (bc), -11 (bc).
- **Representative quotation:** OQ-jaser2024-02: “However, 'voluntary' consent that flows from people’s relative comfort with surveillance, or seeming indifference to or unawareness of its existence, requires much more research (Sommers & Bohns, 2019).” (p. 11, "Hegemony and the Performance of Consent")
- **Support:** theory/review articles 2; commentary or exchange pieces 0; editorial signal n; distinct volumes 2 (4, 5); citation edges among askers 0; most recent ask 2024-03-19 (jaser2024), 32 months before the run.
- **Level:** Field and societal, with individual-level questions about consent.
- **Fit (final scores of members):** 3 × 0; 2 × 1; 1 × 6; 0 × 10. At 2 or above: OQ-scherer2023-13 (2).

Jaser and Tourish (2024) ask why workers, managers and unions consent to surveillance, whose interests it serves, and what response goes beyond individual resistance. Scherer and Neesham (2023) ask how people can recover the capacity for public reason that surveillance capitalism erodes, and they propose oaths, regulation of language-model applications and norms for digital civic spaces. Both articles take up Zuboff (2022), which the journal published before the corpus window. The two differ on the lever: Jaser and Tourish locate the cause in neoliberal ideology and expect change from collective and legislative action, while Scherer and Neesham argue that institutional reform depends on a prior culture of maturity. Consent that is not reluctant compliance "requires much more research" (OQ-jaser2024-02). The conversation was last asked in March 2024, the longest silence in the map.

**Entry.** None; the conversation holds two rival accounts of the same person. One member scores 2 (OQ-scherer2023-13) and six score 1. Jaser and Tourish explain what people under data-driven control do by consent. Scherer and Neesham place the needed capacity outside the systems. The brief describes a capacity exercised inside them. A paper on algorithmacy meets both as alternatives a reviewer may raise.

## Singletons

These 17 OQs are asked by one piece only and fit no conversation above. Most are limits of a single model or calls to test it. Each scores 0 or 1 on fit.

- OQ-georgiou2023-10 (Georgiou 2023; limitation; fit 0): “Although this list of communities may not be comprehensive, it encompasses the most frequently discussed types in the organization and management field.” (p. 6, "Research on Communities of Place, Practice, Users, and Firms")
- OQ-guercini2023-04 (Guercini 2023; limitation; fit 0): “although we yet lack empirical support for our predictions, we can at least state that CA negatively moderates the effects proposed by absorptive capacity theory.” (p. 16, "Theoretical implications")
- OQ-guercini2023-05 (Guercini 2023; future_research_call; fit 0): “Such studies may for example translate our propositions into testable hypotheses and matching research designs, testing and verifying the currency of our main arguments.” (p. 16, "Implications for further research")
- OQ-guercini2023-09 (Guercini 2023; limitation; fit 0): “learning is often assumed rather than directly studied, and is theorized, similar to what we have done here, in rather stylized terms (as associative learning, deliberate learning, etc.).” (p. 17, "Implications for further research")
- OQ-chia2023-03 (Chia 2023; invitation; fit 0): “What we urge, however, is for those strategy theorists,tied to a means–ends logic to admit the force of both practice and situation, and even to further admit a fourth.” (p. 17, "Discussion: What Next for Strategy?")
- OQ-jorgensen2023-06 (Jørgensen 2023; future_research_call; fit 0): “atmospheric thought (and its poetics) carries a critique of scholarship itself – it carries a distinct critical performativity, as it were – which has yet to more fully register and to be more fulsomely enacted.” (p. 12, "Conclusion")
- OQ-hsu2024-01 (Hsu 2024; limitation; fit 0): “While this is early-stage, non-peer-reviewed work, the findings point to a number of consistent patterns across these diverse contexts” (p. 6, "The Case of Creative Work: Professional gatekeepers and creative producers")
- OQ-langenmayr2024-10 (Langenmayr 2024; limitation; fit 0): “The list of theories is neither exhaustive nor exclusive as there may be other, equally relevant theories that could be used to study the themes raised by the equity-based research agenda.” (p. 5, "Theorizing Inclusion in Open Strategy Research")
- OQ-garud2025-06 (Garud 2025; future_research_call; fit 1): “How actors may explore new functionalities by exploiting existing architectures is a topic worth further investigation in the context of organizational ambidexterity.” (p. 15, "Future research on innovation at work in the age of digital technologies and Gen AI")
- OQ-garud2025-09 (Garud 2025; invitation; fit 0): “we propose that organizations can experiment with alternatives to the main dominant themes that structure organizations and work practices.” (p. 17, note 22)
- OQ-garud2025-10 (Garud 2025; future_research_call; fit 0): “Another avenue is knowledge creation and sharing in today’s digital age. Digital repositories serve as living “bodies of knowledge” that are used not only to archive but to continuously create, curate, and categorize information in real time” (p. 15, "Future research on innovation at work in the age of digital technologies and Gen AI")
- OQ-friedrich2026-18 (Friedrich 2026; limitation; fit 0): “A challenge of Braidotti’s critical affirmative theorizing is, however, her eclectic “zigzagging” between various theoretical traditions” (p. 19, "Posthuman feminism for organization theory")
- OQ-corver2026-12 (Corver 2026; future_research_call; fit 0): “Further conceptual and empirical work could explore whether additional types of modeling actions become visible once this vocabulary is applied to settings with different problem structures” (p. 18, "Discussion")
- OQ-corver2026-14 (Corver 2026; limitation; fit 1): “we have said comparatively little about how the people involved in that process actually interpret the consequences it produces in any given instance” (p. 18, "Discussion")
- OQ-corver2026-15 (Corver 2026; boundary_condition; fit 0): “our focus on the modeling process is not meant to suggest that implementation problems in corporate sustainability stem from modeling assumptions alone” (p. 18, "Discussion")
- OQ-pavlisa2026-02 (Pavlisa 2026; invitation; fit 0): “We hope that our contributions will stimulate future conceptual, empirical and practical research in the application of a capitals lens as well as operationalisation of the principle of reciprocal exchange in stakeholder governance.” (p. 20, "Conclusion")
- OQ-pavlisa2026-04 (Pavlisa 2026; boundary_condition; fit 0): “These considerations reveal the boundary conditions of this theory while simultaneously paving the way for further developments of a capitals lens in stakeholder governance.” (p. 19, "Discussion")

## Conversations that continue outside the corpus

The records show which pieces reply to work published elsewhere or in the journal before volume 4(1). The list merges O's and F's; each line names the conversations it feeds.

1. **Surveillance capitalism.** Scherer and Neesham (2023) and Jaser and Tourish (2024) take up Zuboff (2022, *Organization Theory* 3(3)). Feeds R54 and R13.
2. **Organizationality.** Dion et al. (2025) challenge Schoeneborn and colleagues (2019, 2022), published outside the journal; Schoeneborn et al. (2026) reply inside the corpus. Feeds R09 and R11.
3. **Technology, work and interaction.** Hinds and von Krogh (2024) extend the relational view of Bailey et al. (2022). Stark and Vanden Broeck (2024) depart from the view that algorithmic management amplifies scientific management, with Kellogg, Valentine and Christin (2020) among their named interlocutors. Phillips et al. (2024) build on Kennedy and Phillips (2023). Whyte et al. (2023) leave open a debate with Uhlin (2022). Feeds R22, R49 and R14.
4. **Community as logic or context.** Georgiou and Arenas (2023) answer Mutch (2021), published in the journal before the window; Mutch (2025) answers the absence of law in Thornton, Ocasio and Lounsbury (2012). Feeds R31 and R34.
5. **Words and distinctions.** The Abend exchange turns on Abend's book (2023); Suddaby (2024) replies to the book and to Abend (2008). Feeds R12.
6. **Paradox.** Keller et al. (2025) return to Poole and Van de Ven (1989); Bartunek et al. (2025) reply to Mikel-Hong et al. (2024) and state no open question. Feeds R30 and R36.
7. **The iron cage.** Powell and DiMaggio (2023) look back on their 1983 paper. Feeds R16, R46 and R53.
8. **Scandal and formality.** Pozner and Hannigan (2023) follow a prompt from Jourdan (2023); du Gay and Lopdrup Hjorth (2024) argue against King and colleagues' account of the organization as social actor. Feeds R40 and R43.

## Notes for the lead

- **Age of the fit.** The eight articles that hold every OQ at 2 or above appeared between October 2023 and October 2024. Nothing published since then reaches 2. The pick-up stage (S10) should check whether these questions have been taken up outside the journal in the two years since.
- **Conversations that rest on one or two articles.** R27 (Leitzinger and Waeger, 30 of 35 members), R01 (Brennecke et al., 19 of 41), R22 (Whyte et al., 12 of 22), R09 (Dion et al. and Schoeneborn et al., 21 of 34) and R49 (two articles, 22 of 23). Their recurrence is real and thinner than their size suggests.
- **Convened exchanges.** R14 with R21 carries the 5(3) set, R47 the 6(4) set and R12 the 5(4) set. Convening inflates their commentary counts and citation edges.
- **What a critic should test first.** The split in R22 between a medium and a party is my reading of the askers' premises, and no asker states it. The reading matters, because the best conversation-level entry rests on it.
- **Blindness.** O clustered without fit data and F fixed its conversations before seeing any. This reconciliation was made with the brief and the final fit scores open. The table and notes above record each decision at the level of a cluster. Single placements can be checked by setting `RECURRENCE.tsv` beside `RECURRENCE_O.tsv` and `RECURRENCE_F.tsv`.
- **The two anti-dyadic passages.** Patriotta et al. (2025, p. 16) and Dion et al. (2025) are not a conversation under the rule and neither involves a social third party. `SHORTLIST.md` gives the ruling and the text behind it.
