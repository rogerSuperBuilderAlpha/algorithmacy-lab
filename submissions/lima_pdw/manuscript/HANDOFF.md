# The 26 August rebuild — what changed, what it still needs

**Superseded 2026-08-29.** `PAPER.md` was rewritten in full that day from
[`OUTLINE.md`](OUTLINE.md)'s v3 architecture, built against a six-reviewer Fable panel
([`../reviews/fable_panel_2026-08-29_gdoc_merged/`](../reviews/fable_panel_2026-08-29_gdoc_merged/)).
Everything below is history: it describes the 26 August draft, which is itself archived at
[`../archive/2026-08-29_PAPER.md`](../archive/2026-08-29_PAPER.md) (the version current through the
morning of 29 August, with that day's citation-verification sweep applied) — read the repo
[`README.md`](../README.md) for the current status, not this file.

**Written 26 August 2026.** New draft: [`PAPER.md`](PAPER.md). The 19 August draft is
untouched at [`PAPER.md`](PAPER.md) and remains the fallback. Nothing has been committed.

Built from [`OUTLINE.md`](OUTLINE.md), which was built from
[`../reviews/REVIEW_2026-08-26.md`](../reviews/REVIEW_2026-08-26.md) and
[`../literature/RESEARCH_PACKAGE_2026-08-26.md`](../literature/RESEARCH_PACKAGE_2026-08-26.md).

## The lock held

The abstract and introduction in `PAPER.md` are **byte-identical** to `PAPER.md` and to
[`INTRODUCTION.md`](INTRODUCTION.md) — verified by hash, not by eye. So are the title block and the
first-page delta note.

One thing inside the lock's file did change, and it is not prose: `INTRODUCTION.md` carries its own
reference list, whose Zhou entry has no locator. `PAPER.md`'s list gives the article number,
**e70004**, confirmed against the journal version in `../literature/ZHOU_2025_INSTRUMENT.md`. If you
want the two files to agree, that entry is the only edit needed and it touches no locked sentence.

## Budget, moved

| section | v1 | v2 |
|---|---|---|
| Abstract + Introduction (locked) | 896 | 896 |
| Paper 1 of This Dissertation | 838 | 550 + **Table 1** |
| Extant Constructs | 1,975 | 2,218 |
| **Algorithmacy** | **534** | **1,248** |
| Early Empirical Work | 635 | 801 |
| What This Paper Cannot Say | 355 | 464 |
| whole paper with references | ~6,270 | **7,916** |

The construct section more than doubled, which was the point: v1 spent more words summarising Paper
1 than proposing the construct the paper exists to propose. The paper is ~1,650 words longer overall.
No length limit appears anywhere in the workshop materials, and the archived twelve-section draft ran
8,391.

## The three falsifiable sentences, fixed

1. **"The missing piece is a position, not a variable."** The position had been named in print four
   times — Katsh and Rifkin's fourth party (2001), Curchod and colleagues' triad in *ASQ* (2020,
   **which v1 already cited, for far less**), Cameron's algorithmic labor triangle (2024, uncited),
   Healy and Pekarek (2024). v2 names all four, grants that they theorise power, consent and
   vulnerability, and draws the line that survives: none writes a *competence* for the party the
   triangle traps. The claim is now bounded four ways, in the text.
2. **"None names another person."** Long and Magerko's competency 10 is titled *Human Role in AI*.
   v2 narrows to: it names humans as the system's makers, and no competency names another person as a
   party to an interaction the learner is conducting. The narrowed form is stronger — it checks in
   both directions.
3. **"Several responses."** See the open decision below.

## Other repairs carried

- **Paper 1's condition-mapping is no longer attributed to the classics.** v1 had "Hayek (1945)
  showed … accountability arrives through contract and reputation." Hayek says nothing of the kind,
  and that paper is the one every OS/OT reviewer has read. v2 makes Paper 1 the agent of the mapping
  throughout.
- **The open cell is bolted down.** "How a person takes her place" was never one of Paper 1's six
  graded questions. v2 folds it into the *mechanism* cell, which Paper 1 defines as the operation
  that secures the form together with the standing of the party it reaches — so the open cell is now
  one of the graded cells, visible as a half-empty cell in Table 1.
- **Spitzberg and Cupach.** v1 cited them for an ability residing in a party; their relational model
  was written to reject exactly that. v2 turns it into the argument: competence judged by both
  parties is the standard this arrangement cannot meet.
- **The site is described in the construct's own vocabulary.** v1 mapped peers to *intermediary*;
  peers are the counterpart and the gate is the intermediary. v2 also argues the hard case instead of
  asserting it — opacity is a property of the person–arrangement pair, and what the arrangement
  withholds even from its builders is the vote and the criteria behind it.
- **Methods moved to design tense.** `../interview/METHODS_AUDIT.md` records no codebook, coding
  rule, memo file or discard log, and v1 claimed abductive analysis and first-cycle coding in the
  present tense. Bowen (2006) now carries "sensitizing concepts," which v1 used without a cite.
- **Sutherland misquote** ("were apparent" → "were in fact valued", p. 463) and the **Guzman page**
  (p. 73 → p. 74). Both steelmans were corrected too, each with a dated note, so the errors cannot
  reinfect a later draft.
- **New:** Rahman promoted from boundary to evidence (he interviewed eighteen clients, and the
  platform told them their feedback would be "kept anonymous and never shared directly with the
  freelancer"); Zhou's appeal item, where the only contest in the rival scale routes to the machine;
  the field's own audits (50, 169 and 12 studies) turning "we read seven" into a documented negative
  result; Abidin's chiasmus; the Jarrahi and Sutherland lineage; the insider-research quartet;
  Table 1.
- **"What the Construct Buys" is a new subsection** — v1 never said what organization theory gets if
  algorithmacy is real, which left a workshop panel nothing to develop. It also cashes "satisficing,"
  a Simon term of art the locked abstract uses and v1 never mentioned again.

## Prose

The failure mode both reviews named was uniformity, not vocabulary. Measured on body prose, table
and comments excluded:

| | v1 body | v2 body | standard |
|---|---|---|---|
| first person /1k | 4.4 | 4.9 | band 4–8 |
| em-dash /1k | 4.4 | 4.9 | venue 2.93 |
| sentence CV | 0.59 | 0.68 | — |
| ", not" + "rather than" | 21 | 12 | — |
| paragraphs ending on a negation | 17 of 23 in the last three sections | 14 of 55 overall | — |
| "Adding items" | 4 | 1 | — |
| banned emphasis openers | 0 | 0 | 0 |
| performed-rigor sentences | 4 | 0 | 0 |

Two §3 hearing openers were rewritten to break a seven-for-seven template, and the four-beat "still
of the apparatus" anaphora now breaks on its fourth beat. The short punctures survive: *She is
enrolled. Nobody has both. The code they can read. A rating that can close an account does not.*

Citation resolution is clean in both directions across 55 entries.

---

# What still needs you

## 1. The response count collides with the locked abstract — decide before submission

The intake bucket holds **two** objects (the second uploaded 22 August, 05:01Z, and **not yet
read**). v2's empirical section states the number, because both reviews found "several" reads as
evasion in a paper whose credibility rests on saying exactly how little it has. The locked abstract
still says "several responses obtained to date."

`PAPER.md` carries a non-printing `<!-- LOCK CONFLICT -->` comment at that line. **The two
sentences have to move together.** Two ways out:

- **Unlock and correct both.** The abstract drops "several responses obtained to date."
- **Field, and let the sentence become true.** `../interview/EMAIL_TO_SEND.md` is copy-ready and two
  weeks remain. Sending is yours.

## 2. The IRB question — unchanged, and it still outranks the drafting

Protocol 260511078's exempt determination was made in May on a three-wave survey design. The paper
reports data from an LLM-mediated interview with different data and a different collection
mechanism. `../interview/CONSENT.md` tells participants that protocol covers them; `../PLAN.md` §2
says the qualitative protocol "is a separate application." Consent forms are already in
participants' hands. That is an IRB question, not a repo question.

## 3. Whether `correspondence/LIMA_ORGANIZERS.md` ever went

Drafted with a send-by of 29 July.

## 4. One citation in the draft has no source behind it

**Gittell (2002)**, for relational coordination, in the opening of Extant Constructs. It closes the
paper's cheapest relabelling attack — *"algorithmacy is relational coordination performed under
opacity"* — and **no Gittell card, and no relational-coordination card, exists anywhere in the
387-card library.** The reference list carries an `<!-- UNVERIFIED -->` comment. Acquire the source
or cut the clause; do not ship it as it stands.

## 5. Verify before print

- **Curchod and Rahman page anchors.** Both shelf copies are accepted manuscripts, not the version of
  record.
- **Table 1's market-instruments and recognition rows** compress clauses from v1's prose rather than
  from Paper 1 itself. Check them against Paper 1.
- **"Prices their work" was dropped** from the enrollment list, which is now match, rank, close — the
  locked introduction's own version. No Stark card in this library confirmed the pricing function.
- Katsh and Rifkin, Wing and colleagues, Healy and Pekarek, Abidin, Gagrčin, Jarrahi and Sutherland,
  and the whole insider-research quartet are **card-depth**: cited for their positions, never quoted.
  Depth table in [`CITATION_DEPTH.md`](CITATION_DEPTH.md).

## 6. The one thing no reviewer can supply

The empirical section reports what the first participant *did*. The paper's own claim is that
competence is a *conception* of the work. **What did she think the gate was doing?** The transcript
may already hold it. If it does, that sentence is worth more than any repair in this file, because it
is the only place where the construct and the data touch. The second response is also still unread —
`../interview/pull-responses.sh` syncs into a gitignored `responses/`, and the repo is public, so
nothing would be committed.

## Files now stale against v2

`../README.md`, `../PLAN.md`, `OUTLINE.md` and `LOCK.md` all point at `PAPER.md` as the live draft.
They stay correct until you decide v2 replaces v1; none was edited.

## Working files, deletable

`process/2026-08-26_sections_2_3.md`, `process/2026-08-26_sections_4_6.md` — the two halves before assembly. Kept only so the seam
can be inspected.

---

# Second round, 26 August — revised against the call for papers

The call is now transcribed at [`../CALL_FOR_PAPERS.md`](../CALL_FOR_PAPERS.md), with its three
date discrepancies against this arm's files. Four changes followed from it.

**The call settles the dataset question.** "Both theoretical and empirical papers are welcome,
provided they engage substantively with organizational scholarship." The incomplete study is not a
disqualification, so the draft now carries it as a specified design with its holes shown rather
than as an empirical section that reads as a shortfall.

1. **Trinidad is constitutive, not biographical.** The draft had reduced GauntleTT to one sentence
   whose only job was to deny it was the study site — against a call whose distinctive aim is
   emerging contexts "without reducing such contexts to mere empirical sites," and an accepted
   title that promised a Caribbean cohort. It is now a ~190-word argument: the platform-work
   literature forms its constructs at sites the arrangement has already sorted, where any
   difference between two workers arrives pre-explained by skill, task mix, or hours; GauntleTT
   held none of those explanations, so the unevenness had nowhere ordinary to hide. Closes
   [`../AGENDA.md`](../AGENDA.md) item 10, open since August.
2. **`# Early Empirical Work` is now `# The Study in Progress`**, in four subsections, ending in
   **What Remains to Be Collected** and **Table 2** — the four interview blocks against what is
   collected, what each still needs, and what would count as a case against the construct. Two
   blocks carry an incident; two are empty, and the table says so. That table is the placeholder.
3. **Journal fit**, stated once in What the Construct Buys: the form was named in *Organization
   Theory*, and the competence question is what that literature left open.
4. **`# A Research Agenda`**, four runnable studies each with a result that would count — an
   explicit objective of the workshop that the draft previously met only in scattered clauses.

Whole paper now **8,892 words**. Guards after: first person 4.6/1k, em-dash 4.6/1k, negation-ending
paragraphs 14 of 64, banned openers 0.

## Two things this round turned up

**A misstatement about consent, now corrected.** The draft had said consent was "held outside the
course by a third party who receives withdrawals, and the investigator does not learn who declined
until grades are final." No such mechanism exists. [`../interview/CONSENT.md`](../interview/CONSENT.md)
says intake is anonymous, that "no record exists of who was invited and who took part," that **"the
researcher will not know whether you participated,"** and that withdrawal after submission is
impossible because nothing links a file to a person. The true procedure is the stronger answer to
the non-free-consent objection, and the draft now states it, including the cost — a submitted
response cannot be withdrawn. **A misstatement about human-subjects procedure is worse than a
citation error, and this one had survived two review rounds.**

**An unresolved contradiction, flagged and not fixed.** The first-page note tells reviewers
"GauntleTT is where the construct was formed; it is not the study site." But
`../interview/protocols/STUDENT.md` opens: "For people who took part in a cohort: GauntleTT, Cursor
Boston, or the Hult cohort program" — and `protocols/SELF.md` exists specifically to record "how
the Trinidad gate ran." The instrument recruits from GauntleTT; the disclosure says GauntleTT is
not a study site. Both cannot be plainly true.

Two consequences, and the second is the serious one:

- **For reviewers:** the manuscript's own disclosure and its methods section disagree about where
  data comes from.
- **For the IRB:** [`../PLAN.md`](../PLAN.md) §2 records that protocol 260511078 covers the Hult
  sixteen-week cohort. If the student protocol is recruiting GauntleTT and Cursor Boston
  participants, that reaches a population the approved design may not cover. This compounds the
  approval question already open from the 19 August review, and it is the same question:
  what covers the qualitative interview study.

The first-page note is the author's disclosure and was left byte-identical. Resolving this is
yours — either the note widens to say the study reaches the cohorts the student protocol names, or
the protocol narrows. It should not go to reviewers as it stands.

---

# Third round, 26 August — the research round folded in

Gap register: [`../literature/GAPS.md`](../literature/GAPS.md). Round outputs:
`RELATIONAL_COORDINATION_`, `CONTEXT_AND_REGION_`, `FALSIFICATION_SWEEP_`, `VERIFICATION_2026-08-26.md`.

**Paper is now 9,637 words, 65 references.** Lock verified byte-identical after every pass. Guards:
first person 4.7/1k, em-dash 5.2/1k, sentence CV 0.66, negation-ending paragraphs 14 of 65, banned
openers 0, all four short punctures intact. Citation resolution clean in both directions.

## Added

- **The Trinidad argument now has its warrant.** Merton's strategic research site, Bamberger and
  Pratt (2010) on unconventional contexts, and Bothello, Nason and Schnyder in *Organization Studies*
  on what the reverse reading costs — a site read only through constructs formed elsewhere shows up
  as a void, and this cohort would have shown up as having nothing when what it held was the
  phenomenon unobstructed. That sentence answers the workshop's distinctive aim directly.
- **The regional absence is now a fact rather than a silence.** The ILO's 2025 Caribbean study, no
  peer-reviewed journal study of platform labour in Trinidad and Tobago, and Chigbu's two-of-103
  count for Latin America and the Caribbean. All three support the unsorted-site argument.
- **Manky (2026)**, at the close of Extant Constructs: forty Lima ride-hailing drivers who use the
  platform's own data to read the passenger — a counterpart-facing capacity with no construct written
  for it. Regional engagement that is earned by the argument rather than performed.
- **The three frontier near-misses, conceded in What This Paper Cannot Say**, together with the
  sweep's real finding: every counterpart-inclusive construct demotes the intermediary to a tool, a
  delegate, a channel, or a threat, so **the third scope condition carries the whole claim**. The
  paragraph concedes that none of the three has been read in full, and that the claim is stated for
  the coordination of work while medicine, social work and intimacy lie outside the tested terrain.

## Corrections applied this round

1. **Spitzberg's outcome criteria — an error this revision introduced.** Four became five
   (efficiency folds inside effectiveness; coorientation and relationship development were missing),
   and "the first and last" was picking out the wrong pair.
2. **Spitzberg and Cupach's level claim** re-anchored to what the 1984 book verifiably holds
   (molar and molecular). "Measurement at one level licenses no inference at another" is later
   Spitzberg.
3. **Laupichler**, one word: course efficacy is SNAIL's declared *use*, not its validation criterion.
4. **Four reference entries lacked author initials** — the inoculation citations, where incomplete
   entries would undercut the point. Resolved against Crossref and publisher records: Dredge, R., &
   Anderson, J. (2021), *Personal Relationships* 28(3), 627–651; Hu, J. M., & Zhan, E. (2024),
   *BIT* 43(16), 4045–4060; Yang, F., & Liechty, J. M. (2026), Springer. The JMIR preprint stays
   title-cited because its authors are genuinely unretrievable, and it says so.

## New, and author-only

**Definition drift across your own venues.** No independent prior academic use of "algorithmacy"
exists. The sweep found the Substack and **algorithmacy.org — the first global conference on
algorithmacy, Port of Spain, 28–31 October 2026** — whose public definition ("the competency through
which a worker coordinates with another human through an algorithmic third party") differs from the
manuscript's three-operation definition. Its submissions and reviews are **public**, and submissions
closed 1 August. So the construct is publicly attributed under a different definition, three weeks
after Lima, in the country this paper now argues is constitutive. A reviewer who searches the term
finds all of it. Reconcile the definitions or be ready to explain the revision. Related: the "names
are cheap and getting cheaper" line now sits beside a branded conference on the name — defensible,
since the paper's claim is about a position, but expect the question.

**"Algocracy."** Aneesh (*Virtual Migration*, 2006; *Sociological Theory* 27(4), 2009) distinguishes
bureaucracy, market and algocracy as ruling principles — nearly Paper 1's comparative frame, two
decades earlier, and a near-homophone. Neither Aneesh nor Danaher (2016) is a competence construct,
so the position claim is untouched, but the answer should be ready: Aneesh names the form's ruling
principle, algorithmacy names the party's competence.

**Have an answer for Hall, Gardner and Wright (2025)**, "AI, Relational Coordination, and
Performance" in *Production and Operations Management*. The title looks fatal and is not: the AI is a
shared advisory tool in a co-present three-person team, and it stimulated relational coordination
precisely because members could still answer one another.

## Still open, unchanged

The response count against the locked abstract; the IRB coverage question; whether the organizers'
letter went; the GauntleTT contradiction between the first-page note and `protocols/STUDENT.md`; the
second interview response, still unread; and the participant's conception of the gate.

**Reads worth buying before 10 September:** the JMIR preprint in full, Yang and Liechty in full, and
Curchod's version of record for internal pagination — the only verification item that needs a library.
