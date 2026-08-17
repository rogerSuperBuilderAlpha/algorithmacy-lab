# Hegel-series source library

The consolidated, verified research substrate for the nine-post Hegel/coordination Substack series. Built by
the round-3 research pass (Fable grounding + Opus adversarial verification of all nine papers, workflow
`wf_ad0ba178`, 2026-07-16) and collated by Opus. The rewrites of the essays draw from this library rather
than re-deriving sources per post.

## What's here

- **`cards/<citekey>.md`** — one verified card per source (every pinned Hegel edition, every secondary, the
  IIT papers). Each card: YAML frontmatter (citekey, title, authors, year, doi, `edition_pin` for the Hegel
  editions, `used_by_posts`, `verified`, `source_basis`, `generated_run`) + four sections — Summary · Key
  facts / verified quotes with loci · Critical notes & threats · Which posts cite it, for what. Reuses the
  card schema from `org_frontier/research/`.
- **`digests/postN.md`** — the per-paper grounding digest the rewrite works from: claim (at the correct
  altitude), pinned primary passages, secondary anchors/threats, new scholarship, lab receipts with verified
  numbers, refutation condition, the guard check, the verification corrections to apply, and the gates.
- **`research/postN.digest.json`** — the raw structured Stage-1 output (grounding digest + adversarial
  verdict) behind each `digests/postN.md`. Source of truth; the markdown digests are generated from these.
- **`RECEIPTS.md`** — the post → lab-receipt index: every computed figure a post leans on and the repo file
  behind it, re-verified against the repo. The numbers here are canonical; the rewrites must match them.
- **`REFERENCES.md`** — the APA-7 master bibliography for the series, with the pinned editions noted.
  Consistent with what `../check_editions.py` enforces.
- **`CARDS_INDEX.md`** — generated table of all cards (`build_index.py`).
- **`../literature/DEEP_RESEARCH_ROUND3.md`** — the prose synthesis memo for this round (terrain, threats,
  new scholarship, residue), continuing `DEEP_RESEARCH.md` and `DEEP_RESEARCH_ROUND2.md`.

## Guards baked into every card and digest

- **Homology, not identity.** The bridge is "same boundary, different instrument." Never "Hegel anticipated
  Φ."
- **Never demote Φ/IIT.** Not a calculator, not decorative, not unnecessary; modest ≠ self-defeating.
- **Pinned editions:** PR = Wood/Nisbet 1821/1991a · EL main = Brinkmann/Dahlstrom 1830/2010a · EL Zusätze =
  Hackett 1830/1991b · PhG = Pinkard 1807/2018 · SL = di Giovanni 1816/2010b · recognition family Brandom
  2019 / Pinkard 1994 / Pippin 2008 / Honneth 1995 (Polity).

## Regenerating

```
python build_index.py           # rewrite CARDS_INDEX.md from the cards
python build_index.py --check   # CI: fail if the index is stale or a card is malformed
python ../check_editions.py     # audit the posts' bibliographies against the pinned editions
```

The `digests/` and `RECEIPTS.md` are generated from `research/*.digest.json`; re-run the generator in the
scratchpad if the raw digests change.
