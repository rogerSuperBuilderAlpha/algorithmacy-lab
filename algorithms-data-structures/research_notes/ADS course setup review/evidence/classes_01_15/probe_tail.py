# Last checks: Other-approaches coverage, node class definitions, #50 x=0 n<0, exact constraints with <sup>.
import sys, re, json, os, html
key, sheet, syl, fetched = sys.argv[1:5]
kl = open(key).read().split('\n')[:2814]
cur = None; has = {}
for i, ln in enumerate(kl, 1):
    m = re.match(r'\*\*#(\d+) ', ln.strip())
    if m: cur = m.group(1); has[cur] = None
    if cur and ln.strip() == '**Other approaches**': has[cur] = i
print('Problems with NO "Other approaches" table:', [k for k, v in has.items() if v is None])
for path in (key, sheet, syl):
    txt = open(path).read()
    print(os.path.basename(path), ': "class ListNode" found:', 'class ListNode' in txt, '| "class TreeNode" found:', 'class TreeNode' in txt,
          '| "import" lines:', len(re.findall(r'^\s*>?\s*(from \w+ import|import \w+)', txt, re.M)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import board as B
for x, n in ((0.0, -1), (0.0, 0), (10.0, 400), (0.5, -2000)):
    try: print(f'myPow({x}, {n}) ->', B.myPow(x, n))
    except Exception as e: print(f'myPow({x}, {n}) -> {type(e).__name__}: {e}')
for slug in ['running-sum-of-1d-array', 'move-zeroes', 'merge-sorted-array', 'two-sum', 'implement-queue-using-stacks',
             'binary-search', 'powx-n', 'single-number-iii', 'binary-tree-level-order-traversal', 'maximum-depth-of-binary-tree',
             'sort-an-array', 'valid-parentheses']:
    c = json.load(open(os.path.join(fetched, slug + '.json')))['data']['question']['content']
    c = c.replace('<sup>', '^').replace('</sup>', '')
    t = html.unescape(re.sub(r'<[^>]+>', '', c))
    cons = t[t.find('Constraints:'):].split('\n')
    print(slug, '|', ' ; '.join(s.strip() for s in cons[1:8] if s.strip())[:260])
