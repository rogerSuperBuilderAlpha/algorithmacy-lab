"""Parse the fetched LeetCode JSON into plain text: id, title, difficulty, statement, constraints, Python3 starter."""
import json, re, html, sys, pathlib
RAW = pathlib.Path(sys.argv[1])
order = sys.argv[2].split(",")
def text(h):
    h = re.sub(r"<sup>(.*?)</sup>", r"^\1", h)
    h = re.sub(r"<[^>]+>", "", h)
    return re.sub(r"\n\s*\n+", "\n", html.unescape(h)).strip()
for s in order:
    q = json.loads((RAW / f"{s}.json").read_text())["data"]["question"]
    t = text(q["content"])
    py = next((c["code"] for c in q["codeSnippets"] if c["langSlug"] == "python3"), "")
    print(f"=== #{q['questionFrontendId']} {q['title']} [{q['difficulty']}] ({s})")
    print(t)
    print("--- python3 starter:")
    print(py)
    print()
