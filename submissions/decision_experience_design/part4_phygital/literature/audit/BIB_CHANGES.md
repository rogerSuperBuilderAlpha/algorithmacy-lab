# Proposed bibliography changes (Part 4) — for the author

*Written by Claude (lead session), 2026-10-04. Nothing here is applied: the facet `.bib` files are the record, and no file in another arm was edited.*

## 1. Merge decisions

`literature/merge_bibs.py` built `references.bib` from the facet bibs in the order A, B, C, D, E, F, G, X: 320 facet entries, 292 kept. It dropped these 28 as duplicates by key or DOI. Where two facets used different keys for one work, the facet `.md` that lost still cites its own key; a draft must use the kept key.

| dropped key (facet) | kept key (facet) | DOI | reason |
| --- | --- | --- | --- |
| `mele2021smart` (B) | `mele2021smart` (A) | 10.1016/j.jbusres.2020.09.004 | same key |
| `zheng2025phygital` (E) | `zheng2025phygital` (A) | 10.1016/j.tmp.2025.101402 | same key |
| `wilsonnash2026noapp` (E) | `wilsonnash2026captivity` (A) | 10.1002/mar.70098 | same DOI |
| `kim2026when` (E) | `kim2026shadow` (A) | 10.1080/10447318.2025.2558022 | same DOI |
| `baronyelles2019designing` (F) | `baron2019designing` (B) | 10.1080/09654313.2018.1562651 | same DOI |
| `stamatopoulos2021menu` (G) | `stamatopoulos2021menu` (B) | 10.1287/mnsc.2019.3551 | same key |
| `soutjis2017ethnography` (G) | `soutjis2017ethnography` (B) | 10.1016/j.jretconser.2017.08.009 | same key |
| `bitner1992servicescapes` (X) | `bitner1992servicescapes` (B) | 10.1177/002224299205600205 | same key |
| `kotler1973atmospherics` (X) | `kotler1973atmospherics` (B) |  | same key |
| `rosenbaum2011expanded` (X) | `rosenbaum2011expanded` (B) | 10.1108/09564231111155088 | same key |
| `mari2013servicescape` (X) | `mari2013servicescape` (B) | 10.1080/02642069.2011.613934 | same key |
| `kang2019smart` (X) | `kang2019smart` (B) | 10.1111/dmj.12051 | same key |
| `harris2010online` (X) | `harris2010online` (B) | 10.1108/08876041011040631 | same key |
| `hollands2017tippme` (X) | `hollands2017tippme` (B) | 10.1038/s41562-017-0140 | same key |
| `mele2023phygital` (X) | `mele2023phygital` (A) | 10.1007/s43039-023-00070-7 | same key |
| `batat2022phygital` (X) | `batat2024phcx` (A) | 10.1080/0965254x.2022.2059775 | same DOI |
| `brochado2026phygital` (X) | `brochado2026phygital` (A) | 10.1108/jsm-09-2025-0709 | same key |
| `lyons2019phygital` (X) | `lyons2019phygital` (A) | 10.1075/ll.18025.lyo | same key |
| `mele2024agencement` (X) | `mele2025agencement` (A) | 10.1108/josm-03-2023-0113 | same DOI |
| `weiser1991computer` (X) | `weiser1991computer` (D) | 10.1038/scientificamerican0991-94 | same key |
| `greenfield2006everyware` (X) | `greenfield2006everyware` (D) |  | same key |
| `latour1992missing` (X) | `latour1992missing` (C) |  | same key |
| `lessig2006code` (X) | `lessig2006code` (C) |  | same key |
| `barlow2026phygital` (X) | `barlow2026phygital` (A) | 10.1177/02761467251414839 | same key |
| `mertens2022effectiveness` (X) | `mertens2022effectiveness` (B) | 10.1073/pnas.2107346118 | same key |
| `grant2025nudging` (X) | `grant2025nudging` (B) | 10.1080/10408398.2025.2530548 | same key |
| `purohit2026deception` (X) | `purohit2026deception` (F) | 10.48550/arxiv.2603.03218 | same key |
| `mele2020smart` (X) | `mele2021smart` (A) | 10.1016/j.jbusres.2020.09.004 | same DOI |

## 2. Year differences between the bibliography and Crossref

Crossref's date is the print issue where one exists. The house rule is that the version of record governs.

| key | bibliography | Crossref | note |
| --- | --- | --- | --- |
| `grant2025nudging` | 2025 | 2026 | Online 2025; issue 2026 |
| `kandampully2022linking` | 2022 | 2023 |  |
| `akrich1987comment` | 1987 | 2010 | The DOI is the 2010 reprint; 1987 is the original. Keep 1987 and cite the reprint as the copy read |
| `suchman2007reconfigurations` | 2007 | 2006 |  |
| `suchman1994categories` | 1994 | 1993 | Journal volume 2 is dated 1993/1994 |
| `buell2020lastplace` | 2020 | 2021 |  |
| `althenayyan2024notall` | 2024 | 2025 |  |
| `adey2004secured` | 2004 | 2002 | The PDF read says 2004; Crossref says 2002. Unresolved |
| `jensen2023bench` | 2023 | 2024 |  |
| `jensen2017dark` | 2017 | 2018 |  |
| `sunstein2019sludge` | 2019 | 2018 |  |
| `sunstein2020audits` | 2020 | 2022 |  |
| `herd2018administrative` | 2018 | 2019 |  |

## 3. Corrections to records in other arms (not applied)

Facet A resolved these against Crossref. The hospitality arm's files are unchanged.

| Record in `submissions/hospitality_phygital/` | What Crossref gives |
| --- | --- |
| Mameli 2026: bib and card disagree on the first author's given name | Elisa |
| Zheng 2025: bib and card disagree on all three given names | Chunhui, Yunbo, Jia |
| Mosca: 2025 on the card, 2026 in the bib | 2026 |
| Padigar: 2024 on the card, 2025 in the bib | 2025 |
| Mele and Russo-Spena, architecture paper: key says 2022, card says 2021 | 2022 |
| Corinaldesi 2025: given name Ludovica in the bib | Luca |
| Roederer 2026: co-authors | Facet A reports the bib's co-author names are wrong; see its entry |
| Weaver 2025 | 2026, volume 16(2) |
| Kim, Chung and Chung 2025 | 2026 |
| Wilson-Nash 2025 | 2026, *Psychology & Marketing* 43(5), 974–985 |
| Batat, PH-CX: 2024 in the hospitality bib | Online 2022; the issue is 32(8), 2024. Facet A keeps 2024 (`batat2024phcx`); facet X used 2022 |

Elsewhere: the card `org_frontier/research/qualitative/literature/cards/xiang2025judging.md` points to a PDF that facet E found to be a Deliveroo annual report, not the paper.

## 4. Records with no Crossref entry

- Kotler 1973, "Atmospherics as a marketing tool", *Journal of Retailing* 49(4): no Crossref record. The scan's own header reads "Volume 49 Number 4 Winter 1973-1974", pages 48–64. OpenAlex dates it 1974.
- `purohit2026deception` (arXiv) and `jensen2020atmospheres` (HAL) carry DOIs registered outside Crossref.
- Chalmers 2003 (Eurowearable): Crossref lists Chalmers alone; the paper names Chalmers, MacColl and Bell. Facet D follows the document.
## 5. Field changes (facet bibs; not applied)

## dhs2025biometricrule (facet G)
- old: `author = {{Department of Homeland Security, U.S. Customs and Border Protection}}`. `build_references.py` splits authors on " and " before it checks for braces, so the name renders as "Department of Homeland Security, U.S. C., & Protection, B."
- new: either write the author as `{{Department of Homeland Security}}` with the component agency in the title or note, or change the script to split only on " and " outside braces. The same fault is in the Part 2 and Part 3 copies of the script.

## 6. Keys that differ between facets for one work

Facet T and facets E, F and X cite keys that the merge dropped. A draft must use the kept key.

| dropped key | kept key |
| --- | --- |
| `wilsonnash2026noapp` (E) | `wilsonnash2026captivity` (A) |
| `baronyelles2019designing` (F) | `baron2019designing` (B) |
| `mele2024agencement` (X) | `mele2025agencement` (A) |
| `batat2022phygital` (X) | `batat2024phcx` (A) |
| `kim2026when` (E) | `kim2026shadow` (A) |
| `mele2020smart` (X) | `mele2021smart` (A) |

Three facets also disagree on read status for sources another facet read in full: Wilson-Nash (A full, E abstract), Baron 2019 (B full, F abstract), Bitner 1992 and Kotler 1973 (B full, X not reached). The facet that read the source governs.
