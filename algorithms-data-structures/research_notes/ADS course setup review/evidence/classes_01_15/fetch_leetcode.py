# Fetch official statements for the 30 problems of classes 1-15 from LeetCode GraphQL.
# Saves raw JSON per slug in fetched/ and a plain-text digest in fetched/digest.txt.
import json, sys, time, urllib.request, html, re, os
SLUGS = """running-sum-of-1d-array contains-duplicate move-zeroes merge-sorted-array
longest-common-prefix range-sum-query-immutable valid-anagram two-sum valid-palindrome
squares-of-a-sorted-array maximum-average-subarray-i best-time-to-buy-and-sell-stock
valid-parentheses backspace-string-compare number-of-recent-calls implement-queue-using-stacks
next-greater-element-i daily-temperatures reverse-linked-list remove-nth-node-from-end-of-list
fibonacci-number powx-n single-number single-number-iii rank-transform-of-an-array sort-an-array
binary-search find-first-and-last-position-of-element-in-sorted-array maximum-depth-of-binary-tree
binary-tree-level-order-traversal""".split()
Q = "query q($s:String!){question(titleSlug:$s){questionFrontendId title difficulty content exampleTestcases codeSnippets{langSlug code}}}"
outdir = sys.argv[1]
digest = []
for slug in SLUGS:
    path = os.path.join(outdir, slug + '.json')
    if not os.path.exists(path):
        body = json.dumps({"query": Q, "variables": {"s": slug}}).encode()
        req = urllib.request.Request("https://leetcode.com/graphql", data=body,
              headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0",
                       "Referer": "https://leetcode.com/problems/" + slug + "/"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        open(path, 'wb').write(data)
        time.sleep(0.7)
    q = json.load(open(path))['data']['question']
    text = html.unescape(re.sub(r'<[^>]+>', '', q['content'] or ''))
    text = re.sub(r'\n\s*\n+', '\n', text).strip()
    py = [c['code'] for c in (q['codeSnippets'] or []) if c['langSlug'] == 'python3']
    digest.append(f"===== {q['questionFrontendId']} {q['title']} [{q['difficulty']}] ({slug})\n{text}\n--- exampleTestcases:\n{q['exampleTestcases']}\n--- python3 snippet:\n{py[0] if py else 'NONE'}\n")
open(os.path.join(outdir, 'digest.txt'), 'w').write('\n'.join(digest))
print('fetched', len(digest))
