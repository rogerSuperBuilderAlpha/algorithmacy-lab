# V5 — Scaffolding: what it would mean to build a person's growth into a new competence, and who did it

*Facet V5, research round 7, 2026-10-14. Agent-drafted (Claude). None of the text is the author's. Notes for the
drafter, not prose for the paper.*

**What this facet covers.** The evidence for and against wrong (c) of the v4 thesis: that Nadella's post (and the
oral-to-literate transition before it) fails by "not scaffolding the person's growth" to the new competence
(algorithmacy). Five questions: (1) what "scaffolding" means in learning science (Wood, Bruner and Ross 1976;
Vygotsky's zone of proximal development; Collins, Brown and Newman's cognitive apprenticeship); (2) what it means
in design for algorithmic systems (seamful design, folk theories, explanatory debugging, boosts versus nudges);
(3) who historically built people's capacity to read, who paid, and with what result; (4) the capability
approach on literacy and the duties it implies; (5) the case against: paternalism, the weak record of
literacy-education programmes, and responsibilization.

**Read-depth marks.** *Full* = whole text read this session or on a verified card; *Part* = the named pages or
sections read; *Abstract* = abstract or database summary only; *Record* = bibliographic record only.

## Method notes

Search log (appended as the run proceeds).

| # | Tool | Query or target | Result |
| --- | --- | --- | --- |
| 1 | repo read | `v4/RESEARCH_BRIEF.md`, `v4/SOURCE_v4.md`; this arm's facets C, F, M2, M4, M5, N3, Z (grep for Freire, Cuba, scaffold, capability, Sunday school, Self-Taught); card list | Freire ch. 2, Cuba (M5), Sunday schools (C, not opened), Self-Taught (Margo review, carded), capability SEP entry (M4) already held. Cards `johansson1985popular`, `washington1901up`, `brandt1998sponsors`, `kamperman2026ai`, `margo2005williams`, `graff1991literacy`, `street2003whats` exist. |
| 2 | repo read | sister arm `dxd_foundation/literature/`: `library/hertwig2017nudging.md`, `library/ehsan2024seamful.md`, facets L, I, M, G | Hertwig and Grüne-Yanoff card (verified, corrected); Ehsan seamful-XAI card; Fernandes et al. read in part (WP); Eslami 2016 and DeVito 2021 abstract-level in facet I; Bucher 2017 bibliographic only (facet M, no authorised copy). Facet G records Nadella's Dec 2025 post calling AI "a scaffolding for human potential". |
| 3 | WebSearch | Wood, Bruner & Ross 1976 pdf; six functions | No authorised full text; Wiley PDF returns 403. Secondary only. |
| 4 | archive.org FTS (`be-api.us.archive.org/fts/v1/search`) | "beyond his unassisted efforts"; six function names | Dozens of secondary quotations, all attributing the definition to p. 90. The original not reachable. |
| 5 | archive.org (OAPEN mirror) | Belland 2017, *Instructional Scaffolding in STEM Education* (open access, CC BY-NC) | Downloaded `V5/belland2017.pdf`; read ch. 1 pp. 1–6 and ch. 2 pp. 17–28. |
| 6 | archive.org FTS over the lending scan `mindinsocietydev0000vygo` (not borrowed) | "zone of proximal development", "level of potential development", "more capable peers", "functions that have not yet matured", "good learning" | Snippets only; no printed page from the API. Contents snippet places ch. 6 at p. 79. |
| 7 | ERIC | Collins, Brown & Newman 1987, Technical Report 403 (ED284181) | Downloaded `V5/collins1987eric.pdf`; read report pp. 1–8. |

## Findings

### Q1. Scaffolding in learning science

**Wood, Bruner and Ross (1976), `wood1976role`. Secondary (no original read).** *J. Child Psychology and
Psychiatry* 17(2), 89–100, DOI 10.1111/j.1469-7610.1976.tb00381.x (PubMed 932126; Wiley 403). The definition every
secondary source quotes, attributed to p. 90: scaffolding is a process "that enables a child or novice to solve a
problem, carry out a task, or achieve a goal which would be beyond his unassisted efforts" (wording as quoted in
ERIC ED446926 and ED442640, both giving p. 90; seen as archive.org full-text snippets, not in the original). The six
tutor functions — recruitment, reduction in degrees of freedom, direction maintenance, marking critical features,
frustration control, demonstration — are listed in that order across secondary sources (PMC4021139; Belland 2017, p. 22, groups recruitment, frustration control and direction maintenance as support for motivation, and
the other three as support for cognition). *Do not quote the original until the author supplies the PDF.* **Flag for the brief:** the
word "fading" is not Wood, Bruner and Ross's. Belland (2017, p. 21) says the removal of support "was later termed
'fading' by Collins et al. (1989)".

**Belland (2017), `belland2017instructional`. Part** (ch. 1 pp. 1–6; ch. 2 pp. 17–28). *Instructional Scaffolding
in STEM Education*, Springer, open access, DOI 10.1007/978-3-319-02565-0. The most useful single source for what
"scaffolding" requires, because it draws the boundary the thesis needs.
- Definition: "interactive support that leverages what students already know to help them meaningfully participate
  in and gain skill at tasks that are beyond their unassisted abilities" (p. 5, citing Wood et al. 1976 and others).
- What does **not** count: "a calculator does not qualify as a scaffold because while it supports current
  performance, it cannot be reasonably expected to help users calculate independently ... in the future" (p. 5);
  "simply telling students what to do or how to do it does not qualify as scaffolding" (p. 6); "Support that
  continues indefinitely does not meet the scaffolding definition either" (p. 18); "A job aid does not meet the
  definition" (p. 19); "If the tool does all or most of the work ... the possibility of skill gain is compromised"
  (p. 19).
- Contingency: scaffolding pairs "dynamic assessment of the child's current performance characteristics and
  provision of just the right support" (p. 18); it requires "intersubjectivity", a shared understanding of what
  success looks like (p. 18).
- Fading "is designed to gradually transfer the responsibility for the performance of the target skill from the
  scaffold provider to the scaffold receiver" (p. 21).
- The term is imprecise: "the lack of precision that has emerged in the term scaffolding ... an often-lamented
  phenomenon (Pea, 2004; Puntambekar & Hübscher, 2005; Stone, 1998)" (p. 18).
- Effect: in Belland's meta-analysis "the average effect size of computer-based scaffolding was 0.46", above the
  0.13 and 0.16 averages for educational technology in mathematics and reading (p. 27). Population: STEM students,
  K-12 to adult, problem-centred instruction.
- *Bearing:* **for** wrong (c) and **narrows** it. For: by this definition a disclosure is "telling", and a readable
  record is a job aid; neither scaffolds. Narrows: an AI tool that does the work, and any permanent design aid —
  including the sister arm's DXD conventions, which change what the mechanism asks of a person — is a calculator in
  Belland's sense, not a scaffold. If the paper says the post "fails to scaffold", it must say it means support
  aimed at the person's later independent competence, and it must accept that permanent re-representation is a
  different remedy.

**Vygotsky (1978), *Mind in Society*, ch. 6, `vygotsky1978mind`. Snippet** (archive.org full-text search over the
Harvard UP lending scan `mindinsocietydev0000vygo`; not borrowed; printed page not given by the API; the contents
snippet puts ch. 6, "Interaction between Learning and Development", at p. 79). Three overlapping snippets, joined by
me: the zone of proximal development "is the distance between the actual developmental level as determined by
independent problem solving and the level of potential development as determined through problem solving under
adult guidance or in collaboration with more capable peers." Other ch. 6 snippets: the zone "defines those
functions that have not yet matured but are in the process of maturation"; such functions are "the 'buds' or
'flowers' of development rather than the 'fruits'"; "the only 'good learning' is that which is in advance of
development"; learning "awakens a variety of internal developmental processes". *The common citation to p. 86 is
unverified here; check in the book.*
- *Bearing:* **for** and **narrows**. The zone is defined by the presence of someone more capable. For a reader of
  print, the more capable peer was any literate neighbour. For an adaptive, proprietary system, the only party that
  knows the system's workings is its operator. That supports placing the duty to scaffold on the holder of the
  means (Q4), and it narrows the claim: ordinary users cannot scaffold one another in the way literate peers could.

**Collins, Brown and Newman (1987/1989), `collins1987cognitive`. Part** (ERIC ED284181, BBN/CSR Technical Report
403, January 1987, report pp. 1–8; the 1989 chapter in Resnick (ed.), *Knowing, Learning, and Instruction*, is the
usual citation and was not read). Cognitive apprenticeship was built **for teaching reading and writing** — the
title is "Teaching the Craft of Reading, Writing, and Mathematics".
- Standard schooling "render[s] key aspects of expertise invisible to students" (p. 2).
- Apprentices learn by "observation, coaching, and practice, or what we, from the teacher's point of view, call
  modelling, coaching, and fading"; "A key aspect of coaching is the provision of scaffolding, which is the support,
  in the form of reminders and help, that the apprentice requires"; then "the master reduces his participation
  (fades)" (pp. 2–3).
- Craft apprenticeship works where the process "is external and thus readily available to both student and teacher
  for observation"; for cognitive skills it "requires the externalization of processes that are usually carried out
  internally" (p. 4).
- In reciprocal teaching of reading, "students get as much support as they need to carry out the task, but no more.
  Hints and modelling are then gradually faded out" (p. 7).
- *Bearing:* **for** wrong (c). Its premise is that reading itself had to be scaffolded, because the expert's
  process is invisible; the parallel for algorithmacy is that the system's process is invisible to the person
  and visible only to its operator. Externalising the process is the operator's move to make. The text is a
  technical report on schoolchildren; it says nothing about firms or platforms.

### Q2. Scaffolding in design for algorithmic systems

Search additions: OpenAlex records and abstracts (DOI lookups and title searches) for Eslami et al. 2015 and 2016,
DeVito et al. 2017, Bucher 2017, Kulesza et al. 2015, Chalmers 2003; ACM full texts 403; IDEALS (UIUC) 403;
Glasgow Enlighten has no full text for Kulesza; City, University of London repository holds the accepted version
(`V5/kulesza2015.pdf`).

**Kulesza, Burnett, Wong and Stumpf (2015), `kulesza2015principles`. Full** (accepted manuscript, City Research
Online eprint 13819, 11 pp.; pagination is the manuscript's, the IUI proceedings run pp. 126–137, DOI
10.1145/2678025.2701399). *Explanatory Debugging*: "the system explains the reasons for its predictions to its end
user, who in turn explains corrections back" (p. 2). Principles: be sound, be complete, but don't overwhelm (pp.
3–4); be actionable, be reversible, always honour user feedback, incremental changes matter (p. 4). Their earlier
study "relied on human instructors to help participants build useful mental models" (p. 3) — this paper moves
that tutoring into the system. Experiment: 77 participants from the community and university with no more than
introductory programming, 37 control (black-box labelling) and 40 treatment, 30 minutes, a hockey/baseball text
classifier (p. 8). Treatment participants "scored 52% higher on the mental model assessment" (W = 259, p < .001)
and each of their feedback actions was worth roughly two of the control group's (pp. 10–11); mental-model score
correlated with classifier F1, ρ = .282 (p. 11); NASA-TLX showed no extra workload (p. 10).
- *Bearing:* **for** wrong (c), with a narrow scope. It is the cleanest measured case of a system that scaffolds a
  person's understanding through a two-way loop rather than a text to read, and it replaces the human instructor.
  **Narrows:** the person owns the classifier and its goal; the system has no interest against the user; the task
  is 30 minutes in a lab. It says nothing about systems run by a party whose interests diverge from the user's,
  which is the post's case.

**Eslami et al. (2016), `eslami2016first`. Abstract** (OpenAlex; ACM closed; DOI 10.1145/2858036.2858494,
CHI '16, pp. 2371–2382). Qualitative lab study, 40 Facebook users, 10 folk theories of curation. "Users who were
given a probe into the algorithm's operation via an interface that incorporated 'seams,' visible hints disclosing
aspects of automation operations, could quickly develop theories. Users made plans that depended on their
theories." The authors conclude that foregrounding automated processes "may increase interface design complexity,
but it may also add usability benefits." Also held in the sister arm (facet I, abstract level).
- *Bearing:* **for**, as design practice: seams are disclosures, but disclosures shaped so that a person forms and
  tests a theory, which is closer to scaffolding than to a readable record. **Narrows:** this is the researchers'
  probe (FeedVis), not a platform's design; no outcome beyond theory formation and stated plans is measured.

**Eslami et al. (2015), `eslami2015always`. Abstract** (OpenAlex/IDEALS record; ACM DOI 10.1145/2702123.2702556,
CHI '15). 40 Facebook users; "more than half of the participants (62.5%) were not aware of the News Feed algorithm
at all"; after FeedVis, satisfaction two to six months later was similar, but "algorithmic awareness led users to
more actively engage with Facebook and bolstered their overall feelings of control on the site."
- *Bearing:* **narrows**. Awareness raised feelings of control and engagement; it did not show greater competence,
  and "feelings of control" is the outcome Vaccaro et al. (2018, sister arm facet H) show can be a placebo.

**Chalmers (2003), `chalmers2003seamful`. Abstract** (IEE Eurowearable '03, pp. 11–16, DOI 10.1049/ic:20030140).
Seamful design questions "the assumption that seamless integration ... is necessarily a design requirement"; when
seams show, "users perceive and appropriate them for their own uses"; he proposes "making it a deliberate policy
to reveal and use seams." Chalmers and MacColl's 2003 UbiComp workshop paper, the usual citation, was not located.
Ehsan et al. (2024) carry the idea into explainable AI; the sister arm's card (`dxd_foundation/literature/library/
ehsan2024seamful.md`, partial, S2-corrected) finds the evidence formative (43 practitioners, no end-user test) and
notes that "strategic revelation and concealment" leaves the choice of seams with the builder.
- *Bearing:* **narrows**. Seamful design is the design tradition nearest to scaffolding, but its record is
  design-method reports, and the builder decides which seams the person may see.

**DeVito, Gergle and Birnholtz (2017), `devito2017algorithms`. Abstract** (OpenAlex; ACM 403; DOI
10.1145/3025453.3025659, CHI '17, pp. 3163–3174). Content analysis of 102,827 #RIPTwitter tweets: resistance to
algorithmic change "largely revolves around expectation violation, with folk theories acting as frames"; more
detailed folk theories go with more specific reactions. DeVito (2021) (`devito2021adaptive`, this arm N3 and sister
facet I, abstract): because platforms change, users "must constantly re-evaluate their folk theories."
- *Bearing:* **for**, indirectly. People build the competence themselves, unaided, from outcomes and rumour —
  self-taught, like the freedpeople (Q3) — and the platform's changes undo what they built. That is the
  condition under which a person cannot reach competence without the operator's help. **Narrows:** these are
  descriptive studies; none tests an intervention.

**Bucher (2017), `bucher2017algorithmic`. Abstract** (DOI 10.1080/1369118x.2016.1154086; ICS 20(1), 30–44; sister
facet M found no authorised copy). Tweets and interviews with 25 ordinary users; the "algorithmic imaginary —
ways of thinking about what algorithms are, what they should be and how they function" plays "a generative role in
moulding the Facebook algorithm itself."
- *Bearing:* **narrows**. Users are not empty vessels to be scaffolded; they already act on the system through
  their imaginaries, and the system learns from them. Wrong (c) must not describe the person as competence-less.

**Hertwig and Grüne-Yanoff (2017), `hertwig2017nudging`. Full (reused; sister arm card verified and corrected,
`dxd_foundation/literature/library/hertwig2017nudging.md`).** Boosts "target competences rather than immediate
behavior" (p. 977); reversibility test: if behaviour persists after the intervention is removed, it was more likely
a boost (p. 981); boosts must be "explicit, visible, and transparent" and so respect autonomy (p. 982); "The mere
provision of information is often not enough" (p. 977); boosts can equip people for "commercially constructed
choice architectures and industry nudges" (p. 981); whether boosts beat nudges "is an empirical question" (p. 978).
- *Bearing:* **for** wrong (c) as a frame: a disclosure regime is an "educative nudge" at most (p. 977), and the
  boost is the named alternative that builds competence. **Narrows:** the authors claim no superiority for boosts,
  and a short-term boost includes changing the representation (natural frequencies, p. 977), which covers what the
  sister arm calls re-representation. The scaffold/calculator line in Belland (Q1) and the long-term/short-term
  boost line here are the same line drawn twice.

### Q3. Who historically scaffolded the move to reading, who paid, and what came of it

Search additions: archive.org full-text search for the UNESCO Cuba report (Lorenzetto and Neys 1965: cited
everywhere, not digitised that I could find; UNESDOC returns 403 to scripts and to WebFetch); Bhola (1984) found as
an open microfiche scan (`micro_IA41948409_0395`, downloaded to `V5/bhola1984.pdf`, OCR text extracted; printed page
= PDF page + 3); Boughton and Durnan (2014), open at the University of Malta repository (`V5/boughton_cuba.pdf`);
Williams, *Self-Taught*, and Freire and Macedo (1987) as full-text-search snippets over lending scans (not
borrowed); Alvord's 1866 Bureau report as reprinted in Fleming (1905), open scan `reconstructionof01flem`.

**Bhola (1984), `bhola1984campaigning`. Part** (Cuba chapter pp. 88–105; ch. "Why literacy?" pp. 30–31; Brazil
chapter pp. 126–136). UNESCO, Paris, *Campaigning for Literacy: Eight National Experiences of the Twentieth
Century*. The book "advocates the literacy campaign" (Preface) — a sponsor's own assessment; Cuban figures are
official, via Fagen and Kozol.
- *Cuba 1961 — who scaffolded.* Schools closed for eight months; "everyone of 13 years and older, including
  teachers" went to teach peasants, lodging "in the homes of illiterates, teaching small groups of two to three
  adults" (p. 92). About 100,000 instructors were trained at Varadero; the final force was 268,420 (popular
  instructors 120,632; workers' brigades 13,016; Conrado Benítez student brigades 100,000; teachers 34,772) (p. 97).
  No classes: tutors met learners at home, a ratio "of 1:3 and sometimes 1:2", which "gave adult illiterates greater
  confidence" (p. 98). Three tests: initial, intermediate (monitoring), final (p. 102). Itinerant "Study Coaches"
  went to the most isolated learners (p. 100).
- *Who paid.* The state's National Literacy Commission had a finance section (p. 95); each brigadista received a kit
  and "ten pesos a month for incidental expenses" (p. 98); the labour was mobilised, not hired.
- *Outcomes.* Illiteracy of 23.6 per cent (age 10+) among 979,207 people; "made 707,212 literate during 1961,
  resulting in an illiteracy rate of only 3.9 per cent" (p. 100), at "approximately" the end-of-first-grade level
  (p. 100). Follow-up: *El Placer de Leer* distributed free, rural libraries, the *Seguimiento* course from February
  1962; "some 586,000 people returned to school" for sixth grade, about 65,500 graduating by 1966 (pp. 102–103).
  The municipal files "merely provided numerical data on the number of persons declared literate" (p. 104).
- *Whom it served.* The primer *Venceremos*'s lessons included "The Revolution; Fidel is Our Leader" (p. 100); the
  follow-up meant "recruitment through education of the erstwhile underprivileged into the service of the
  revolution" (p. 102); adult-education objectives include "the Marxist-Leninist conception of the world" (p. 103);
  Bhola's lesson 2: "Literacy campaigns cannot be justified in purely economic terms. Ideological justifications are
  necessary" (p. 104).
- *Brazil's MOBRAL (1967–80).* Funded by government, 6.75 per cent of the Sports Lottery and a 2 per cent
  corporate tax deduction; US$66 million in 1979 (p. 129). Its reading method has "the same" technical structure as
  Freire's, but the generative themes "set the two methods apart" (p. 130) — the military regime kept Freire's
  technique and dropped his content. External evaluations found instructor training "lasting only a few days" and
  "failure, in many cases, in follow-up" (p. 134); "critics have not always been convinced of the validity of
  official statistics" (p. 136).
- *General.* "literacy has not always been used exclusively for conscientization but also for mystification and for
  creating and reinforcing dependencies" (pp. 30–31).
- *Bearing:* **for** wrong (c) — the record contains large, measured, sponsor-funded scaffolding of adults (one tutor
  to two or three learners, in the learner's home, with tests and follow-up), so "not scaffolding" is a choice, not
  a historical impossibility. **Narrows** — every well-funded scaffold in this record served its sponsor's
  project (revolution in Cuba; a military regime's development plan in Brazil), which is Brandt's point; and the
  measured outcome was a first-grade reading level.

**Boughton and Durnan (2014), `boughton2014cubas`. Part** (pp. 325–330, 345–346). *Postcolonial Directions in
Education* 3(2), 325–359. Cuba's *Yo, Sí Puedo* model descends from 1961 and has "mobilised over six million
people in twenty-nine countries" (abstract, authors' report); "the enthusiasm for mass campaigns ... came up
against opposition from the World Bank, which used its increasing control over international education aid funding
in the 1980s to call a halt" (p. 327, citing Jones 1990). Cuba's 1961 campaign "pre-dated Freire's initial work in
Brazil, and was one of its inspirations" (p. 345). Authors are participant-researchers in Timor-Leste's campaign.
- *Bearing:* **for** (scaffolding at scale is a funding decision that funders have refused) and **narrows**
  (written by advocates).

**Alvord (1866), report of the inspector of Freedmen's Bureau schools, `alvord1866report`. Part** (as reprinted in
Fleming 1905, *The Reconstruction of the Seceded States, 1865–76*, NY State Education Dept syllabus, pp. 144–146;
original: report of 1 January 1866, Senate Ex. Doc. 39th Cong., 1st Sess.). "in very many places I have found
what I will call 'native schools,' often rude and very imperfect, but there they are, a group, perhaps, of all ages,
trying to learn. Some young man, some woman, or old preacher, in cellar, or shed, or corner of a negro meetinghouse,
with the alphabet in hand, or a torn spelling book, is their teacher" (Fleming p. 145). Adults "gladly avail
themselves of the evening and Sabbath schools"; in colored regiments "nearly every man can now read" where few
knew their letters, with officers and chaplains as teachers (p. 144).
- *Bearing:* **for** — the freedpeople scaffolded one another before any sponsor arrived; the state's own
  inspector recorded it. This matches Washington's "a whole race trying to go to school" (`washington1901up`, p. 30)
  and the community-paid teacher (p. 29).

**Williams (2005), *Self-Taught*, `williams2005self`. Snippet** (archive.org full-text search over lending scan
`selftaughtafrica0000will`; not borrowed; no printed pages). Freedpeople "constructed school buildings, provided
churches for use as schools, paid tuition when they could afford to, and frequently operated completely
self-sustaining schools"; one school "With 150 students ... was fully self-sustaining, receiving no assistance from
the Freedmen's Bureau"; Williams quotes Morris that "Black education was a cooperative venture involving the
Freedmen's Bureau, benevolent societies, and a corps of teachers that by July 1870 numbered 3,500"; she records
"wrangling with northern white missionaries over control of schools". The arm's card `margo2005williams` (verified)
adds the 1868 federal finding that Black teachers "accounted for slightly more than half of those teaching
ex-slaves" (p. 590) and the census decline in illiteracy from 84 per cent (1870) to 26 per cent (1920) (p. 590).
- *Bearing:* **for** and **narrows**. For: the people denied literacy built their own scaffolds and paid for them,
  and the sponsors (Bureau, missionaries) arrived second and fought for control. Narrows: the strongest historical
  scaffold was self-organised, not supplied by the holder of the means — which cuts against making the operator
  the scaffolder and toward the person's own collective action.

**Freire and Macedo (1987), *Literacy: Reading the Word and the World*, `freire1987literacy`. Snippet** (lending scan
`literacyreadingw00frei`; not borrowed; no printed pages, except a running head placing "Literacy in Guinea-Bissau
Revisited" at about pp. 95–99). "Reading the world always precedes reading the word, and reading the word implies
continually reading the world" (two overlapping snippets, joined). On Guinea-Bissau, the
dialogue discusses the decision to "adopt the Portuguese language as the main vehicle in the literacy campaign"
(snippet; who decided is not shown); Freire: "My method did not
fail, as has been claimed. Nor did it fail in Cape Verde or Sao Tome"; "What I could not do in Guinea-Bissau is
overstep the political limitations of the moment." Freire (1970, ch. 2) on "banking" education (p. 72) is held in
facet F (read in part).
- *Bearing:* **for** wrong (b) and (c) together: a campaign conducted in the colonial written language — not the
  learners' spoken Creole — is the clearest historical case of teaching people in a medium that is not theirs, and
  even Freire's defenders concede the outcome there was contested. **Narrows:** the snippets give Freire's defence,
  not the critics' evidence; do not state outcomes for Guinea-Bissau from this source.

**Sunday schools and the sponsor's limit (held in facet C).** Hannah More, 1801: "My plan of instruction is
extremely simple and limited ... I allow of no writing for the poor. My object is not to make fanatics, but to
train up the lower classes in habits of industry and piety" (Roberts 1835, vol. II, p. 72; `roberts1835memoirs`,
facet C entry 14, read in part). Laqueur (1976) not opened.
- *Bearing:* **narrows** — the sponsor scaffolded reading and withheld writing: the person could receive texts and
  not answer them. This is the closest historical analogue to a regime that builds the capacity to read the
  operator's records while withholding the means to act on the system.

**Johansson (1985), `johansson1985popular` (card, full, corrected).** The Swedish church taught reading through the
home, tested at confirmation, communion, marriage and migration, and held people "to the book" by "worldly compulsion
and church discipline" (p. 64); peasants resisted "costly school systems" because reading "had no obvious practical
use" (p. 63). **Narrows:** the most successful pre-industrial reading campaign was coercive scaffolding by the
sponsor, with access to marriage as the sanction.

**Brandt (1998), `brandt1998sponsors` (card, verified).** Sponsors "enable, support, teach, model, as well as
recruit, regulate, suppress, or withhold literacy—and gain advantage by it in some way" (p. 166); their interests
and the learner's "do not have to converge" (p. 166). **Narrows** every "for" item above: a firm that scaffolds its
users' algorithmacy is a sponsor in Brandt's sense and will set the terms.

### Q4. The capability approach: literacy as a capability, and what follows for those who hold the means

Search additions: archive.org full-text search over the Harvard UP lending scan of Nussbaum (2011)
`creatingcapabili0000nuss` (not borrowed; no printed pages); the SEP entry (Robeyns and Byskov) held locally from
facet M4 (`berthon_ethics_local/pdfs/M4/sep_capability-approach.txt`); Sen (1999) — the only archive.org copy is a
community upload I did not use; record only.

**Nussbaum (2011), *Creating Capabilities*, `nussbaum2011creating`. Snippet.** The list's fourth capability,
"Senses, imagination, and thought", is to be exercised in a way "informed and cultivated by an adequate education,
including, but by no means limited to, literacy and basic mathematical and scientific training" (two snippets,
joined). The distinction that matters: *internal capabilities* (trained, "fluid and dynamic" traits of the person)
versus *combined capabilities* ("internal capabilities plus the social/political/economic conditions"). "A society
might do quite well at producing internal capabilities but might cut off the avenues through which people actually
have the opportunity" to function. A just order "must secure to all citizens at least a threshold level of these ten
Central Capabilities." Following Wolff and De-Shalit, a "fertile functioning ... tends to promote other related
capabilities"; "corrosive disadvantage" is its flip side.
- *Bearing:* **for** and **narrows**. For: literacy is on the list, and the duty to secure the threshold falls on
  whoever orders social conditions. Narrows sharply: scaffolding builds *internal* capability; a person who has
  learned the system's ways but has no avenue to act on it (no contest, no exit, no voice) lacks the *combined*
  capability. So wrong (c) cannot stand alone — it needs wrong (a)/(b)'s point about the avenues, and the paper
  should say scaffolding without an avenue to act is Nussbaum's case of a society that trains people and then
  cuts them off.

**Robeyns and Byskov, "The Capability Approach" (SEP), `robeyns2025capability`. Part** (§2.3, held from facet M4).
A *conversion factor* is "the degree in which a person can transform a resource into a functioning"; personal
conversion factors include "reading skills"; social and environmental factors include "public policies" and "the
means of transportation and communication"; Sen's "capability" refers "to an opportunity made feasible, and
constrained by, both internal (personal) and external (social and environmental) conversion factors" (§2.3).
- *Bearing:* **for**, as the paper's cleanest analytic frame. A disclosure is a resource. Its value to a person
  depends on a personal conversion factor (the competence to use it — what scaffolding builds) and on environmental
  factors (the design of the record and the system — what the deploying firm controls). A regime of disclosure that
  attends to neither has not given anyone a capability. This frame joins wrongs (a), (b) and (c) without the
  paper's needing to claim that disclosure is worthless.

**Sen (1999), *Development as Freedom*, `sen1999development`. Record** (Knopf; not opened). Cite through Robeyns
and Byskov until a copy is read.

### Q5. The case against wrong (c)

Search additions: Consensus (two queries: AI/algorithmic-literacy interventions; platform duty to scaffold);
OpenAlex for Fernandes et al. (2014), Kaiser et al., Willis (2008); NBER w27057 PDF (`V5/kaiser2020nber.pdf`, read
printed pp. 1–4, 15–17, 21–22; printed page = PDF page − 1); Fernandes et al. June 2013 working paper (sister arm's local copy, `dxd_foundation_local/
pdfs/L/fernandes2013wp.pdf`, re-paginated this session); Puppart et al. (arXiv 2503.10556, `V5/puppart2025.pdf`,
read pp. 1–9). Penn Law's repository (Willis) returned 403; ScienceDirect (Leichtmann) returned 403; Scholar
Gateway returned "Access denied".

**Fernandes, Lynch and Netemeyer (2014), `fernandes2014financial`. Part** (working paper of 2 June 2013, pp. 2, 14,
22; published abstract via OpenAlex). The published meta-analysis covers "168 papers covering 201 prior studies"
(the 2013 working paper: 155 papers, 188 studies, p. 2). "interventions to improve financial literacy explain only
0.1% of the variance in financial behaviors studied, with weaker effects in low-income samples" (published
abstract); "at delays of 20 months or greater, there is no significant effect of even 24 hours of instruction"
(WP p. 14). Their alternative is not "design instead": defaults "work best when almost all consumers have similar
needs. When consumers' needs are heterogeneous, one needs to know something to decide for oneself. Here,
'just-in-time' financial education may have promise, alone and embedded in decision support systems" (WP p. 22).
- *Bearing:* **against** wrong (c) as decontextualised training ("teach people algorithmacy" in a course), and
  **for** a narrower wrong (c): support delivered at the moment of decision, inside the system — which is what
  scaffolding in Belland's sense is (support given "while students engage with problems", p. 18).

**Kaiser, Lusardi, Menkhoff and Urban (2020/2022), `kaiser2022financial`. Part** (NBER w27057, 2020; published
*J. Financial Economics* 145(2), 2022, 255–272, DOI 10.1016/j.jfineco.2021.09.022, not read). 76 randomised
experiments, more than 160,000 people. The weighted effect is "at least three times as large as the weighted
average effect documented in Fernandes et al. (2014), which examined 13 Randomized Controlled Trials" (p. 3); with
heterogeneous true effects, about 0.10 SD, "approximately 5.5 times larger" (pp. 16–17); "one of the main findings
of Fernandes et al. (2014) is not confirmed in this larger sample of RCTs" (p. 16); effects similar to
behaviour-change interventions in health and energy (p. 17). They "do not find strong evidence to support a rapid
decay ... though we do not find support for the sustainability of long-run effects either" (p. 3); no difference
for low-income people (p. 3).
- *Bearing:* **narrows the strongest objection.** The 0.1% figure, which the brief calls "very relevant", has been
  re-estimated on a larger RCT base: education has a real, small effect (about a tenth of a standard deviation),
  comparable to other behaviour-change interventions. The paper should not cite Fernandes's 0.1% without Kaiser
  et al.'s correction. Neither study concerns algorithmic systems.

**Willis (2008), "Against Financial-Literacy Education", `willis2008against`. Abstract** (Penn Law repository record
via OpenAlex; full text 403; *Iowa Law Review* 94, 197). Financial-literacy education is "a necessary corollary to
the disclosure model of regulation"; the belief in it "lacks empirical support" and is "implausible, given the
velocity of change in the financial marketplace ... and the disparity between educators and financial services
firms in resources"; "For some consumers, financial education appears to increase confidence without improving
ability"; "the regulation through education model blames them for their plight, shaming them and deflecting calls
for effective market regulation"; consumers "generally do not serve as their own doctors and lawyers."
- *Bearing:* **against** — the strongest form of the objection. "Scaffold the user" is the education half of the
  disclosure model, not its alternative, and it carries the same responsibilization as wrong (a). Willis's
  conditions — a fast-changing product, a resource gap between educator and firm — fit adaptive AI systems better
  than they fit mortgages. Her remedy is regulation, not competence.

**Puppart et al. (2025), `puppart2025brief`. Part** (arXiv 2503.10556, preprint, pp. 1–9). Randomised; high-school
students; ChatGPT advice wrong on half of eight puzzles. Over-reliance in "52.1% (SD = 28.90) of trials with
incorrect recommendations" (p. 8); the text-based literacy intervention "did not significantly reduce over-reliance"
and raised under-reliance (abstract; p. 8). Sample n = 36 (Figure 2, p. 9) — very small; preprint.
- *Bearing:* **against** brief, text-based AI literacy (which is a disclosure about the system, not a scaffold).

**Leichtmann et al. (2023), `leichtmann2023effects`. Abstract** (CHB 139, 107539; ScienceDirect 403). N = 410
online, 2×2: in-task XAI explanations improved performance and trust calibration; "the educational intervention,
domain-specific (i.e., mushroom) knowledge, and AI knowledge had no effect on performance."
- *Bearing:* **against** up-front training, **for** support inside the task — the same split as Fernandes's
  just-in-time point and Belland's definition.

**Chiang and Yin (2022), `chiang2022exploring`. Abstract** (IUI '22, pp. 148–161). Randomised; an interactive,
model-specific tutorial reduced over-reliance only for people already able to do the task; "low-performing
individuals' reliance on the ML model is not affected by the presence or the type of user tutorial."
- *Bearing:* **narrows** — scaffolding as delivered helped those who least needed it; a Matthew effect the paper
  must name.

**Lin (2025), `lin2025vernacular`. Abstract** (Asian J. Communication 36(3), 255–274). 316 official Douyin
"algorithm explanation" videos and articles plus 22 diary-interviews: the platform's transparency discourse
"selectively presents algorithmic information and shifts responsibility to automated systems, content creators, and
state regulation" and "legitimises the platform control through a carefully crafted illusion of transparency."
- *Bearing:* **against** trusting the operator to scaffold — the operator's own "literacy" materials served the
  operator (Brandt's sponsor, in the present).

**Ramesh, Kameswaran, Wang and Sambasivan (2022), `ramesh2022platform`. Abstract** (FAccT '22, pp. 1917–1928).
29 financially stressed users of Indian instant-loan apps "assumed responsibility for their negative experiences,
thus releasing the high-powered loan platforms from accountability obligations"; the authors call for interventions
"that enhance agency of users" and caution against "a purely technical approach."
- *Bearing:* **for** wrong (a) and a **warning** for (c): responsibility migrates to the user even without anyone
  asking it to; a scaffolding programme would have to work against that drift, not with it.

**Paternalism.** I found no source that argues capacity-building is paternalistic in the way nudging is; Hertwig and
Grüne-Yanoff hold the reverse — boosts need the person's cooperation and are "more respectful of autonomy" (p. 982,
sister card). The paternalism risk in the record is different: the sponsor chooses the content (Cuba's primer;
MOBRAL's themes; More's no-writing rule) and treats the learner as empty (Freire's "banking", 1970, p. 72; Bucher's
users already have an imaginary). Kamperman and Graff (2026, card) add that the literacy myth makes failure "the
fault of the individual" (p. 36). Note that Kamperman and Graff is a critique, not evidence that programmes fail.

**Prior work that already frames explanation as scaffolding (novelty check).** Lund et al. (2026), "Explainable
artificial intelligence as AI literacy scaffolding", *J. Documentation*, pp. 1–14, DOI 10.1108/jd-02-2026-0088,
`lund2026explainable`, **Abstract**: proposes "contingent support calibrated to the learner's Zone of Proximal
Development, progressive fading of explanatory support as competence grows, and the reframing of explanations as
entry points for inquiry rather than disclosure endpoints." Rohlfing et al. (2021), *IEEE TCDS* 13(3), 717–728,
`rohlfing2021explanation`, **Abstract**: explanation as a co-constructed social practice whose framework "relies on
the key concepts of monitoring and scaffolding". Oeldorf-Hirsch and Neubaum (held in this arm, M2/N3) set
"balancing users' expectations of algorithmic literacy with developers' responsibility" as a research direction.
- *Bearing:* **narrows** the novelty of wrong (c): the move "explanations should scaffold, not just disclose" is
  in print (Lund et al. 2026, two months before the post). What I did not find is the historical argument — that
  the oral-to-literate transition shows who scaffolded and whom it served.

### A note on Nadella's own word

The sister arm's facet G (`dxd_foundation/literature/facets/G_nadella_lineage.md`, read in full there) records that
Nadella's December 2025 post wants AI to be "a scaffolding for human potential vs a substitute", calls it "a product
design question we need to debate", and uses "scaffolds" for orchestration of models and agents. So the word is his.
The paper must say "the insider post (P1–P21) offers no scaffold", not "Nadella ignores scaffolding"; and it can
note that his "scaffolding" there means a system that supports people, which by Belland's test (support that
"continues indefinitely" is not scaffolding, p. 18) is a calculator, not a scaffold.

## Sorted for, narrows, against (wrong (c): "not scaffolding the person's growth to algorithmacy")

**For.**
1. Learning science draws the line the thesis needs: telling, a job aid and permanent support are not scaffolding;
   scaffolding is contingent support toward later independent performance (Belland 2017, pp. 5–6, 18–21; Collins,
   Brown and Newman 1987, pp. 2–3, 7). A disclosure or readable record is "telling".
2. Cognitive apprenticeship was invented for teaching reading, because the expert's process is invisible and must
   be externalised (Collins et al. 1987, pp. 2, 4). The operator is the only party who can externalise an
   adaptive system's process (Vygotsky's "more capable peer", ch. 6).
3. Measured systems that scaffold through a two-way loop work: Explanatory Debugging raised mental-model scores 52%
   (Kulesza et al. 2015, pp. 10–11); seams let users form and plan from theories (Eslami et al. 2016, abstract);
   computer-based scaffolding averages g = 0.46 (Belland 2017, p. 27).
4. History shows scaffolding of adults at scale was possible and was a sponsor's choice: Cuba 1961, 268,420
   tutors, 1:2–3 in learners' homes, 707,212 declared literate (Bhola 1984, pp. 92, 97–98, 100).
5. The capability approach makes a disclosure a resource whose value depends on personal and environmental
   conversion factors (SEP §2.3); literacy is on Nussbaum's list (2011).
6. In one comparison, in-task explanations improved performance where an up-front educational intervention did not
   (Leichtmann et al. 2023, abstract); Fernandes et al. recommend just-in-time support where needs differ (WP p. 22).

**Narrows.**
1. "Fading" is Collins et al.'s word (1989), not Wood, Bruner and Ross's (Belland 2017, p. 21); the 1976 original
   was not read.
2. By the scaffolding definition, permanent design aids (including the sister arm's re-representation) are
   calculators, not scaffolds; the paper must choose which remedy it means or name both.
3. Every funded scaffold in the record served its sponsor: Cuba's primer ("Fidel is Our Leader", Bhola p. 100),
   MOBRAL's Freire-without-Freire (p. 130), More's no-writing rule (Roberts 1835, p. 72), Sweden's compulsion
   (Johansson 1985, p. 64). Brandt (1998, p. 166) names the pattern. An operator that scaffolds its users is a
   sponsor.
4. The strongest historical scaffolds were self-organised (Alvord 1866 in Fleming 1905, p. 145; Williams 2005;
   Washington 1901, pp. 29–30) — which points to the person's own collective action as well as to the holder's
   duty.
5. Internal capability without an avenue to act is not a capability (Nussbaum 2011): (c) needs (a) and (b).
6. Users already act through folk theories and imaginaries (Bucher 2017; DeVito et al. 2017); they are not blank.
7. Interactive tutorials helped only people already competent (Chiang and Yin 2022).
8. "Explanations as scaffolds, not disclosure endpoints" is already in print (Lund et al. 2026; Rohlfing et al.
   2021).
9. Nadella has used "scaffolding" himself (sister facet G).

**Against.**
1. Financial-literacy education explained 0.1% of variance in behaviour and decayed to nothing by 20 months
   (Fernandes et al. 2014) — but see Kaiser et al. (2020/2022): on 76 RCTs, a real effect of about 0.10 SD, the 0.1%
   "not confirmed".
2. Willis (2008): education is the disclosure model's corollary, raises confidence without ability, and blames the
   person; with fast-changing products and a resource gap, competence-building is implausible and regulation is the
   remedy. This is the strongest objection to wrong (c), and it applies with more force to adaptive AI.
3. Brief AI-literacy interventions did not reduce over-reliance (Puppart et al. 2025, n = 36) and education did not
   improve performance (Leichtmann et al. 2023).
4. Operator-led "algorithm literacy" served the operator (Lin 2025, Douyin).
5. Responsibility drifts to users without anyone pushing it (Ramesh et al. 2022); a scaffolding duty could
   accelerate that drift.

## What the paper can say (notes for the drafter, with sources)

1. In learning science, scaffolding is support that lets a person do now what they cannot yet do alone and that is
   withdrawn as they become able to do it; telling a person what to do, a job aid, and support that never ends do
   not count (Belland 2017, pp. 5–6, 18–21).
2. By that definition, a disclosure, a readable record and an emergency brake held by the deployer are not
   scaffolds, and the insider post offers nothing that would count as one (post P9, P15, P19–P20; Belland 2017).
3. Collins, Brown and Newman designed cognitive apprenticeship to teach reading and writing because expert reading
   is an invisible process that a teacher must externalise (1987, pp. 2–4); an adaptive system's process is
   invisible to everyone but its operator.
4. Where systems have been built to explain themselves and take correction back, novices' understanding rose
   measurably — by 52% on a mental-model test in one lab study (Kulesza et al. 2015, pp. 10–11) — though in a setting
   where the system served the user alone.
5. Cuba's 1961 campaign shows that a sponsor can scaffold adults at scale — 268,420 tutors working with two or
   three learners each in their homes, 707,212 people declared literate at a first-grade level — and that the
   sponsor wrote its own politics into the primer (Bhola 1984, pp. 92, 97–98, 100).
6. The most striking scaffolds of the American transition were the freedpeople's own "native schools", which a
   Freedmen's Bureau inspector found already running in 1866 and which communities paid for themselves (Alvord in
   Fleming 1905, p. 145; Washington 1901, pp. 29–30; Margo 2005, p. 590).
7. Literacy's sponsors have scaffolded in their own interest: Hannah More taught reading and "allow[ed] of no
   writing for the poor" (Roberts 1835, p. 72), and Brandt names sponsors as agents who teach or withhold literacy
   "and gain advantage by it" (1998, p. 166).
8. On the capability approach, a disclosure is a resource whose worth depends on the person's competence and on
   the design of the environment (Robeyns and Byskov, SEP §2.3), and training that leaves people no avenue to act
   does not give them a capability (Nussbaum 2011).
9. The evidence on teaching people to cope with complex products is contested: one meta-analysis found financial
   education explained 0.1% of variance in behaviour (Fernandes et al. 2014), and a later one on 76 randomised trials
   found a small but real effect (Kaiser et al. 2022).
10. Willis (2008) argues that education is the disclosure model's companion and shifts blame to the consumer; the
    paper must answer her by specifying in-task, operator-provided support that fades, not courses — and by
    pairing it with the avenues to act (Fernandes et al. 2014 WP p. 22; Leichtmann et al. 2023).

## Gap statement

I found no work that uses the history of the oral-to-literate transition (Cuba 1961, freedpeople's schools,
Sunday schools, the Swedish church) to argue that firms deploying adaptive AI owe users scaffolding toward
competence, in Consensus (two queries), OpenAlex title searches, the arm's facets (C, F, M2, M4, M5, N3, Z) and the
sister arm's facets (G, I, L, M). The closest works argue the design move without the history (Lund et al. 2026;
Rohlfing et al. 2021) or the history without the design move (Kamperman and Graff 2026; Brandt 1998). This is a
search of those sources only; Scholar Gateway was unavailable.

## Read-depth tally

| Depth | Works |
| --- | --- |
| Full | Kulesza et al. 2015 (accepted MS); Hertwig and Grüne-Yanoff 2017 (sister card); Johansson 1985, Brandt 1998, Margo 2005, Kamperman and Graff 2026, Washington 1901 (arm cards, as carded) |
| Part | Belland 2017; Collins, Brown and Newman 1987; Bhola 1984; Boughton and Durnan 2014; Alvord 1866 (Fleming reprint); Fernandes et al. 2014 (WP); Kaiser et al. 2020; Puppart et al. 2025; Robeyns and Byskov (SEP); Freire 1970 (facet F) |
| Snippet | Vygotsky 1978; Williams 2005; Freire and Macedo 1987; Nussbaum 2011 |
| Abstract | Eslami et al. 2015, 2016; DeVito et al. 2017; Bucher 2017; Chalmers 2003; Willis 2008; Leichtmann et al. 2023; Chiang and Yin 2022; Lin 2025; Ramesh et al. 2022; Lund et al. 2026; Rohlfing et al. 2021 |
| Secondary | Wood, Bruner and Ross 1976 (definition via ERIC documents and Belland) |
| Record | Sen 1999; Collins, Brown and Newman 1989 chapter; Lorenzetto and Neys 1965; Laqueur 1976 |

**For the author to supply:** Wood, Bruner and Ross (1976) PDF (p. 90 definition; the page listing the six functions); Vygotsky
(1978) ch. 6 printed page for the ZPD definition (commonly p. 86); Sen (1999) on literacy; Willis (2008) full text;
Lorenzetto and Neys (1965) UNESCO report.

## Cards written (all `verified: pending`)

`belland2017instructional` (partial-text), `collins1987cognitive` (partial-text), `vygotsky1978mind` (partial-text,
snippets), `kulesza2015principles` (full-text, accepted MS), `bhola1984campaigning` (partial-text),
`alvord1866report` (partial-text, Fleming reprint), `fernandes2014financial` (partial-text, WP), `kaiser2022financial`
(partial-text, NBER WP), `willis2008against` (abstract), `nussbaum2011creating` (partial-text, snippets),
`lund2026explainable` (abstract). Existing cards cited, not rewritten: `johansson1985popular`, `brandt1998sponsors`,
`washington1901up`, `margo2005williams`, `kamperman2026ai`; sister-arm card `hertwig2017nudging`.
