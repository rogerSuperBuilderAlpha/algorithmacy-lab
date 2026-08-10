# G0 — audit of CLAIMS.md against the seven dossiers

Run 2026-08-10. Scope: 717 rows in `v4/factbase/CLAIMS.md`, 147 rows in
`v4/factbase/PROCESS_NOTES.md`, checked against
`research/deep/2026-08-01_s1.md` … `_s7.md` and against the per-dossier extracts in
`v4/extract/`. Nothing was edited; this file reports only.

---

## Verdict

**Pass with corrections.**

The merge is sound in its bones. Twenty-four of twenty-nine sampled rows are correct on all
three tests — claim, class, locator — and the two verification traps that would have been
catastrophic came up clean: **every Bordwell 1985 and Chatman 1990 primary-text row is
already at B**, and **no film-content row is rated A or B on the strength of the transcript
or the disc.** The dossiers' own single-lens and abstract-only flags were honoured in 32
places where the extractor wrote the qualifier into the class cell.

What fails is consistency where the qualifier was *absent*. Twelve rows carry a class the
dossier does not support, and in every case an identically-provenanced row elsewhere in the
same file was correctly downgraded — so the errors are omissions of an existing rule, not
disagreements about it. One further row propagates an unverified dossier inference in a form
that could launder a class-D quotation into print.

**Mis-rated rows found: 12 (class) + 1 (claim drift) = 13 requiring action; 4 advisory.**

---

## Part 1 — Sample and verify (29 rows)

Sampled across all seven dossiers, over-weighted to class A (24 of 29 rows are A).

| Row | Class | Dossier basis | Verdict |
|---|---|---|---|
| S1-006 | A | s1:57–62, Pierson via Criterion/Wayback; "All three lenses confirmed every quotation verbatim against a retrieved text" | correct |
| S1-015 | A | s1:167, Canby verbatim, Wayback capture | correct |
| S1-023 | A | s1:134 and 591–592; Macor p. 102 full OCR, Internet Archive | correct |
| S1-053 | A | s1:348–349, AFI cast table, "parsed programmatically by two lenses" | correct |
| S1-055 | A | s1:351–354 and 370; all four divergences and the McCarty entry are in the dossier verbatim | correct |
| S1-065 | C | s1 Absences; Box Office Mojo cited with no URL, no lens, no method | correct |
| S2-018 | A | s2:102, 121–122; Simmel/Wolff OCR retrieved; scope correction reproduced exactly | correct |
| S2-049 | A | s2:296–305; full text word-searched (10,684 words), abstract quoted whole | correct — locator "abstract" but the body *was* retrieved |
| S2-065 | A | s2:384–385, "three lenses ran it independently" | correct |
| S2-095 | B | s2:648, "THE ARTICLE ITSELF WAS NEVER OPENED"; p. 1016 stable across five quoting sources | correct — textbook B |
| S3-013 | A | s3:76–78; two lenses OCR'd 17 leaves at 200 and 250 dpi | correct |
| S3-032 | A | s3 cit. 9; row itself prints the caveat that the sentence was read only in the 2006 working paper | correct |
| S3-073 | A | s3 cit. 15; rows reproduced by all three lenses | correct |
| S3-083 | A | s3:558–559 | correct, but see advisory A3 — the dossier's instruction to "label any printed distance as the chapter's measurement" did not survive the merge |
| S4-009 | A | s4:46–49, "verbatim, at reprint line 679" | correct |
| S4-032 | B | s4:182–186, "No page image was obtained by any lens… convergence across independent citing works" | correct |
| S4-041 | A | s4 cit. 5, "full text retrieved through the Scholar Gateway corpus by two lenses" | correct |
| S4-053 | A | s4:363–367 | **claim drifts from source** — see Trap findings |
| S4-057 | A | s4:401–408; all three lenses retrieved via r.jina.ai, lens 2 diffed clause by clause | correct |
| S5-003 | A | s5:31–34, §1 verbatim from the arXiv PDF | correct |
| S5-102 | A | s5 Absences: "An angle converted the official ballot-pamphlet text… and searched it" | **class wrong (should be C)** — one angle, no corroboration |
| S5-148 | A | s5:705–708, abstract quotations only; interior quotations "could not be verified by any route" | **class wrong (should be C)** |
| S5-155 | B | extract cell: "Bibliographically verified via Crossref but paywalled and not read this pass" | **class wrong (should be C)** — a Crossref record is metadata, not convergence |
| S6-024 | A | s6 cit. 5, quotations verified 3-0 in the UEA accepted manuscript | correct |
| S6-050 | A | s6 cit. 11: "Crossref and the Birkbeck record agree; abstract verified verbatim" — body never retrieved | **class wrong (should be C)** |
| S6-096 | A | s6 cit. 15, "every quoted figure verified 3-0"; locator matches the dossier's corrected pagination exactly | correct |
| S7-056 | A | s7:228; Tzioumakis version of record retrieved past Anubis by three lenses | correct |
| S7-095 | A | s7:411–412; Box Office Mojo "read directly by three lenses; all six cited fields match" | correct |
| S7-122 | A | s7 Absences, Macor p. 104 verbatim; s7 cit. 2 confirms pp. 104, 106–107 by three lenses | correct |

**Sample tally:** 24 correct · 4 class wrong · 1 claim drift · 0 locators wrong or invented.

No invented locator was found anywhere in the sample. Where the dossier gives no page, the
row says so ("NONE," "(page not given by dossier)," "NONE (no pagination available)") rather
than manufacturing one. That is the merge's strongest single feature.

---

## Part 2 — The four traps

### Trap 1 — Bordwell 1985 and Chatman 1990: **clean, no action**

The extractor's report is accurate about the dossier and wrong about the file. s4:710–715
does say:

> "**No page image of Bordwell 1985 or Chatman 1990 was obtained by any angle.** … Every page
> number for those two books rests on convergence across independent citing works, and one of
> them (Chatman 115 vs 116) is not unanimous."

Every row that quotes those two books as primary text already carries B: S4-032, S4-033,
S4-034, S4-035 (Bordwell pp. 53, 62), S4-038, S4-039, S4-040 (Chatman pp. 113, 134), S4-042.
The word "verbatim" appears in S4-039 and S4-040, but each is qualified in the claim cell
itself ("confirmed twice with locator via…", "reconstructed by lens 2 from two continuous
Open Library snippets"), and S4-040 additionally carries the dossier's own "weakest of the
three" note. The A-rated rows in the same neighbourhood are A for the right reason: S4-036
and S4-037 are Schmidt's own retrieved text, S4-041 is Thomson-Jones's retrieved text, S4-043
is Slugan's retrieved PDF. S1-093 and S1-094 (*Poetics of Cinema* p. 215) are D.

**One caveat.** S4-032–S4-035 and S4-038 are class B and therefore writable under the file's
own drafting rule. That is correct by the definitions, but a library check on two pages closes
the whole cluster; the dossier says as much ("One library check closes it," s4:186).

### Trap 2 — the Absences sections: **mostly handled, four rows to fix**

The extractors' formal observation is right. Each dossier's header states that "Twelve claims
went into verification"; the three-lens vote applies to the numbered Findings only, and the
Absences sections carry no vote counts. 114 extracted rows originate in Absences material.
The merge sorted them well: 42 went to PROCESS_NOTES as search records, 35 landed at C, 5 at
D, 2 at X. Eighteen stayed at A.

Of those eighteen, twelve are correctly A because the Absences text itself records retrieval
and the source is separately confirmed elsewhere in the dossier — S7-122/123/124 (Macor and
Pierson, both in the s7 confirmed-citations list with three-lens confirmation), S7-129,
S4-095/097/099, S6-080/081/082/085/090 ("Two field-defining reviews were read in full text and
word-searched"; "Full text of Cohn 2020 contains zero occurrences of…").

Six should move:

- **S5-102, S5-103, S5-104, S5-105** — the Prop 22 cluster. The dossier's own sentence is
  "**An angle** converted the official ballot-pamphlet text of Proposition 22 … to text and
  searched it." One angle, no corroboration, no vote. The file's own precedent is
  unambiguous: seven rows elsewhere were downgraded to C on exactly this ground
  (S1-092, S3-024, S3-045, S3-049, S5-146, S5-151, S6-099). S5-104 is the one that matters —
  it is a *negative* claim about statutory text ("Prop 22 contains no notice-period
  requirement, no written-reasons requirement, and no specified standard for the appeals
  process") that a chapter would print as settled law on a single unreplicated text search.
- **S6-087** — Uzunca and Kas. The dossier mentions the article only inside a parenthesis and
  never records opening it. The extractor's own cell read "A (quoted phrase); C (surrounding
  description)"; the merge kept the A and dropped nothing, so the surrounding description now
  travels at A.
- **S4-096** — Moretti, *Network Theory, Plot Analysis*. Quoted with a page and a URL in the
  Absences section, with no retrieval statement and no lens. Advisory rather than firm: the
  pamphlet is open-access and the quotation is not load-bearing.

### Trap 3 — abstract-only rows presented as verbatim: **six rows, all self-disclosing**

Thirty-two rows (not 33) were downgraded at merge because the extractor's class cell carried a
qualifier — e.g. `A (abstract only — chapter body is D)` → C for S1-040, `A (abstract only)` → C
for S5-077 through S5-080. Thirty-one rows carry an "abstract" or "metadata" locator and remain
at A. Most of those are right: either the body was retrieved as well (S2-049, S3-028/029/031/044/048,
S6-024/030/040/047/051/071/072, S7-002/054), or the claim *is about the metadata* and the record
was consulted directly (S1-033, S2-071, S3-004/022/027/030/047/104, S6-098).

Four are genuinely abstract-only with the qualifier missing:

| Row | Class | Dossier's own words |
|---|---|---|
| S5-038 | A → **C** | s5 cit. 5: "Crossref and Semantic Scholar both return the publisher abstract; every quoted clause verbatim." Body never opened — yet the row characterises the paper as a whole ("present their location-pricing framework as a proposed stylized model … not as a description of what Uber's actual system does"). |
| S5-148 | A → **C** | s5:705–712: "its abstract quotations are verbatim … But the three interior quotations the section wanted … could not be verified by any route." Directly parallel to Cameron 2024 (S5-076–S5-080), all of which are C. |
| S6-050 | A → **C** | s6 cit. 11: "Crossref and the Birkbeck record agree; abstract verified verbatim." |
| S6-070 | A → **C** | s6 cit. 13: "Abstract verified verbatim; the interview count and the sub-element definitions still need the PDF." |

Two further metadata-only rows are rated **B**, which is worse than the abstract cases,
because B licenses drafting:

| Row | Class | Dossier's own words |
|---|---|---|
| S5-155 | B → **C** | "Bibliographically verified via Crossref but paywalled and not read this pass." A Crossref record is metadata, not convergence across secondary sources. Precedent: S5-113, identical situation, was downgraded from `B — Crossref bibliographic confirmation only` to C. |
| S6-102 | B → **C** | "This paper's citation record … is confirmed against the Crossref deposit. Its argument has not been read — Duke University Press returns 403 on every access route attempted." Compare S7-133, the same situation, rated D. |

And one row is B on no evidentiary basis at all:

| Row | Class | Text |
|---|---|---|
| S5-115 | B → **C** | "listed by the dossier as already verified by the project; **no verification method given this pass**." This is not convergence; it is an inherited verdict. It is the shape of failure the rebuild exists to prevent — a verdict recorded upstream and carried downstream unread. |

Mitigation worth recording: every one of these rows carries "abstract," "bibliographic record"
or "Crossref" in its locator or claim cell, so a drafter who reads the row sees the problem
even at the wrong class. The danger is real but second-order.

**Documentation defect.** CLAIMS.md's printed class key reads "`C` second-hand, abstract-only,
or a paraphrase of an unopened source" and does not mention single-lens retrieval — yet the
merge downgraded seven rows for exactly that. The key should be amended to match the practice,
or the practice will drift back.

### Trap 4 — film-content rows: **clean, no action**

No claim about what happens on screen, what a character says, or how a scene is shot is rated
A or B on the film. The two rows that read the film directly — S1-052 (cast crawl from frames
at 1 fps) and S1-057 (tail of the transfer) — are C, with the note "single lens, uncorroborated
(was A)". The transcript row S4-079 is D. S3 states the rule in the dossier's own words: "**No
dialogue line can be quoted as evidence this pass.** … (The project holds its own transcript at
`research/slacker_transcript.md`, which this run could not independently authenticate against a
published source.)"

The A-rated rows that *mention* the film's content are all claims about a retrieved secondary
text — Gaughen's location list (S3-052/053/055), Rosenbaum and Walters in Criterion reprints
(S4-057, S4-065, S4-070), AFI's and Criterion's cast tables (S1-053, S1-055). Each is correctly
framed as "X wrote," not as "the film shows."

One row is misfiled rather than mis-rated: **S1-077** ("The Internet Archive transfer … is
Criterion-sourced, total duration 6043.66 seconds") is a retrieval fact about this research run
and belongs in PROCESS_NOTES.

### The drift finding — S4-053

This is the single most dangerous row in the file, and it is not a class error.

S4-053 quotes Poulaki relaying Bordwell, then adds: *"This is an independent second attestation
of the *Poetics of Cinema* p. 215 passage the chapter already quotes at its note 32."* The
sentence is copied faithfully from s4:365–367, so the merge did not invent it — but it is a
dossier inference, not a source-attested fact, and it is wrong in two ways.

1. **Different sentence.** The chapter's note 32 attaches to *"This isn't a network so much as a
   wiggly, knotted string"* (`chapter/archive/chapter_v2.md:168`). Poulaki quotes the sentence
   *before* it. Poulaki attests an adjacent sentence on the same page, not the quoted one.
2. **Not verbatim.** Poulaki (or the dossier's transcription of her) prints *"the narration
   doesn't bare unexpected connections among them."* The project's own verified reading of
   p. 215 (`research/verification_log.md:12`) has Bordwell writing *"the narration doesn't
   **lay** bare unexpected connections among them."* A word is missing.

The risk: S1-094 — the "wiggly, knotted string" line — is class **D**, "may not be asserted at
all until the author supplies it." A drafter working from CLAIMS.md alone reads S4-053, sees
class A and the phrase "independent second attestation of the p. 215 passage the chapter
already quotes at its note 32," and prints the D quotation as corroborated. That is the exact
laundering mechanism — an upstream gloss propagating unread — that produced the fatal error four
panels missed.

Recommended repair: keep A for Poulaki's own sentence (her dissertation was retrieved and
paginated by two lenses); strike the second sentence of the claim cell or rewrite it as
"Poulaki quotes an adjacent sentence from the same page; it is not the sentence at the
chapter's note 32, and her rendering drops 'lay' from 'lay bare'"; and rate the Bordwell
wording inside it C. The row's provenance note already says "D (Bordwell 2007 itself not opened
by any lens)" — the note is right and the claim text contradicts it.

---

## Part 3 — Judging the separation

Ten rows spot-checked in PROCESS_NOTES.

| Row | Moved out on source | Verdict |
|---|---|---|
| S1-005 | "Section 1 chapter draft, quoted in dossier" | **correct** — a fact about the artifact being rebuilt, not about the world |
| S3-046 | "Dossier synthesis of Donovan et al. and Duranton & Puga" | **correct** — a synthesis, and the row says so |
| S5-095 | "dossier synthesis of S5-092–S5-094" | **correct** |
| S7-023 | "Pierson, in Macor 2010 (page not specified in dossier)" | **FALSE POSITIVE** — verbatim Pierson quotation ("the entire company was poised to collapse") about Orion at the time of the video release. A §7 fact. Caught only because the word "dossier" sits in a parenthetical. |
| S7-024 | same | **FALSE POSITIVE** — "They saw no evidence that *Slacker* should be treated any differently." This is the sentence §7's whole argument about the home-video gate turns on. |
| S5-092 | "Uber marketplace page (unnamed in dossier beyond…)" | **FALSE POSITIVE** — two verbatim quotations from Uber's own marketplace page ("we evaluate nearby drivers and riders in one batch"; "closest doesn't always mean quickest"). A platform fact, class C, chapter-usable with the C caveat. |
| S5-112 | "Ajunwa (source title not given in dossier excerpt)" | **FALSE POSITIVE** — the verbatim *tertius bifrons* definition. §5 and §2 both need it. |
| S6-083 | "Zhang, [first name not given by dossier], and Liu…" | **FALSE POSITIVE** — verbatim quotation plus sample description (N=18, YouTube users aged 60–75). Bears directly on §6's transfer claim. |
| S3-078 | "Macor 2010 / Census sources per dossier's 'how this lands' synthesis" | **FALSE POSITIVE** — Austin's housing stock grew 48.0% (70,427 net units) against 34.6% population growth, 1980–1990. A city fact from Census sources. It is a synthesis of two retrieved sources, not a record of the run. |
| S2-060 | "Obstfeld 2005 (not directly retrieved in this dossier…)" | **FALSE POSITIVE** — "*Tertius iungens* is Obstfeld's 2005 coinage, not Simmel's." A literature fact §2 must not get wrong. |

**Seven false positives in ten.** The filter matched the substring "dossier" wherever it
appeared in a source cell, including inside parentheticals that were *disclaiming* dossier
provenance ("not directly retrieved in this dossier," "page not specified in dossier," "first
name not given by dossier"). That inversion is the whole failure: the parenthetical marks the
row as *more* carefully sourced, and the filter read it as *less*.

Three further rows are borderline and worth a second look: **S5-114** (Rosenblat and Stark's
start page, corroborated by Dubal), **S5-150** (the corrected Rahman and Valentine abstract text
— usable and currently invisible), **S3-082** (the five divergences between Tretter's
transcription and the 1928 Koch & Fowler original, three of them inside the span the chapter
would print — arguably the single most print-critical row now sitting in PROCESS_NOTES).

**The reverse leak.** The separation also ran only one way. Facts about the chapter draft were
moved out of CLAIMS for S1 (S1-005, S1-051, S1-090) but left in for S4, S5 and S6: S4-003,
S4-004, S4-012, S4-013, S4-028, S4-029, S4-031, S5-120, S6-001, S6-049, S6-069, S1-045 are all
statements about `chapter_v2.md`, `draft_v0.md` or the project's own notes, sitting in the fact
base at class A. They are not citable facts about the world either. Thirteen rows, low risk,
but the inconsistency will confuse the drafter about what CLAIMS.md contains.

---

## Rows needing re-rating

**Firm — class is wrong by the dossier's own words (12):**

| Row | Now | Should be | Ground |
|---|---|---|---|
| S5-038 | A | **C** | abstract only; body never opened; row characterises the whole paper |
| S5-102 | A | **C** | single angle, no corroboration |
| S5-103 | A | **C** | single angle, no corroboration |
| S5-104 | A | **C** | single angle; negative claim about statutory text |
| S5-105 | A | **C** | single angle, no corroboration |
| S5-115 | B | **C** | "no verification method given this pass" — inherited verdict, not convergence |
| S5-148 | A | **C** | abstract only; interior quotations unverifiable by any route |
| S5-155 | B | **C** | Crossref metadata only, "not read this pass" |
| S6-050 | A | **C** | abstract verified; body not retrieved |
| S6-070 | A | **C** | abstract verified; PDF still needed for the body |
| S6-087 | A | **C** | no retrieval recorded anywhere in the dossier |
| S6-102 | B | **C** | Crossref deposit only; "Its argument has not been read" |

**Firm — claim drift (1):**

| Row | Action |
|---|---|
| S4-053 | Keep A for Poulaki's sentence. Strike or rewrite the "independent second attestation" clause; it is not the sentence at the chapter's note 32 and the relayed wording drops "lay." Rate the relayed Bordwell wording C. |

**Advisory (4):**

| Row | Now | Suggested | Ground |
|---|---|---|---|
| S6-054 | A | C or A-with-note | "Print the abstract sentence; hold the body quotations" — abstract verified twice, so A is defensible |
| S4-096 | A | C or A-with-note | Absences quotation, open-access source, no retrieval or lens statement |
| S1-077 | A | move to PROCESS_NOTES | a retrieval fact about this research run |
| S3-083 | A | A-with-note | restore the dossier's instruction: "label any printed distance as the chapter's measurement" |

**Return to CLAIMS from PROCESS_NOTES (7 firm, 3 borderline):**

Firm: S7-023, S7-024, S5-092, S5-112, S6-083, S3-078, S2-060.
Borderline: S5-114, S5-150, S3-082.

**Housekeeping:** amend the class key in CLAIMS.md's header to include single-lens retrieval
under C, so the rule the merge actually applied is written down.
