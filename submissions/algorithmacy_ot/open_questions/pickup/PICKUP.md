# Pick-up: who took up, answered or contested each shortlisted question

[Written by Fable (claude-fable-5-2), S10f, 2026-11-22]

Run `ot-oq-2026-11`. This file consolidates the pick-up evidence for the ten candidates in `synthesis/SHORTLIST.md`. It merges `PICKUP_P1.md` and `PICKUP_P2.md` with their appended corrections, `GAP_CHECK.md`, and the 19 cards in `pickup/cards/`. I checked every card against its source text on 22 November 2026, and each card now ends with a "Fable check" section. Where this file and a batch report differ, this file holds. Every quotation below comes from a card or from `GAP_CHECK.md` and carries its locator. I located each card quotation in its source myself. The gap check's quotations I did not re-read; they stand on that stage's reading, at the depth it reports.

## What the evidence is, and where it stops

- **Triage.** Two triage agents read the title and abstract of 272 citing rows (stark2024 127, justesen2024 52, hinds2024 39, hsu2024 28, phillips2024 17, racker2024 9; my count from `TRIAGE_T1.tsv` and `TRIAGE_T2.tsv`). They classed 114 rows `possible_takeup`, 4 `possible_answer`, 133 `passing`, 21 `unclear` and none `possible_contest`.
- **Cards.** Readers carded 19 works: all four `possible_answer` rows and fifteen of the other flagged works. For most candidates the cards are a sample of the flagged works. "No answer among the carded works" is a statement about that sample.
- **Read depth after my check.** Full text: 8 (alishani2025, avnoon2026, bujold2026, chao2026, decius2026, gulbrandsen2025, phillips2026, zelles2026). Partial: 7 (aleksic2026, choroszewicz2026, dowsett2026, hubert2025, johnsson2026, rikala2025, steiger2026). Abstract only: 3 (akhil2026, ivarsson2026, zientara2026). Unread: 1 (hall2025).
- **Gap check.** It covers candidates 1 to 3 only: 43 queries on the OpenAlex search API and Consensus, 22 November 2026. Scholar Gateway refused every call.
- **Unread texts that could change a line below.** Hall and Kuhn (2025), for candidate 1. S.G. and Lyytinen (2026) and Ivarsson and Islind (2026), for candidate 6. Zientara (2026), for candidate 8. From the gap check: Gloy (2025), known through a review; Curchod et al. (2020), Emigh (2024), Snyder (2025) and Riedl et al. (2026), each read as an abstract.

## How to read the entries

**Class.** The pick-up brief's four classes: `passing` (a mention), `takes_up` (the work works on the question), `answers` (it offers an answer), `contests` (it disputes the question or its premise).

**Citation edge.** The plan counts a citing work "only if its reference list holds the OT article". Several cards class a work against a candidate whose askers it does not cite, so each entry carries a second mark:

- *on the question*: the work cites an asker of the candidate, and the citing passage bears on the question's substance;
- *other point*: the work cites an asker of the candidate for something else;
- *no edge*: the work cites no asker of that candidate. Under the plan's rule it is not pick-up for that candidate, and I report it as convergent evidence.

## Result of the card check

| Verdict | Cards |
|---|---|
| used (14) | aleksic2026, alishani2025, avnoon2026, bujold2026, chao2026, decius2026, dowsett2026, gulbrandsen2025, johnsson2026, phillips2026, rikala2025, steiger2026, zelles2026, zientara2026 (abstract only) |
| used_with_corrections (4) | akhil2026, ivarsson2026, choroszewicz2026, hubert2025 |
| held (1) | hall2025 |

Every quotation on every card is in its source at the stated page, with one locator corrected (hubert2025, résumé). The corrections that change what the batch reports say:

1. **Candidate 6 has no confirmed answer.** akhil2026 and ivarsson2026 move from `answers` to `takes_up, possible answer (abstract only)`. Both cards rest on the same title and abstract from which triage had already judged them `possible_answer:6`; the readers could not open either paper, so the cards add no evidence and cannot carry a stronger class. This reverses the S10e correction appended to `PICKUP_P2.md`.
2. **bujold2026 on candidate 3.** `answers` holds for the choice as the shortlist assembles it, in the worker–organization relation. The article does not answer OQ-stark2024-07, which it never mentions, and toward that call's premise it leans to `contests`: the exchange partner is "the organization (not the algorithm)" (p. 15).
3. **Citation edges.** decius2026 and choroszewicz2026 answer candidate 8 without citing any of its askers. johnsson2026 cites stark2024 only, which asks neither candidate 2 nor candidate 6. These stay in the file as convergent evidence.
4. **choroszewicz2026.** The interview excerpt on p. 9 holds two colleagues, the caller the worker had advised and the colleague she then consulted; the card had one.
5. **`PICKUP_P1.md`, candidate 3**, says of Bujold et al. that "Specifying intent is absent". As an ability it is. The nearest construct is "human influence", "the extent to which workers have a voice, exert control over the system, opt out if desired, and contribute input" (p. 8), which the organization sets.
6. **`PICKUP_P1.md`** quotes Gulbrandsen and Just at pp. 162 and 161; the pages are 163 and 162 (S10e).

## The ten candidates at a glance

Flagged rows are triage rows classed `possible_takeup` or `possible_answer` for the candidate; a work that cites two asking articles has two rows.

| Candidate | Flagged rows | Cards that touch it | Answers | Contests | Nearest to algorithmacy's answer |
|---|---|---|---|---|---|
| 1 Communication field | 3 | 3 (and hall2025, unread) | none | none | none; one sentence in Gulbrandsen and Just (p. 162) |
| 2 Blind following | 8 | 4 | none | none | Steiger et al., a team process (p. 15) |
| 3 Partner or medium | 29 | 7 | bujold2026, in its scope | none classed | Bujold et al.: the position, for one party |
| 4 Co-opted person | 32 | 3 | none | none | Choroszewicz: users as "interpreters" (p. 9) |
| 5 Expertise | 23 | 5 | none | none (one finding contested) | Hubert: "fonctions d'orchestration" (p. 7) |
| 6 Invisible work | 26 | 6 | none confirmed; two possible, abstract only | none | Choroszewicz; S.G. and Lyytinen (abstract) |
| 7 Artificial persons | 21 | 2 | none | none | none |
| 8 Accountability | 20 | 8 | zelles2026; choroszewicz2026 and decius2026 with no edge | none | Bujold et al.'s moderator (p. 15) |
| 9 Digital brokerage | 5 | 1 | none | none | not examined |
| 10 Coordination | 14 | 1 | none | none | not examined |

## Candidate 1. Organization and communication as one field (OQ-stark2024-06)

- **Takes up.** gulbrandsen2025 (full; other point), weakly and without framing it as the call. The review reports that "people's ability to participate is constrained by the platforms' ability to organise publics" (p. 163); its one citation of Stark and Vanden Broeck supports the point that platforms "remain businesses, first and foremost" (p. 161).
- **Passing.** phillips2026 (full; other point): "Intelligent technologies now underpin much of the communication and interaction through which we organize." (p. 252). alishani2025 (full; no edge): a chatbot gives "a much more direct and uninterrupted form of communication" (p. 41).
- **Not touched.** zelles2026 and avnoon2026, though both cite stark2024.
- **Unread.** hall2025 (held). Hall and Kuhn's 15-page review on communicatively theorizing corporations cites stark2024 and is the likeliest engagement by its title.
- **Answers or contests.** None.
- **Gap check.** The nearest sequences sort by medium. Emigh (2024, abstract only): "Orality, literacy, and digitality are forms of knowledge and communication based on speech, reading and writing, and electronic technologies using binary formats, respectively." Heyd (2021, full text) proposes "the stage of tertiary orality" (p. 136). Gloy's *From orality via literacy to artificial intelligence* (2025) is known only through a review. The gap-check agent found no work that classifies communicative capacities by the form of the relation and extends oracy and literacy to a capacity for triads, in OpenAlex or Consensus.
- **Algorithmacy's answer already given?** No. Gulbrandsen and Just come nearest in one sentence they do not develop: "when users become aware that they are interacting with technologies rather than directly with each other, this awareness shapes their social and their technical interactions" (p. 162).
- **State.** The least taken up of the ten, and incomplete while Hall and Kuhn stays unread.

## Candidate 2. Blind following and emergent interdependence (OQ-hinds2024-04)

- **Takes up.** steiger2026 (partial; other point): teams "must repeatedly clarify what GenAI may influence, what it should contribute, and how strongly they intend to rely on its output" (p. 15). hubert2025 (partial; on the question's mechanism, borderline): "Sans artefacts probatoires, les réponses oscillent entre contournement et dépendance aveugle." (p. 25). johnsson2026 (partial; no edge): "As employees resolve certain issues individually through AI tools rather than turning to colleagues, the number of occasions where knowledge is articulated and circulated within the team decreases." (p. 45). choroszewicz2026 (partial; no edge): "users worried that the AI's fluency and confidence could lead to tacit acceptance or overreliance" (p. 9).
- **Answers or contests.** None. No work poses the question in the askers' words. Steiger et al. imply a conditional no: reliance rose where teams were exhausted (the oracle role, p. 13).
- **Convergence.** Following the system blindly is a risk that depends on conditions: the team's remaining capacity (Steiger et al.), evidence artefacts (Hubert), the tool's fluency (Choroszewicz). Johnsson and Nikolausson document the colleague dropping from view, as fewer exchanges.
- **Gap check.** Yuh, Cho and Lee (2026; abstract and three excerpts) come closest: "learners must be trained to coordinate human-AI-human collaboration in realistic clinical settings." Their competence is collective, "collaborative—not merely individual" (body text), and aimed at the AI's output. Lyons and Stokes (2012, abstract only) report that with automation present, "reliance on the human aid decreased during high-risk decisions". The gap-check agent found no work that proposes an individual's capacity to keep a mediated colleague in view as the remedy.
- **Algorithmacy's answer already given?** No. The nearest rival, delegation calibration, is a team process of setting reliance. No work has a member telling whether guidance reflects the system or the colleague.

## Candidate 3. Partner or medium: technology between people

- **Answers.** bujold2026 (full; other point), for the worker–organization relation. Bujold, Gaudet and Parent-Rocheleau reject the medium picture, since AM "employs advanced algorithms rather than simply using technology as a communication medium" (p. 6), and the partner picture, since workers engage organizational intentions "rather than forming relationships with the algorithms themselves" (p. 6). In their place: "Technological intermediaries are systems that stand between two parties in a relationship, shaping how each party perceives and interacts with the other by executing actions on behalf of one party" (pp. 2–3). The two parties are a worker and an organization; the intermediary acts for the organization and evaluates the worker; colleagues appear only as future research (p. 18).
- **Takes up.** alishani2025 (full; other point): professionals behind a government chatbot "apply discretion in making technological artifacts fit with real-world conversations" (p. 41). decius2026 (full; other point), on the party side: "Individuals benefit from treating AI as a collaborative partner that can augment judgment while preserving human agency." (p. 35).
- **Passing.** zelles2026 (full): "The platform stands formally independent of both parties." (p. 17). gulbrandsen2025, avnoon2026 and phillips2026 (all full).
- **Contests.** None classed. Bujold et al. lean that way toward the partner premise of OQ-stark2024-07 without citing it (correction 2 above).
- **Gap check.** The triad has precedents. Pfadenhauer and Kirschner (2017, full text) describe platforms that bypass "the traditional dyadic healthcare service encounter in a twofold manner" (p. 7). Curchod et al. (2020, abstract only) find "an implicit coalition between buyers and the platform owner, who join together in the evaluation procedures". Edwards et al. (2026, abstract only) hold both pictures at once. The gap-check agent found no work that sets technology as an evaluating, binding intermediary between two people against both pictures and names the competence that position requires.
- **Algorithmacy's answer already given?** In structure, in part; in substance, no. The third position is taken for one relation (Bujold et al.) and observed in another (Zelles et al.). Bujold et al. name two of the three parts as conditions: "Workers may struggle to understand not only current decision logic but also why and how that logic changes over time" (p. 11), and "workers with greater technological knowledge may better distinguish between system inherent flaws and organizational choices" (p. 15). No work names an ability, and none puts a second person behind the system whom the system also evaluates.

## Candidate 4. The co-opted person's side

- **Takes up.** choroszewicz2026 (partial; on the question): users were "positioned as performing three roles—testers, AI outputs' quality verifiers and interpreters" (p. 9). rikala2025 (partial; on the question): "Meta-work was found to increase burdens and worsen technostress." (p. 1). aleksic2026 (partial; other point): chatbot use goes with "higher levels of autonomy, competence, and relatedness" (p. 236).
- **Answers or contests.** None.
- **Convergence.** All three answer in the askers' genus, the experience and the costs of the person.
- **Algorithmacy's answer already given?** No. The works describe burdens and responses. Choroszewicz comes nearest by naming interpretation as a role imposed on users, and what her users interpret is the tool's output.
- **Coverage.** Three cards against 32 flagged rows, the thinnest sample in the set.

## Candidate 5. Expertise and the division of labour

- **Takes up.** hubert2025 (partial; on the question): "la valeur ne réside plus dans une expertise substitutive, mais dans des fonctions d'orchestration." (p. 7). dowsett2026 (partial; on the question): GenAI "allows novices to enter expert domains" (p. 168). avnoon2026 (full; other point) poses the retention question and leaves it: "Only time and further study will tell." (p. 8). akhil2026 (abstract only; no edge).
- **Passing.** choroszewicz2026 (no edge).
- **Answers or contests.** None. Dowsett contests one finding that Hsu and Bechky report, and takes the question up.
- **Algorithmacy's answer already given?** No. Expertise moves in these works, as it does in the brief, and the new demand they name is orchestrating evidence, adjudicating machine claims or guarding one's scope. None calls the demand relational.

## Candidate 6. Invisible work and opacity

- **Takes up.** choroszewicz2026 (partial; on the question): prolonged engagement "can function as users' invisible work to compensate for the limitations of AI tools (Justesen and Plesner, 2024)" (p. 6). rikala2025 (partial; on the question): "only 14% of responses reported meta-work" (p. 17).
- **Takes up, possible answer (abstract only).** akhil2026: "We position argumentation labor as a layered, additive form of invisible labor that extends, rather than replaces, the classical articulation, coordination, and infrastructural work." (abstract). ivarsson2026: "a taxonomy of five forms of invisible work involved in producing personal data: strategizing, resourcing, maintenance, interpretative, and care work." (abstract). The citation of justesen2024 rests on OpenAlex's index for both.
- **Passing.** johnsson2026 and hubert2025 (both no edge).
- **Answers or contests.** None confirmed.
- **Algorithmacy's answer already given?** In part, for one part. Choroszewicz treats interpreting AI output as invisible work and adds "interpretative" opacity (p. 9); S.G. and Lyytinen's abstract does the same for adjudicating machine reasoning. Neither covers specifying intent or keeping track, and neither has a colleague on the far side of the system. The S.G. and Lyytinen paper needs a full read before anyone writes a sentence about it.

## Candidate 7. Artificial persons, technology as structure

- **Takes up.** phillips2026 (full; on the question), on both sides: he names the assumption that "technology is something an organization has rather than something an organization is" (p. 250) and keeps the agent picture, "we are no longer alone" (p. 248). The phrase "artificial persons" does not occur in the essay. decius2026 (full; other point), on the party side, with personhood disclaimed (p. 3).
- **Not touched.** chao2026.
- **Answers or contests.** None.
- **Algorithmacy's answer already given?** No. Phillips puts the change in theory, and he never asks what members must be able to do.

## Candidate 8. Accountability when an algorithm decides (OQ-stark2024-04)

- **Answers.** zelles2026 (full; on the question), the one carded work that engages the askers' principle as such: on delivery platforms "responsibility is systematically displaced from the platform" to "the courier" and "the customer" (p. 17), and in traditional firms "formal managerial accountability is preserved rather than displaced" (p. 20).
- **Answers, no edge.** choroszewicz2026 (partial): users "absorb the burden and consequences of testing immature AI tools without having sufficient control" (p. 10). decius2026 (full): "accountability should be allocated across the chain of design, deployment, oversight, and use" (p. 36), offered as a practical implication.
- **Takes up.** chao2026 (full; other point): "the accountability architecture is a design variable" (p. 2). bujold2026 (full; other point), on attribution: the organization, "not the algorithm", is the exchange partner (p. 15). zientara2026 (abstract only): "who bears responsibility for a system's consequences" (abstract).
- **Passing.** alishani2025 (no edge), avnoon2026.
- **Contests.** None.
- **Convergence.** Accountability lands on the nearest human unless an organization re-anchors it.
- **Algorithmacy's answer already given?** No, and the shortlist expects none: every work answers the liability question. Two passages supply the participant's problem without theorizing it. Zelles et al. code a courier's complaint as "opacity of the system; denial of the rating’s existence; no addressable counterpart" (table, p. 10). Bujold et al.'s moderator (p. 15, quoted under candidate 3) is the nearest thing in the set to algorithmacy's first part, with an organization on the other side.

## Candidates 9 and 10

- **9, digital brokerage.** One card touches it: bujold2026, `passing`, with no edge (it cites neither hinds2024 nor brennecke2025). Triage T2 reports that among the works citing hinds2024 "none touches the brokerage question (9) except the platform-governance paper", which was not carded. The pick-up for candidate 9 is unexamined.
- **10, coordination.** One card touches it: steiger2026, `takes_up` (other point), where delegation calibration is a coordination process. Triage T1 reports of the three take-up works citing racker2024 that "none involves algorithms, platforms or AI"; none was carded. The pick-up for candidate 10 is unexamined beyond that.

## Across the candidates

- **No contest.** No carded work contests a shortlisted question, and triage found no `possible_contest` in 272 rows.
- **Two answers with a citation edge.** Bujold et al. on candidate 3, in their scope, and Zelles et al. on candidate 8.
- **Three convergences.** The intermediary's position is visible (Bujold et al.; Zelles et al.). Interpreting a machine's output appears as imposed or unrecognized work (Choroszewicz; S.G. and Lyytinen's abstract) and as a moderator (Bujold et al.). The colleague drops from view (Johnsson and Nikolausson; Lyons and Stokes's abstract in the gap check).
- **What no work does.** In every case the object of the skill, the labour or the trust is the system or its output. I found no work that names a person's ability to work with another person through a system that evaluates both, in the 19 carded works at the depths stated above; the gap-check agent found none for candidates 1 to 3 in OpenAlex and Consensus on 22 November 2026, with Scholar Gateway unavailable.
