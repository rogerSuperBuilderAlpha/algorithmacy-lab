"""Build the corpus for the algorithmic_management_claims review.

Merges two source channels harvested via the academic semantic-search connectors:

  1. Scholar Gateway result payloads (JSON), matched by their executed-query string to the six
     queries run for this review. Each result carries title, abstract, publication date, and DOI.
  2. A Consensus-derived seed file (literature/consensus_seed.jsonl) holding canonical and empirical
     algorithmic-management sources the Scholar Gateway queries did not surface, transcribed from the
     Consensus search results (title, abstract, year, DOI where known).

The builder deduplicates by DOI and by normalized title, applies the corpus boundary (an
algorithmic-management / algorithmic-control term AND a worker / gig / platform / labor term), slugifies,
and writes:

  literature/corpus.jsonl        — one screened in-boundary source per line {slug,title,abstract,year,doi}
  literature/screened_out.jsonl  — candidates dropped by the boundary rule (auditable)

    python3 -m org_frontier.reviews.algorithmic_management_claims.build_corpus \
        --sg-dir <dir-with-scholar-gateway-txt-files>

Standard library only. Deterministic given the saved search payloads.
"""

import argparse
import glob
import json
import os
import re

HERE = os.path.dirname(__file__)

# The six executed-query strings for this review (Scholar Gateway records are matched on these,
# so payloads written by other concurrent reviews in the same results dir are ignored).
MY_QUERIES = {
    "algorithmic management of workers on digital labor platforms",
    "algorithmic control of gig workers in the platform economy",
    "algorithmic management as a new form of control over workers",
    "platform work algorithmic management systematic review",
    "algorithmic management effects on productivity and firm performance",
    "worker experience wellbeing and resistance under algorithmic management",
}

# Boundary = an algorithm signal AND a work signal. The algorithm stem covers algorithmic
# management / control / surveillance / governance / scores / panopticon / manipulation; the work
# stem keeps the corpus to the algorithmic-management-OF-WORKERS literature and excludes generic
# algorithm-in-finance / law-and-society / firm-productivity hits that lack a worker referent.
AM_TERMS = re.compile(r"algorithm|digital taylor", re.I)
WORK_TERMS = re.compile(
    r"\bworker|\bgig\b|platform work|platform-?mediated|platform econom|platform capital|"
    r"labou?r|\bemployee|crowdwork|delivery (rider|driver|worker)|ride-?hail|\bUber\b|deliveroo|"
    r"online labo?r|app-?work|workforce|workplace|working condition|employment|\bHRM\b|"
    r"job (design|quality|crafting)|surveillance economy|transportation platform", re.I)


def _slugify(title, year, taken):
    base = re.sub(r"[^a-z0-9]+", "", (title or "").lower())[:24] or "src"
    slug = f"{base}{year or ''}"
    out, n = slug, 1
    while out in taken:
        n += 1
        out = f"{slug}_{n}"
    taken.add(out)
    return out


def _norm_title(t):
    return re.sub(r"[^a-z0-9]+", "", (t or "").lower())


def _year_from_date(s):
    if not s:
        return None
    m = re.search(r"(19|20)\d{2}", str(s))
    return int(m.group(0)) if m else None


def load_scholar_gateway(sg_dir):
    recs = []
    for f in sorted(glob.glob(os.path.join(sg_dir, "*.txt"))):
        try:
            payload = json.load(open(f))
        except (ValueError, OSError):
            continue
        if payload.get("tool") != "semanticSearch":
            continue
        q = (payload.get("provenance") or {}).get("query_as_executed", "")
        if q not in MY_QUERIES:
            continue
        for r in payload.get("results", []):
            md = (r.get("metadata") or {}).get("additionalMetadata") or {}
            title = md.get("title")
            if not title:
                continue
            recs.append({
                "title": title.strip(),
                "abstract": (md.get("abstract") or "").strip(),
                "year": _year_from_date(md.get("publicationDate")),
                "doi": (r.get("doi") or "").lower() or None,
                "source": "scholar_gateway",
            })
    return recs


def load_consensus_seed():
    p = os.path.join(HERE, "literature", "consensus_seed.jsonl")
    if not os.path.exists(p):
        return []
    out = []
    for line in open(p):
        line = line.strip()
        if line:
            r = json.loads(line)
            r["doi"] = (r.get("doi") or None) and r["doi"].lower()
            out.append(r)
    return out


def in_boundary(text):
    return bool(AM_TERMS.search(text or "") and WORK_TERMS.search(text or ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sg-dir", required=True, help="directory holding Scholar Gateway *.txt payloads")
    a = ap.parse_args()

    raw = load_scholar_gateway(a.sg_dir) + load_consensus_seed()

    # dedupe by DOI, then by normalized title
    by_doi, by_title, merged = {}, {}, []
    for r in raw:
        doi = r.get("doi")
        nt = _norm_title(r["title"])
        if doi and doi in by_doi:
            continue
        if nt in by_title:
            continue
        if doi:
            by_doi[doi] = r
        by_title[nt] = r
        merged.append(r)

    taken, kept, dropped = set(), [], []
    for r in merged:
        (kept if in_boundary(r["title"] + " " + r.get("abstract", "")) else dropped).append(r)

    for r in kept:
        r["slug"] = _slugify(r["title"], r["year"], taken)

    os.makedirs(os.path.join(HERE, "literature"), exist_ok=True)
    with open(os.path.join(HERE, "literature", "corpus.jsonl"), "w") as fh:
        for r in kept:
            fh.write(json.dumps({"slug": r["slug"], "title": r["title"],
                                 "abstract": r.get("abstract", ""), "year": r["year"],
                                 "doi": r.get("doi"), "source": r["source"]}) + "\n")
    with open(os.path.join(HERE, "literature", "screened_out.jsonl"), "w") as fh:
        for r in dropped:
            fh.write(json.dumps(r) + "\n")

    n_sg = sum(1 for r in kept if r["source"] == "scholar_gateway")
    n_c = sum(1 for r in kept if r["source"] == "consensus")
    print(f"raw candidates: {len(raw)}  |  after dedupe: {len(merged)}")
    print(f"kept (in-boundary): {len(kept)}  (scholar_gateway {n_sg}, consensus {n_c})  |  "
          f"screened out: {len(dropped)}")
    print("wrote literature/corpus.jsonl, literature/screened_out.jsonl")


if __name__ == "__main__":
    main()
