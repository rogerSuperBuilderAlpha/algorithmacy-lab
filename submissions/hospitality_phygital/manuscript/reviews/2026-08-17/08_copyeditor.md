# 08 — Copyeditor · Intellect Harvard

Reviewer 08. Mechanics only. Line numbers refer to `manuscript/DRAFT.md` as it stands on 2026-08-17.

## 1. Who I am

I copyedit for Intellect journals and I read reference lists before I read arguments, because a list
tells me in thirty seconds how much of the rest I will have to check. I came to this one expecting
the usual: an APA-shaped bibliography wearing a Harvard costume, a dozen citations that resolve
nowhere, and a scattering of American spellings. Two of those three expectations were wrong. The
citation apparatus is, by the standards of what crosses my desk, unusually well disciplined: every
one of the 123 distinct in-text citations resolves to an entry, the author-count conventions ("et
al." versus "X and Y") are correct in every single instance, the Oxford comma holds across 48 lists
without one lapse, and there is not a single false '-ise'. What is wrong is wrong at the level of
house style rather than accuracy, which means it is wholly fixable — but it is wrong in 120 entries
at once.

## 2. The read — findings ranked by damage

Except where noted, these fixes cost **zero body words**. Two of them add words that are not body
words (mandatory apparatus), and one of them *frees* words.

---

### [FIX] F1. The reference list is in Title Case; Intellect Harvard is sentence case. 120 of 124 entries.

The Notes for Contributors give two worked examples, and both are sentence case:

> Cheng, Mingming and Foley, Carmel (2019), 'Algorithmic management: The case of Airbnb',
> *International Journal of Hospitality Management*, 83, pp. 33–36.

The draft has that same entry (L557) as `'Algorithmic Management: The Case of Airbnb'`. Every article
and book title in the list is capitalized this way. This is the single largest mechanical defect in
the manuscript, and it is a hundred-per-cent hit rate on a rule the Notes demonstrate rather than
merely state.

**Correction.** Down-case all article, chapter and book titles to sentence case: initial capital,
capital after a colon, proper nouns and acronyms retained. Journal titles stay in title case and stay
italic — those are correct as they stand. Worked examples of the transformation:

- L511 → `'Seeing without knowing: Limitations of the transparency ideal and its application to algorithmic accountability'`
- L525 → `'What does phygital really mean? A conceptual introduction to the phygital customer experience (PH-CX) framework'`
- L601 → `'Strategic responses to algorithmic recommendations: Evidence from hotel pricing'`
- L707 → `'Artificial intelligence and management: The automation-augmentation paradox'`
- L519 → `*Experiential marketing: Consumer behavior, customer experience and the 7Es*` (keep 'behavior' — it is the published title)
- L631 → `'Blame the robot: Role responsibility and ethical issues regarding AI-based care robots'`

Note the interaction with the language rule: **do not** anglicize spellings inside titles. 'Behavior'
(L519, L535, L625), 'Judgment' (L535), 'Modeling' (L669), 'Labor' (L677, L753), 'Travelers' (L655),
'Centered' (L617, L693) and 'toward' (L527, L617, L729) are all correct as printed, because they are
what the source says. I flag them here only so a global find-and-replace does not eat them.

---

### [FIX] F2. The all-in word count is over the ceiling, and the reference list is why.

The Notes rule the article at 6,000–9,000 words **including notes, references, contributor biography,
keywords and abstract**. My counts:

| component | words |
|---|---|
| Body §1–§9 (incl. headings and both tables) | 5,883 |
| References, 124 entries | 3,449 |
| Abstract (not yet in file, budgeted) | 180 |
| Keywords, six (not yet in file) | 12 |
| Contributor biographies, two (not in file) | 200 |
| AI acknowledgment (not in file) | 50 |
| **Total** | **≈9,774** |

That is roughly **770 words over the ceiling**, and `JOURNAL_SPEC.md` anticipated it: it budgeted ~60
entries at ~1,620 words. There are 124 entries at 3,449.

I raise this as a copyeditor, not as an editor: the panel brief describes ~400 words of headroom to
spend in the body, and under the Notes' inclusive count that headroom does not exist. It can be
created — but only in the list. Cutting ~28 references recovers ~780 words and puts the manuscript
under 9,000 with room. **This is a decision for the author and the editor-reviewer, not for me**; I
am reporting the arithmetic so the decision is made with the right number in front of it. If the
brief's 400 body words are spent without touching the list, the submission goes in at ~10,170 all-in.

---

### [FIX] F3. Three direct quotations, no page locators, and double quote marks.

The Notes require single quote marks and the `(Bordwell 1989: 9)` form. There are exactly three
quotations in the body and all three are wrong on both counts. The colon-page form is never exercised
anywhere in the manuscript — I searched; there are zero page locators in 156 citation instances.

- **L38.** `describes "guests without hosts": platform hospitality in which algorithmic governance
  renders the human host visible, disciplined, and ultimately dispensable (Germann Molz 2026).`
  → `describes 'guests without hosts': platform hospitality in which algorithmic governance renders
  the human host visible, disciplined, and ultimately dispensable (Germann Molz 2026: 00).`
- **L363–364.** `creating "a continuum in terms of customer value from physical to digital settings
  and vice versa" (Batat and Hammedi 2023)`
  → `creating 'a continuum in terms of customer value from physical to digital settings and vice
  versa' (Batat and Hammedi 2023: 00)`
- **L365–366.** `aims at "fluidifying" the guest's journey between online and offline (Batat 2024)`
  → `aims at 'fluidifying' the guest's journey between online and offline (Batat 2024: 00)`

Fill `00` with the actual page. All three quotations are well under 40 words, so run-in with single
quotes is correct; no display block is needed.

---

### [FIX] F4. Mandatory components absent from the file.

Seven required items are not present. Six of them are not body words and so do not compete with the
brief's headroom.

1. **Keywords — six, one or two words each.** None in the file. Draft supplied in §4 below.
2. **Abstract, 100–200 words.** None in the file.
3. **Statement of Contribution, 100–150 words**, answering the two prescribed questions, anonymized.
4. **Highlights**, three to five bullets, ≤85 characters including spaces, in a separate file with
   'Highlights' in the filename.
5. **AI acknowledgment**, its own headed section at the end of the article, **before** the References
   — the draft ends at §9 and goes straight to `## References`. Draft supplied in §4.
6. **Contributor biographies**, 50–100 words each.
7. **ORCID** for each contributor.

---

### [FIX] F5. Anonymity: two lines of front matter must be deleted before submission.

- **L3.** `For the *Hospitality & Society* special issue on phygital hospitality.` Names the venue and
  the special issue. The brief rules this out and the Notes accord strict anonymity to contributors.
- **L5–8.** The italic process note beginning `*Pierre's rewrite of 2026-08-11...*` **names an
  author**. It also names a working file (`BUILDOUT.md`). This is the fastest way to lose double-anonymized
  review that exists in this document, and it sits above the title of the paper.

Delete both blocks. The file should open on the title.

I note separately, as a matter for reviewer 01/07 rather than for me, that **L35** reads
`*Hospitality & Society* has already raised the question...`. Citing the target journal by name in
the body is not an anonymity breach — the works cited are published — but it does signal the venue,
and a cautious editor may prefer 'the hospitality literature has already raised'. **[CONSIDER]**

---

### [FIX] F6. Nested quotation marks: 14 entries use single-inside-single; the Notes require double inside single.

Every affected entry, with the inner marks to be changed from `‘ ’` to `" "`:

L517 Are; L521 Batat ('Le Petit Chef'); L579 DeVito; L585 Edwards and Veale; L589 Eslami ('Like');
L595 Folger ('Voice'); L603 Germann Molz ('Belong Anywhere'); L621 Introna; L633 Larivière ('Service
Encounter 2.0'); L639 Lee and Lu ('AI Consciousness'); L685 Padigar ('Good' and 'Bad' — two pairs);
L733 Vaccaro; L737 Weaver ('Fast Hospitality', 'Liquid', 'Solid' — three pairs); L743 Yeung
('Hypernudge').

Example, L743:
`Yeung, Karen (2017), '"Hypernudge": Big data as a mode of regulation by design', *Information, Communication & Society*, 20:1, pp. 118–136.`

While there: the list mixes straight `'` (as title delimiters, 254 of them) with curly `‘ ’` (the 17
nested pairs). Set the whole file to curly typographic quotes on export to Word, or leave the whole
file straight and let Word's autocorrect do it — but do not ship the mixture.

---

### [FIX] F7. Dash and hyphen defects in the reference list. Six instances.

Three are conversion artifacts and will be visible to a reader:

- **L575.** `*Journal of Marketing Management*, 40:5--6` → `40:5–6` (LaTeX double hyphen)
- **L647.** `Distinct Algorithmic Functions –- Evidence from the Meituan Platform` → `functions — evidence from`
  (en dash + stray hyphen; note this title also takes the F1 down-casing)
- **L715.** `Service Agents in Hospitality Settings –- Insights from a Field Study` → `settings — insights from a field study`

Three are hyphens where the rest of the list uses en dashes for ranges:

- **L535.** `31:1-2` → `31:1–2`
- **L547.** `5:2-3` → `5:2–3`
- **L699.** `44:13-14` → `44:13–14`

Page extents are already correct: 97 en dashes, no hyphenated page ranges anywhere.

---

### [FIX] F8. 'pp.' before a single number. Twelve entries.

Each of these is an article number, not a page extent, so 'pp.' is wrong in all twelve. Pick one house
treatment and apply it to all: either bare (`6:9, 236`) or `p.` (`6:9, p. 236`). I would use the bare
article number, which is what Intellect journals tend to print.

L515 Andreev `pp. 236` · L521 Batat `pp. 121013` · L611 Hatherley `pp. 20` · L629 Kim `pp. 102795` ·
L631 Kropf `pp. 30` · L639 Lee and Lu `pp. 103928` · L643 Li `pp. 102930` · L647 Lin `pp. 569` ·
L651 Liu `pp. 104640` · L667 Moganadas `pp. 213` · L687 Pan `pp. 104994` · L755 Zientara `pp. 103355`

---

### [FIX] F9. One reference entry is never cited. The list must contain only works cited.

**L533, Belanche, Casaló, Flavián and Schepers (2020),** 'Robots or Frontline Employees?...' appears
nowhere in the body. The Notes are explicit: the References list contains only works cited in text;
anything else goes to a separate 'Further Reading'.

Two options, and the author should choose deliberately: **delete it** (recovers ~30 words against F2),
or **cite it**. It is a natural companion to the responsibility-attribution point in §3 — if it
belongs, it belongs at L131–132 beside Sharma and Mattila.

The other direction is clean: **all 123 distinct in-text citations resolve**, and all 156 citation
instances parse. I checked author-count form on every one — no "et al." on a two-author source, no
"X and Y" on a three-author source, no bare surname where the entry has co-authors. Zero errors. That
is rare and it should be said.

---

### [FIX] F10. One entry is out of alphabetical order.

**L677, Möhlmann et al. (2021)** sits after `Mosca et al. (2025)` and before `Nguyen et al. (2024)`.
It has been sorted by character code rather than by letter, so 'ö' fell past 'z'. Move it to sit
between **Moganadas (L667)** and **Morosan (L669)**. The remaining 123 entries are in correct order,
including the `Vaccaro / van Doorn` pair, which is right as it stands.

---

### [FIX] F11. `(ed.)` should be `(eds)`. One instance.

**L635.** `in Lashley, Conrad and Morrison, Alison (ed.), *In Search of Hospitality...*` → `(eds)`.
Two editors, and Intellect sets it without the full stop.

---

### [CONSIDER] F12. Fourteen entries are incomplete: no page extent, and nine also have no volume.

These will read as unfinished to a production editor even though several are legitimately online-first.

*No volume, issue or pages:* L559 Choi and Chao · L573 De Vos et al. 2023 (conference paper — may be
correct as is) · L599 Gao and Thebault-Spieker · L613 Hemmer et al. · L617 Hirsbrunner et al. ·
L645 Lin 2025 · L721 Sharma and Mattila · L737 Weaver.

*Volume but no pages:* L587 Ehsan et al. `8:CSCW1` · L641 Li and Sun `38:4` · L661 Mameli et al. `28:1` ·
L749 Yurrita et al. `9:CSCW` · L753 Zhou et al. `63:2`.

*Missing place and publisher:* **L593, Fink, Melanie (2025), *Human Oversight under Article 14 of the
EU AI Act*.** — this is a title and nothing else. It needs `Place: Publisher` or, if it is a working
paper or report, the issuing body.

Where a source is genuinely online-first, Intellect accepts the entry without volume; where it now has
a volume, add it. Either way, make the eight *no-volume* entries look like a decision rather than an
omission.

---

### [CONSIDER] F13. Twelve multi-citation groups break the manuscript's own ordering convention.

Thirty of the 42 multi-work parentheses are chronological. These twelve are not, and reordering costs
nothing:

- L54 `(Lynch 2017; Beatty et al. 2016)` → `(Beatty et al. 2016; Lynch 2017)`
- L134 `(Kropf et al. 2026; Santoni de Sio and Mecacci 2021)` → reverse
- L143 `(Rahman 2021; Calo and Rosenblat 2017)` → reverse
- L180 `(Raisch and Krakowski 2021; Parasuraman et al. 2000)` → reverse
- L234 `(Garcia et al. 2026; Huang and Lo 2025; Kim et al. 2021)` → reverse
- L252 `(Eslami et al. 2016; DeVito et al. 2017; Ytre-Arne and Moe 2021; Jhaver et al. 2018)` → `(Eslami et al. 2016; DeVito et al. 2017; Jhaver et al. 2018; Ytre-Arne and Moe 2021)`
- L324 `(Yurrita et al. 2023; Lee et al. 2019)` → reverse
- L326 `(Fink 2025; Sterz et al. 2024; Li and Sun 2025)` → `(Sterz et al. 2024; Fink 2025; Li and Sun 2025)`
- L379 `(Lind et al. 1990; Goodwin and Ross 1992; Folger 1977)` → `(Folger 1977; Lind et al. 1990; Goodwin and Ross 1992)`
- L416 `(Mosca et al. 2025; Casalegno et al. 2020)` → reverse
- L426 `(Okhuysen and Bechky 2009; Bovens 2007)` → reverse
- L440 `(Christou et al. 2020; Parkinson et al. 2022; Pan et al. 2025)` — currently `Christou; Pan; Parkinson`

---

### [FIX] F14. Term inconsistency: 'design features' versus 'design principles'.

The §6 heading (**L303**) reads **Five design features**. The section body calls them **principles**
three times — L311 `The design principles developed here`, L313 `five design principles for more
hospitable phygital systems`, L341 `an important division between these principles` — and §8 (**L476**)
reverts to `the five design features`. A referee will notice, because this is one of the paper's three
named contributions.

Pick one and apply it in all five places. My recommendation is **principles**, since that is what the
argument-bearing sentences already use; then §6's heading becomes 'Five design principles' and L476
becomes 'the five design principles'. **Check against the abstract the editor has already seen** — if
that says 'features', invert the fix and change L311/L313/L341 instead. Zero net words either way.

Smaller sibling, same class: **L204** calls them `five practical questions`, Table 1 (**L208**) calls
them `Five diagnostic questions`, and **L245** calls them `The diagnostic questions`. Make L204 read
`five diagnostic questions at any phygital touchpoint`.

The other constructs hold perfectly and I checked each: augmentative/substitutive; common
understanding, predictability, accountability (identically ordered at L184, L191–192 and L424);
competence versus standing; the three competences; touchpoint (never 'touch point'); well-being
(never 'wellbeing').

---

### [FIX] F15. One American spelling. One.

**L63.** `one party holds obligations toward the other` → **towards**. The body uses 'towards' at L141,
L153, L296 and L427, so this is the odd one out rather than a policy choice.

Otherwise the language rule is met: 'centred' (L13, L487), 'centre' (L62), 'behaviour' (L142, L188),
'honour' (L338), 'judgement' (L420), 'modelled' (L243), and every '-ize' form correct —
'personalized/personalize/personalization', 'recognize', 'summarizes', 'emphasize', 'organization',
'industrializes'. **Zero false '-ise' endings** in the manuscript. I checked each of the fourteen
'-ise'-looking words and all are legitimate ('raised', 'praise', 'precise', 'revise', 'arise',
'exercising', 'improvised').

---

### [CONSIDER] F16. Pronoun for the generic guest wobbles once.

The paper commits to a singular female guest and holds it for six passages (L61, L92, L240–247, L338,
L387–389, L402–406). One sentence breaks it:

**L378.** `whether the guest ultimately gets what they want` → `whether the guest ultimately gets what
she wants`.

Related, and genuinely ambiguous rather than merely inconsistent: **L262–263**, `the employee is
effectively lending the guest their own capacity to specify the request` — 'their' can be read as the
guest's, which inverts the sentence. Suggest: `the employee is effectively lending the guest a
capacity that belongs to the employee.` (+2 words)

---

### [CONSIDER] F17. Two contributors are named differently across entries.

- **Lipnickas, Gintare** (L545 Brochado et al. 2026; L571 De Vos et al. 2026) versus
  **Lipnickas, Gintaras** (L573 De Vos et al. 2023; L575 De Vos et al. 2024).
- **Harris, Jane** (L545, L571) versus **Harris, Jennifer** (L575).

One of each pair is wrong, or the two are different people. Flagged under VERIFY.

## 3. Where it is strong — do not disturb these in revision

Named so that a hurried find-and-replace does not undo work that is already right:

1. **The citation-to-reference correspondence.** 123 distinct citations, 156 instances, zero
   unresolved, zero author-count errors, one uncited entry. This is the cleanest apparatus I have
   checked this year and it should not be re-generated from a bibliography tool.
2. **The '-ize' discipline.** Not one false '-ise'. Whatever produced it, keep it.
3. **The Oxford comma.** 48 lists, no misses.
4. **Citation register.** Parenthetical throughout, no narrative `Author (year)` forms at all, no
   ampersands in text, no comma between author and year anywhere, no 'no.', no 'vol.', no 'ibid.',
   no DOIs. Commas rather than full stops between reference parts, in all 124 entries. The 'in' rule
   is honoured — it appears once, correctly, on the only book chapter.
5. **Heading style.** All nine headings in sentence case and internally consistent.
6. **Page extents.** 97 en dashes and not one hyphenated range.

## 4. Best spend — the 150 words

The brief offers 150 of the spare 400. I would not put them in the body, for the reason in F2. I would
spend them on the two mandatory components that are missing, cost nothing against the body budget, and
would otherwise be written in a hurry on 3 September.

**Keywords (12 words, mandatory, six required, one or two words each):**

> phygital hospitality; algorithmic mediation; host obligation; accountability; contestability; guest agency

**AI acknowledgment section (~50 words, mandatory, placed after §9 and before the References, in the
journal's prescribed wording):**

> **Acknowledgment of the Use of Generative AI and AI-Assisted Technologies in the Writing Process**
>
> Throughout the preparation of this work, the author(s) employed [NAME OF TOOL / SERVICE] to
> [PURPOSE]. Following the utilization of this tool/service, the author(s) thoroughly reviewed and
> edited the content as necessary, assuming full responsibility for the publication's content.

I have deliberately left the two slots empty. The disclosure is the authors' own statement and it has
to be true; I will not draft a description of a process I did not observe.

**The remaining ~90 words** go to the Statement of Contribution (100–150 required) — but that is the
editor-reviewer's brief to draft, not mine.

## 5. Verdict

**Minor revisions**, on mechanics. Nothing here touches the argument; every finding is a find-and-fix,
and the apparatus underneath is in better order than the surface suggests.

**The single most important fix is F1**: 120 of 124 reference entries are in Title Case where Intellect
Harvard is sentence case. It is the largest single defect by count, it is visible on the first page a
production editor opens, and it is the one an author is most likely to leave until last and then run
out of time on. Do it first, by hand, and do not let a global lower-casing pass touch the journal
titles or the American spellings inside published titles.

**Counts by class:** title-case entries 120 · nested-quote entries 14 · incomplete entries 14 ·
misordered citation groups 12 · single-page 'pp.' 12 · dash/hyphen defects 6 · quotation-mark and
page-locator defects 3+3 · term inconsistencies 2 · name inconsistencies 2 · anonymity leaks 2 ·
pronoun defects 2 · uncited entries 1 · ordering errors 1 · `(ed.)` 1 · US spellings 1 · unresolved
citations 0 · false '-ise' 0.

## 6. VERIFY — checks I could not complete from the file

1. **The three quotation page numbers** (F3). I have no access to the sources; `00` must be replaced
   from Germann Molz (2026), Batat and Hammedi (2023) and Batat (2024).
2. **Shabnam et al. 2026 (L719)** gives `*Journal of Services Marketing*, 40:4, pp. 1–17`, and
   **Batat 2026 (L527)** gives the same journal, same `40:4`, at `pp. 505–518`. Two articles cannot
   both begin at page 1 in one issue. One of these is online-first pagination that has since been
   superseded. Check both.
3. **Brochado et al. 2026 (L545)** `pp. 1–20` and **De Vos et al. 2026 (L571)** `pp. 1–23`, both
   *Journal of Services Marketing* with no volume. If these have since been issued, add volume, issue
   and final pages; if not, the form is acceptable.
4. **Lipnickas, Gintare / Gintaras** and **Harris, Jane / Jennifer** (F17). Check the author lines on
   the four papers.
5. **Fink (2025), L593.** Establish what this is — monograph, chapter, working paper — and complete it.
6. **Casalegno et al. (2020), L551** and **Mosca and La Rosa (2019), L673**, both *Symphonya. Emerging
   Issues in Management*, both with page extents and no issue number. *Symphonya* numbers its issues;
   check whether the number should be there.
7. **The abstract**, which is not in this file, for the 'features' versus 'principles' decision in F14
   and for the 100–200 word rule.
8. **The 'six keywords' rule.** There are no keywords in the file at all, so I could only draft a set
   (§4), not check one.
