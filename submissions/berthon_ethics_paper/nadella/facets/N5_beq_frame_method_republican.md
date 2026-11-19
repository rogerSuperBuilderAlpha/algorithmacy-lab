# N5 — The structural models, the analogy method, and whether internal critique binds a present actor

*Facet N5, 2026-10-24. Agent-drafted. The author has not reviewed it, and none of the text is the author's.*

**What this facet covers.** Three things the outline leans on without cards: (Q1) what the six structural-model
papers actually do, measured against the outline's description of them (Luchs; Diamantis; Kugelberg and Kugelberg;
Sharon and Gellert; Seele and Schultz; Kingston and Carnovale); (Q2) how the analogy method is stated in the
literature, and whether mapping a shared property is enough to carry a verdict from source to target (A6); (Q3)
whether the internal-critique frame and republican non-domination give a standard that binds a present actor (A7),
including the strongest objections. (Q4) BEQ's author instructions, checked against the outline.

**The question the synthesis answers.** Can the paper's frame make literacy-era verdicts bind Nadella and Microsoft,
and do its model papers license the outline's structure? Short answer, argued in (c): the structure is licensed,
with four corrections of fact about the models (Luchs's shares; Diamantis's concession is distributed; Kugelberg's
first move is a steelman of the opponent; Sharon and Gellert write prose, not a grid). A6 holds only in a stricter
form: the shared property must be the one the historical verdict turned on (Bartha's prior association), with no
critical disanalogy. A7 does not hold on internal critique alone. Walzer's own lecture III, the SEP taxonomy and the
Fraser/von Samson debate agree that a past community's standards bind a present actor only if the actor shares or
professes them, or if their authority is independent. The bridge stands if it rests on two supports: the present
actor's own professions and promises (benchmarks 2 and 3 in present tense), and non-domination as a value the
republican tradition carries across eras by separating core value from period prejudice.

**Premises and outline sections served.** A1, A6, A7 (and A5, A8, B2, CB in passing); Introduction, "Standards of
judgement", present case, Objections, Conclusion, Length.

**Legend for read status.** *Read in full* = I opened the whole text this session. *Read in part* = I opened the text
and read the named pages or sections. *Abstract only* = a database abstract and nothing else. *Not accessible* = no
text. Downloads are in `~/iit-playground/berthon_ethics_local/pdfs/nadella/N5/` (outside the repo); Walzer is the
arm's existing copy at `pdfs/M4/walzer1985.pdf`.

**Count by read status (21 bib keys).** Read in full 10 (`luchs2026taking`, `diamantis2025danger`,
`kugelberg2026practice`, `sharon2024regulating`, `seele2022greenwashing`, `kingston2026social`,
`vonsamson2025immanent`, `hamilton2025digital`, `lovett2026republicanism`, `beq2026preparing`); read in part 4
(`ketokivi2017reasoning`, `bartha2019analogy`, `celikates2023critical`, `walzer1988interpretation`); abstract only 1
(`fraser2023limits`); not accessible 6 (`jaeggi2018critique`, `jaeggi2015towards`, `maas2022neo`, `gadeke2020mugger`,
`pettit1997republicanism`, `maas2023ailike`). Sources opened: 15. Cards written: 14 (12 new, 2 upgrades). Reused and
not reopened: `qadri2026ai` (CARD_INDEX: full, verified), `moodyadams1994culture`, `muldoon2023algorithmic`,
`hoeksema2023digital`.

---

## (a) Search log

All searches ran on 2026-10-24. "Fetch" = curl with a plain browser user-agent. No paywall, bot wall or captcha was
bypassed; every 403 below was logged and left.

| # | Source | Exact query / request | Hits | Notes |
|---|---|---|---|---|
| 1 | Repo reads | `BRIEF.md`, `ARGUMENT_AND_OUTLINE.md`, `RESEARCH_PLAN.md`, `README.md`, `COVERAGE_PREMISES.md`, ledger N01-N08, H24, O03, D01; CARD_INDEX greps (walzer, pettit, lovett, qadri, jaeggi, celikates, gädeke, muldoon, hoeksema, moody) | n/a | Existing: `walzer1988interpretation` (partial, writer-grounded), `lovett2026republicanism` (partial), `pettit1997republicanism` (secondary), `qadri2026ai` (full). |
| 2 | Local PDFs | pdftotext of the six lead-supplied PDFs | 6 | All full texts. |
| 3 | Crossref | `api.crossref.org/works/<doi>` for the six model papers, Ketokivi, von Samson, Hamilton, Fraser | 10/10 | Titles, venues, years match. |
| 4 | OpenAlex | `works/doi:` for Maas 2022, Gädeke 2020, Ketokivi 2017, Pettit 1997, Jaeggi 2018 | 5 | OA locations listed; Pettit and Jaeggi 2018 closed. |
| 5 | EUR repository | `pure.eur.nl/ws/files/47767457/REPUB_102289.pdf` | 200 PDF | Ketokivi et al., publisher's PDF (art. 25fa). |
| 6 | Utrecht repository | `dspace.library.uu.nl/handle/1874/407680` | 200 HTML | No PDF link on the landing page. Gädeke not read. |
| 7 | ScienceDirect | Maas 2022 `/pii/S2666659621000159/pdf` | 403 | Bot wall. Stopped. |
| 8 | SEP | `entries/reasoning-analogy/`, `entries/critical-theory/`, `entries/republicanism/` | 200 ×3 | Revision dates 25 Jan 2019, 12 Dec 2023, 12 Aug 2026. |
| 9 | OpenAlex search | `search=Stahl immanent critique`; `search=Jaeggi immanent critique forms of life` | 8 + 8 | Found Fraser 2023, von Samson 2025, Jaeggi 2015, Stahl 2013. |
| 10 | OUP, Cairn, Wiley | Fraser 2023 PDF; Jaeggi 2015 PDF; von Samson Wiley PDF | 403 ×3 | Bot walls. Stopped. |
| 11 | HU Berlin edoc | von Samson bitstream `88cd4415-...` | 200 PDF | Author deposit; matches published CC BY text. |
| 12 | Tanner Lectures | `walzer88.pdf` | 404 | Page gone; used the arm's local copy (sha256 matches the earlier card). |
| 13 | Consensus | "republican non-domination artificial intelligence platform power arbitrary power governance" | error | Monthly quota exhausted. No Consensus results this round. |
| 14 | WebSearch | `"domination" republican theory artificial intelligence "arbitrary power" tech companies open access article 2024 OR 2025` | 9 | Led to Hamilton (arXiv 2510.00312). |
| 15 | arXiv | `arxiv.org/pdf/2510.00312` | 200 PDF | Hamilton preprint. arXiv API query returned an empty body. |
| 16 | WebSearch | `Matthijs Maas "AI is Like" literature review AI metaphors analogies policy pdf` | 9 | law-ai.org page returned 403. |
| 17 | WebSearch | `Business Ethics Quarterly author instructions word limit manuscript Cambridge` | 9 | Pointed to Cambridge "Preparing your materials". |
| 18 | Cambridge Core | `core-cms.cambridgecore.org/.../preparing-your-materials` (fail, code 000); `www.cambridge.org/core/journals/business-ethics-quarterly/information/author-instructions/preparing-your-materials` | 200 | Full instructions read. |
| 19 | Lead notes | `scratchpad/beq/NOTES.md` | n/a | Read as a lead only (15 recent BEQ articles); not cited as a source. |

---

## (b) Entries

### Q1. The six structural-model papers

**1. Luchs (2026)**, "Taking artificial intelligence from the 'priesthood' ...", *ICS*, online 28 Sep 2026.
`luchs2026taking`; card `literature/cards/berthon_ethics_paper/luchs2026taking.md`. Crossref matched. **Read in full.**
Argues that "each of these moments of 'democratization' is marked by a certain duality" (p. 1; p. 3): access widened
and control centralised, from time-sharing through abstraction to platforms; a CDA of Google Cloud documents is
"structured around the themes identified in the media-genealogical analysis" (p. 3). Opens on Fei-Fei Li's 2017
keynote; "The attempt to 'democratize' computing is by no means new" (p. 2); closes "the media-genealogical analysis
challenges this rhetoric" (p. 14). **Measured shares** (body words, my count; abstract, notes, figures, running heads
excluded): introduction 1,159 (17.6%); genealogy 2,761 (41.9%: 1,071 / 894 / 794); present case 1,994 (30.3%);
conclusion 677 (10.3%); body total 6,591. **Factual slip:** "since the release of ChatGPT in 2018" (p. 13); ChatGPT
launched on 30 November 2022. **Second slip:** software crisis "officially declared in 1968" (p. 6) but "during the
software crisis in the 1970s" (p. 14). *Bearing:* supports the outline's shape (A1, CA); narrows the Length row.

**2. Diamantis (2025)**, "The Danger of Contextual Integrity", *BEQ*, online 27 Oct 2025. `diamantis2025danger`; card
`.../diamantis2025danger.md`. Crossref matched. **Read in full.** A legal-realist critique: CI as a rule of decision
would favour the "repeat player" (p. 1). It calls itself "an internal critique of contextual integrity, not to
advocate for any alternative theory" (p. 4). **Concession move**, distributed: the adherents' good prescriptions "all
accord with widely shared opinions among privacy scholars" (p. 7); the exercise "stacks the legal realist deck in
favor of contextual integrity" by assuming neutral judges (p. 8); CI may favour David "in the short term" (p. 8);
"For all I have said, contextual integrity may still be the best theory available" (p. 19). **Worked case** (§3.5,
pp. 15-16): CI's own library analogy, followed to the library card, would entitle Google to demand ID; "Surely that
is a result every friend of privacy wants to avoid" (p. 16). Eight mechanism subsections; objection replies sit
inside them (§3.1, §3.8). *Bearing:* supports the outline's grafts, narrower in form (A7, A8).

**3. Kugelberg and Kugelberg (2026)**, "Practice-Dependent Governance of AI", *JBE*, online 22 Jun 2026.
`kugelberg2026practice`; card `.../kugelberg2026practice.md`. Crossref matched. **Read in full** (PDF pages).
**Steelman:** they answer the inconclusiveness objection on their opponent's behalf: "inconclusiveness in the form
of reasonable disagreement does not by itself undermine the ideal of moral machine regulation" (p. 6), then press two
"fundamental objections" (p. 6). **Objection order against their own view:** status quo bias (pp. 9-10), then "A
powerful objection" on practice delineation (p. 10). On standards: institutions "do not always deliver on their
promises, we can never take the status quo as a given" (p. 3); the approach "can recommend fundamental reform when a
practice no longer serves the values that justify it" (p. 10); AI is not "simply an additional ingredient that
supervenes onto a stable practice" (p. 10, quoting Gabriel). *Bearing:* supports A7's benchmark 3; complicates A7 by
granting that AI changes the practice (A8 must answer).

**4. Sharon and Gellert (2024)**, "Regulating Big Tech expansionism?", *ICS* 27(15): 2651-2668.
`sharon2024regulating`; card `.../sharon2024regulating.md`. Crossref matched. **Read in full.** Walzerian "sphere
transgressions"; four risks (privacy and three beyond it) tested against seven EU instruments. **Cross-test:** §3.2-3.5
take one risk each and run every instrument against it, in prose; there is no table (pp. 2659-2662); "none of them
properly address the risks we identify" (p. 2652). Concession: "our aim is not to construct a facile critique" (p.
2663). *Bearing:* supports A6's property-by-property testing; narrows the outline's "grid".

**5. Seele and Schultz (2022)**, "From Greenwashing to Machinewashing", *JBE* 178(4): 1063-1089.
`seele2022greenwashing`; card `.../seele2022greenwashing.md`. Crossref matched. **Read in full.** **Method:** "An
analogy typically links a source and a target domain through structural mapping" (p. 1065); boundaries stressed by
problematisation (p. 1065); mapping across five dimensions (p. 1070). **Where it breaks:** seven idiosyncrasies
(pp. 1067-1070), e.g. fluid algorithms that "change shape via software updates"; "Machinewashing should not be
considered a mere extension of greenwashing" (p. 1067); "researchers and theorists should not simply accept the
analogy for its own sake" (p. 1084). *Bearing:* supports A6's procedure; does not warrant normative transfer (its aim
is concept-building).

**6. Kingston and Carnovale (2026)**, "Social Upgrading in Global Supply Chains", *BEQ*, online 14 Jan 2026.
`kingston2026social`; card `.../kingston2026social.md`. Crossref matched. **Read in full.** **Working precedent:** the
principles "might sound overly ideal. However, there is at least one supply chain governance regime that contains all
of these elements, if in imperfect form" (p. 19): the Accord, legally binding under Dutch law, with settled cases
(pp. 19-20), and "a work in progress" (p. 20). Duty: cede power to third parties in binding ways; federated CSR "Just
as constitutions constrain responsible states" (p. 17). *Bearing:* supports the conclusion's precedent move (CB, B2).

### Q2. The analogy method

**7. Ketokivi, Mantere and Cornelissen (2017)**, *AMR* 42(4): 637-658. `ketokivi2017reasoning`; card
`.../ketokivi2017reasoning.md`. Crossref matched. **Read in part (pp. 637-654).** Seele and Schultz's method source.
"Structural soundness requires that a sufficient number of similarities be identified and no critical dissimilarities
found" (p. 650); hasty generalisation glosses "potentially relevant dissimilarities" (p. 647). Scope: explanatory
theory only. *Bearing:* supports A6's procedure; silent on normative transfer.

**8. Bartha (2019)**, "Analogy and Analogical Reasoning", SEP. `bartha2019analogy`; card `.../bartha2019analogy.md`.
SEP record (revision 25 Jan 2019). **Read in part** (§§2-4 as listed). Overall similarity "is not a reliable guide to
plausibility" (§3.5.2); "Greater systematicity is neither necessary nor sufficient ... There is no short-cut via
syntax" (§3.4). Articulation model: "Prior Association" in the source between the shared features and the projected
one, and "no critical disanalogy" (§3.5.2). Legal example: the Donoghue duty extends to a negligent lift repair but not
to a workman who could inspect the crane (§2.1). Precedent "pre-supposes a common set of social values" (§4.4).
*Bearing:* **refines and narrows A6**; supports the form of A7.

**9. Qadri, Prabhakaran and Denton (2026)**, existing card `berthon_ethics_course/qadri2026ai.md` (full, verified).
Not reopened. Verified per CARD_INDEX that it exists: arXiv 2609.31482, ICML 2026 workshop. It makes the same point
as Bartha for AI governance ("imprecise about which property of the technology carries the comparison", p. 1).
*Bearing:* supports A6 (properties, not gestalt).

### Q3. Internal critique, immanent critique, and republican non-domination

**10. Walzer (1988)**, Tanner Lectures, upgrade card `.../walzer1988interpretation.md`. **Read in part** (pp. 33-35,
42; lecture III pp. 57-70). The prophet's message "depends upon previous messages ... The past tense is significant"
(p. 59); repentance is "parasitic upon a previously accepted and commonly understood morality" (p. 63); a detached
critic gets only "a minimal conversation" (p. 65). Limit: the Exodus pledge law "isn't universally known ... it's not
obvious that our ideas are unjust" (p. 69). Changed conditions gave the old law "a new relevance" (p. 70).
*Bearing:* supports A7's shape; **narrows** it to actors inside the tradition.

**11. Celikates and Flynn (2023)**, "Critical Theory", SEP. `celikates2023critical`; card `.../celikates2023critical.md`.
**Read in part** (§2.1 whole, §2.3, §2.5 opening). Internal critique uses standards "already recognized by those
criticized"; external uses standards "not (or not yet) recognized"; immanent critique draws on the implicit norms of
constitutive practices (§2.1). *Bearing:* **narrows A7**: benchmark 2 binds whoever now professes the standard;
benchmarks 1 and 3 show past failure, not present binding.

**12. von Samson (2025)**, "Is Immanent Critique Possible?", *EJP* 33(4): 1308-1325. `vonsamson2025immanent`; card
`.../vonsamson2025immanent.md`. Crossref matched. **Read in full.** The Fraser dilemma: "Either they grant normative
authority to de facto governing norms, which renders social critique structurally conservative. Or they deny it, in
which case immanent critique loses its normative bite." (p. 1308) Resolution: "methodology, not metaethics" (p.
1318); authority must be "independently justifiable" ("We might have signed a contract. We might have made a
promise.", p. 1318); Jaeggi's critique by a formation's own "promises" (pp. 1316-1317). *Bearing:* **refutation
sought, found in narrowed form**: A7 cannot rest on the past norms' embeddedness; it can rest on present promises.

**13. Fraser (2023)**, "The Limits of Immanent Critique", *Proc. Aristotelian Soc.* 123(2): 97-125. `fraser2023limits`.
Crossref matched. **Abstract only** (OpenAlex): the prospects for immanent criticism "are bleak: they must either
commit to an implausible social ontology, a flawed meta-normative theory, or both." *Bearing:* refutes an unqualified
A7; known in detail only through von Samson.

**14. Lovett (2026)**, "Republicanism", SEP, upgrade card `.../lovett2026republicanism.md`. **Read in full** (§§1.2-5).
Liberty as a "structural relationship ... rather than ... a contingent pattern of outcomes" (§1.2); "render him less of
a master" (§2.1); resilient constraints; "better able to cope" (§2.2). On carrying a tradition forward: period
elitism "might merely reflect the accidental prejudices of their day"; contemporary republicans "do not aim to
anachronistically implement the republicanism of yore for its own sake" (§4). Warning about "new forms of dependency
and arbitrary power through those very laws and policies designed to enhance individual freedom" (§4.1). *Bearing:*
**supports A7** via an external value; supports A5 and A1.

**15. Hamilton (2025)**, "Digital Domination", Oxford Intersections (arXiv 2510.00312). `hamilton2025digital`; card
`.../hamilton2025digital.md`. Crossref matched. **Read in full** (preprint). Republican liberty "has, then, been
applied to whatever kinds of domination develop" (p. 5); concedes mass media posed the same threat: "I have no
disagreement here" (p. 9); counts vendor-granted controls as antipower (p. 10). *Bearing:* supports A1 and A7;
**complicates A5** (a published view that vendor-declared controls count).

**16. Not opened (republican and immanent critique):** Jaeggi 2018 (closed); Jaeggi 2015 (Cairn 403); Maas 2022 (403);
Gädeke 2020 (no PDF link); Pettit 1997 (closed; existing secondary card stands, not upgraded). See (e).

### Q4. BEQ author instructions

**17. BEQ, "Preparing your materials"**, Cambridge Core, retrieved 2026-10-24. `beq2026preparing`. **Read in full.** No
card. "The length of an initial submission may not exceed 12,000 words (including the body of the text and the
footnotes, but not including the abstract, tables, figures, or references)"; whole manuscript "not ... more than 50
pages"; abstract "not more than 150 words"; up to six keywords. "Avoid using the first level heading INTRODUCTION to
start the paper." Research article types include "Normative theory work" and "Historical work that makes an
original theoretical contribution". Unlikely to succeed: "Case studies that are largely descriptive." Footnotes, not
endnotes; three citation styles; self-reference in the third person; generative-AI use must be declared ("You should
always declare and describe your use of an AI tool if you have used it to generate text"). I found no rule on first
person. *Bearing:* no element of the outline is forbidden; three constraints apply (see (c) Q4).

**Recent BEQ length (my counts).** Diamantis 2025: about 11,500 words including footnotes, 21 pp. Kingston and
Carnovale 2026: about 12,000 words before the reference list, including footnotes, 28 pp. Both sit at or near the cap,
so "BEQ's recent conceptual papers run 10,000-12,000" is consistent with these two, footnotes included.

---

## (c) Synthesis by question

### Q1. Do the models do what the outline says?
Largely yes; four details are wrong. Luchs's shares are 17.6/41.9/30.3/10.3, not 19/45/28/8; the body is about 6,600
words, and the outline's ~7,000 holds only with abstract and notes. Luchs also contains two slips (ChatGPT "2018",
p. 13; software crisis 1968 vs "1970s"). Diamantis concedes in three places (p. 7, p. 8, p. 19), not once "at the
outset", and his concession includes a stance (assume the most favourable judge). Kugelberg and Kugelberg's first
move is to defend their opponent against a weak objection (p. 6); only against their own view do they go weak to
"powerful" (pp. 9-10). Sharon and Gellert cross-test risk by instrument in prose subsections, with no grid. Kingston and
Carnovale's precedent move is as described, including the concession that the duty "might sound overly ideal".

### Q2. Is shared-property mapping enough to carry a verdict?
No, not as stated in A6. Seele and Schultz and Ketokivi et al. supply the procedure (map, then find critical
dissimilarities) for explanatory analogies; neither addresses carrying a wrong. Bartha's articulation model supplies
the missing condition: the shared property must be the one the source verdict turned on (prior association), and no
critical disanalogy may defeat it. A6 should read, in substance: each pairing shares the property *on which the
historical practice was condemned*. A pairing whose shared property is real but was not the ground of the historical
verdict fails. Bartha's Donoghue example shows the test in law; Qadri et al. make the same point for AI analogies.

### Q3. Does the internal-critique frame bind a present actor?
Not by itself. Three independent sources converge. Walzer's lecture III holds a community to its past standards
only when it shares them, and he declines to judge present practice by the Exodus pledge law (p. 69). The SEP entry
defines internal critique by standards "already recognized by those criticized". Fraser and von Samson argue that
norms embedded in a practice have no authority without independent reasons. Taken together, the three benchmarks
establish that the literacy-era practices failed; they do not establish that the literacy-era standard is Microsoft's.

Two supports make the bridge hold. The first is the present actor's own professions and promises: Nadella's "trust
architecture" (P3), Microsoft's Responsible AI Standard (E14), the post's own admissions (P9). That is benchmark 2 and
3 in the present tense, and von Samson's "We might have made a promise" (p. 1318). The second is an external value with
a cross-era warrant: non-domination, which republicans carry forward by separating the core value from "the
accidental prejudices of their day" (Lovett §4), and which Hamilton applies to "whatever kinds of domination develop"
(p. 5). Bartha's precedent paragraph names the condition both supports meet: a "common set of social values".

Two cautions for A8. Kugelberg and Kugelberg (p. 10) and Seele and Schultz (p. 1070) both say AI changes the practice
it enters; that is the strongest published form of "something has changed". Walzer (p. 70) supplies the reply: changed
conditions can give the old standard "a new relevance".

### Q4. Does BEQ forbid anything in the outline?
No. Three constraints follow. The 12,000-word cap counts footnotes, so the ~11,000-word budget leaves about 1,000 words
for notes. The section the outline calls "Introduction" must carry no heading. The present case must make a
theoretical contribution and must not read as a "largely descriptive" case study. Any generative-AI text in the
manuscript must be declared.

### Claims the sources contradict (in our argument, the ledger or earlier facets)
1. **Outline, Length:** "introduction about 19 per cent, genealogy about 45, present case about 28, conclusion about 8";
   "Luchs runs about 7,000 words." Measured: 17.6 / 41.9 / 30.3 / 10.3; body about 6,600 (card `luchs2026taking`).
2. **Outline, Standards of judgement:** "Concede at the outset ... (Diamantis's concession move)." Diamantis's
   concessions are distributed (pp. 7, 8, 19) (card `diamantis2025danger`).
3. **Outline, Objections:** "Kugelberg and Kugelberg's order: dismiss the weak objection first." Their first move
   rebuts a weak objection *to their opponent* (p. 6) (card `kugelberg2026practice`).
4. **Outline, present case:** "a failure × move grid (Sharon and Gellert's risk × instrument cross-test)." They use
   one prose subsection per risk; the grid is the paper's own addition (card `sharon2024regulating`).
5. **A6 Support column:** "(Seele & Schultz, 2022: map the source onto the target, then state where the mapping
   breaks)" as the warrant for pairings. It is the procedure, not the warrant; the warrant needs Bartha's prior
   association (cards `seele2022greenwashing`, `bartha2019analogy`).
6. **A7 Support column:** "The internal-critique frame (three benchmarks)." On Walzer's own account (p. 69), on the
   SEP taxonomy and on Fraser/von Samson, the frame binds a present actor only through standards the actor shares or
   professes; it needs the present-tense professions and/or non-domination (cards `walzer1988interpretation`,
   `celikates2023critical`, `vonsamson2025immanent`, `lovett2026republicanism`).
7. **Ledger N04** ("used to describe positions, not to condemn them"): for A7 to hold, the paper may need non-domination
   to do normative work, not only description. This is a change of role for the author to rule on.

---

## (d) What the argument can rest on

| Premise / claim | Cards and read status |
|---|---|
| A1: the four design questions as the settled things | `lovett2026republicanism` (full: contestation §4.2; structural freedom §1.2); `hamilton2025digital` (full). The four-question list itself remains the author's ruling; no source states it. |
| A6, procedure (map, then state breaks) | `seele2022greenwashing` (full); `ketokivi2017reasoning` (part, pp. 637-654) |
| A6, warrant (property = ground of the past verdict; no critical disanalogy) | `bartha2019analogy` (part, §3.5.2, §2.1); `berthon_ethics_course/qadri2026ai` (full, verified) |
| A6, property-by-property cross-test | `sharon2024regulating` (full) |
| A7, shape (past standards held against a present community) | `walzer1988interpretation` (part, lecture III pp. 59-70) |
| A7, limit (only if shared or professed) | `walzer1988interpretation` (p. 69); `celikates2023critical` (part, §2.1); `vonsamson2025immanent` (full); `fraser2023limits` (abstract only) |
| A7, support 1: present-tense professions and promises | `vonsamson2025immanent` (full, p. 1318, pp. 1316-1317); `kugelberg2026practice` (full, p. 3); `diamantis2025danger` (full, p. 4) |
| A7, support 2: non-domination across eras | `lovett2026republicanism` (full, §4); `hamilton2025digital` (full, p. 5, p. 9) |
| A8, "something has changed" (strongest form) | `kugelberg2026practice` (p. 10); `seele2022greenwashing` (p. 1070). Reply: `walzer1988interpretation` (p. 70) |
| A5, envelope declared to the deployer leaves a master | `lovett2026republicanism` (§2.1, §2.2, §4.1). Counter-view: `hamilton2025digital` (p. 10) |
| B2 / CB, ceding power to third parties; working precedent | `kingston2026social` (full) |
| Outline structure (Luchs's shape; grafts) | `luchs2026taking`, `diamantis2025danger`, `kugelberg2026practice`, `kingston2026social` (all full) |
| BEQ fit | `beq2026preparing` (full; no card) |

UNSUPPORTED: that Microsoft or Nadella professes any *literacy-era* standard. The present-tense route needs the
Microsoft cards (E14) and facet N1/N4 to supply the professed standards row by row.

---

## (e) Gaps and blocks

| Source | Why not read | Where a Bentley library user would find it |
|---|---|---|
| Fraser, R. (2023), "The Limits of Immanent Critique", *Proc. Aristotelian Soc.* 123(2): 97-125, doi 10.1093/arisoc/aoad005 | OUP PDF 403 (bot wall) | Oxford Academic via Bentley's OUP journals subscription; also JSTOR if held |
| Jaeggi, R. (2018), *Critique of Forms of Life*, Harvard UP, doi 10.4159/9780674988712 | Closed | De Gruyter/Harvard ebook via library catalogue; interlibrary loan. Pages 9-24, 318-319 are the ones cited by the SEP entry |
| Jaeggi, R. (2015), "Towards an Immanent Critique of Forms of Life", *Raisons politiques* 57, doi 10.3917/rai.057.0013 | Cairn 403 | Cairn.info (check Bentley access) or ILL |
| Stahl, T. (2022), *Immanent Critique*, Rowman & Littlefield (trans. of 2013), doi 10.5040/9798881812409 | Not tried after OpenAlex showed no OA | Bloomsbury Collections, if licensed; ILL |
| Maas, J. (2022), "A Neo-Republican Critique of AI Ethics", *J. Responsible Technology* 9, doi 10.1016/j.jrt.2021.100022 | ScienceDirect 403 (gold OA behind a bot wall) | ScienceDirect in a browser (OA); or DOAJ record 9830212f07814fda8e605db45b15e323 |
| Gädeke, D. (2020), "Does a Mugger Dominate?", *J. Political Philosophy* 28(2): 199-221, doi 10.1111/jopp.12202 | Utrecht landing page had no PDF link | Wiley Online Library (hybrid OA) in a browser; Utrecht repository hdl 1874/407680 |
| Pettit, P. (1997), *Republicanism*, OUP, doi 10.1093/0198296428.001.0001 | Closed | Oxford Scholarship Online via Bentley, or the print copy in the catalogue (call number not checked). Pages needed: 52, 62, 73-74, 107, 186-187 |
| Lovett, F. (2010), *A General Theory of Domination and Justice*, OUP | Not searched beyond the SEP entry | Oxford Scholarship Online; ILL |
| Bartha, P. (2010), *By Parallel Reasoning*, OUP | Not searched | Oxford Scholarship Online |
| Maas, M. M. (2023), "AI is Like... A Literature Review of AI Metaphors", Institute for Law & AI | law-ai.org 403 | SSRN or the institute's site in a browser |
| Walzer, M. (1987), *Interpretation and Social Criticism*, Harvard UP | Not opened; pagination differs from the Tanner text | Bentley catalogue or ILL (call number not checked) |
| Walzer Tanner front matter (year 1988, Utah imprint) | Tanner PDF now 404 | Tanner Lectures vol. 8 print copy, front matter |
| Consensus searches | Monthly quota exhausted (resets 1 Nov) | Rerun the republican-AI and analogy queries next round |
