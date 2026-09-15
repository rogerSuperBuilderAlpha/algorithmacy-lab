# Panel synthesis — Who Hosts the Guest? — 2026-09-03

Eight reviewers on Fable 5.1, reading `manuscript/DRAFT.md` (the 26 August text: body 8,624 words
against a 9,000 ceiling under the body-only ruling, 123 references, 23/23 preflight checks green)
independently, the day before the window closes. Brief and personas in `PANEL_BRIEF.md`; the eight
files hold the full commentary and every drafted replacement. This file adjudicates, ranks by
convergence and severity, and gives the evening's order of work. Where a reviewer's claim about a
source was contested, I checked it against the cards and the 18 August audit before adopting it; the
adjudications are in §3 and they overrule individual reviews.

## 1. Verdicts

| # | Reviewer | Field | Verdict | Single most important fix |
|---|---|---|---|---|
| 01 | Ellery | critical hospitality theory | minor | l.61 bare-presence claim vs the conditional tradition; move Derrida there to do work |
| 02 | Sarkisyan | phygital service research | minor | engage Shabnam et al. 2026 at the §3 gap statement (l.51) |
| 03 | Chow | hospitality technology, robots | minor, ready tomorrow | credit Gursoy 2026 for "AI redistributes agency" at l.63; cite Gao et al. 2026 |
| 04 | Reinholt | algorithmic management | minor | cite Jianu, Ashton and Lugosi 2025, carded and uncited, at ll.63, 67, 108 |
| 05 | Furtado | responsibility ethics | minor, doable tonight | drop the second "only" at l.61 and rebuild the trustee pair |
| 06 | Reviewer 2 | hostile generalist | minor, would not hold submission | l.33 contestability definition is thinner than the paper's own sources |
| 07 | Editor | special issue | minor on the manuscript; **packet not ready** | regenerate `submission/` from tonight's DRAFT; add the AI acknowledgment |
| 08 | Copyeditor | Intellect Harvard | minor, mechanics | delete l.3; fix four wrong-author entries; reconcile the packet |

**Nobody attacked the argument.** As on 17 August, every finding is a source read too thinly, a
claim scoped too widely, an internal inconsistency, or apparatus. Two things changed since then.
First, the novelty claim was re-run by 03 against everything published through today and still
holds. Second, the paper's own library now holds three verified sources the text does not cite
(Jianu 2025, Gao 2026, Hirschman 1970, each carded and two of them marked `status: cited`, meaning
a cut removed them), and two published neighbours the arm's own notes flagged as must-engage
(Gursoy 2026 in the bib note; Shabnam 2026 in reviewer 02's 17 August report) are still unengaged.
The exposures are all in how the paper describes its neighbours, not in what it argues.

## 2. The finding that ranks first is not in the manuscript

**The submission packet describes a different paper.** 07 and 08 independently found that
`submission/FRONT_MATTER.md` and `submission/RESPONSE_TO_EDITOR.md` (both 17 August) carry a
different title, a different abstract, a different keyword set, and highlights and a Statement of
Contribution that name "hospitality algorithmacy" and "coordinative sovereignty", terms that occur
zero times in `DRAFT.md`. The response letter points four editor requests at sections that have
moved, quotes a sentence that is not in the manuscript, claims Lynch et al. 2021 is cited (it is not
in the list), and states a body of 6,500 words. `preflight.py` validates the stale file, which is why
it reports 198 abstract words while `DRAFT.md`'s abstract is 202. And the **mandatory AI-acknowledgment
section is absent** from `DRAFT.md`; the file goes from §9 to References. That is a desk-return item.

This is an hour's work, costs zero body words, and 07's R19–R21 supply the text. Do it first.

## 3. Adjudications — where reviewers disagreed, and what the record says

1. **Martin and Waldman, l.124, "oversight and audit lowered it".** 04, 06 and 07 doubted it; 06
   thought it contradicted the authors' sibling paper. 05 said it was verified. **05 is right.** The
   18 August audit read the full text (`reviews/2026-08-18/sources_05.md` §1): "impact assessment,
   human-in-the-loop, and external audit *lower* legitimacy relative to mere notice ('This was a
   surprise and counter to the hypothesis,' β for appeals = 4.54)". The card is stale (abstract-era
   summary). Keep "lowered". Fix only the dangling antecedent ("the three") and the year (issue
   183:3 is 2023). Do not adopt 04's R16 or 06's R2 weakening.
2. **Garcia et al., l.67 and l.98.** 03 said the mechanism is reversed; 06 and 07 said the wording
   matches the abstract. **03 is right on precision, and it strengthens the example.** The abstract
   (quoted by 03; bib note agrees: "recommendations are written in anticipation of deviation") has
   managers *under-adjusting* because adjustment costs effort, and the algorithm biasing its
   recommendation to compensate. "Counted on revenue managers to adjust them" (l.98) can be read
   the wrong way; "expect staff to override their suggestions" (l.67) is wrong: inertia, not
   override. And neither Bendoly nor Garcia is at the front desk. Adopt 03's R3 and R4, which are
   written direction-neutral because nobody on the project has read the body. 07's VERIFY on the
   authors' own recommendation (automating the adjustment) stays open; the abstract's last clause
   supports it.
3. **Mosca et al. 2026b as the sole citation for the knowledge/discretion/authority triad, l.63 and
   l.150.** 02, 03 and 07 all flag it; the card (`mosca2025phygital.md`) is abstract-depth,
   records well-being valence only, and says "never the sole support for anything". **Adopt.** The
   triad is the paper's own. Cite Gursoy 2026 for the redistribution-of-agency observation (bib note:
   "already says AI redistributes agency… MUST BE ENGAGED IN SEC 3"; 03 confirmed the phrase
   verbatim against the deposited abstract), move Mosca to the l.156 well-being cluster where the
   card says it belongs, and leave Casalegno alone on l.150.
4. **Manfreda, l.41.** 01 says the card says "gratitude"; 07 says it says "altruism, generosity,
   kinship". **01 is right.** `manfreda2025reciprocal.md`: "driven by gratitude rather than by
   obligation or indebtedness", and the card asks for the disclaimer to be quoted, not paraphrased.
5. **Zhou's three remediating items, l.110.** 06 doubted the card supports the three-way split.
   **The manuscript is right.** The 17 August reviewer 04 transcribed the three validated items from
   the scale table (`reviews/2026-08-17/04_algorithmic_management.md` ll.68–74). Given names on the
   card and in the list disagree; the copyeditor's.
6. **'fluidify', l.126.** 06 and 08 say no card verifies it; 02 says verified. **02 is right,
   with a correction.** `CLAIMS.md` row 21 and `LIBRARY.md` l.66 record "fluidifying" verbatim in
   Batat's abstract. The manuscript quotes "fluidify", the wrong inflection inside quotation marks.
   Quote "fluidifying" with the abstract's page (Batat 2024: 1220), or paraphrase without marks.
7. **Mameli "contains no discussion of friction at all", l.126.** 06 wants it softened because the
   card is abstract-only. 02 and 07 record that 02 verified it against the open-access full text on
   17 August (no "friction"/"frictionless"; "seamless" once, affirmatively). **Keep as is.** If the
   OA article is reachable tonight, a thirty-second find settles it for good.
8. **Spektor task-list withholding, l.67.** 04, 06 and 07 raised VERIFY. **Closed:** the 18 August
   `SOURCE_AUDIT.md` item 7 read it in the 2023 paper ("only in the most limited configurations"),
   which is what the manuscript says.
9. **The second "only" at l.61.** 01, 05, 06 and 07 say drop; 03 says keep. **Drop.** 05's argument
   is decisive: ownership non-delegability is generic to every role-making duty (controller and
   processor, hospital and outsourced nursing, trustee and delegate), so welcome is not unique on
   that axis. The paper's real point, which 05's rewrite makes the trustee pair say, is that a host
   who hands the answering to a system hands it to a party that cannot receive it.
10. **The bare-presence claim at l.61 against the conditional tradition.** 01 says it fails; 05 says
    it survives if "arrived" means arrived as a guest; 07 says §2's "admit" already carries the
    answer. **Adopt 01's rewrite**, because it costs 20 words, it converts the sentence a Derridean
    referee rejects into one that enlists him, and Derrida is otherwise cited decoratively at l.41
    (the card says exactly what the paper wanted him for and the text never uses it).
11. **Fink 2025.** 01, 02, 03, 05 and 06 say cut; 04, 07 and 08 say complete the entry and keep once.
    **Cut** from both sites and the list. Sterz et al. carry l.122, Bovens carries l.136, the
    in-text apology goes with it, and the paper loses nothing it quotes. If the authors prefer to
    keep it, 08's entry (SSRN working paper with DOI) is the form, cited once at l.122 with no apology.
12. **The well-being paragraph, l.156.** 01, 02, 07 keep; 03, 06 halve; 05 cut or flatten. **Keep,
    trim the closer.** 07's reason is decisive: it is the paper's only contact with the issue's
    well-being theme and the response letter points at it. Add the colon (08), end on "a job for
    future work" (07 R17), and give it Mosca 2026b (adjudication 3). 03's halving is a CONSIDER.
13. **The language-habit paragraph, l.71.** 01, 02, 06 cut; 03, 05, 07 keep. **Author's call**; the
    tie is real. It is the paper's most cuttable 120 words and its only reflexive move. If words are
    needed after everything below, it is the reserve. Either way cut "and it is worth resisting".
14. **Lynch et al. 2011, l.21, "hospitality and virtuality" and "hostages of each other".** The
    full-text card records neither. Unresolved. Fallback (07): if the phrase cannot be located
    tonight, drop the hostage clause so nothing sounds quoted that is not.

## 4. FIX TONIGHT — ranked, with the chosen rewrite

Costs are body words. Pointers are to the reviewer file and rewrite number; where two reviewers
drafted the same fix the better one is named. Where three reviewers' rewrites overlap on one
paragraph (l.61), a merged text is given in §5.

### A. Apparatus (zero body words, referee-visible on day one)

1. **Regenerate the packet from tonight's DRAFT.** Title, abstract, keywords, highlights,
   Statement of Contribution, response letter. 07 R19–R21 (statement, highlights, letter rows); 08
   finding 2 (highlight drafts in the manuscript's vocabulary). Delete "hospitality algorithmacy"
   and "coordinative sovereignty" everywhere in `submission/`. Repoint `preflight.py` at DRAFT.md's
   abstract. — 07, 08.
2. **Write the AI-acknowledgment section** after §9, before References, in the Notes' form
   (`JOURNAL_SPEC.md`). Only the authors can write it and it must be true. — 07, 08.
3. **Delete l.3** ("For the *Hospitality & Society* special issue…"). — 01, 02, 04, 05, 06, 07, 08.
4. **Abstract, l.7: 202 words and one reversed claim.** "the guest can be left with no one to answer
   to" says the guest owes the answering; the body (l.168) has "no one to answer them". Adopt 07 R1
   (198 words, adds the employee half the call asks for). Minimal alternative: fix "to answer to" →
   "who must answer them", cut "This paper asks a simple question with an awkward answer.", apply
   08's two one-word trims → 192. — 07, 08.
5. **Figure 1 exists only as a caption; no figure file anywhere under `manuscript/`.** Supply it as a
   separate file with "[Figure 1 near here]" at l.27, or delete l.27 and "Figure 1 sets out the
   logic that leads to this thesis." at l.25 (−10). — 06, 07, 08.
6. **Reference list: four wrong-author entries, Crossref-confirmed.** Li and Sun (Huanhuan,
   Zongfeng, e70067); Lin 2025 (Hui, 11:1); Hirsbrunner (Kleemann, Steven; Tahraoui, Milan Nebyl;
   10, 1638257); Mameli (Elisa; full subtitle; 28:1, 19). Plus Huang and Lo (first author Zuwen;
   deposited title differs) and Kim 2025 (first author Hyunkyu). 08 finding 4; 03 finding 7.
7. **Reference list: online-first years paired with issue volumes.** Lv 2024 → 2025 (l.120, l.316);
   Xu 2020 → 2021 (l.102, l.122, l.402); Martin and Waldman 2022 → 2023 (l.124, l.326). The list's
   own policy is issue year (Choi and Chao, Park, Batat 2026 all follow it). 08 finding 6; 02, 03.
8. **Reference list: locators supplied.** Zhou (e70004), Weaver (online first, DOI), Casalegno and
   Mosca/La Rosa (Symphonya issue numbers), Gao and Thebault-Spieker (10:2), Yurrita 2025 (9:7),
   Choi and Chao full title. 08 finding 5.
9. **l.19 "This journal has already asked"** → "Hospitality scholars have already asked" (08) or the
   journal's name (07 R4). Positioning sentence; zero cost. — 07, 08.
10. **Mechanics block (08 findings 9–12):** commas inside closing quotes at ll.37, 71, 81 → outside;
    "section 7" → "Section 7" (l.112); three title-case stragglers (ll.208, 296, 416);
    "face-recognition" → "facial recognition" (l.102); two surviving "she" for the guest (ll.41, 122)
    → "they".

### B. Source precision (a referee who opens the source will catch each of these)

11. **l.63 and l.150, the triad's citation.** Adjudication 3. Replace the first sentence of l.63 with
    03 R2 minus its trailing Mosca citation:
    > As algorithms take on these jobs, agency gets redistributed across the arrangement. The most recent account of the hospitality triad already says so, and it puts guest autonomy and the governance of algorithmic actors on its agenda (Gursoy 2026). We divide that agency into three things, because they need not travel together: knowledge, discretion, and authority.
    At l.150 drop "(Mosca et al. 2026b;" leaving Casalegno. At l.156 add Mosca et al. 2026b beside
    Batat 2022 (07 R6). +35. — 02, 03, 07.
12. **Jianu, Ashton and Lugosi 2025, carded, verified, uncited.** A Delphi study of algorithmic
    management in hotels, *IJHM* 129, 104168, co-authored by an editor of this journal, whose card
    says it "closed the arm's largest evidence gap". Adopt 04 R1 (l.63, Spektor moved off
    "explaining them to guests"), R3 (l.67, managers' running negotiation), R4 (l.108, replaces the
    De Vos 2023 conference abstract with Beatty 2016 + Jianu for the lending claim). +55, one entry
    added, one removed. — 04; the De Vos 2023 half also 02 R8, 03, 06, 07 R8.
13. **Garcia mechanism and placement, l.67 and l.98.** Adjudication 2. 03 R3 and R4. +35 net. — 03.
14. **Hirschman.** Card exists, `status: cited`. One sentence after "The fifth principle: guests must
    keep a real alternative." (l.122). Adopt 04 R14:
    > Voice carries weight when exit stays possible, and an organization that raises the price of leaving has weakened the complaint along with the departure (Hirschman 1970).
    +27, plus the entry (01 R16 / 04 R14 give it in Intellect form). — 01, 04, 06, 07; 05 consider.
15. **Gao, Tan and Wan-Zainal-Shukri 2026, "Hostessing by robots?", in this journal, carded and held
    "for section 3" with the note that not citing it "would be visible".** One clause in the l.61
    perception list, and "owes" in the closer. Merged text in §5. +30, one entry (online first, DOI
    10.1386/hosp_00109_1). — 03, 06.
16. **l.61 closer aligned with l.51.** "no one imagining it as the keeper of the threshold" is
    refuted by the paper's own §3 (Germann Molz, Riordan, Roelofsen and Minca all imagine it) and by
    Gao's title. "no one asking what it would owe as the keeper of the threshold." +3. — 01 R11, 03.
17. **l.51, absence clause.** "What it has not yet asked is what that third party owes" is what
    Sharma and Mattila 2026 ask (title and abstract). Keep only the second half, "where the
    obligation goes when…". 05 R5. −9. — 05.
18. **l.61, Sharma and Mattila as the heir question.** Their question is whether robots *should be
    afforded* responsibilities, the question §1 sets aside at l.23. One clause ties §4 to §1. In the
    merged text. +15. — 03, 05.
19. **l.61, Belanche undersold, l.122.** "differently" hides the finding: less responsibility to the
    robot, more to the firm, especially on failure (card confirms). That is guests already looking
    past the machine to the institution. Adopt 05 R7 (or 03 R5). +10. — 03, 05.
20. **l.23, "Almost no one thinks software picks up moral duties".** Contradicted by the paper's own
    l.61 citation: Kropf et al. 2026 argue a care robot can hold role responsibility (05 fetched and
    quoted the abstract). Adopt 05 R2a:
    > Some in machine ethics hold that a machine can carry the duties of a role it occupies (Kropf et al. 2026). Most do not, and we do not need to settle it.
    +12. Kropf then leaves the governance clause at l.61 (Santoni de Sio carries it). — 05.
21. **l.41, three overclaims on hospitality's own ground.** Manfreda → "gratitude and reciprocation,
    not obligation" (adjudication 4; 01 R6, −6). Pijls: "It tried to measure something next to it,
    and the questions did not survive" (`CLAIMS.md` row 10: the autonomy items meant *not* having to
    ask; 01 R5, +3). "under-theorized" → "The guest's side of the commercial bargain remains, for
    practical purposes, unmeasured" (the guest's obligations are the field's oldest topic; the
    evidence is about measurement; 01 R7, 0). — 01.
22. **l.17, Bulley cited for the reading he argued against.** `NOTES.md` l.640 and l.1132 record
    that an earlier draft carried his post-threshold argument and the cut removed it. Adopt 01 R3:
    > A host does not merely perform tasks. A host takes in the arriving stranger and accepts some responsibility for how that person is received (Lashley 2000). That responsibility does not end at the door. The host's power over the guest runs through the whole stay, and so does what the host owes (Bulley 2015).
    +26. VERIFY against Bulley if the PDF is to hand; the notes are the only record. — 01.
23. **l.112, Cheng and Duggan cited for a mechanism neither tested; Lin's feedback effect attached
    to §7's guest-side principle.** Morrison 2014 is carded (`status: cited`) and names the mechanism
    (futility). Adopt 04 R9, which states the inference as the paper's and cuts the cross-reference
    to Section 7. +17, one entry. — 04; 06, 07 consider.
24. **l.110, Lin 2025 cited as if it studied guests and pricing.** Card: 31 Douyin users; "supports
    the structure of the claim and not its setting." 04 R6 or 06 R5c. +11 to +19. — 04, 06.
25. **l.122, Kim et al. 2025.** A 540-respondent survey of *mandatory* self-service framed as shadow
    work; "guests describe" implies interviews and "optional" is the paper's extension. Adopt 04 R15
    (attributes the frame, lets the paper extend it). +8. — 02, 03, 04, 06.
26. **l.122, Xu et al. and Boo and Chua cited for the cost of declining.** Both are facial-recognition
    adoption studies; neither discusses a penalized alternative. Delete the parenthetical; both stay
    in the list via l.102. −6. — 02, 06.
27. **l.120, Yeung cited as design advice.** Hypernudge is a critique; the card says it supplies the
    contrast. 06 R5b. +15. — 06.
28. **l.63, Zervas cited for authority drift.** Card (full text): a ratings non-portability study;
    "carries the exit-cost half". Drop from l.63, rehouse at l.134 "the one who built their history on
    another platform, where it does not travel (Zervas et al. 2021)". 04 R2, R19. +4. — 04.
29. **l.110, "The first validated scale of algorithmic competency".** Dogruel et al. 2022 refutes it
    unscoped; Zhou claim priority for platform workers. "first validated scale of workers'
    algorithmic competency". +1. — 03, 04, 07.
30. **l.152, Zhou cited for a claim made against Zhou.** "(Zhou et al. 2025; Are 2025)" → "(Vaccaro
    et al. 2020; Are 2025)". 0. — 04.
31. **l.126, the seamlessness claim is unscoped and the paper's own l.134 citations (Padigar 2025,
    Phillips 2024) refute it.** Scope to the phygital frameworks and concede consumer research. 02
    R14 (scope words) or 06 R3 (+25, concedes explicitly). "Extended-reality frameworks" → singular.
    Quotation locators: (Batat and Hammedi 2023: 10); "fluidifying" (Batat 2024: 1220) per
    adjudication 6. Weaver "examines" → "criticizes" (card supports). +8 to +25. — 02, 06.
32. **l.77 and l.79, Okhuysen and Bechky inside a denial of importing, and "accountability" changing
    sense between source and paper.** Five reviewers flag the both-ways sentence; 05 finds the
    equivocation under it (task accountability there, answerability here; `CLAIMS.md` item 18 calls
    it "the most attackable joint"). Adopt 05 R3. +18. — 01, 02, 05, 06, 07.
33. **l.33, "Contestability is a feature of a system".** The paper's own §7 sources (Alfrink,
    Hirsbrunner, Yurrita 2025) have moved contestability from feature to relation; as written the
    definition is a straw version and "standing" reads as a relabel to the referee most likely to be
    assigned. Minimal: 05 F17, "Contestability, at least as design work mostly uses it, is a feature
    of a system" (+7). Full: 06 R1 (+54, concedes the move and says what standing adds). Take the
    minimal tonight; 06's is the top CONSIDER. — 05, 06.
34. **l.69, "shows" → "argues"** for Casalegno (conceptual paper). 0. — 05.
35. **l.166, "accept responsibility for" → "answer for"**, restoring §2's stipulation of the word. 0.
    — 05.
36. **l.160, "we could find no study of this kind" → "… of this kind among guests"** (Jhaver 2018 is
    folk theory among Airbnb hosts and is cited at l.106). +3. — 04, 06.

### C. The three known leftovers, settled

37. **l.112, "five words" is six.** "six words" (or 07's "fits in a sentence"). — all eight.
38. **l.152, the §6 sentence repeated verbatim in §8.** End at "algorithmic competence, and it
    travels well beyond hospitality." −14. — all.
39. **l.150, the human-centricity sentence collapses as punctuated.** Colon after "withholds", full
    stop after "relational judgment". 0. — 02, 05, 06, 07, 08.
40. **l.156, same fault**: colon after "join them", full stop after "institutions"; drop "not a
    claim we have earned here". −9. — 07, 08.
41. **Fink**: cut both sites and the entry (adjudication 11). −14.
42. **Martin and Waldman, l.124**: keep "lowered" (adjudication 1); fix the antecedent, 07 R12
    first version: "One study compared appeal, oversight, and audit as remedies for an adverse
    algorithmic outcome: an appeal that reached the decision raised its perceived legitimacy, while
    oversight and audit lowered it (Martin and Waldman 2023)." +4.

### D. Register (the paper's one uniformity, and six announcements of plainness)

43. **Six announcements of plainness**, zero in the exemplars: l.33 "We should be clear about what
    'standing' adds", l.37 "We should also be plain about", l.55 "Before going further, we should
    be clear", l.67 "and we should say so plainly", l.71 "and it is worth resisting", l.130 "and it
    is worth saying plainly that it is not". 01 R4, R8, R10, R12, R19; 05 R13. −43. — 01, 02, 04,
    05, 06.
44. **l.128–130, the antithesis stack**: "not a good in itself. It is…", "not friction-filled. It is
    interruptible", "not friction but interruptibility", three in 150 words. Thin to one. 03 R9 or
    02 R15. −30. — 01, 02, 03, 05, 06.
45. **l.45, third restatement of the shape claim** ("It helps to see this as a change in the shape
    of the relationship…"); l.47 delivers it. 01 R9. −21. — 01.
46. **"quietly" ×10.** Keep l.19, l.63, and l.108's "quietly translating"; cut seven. 04 R23. −7.
47. **"Strikingly," l.122.** −1. — 01, 02, 03, 04, 05, 06.
48. **l.136, "The verb in the fourth stage is chosen with care"** → "matters" or cut the clause.
    −3 to −10. — 04, 05.
49. **l.110, the third restatement** ("Appealing is an act; being answerable to the appeal is an
    institutional relation."). Cut. −12. — 04, 05.
50. **l.67, "have been seen to lock"** → active (Spektor is the agent and is cited). −4. — 01, 02,
    03, 05, 06.
51. **l.134, "were shown to reduce … the lesson drawn was"**: two agentless passives where the agent
    matters. 01 R20 owns the lesson as the paper's ("the obvious lesson is…"); the card does not
    record Cui et al. drawing it, so do not attribute it to them. 0. — 01, 05, 07.

## 5. Merged rewrite for l.61 (findings 15, 16, 18, 20-adjacent; adjudications 9 and 10)

Three reviewers rewrote overlapping sentences of this paragraph. This merges 03 R1 (Gao, Sharma),
01 R1 (conditions, Derrida), 05 R1 (trustee pair) and 05 R6 (antecedent), with 05 R2b (Kropf
answered) as the optional last step. Split into two paragraphs at "Duties differ". Net about +115
with R2b, +60 without.

> Some recent work has started to put machines in something like the host's chair, but it keeps asking a different question. Studies of 'robotic hospitableness' test whether a robot can make guests feel welcomed, attended to, and reassured (Liu et al. 2026); an emerging theory of AI consciousness asks whether guests can experience genuine hospitality from a machine at all (Lee and Lu 2024); and a recent hospitality study of robots in hostessing roles asks what a de-feminized, non-human welcome feels like to the guest (Gao et al. 2026). Those are questions about what guests perceive. Whether a party seems hospitable and whether it occupies a position that owes the guest something are two different matters, and only the second is independent of what the guest happens to believe. Another line of work asks whether hospitality robots should be afforded rights and responsibilities of their own, and frames the responsibilities as governance: liability, safety, data protection, consent (Sharma and Mattila 2026). That is the heir question we set aside above, and it leaves ours open.
>
> Duties differ in what triggers them. Care is owed because someone is in need. Fiduciary duties are owed because someone has been trusted. Governance duties exist because a system creates risk (Santoni de Sio and Mecacci 2021). A welcome is triggered by one thing only: someone has arrived. Every real welcome sets conditions, a booking, a name, a card that clears, and the question hospitality theory asks about those conditions is who sets them and whether the arrival can still contest them (Derrida and Dufourmantelle 2000). The trigger is still arrival itself, not need, trust, or risk. The ownership of a welcome, as distinct from its performance, cannot be handed off without handing off the role itself. That much is true of any duty that makes a role. What is peculiar to the threshold is where the role goes. A trustee who delegates the work of a trust is still the trustee, and one who resigns leaves a successor the beneficiary can name. A host who gives the answering to a system has given it to no one. The nearest challenge comes from care. Kropf et al. (2026) argue that a robot can hold the role responsibility of a carer without being a moral agent, and even they hold that recognizing this narrows the responsibility gap without displacing human accountability. That is our position at the threshold. Philosophy of technology has imagined the machine as a guest we might extend hospitality to (Introna 2010). Across the hospitality and service literatures we could find no one asking what it would owe as the keeper of the threshold.

Then at l.41 drop Derrida from the mutual-bond parenthesis (01 R2), so he is cited where he works.

## 6. CONSIDER — the author's calls, ranked by what they buy

1. **Shabnam et al. 2026 at the §3 gap (l.51), +71.** 02's single most important fix, raised on 17
   August and again tonight. The TPSR agenda names agency, governance and interpretive labour as
   the open ambiguities of algorithmically mediated service and says existing frameworks cannot
   explain how digitally enforced rules redistribute labour; the paper cites it once, in a §7 aside.
   02 R1 makes the gap belong to the field and says what the paper adds. VERIFY the paraphrase
   against the abstract (no card). Leaning fix: with 11 done for the hospitality side, this does the
   same for the service side.
2. **The forum's provenance at l.79, +50.** 05 R4: Bovens's forum presupposes an institutional
   relation the guest lacks; the answer is in the paper's own definition of welcome (responsiveness
   and exception are answerability, owed on arrival), and §7's stage 4 builds the place. Depends on
   nothing unverified. Leaning fix.
3. **06 R1, the full contestability concession at l.33, +54** (over the minimal hedge in 33).
4. **The language-habit paragraph, l.71**: tie (adjudication 13). The reserve if words run short.
5. **01 R4 second part, +30**: name what the welcome definition sets aside (hospitableness: care,
   generosity, pleasure in company) and why (a machine can imitate all three and cannot confer
   standing).
6. **01's threshold sentence at l.130, +25**: interruptibility named as the field's own figure, the
   threshold, which is what answers "seamful design in a hospitality register" from hospitality
   theory rather than from HCI.
7. **07's spend A, +39**: answer the title in one sentence at l.168 ("The host is whoever can still
   be asked and is still obliged to answer.").
8. **07's spend C, +38**: "The threshold itself has moved" at l.59, the paper's only sentence
   addressed to the call's politics-of-space criterion.
9. **06's worked run of the six questions on the pricing case, +52 net.** The paper says the test is
   something a manager can do and never does it once. Also 06 R13: Table 1 caption reverts to the
   binary l.81 renounced; row 1 should read "whether the decision can be pinned on a party at all".
10. **04 R5, +43**: the third fragility of the lending (it is invisible labour; Pedersen and Pors
    already in the list).
11. **04 R17, +38**: Yurrita 2025's hosts naming "who is accountable" as the precondition for
    contesting, the counterparty thesis from the subject's side.
12. **06 F8**: principle two (adjust settings) has no parent condition; say which principle answers
    which. +35.
13. **06 R4 / Yuan 2026**: the augment/substitute pair is the service triad's own; one sentence
    distinguishing the paper's use. +40; Yuan is carded as the rival.
14. **03 R7**: "The guest-facing half has barely been studied" → what has not been studied is where
    authority sits, not what guests perceive. +15.
15. **03 R14**: the check-in inference from a modelling choice, l.102. 0.
16. **03**: Kim 2021 beside Garcia at l.100 → Belanche. 0.
17. **04 R11**: Zientara's voice is collective ("prefer to quit rather than organize"). −2. VERIFY.
18. **07 R2**: keyword "hospitality standing" is a phrase the body never uses → "guest standing".
19. **08 findings 16–17**: twelve citation groups out of chronological order; drop the a/b on Mosca.
20. **08 finding 18 / 07 F16**: the roadmap paragraph at l.25 (140 words the abstract has spent, a
    form neither exemplar uses). Cutting it pays for every spend above.
21. **06 F11**: self-citation signature at l.118 (Mosca and La Rosa, Mosca 2026a, De Vos 2026 in one
    sentence). Cut Mosca 2026a; Sterz carries the claim. 07 F22 concurs: do not add one more editor
    citation.
22. **04 F17**: Kellogg, Valentine and Christin 2020 behind "algorithmic direction". No card; do not
    cite without verifying.

## 7. CARRY FORWARD

- The full forum treatment (05 F10): what distinguishes the property's own forum from the appeal
  desks Vaccaro and Are found wanting; external recourse; who audits the forum.
- §7's paragraphs open cold at ll.126, 132, 134 (06); the one cohesion fault, not fixable without
  restructuring.
- Guest-facing staff under algorithmic direction have not been studied; l.67 says so (04 F19).
- The spatial thinness beyond 07's spend C; Park 2026 on lobbies is the door (07 F23).
- Krzywdzinski 2024 and Keegan 2025, carded with verification debts (04 F18).
- Stock-Homburg and Kegel, Wang et al. 2026 on Airbnb hosts (03), unverified, optional.
- The card library disagrees with the reference list on given names for Zhou, Lin 2026, Choi, De
  Vos 2023, Lee and Lu, Schmidt, and carries stale "rejected"/"not admitted" statuses on Martin and
  Waldman, Spektor 2023 DIS, Ehsan and Bovens, all cited. Fix after submission so the next pass is
  not misled (03, 04, 07, 08).
- Cards missing for Garcia, Introna, Pijls, Bulley, Gursoy, Bendoly, Kropf, Santoni de Sio,
  Riordan, Lind, Zientara, Costanza-Chock, Shabnam, Odekerken-Schröder.

## 8. Word budget

Body 8,624; ceiling 9,000; headroom 376.

| block | net |
|---|---|
| A apparatus | 0 (−10 if Figure 1 is cut) |
| B source precision, items 11–36, with the merged l.61 at +115 | about +405 |
| C leftovers, items 37–42 | about −33 |
| D register, items 43–51 | about −130 |
| **FIX TONIGHT total** | **about +240** → body ≈ 8,865 |
| CONSIDER 1 (Shabnam) | +71 → 8,936 |
| CONSIDER 2 (forum) | +50 → 8,986 |
| reserve: language-habit paragraph | −120 |
| reserve: roadmap paragraph | −140 |

Everything in FIX TONIGHT fits with ~135 to spare. The first two CONSIDERs fit on top if one of the
two reserve paragraphs goes, or the merged l.61 drops Kropf R2b (−58). Do not spend past 8,950
without a read-aloud; the register is the paper's asset and the additions are all citation-bearing
prose.

## 9. VERIFY — consolidated, what only a PDF or the authors can settle

1. Bulley 2015: the post-threshold argument (01 R3). Notes are the only record.
2. Lynch et al. 2011: "hospitality and virtuality", "hostages of each other" (l.21). Card silent.
3. Germann Molz 2026: "visible, disciplined, and finally dispensable" (l.19). Card abstract-only.
4. Riordan 2024: supports "platforms push the human host out of view"? Card absent; the Germann
   Molz card says the Riordan sentence was retired and it is still cited.
5. Shabnam 2026 abstract wording before CONSIDER 1 goes in.
6. Gursoy 2026 "redistributes agency": 03 confirmed against the deposited abstract; no card.
7. Kropf 2026 abstract: 05 fetched and quoted; no card.
8. Garcia 2026: the authors' own recommendation (automating adjustment); abstract's last clause
   supports it; nobody has read the body.
9. Cui 2020: whether the authors draw the expand-reputation lesson themselves. Card silent; 01 R20
   owns the lesson rather than attributing it.
10. De Vos 2026 at l.118 "employees tend to resist technology when its purpose is hidden": card does
    not hold it (07 F8). Fallback wording in 07.
11. Batat and Hammedi 2023: abstract on p. 10; Batat 2024: abstract on p. 1220. Confirm in the PDFs
    before writing the locators.
12. Mameli 2026: a find on the OA text if reachable (adjudication 7).
13. Batat 2021: whether the projection can be declined (02, [CARRY FORWARD]).
14. Kim 2025: sample setting, and the first author's name (Hyunkyu per Crossref).
15. Abstract length in Word, not by whitespace, before upload.
16. The AI acknowledgment must describe what happened.

## 10. Protect — the consensus list, do not touch tonight

- l.23: "The problem is not the missing human face. It is the missing answerable counterparty."
- l.19: "That work asks what happens as the host is erased. We ask the next question."
- l.33: "Standing is the prior condition that makes a challenge more than a complaint shouted into
  the void."
- l.41: the Pijls passage as an argument.
- l.47: the chain and the break.
- l.51: "Hospitality scholarship, in other words, was already worrying that a third party had
  unsettled the question of who hosts while the service literature was busy naming the triad."
- l.61: "Whether a party seems hospitable and whether it occupies a position that owes the guest
  something are two different matters…"; "A welcome is owed for one reason only: someone has
  arrived"; the trustee pair (in its rebuilt form).
- l.65: "Discretion acts on the single case. Authority acts on the rule."
- l.67: the evidence-unevenness paragraph, which licenses every borrowing from platform labour.
- l.81: "Accountability cannot be bought back with the other two."
- l.83: the transparency inversion.
- l.98: the Garcia concession in its three-sentence form.
- l.110: "Skill cannot conjure a counterparty"; the Zhou reading.
- l.112: "competence is learned, standing is conferred."
- l.124: "Some problems ask people to become more capable. Others ask institutions to become more
  answerable."
- l.128: "A system built never to interrupt the guest can become a system the guest cannot
  interrupt."
- l.130: "A visible seam is no use to a guest unless somebody stands behind it."
- l.132: the Lind passage with its boundary.
- l.134: "A remedy that needs the guest to have been legible all along is no use to the guest whose
  problem is that the system cannot read them."
- l.168: "somebody still owes the guest a welcome."

## 11. Order of work for the evening

1. Block A (apparatus): packet, AI acknowledgment, l.3, abstract, Figure 1, reference list. An hour.
   Zero body words. This is what the editor reads first.
2. The merged l.61 paragraph (§5) and l.41's Derrida move. The paper's spine, four reviewers.
3. Block B items 11–14 (Gursoy/Mosca, Jianu, Garcia, Hirschman): the four sources a referee from
   this community will look for.
4. Block C (the six known leftovers) and Block B items 21–36 (the citation-precision list), each
   under five minutes.
5. Block D register cuts, then `wordcount.py` and `preflight.py`.
6. Decide CONSIDER 1 and 2 against the count.
7. Read aloud. Then the packet again, against the final text.
