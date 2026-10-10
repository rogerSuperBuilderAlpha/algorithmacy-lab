# Part 4 — Argument map

<!-- Claude-drafted (lead session), 2026-10-04. Nothing here is author text. Each row points to a facet and
the facet's own locator. "Grade" is the read status of the weakest source the row depends on:
  [checked]  I opened the source and found the quoted words (literature/audit/AUDIT_00.md)
  [full]     a facet agent read the full text; not re-checked by me
  [abstract] read at abstract level only
  [T1–T3]    a statute, court or regulator document, or a company's own document (facet G's tiers)
Bearing: supports / complicates / refutes, against the four forms in README.md. -->

**Thesis under test.** Decision experience design (DXD) is not only a software or digital concept; there is
a physical decision experience design, and the phygital literature shows it.

**How to read this file.** Section 1 maps each argument the series already makes onto what the physical and
phygital literatures say about it. Section 2 gives what phygital researchers themselves raise. Section 3 is
the counter-case. Section 4 states what the evidence lets Part 4 claim. The case-by-case adjudication is in
`literature/facets/T_adjudication.md`; this file does not repeat its table.

## 1. The baseline arguments, extended

| # | Baseline argument (where the series makes it) | What the physical and phygital literature says | Source and locator | Grade | Bearing |
| --- | --- | --- | --- | --- | --- |
| B1 | DXD concerns an adaptive intermediary that reads several parties and commits an outcome binding on them (Part 1, l. 34) | Ride-hail carries all four marks with two people bound at one place: driver and rider meet at the kerb the app chose | E `cameron2024making` p. 486; `mohlmann2021algorithmic` pp. 2007–2010 | [checked] | supports form 1 |
| B1 | same | The airport gate carries all four marks, and a human gatekeeper commits what the system proposes | G (CBP, TSA, GAO, DHS 2025 rule); F `kitchin2009airport` ms p. 13 | [T1–T3]; [full] | supports form 1; complicates it (algorithm plus person) |
| B1 | same | In the warehouse the customer is an order; at the face-recognition kiosk the hotel is not read; in delivery the customer rates and is not rated | E, "Evidence against", item 1 | [full] | complicates form 1: "binds both" holds in two physical cases |
| B1 | same | A four-mark intermediary needs no physical layer: Rahman's freelance platform; Gandini, the platform is the point of production "irrespective of 'where'" | E `rahman2021invisible`; `gandini2019labour` p. 12 | [checked]; [full] | complicates form 4 |
| B2 | UX professionalised on ergonomics and moved outward from the hardware (Part 1, ll. 20, 70–80) | Computing moved into rooms and objects before it reached the decision. HCI's work on that stage models one user and one system; no source found models an intermediary reading two parties | D synthesis D3, "Evidence against" | [full] | the genealogy extends; no support for form 2 |
| B2 | same | Suchman: the machine reads "a restricted set of effects… onto a prescribed template" and she sets disclosure aside for engineering alternatives for repair | D `suchman1985plans` p. 124 | [full] | supports the not-legibility ruling with a 1985 precedent |
| B3 | Choice architecture has "a visible human designer, a static menu, and a single chooser" (Part 1, l. 48) | The predecessor's own taxonomists define physical choice architecture as "not designed to be interactive or tailored to specific individuals" and exclude the system that reads purchases | B `hollands2017tippme`, "Focus"; `hollands2013altering` | [checked] | supports form 3 with a boundary; supports the "holds still" test |
| B3 | same | Thaler and Sunstein's architect is "a figment"; most act "without realizing it"; "some nudges are unintentional" | B `thaler2008nudge` pp. 3, 10 | [checked] | refutes "visible" in Part 1 l. 48; "identifiable" (l. 42) stands |
| B3 | same | Bitner's servicescape already has two users, customers and employees, with conflicting needs the designer settles once | B `bitner1992servicescapes` pp. 58, 61 | [checked] for the words; pages are the facet's | refutes "single chooser" as a description of designed physical space |
| B3 | same | Servicescape and choice-architecture literatures do not cite each other in the texts obtained; the crossover runs one way | B body-text check (four reviews not obtained) | [full], incomplete | a gap Part 4 can state narrowly |
| B4 | Algorithmacy's three operations: interpreting, specifying intent, keeping track (Part 1, l. 94) | Observed among ride-hail and warehouse workers; no phygital customer study examines them | E synthesis E4 | [full] | supports form 1 for workers; open for customers |
| B5 | A competence, not disclosure, predicts decision quality (numeracy model; Part 1, ll. 122–124) | No study measures a competence moderating an outcome in a physical setting | E synthesis E5(a), searches logged | gap | the mechanism has no physical-setting evidence |
| B6 | Algorithmacy is not legibility (Part 1, l. 22; author ruling) | The phygital field's own remedies are legibility remedies: explain the change, signpost, inform | A synthesis A4; `wilsonnash2026captivity` | [checked] | Part 4 would be arguing against the field it enters through |
| B6 | same | At the airport, required signs naming the opt-out were absent or stale | G `gao2022facialtestimony` | [T3], partial read | supports B6: a disclosure that is not kept does not secure exit |
| B7 | Counter-delegation: the person gets their own agent (Part 1, l. 144) | No deployed tool acts for the worker or customer at the point of delivery; existing tools work on the record afterwards | E synthesis E5(b), searches logged | gap | no physical case yet |
| B8 | Structural refusal: a costless exit (Part 1, l. 146) | "App required" access produces "coerced participation in systems that have become unavoidable"; the rule needs no adaptive system | A `wilsonnash2026captivity` §2.1 | [checked] | supports form 4; shows form 4 holds without an algorithm |
| B8 | same | DHS's 2025 rule concedes citizens who declined face matching were sent to secondary screening or told they could not board; non-citizens lose the opt-out | G `dhs2025biometricrule` | [T1], partial read | supports form 4 |
| B8 | same | Exit is often graded, and sometimes designed in: Cameron's "programmed leniency"; Disney's free standby line | E `cameron2024making` p. 488; G Disney terms | [checked]; [T2] | complicates l. 146, which treats exit as costless or not |
| B8 | same | A physical structural refusal exists pre-digitally: the installer's shunt fuse on Akrich's charge regulator | C `akrich1987comment` §§31–34 | [full] | supports form 2 weakly |
| B9 | A declared operating envelope; behaviour that fails conspicuously (Part 1, l. 148) | SFpark changes prices by a published rule, by block, about every six weeks: the envelope principle in a physical deployment | G `sfmta2014sfparkevaluation`; Pierce and Shoup | [T3], partial read | supports form 1 narrowly; strains the "holds still" test |
| B9 | same | Amazon's stated reason for retreating from cashierless checkout in its grocery stores: shoppers wanted a running receipt on the cart | G Amazon post | [checked] (live page) | supports form 4: people asked for a conspicuous commitment |
| B10 | Seamful design (Part 1, l. 152) | Weiser's own 1994 slides: "seamful systems, with beautiful seams". Seamful design did not begin as a reply to him | D `weiser1994invisible`, slide 19 | [checked] | corrects the usual history |
| B10 | same | Chalmers's seams are technical limits that users exploit; the disclosure sense comes from Ehsan 2024 | D synthesis D2 | [full] | Part 1's gloss fits Ehsan, not Chalmers |
| B10 | same | 118 works join "phygital" to "seamless"; one joins it to "seamful". Bell and Dourish called seamlessness "a chimera" in 2007 | D gap search; `belldourish2007yesterdays` | [checked] for Bell and Dourish | supports Part 4: phygital researchers repeat a position HCI answered |
| B11 | A dark pattern is known by its effect (Part 3 draft) | No located work calls a physical structure a dark pattern. The idea exists under other names; the hostile-design literature is split on intent | F synthesis F4; `rosenberger2023classification` p. 56; `petty2016london` | [full] | Part 4 would rename; it cannot cite that literature for either side without saying which |
| B11 | same | Greenberg et al. applied "dark patterns" to proximity-sensing systems in 2014, with captivity as a pattern | X `greenberg2014dark` §1 | [full] | prior art on the extension off the screen |
| B12 | The designer's obligation rests on mandatory participation (Part 2 draft) | Exit is priced in physical arrangements with no intermediary: the turnstile, the GP surgery, the station through which most passengers must pass | A `wilsonnash2026captivity`; B `baron2019designing` | [checked]; [full] | Part 2's ground reaches arrangements Part 1 files under choice architecture |
| B12 | same | The casino and the theme park are voluntary venues | F; Part 3 draft l. 77 | [full] | Part 2's ground does not reach two of the leisure cases |
| B13 | Scripts and prescription (Part 2 draft, l. 99) | Latour's artifacts bind one party, the user, for an absent designer; sensing runs under a fixed rule | C `latour1992missing`, case table | [checked] | refutes form 2 through Latour |
| B13 | same | Akrich's electricity meter binds producer and consumer: "il faut « l'accord » des deux pour le faire tourner"; she calls it an arbiter | C `akrich1987comment` §§26, 30 | [checked] | supports form 2: two marks, holds still |
| B13 | same | The Moses bridges story is contested: Joerges shows commercial traffic was barred from the parkways anyway | C `joerges1999politics` | [full]; 6 of 11 quotations matched by me | Part 4 must not repeat the story |
| B13 | same | Joerges: built form rarely binds; "control rights" do | C `joerges1999politics` p. 20 | [full] | refutes a strong form 4 |
| B14 | A decision differs from a choice; the test at the match (Part 3 draft) | The test applies only where two parties' outcomes are committed together. Nine of the adjudicated arrangements have no such moment | T section 4, strain 5 | — | the test grades exchanges; it is not a mark of DXD |
| B15 | The history of reading is an analogy (Part 2 draft) | Nothing in the run bears on it | — | — | carried unchanged |

## 2. What phygital researchers raise

| # | Issue | Who raises it | Grade | Bearing |
| --- | --- | --- | --- | --- |
| P1 | The term lacks a definition; "Vagueness in using the term characterises most of the studies"; an "ontological 'mess'" | Mele et al. 2023, §§1, 3.1, 4 | [checked] | the field concedes thin theory (counter-case X2) |
| P2 | Phygital should mean a framework for the customer's movement between physical and digital settings, made "fluid" | Batat, PH-CX framework | [abstract] — **gate not met** | the essay's entry point rests on an abstract |
| P3 | The real/digital dichotomy is "no longer clearly sustainable"; phygital materiality has "intelligence and autonomy" | Mele and Russo-Spena, agencement paper, pp. 224, 217 | [checked] for the first; [full] for the second | cuts both ways: the split may be obsolete, and the field already names two of the marks |
| P4 | "algorithmic mediation of agency" and "digitally enforced rules" in phygital service | Shabnam et al. 2026 | [full] | form 1 is partly pre-stated in the field's vocabulary |
| P5 | Digital technology captivity: being compelled to use a digital layer to reach a physical service | Wilson-Nash et al. 2026 | [checked] | form 4; the inclusion issue the author named |
| P6 | Friction is a defect to remove; some defend it | Padigar 2025; A synthesis A3 | [full] | sets up the seamless/seamful contrast |
| P7 | Physical retail is "static and non-adaptive"; phygital design is "adaptive responsiveness within shared physical space" | Barlow and Johnson 2026 | [abstract], confirmed by me on the publisher's page | **prior art on the test's central contrast** |
| P8 | Customer and employee are "rarely examined together" | Mulcahy et al. 2026, as reported in A | [abstract] | no phygital paper models a match binding two parties: the room Part 4 has |

## 3. The counter-case

| Line | Strongest form | Grade | Rating (facet X) | What answers it, and how far |
| --- | --- | --- | --- | --- |
| X1 | Physical DXD is servicescape and choice architecture renamed | Bitner and Kotler read in full by facet B | strong on scope | Hollands's exclusion of tailored, interactive interventions (B). It answers the line only for cases that read and adapt |
| X2 | "Phygital" is a marketing coinage with thin theory | Mele et al. 2023 | strong | Not answered. The origin story (an agency, 2007) rests on secondary web pages |
| X3 | Part 1 contradicts Part 4: either every physical case has an algorithm behind it and Part 4 is Part 1 with a door attached, or a case without one counts and Part 1's boundary is repealed | Part 1, ll. 34, 42, 48, 118 | **most damaging** | T: the four-mark cases have an algorithm behind them; what the door adds is control during the task and a second body. The second horn depends on the author's ruling on human readers |
| X4 | Others said it: ubiquitous computing, smart-city critique, Lessig's architecture, Latour | Weiser 1991; Kitchin 2014; Lessig 2006 | moderate | None of them models the two-party match (D, C). Barlow and Johnson state the contrast |
| X5 | Exit is cheap in physical space | Hirschman 1970 on the shop | moderate | Wilson-Nash, Baron, the DHS rule: exit is priced in specific settings (A, B, G) |
| X6 | Static physical design works and is cheap | Nudge meta-analyses, food domain | weak to moderate | Not in dispute; it is form 3 |
| X7 | "Holds still" does not separate anything: stores re-merchandise from data, and hotel desks quoted yield-managed rates in 1989 | Kimes 1989, p. 14 | moderate | Hollands and Grant draw the line at tailoring and interaction. A threshold is still owed (T, strain 2) |

## 4. What the evidence lets Part 4 claim

From `T_adjudication.md`, section 3. Each is the narrowest statement the facets support.

1. **Form 1 holds for two cases.** Where a platform that is neither party reads both and commits a match, the physical layer is where two people honour it at once, under a clock, during the task. Ride-hail shows it; the airport gate shows it with a human at the point of commitment.
2. **Form 2 has no four-mark case.** A physical device can hold and enforce a two-party contract (Akrich's meter). A human reader can read both, bind both and adjust. Nothing without a digital system does all four. Whether the human cases count is the author's ruling.
3. **Form 3 is the default verdict.** An arrangement that reads no one in the encounter and applies one rule to everyone is choice architecture by that field's own definition, with or without a chip. This covers most of what the facets document.
4. **Form 4 is the best-evidenced and the least distinctive.** A ruling becomes a fact in a place and leaving has a price there, but that is true of rulings in general. What marks the algorithmic cases is whether a person is present to answer for the ruling.

Two cross-cutting findings: in most physical settings the intermediary is an algorithm plus a person (E, F); and the adaptive physical case is older than the web platform (the tracked casino floor from the mid-1980s; yield-managed front desks by 1989), so form 1 cannot be told as a history of the algorithm arriving in physical space.
