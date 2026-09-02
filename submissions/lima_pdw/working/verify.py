import sys, json, urllib.request, urllib.parse, time

HDR = {"User-Agent": "diss-lib/1.0 (mailto:rhunt@bentley.edu)"}

def fetch(url):
    req = urllib.request.Request(url, headers=HDR)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)

def show(m):
    au = "; ".join((a.get("family", "") + ", " + a.get("given", "")) for a in m.get("author", []))
    ct = m.get("container-title") or []
    print("  T:", (m.get("title") or [None])[0])
    print("  A:", au)
    print("  V:", ct[0] if ct else m.get("publisher"))
    import re
    a = m.get("abstract")
    a = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", a)).strip() if a else "NO ABSTRACT"
    print("  ABS:", a[:1100])
    print("  Y:", m.get("issued", {}).get("date-parts", [[None]])[0][0],
          "| vol", m.get("volume"), "iss", m.get("issue"), "pp", m.get("page"),
          "| type", m.get("type"), "| ISBN", m.get("ISBN"))
    print("  DOI:", m.get("DOI"))

def show_brief(m, idx):
    au = "; ".join((a.get("family", "") + ", " + a.get("given", "")) for a in m.get("author", []))
    ct = m.get("container-title") or []
    y = m.get("issued", {}).get("date-parts", [[None]])[0][0]
    print(f"  [{idx}] {au} ({y}). {(m.get('title') or [None])[0]}")
    print(f"       {ct[0] if ct else m.get('publisher')} | vol {m.get('volume')} iss {m.get('issue')} "
          f"pp {m.get('page')} | DOI {m.get('DOI')} | type {m.get('type')}")

def search(query, rows=5):
    """Bibliographic search fallback for entries with no known DOI.
    Usage: python3 verify.py --search "Author Year Title fragment"
    Prints the top N Crossref candidates; the caller judges the match
    (require agreement on first-author surname + year + journal, not title alone)."""
    url = ("https://api.crossref.org/works?query.bibliographic="
           + urllib.parse.quote(query) + f"&rows={rows}")
    try:
        msg = fetch(url)["message"]
        items = msg.get("items", [])
        if not items:
            print("  NO CANDIDATES")
            return
        for i, m in enumerate(items, 1):
            show_brief(m, i)
    except Exception as e:
        print("  FAIL", e)

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--search":
        search(" ".join(args[1:]))
    else:
        for d in args:
            print("###", d)
            try:
                show(fetch("https://api.crossref.org/works/" + d)["message"])
            except Exception as e:
                print("  FAIL", e)
            time.sleep(0.3)
