import sys, json, urllib.request, time

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

for d in sys.argv[1:]:
    print("###", d)
    try:
        show(fetch("https://api.crossref.org/works/" + d)["message"])
    except Exception as e:
        print("  FAIL", e)
    time.sleep(0.3)
