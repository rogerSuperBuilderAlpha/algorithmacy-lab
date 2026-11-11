#!/usr/bin/env python3
"""Print the bibliographic fields of a key's registry records (Crossref, OpenAlex, Open Library) for a card
writer to read. Display only: it writes nothing.    python3 -I tools/show_record.py KEY [KEY ...]"""
import json, os, re, sys, html
S = os.path.expanduser("~/iit-playground/pt_ai_animation_local/pdfs")

def inv(ai):
    if not ai: return ""
    pos = {}
    for w, ps in ai.items():
        for p in ps: pos[p] = w
    return " ".join(pos[i] for i in sorted(pos))

for key in sys.argv[1:]:
    d = os.path.join(S, key); print("=" * 100); print(key, "|", sorted(os.listdir(d)) if os.path.isdir(d) else "NO FOLDER")
    if not os.path.isdir(d): continue
    for fn in sorted(os.listdir(d)):
        p = os.path.join(d, fn)
        if fn.startswith("crossref") and fn.endswith(".json"):
            m = json.load(open(p)).get("message", {})
            print(f"-- {fn}: type={m.get('type')} title={m.get('title')} subtitle={m.get('subtitle')}")
            print("   authors:", [(a.get('given'), a.get('family') or a.get('name')) for a in m.get('author', [])], "| editors:", [(a.get('given'), a.get('family')) for a in m.get('editor', [])])
            print("   container:", m.get('container-title'), "| publisher:", m.get('publisher'), "| vol:", m.get('volume'), "issue:", m.get('issue'), "pages:", m.get('page'), "| ISBN:", m.get('ISBN'))
            print("   issued:", m.get('issued', {}).get('date-parts'), "| published-print:", (m.get('published-print') or {}).get('date-parts'), "| published-online:", (m.get('published-online') or {}).get('date-parts'), "| DOI:", m.get('DOI'))
            ab = m.get('abstract'); print("   abstract:", re.sub(r"<[^>]+>", " ", html.unescape(ab)).strip()[:1500] if ab else None)
        elif fn.startswith("openalex") and fn.endswith(".json"):
            w = json.load(open(p))
            if "results" in w: print(f"-- {fn}: search response with {len(w['results'])} results"); continue
            print(f"-- {fn}: {w.get('id')} type={w.get('type')} year={w.get('publication_year')} title={w.get('title')}")
            print("   authors:", [a.get('author', {}).get('display_name') for a in w.get('authorships', [])][:6], "| source:", ((w.get('primary_location') or {}).get('source') or {}).get('display_name'), "| oa:", (w.get('open_access') or {}).get('is_oa'))
            b = w.get('biblio') or {}; print("   biblio:", b, "| cited_by:", w.get('cited_by_count'))
            print("   abstract:", inv(w.get('abstract_inverted_index'))[:1500] or None)
        elif fn.startswith("openlibrary") and fn.endswith(".json"):
            o = json.load(open(p))
            for part in ("edition", "work", "search"):
                if part in o or (isinstance(o, dict) and part == "edition" and "title" in o):
                    pass
            print(f"-- {fn}: keys={list(o.keys())[:12] if isinstance(o, dict) else type(o)}")
            if isinstance(o, dict):
                e = o.get("edition") or o
                print("   title:", e.get("title"), "| subtitle:", e.get("subtitle"), "| authors:", e.get("authors"), "| by_statement:", e.get("by_statement"))
                print("   publishers:", e.get("publishers"), "| publish_date:", e.get("publish_date"), "| pages:", e.get("number_of_pages"), "| isbn13:", e.get("isbn_13"), "isbn10:", e.get("isbn_10"), "| publish_places:", e.get("publish_places"))
                wk = o.get("work") or {}
                if wk: print("   work:", wk.get("title"), "| first_publish_date:", wk.get("first_publish_date"), "| desc:", (wk.get("description") if isinstance(wk.get("description"), str) else (wk.get("description") or {}).get("value", ""))[:600])
                if "docs" in o: print("   search docs:", [(x.get("title"), x.get("first_publish_year"), x.get("publisher", [None])[:2], x.get("isbn", [None])[:3]) for x in o["docs"][:5]])
        elif fn.endswith((".pdf", ".txt", ".html", ".xml")):
            print(f"-- {fn}: {os.path.getsize(p)} bytes")
