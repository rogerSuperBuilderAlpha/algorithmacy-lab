#!/usr/bin/env python3
"""Resolve every card's DOI and compare the registered title and year with the card.

Copied from D/current/monograph/library/tools/check_dois.py (itself adapted from W/dxd_foundation/literature/audit/check_dois.py); reads card frontmatter.

    python3 -I tools/check_dois.py            # writes DOI_CHECK.md
    python3 -I tools/check_dois.py KEY ...    # check only these cards, print results

It asks Crossref (api.crossref.org/works/<doi>) and, when Crossref has no record, doi.org with CSL-JSON
content negotiation (covers DataCite DOIs such as arXiv's). Metadata only: it does not check that a claim
made about a source is true. Cards with no DOI are listed for checking by hand.
"""
import difflib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_index import LIB, load  # noqa: E402

UA = {"User-Agent": "algorithmacy-pt-ai-animation-library/1.0 (stdlib urllib)"}


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def get(url, accept=None):
    h = dict(UA)
    if accept:
        h["Accept"] = accept
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=30) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(3 * (attempt + 1))
        except Exception:
            time.sleep(3 * (attempt + 1))
    return "ERROR"


def lookup(doi):
    q = urllib.parse.quote(doi, safe="/")
    r = get("https://api.crossref.org/works/" + q)
    if isinstance(r, dict):
        m = r["message"]
        title = " ".join(m.get("title") or [])
        if m.get("subtitle"):
            title += " " + " ".join(m["subtitle"])
        years = {str(m[k]["date-parts"][0][0]) for k in ("issued", "published-print", "published-online", "published")
                 if m.get(k) and m[k].get("date-parts") and m[k]["date-parts"][0] and m[k]["date-parts"][0][0]}
        return "Crossref", title, years
    r2 = get("https://doi.org/" + q, accept="application/vnd.citationstyles.csl+json")
    if isinstance(r2, dict):
        years = set()
        for k in ("issued", "published"):
            try:
                years.add(str(r2[k]["date-parts"][0][0]))
            except Exception:
                pass
        return "doi.org", str(r2.get("title") or ""), years
    return ("ERROR" if "ERROR" in (r, r2) else "NOT FOUND"), "", set()


def verdict(card):
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", card.get("doi", "")).strip()
    src, rtitle, years = lookup(doi)
    title, year = card.get("title", ""), card.get("year", "")[:4]
    ratio = difflib.SequenceMatcher(None, norm(title), norm(rtitle)).ratio() if rtitle else 0.0
    if src in ("ERROR", "NOT FOUND"):
        v = src
    elif ratio < 0.6 and norm(title) not in norm(rtitle) and norm(rtitle) not in norm(title):
        v = "TITLE MISMATCH"
    elif year and years and year not in years:
        v = "ok (year convention)" if card.get("registered_year") in years else "year differs"
    else:
        v = "ok"
    return (card["key"], doi, src, f"{ratio:.2f}", year, "/".join(sorted(years)), v, rtitle[:90])


def main():
    cards, _ = load()
    keys = sys.argv[1:]
    if keys:
        for c in cards:
            if c["key"] in keys:
                print(verdict(c) if c.get("doi") else (c["key"], "no DOI"))
        return 0
    rows, nodoi = [], []
    for c in cards:
        if c.get("status") == "dropped":
            continue
        if not c.get("doi"):
            nodoi.append((c["key"], c.get("url") or "(no identifier)"))
            continue
        rows.append(verdict(c))
        time.sleep(0.15)
    bad = [r for r in rows if r[6] != "ok"]
    out = ["# DOI check", "",
           "*Written by `tools/check_dois.py`. Metadata only: the registered title and year against the card.*", "",
           f"Cards with a DOI: {len(rows)}. ok: {len(rows) - len(bad)}. "
           + "; ".join(f"{v}: {sum(1 for r in rows if r[6] == v)}"
                       for v in ("year differs", "TITLE MISMATCH", "NOT FOUND", "ERROR"))
           + f". Cards with no DOI: {len(nodoi)}.", "",
           "## Rows needing a look", "",
           "| key | doi | source | title ratio | card year | registered year(s) | verdict | registered title |",
           "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    out += ["| `" + r[0] + "` | " + " | ".join(x.replace("|", "/") for x in r[1:]) + " |" for r in bad]
    out += ["", "## Cards with no DOI (check by hand)", "", "| key | identifier |", "| --- | --- |"]
    out += [f"| `{k}` | {u.replace('|', '/')} |" for k, u in nodoi]
    open(os.path.join(LIB, "DOI_CHECK.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(out[4])
    return 0


if __name__ == "__main__":
    sys.exit(main())
