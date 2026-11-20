"""Measure input and auxiliary memory with tracemalloc at the input sizes the key states (classes 16-30).

input  = traced bytes held after the input is built (what the caller owns)
aux    = tracemalloc peak during the call minus the traced bytes before the call
         (includes the returned output and every temporary; recursion frames are not traced)
kept   = traced bytes still held after the call (output + anything left behind)
Units: KiB = 1024 B, MiB = 1024^2 B (the key's "KB"/"MB" figures match binary units, e.g. 5,000 x 100 B = "488 KB").
Run: /opt/homebrew/bin/python3.13 memory_measure.py
"""
import gc, random, string, sys, tracemalloc, itertools
from collections import deque
import board_solutions as S
from lc_types import TreeNode, balanced_bst, height

random.seed(7)
ROWS = []


def fmt(b):
    if b >= 1024 * 1024:
        return f"{b/1024/1024:.2f} MiB"
    if b >= 1024:
        return f"{b/1024:.1f} KiB"
    return f"{b} B"


def measure(label, build, run, key_input, key_aux):
    gc.collect()
    tracemalloc.start()
    base = tracemalloc.get_traced_memory()[0]
    inp = build()
    gc.collect()
    after_in = tracemalloc.get_traced_memory()[0]
    tracemalloc.reset_peak()
    out = run(inp)
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    res = dict(label=label, input=after_in - base, aux=peak - after_in, kept=cur - after_in)
    ROWS.append(res)
    print(f"{label:<34} input {fmt(res['input']):>11} (key {key_input:>7}) | aux peak {fmt(res['aux']):>11} "
          f"(key {key_aux:>7}) | kept after call {fmt(res['kept'])}")
    return out, inp


# ---------------- Class 16
def chain_free_bst(n, lo=257):
    vals = sorted(random.sample(range(lo, 10**7), n))
    return balanced_bst(vals)

measure("#700 n=5000 balanced BST", lambda: chain_free_bst(5000), lambda r: S.searchBST(r, 1), "488 KB", "100 B")
r = TreeNode(300)
print("   sys.getsizeof(TreeNode instance) =", sys.getsizeof(r), "; height of 10,000-node balanced BST =",
      height(balanced_bst(list(range(10000)))))
measure("#98 n=10000 balanced BST", lambda: chain_free_bst(10000), lambda r: S.isValidBST(r), "977 KB", "2.1 KB")

# ---------------- Class 17
def run703(stream):
    obj = S.KthLargest(10_000, [])
    for v in stream:
        obj.add(v)
    return obj
measure("#703 k=1e4, 1e5 distinct ints>256", lambda: random.sample(range(257, 10**7), 100_000), run703, "2.7 MB", "88 KB")
measure("#703 LeetCode max: k=1e4,1e4+1e4 vals", lambda: [random.randint(-10**4, 10**4) for _ in range(20_000)],
        lambda s: (lambda o: [o.add(v) for v in s[10_000:]])(S.KthLargest(10_000, s[:10_000])), "-", "-")

measure("#347 n=1e5 all distinct, k=100", lambda: random.sample(range(257, 10**7), 100_000),
        lambda nums: S.topKFrequent(nums, 100), "3.4 MB", "5.0 MB")
measure("#347 LeetCode max: n=1e5 in [-1e4,1e4]", lambda: [random.randint(-10**4, 10**4) for _ in range(100_000)],
        lambda nums: S.topKFrequent(nums, 100), "-", "-")

# ---------------- Class 18
for (sr, sc) in ((0, 0), (25, 25)):
    measure(f"#733 50x50 one colour, start {sr},{sc}", lambda: [[1] * 50 for _ in range(50)],
            lambda img, sr=sr, sc=sc: S.floodFill(img, sr, sc, 2), "23 KB", "79 KB")
measure("#200 300x300 all land", lambda: [["1"] * 300 for _ in range(300)], S.numIslands, "722 KB", "3.1 MB")

# stack peak lengths (independent of tracemalloc)
def peak_stack_flood(R, C, sr, sc):
    img = [[1] * C for _ in range(R)]; img[sr][sc] = 2; st = [(sr, sc)]; pk = 1
    while st:
        r, c = st.pop()
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < R and 0 <= nc < C and img[nr][nc] == 1:
                img[nr][nc] = 2; st.append((nr, nc))
        pk = max(pk, len(st))
    return pk
print("   peak stack length, 50x50 from (0,0):", peak_stack_flood(50, 50, 0, 0), "of 2500;",
      "from (25,25):", peak_stack_flood(50, 50, 25, 25), "; 300x300 from (0,0):", peak_stack_flood(300, 300, 0, 0), "of 90000")

# ---------------- Class 19
measure("#1971 n=1e5 path graph", lambda: [[i, i + 1] for i in range(100_000 - 1)],
        lambda e: S.validPath(100_000, e, 0, 100_000 - 1), "13.0 MB", "20.0 MB")
def oranges():
    g = [[1] * 10 for _ in range(10)]; g[0][0] = 2; return g
measure("#994 10x10, one rotten corner", oranges, S.orangesRotting, "1.5 KB", "1.9 KB")

# ---------------- Class 20
measure("#207 V=2000 chain", lambda: [[i + 1, i] for i in range(1999)], lambda p: S.canFinish(2000, p), "266 KB", "259 KB")
measure("#210 V=2000 chain", lambda: [[i + 1, i] for i in range(1999)], lambda p: S.findOrder(2000, p), "266 KB", "276 KB")

# ---------------- Class 21
def times743():
    pairs = [(u, v) for u in range(1, 101) for v in range(1, 101) if u != v]
    return [[u, v, random.randint(1, 100)] for u, v in random.sample(pairs, 6000)]
measure("#743 V=100 E=6000 w=1..100", times743, lambda t: S.networkDelayTime(t, 100, 1), "469 KB", "590 KB")
# instrument the heap peak for #743
def heap_peak_743(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))
    dist, heap, pk, pushes = {}, [(0, k)], 1, 1
    import heapq
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = d
        for nxt, w in graph[node]:
            if nxt not in dist:
                heapq.heappush(heap, (d + w, nxt)); pushes += 1
        pk = max(pk, len(heap))
    return pk, pushes, max(dist.values())
t = times743(); print("   #743 heap peak entries, total pushes, max distance:", heap_peak_743(t, 100, 1))

def heights1631():
    h = [[1] * 100 for _ in range(100)]; h[99][99] = 5; return h
measure("#1631 100x100 flat except goal", heights1631, S.minimumEffortPath, "84 KB", "98 KB")
def heap_peak_1631(heights):
    import heapq
    rows, cols = len(heights), len(heights[0]); best = [[float('inf')] * cols for _ in range(rows)]
    best[0][0] = 0; heap = [(0, 0, 0)]; pk = 1; pushes = 1
    while heap:
        effort, r, c = heapq.heappop(heap)
        if r == rows - 1 and c == cols - 1:
            return pk, pushes
        if effort > best[r][c]:
            continue
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols:
                new = max(effort, abs(heights[nr][nc] - heights[r][c]))
                if new < best[nr][nc]:
                    best[nr][nc] = new; heapq.heappush(heap, (new, nr, nc)); pushes += 1
        pk = max(pk, len(heap))
print("   #1631 flat case: heap peak entries, pushes:", heap_peak_1631(heights1631()))
rh = [[random.randint(1, 10**6) for _ in range(100)] for _ in range(100)]
print("   #1631 random heights: heap peak entries, pushes:", heap_peak_1631(rh))

# ---------------- Class 22
measure("#547 n=200 identity matrix", lambda: [[1 if i == j else 0 for j in range(200)] for i in range(200)],
        S.findCircleNum, "325 KB", "1.8 KB")
measure("#684 n=1000 path + [1,n] last", lambda: [[i, i + 1] for i in range(1, 1000)] + [[1, 1000]],
        S.findRedundantConnection, "133 KB", "35 KB")

# ---------------- Class 23
def words8(n=10_000):
    return ["".join(random.choice(string.ascii_lowercase) for _ in range(8)) for _ in range(n)]
W = words8()
def build_trie(ws):
    t = S.Trie()
    for w in ws:
        t.insert(w)
    return t
_, _ = measure("#208 10,000 random 8-letter words", lambda: list(words8()), build_trie, "557 KB", "11.6 MB")
t = build_trie(W)
cnt, st = 0, [t.root]
while st:
    d = st.pop(); cnt += 1
    st.extend(v for k, v in d.items() if k != '$')
prefixes = sum(len({w[:d] for w in W}) for d in range(1, 9))
print(f"   #208 trie dict count incl. root: {cnt}; distinct prefixes: {prefixes};"
      f" key's own formula sum min(26^d,10000) = {sum(min(26**d, 10_000) for d in range(1, 9))}")
print("   sys.getsizeof({}) =", sys.getsizeof({}), "; {'a': {}} =", sys.getsizeof({'a': {}}),
      "; dict with 6 keys =", sys.getsizeof(dict.fromkeys('abcdef')))
def board12():
    return [[random.choice(string.ascii_lowercase) for _ in range(12)] for _ in range(12)]
measure("#212 10,000 words, 12x12 board", lambda: (words8(), board12()), lambda a: S.findWords(a[1], a[0]), "559 KB", "11.6 MB")

# ---------------- Class 24
measure("#78 n=10", lambda: list(range(-5, 5)), S.subsets, "416 B", "105 KB")
measure("#51 n=8", lambda: 8, S.solveNQueens, "28 B", "51 KB")

# ---------------- Class 25
measure("#55 n=10,000 all 1", lambda: [1] * 10_000, S.canJump, "78 KB", "200 B")
measure("#135 n=20,000 increasing", lambda: list(range(20_000)), S.candy, "703 KB", "696 KB")
measure("#135 n=50,000 increasing (real limit)", lambda: list(range(50_000)), S.candy, "-", "-")

# ---------------- Class 26
measure("#56 n=10,000 disjoint", lambda: [[3 * i, 3 * i + 1] for i in range(10_000)], S.merge, "1.3 MB", "869 KB")
measure("#218 n=10,000 rising, nested", lambda: [[i, 10**9, 10**6 + i] for i in range(10_000)], S.getSkyline, "1.6 MB", "3.4 MB")

# ---------------- Class 27
measure("#198 n=100 values<=400", lambda: [random.randint(257, 400) for _ in range(100)], S.rob, "3.6 KB", "150 B")
measure("#322 amount=10,000 coins [1,2,5]", lambda: [1, 2, 5], lambda c: S.coinChange(c, 10_000), "164 B", "316 KB")
dp_vals = None

# ---------------- Class 28
measure("#300 n=2,500 increasing", lambda: list(range(1, 2501)), S.lengthOfLIS, "88 KB", "81 KB")
def two_strings(n):
    return ("".join(random.choice(string.ascii_lowercase) for _ in range(n)),
            "".join(random.choice(string.ascii_lowercase) for _ in range(n)))
measure("#1143 m=n=1000 random", lambda: two_strings(1000), lambda a: S.longestCommonSubsequence(*a), "2.0 KB", "8.1 MB")

# ---------------- Class 29
measure("#72 m=n=500 random", lambda: two_strings(500), lambda a: S.minDistance(*a), "1.1 KB", "6.3 MB")
measure("#10 m=n=20", lambda: ("a" * 20, "a*" * 10), lambda a: S.isMatch(*a), "122 B", "4.9 KB")

# ---------------- Class 30
measure("#127 N=3125 over a-e, aaaaa->eeeee", lambda: ["".join(p) for p in itertools.product("abcde", repeat=5)],
        lambda wl: S.ladderLength("aaaaa", "eeeee", wl), "165 KB", "507 KB")
def run295(stream):
    mf = S.MedianFinder()
    for v in stream:
        mf.addNum(v)
    return mf
measure("#295 n=50,000 adds in [-1e5,1e5]", lambda: [random.randint(-10**5, 10**5) for _ in range(50_000)], run295, "1.3 MB", "1.8 MB")
