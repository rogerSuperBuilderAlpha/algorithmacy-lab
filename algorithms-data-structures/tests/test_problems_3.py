"""Correctness tests for 14 board solutions, #208 through #295 (Classes 24 to 30 of draft 3 and
Class 25's tries): LeetCode examples, edge cases, random inputs vs brute force, and runs at
LeetCode's constraint limits. Run: python3.13 -s test_problems_3.py"""
import copy, random, re, sys, time, itertools
from collections import Counter, deque
from functools import lru_cache
import board_solutions as S

random.seed(20261112)
RESULTS = []


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    if not cond:
        print(f"  FAIL {name} {str(detail)[:300]}")


def section(t):
    print(f"\n=== {t}")


# ---------------------------------------------------------------- #208
section("#208 Trie")
t = S.Trie(); out = []
t.insert("apple"); out.append(t.search("apple")); out.append(t.search("app"))
out.append(t.startsWith("app")); t.insert("app"); out.append(t.search("app"))
check("208 ex1", out == [True, False, True, True])
for trial in range(300):
    t = S.Trie(); words = set()
    for _ in range(60):
        op = random.choice(("insert", "search", "startsWith"))
        w = "".join(random.choice("ab") for _ in range(random.randint(1, 5)))
        if op == "insert":
            t.insert(w); words.add(w)
        elif op == "search":
            check("208 random search", t.search(w) == (w in words))
        else:
            check("208 random prefix", t.startsWith(w) == any(x.startswith(w) for x in words))
t = S.Trie(); w = "a" * 2000
t0 = time.perf_counter()
for i in range(10**4):
    t.insert(w); t.search(w); t.startsWith(w)
print(f"  3x10^4 calls on a 2000-letter word: {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #212
section("#212 findWords")
b1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
got = S.findWords(copy.deepcopy(b1), ["oath", "pea", "eat", "rain"])
print("  ex1 returned (order as produced):", got)
check("212 ex1 (as set)", sorted(got) == ["eat", "oath"])
check("212 ex2", S.findWords([["a","b"],["c","d"]], ["abcb"]) == [])
check("212 1x1", S.findWords([["a"]], ["a", "b", "aa"]) == ["a"])
check("212 prefix words", sorted(S.findWords([["a", "b"], ["c", "d"]], ["a", "ab", "abd", "abdc", "abdca"])) == ["a", "ab", "abd", "abdc"])


def exist(board, word):
    R, C = len(board), len(board[0])
    def dfs(r, c, i, used):
        if board[r][c] != word[i]:
            return False
        if i == len(word) - 1:
            return True
        used.add((r, c))
        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in used and dfs(nr, nc, i + 1, used):
                used.discard((r, c)); return True
        used.discard((r, c)); return False
    return any(dfs(r, c, 0, set()) for r in range(R) for c in range(C))


for trial in range(1500):
    R, C = random.randint(1, 4), random.randint(1, 4)
    board = [[random.choice("abc") for _ in range(C)] for _ in range(R)]
    words = list({"".join(random.choice("abc") for _ in range(random.randint(1, 6))) for _ in range(random.randint(1, 15))})
    got = S.findWords(copy.deepcopy(board), words)
    want = sorted(w for w in words if exist(board, w))
    check("212 random", sorted(got) == want and len(got) == len(set(got)), (board, words, got))
# heavy cases at the constraint limits (12x12 board, up to 3*10^4 words of length <= 10)
board = [["a"] * 12 for _ in range(12)]
words = ["a" * 9 + ch for ch in "bcdefghijklmnopqrstuvwxyz"]
t0 = time.perf_counter(); out = S.findWords(copy.deepcopy(board), words)
print(f"  12x12 all-'a' board, 25 words 'aaaaaaaaa?' (none present): {len(out)} found in {time.perf_counter()-t0:.1f} s")
rnd_board = [[random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(12)] for _ in range(12)]
words = list({"".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10)) for _ in range(30000)})
t0 = time.perf_counter(); out = S.findWords(copy.deepcopy(rnd_board), words)
print(f"  12x12 random board, 3x10^4 random 10-letter words: {len(out)} found in {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #78
section("#78 subsets")
canon = lambda res: sorted(tuple(sorted(s)) for s in res)
check("78 ex1", canon(S.subsets([1, 2, 3])) == canon([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))
check("78 ex1 exact order", S.subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
print("  ex1 returned order:", S.subsets([1, 2, 3]))
check("78 ex2", canon(S.subsets([0])) == canon([[], [0]]))
for trial in range(500):
    nums = random.sample(range(-10, 11), random.randint(1, 10))
    res = S.subsets(nums)
    want = sorted(tuple(sorted(c)) for r in range(len(nums) + 1) for c in itertools.combinations(nums, r))
    check("78 random", canon(res) == want and len(res) == 2 ** len(nums))

# ---------------------------------------------------------------- #51
section("#51 solveNQueens")
check("51 ex1", sorted(S.solveNQueens(4)) == sorted([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]))
check("51 ex2", S.solveNQueens(1) == [["Q"]])


def brute_queens(n):
    out = []
    for perm in itertools.permutations(range(n)):
        if len({r - c for r, c in enumerate(perm)}) == n and len({r + c for r, c in enumerate(perm)}) == n:
            out.append(["." * c + "Q" + "." * (n - c - 1) for c in perm])
    return sorted(out)


for n in range(1, 10):
    got = S.solveNQueens(n)
    check(f"51 n={n}", sorted(got) == brute_queens(n))
    print(f"  n={n}: {len(got)} solutions")
t0 = time.perf_counter(); S.solveNQueens(9)
print(f"  n=9 time: {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #55
section("#55 canJump")
check("55 ex1", S.canJump([2, 3, 1, 1, 4]) is True)
check("55 ex2", S.canJump([3, 2, 1, 0, 4]) is False)
check("55 single zero", S.canJump([0]) is True)
check("55 [0,1]", S.canJump([0, 1]) is False)
for trial in range(5000):
    nums = [random.randint(0, 3) for _ in range(random.randint(1, 12))]
    reach = [False] * len(nums); reach[0] = True
    for i in range(len(nums)):
        if reach[i]:
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                reach[j] = True
    check("55 random", S.canJump(nums) == reach[-1])

# ---------------------------------------------------------------- #135
section("#135 candy")
check("135 ex1", S.candy([1, 0, 2]) == 5)
check("135 ex2", S.candy([1, 2, 2]) == 4)
check("135 single", S.candy([5]) == 1)
check("135 all equal", S.candy([3, 3, 3]) == 3)
for trial in range(1500):
    n = random.randint(1, 6)
    r = [random.randint(0, 3) for _ in range(n)]
    best = min(sum(c) for c in itertools.product(range(1, n + 1), repeat=n)
               if all((r[i] <= r[i-1] or c[i] > c[i-1]) for i in range(1, n))
               and all((r[i] <= r[i+1] or c[i] > c[i+1]) for i in range(n - 1)))
    check("135 random (exhaustive)", S.candy(r) == best, r)
r = list(range(5 * 10**4))
t0 = time.perf_counter(); S.candy(r)
print(f"  n=5*10^4 increasing: {(time.perf_counter()-t0)*1000:.1f} ms")

# ---------------------------------------------------------------- #198
section("#198 rob")
check("198 ex1", S.rob([1, 2, 3, 1]) == 4)
check("198 ex2", S.rob([2, 7, 9, 3, 1]) == 12)
check("198 single", S.rob([0]) == 0)
check("198 two", S.rob([2, 1]) == 2)
for trial in range(3000):
    nums = [random.randint(0, 400) for _ in range(random.randint(1, 12))]
    best = 0
    for mask in range(1 << len(nums)):
        if mask & (mask >> 1) == 0:
            best = max(best, sum(v for i, v in enumerate(nums) if mask >> i & 1))
    check("198 random", S.rob(nums) == best)

# ---------------------------------------------------------------- #322
section("#322 coinChange")
check("322 ex1", S.coinChange([1, 2, 5], 11) == 3)
check("322 ex2", S.coinChange([2], 3) == -1)
check("322 ex3", S.coinChange([1], 0) == 0)
check("322 greedy trap", S.coinChange([1, 3, 4], 6) == 2)
check("322 huge coin", S.coinChange([2**31 - 1], 3) == -1)
for trial in range(3000):
    coins = random.sample(range(1, 15), random.randint(1, 4)); amount = random.randint(0, 40)
    dist = {0: 0}; q = deque([0])
    while q:
        a = q.popleft()
        for c in coins:
            if a + c <= amount and a + c not in dist:
                dist[a + c] = dist[a] + 1; q.append(a + c)
    check("322 random (BFS ref)", S.coinChange(coins, amount) == dist.get(amount, -1))
coins = list(range(1, 13))
t0 = time.perf_counter(); S.coinChange(coins, 10**4)
print(f"  12 coins, amount 10^4: {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #300
section("#300 lengthOfLIS")
check("300 ex1", S.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
check("300 ex2", S.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4)
check("300 ex3", S.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1)
check("300 single", S.lengthOfLIS([-10**4]) == 1)
for trial in range(1500):
    nums = [random.randint(-5, 5) for _ in range(random.randint(1, 11))]
    best = max(len(c) for r in range(1, len(nums) + 1) for c in itertools.combinations(nums, r)
               if all(a < b for a, b in zip(c, c[1:])))
    check("300 random (exhaustive)", S.lengthOfLIS(nums) == best)
nums = list(range(2500))
t0 = time.perf_counter(); S.lengthOfLIS(nums)
print(f"  n=2500 increasing: {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #1143
section("#1143 LCS")
check("1143 ex1", S.longestCommonSubsequence("abcde", "ace") == 3)
check("1143 ex2", S.longestCommonSubsequence("abc", "abc") == 3)
check("1143 ex3", S.longestCommonSubsequence("abc", "def") == 0)
for trial in range(1500):
    a = "".join(random.choice("abc") for _ in range(random.randint(1, 8)))
    b = "".join(random.choice("abc") for _ in range(random.randint(1, 8)))
    best = 0
    for r in range(len(a), 0, -1):
        if any(it_ok for it_ok in (all(ch in iter_b for ch in c) for c in itertools.combinations(a, r)
                                   for iter_b in [iter(b)])):
            best = r; break
    check("1143 random (exhaustive)", S.longestCommonSubsequence(a, b) == best, (a, b))
a = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1000))
b = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1000))
t0 = time.perf_counter(); v = S.longestCommonSubsequence(a, b)
print(f"  m=n=1000 random lowercase: LCS={v}, {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #72
section("#72 minDistance")
check("72 ex1", S.minDistance("horse", "ros") == 3)
check("72 ex2", S.minDistance("intention", "execution") == 5)
check("72 both empty", S.minDistance("", "") == 0)
check("72 one empty", S.minDistance("", "abc") == 3 and S.minDistance("abc", "") == 3)


def bfs_edit(a, b, alpha="ab"):
    maxlen = max(len(a), len(b)) + 1
    dist = {a: 0}; q = deque([a])
    while q:
        w = q.popleft()
        if w == b:
            return dist[w]
        nbrs = set()
        for i in range(len(w)):
            nbrs.add(w[:i] + w[i+1:])
            for ch in alpha:
                nbrs.add(w[:i] + ch + w[i+1:])
        if len(w) < maxlen:
            for i in range(len(w) + 1):
                for ch in alpha:
                    nbrs.add(w[:i] + ch + w[i:])
        for x in nbrs:
            if x not in dist:
                dist[x] = dist[w] + 1; q.append(x)


for trial in range(1500):
    a = "".join(random.choice("ab") for _ in range(random.randint(0, 5)))
    b = "".join(random.choice("ab") for _ in range(random.randint(0, 5)))
    check("72 random (BFS over strings)", S.minDistance(a, b) == bfs_edit(a, b), (a, b))
a = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(500))
b = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(500))
t0 = time.perf_counter(); v = S.minDistance(a, b)
print(f"  m=n=500 random lowercase: distance={v}, {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #10
section("#10 isMatch")
check("10 ex1", S.isMatch("aa", "a") is False)
check("10 ex2", S.isMatch("aa", "a*") is True)
check("10 ex3", S.isMatch("ab", ".*") is True)
check("10 mississippi", S.isMatch("mississippi", "mis*is*p*.") is False)
check("10 aab", S.isMatch("aab", "c*a*b") is True)
for trial in range(20000):
    s = "".join(random.choice("ab") for _ in range(random.randint(1, 6)))
    toks = []
    for _ in range(random.randint(1, 5)):
        tok = random.choice("ab.")
        if random.random() < 0.4:
            tok += "*"
        toks.append(tok)
    p = "".join(toks)[:20]
    check("10 random (re.fullmatch)", S.isMatch(s, p) == (re.fullmatch(p, s) is not None), (s, p))

# ---------------------------------------------------------------- #127
section("#127 ladderLength")
check("127 ex1", S.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5)
check("127 ex2", S.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0)
check("127 one step", S.ladderLength("a", "c", ["a", "b", "c"]) == 2)
for trial in range(2000):
    L = random.randint(1, 3)
    pool = ["".join(p) for p in itertools.product("abc", repeat=L)]
    wl = random.sample(pool, random.randint(1, len(pool)))
    bw = random.choice(pool); ew = random.choice([w for w in pool if w != bw] or [bw])
    if bw == ew:
        continue
    nodes = list(set(wl) | {bw})
    adj = {u: [v for v in nodes if v in wl and sum(x != y for x, y in zip(u, v)) == 1] for u in nodes}
    dist = {bw: 1}; q = deque([bw])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1; q.append(v)
    want = dist.get(ew, 0) if ew in wl else 0
    check("127 random (explicit graph BFS)", S.ladderLength(bw, ew, wl) == want, (bw, ew, wl))
pool = ["".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10)) for _ in range(4999)]
t0 = time.perf_counter(); S.ladderLength("a" * 10, pool[-1], pool)
print(f"  wordList 4999 random 10-letter words: {(time.perf_counter()-t0)*1000:.0f} ms")
pool = ["".join(p) for p in itertools.product("abcde", repeat=5)]
t0 = time.perf_counter(); v = S.ladderLength("aaaaa", "eeeee", pool)
print(f"  memory-estimate case (3125 words over a-e, aaaaa->eeeee): answer {v}, {(time.perf_counter()-t0)*1000:.0f} ms")

# ---------------------------------------------------------------- #295
section("#295 MedianFinder")
mf = S.MedianFinder(); mf.addNum(1); mf.addNum(2); a1 = mf.findMedian(); mf.addNum(3); a2 = mf.findMedian()
check("295 ex1", (a1, a2) == (1.5, 2.0))
print("  ex1 types:", type(a1).__name__, type(a2).__name__)
for trial in range(500):
    mf = S.MedianFinder(); seen = []
    for _ in range(40):
        v = random.randint(-10**5, 10**5); mf.addNum(v); seen.append(v); seen.sort()
        n = len(seen)
        want = seen[n // 2] if n % 2 else (seen[n // 2 - 1] + seen[n // 2]) / 2
        check("295 random", abs(mf.findMedian() - want) < 1e-5)
mf = S.MedianFinder()
t0 = time.perf_counter()
for i in range(25000):
    mf.addNum(random.randint(-10**5, 10**5)); mf.findMedian()
print(f"  5*10^4 calls: {(time.perf_counter()-t0)*1000:.0f} ms")

ok = sum(1 for _, c in RESULTS if c); bad = len(RESULTS) - ok
print(f"\nTOTAL checks: {len(RESULTS)}, passed {ok}, failed {bad}")
print("failures by test:", dict(Counter(n for n, c in RESULTS if not c)))
