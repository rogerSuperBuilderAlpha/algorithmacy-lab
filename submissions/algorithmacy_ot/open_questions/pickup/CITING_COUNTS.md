[Written by a Haiku lookup agent, stage S10]

# Citing-works counts: OpenAlex and OpenCitations

Generated 2026-11-22 by citing/fetch_citing.py (stdlib, one request per second). Union is keyed on lower-cased DOI; OpenAlex records without a DOI are kept as separate rows. "with abstract" and "with OA pdf" are counted over the union rows.

| key | OpenAlex cited_by_count | citing works found (OpenAlex) | (OpenCitations) | union | with abstract | with OA pdf |
|---|---|---|---|---|---|---|
| stark2024 | 147 | 127 | 24 | 127 | 99 | 55 |
| hinds2024 | 42 | 39 | 13 | 39 | 37 | 15 |
| justesen2024 | 53 | 50 | 21 | 52 | 45 | 28 |
| phillips2024 | 17 | 17 | 7 | 17 | 14 | 11 |
| hsu2024 | 26 | 27 | 11 | 28 | 22 | 19 |
| grodal2024 | 22 | 24 | 4 | 24 | 20 | 16 |
| orlikowski2023 | 170 | 157 | 55 | 158 | 130 | 76 |
| scherer2023 | 35 | 32 | 10 | 33 | 28 | 12 |
| racker2024 | 9 | 9 | 2 | 9 | 8 | 6 |
| suddaby2024 | 8 | 8 | 3 | 8 | 8 | 1 |
| patriotta2025 | 5 | 5 | 0 | 5 | 5 | 2 |
| dion2025 | 1 | 1 | 0 | 1 | 1 | 0 |
| schoeneborn2026 | 0 | 0 | 0 | 0 | 0 | 0 |
| cornelissen2024 | 55 | 50 | 22 | 51 | 43 | 10 |

## Request failures

None. Every request returned HTTP 200.

OpenCitations: the COCI v1 endpoint was tried first and the v2 endpoint second; the per-key attempt log is in citing/<key>_opencitations.json. Rows whose DOI came only from OpenCitations take their metadata from an OpenAlex DOI lookup (citing/<key>_openalex_doi_lookup.json); rows with no lookup hit have blank metadata.
Total HTTP requests issued: 47.
