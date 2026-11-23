[Written by Sonnet (claude-sonnet-5-5), stage S15b, 2026-11-23]

# Gap search rerun (S15b)

## 1. Result

**Both rerun sources failed again, so this rerun found no records and adds nothing to `../s14/GAP_SEARCH.md` §2.** The S14 verdict stands unchanged. It stands because the rerun produced no evidence, not because the rerun tested it. The gap in S14 §6 (no Scholar Gateway, no working Semantic Scholar search) is still open.

- **Scholar Gateway** (`semanticSearch`): the tool loaded, and the first call returned `ACCESS_DENIED: Access denied`, as on the first run. I logged it and made no further calls, as instructed.
- **Semantic Scholar Graph API** (`/graph/v1/paper/search`, User-Agent `ot-oq-research/1.0`): every call returned HTTP 429 ("Too Many Requests ... apply for a key for higher rate limits"), 17 calls in all. I waited 4 s between queries and backed off 15, 30, 45 and 60 s inside a query (a further 60 s pause preceded the last call). Three of the 12 planned queries were reached, all four retries each; the run was stopped at query 4 once the 429s showed no sign of lifting. Facets (a)–(e) were queued; none returned a result. The shared unauthenticated pool is the likely cause. A free API key (`x-api-key` header) is the usual fix, and I did not request one.

No record, DOI or quotation is given here, because none was retrieved. Nothing is from memory.

## 2. Query log

| date | source | query | n results | note |
|---|---|---|---|---|
| 2026-11-23 | Scholar Gateway semanticSearch | Do platform users or workers attribute actorhood or responsibility to the digital platform itself? (facet a, topN 10) | 0 | ACCESS_DENIED; source dropped |
| 2026-11-23 | Semantic Scholar paper/search | platform workers attribute responsibility to the platform (a) | 0 | HTTP 429 x4 (backoff 15/30/45/60 s) |
| 2026-11-23 | Semantic Scholar paper/search | users attribution of actorhood to digital platforms (a) | 0 | HTTP 429 x4 |
| 2026-11-23 | Semantic Scholar paper/search | customers blame platform algorithm or worker for service failure (b) | 0 | HTTP 429 x4 |
| 2026-11-23 | Semantic Scholar paper/search | blame attribution gig worker platform algorithm customer (b) | 0 | HTTP 429 x4 |
| 2026-11-23 | Semantic Scholar paper/search | organizationality of digital platforms (d), single probe after a 60 s pause | 0 | HTTP 429 |

Not run (stopped after the 429 run): competence (c) x2, organizationality / collective actorhood (d) x3, follow-ups of Stark & Vanden Broeck 2024 and Schoeneborn et al. 2026 (e) x2, accountability / deflected responsibility x1.

## 3. What would settle it

1. Get a Semantic Scholar API key and rerun the queued facets (query list: scratchpad `queries.txt`, 12 lines), or reconnect Scholar Gateway.
2. Until then, S14's OpenAlex citation snowballs (0 citers of Schoeneborn et al. 2026; 127 of Stark & Vanden Broeck 2024) remain the only follow-up evidence.
