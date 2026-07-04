"""Harvest a citation graph around a seed set, via the Semantic Scholar Graph API.

For each seed (a DOI, or a title to search), this resolves a Semantic Scholar paperId, then pulls the
seed's outbound references and inbound citers, and writes one edge file per seed. The result feeds
bibliometrics.py. Two disciplines matter and are built in:

  * Checkpointing — one file per seed, and a seed whose file already exists is skipped. A run killed
    by a rate limit or a timeout is simply restarted; it resumes where it stopped.
  * Backoff — a 429 triggers an exponential wait. The public API is unauthenticated and slow; harvest
    is meant to run unattended, not fast.

Seeds file is JSON: a list of {"slug": "...", "doi": "..."} or {"slug": "...", "title": "..."}.
Semantic Scholar elides references for many publishers, so the outbound `refs` list is often empty
even when the paper has references; the inbound `citers` list is the more reliable channel. Both are
recorded so downstream code can use whichever is present.

Run:

    python -m org_frontier.reviews.lib.harvest seeds.json --out edges/

Standard library only (urllib). No API key required; set S2_API_KEY in the environment to raise the
rate limit if you have one.
"""

import argparse
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

_API = "https://api.semanticscholar.org/graph/v1"
_REF_FIELDS = "paperId,externalIds,title,year,venue,citationCount"


def _get(url, tries=6):
    """GET with 429/5xx exponential backoff. Returns parsed JSON or None."""
    key = os.environ.get("S2_API_KEY")
    headers = {"x-api-key": key} if key else {}
    wait = 3.0
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(wait)
                wait *= 2
                continue
            return None
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            time.sleep(wait)
            wait *= 2
    return None


def resolve(seed):
    """Return (paperId, handle) for a seed with a doi or a title, or (None, None)."""
    if seed.get("doi"):
        handle = "DOI:" + seed["doi"]
        data = _get(f"{_API}/paper/{urllib.parse.quote(handle)}?fields=paperId")
        if data and data.get("paperId"):
            return data["paperId"], handle
    if seed.get("title"):
        q = urllib.parse.quote(seed["title"])
        data = _get(f"{_API}/paper/search?query={q}&limit=1&fields=paperId,title")
        if data and data.get("data"):
            return data["data"][0]["paperId"], "TITLE:" + seed["title"]
    return None, None


def _page(pid, kind):
    """All references (kind='references') or citers (kind='citations') for a paperId."""
    out = []
    offset = 0
    while True:
        url = (f"{_API}/paper/{pid}/{kind}?fields={_REF_FIELDS}"
               f"&limit=100&offset={offset}")
        data = _get(url)
        if not data or not data.get("data"):
            break
        for row in data["data"]:
            p = row.get("citedPaper") or row.get("citingPaper") or {}
            ext = p.get("externalIds") or {}
            out.append({"id": p.get("paperId"), "doi": ext.get("DOI"), "t": p.get("title"),
                        "year": p.get("year")})
        offset += 100
        if offset >= 1000 or len(data["data"]) < 100:
            break
        time.sleep(1.0)
    return out


def harvest_seed(seed, out_dir):
    """Resolve one seed and write its edge file. Returns the edge dict (or an error stub)."""
    path = os.path.join(out_dir, seed["slug"] + ".json")
    if os.path.exists(path):
        return json.load(open(path))
    pid, handle = resolve(seed)
    if not pid:
        rec = {"handle": handle, "error": "unresolved", "refs": [], "citers": []}
    else:
        rec = {"handle": handle, "doi": seed.get("doi"), "title": seed.get("title"),
               "refs": _page(pid, "references"), "citers": _page(pid, "citations")}
    json.dump(rec, open(path, "w"))
    return rec


def run(seeds_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    seeds = json.load(open(seeds_path))
    done = skipped = failed = 0
    for i, seed in enumerate(seeds, 1):
        path = os.path.join(out_dir, seed["slug"] + ".json")
        if os.path.exists(path):
            skipped += 1
            continue
        rec = harvest_seed(seed, out_dir)
        if rec.get("error"):
            failed += 1
        else:
            done += 1
        print(f"[{i}/{len(seeds)}] {seed['slug']}: "
              f"{'ERR ' + rec['error'] if rec.get('error') else str(len(rec['refs'])) + ' refs, ' + str(len(rec['citers'])) + ' citers'}")
        time.sleep(1.0)
    print(f"\nharvested {done}, skipped {skipped} (already done), unresolved {failed}; "
          f"edge files in {out_dir}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seeds", help="JSON list of {slug, doi|title}")
    ap.add_argument("--out", default="edges", help="output directory for per-seed edge files")
    a = ap.parse_args()
    run(a.seeds, a.out)


if __name__ == "__main__":
    main()
