# Source-side audit — slice 05 (martinwaldman2022legitimate … raisch2021paradox)

Audit date: 2026-08-17. Auditor: source-verification agent, slice 05 of the bibliography audit.

**Standard applied.** A source counts as verified only against the publisher's own record or the DOI
resolver. Where a publisher blocked non-browser access (Sage, Elsevier/ScienceDirect, Taylor &
Francis, Wiley, MDPI, AOM, MISQ, IEEE all return 403 or a Cloudflare/Akamai wall to this
environment; no Chrome browser was connected this session), the raw Crossref record — the DOI
registry entry the publisher itself deposits — served as the resolver-side authority. Every author
divergence below was re-checked against the raw Crossref JSON, not a summarizer's paraphrase. Two
publisher abstracts (AOM) were recovered from Wayback snapshots of the publisher's own pages;
those routes are named where used.

**Headline results.** Five entries carry corrupted author given names (pan2025dark,
park2026lobbies, pigac2026transparency, mosca2025phygital, moganadas2026wellbeing) — the same
failure mode as the project's three earlier catches. Three entries mix online-first year with
print-issue volume/pages (nguyen2024stereotypes, pedersen2022, mosca2025phygital;
martinwaldman2022legitimate has the same structure but its note discloses it). The three assigned
disputes (phillips year, padigar year, odekerken year) are all resolved below. Full text was
obtained and read for pijls2017measuring, phillips2024physical, martinwaldman2022legitimate, and
odekerken2021service.

---

## 1. martinwaldman2022legitimate

Bib: Martin & Waldman, "Are Algorithmic Decisions Legitimate?…", J. Business Ethics, 2022, 183(3), 653–670, doi:10.1007/s10551-021-05032-7.

- **IDENTITY: CONFIRMED** — Crossref registry record and the Springer PDF itself
  (https://link.springer.com/content/pdf/10.1007/s10551-021-05032-7.pdf). Authors Kirsten Martin,
  Ari Waldman. Volume 183(3), 653–670. Springer's own header reads "Journal of Business Ethics
  (2023) 183:653–670"; published online 10 Feb 2022. The bib's year 2022 is the online year; the
  cited issue is 2023. The note already discloses this ("Online 2022, print 2023").
- **FULL TEXT: OBTAINED** — publisher PDF, CC-BY, via Unpaywall pointer; read (front matter,
  abstract, intro; results section text-extracted and checked).
- **WHAT IT ARGUES** (from full text): Nine factorial-vignette surveys on perceived legitimacy of
  firms' algorithmic decisions. Notices and impact statements do not raise perceived legitimacy;
  good outcomes do. An appeal process is the one governance mechanism that creates a "legitimacy
  dividend" for bad outcomes — and impact assessment, human-in-the-loop, and external audit
  *lower* legitimacy relative to mere notice ("This was a surprise and counter to the
  hypothesis," β for appeals = 4.54, p < 0.01). Arbitrary or morally dubious inputs (race, day of
  week) impose a legitimacy penalty no outcome or procedure overcomes.
- **FLAGS**: The bib note's strong claim — appeals the only mechanism conferring legitimacy on
  adverse decisions, oversight and audit lowering it — is verified verbatim in the results. Only
  the year style needs a decision: cite 2023 if 183(3):653–670 stays in the entry.

## 2. moganadas2026wellbeing

Bib: Moganadas, Sharon Rajkumar; Goh, Guan Gan; Cheah, Chee Sun; Shidik, Guruh Fajar. Societies, 2026, 16(7), 213, doi:10.3390/soc16070213.

- **IDENTITY: DIVERGENT — three of four author names wrong.** Raw Crossref JSON (MDPI-deposited):
  **Sharmila Rani Moganadas; Gerald Guan Gan Goh; Chew Sze Cheah; Guruh Fajar Shidik**. The bib has
  "Sharon Rajkumar Moganadas" (invented given names), "Guan Gan Goh" (missing "Gerald"), and "Chee
  Sun Cheah" (should be "Chew Sze"). Title, journal, 16(7):213, and date (8 July 2026) all match.
- **FULL TEXT: BLOCKED** — MDPI serves 403/Access Denied (Akamai) to both WebFetch and curl from
  this environment, on the article page and the /pdf route, after a rate-limit backoff retry. The
  article is gold OA; a browser session would get it trivially.
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): PRISMA review of 57
  peer-reviewed articles (2014–2025) on digital transformation and employee well-being; finds the
  literature fragmented across technologies, disciplines, and well-being constructs; builds five
  aggregate dimensions (conditions, resources/demands, mediating processes, context, outcomes);
  calls for temporally sensitive, context-specific research. This matches the bib note's use
  (individual-level scope, fragmentation as the field's own diagnosis).
- **FLAGS**: The note claims readdepth=full-text, yet the author list is corrupted — whoever read
  the full text did not take the byline from it. Fix all three names before submission. Content
  claims themselves check out against the abstract.

## 3. mohlmann2021algorithmic

Bib: Möhlmann, Zalmanson, Henfridsson, Gregory. MIS Quarterly, 2021, 45(4), 1999–2022, doi:10.25300/MISQ/2021/15333.

- **IDENTITY: CONFIRMED** — raw Crossref registry record: all four authors with given names exactly
  as in the bib; MIS Quarterly 45(4), 1999–2022, December 2021.
  (Möhlmann's own faculty site lists "54(4)" — a typo on her page, not in the bib.)
- **FULL TEXT: BLOCKED** — misq.umn.edu returns 403 to WebFetch and a Cloudflare challenge to
  curl; Unpaywall reports closed with no repository copy; the author's site links no PDF.
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): "Online labor platforms
  (OLPs) can use algorithms along two dimensions: matching and control." Grounded theory from Uber
  drivers plus executive/engineer interviews; "in the context of both algorithmic matching and
  algorithmic control, platform workers experience tensions relating to work execution,
  compensation, and belonging," which trigger market-like and organization-like responses.
- **FLAGS**: **The assigned question is settled: matching and control are two parallel
  dimensions, not a temporal conversion.** The abstract's framing is dimensional throughout —
  platforms "can use" algorithms along both dimensions, and worker tensions arise under both
  simultaneously. If the manuscript reads "when matching meets control" as a story of matching
  platforms *becoming* control platforms, that overreads the title; the safe citation is to the
  coexistence of the two dimensions and the tensions they jointly produce.

## 4. morosan2016

Bib: Morosan & DeFranco, "Modeling Guests' Intentions to Use Mobile Apps in Hotels", IJCHM, 2016, 28(9), 1968–1991, doi:10.1108/IJCHM-07-2015-0349.

- **IDENTITY: CONFIRMED** — Emerald publisher page
  (https://www.emerald.com/insight/content/doi/10.1108/IJCHM-07-2015-0349/full/html): Cristian
  Morosan, Agnes DeFranco; 28(9), 1968–1991, 2016. One divergence: the publisher title carries a
  subtitle the bib truncates — "…in hotels: The roles of personalization, privacy, and
  involvement."
- **FULL TEXT: BLOCKED** — Emerald serves metadata and abstract but the body is subscription-only;
  Unpaywall not consulted for this entry (low stakes), no OA route attempted beyond the publisher.
- **WHAT IT ARGUES** (publisher abstract): SEM on a nationwide US sample; model explains 79% of
  variance in intention to use hotel-branded apps; involvement is the strongest predictor,
  followed by app-related privacy concerns and perceived personalization benefits.
- **FLAGS**: Restore the subtitle or accept the truncation knowingly. Content matches the note
  ("personalization-privacy in hotel apps").

## 5. mosca2025phygital

Bib: Mosca, Civera, Chiaudano, Shakil (Hassan). J. Macromarketing, 2025, 46(3), 426–445, doi:10.1177/02761467251403943.

- **IDENTITY: DIVERGENT — fourth author's given name wrong, and year mixed.** Raw Crossref JSON
  (Sage-deposited): Fabrizio Mosca; Chiara Civera; Valentina Chiaudano; **Hafsa Shakil** — the bib
  has "Hassan Shakil". Volume 46(3), 426–445 confirmed; online 15 Dec 2025, print issue September
  **2026**. The bib's 2025 is the online year attached to a 2026 issue's volume/pages.
- **FULL TEXT: BLOCKED** — Sage returns 403; Unpaywall reports closed, no repository copy.
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): Conceptual paper theorizing
  the museum as a phygital ecosystem; three-level, tri-dimensional framework of value co-creation;
  phygitalization "reconfigures the spatial and relational boundaries of cultural experience …
  and redistributes agency among institutional and non-institutional actors." The redistribution
  claim the bib note leans on is verbatim in the abstract, and the abstract's register is
  emancipatory — consistent with the note's reading that Mosca does not ask what obligation
  travels with the agency.
- **FLAGS**: Fix "Hassan"→"Hafsa". Decide the year: 2026 if citing 46(3):426–445, or 2025
  online-first without volume/pages. This is an SI-editor citation — a name error here is the most
  visible kind.

## 6. nguyen2024stereotypes

Bib: Nguyen, Yankholmes, Ladkin, Osman. Tourism Review, 2024, 80(7), 1413–1426, doi:10.1108/TR-09-2023-0612.

- **IDENTITY: DIVERGENT — year.** Emerald publisher page
  (https://www.emerald.com/insight/content/doi/10.1108/TR-09-2023-0612/full/html) and raw
  Crossref agree: all four authors as in the bib; online 2 Aug 2024; print issue 8 Sep **2025**,
  volume 80(7), 1413–1426. The bib pairs the 2024 online year with the 2025 issue's
  volume/issue/pages.
- **FULL TEXT: BLOCKED** — Emerald subscription body; no OA route found.
- **WHAT IT ARGUES** (publisher abstract): Interviews with 34 Vietnamese service providers;
  staff categorize guests by nationality before arrival; service runs smoothly when guest
  behaviour matches the stereotype script and mismatch produces failures requiring adaptive
  recovery. Matches the bib note's "torque in the field's own voice" use exactly.
- **FLAGS**: Year should be 2025 to match 80(7):1413–1426 (or drop volume/pages and keep 2024).

## 7. odekerken2021service

Bib: Odekerken-Schröder, Mennens, Steins, Mahr. J. Service Management, 2022, 33(2), 246–292, doi:10.1108/JOSM-10-2020-0372.

- **IDENTITY: CONFIRMED** — Emerald publisher page
  (https://www.emerald.com/insight/content/doi/10.1108/JOSM-10-2020-0372/full/html): all four
  authors as in the bib; online 25 Aug 2021; print issue 28 Feb 2022; 33(2), 246–292.
- **FULL TEXT: OBTAINED** — CC-BY author-accepted manuscript from QUT ePrints
  (https://eprints.qut.edu.au/212941/1/10_1108_JOSM_10_2020_0372.pdf), text-extracted and read at
  the abstract/findings level; publisher HTML abstract also read at Emerald.
- **WHAT IT ARGUES** (from full text and publisher abstract): The literal "service triad"
  (robot–customer–frontline employee), studied in a field study (n=108, fast-casual dining) plus
  scenario experiments (n=361). Robot anthropomorphism drives utilitarian value, social presence
  drives hedonic value; high FLE interaction quality can compensate for lower robot performance —
  evidence for augmentation rather than pure substitution. Matches the note.
- **FLAGS**: **Year dispute resolved: 2022 is right for the cited issue.** Online-first was 2021
  (hence the citekey), and the note already documents the choice ("the year now follows the
  printed issue"). Internally consistent; only the citekey's "2021" is cosmetic.

## 8. okhuysenbechky2009

Bib: Okhuysen & Bechky, "Coordination in Organizations: An Integrative Perspective", AoM Annals, 2009, 3(1), 463–502, doi:10.5465/19416520903047533.

- **IDENTITY: CONFIRMED** — DOI resolves through doi.org to journals.aom.org; raw Crossref
  registry record: Gerardo A. Okhuysen, Beth A. Bechky; Annals 3(1), 463–502, 2009. One registry
  quirk: the deposited title is "10 Coordination in Organizations…" — the "10" is the chapter
  number from the Annals' volume-as-book format, not part of the working title; the bib's form is
  the correct citable title.
- **FULL TEXT: BLOCKED** — every route failed: journals.aom.org 403 (direct and via doi.org),
  tandfonline.com (the legacy 10.1080 host) Cloudflare-walled, Unpaywall closed on both DOI forms,
  Semantic Scholar API has no OA PDF, scholar.archive.org has no copy, web searches surfaced only
  ResearchGate/Scispace gates. The **publisher abstract was recovered** from a Wayback snapshot of
  the journals.aom.org article page itself (gzip-decompressed curl fetch).
- **WHAT IT ARGUES** (publisher abstract, archived publisher page): Coordination is "the process
  of interaction that integrates a collective set of interdependent tasks." The review organizes
  the literature by coordination mechanisms, then proposes that "coordination mechanisms (such as
  routines, meetings, plans, and schedules) impact the work of organizations by creating three
  integrative conditions for coordinated activity: **accountability, predictability, and common
  understanding**."
- **FLAGS**: **The load-bearing claim holds at the publisher-abstract level**: the three
  conditions are exactly accountability, predictability, and common understanding, produced by
  mechanisms rather than being mechanisms themselves — which is how Section 6 uses them. What
  this audit could not do is check the body's *definitions* of each condition (the abstract names
  but does not define them); the paper's own glosses (e.g., accountability as knowing who is
  responsible for what) remain unverified here. If a sentence in the manuscript paraphrases the
  definitions, someone with library access should check them against pp. 483–488. Note the
  abstract says "integrative conditions"; the note's "integrating conditions" is a harmless
  paraphrase but should not appear inside quotation marks.

## 9. pan2025dark

Bib: Pan, Shan-Yan; Lin, Yan; Wong, Jose Weng Chou. Tourism Management, 2025, 106, 104994, doi:10.1016/j.tourman.2024.104994.

- **IDENTITY: DIVERGENT — two of three author given names wrong.** Raw Crossref JSON
  (Elsevier-deposited): **Su-Ying Pan; Yangpeng Lin; Jose Weng Chou Wong**. The bib has "Shan-Yan
  Pan" and "Yan Lin". Volume 106, article 104994, February 2025 print — confirmed (the prior
  sweep's 2024→2025 year correction was right).
- **FULL TEXT: BLOCKED** — ScienceDirect serves a bot-wall shell to curl even with referer chain
  through linkinghub; Unpaywall closed; even the Wayback snapshot of the article page is an
  archived Cloudflare error. Elsevier deposits no abstract to Crossref, so no qualifying
  characterization source was reachable at all.
- **WHAT IT ARGUES**: not characterized this audit (the bib note's characterization — robot risk
  awareness → withdrawal behaviours, authors recommending augmentation over automation — rests on
  the prior sweep's abstract read and was not re-verifiable here).
- **FLAGS**: Fix both given names. This is the "STRONGEST employee-discretion citation" per the
  note, so the byline error would land in a load-bearing spot. Su-Ying Pan is an established
  hospitality-OB scholar (Macau); "Shan-Yan" looks like the same secondary-index corruption
  pattern as the project's earlier catches.

## 10. papadopoulos2021violation

Bib: Papadopoulos, Lopez-Andreu, Jamalian. Industrial Relations Journal, 2021, 52(4), 315–330, doi:10.1111/irj.12337.

- **IDENTITY: CONFIRMED** — raw Crossref registry record: Orestis Papadopoulos, Marti
  Lopez-Andreu, Mandi Jamalian; 52(4), 315–330, July 2021 (online 5 July 2021, same-year issue —
  no online/print split to trip over).
- **FULL TEXT: BLOCKED** — Wiley 403 to WebFetch and Cloudflare to curl; no OA copy found.
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): Interviews and documents on
  labour violation in UK hotels; organisational, institutional, and individual factors make
  silence dominant; for precarious workers the UK individual-employment-rights model has "no
  substance," jeopardising both enforcement and workers' knowledge of their rights. The bib
  note's paraphrase is accurate, including the quoted phrase.
- **FLAGS**: none.

## 11. parasuraman2000types

Bib: Parasuraman, Sheridan, Wickens. IEEE Trans. SMC–A, 2000, 30(3), 286–297, doi:10.1109/3468.844354.

- **IDENTITY: CONFIRMED (with one caveat)** — raw Crossref registry record: R. Parasuraman, T.B.
  Sheridan, C.D. Wickens; IEEE Transactions on Systems, Man, and Cybernetics – Part A; 30(3),
  286–297, May 2000. The registry stores initials only, consistent with the bib's Raja / Thomas
  B. / Christopher D.; the full given names were not independently confirmable because IEEE
  Xplore is unreachable (403 live; even the Wayback snapshot is an archived block page). No
  serious doubt — these are the canonical authors — but the letter of the standard was met only
  at initial depth.
- **FULL TEXT: BLOCKED** — IEEE Xplore unreachable by every route tried (direct, doi.org,
  Wayback); Elsevier-style abstract not deposited to Crossref; no OA copy hunted beyond one
  search pass.
- **WHAT IT ARGUES**: not characterized this audit. The bib cites it only for the
  levels-of-automation lineage and the note's four stated contrasts, which do not depend on
  details beyond the model's well-known structure; still, no qualifying source was reached.
- **FLAGS**: none beyond the initial-depth caveat.

## 12. park2026lobbies

Bib: Park, Sanghoon; Lee, Jeong Zoo; Lehto, Xinran Y. JHTR, 2026, 50(2), 170–187, doi:10.1177/10963480241305760.

- **IDENTITY: DIVERGENT — two of three author names wrong.** Raw Crossref JSON (Sage-deposited):
  **Soona Park; Jianan Z. Lee; Xinran Y. Lehto**. The bib has "Sanghoon Park" and "Jeong Zoo Lee"
  — both given names invented. Volume 50(2), 170–187, print February 2026 (online 21 Dec 2024) —
  year and locators confirmed.
- **FULL TEXT: BLOCKED** — Sage 403; Unpaywall closed.
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): Choice-based conjoint
  study of guests' preferred lobby designs integrating local-community elements (visual,
  functional, activity design); preferred elements build sense of place and community for local
  and non-local guests, with synergistic combinations; framed as bridging design attributes and
  guest well-being. This supports the note's use — well-being and community joined through
  physical design, no automation.
- **FLAGS**: Fix both names. Same corruption pattern as pan2025dark and the project's earlier
  catches; "Sanghoon Park" is a common academic name that a secondary index could easily have
  substituted for the less common "Soona Park."

## 13. parkinson2022online

Bib: Parkinson, Schuster, Mulcahy. J. Service Research, 2022, 25(1), 108–125, doi:10.1177/10946705211018860.

- **IDENTITY: CONFIRMED** — raw Crossref registry record: Joy Parkinson, Lisa Schuster, Rory
  Mulcahy; 25(1), 108–125; online 1 June 2021, print February 2022. Bib year 2022 matches the
  cited issue.
- **FULL TEXT: BLOCKED this audit** — Sage 403; Unpaywall closed. (The bib note records
  readdepth=full from the 2026-08-09 pass; this audit could not repeat that read.)
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): Case study of an online
  weight-management forum that became an online third place; proposes a framework of online
  third-place characteristics and their effects on eudaimonic and hedonic well-being; social
  density, equity, and personalization substitute for a servicescape; explicitly oriented to
  unintended consequences and their management through design (segmentation, empowerment). The
  note's both-valences-plus-design-dependency reading is what the abstract says.
- **FLAGS**: none.

## 14. pedersen2022

Bib: Pedersen & Pors. JPART, 2022, 33(1), 80–93, doi:10.1093/jopart/muac012.

- **IDENTITY: DIVERGENT — year.** OUP publisher page
  (https://academic.oup.com/jpart/article/33/1/80/6564140) and raw Crossref agree: Kirstine Zinck
  Pedersen, Anja Svejgaard Pors; online 5 March 2022; print issue January **2023**; 33(1), 80–93.
  The bib pairs the 2022 online year with the 2023 issue's volume/pages — same mixed style as
  nguyen.
- **FULL TEXT: BLOCKED** — OUP body is subscription-only; no OA copy hunted beyond the publisher
  page (the entry is not load-bearing enough to justify more).
- **WHAT IT ARGUES** (publisher abstract): Comparative ethnography of Danish healthcare and
  citizen services; standardization technologies produce "rough categorizations and scripts for
  action" that require new discretionary work rather than eliminating it; three discretionary
  response types (adaptive handling, attentive compensation, affective encouragement). Exactly
  the note's "standardization does not eliminate discretion; it generates new discretionary
  work."
- **FLAGS**: Year should be 2023 to match 33(1):80–93, or drop the locators and cite 2022 advance
  access. Citekey "pedersen2022" can stand either way.

## 15. phillips2024physical

Bib: Phillips, Russell-Bennett, Kowalkiewicz. Service Industries Journal, 2024, 44(13-14), 919–948, doi:10.1080/02642069.2022.2119222.

- **IDENTITY: CONFIRMED — author list re-verified independently, twice.** (1) Raw Crossref
  registry record (T&F-deposited): exactly three authors — Chelsea Phillips, Rebekah
  Russell-Bennett, Marek Kowalkiewicz. (2) The author-accepted manuscript itself (QUT ePrints,
  https://eprints.qut.edu.au/234936/) carries the same three names on its title page, with QUT
  affiliations. There is no trace of Odekerken-Schröder, Mahr, or Letheren; the prior sweep's
  correction was right and holds at the publisher-deposited record and on the manuscript. Volume
  44(13-14), 919–948 confirmed.
- **FULL TEXT: OBTAINED** — CC-BY-NC author-accepted manuscript, QUT ePrints
  (https://eprints.qut.edu.au/234936/1/114695683.pdf); first eight pages read as images, rest
  available. Publisher page (tandfonline.com) is 403-walled; Unpaywall reports the publisher
  version closed.
- **WHAT IT ARGUES** (from full text): Interviews with 30 customers in a simulated just-walk-out
  retail experience. Customer effort has physical, cognitive, and interpersonal components and is
  transferable; removing high interpersonal effort makes the experience more forgettable
  ("slippery"); desire for effortful human interaction, shopping value type, technology attitude,
  and age moderate. Contributions: effort perceptions are subjective, effort is transferable,
  desire for memorability is variable.
- **FLAGS**: **Year dispute resolved**: published online 20 Sep 2022 (hence the 2022-registered
  DOI and the manuscript's "© 2022 Informa UK" line); the print issue is 44(13-14), 25 Oct
  **2024**. The bib's 2024 + 44(13-14):919–948 is internally consistent print-issue style — keep
  it, and expect the DOI to look "old" because it is the online-first DOI. No change needed
  unless the manuscript's in-text citation says 2022 somewhere.

## 16. pigac2026transparency

Bib: Pigac, Tin; Lee, Ada; Huang, Alice. Cornell Hospitality Quarterly, 2026, 67(3), 283–297, doi:10.1177/19389655261433944.

- **IDENTITY: DIVERGENT — two of three author given names wrong.** Raw Crossref JSON
  (Sage-deposited): **Tilen Pigac; Ada Lee; Ava Huang**. The bib has "Tin Pigac" and "Alice
  Huang"; only Ada Lee is right. Volume 67(3), 283–297; online 9 April 2026, print August 2026 —
  year and locators confirmed. The DOI exists and resolves; the entry's existence is not in doubt.
- **FULL TEXT: BLOCKED** — Sage 403; no OA copy (2026 paper, none expected yet).
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): 50 semi-structured guest
  interviews across three continents, segmented by a technology-comfort scale; develops a
  "Dynamic Transparency Protocol" — transparency preferences vary by guest profile and service
  stage via user-centric adaptation, situational sensitivity, and emotional matching;
  low-digital-comfort guests want human-mediated, simplified disclosure; framed as trust
  management. Matches the bib note, including its critical framing ("transparency as trust
  management rather than as an answer to a withholding").
- **FLAGS**: Fix "Tin"→"Tilen" and "Alice"→"Ava". The note itself said "Author list to confirm at
  proof" — confirmed now, and two of three were wrong.

## 17. pijls2017measuring

Bib: Pijls, Groen, Galetzka, Pruyn. IJHM, 2017, 67, 125–133, doi:10.1016/j.ijhm.2017.07.008.

- **IDENTITY: CONFIRMED** — raw Crossref registry record (Ruth Pijls; Brenda H. Groen; Mirjam
  Galetzka; Ad T.H. Pruyn; IJHM 67, 125–133, Oct 2017) and the published-version PDF itself
  (Elsevier-typeset, "International Journal of Hospitality Management 67 (2017) 125–133"),
  archived at the University of Twente repository.
- **FULL TEXT: OBTAINED** — published version via UTwente
  (https://ris.utwente.nl/ws/portalfiles/portal/16817924/measuring.pdf); read in full (9 pages).
  ScienceDirect itself is bot-walled.
- **WHAT IT ARGUES** (from full text): Develops and validates the Experience of Hospitality Scale
  (EH-Scale): 13 items, three factors — *inviting* (feeling invited, openness, experiencing
  freedom), *care* (support, involvement, treated like a king/queen, effort, relief of tasks and
  worries, interest, feeling important), *comfort* (at ease, comfortable, relaxed). It measures
  the guest's felt experience of hospitality in any service environment, deliberately shifted
  away from employee-behaviour ("hospitableness") scales.
- **FLAGS — this is the material finding for the claim audit.** The exploratory phase *did*
  surface an "autonomy" dimension ("the level of control over what happens seems to be part of
  the experience of hospitality"), but it did not survive validation as an agency measure: one
  autonomy item ("experiencing freedom") folded into the *inviting* factor, and the two items
  closest to guest agency — **"feeling independent" and "having choice" — were removed during CFA
  for low loadings**. The validated instrument therefore measures felt welcome, care, and
  comfort; guest agency survives only as a single "freedom" item inside *inviting*. Calling it
  an "affect scale" is slightly unfair (it is an experience scale with affective and relational
  content), but the claim-audit's worry is right in substance: **the EH-Scale cannot carry a
  claim about guest agency.** It can carry claims about guests feeling invited, cared for, and at
  ease — and it documents that the field's own instrument tried to keep control/choice items and
  lost them psychometrically, which is itself a citable fact if the manuscript wants one.

## 18. padigar2024friction

Bib: Padigar, Li, Manjunath. Psychology & Marketing, year field 2025, 42(1), 21–43, doi:10.1002/mar.22111.

- **IDENTITY: CONFIRMED** — raw Crossref registry record: Manjunath Padigar; Yi Li; Chandana N.
  Manjunath; Psychology & Marketing 42(1), 21–43; online 21 Aug 2024; print January 2025.
- **FULL TEXT: BLOCKED** — the article is CC-BY hybrid-OA at Wiley per Unpaywall, but Wiley's
  pdfdirect route serves a Cloudflare wall to both WebFetch and curl from this environment. A
  browser session would get it.
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): Defines friction as
  customer effort toward consumption goals; four types from task desirability × task value —
  frustrating, constructive, preference-based, rewarding; topic-modeling of frictionless-CX
  announcements shows practice eliminates all friction indiscriminately; eliminating constructive
  friction (low-desirability, high-value tasks) "may hinder value creation." The bib note's "four
  friction types, and eliminating constructive friction may hinder value creation" is verbatim-
  accurate.
- **FLAGS**: **Year dispute resolved: the year field (2025) is right** for the cited issue
  42(1):21–43; the citekey's "2024" records the online-first year. Same pattern as phillips —
  internally consistent, nothing to change except, optionally, the citekey.

## 19. rahman2021cage

Bib: Rahman. ASQ, 2021, 66(4), 945–988, doi:10.1177/00018392211010118.

- **IDENTITY: CONFIRMED** — raw Crossref registry record: Hatim A. Rahman (sole author); ASQ
  66(4), 945–988; online 21 Apr 2021, print December 2021. Same-year issue, no split.
- **FULL TEXT: BLOCKED** — Sage 403; Unpaywall closed.
- **WHAT IT ARGUES** (publisher-deposited abstract, via DOI registry): Three-plus years of
  interviews, archival data, and participant observation on a labor platform; freelancers
  experience an opaque evaluation algorithm as control but cannot align behavior with criteria
  they cannot identify; responses diverge (experimentation vs. constrained activity) by
  performance level, platform dependence, and score setbacks; names the "invisible cage" —
  control in which success criteria and their changes are unpredictable. The note's "control
  through measurement rather than command" is a fair compression.
- **FLAGS**: none.

## 20. raisch2021paradox

Bib: Raisch & Krakowski. AMR, 2021, 46(1), 192–210, doi:10.5465/amr.2018.0072.

- **IDENTITY: CONFIRMED** — raw Crossref registry record: Sebastian Raisch, Sebastian Krakowski;
  AMR 46(1), 192–210, January 2021.
- **FULL TEXT: BLOCKED this audit** — AOM 403 live; no OA copy. The **publisher abstract was
  recovered** from a Wayback snapshot of the journals.aom.org article page. (The bib note records
  readdepth=full from a prior pass.)
- **WHAT IT ARGUES** (publisher abstract, archived publisher page): Automation (machines take
  over a human task) vs. augmentation (humans collaborate closely with machines); against the
  normative "prioritize augmentation" advice, argues from paradox theory that in management the
  two "cannot be neatly separated" — they are interdependent across time and space, and
  overemphasizing either fuels negative reinforcing cycles; organizations should hold both. This
  is exactly the non-separability thesis the bib note says the manuscript absorbed as motivation.
- **FLAGS**: none. The note's task-allocation-level reading is consistent with the abstract.

---

## Summary table

| # | Citekey | Identity | Full text | Divergences / flags |
|---|---------|----------|-----------|---------------------|
| 1 | martinwaldman2022legitimate | CONFIRMED (Crossref + Springer PDF) | OBTAINED (publisher CC-BY PDF) | year 2022=online; issue 183(3) is 2023 (note discloses) |
| 2 | moganadas2026wellbeing | **DIVERGENT** (Crossref) | BLOCKED (MDPI Akamai 403) | 3 of 4 author names wrong: Sharmila Rani / Gerald Guan Gan / Chew Sze |
| 3 | mohlmann2021algorithmic | CONFIRMED (Crossref) | BLOCKED (MISQ Cloudflare; no OA) | none; matching+control = two parallel dimensions |
| 4 | morosan2016 | CONFIRMED (Emerald) | BLOCKED (subscription) | title subtitle truncated in bib |
| 5 | mosca2025phygital | **DIVERGENT** (Crossref) | BLOCKED (Sage 403) | 4th author "Hassan"→**Hafsa** Shakil; 46(3) is Sept 2026, bib says 2025 |
| 6 | nguyen2024stereotypes | **DIVERGENT** (Emerald) | BLOCKED (subscription) | year: 80(7):1413–1426 is 2025, bib says 2024 |
| 7 | odekerken2021service | CONFIRMED (Emerald) | OBTAINED (QUT ePrints CC-BY AAM) | none; 2022 correct for 33(2) |
| 8 | okhuysenbechky2009 | CONFIRMED (Crossref via doi.org) | BLOCKED (all routes); publisher abstract recovered via Wayback | three conditions confirmed at abstract level; body definitions unchecked |
| 9 | pan2025dark | **DIVERGENT** (Crossref) | BLOCKED (ScienceDirect bot-wall; no abstract anywhere) | given names wrong: **Su-Ying** Pan, **Yangpeng** Lin |
| 10 | papadopoulos2021violation | CONFIRMED (Crossref) | BLOCKED (Wiley) | none |
| 11 | parasuraman2000types | CONFIRMED (Crossref, initials only) | BLOCKED (IEEE all routes) | full given names not independently confirmed |
| 12 | park2026lobbies | **DIVERGENT** (Crossref) | BLOCKED (Sage 403) | given names wrong: **Soona** Park, **Jianan Z.** Lee |
| 13 | parkinson2022online | CONFIRMED (Crossref) | BLOCKED this audit (Sage) | none |
| 14 | pedersen2022 | **DIVERGENT** (OUP + Crossref) | BLOCKED (subscription) | year: 33(1):80–93 is 2023, bib says 2022 |
| 15 | phillips2024physical | CONFIRMED (Crossref + AAM title page) | OBTAINED (QUT ePrints AAM) | 3 authors re-verified; 2024 correct for print issue, DOI is the 2022 online DOI |
| 16 | pigac2026transparency | **DIVERGENT** (Crossref) | BLOCKED (Sage 403) | given names wrong: **Tilen** Pigac, **Ava** Huang |
| 17 | pijls2017measuring | CONFIRMED (Crossref + published PDF) | OBTAINED (UTwente published version, read in full) | agency items dropped in validation — see claim-audit finding |
| 18 | padigar2024friction | CONFIRMED (Crossref) | BLOCKED (Wiley Cloudflare, despite CC-BY) | year field 2025 correct; citekey 2024 = online year |
| 19 | rahman2021cage | CONFIRMED (Crossref) | BLOCKED (Sage) | none |
| 20 | raisch2021paradox | CONFIRMED (Crossref) | BLOCKED this audit; publisher abstract via Wayback | none |

Identity: 13 confirmed, 7 divergent (5 author-name corruptions, 2 pure year mix-ups; mosca has both).
Full text obtained and read: 4 (pijls in full; phillips, martinwaldman, odekerken at substantive depth).

## The three assigned disputes, resolved

**phillips2024physical — authors and year.** The author list is three names and only three:
Chelsea Phillips, Rebekah Russell-Bennett, Marek Kowalkiewicz — confirmed independently at the
DOI registry (T&F-deposited) and on the title page of the author-accepted manuscript at QUT
ePrints, with QUT affiliations. The previously invented Odekerken-Schröder/Mahr/Letheren names
appear nowhere. On the year: the paper went online 20 September 2022 (which is why the DOI string
and the © line say 2022) and reached its print issue — 44(13-14), pp. 919–948 — on 25 October
2024. The bib's "2024" is the print-issue year matching the volume/issue/pages it cites, so the
entry is internally consistent as it stands. The project's research pass and the bib are both
right; they are describing different publication events.

**padigar2024friction — 2024 vs 2025.** Registry record: online 21 August 2024, print issue
January 2025, and the bib cites the print locators 42(1):21–43. The year field (2025) is correct;
the citekey's 2024 records the online year and is harmless. No edit required.

**odekerken2021service — 2021 vs 2022.** Emerald's own page: online-first 25 August 2021, print
issue 33(2) on 28 February 2022, pp. 246–292. The bib cites the print issue, so 2022 is correct,
exactly as the note's 2026-08-17 re-verification concluded. The citekey's 2021 is cosmetic.

## Recommended fixes (in priority order)

1. **pan2025dark**: author given names → Pan, Su-Ying; Lin, Yangpeng.
2. **park2026lobbies**: author given names → Park, Soona; Lee, Jianan Z.
3. **pigac2026transparency**: author given names → Pigac, Tilen; Huang, Ava.
4. **mosca2025phygital**: fourth author → Shakil, Hafsa; and either year → 2026 or drop
   volume/issue/pages. SI-editor citation — highest visibility.
5. **moganadas2026wellbeing**: authors → Moganadas, Sharmila Rani; Goh, Gerald Guan Gan; Cheah,
   Chew Sze. Also downgrade the note's readdepth claim or re-read at proof.
6. **nguyen2024stereotypes**: year → 2025 (keeping 80(7):1413–1426), or drop locators.
7. **pedersen2022**: year → 2023 (keeping 33(1):80–93), or drop locators.
8. **morosan2016**: restore the publisher subtitle if house style keeps subtitles.
9. **pijls2017measuring**: wherever the manuscript leans on it for guest *agency*, re-anchor the
   sentence on inviting/care/comfort — the validated scale dropped its choice and independence
   items — or cite the dropped-items fact explicitly.

## Failed routes (so nobody repeats them)

Direct WebFetch 403: tandfonline.com, onlinelibrary.wiley.com, journals.sagepub.com,
journals.aom.org, misq.umn.edu, mdpi.com, sciencedirect.com (via linkinghub). curl with browser
UA also fails on all of these (Cloudflare/Akamai). link.springer.com article pages bounce through
an idp.springer.com redirect loop for WebFetch, but the /content/pdf/ route works for OA items.
MDPI blocks this network outright ("Access Denied", Akamai) — a browser or another network is
needed for MDPI full texts. Wayback snapshots of publisher pages work for AOM (with `--compressed`;
plain curl yields gzip garbage) but are rate-limited (429s; ~60–90s backoff needed), and the
archived ScienceDirect and IEEE pages are themselves archived block pages. Semantic Scholar's
API has no OA PDF for okhuysenbechky2009 or mohlmann2021algorithmic; scholar.archive.org has no
okhuysen copy; Möhlmann's personal site lists the paper without a PDF. No Chrome browser was
connected this session (claude-in-chrome extension not running), which is what kept the Sage and
Elsevier publisher pages out of reach.
