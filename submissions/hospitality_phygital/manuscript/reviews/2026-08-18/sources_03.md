# Source-side audit — slice 03 (21 citekeys, christou2020tourists … hemmer2025complementarity)

Audited 2026-08-17. Method: every DOI resolved through doi.org itself, using content negotiation to
retrieve the publisher-deposited record (the "DOI resolver" route the audit rule permits), plus the
publisher's own page wherever one was reachable. No identity claim below rests on Google Scholar,
ResearchGate, Semantic Scholar, OpenAlex, a citation aggregator, or a search summary. Where a
search summary appears at all it is labelled a lead and given no evidentiary weight. The user's
Chrome extension was not connected, so every route was command-line or WebFetch; blockers are named
per source so nobody repeats them.

Evidence-class labels used below:
- **DOI-resolver record** — the publisher-deposited metadata returned by doi.org content negotiation.
- **Publisher page** — the publisher's own HTML article page.
- **Journal repository** — the journal's own institutional repository (counts as publisher).
- **Preprint (author's)** — arXiv or SSRN full text; used for reading, never alone for identity.

---

## 1. christou2020tourists

**Bib entry:** Christou, Simillidou & Stylianou, "Tourists' Perceptions Regarding the Use of
Anthropomorphic Robots in Tourism and Hospitality," *IJCHM* 32(11), 3665–3683, 2020,
doi:10.1108/IJCHM-05-2020-0423.

**IDENTITY: CONFIRMED** against the publisher page,
https://www.emerald.com/insight/content/doi/10.1108/IJCHM-05-2020-0423/full/html — title, all three
authors in order (Prokopis Christou, Aspasia Simillidou, Maria C. Stylianou), journal, 32(11),
3665–3683, 2020. Exact match on every field.

**FULL TEXT: BLOCKED** — Emerald paywall; the /full/pdf route returns 403.

**WHAT IT ARGUES** (publisher abstract): 78 interviews; tourists favour humanlike robots and see
value in them, while also voicing concern about robots displacing human workers in a
"human-driven" industry; organisations risk appearing impersonal if robots appear to replace staff.
The bib note's "genuinely ambivalent" reading is supported.

**FLAGS:** none.

---

## 2. costanzachock2020design

**Bib entry:** Costanza-Chock, *Design Justice: Community-Led Practices to Build the Worlds We
Need*, MIT Press, 2020, doi:10.7551/mitpress/12255.001.0001.

**IDENTITY: CONFIRMED** via the DOI-resolver record (MIT Press deposit): "Design Justice," Sasha
Costanza-Chock, The MIT Press, published 2020-03-03; the deposit carries the publisher's full
description and the resolver's primary URL is
https://direct.mit.edu/books/book/4605/Design-JusticeCommunity-Led-Practices-to-Build-the (slug
confirms the subtitle). Open-access edition (Knowledge Unlatched funding named in the deposit).

**FULL TEXT: BLOCKED** on every open route tried this pass: direct.mit.edu 403, mitpress.mit.edu
403, design-justice.pubpub.org 403. The book is OA, so this is bot-blocking, not a paywall — a
human with a browser will get it in one click. The card's TravelingWhileTrans body-scanner claim
(readdepth=chapter, verified 2026-08-09) was therefore not re-verified this pass.

**WHAT IT ARGUES** (publisher description, from the deposit): design led by marginalised
communities; universalist design practices erase intersectionally disadvantaged groups under the
matrix of domination; documents community-led design practices grounded in social movements.

**FLAGS:** none on identity. Re-read the Introduction's scanner passage in a browser before proof.

---

## 3. cotter2019visibility

**Bib entry:** Cotter, "Playing the Visibility Game…," *New Media & Society* 21(4), 895–913, 2019,
doi:10.1177/1461444818815684.

**IDENTITY: CONFIRMED** via the DOI-resolver record (SAGE deposit): Kelley Cotter, NM&S 21(4),
895–913; online first 2018-12-14, print April 2019. The bib's 2019 is the print year — correct.

**FULL TEXT: BLOCKED** — journals.sagepub.com returns 403 to both WebFetch and curl.

**WHAT IT ARGUES** (publisher abstract, verbatim in the deposit): thematic analysis of Instagram
influencer discussions; influence-seeking resembles a game built around rules encoded in
algorithms; the closing sentence is "algorithms structure, but do not unilaterally determine user
behavior" — the bib note's altitude quote is genuine and sits in the abstract itself.

**FLAGS:** none.

---

## 4. derrida2000hospitality

**Bib entry:** Derrida & Dufourmantelle, *Of Hospitality*, Stanford University Press, 2000; note
says trans. Rachel Bowlby.

**IDENTITY: CONFIRMED (book-level)** — no DOI exists. Stanford UP's catalog is behind a Vercel
security checkpoint (429) and blocked this pass. Two independent confirmations stand in: (a) the
Internet Archive's scan of the print book (item `ofhospitality0000derr`): "Of hospitality,"
creator Derrida, associated name Dufourmantelle, Stanford, Calif.: Stanford University Press,
2000, ISBNs 0804734054 / 0804734062 / 9780804734066, x + 160 pp; (b) the publisher-deposited
reference list of germannmolz2026 cites it as *Of Hospitality: Anne Dufourmantelle Invites Jacques
Derrida to Respond* (2000). The Bowlby-translator attribution in the note was not re-verified this
pass (the scan's metadata omits the translator).

**FULL TEXT: NOT ATTEMPTED** — print book; the scan is lending-restricted.

**WHAT IT ARGUES:** not characterized this pass (book; prior verification 2026-08-07 stands).

**FLAGS:** minor — the full title carries the subtitle naming Dufourmantelle as interlocutor; the
two-author form the bib uses is the standard citation and is fine.

---

## 5. devito2017folk

**Bib entry:** DeVito, Gergle & Birnholtz, "'Algorithms Ruin Everything': #RIPTwitter, Folk
Theories, and Resistance…," CHI 2017, 3163–3174, doi:10.1145/3025453.3025659.

**IDENTITY: CONFIRMED, one name-form nuance** via the DOI-resolver record (ACM deposit):
CHI 2017 proceedings, pages 3163–3174, three authors in order — but the publisher's current record
gives the first author as **Michael Ann DeVito**, where the bib has "Michael A. DeVito" (the form
on the original printing). ACM has applied its name-change policy to the record. The deposit's
title field carries only the main title ("Algorithms ruin everything"); the subtitle in the bib is
consistent with the known paper.

**FULL TEXT: BLOCKED** — dl.acm.org 403; no author-site copy located (search budget exhausted).

**WHAT IT ARGUES:** not characterized this pass (no abstract in the deposit).

**FLAGS:** decide the name policy once for the whole bibliography: ACM's current record says
"Michael Ann DeVito," and devito2021adaptive elsewhere in the bib will hit the same question.

---

## 6. devos2023einteraction

**Bib entry:** De Vos, Qesja & Lipnickas, "E-Interaction Behaviour and Customer Experience: The
Role of Psychological Comfort," Proc. 2023 Global Fashion Management Conference at Seoul,
doi:10.15444/gmc2023.05.03.04.

**IDENTITY: DIVERGENT** — the DOI-resolver record (GAMMA, the proceedings publisher) confirms the
title, venue (Global Fashion Management Conference, 2023) and DOI, but:
- **Author given names differ:** publisher deposit says **Bora Qesja** and **Ged Lipnickas**; the
  bib says **Blerina** Qesja and **Gintaras** Lipnickas. The same publisher-side names recur on
  the T&F deposit for devos2024disabilities (below), so two independent publishers agree against
  the bib.
- The deposit's page field is **438–438: this is a one-page conference abstract**, not a full
  paper. The bib note leans on it as "an editor's own study" isolating service manner and need
  identification; a one-page abstract cannot carry much.
- The deposit itself is glitchy (an empty first-author slot; "Svetlana De / Vos" mis-split) — the
  publisher's metadata hygiene is poor, so double-check against the printed abstract at proof.

**FULL TEXT: BLOCKED** — gmcproceedings.net serves a self-signed certificate on https and a
JavaScript navigation shell with no article content on http.

**WHAT IT ARGUES:** not characterized (one-page abstract; not retrievable).

**FLAGS:** fix given names (see devos2024disabilities); downgrade evidentiary weight — cite as
conference abstract or drop the load it carries.

---

## 7. devos2024disabilities

**Bib entry:** De Vos, Qesja, Lipnickas & Harris, "Exploring the Higher Education Experiences of
Students Living with Disabilities…," *Journal of Marketing Management* 40(5–6), 450–480, 2024,
doi:10.1080/0267257X.2024.2329090.

**IDENTITY: DIVERGENT — three of four given names are wrong.** The DOI-resolver record (Taylor &
Francis deposit) confirms title, journal, 40(5–6), 450–480, 2024, and gives the authors as:
**Svetlana De Vos, Bora Qesja, Ged Lipnickas, Joanne Harris.** The bib has **Blerina** Qesja,
**Gintaras** Lipnickas, **Jennifer** Harris. This is the exact corrupted-author-list pattern the
project has caught three times before. The wrong names look like invented "expansions" of the real
ones (Bora→Blerina, Ged→Gintaras, Joanne→Jennifer).

**FULL TEXT: BLOCKED** — tandfonline.com 403 to all routes tried.

**WHAT IT ARGUES:** not characterized this pass (no abstract in the deposit); the enchantment /
re-enchantment / disenchantment claim in the note stands on the prior abstract read only.

**FLAGS: MUST FIX the author list.** Spillover: **devos2026strength** and **devosqesja2022journey**
(outside this slice) reuse "Blerina" and "Gintaras" and need the same correction; whoever holds
that slice should verify against the publisher rather than copy this one.

---

## 8. duggan2026tensions

**Bib entry:** Duggan, Dasgupta, McDonnell, Carbery & Sherman, "Tensions in Algorithmic HRM…,"
*IJHRM* 37(8), 1432–1465, 2026, doi:10.1080/09585192.2026.2699267.

**IDENTITY: DIVERGENT on one given name.** The DOI-resolver record (T&F deposit) confirms title,
journal (*The International Journal of Human Resource Management*), 37(8), 1432–1465, 2026, and
four of five authors exactly (James Duggan; Anthony McDonnell; Ronan Carbery; Ultan Sherman). The
second author in the publisher record is **Prakriti Dasgupta**; the bib says **Pritha Dasgupta**.

**FULL TEXT: BLOCKED** — tandfonline.com 403.

**WHAT IT ARGUES:** not characterized this pass (no abstract in the deposit); the
"silence-as-enforced" reading rests on the prior abstract read.

**FLAGS:** fix the given name to Prakriti (publisher-deposited form).

---

## 9. edwardsveale2017slave

**Bib entry:** Edwards & Veale, "Slave to the Algorithm?…," *Duke Law & Technology Review* 16(1),
18–84, 2017, no DOI.

**IDENTITY: CONFIRMED** against the journal's own repository page,
https://scholarship.law.duke.edu/dltr/vol16/iss1/2/ — title, both authors, DL&TR 16(1), 18–84,
2017.

**FULL TEXT: OBTAINED** — repository PDF (974 KB) downloaded and read in part. Title page confirms
authors and affiliations (Edwards, Strathclyde; Veale, UCL). "Transparency fallacy" appears
throughout, including a section heading "Avoiding a 'Transparency Fallacy'" — the note's phrase is
genuine and central.

**WHAT IT ARGUES** (from the full text): a GDPR "right to an explanation" is unlikely to remedy
algorithmic harms — the law is restrictive and unclear on when explanation rights trigger, and ML
explanations may not satisfy the legal conception of "meaningful information about the logic of
processing"; other GDPR instruments (erasure, portability, DPIAs) are the more promising route.

**FLAGS:** none.

---

## 10. ehsan2024seamfulxai

**Bib entry:** Ehsan, Liao, Passi, Riedl & Daumé III, "Seamful XAI…," *PACM HCI* 8(CSCW1), 2024,
doi:10.1145/3637396.

**IDENTITY: CONFIRMED** via the DOI-resolver record (ACM deposit): PACM HCI 8(CSCW1), 2024, pages
1–29, five authors in the bib's order. The deposit writes the last author "Hal Daumé" without the
"III"; the arXiv title page has "HAL DAUMÉ III" — the bib's form is right.

**FULL TEXT: OBTAINED** — arXiv:2211.06753v2 (author's preprint of the CSCW paper; title page and
abstract read, authors and title match the publisher record).

**WHAT IT ARGUES** (publisher abstract + preprint): black-boxing makes the experience seamless but
hiding seams risks disempowering users; seamful design can foster explainability by revealing
sociotechnical mismatches; co-design with 43 practitioners and end-users; revealing seams helped
users foresee AI harms and augmented user agency. The note's "converts seamfulness into an agency
argument" is accurate.

**FLAGS:** none.

---

## 11. eslami2016folk

**Bib entry:** Eslami et al. (7 authors), "First I 'Like' It, Then I Hide It: Folk Theories of
Social Feeds," CHI 2016, 2371–2382, doi:10.1145/2858036.2858494.

**IDENTITY: CONFIRMED** via the DOI-resolver record (ACM deposit): all seven authors in the bib's
exact order (Eslami, Karahalios, Sandvig, Vaccaro, Rickman, Hamilton, Kirlik), CHI 2016, pages
2371–2382.

**FULL TEXT: BLOCKED** — dl.acm.org 403; two UIUC course-site URL guesses returned error stubs.

**WHAT IT ARGUES:** not characterized this pass (no abstract in the deposit).

**FLAGS:** none.

---

## 12. fink2025oversight — publication status settled

**Bib entry:** @techreport, Fink, "Human Oversight under Article 14 of the EU AI Act," SSRN working
paper 5147196, 2025, doi:10.2139/ssrn.5147196.

**IDENTITY: CONFIRMED** via the DOI-resolver record: SSRN posted-content, Melanie Fink, posted 2025
(record created 2025-04-22), resolving to https://www.ssrn.com/abstract=5147196. A **second SSRN
posting of the same paper exists** (abstract 5146118, doi:10.2139/ssrn.5146118, created one day
earlier); the bib's number is valid, the duplicate is just SSRN noise.

**PUBLICATION STATUS:** the paper's own title page (full text, below) states: "Forthcoming in:
Gianclaudio Malgieri, Gloria González Fuster, Alessandro Mantelero, and Gabriela Zanfir-Fortuna
(eds), *AI Act Commentary: A Thematic Analysis* (Hart-Bloomsbury, forthcoming 2026)." So it is a
**book chapter in press**, not a journal article, and as of this audit no published version has
appeared that I could verify (Bloomsbury's site blocks fetches; no library record checked). The
"working paper — do not let it carry a claim alone" rule should stay until the chapter is out;
at proof, cite as chapter-in-press if the volume has appeared.

**FULL TEXT: OBTAINED** — 16-page PDF via the AI Governance Library's hosted copy
(aigouvernance.com); identity of the copy checked against the SSRN record (title, author,
affiliations). Roughly half read closely (title page, §§1–2, §§5–7).

**WHAT IT ARGUES** (from the full text): Article 14 requires that high-risk AI systems can be
"effectively overseen by natural persons"; Fink organises the obligations under three markers —
authority, comprehension, environment; "a *pro forma* human that 'rubber-stamps' the AI system's
output does not meet this criterion" (p. 3, her words); oversight is not a panacea, its
limitations especially affect output-oriented goals, while process-oriented goals ("provide 'the
ear' necessary to safeguard the right to be heard," p. 14) are more attainable.

**FLAGS:**
1. **The bib note misattributes "liability sponges."** In the paper the phrase is quoted from
   Crootof, Kaminski and Nicholson Price II ('Humans in the Loop' (2023) 76 Vanderbilt Law Review
   429, at 483 — her fn 77): overseers "risk becoming 'liability sponges', taking 'the fall' when
   things go wrong without having the corresponding agency that justifies responsibility." If the
   manuscript uses the phrase, credit Crootof et al., via Fink.
2. The note's "four-part test" language belongs to sterz2024effectiveness, not Fink — the notes
   currently keep them straight; keep it that way.
3. Update the entry when the Hart-Bloomsbury volume lands.

---

## 13. folger1977voice — see the closing section below for the full verdict.

**Bib entry:** Folger, "Distributive and Procedural Justice: Combined Impact of 'Voice' and
Improvement on Experienced Inequity," *JPSP* 35(2), 108–119, 1977, doi:10.1037/0022-3514.35.2.108.
Note claims: "Voice reduces experienced injustice independent of outcome."

**IDENTITY: CONFIRMED** via the DOI-resolver record (APA deposit): exact title, sole author Robert
Folger, *Journal of Personality and Social Psychology* 35(2), 108–119, February 1977. Every
bibliographic field in the bib entry is right.

**FULL TEXT: BLOCKED** — full route list and the claim verdict in the closing section.

**FLAGS:** the `claim-contradicted` flag on the card **stands**; the §7 sentence must not survive
to submission in its current form. Details below.

---

## 14. fuller1991consumers

**Bib entry:** Fuller & Smith, "Consumers' Reports: Management by Customers in a Changing
Economy," *Work, Employment and Society* 5(1), 1–16, 1991, doi:10.1177/0950017091005001002.

**IDENTITY: CONFIRMED** via the DOI-resolver record (SAGE deposit): both authors, WES 5(1), 1–16,
March 1991.

**FULL TEXT: BLOCKED** — journals.sagepub.com 403.

**WHAT IT ARGUES** (publisher abstract, in the deposit): managers use customer feedback to monitor,
evaluate and discipline service workers; management by customers may deepen and complicate
authority relations and give rise to new forms of workplace conflict. The note's
"origin of management-by-customers as a labour-control concept" is exactly what the abstract says.

**FLAGS:** none.

---

## 15. gaothebault2026townie

**Bib entry:** "Gao, Zhaoyi and Thebault-Spieker, Jacob," "Is Your Chatbot a Tourist or a
Townie?…," *PACM HCI*, 2026, doi:10.1145/3788058.

**IDENTITY: DIVERGENT — first author's given name is wrong.** The DOI-resolver record (ACM
deposit) gives the authors as **Zihan Gao** and Jacob Thebault-Spieker; the bib says **Zhaoyi**
Gao. The record also supplies the missing volume/issue: PACM HCI **10(2)** (CSCW, article
CSCW022), pp. 1–45, 2026. (The deposit's title field carries a trailing "CSCW022" artifact —
publisher noise, not a title change.)

**FULL TEXT: BLOCKED** — dl.acm.org 403; no arXiv version found via the arXiv export API.

**WHAT IT ARGUES** (publisher abstract, in the deposit): benchmark of 12,000+ QA pairs on local
knowledge; the finding is a **dual, context-dependent geographic bias** — an "urban advantage" in
formal news contexts but an "urban penalty" on social-media data — plus a domain bias: models
handle concrete physical questions but "consistently struggle to capture the nuanced relational
and cognitive dimensions of a community."

**FLAGS:** (1) fix the given name to Zihan; add volume 10, issue 2 (CSCW). (2) The bib note's flat
"LLMs carry an urban advantage" is half the finding — the abstract's own claim is a dual bias. The
half the manuscript leans on (failure on relational, community-held knowledge) **is** supported
verbatim; just don't restate the urban-advantage half without the news-context qualifier.

---

## 16. garcia2026strategic

**Bib entry:** Garcia, Tolvanen & Wagner, "Strategic Responses to Algorithmic Recommendations:
Evidence from Hotel Pricing," *Management Science* 72(1), 609–626, 2026,
doi:10.1287/mnsc.2022.03740.

**IDENTITY: CONFIRMED** via the DOI-resolver record (INFORMS deposit): title, three authors in
order, MS 72(1), 609–626, January 2026. Exact match. Special issue on the Human-Algorithm
Connection (Ockenfels).

**FULL TEXT: BLOCKED** — pubsonline.informs.org 403.

**WHAT IT ARGUES** (publisher abstract, in the deposit): high-resolution hotel-pricing data;
price-adjustment costs of human decision makers create a conflict of interest with the algorithmic
advisor; in equilibrium the algorithm's recommendations are **strategically biased** and lead to
suboptimal pricing; a structural model quantifies the losses and estimates the benefits of a shift
to fully automated pricing.

**FLAGS:** framing caution for claim 9. The note's reading — "recommendations are written in
anticipation of deviation" — is supported (that is the strategic bias). But the paper's own
punchline runs the other way: persistent human discretion is a *cost*, and full automation would
do better. Cite it for the fact of persistent discretion, not as an endorsement of discretion.

---

## 17. germannmolz2026 — the §1 question settled

**Bib entry:** Germann Molz, "Guests without Hosts: On the Digital Biopolitics of Network
Hospitality," *Hospitality & Society* 16(1), 63–82, 2026, doi:10.1386/hosp_00107_1.

**IDENTITY: CONFIRMED** via the DOI-resolver record (Intellect deposit): sole author Jennie
Germann Molz (College of the Holy Cross), H&S 16(1), 63–82, print 2026-03-01. Exact match.

**FULL TEXT: BLOCKED** — intellectdiscover.com 403 on both the article page and the crawler-PDF
link the deposit itself lists. The "full text still owed" debt in the bib note remains open.

**WHAT IT ARGUES** (publisher abstract, verbatim in the deposit — this settles the pivot
question): the phrase was "**Originally conceived to describe the blurring of hosting and guesting
practices in network hospitality**," and "is now devastatingly suited to more recent images of
travellers stranded by disasters and pandemics, unwelcome strangers at the border or the
replacement of human hospitality workers with robots and AI." She then reads the concept **from
two directions**: "an inhospitable form of institutional and algorithmic governance that
constrains hosts and guests in extractive relations" *and* "a potential model of collaborative
sociality through which we might imagine and enact alternative futures," through two figures (the
*absent Superhost*, the *mobile neighbour*), "to consider the digital biopolitics involved in
visibilizing, (self-)disciplining and **erasing hosts**."

**FLAGS:** the manuscript's §1 pivot, if it rests on "guests without hosts = erasure," overreads
the source. Erasure is one of three biopolitical operations in one of two readings; the phrase's
origin is the *blurring* of hosting and guesting, and half the article is affirmative (collaborative
sociality). The bib note's differentiation ("she asks what becomes of hospitality when the host is
erased") survives only in weakened form — she also asks what hostless hospitality makes possible.
Rewrite the pivot to credit the blurring origin and the dual reading; the erasure strand can still
carry the paper's question about whether the successor inherits the obligation.

---

## 18. goodwin1992consumer

**Bib entry:** Goodwin & Ross, "Consumer Responses to Service Failures…," *Journal of Business
Research* 25(2), 149–163, 1992, doi:10.1016/0148-2963(92)90014-3.

**IDENTITY: CONFIRMED** via the DOI-resolver record (Elsevier deposit): both authors, JBR 25(2),
149–163, September 1992.

**FULL TEXT: BLOCKED** this pass — Elsevier/ScienceDirect not open. The bib note records
readdepth=full-archived from 2026-08-09; nothing found today contradicts the note's content claim
(voice without tangible offering associated with lower fairness in some conditions), but I could
not re-read it.

**WHAT IT ARGUES:** not characterized this pass (no abstract in the deposit).

**FLAGS:** none. As the designated "conditionality" leg of the repaired Folger argument it is
bibliographically sound.

---

## 19. gursoy2026reconceptualizing

**Bib entry:** Gursoy, "Reconceptualizing Customer Experience Co-Creation and Service Delivery in
the Age of Artificial Intelligence," *JHMM* 35(2), 151–165, 2026, doi:10.1080/19368623.2025.2611513.

**IDENTITY: CONFIRMED** via the DOI-resolver record (T&F deposit): sole author Dogan Gursoy, JHMM
35(2), 151–165; online 2026-01-06, in the print issue 2026-02-17. The bib's year and the note's
"in print Feb 2026" are both right.

**FULL TEXT: BLOCKED** — tandfonline.com 403; no abstract in the deposit either.

**WHAT IT ARGUES:** not characterized this pass. **The note's own instruction — "Obtain full text
before revising" §3 — remains unmet**, and this is the source the notes call THE THREAT. It is the
one identity-confirmed source in this slice whose content the project still knows only from one
abstract read.

**FLAGS:** unread must-engage source; needs a library pull, not another crawl.

---

## 20. hatherley2025moving

**Bib entry:** Hatherley, "A Moving Target in AI-Assisted Decision-Making…," *Ethics and
Information Technology* 27, article 20, 2025, doi:10.1007/s10676-025-09829-2.

**IDENTITY: CONFIRMED** via the DOI-resolver record (Springer deposit): sole author, EIT volume
27, **issue 2**, article number 20, online 2025-04-04, print June 2025. The bib's "pages = 20" is
the article number — add issue 2 if the reference style wants it.

**FULL TEXT: not fetched** — the deposit carries the full abstract and the bib records an arXiv
mirror (2504.05210); Springer access was not tested. Low-risk.

**WHAT IT ARGUES** (publisher abstract, in the deposit): model updating introduces a distinct
sub-type of opacity — update opacity — "when users cannot understand how or why an update has
changed the reasoning or behaviour of an ML system"; available black-box solutions are
"largely ill-equipped to address" it; candidate strategies (bi-factual explanations, dynamic model
reporting, update compatibility) each carry limits. The bib note is an accurate compression.

**FLAGS:** none.

---

## 21. hemmer2025complementarity

**Bib entry:** "Hemmer, Patrick and Schemmer, Max and Vössing, Michael and Kühl, Niklas,"
"Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence," *EJIS*, 2025,
doi:10.1080/0960085X.2025.2475962.

**IDENTITY: DIVERGENT — the bib is missing an author.** The DOI-resolver record (T&F deposit)
lists **five** authors: Patrick Hemmer, Max Schemmer, Niklas Kühl, Michael Vössing, **Gerhard
Satzger** — the bib has four, omits Satzger, and orders Vössing before Kühl. The arXiv v2 title
page (read directly) also has five authors including Satzger, so even the preprint the bib note
cites (arXiv:2404.00029) contradicts the bib's list. The deposit also supplies the now-assigned
issue data the bib lacks: **EJIS 34(6), 979–1002**, online 2025-08-27, print November 2025.

**FULL TEXT: OBTAINED** — arXiv:2404.00029v2 (title page and abstract read; identity checked
against the publisher record).

**WHAT IT ARGUES** (preprint full text, abstract): complementary team performance (CTP) — a level
neither human nor AI attains alone — has rarely been observed; the paper formalises
complementarity's theoretical potential versus realised effect and identifies **information
asymmetry and capability asymmetry** as the two sources, illustrated in two empirical studies. The
note's differentiation (ex-post performance test over internal decision tasks, no answerability to
an outside party) is consistent with what I read.

**FLAGS: MUST FIX** — add Satzger, restore publisher order (Hemmer, Schemmer, Kühl, Vössing,
Satzger), add 34(6), 979–1002.

---

# Summary table

| # | citekey | Identity | Full text | Divergences / flags |
|---|---------|----------|-----------|---------------------|
| 1 | christou2020tourists | CONFIRMED (Emerald page) | BLOCKED (paywall) | — |
| 2 | costanzachock2020design | CONFIRMED (DOI resolver) | BLOCKED (bot-blocks on an OA book) | re-check scanner passage in a browser |
| 3 | cotter2019visibility | CONFIRMED (DOI resolver) | BLOCKED (SAGE 403) | — |
| 4 | derrida2000hospitality | CONFIRMED (book scan; SUP site blocked) | not attempted | translator not re-verified |
| 5 | devito2017folk | CONFIRMED (DOI resolver) | BLOCKED (ACM 403) | publisher now lists "Michael Ann DeVito" |
| 6 | devos2023einteraction | **DIVERGENT** (given names) | BLOCKED (dead publisher site) | one-page abstract; Bora not Blerina, Ged not Gintaras |
| 7 | devos2024disabilities | **DIVERGENT** (3 of 4 given names) | BLOCKED (T&F 403) | Bora Qesja, Ged Lipnickas, Joanne Harris — fix; spillover to 2 entries outside slice |
| 8 | duggan2026tensions | **DIVERGENT** (1 given name) | BLOCKED (T&F 403) | Prakriti not Pritha Dasgupta |
| 9 | edwardsveale2017slave | CONFIRMED (journal repository) | **OBTAINED** (read in part) | — |
| 10 | ehsan2024seamfulxai | CONFIRMED (DOI resolver) | **OBTAINED** (arXiv) | — |
| 11 | eslami2016folk | CONFIRMED (DOI resolver) | BLOCKED (ACM 403) | — |
| 12 | fink2025oversight | CONFIRMED (DOI resolver) | **OBTAINED** (hosted copy, read) | chapter in press, Hart-Bloomsbury 2026; "liability sponges" is Crootof et al.'s phrase; duplicate SSRN id 5146118 |
| 13 | folger1977voice | CONFIRMED (DOI resolver) | BLOCKED (APA; all routes) | **claim-contradicted stands** — see below |
| 14 | fuller1991consumers | CONFIRMED (DOI resolver) | BLOCKED (SAGE 403) | — |
| 15 | gaothebault2026townie | **DIVERGENT** (given name) | BLOCKED (ACM 403; no arXiv) | Zihan not Zhaoyi Gao; add 10(2); dual-bias nuance |
| 16 | garcia2026strategic | CONFIRMED (DOI resolver) | BLOCKED (INFORMS 403) | paper favours full automation — framing caution |
| 17 | germannmolz2026 | CONFIRMED (DOI resolver) | BLOCKED (Intellect 403) | **phrase coined for blurring, dual reading — §1 pivot overreads "erasure"** |
| 18 | goodwin1992consumer | CONFIRMED (DOI resolver) | BLOCKED (Elsevier) | — |
| 19 | gursoy2026reconceptualizing | CONFIRMED (DOI resolver) | BLOCKED (T&F 403) | THE THREAT is still unread — library pull needed |
| 20 | hatherley2025moving | CONFIRMED (DOI resolver) | not fetched (abstract in deposit; arXiv exists) | add issue 2 |
| 21 | hemmer2025complementarity | **DIVERGENT** (missing author) | **OBTAINED** (arXiv) | add Gerhard Satzger; fix order; add 34(6), 979–1002 |

Counts: 16 identity-confirmed, 5 divergent (all on author fields), 0 unconfirmed. Full text
obtained for 4; blocked for 15; not attempted/not needed for 2. Every divergence in this slice is
an author-name or author-count error, and every one was caught only at the publisher record —
which is the pattern the audit rule predicted.

---

# folger1977voice — what is established, and on what evidence

**The bibliographic identity is settled.** The DOI resolver returns the APA-deposited record:
Robert Folger (sole author), "Distributive and procedural justice: Combined impact of voice and
improvement on experienced inequity," *Journal of Personality and Social Psychology* 35(2),
108–119, February 1977, PsycNet record 1977-27495-001. Every field in the bib entry matches.

**The full text remains unobtained.** Routes tried this pass, all failed, listed so nobody repeats
them: APA PsycNet article page (renders a JavaScript loading shell to WebFetch; 403 to curl);
doi.apa.org landing (403); the publisher PDF link embedded in the Crossref deposit,
psycnet.apa.org/journals/psp/35/2/108.pdf (403); the PsycNet internal JSON API (endpoint exists,
rejects guessed method names); academia.edu, which hosts what appears to be a scan (403 to both
WebFetch and curl); ResearchGate (excluded by rule and blocked anyway); PubMed (the article is not
indexed); Google Books API (no snippets); archive.org search-inside on the Lind & Tyler 1988 book
(403, lending-protected); the UNO master's thesis on the frustration effect at
digitalcommons.unomaha.edu (bepress bot-check returns 202/empty); CORE work page (403). Prior
passes had already exhausted Unpaywall, OpenAlex, Semantic Scholar, CORE, OpenAIRE and Internet
Archive. **The one realistic remaining route is Bentley library access to APA PsycArticles**, or
the academia.edu scan opened in a signed-in browser.

**What the claim audit establishes without the full text.** Two evidence classes, stated in order
of strength:

1. **Read directly from an original peer-reviewed article** (not a summary): Lind, Kanfer & Earley
   1990, "Voice, Control, and Procedural Justice," *JPSP* 59(5), 952–959 — obtained as a scan of
   the printed article from an MIT course server and read. It classifies Folger 1977, with Folger
   et al. 1979 and Folger, Rosenfield & Robinson 1983, as "studies of what is termed the
   frustration effect," experiments which "showed that people react quite negatively to ostensibly
   high voice procedures" when outcomes or communications focus attention on possible bias. The
   same article separately cites Folger 1977 as evidence that "the voice effect enhances
   procedural fairness even when the individual making the fairness judgment has no direct control
   over the decision itself." So the procedural-justice literature itself, in print, reads Folger
   1977 as carrying *both* results the card describes: a positive voice effect on the
   process-satisfaction measure, and a frustration effect on outcome evaluations.

2. **Abstract-shaped text, secondary, consistent across four independent retrievals** (two in the
   2026-08-08 card pass, two today): the design is 3 factors (inequity/equity × voice/mute ×
   constant/improve) on sixth-grade boys in a card-sorting task, and on outcome fairness "a pay
   sequence that improved after voice was perceived as less fair than the same sequence that
   improved without voice, while a constant sequence was perceived more fair given voice than no
   voice," chiefly in the inequity conditions, with the procedural-satisfaction effect on a
   separate measure. This text has the exact shape of the APA abstract and never varies across
   retrievals, but under this project's rule it remains a lead, not a source.

**Verdict.** The manuscript's §7 sentence — that Folger found voice reduces experienced injustice
*independently of whether the outcome improved* — is contradicted by every piece of evidence
reachable, and supported by none. Independence is an interaction away from what the study is cited
*for* in the later literature: on outcome fairness the 1977 result is a voice × improvement
interaction whose improve cell runs in the *reverse* direction (the frustration effect), and the
outcome-independent finding the manuscript wants lives in the *procedural-satisfaction* measure
and, cleanly, in Lind, Kanfer & Earley 1990 — which the bib already holds as the designated repair
anchor, and whose post-decision-voice result I verified today against the article's own text
("Both pre- and postdecision voice led to higher fairness judgments than no voice"). The
`claim-contradicted` flag stands. The safe repair is the one the card drafts: cite Folger 1977 for
voice raising satisfaction with the allocation process itself while *interacting* with improvement
on outcome fairness, and move the outcome-independence weight onto lind1990 (and the
conditionality onto goodwin1992consumer). The current sentence must not reach a referee: this is
the one citation in §7 a procedural-justice reviewer will know by heart, the strength of my
correction is "original 1990 JPSP article read in full plus a four-times-consistent abstract
trace," and the residual risk — that the actual 1977 results section somehow supports independence
against its own abstract and thirty years of citation practice — is small but nonzero until
someone reads pages 108–119 through the library.
