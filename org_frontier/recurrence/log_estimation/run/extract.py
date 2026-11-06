import sys,json
R={"kubernetes/kubernetes","facebook/react","microsoft/vscode","django/django","rust-lang/rust"}
for l in sys.stdin:
    try:e=json.loads(l)
    except Exception:continue
    if e["repo"]["name"] not in R:continue
    p=e.get("payload",{});pr=p.get("pull_request") or {}
    body=((p.get("comment") or {}).get("body") or "")[:200]
    rv=(p.get("review") or {}).get("state")
    print(json.dumps({"t":e["created_at"],"repo":e["repo"]["name"],"type":e["type"],"actor":e["actor"]["login"],
      "action":p.get("action"),"merged":pr.get("merged"),"merged_by":(pr.get("merged_by") or {}).get("login"),
      "ref":p.get("ref"),"review":rv,"body":body}))
