# Reference PDFs (gitignored)

The open-access PDFs for this program's references are acquired locally and **not committed** (`*.pdf` is
gitignored — the corpus is ~1–3 GB across the watch). They are reproducible from
[`../pdfs.manifest.json`](../pdfs.manifest.json), which records, for every reference, its acquisition
status, the open-access source, the exact `source_url`, and a `sha256` of the retrieved file.

To refetch: run the acquisition chain (arXiv → Unpaywall → Europe PMC → DOI content-negotiation →
OA-publisher templates) over `../references.bib`, or pull each `source_url` from the manifest and verify
against the recorded `sha256`. Only open-access sources are used; paywalled full text is never scraped.

The per-paper annotation cards built from these PDFs live in [`../cards/`](../cards/) and are indexed in
[`../REFERENCES.md`](../REFERENCES.md).
