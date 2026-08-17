# Source-side bibliography audit — slice 01 (21 citekeys)

Audit date: 2026-08-17. Auditor: source-audit agent.

**Method.** Every identity verdict below rests on the publisher's own page or on the DOI
resolver's registration record (`doi.org` content negotiation, which serves the metadata the
publisher deposited when registering the DOI). No identity claim rests on Google Scholar,
OpenAlex, Semantic Scholar, ResearchGate, or search snippets. Aggregators (Unpaywall, web
search) were used only to *locate* full-text copies, never as evidence of what a source is.
Full-text attempts and their blockers are recorded per source. Environment notes that
constrain the whole slice: no Chrome extension was connected, so every publisher that
challenge-walls programmatic clients stayed walled — WebFetch and curl both received 403 or
JS-challenge pages from **ScienceDirect/linkinghub (Elsevier), SpringerLink, SAGE, INFORMS,
AEA, Taylor & Francis, Intellect Discover, SSRN, and (new since the last sweep) HAL**.
Emerald served its abstract page. Symphonya, Firenze UP, and the TU Delft and Cambridge
institutional repositories served full PDFs.

**Headline results.** Four entries carry wrong author names against the publisher record —
`devos2026employee` (7 of 10 given names wrong), `choichao2024reactions` (first author
"Jaee" should be **Jungmin** Choi, plus a truncated title), `leelu2024consciousness`
(first author "Woo Hyuk Lee" should be **Wangoo Lee** — a live name collision with a
different hospitality scholar), and `moscalarosa2019` (co-author "Elisa" should be
**Emily** La Rosa, and the pages are wrong: 82–94, not 103–116). Two more have stale or
wrong year/issue data: `mosca2026ai` (publisher's version of record self-cites as **2025**)
and `sharmamattila2025rights` (now assigned to issue 50(6), 904–920, 2026). The wrong given
names follow the same-initial substitution pattern of the project's three earlier
fabrication catches, and three of the four sit in entries whose notes say "verified".

---

## 1. alfrink2023contestable

```bibtex
@article{alfrink2023contestable,
  author  = {Alfrink, Kars and Keller, Ianus and Kortuem, Gerd and Doorn, Neelke},
  title   = {Contestable {AI} by Design: Towards a Framework},
  journal = {Minds and Machines},
  year    = {2023},
  volume  = {33},
  pages   = {613--639},
  doi     = {10.1007/s11023-022-09611-z},
  note    = {verified 2026-08-07 (Crossref DOI resolved). The constructive alternative: contestability across the lifecycle}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Springer deposit): "Contestable AI by
Design: Towards a Framework", Kars Alfrink, Ianus Keller, Gerd Kortuem, Neelke Doorn,
*Minds and Machines* 33(4), 613–639, CC-BY. Online 2022-08-13; the 33(4) issue is the
December 2023 issue, so year 2023 is right. Cross-checked against the TU Delft repository
record for the published version.

**FULL TEXT: OBTAINED** — TU Delft repository, final published version (CC-BY):
`https://repository.tudelft.nl/file/File_164f7b50-13bc-4c97-b634-7bef415e0cac` (28 pp.).
SpringerLink itself served a JS challenge to both curl and WebFetch despite the article
being gold OA.

**WHAT IT ARGUES** (from full text): Extracts, by qualitative-interpretative literature
synthesis and visual mapping, the sociotechnical elements of contestable AI and organizes
them into a framework of five system features (among them built-in safeguards and channels
for scrutiny by subjects or third parties) and six development practices (ex-ante
safeguards onward), mapped onto AI lifecycle stages. Evidence is a structured literature
review, not an empirical test.

**FLAGS**: Missing `number = {4}` — the resolver record carries the issue. Otherwise clean.

---

## 2. batat2019experiential

```bibtex
@book{batat2019experiential,
  author    = {Batat, Wided},
  title     = {Experiential Marketing: Consumer Behavior, Customer Experience and the 7Es},
  year      = {2019},
  publisher = {Routledge},
  address   = {London},
  doi       = {10.4324/9781315232201},
  note      = {P9; SI EDITOR (Batat). The 7Es scaffold under section 2's five criteria: [...] No second edition exists. verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Routledge deposit): "Experiential
Marketing", subtitle "Consumer Behavior, Customer Experience and The 7Es", Wided Batat,
Routledge, edition 1, published online 2019-01-10, eISBN 9781315232201. The Taylor &
Francis landing page (`taylorfrancis.com/books/9781351867368`) returned 403, so the
resolver record is the publisher-side evidence. Resolver's publisher-location string reads
"Abingdon, Oxon ; New York, NY", not London — `address` is close enough for Routledge
front matter but a copyeditor may prefer Abingdon/New York.

**FULL TEXT: BLOCKED** — Taylor & Francis 403 (WebFetch and curl); Unpaywall lists no OA
location for the book.

**WHAT IT ARGUES**: not characterized (no full text; no abstract in the resolver record).

**FLAGS**: `address = {London}` vs the deposit's Abingdon/New York — cosmetic. Nothing
substantive.

---

## 3. chengfoley2019

```bibtex
@article{chengfoley2019,
  author  = {Cheng, Mingming and Foley, Carmel},
  title   = {Algorithmic Management: The Case of {Airbnb}},
  journal = {International Journal of Hospitality Management},
  year    = {2019},
  volume  = {83},
  pages   = {33--36},
  doi     = {10.1016/j.ijhm.2019.04.009},
  note    = {Names short-term-rental hosting as algorithmically managed work, in a hospitality journal; crossref-verified 2026-08-07}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Elsevier deposit): "Algorithmic management:
The case of Airbnb", Mingming Cheng, Carmel Foley, IJHM 83, 33–36, print October 2019.
Every field matches.

**FULL TEXT: BLOCKED** — linkinghub.elsevier.com redirect page only; sciencedirect.com 403
to WebFetch and challenge-page to curl. Curtin espace holds the authors' 2018 companion
("The sharing economy and digital discrimination") but no repository copy of this 2019
paper was found (searched espace.curtin and opus.lib.uts).

**WHAT IT ARGUES**: not characterized (no full text, no abstract in the resolver record).
The resolver's deposited reference list (Foucault's *Discipline and Punish*, netnography
sources) is consistent with the note's framing but is not a substitute for reading it.

**FLAGS**: A four-page paper (33–36) — a research note / viewpoint length; fine if cited as
a framing source, worth knowing it is not an empirical study.

---

## 4. cui2020reducing

```bibtex
@article{cui2020reducing,
  author  = {Cui, Ruomeng and Li, Jun and Zhang, Dennis J.},
  title   = {Reducing Discrimination with Reviews in the Sharing Economy: Evidence from Field Experiments on {Airbnb}},
  journal = {Management Science},
  year    = {2020},
  volume  = {66},
  number  = {3},
  pages   = {1071--1094},
  doi     = {10.1287/mnsc.2018.3273},
  note    = {The guest-side anchor. [...] verified 2026-08-07}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (INFORMS deposit): exact title, Ruomeng Cui,
Jun Li, Dennis J. Zhang, *Management Science* 66(3), 1071–1094, March 2020. Every field
matches.

**FULL TEXT: BLOCKED** — pubsonline.informs.org 403 (WebFetch); the SSRN delivery URL for
the working paper (abstract 2882982) served a Cloudflare interstitial to curl.

**WHAT IT ARGUES** (from the publisher-deposited abstract in the resolver record): Four
randomized field experiments on 1,801 Airbnb hosts with fictitious guest accounts; requests
from guests with African-American-sounding names are 19.2 pp less likely to be accepted,
and a positive review on the guest's page closes the gap to statistical
indistinguishability, while self-claimed tidiness/friendliness information does not. The
bib note's characterization is accurate.

**FLAGS**: none.

---

## 5. edelman2017discrimination

```bibtex
@article{edelman2017discrimination,
  author  = {Edelman, Benjamin and Luca, Michael and Svirsky, Dan},
  title   = {Racial Discrimination in the Sharing Economy: Evidence from a Field Experiment},
  journal = {American Economic Journal: Applied Economics},
  year    = {2017},
  volume  = {9},
  number  = {2},
  pages   = {1--22},
  doi     = {10.1257/app.20160213},
  note    = {verified 2026-08-07 (Crossref DOI resolved). The principal guest-side study [...]}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (AEA deposit): exact title, Benjamin Edelman,
Michael Luca, Dan Svirsky, *AEJ: Applied Economics* 9(2), 1–22, April 2017. Every field
matches.

**FULL TEXT: OBTAINED** — author copy at
`https://www.benedelman.org/publications/airbnb-guest-discrimination-2016-09-16.pdf`,
header "forthcoming, American Economic Journal: Applied Economics" — i.e., the accepted
working-paper version, not the typeset VoR (pubs.aeaweb.org 403).

**WHAT IT ARGUES** (from full text, working-paper version): In a field experiment on
Airbnb, applications from guests with distinctively African-American names were 16% less
likely to be accepted than identical guests with distinctively White names; discrimination
appears across landlord sizes and is concentrated among hosts with no prior
African-American guest, implicating the platform's design choices (name display) rather
than host conduct alone.

**FLAGS**: The obtained copy predates the VoR; any quoted number should be re-checked
against the typeset version at proof (the 16%/16-percentage-point phrasing differs across
versions of this paper's press coverage — the working paper says "16% less likely").

---

## 6. filippas2022inflation

```bibtex
@article{filippas2022inflation,
  author  = {Filippas, Apostolos and Horton, John J. and Golden, Joseph},
  title   = {Reputation Inflation},
  journal = {Marketing Science},
  year    = {2022},
  volume  = {41},
  number  = {4},
  pages   = {733--745},
  doi     = {10.1287/mksc.2022.1350},
  note    = {The named pattern for reputation remedies degrading their own signal [...] verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED, one field short** — DOI resolver record (INFORMS deposit):
"Reputation Inflation", *Marketing Science* 41(4), 733–745, July 2022. Divergence: third
author is deposited as **"Joseph M. Golden"**; the bib drops the middle initial. Trivial
but exact-list rule says record it.

**FULL TEXT: OBTAINED** — author working-paper copy at
`https://apostolos-filippas.com/papers/inflation.pdf` (INFORMS VoR 403).

**WHAT IT ARGUES** (from full text, working-paper version): Average buyer ratings of
sellers rose substantially over time in five online marketplaces; the authors decompose the
rise into genuine satisfaction growth versus "reputation inflation" (higher ratings without
higher satisfaction) and, using transaction-level data from one marketplace, attribute much
of the rise to inflation, degrading the rating system's informativeness.

**FLAGS**: `Golden, Joseph` → should be `Golden, Joseph M.` per the deposit.

---

## 7. germannmolz2018scale

```bibtex
@article{germannmolz2018scale,
  author  = {Germann Molz, Jennie},
  title   = {Discourses of Scale in Network Hospitality: From the Airbnb Home to the Global Imaginary of ``Belong Anywhere''},
  journal = {Hospitality \& Society},
  year    = {2018},
  volume  = {8},
  number  = {3},
  pages   = {229--251},
  doi     = {10.1386/hosp.8.3.229_1},
  note    = {P9; TARGET JOURNAL. [...] Pagination discrepancy: article page says 229-251, issue TOC says 229-252; check at proof. verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Intellect deposit): exact title (typeset
with single quotes around 'belong anywhere'), Jennie Germann Molz, *Hospitality & Society*
8(3), 229–251, September 2018. All fields match the bib. The Intellect Discover landing
page 403'd, so the note's known 229-251/229-252 TOC discrepancy could not be re-inspected;
the deposit says 229–251, which is what the bib carries.

**FULL TEXT: BLOCKED** — intellectdiscover.com 403; Holy Cross CrossWorks
`viewcontent.cgi` 403; the academia.edu author manuscript is login-walled.

**WHAT IT ARGUES** (from the publisher-deposited abstract in the resolver record): Analyzes
how Airbnb stakeholders construct spatial scales — from the host's home through
neighbourhood and city to the "Belong Anywhere" global imaginary — plus temporal and
digital scales, arguing that scale-talk is deployed to assert power, assign moral
responsibility, and make claims to belonging. Discourse analysis of scholarship, news, and
corporate marketing materials.

**FLAGS**: Keep the note's check-at-proof instruction on the terminal page.

---

## 8. roelofsenminca2018

```bibtex
@article{roelofsenminca2018,
  author  = {Roelofsen, Maartje and Minca, Claudio},
  title   = {The Superhost: Biopolitics, Home and Community in the {Airbnb} Dream-World of Global Hospitality},
  journal = {Geoforum},
  year    = {2018},
  volume  = {91},
  pages   = {170--181},
  doi     = {10.1016/j.geoforum.2018.02.021},
  note    = {The badge grades the host and withholds a seat; crossref-verified 2026-08-07}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Elsevier deposit): "The Superhost.
Biopolitics, home and community in the Airbnb dream-world of global hospitality", Maartje
Roelofsen, Claudio Minca, *Geoforum* 91, 170–181, May 2018. The deposited title uses a
period after "The Superhost" where the bib uses a colon — a house-style normalization, not
an error.

**FULL TEXT: BLOCKED** — ScienceDirect 403/challenge; the Macquarie University research
portal record lists no downloadable file; no other repository copy found.

**WHAT IT ARGUES**: not characterized (no full text; Elsevier deposits no abstracts to
Crossref).

**FLAGS**: none beyond the punctuation note.

---

## 9. batat2021ar

```bibtex
@article{batat2021ar,
  author  = {Batat, Wided},
  title   = {How Augmented Reality ({AR}) Is Transforming the Restaurant Sector: Investigating the Impact of ``Le Petit Chef'' on Customers' Dining Experiences},
  journal = {Technological Forecasting and Social Change},
  year    = {2021},
  volume  = {172},
  pages   = {121013},
  doi     = {10.1016/j.techfore.2021.121013},
  note    = {P9; SI EDITOR (Batat). Her own hospitality-venue technology study [...] verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Elsevier deposit): exact title, Wided Batat,
*Technological Forecasting and Social Change* 172, article 121013, November 2021. Matches.

**FULL TEXT: BLOCKED** — ScienceDirect 403/challenge. A deposited copy of the published PDF
exists at HAL (`normandie-univ.hal.science/hal-04455601`, file
`S0040162521004455.pdf` — located via the HAL API, which returns the file URL), but HAL now
fronts an Anubis bot-wall: curl received "Making sure you're not a bot!" and WebFetch
"Access Denied". A human in a browser will get this PDF trivially; this session could not.

**WHAT IT ARGUES**: not characterized (no full text obtained, no abstract in the resolver
record).

**FLAGS**: none on identity. Full text is one browser-click away if anyone needs it — the
HAL URL above.

---

## 10. choichao2024reactions

```bibtex
@article{choichao2024reactions,
  author  = {Choi, Jaee and Chao, Melody Manchi},
  title   = {For Me or against Me? Reactions to {AI} (vs. Human) Decisions},
  journal = {Personality and Social Psychology Bulletin},
  year    = {2024},
  doi     = {10.1177/01461672241288338},
  note    = {P9; PRODUCTIVE COMPLICATION. Six experiments, N=2,794 [...] verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: DIVERGENT** — DOI resolver record (SAGE deposit), corroborated by the
publisher-formatted PDF itself (see below):

- **First author**: publisher says **Jungmin Choi**. The bib's "Jaee Choi" is wrong — and
  "Jaee Choi" is the name of a real, different researcher (hospitality field), so this is a
  name-collision-grade error, same class as the project's earlier catches.
- **Second author**: publisher prints "Melody M. Chao" (the bib's "Melody Manchi" is the
  correct expansion of the M. — Chao's full name — so this half is defensible, but the VoR
  prints the initial).
- **Title**: the bib truncates it. Full deposited/printed title: "For Me or Against Me?
  Reactions to AI (vs. Human) Decisions **That Are Favorable or Unfavorable to the Self and
  the Role of Fairness Perception**".
- **Issue assignment**: the article has left OnlineFirst — now *PSPB* **52(3), 671–691**,
  print March 2026 (online 2024-10-24). The bib carries year 2024 with no volume/pages.

**FULL TEXT: OBTAINED** — publisher-formatted PDF via the University of Cambridge Apollo
repository:
`https://www.repository.cam.ac.uk/bitstreams/2f8fdfda-15d7-48c4-afe5-330c8bd1c7e9/download`
(journals.sagepub.com 403 for both landing and PDF).

**WHAT IT ARGUES** (from full text): Six experiments (N = 2,794) grounded in fairness
heuristic theory. When the decision outcome is unfavorable, an AI decider is perceived as
fairer than a human and draws a less negative reaction, an effect carried by AI's perceived
unemotionality; reminders of AI bias attenuate the AI–human fairness gap. The bib note's
characterization is accurate; only the author name and citation fields are wrong.

**FLAGS**: Fix the first author to **Choi, Jungmin**; restore the full title; add
`volume={52}, number={3}, pages={671--691}` and decide 2024 (online) vs 2026 (issue) per
the journal's citation style. The wrong given name in a "verified" entry is exactly the
secondary-source contamination pattern this audit exists to catch.

---

## 11. devos2026employee

```bibtex
@article{devos2026employee,
  author  = {De Vos, Svetlana and Haykal, Karl-Anthony and Qesja, Blerina and Soleimani, Sadaf and Harris, Jane and Lipnickas, Gintare and Brodhead Ahmadi, Seyedeh Roya and Brochado, Ana and Rao Hill, Sally and Rajic, Sanja},
  title   = {Enhancing Phygital Employee Experience in High-Involvement Professional Service Organizations},
  journal = {Journal of Services Marketing},
  year    = {2026},
  pages   = {1--23},
  doi     = {10.1108/JSM-09-2025-0707},
  note    = {SI EDITOR (De Vos). STRONG [...] Ahead-of-print, online 2026-04-20. verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: DIVERGENT — the worst entry in this slice.** The Emerald publisher page
(`https://www.emerald.com/insight/content/doi/10.1108/JSM-09-2025-0707/full/html`, reached
directly) and the DOI resolver record agree with each other and against the bib on **seven
of ten given names**. Family names, author count, and order are all correct; the given
names attached to them are not:

| # | Bib says | Publisher says |
|---|----------|----------------|
| 2 | Karl-Anthony Haykal | **Kay-Anne Haykal** |
| 3 | Blerina Qesja | **Bora Qesja** |
| 4 | Sadaf Soleimani | **Samaneh Soleimani** |
| 5 | Jane Harris | **Joanne Harris** |
| 6 | Gintare Lipnickas | **Gediminas Lipnickas** |
| 7 | Seyedeh Roya Brodhead Ahmadi | **Sarah Renee Brodhead Ahmadi** |
| 10 | Sanja Rajic | **Sandro Rajic** |

De Vos, Brochado, and Rao Hill are correct. Every wrong name shares an initial with the
right one — the same same-initial substitution signature as the project's three prior
fabrication catches. Title, journal, year, ahead-of-print pages 1–23, and DOI all match
(online 2026-04-20, still no volume/issue).

**Companion flag**: `brochado2026phygital` (not in this slice) lists the same nine-author
team and therefore almost certainly carries the same corrupted given names. Whoever audits
that slice should check it against `10.1108/JSM-09-2025-0709`.

**FULL TEXT: BLOCKED** — Emerald serves the abstract page but the full text is paywalled;
Unpaywall lists no OA copy.

**WHAT IT ARGUES** (from the publisher abstract): Qualitative study of employee experience
during phygital transformation in two professional-service settings (independent coaching
practices; a large public medical institution). Identifies required employee capabilities
(digital literacy, data fluency, cross-channel orchestration), an "implementation gap"
whose poor execution cascades into frustration, and finds that connecting technology to a
higher purpose ("spiritual alignment") sustains employee engagement — the finding the
manuscript leans on, confirmed at the publisher.

**FLAGS**: Correct all seven given names before lock. Still ahead-of-print — volume/issue
must be re-checked at proof. The note's "verified 2026-08-09" plainly did not check the
author list against the publisher.

---

## 12. introna2010measure

```bibtex
@article{introna2010measure,
  author  = {Introna, Lucas D.},
  title   = {The `Measure of a Man' and the Ethos of Hospitality: Towards an Ethical Dwelling with Technology},
  journal = {AI \& Society},
  year    = {2010},
  volume  = {25},
  number  = {1},
  pages   = {93--102},
  doi     = {10.1007/s00146-009-0242-1},
  note    = {Philosophy of tech runs hospitality the other way [...] verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Springer deposit): "The 'measure of a man'
and the ethos of hospitality: towards an ethical dwelling with technology", Lucas D.
Introna, *AI & SOCIETY* 25(1), 93–102, online November 2009, print April 2010. Every bib
field matches.

**FULL TEXT: BLOCKED** — SpringerLink JS-challenge; Lancaster EPrints has a metadata-only
record (eprints.lancs.ac.uk/45631, no file); remaining copies are ResearchGate/academia.edu
login walls.

**WHAT IT ARGUES**: not characterized — no full text and no abstract in the resolver
record. (Search snippets describe the Star Trek "Measure of a Man" framing the title
announces, but that is aggregator text, so it does not qualify under this audit's rules.)

**FLAGS**: none on identity.

---

## 13. kropf2026blame

```bibtex
@article{kropf2026blame,
  author  = {Kropf, Mario and Sp{\"o}ck, Christoph and Werner, Roman},
  title   = {Blame the Robot: Role Responsibility and Ethical Issues Regarding AI-Based Care Robots},
  journal = {International Journal of Social Robotics},
  year    = {2026},
  volume  = {18},
  number  = {2},
  pages   = {30},
  doi     = {10.1007/s12369-026-01369-z},
  note    = {THE machine-ethics counterexample [...] Article number 30. verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Springer deposit): exact title, Mario Kropf,
Christoph Spöck, Roman Werner, *International Journal of Social Robotics* 18(2), article
number 30, February 2026 (online 2026-02-16). The bib's `pages = {30}` is the article
number, which the note already discloses.

**FULL TEXT: BLOCKED** — the article is OA (CC-BY per Unpaywall, pointing only back to
SpringerLink), but SpringerLink JS-challenges programmatic clients and no institutional
repository copy was found (searched Graz unipub and general web).

**WHAT IT ARGUES** (from the publisher-deposited abstract in the resolver record):
Distinguishes role responsibility from moral responsibility and argues care robots can
bear the former in virtue of their social function in caregiving, even though they cannot
bear the latter — the position the manuscript uses as its machine-ethics counterexample.
The note's characterization matches the deposited abstract.

**FLAGS**: Consider `articleno`/`eid` style at proof rather than `pages={30}`, per the
target journal's BibTeX conventions.

---

## 14. leelu2024consciousness

```bibtex
@article{leelu2024consciousness,
  author  = {Lee, Woo Hyuk and Lu, Lu},
  title   = {The Hospitable Thought That Counts: An Emerging Theory of ``{AI} Consciousness'' in Genuine Hospitality},
  journal = {International Journal of Hospitality Management},
  year    = {2024},
  volume  = {123},
  pages   = {103928},
  doi     = {10.1016/j.ijhm.2024.103928},
  note    = {P9; CLOSEST SINGLE COMPETITOR [...] Article number to re-check at proof. verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: DIVERGENT** — DOI resolver record (Elsevier deposit): first author is
**Wangoo Lee**, not "Woo Hyuk Lee". The PolyU Institutional Research Archive record for
this exact article (handle 10397/110073, reached directly) confirms "Lee, W" at PolyU —
Wangoo Lee's institution. **"Woo Hyuk Lee" is a different, active hospitality researcher**,
so as written the bib credits the wrong person — a referee-visible name collision. All
other fields match: IJHM 123, article 103928, October 2024, second author Lu Lu.

**FULL TEXT: BLOCKED** — ScienceDirect 403/challenge; the PolyU repository copy is
embargoed until 2027-10-31.

**WHAT IT ARGUES**: not characterized under this audit's rules — no full text and no
abstract in the resolver record. (Search summaries describe a "Consciousness Attribution
Model of AI Hospitableness"; treat that as unverified until someone reads the paper.)

**FLAGS**: Fix the first author to **Lee, Wangoo**. The existing note's competitor framing
("attributional rather than positional") rests on an abstract this project has not obtained
from the publisher — flag the characterization itself as second-hand.

---

## 15. liu2026hospitableness

```bibtex
@article{liu2026hospitableness,
  author  = {Liu, Gus Guanrong and Benckendorff, Pierre and Walters, Gabby},
  title   = {Conceptualizing Hospitableness in Human-Robot Hospitality Interactions},
  journal = {International Journal of Hospitality Management},
  year    = {2026},
  volume  = {135},
  pages   = {104640},
  doi     = {10.1016/j.ijhm.2026.104640},
  note    = {Newest hospitality-specific capacity name, robotic hospitableness [...] verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Elsevier deposit): "Conceptualizing
hospitableness in human–robot hospitality interactions", Gus Guanrong Liu, Pierre
Benckendorff, Gabby Walters, IJHM 135, article 104640, May 2026. Matches (bib hyphen vs
en-dash in "human–robot" is cosmetic).

**FULL TEXT: BLOCKED** — the article is OA at the publisher (Unpaywall points to the
doi.org landing), but ScienceDirect 403/challenge-walls programmatic clients. No repository
copy found (UQ espace not surfaced in searches).

**WHAT IT ARGUES**: not characterized (no full text obtained; no abstract in the resolver
record). The note's "robotic hospitableness / co-creators" characterization is carried over
from the prior sweep, unverified here.

**FLAGS**: none on identity. OA in any human browser — one click for whoever holds a
browser session.

---

## 16. mosca2026ai

```bibtex
@article{mosca2026ai,
  author  = {Mosca, Fabrizio},
  title   = {Artificial Intelligence as a Strategic Inflection Point: Implications for Firms, Industries, and Global Competitiveness},
  journal = {Journal of Emerging Perspectives},
  year    = {2026},
  volume  = {2},
  pages   = {3--7},
  doi     = {10.36253/jep-20876},
  note    = {P9; SI EDITOR (Mosca). Names transparency and human oversight as the governance answer [...] verified 2026-08-11; readdepth=full-text}
}
```

**IDENTITY: DIVERGENT on year** — Firenze University Press publisher page (reached
directly, OA) and the version-of-record PDF: title, author, *Journal of Emerging
Perspectives* vol 2, pp. 3–7 all match, **but the VoR's own citation line reads "Mosca, F.
(2025)"**, the page's citation_date meta is 2025, the volume is labeled "Vol. 2 (2025)",
and the article states "Published: December 20, 2025". Crossref's issued date is 2026-07-18
(a late deposit), which is presumably where the bib's 2026 came from. The publisher's
self-citation is 2025.

**FULL TEXT: OBTAINED** — publisher OA PDF
(`https://oaj.fupress.net/index.php/jep/article/download/20876/15125`, CC-BY), read.

**WHAT IT ARGUES** (from full text): An editor's essay framing generative/agentic AI as a
strategic inflection point across five questions (managerial processes, investment
geography, infrastructure gaps, frontier players, governance hurdles), drawing on
international-organization and policy sources rather than original data. It does name
"transparency, accountability, and stringent human oversight" (in its EU AI Act
discussion) and describes human work shifting to "framing, validation, and interpretation"
— the two claims the manuscript's note attributes to it check out verbatim.

**FLAGS**: Change `year` to **2025** (and cite as such) unless the manuscript's reference
style keys on Crossref's issued date; the publisher's own citation line is 2025. Note
also this is an editorial essay, not a peer-reviewed empirical article — cite it as an
editor's words (which is how the note uses it).

---

## 17. moscalarosa2019

```bibtex
@article{moscalarosa2019,
  author  = {Mosca, Fabrizio and La Rosa, Elisa},
  title   = {4.0 Technology within Fashion and Luxury Production},
  journal = {Symphonya. Emerging Issues in Management},
  year    = {2019},
  number  = {2},
  pages   = {103--116},
  doi     = {10.4468/2019.2.08mosca.larosa},
  note    = {P9; SI EDITOR (Mosca). THE LIVE OBJECTION: recommends keeping technological implementation UNDISCLOSED [...] verified 2026-08-11; readdepth=full-text}
}
```

**IDENTITY: DIVERGENT** — Symphonya publisher page
(`https://symphonya.unicusano.it/article/view/13276`, reached directly) and the VoR PDF:

- **Co-author**: **Emily La Rosa**, not "Elisa La Rosa". The PDF byline reads "Fabrizio
  Mosca**, Emily La Rosa***".
- **Pages**: **82–94**, not 103–116. Publisher citation meta: firstpage 82, lastpage 94;
  the Crossref deposit also says 82.

Title, journal, year 2019, issue 2 all match.

**FULL TEXT: OBTAINED** — publisher OA PDF
(`https://symphonya.unicusano.it/article/download/13276/11868`), read.

**WHAT IT ARGUES** (from full text): Survey-based study (managers plus potential customers)
of Industry 4.0 adoption in luxury fashion manufacturing: managers judge 4.0 technologies
compatible with product quality, customers view them negatively, and the authors conclude
firms should "implement these systems without disclosing them to customers." The
manuscript's use of it as the live concealment objection is exactly right.

**FLAGS**: Fix the co-author to **La Rosa, Emily** and the pages to **82--94**. The note
claims full-text read and "verified 2026-08-11" — yet both the name and the pages were
wrong, so the prior verification never touched the publisher record. (Where 103–116 came
from is unclear; possibly a different edition's pagination or a secondary index.)

---

## 18. santonidesio2021gaps

```bibtex
@article{santonidesio2021gaps,
  author  = {Santoni de Sio, Filippo and Mecacci, Giulio},
  title   = {Four Responsibility Gaps with Artificial Intelligence: Why They Matter and How to Address Them},
  journal = {Philosophy \& Technology},
  year    = {2021},
  volume  = {34},
  number  = {4},
  pages   = {1057--1084},
  doi     = {10.1007/s13347-021-00450-x},
  note    = {Claim-28 sentence one IS this thesis [...] verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Springer deposit): "Four Responsibility Gaps
with Artificial Intelligence: Why they Matter and How to Address them", Filippo Santoni de
Sio, Giulio Mecacci, *Philosophy & Technology* 34(4), 1057–1084, online May 2021, print
December 2021. All bib fields match.

**FULL TEXT: OBTAINED** — TU Delft repository, final published version:
`https://repository.tudelft.nl/file/File_dd477ea4-487b-4ce2-80b8-bf691a6c790e` (also
mirrored at d-nb.info/1241162026/34; SpringerLink itself JS-challenged).

**WHAT IT ARGUES** (from full text): The "responsibility gap" is not one problem but at
least four — culpability, moral accountability, public accountability, and active
responsibility gaps — with distinct technical, organizational, legal, and societal sources,
each needing its own remedy. The note's "active-responsibility gap = the forward-looking
obligation" is faithful to the paper's own taxonomy.

**FLAGS**: none.

---

## 19. sharmamattila2025rights

```bibtex
@article{sharmamattila2025rights,
  author  = {Sharma, Amit and Mattila, Anna S.},
  title   = {Rights and Responsibilities of Hospitality Service Robots},
  journal = {Journal of Hospitality \& Tourism Research},
  year    = {2025},
  doi     = {10.1177/10963480251393749},
  note    = {P9; [...] OnlineFirst 2025-10-23. FULL PUBLISHER ABSTRACT retrieved via OpenAlex 2026-08-17 [...] verified 2026-08-11; abstract re-verified 2026-08-17; readdepth=publisher-abstract}
}
```

**IDENTITY: DIVERGENT (stale — the article has landed in an issue)** — DOI resolver record
(SAGE deposit): "Rights and Responsibilities of Hospitality Service Robots", Amit Sharma,
Anna Mattila, *Journal of Hospitality & Tourism Research* **50(6), 904–920**, print
**August 2026**; deposited online date **2026-01-16**. Three consequences:

- The bib's `year = {2025}` with no volume/pages is now behind the record: the citation
  should read 50(6), 904–920, 2026 (or keep the online year per style — but the fields
  must be added).
- The note's "OnlineFirst 2025-10-23" does not match the deposit's online date of
  2026-01-16. The 2025 date presumably came from OpenAlex; one more instance of a
  secondary index disagreeing with the registration record.
- Authors: deposit says "Anna Mattila"; the bib's "Anna S. Mattila" is her standard
  published form — not an error, just noting the deposit lacks the initial.

**FULL TEXT: BLOCKED, again** — journals.sagepub.com serves Cloudflare to every
programmatic client, PDF URL included (`/doi/pdf/10.1177/10963480251393749?download=true`
returned the challenge HTML), exactly as the prior note records. The article is CC-BY
hybrid OA; a human browser gets it, this session could not.

**WHAT IT ARGUES** (from the publisher-deposited abstract in the resolver record — now
first-hand, upgrading the note's OpenAlex-sourced version, with which it agrees): Examines
whether hospitality service robots should be afforded rights and responsibilities through
a stakeholder-theory lens; its stated emphasis is governance and risk management —
clarifying accountability (liability, safety, data protection, consent), guest trust, and
regulatory preparation. This confirms the note's account and the removal of the
employee-duty-delegation framing.

**FLAGS**: Update to 50(6), 904–920, 2026 at proof. The abstract's provenance can now be
recorded as DOI-resolver, not OpenAlex.

---

## 20. zientara2023unpicking

```bibtex
@article{zientara2023unpicking,
  author  = {Zientara, Piotr and Adamska-Mieruszewska, Joanna and B{\k a}k, Monika},
  title   = {Unpicking the Mechanism Underlying Hospitality Workers' Intention to Join a Union and Intention to Quit a Job. Evidence from the {UK}},
  journal = {International Journal of Hospitality Management},
  year    = {2023},
  volume  = {108},
  pages   = {103355},
  doi     = {10.1016/j.ijhm.2022.103355},
  note    = {P8; Hirschman-framed and hospitality-native [...] verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (Elsevier deposit): exact title, Piotr
Zientara, Joanna Adamska-Mieruszewska, Monika Bąk, IJHM 108, article 103355, January 2023.
All fields match.

**FULL TEXT: BLOCKED** — the article is OA at ScienceDirect (Unpaywall lists the publisher
PDF), but ScienceDirect 403/challenge-walls programmatic clients; no repository copy found.

**WHAT IT ARGUES**: not characterized under this audit's rules — no full text obtained and
no abstract in the resolver record. (Search snippets report stress/dissatisfaction raising
quit intention but not union-joining intention, which is consistent with the note's
exit-not-voice framing — but that is aggregator text and stays unverified.)

**FLAGS**: none on identity. OA in a human browser.

---

## 21. ananny2018seeing

```bibtex
@article{ananny2018seeing,
  author  = {Ananny, Mike and Crawford, Kate},
  title   = {Seeing without Knowing: Limitations of the Transparency Ideal and Its Application to Algorithmic Accountability},
  journal = {New Media \& Society},
  year    = {2018},
  volume  = {20},
  number  = {3},
  pages   = {973--989},
  doi     = {10.1177/1461444816676645},
  note    = {verified 2026-08-07 (Crossref DOI resolved). Disclosure supplies visibility and leaves the forum absent}
}
```

**IDENTITY: CONFIRMED** — DOI resolver record (SAGE deposit): exact title, Mike Ananny,
Kate Crawford, *New Media & Society* 20(3), 973–989; online December 2016, issue 2018. All
bib fields match.

**FULL TEXT: BLOCKED** — journals.sagepub.com 403; Unpaywall lists no OA location;
Microsoft Research's publication page links only back to SAGE; mike.ananny.org exposes no
papers list; the USC Annenberg file surfaced by search is Ananny's CV, not the paper; .edu
course-mirror searches found citations but no hosted PDF. This widely-taught paper appears
to have no legitimate open copy.

**WHAT IT ARGUES** (from the publisher-deposited abstract in the resolver record):
Critically interrogates the transparency ideal — the assumption that seeing a system
equates to knowing and governing it — traces its epistemological roots, presents ten
limitations of transparency as applied to algorithmic systems, and sketches an alternative
typology of algorithmic accountability. The note's gloss (visibility without a forum) is a
fair compression.

**FLAGS**: none.

---

## Summary table

| citekey | identity | full text | flags |
|---|---|---|---|
| alfrink2023contestable | CONFIRMED | OBTAINED (TU Delft repo, VoR) | add `number={4}` |
| batat2019experiential | CONFIRMED (resolver; T&F 403) | BLOCKED (T&F 403) | address Abingdon/NY vs London, cosmetic |
| chengfoley2019 | CONFIRMED | BLOCKED (ScienceDirect) | 4-page viewpoint, not empirical |
| cui2020reducing | CONFIRMED | BLOCKED (INFORMS 403, SSRN Cloudflare) | none; abstract verified at resolver |
| edelman2017discrimination | CONFIRMED | OBTAINED (author WP copy, pre-VoR) | re-check quoted numbers against VoR at proof |
| filippas2022inflation | CONFIRMED | OBTAINED (author WP copy, pre-VoR) | add middle initial: Golden, Joseph M. |
| germannmolz2018scale | CONFIRMED | BLOCKED (Intellect 403, CrossWorks 403) | keep terminal-page check at proof |
| roelofsenminca2018 | CONFIRMED | BLOCKED (ScienceDirect; MQ record file-less) | title period-vs-colon, cosmetic |
| batat2021ar | CONFIRMED | BLOCKED (ScienceDirect; HAL Anubis wall — URL in §9) | none |
| choichao2024reactions | **DIVERGENT** | OBTAINED (Cambridge Apollo, publisher PDF) | **first author is Jungmin Choi, not Jaee**; truncated title; now 52(3), 671–691, 2026 |
| devos2026employee | **DIVERGENT** | BLOCKED (Emerald paywall; publisher abstract obtained) | **7 of 10 given names wrong**; companion brochado2026phygital likely same; ahead-of-print |
| introna2010measure | CONFIRMED | BLOCKED (Springer challenge; Lancaster metadata-only) | characterization is second-hand, unread |
| kropf2026blame | CONFIRMED | BLOCKED (Springer challenge, despite CC-BY) | pages={30} is an article number |
| leelu2024consciousness | **DIVERGENT** | BLOCKED (ScienceDirect; PolyU embargo to 2027-10) | **first author is Wangoo Lee, not Woo Hyuk Lee** — live name collision |
| liu2026hospitableness | CONFIRMED | BLOCKED (ScienceDirect, though gold OA) | characterization second-hand, unread |
| mosca2026ai | **DIVERGENT (year)** | OBTAINED (Firenze UP OA PDF) | **VoR self-cites as 2025**, bib says 2026; editorial essay, not peer-reviewed data |
| moscalarosa2019 | **DIVERGENT** | OBTAINED (Symphonya OA PDF) | **Emily (not Elisa) La Rosa; pages 82–94 (not 103–116)** — in a "readdepth=full-text, verified" entry |
| santonidesio2021gaps | CONFIRMED | OBTAINED (TU Delft repo, VoR) | none |
| sharmamattila2025rights | **DIVERGENT (stale)** | BLOCKED (SAGE Cloudflare, as before) | now 50(6), 904–920, 2026; deposit online date 2026-01-16 contradicts note's 2025-10-23 |
| zientara2023unpicking | CONFIRMED | BLOCKED (ScienceDirect, though OA) | characterization second-hand, unread |
| ananny2018seeing | CONFIRMED | BLOCKED (SAGE; no OA copy exists anywhere found) | none |

**Counts**: 14 CONFIRMED, 7 DIVERGENT, 0 UNCONFIRMED. Full text obtained for 7 of 21 (4
versions of record, 2 author working papers, 1 publisher-formatted repository copy);
publisher abstracts additionally secured for 6 of the blocked 14; 6 sources remain
uncharacterized from primary evidence (chengfoley2019, roelofsenminca2018, batat2021ar,
introna2010measure, leelu2024consciousness, liu2026hospitableness, zientara2023unpicking —
seven, counting all).

**Bib edits required before manuscript lock** (in priority order):
1. `devos2026employee` — seven given names (table in §11).
2. `choichao2024reactions` — first author Jungmin Choi; full title; 52(3), 671–691.
3. `leelu2024consciousness` — first author Lee, Wangoo.
4. `moscalarosa2019` — La Rosa, Emily; pages 82--94.
5. `mosca2026ai` — year 2025 per the publisher's own citation line.
6. `sharmamattila2025rights` — add volume 50, number 6, pages 904--920; year per style.
7. `filippas2022inflation` — Golden, Joseph M.
8. `alfrink2023contestable` — add number 4.
