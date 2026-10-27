---
citekey: uis2026adult
title: "Adult illiterate population and adult literacy rate, 15+ years (February 2026 Data Release)"
authors: UNESCO Institute for Statistics
year: 2026
type: web
doi: null
venue: UIS public data API / UIS Data Browser (indicators ILLPOP.AG15T99, ILLPOPF.AG15T99, LR.AG15T99 and sex variants)
source_basis: full-text
pages_read: "all records in the saved world series (SDG: World, 1989-2024) and the saved 2024 regional query; the indicator metadata served with them"
source_url: https://databrowser.uis.unesco.org/
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/F/uis_world_series.json
sha256: 174e4bae83b3d7915ca913b91dd14df69a321957381e2c89c35e0f5e13cd6ee4
manuscript_lines: [109]
ledger_rows: [P4-018, P4-021, P4-022]
verified: corrected
written: 2026-10-14
---

Text note: I read two API responses saved by the arm on 2026-10-13: `uis_world_series.json` (above) and
`uis_2024.json` (same folder, sha256 1e19a3fc44667d62e5b75e1661ee962e0dad0c31e019aa92d2b502d8b0acbbdc). I did
not re-query the API. The metadata in the series file gives "lastDataUpdate: 02/09/2026" and "February 2026
Data Release". I computed the shares below with Python from the saved records.

## Summary
The data set is the UNESCO Institute for Statistics' series on adult (15+) literacy, as served by its public API
in the February 2026 release. For the "SDG: World" aggregate it gives the adult literacy rate yearly from 1989
to 2024 and the number of illiterate adults from 1993 to 2024, by sex. The indicator metadata define the
illiterate population as "persons that cannot read and write". Illiteracy is "typically measured according to
the inability to comprehend a short simple statement on everyday life". The metadata list sources (censuses,
household and labour-force surveys) and limitations: national definitions differ, some countries equate no
schooling with illiteracy, and some data are self-reported. In 2024 the world had 739,139,712 illiterate
adults, 466,257,152 of them women, a female share the series reports as 63%. The adult literacy rate was
87.74%. The world rate rose from 74.63% in 1990 to 81.12% in 2000 and 85.96% in 2015. The illiterate count fell
from 947,961,216 in 1993 to 801,852,096 in 2000.

## Key facts it relies on
- ILLPOP.AG15T99, SDG: World, 2024: 739,139,712; ILLPOP.AG15T99.F: 466,257,152; ILLPOPF.AG15T99: 63
  (`uis_2024.json`). My arithmetic: 466,257,152 / 739,139,712 = 63.08%.
- LR.AG15T99, world: 74.63 (1990), 81.12 (2000), 85.96 (2015), 87.74 (2024). Illiteracy rate (100 minus
  literacy): 25.37%, 18.88%, 14.04%, 12.26%.
- Relative fall in the illiteracy rate 1990-2000: (25.37 - 18.88) / 25.37 = 25.6% (my computation).
- Definition: "The number of persons that cannot read and write. Illiteracy is typically measured according to
  the inability to comprehend a short simple statement on everyday life" (metadata, "Number of illiterates").
- Limitations: "Some countries apply definitions and criteria for literacy which are different from the
  international standards, or equate persons with no schooling to illiterates, or change definitions between
  censuses. Some assessments of literacy may also rely on self-reporting" (metadata).
- Qualifiers: the illiterate counts for 1993-1999 carry "UIS_EST"; the world literacy-rate records carry no
  qualifier (my tally of the saved records).

## Critical notes from the literature
- The world series has a step between 1996 and 1997: the literacy rate rises 2.0 points (77.30 to 79.30), against
  about 0.45 a year in 1990-1996; the next year adds 1.22 more, then 0.38 and 0.22; and the count drops by 72.7 million. Facet F found no explanation for it
  (`literature/facets/F_promise_and_campaigns.md`:250). By my arithmetic, that one-year step is about 31% of the
  1990-2000 fall in the illiteracy rate (2.0 of 6.49 points). The "about a quarter" figure may partly reflect a
  revision or series break, not only change on the ground.
- The ledger notes that line 109 gives no end year for "from 25.4 to 18.9 percent" (2000) and that Jomtien set its
  target per country, so the world rate is the paper's yardstick, not the Framework's (`review/v3/ledger_parts/
  P4.md`, P4-018).
- The UIS definition is a census or survey yes/no on a simple statement, often self-reported, not a tested skill
  (F:250). The 2015 GMR Summary reports that direct assessment finds more adults deficient than self-declaration
  (UNESCO 2015, p. 29; card `unesco2015efa`).

## Key topics covered
adult literacy rate, illiterate population, world and regional aggregates, sex disaggregation, literacy definition and measurement, data limitations, time series 1989-2024

## Where the manuscript uses it
- v2 line 109: "The world rate fell by about a quarter, from 25.4 to 18.9 percent (UNESCO Institute for Statistics,
  2026)." World illiteracy 25.37% (1990) to 18.88% (2000); relative fall 25.6%. **holds** for the numbers; the
  sentence omits the years 1990 and 2000, and the 1996-97 step is a caveat.
- v2 line 109: "In 2024, 739 million adults could not read and write a simple statement, 63 percent of them women
  (UNESCO Institute for Statistics, 2026)." 739,139,712 and 63% (`uis_2024.json`). **holds**; "a simple
  statement" conflates the definition ("cannot read and write") with the usual measure ("comprehend a short
  simple statement"), which is harmless.
- Reference-list entry (v2 line 383): "February 2026 data release [Data set]". Matches the metadata
  ("February 2026 Data Release", last update 02/09/2026). **holds**.

## Verifier notes
- Recomputed both sha256s (series and `uis_2024.json`): match. Recomputed from the saved records: 2024 world 739,139,712 illiterate adults, 466,257,152 women, ILLPOPF 63; LR 74.63 (1990), 81.12 (2000), 85.96 (2015), 87.74 (2024); relative fall in illiteracy 1990-2000 25.58%. All match the card.
- Metadata definition, limitations, data sources, "February 2026 Data Release" and lastDataUpdate 02/09/2026 confirmed verbatim; UIS_EST qualifiers on 1993-1999 counts only, none on the literacy rate, confirmed.
- Corrected a critical note: the card said the 1996-97 step stood against "about 0.45 a year either side". The series gives about 0.45 a year for 1990-96 but 1.22 for 1997-98 (then 0.38, 0.22), so "either side" was wrong. The 2.0-point step, the 72.7 million drop and the 31% share are right.
- Uses at line 109 (both sentences) and the reference entry: verdicts confirmed. Date 2026-10-14.
