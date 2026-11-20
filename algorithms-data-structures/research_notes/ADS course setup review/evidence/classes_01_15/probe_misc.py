# Targeted probes behind specific claims in the key (classes 1-15).
# Run: python3.13 -I probe_misc.py <path to ADS_In_Class_Solutions.md> <path to ADS_In_Class_Board_Problems.md>
import sys, os, gc, re, random, time, tracemalloc, resource, subprocess, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import board as B
from board import ListNode, TreeNode
HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
random.seed(3)


def traced(f):
    gc.collect(); tracemalloc.start(); b = tracemalloc.get_traced_memory()[0]
    keep = f(); a = tracemalloc.get_traced_memory()[0]; tracemalloc.stop(); return keep, a - b


print('== (a) int size: sys.getsizeof vs tracemalloc, by how the int is made ==')
for label, mk in [('range item 1000..', lambda: list(range(1000, 101000))),
                  ('int("...") parse', lambda: [int(str(v)) for v in range(1000, 101000)]),
                  ('json.loads', lambda: json.loads('[' + ','.join(str(v) for v in range(1000, 101000)) + ']')),
                  ('a + b (compact)', lambda: [v + 1 for v in range(1000, 101000)])]:
    keep, b = traced(mk)
    print(f'  {label:18s}: getsizeof={sys.getsizeof(keep[5])}  traced per element (minus 8 B list slot) = {(b - 56) / len(keep) - 8:.2f}')
x = 2**30 - 1; y = 2**30 + 5
print(f'  getsizeof(2**30-1)={sys.getsizeof(x)}, getsizeof(2**30+5)={sys.getsizeof(y)}, getsizeof("")={sys.getsizeof("")}, getsizeof("a"*200)={sys.getsizeof("a"*200)}')

print('== (b) tracemalloc and recursion frames ==')
def down(k):
    if k == 0: return 0
    return down(k - 1) + 0
gc.collect(); tracemalloc.start(); tracemalloc.reset_peak(); b0 = tracemalloc.get_traced_memory()[0]
down(900); p = tracemalloc.get_traced_memory()[1] - b0; tracemalloc.stop()
print(f'  traced peak for 900 nested Python calls: {p} B  (frames are not visible to tracemalloc)')

FRAME_CHILD = r'''
import sys, resource, gc
sys.path.insert(0, sys.argv[1]); import board as B
from board import TreeNode
which, depth = sys.argv[2], int(sys.argv[3])
sys.setrecursionlimit(depth + 1000)
if which == 'maxDepth':
    root = None
    for _ in range(depth): root = TreeNode(1, root)   # left-leaning chain
    gc.collect(); r0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    B.maxDepth(root)
elif which == 'myPow_shape':      # same locals/stack shape as the key's myPow, made deep with n-1 steps
    def p(x, n):
        if n < 0:
            return 1 / p(x, -n)
        if n == 0:
            return 1.0
        half = p(x, n - 1)
        if n % 2 == 0:
            return half * half
        return half * half * x
    gc.collect(); r0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    p(1.0, depth)
elif which == 'fib_go':           # the key's go(k) closure, deep with a pre-filled memo except one chain
    memo = {0: 0, 1: 1}
    def go(k):
        if k not in memo:
            memo[k] = go(k - 1) + 0
        return memo[k]
    gc.collect(); r0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    go(depth)
r1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print((r1 - r0) / depth)
'''
open(os.path.join(HERE, '_frame_child.py'), 'w').write(FRAME_CHILD)
for which in ('maxDepth', 'myPow_shape', 'fib_go'):
    out = subprocess.run([PY, '-I', os.path.join(HERE, '_frame_child.py'), HERE, which, '200000'], capture_output=True, text=True)
    print(f'  RSS growth per active call, {which} at depth 200,000: {out.stdout.strip() or out.stderr.strip()[-200:]} B (macOS ru_maxrss is in bytes)')

print('== (c) #104 recursion depth on a chain (default limit) ==')
print('  sys.getrecursionlimit() =', sys.getrecursionlimit())
def chain(n):
    root = None
    for _ in range(n): root = TreeNode(1, root)
    return root
for n in (990, 1000, 10_000):
    try:
        r = B.maxDepth(chain(n)); print(f'  chain of {n}: returned {r}')
    except RecursionError as e:
        print(f'  chain of {n}: RecursionError: {e}')
sys.setrecursionlimit(10_100)
print('  after sys.setrecursionlimit(10_100), chain of 10,000:', B.maxDepth(chain(10_000)))
sys.setrecursionlimit(1000)

print('== (d) key board code for #933 and #102 run verbatim, without an import line ==')
src933 = '''
class RecentCounter:
    def __init__(self):
        self.window = deque()
    def ping(self, t):
        self.window.append(t)
        while self.window[0] < t - 3000:
            self.window.popleft()
        return len(self.window)
RecentCounter().ping(1)
'''
try:
    exec(src933, {})
except NameError as e:
    print('  #933:', type(e).__name__, e)

print('== (e) #125: are s[i] and .lower() results cached singletons? ==')
s = 'Ab'
print(f"  s[0] is 'A': {s[0] is 'A'};  'A'.lower() is 'a': {'A'.lower() is 'a'};  'a'.lower() is 'a': {'a'.lower() is 'a'}")

print('== (f) list built by append: spare room ==')
for n in (200, 10_000, 10_001, 100_000):
    a = []
    for i in range(n): a.append(None)
    cap = (sys.getsizeof(a) - 56) // 8
    print(f'  n={n}: capacity {cap}, spare {100 * (cap - n) / n:.1f}%')

print('== (g) dict bytes per entry (int keys), sys.getsizeof ==')
for n in (31, 1000, 9_999, 10_000, 100_000):
    d = {i + 10**6: i for i in range(n)}
    print(f'  {n} entries: {sys.getsizeof(d)} B = {sys.getsizeof(d) / n:.1f} B/entry')
d = {}
for ch in 'abcdefghijklmnopqrstuvwxyz': d[ch] = 1000
print(f'  26 str keys: {sys.getsizeof(d)} B;  3-entry pairs dict: {sys.getsizeof({")": "(", "]": "[", "}": "{"})} B;  memo {{0:0,1:1}} grown to 31: ', end='')
m = {0: 0, 1: 1}
for k in range(2, 31): m[k] = k
print(sys.getsizeof(m), 'B')

print('== (h) set table for 100,000 elements (#217) ==')
st = set(range(10**6, 10**6 + 100_000)); sz = sys.getsizeof(st); base = sys.getsizeof(set())
print(f'  getsizeof={sz}, empty set={base}, table bytes={sz - base}, slots of 16 B={(sz - base) / 16:.0f} (= 2**{((sz - base) // 16).bit_length() - 1})')
st2 = set()
for v in range(10**6, 10**6 + 100_000): st2.add(v)
print(f'  same set built by add(): getsizeof={sys.getsizeof(st2)}')

print('== (i) #977 alternative: comparisons made by sorted() on the squares ==')
class C:
    n = 0
    __slots__ = ('v',)
    def __init__(self, v): self.v = v
    def __lt__(self, o): C.n += 1; return self.v < o.v
nums = sorted(random.randint(-10**4, 10**4) for _ in range(10_000))
C.n = 0; sorted(C(x * x) for x in nums)
print(f'  n=10,000 sorted input with negatives: {C.n} comparisons (n log2 n = {int(10_000 * 13.29)}); squares form two runs')
rnd = [random.randint(0, 10**8) for _ in range(10_000)]
C.n = 0; sorted(C(x) for x in rnd)
print(f'  n=10,000 random values: {C.n} comparisons')

print('== (j) list.sort() auxiliary memory (sort alternatives of #217, #136) ==')
a = [random.randint(10**6, 10**9) for _ in range(30_000)]
gc.collect(); tracemalloc.start(); tracemalloc.reset_peak(); b0 = tracemalloc.get_traced_memory()[0]
a.sort(); p = tracemalloc.get_traced_memory()[1] - b0; tracemalloc.stop()
print(f'  in-place sort of 30,000 random ints: traced peak {p} B = {p / 30_000:.2f} B per element (merge buffer)')

print('== (k) #14 alternative "sort, compare first and last": character work ==')
class S:
    cmp = 0; chars = 0
    __slots__ = ('s',)
    def __init__(self, s): self.s = s
    def __lt__(self, o):
        S.cmp += 1
        k = 0
        while k < min(len(self.s), len(o.s)) and self.s[k] == o.s[k]: k += 1
        S.chars += k + 1
        return self.s < o.s
m_, L = 200, 200
strs = ['a' * (L - 1) + random.choice('bcdefghijklmnopqrstuvwxyz') for _ in range(m_)]
S.cmp = S.chars = 0; sorted(S(x) for x in strs)
print(f'  m=200 strings of L=200 sharing a 199-char prefix: {S.cmp} comparisons, {S.chars} char comparisons; S = m*L = {m_ * L}')

print('== (l) #1331: where is the peak? ==')
def ranks_only(arr):
    rank = {}
    for x in sorted(set(arr)):
        rank[x] = len(rank) + 1
    return rank
arr = random.sample(range(257, 10**9), 100_000)
for f in (ranks_only, B.arrayRankTransform):
    gc.collect(); tracemalloc.start(); tracemalloc.reset_peak(); b0 = tracemalloc.get_traced_memory()[0]
    r = f(arr); p = tracemalloc.get_traced_memory()[1] - b0; tracemalloc.stop(); del r
    print(f'  {f.__name__}: traced peak {p / 2**20:.2f} MB')

print('== (m) #232 and #912 timing as n doubles (amortized O(1) / O(n log n)) ==')
def q_run(n):
    q = B.MyQueue()
    for i in range(n): q.push(i)
    for i in range(n): q.pop()
for n in (100_000, 200_000, 400_000):
    t = time.perf_counter(); q_run(n); print(f'  MyQueue {n} push + {n} pop: {time.perf_counter() - t:.3f}s')
for n in (50_000, 100_000, 200_000):
    a = [random.randint(-5 * 10**4, 5 * 10**4) for _ in range(n)]
    t = time.perf_counter(); B.sortArray(a); print(f'  sortArray n={n}: {time.perf_counter() - t:.3f}s')

print('== (n) key vs student sheet: statement + example text, and stated memory size ==')
key_md, sheet_md = sys.argv[1], sys.argv[2]
def blocks(path, stop, limit):
    lines = open(path).read().split('\n')[:limit]
    out = {}; cur = None
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        m = re.match(r'\*\*#(\d+) ', s)
        if m: cur = m.group(1); out[cur] = {'line': i, 'text': []}; continue
        if cur and s.startswith(stop): cur = None; continue
        if cur and s and not s.startswith('**Easy') and not s.startswith('**Medium') and not s.startswith('[[http'):
            out[cur]['text'].append(s)
    return {k: (v['line'], ' '.join(v['text'])) for k, v in out.items()}
kb = blocks(key_md, '**Solution', 2815)
sb = blocks(sheet_md, 'Start with', 1570)
diffs = [k for k in kb if kb[k][1] != sb.get(k, (0, ''))[1]]
print(f'  problems compared: {len(kb)}; statement/example text differs for: {diffs or "none"}')
klines = open(key_md).read().split('\n')[:2815]; slines = open(sheet_md).read().split('\n')[:1570]
def para_after(lines, start_pat):
    out = []
    for i, ln in enumerate(lines):
        if ln.strip().startswith(start_pat):
            buf = [ln.strip()]
            j = i + 1
            while j < len(lines) and lines[j].strip(): buf.append(lines[j].strip()); j += 1
            out.append(' '.join(buf))
    return out
ka = [re.sub(r'^\*\*Assumptions\.\*\* ', '', p) for p in para_after(klines, '**Assumptions.**')]
sa = [re.sub(r'^Memory estimate, for ', '', p) for p in para_after(slines, 'Memory estimate, for')]
mism = [(i, a[:70], b[:70]) for i, (a, b) in enumerate(zip(ka, sa)) if not a.lower().startswith(b.lower().rstrip('.')[:40])]
print(f'  memory-size sentences: key {len(ka)}, sheets {len(sa)}; sheet sentence not a prefix of key assumption: {mism or "none"}')
