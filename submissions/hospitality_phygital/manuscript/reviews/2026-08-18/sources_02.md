# Source-side audit — slice 02 (21 citekeys)

Audited 2026-08-17 against `literature/references.bib`. The binding rule: identity counts as
verified only against the publisher record or the DOI resolver.

**How the blocked publishers were handled.** Sage, Taylor & Francis, MDPI, Wiley, ACM, Intellect,
MIT Press, and Springer all return 403 to automated fetching of their article pages (no browser
extension was connected this session). For those, identity rests on DOI content negotiation at
doi.org — `Accept: application/vnd.citationstyles.csl+json`, which returns the metadata the
publisher itself deposited with the DOI registry — plus, where one exists, a Wayback capture of
the publisher's own page. Each entry below names its basis. Emerald, Symphonya, Intellect's DOI
metadata, and columbialawreview.org were reachable directly. Aggregators (Unpaywall, Semantic
Scholar, DOAJ) were used only to locate full texts, never as identity evidence.

**Headline findings.**

1. **brochado2026phygital: six of nine given names are wrong** — the author list in the bib does
   not match the publisher record and looks fabricated at the given-name level.
2. **andreev2025destination: one given name is wrong** (bib "Panagiotis Kosmas"; publisher
   "Petros Kosmas").
3. **casalegno2020circular: pages are wrong** (bib 143–158; published PDF 149–164) despite a card
   claiming a full-text read.
4. **bovens2007accountability is fully resolved**: the published ELJ version is openly available
   from the Utrecht University repository, was obtained and read in full, and the actor–forum
   definition the manuscript rests on is verbatim-correct.

---

## anderson2015transformative

```bibtex
@article{anderson2015transformative,
  author  = {Anderson, Laurel and Ostrom, Amy L.},
  title   = {Transformative Service Research: Advancing Our Knowledge about Service and Well-Being},
  journal = {Journal of Service Research},
  year    = {2015},
  volume  = {18},
  number  = {3},
  pages   = {243--249},
  doi     = {10.1177/1094670515591316},
  note    = {P7; TSR anchor ... verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata (publisher-deposited): Laurel Anderson, Amy L.
Ostrom; Journal of Service Research 18(3), 243–249, 2015. The registry deposit carries only the
short title "Transformative Service Research"; the subtitle is confirmed by the Wayback capture of
the publisher's own page (`journals.sagepub.com/doi/full/10.1177/1094670515591316`, title:
"Transformative Service Research: Advancing Our Knowledge About Service and Well-Being"). Live
Sage page returns 403 to automation.

**FULL TEXT: OBTAINED** — the Wayback capture of the Sage page contains the complete HTML text of
this free-access guest editorial (~37k characters); read in substance.

**WHAT IT ARGUES** (full text): The guest editorial for the JSR special issue defines TSR as any
research investigating the relationship between service and well-being, aimed at "uplifting
changes" for "individuals (both consumers and employees), families, communities, society, and the
ecosystem more broadly," and states that "indicators of both increasing and decreasing well-being
take center stage." It then organizes the ten special-issue articles under three themes:
codestruction/negative service, collectives and social phenomena, and coproduction/cocreation.

**FLAGS:** None material. The two claims the bib note takes from it (the remit list; the
increasing-and-decreasing-well-being sentence) are both verbatim-present in the text ("center
stage," US spelling).

---

## andreev2025destination

```bibtex
@article{andreev2025destination,
  author  = {Andreev, Hristo and Kosmas, Panagiotis and Livieratos, Antonios D. and Theocharous, Antonis L. and Zopiatis, Anastasios},
  title   = {Destination (Un)Known: Auditing Bias and Fairness in {LLM}-Based Travel Recommendations},
  journal = {AI},
  year    = {2025},
  volume  = {6},
  number  = {9},
  pages   = {236},
  doi     = {10.3390/ai6090236},
  note    = {P9; ... 216 traveller profiles, measurable bias in every category ... verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: DIVERGENT.**
- **Kosmas's given name is wrong.** Publisher-deposited DOI metadata: **Petros Kosmas**. The
  published PDF byline reads "Petros Kosmas"; his institution's repository record reads "Kosmas,
  Petros C." The bib says "Panagiotis" — a different person's name.
- Minor: the published byline reads "Antonis Theocharous" without the middle initial; the Cyprus
  University of Technology repository lists "Theocharous, Antonis L." The bib's "Antonis L." is
  defensible but does not match the byline.
- Everything else matches: title, *AI* 6(9), article 236, published 2025-09-19.

MDPI's site returns 403 to automation (WebFetch and curl both); identity basis is DOI content
negotiation plus the published PDF itself (below).

**FULL TEXT: OBTAINED** — the published MDPI version (CC BY, 30 pp.) from the co-author
institution's repository: `https://ktisis.cut.ac.cy/bitstream/handle/20.500.14279/35601/ai-06-00236.pdf`.
Read title page, abstract, and introduction.

**WHAT IT ARGUES** (full text): A controlled, persona-based audit of ChatGPT and DeepSeek
generating 6,480 recommendations for 216 traveller profiles varying origin, age, gender identity,
and trip theme; six bias families (popularity, geographic, cultural, stereotype, demographic,
reinforcement) quantified via tourism rankings, Hofstede scores, a 150-term cliché lexicon, and
information-theoretic distances. Finds measurable bias in every category and concludes
unconstrained LLMs are "active amplifiers of structural imbalances"; proposes a public-interest
re-ranking layer. The bib note's evidence claims (216 profiles; bias in every category tested)
are accurate.

**FLAGS:** Correct the author to **Kosmas, Petros C.** (or "Petros" to match the byline). This is
the failure mode the project has been burned by three times; the note's "verified 2026-08-11"
cannot have touched the publisher record.

---

## are2025appeals

```bibtex
@article{are2025appeals,
  author  = {Are, Carolina},
  title   = {``Dysfunctional'' Appeals and Failures of Algorithmic Justice in Instagram and TikTok Content Moderation},
  journal = {Information, Communication \& Society},
  year    = {2025},
  volume  = {28},
  number  = {11},
  pages   = {1997--2014},
  doi     = {10.1080/1369118X.2024.2396621},
  note    = {P9; DIRECT HEIR TO vaccaro2020contesting ... "algorithmic cop, jury and judge" ... verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: Carolina Are; Information, Communication &
Society 28(11), 1997–2014; online 2024-08-30, print issue 2025. The version-of-record PDF (below)
carries the identical citation line. T&F's site returns 403 to automation.

**FULL TEXT: OBTAINED** — the version of record (open access, CC BY) from the Northumbria
University research portal (`researchportal.northumbria.ac.uk/ws/portalfiles/portal/169889739/...`).
Read front matter, abstract, and introduction.

**WHAT IT ARGUES** (full text): Interviews with de-platformed users across activism, sex work,
sex education, and LGBTQIA+ self-expression, examined through fairness and due-process
literatures; finds platform appeals opaque and loophole-ridden, leaving room for discrimination,
fraud and scams, with platforms acting — the abstract's own metaphor — as "algorithmic cop, jury
and judge." The bib note's quotation is verbatim-grounded.

**FLAGS:** None. Online-first year (2024) vs. issue year (2025) is handled correctly by the bib.

---

## batat2022tlr

```bibtex
@article{batat2022tlr,
  author  = {Batat, Wided},
  title   = {Transformative Luxury Research ({TLR}): An Agenda to Advance Luxury for Well-Being},
  journal = {Journal of Macromarketing},
  year    = {2022},
  volume  = {42},
  number  = {4},
  pages   = {609--623},
  doi     = {10.1177/02761467221135547},
  note    = {P9; SI EDITOR (Batat) ... asks how luxury ecosystems affect "the individual and collective well-being at the economic, cognitive, emotional, and social levels." ... verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: exact title, Wided Batat, Journal of
Macromarketing 42(4), 609–623, print December 2022 (online 2022-10-26). Live Sage page 403.

**FULL TEXT: BLOCKED** — Sage paywall; Unpaywall reports no OA location; no usable Wayback
capture attempted beyond the paywall. The publisher-deposited abstract was retrieved from the DOI
registry.

**WHAT IT ARGUES** (publisher-deposited abstract): Introduces the TLR framework at the
intersection of luxury research, macromarketing, and transformative consumer research,
conceptualizing how the luxury ecosystem affects the well-being of individuals and communities
across production, consumption, and macroenvironment interactions.

**FLAGS:** The bib note's quoted phrase — "the individual and collective well-being at the
economic, cognitive, emotional, and social levels" — is **not in the deposited abstract** and
could not be checked against the full text. The abstract does support the individual/collective
framing in paraphrase. If the manuscript quotes that string, someone with Sage access must verify
it against the article body before submission.

---

## batat2024phcx

```bibtex
@article{batat2024phcx,
  author  = {Batat, Wided},
  title   = {What Does Phygital Really Mean? A Conceptual Introduction to the Phygital Customer Experience ({PH-CX}) Framework},
  journal = {Journal of Strategic Marketing},
  year    = {2024},
  volume  = {32},
  number  = {8},
  pages   = {1220--1243},
  doi     = {10.1080/0965254X.2022.2059775},
  note    = {CFP core; verified 2026-08-07}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: exact title, Wided Batat, Journal of Strategic
Marketing 32(8), 1220–1243; online 2022-04-05, print issue 2024-11-16. A Wayback capture of the
T&F page corroborates title and abstract (captured while online-first, "Vol 0, No 0"). Live T&F
page 403.

**FULL TEXT: BLOCKED** — T&F paywall; Unpaywall reports no OA location. Publisher abstract
obtained from the archived T&F page.

**WHAT IT ARGUES** (publisher abstract): Phygital lacks academic conceptualization and is
wrongly confined to channel logic (multi/cross/omnichannel); proposes PH-CX as a holistic
framework for the dynamics of customers shifting between physical and digital settings,
identifying driving forces, connectors, and pillars for designing experiences.

**FLAGS:** Minor: the article circulated as "Batat (2022)" online-first for two years before the
2024 issue; the bib's 2024 with volume/issue is the correct print citation, but cross-check that
the manuscript text does not cite it as 2022 anywhere.

---

## batat2026psr

```bibtex
@article{batat2026psr,
  author  = {Batat, Wided},
  title   = {Phygital Service Research ({PSR}): Advancing {FSR} and {TSR} toward Human-First Experience Design in Hybrid Physical-Digital Ecosystems},
  journal = {Journal of Services Marketing},
  year    = {2026},
  volume  = {40},
  number  = {4},
  pages   = {505--518},
  doi     = {10.1108/JSM-09-2025-0600},
  note    = {PSR proper; postdates the CFP ... verified 2026-08-07}
}
```

**IDENTITY: CONFIRMED** — against the Emerald publisher page itself
(`emerald.com/jsm/article/40/4/505/1323167/...`): Wided Batat, Journal of Services Marketing
40(4), 505–518, online 2025-12-09, issue 2026.

**FULL TEXT: BLOCKED** — Emerald paywall ($39 pay-per-view); Unpaywall reports no OA location.

**WHAT IT ARGUES** (publisher abstract): Introduces Phygital Service Research as an extension of
foundational and transformative service research, organized around hybrid embodiment, contextual
fluidity, multidimensional entanglement, and holistic innovation, and proposes "phyginography" as
an emerging methodology grounded in "phygital phenomenology."

**FLAGS:** None.

---

## batathammedi2023ert

```bibtex
@article{batathammedi2023ert,
  author  = {Batat, Wided and Hammedi, Wafa},
  title   = {The Extended Reality Technology ({ERT}) Framework for Designing Customer and Service Experiences in Phygital Settings: A Service Research Agenda},
  journal = {Journal of Service Management},
  year    = {2023},
  volume  = {34},
  number  = {1},
  pages   = {10--33},
  doi     = {10.1108/JOSM-08-2022-0289},
  note    = {P9; SI EDITOR (Batat). ... "a continuum in terms of customer value from physical to digital settings and vice versa." ... verified 2026-08-11; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — against the Emerald publisher page: Wided Batat, Wafa Hammedi; Journal
of Service Management 34(1), 10–33, published 2023-01-02.

**FULL TEXT: BLOCKED** — Emerald paywall / DeepDyve rental; no OA per Unpaywall.

**WHAT IT ARGUES** (publisher abstract): Proposes the ERT framework from an experiential
perspective, categorizing technologies and their effects on experience design across cognitive,
social, sensory, and contextual dimensions, "creating value continuums between physical and
digital spaces."

**FLAGS:** The bib note's quotation ("a continuum in terms of customer value from physical to
digital settings and vice versa") is close to but not identical with the abstract's wording; the
exact string presumably sits in the article body, which was not reachable. Verify before quoting
in print.

---

## beatty2016compliance

```bibtex
@article{beatty2016compliance,
  author  = {Beatty, Sharon E. and Ogilvie, Jessica and Northington, William Magnus and Harrison, Mary P. and Holloway, Betsy Bugg and Wang, Sijun},
  title   = {Frontline Service Employee Compliance with Customer Special Requests},
  journal = {Journal of Service Research},
  year    = {2016},
  volume  = {19},
  number  = {2},
  pages   = {158--173},
  doi     = {10.1177/1094670515624978},
  note    = {The rival account of the exception ... verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: all six authors, in the bib's order and with the
bib's given names (Sharon E. Beatty; Jessica Ogilvie; William Magnus Northington; Mary P.
Harrison; Betsy Bugg Holloway; Sijun Wang); Journal of Service Research 19(2), 158–173; print May
2016, online 2015-12-30. Live Sage page 403.

**FULL TEXT: BLOCKED** — Sage paywall; no OA per Unpaywall. Publisher-deposited abstract
retrieved from the DOI registry.

**WHAT IT ARGUES** (publisher-deposited abstract): Uses grounded theory and content analysis of
critical incidents to model how and when frontline employees comply with customer special
requests — requests beyond usual job duties — and the consequences of complying or failing to
comply for customer satisfaction and the firm.

**FLAGS:** None ("Compliance With" vs "with" is capitalization only).

---

## belanche2020

```bibtex
@article{belanche2020,
  author  = {Belanche, Daniel and Casal{\'o}, Luis V. and Flavi{\'a}n, Carlos and Schepers, Jeroen},
  title   = {Robots or Frontline Employees? Exploring Customers' Attributions of Responsibility and Stability after Service Failure or Success},
  journal = {Journal of Service Management},
  year    = {2020},
  volume  = {31},
  number  = {2},
  pages   = {267--289},
  doi     = {10.1108/JOSM-05-2019-0156},
  note    = {Triad prior art AND the guest-side accountability finding ... verified 2026-08-07, re-verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** — against the Emerald publisher page and the published PDF itself:
Daniel Belanche, Luis V. Casaló, Carlos Flavián, Jeroen Schepers; Journal of Service Management
31(2), 267–289, 2020.

**FULL TEXT: OBTAINED** — the published version (CC BY) via the University of Zaragoza
repository (`zaguan.unizar.es/record/95627/files/texto_completo.pdf`). Read title page, abstract,
and introduction.

**WHAT IT ARGUES** (full text): Two vignette-based experiments (hotel reception, restaurant
waiter; US respondents) grounded in attribution theory. Customers attribute less responsibility
to robots as agents but hold the firm more accountable for robot performance than for employee
performance, and perceive robot failures as more stable; communicating analytical AI capabilities
softens the stability attribution. This matches the bib note's characterization exactly,
including the organizational reading of accountability.

**FLAGS:** None.

---

## bendoly2013realtime

```bibtex
@article{bendoly2013realtime,
  author  = {Bendoly, Elliot},
  title   = {Real-Time Feedback and Booking Behavior in the Hospitality Industry: Moderating the Balance between Imperfect Judgment and Imperfect Prescription},
  journal = {Journal of Operations Management},
  year    = {2013},
  volume  = {31},
  number  = {1-2},
  pages   = {62--71},
  doi     = {10.1016/j.jom.2012.06.003},
  note    = {P2; CITE AS A COMPLICATION, NOT SUPPORT ... verified 2026-08-09; readdepth=partial-full}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: exact title, Elliot Bendoly (sole author),
Journal of Operations Management 31(1-2), 62–71, print January 2013. The DOI now resolves to
Wiley (JOM's current host), whose page returns 403 to automation.

**FULL TEXT: BLOCKED** — Wiley paywall; no OA per Unpaywall or Semantic Scholar; the author's
site (bendoly.net) was unreachable (connection failure). Publisher-deposited abstract retrieved
from the DOI registry.

**WHAT IT ARGUES** (publisher-deposited abstract): Revenue-management price points are "by their
very nature, imperfect prescriptions"; hotel agents "are often given the latitude to accept rate
bids below the pricing prescriptions," and the study examines how real-time feedback moderates
the balance between imperfect judgment and imperfect prescription. This supports the note's
"guidelines not mandates; sanctioned deviation latitude" reading at abstract level.

**FLAGS:** None on identity. The note records a prior partial-full read; nothing found here
contradicts it.

---

## bitner2000technology

```bibtex
@article{bitner2000technology,
  author  = {Bitner, Mary Jo and Brown, Stephen W. and Meuter, Matthew L.},
  title   = {Technology Infusion in Service Encounters},
  journal = {Journal of the Academy of Marketing Science},
  year    = {2000},
  volume  = {28},
  number  = {1},
  pages   = {138--149},
  doi     = {10.1177/0092070300281013},
  note    = {Triad prior art; earliest antecedent ... verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED** (with one caveat). DOI resolver metadata: "Technology Infusion in
Service Encounters," JAMS 28(1), 138–149, 2000; authors deposited as initials only — M. J.
Bitner, S. W. Brown, M. L. Meuter. Initials are consistent with the bib's full names, but the
full given names ("Mary Jo," "Stephen W.," "Matthew L.") could not be read off any publisher
surface this session: Sage 403, Springer's JAMS host behind a bot challenge, no Wayback snapshot.
The names are standard for these well-known authors; the caveat is documentary, not substantive.

**FULL TEXT: BLOCKED** — Sage 403; Springer host bot-challenged; no OA per Unpaywall or Semantic
Scholar; no Wayback snapshot; no abstract deposited in the DOI registry.

**WHAT IT ARGUES:** Not characterized — neither full text nor a publisher abstract was
obtainable this session.

**FLAGS:** None beyond the initials caveat above.

---

## boochua2022facial

```bibtex
@article{boochua2022facial,
  author  = {Boo, Huey Chern and Chua, Bee-Lia},
  title   = {An Integrative Model of Facial Recognition Check-in Technology Adoption Intention: The Perspective of Hotel Guests in {Singapore}},
  journal = {International Journal of Contemporary Hospitality Management},
  year    = {2022},
  volume  = {34},
  number  = {11},
  pages   = {4052--4079},
  doi     = {10.1108/IJCHM-12-2021-1471},
  note    = {The threshold, studied as a privacy calculus ... verified 2026-08-07}
}
```

**IDENTITY: CONFIRMED** — against the Emerald publisher page: Huey Chern Boo, Bee-Lia Chua;
IJCHM 34(11), 4052–4079, published 2022-10-21.

**FULL TEXT: BLOCKED** — Emerald paywall ($41); no OA per Unpaywall.

**WHAT IT ARGUES** (publisher abstract): Combines TAM, privacy calculus, and personal
innovativeness; SEM on survey data from guests of four- and five-star Singapore hotels. Guests
weigh benefits against risks; trust directs attention to benefits while privacy concern triggers
risk perception, and "ease of use of facial recognition check-in system could possibly backfire."

**FLAGS:** None.

---

## bovens2007accountability

```bibtex
@article{bovens2007accountability,
  author  = {Bovens, Mark},
  title   = {Analysing and Assessing Accountability: A Conceptual Framework},
  journal = {European Law Journal},
  year    = {2007},
  volume  = {13},
  number  = {4},
  pages   = {447--468},
  doi     = {10.1111/j.1468-0386.2007.00378.x},
  note    = {Canonical: accountability as a relationship between an actor and a forum, verbatim confirmed. Claim 16 cites rather than argues. verified 2026-08-09; readdepth=full}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: Mark Bovens, European Law Journal 13(4),
447–468, July 2007 (online 2007-06-07); the deposited title carries a footnote superscript
("...Framework1"), which is the article's opening endnote, not a title discrepancy. The published
PDF (below) confirms every field on its own masthead: "European Law Journal, Vol. 13, No. 4, July
2007, pp. 447–468." Wiley's live page 403s to automation.

**FULL TEXT: OBTAINED AND READ IN FULL** — the published Blackwell version from the Utrecht
University repository. Route worth recording: the portal file URL
(`research-portal.uu.nl/files/3099549/...`) sits behind a Cloudflare challenge, but the DSpace
REST API serves the bitstream openly:
`dspace.library.uu.nl/server/api/core/bitstreams/62d0c566-e33f-4693-8f73-146abfd542eb/content`
(item handle 1874/35005). All 22 journal pages read.

**WHAT IT ARGUES** (full text): Bovens rejects broad, evaluative uses of "accountability" and
defines it narrowly as a social relation: "a relationship between an actor and a forum, in which
the actor has an obligation to explain and to justify his or her conduct, the forum can pose
questions and pass judgement, and the actor may face consequences" (p. 450, italicized; restated
p. 467). Box 1 (p. 452) gives seven constitutive elements; Box 2 (p. 461) classifies
accountability by forum, actor, conduct, and obligation; the assessment half supplies three
evaluative perspectives — democratic, constitutional, learning — each generating its own kind of
accountability deficit. The evidence is conceptual analysis with EU-governance illustrations
(the Cresson case, comitology, OLAF), not empirics.

**FLAGS:**
- The card (`library/cards/bovens2007accountability.md`) records `read_depth: abstract` and "not
  admitted to the bibliography," while the bib note claims `readdepth=full` and the entry sits in
  references.bib. Card and bib disagree; whichever is authoritative, the substantive question is
  now closed — the full text exists openly, has been read, and the actor–forum definition the
  manuscript's contribution rests on is verbatim-correct as the bib note claims.
- The manuscript reportedly cites it four times; nothing in the full text undercuts a
  definitional citation, and the paper's own insistence that transparency and responsiveness are
  *not* accountability (pp. 453–454) actively strengthens a mediation argument that
  distinguishes information flows from obligation.

---

## bowkerstar1999sorting

```bibtex
@book{bowkerstar1999sorting,
  author    = {Bowker, Geoffrey C. and Star, Susan Leigh},
  title     = {Sorting Things Out: Classification and Its Consequences},
  publisher = {MIT Press},
  address   = {Cambridge, MA},
  year      = {1999},
  note      = {verified 2026-08-07 against the MIT Press record; monograph, no DOI. verified 2026-08-07 (Crossref DOI resolved). ISBN 9780262024617. ``Torque'' names the guest the category does not fit}
}
```

**IDENTITY: CONFIRMED.** The MIT Press's own monograph DOI record (10.7551/mitpress/6352.001.0001,
resolving to `direct.mit.edu/books/book/4738/`) deposits: "Sorting Things Out," Geoffrey C.
Bowker and Susan Leigh Star, The MIT Press, published 1999-09-29, electronic ISBN 9780262269070,
with the publisher's full descriptive blurb. mitpress.mit.edu and direct.mit.edu both 403 to
automation, so the print ISBN in the bib (9780262024617, the 1999 hardcover) was not directly
re-confirmable this session; it is consistent with the record and with the bib's own 2026-08-07
verification against the MIT Press page.

**FULL TEXT: BLOCKED** — no open full text exists; direct.mit.edu is paywalled and the only
other route is archive.org controlled lending, which cannot be exercised here.

**WHAT IT ARGUES** (publisher-deposited description): Classification systems are the scaffolding
of information infrastructures; through the ICD, the Nursing Interventions Classification,
apartheid race classification, and tuberculosis, the book shows how categories are made
invisible, how they order human interaction, and that each standard "valorizes some point of view
and silences another."

**FLAGS:** The note's claim that "torque" names the person the category does not fit is standard
for the book (the apartheid chapter) but was not verified against the text this session. The
note's duplicated "verified 2026-08-07" line is cosmetic.

---

## brochado2026phygital

```bibtex
@article{brochado2026phygital,
  author  = {Brochado, Ana and De Vos, Svetlana and Qesja, Blerina and Soleimani, Sadaf and Brodhead Ahmadi, Seyedeh Roya and Haykal, Karl-Anthony and Lipnickas, Gintare and Harris, Jane and Rao Hill, Sally},
  title   = {Is Phygital the New Normal? A Literature Review of the Evolution of Services Marketing},
  journal = {Journal of Services Marketing},
  year    = {2026},
  pages   = {1--20},
  doi     = {10.1108/JSM-09-2025-0709},
  note    = {SI EDITOR (De Vos). STRONG AND ALSO THE EXPOSURE ... Ahead-of-print, online 2026-06-18. verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: DIVERGENT — MAJOR.** Two independent publisher surfaces agree against the bib: the
Emerald article page and the publisher-deposited DOI metadata both give the author list as

| # | Publisher record | Bib entry | Verdict |
|---|---|---|---|
| 1 | Ana Brochado | Brochado, Ana | ok |
| 2 | Svetlana De Vos | De Vos, Svetlana | ok |
| 3 | **Bora** Qesja | Qesja, **Blerina** | wrong given name |
| 4 | **Samaneh** Soleimani | Soleimani, **Sadaf** | wrong given name |
| 5 | **Sarah Renee Brodhead** Ahmadi | Brodhead Ahmadi, **Seyedeh Roya** | wrong given names AND wrong family split (family is "Ahmadi"; "Brodhead" belongs to the given names) |
| 6 | **Kay-Anne** Haykal | Haykal, **Karl-Anthony** | wrong given name |
| 7 | **Gediminas** Lipnickas | Lipnickas, **Gintare** | wrong given name |
| 8 | **Joanne** Harris | Harris, **Jane** | wrong given name |
| 9 | Sally Rao Hill | Rao Hill, Sally | ok |

Six of nine given names are wrong, several replaced with plausible-sounding names of the same
ethnic flavor — the signature of a hallucinated author list. Title, journal, ahead-of-print
status (online 2026-06-18), and pages 1–20 all confirm.

**FULL TEXT: BLOCKED** — Emerald paywall ($39); no OA per Unpaywall.

**WHAT IT ARGUES** (publisher abstract): A review of 105 Scopus-indexed papers (Jan 2017–Aug
2025) using narrative and semantic analysis; phygital experiences sit at the core of contemporary
services marketing, and the field remains "fundamentally consumer-centred and technology-enabled"
— the exact phrase the manuscript's framing leans on, confirmed in the abstract.

**FLAGS:** Fix the author list before anything else in this slice. The note's "verified
2026-08-09" was recorded over a list the publisher record contradicts, so whatever that
verification consulted, it was not the publisher. The citation's argumentative use
(consumer-centred/technology-enabled) survives intact.

---

## bulley2015ethics

```bibtex
@article{bulley2015ethics,
  author  = {Bulley, Dan},
  title   = {Ethics, Power and Space: International Hospitality beyond Derrida},
  journal = {Hospitality \& Society},
  year    = {2015},
  volume  = {5},
  number  = {2-3},
  pages   = {185--201},
  doi     = {10.1386/hosp.5.2-3.185_1},
  note    = {P1; LOAD-BEARING -- host authority is not spent at admission but exercised continuously over the guest inside the space ... verified 2026-08-09; readdepth=abstract}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: Dan Bulley, Hospitality & Society 5, 185–201,
2015. The registry's issue field says "2" alone, but the DOI suffix itself (`hosp.5.2-3.185_1`)
and the QUB deposit's citation line ("5(2-3), 185-201") both give the double issue; the bib's
"2-3" is correct. Intellect Discover's live page 403s to automation.

**FULL TEXT: PARTIAL** — the peer-reviewed accepted manuscript from the Queen's University
Belfast research portal
(`pureadmin.qub.ac.uk/ws/files/17482394/Bulley_Ethics_Power_and_Space_Hospitality_and_Society.pdf`).
The deposited file runs a cover sheet plus roughly the first nine manuscript pages and ends
mid-article; the refugee-camps section is not in the file. What exists was read.

**WHAT IT ARGUES** (from the obtained portion): Reaffirms hospitality's importance for
international ethics while pushing past Derrida's fixation on sovereign mastery: hospitality is a
spatial, affective, relational practice in which inside/outside distinctions "need to be
policed, managed and controlled, even after the threshold of the home is crossed," and welcoming
*produces* the home, its borders and its affect. The bib note's load-bearing claim — host
authority exercised continuously after admission — is directly and verbatim-adjacently supported.

**FLAGS:** None on identity. Note for the record: the open deposit is truncated, so any quotation
from the article's second half still needs the published version.

---

## calorosenblat2017taking

```bibtex
@article{calorosenblat2017taking,
  author  = {Calo, Ryan and Rosenblat, Alex},
  title   = {The Taking Economy: {Uber}, Information, and Power},
  journal = {Columbia Law Review},
  year    = {2017},
  volume  = {117},
  number  = {6},
  pages   = {1623--1690},
  note    = {Information asymmetry as the constitutive resource; law review, no DOI; SSRN 2929643;
             verified 2026-08-07 against the journal record}
}
```

**IDENTITY: CONFIRMED** — against the journal's own site and its own PDF
(`columbialawreview.org/content/the-taking-economy-uber-information-and-power/`): Ryan Calo &
Alex Rosenblat, Columbia Law Review Vol. 117 No. 6, Essay. The page range was verified in the
PDF: opens at 1623, closes at 1690.

**FULL TEXT: OBTAINED** — the journal's PDF
(`columbialawreview.org/wp-content/uploads/2017/10/Calo-Rosenblat_The-Taking-Economy.pdf`); read
abstract, table of contents, introduction, and the concluding pages.

**WHAT IT ARGUES** (full text): Sharing-economy firms sit between consumers and providers with a
"unique capacity to monitor and nudge all participants," which they can leverage into digital
market manipulation — "taking." Consumer protection law, with its longtime focus on asymmetries
of information and power, is the best-positioned legal response, provided it evolves (incentive
alignment, line-drawing, or fiduciary duties for data intermediaries). The bib note's
"information asymmetry as the constitutive resource" is a fair one-line gloss.

**FLAGS:** None.

---

## casalegno2020circular

```bibtex
@article{casalegno2020circular,
  author  = {Casalegno, Cecilia and Civera, Chiara and Mosca, Fabrizio and Freeman, R. Edward},
  title   = {Circular Economy and Relationship-Based View},
  journal = {Symphonya. Emerging Issues in Management},
  year    = {2020},
  number  = {1},
  pages   = {143--158},
  doi     = {10.4468/2020.1.12casalegno.civera.mosca.freeman},
  note    = {P9; SI EDITOR (Mosca) WITH FREEMAN ... "overlap and converge." ... verified 2026-08-11; readdepth=full-text}
}
```

**IDENTITY: DIVERGENT on pages.** The journal's own record
(`symphonya.unicusano.it/index.php/sym/article/view/13383`) and the published PDF both give
**149–164**; the PDF's own citation footer reads "Symphonya. Emerging Issues in Management
(symphonya.unicusano.it), (1), 149-164." The bib says 143–158 — start and end both off. Authors
(including R. Edward Freeman), title, journal, issue (1), year (2020), and DOI all confirm.

**FULL TEXT: OBTAINED** — the journal's OA PDF
(`symphonya.unicusano.it/article/download/13383/11922`; the `view` URL serves HTML, the
`download` URL serves the PDF). All 16 pages read.

**WHAT IT ARGUES** (full text): Reconceptualizes the circular economy as "an open and dynamic
loop of relationships" on stakeholder-theory grounds, against the closed materials-circulation
reading. The abstract states verbatim that "stakeholders' power, roles and responsibilities
overlap and converge into an emergent joint-value creation process" — the quotation in the note
and card holds. Evidence is a single COVID-19 case, the Robiola di Roccaverano cheese consortium,
where consumers and retailers became intermediaries and institutions became promoters ("relate
and reallocate"), read as stakeholders abandoning fixed roles under urgent common claims.

**FLAGS:** Fix pages to **149–164**. The card (`library/cards/casalegno2020circular.md`) claims
"Open-access PDF read in full from the Symphonya site," yet the wrong pages sat in the bib —
the read did not include checking the entry against the artifact. Also worth knowing for section
3's use: the redistribution evidence is one small qualitative case plus conceptual argument, so
cite it as the editors' *premise*, not as an established empirical regularity.

---

## chalmers2004seamful

```bibtex
@inproceedings{chalmers2004seamful,
  author    = {Chalmers, Matthew and Galani, Areti},
  title     = {Seamful Interweaving: Heterogeneity in the Theory and Design of Interactive Systems},
  booktitle = {Proceedings of the 5th Conference on Designing Interactive Systems ({DIS} '04)},
  year      = {2004},
  pages     = {243--252},
  doi       = {10.1145/1013115.1013149},
  note      = {Design-theory ally for section 7 ... verified 2026-08-07}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: Matthew Chalmers, Areti Galani; "Proceedings of
the 5th conference on Designing interactive systems: processes, practices, methods, and
techniques" (DIS04, Cambridge, MA, August 2004), pp. 243–252. ACM deposited only the short title
"Seamful interweaving"; the full title with subtitle is confirmed on the author's camera-ready
copy (below), which carries the ACM DIS2004 copyright block. ACM DL 403s to automation.

**FULL TEXT: OBTAINED** — the author's copy at
`dcs.gla.ac.uk/~matthew/papers/DIS2004v3.pdf` (camera-ready, ACM two-column format; the file runs
6 pages against the published 243–252 span, so pagination differs from the version of record).
Read in full.

**WHAT IT ARGUES** (full text): Against Weiser's "disappearance" ideal and beyond Dourish's
embodied interaction: everyday activity interweaves heterogeneous media, and seams — the visible
joins and boundaries between parts of a system — are things people accommodate, appropriate, and
use as resources rather than defects to engineer away. Grounded in the Equator City project's
Mack Room mixed-reality museum trials (three coupled visitors: on-site handheld, web, VR).
Directly supports the note's "seams as resources for action, not defects."

**FLAGS:** None material. If the manuscript pin-cites page numbers, use the ACM pagination, not
the author copy's.

---

## cheng2025silence

```bibtex
@article{cheng2025silence,
  author  = {Cheng, Mengting and Zhang, Long and Wang, Haiqing},
  title   = {The Effect of Artificial Intelligence Awareness on Frontline Service Employees' Silence: The Roles of Psychological Contract Breach and Moral Identity},
  journal = {International Journal of Contemporary Hospitality Management},
  year    = {2025},
  volume  = {37},
  number  = {5},
  pages   = {1845--1861},
  doi     = {10.1108/IJCHM-07-2024-0968},
  note    = {The voice claim, in a hospitality journal ... verified 2026-08-07}
}
```

**IDENTITY: CONFIRMED** — against the Emerald publisher page: Mengting Cheng, Long Zhang,
Haiqing Wang; IJCHM 37(5), 1845–1861; online 2025-03-04, issue 2025-04-07.

**FULL TEXT: BLOCKED** — Emerald paywall ($41); no OA per Unpaywall.

**WHAT IT ARGUES** (publisher abstract): Two-wave survey of 355 Chinese hotel employees: "AI
awareness increases frontline service employees' silence by prompting psychological contract
breach," with moral identity mitigating the effect. The bib note's claim is the abstract's own
finding, verbatim in substance.

**FLAGS:** None.

---

## christin2017practice

```bibtex
@article{christin2017practice,
  author  = {Christin, Ang{\`e}le},
  title   = {Algorithms in Practice: Comparing Web Journalism and Criminal Justice},
  journal = {Big Data \& Society},
  year    = {2017},
  volume  = {4},
  number  = {2},
  pages   = {1--14},
  doi     = {10.1177/2053951717718855},
  note    = {verified 2026-08-07 (Crossref DOI resolved). Categories of judgement relocated from practitioner discretion into a vendor's model}
}
```

**IDENTITY: CONFIRMED.** DOI resolver metadata: Angèle Christin, Big Data & Society 4(2), 2017
(online 2017-07-16, issue December 2017). The journal is eLocator-based — the registry's page
field is the article number 205395171771885 — so "1–14" is the PDF's internal pagination, a
convention the author's own CV also uses ("4 (2): 1-14").

**FULL TEXT: OBTAINED** — the article is gold OA (CC BY-NC-ND) but Sage's live site blocks
automated access; the full text was read from a Wayback capture of the publisher's own full-text
page (`web.archive.org/web/2020id_/https://journals.sagepub.com/doi/full/10.1177/2053951717718855`,
~70k characters of article text). Abstract, introduction, and targeted sections read.

**WHAT IT ARGUES** (full text): Multi-sited ethnography comparing how algorithms are actually
used in web journalism and criminal justice. In both fields Christin finds "decoupling" — a gap
between algorithms' intended and actual effects — and a repertoire of "buffering" strategies
(foot-dragging, gaming, open critique) by which practitioners minimize the instruments' impact
on their work.

**FLAGS:** One substantive caution. The bib note glosses the paper as "categories of judgement
relocated from practitioner discretion into a vendor's model." Christin does use the phrase
"categories of judgment" (experts' autonomy in applying them is what algorithms challenge), but
her *finding* runs the other way: in practice the relocation largely fails — practitioners
buffer, and algorithmic power is blunted. If the manuscript cites her for a completed relocation
of judgment, a referee who knows the paper will object; cite her for the contest over discretion,
or for decoupling, not for displacement accomplished. Check the manuscript's sentence against
this. Cosmetic: pages "1–14" against an eLocator journal is tolerated but "205395171771885" (or
no pages) is the stricter form.

---

## Summary table

| citekey | identity | full text | flags |
|---|---|---|---|
| anderson2015transformative | CONFIRMED (DOI registry + archived Sage page) | OBTAINED (archived publisher HTML) | registry deposit lacks subtitle; none material |
| andreev2025destination | **DIVERGENT** — Kosmas is Petros (C.), not Panagiotis | OBTAINED (published PDF via CUT repository) | fix given name; byline lacks Theocharous's "L." |
| are2025appeals | CONFIRMED | OBTAINED (CC BY VoR via Northumbria portal) | none |
| batat2022tlr | CONFIRMED (DOI registry) | BLOCKED (Sage paywall, no OA) | note's quoted phrase unverifiable without full text |
| batat2024phcx | CONFIRMED (DOI registry + archived T&F page) | BLOCKED (T&F paywall, no OA) | online-first 2022 vs print 2024 — bib correct, check in-text usage |
| batat2026psr | CONFIRMED (Emerald page) | BLOCKED (Emerald paywall) | none |
| batathammedi2023ert | CONFIRMED (Emerald page) | BLOCKED (Emerald paywall) | note's quotation only approximated by abstract |
| beatty2016compliance | CONFIRMED (DOI registry) | BLOCKED (Sage paywall, no OA) | none |
| belanche2020 | CONFIRMED (Emerald page + published PDF) | OBTAINED (CC BY via Zaragoza repository) | none |
| bendoly2013realtime | CONFIRMED (DOI registry) | BLOCKED (Wiley paywall; author site unreachable) | none |
| bitner2000technology | CONFIRMED (DOI registry; authors deposited as initials) | BLOCKED (Sage 403, Springer bot-wall, no OA) | given names rest on initials + general knowledge; not characterized |
| boochua2022facial | CONFIRMED (Emerald page) | BLOCKED (Emerald paywall) | none |
| bovens2007accountability | CONFIRMED (DOI registry + published PDF) | **OBTAINED, read in full** (UU repository via DSpace API) | card/bib disagree on read-depth and admission; definition verbatim-correct |
| bowkerstar1999sorting | CONFIRMED (MIT Press monograph DOI record) | BLOCKED (no open full text; lending only) | hardcover ISBN not re-confirmable this session; "torque" claim unverified against text |
| brochado2026phygital | **DIVERGENT — 6 of 9 given names wrong** (+ Ahmadi family-name split) | BLOCKED (Emerald paywall) | fabricated-looking author list; "consumer-centred and technology-enabled" confirmed |
| bulley2015ethics | CONFIRMED (DOI registry; issue 2-3 per DOI suffix + deposit) | PARTIAL (QUB accepted MS, deposit truncated) | load-bearing claim directly supported by obtained portion |
| calorosenblat2017taking | CONFIRMED (journal site + PDF; 1623–1690 verified) | OBTAINED (journal's own PDF) | none |
| casalegno2020circular | **DIVERGENT — pages are 149–164, not 143–158** | OBTAINED, read in full (journal OA PDF) | fix pages; evidence is one qualitative case — cite as premise |
| chalmers2004seamful | CONFIRMED (DOI registry; subtitle via author copy) | OBTAINED (author camera-ready copy) | pin-cites must use ACM pagination |
| cheng2025silence | CONFIRMED (Emerald page) | BLOCKED (Emerald paywall) | none |
| christin2017practice | CONFIRMED (DOI registry) | OBTAINED (archived publisher full-text page; gold OA) | note's gloss inverts her finding — cite decoupling/contest, not accomplished relocation |

**Corrections to make in references.bib:** andreev2025destination (Kosmas, Petros C.),
brochado2026phygital (full author list per the table above), casalegno2020circular (pages
149–164). **Claims to re-check in the manuscript:** the batat2022tlr quotation, the
batathammedi2023ert quotation, and any sentence citing christin2017practice for relocated
judgment.
