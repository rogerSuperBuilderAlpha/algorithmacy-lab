# Brief: check every claim, quotation and citation in MANUSCRIPT_v4 (2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
`MANUSCRIPT_v4.md` is a new draft that Claude wrote today from facets V1–V6 (`literature/facets/V*.md`) and the
verified v3. You wrote none of it. Earlier rounds found that drafters most often err by turning a reported claim into
a fact, claiming more than the source, cutting a quotation so its sense changes, quoting a source other than the
one cited, or giving a wrong page. You are the check that stops those errors reaching the author.

## For every sentence in your sections that states a fact, quotes, or cites
1. Find the source: the card in `literature/cards/<key>.md` (its `local_path`), the facet record, or the local
   text under `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/**` or
   `/Users/ludwitt/iit-playground/dxd_foundation_local/**`. Open the **source text itself** at the page given; do not
   trust the card's or facet's paraphrase when the text is available. Nadella's post is at
   `~/iit-playground/dxd_foundation_local/nadella_2026-10-10_models_as_insider_risks.txt` (paragraphs P1–P21; the
   manuscript cites them as "para. N").
2. Test: (a) **true** at that page; (b) **not overstated** (hedges kept, reported claims not turned into facts);
   (c) **quotation exact** (normalise whitespace, line-break hyphenation, curly quotes only; ellipses marked; words
   attributed to the source actually read); (d) **page or paragraph right**; (e) **the cited work has a reference
   entry** and the entry matches the card (authors, year, title, venue, DOI).
3. Verdict per sentence: `pass` | `fail-true` | `fail-overstated` | `fail-quote` | `fail-locator` | `fail-ref` |
   `cannot-check (why)`. For each fail give the **exact corrected sentence**, as small a change as possible. Do not
   restyle prose; this is a fact check, not an edit.

## Output
`v4/V4_CHECK_<X>.md`: a table `| § | sentence (first 8 words) | verdict | evidence (source + page) | corrected sentence |`,
then `## Rates`. Write the file as you go so a stop mid-run leaves usable work.

## Rules
- Read only. Do not edit the manuscript or any other file; write only your check file.
- Never put any e-mail address in a header, URL or User-Agent. No paywall bypass; skip Unpaywall. Downloads go to
  `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/v4check/`, untrusted (`pdftotext`; Python with `-I`).
- Return the rates and every fail in one line each.
