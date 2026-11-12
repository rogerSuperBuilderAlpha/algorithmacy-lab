"""Correctness tests for 14 board solutions, #700 through #684 (Classes 14 to 22 of draft 3, apart
from Classes 15 and 21, which test_problems_4.py covers): LeetCode examples, edge cases, random
inputs vs brute force, and runs at LeetCode's constraint limits. Run: python3.13 -s test_problems_2.py"""
import copy, random, sys, time, itertools
from collections import Counter, deque
import board_solutions as S
from lc_types import TreeNode, build_tree, to_level, bst_insert, balanced_bst

random.seed(20261112)
RESULTS = []


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    if not cond:
        print(f"  FAIL {name} {detail}")


def section(t):
    print(f"\n=== {t}")


# ---------------------------------------------------------------- #700
section("#700 searchBST")
root = build_tree([4, 2, 7, 1, 3])
check("700 ex1", to_level(S.searchBST(root, 2)) == [2, 1, 3])
check("700 ex2", S.searchBST(root, 5) is None)
check("700 single hit", S.searchBST(TreeNode(1), 1).val == 1)
check("700 single miss", S.searchBST(TreeNode(1), 2) is None)
for t in range(2000):
    vals = random.sample(range(1, 200), random.randint(1, 40))
    r = None
    for v in vals:
        r = bst_insert(r, v)
    q = random.randint(1, 200)
    got = S.searchBST(r, q)
    # brute: scan every node
    want, st = None, [r]
    while st:
        n = st.pop()
        if n is None:
            continue
        if n.val == q:
            want = n
        st += [n.left, n.right]
    check("700 random", got is want, (vals, q))
chain = None
vals = list(range(1, 5001))
r = TreeNode(1); cur = r
for v in vals[1:]:
    cur.right = TreeNode(v); cur = cur.right
t0 = time.perf_counter(); got = S.searchBST(r, 5000); dt = time.perf_counter() - t0
check("700 5000-node chain", got is not None and got.val == 5000)
print(f"  5000-node right chain, val at bottom: {dt*1000:.2f} ms")

# ---------------------------------------------------------------- #98
section("#98 isValidBST")
check("98 ex1", S.isValidBST(build_tree([2, 1, 3])) is True)
check("98 ex2", S.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) is False)
check("98 single", S.isValidBST(TreeNode(0)) is True)
check("98 dup left", S.isValidBST(build_tree([2, 2])) is False)
check("98 dup right", S.isValidBST(build_tree([2, None, 2])) is False)
check("98 int min/max", S.isValidBST(build_tree([-2**31, None, 2**31 - 1])) is True)
check("98 deep violation", S.isValidBST(build_tree([5, 4, 6, None, None, 3, 7])) is False)


def children_only(node):
    """The 'common mistake' from key step 1: compare each node with its direct children only."""
    if node is None:
        return True
    if node.left and not node.left.val < node.val:
        return False
    if node.right and not node.right.val > node.val:
        return False
    return children_only(node.left) and children_only(node.right)


print("  children-only check on key's example [5,1,4,null,null,3,6]:",
      children_only(build_tree([5, 1, 4, None, None, 3, 6])))
print("  children-only check on [5,4,6,null,null,3,7]:",
      children_only(build_tree([5, 4, 6, None, None, 3, 7])))


def inorder_increasing(root):
    out, st, n = [], [], root
    while st or n:
        while n:
            st.append(n); n = n.left
        n = st.pop(); out.append(n.val); n = n.right
    return all(a < b for a, b in zip(out, out[1:]))


def random_tree(size, lo, hi):
    nodes = [TreeNode(random.randint(lo, hi)) for _ in range(size)]
    for i in range(1, size):
        while True:
            p = nodes[random.randrange(i)]
            side = random.choice(('left', 'right'))
            if getattr(p, side) is None:
                setattr(p, side, nodes[i]); break
    return nodes[0]


for t in range(3000):
    size = random.randint(1, 12)
    if t % 2:
        vals = sorted(random.sample(range(-20, 20), size))
        r = None
        for v in random.sample(vals, size):
            r = bst_insert(r, v)
        if random.random() < 0.5:  # perturb one value
            st, allnodes = [r], []
            while st:
                n = st.pop()
                if n: allnodes.append(n); st += [n.left, n.right]
            random.choice(allnodes).val = random.randint(-20, 20)
    else:
        r = random_tree(size, -3, 3)
    check("98 random", S.isValidBST(r) == inorder_increasing(r))
# deep chain: LeetCode allows up to 10^4 nodes; a sorted insertion order gives a chain
print("  sys.getrecursionlimit() =", sys.getrecursionlimit())
for depth in (900, 1000, 10_000):
    r = TreeNode(0); cur = r
    for v in range(1, depth):
        cur.right = TreeNode(v); cur = cur.right
    try:
        out = S.isValidBST(r)
        print(f"  right chain of {depth} nodes: returned {out}")
    except RecursionError as e:
        print(f"  right chain of {depth} nodes: RecursionError: {e}")

# ---------------------------------------------------------------- #703
section("#703 KthLargest")
obj = S.KthLargest(3, [4, 5, 8, 2])
check("703 ex1", [obj.add(v) for v in (3, 5, 10, 9, 4)] == [4, 5, 5, 8, 8])
obj = S.KthLargest(4, [7, 7, 7, 7, 8, 3])
check("703 ex2", [obj.add(v) for v in (2, 10, 9, 9)] == [7, 7, 7, 8])
obj = S.KthLargest(1, [])
check("703 empty nums k=1", [obj.add(v) for v in (-3, -2, -4, 0, 4)] == [-3, -2, -2, 0, 4])
for t in range(2000):
    nums = [random.randint(-5, 5) for _ in range(random.randint(0, 10))]
    k = random.randint(1, len(nums) + 1)
    obj = S.KthLargest(k, list(nums))
    seen = list(nums)
    for _ in range(10):
        v = random.randint(-5, 5); seen.append(v)
        check("703 random", obj.add(v) == sorted(seen, reverse=True)[k - 1])
nums = [random.randint(-10**4, 10**4) for _ in range(10**4)]
t0 = time.perf_counter(); obj = S.KthLargest(10**4, nums)
for _ in range(10**4): obj.add(random.randint(-10**4, 10**4))
print(f"  k=10^4, 10^4 nums, 10^4 adds: {(time.perf_counter()-t0)*1000:.1f} ms")

# ---------------------------------------------------------------- #347
section("#347 topKFrequent")
check("347 ex1", sorted(S.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2])
check("347 ex2", S.topKFrequent([1], 1) == [1])
check("347 ex3", sorted(S.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)) == [1, 2])
check("347 negatives", sorted(S.topKFrequent([-1, -1, -2], 1)) == [-1])
tested = 0
while tested < 2000:
    nums = [random.randint(-6, 6) for _ in range(random.randint(1, 30))]
    cnt = Counter(nums).most_common()
    k = random.randint(1, len(cnt))
    if k < len(cnt) and cnt[k - 1][1] == cnt[k][1]:
        continue  # LeetCode guarantees a unique answer
    tested += 1
    check("347 random", sorted(S.topKFrequent(nums, k)) == sorted(v for v, _ in cnt[:k]))
nums = [random.randint(-10**4, 10**4) for _ in range(10**5)]
t0 = time.perf_counter(); S.topKFrequent(nums, 100)
print(f"  n=10^5: {(time.perf_counter()-t0)*1000:.1f} ms; distinct values possible under constraints: {2*10**4+1}")

# ---------------------------------------------------------------- #733
section("#733 floodFill")
check("733 ex1", S.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
check("733 ex2", S.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]])
check("733 1x1", S.floodFill([[5]], 0, 0, 7) == [[7]])


def ref_fill(img, sr, sc, color):
    img = copy.deepcopy(img); old = img[sr][sc]
    R, C = len(img), len(img[0]); seen = {(sr, sc)}; q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen and img[nr][nc] == old:
                seen.add((nr, nc)); q.append((nr, nc))
    for r, c in seen:
        img[r][c] = color
    return img


for t in range(3000):
    R, C = random.randint(1, 7), random.randint(1, 7)
    img = [[random.randint(0, 2) for _ in range(C)] for _ in range(R)]
    sr, sc, col = random.randrange(R), random.randrange(C), random.randint(0, 2)
    check("733 random", S.floodFill(copy.deepcopy(img), sr, sc, col) == ref_fill(img, sr, sc, col))
img = [[0] * 50 for _ in range(50)]
t0 = time.perf_counter(); S.floodFill(img, 0, 0, 1)
print(f"  50x50 uniform: {(time.perf_counter()-t0)*1000:.2f} ms")

# ---------------------------------------------------------------- #200
section("#200 numIslands")
g1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
g2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
check("200 ex1", S.numIslands(copy.deepcopy(g1)) == 1)
check("200 ex2", S.numIslands(copy.deepcopy(g2)) == 3)
check("200 1x1 water", S.numIslands([["0"]]) == 0)
check("200 1x1 land", S.numIslands([["1"]]) == 1)
check("200 diagonal not connected", S.numIslands([["1", "0"], ["0", "1"]]) == 2)


def ref_islands(g):
    R, C = len(g), len(g[0]); parent = {}
    def f(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for r in range(R):
        for c in range(C):
            if g[r][c] == "1":
                parent[(r, c)] = (r, c)
    for r in range(R):
        for c in range(C):
            if g[r][c] == "1":
                for nr, nc in ((r+1, c), (r, c+1)):
                    if nr < R and nc < C and g[nr][nc] == "1":
                        a, b = f((r, c)), f((nr, nc))
                        if a != b: parent[a] = b
    return len({f(x) for x in parent})


for t in range(3000):
    R, C = random.randint(1, 8), random.randint(1, 8)
    g = [[random.choice("01") for _ in range(C)] for _ in range(R)]
    check("200 random", S.numIslands(copy.deepcopy(g)) == ref_islands(g))
g = [["1"] * 300 for _ in range(300)]
t0 = time.perf_counter(); S.numIslands(g)
print(f"  300x300 all land: {(time.perf_counter()-t0)*1000:.1f} ms")
g = [["1" if (r + c) % 2 == 0 else "0" for c in range(300)] for r in range(300)]
t0 = time.perf_counter(); out = S.numIslands(g)
print(f"  300x300 checkerboard ({out} islands): {(time.perf_counter()-t0)*1000:.1f} ms")

# ---------------------------------------------------------------- #1971
section("#1971 validPath")
check("1971 ex1", S.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True)
check("1971 ex2", S.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) is False)
check("1971 n=1 no edges", S.validPath(1, [], 0, 0) is True)
check("1971 src==dst isolated", S.validPath(3, [[0, 1]], 2, 2) is True)
for t in range(3000):
    n = random.randint(1, 9)
    pairs = [p for p in itertools.combinations(range(n), 2)]
    edges = [list(p) for p in random.sample(pairs, random.randint(0, len(pairs)))]
    s, d = random.randrange(n), random.randrange(n)
    reach = [[i == j for j in range(n)] for i in range(n)]
    for a, b in edges:
        reach[a][b] = reach[b][a] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
    check("1971 random", S.validPath(n, edges, s, d) == reach[s][d])
n = 2 * 10**5
edges = [[i, i + 1] for i in range(n - 1)]
t0 = time.perf_counter(); out = S.validPath(n, edges, 0, n - 1)
print(f"  n=2e5 path graph: {out} in {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #994
section("#994 orangesRotting")
check("994 ex1", S.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4)
check("994 ex2", S.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1)
check("994 ex3", S.orangesRotting([[0, 2]]) == 0)
check("994 all empty", S.orangesRotting([[0]]) == 0)
check("994 fresh only", S.orangesRotting([[1]]) == -1)
check("994 two sources", S.orangesRotting([[2, 1, 1, 1, 2]]) == 2)


def ref_rot(g):
    g = copy.deepcopy(g); R, C = len(g), len(g[0]); m = 0
    while True:
        if not any(1 in row for row in g):
            return m
        new = [(r, c) for r in range(R) for c in range(C) if g[r][c] == 1 and any(
            0 <= r+dr < R and 0 <= c+dc < C and g[r+dr][c+dc] == 2 for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))]
        if not new:
            return -1
        for r, c in new:
            g[r][c] = 2
        m += 1


for t in range(3000):
    R, C = random.randint(1, 6), random.randint(1, 6)
    g = [[random.choice((0, 1, 1, 2)) for _ in range(C)] for _ in range(R)]
    check("994 random", S.orangesRotting(copy.deepcopy(g)) == ref_rot(g))

# ---------------------------------------------------------------- #207 / #210
section("#207 canFinish / #210 findOrder")
check("207 ex1", S.canFinish(2, [[1, 0]]) is True)
check("207 ex2", S.canFinish(2, [[1, 0], [0, 1]]) is False)
check("210 ex1", S.findOrder(2, [[1, 0]]) == [0, 1])
o = S.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
check("210 ex2", o in ([0, 1, 2, 3], [0, 2, 1, 3]), o)
check("210 ex3", S.findOrder(1, []) == [0])
check("210 cycle", S.findOrder(3, [[0, 1], [1, 2], [2, 0]]) == [])
check("207 self-loop", S.canFinish(1, [[0, 0]]) is False)


def has_order_brute(n, pre):
    for perm in itertools.permutations(range(n)):
        pos = {c: i for i, c in enumerate(perm)}
        if all(pos[b] < pos[a] for a, b in pre):
            return True
    return False


for t in range(1500):
    n = random.randint(1, 6)
    pairs = [[a, b] for a in range(n) for b in range(n) if a != b]
    pre = random.sample(pairs, random.randint(0, min(len(pairs), 8)))
    want = has_order_brute(n, pre)
    check("207 random", S.canFinish(n, pre) == want)
    o = S.findOrder(n, pre)
    if want:
        pos = {c: i for i, c in enumerate(o)}
        check("210 random valid", sorted(o) == list(range(n)) and all(pos[b] < pos[a] for a, b in pre), (n, pre, o))
    else:
        check("210 random empty", o == [])
pre = [[i + 1, i] for i in range(1999)]
t0 = time.perf_counter(); S.canFinish(2000, pre); S.findOrder(2000, pre)
print(f"  V=2000 chain both: {(time.perf_counter()-t0)*1000:.1f} ms")

# ---------------------------------------------------------------- #743
section("#743 networkDelayTime")
check("743 ex1", S.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2)
check("743 ex2", S.networkDelayTime([[1, 2, 1]], 2, 1) == 1)
check("743 ex3", S.networkDelayTime([[1, 2, 1]], 2, 2) == -1)
check("743 zero weights", S.networkDelayTime([[1, 2, 0], [2, 3, 0]], 3, 1) == 0)
INF = float('inf')
for t in range(3000):
    n = random.randint(1, 7)
    pairs = [(u, v) for u in range(1, n + 1) for v in range(1, n + 1) if u != v]
    if not pairs:
        times = []
    else:
        times = [[u, v, random.randint(0, 10)] for u, v in random.sample(pairs, random.randint(1, len(pairs)))]
    k = random.randint(1, n)
    d = {i: INF for i in range(1, n + 1)}; d[k] = 0
    for _ in range(n):  # Bellman-Ford
        for u, v, w in times:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
    want = -1 if INF in d.values() else max(d.values())
    check("743 random", S.networkDelayTime(times, n, k) == want, (times, n, k))
pairs = [(u, v) for u in range(1, 101) for v in range(1, 101) if u != v]
times = [[u, v, random.randint(0, 100)] for u, v in random.sample(pairs, 6000)]
t0 = time.perf_counter(); S.networkDelayTime(times, 100, 1)
print(f"  V=100, E=6000: {(time.perf_counter()-t0)*1000:.1f} ms")

# ---------------------------------------------------------------- #1631
section("#1631 minimumEffortPath")
check("1631 ex1", S.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2)
check("1631 ex2", S.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1)
check("1631 ex3", S.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0)
check("1631 1x1", S.minimumEffortPath([[7]]) == 0)


def ref_effort(h):
    R, C = len(h), len(h[0])
    cands = sorted({0} | {abs(h[r][c] - h[nr][nc]) for r in range(R) for c in range(C)
                          for nr, nc in ((r+1, c), (r, c+1)) if nr < R and nc < C})
    for lim in cands:
        seen = {(0, 0)}; st = [(0, 0)]
        while st:
            r, c = st.pop()
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen and abs(h[nr][nc]-h[r][c]) <= lim:
                    seen.add((nr, nc)); st.append((nr, nc))
        if (R-1, C-1) in seen:
            return lim


for t in range(3000):
    R, C = random.randint(1, 6), random.randint(1, 6)
    h = [[random.randint(1, 20) for _ in range(C)] for _ in range(R)]
    check("1631 random", S.minimumEffortPath(h) == ref_effort(h))
h = [[random.randint(1, 10**6) for _ in range(100)] for _ in range(100)]
t0 = time.perf_counter(); S.minimumEffortPath(h)
print(f"  100x100 random heights: {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #547
section("#547 findCircleNum")
check("547 ex1", S.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
check("547 ex2", S.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3)
check("547 n=1", S.findCircleNum([[1]]) == 1)
for t in range(3000):
    n = random.randint(1, 9)
    m = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.25:
                m[i][j] = m[j][i] = 1
    seen, comps = set(), 0
    for i in range(n):
        if i not in seen:
            comps += 1; st = [i]; seen.add(i)
            while st:
                x = st.pop()
                for y in range(n):
                    if m[x][y] and y not in seen:
                        seen.add(y); st.append(y)
    check("547 random", S.findCircleNum(m) == comps)

# ---------------------------------------------------------------- #684
section("#684 findRedundantConnection")
check("684 ex1", S.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3])
check("684 ex2", S.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4])


def is_tree(n, es):
    p = list(range(n + 1))
    def f(x):
        while p[x] != x:
            x = p[x]
        return x
    for a, b in es:
        ra, rb = f(a), f(b)
        if ra == rb:
            return False
        p[ra] = rb
    return len(es) == n - 1


for t in range(3000):
    n = random.randint(3, 9)
    perm = list(range(1, n + 1)); random.shuffle(perm)
    es = [sorted([perm[i], perm[random.randrange(i)]]) for i in range(1, n)]
    existing = {tuple(e) for e in es}
    extra = random.choice([(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1) if (a, b) not in existing])
    es.append(list(extra)); random.shuffle(es)
    want = next(e for e in reversed(es) if is_tree(n, [x for x in es if x is not e]))
    check("684 random", S.findRedundantConnection(es) == want, es)

ok = sum(1 for _, c in RESULTS if c); bad = len(RESULTS) - ok
print(f"\nTOTAL checks: {len(RESULTS)}, passed {ok}, failed {bad}")
fails = Counter(n for n, c in RESULTS if not c)
print("failures by test:", dict(fails))
