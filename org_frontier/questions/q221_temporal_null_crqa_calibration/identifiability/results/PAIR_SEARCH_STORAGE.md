# Storage of the bounded-search record

`pair_search.json` (731,681 bytes) is no longer committed. In its place is `pair_search.json.gz` (24,174 bytes),
a deterministic gzip of the **identical bytes**: level 9, mtime 0, no embedded file name.

- **Content checksum (raw JSON SHA-256):** `7c54d45b690081003c836b696d6d63014aa5428a1d8221449a3ba2c75a58ba13`.
  This is the same value as before compression, and `../pair_search_data.py` checks it on every load.
- **Restore the plain JSON**, for scripts and documents that refer to `results/pair_search.json`, such as
  `independent_audit/screen_all_candidates.py` and `screen_verified_marginals.py`:
  ```
  python -m org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.pair_search_data --restore
  ```
  The restored file is git-ignored.
- **Verify:** `... pair_search_data --check`, or the test `identifiability/test_pair_search_data.py`.
- **Regenerate from scratch:** `python -m ...identifiability.pair_search`. It is deterministic and takes
  about 290 s; it writes the `.gz` through `pair_search_data.save`.
