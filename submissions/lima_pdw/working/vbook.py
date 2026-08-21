import sys, json, urllib.request, urllib.parse, time

HDR = {"User-Agent": "diss-lib/1.0 (mailto:rhunt@bentley.edu)"}

def get(url):
    req = urllib.request.Request(url, headers=HDR)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)

for q in sys.argv[1:]:
    print("###", q)
    try:
        if q.replace("-", "").isdigit():
            d = get("https://openlibrary.org/api/books?bibkeys=ISBN:%s&format=json&jscmd=data" % q)
            for k, v in d.items():
                print("  ", k, "->", v.get("title"), "|", [a["name"] for a in v.get("authors", [])],
                      "|", v.get("publish_date"), "|", [p["name"] for p in v.get("publishers", [])],
                      "|", v.get("identifiers", {}).get("isbn_13"), v.get("identifiers", {}).get("isbn_10"))
            if not d:
                print("   NOT FOUND")
        else:
            d = get("https://openlibrary.org/search.json?q=" + urllib.parse.quote(q) + "&fields=title,author_name,first_publish_year,publisher,isbn,publish_year&limit=3")
            for doc in d.get("docs", []):
                isbns = doc.get("isbn", [])
                i13 = [i for i in isbns if len(i) == 13][:6]
                print("  -", doc.get("title"), "|", doc.get("author_name"), "|", doc.get("first_publish_year"),
                      "|", (doc.get("publisher") or [])[:4])
                print("    isbn13:", i13)
    except Exception as e:
        print("   FAIL", e)
    time.sleep(0.4)
