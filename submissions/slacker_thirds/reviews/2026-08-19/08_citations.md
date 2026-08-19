# Seat 08 — citations and provenance

**Provenance of this file.** The Fable seat assigned here terminated twice on API spend limits, the
first time before writing anything, the second after reporting only that Reich had been verified. No
review file survived either run, and **nothing from those runs is reported here**. What follows was run
by the orchestrator directly, with the same verification rule the brief imposes on every seat. It is
narrower than a full seat: it covers the sources with the highest provenance risk and the sources the
other seats did not reach, and it says plainly where it stopped.

**Manuscript:** `chapter.md`, pinned at `db5468d`. 39 notes, 52 bibliography entries.

## 0. Word-budget impact

| # | Change | Class | Body Δ |
| --- | --- | --- | --- |
| C1 | Note 19: restore or mark Simmel's truncated clause | note-only | 0 |
| C2 | Note 36: "the cut" → "the camera" | note-only | 0 |
| C3 | Bibliography: refile Ajunwa; head the film entry as Filmography | apparatus | 0 |

**Seat total: 0 body words.** Every repair this seat proposes is apparatus.

## 1. Title block

Citation and provenance verification, for a Bloomsbury collection chapter in Chicago with endnotes.
Standpoint: the reader who checks quotations against sources and asks, of every quoted sentence, *who
actually wrote it*. The three real errors in this chapter's history were all provenance faults, not
mechanical ones, and none was caught by a reviewer.

## 2. Step 0 — register and bar

Register confirmed: first-person film-studies chapter, Chicago endnotes. Nothing in this seat's scope
touches voice. Judged hard: quotation fidelity character by character, attribution of quoted sentences
to their actual authors, and page pins.

## 3. Part 1 — findings, ranked by damage

### F1. Note 19 silently truncates Simmel, and the dropped clause is one the argument wants. VERIFIED.

Note 19 quotes *Soziologie* (1908), 321, ending at "eine besonders günstige Konstellation für die
Verbindung ist." Retrieved from the first-edition scan (archive.org `soziologieunter00simm`, via curl
with a browser user-agent — WebFetch is blocked from archive.org). Simmel's sentence continues:

> …eine besonders günstige Konstellation für die Verbindung ist, **insbesondere wo es sich um
> ausgedehnte Kreise handelt**.

"Especially where extended circles are concerned." The chapter is *about* a city-scale collective, so
the dropped clause narrows Simmel's thesis in precisely the direction the chapter needs. Restore it or
mark the trim with an ellipsis; leaving a silent truncation in a note whose whole purpose is philological
exactness is the one place this chapter looks careless. The same page confirms both examples in altered
form, as note 16 now correctly says: "Gefahr, die immer drohte" and "der weltumfassende Gott des
Christentums."

### F2. Note 36 carries retired vocabulary. VERIFIED. (Reported independently by seats 01, 02, 03, 04, 05.)

"…no retrieved source pairs the city as reach with **the cut** as selection." A grep across the entire
body returns zero instances of "the cut"; the chapter says "the camera" throughout, deliberately, since
hand-offs occur inside single takes. This note is the last surviving instance in the file. One word.

### F3. Bibliography filing. VERIFIED, mechanical.

Ajunwa is filed after Amazon and Austin Film Commission; alphabetically it precedes both. The *Slacker*
entry sits unheaded at the end after Warner, out of sequence — it wants a Filmography head, as earlier
versions of this chapter carried.

## 4. Part 2 — seat-specific audit

### Bucket A — author-only, no effort spent

Berg, *Film Criticism* 31, 24–26. Whether *Slacker* appears in Bordwell's chapter filmography, 245–250.
The Criterion disc items. An optional *Uberland* page reference. One line each, as instructed.

### Bucket B — closed by prior verification, re-checked only

Simmel p. 103/p. 321 and the 1902 *AJS* serialization: the chapter's current text still says what the
verified version said, with the exception of F1. Note 4's "baton-passing" attribution: **re-verified
below and correct.** Note 16's "altered form": correct, and confirmed against the 1908 page. No use of
the Stone "movement of these films" phrasing as Stone's prose appears anywhere in the chapter.

### Bucket C — live verification performed this session

| Source | Note | Claim checked | Result |
| --- | --- | --- | --- |
| Reich, *Yale LJ* 73 (1964) | 26 | "by procedures which, in varying degrees, represent short-cuts that tend to augment the power of the grantor at the expense of the recipient," **at 751** | **VERIFIED** verbatim; pin exact. Full sentence begins "The granting, regulation, and revocation of government largess is carried on by…", so the chapter's "Reich wrote about government largess" is right. |
| Reich, *Yale LJ* 73 | 28 | "should no longer be tolerated," **at 783** | **VERIFIED** verbatim; pin exact. Context: "The denial of any form of privilege or benefit on the basis of undisclosed reasons should no longer be tolerated." The chapter's paraphrase is accurate. |
| Stark & Pais, *Sociologica* 14.3 | 29 | "the behavior of providers and users, enrolling them in the practices of algorithmic management without managerial authority having been delegated to them," **at 49** | **VERIFIED** verbatim; printed folio 49 confirmed. |
| Stark & Pais | 29 | "whereas for markets the verb is contract, the verb for hierarchy is command, and for networks it is collaborate. By contrast, platforms co-opt," **at 48** | **VERIFIED** verbatim; printed folio 48 confirmed. |
| Małecka, *Text Matters* 5 | 4 | "fluid camera and a kind of 'baton-passing' among the characters" is **Macor quoted in Małecka**, at 191 | **VERIFIED.** Małecka's text reads: "Using 'the fluid camera and a kind of "baton-passing" among the characters as they [run] into one another' (Macor 96)". The attribution is correct, Macor's page 96 is correct, and the quote sits on printed page **191**. This is the provenance fault the gap-fill pass caught, and it has stayed fixed. |
| Małecka | 5 | "unite by unanimously doing nothing," at 194 | **VERIFIED** verbatim ("Linklater's protagonists unite by unanimously doing nothing"); printed folio **194** confirmed. |
| Parker & Pratt, SEP "Josiah Royce" | 24 | Authors, and revision date **January 15, 2026** | **VERIFIED.** Entry reads "First published Tue Aug 3, 2004; substantive revision Thu Jan 15, 2026," authored by Kelly A. Parker and Scott Pratt. §2.2.2 exists ("Theory of Community") and treats communities of memory and hope. |
| Simmel, *Soziologie* (1908), 321 | 19 | German quotation and both examples | **VERIFIED**, with the truncation at F1. |

### Mechanical apparatus — clean, confirmed once

39 note markers, 39 notes defined, no marker used twice, no note defined and unused, no note used and
undefined, first-use order strictly sequential 1–39. Five three-em dash continuations, all following a
same-author entry. All 20 dialogue quotations resolve against `sources/transcript.md`; the 23 body
quotations that do not resolve are scholarly, legal, or web sources, which is correct. No fabricated
quotation anywhere in the chapter. This is a clean apparatus and needed only the one pass the brief
allowed it.

## 5. Part 3 — paste-ready revisions

**C1, note 19** — end the German at the sentence's true end:

> …eine besonders günstige Konstellation für die Verbindung ist, insbesondere wo es sich um ausgedehnte
> Kreise handelt.

**C2, note 36** — "the cut as selection" → "the camera as selection."

**C3, bibliography** — move Ajunwa above Amazon; give the *Slacker* entry a `Filmography` head.

## 6. Verdict

**Minor revisions.** Every load-bearing quotation this seat could retrieve is verbatim and every page pin
it could check is exact — Reich twice, Stark & Pais twice, Małecka twice, Parker & Pratt, Simmel. That is
an unusually good result for a chapter with 39 notes, and it reflects the gap-fill pass that preceded it.

- **Single most important fix:** F1. It is the only place where the chapter's own quotation practice
  falls short of the standard the chapter sets, and the restored clause helps the argument.
- **Biggest genuine strength:** the Małecka/Macor attribution. A chapter that quotes a quoter and says so,
  with both pages right, is doing the thing most manuscripts get wrong.
- **The one thing only the author can supply:** the four Bucket A items, and a decision on the Kracauer
  pin if seat 05's addition to note 36 is adopted.

## 7. VERIFY — not adopted, stated as questions

- **Feld, *AJS* 86 (1981), at 1016** — "will tend to become interpersonally tied and form a cluster."
  `UNVERIFIED — do not adopt.` JSTOR is paywalled and the phrase did not appear in the open citing
  literature I could reach. The quotation is widely used and almost certainly right; it is simply
  unconfirmed **by me**, and the brief forbids reporting an unverified check as a finding.
- **Ciafone, *IJoC* 8 (2014), at 2683n3** — `UNVERIFIED`. The IJoC article URL I tried returned 404. This
  matters slightly more than the others because note 13 uses Ciafone to hedge the Bordwell-filmography
  gap that is itself a standing author task.
- **Kracauer, *Theory of Film*** — if seat 05's note 36 addition is adopted: the wording "a region where
  the accidental prevails over the providential" is confirmed verbatim, but sources place the passage at
  **p. 301**, not the cited 62–63. `Pin UNVERIFIED — check the edition before press.`
- Not reached this session, all `UNVERIFIED`: Royce 1913 vol. 2 at 2:45–46, 2:50, 2:60–61, 2:67, 2:68;
  Kegley 102–103; Viljoen; Strawson; Marlovits; Price; Ramirez; Soldani; Tröhler; Barns; Duranton & Puga;
  Warner 62ff; Ajunwa; Vallas & Schor 282; Neuberger; Amazon BSA §3. Seat 03 covered the Uber pages, the
  three EU instruments, the RDU report, and Rosenblat & Stark; seat 01 covered Linklater, Walters, and
  Gaughen; seat 04 covered Bizarro. The remainder is genuinely unchecked.

## 8. Closed-item re-check

Items 12, 13, 14 (the three gap-fill provenance corrections): **Hold** — 12 re-verified against Małecka
directly, 13 confirmed absent, 14 confirmed against the 1908 page. Item 19 (note keys unique and
sequential): **Holds.** Item 20 (camera not cut): **Regresses**, in note 36 only. Items 1–11 and 15–18:
**Not this seat.**

## 9. What this seat is not judging

Prose, argument, film fidelity, or collection fit. It did not re-audit the mechanical apparatus beyond
the single confirming pass. It did not spend effort on the four author-only items. And it does not claim
completeness: the VERIFY list above is long, and a pre-press pass should close it.
