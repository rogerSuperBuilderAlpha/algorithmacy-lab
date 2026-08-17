# Source-side audit — slice 06 (20 citekeys)

Audit date: 2026-08-17. Auditor: source-verification agent, run against
`literature/references.bib`. Binding rule applied: identity counts as verified only against the
publisher's own record or the DOI resolver (Crossref REST API, the registration agency behind
doi.org, whose metadata is deposited by the publisher). Full-text copies were taken from
publisher pages, author or institutional repositories, and author-hosted sites; every route,
successful or failed, is named per entry.

Access environment for this run: the Chrome browser extension was not connected, so all
publisher sites fronted by Cloudflare bot protection returned 403 to every client available
(WebFetch, curl with browser UA, jina reader — itself 401 on this network). That blocked
**dl.acm.org, onlinelibrary.wiley.com, intellectdiscover.com, journals.sagepub.com,
tandfonline.com, pubsonline.informs.org, researchgate.net, research.tudelft.nl file downloads,
and scispace.com**. Emerald, arXiv, Wayback Machine, MIT DSpace, RUG Pure, KCL Pure, UCF STARS,
Maastricht CRIS, Tech Solidarity Lab, and authors' personal sites were reachable. Do not re-try
the blocked hosts with curl/WebFetch; they need a real browser session.

Headline: **six corrupted author lists** in this slice (shabnam2026tpsr, schmidt2025field,
shi2025residents, spektor2025working, xing2026algorithmic, zhou2025competency), every one a
given-name substitution with family names and author order intact — the same signature as the
three fabrications this project caught before. One phantom volume/issue (shabnam2026tpsr).

---

## 1. riordan2024digitally

**Bib entry:** Riordan, Tyler, "Digitally Mediated Hospitality and Algorithmic Hostility in the
Platform Economy…", *Hospitality & Society* 14(3), 277–299, 2024, doi:10.1386/hosp_00083_1.

**IDENTITY: CONFIRMED** — Crossref DOI record (https://api.crossref.org/works/10.1386/hosp_00083_1):
Tyler Riordan (sole author, ORCID-authenticated, University of Queensland), *Hospitality &
Society* 14(3), 277–299, published 2024-09-01, Intellect. Exact match on every field.

**FULL TEXT: BLOCKED** — intellectdiscover.com 403 (Cloudflare); Unpaywall: not OA, no
repository deposit; a ResearchGate copy exists but RG also 403s non-browser clients.

**WHAT IT ARGUES** *(from the Crossref-deposited publisher abstract)*: Multi-sited ethnography
(participant observation incl. bicycle shadowing, plus semi-structured interviews) of
platform-based food-delivery workers, predominantly migrants. Maps their interactions onto
Lashley's commercial/private/social domains, documents digital interactions beyond them, and
proposes a new **virtual domain** at the threshold of material and virtual contexts, alongside
algorithmic hostility as hospitality's counter-concept.

**FLAGS:** None on identity. The bib note's usage rule (cite as the concept this paper extends,
sector is food delivery, not hotel evidence) matches the abstract.

---

## 2. schmidt2025field

**Bib entry:** "Schmidt, Anne Lise and Koerten, Kaj and Tuomi, Aarni and El-Manstrly, Dahlia and
Wiegerink, Karoline", *Strategic Change* 34(4), 559–575, 2025, doi:10.1002/jsc.2637.

**IDENTITY: DIVERGENT** — Crossref DOI record (10.1002/jsc.2637): authors are **Alexander
Lennart Schmidt** (Hotelschool The Hague, ORCID 0000-0003-3354-6053), **Klaas Koerten**
(Hotelschool The Hague / TU Delft), Aarni Tuomi, Dahlia El-Manstrly, Karoline Wiegerink.
- Bib "Anne Lise Schmidt" → publisher **Alexander Lennart Schmidt** (wrong given names).
- Bib "Kaj Koerten" → publisher **Klaas Koerten** (wrong given name).
- Title, journal, 34(4) 559–575, print July 2025 (online 2025-01-31): all match.

**FULL TEXT: BLOCKED** — the published PDF is free at
onlinelibrary.wiley.com/doi/pdfdirect/10.1002/jsc.2637 (Unpaywall: publisher publishedVersion)
but Wiley's Cloudflare 403s every non-browser client. Trivially obtainable in a browser session.

**WHAT IT ARGUES** *(from the Crossref-deposited publisher abstract)*: Field experiment in a
real hotel, 200 participants, human and robotic service agents **simultaneously available** at
the information-provision touchpoint; finds **indifferent effects** between human and robot on
guests' experience of hospitality, satisfaction, and revisit intentions, challenging assumptions
from hypothetical-scenario studies. The bib note's substance (rare field experiment, disciplines
over-reading of kim2021preference) is supported.

**FLAGS:** Corrupted author list — fix to `Schmidt, Alexander Lennart and Koerten, Klaas and …`.

---

## 3. scottorlikowski2012accountability

**Bib entry:** Scott, Susan V. and Orlikowski, Wanda J., *Accounting, Organizations and Society*
37(1), 26–40, 2012, doi:10.1016/j.aos.2011.11.005.

**IDENTITY: CONFIRMED** — Crossref DOI record: Susan V. Scott, Wanda J. Orlikowski, AOS 37(1)
26–40, January 2012, Elsevier. Exact match.

**FULL TEXT: OBTAINED** — author submitted version from MIT DSpace
(dspace.mit.edu/handle/1721.1/108306, bitstream download; ~11,250 words). ScienceDirect itself
403s.

**WHAT IT ARGUES** *(from full text, submitted version)*: Using TripAdvisor in the travel
sector, the paper shows how a social-media rating apparatus **materializes a new relation of
accountability** — anonymous, algorithmically ranked traveler reviews displace professionally
audited accountability schemes, reconfiguring who answers to whom. Grounding for the
manuscript's triad-in-this-sector claim is solid.

**FLAGS:** None.

---

## 4. shabnam2026tpsr

**Bib entry:** "Shabnam, Sadia and Roy, Sanjit Kumar and Roten, Yves Sabbah and Singh, Gurmeet
and Suh, Taewon and Li, Hongfei", *Journal of Services Marketing* **40(4)**, 1–17, 2026,
doi:10.1108/JSM-09-2025-0679.

**IDENTITY: DIVERGENT** — verified against **both** the live Emerald publisher page
(emerald.com/jsm/article/doi/10.1108/JSM-09-2025-0679/1385027/) and Crossref. Publisher authors,
in order: **Saadia Shabnam** (Curtin), **Sanjit K. Roy** (Edith Cowan), **Yonathan Silvain
Roten** (EM Normandie), **Gaganpreet Singh** (O.P. Jindal), **Taewon Suh** (Texas State),
**Hairong Li** (Michigan State). Divergences:
- "Sadia" → **Saadia** Shabnam.
- "Yves Sabbah Roten" → **Yonathan Silvain Roten** (entirely different given names).
- "Gurmeet Singh" → **Gaganpreet Singh** (different person's name; Gurmeet Singh is a real,
  different services scholar in Fiji — this is how fabricated lists survive spot checks).
- "Li, Hongfei" → **Hairong Li**.
- Volume/issue: bib says **40(4)**; publisher and Crossref both say **ahead-of-print, no volume,
  no issue** (online 2026-07-03, pp. 1–17). The bib note's "VOLUME CORRECTED 39->40 in
  verification sweep" has no publisher basis — both numbers appear invented. Only "Suh, Taewon"
  and the family names survive contact with the record.

**FULL TEXT: OBTAINED** — the article is CC BY 4.0 and the full text is served on the Emerald
page (read via WebFetch against the publisher page).

**WHAT IT ARGUES** *(from publisher full text)*: Conceptual paper integrating activity theory
with transformative service research and phygital service research. Transformative outcomes in
phygital environments arise from interactions among artefacts, governance rules, communities and
labour divisions; five testable propositions; no original empirical evidence. It **does state
the gap the manuscript cites it for**, verbatim: "existing frameworks do not explain how
algorithmic systems autonomously redirect, constrain or reconfigure agency through decision
automation and behavioural nudging." And it **does not critique smoothness** — it critiques
opacity, governance rigidity, and engagement-optimisation framing, exactly as the bib note says.

**FLAGS:** Worst entry in the slice: four corrupted given names plus a phantom volume/issue.
Cite as ahead-of-print until Emerald assigns an issue. The corrupted list is also in any
rendered reference list that inherits the bib.

---

## 5. shi2025residents

**Bib entry:** "Shi, Fang and Han, Xiaonan and Samaniego-Chávez, Carlos Eduardo", *Journal of
Travel Research* 64(4), 950–965, 2025, doi:10.1177/00472875231224238.

**IDENTITY: DIVERGENT** — Crossref DOI record: **Fangfang Shi** (ORCID 0000-0001-8176-4712,
Dongbei University of Finance and Economics), **Xing Han** (Dalian University), **Carla
Estefanía Samaniego-Chávez** (Dongbei UFE). Three of three given names wrong:
- "Fang" → **Fangfang** Shi.
- "Xiaonan" → **Xing** Han.
- "Carlos Eduardo" → **Carla Estefanía** Samaniego-Chávez (the fabrication even swapped the
  author's gendered given name).
- JTR 64(4) 950–965, print April 2025 (online 2024-01-31): match.

**FULL TEXT: BLOCKED** — Sage 403; Unpaywall: no OA location.

**WHAT IT ARGUES** *(from the Crossref-deposited publisher abstract)*: Develops and validates
the residents' perceived benefits scale (RPBS) for host–guest interaction — 52 interviews plus
two resident surveys; five dimensions (emotional lift, local pride, altruism, destination
attraction, self-development); benefits predict interaction intention. The bib note's narrowing
(host is a destination resident, construct is a benefit accruing to the host, no commercial
service relation) is consistent with the abstract.

**FLAGS:** Fully corrupted given-name set; fix all three.

---

## 6. spektor2023designing

**Bib entry:** Spektor, Franchesca; Fox, Sarah E.; Awumey, Ezra; Riordan, Christine A.; Rho, Hye
Jin; Kulkarni, Chinmay; Martinez-Lopez, Marlen; Stringam, Betsy; Begleiter, Ben; Forlizzi, Jodi.
DIS '23, pp. 623–637, doi:10.1145/3563657.3596018. Note claims readdepth=full.

**IDENTITY: CONFIRMED** — Crossref DOI record: all 10 authors, in the bib's exact order; DIS '23
proceedings, pp. 623–637, published 2023-07-10, ACM. (Crossref renders "Sarah E" without the
period; not a divergence.)

**FULL TEXT: OBTAINED** — author-lab PDF from Tech Solidarity Lab
(techsolidaritylab.com/assets/pdfs/Spektor et al-Designing_for_Wellbeing_DIS23.pdf), camera-ready
ACM version, ~13,700 words, read in full. dl.acm.org itself (page and gold-OA PDF) 403s.

**WHAT IT ARGUES** *(from full text)*: Workshops, interviews, and participatory prototyping with
**unionized guest room attendants (GRAs) — "known more colloquially as housekeepers" (the
paper's own footnote 2)** — around "UpKeep" (pseudonym), an algorithmic manager "widely deployed
in hotels to coordinate guest room attendants (GRAs) and supervisors in housekeeping service…
used to order room cleaning assignments, and mediate digital communication and task allocation
between GRAs and other departments." Worker-generated redesigns organized around self-efficacy,
transparency, and workload. See the Spektor findings section below for the mechanics.

**FLAGS:**
1. **Internal contradiction on read depth.** The bib note says `readdepth=full`; the only card
   for this paper (`library/cards/spektor2023dis.md`) says `read_depth: abstract`, `status:
   rejected`, "Not admitted to the bibliography." There is no card under the citekey
   `spektor2023designing` at all. One of the two records is wrong; the library and bib disagree
   about whether this load-bearing source was ever read before today.
2. **The bib note overstates the rejection affordance** ("offers an in-app rejection workers
   cannot use without fearing dismissal"). In the paper, display-as-rejectable-request was a
   *participant-proposed prototype concept*; Session 2 feedback was that "GRAs could not
   realistically assert in-app rejections without fear of termination." UpKeep as deployed does
   not offer rejection. `manuscript.md` line ~60 ("offering a rejection affordance that workers
   feared to use") and line ~268 repeat the error.
3. **Task-list withholding is mislocated.** `manuscript.md` (~line 267): "withheld the day's
   full task list under common configurations." The paper says the opposite about prevalence:
   "many did allow GRAs to see their whole board. Only in the most limited configurations, GRAs
   were instead shown one assignment at a time." What most configurations withheld was
   **self-sequencing** ("almost none… allowed for self-sequencing"), not the list itself.
4. Credits: supported — rooms carry credit values, and workers imagined credit records feeding
   union grievance hearings and contract negotiations ("contractual credits" is a fair gloss).

---

## 7. spektor2025working — priority item

**Bib entry:** "Spektor, Franchesca and Fox, Sarah E. and **Min, Susan** and **Sarfo, Gabriel**
and Stringam, Betsy and Riordan, Christine A. and Rho, Hye Jin and Begleiter, Ben and Forlizzi,
Jodi", DIS '25, pp. 3221–3234, doi:10.1145/3715336.3735704. Note: "ACM returned 403… OBTAIN
BEFORE CITING… readdepth=metadata."

**IDENTITY: DIVERGENT** — verified against **two** publisher-side records: the Crossref DOI
record and a Wayback Machine snapshot (2025-07-19, HTTP 200) of ACM's own dl.acm.org page. Both
give, in order: Franchesca Spektor (CMU), Sarah E Fox (CMU), **Somang Min** (New Mexico State),
**Grace Sarfo** (New Mexico State), Betsy Stringam (NMSU School of Hotel, Restaurant…),
Christine A. Riordan (UIUC), Hye Jin Rho (MSU), Ben Begleiter (UNITE HERE), Jodi Forlizzi (CMU).
- Bib "Min, Susan" → publisher **Somang Min**.
- Bib "Sarfo, Gabriel" → publisher **Grace Sarfo**.
- Author count (9), order, venue, pages 3221–3234, year 2025: all match.
The never-obtained source has a corrupted author list — consistent with the entry having been
built from a secondary index, exactly the failure mode the project has caught three times. The
corruption is already propagated into `manuscript/DRAFT.md` (line ~787) and
`manuscript/SHORT_DRAFT.md` (lines ~140, ~203) reference lists.

**FULL TEXT: BLOCKED** — routes tried, all named: dl.acm.org page and /doi/pdf/ (403 via
WebFetch and via curl with browser UA; the paper is gold OA at ACM per Unpaywall, but Cloudflare
gates it); jina.ai reader proxy (401, network reputation); Chrome extension (not connected);
Unpaywall (only ACM's own PDF listed, no repository deposit); OpenAlex locations (same);
Semantic Scholar (paper not indexed); Tech Solidarity Lab publications page (stale — lists only
through CSCW 2025 preprints, not this paper); franchescaspektor.com (unreachable); figshare
search (empty); targeted web searches for any PDF (none); Wayback CDX for the PDF URL (no
snapshot). **The "OBTAIN BEFORE CITING" condition remains unresolved: no full text exists
outside ACM's blocked DL.** A browser session on dl.acm.org would likely get it (DIS '25 is open
access there).

**WHAT IT ARGUES** *(publisher abstract, from the archived ACM page — marked: abstract only)*:
"Algorithmic management is transforming traditional face-to-face service sectors like
hospitality… we conducted an interview study in a unionized, mid-sized urban hotel on the West
Coast of the USA… we examine how an algorithmic management (AM) platform mediates work in **a
housekeeping department**. Our analysis highlights the effects of AM on social processes,
revealing that despite careful configuration, the tool's implementation still challenges
traditional communication and coordination… We offer design opportunities for flexible workplace
technologies that support, rather than frustrate, the relational aspects of service work."

**FLAGS:** (1) Corrupted given names for authors 3 and 4, in bib and both draft reference lists.
(2) Still cited without any full-text read anywhere in the project; no card exists. (3) The
study population is **back-of-house housekeeping**, not front-desk or guest-staff interaction —
see the settlement section below.

---

## 8. starruhleder1996infrastructure

**Bib entry:** Star & Ruhleder, *Information Systems Research* 7(1), 111–134, 1996,
doi:10.1287/isre.7.1.111.

**IDENTITY: CONFIRMED** — Crossref DOI record: Susan Leigh Star, Karen Ruhleder, ISR 7(1)
111–134, March 1996, INFORMS. Exact match.

**FULL TEXT: BLOCKED** — pubsonline.informs.org 403; Unpaywall: not OA; scispace mirror 403; the
MIT Press *Boundary Objects and Beyond* chapter reprint (direct.mit.edu chapter-pdf) also 403.
Course-hosted copies exist but none reachable from this run's clients.

**WHAT IT ARGUES:** Not characterized in this audit — no publisher abstract in the Crossref
record and no full text obtained. (The bib note's gloss — infrastructure becomes effective as it
sinks out of sight — is the paper's standard reception, but this run could not ground it in the
source.)

**FLAGS:** None on identity.

---

## 9. sterz2024effectiveness

**Bib entry:** Sterz; Baum; Biewer; Hermanns; Lauber-Rönsberg; Meinel; Langer. FAccT '24,
pp. 2495–2507, doi:10.1145/3630106.3659051.

**IDENTITY: CONFIRMED** — Crossref DOI record: all 7 authors in the bib's order, FAccT '24,
pp. 2495–2507, June 2024, ACM. Exact match.

**FULL TEXT: OBTAINED** — arXiv:2404.04059v2 (authors' submitted version; ~13,000 words; the ACM
published version is gold OA but Cloudflare-blocked). Note the read version is the preprint.

**WHAT IT ARGUES** *(from full text, arXiv version)*: Human oversight of high-risk AI (the AI
Act's Article 14 is the anchor) is **effective only if the overseer has** "(a) sufficient causal
power with regard to the system and its effects, (b) suitable epistemic access to relevant
aspects of the situation, (c) self-control, and (d) fitting intentions for their role" — with
(a)–(c) graded, and facilitators/inhibitors for each. The bib note's four-part-test reading is
verbatim-supported.

**FLAGS:** None.

---

## 10. vaccaro2020contesting

**Bib entry:** Vaccaro, Sandvig, Karahalios, *PACM HCI* 4(CSCW2), 1–22, 2020, doi:10.1145/3415238.

**IDENTITY: CONFIRMED** — Crossref DOI record: Kristen Vaccaro, Christian Sandvig, Karrie
Karahalios, PACMHCI 4(CSCW2) 1–22, Oct 2020, ACM. (Crossref's own title string carries a typo,
"ItWants," and drops the subtitle; the author PDF and ACM page carry the full title as in the
bib. Not a bib defect.)

**FULL TEXT: OBTAINED** — author-hosted PDF
(s3.amazonaws.com/kvaccaro.com/documents/vaccaro_cscw2020.pdf, found via the author's
publications.json). dl.acm.org 403.

**WHAT IT ARGUES** *(from full text)*: Between-subjects experiment on contesting automated
content moderation, comparing a **no-appeal baseline** against three appeal designs (written
appeal to human, to algorithm, behavioral appeal). "None of the appeal designs improve FACT
perceptions [Fairness, Accountability, feelings of Control, Trustworthiness] compared to a no
appeal baseline." Qualitative analysis: users contest the decision, the goal of moderation, the
automation itself, and the system's inconsistency. The bib note's "contestability null" is
exactly right (note it covers accountability *and* the other three FACT constructs).

**FLAGS:** None.

---

## 11. vandoorn2017domo

**Bib entry:** van Doorn; Mende; Noble; Hulland; Ostrom; Grewal; Petersen, *Journal of Service
Research* 20(1), 43–58, 2017, doi:10.1177/1094670516679272.

**IDENTITY: CONFIRMED** — Crossref DOI record: all 7 authors in order, JSR 20(1) 43–58, print
February 2017 (online 2016-11-28). Exact match; bib's 2017 is the print year, correct for a
volume-paginated citation.

**FULL TEXT: OBTAINED** — accepted version from University of Groningen Pure
(pure.rug.nl/ws/files/42242572/Domo_Arigato_Mr._Roboto.pdf). Sage 403.

**WHAT IT ARGUES** *(from full text/abstract of accepted version)*: Introduces **automated
social presence (ASP)** — the extent to which technology makes customers feel the presence of
another social entity — with a typology crossing automated and human social presence at
organizational frontlines, propositions on ASP → service outcomes, and a research agenda. The
bib note ("technology as automated social presence substituting for the employee; not host") is
accurate.

**FLAGS:** None.

---

## 12. weaver2025fast — priority item

**Bib entry:** Weaver, Adam, "'Fast Hospitality' and Technology…", *Hospitality & Society*,
2025, doi:10.1386/hosp_00098_1, no volume/issue (note: OnlineFirst 2025-10-28).

**IDENTITY: CONFIRMED** — Crossref DOI record: Adam Weaver, *Hospitality & Society*, issued
2025-10-28, **no volume, issue, or pages assigned** (still true at audit date), Intellect. The
archived Intellect publisher page (Wayback 2026-04-16 snapshot, HTTP 200) carries the same
citation metadata (author Adam Weaver, date 2025/10/28, no volume). Bib matches, including its
deliberate omission of volume/issue.

**FULL TEXT: BLOCKED** — intellectdiscover.com 403 live; Unpaywall: not OA; no repository copy
found. The **publisher abstract was obtained** from the archived Intellect page.

**WHAT IT ARGUES** *(publisher abstract, archived Intellect page — marked: abstract only)*: The
article "explores the use of technology to provide hospitality at high speed." Economic
competition and profitability "underpin the need for speed"; trade-journal articles evidence a
"corporate-managed push for technology-driven speed." 'Fast hospitality' blends the desire for
speed and liquid relations with the profit-seeking practices of solidly entrenched corporations;
Bauman's liquid and solid are read as contemporaneously connected rather than as historical
transition.

**FLAGS:** One framing caution for the manuscript's own critique: Weaver's target is **speed**,
not smoothness or seamlessness — neither word appears in the abstract, and the evidence base is
trade journals, not phygital frameworks. The bib note's conclusion (narrow the manuscript's
claim to seamlessness as a stated *design value* inside phygital frameworks) survives, and in
fact gets stronger: this journal has criticized technology-driven *acceleration*, which is
adjacent to but not identical with the seamlessness critique the manuscript makes. Do not cite
Weaver as having already criticized "smoothing" per se.

---

## 13. xing2026algorithmic

**Bib entry:** "Xing, Yijun and Zhang, Jason Z.", *IJCHM* 38(4), 1433–1452, 2026,
doi:10.1108/IJCHM-07-2025-1138.

**IDENTITY: DIVERGENT** — live Emerald publisher page
(emerald.com/ijchm/article/38/4/1433/1349280/) and Crossref both give: **Yunfei Xing** (Jilin
University, Changchun, China) and **Justin Z. Zhang** (University of North Florida).
- "Yijun Xing" → **Yunfei Xing** (Yijun Xing is a different, real management scholar).
- "Jason Z. Zhang" → **Justin Z. Zhang**.
- IJCHM 38(4) 1433–1452, published 2026 (online 2026-03-19): match.

**FULL TEXT: BLOCKED** — Emerald paywall ($41 PPV); Unpaywall: not OA.

**WHAT IT ARGUES** *(publisher abstract, Emerald page)*: How AI transforms customer experience
management in hospitality via "predictive, adaptive and algorithmically mediated interactions";
five dimensions of AI-reshaped guest experience; tensions among "efficiency, authenticity,
personalization and agency"; research priorities on emotional intelligence, human–AI teamwork,
trust, ethics, cross-cultural adaptation. Overlap with the manuscript's claim-space is real but
this is a CX-management-side agenda, not a hospitality-norm or worker-standing argument.

**FLAGS:** Corrupted given names for both authors.

---

## 14. xu2020facial

**Bib entry:** Xu, Feng Zeng; Zhang, Yun; Zhang, Tingting; Wang, Jing, *JHMM* 30(3), 373–393,
**2020**, doi:10.1080/19368623.2020.1813670.

**IDENTITY: CONFIRMED, one year nuance** — Crossref DOI record: same four authors in order, JHMM
30(3) 373–393; **online 2020-10-09, print issue 2021-04-03**. The bib's year 2020 is the
online-first year attached to print volume/issue/pages that belong to 2021. Most styles would
cite this as 2021.

**FULL TEXT: BLOCKED** — tandfonline.com 403; Wayback: no snapshot of the article page; the UCF
STARS record (stars.library.ucf.edu/ucfscholar/983, co-author's institution) is metadata-only,
no public file. Publisher-equivalent abstract obtained from that repository record (which dates
the paper 2021).

**WHAT IT ARGUES** *(repository-record abstract, matching publisher metadata — marked: abstract
only)*: Survey of 391 hotel guests on facial-recognition check-in adoption via security,
privacy, and trust, across three prior-experience scenarios; finds **privacy has a greater
impact on trust than security**.

**FLAGS:** Year normalization (2020 online vs 2021 print issue) — decide one convention and note
it; no author or venue problems.

---

## 15. yeung2017hypernudge

**Bib entry:** Yeung, Karen, *Information, Communication & Society* 20(1), 118–136, 2017,
doi:10.1080/1369118X.2016.1186713.

**IDENTITY: CONFIRMED** — Crossref DOI record: Karen Yeung, ICS 20(1) 118–136, print 2017-01-02
(online 2016-05-22). Exact match; 2017 print-year citation is correct.

**FULL TEXT: OBTAINED** — peer-reviewed accepted version from King's College London Pure
(kclpure.kcl.ac.uk). T&F 403.

**WHAT IT ARGUES** *(from full text, accepted version)*: Big-Data-driven personalization
constitutes nudging that is networked, continuously updated, dynamic and pervasive — hence
"hypernudge" — operating as regulation by design; Yeung mounts a liberal, rights-based critique
of these techniques. Fits the bib note ("the steering the affordances are designed against").

**FLAGS:** None.

---

## 16. ytrearnemoe2021folk

**Bib entry:** Ytre-Arne, Brita and Moe, Hallvard, *Media, Culture & Society* 43(5), 807–824,
2021, doi:10.1177/0163443720972314.

**IDENTITY: CONFIRMED** — Crossref DOI record: Brita Ytre-Arne, Hallvard Moe, MCS 43(5) 807–824,
print July 2021 (online 2020-12-15), CC BY 4.0. Exact match.

**FULL TEXT: BLOCKED** — despite the CC BY license, journals.sagepub.com 403s all available
clients, and the Norwegian repository route (hdl 11250/2739391 → national NVA archive) is a
JavaScript SPA that no non-browser client can traverse. Trivially obtainable in a browser.

**WHAT IT ARGUES** *(Crossref-deposited publisher abstract)*: Thematic analysis of open-ended
answers from a 2019 **representative survey of Norwegians**; five folk theories of algorithms —
confining, practical, reductive, intangible, exploitative; the central emotional response is
**digital irritation** rather than resignation. Supports the bib note's use (representative-
sample scale; response as a property of the form is the project's gloss, not the paper's words).

**FLAGS:** None.

---

## 17. yurrita2023disentangling

**Bib entry:** Yurrita; Draws; Balayn; Murray-Rust; Tintarev; Bozzon. CHI '23, pp. 1–21,
doi:10.1145/3544548.3581161.

**IDENTITY: CONFIRMED** — Crossref DOI record: all 6 authors in order, CHI '23 proceedings,
pp. 1–21, April 2023, ACM, CC BY. Exact match.

**FULL TEXT: BLOCKED** — ACM gold-OA PDF Cloudflare-gated; no arXiv version (arXiv API: no
match); Maastricht University CRIS record (Tintarev's institution) has the abstract but no file.

**WHAT IT ARGUES** *(abstract from Maastricht CRIS record, identical to publisher's — marked:
abstract only)*: User study, **N = 267**, loan-approval scenario, high- and low-stakes; finds
"explanations and contestability contribute to informational and procedural fairness
perceptions, respectively, but we find no evidence for an effect of human oversight." The bib
note — contestability moved procedural fairness, oversight moved nothing — is exactly supported.

**FLAGS:** None.

---

## 18. yurrita2025needs

**Bib entry:** Yurrita; Verma; Balayn; Alfrink; Gadiraju; Bozzon, *PACM HCI* 9(**CSCW**), 2025,
doi:10.1145/3757415 (no pages).

**IDENTITY: CONFIRMED, one field imprecise** — Crossref DOI record: all 6 authors in order,
PACMHCI vol 9 **issue 7** (ACM's CSCW2 2025 issue; article CSCW234), pp. 1–29, October 2025.
The bib's `number = {CSCW}` is imprecise (PACMHCI 2025 has CSCW1–CSCW2 halves) and pages/article
number are missing.

**FULL TEXT: BLOCKED** — ACM 403; TU Delft portal file
(research.tudelft.nl/files/260687877/3757415.pdf) sits behind Cloudflare; the Utrecht DSpace
copy (dspace.library.uu.nl/handle/1874/479050) is a JS SPA. Abstract obtained from the TU Delft
portal record (authors' institution; Google-Scholar-standard citation metadata).

**WHAT IT ARGUES** *(TU Delft record abstract, matching publisher metadata — marked: abstract
only)*: 21 semi-structured interviews with "citizens with experience renting their homes out"
facing an **illegal holiday rental detection** process (public-sector, high-risk); decision
subjects need interventions facilitating "(1) cooperation in sense-making, (2) support in
contestation acts, and (3) appropriate responsibility attribution." The bib note's reading
(subjects need clarity about who is accountable before they can contest; hospitality-adjacent
short-term rental hosts) is supported.

**FLAGS:** Tighten `number` to CSCW2 (or issue 7) and add article/pages if the style needs them.

---

## 19. zervas2021reputation

**Bib entry:** Zervas; Proserpio; Byers, *Marketing Letters* 32(1), 1–16, 2021,
doi:10.1007/s11002-020-09546-4.

**IDENTITY: CONFIRMED** — Crossref DOI record: Georgios Zervas, Davide Proserpio, John W.
Byers, Marketing Letters 32(1) 1–16, print March 2021 (online 2020-11-04), Springer. Exact match.

**FULL TEXT: OBTAINED** — author-hosted PDF (people.bu.edu/zg/publications/airbnbreviews.pdf;
version not marked as the journal PDF — treat as the authors' near-final text). Springer link
not attempted beyond Unpaywall (not OA).

**WHAT IT ARGUES** *(from full text, author version)*: Nearly 95% of Airbnb properties average
4.5–5 stars while comparable TripAdvisor hotel/B&B averages are 3.8–4.1 with more variance; for
**properties cross-listed on both platforms**, proportionally more get top ratings on Airbnb
than on TripAdvisor.

**FLAGS:** The bib note's gloss — "Host reputation does not travel across platforms" — is
stronger than the finding. The paper shows the *same property's rating differs systematically
across platforms* (platform-inflated ratings), which supports non-portability of the rating
signal but is not framed as a portability test. Check the manuscript sentence built on this.

---

## 20. zhou2025competency — priority item

**Bib entry:** "Zhou, Le and Lei, Xue and Liu, Min and Huang, Xu and Hou, Rui", *Asia Pacific
Journal of Human Resources* 63(2), 2025, doi:10.1111/1744-7941.70004. Note claims
readdepth=full-text, "Open access."

**IDENTITY: DIVERGENT** — Crossref DOI record and the authors' own working-paper title page
agree: **Lian Zhou** (Guangdong University of Technology), **Xue Lei** (East China University of
Science and Technology), **Mingwei Liu** (Rutgers), **Xinran Huang** (GDUT), **Rui Hou** (GDUT).
- "Le Zhou" → **Lian Zhou** (Le Zhou is a different, real I-O psychologist at Minnesota).
- "Min Liu" → **Mingwei Liu**.
- "Xu Huang" → **Xinran Huang** (Xu Huang is a different, real HK management professor).
- Lei and Hou correct. APJHR 63(2), 2025, CC BY-NC-ND: match (no page numbers in the DOI
  record; article-number journal).

**FULL TEXT: OBTAINED (working-paper version) / published version BLOCKED** — Wiley
(onlinelibrary.wiley.com, including the pdfdirect OA link) 402/403 on every available client
despite the CC BY-NC-ND license; no Wayback snapshot. Obtained and read in full the authors'
February 2025 Rutgers CGWE working paper of the same title
(smlr.rutgers.edu/sites/default/files/Documents/Centers/CGWE/CGWE_WorkingPaper_2025.02.pdf).
**Caveat: the validated-item wording below is from the working paper; the published APJHR
wording could differ and should be checked against the journal PDF in a browser session.**

**WHAT IT ARGUES** *(from full text, working-paper version)*: First validated scale of
Algorithmic Competency (AC) for on-demand platform workers; five Chinese samples; four
dimensions — understanding, embracing, leveraging, remediating AM; AC predicted by peer social
support and cognitive job crafting; AC explains incremental variance in customer-oriented
service behavior and gig-work identification. Full item detail in the Zhou section below.

**FLAGS:** Three corrupted given names. The bib note's four-dimension claim is confirmed; its
"readdepth=full-text" is plausible only if a prior session had browser access to Wiley — this
run could not reproduce that route.

---

## Summary table

| # | Citekey | Identity | Full text | Key flag |
|---|---------|----------|-----------|----------|
| 1 | riordan2024digitally | CONFIRMED (Crossref) | BLOCKED (Intellect 403, no OA) | — |
| 2 | schmidt2025field | **DIVERGENT** | BLOCKED (Wiley 403; free PDF exists) | Anne Lise→Alexander Lennart Schmidt; Kaj→Klaas Koerten |
| 3 | scottorlikowski2012accountability | CONFIRMED (Crossref) | OBTAINED (MIT DSpace, submitted) | — |
| 4 | shabnam2026tpsr | **DIVERGENT** | OBTAINED (Emerald, CC BY) | 4 given names wrong; phantom vol 40(4) — actually ahead-of-print |
| 5 | shi2025residents | **DIVERGENT** | BLOCKED (Sage 403, no OA) | All 3 given names wrong (incl. Carlos→Carla) |
| 6 | spektor2023designing | CONFIRMED (Crossref) | OBTAINED (author-lab PDF, read full) | bib/card contradict on read depth; 2 claim overstatements in drafts |
| 7 | spektor2025working | **DIVERGENT** (Crossref + archived ACM page) | **BLOCKED** (ACM 403 everywhere; no deposit) | Susan→Somang Min; Gabriel→Grace Sarfo; OBTAIN-BEFORE-CITING unresolved |
| 8 | starruhleder1996infrastructure | CONFIRMED (Crossref) | BLOCKED (INFORMS 403, no OA) | not characterized this run |
| 9 | sterz2024effectiveness | CONFIRMED (Crossref) | OBTAINED (arXiv v2, preprint) | — |
| 10 | vaccaro2020contesting | CONFIRMED (Crossref) | OBTAINED (author S3 PDF) | — |
| 11 | vandoorn2017domo | CONFIRMED (Crossref) | OBTAINED (RUG Pure, accepted) | — |
| 12 | weaver2025fast | CONFIRMED (Crossref + archived Intellect) | BLOCKED (Intellect 403); publisher abstract obtained | critiques *speed*, not smoothness |
| 13 | xing2026algorithmic | **DIVERGENT** (Emerald page + Crossref) | BLOCKED (Emerald paywall) | Yijun→Yunfei Xing; Jason→Justin Z. Zhang |
| 14 | xu2020facial | CONFIRMED (year nuance) | BLOCKED (T&F 403; UCF metadata-only) | 2020 online vs 2021 print issue |
| 15 | yeung2017hypernudge | CONFIRMED (Crossref) | OBTAINED (KCL Pure, accepted) | — |
| 16 | ytrearnemoe2021folk | CONFIRMED (Crossref) | BLOCKED (Sage 403 despite CC BY) | — |
| 17 | yurrita2023disentangling | CONFIRMED (Crossref) | BLOCKED (ACM 403 despite CC BY); abstract via UM CRIS | — |
| 18 | yurrita2025needs | CONFIRMED (issue field imprecise) | BLOCKED (ACM/TUD/UU all gated); abstract via TU Delft | number={CSCW} → CSCW2/issue 7; pages 1–29 missing |
| 19 | zervas2021reputation | CONFIRMED (Crossref) | OBTAINED (author BU PDF) | note's "does not travel" gloss stronger than finding |
| 20 | zhou2025competency | **DIVERGENT** | WP OBTAINED; published Wiley version BLOCKED | Le→Lian Zhou; Min→Mingwei Liu; Xu→Xinran Huang |

Tally: identity confirmed 14, divergent 6. Full text obtained 8 (one as working paper, one as
preprint, three as accepted/submitted author versions), publisher-abstract-only 6, neither 6
(riordan, shi, starruhleder, ytrearnemoe at abstract-from-Crossref only or less).

---

## Settlement: the two Spektor questions

**Whose work does spektor2025working study?** Back-of-house housekeeping, on the publisher's own
abstract (archived dl.acm.org page): an interview study of "how an algorithmic management (AM)
platform mediates work in a housekeeping department" of a unionized, mid-sized urban West Coast
hotel, focused on peer communication and coordination among housekeeping workers. It is the
direct sequel to the 2023 GRA study, by the same team, at the same kind of site. Nothing in the
publisher record supports citing it for front-desk work or for guest–staff relationships — the
"peer relationships" of the title are worker-to-worker. Any manuscript claim that needs
front-desk or guest-facing evidence cannot draw it from this paper, and since the full text has
still never been obtained by anyone on this project, the bib's own "OBTAIN BEFORE CITING"
condition remains in force. Current drafts cite it inside back-of-house sentences
(`DRAFT.md` ~178–181, `manuscript.md` ~266), which is the right placement — but those sentences
attribute specific mechanics (fixed sequences, withheld information) to "Spektor et al. 2023,
2025" jointly, and only the 2023 paper has been read.

**Whose work does spektor2023designing study, and what is "room assignment"?** Settled from the
full text. The participants were unionized **guest room attendants — the paper's own footnote:
"known more colloquially as housekeepers" — all identifying as women**, plus the housekeeping
supervisors who coordinate them. "UpKeep" (pseudonym) "is used to order room cleaning
assignments, and mediate digital communication and task allocation between GRAs and other
departments": room assignment means **allocating rooms to housekeepers to clean**, each room
priced in credits, with supervisors assigning and re-assigning via the app. The front desk
appears in the paper only as an adjacent department that sends GRAs extra tasks and late
assignments. A front-desk claim cited to this paper is therefore a misattribution. Two precision
repairs for the drafts, both from the full text:

1. *Rejection affordance.* UpKeep as deployed offers no rejection. Displaying assignments as
   accept/reject requests was a worker-proposed prototype, and the workers themselves then
   rejected it: "GRAs could not realistically assert in-app rejections without fear of
   termination." Rewrite `manuscript.md` ~60 ("offering a rejection affordance that workers
   feared to use") and ~268, and the bib note, so the affordance is a considered-and-refused
   design idea, not a system feature.
2. *Task-list withholding.* "Only in the most limited configurations, GRAs were instead shown
   one assignment at a time… many did allow GRAs to see their whole board." What most
   configurations removed was **self-sequencing** — "almost none of the UpKeep configurations we
   discussed allowed for self-sequencing." `manuscript.md` ~267 ("withheld the day's full task
   list under common configurations") inverts the prevalence; the defensible sentence is: fixed
   the order of work under almost all observed configurations, and in the most restrictive ones
   withheld the full day's list as well.

Also on the record: the bib says this paper was read in full (`readdepth=full`), while the only
library card for it (`spektor2023dis.md`) says abstract-depth, status rejected, "Not admitted to
the bibliography." The two project records cannot both be right; as of this audit the paper
*has* now been read in full and the card should be superseded.

---

## Settlement: the Zhou "remediating" items

Source: the authors' February 2025 working paper (Rutgers CGWE WP 2025.02), read in full — the
published APJHR version is Cloudflare-blocked to this run, so item wording carries a
working-paper caveat.

The scale development ran: interviews (Sample 1) → 14 items content-validated (of which **4**
pertained to Remediating AM) → EFA (Sample 2, N=275/312 recruited) and CFA (Sample 3, N=213)
producing a **final 12-item scale in which Remediating AM has exactly three validated items**
(Table 2, items 4–6):

- **Item 4.** "I can address deficiencies in AM by integrating personal experience." (EFA
  loading .76; CFA .92)
- **Item 5.** "I can supplement AM's shortcomings (i.e., imprecise navigation) through the help
  of WeChat groups or other tools." (.84; .83)
- **Item 6.** "I can use platform APP functions (i.e., reporting exceptions and appealing) to
  resolve vulnerabilities in AM." (.62; .54 — the weakest loadings on the factor)

The construct definition: "Remediating AM involves platform workers' ability to address or
supplement the deficiencies of AM"; the authors chose "Remediating" over "Circumventing" to
denote addressing AM's shortcomings rather than bypassing the algorithmic process.

What is a validated item versus an interview exemplar: Table 1's vivid material — the Heiland
(2023) quote about experienced riders knowing they are not always in the AM-suggested hot-zone
center, and the Cameron (2024) quotes about monitoring heat maps and automated screenshots —
are **illustrative exemplars from the literature and interviews, not scale items**. Only the
three numbered items above were validated.

Consequence for the manuscript's argument: the claim that this scale "folds appeal into
individual competency" rests on **one validated item of three** — item 6, which treats the
platform's own remedy channels ("reporting exceptions and appealing") as instruments of
individual skill — and that item is the weakest-loading of the trio. Items 4 and 5 are
experience-based and peer-tool-based supplementation, not appeal. The collision the manuscript
wants is real but narrower than "remediating = appeal-as-competency": cite item 6 specifically,
note that the dimension's other two items are about compensating for AM's deficiencies rather
than contesting its decisions, and re-verify the item wording against the published Wiley PDF
before submission.

---

## Recommended bib fixes (for the editor pass, not applied here)

1. `schmidt2025field`: `Schmidt, Alexander Lennart and Koerten, Klaas and …`
2. `shabnam2026tpsr`: `Shabnam, Saadia and Roy, Sanjit K. and Roten, Yonathan Silvain and
   Singh, Gaganpreet and Suh, Taewon and Li, Hairong`; drop `volume`/`number` (ahead-of-print).
3. `shi2025residents`: `Shi, Fangfang and Han, Xing and Samaniego-Ch\'avez, Carla Estefan\'ia`.
4. `spektor2025working`: `Min, Somang` and `Sarfo, Grace`; same fix in DRAFT.md and
   SHORT_DRAFT.md reference lists; note stays "OBTAIN BEFORE CITING" until the ACM PDF is read.
5. `xing2026algorithmic`: `Xing, Yunfei and Zhang, Justin Z.`
6. `zhou2025competency`: `Zhou, Lian and Lei, Xue and Liu, Mingwei and Huang, Xinran and Hou, Rui`.
7. `yurrita2025needs`: `number = {CSCW2}` (Crossref: vol 9, issue 7), add `pages = {1--29}` or
   the article number per style.
8. `xu2020facial`: pick one year convention (print 2021 matches vol 30(3) 373–393).
