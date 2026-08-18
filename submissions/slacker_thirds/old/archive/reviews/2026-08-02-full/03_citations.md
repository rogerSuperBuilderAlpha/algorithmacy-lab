# Full review, axis 3 — citations

**Target:** `chapter/chapter_v3.md` at 22ecb08: 77 notes, three-part bibliography (60 works cited, 3
cases, 23 primary/documentary sources).
**Method:** scripted both-directions checks (body keys ↔ note definitions; notes ↔ bibliography;
per-section alphabetization), Crossref resolution for every DOI printed in the chapter, and quote
fidelity via the axis-2 primary retrievals.
**Verdict: minor revisions** — one missing bibliography entry, one title misspelling, two ordering
faults, one missing note, plus small consistency items.

## 1. Mechanical results

- **Note keys: clean.** 77 keys in the body, 77 definitions, every key resolves both directions, no
  duplicates, and the notes appear in body first-use order.
- **Bibliography → notes: clean.** Every bibliography entry's work is cited in at least one note. The
  Möhlmann orphan panel 3 found (D2) is gone.
- **Notes → bibliography: one failure. Rosenfeld, Thomas, and Hausen (notes 23–24) has no
  bibliography entry.** Surgical: add under Works cited, after Rosenblat & Stark — "Rosenfeld,
  Michael J., Reuben J. Thomas, and Sonia Hausen. 'Disintermediating Your Friends: How Online Dating
  in the United States Displaces Other Ways of Meeting.' *Proceedings of the National Academy of
  Sciences* 116, no. 36 (2019): 17753–17758." (DOI 10.1073/pnas.1908630116 in the project record.)
- **Alphabetization: two faults.** In Primary and documentary sources, Criterion Collection is filed
  before Canby. And "A $23,000 Film Is Turning Into a Hit" is filed as if under "$" (after Howe);
  Chicago files numerals as spelled, so the headline belongs under "Twenty-three," after Turan.
  The apparent misorders the script also flagged (Poulaki 3-em-dash pair, the two Smith entries, the
  two Census entries) are correct on inspection — same-author works sort by title, and Essex precedes
  Henderson as second author.

## 2. Entry-level faults

**CI1. The Simmel 1908 title is misspelled in the bibliography.** "Sociologie: Untersuchungen über
die Formen der Vergesellschaftung" — the German title is *Soziologie*. Note 13 has it right.
Surgical.

**CI2. The *Film Comment* sentence in §7 has no note** (axis 2, CT5). The tip half is verifiable in
the Criterion reprint of Pierson; the relatives call is Macor's, page unconfirmed. Add the note with
the page marked for print confirmation.

**CI3. The *Papachristou* pin cites are wrong** (axis 2, CT6). "at 156–58, 164" → "at 162, 164, 170,"
verified against the official U.S. Reports PDF this pass.

## 3. DOI and record checks

Every DOI printed in the chapter resolves and matches: Gagrčin et al. (28.1: 423–447, 2026),
Oeldorf-Hirsch & Neubaum (27.2: 681–701, 2025), Brodsky et al. (12.3: 43–57, 2020), Kendall (75.1:
41–46, 2021), Anikina (119–138). One anomaly for the record: Crossref's deposit for Anikina carries
"volume 13," which contradicts the publisher's own issue record (*Digital Culture & Society* 7,
no. 2, 2021 — also encoded in the DOI string dcs-2021-**07**02**06**). The chapter's 7(2) is right;
no change.

The three references the reframe pass added to `literature/references.md` (Anikina, Kendall,
Althouse) all carry verification records in `research/gap_film_theory.md`, satisfying the standing
rule. Althouse's post, the Savlov interview, the Amazon policy page, and the Criterion cast page were
re-verified live or via Wayback this pass (axis 2). `literature/references.md` remains the month-stale
file `outline_v3.md` says must be rebuilt rather than patched; that rebuild stays an author-side task
and is out of this pass's scope.

## 4. Quote fidelity

Checked every quotation with a retrievable source (axis 2 details). Two faults, both already logged
there: the Amsterdam translation drift (CT2) and the Bengesser statistic (CT1, a paraphrase rather
than a quotation). Two borderline renderings, flagged only:

- **Loschky et al.** The body quote ends "irrespective of their viewing condition." — the source
  sentence continues "or whether they made the critical inference." Ending a quotation mid-sentence
  without ellipsis is defensible Chicago practice and the omission does not change the sense; leave,
  or add an ellipsis at press.
- **Slugan.** The chapter quotes "little debate on this matter among film scholars in general" and
  paraphrases the rest of the endnote. The endnote's other half (the debate is "very lively among
  those applying analytic philosophy to film") is carried by the chapter's own "I take the
  philosophers' minority position inside film studies." Fair.

## 5. Consistency items

- **Small & Gose lacks the abstract-only mark** that Boom and Poulaki's *Screen* article carry. The
  body claim is supportable from the abstract, but the convention should be uniform. Surgical: append
  "*Abstract consulted only.*" to the entry.
- **Variety entry has no date** ("Variety Staff. 'Slacker.' *Variety*."). The research record is
  genuinely ambiguous (archived under 31 December 1990; the page's own crew block says "Extract of a
  review from 1991"), and note 4 discloses the trade-press gap. Leave for the author; do not invent a
  date.
- **Bordwell 1985 p. 62 is convergence-verified only** and note 38 does not say so, unlike the
  chapter's practice for Moretti (note 44) and Feld (note 18). Optional one-clause disclosure;
  the page is already on the author's library list.
- Live/database sources (AFI, Box Office Mojo, Criterion, Amazon, Althouse) carry URLs and access
  dates where the chapter cites the live page. The Savlov and Walters *Austin Chronicle* entries cite
  the dated article, which needs no access date. T5 (archive the Amazon page to the Internet Archive
  before press) remains open and author-side.
- Lettered note keys (11a, 18a, 20a, 47a, 71a) will need renumbering at press; mechanical, and
  contingent on the collection's citation style (editor query item 3). No action now.

## 6. What this axis is not judging

Whether the right sources are cited for the argument (axis 1), the truth of the claims they support
(axis 2), prose (axis 4).
