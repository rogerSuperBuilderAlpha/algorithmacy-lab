# 08 — Copyeditor · Intellect Harvard

Reviewer 08. Mechanics only. Line numbers refer to `manuscript/DRAFT.md` as it stands on 2026-09-03
(417 lines; body §1–§9 at lines 11–168; References at 170–416). Where I cite a publisher record I
checked it against the Crossref API this evening; where I could not, the item is under VERIFY.

## Step 0 — register note

The register is the second author's and I have left it alone. Every replacement below is punctuation,
a name, a number, a locator or a one-word substitution, and none is longer than what it replaces
except where a reference entry gains the fields the Notes require. No em-dashes are introduced into
the body; where a sentence needs a break that a dash would supply, I use a colon, which the body
already uses.

## What my predecessor caught, and what was applied

| 17 Aug catch | status on 3 Sep |
|---|---|
| F1 sentence-case titles (120 entries) | **applied**, three stragglers remain (below: L296, L208, L416) |
| F2 all-in overage | superseded by the body-only ruling |
| F3 double quotes on three quotations | **applied**; page locators **not applied** (L126, two quotations) |
| F4 abstract and keywords in file | **applied** in DRAFT.md; but see finding 2 on the second abstract |
| F5 anonymity, front-matter lines | **half applied**: the process note naming an author is gone; **line 3 still names the venue and the special issue** |
| F6 nested quotes double-inside-single (14 entries) | **applied**, all fourteen |
| F7 six dash defects | **applied**, all six |
| F8 'pp.' before article numbers (12) | **applied**, all twelve |
| F9 Belanche uncited | **applied**, now cited at L122 |
| F10 Möhlmann misfiled | **applied** |
| F11 (ed.) → (eds) | **applied** |
| F12 incomplete entries (14) | **not applied**; and Crossref now shows four of them carry wrong author names |
| F13 twelve non-chronological citation groups | **not applied** |
| F14 features/principles | **applied**; §7 says 'principles' throughout and Table 1 is now 'Six questions' everywhere |
| F15 'toward' | **applied** |
| F16 guest pronoun | **inverted rather than fixed**: the body now runs on 'they', with two surviving 'she's |
| F17 Lipnickas/Harris names | **applied** ('Gediminas', 'Joanne'), one residual 'Ged' |

## 1. Who I am

I copyedit for Intellect and I read the reference list first. This list is in far better shape than
the one I saw on 17 August: sentence case, the colon form, bare article numbers, en dashes, nested
quotes, alphabetical order. What is wrong tonight is smaller in count and larger in consequence.
Line 3 still tells the referee which journal and which special issue the paper is for. Four
reference entries name authors who did not write the paper. And the submission's front-matter file
carries a different title, a different abstract, different keywords and highlights that use two terms
the manuscript never uses, while the preflight script validates that stale file rather than the
abstract in DRAFT.md. Everything else is the ordinary evening's work.

## 2. The read — ranked by damage

Costs are body words unless stated. Reference-list fixes cost nothing against the 376.

---

### [FIX TONIGHT] 1. Line 3 names the venue and the special issue. Delete it.

**L3.** `For the *Hospitality & Society* special issue on phygital hospitality.`

Delete the line. The preflight check 'the venue is not named in the body' passes because line 3 is
above the abstract, not in the body; the referee's PDF will not make that distinction. It also
carries the only ampersand in running text. Cost: 0.

---

### [FIX TONIGHT] 2. Two abstracts, two titles, two keyword sets. The front-matter file is stale and the machine is checking the wrong one.

`submission/FRONT_MATTER.md` (dated 17 August) and `DRAFT.md` disagree on every front-matter
component, and `preflight.py` line 121 reads its abstract, keyword and highlight checks from
FRONT_MATTER.md, not from DRAFT.md.

| component | DRAFT.md | FRONT_MATTER.md |
|---|---|---|
| Title (L1 / FM L14) | *Who Hosts the Guest? Algorithmic Mediation, Standing, and Responsibility in Phygital Hospitality* | *Who Hosts the Guest? Reconfiguration of Hospitality in Phygital Spaces* |
| Abstract (L7 / FM L25–40) | 'Phygital hospitality promises a smoother welcome…' **202 words** by whitespace count (what Word will report) | 'Phygital hospitality scholarship presents…' 198 words |
| Keywords (L9 / FM L44–45) | phygital hospitality; algorithmic mediation; host-guest relationship; accountability; contestability; hospitality standing | phygital hospitality; algorithmic mediation; guest agency; employee discretion; well-being; contestability |
| Highlights (FM L76–80) | none in DRAFT.md | five bullets, two of which use **'hospitality algorithmacy'** and **'coordinative sovereignty'** |
| Statement of Contribution (FM L56–70) | none | refers to 'five design features', 'augmentative and substitutive', 'a triadic account' |
| AI acknowledgment | **absent** from DRAFT.md; the file ends at §9 and goes straight to References | FM L100 says it is 'drafted at the end of the manuscript' |

The words *algorithmacy*, *sovereignty*, *augmentative*, *triadic* and *design feature* occur zero
times in DRAFT.md (I counted). A highlight that names a construct the article does not contain will
be the first thing a referee notices, and it will read as a paper that was rewritten after its
apparatus was filed. Which document governs is the author's call; the brief says DRAFT.md is the
governing text, so:

- **Abstract.** Use DRAFT.md's, and trim it by two words so it is under 200 by any counter. Two
  one-word cuts that change nothing: L7 `But hospitality was never only about smooth service.` →
  `But hospitality was never only smooth service.`; and L7 `built on three things a guest needs (a
  shared understanding, predictability, and someone accountable)` → `built on three things a guest
  needs (shared understanding, predictability, and someone accountable)`. 200 words.
- **Keywords.** DRAFT.md's six. All are one or two words ('host-guest relationship' counts as two).
- **Highlights.** Rewrite bullets 1, 3 and 4 in the manuscript's own vocabulary. Drafts, with
  character counts:
  - `Algorithms can perform a host's functions without inheriting a host's obligation.` [82]
  - `Mediation replaces hospitality wherever no party must answer for what it decides.` [81]
  - `Competence is learned by guests and staff; standing is conferred by the institution.` [84]
  - Bullet 2 (`Algorithms now perform hosting functions and redistribute discretion and authority.`
    [83]) and bullet 5 (`A transformation roadmap that no property can discharge by procurement
    alone.` [77]) can stand, though 'transformation roadmap' is not the manuscript's phrase; L136
    says 'a roadmap of rising commitment'.
- **Statement of Contribution.** Replace 'five design features' with 'five design principles',
  'augmentative and substitutive mediation specified as a checkable condition' with 'a checkable
  test, six questions on three conditions, for telling mediation that helps from mediation that
  replaces', and 'a triadic account' with 'an account of the missing counterparty'. This is
  reviewer 07's brief to approve, but the vocabulary mismatch is mine to flag.
- **AI acknowledgment.** Add the headed section after L168 and before `## References`, in the
  Notes' wording, with the two slots filled by the authors. I will not draft a description of a
  process I did not observe.
- **Title.** Pick one. DRAFT.md's is the one the body was written under.

Cost: 0 body words. Everything here is apparatus.

---

### [FIX TONIGHT] 3. 'This journal' in the body signals the venue.

**L19.** `This journal has already asked what happens to hospitality when platforms push the human host out of view (Riordan 2024; Germann Molz 2026).`
→ `Hospitality scholars have already asked what happens to hospitality when platforms push the human host out of view (Riordan 2024; Germann Molz 2026).`

The 17 August version named *Hospitality & Society* here; it has been softened to 'This journal',
which with both citations resolving to H&S entries says the same thing. The brief bars the body from
stating 'the paper's own positioning'. Cost: 0 (five words for five).

---

### [FIX TONIGHT] 4. Four reference entries carry the wrong authors. Crossref-verified tonight.

These were on the 17 August incomplete list; the cards themselves flagged 'names to confirm at
proof'. Confirmed, and the names in the draft are wrong.

**L302.** `Li, Hui and Sun, Zhiyuan (2025), 'Is algorithmic accessibility sufficient? The pivotal role of accessibility and accountability in shaping trust in automated decision-making', *Governance*, 38:4.`
→ `Li, Huanhuan and Sun, Zongfeng (2025), 'Is algorithmic accessibility sufficient? The pivotal role of accessibility and accountability in shaping trust in automated decision-making', *Governance*, 38:4, e70067.`
(Crossref 10.1111/gove.70067: Li, Huanhuan; Sun, Zongfeng; article e70067.)

**L306.** `Lin, Hongyu (2025), 'Oscillation between resist and to not? Users' folk theories and resistance to algorithmic curation on Douyin', *Social Media + Society*.`
→ `Lin, Hui (2025), 'Oscillation between resist and to not? Users' folk theories and resistance to algorithmic curation on Douyin', *Social Media + Society*, 11:1.`
(Crossref 10.1177/20563051251313610: Lin, Hui; vol. 11 issue 1, January 2025.)

**L278.** `Hirsbrunner, Simon David, Kleemann, Sonja and Tahraoui, Mohammad Nadim (2025), 'Contestation in artificial intelligence as a practice: From a system-centered perspective of contestability toward normative contextualization, situative critique and organizational culture', *Frontiers in Communication*.`
→ `Hirsbrunner, Simon David, Kleemann, Steven and Tahraoui, Milan Nebyl (2025), 'Contestation in artificial intelligence as a practice: From a system-centered perspective of contestability toward normative contextualization, situative critique and organizational culture', *Frontiers in Communication*, 10, 1638257.`
(Crossref 10.3389/fcomm.2025.1638257: Kleemann, Steven; Tahraoui, Milan Nebyl; vol. 10, article 1638257.)

**L322.** `Mameli, Eleonora, Scarles, Caroline, Stangl, Brigitte and Frohlich, David (2026), 'A comprehensive framework for phygital tourism experiences', *Information Technology & Tourism*, 28:1.`
→ `Mameli, Elisa, Scarles, Caroline, Stangl, Brigitte and Frohlich, David (2026), 'A comprehensive framework for phygital tourism experiences: Bridging academic insights and industry practices across sectors', *Information Technology & Tourism*, 28:1, 19.`
(Crossref 10.1007/s40558-026-00362-6: Mameli, Elisa; full title has a subtitle; article 19.)

In-text citations are by surname only, so L110, L124, L126 need no change. The library cards for
these four are wrong in the same places and should be corrected after submission; that is not
tonight's job.

---

### [FIX TONIGHT] 5. The remaining incomplete entries, with the missing locators supplied.

Every locator below comes from the `.bib`, the card, or Crossref this evening, as marked.

**L256.** `Fink, Melanie (2025), *Human oversight under article 14 of the EU AI act*.`
→ `Fink, Melanie (2025), 'Human oversight under Article 14 of the EU AI Act', SSRN working paper 5147196, https://doi.org/10.2139/ssrn.5147196. Accessed 11 August 2026.`
(`.bib` @techreport: SSRN, working paper 5147196; card verified full-text 2026-08-11.) 'Article 14'
and 'AI Act' are proper names and keep their capitals; a working paper takes single quotes, not
italics. **With the entry completed, the in-text apology at L122 can go**: see finding 15.

**L414.** `... *Asia Pacific Journal of Human Resources*, 63:2.` → `... *Asia Pacific Journal of Human Resources*, 63:2, e70004.`
(Crossref 10.1111/1744-7941.70004: article e70004; authors as in draft are correct.)

**L398.** `Weaver, Adam (2025), '"Fast hospitality" and technology: Contemporaneous connections between "liquid" and "solid" in modern times', *Hospitality & Society*.`
→ `Weaver, Adam (2025), '"Fast hospitality" and technology: Contemporaneous connections between "liquid" and "solid" in modern times', *Hospitality & Society*, online first, https://doi.org/10.1386/hosp_00098_1. Accessed 11 August 2026.`
(Crossref still carries no volume or issue; published 28 October 2025.)

**L214.** `*Symphonya. Emerging Issues in Management*, pp. 149–164.` → `*Symphonya. Emerging Issues in Management*, 1, pp. 149–164.`
(`.bib` number = 1; *Symphonya* numbers issues within the year and has no volume.)

**L336.** `*Symphonya. Emerging Issues in Management*, pp. 103–116.` → `*Symphonya. Emerging Issues in Management*, 2, pp. 103–116.`
(`.bib` and Crossref: issue 2. 'La Rosa, Emily' is confirmed by Crossref; the card's 'Elisa' is wrong.)

**L260.** `... *Proceedings of the ACM on Human-Computer Interaction*.` → `... *Proceedings of the ACM on Human-Computer Interaction*, 10:2, CSCW022.`
(Crossref 10.1145/3788058: vol. 10 issue 2, pp. 1–45, April 2026; the article ID 'CSCW022' is
leaked in the Crossref title string. VERIFY the ACM Digital Library label before relying on it.)

**L410.** `... *Proceedings of the ACM on Human-Computer Interaction*, 9:CSCW.` → `... *Proceedings of the ACM on Human-Computer Interaction*, 9:7 (CSCW).`
(Crossref: vol. 9 issue 7, pp. 1–29, October 2025. Article number not in Crossref: VERIFY.)

**L250.** `... 8:CSCW1.` → keep as is; Crossref confirms 8:CSCW1, 29 pages. Article number: VERIFY.

**L222.** `Choi, Jungmin and Chao, Melody M. (2026), 'For me or against me? Reactions to AI (vs. human) decisions', ...`
→ `Choi, Jungmin and Chao, Melody M. (2026), 'For me or against me? Reactions to AI (vs. human) decisions that are favorable or unfavorable to the self and the role of fairness perception', *Personality and Social Psychology Bulletin*, 52:3, pp. 671–691.`
(Crossref: the draft truncates the title after the first clause. 'favorable' is the published
spelling.)

The three *Journal of Services Marketing* entries (L208 Brochado, L234 De Vos 2026, L380 Shabnam)
remain volume-less in Crossref tonight; 'pp. 1–20 / 1–23 / 1–17' with no volume is acceptable
Intellect form for online-first. L236 De Vos et al. 2023 (conference paper) is acceptable without
pages; adding `https://doi.org/10.15444/gmc2023.05.03.04` would help a reader find it. [CONSIDER]

---

### [FIX TONIGHT] 6. Year and volume disagree in three entries, against the list's own policy.

The list dates online-first articles by their **issue** year (Choi and Chao 2026 with 52:3, online
2024; Park et al. 2026 with 50:2, online 2024; Batat 2026 with 40:4, online 2025). Three entries
break that policy, and two of them sit beside a same-journal entry that follows it:

- **L316** `Lv, Linxiang ... (2024), ... *Journal of Travel Research*, 64:8, pp. 1974–1988.` → `(2025)`.
  Crossref: online August 2024, issue November 2025. L384 Shi et al. is dated 2025 at 64:4 of the
  same journal; the two cannot both be right. In text, **L120** `(Morosan and DeFranco 2016; Lv et al. 2024)` → `Lv et al. 2025`.
- **L402** `Xu, Feng Zeng ... (2020), 'Facial recognition check-in services at hotels', *Journal of Hospitality Marketing & Management*, 30:3, pp. 373–393.` → `(2021)`.
  Crossref: online October 2020, issue April 2021; L270 Gursoy is 35:2 in 2026, so volume 30 is
  2021. In text, **L102** and **L122** `Xu et al. 2020` → `Xu et al. 2021`.
- **L326** `Martin, Kirsten and Waldman, Ari (2022), ... *Journal of Business Ethics*, 183:3, pp. 653–670.` → `(2023)`.
  Crossref: online February 2022, issue March 2023. In text, **L124** `(Martin and Waldman 2022)` → `2023`.

If the authors prefer the online year, the alternative is to drop the volume and pages from these
three; what cannot stand is a 2020 date on a 2021 issue. Cost: 0.

---

### [FIX TONIGHT] 7. 'Five words' is six.

**L112.** `The distinction can be put in five words: competence is learned, standing is conferred.`
→ `The distinction can be put in six words: competence is learned, standing is conferred.`

Or drop the count: `The distinction is short: competence is learned, standing is conferred.` The
brief lists this as a known catch awaiting a decision. Cost: 0 or −3.

---

### [FIX TONIGHT] 8. Two sentences in §8 have lost their punctuation and read as a list of five.

**L150.** `Human-centricity, on this reading, is about what the arrangement protects or withholds, guest agency, employee discretion, relational judgment, and keeping humans visible in the encounter is neither necessary nor sufficient for any of the three.`
→ `Human-centricity, on this reading, is about what the arrangement protects or withholds: guest agency, employee discretion, and relational judgment. Keeping humans visible in the encounter is neither necessary nor sufficient for any of the three.`

As set, 'keeping humans visible' parses as the fourth item of the list and 'any of the three' has
no antecedent. Cost: 0 words.

**L156.** `Our framework suggests one mechanism that might join them, the same withholdings that shrink one guest's standing may, in aggregate, shape what a community can expect from its hospitable institutions, but establishing that is a job for future work, not a claim we have earned here.`
→ `Our framework suggests one mechanism that might join them: the same withholdings that shrink one guest's standing may, in aggregate, shape what a community can expect from its hospitable institutions. Establishing that is a job for future work, not a claim we have earned here.`

Cost: −1. Whether the paragraph earns its place is reviewer 07's question; if it stays, it should
parse.

---

### [FIX TONIGHT] 9. Commas inside closing quotation marks. Three instances, US convention in a British house.

- **L37.** `We should also be plain about the word 'welcome,' because` → `the word 'welcome', because`
- **L71.** `To say that a system 'forecasts the guest,' 'biases its own recommendations,' or 'revises its rules' reads smoothly` → `'forecasts the guest', 'biases its own recommendations', or 'revises its rules'`
- **L81.** `mediation is not simply 'helpful' or 'substitutive,' on or off.` → `'helpful' or 'substitutive', on or off.`

L13 (`'That's what the system shows.'`) is a complete quoted sentence and its full stop belongs
inside; leave it. L19 (`'guests without hosts': platform`) is already right.

---

### [FIX TONIGHT] 10. 'section 7' and 'Section 6'.

**L112.** `feedback is one of the things section 7 asks designers to build` → `Section 7`.
**L160.** `the three competences from Section 6` is the other instance. Capitalized cross-references are
the Intellect norm. Cost: 0.

---

### [FIX TONIGHT] 11. Three title-case stragglers in the reference list.

- **L296.** `*In Search of Hospitality: Theoretical Perspectives and Debates*` → `*In search of hospitality: Theoretical perspectives and debates*`. Every other book title in the list is sentence case (Batat 2019, Bowker and Star, Costanza-Chock, Derrida).
- **L208.** `'Is phygital the New normal? A literature review...'` → `'Is phygital the new normal? A literature review...'`
- **L416.** `'...intention to quit a job. evidence from the UK'` → `'...intention to quit a job. Evidence from the UK'`. A full stop mid-title takes a capital after it; that is the published form.

---

### [FIX TONIGHT] 12. 'face-recognition' as a noun.

**L102.** `their willingness to accept face-recognition at the hotel door` → `their willingness to accept facial recognition at the hotel door`. Both sources cited in that sentence (Xu et al.; Boo and Chua) say 'facial recognition', and a noun phrase takes no hyphen. Cost: 0.

---

### [CARRY FORWARD] 13. The two Batat quotations at L126 have no page locators, and one of them is unverified.

**L126.** `Extended-reality frameworks describe their purpose as a 'continuum in terms of customer value from physical to digital settings and vice versa' (Batat and Hammedi 2023); the founding framework of phygital customer experience aims to 'fluidify' the journey between online and offline (Batat 2024)`

- The Batat and Hammedi quotation is verified on the card **from the abstract** [card
  `batathammedi2023ert.md`, line 27]. The abstract sits on the article's first page, so
  `(Batat and Hammedi 2023: 10)` is defensible tonight. [FIX TONIGHT]
- The word 'fluidify' does not appear on the Batat 2024 card, which was read at abstract depth only,
  and the card records no verified quotation at all. Either someone finds the page in the article
  (pp. 1220–1243) or the quotation marks come off: `aims to make the journey between online and
  offline fluid (Batat 2024)`. Do not ship a quoted word with no locus. [CARRY FORWARD if no one can
  open the PDF tonight; otherwise FIX TONIGHT]

L19's `'guests without hosts'` is the article's title and needs no page.

---

### [CONSIDER] 14. The guest's pronoun.

The body has settled on singular 'they' for the guest (L25, L31, L33, L41, L61, L77, L79, L102,
L132, L134, L168; eleven instances). Two 'she's survive:

- **L41.** `whether the guest had a choice and whether she felt independent` → `whether they felt independent`
- **L122.** `She should not be treated as a problem to manage.` → `Such a guest should not be treated as a problem to manage.` (+2) or `They should not be treated...` (0)

L110's 'herself' and 'her' refer to the platform worker in Zhou et al.'s scale and can stay. My
predecessor asked for 'she' throughout; the author went the other way, which is fine so long as it is
all the way.

---

### [CONSIDER] 15. The Fink apology in text.

**L122.** `(Sterz et al. 2024; Li and Sun 2025; and, on human oversight under the EU AI Act, Fink 2025, still unpublished at the time of writing)`
→ `(Sterz et al. 2024; Li and Sun 2025; Fink 2025)`

Once the reference entry says 'SSRN working paper' (finding 5), the parenthesis says it for the
reader who cares and the body need not. Cost: **−13 words**, which is the cheapest saving in the
paper. The brief lists 'complete it, cut it, or keep it'; my vote is complete and shorten. Fink is
cited again at L136 without apology, so the text is already inconsistent about whether it needs one.

---

### [CONSIDER] 16. Twelve citation groups still break the chronological convention.

Twenty-six of thirty-eight multi-work parentheses run in date order. The twelve that do not, with
the reordering:

- L31 `(Lynch 2017; Beatty et al. 2016)` → `(Beatty et al. 2016; Lynch 2017)`
- L51 `(Roelofsen and Minca 2018; Germann Molz 2018)` → alphabetical within the year: `(Germann Molz 2018; Roelofsen and Minca 2018)`
- L61 `(Kropf et al. 2026; Santoni de Sio and Mecacci 2021)` → reverse
- L63 `(Rahman 2021; Calo and Rosenblat 2017)` → reverse
- L77 `(Raisch and Krakowski 2021; Parasuraman et al. 2000)` → reverse
- L100 `(Garcia et al. 2026; Kim et al. 2021)` → reverse
- L106 `(Eslami et al. 2016; DeVito et al. 2017; Ytre-Arne and Moe 2021; Jhaver et al. 2018)` → `(Eslami et al. 2016; DeVito et al. 2017; Jhaver et al. 2018; Ytre-Arne and Moe 2021)`
- L122 `(Yurrita et al. 2023; Lee et al. 2019)` → reverse
- L134 `(Padigar et al. 2025; Phillips et al. 2024)` → reverse
- L150 `(Mosca et al. 2026b; Casalegno et al. 2020)` → reverse
- L154 `(Okhuysen and Bechky 2009; Bovens 2007)` → reverse
- L156 `(De Vos et al. 2024; Christou et al. 2020; Pan et al. 2025; Parkinson et al. 2022)` → `(Christou et al. 2020; Parkinson et al. 2022; De Vos et al. 2024; Pan et al. 2025)`

Same list as 17 August, none applied. Zero cost; a referee will not reject over it, but a copyeditor
will query every one.

---

### [CONSIDER] 17. 'Mosca 2026a' and 'Mosca et al. 2026b' do not need the letters.

Harvard suffixes disambiguate identical author-year strings. 'Mosca 2026' and 'Mosca et al. 2026'
are already distinct. Drop the 'a' and 'b' at L118, L63, L150, L334 and L338. If the authors keep
them, they are at least correctly assigned (single author first in the list). Cost: 0.

---

### [CONSIDER] 18. Figure 1 is a caption without a figure.

**L27.** `Figure 1. How hosting's functions migrate but its obligation does not` and **L25** `Figure 1 sets out the logic that leads to this thesis.`

There is no figure file anywhere under `manuscript/` or `manuscript/submission/`. Either the figure
exists on the author's machine and goes up as a separate file with `[Figure 1 near here]` at L27, or
both lines come out (−10 body words, and the caption). A caption with no figure will bounce at
upload. The brief marks this as known; I mark it as a thing that cannot be left as it is.

---

### [CONSIDER] 19. Small consistencies, none of which a referee will reject over.

- **Table column capitalization.** Table 1 column 2 is lower-case throughout ('predictability');
  Table 2 column 2 is capitalized ('Map phygital touchpoints') and column 3 lower-case ('attention').
  Each column is internally consistent; a production editor will make them agree. Leave or fix.
- **'skills' / 'competences'.** §6 introduces 'three' as 'skills' (L106, L108) and §8 recalls them as
  'the three competences from Section 6' (L160). The section title is 'Competence is not standing'.
  One word would help; 'competences' at L106 costs nothing.
- **'artificial intelligence' → 'artificial intelligence (AI)'** at L15, since 'AI' is used unglossed
  from L17 on. +1 word.
- **'host-guest'** (L9, L77, L384) with a hyphen where an en dash is the typographic norm for a
  relation between equals. Consistent as it stands; Intellect's typesetter may change it.
- **L236** 'Lipnickas, Ged' against 'Lipnickas, Gediminas' at L208 and L234. Both are the published
  forms; a list is tidier with one.
- **L178** `'Destination (Un)Known: ...'` keeps a mid-title capital. It is the published styling;
  leave.
- **'handoff'** (L59, L69) as one word beside 'handed off' (L61). Consistent by part of speech.

---

## 3. Where it is strong — do not disturb

1. **Citation–reference correspondence, both ways, by eye.** 123 entries, every one cited; every
   in-text citation resolves; the two Chengs, two Kims, two Lees, two Lis, two Lins, two Lynches,
   two Spektors, two Yurritas and two Germann Molzes are all distinguishable in text. No 'et al.' on
   a two-author work, no 'X and Y' on a three-author work.
2. **The list's form.** Sentence case, single quotes on articles, italic journals, `volume:number`,
   `pp.` on extents and bare article numbers, commas between parts, `(eds)`, en dashes on every
   range, double-inside-single on all fourteen nested titles, 'in' once and correctly. This is now
   an Intellect list.
3. **Language.** Zero US spellings in the body ('behaviour', 'centred', 'honour', 'favourite',
   'defence', 'sceptical', 'programme', 'modelled', 'towards'); every US spelling in the list is a
   published title and correctly untouched. Zero false '-ise'. 'judgment' is used consistently.
4. **Oxford comma.** Held in every list I could find in the body.
5. **No double quotes, no em-dashes, no bold in running text, no ampersand** in the body.
6. **Enumerations add up.** Four words (L35), four duties (L61), three redistributed things (L63),
   three conditions (L79), six questions and six table rows (L85, Table 1), three skills (L106),
   three remediating routes (L110), two reasons (L108), three principles plus two (L120, L122), three
   compared mechanisms (L124), five stages and five table rows (Table 2), three contributions (L150),
   three studies (L160), '57 studies and 84 industry cases' (L126, matches the card). The one miss
   is finding 7.
7. **Term consistency.** 'standing' (as term), 'counterparty' (8, one spelling), 'interruptible /
   interruptibility' (6), 'touchpoint' (7, never 'touch point'), 'well-being' (body), 'self-service',
   'check-in', 'front-desk' as modifier and 'front desk' as noun, 'phygital' lower-case except at
   sentence start. All hold.

## 4. Best spend — the 100 words

I would not put them in the body. Finding 15 hands back thirteen. I would spend the evening's words
on the apparatus in finding 2, which costs nothing against the ceiling and is where the referee will
first see a mismatch: the three rewritten highlights above (247 characters) and the Statement of
Contribution brought into the manuscript's vocabulary. If body words must be spent, the one
sentence I would add is the missing gloss at L15, `artificial intelligence (AI)`, and the rest I
would hold.

## 5. Verdict

**Minor revisions**, on mechanics; nothing here touches the argument. The single most important fix
is **finding 2 together with finding 1**: delete line 3, and make the abstract, keywords, highlights
and Statement of Contribution that go up tomorrow the ones that describe this manuscript. The
reference list needs finding 4 (four wrong author names) before it goes anywhere; the rest is an
hour.

**Counts by tag:** [FIX TONIGHT] 12 findings (1–12), covering 4 wrong-author entries, 9 completed
locators, 3 year/volume corrections with 4 in-text changes, 3 title-case stragglers, 3 quotation
commas, 2 §8 sentences, 1 anonymity line, 1 venue signal, 1 'five words', 1 'section', 1 hyphen ·
[CONSIDER] 6 findings (14–19) · [CARRY FORWARD] 1 finding (13, the 'fluidify' locus) ·
unresolved citations 0 · uncited entries 0 · US spellings 0 · false '-ise' 0.

## 6. VERIFY — what I could not settle from here

1. **'fluidify' (L126, Batat 2024).** No verified quotation on the card; the page is unknown. Quote
   marks off, or a page on.
2. **ACM article numbers** for L250 Ehsan (8:CSCW1), L260 Gao and Thebault-Spieker (10:2, 'CSCW022'
   leaked in the Crossref title), L410 Yurrita et al. 2025 (9:7). Crossref does not carry them; the
   ACM Digital Library page does.
3. **Weaver 2025 (L398).** Still online-first in Crossref on 3 September. If *H&S* has since assigned
   it to 16:1 or 16:2, add the issue and drop 'online first'.
4. **Kim, Hyunsu et al. 2025 (L288).** `*International Journal of Human-Computer Interaction*, 42:10`
   is a 2026 volume (vol. 41 is 2025). Crossref returned no journal record for the title tonight;
   check the year against the issue, as in finding 6.
5. **'Brodhead Ahmadi, Sarah Renee'** (L208, L234). The publisher metadata parses the surname as
   'Ahmadi' with 'Brodhead' as a middle name; the `.bib` was corrected on 18 August to 'Brodhead
   Ahmadi'. One of the two is a filing decision the author of the paper can confirm.
6. **Lee and Lu 2024 (L300), article 103928.** The card says two sources disagree on the number;
   Crossref confirms 103928. Settled, but recorded here since the card still carries the flag.
7. **The library cards** for Li and Sun, Lin 2025, Hirsbrunner, Mameli, Mosca and La Rosa, Gao and
   Thebault-Spieker, Zhou et al. and Lin et al. 2026 carry the given names that Crossref contradicts.
   Not a submission item; a post-submission housekeeping item so the next paper does not inherit
   them.
8. **The AI acknowledgment** must describe what actually happened, and only the authors can say.
