"""Build literature/corpus.jsonl from the Scholar Gateway semantic-search result files.

Reads the raw semanticSearch JSON payloads saved by the connector, extracts one record per unique
article (deduped by DOI, then by title), screens to in-boundary empirical-plausible sources, and
writes {slug, title, abstract, year, doi} lines. Standard library only.

    python -m org_frontier.reviews.reproducibility_signaling.build_corpus <results_dir>
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(__file__)

# Non-empirical genres to drop from an empirical-paper corpus (title-cue screen).
DROP_TITLE = re.compile(
    r"\b(a review|literature review|systematic review|meta-analysis|meta analysis|"
    r"research agenda|call for|editorial|commentary|book review|erratum|corrigendum|"
    r"introduction to the special issue|a framework for|toward a theory|conceptual)\b",
    re.I,
)


def slugify(title, year, used):
    base = re.sub(r"[^a-z0-9]", "", (title or "").lower())[:24] or "untitled"
    slug = f"{base}{year or ''}"
    s, i = slug, 2
    while s in used:
        s = f"{slug}_{i}"
        i += 1
    used.add(s)
    return s


def year_of(md):
    for key in ("publicationDate", "publication_date"):
        v = md.get(key)
        if v:
            m = re.search(r"\b(19|20)\d{2}\b", str(v))
            if m:
                return int(m.group(0))
    return None


def main():
    results_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    files = sorted(glob.glob(os.path.join(results_dir, "*semanticSearch*.txt")))
    by_doi, by_title = {}, {}
    records = []
    for f in files:
        try:
            payload = json.load(open(f))
        except (ValueError, OSError):
            continue
        for r in payload.get("results", []):
            md = (r.get("metadata") or {}).get("additionalMetadata") or {}
            doi = (r.get("doi") or md.get("doi") or "").lower().strip()
            title = (md.get("title") or "").strip()
            abstract = (md.get("abstract") or "").strip()
            if not title or not abstract or len(abstract) < 120:
                continue
            if md.get("isRetracted"):
                continue
            key_t = re.sub(r"[^a-z0-9]", "", title.lower())
            if doi and doi in by_doi:
                continue
            if key_t in by_title:
                continue
            if DROP_TITLE.search(title):
                continue
            year = year_of(md)
            if not year or year < 2015 or year > 2025:
                continue
            rec = {"title": title, "abstract": re.sub(r"\s+", " ", abstract).strip(),
                   "year": year, "doi": doi}
            if doi:
                by_doi[doi] = rec
            by_title[key_t] = rec
            records.append(rec)

    # Cap per year to keep the corpus in the ~60-90 target band with an even year spread.
    from collections import Counter, defaultdict
    MAX_PER_YEAR = 8
    records.sort(key=lambda r: (r["year"], r["title"]))
    kept, per_year = [], defaultdict(int)
    for r in records:
        if per_year[r["year"]] < MAX_PER_YEAR:
            per_year[r["year"]] += 1
            kept.append(r)
    records = kept

    used = set()
    for r in records:
        r_slug = slugify(r["title"], r["year"], used)
        r["slug"] = r_slug

    out = os.path.join(HERE, "literature", "corpus.jsonl")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        for r in records:
            fh.write(json.dumps({"slug": r["slug"], "title": r["title"],
                                 "abstract": r["abstract"], "year": r["year"],
                                 "doi": r["doi"]}, ensure_ascii=False) + "\n")
    yrs = [r["year"] for r in records]
    from collections import Counter
    print(f"corpus: {len(records)} sources -> {out}")
    print(f"year range {min(yrs)}-{max(yrs)}")
    print("by year:", dict(sorted(Counter(yrs).items())))


if __name__ == "__main__":
    main()
