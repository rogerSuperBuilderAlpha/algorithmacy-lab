#!/usr/bin/env python3
"""On-demand card backfill: retry open-access acquisition over every uncarded reference and
surface any that have become open-access since the last pass. Stdlib only.

A reference is "uncarded" when it has a resolvable identifier (DOI or arXiv id) but no card under
`<program>/literature/cards/`. For each, this retries `oa_acquire.acquire`; newly-downloadable PDFs
are saved to `<program>/literature/pdfs/<citekey>.pdf` (gitignored), the program manifest is updated,
and a card-writing config is written for the multi-agent card workflow.

    python org_frontier/research/card_backfill.py            # scan + retry, report only
    python org_frontier/research/card_backfill.py --write     # also save PDFs + write card config

After a run that finds new PDFs, write their cards with the reference-card workflow (the same
write + adversarial-verify pipeline that built the deck), then land per the standard PR flow. With
no newly-available papers the deck is already current and nothing is written.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import oa_acquire  # noqa: E402

PROGRAMS = ["computational", "field", "qualitative", "recurrence", "survey", "cognition"]


def parse_bib(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", txt, re.S):
        body = m.group(3)

        def f(k):
            mm = re.search(r"%s\s*=\s*\{([^}]+)\}" % k, body)
            return mm.group(1).strip() if mm else None
        out.append({"citekey": m.group(2).strip(), "type": m.group(1).lower(), "title": f("title"),
                    "author": f("author"), "year": f("year"), "doi": f("doi"), "eprint": f("eprint"),
                    "url": f("url"), "journal": f("journal")})
    return out


def global_carded():
    """Every carded citekey and DOI across all programs. Dedup is global: a paper carded in one
    program (the canonical owner of a cross-program reference) is not re-carded in another."""
    ck, doi = set(), set()
    for p in PROGRAMS:
        for c in glob.glob(os.path.join(HERE, p, "literature", "cards", "*.md")):
            ck.add(os.path.basename(c)[:-3])
            m = re.search(r"^doi: (.+)$", open(c, encoding="utf-8").read(), re.M)
            if m and m.group(1).strip() != "null":
                doi.add(m.group(1).strip().lower())
    return ck, doi


def main():
    write = "--write" in sys.argv
    config = {}
    summary = {}
    carded_ck, carded_doi = global_carded()
    for p in PROGRAMS:
        lit = os.path.join(HERE, p, "literature")
        entries = parse_bib(os.path.join(lit, "references.bib"))
        pdir = os.path.join(lit, "pdfs")
        newly = []
        for e in entries:
            ck = e["citekey"]
            doi = (e.get("doi") or "").strip().lower()
            if ck in carded_ck or (doi and doi in carded_doi):
                continue
            if not (e.get("doi") or e.get("eprint")):
                continue
            dest = os.path.join(pdir, ck + ".pdf")
            if os.path.exists(dest) and os.path.getsize(dest) > 15000:
                pass  # already have the PDF, just not carded yet
            else:
                r = oa_acquire.acquire(e)
                if r["status"] != "ACQUIRED":
                    continue
                if write:
                    os.makedirs(pdir, exist_ok=True)
                    open(dest, "wb").write(r["_data"])
                e["_oa"] = (r.get("oa_source"), r.get("source_url"), r.get("sha256"))
            newly.append(e)
            carded_ck.add(ck)  # within-run dedup: don't re-stage a shared paper for another program
            if doi:
                carded_doi.add(doi)
        summary[p] = len(newly)
        if newly and write:
            cards_abs = os.path.join(lit, "cards")
            wp = []
            for e in newly:
                oa = e.get("_oa", (None, None, None))
                wp.append({"citekey": e["citekey"], "title": e.get("title", ""), "authors": e.get("author", ""),
                           "year": e.get("year", ""), "doi": e.get("doi"), "arxiv": e.get("eprint"),
                           "journal": e.get("journal", ""), "programs": [p],
                           "pdf_path": os.path.join(pdir, e["citekey"] + ".pdf"),
                           "oa_source": oa[0], "source_url": oa[1], "sha256": oa[2]})
            config[p] = wp
    total = sum(summary.values())
    print("newly-available uncarded references:", {k: v for k, v in summary.items() if v})
    print("TOTAL newly available:", total)
    if write and config:
        out = os.path.join(HERE, "backfill_cards_config.json")
        json.dump(config, open(out, "w"), ensure_ascii=False, indent=1)
        print("card-writing config written:", out, "(feed to the reference-card workflow)")
    elif total and not write:
        print("re-run with --write to download the PDFs and stage the card-writing config.")
    else:
        print("the deck is current; nothing to backfill.")


if __name__ == "__main__":
    main()
