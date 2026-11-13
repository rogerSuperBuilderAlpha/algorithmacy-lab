<!-- SIMULATED review, written by a Claude subagent on 11 Nov 2026 for the authors' preparation; not a journal review. -->

# Panelist 08: copyeditor, Intellect Harvard

**Manuscript:** `manuscript/DRAFT_v6.md`, 'Who hosts the guest? Algorithmic mediation, standing and responsibility in phygital hospitality'
**Also read:** `reviews/journal_2026-11/REVIEWS_FULL.md`, `submission/RESPONSE_TO_REVIEWERS_v6.md`, `JOURNAL_SPEC.md` and `literature/references.bib`. I searched all the cards in `library/cards/` by script and read about 45 of them directly. For one term the card does not record, I also read the saved Bulley (2015) manuscript text under `revision_2026-11/research/sources/`. I read nothing under `rewrite_2026-11/`.

**How I locate things.** I count prose paragraphs within each section or subsection, one-sentence lead-ins included (as the letter and R1 do), and leave out lists, tables and captions. HO is 'The host's power and the host's obligation'; DS is 'Delegation and standing'; AH is 'Assembled hosts at the touchpoint'; Split, Test, Reachable and Design are its four subsections. L is the line in DRAFT_v6.md.

**What I ran rather than read.** I wrote four throwaway scripts in my scratchpad, outside the repository:
- One extracted every single-quoted string in the body (74) and searched the cards for it. All but two matched verbatim; I confirmed those two by hand (Baum and Laux's 'rubber-stamps' on the version-of-record p. 126; the AI Act's 'stop' button, art. 14(4)(e)).
- One listed every year in the body with its context. I matched that list by eye against the 83 reference entries.
- One checked the 36 quotations the response letter attributes to the revised text against DRAFT_v6.md. All 36 are string-exact.
- One counted words, sentences and paragraphs.

`wordcount.py` and `preflight.py` both abort on DRAFT_v6.md as it stands, because each looks for a `## 1.` heading and v6's headings are unnumbered. I could not reproduce the brief's '20 of 23 checks'. My own count reproduces the 8,385-word body. That figure already includes table rows, which `wordcount.py`'s docstring says it counts; without them the body is 8,093. The brief's 'about 8,470 if table text is counted' therefore counts the tables twice. Either way the headroom is about 600 words.

---

## Step 0: register note

I judge mechanics against `JOURNAL_SPEC.md`: Intellect Harvard (`(Bordwell 1989: 9)`, volume:number, 'pp.' before extents, single-quoted article titles, italic journal titles), British spelling with 'ize', single quotation marks with doubles inside, and displayed quotations over 40 words. Where the spec is silent, as it is on legal sources, table captions and sub-lists in the references, I hold the manuscript to its own consistency and mark Intellect's house rule VERIFY. On register I follow the brief (the journal's measured habits, cohesion first) only where a mechanical habit produces the mannered effect.

---

## Part 1: rigour and argument, from a copyeditor's chair

My lens is narrow: whether each citation, locator, quotation, term and number is right and consistent. The argument itself belongs to the other seven panelists.

### What is already sound

Most of the apparatus is clean, and the authors should know which parts not to touch.
- **Citations match the reference list both ways.** All 83 entries are cited in the body, and every author–year citation in the body resolves to an entry. The four cases and seven statutes in the Cases and Legislation lists are all cited, and nothing cited is missing from them.
- **Quotations are accurate.** Every quotation matches its source card or saved text word for word, including the oddities that belong to the sources: Slattery's missing comma in 'not philanthropic it is economic' (HO ¶3, L32) is his. Nested quotation marks are right: 'through a "stop" button' (Conclusion ¶2, L149) correctly turns the Act's inner single quotes into doubles. No quotation reaches 40 words; the longest, from GDPR art. 22(3), runs to 27.
- **Spelling is consistently British with 'ize'.** I found no '-ise' verb and no American '-or' or '-er' spelling outside titles and proper names ('Labor' in EMTALA, 'Travelers' in Sandoval-Strausz's title). 'Judgement' (the faculty) and 'judgment' (a court's) are split correctly throughout.
- **Front-end form complies.** The abstract is 175 words (the limit is 100–200), there are six keywords of one or two words each, and the title is in sentence case.
- **The AI-acknowledgment section is in the right place.** Its heading reproduces the spec's wording exactly and sits after the Conclusion and before the References, as `JOURNAL_SPEC.md` requires.
- **Tables are called before they appear and in order.** Reachable ¶2 calls Table 1; Design ¶4 calls Table 2; Table 2's fourth row calls Table 1 back.

### Introduction

- **Abstract and introduction share sentences.** Introduction ¶1 (L18) repeats the abstract's first sentence nearly word for word ('from admission and pricing to check-in, room allocation and complaints'), and its last sentence repeats the abstract's second ('places the party … at a distance from the guest it affects'). An editor reads the two pages back to back and will notice. See Part 2 and rewrite 1.
- **Lynch et al. (2011) is cited without a page.** Introduction ¶2 (L20) cites it for 'a lens on social relations and power'. The card supports 'a lens upon social relations' but records nothing about power. See The read, finding 1.
- **Two parenthetical strings break the paper's own order.** The paper otherwise lists citations chronologically, but '(Germann Molz 2026; Riordan 2024)' (Introduction ¶2, L20) and '(Rahman 2021; Calo and Rosenblat 2017)' (Split ¶4, L82) run backwards.

### The host's power and the host's obligation

- **Unlocated attributions.** HO ¶1 (L28) and HO ¶3 (L32) carry three of the five unlocated Lynch et al. (2011) attributions, plus O'Gorman (2009) and Varley et al. (2018) without pages (finding 1).
- **The King attribution is wrong in form.** HO ¶10 (L46) attributes a sentence to 'King's formulation' that is Golubovskaya et al.'s own sentence (finding 3).
- **Serial comma.** HO ¶4 (L34) writes 'a moment at which it comes into force, and a holder', with a serial comma. Introduction ¶3 (L22) gives the same phrase without one. The paper should pick one rule; British practice, and most of this manuscript, omits it (rewrite 2).
- **Jurisdiction.** HO ¶7 (L40) says 'Great Britain' for the Equality Act, which the card confirms (extent E+W+S). Conclusion ¶3 later calls the legal sources 'English' (finding 9).

### Delegation and standing

The section carries most of the pinpoint problems.
- **Morgan (2015).** DS ¶2 (L54) and DS ¶4 (L58) cite pp. 7–8 and p. 7. Those are pages of the accepted manuscript, not of the *Cambridge Law Journal* article (pp. 109–139) that the list gives (finding 2; also R1, R2).
- **Crinkley.** DS ¶3 (L56) pinpoints by paragraph ('paras 7, 9'; 'paras 9, 49–52') a decision the Cases list cites to the Federal Reporter. The card supplies the reporter pages (finding 2; also R1).
- **Bulley's term.** DS ¶3 borrows 'assembled host' from Bulley (2015) without quotation marks or a page. The card does not record the phrase. I found it in the saved author manuscript (pp. 14 and 16), so the attribution is sound; it lacks a locator (finding 2; rewrite 4).
- **Kong.** DS ¶5 (L60) closes a single-sentence quotation from Kong with three locators, '(2026: 4–5, 10)'. The quotation is on p. 10 (rewrite 7).
- **Thompson.** DS ¶6 (L62) quotes Thompson's 'X has a right against Y' correctly from his table (p. 335). Set beside 'X has a duty to Y to do A', though, it reads as a slip: X appears to hold the duty and the right against the same person. The card notes that the relettered form, 'Y has a right against X', is not on p. 335, so the paper cannot simply swap the letters inside the quotation marks (rewrite 8).
- **Which/that.** DS ¶3 mixes restrictive 'which' and 'that' inside one sentence: 'the party which holds itself out … the party that controls … a party which only arranges' (rewrite 5).

### Assembled hosts at the touchpoint

- **Kaniadakis and Farmaki.** Split ¶2 (L78) cites '2022: 14'. The card records p. 14 as a page of the 21-page OnlineFirst PDF, while the list gives the 2024 issue (26:10, pp. 5763–5783). Year, volume and pinpoint each belong to a different version (finding 2; also R1, R2).
- **Table 1 and its prose disagree.** Reachable ¶3 (L121) says 'Identity checks, room allocation and pricing need a later appeal by default'. Table 1 (L115) gives identity verification 'A staffed fallback', not a later appeal. The same table renames 'room allocation' as 'Room assignment' (L116) and 'identity checks' as 'Identity verification' (finding 4).
- **Table 2 drifts from the prose that introduces it.** Design ¶4 (L133) has an 'identifiable actor'; Table 2's stage 4 (L142) has 'an accountable actor'. The prose's stage 3 supports what people can 'understand, adjust and challenge'; Table 2's stage 3 (L141) supports only 'interpretation and adjustment'. Stage 5's 'Accountability, through exit' and stage 1's 'Common understanding' are already flagged (also R1, R2, R3).
- **Sentence length.** Design ¶1 (L127) holds the longest sentence in the paper: 61 words with citations, 52 without. It contradicts the letter's reply to R3.2 (finding 5).
- **Special issue.** The AH opening paragraph (L72) names 'this special issue'. It names no editor, so anonymity holds, and the editor will judge the positioning. R1 has already corrected the idiom ('To keep with' should be 'In keeping with'). The clause can simply go, saving eight words.

### Conclusion

- **Undefined term.** Conclusion ¶2 (L149) introduces 'a typology of decisions', a word the body never uses for Table 1.
- **Tables not named.** The same sentence names neither table, although the letter tells R1 that 'Where the paper refers to a table, it names it' (rewrite 11).
- **Jurisdictions.** Conclusion ¶3 (L151) describes the legal sources as 'English, United States federal and European Union law'. Two of the British statutes extend to Great Britain, the cards say, and DS ¶3 itself says Crinkley was decided 'under North Carolina law' (finding 9; also R2, R3; rewrite 12).
- **'Framework'.** Conclusion ¶4 and ¶5 keep the bare 'framework' (also R1).

### Reference list, Cases and Legislation

The detail is under findings 2, 6, 7 and 8. In summary:
- **One misnamed journal.** Slattery's entry gives the wrong journal title (finding 6).
- **One truncated title.** Lyons et al. (2021) loses its subtitle.
- **Six titles break the sentence-case rule** that the rest of the list follows.
- **About a dozen entries are incomplete.** Each lacks an article number, an issue, an editor, a place, a URL or a page.
- **The legal lists mix conventions.** They use 'v.' with Bluebook-style court parentheticals for an American case and the same 'v.' for English ones.

`JOURNAL_SPEC.md` says nothing about legal sources, so I mark Intellect's form VERIFY throughout.

---

## Part 2: slop audit, from a copyeditor's chair

I count only to point at passages. The question is whether a desk editor at Intellect, reading for house style, would query the passage as mannered.

**1. The abstract pasted into the introduction.** The abstract's first sentence (L12) and Introduction ¶1's first sentence (L18) share the clause 'much of the work of hosting, from admission and pricing to check-in'. Each continues 'room allocation and complaints'. The abstract's 'places the party that decides at a distance from the guest' returns as Introduction ¶1's closing sentence, with 'who' for 'that'. R3 has caught the thesis refrain (also R3). This is a different fault: whole sentences recycled at the paper's two most-read places.

**2. Pseudo-clefts.** Eight declarative sentences open 'What X is Y':
- Introduction ¶3 (L22): 'What can fail is its exercise'.
- HO ¶7 (L40), twice in succession: 'What separates hospitality…'; 'What remains distinctive is narrower'.
- HO ¶9 (L44): 'What the law does give is'.
- DS ¶4 (L58): 'What algorithmic delegation changes is the performer'.
- DS ¶9 (L68): 'What a guest can expect … is therefore a hearing'.
- Split ¶3 (L80): 'What phygital arrangements change is therefore not'.
- Design ¶2 (L129): 'What guests need is not a human presence as such'.

DS ¶6 (L62) then repeats 'what can fail is its exercise' verbatim from Introduction ¶3. One cleft per section can carry emphasis; eight, two of them paired with 'therefore' and two with 'not … but', read as a template.

**3. Hedging tags.** Five sentences hang a qualifier off the front or middle: 'On that view' (Introduction ¶2, L20), 'on these accounts' (HO ¶1, L28), 'On this account' (HO ¶5, L36), 'on this reading' (HO ¶9, L44) and 'on this reading' (Conclusion ¶2, L149). Each tells the reader that a gloss is being applied rather than applying it. Most can go without loss.

**4. No em-dashes, so glosses ride on commas.** The body has none in 8,385 words. Introduction ¶1's three stipulations run on gapping alone, so the reader must hold 'we call' across two semicolons: 'the guest, the staff, the property, the firms and the systems together, a phygital arrangement'. Read aloud, 'together, a phygital arrangement' is hard to follow. An em-dash or a second 'we call' would let the sentence breathe. I flag this only because the house style the brief points to favours the em-dash for exactly this job.

**5. Restrictive 'which'.** 'Party which' appears three times (DS ¶3 twice, Conclusion ¶4 once) against 'party that' five times. Intellect's desk will normalize these to 'that'. Better that the authors do it, since DS ¶3 mixes both in one sentence.

**6. Long sentences.** Ten sentences exceed 50 words with their citations, and seven still exceed 50 without them. The longest are:
- Design ¶1 (L127), 61 words: 'Three principles belong to the interface: explain a decision where it lands'.
- Introduction ¶2 (L20), 60: 'This journal has studied platforms since its first volume'.
- Introduction ¶2 (L20), 59: 'The phygital literature presents such systems as means'.

These matter here because the letter promises R3 that none exceeds 'about fifty words' (finding 5). R3's further points ('therefore' eleven times, contrast pairs, numbered inventories, aphoristic endings) stand, and I do not repeat them (also R3).

The rest reads as written for the journal. The quotations are integrated cleanly, the citations sit where the claims are, and paragraphs average 170 words, inside the 130–200 the brief measured. Two paragraphs run long: DS ¶3 at 293 words and Conclusion ¶2 at 287.

---

## Part 3: line-level rewrites

Suggestions only; the authors' read-aloud decides. Word costs are body words.

**1. Introduction ¶1, L18, the sentence the abstract already uses.**
- Original: 'Phygital hospitality hands much of the work of hosting, from admission and pricing to check-in, room allocation and complaints, to systems and firms that the guest rarely sees.'
- Suggestion: 'In phygital hospitality, systems and firms that the guest rarely sees now do much of the work of hosting.' (Saves 9 words. The next four sentences already name the jobs.)

**2. HO ¶4, L34, serial comma.**
- Original: 'it has a content, a moment at which it comes into force, and a holder'.
- Suggestion: 'it has a content, a moment at which it comes into force and a holder', matching Introduction ¶3. (0 words)

**3. HO ¶10, L46, the King attribution, after 'the guest's duties narrow:'.**
- Original: 'in King's formulation, as Golubovskaya et al. report it, the guest's 'only obligation is to pay and behave reasonably' (2017: 1286).'
- Suggestion: 'Golubovskaya et al., following King (1995), give the guest's 'only obligation' as 'to pay and behave reasonably' (2017: 1286).' (Saves about 1 word. The quoted words are theirs, not King's.)

**4. DS ¶3, L56, Bulley's term.**
- Original: 'an assembled host (2015)'.
- Suggestion: 'an 'assembled host' (2015: [page])'. (0 words. A term borrowed from a named author goes in quotation marks at first use, with its page.)

**5. DS ¶3, L56, which/that.**
- Original: 'the party which holds itself out as host … a party which only arranges a service'.
- Suggestion: 'the party that holds itself out as host … a party that only arranges a service'. (0 words. The same change applies in Conclusion ¶4, L153.)

**6. DS ¶3, L56, and Split ¶3, L80, Crinkley pinpoints.**
- Original: '(1988: paras 7, 9)'; '(1988: paras 9, 49–52)'; '(1988: para 7)'.
- Suggestion: '(1988: 159)'; '(1988: 159, 166–67)'; '(1988: 159)'.

The card maps paras 7 and 9 to p. 159, paras 49 to the middle of 51 to p. 166, and the rest of 51 and para 52 to p. 167 of 844 F.2d. (Saves 4 words.)

**7. DS ¶5, L60, the Kong quotation.**
- Original: 'Kong grounds that responsibility in the deployer's control over the act of delegating and concludes that 'one who elects a delegate that cannot answer thereby elects to answer for it' (2026: 4–5, 10).'
- Suggestion: 'Kong grounds that responsibility in the deployer's control over the act of delegating (2026: 4–5) and concludes that 'one who elects a delegate that cannot answer thereby elects to answer for it' (2026: 10).' (Adds 2 words.)

**8. DS ¶6, L62, Thompson.**
- Original: 'Thompson's forms of directed duty, 'X has a duty to Y to do A' and 'X has a right against Y' (2004: 335), fix who owes what to whom without mentioning answering.'
- Suggestion: 'Thompson's form of directed duty, 'X has a duty to Y to do A' (2004: 335), fixes who owes what to whom without mentioning answering.' (Saves 7 words.)

**9. Reachable ¶3, L121, the sentence that contradicts Table 1.**
- Original: 'Identity checks, room allocation and pricing need a later appeal by default, and a reachable person where failure would refuse entry or leave a room unusable.'
- Suggestion: 'Identity checks need a staffed fallback, room allocation and pricing a later appeal, and the first two a reachable person where failure would refuse entry or leave a room unusable.' (Adds 4 words.)

If the authors mean the prose, change Table 1's identity row instead.

**10. Tables 1 and 2, L116, L141, L142: terms that drift from the prose.**
- Original: 'Room assignment'; 'Builds the capabilities that support interpretation and adjustment'; 'an accountable actor with authority to change outcomes'.
- Suggestion: 'Room allocation'; 'Builds the capabilities that let guests and employees understand, adjust and challenge decisions'; 'an identifiable actor with authority to change outcomes'. (Adds 4 words.)

**11. Conclusion ¶2, L149, the three contributions.**
- Original: 'and third, a test, a typology of decisions and five stages for organizations.'
- Suggestion: 'and third, a test, a typology of decisions (Table 1) and five stages for organizations (Table 2).' (Adds 4 words, and makes the letter's R1.5 reply true.)

**12. Conclusion ¶3, L151, the jurisdictions.**
- Original: 'its legal sources are English, United States federal and European Union law, with one decision of a United States federal appeals court'.
- Suggestion: 'its legal sources are English and British law, United States federal law, one federal appeals decision applying the law of North Carolina, and European Union law'. (Adds 4 words; also R2, R3.)

---

## Who I am

I copyedit for Intellect's social-science journals, *Hospitality & Society* among them, and my job is the stage after acceptance. I check that every citation resolves, that every page number belongs to the version in the list, that quotation marks and capitals follow house style, and that a term means the same thing on page 3 and page 23. I came to this paper expecting a conceptual manuscript drafted at speed to fail on the apparatus: invented locators, quotations drifting from their sources, a reference list half in APA. It does not. The quotations are exact and the citation network closes in both directions, which is rarer than it should be. What it gets wrong is the layer beneath that. Several pinpoints come from a different version of a source than the one listed. A handful of attributions rest on a card that does not record them. And the tables and prose drifted apart during revision.

## The read

Findings are ranked by the damage they would do if a referee, the special-issue editor or Intellect's production desk found them first.

**1. Five attributions to the journal's founding editorial, and one to a work never listed, cannot be checked against the card.** [FIX if the full text is to hand, about half a day; otherwise CARRY FORWARD]

The paper attributes five specific claims to Lynch et al. (2011), none with a page:
- 'a lens on social relations and power' (Introduction ¶2, L20);
- a duty to the stranger in 'the Greek, Roman and Enlightenment traditions … that was sacred and reached beyond shelter to protection' (HO ¶1, L28);
- 'a similar claim from Aramberri' (HO ¶3, L32);
- the editors' answer, that 'hospitality still describes what passes between strangers within the commercial realm' (HO ¶3, L32);
- micro-hosts and macro-hosts 'after Robinson and Lynch', with a train company as the example (DS ¶3, L56).

The card `lynch2011theorizing` records three quotations without locators (the journal's aim, its opening paradox and its antonym pairs) and supports 'a lens upon social relations'. It records nothing about sacred duty, Aramberri, the editors' answer, macro-hosts or power. No other card does, and no saved full text exists under `revision_2026-11/research/sources/`. The claims may all be right. But this is the journal's founding editorial. The Lynch card notes that Germann Molz is its second author, and the bibliography's note on Germann Molz (2026) calls her a current *Hospitality & Society* co-editor and a likely reviewer. A misdescription here is the error most likely to be noticed by the person best placed to notice it.

'After Robinson and Lynch' also names a work that has no year and no reference entry. It needs one, or a 'cited in' form.

The fix is to find each claim in the editorial, add its page, and add Robinson and Lynch to the list. This costs about 12 body words for pages and nothing in the reference list. None of R1, R2 or R3 raised this.

**2. Pinpoints that belong to a different version of the source than the one listed.** [FIX, 0 body words, after the version-of-record pages are found]

Morgan's 'pp. 7–8' and Kaniadakis and Farmaki's '2022: 14' are known (also R1, R2), but R1 and R2 read them as out-of-range typos. The cards show they are a version problem, and the same problem recurs elsewhere:
- **Morgan (2015).** DS ¶2, L54 (7–8) and DS ¶4, L58 (7). The card says 'Locators are pages of the accepted manuscript (AM pdf p.), not journal pages', and that the wording 'may differ slightly from the version of record'. Both the pages and the quotation need checking against *CLJ* 74:1.
- **Kaniadakis and Farmaki (2022).** Split ¶2, L78. The card says 'Locators are the OnlineFirst pages 1-21, NOT the issue pages'. The list then gives the 2024 issue's volume. Choose one version and make year, volume and page agree. If the OnlineFirst PDF and the issue run in parallel (21 pages each), p. 14 would be p. 5776; VERIFY.
- **Crinkley (1988).** DS ¶3, L56 and Split ¶3, L80. 'Paras' are Public.Resource.Org's paragraph numbers; the Cases list cites 844 F.2d. The card maps them to reporter pages 159, 166 and 167 (rewrite 6). R1 raised the form; the mapping is new.
- **Bulley (2015).** 'Assembled host' (DS ¶3, L56) has no page at all. It is at pp. 14 and 16 of the author manuscript; the journal page is VERIFY.
- **Author-manuscript locators that the body omits.** These sources carry locators only to accepted or author manuscripts, and the body gives no page for them. Each specific claim needs a version-of-record page:
  - O'Gorman (2009), HO ¶1, L28 (author-version p. 11);
  - Varley et al. (2018), HO ¶1, L28 (section 2, second paragraph);
  - Moysidou and Stanley (2023), DS ¶7, L64 (accepted manuscript p. 12);
  - Petie et al. (2025), AH opening, L72 (manuscript p. 11).
- **Baum and Laux (2026).** The card records that the chapter's own footer reads 'LNCS 17146, pp. 115–130, 2027'. Either year can be defended; whichever the authors choose, say so.

The letter makes this matter. Its reply to R3.22 says 'We have checked every quotation and locator … against the text of its source'. Quotations, yes: I confirmed all of them. Locators, no: at least three point to a version other than the one listed. Either fix the locators or soften the letter.

**3. A second-hand quotation attributed to the wrong author.** [FIX, 0 words]

HO ¶10 (L46) introduces the guest's duty to 'pay and behave reasonably' with 'in King's formulation, as Golubovskaya et al. report it'. The card for Golubovskaya et al. gives their sentence as '…empowers the guest, whose only obligation is to pay and behave reasonably (King, 1995)' (p. 1286). The quoted words are therefore theirs, not King's, and King's own card records the source at abstract depth only. The phrase 'King's formulation' claims a wording nobody on this project has seen.

R3 asks the authors to cite King directly at HO ¶1 (L28). I disagree (contra R3). Citing King directly would turn a reported claim into a quotation from an unread source. The Varley card says outright to cite it 'as Varley et al.'s statement, not as King's words'. The draft's 'on the authority of King (1995)' at HO ¶1 is the correct form. HO ¶10 should follow it (rewrite 3).

**4. Table 1 and the prose that explains it disagree, and its row labels drift.** [FIX, about 8 words]

Reachable ¶3 (L121) assigns identity checks 'a later appeal by default'; Table 1 (L115) assigns them 'A staffed fallback'. A referee who checks the table against its gloss will find the mismatch in a minute, and R2's comments on Table 1's placements make it likely that someone will check. Two labels also drift:
- **'Room allocation' versus 'Room assignment'.** The abstract (L12), Introduction ¶1 (L18) and Reachable ¶3 (L121) say 'room allocation'; Table 1 (L116) says 'Room assignment'.
- **'Identity checks' versus 'Identity verification'.** Reachable ¶3 says 'identity checks'; Table 1 says 'Identity verification'.

Table 2 drifts in the same way ('accountable actor' against the prose's 'identifiable actor'; 'interpretation and adjustment' against 'understand, adjust and challenge'). See rewrites 9 and 10. This is new; R1, R2 and R3 judged the tables' content, not their agreement with the prose.

**5. The letter states numbers the manuscript does not bear out.** [FIX, 0 to 30 words]

Three statements in the letter fail a count:
- **Sentence length.** R3.2 is told 'no sentence in the revised paper runs to more than about fifty words'. By my count ten exceed 50 words with their citations and seven without; the longest is 61 (Design ¶1, L127). Either split the three longest (L127, L20 twice) or change the letter to 'about sixty'. The R3 agent recorded the 61-word sentence in its notes but did not tie it to the letter.
- **Tables.** R1.5 is told 'Where the paper refers to a table, it names it'. Conclusion ¶2's 'typology of decisions' and 'five stages' name neither table (rewrite 11).
- **Questions.** R3.1 is told 'one question remains'. Two remain in the body, plus one in a heading (also R1, R3).

**6. A misnamed journal.** [FIX, 0 body words]

The list gives Slattery's journal as '*The Journal of Hospitality Leisure Sport and Tourism*' (L301). The card's venue line reads 'Journal of Hospitality, Leisure, Sport and Tourism Education', and its source basis abbreviates the journal 'JoHLSTE', as does the DOI (10.3794/johlste.11.7). The listed title drops 'Education', the commas and, probably, the initial 'The'. A typesetter will not catch this; a referee who looks up Slattery will. This is new.

**7. Incomplete or inconsistent entries.** [FIX, 0 body words]

The spec asks for volume:number and 'pp.' before extents; the following fall short. Items already flagged elsewhere are marked.

*Missing article numbers, subtitles or issues:*
- **Kong (2026)**, L239: '6:5.' lacks the article number 518 (card: 'AI and Ethics 6(5), article 518').
- **Hatherley (2025)**, L227: '27:2.' lacks article 20 (card: 'Ethics Inf Technol (2025) 27:20') (also R1).
- **Lin (2025)**, L247: '11:1.' lacks an e-locator; VERIFY (also R1).
- **Lyons et al. (2021)**, L257: the title stops at 'Conceptualising contestability'. The card gives the full title, 'Conceptualising Contestability: Perspectives on Contesting Algorithmic Decisions', and article 106.
- **Mosca and La Rosa (2019)**, L271: has no issue. The bib records issue 2 (DOI 10.4468/2019.2.08…).

*Online-first entries:*
- **Brochado et al. (2026)**, L195, and **Shabnam et al. (2026)**, L297: these are online-first, and the card for Shabnam et al. records 'no volume, issue or printed page numbers'. Their 'pp. 1–20' and 'pp. 1–17' are PDF page counts, not page extents. Mark them as online first, with DOIs (volumes also R1).

*Books, chapters and reports:*
- **Baum and Laux (2026)**, L179: stray ', :'; no editors, series (Lecture Notes in Computer Science, 17146) or place (also R1, R2 in part).
- **Darwall (2013)**, L209: stray ', :'. The card gives the book's subtitle, *Essays in Second-Personal Ethics I*, and the place is missing (also R1, R2 in part).
- **Article 29 Data Protection Working Party (2018)**, L167: an online-only document with no URL or adoption date. The card holds both (adopted 3 October 2017, revised 6 February 2018; ec.europa.eu/newsroom/article29/items/612053).

*Year mismatches* (also R1, R2):
- **Kaniadakis and Farmaki**, L233: dated 2022 with the 2024 volume.
- **Kim et al.**, L235: dated 2025 with volume 42, which is probably the 2026 issue; VERIFY.

*Legislation:*
- **GDPR**, L351: lacks its page. The card gives 'L 119, 4.5.2016, pp. 1-88'.
- **EMTALA**, L343: omits 'Pub. L. 99-272', although the Civil Rights Act entry, L341, gives its Pub. L. The card for each supplies it.

*Initials:* 'Richard N.S.' (L225) against 'A. K.' and 'Amy L.' elsewhere.

**8. Capitals in titles.** [FIX, 0 body words]

The list uses sentence case with a capital after a colon, as the spec's examples do ('Algorithmic management: The case of Airbnb'). Seven entries break it:
- Blain and Lashley, 'The New service metaphor?', L187 (also R1).
- Brochado et al., 'Is phygital the New normal?', L195.
- Burdick, '… companies. part I', L199, which should read 'Part I'.
- Sandoval-Strausz, 'jim crow', L293, which should read 'Jim Crow' (also R1).
- Golubovskaya et al., ': do employees understand?', L225.
- O'Gorman, ': from the fanciful to factual', L277.
- Kong, ': why deploying…', L239.

The last three are lowercase after the colon where every other entry capitalizes. Di Domenico and Lynch's 'Host/Guest' (L213) should be 'Host/guest'. Book titles are inconsistent too. Hirschman's is in sentence case with a stray capital ('… and States', L229), while Darwall's, Thompson's and Baum and Laux's books are in title case. Intellect's rule for book titles is VERIFY; one rule is not.

**9. Legal sources: form, jurisdiction and internal agreement.** [FIX for consistency; VERIFY for Intellect's form]

`JOURNAL_SPEC.md` confirms only the general rules: year in brackets, commas between parts, a list titled 'References' holding only cited works. On those terms the Cases and Legislation lists comply. The spec says nothing about separate 'Cases' and 'Legislation' sub-lists, italic case names, 'v' or 'v.', or how to pinpoint a case. Within that silence the manuscript is internally inconsistent:
- **Case names are roman**, in the body and in the list (L38, L42, L54–58, L331–337). OSCOLA and most Harvard variants italicize them. VERIFY Intellect's rule; whatever it is, apply it to the short forms too ('in Woodland', L58).
- **'v.' is used throughout.** The cards and bib entries for the English cases write 'Lane v Cotton' and 'Woodland v Essex County Council', the OSCOLA form. The Crinkley entry, L333, is a Bluebook–Harvard hybrid: '(1988) 844 F.2d 156 (4th Cir.)'. VERIFY and pick one.
- **Calye's Case is pinpointed by 'fol. 33a/33b/32b'** (L38, L42, L58). OSCOLA would cite '8 Co Rep 32a, 33a'. VERIFY.
- **The Civil Rights Act's short title is 'Civil Rights Act of 1964'** (both card and bib). The list and body drop 'of' (L123, L341).
- **Jurisdiction.** The cards give the Hotel Proprietors Act and the Equality Act the extent E+W+S, and HO ¶7 rightly says 'Great Britain'. Conclusion ¶3 nonetheless calls the legal sources 'English' and its American law 'federal', although DS ¶3 says Crinkley was decided 'under North Carolina law' (also R2, R3; rewrite 12).

**10. Terms that change between sections.** [FIX, 0 to 30 words; CONSIDER for the definition]

The paper's thesis turns on a reachable holder of authority, and its wording for that holder varies:
- 'a reachable party with authority' (abstract, L12; Reachable ¶1, L105);
- 'a reachable person' (Table 1, five rows; Reachable ¶3);
- 'someone with authority' (six times);
- 'anyone with authority' (three times);
- 'reachable authority' (Design ¶2, L129).

The argument makes firms (parties) the holders and has employees (persons) do the answering, so 'party' and 'person' are not interchangeable. A copyeditor can only query this. The authors should say once which is meant, perhaps in the best-spend sentence below. 'Typology' appears only in the Conclusion; 'answerability' appears in a heading, the Table 2 title and the Conclusion but is never defined (also R1).

**11. Smaller mechanics.** [FIX, net saving of about 15 words]
- Abstract–introduction duplication (Part 2.1; rewrite 1).
- The serial comma (rewrite 2).
- Restrictive 'which' (Part 2.5; rewrite 5).
- Two out-of-order citation strings (Introduction ¶2, Split ¶4).
- Kong's triple locator on one quotation (rewrite 7).
- Thompson's form, which reads as a slip (rewrite 8).
- The in-text 'Article 29 Working Party' (L99, L121, L123) does not match the list's 'Article 29 Data Protection Working Party' (L167). The author element of an in-text citation should match the list's first element. Shortening the list entry costs nothing.

**12. Tooling.** [FIX, outside the manuscript]

`wordcount.py` and `preflight.py` abort on DRAFT_v6.md ('ABORT: no body found'; `IndexError` at `preflight.py` line 41). The authors should not rely on either for the resubmission until the scripts accept unnumbered headings. The body figure the brief quotes, 8,385, already counts table rows.

## Where it is strong

Any revision should keep the following.
- **The quotations.** All 74 single-quoted strings in the body match their sources, and the hard cases are handled with care: the Hotel Proprietors Act's ellipsis (L42), Baum and Laux's version-of-record spelling 'rubber-stamps' (L129), and the AI Act's nested 'stop' (L149).
- **The citation network.** It closes in both directions across 83 references, four cases and seven statutes. Most manuscripts I see at this stage do not manage that.
- **The response letter's quotations.** All 36 quotations of the revised text are string-exact, and its paragraph locators match the draft.
- **Language and front matter.** British spelling with 'ize' is consistent, with the judgement/judgment distinction right. The abstract length, keywords, the AI-acknowledgment heading and its placement all meet the spec.
- **Second-hand citation at HO ¶1.** 'Varley et al. (2018) put the point on the authority of King (1995)' (L28) is the correct way to handle a source read only in abstract. It should stay as it is, and HO ¶10 should copy it.

## Best spend

Most of my findings cost no body words, because references do not count against the limit. I would spend about 75 of the 150 words: three sentences, plus small additions to existing ones.

*Suggested, for the authors' read-aloud (drafted by the reviewer):*

> **Reachable ¶1, after its last sentence (L105), +33 words.** By a reachable party we mean the party that holds the host's role, acting through a person (an employee or manager) whom the guest can contact while the decision can still be changed.

> **Reachable ¶2, replacing L107, +10 words.** Table 1 places common hospitality decisions against this boundary, and serves as a typology of the recourse each needs.

> **Conclusion ¶3, replacing its first limit (L151), +4 words.** First, its legal sources are English and British law, United States federal law, one federal appeals decision applying the law of North Carolina, and European Union law, so the account of when the obligation comes into force and who holds it may not travel unchanged to other jurisdictions.

Add to these rewrites 9, 10 and 11 (12 words), and the page locators for Lynch et al. (2011) and Bulley (about 15 words). I would leave the remaining 75 words to the panelists whose findings need argument.

## Verdict

**Minor revision on mechanics.** The apparatus is unusually clean at the level that tools check, and flawed at the level they do not: version-matched pinpoints, attributions the cards cannot confirm, and tables that drifted from their prose. Every item but finding 1 is a day's work.

**The single most important fix:** before resubmission, find each of the five Lynch et al. (2011) attributions in the editorial and give it a page. Then convert every pinpoint to the pagination of the version the reference list names: Morgan, Kaniadakis and Farmaki, Crinkley, Bulley, and Baum and Laux's year.

## VERIFY

1. **Lynch et al. (2011).** Not on any card, and no saved full text:
   - 'social relations and power';
   - the Greek, Roman and Enlightenment sacred duty;
   - Aramberri;
   - the editors' answer on 'the commercial realm';
   - micro-hosts and macro-hosts after Robinson and Lynch, with the train company.

   Also find the year and reference for Robinson and Lynch.
2. **Version-of-record pages:**
   - Morgan (2015), the quotation at AM p. 7 and the claim at AM pp. 7–8;
   - Bulley (2015), 'assembled host', AM pp. 14 and 16;
   - O'Gorman (2009), author version p. 11;
   - Moysidou and Stanley (2023), AM p. 12;
   - Petie et al. (2025), MS p. 11;
   - Varley et al. (2018), section 2;
   - Kaniadakis and Farmaki, OnlineFirst p. 14, which is probably issue p. 5776.
3. **Morgan's wording.** The card warns that the accepted manuscript's wording 'may differ slightly from the version of record'. Recheck 'No duty of care can be delegated, but its performance may well be' against *CLJ* 74:1.
4. **Intellect's form for legal sources:**
   - separate 'Cases' and 'Legislation' sub-lists under References;
   - italic case names;
   - 'v' or 'v.';
   - whether to pinpoint the Coke Reports by folio;
   - the form for United States statutes and Official Journal citations.

   `JOURNAL_SPEC.md` is silent on all of these.
5. **Other Intellect house rules the spec does not state:**
   - table-caption form ('Table 1.' in bold against 'Table 1:') and whether tables go in the text or at the end with call-outs;
   - '…' against '[…]' in quotations;
   - whether book titles take sentence or title case;
   - whether three-author works take 'et al.' at first citation.
6. **Online-first and year questions:**
   - Brochado et al. and Shabnam et al.: whether they now have a volume and issue (possibly *JSM* 40:4, with Batat 2026; unconfirmed);
   - Kim et al. (2025): the year of volume 42, issue 10;
   - Lin (2025): its e-locator;
   - Baum and Laux: 2026 or 2027.
7. **Thompson (2004).** The card gives the publisher as Clarendon Press; the list says Oxford University Press. Clarendon is an imprint of OUP, but use the imprint on the title page.
8. **Pitt-Rivers (2012).** HAU reprints the 1977 chapter, and the card gives both paginations. Intellect may prefer '(Pitt-Rivers [1977] 2012: 513)'.
