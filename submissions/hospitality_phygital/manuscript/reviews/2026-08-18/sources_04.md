# Source-side audit — slice 04 (21 citekeys, hemmington2007 … manfreda2025reciprocal)

Audit date: 2026-08-17. Auditor: source-audit agent (slice 04 of the bibliography audit).

**Method.** Every DOI-bearing entry was checked against the DOI resolver's registration record (Crossref, `api.crossref.org/works/<doi>` — publisher-deposited metadata), and against the publisher's own page or the publisher-formatted PDF wherever a route existed. Identity verdicts below rest only on those two source classes. Full texts were pursued publisher-first, then via institutional repositories located through Unpaywall; repository copies were used for *reading* only, never for identity. Characterizations are marked by evidence level: **[full text]**, **[publisher abstract]** (Crossref-deposited or publisher page), or "not characterized."

**Blocked routes, so nobody repeats them.** Direct fetches (WebFetch and curl, browser UA) return 403/bot-challenge at: `mdpi.com` (article page and `/pdf`), `sciencedirect.com`, `linkinghub.elsevier.com`, `tandfonline.com`, `dl.acm.org`, `intellectdiscover.com`, `journals.sagepub.com` (incl. OA PDFs), `onlinelibrary.wiley.com`, `psycnet.apa.org` (JS shell), `pmc.ncbi.nlm.nih.gov` (reCAPTCHA), and `link.springer.com` (303 cookie-bounce to `idp.springer.com`, defeats both WebFetch and cookie-jar curl). The Chrome browser extension was not connected this session. Working routes: Crossref API, Europe PMC REST (`ebi.ac.uk/europepmc/.../fullTextXML`), `mdpi-res.com` direct PDF server, `emerald.com` (surprisingly open), `frontiersin.org`, Unpaywall API, and institutional repositories (Bournemouth eprints, KCL Pure, Brunel BURA, PolyU IRA, MIT course pages, UT-Austin author pages).

**Headline finding.** Seven of the eight 2025–2026 entries carry corrupted author given names — the exact secondary-index corruption pattern this project has caught three times before. One (huanglo2025failure) also carries an entirely wrong title, and its note reverses the direction of the paper's finding. Details per source.

---

## 1. hemmington2007

**Bib:** Hemmington, N., "From Service to Experience: Understanding and Defining the Hospitality Business," *The Service Industries Journal* 27(6), 747–755, 2007. doi:10.1080/02642060701453221.

**IDENTITY: CONFIRMED** — Crossref DOI record matches every field (title, sole author Nigel Hemmington, 27(6), 747–755, Sept 2007). tandfonline.com itself is 403-walled, but the DOI-resolver record plus the author-manuscript header ("The Service Industries Journal, September 2007, Volume 27, Number 6") concur.

**FULL TEXT: OBTAINED** — author manuscript, Bournemouth eprints: `http://eprints.bournemouth.ac.uk/836/1/Hemmington_Output_4.pdf` (19 pp.).

**WHAT IT ARGUES [full text]:** The failure to define hospitality as a commercial phenomenon has fragmented the field; redefining hospitality as *behaviour and experience* rather than service delivery yields a five-part framework for the commercial domain: the host–guest relationship, generosity, theatre and performance, "lots of little surprises," and the security of strangers. Conceptual essay, no empirical study. The bib note's gloss ("hospitality as host-guest relationship rather than service delivery") is accurate.

**FLAGS:** None. (Manuscript punctuation: published title uses a colon; the author manuscript uses a semicolon — bib is correct.)

---

## 2. hirsbrunner2025contestation

**Bib:** Hirsbrunner, S. D., **Kleemann, Sonja**, **Tahraoui, Mohammad Nadim**, "Contestation in Artificial Intelligence as a Practice…," *Frontiers in Communication*, 2025. doi:10.3389/fcomm.2025.1638257.

**IDENTITY: DIVERGENT** — Crossref **and** the Frontiers publisher page (fetched successfully) both give: Simon David Hirsbrunner (U. Tübingen), **Steven Kleemann** (U. Potsdam / Berlin School of Economics and Law), **Milan Nebyl Tahraoui** (BSEL / Centre Marc Bloch). Two of three given names in the bib are wrong ("Sonja" → Steven; "Mohammad Nadim" → Milan Nebyl). Also missing from the bib: volume 10, article 1638257; published online 11 Dec 2025.

**FULL TEXT: OBTAINED** — Frontiers article page fetched in full (`frontiersin.org/journals/communication/articles/10.3389/fcomm.2025.1638257/full`).

**WHAT IT ARGUES [full text]:** Primarily conceptual (practice theory after Schatzki, plus EU regulatory analysis and the authors' participation in an AI police-intelligence project). Contestability-by-design is too system-centered; contestation should be studied as embodied social practice — motivations, critical practices inside organizations, legal-regulatory contextualization, culture for contestation, external oversight, and outright rejection of AI. The note's "friendly amendment" framing (structural capability on the stakeholder side, organizational culture, legal context) is accurate.

**FLAGS:** Fix both given names before submission — a corrupted author list on a 2025 Frontiers paper is exactly what a referee's quick DOI click exposes. Add volume/article number.

---

## 3. huanglo2025failure

**Bib:** **Huang, Zilong** and Lo, Ada, "**Human versus Robot Service Provider Agents in Service Failures: The Moderating Role of Failure Type**," *Information Technology & Tourism* 27(2), 417–448, 2025. doi:10.1007/s40558-025-00314-6.

**IDENTITY: DIVERGENT — worst entry in the slice.** Crossref and the publisher-formatted PDF both give: **Zuwen Huang** and Ada Lo (both School of Hotel & Tourism Management, Hong Kong PolyU), title "**Human vs. robot service provider agents in service failures: comparing customer dissatisfaction and the mediating role of forgiveness and service recovery expectation**." The bib's given name is wrong AND the bib title is not the article's title — it reads like a title reconstructed from a summary (the note itself said "Title wording to confirm against the article at proof"; confirmed now: it is wrong). Vol/issue/pages/year check out (27(2), 417–448; online 18 Feb 2025, issue June 2025).

**FULL TEXT: OBTAINED** — CC-BY version of record via PolyU IRA: `https://ira.lib.polyu.edu.hk/bitstream/10397/112142/1/s40558-025-00314-6.pdf` (link.springer.com itself is bot-walled).

**WHAT IT ARGUES [full text]:** 3 (SPA: human / humanoid robot / non-humanoid robot) × 2 (failure type: process / outcome) between-subjects scenario experiment; two-way ANCOVA plus serial mediation (process-failure model N = 196). As SPA humanness increases, forgiveness **decreases**, service-recovery expectation rises, and dissatisfaction **intensifies** — and these differences appear **only in process failures**, not outcome failures. Forgiveness → SRE serially and fully mediate (direct effect ns). Grounded in Mind Perception, Attribution, and Expectancy Disconfirmation theory. Note: this is a **vignette/scenario experiment**, not a field experiment.

**FLAGS:** (1) Replace the title and given name. (2) **The note's gloss reverses the finding's direction.** "Human preference is contingent on FAILURE TYPE" is wrong as stated: the paper documents a *humanness penalty* in process failures — customers forgive robots more and are more dissatisfied with humans when the process fails. What survives is the structural point (human/robot differences are contingent on a coordination-shaped variable, failure type, not on taste), but any manuscript sentence implying guests *prefer humans* in process failures cites this paper against itself. Check section 4's sentence verbatim before proof.

---

## 4. jhaver2018anxiety

**Bib:** Jhaver, Karpfen, Antin, "Algorithmic Anxiety and Coping Strategies of Airbnb Hosts," CHI 2018, 1–12. doi:10.1145/3173574.3173995.

**IDENTITY: CONFIRMED** — Crossref matches (Shagun Jhaver, Yoni Karpfen, Judd Antin; CHI '18 proceedings; pp. 1–12; April 2018), and the published ACM-formatted PDF confirms authors/affiliations (Georgia Tech; Airbnb ×2).

**FULL TEXT: OBTAINED** — author-hosted published PDF: `https://shagunjhaver.com/research/articles/jhaver-2018-airbnb/jhaver-2018-airbnb.pdf` (dl.acm.org is 403-walled).

**WHAT IT ARGUES [full text, first pages + abstract]:** Interviews with 15 Airbnb hosts. Hosts engage in a *double negotiation* — appealing simultaneously to potential guests and to partially transparent evaluative algorithms; perceived lack of control and uncertainty over algorithmic evaluation produces *algorithmic anxiety*; hosts cope by reverse-engineering the algorithm and comparing themselves to other hosts; design implications follow. The note's use (hospitality algorithmacy observed in a hospitality setting) is accurate.

**FLAGS:** None. Small-N qualitative study — fine as long as the manuscript cites it for the phenomenon, not for prevalence.

---

## 5. jung2019undermining

**Bib:** Jung, H. S. and Yoon, H. H., "The Effects of Social Undermining on Employee Voice and Silence and on Organizational Deviant Behaviors in the Hotel Industry," *JSTP* 29(2), 213–231, 2019. doi:10.1108/JSTP-06-2018-0131.

**IDENTITY: CONFIRMED** — Crossref and the Emerald publisher page (fetched successfully, one of the few open publisher hosts) both match every field: Hyo Sun Jung, Hye Hyun Yoon; 29(2), 213–231, 2019.

**FULL TEXT: BLOCKED** — Emerald serves the record page but the full text is subscription-only; Unpaywall shows no OA copy.

**WHAT IT ARGUES [publisher abstract, Crossref-deposited and Emerald page]:** Survey of 344 five-star hotel employees in South Korea (SEM). Undermining by supervisor, coworker, **and customer** each depresses voice and increases silence; silence predicts organizational deviance, voice does not. The note's claim — the guest is one of three voice-suppressors before any algorithm enters — is exactly what the abstract reports.

**FLAGS:** None on identity or use. Cross-sectional single-country survey; keep the citation at "depresses voice," not causal language.

---

## 6. kim2021preference

**Bib:** Kim, S., Kim, J., Badu-Baiden, F., Giroux, M., Choi, Y., "Preference for Robot Service or Human Service in Hotels? Impacts of the COVID-19 Pandemic," *IJHM* 93, 102795, 2021. doi:10.1016/j.ijhm.2020.102795.

**IDENTITY: CONFIRMED** — Crossref matches all fields (lead author registered as "Seongseop (Sam) Kim"; IJHM 93, article 102795, Feb 2021).

**FULL TEXT: OBTAINED** — Europe PMC full-text XML (PMC9998175), the publisher-deposited pandemic-collection copy. (sciencedirect.com and pmc.ncbi.nlm.nih.gov front doors both blocked; the EBI REST endpoint works.)

**WHAT IT ARGUES [full text]:** Series of experiments (Studies 1A/1B, 2A/2B, 3, 4; e.g., Study 2A: 162 MTurk adults, COVID-threat news article vs. control, then robot-staffed vs. human-staffed hotel choice). When COVID-19 risk is salient, consumers evaluate and choose robot-staffed hotels **more** favorably — the reverse of pre-pandemic findings — with perceived threat moderating the preference.

**FLAGS:** Watch the manuscript's use. The note files this as "human accessibility with an empirical floor," and the huanglo note accuses others of "over-reading kim2021preference." The paper's own headline is a *robot* preference under threat salience; the human-preference baseline lives in the pre-COVID literature it cites, not in its data. Any sentence citing this paper for human preference must be conditioned on the non-threat baseline.

---

## 7. kim2025shadow

**Bib:** **Kim, Hyunsu**, Chung, Chanho, Chung, Namho, "When Customers Resist Self-Service Technology: A Shadow Work Perspective," *IJHCI* 42(10), 7269–7287, 2025. doi:10.1080/10447318.2025.2558022.

**IDENTITY: DIVERGENT** — Crossref gives **Hyunkyu Kim**, Chanho Chung, Namho Chung. Bib's "Hyunsu" is wrong. Title, journal (*International Journal of Human–Computer Interaction*), 42(10), 7269–7287 match — but 42(10) is the **print issue of 19 May 2026**; online-first was 15 Sept 2025. The bib pairs year 2025 with the 2026 print volume/issue/pages.

**FULL TEXT: BLOCKED** — tandfonline.com 403 (attempted directly); not OA per Unpaywall; no Crossref-deposited abstract; no repository copy found.

**WHAT IT ARGUES:** Not characterized — no publisher abstract was reachable. The note's content claims (mandatory self-service as shadow work; job-demand/control/support dynamics predicting stress and resistance) remain **unverified** in this audit.

**FLAGS:** Fix given name. Decide the year convention: cite as 2025 online-first (drop vol/issue/pages) or as 2026, 42(10), 7269–7287 — the current hybrid is internally inconsistent and a referee with library access will see it. Content claims still resting on whatever the prior verifier read.

---

## 8. lariviere2017service

**Bib:** Larivière, Bowen, Andreassen, Kunz, Sirianni, Voss, Wünderlich, De Keyser, "'Service Encounter 2.0'…," *JBR* 79, 238–246, 2017. doi:10.1016/j.jbusres.2017.03.008.

**IDENTITY: CONFIRMED** — Crossref matches the complete eight-author list in order, with diacritics (Larivière, Wünderlich), JBR 79, 238–246, Oct 2017.

**FULL TEXT: BLOCKED** — ScienceDirect 403; KU Leuven Lirias record resolves to a discovery-layer redirect with no accessible file; no other OA location per Unpaywall.

**WHAT IT ARGUES:** Not characterized — Elsevier deposits no abstract to Crossref and the journal page is unreachable. The note's claims (earliest explicit three-way technology/employee/customer framing; technology augments or substitutes the employee) remain **unverified this round**; they rest on the prior abstract-level verification of 2026-08-09.

**FLAGS:** None on identity. If the triad-concession paragraph leans hard on this paper's exact wording, someone with access should confirm before proof.

---

## 9. lashley2000towards

**Bib:** Lashley, C., "Towards a Theoretical Understanding," in Lashley & Morrison (eds.), *In Search of Hospitality: Theoretical Perspectives and Debates*, Butterworth-Heinemann, Oxford, 2000, pp. 1–16. (No DOI.)

**IDENTITY: PARTIALLY CONFIRMED** — Elsevier's own shop page for the book (`shop.elsevier.com/books/in-search-of-hospitality/morrison/978-0-08-050856-6`) confirms chapter 1 is "Towards a theoretical understanding" by Lashley; the Internet Archive's scan of the physical book confirms Butterworth-Heinemann, Oxford, 2000, ISBNs 0750645628 / 0750654317. **The page range is unconfirmed**: neither publisher TOC shows pages, and Lynch et al. (2011) — read in full for entry 18 — cite this chapter in their reference list as "'Introduction'… pp. 1–17". Multiple independent citations elsewhere also use 1–17.

**FULL TEXT: BLOCKED** — the archive.org copy is borrow-gated; no OA chapter copy found.

**WHAT IT ARGUES:** Not characterized (not read this round). The note's claim (three domains of hospitality: commercial, private, social) is the standard reading of this chapter but was not verified against the text here.

**FLAGS:** Pages 1–16 vs. 1–17 needs settling against the physical book at proof. Note also that the founding editorial itself cites this chapter under the title "Introduction" — if the manuscript quotes Lashley 2000 with a page number, verify the page against a physical/scanned copy.

---

## 10. lee2019procedural

**Bib:** Lee, M. K., Jain, A., **Cha, Hea Jin**, Ojha, S., Kusbit, D., "Procedural Justice in Algorithmic Fairness: Leveraging Transparency and Outcome Control for Fair Algorithmic Mediation," *PACM HCI* 3(CSCW), 1–26, 2019. doi:10.1145/3359284.

**IDENTITY: CONFIRMED with one divergence** — Crossref registers the short title ("Procedural Justice in Algorithmic Fairness") but the published ACM-formatted article (obtained) carries the full subtitle exactly as in the bib. Authors per the published paper: Min Kyung Lee, Anuraag Jain, **Hae Jin Cha**, Shashank Ojha, Daniel Kusbit — the bib spells the third author "**Hea** Jin"; the article prints "**Hae** Jin" (both Crossref and the PDF byline). Vol 3, CSCW, **Article 182** (Nov 2019), 26 pages — bib's "1–26" is a tolerable rendering but "Article 182" is the canonical locator.

**FULL TEXT: OBTAINED** — author-hosted copy of the ACM version: `https://pages.ischool.utexas.edu/hai-files/files/publications/45/2019-CSCW-Al_ProceduralFairness.pdf` (dl.acm.org 403).

**WHAT IT ARGUES [full text, first page + abstract]:** Proposes a procedural-justice framework for algorithmic decisions; builds an interface (goods division case) implementing standards clarity, outcome explanation (input–output matrix), and interactive group outcome control; within-subjects laboratory study. Standards clarity alone did **not** raise perceived fairness; outcome explanation had **mixed** effects (could decrease perceived fairness and reduce perceived algorithmic accountability); **outcome control universally improved perceived fairness** — people saw the decision's inherent limits and redistributed to fit context. The note's claim is exact.

**FLAGS:** Fix "Hea Jin" → "Hae Jin". Nuance worth carrying: "universally" means across participants in one within-subjects lab study of goods division — the transparency components' *mixed/negative* results are part of the same finding and actually sharpen the manuscript's adjustability-over-transparency argument.

---

## 11. li2021systematic

**Bib:** Li, M., Yin, D., Qiu, H., Bai, B., "A Systematic Review of AI Technology-Based Service Encounters…," *IJHM* 95, 102930, 2021. doi:10.1016/j.ijhm.2021.102930.

**IDENTITY: CONFIRMED** — Crossref matches all four authors in order (Minglong Li, Dexiang Yin, Hailian Qiu, Billy Bai), IJHM 95, article 102930, May 2021.

**FULL TEXT: BLOCKED** — ScienceDirect 403; not OA per Unpaywall; no Crossref abstract; no repository copy found.

**WHAT IT ARGUES:** Not characterized. The note's specific claims (literal customer–employee–AI encounter triad; four modes: AI-supplemented, AI-generated, AI-mediated, AI-facilitated) are **unverified this round** — they rest on the 2026-08-09 abstract-level verification. Since this is billed as "THE key concession citation for sec 3," someone with Elsevier access should re-read the abstract or text before proof.

**FLAGS:** None on identity.

---

## 12. lin2025oscillation

**Bib:** **Lin, Hongyu**, "Oscillation between Resist and to Not? Users' Folk Theories and Resistance to Algorithmic Curation on Douyin," *Social Media + Society*, 2025. doi:10.1177/20563051251313610.

**IDENTITY: DIVERGENT** — the author is **Hui Lin** (King's College London), per Crossref **and** the Sage version-of-record PDF byline. Bib's "Hongyu" is wrong (the note flagged "author given name to confirm" — confirmed: it needs correction). Bib also omits volume 11, issue 1, pages 1–13 / article 20563051251313610, Jan–March 2025.

**FULL TEXT: OBTAINED** — Sage VoR (CC BY-NC) via KCL Pure: `https://kclpure.kcl.ac.uk/ws/files/358195628/Oscillation_Between_Resist_and_to_Not_Version_of_Record.pdf` (journals.sagepub.com blocks direct download even for OA).

**WHAT IT ARGUES [full text, abstract + opening]:** Walk-through method plus diary-interviews, 31 Douyin users. Users hold articulate folk theories and voice annoyance (algorithmic simplification, commercial exploitation, political agenda-setting) yet behave in contradiction — *oscillated resistance*. The paradox reflects both the reconciling of sociocultural needs with algorithmic irritation and **digital resignation** under strict platform regulation and censorship; resistance stays "constrained within the dominant use of technological affordances," a continuous negotiation, not a subversive force. The note's "sharpest statement of the separation" (competence documented, non-conversion into influence documented, same study) is accurate.

**FLAGS:** Fix given name; add 11(1) and pagination.

---

## 13. lin2026voice  *(priority)*

**Bib:** **Lin, Wei; Zhang, Min; Zhang, Wei; Zhang, Chi**, "Will Employees Still Speak Up under Algorithmic Management?…," *Systems* 14(5), 569, 2026. doi:10.3390/systems14050569.

**IDENTITY: DIVERGENT — all four given names are wrong.** Crossref and the MDPI-published PDF byline both give: **Wanliang Lin, Mingyu Zhang, Wenjia Zhang, Can Zhang**, all School of Economics and Management, Beijing Jiaotong University. Journal/volume/issue/article (Systems 14(5):569, published 16 May 2026, CC BY) match.

**FULL TEXT: OBTAINED** — publisher PDF via MDPI's content server: `https://mdpi-res.com/d_attachment/systems/systems-14-00569/article_deploy/systems-14-00569.pdf` (mdpi.com itself 403s; results section read in full, pp. 1–2, 16–20).

**WHAT IT ARGUES [full text]:** One-to-one matched data from **351 employee–supervisor pairs** in a large Chinese platform enterprise (Meituan); SEM + bootstrapping; signaling theory. Direct effects on felt responsibility for constructive change (FRCC): algorithmic directing **−0.650***, scheduling **−0.595***, monitoring **−0.515*** — and algorithmic **feedback +0.345*** (all p < .001); FRCC → voice **0.431***. So three algorithmic functions suppress voice through reduced felt responsibility, while **feedback raises voice** (conditional indirect effect positive at both WLOC levels: +0.182 internal, +0.095 external). Work locus of control moderates every path: external WLOC amplifies the three negative effects; internal WLOC amplifies feedback's positive effect. Controls include algorithmic transparency, explainability, trust, efficacy — **no climate construct anywhere**, confirming the note's point that the prior-voice-climate interaction remains untested.

**FLAGS:** (1) Replace all four given names — this is the fabricated-author-list pattern verbatim. (2) The priority concern is confirmed with numbers: **any manuscript sentence citing this paper flatly for algorithmic silence/suppression misstates a quarter of its result.** The honest citation is the split: directing/scheduling/monitoring suppress voice via felt responsibility; feedback enhances it. The bib note itself already states this correctly — the manuscript text is what needs checking.

---

## 14. lind1990voice  *(priority — claim-23 repair anchor)*

**Bib:** Lind, E. A., Kanfer, R., Earley, P. C., "Voice, Control, and Procedural Justice: Instrumental and Noninstrumental Concerns in Fairness Judgments," *JPSP* 59(5), 952–959, 1990. doi:10.1037/0022-3514.59.5.952.

**IDENTITY: CONFIRMED** — Crossref/APA registration matches every field, and the published article scan confirms: E. Allan Lind (American Bar Foundation), Ruth Kanfer (U. Minnesota), P. Christopher Earley (U. Minnesota); JPSP 1990, Vol. 59, No. 5, 952–959.

**FULL TEXT: OBTAINED AND READ IN FULL** — published-article PDF hosted on an MIT course page: `https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Justice/Lind_et_al_1990_Voice_control.pdf` (psycnet.apa.org unreachable; a figshare deposit also exists per Unpaywall).

**WHAT IT ACTUALLY FOUND [full text]:** 3 (no voice / postdecision voice / predecision voice) × 3 (no / irrelevant / relevant information) between-subjects goal-setting experiment; 179 usable male undergraduates (180 run, 1 dropped), 5-point single-item fairness measures. Core result — the one the manuscript needs: **postdecision voice, delivered with an explicit statement that the goal "would not be changed regardless of what the subject said" and with the goal in fact unchanged, still raised both procedural fairness (2.43 → 3.15) and outcome fairness (2.11 → 2.72) relative to no voice**, with all pairwise contrasts significant. Postdecision voice also raised goal acceptance and task performance. So the drafted replacement does carry the load: voice retained value after the decision, with zero instrumental capacity.

**Conditions and reversals the manuscript must respect:**
- **Predecision voice beat postdecision voice** on both fairness measures (3.70 / 3.31). Post-decision voice retains *some* value, not equal value. The authors' own arithmetic: the symbolic component (no-voice→post, .72) was slightly *larger* than the instrumental increment (post→pre, .55).
- **The perceived-control confound:** subjects in the postdecision condition reported *more* control than no-voice subjects despite the explicit denial — an illusion-of-control or group-value effect the study cannot discriminate. In the mediation (ANCOVA) analyses, perceived control absorbed most of the voice effect on procedural fairness (η² .19 → .03, still significant) and **all** of it on outcome fairness (ns after control removed). The paper's claim is therefore "not *all* of the voice effect is control-mediated," not "voice works independently of control."
- **A documented reversal condition:** the paper itself flags Folger's *frustration effect* — ostensibly high-voice procedures produce actively negative reactions when repeated unfavorable outcomes or cues reveal bias subverting the input. Lind & Tyler's position: frustration effects occur when the procedure is blatantly biased. If the manuscript derives a design recommendation (post-decision voice channels in phygital service), this boundary is the load-bearing caveat.
- **The abuse warning:** the discussion (citing Cohen) explicitly warns that voice-based fairness enhancement can be exploited — sham voice can manufacture "false consciousness" of fair procedure. For a paper about algorithmic hospitality interfaces, this cuts close: Lind et al. are as much a warning about *fabricated* voice affordances as an endorsement of post-decision voice.
- Sample: male undergraduates only; single-item measures; lab goal-setting task.

**FLAGS:** Identity clean; the citation supports the repaired claim 23. Recommend the manuscript cite it *with* the predecision>postdecision ordering and the frustration-effect boundary, or a referee steeped in the justice literature will supply them.

---

## 15. lisun2025accessibility

**Bib:** **Li, Hui** and **Sun, Zhiyuan**, "Is Algorithmic Accessibility Sufficient?…," *Governance* 38(4), 2025. doi:10.1111/gove.70067.

**IDENTITY: DIVERGENT — both given names wrong.** Crossref gives **Huanhuan Li** and **Zongfeng Sun**. (The note flagged "author names to confirm at proof" — confirmed: both need correction.) Also: article e70067, issue 4 is the **Oct 2025 print issue** (online 27 Sept 2025); bib gives 38(4) with year 2025, which is consistent, but no article number.

**FULL TEXT: BLOCKED** — onlinelibrary.wiley.com 403 (attempted); not OA per Unpaywall.

**WHAT IT ARGUES [publisher abstract, Crossref-deposited]:** Two survey experiments with "real-world" scenarios, varying algorithmic accessibility and accountability under different decision risks. **Accountability exerts a stronger influence than accessibility** on perceived trustworthiness of both algorithms and bureaucrats; accountability × decision-risk interaction significant.

**FLAGS:** (1) Fix both given names. (2) The note's claim that the accountability effect "work[s] through procedural justice in the same Lind and Tyler tradition section 7 uses" is **not in the abstract** — it may be in the theory section, but it is unverified; do not let that mechanism claim into the manuscript without full-text confirmation. The abstract-safe claim is the accessibility-insufficient / accountability-pivotal contrast.

---

## 16. lugosi2008

**Bib:** Lugosi, P., "Hospitality Spaces, Hospitable Moments…," *Journal of Foodservice* 19(2), 139–149, 2008. doi:10.1111/j.1745-4506.2008.00092.x.

**IDENTITY: CONFIRMED** — Crossref matches all fields (Peter Lugosi; 19(2), 139–149, 2008).

**FULL TEXT: OBTAINED** — accepted pre-proof version, Bournemouth eprints: `http://eprints.bournemouth.ac.uk/16027/3/P_Lugosi_JOFS_Hospitality_spaces_resubmission.pdf`.

**WHAT IT ARGUES [full text, abstract + opening; also Crossref abstract]:** Distinguishes three dimensions: hospitality as commercial provision of food/drink/shelter/entertainment; hospitality as a means to social or political ends; and *meta-hospitality* — temporary emotional states of being distinct from rational manifestations, tied to *communitesque moments* (short-lived emotional bonds). A case study identifies three shaping factors: ecology, participants' roles, capabilities. The note's gloss "hospitable moments as emergent and unscripted" is a fair reading (meta-hospitality is episodic and cannot be guaranteed by transactional design), though the words "emergent/unscripted" are the manuscript's, not the paper's.

**FLAGS:** None.

---

## 17. lv2024autonomy

**Bib:** Lv, Chen, Liu, Chen, "Alleviating Travelers' Privacy Concern in Personalized Recommendations through Perceived Information Autonomy," *JTR* 64(8), 1974–1988, 2024. doi:10.1177/00472875241268511.

**IDENTITY: DIVERGENT (two fields)** — Crossref: authors match (Linxiang Lv, Siyun Chen, Gus Guanrong Liu, Mingwen Chen), but (1) the registered title continues: "…Perceived Information Autonomy**: Strategies via Hedge Words and Communication Styles**" — the bib truncates the subtitle; (2) **year**: online-first 16 Aug 2024, but volume 64(8), 1974–1988 is the **Nov 2025 print issue**. The bib pairs the 2024 online year with the 2025 print volume/issue/pages — same hybrid problem as kim2025shadow.

**FULL TEXT: BLOCKED** — Sage; not OA per Unpaywall.

**WHAT IT ARGUES [publisher abstract, Crossref-deposited]:** A field study on Facebook plus three experiments. Hedge words (uncertain expressions) in personalized recommendation labels reduce privacy concern and improve attitudes; the effect is **mediated by travelers' autonomy over their personal information** and moderated by communication style. The note's use (perceived information autonomy as the empirical mechanism behind the adjustability affordance) matches the abstract.

**FLAGS:** Restore the subtitle; resolve the 2024/2025 year–volume pairing. Note the mechanism is about *perceived* autonomy induced by phrasing (hedge words) — if the manuscript cites it for actual adjustability affordances, that is one step beyond the study's manipulation.

---

## 18. lynch2011theorizing  *(priority — target journal's founding statement)*

**Bib:** Lynch, Germann Molz, McIntosh, Lugosi, Lashley, "Theorizing Hospitality," *Hospitality & Society* 1(1), 3–24, 2011. doi:10.1386/hosp.1.1.3_2.

**IDENTITY: CONFIRMED** — Crossref matches: Paul Lynch, Jennie Germann Molz, Alison McIntosh, Peter Lugosi, Conrad Lashley (Crossref renders "Mcintosh" — a casing artifact; the article byline reads McIntosh); H&S 1(1), 3–24, 2011. (intellectdiscover.com is 403-walled; Strathclyde and Bournemouth institutional records concur on all fields.)

**FULL TEXT: OBTAINED AND READ IN FULL** — author version via Bournemouth eprints: `https://eprints.bournemouth.ac.uk/18396/3/HOSP_1.1_1_2_editorial_Lynch_et_al.pdf` (22 pp.; cover sheet warns it is the pre-final version — fine for reading, cite the published pagination).

**WHAT IT ARGUES [full text]:** The read_depth:metadata gap is now closed. The founding editorial's argument: hospitality studies has become "intrinsically inhospitable" to the interdisciplinary study of hospitality; the dominant managerial definition (provision of food/drink/accommodation) "reduces hospitality to an economic activity" and constrains its intellectual possibilities. It organizes the literature via Brotherton & Wood's two themes — **hospitality as social control** (management of the stranger; Selwyn's "hospitality converts"; hostipitality — hospitality always entailing its opposite) and **hospitality as social and economic exchange** (gift exchange, the exchange paradox, micro-hosts/macro-hosts via Robinson & Lynch, guest–guest hosting via Lugosi) — plus **hospitality as metaphor/social lens**. It then sets a research agenda of named areas, including, verbatim as an agenda item, **"Hospitality and virtuality"**: hospitality as a lens on "the way humans interact with each other in virtual spaces and with new technologies in physical spaces," citing Ciborra's question of how humans and technologies host each other, technology as "an ambivalent and threatening stranger," and the warning that "like all guests, technology can dominate the host… humans and technologies can become hostages of each other." Journal ambitions: international, multidisciplinary, social-science, ultimately concerned with developing theoretical perspectives on hospitality and hospitableness.

**FLAGS:** (1) None on identity. (2) For fit: the "Hospitality and virtuality" agenda item and the Ciborra discussion are the strongest possible warrant that the phygital paper answers the journal's founding call — worth citing to the specific pages rather than generically. (3) Referee-facing detail: the editorial also discusses Bell's non-human hospitality and the mediatory role of the built environment — a referee who knows this text will expect the manuscript to acknowledge that the founding statement already contemplated non-human and technological hosts. (4) Incidental: its reference list cites Lashley 2000 as "'Introduction', pp. 1–17" — see entry 9's page-range flag.

---

## 19. lynch2017mundane

**Bib:** Lynch, P., "Mundane Welcome: Hospitality as Life Politics," *Annals of Tourism Research* 64, 174–184, 2017. doi:10.1016/j.annals.2017.04.001.

**IDENTITY: CONFIRMED** — Crossref matches (Paul Lynch; ATR 64, 174–184, May 2017).

**FULL TEXT: BLOCKED this round** — ScienceDirect 403; the Napier worktribe repository entry (`napier-surface.worktribe.com/824942/...`) serves an HTML wrapper with no reachable file. Bib records a prior full read (readdepth=full, 2026-08-09).

**WHAT IT ARGUES:** Not characterized in this audit (no publisher abstract deposited; full text not re-obtained). Prior verification stands on its own record.

**FLAGS:** None on identity.

---

## 20. mameli2026framework

**Bib:** **Mameli, Eleonora**, Scarles, Stangl, Frohlich, "A Comprehensive Framework for Phygital Tourism Experiences," *ITT* 28(1), 2026. doi:10.1007/s40558-026-00362-6.

**IDENTITY: DIVERGENT** — Crossref and the published PDF byline both give **Elisa Mameli** (Surrey), Caroline Scarles, Brigitte Stangl, David Frohlich. Bib's "Eleonora" is wrong. Registered title continues: "…phygital tourism experiences**: bridging academic insights and industry practices across sectors**" — bib truncates. Article number 19 (ITT 28:19), online 14 Feb 2026, issue June 2026, CC BY.

**FULL TEXT: OBTAINED** — version of record via Brunel BURA: `http://bura.brunel.ac.uk/bitstream/2438/32941/1/FullText.pdf` (link.springer.com bot-walled despite CC BY; pages 1, 20–26 read: abstract, industry-analysis findings, gaps table, framework, conclusions).

**WHAT IT ARGUES [full text, sections read]:** REVIEW article. Narrative systematic review (PRISMA-guided) of **57 academic articles** plus content analysis of **84 industry phygital examples across 11 sectors** — matching the note's numbers. Four themes (defining phygital; customer responses; technological components; phygital strategies); proposes an integrated framework (physical–digital "ratio" continuum after Milgram & Kishino; typologies; features; stakeholder engagement). Identified gaps (Table 7): accessibility, privacy/security, older generations, non-luxury/SME contexts, post-experience stage, longitudinal and mixed methods. The conclusion affirms phygital as "characterised by the **seamless integration** of sensory, spatial, and technological elements."

**FLAGS:** (1) Fix given name and restore the subtitle; add article number 19. (2) The note's gap claim holds in everything read: seamlessness is asserted as constitutive, never problematized, and **no friction discussion appears anywhere in the gaps table, framework, or conclusions** (pp. 20–26, plus abstract). Caveat for honesty: I read ~9 of 31 pages; the "no friction discussion anywhere" universal was checked against the sections where such discussion would live (gaps, agenda, conclusions), not the full text line-by-line.

---

## 21. manfreda2025reciprocal  *(priority — gratitude vs. obligation)*

**Bib:** Manfreda, A. and Harkison, T., "Beyond Exchange: Decoding Reciprocal Hospitableness in Luxury Lodge Experiences," *JHTM* 62, 173–187, 2025. doi:10.1016/j.jhtm.2025.01.011.

**IDENTITY: CONFIRMED** — Crossref matches (Anita Manfreda, Tracy Harkison; JHTM 62, 173–187, March 2025).

**FULL TEXT: BLOCKED** — ScienceDirect 403; not OA per Unpaywall. The full abstract was obtained verbatim from the lead author's institutional research portal (research.torrens.edu.au), which mirrors the publisher abstract. (An AUT OJS conference paper, "A model of reciprocal hospitableness for luxury lodges," is openly downloadable but is a *different, earlier document* — do not conflate.)

**WHAT IT ARGUES [publisher abstract]:** Multiple-case study of luxury lodges; proposes a multi-stakeholder model of reciprocal hospitableness. Hospitableness — "altruism/generosity, sense of belonging/fictive kinship, meaningful connection, comfort/homely atmosphere, and inclusivity" — is reciprocated among guests, hosts, and other stakeholders; contributions framed via social exchange and reciprocity, transformative luxury, sustainable luxury.

**FLAGS — the priority question:** **The abstract frames the reciprocation as neither gratitude nor obligation.** It speaks of altruism/generosity, fictive kinship, and mutual exchange. The bib note's assertion that guest reciprocation is "framed **explicitly** as GRATITUDE-DRIVEN RECIPROCATION rather than obligation" is **not supported at the abstract level** — if "gratitude" appears, it is in the body text, which I could not reach. Two consequences: (a) the specific behavioral examples in the note (tidying rooms, returning glasses, praising staff in reviews) are also body-text claims, unverified here; (b) if Section 2's narrowing move ("what the guest OWES") leans on the gratitude-vs-obligation contrast, that contrast currently rests on nobody's verified reading. Someone with Elsevier access must confirm the gratitude framing before the manuscript asserts it — or the sentence should be rewritten to the abstract-safe claim: reciprocation is documented as mutual, altruistic exchange, not as obligation.

---

## Summary table

| # | citekey | identity | full text | flags |
|---|---------|----------|-----------|-------|
| 1 | hemmington2007 | CONFIRMED | OBTAINED (Bournemouth eprints) | — |
| 2 | hirsbrunner2025contestation | DIVERGENT: 2 given names (Steven Kleemann; Milan Nebyl Tahraoui); vol/art. no. missing | OBTAINED (Frontiers) | fix authors |
| 3 | huanglo2025failure | DIVERGENT: given name (Zuwen); **title wrong** | OBTAINED (PolyU IRA, CC-BY VoR) | note reverses finding's direction (humanness *penalty* in process failures) |
| 4 | jhaver2018anxiety | CONFIRMED | OBTAINED (author-hosted VoR) | — |
| 5 | jung2019undermining | CONFIRMED (Emerald page + Crossref) | BLOCKED (subscription) | abstract-level use accurate |
| 6 | kim2021preference | CONFIRMED | OBTAINED (Europe PMC XML) | headline is *robot* preference under COVID salience — condition any human-preference use |
| 7 | kim2025shadow | DIVERGENT: given name (Hyunkyu); 2025 year paired with 2026 print vol/issue | BLOCKED (T&F 403; no OA) | not characterized; note claims unverified |
| 8 | lariviere2017service | CONFIRMED | BLOCKED (SD 403; Lirias dead-end) | not characterized this round |
| 9 | lashley2000towards | PARTIAL: book/chapter/title/year confirmed; **pages 1–16 unconfirmed** (1–17 in H&S editorial's refs) | BLOCKED (borrow-gated) | verify pages at proof |
| 10 | lee2019procedural | CONFIRMED; given-name spelling **Hae** Jin Cha (bib: Hea) | OBTAINED (author-hosted VoR) | fix spelling; Article 182 canonical |
| 11 | li2021systematic | CONFIRMED | BLOCKED (SD 403; no OA) | not characterized; key concession claims unverified this round |
| 12 | lin2025oscillation | DIVERGENT: author is **Hui Lin** (bib: Hongyu); vol/issue missing | OBTAINED (KCL Pure, Sage VoR) | fix author; add 11(1) |
| 13 | lin2026voice | DIVERGENT: **all 4 given names wrong** (Wanliang Lin, Mingyu Zhang, Wenjia Zhang, Can Zhang) | OBTAINED (MDPI VoR) | feedback **raises** voice (+0.345→FRCC); cite the 3-vs-1 split, not blanket silence |
| 14 | lind1990voice | CONFIRMED | OBTAINED & read in full (MIT-hosted VoR) | supports claim 23; carry pre>post ordering, control confound, frustration-effect boundary, sham-voice warning |
| 15 | lisun2025accessibility | DIVERGENT: **both given names wrong** (Huanhuan Li; Zongfeng Sun) | BLOCKED (Wiley 403; no OA) | fix authors; "procedural justice mechanism" not in abstract — unverified |
| 16 | lugosi2008 | CONFIRMED | OBTAINED (Bournemouth eprints) | — |
| 17 | lv2024autonomy | DIVERGENT: subtitle truncated; 2024 year paired with Nov-2025 print vol/issue/pages | BLOCKED (Sage; no OA) | abstract supports mediation claim; fix title/year pairing |
| 18 | lynch2011theorizing | CONFIRMED | OBTAINED & read in full (Bournemouth eprints) | metadata gap closed; "Hospitality and virtuality" agenda item is the fit warrant; editorial already contemplates non-human hosts |
| 19 | lynch2017mundane | CONFIRMED | BLOCKED this round (SD 403; Napier wrapper) | prior full read on record |
| 20 | mameli2026framework | DIVERGENT: given name (**Elisa**, not Eleonora); subtitle truncated; art. no. 19 missing | OBTAINED (Brunel BURA VoR) | gap claim supported in sections read; seamlessness affirmed, friction absent from gaps/conclusions |
| 21 | manfreda2025reciprocal | CONFIRMED | BLOCKED (SD 403; no OA); publisher abstract obtained | **gratitude framing NOT in abstract** — verify in full text or rewrite Section 2's contrast |

### Corrections needed in references.bib (mechanical)

1. `hirsbrunner2025contestation`: Kleemann, Steven; Tahraoui, Milan Nebyl; add `volume = {10}`, article 1638257.
2. `huanglo2025failure`: author Huang, Zuwen; title → "Human vs. Robot Service Provider Agents in Service Failures: Comparing Customer Dissatisfaction and the Mediating Role of Forgiveness and Service Recovery Expectation".
3. `kim2025shadow`: author Kim, Hyunkyu; resolve year/volume pairing (2025 online-first *or* 2026, 42(10), 7269–7287).
4. `lee2019procedural`: Cha, Hae Jin; optionally cite as Article 182.
5. `lin2025oscillation`: author Lin, Hui; add `volume = {11}, number = {1}`.
6. `lin2026voice`: authors Lin, Wanliang; Zhang, Mingyu; Zhang, Wenjia; Zhang, Can.
7. `lisun2025accessibility`: authors Li, Huanhuan; Sun, Zongfeng; add article e70067.
8. `lv2024autonomy`: append subtitle "Strategies via Hedge Words and Communication Styles"; resolve 2024/2025 pairing.
9. `mameli2026framework`: author Mameli, Elisa; append subtitle "bridging academic insights and industry practices across sectors"; add article 19.
10. `lashley2000towards`: confirm pages (1–16 vs 1–17) against a physical copy.

### Substantive checks owed to the manuscript text (not the bib)

- **huanglo2025failure**: section 4's sentence must state the humanness *penalty* direction, not "human preference."
- **lin2026voice**: any silence claim must carry the feedback-raises-voice exception.
- **manfreda2025reciprocal**: the gratitude-vs-obligation contrast is unverified; confirm in full text or narrow to the abstract-safe mutual-altruistic-exchange framing.
- **lisun2025accessibility**: drop or verify the "works through procedural justice" mechanism sentence.
- **lind1990voice**: pair the post-decision voice claim with its boundary conditions (pre>post; frustration effect under blatant bias; Cohen's sham-voice warning — the last being independently useful for the paper's argument).
- **kim2021preference**: human-preference uses must be conditioned on the non-threat baseline.
