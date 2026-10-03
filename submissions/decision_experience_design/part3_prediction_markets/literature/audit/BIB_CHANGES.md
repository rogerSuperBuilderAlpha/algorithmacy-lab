# Proposed .bib changes (Part 3) — for the author

From `AUDIT_00.md`, 2026-10-03. **Not applied to the facet .bib files**: each needs the author's approval,
matching the Part 1 and Part 2 practice. `literature/references.bib` is a built file and already reflects the
merge decisions in section 1; reverse any of them by editing the facet files and rebuilding.

## 1. Merge decisions made in `references.bib` (518 facet entries, 472 kept)

First-wins merge in the order H, A, B, C, L, M, X, D. 34 same-key repeats dropped. 12 entries dropped because
another key already held the same DOI:

| dropped key (facet) | kept key (facet) | DOI |
|---|---|---|
| cowgill2014corporate (B) | cowgill2015corporate (A) | 10.1093/restud/rdv014 |
| nam2026calibration (C) | le2026decomposing (A) | 10.48550/arxiv.2602.19520 |
| sah2026reddit (C) | sah2026visualizations (B) | 10.48550/arxiv.2608.16814 |
| johnson2025 (L), johnson2025addiction (D) | johnson2025prediction (A) | 10.1111/add.70272 |
| lei2026 (L) | lei2026manufacturing (B) | 10.2139/ssrn.7461319 |
| gandhi2014belief (M) | gandhi2015belief (A) | 10.1093/restud/rdu017 |
| smith2006market (X) | smith2006p2p (M) | 10.1111/j.1468-0335.2006.00518.x |
| franck2010prediction (X) | franck2010bookmakers (M) | 10.1016/j.ijforecast.2010.01.004 |
| levitt2004why (X) | levitt2004gambling (M) | 10.1111/j.1468-0297.2004.00207.x |
| moshrefi2026prices (X) | moshrefi2026parlays (C) | 10.1109/cifer67845.2026.11692409 |
| mellers2014psychological (X) | mellers2014psych (B) | 10.1177/0956797614524255 |

## 2. Duplicates still in `references.bib` (no shared DOI, so the merge did not catch them)

- `ca9_2026assad` and `ca92026assad`; `ca3_2026flaherty` and `ca32026flaherty`; `ca6_2026schuler` and `ca62026orgel`; `ca9_2026bluelake` and `ca92026bluelake`. Proposed: keep the facet L keys.
- `cardozo2026favorite` (X, no DOI) and `cardozo2026flb` (D, arXiv DOI). Proposed: keep `cardozo2026flb`.
- `sah2026prediction` (X, "Sah, S. and others", no DOI) and `sah2026visualizations`. Proposed: keep `sah2026visualizations`.
- `diercks2026macro` (D, SSRN DOI 10.2139/ssrn.6093294) and `diercks2026kalshi` (FEDS DOI). Proposed: keep `diercks2026kalshi`.
- `pew2026may` / `pew2026sep` (D) and `pew2026volume` / `pew2026typical` (X). Proposed: keep the facet D keys, which carry URLs.

## 3. Field changes proposed in facet files

## arrow2008promise (facet A)

Facet A marks it not obtained; facet H read the publisher PDF from Hanson's archive.

- old: read status "not obtained"
- new: read status "full text (https://mason.gmu.edu/~rhanson/PromisePredMkt.pdf)"

## stout1999 (facet L)

Crossref (https://api.crossref.org/works/10.2307/1373070) gives first page 701 only.

- old: `pages = {701--786}`
- new: keep, and confirm the end page against the article before print

## chapkovski2024gamification (facet B)

Crossref gives the issue year 2026; the key carries the online-first year.

- old: key `chapkovski2024gamification`
- new: no key change proposed; cite in text as 2026

## hanson2007logarithmic (facets H, A)

Crossref's issued date is 2012-12-13 (deposit); volume 1(1), pp. 3–15.

- old (facet A before this run): year 2012
- new: year 2007, as facets H and A now record; confirm against the journal's own issue page before print
