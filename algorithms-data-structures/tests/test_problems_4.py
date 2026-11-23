"""Tests for the eight board problems added in draft 3.

#1122 and #75 (Class 11), #110 and #1382 (Class 15), #1334 and #787 (Class 21),
#1584 and #1489 (Class 23). Each problem runs LeetCode's examples, random
inputs checked against a slower brute-force solution, and one run at
LeetCode's size limits. The solutions come from solutions.py, which
extract_solutions.py builds from source/problems.md.
Run: python3.13 -s test_problems_4.py
"""
import heapq
import itertools
import random
import sys
import time

import solutions as S

random.seed(20261112)
INF = float('inf')
results = {}


def record(pid, ok, detail):
    results[pid] = ok
    print(f"#{pid}: {'PASS' if ok else 'FAIL'} | {detail}")


# ---------- tree helpers ----------
TreeNode = S.TreeNode


def build_tree(level):
    if not level or level[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in level]
    kids = iter(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        node.left = next(kids, None)
        node.right = next(kids, None)
    return nodes[0]


def random_tree(n, lo=-100, hi=100):
    if n == 0:
        return None
    nodes = [TreeNode(random.randint(lo, hi)) for _ in range(n)]
    for i in range(1, n):
        parent = nodes[random.randrange(i)]
        while True:
            side = random.choice(('left', 'right'))
            if getattr(parent, side) is None:
                setattr(parent, side, nodes[i])
                break
            parent = getattr(parent, side)
    return nodes[0]


def inorder(root):
    out, stack, node = [], [], root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out


def height_naive(node):
    if node is None:
        return 0
    return 1 + max(height_naive(node.left), height_naive(node.right))


def balanced_naive(node):
    if node is None:
        return True
    return (abs(height_naive(node.left) - height_naive(node.right)) <= 1
            and balanced_naive(node.left) and balanced_naive(node.right))


def is_bst(node, lo=-INF, hi=INF):
    if node is None:
        return True
    return lo < node.val < hi and is_bst(node.left, lo, node.val) and is_bst(node.right, node.val, hi)


# ---------- #1122 Relative Sort Array ----------
def ref_1122(arr1, arr2):
    pos = {x: i for i, x in enumerate(arr2)}
    return sorted(arr1, key=lambda x: (pos.get(x, len(arr2)), x))


bad = 0
ex = [(([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]), [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]),
      (([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]), [22, 28, 8, 6, 17, 44])]
for args, want in ex:
    bad += S.relativeSortArray(*args) != want
for _ in range(3000):
    arr1 = [random.randint(0, random.choice((10, 1000))) for _ in range(random.randint(1, 60))]
    arr2 = random.sample(sorted(set(arr1)), random.randint(1, len(set(arr1))))
    bad += S.relativeSortArray(list(arr1), list(arr2)) != ref_1122(arr1, arr2)
arr1 = [random.randint(0, 1000) for _ in range(1000)]
arr2 = random.sample(sorted(set(arr1)), min(1000, len(set(arr1))))
t = time.perf_counter(); S.relativeSortArray(arr1, arr2); t = time.perf_counter() - t
record(1122, bad == 0, f"examples 2, random 3000, bad={bad}; max-size run {t:.3f}s")

# ---------- #75 Sort Colors ----------
bad = 0
for nums, want in (([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]), ([2, 0, 1], [0, 1, 2])):
    a = list(nums); S.sortColors(a); bad += a != want
for _ in range(5000):
    nums = [random.randint(0, 2) for _ in range(random.randint(1, 40))]
    a = list(nums); r = S.sortColors(a); bad += a != sorted(nums) or r is not None
for nums in ([0], [1], [2], [2, 2, 2], [0, 0, 0], [2, 1, 0] * 100):
    a = list(nums); S.sortColors(a); bad += a != sorted(nums)
record(75, bad == 0, f"examples 2, edge 6, random 5000, bad={bad}")

# ---------- #110 Balanced Binary Tree ----------
bad = 0
for level, want in (([3, 9, 20, None, None, 15, 7], True), ([1, 2, 2, 3, 3, None, None, 4, 4], False), ([], True)):
    bad += S.isBalanced(build_tree(level)) != want
for _ in range(3000):
    root = random_tree(random.randint(0, 30))
    bad += S.isBalanced(root) != balanced_naive(root)
chain = None
for v in range(900):
    chain = TreeNode(v, chain, None)
chain_900 = S.isBalanced(chain)
chain = None
for v in range(1000):
    chain = TreeNode(v, chain, None)
try:
    S.isBalanced(chain)
    deep = 'returned'
except RecursionError:
    deep = 'RecursionError'
record(110, bad == 0 and chain_900 is False,
       f"examples 3, random 3000, bad={bad}; chain of 900 -> {chain_900}; chain of 1,000 -> {deep} (expected at Python's default limit)")

# ---------- #1382 Balance a Binary Search Tree ----------
def random_bst(values):
    root = None
    for v in values:
        if root is None:
            root = TreeNode(v); continue
        node = root
        while True:
            if v < node.val:
                if node.left is None:
                    node.left = TreeNode(v); break
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(v); break
                node = node.right
    return root


bad = 0
for level in ([1, None, 2, None, 3, None, 4], [2, 1, 3]):
    root = build_tree(level); before = inorder(root)
    out = S.balanceBST(root)
    bad += not (inorder(out) == before and is_bst(out) and balanced_naive(out))
for _ in range(2000):
    vals = random.sample(range(1, 10 ** 5 + 1), random.randint(1, 60))
    if random.random() < 0.3:
        vals.sort()
    root = random_bst(vals); before = inorder(root)
    out = S.balanceBST(root)
    bad += not (inorder(out) == before and is_bst(out) and balanced_naive(out))
chain = None
for v in range(10 ** 4, 0, -1):
    chain = TreeNode(v, None, chain)
t = time.perf_counter(); out = S.balanceBST(chain); t = time.perf_counter() - t
ok_chain = inorder(out) == list(range(1, 10 ** 4 + 1)) and height_naive(out) == 14
record(1382, bad == 0 and ok_chain, f"examples 2, random 2000, bad={bad}; 10,000-node chain balanced to height 14: {ok_chain} ({t:.3f}s)")

# ---------- #1334 Find the City ----------
def ref_1334(n, edges, threshold):
    adj = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a].append((b, w)); adj[b].append((a, w))
    best_city, fewest = -1, n + 1
    for s in range(n):
        dist = [INF] * n; dist[s] = 0; pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w; heapq.heappush(pq, (d + w, v))
        count = sum(1 for j in range(n) if j != s and dist[j] <= threshold)
        if count <= fewest:
            fewest, best_city = count, s
    return best_city


bad = 0
bad += S.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) != 3
bad += S.findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) != 0
for _ in range(1500):
    n = random.randint(2, 12)
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    chosen = random.sample(pairs, random.randint(1, len(pairs)))
    edges = [[a, b, random.randint(1, 20)] for a, b in chosen]
    th = random.randint(1, 40)
    bad += S.findTheCity(n, edges, th) != ref_1334(n, edges, th)
n = 100
edges = [[a, b, random.randint(1, 10 ** 4)] for a in range(n) for b in range(a + 1, n)]
t = time.perf_counter(); S.findTheCity(n, edges, 5000); t = time.perf_counter() - t
record(1334, bad == 0, f"examples 2, random 1500, bad={bad}; n = 100 with all 4,950 edges: {t:.3f}s")

# ---------- #787 Cheapest Flights Within K Stops ----------
def ref_787(n, flights, src, dst, k):
    best = INF
    adj = [[] for _ in range(n)]
    for a, b, p in flights:
        adj[a].append((b, p))
    stack = [(src, 0, 0)]  # node, cost, edges used
    seen_best = {}
    while stack:
        u, c, e = stack.pop()
        if u == dst:
            best = min(best, c); continue
        if e == k + 1:
            continue
        if seen_best.get((u, e), INF) <= c:
            continue
        seen_best[(u, e)] = c
        for v, p in adj[u]:
            stack.append((v, c + p, e + 1))
    return -1 if best == INF else best


bad = 0
fl = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
bad += S.findCheapestPrice(4, fl, 0, 3, 1) != 700
fl = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
bad += S.findCheapestPrice(3, fl, 0, 2, 1) != 200
bad += S.findCheapestPrice(3, fl, 0, 2, 0) != 500
for _ in range(2000):
    n = random.randint(2, 8)
    pairs = [(a, b) for a in range(n) for b in range(n) if a != b]
    chosen = random.sample(pairs, random.randint(0, min(len(pairs), n * (n - 1) // 2)))
    flights = [[a, b, random.randint(1, 50)] for a, b in chosen]
    src, dst = random.sample(range(n), 2)
    k = random.randint(0, n - 1)
    bad += S.findCheapestPrice(n, flights, src, dst, k) != ref_787(n, flights, src, dst, k)
n = 100
pairs = random.sample([(a, b) for a in range(n) for b in range(n) if a != b], n * (n - 1) // 2)
flights = [[a, b, random.randint(1, 10 ** 4)] for a, b in pairs]
t = time.perf_counter(); S.findCheapestPrice(n, flights, 0, 99, 99); t = time.perf_counter() - t
record(787, bad == 0, f"examples 3, random 2000, bad={bad}; n = 100, 4,950 flights, k = 99: {t:.3f}s")

# ---------- #1584 Min Cost to Connect All Points ----------
def ref_1584(points):
    n = len(points)
    es = sorted((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j)
                for i in range(n) for j in range(i + 1, n))
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    total = 0
    for w, i, j in es:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj; total += w
    return total


bad = 0
bad += S.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) != 20
bad += S.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) != 18
bad += S.minCostConnectPoints([[0, 0]]) != 0
for _ in range(1500):
    pts = set()
    while len(pts) < random.randint(1, 25):
        pts.add((random.randint(-50, 50), random.randint(-50, 50)))
    pts = [list(p) for p in pts]
    bad += S.minCostConnectPoints(pts) != ref_1584(pts)
pts = set()
while len(pts) < 1000:
    pts.add((random.randint(-10 ** 6, 10 ** 6), random.randint(-10 ** 6, 10 ** 6)))
pts = [list(p) for p in pts]
t = time.perf_counter(); S.minCostConnectPoints(pts); t = time.perf_counter() - t
record(1584, bad == 0, f"examples 2, edge 1, random 1500, bad={bad}; 1,000 points: {t:.3f}s")

# ---------- #1489 Critical and Pseudo-Critical Edges ----------
def ref_1489(n, edges):
    m = len(edges)
    weights = {}
    for combo in itertools.combinations(range(m), n - 1):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        ok = True
        for i in combo:
            a, b, _ = edges[i]
            ra, rb = find(a), find(b)
            if ra == rb:
                ok = False; break
            parent[ra] = rb
        if ok:
            weights[combo] = sum(edges[i][2] for i in combo)
    best = min(weights.values())
    msts = [set(c) for c, w in weights.items() if w == best]
    critical = sorted(i for i in range(m) if all(i in t for t in msts))
    pseudo = sorted(i for i in range(m) if any(i in t for t in msts) and i not in critical)
    return [critical, pseudo]


def norm(ans):
    return [sorted(ans[0]), sorted(ans[1])]


bad = 0
bad += norm(S.findCriticalAndPseudoCriticalEdges(5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]])) != [[0, 1], [2, 3, 4, 5]]
bad += norm(S.findCriticalAndPseudoCriticalEdges(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]])) != [[], [0, 1, 2, 3]]
for _ in range(600):
    n = random.randint(2, 6)
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    while True:
        chosen = random.sample(pairs, random.randint(n - 1, len(pairs)))
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for a, b in chosen:
            parent[find(a)] = find(b)
        if len({find(v) for v in range(n)}) == 1:
            break
    edges = [[a, b, random.randint(1, 4)] for a, b in chosen]
    bad += norm(S.findCriticalAndPseudoCriticalEdges(n, edges)) != ref_1489(n, edges)
n = 100
pairs = random.sample([(a, b) for a in range(n) for b in range(a + 1, n)], 200 - (n - 1))
pairs += [(i, i + 1) for i in range(n - 1)]
pairs = list(dict.fromkeys(pairs))[:200]
edges = [[a, b, random.randint(1, 1000)] for a, b in pairs]
t = time.perf_counter(); S.findCriticalAndPseudoCriticalEdges(n, edges); t = time.perf_counter() - t
record(1489, bad == 0, f"examples 2, random 600 checked against every spanning tree, bad={bad}; n = 100, 200 edges: {t:.3f}s")

passed = sum(results.values())
print(f"\nSUMMARY: {passed} PASS of {len(results)}")
sys.exit(0 if passed == len(results) else 1)
