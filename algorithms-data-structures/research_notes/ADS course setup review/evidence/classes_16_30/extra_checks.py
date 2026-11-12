"""Targeted checks of specific claims in the key (classes 16-30)."""
import ast, heapq, random, string, sys, time, tracemalloc, gc, itertools, inspect
import board_solutions as S
random.seed(11)

print("== deque import: run the #1971 board code exactly as printed (no import) in a fresh namespace")
src = inspect.getsource(S.validPath)
ns = {}
exec(src, ns)
try:
    ns["validPath"](3, [[0, 1], [1, 2], [2, 0]], 0, 2)
except NameError as e:
    print("   NameError:", e)

print("\n== #198 recurrence exactly as written in key step 2 (best[i] = first i houses; uses nums[i])")
def literal(nums):
    n = len(nums); best = [0] * (n + 1); best[0] = 0; best[1] = nums[0]
    for i in range(2, n + 1):
        best[i] = max(best[i - 1], best[i - 2] + nums[i])
    return best[n]
for nums in ([1, 2, 3, 1], [2, 7, 9, 3, 1]):
    try:
        print("  ", nums, "->", literal(nums))
    except IndexError as e:
        print("  ", nums, "-> IndexError:", e)
def corrected(nums):
    n = len(nums); best = [0] * (n + 1); best[1] = nums[0]
    for i in range(2, n + 1):
        best[i] = max(best[i - 1], best[i - 2] + nums[i - 1])
    return best[n]
print("   corrected (nums[i-1]):", corrected([1, 2, 3, 1]), corrected([2, 7, 9, 3, 1]))

print("\n== #295 heap operations per addNum (count heappush/heappop calls)")
calls = {"push": 0, "pop": 0}
orig_push, orig_pop = heapq.heappush, heapq.heappop
def cpush(h, x): calls["push"] += 1; return orig_push(h, x)
def cpop(h): calls["pop"] += 1; return orig_pop(h)
S.heapq.heappush, S.heapq.heappop = cpush, cpop
mf = S.MedianFinder(); per = []
for v in [5, 1, 9, 3, 7, 2, 8]:
    before = calls["push"] + calls["pop"]; mf.addNum(v); per.append(calls["push"] + calls["pop"] - before)
S.heapq.heappush, S.heapq.heappop = orig_push, orig_pop
print("   heap operations per addNum:", per, "max =", max(per))

print("\n== #1143 LCS of random lowercase strings, m = n = 1000 (10 samples), and new ints > 256 kept in the table")
def lcs_table(a, b):
    m, n = len(a), len(b); dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j-1] + 1 if a[i-1] == b[j-1] else max(dp[i-1][j], dp[i][j-1])
    return dp
vals, bigobjs = [], []
for _ in range(10):
    a = "".join(random.choice(string.ascii_lowercase) for _ in range(1000))
    b = "".join(random.choice(string.ascii_lowercase) for _ in range(1000))
    dp = lcs_table(a, b); vals.append(dp[-1][-1])
    bigobjs.append(len({id(x) for row in dp for x in row if x > 256}))
print("   LCS values:", vals, "mean", sum(vals) / len(vals))
print("   distinct int objects > 256 held by the table:", bigobjs, "-> bytes at 32 B each ~", max(bigobjs) * 32)

print("\n== #72 edit distance m = n = 500 random: distance, share of cells > 256, distinct new int objects > 256")
for _ in range(3):
    a = "".join(random.choice(string.ascii_lowercase) for _ in range(500))
    b = "".join(random.choice(string.ascii_lowercase) for _ in range(500))
    m, n = 500, 500; dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j-1] if a[i-1] == b[j-1] else 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    cells = sum(1 for row in dp for x in row if x > 256)
    objs = len({id(x) for row in dp for x in row if x > 256})
    print(f"   distance {dp[m][n]}; cells > 256: {cells} ({cells/251001:.1%}); distinct int objects > 256: {objs}")

print("\n== #703 at LeetCode's limits (k = 10^4, nums 10^4, 10^4 adds), clean harness")
nums = [random.randint(-10**4, 10**4) for _ in range(10**4)]; adds = [random.randint(-10**4, 10**4) for _ in range(10**4)]
gc.collect(); tracemalloc.start(); b0 = tracemalloc.get_traced_memory()[0]
obj = S.KthLargest(10**4, nums)
for v in adds: obj.add(v)
cur, pk = tracemalloc.get_traced_memory(); tracemalloc.stop()
print(f"   aux peak {(pk-b0)/1024:.1f} KiB, kept {(cur-b0)/1024:.1f} KiB; heap len {len(obj.heap)}")

print("\n== #127 heavier run: 5000 words of length 10 over {a,b,c}, all reachable from 'aaaaaaaaaa'")
pool = set()
while len(pool) < 5000:
    pool.add("".join(random.choice("abc") for _ in range(10)))
pool = sorted(pool); end = pool[-1]
t0 = time.perf_counter(); v = S.ladderLength("a" * 10, end, pool)
print(f"   answer {v}, {(time.perf_counter()-t0)*1000:.0f} ms")

print("\n== #212 heavier: 12x12 all-'a' board, 3x10^4 words = 10 pure a-runs + a^j followed by other letters")
board = [["a"] * 12 for _ in range(12)]
words = set()
for k in range(1, 11):
    words.add("a" * k)
while len(words) < 30000:  # long 'a' prefix, then 1-5 other letters (keeps deep 'a' trie paths alive)
    j = random.randint(5, 9); L = random.randint(j + 1, 10)
    words.add("a" * j + "".join(random.choice("bcdefghijklmnopqrstuvwxyz") for _ in range(L - j)))
t0 = time.perf_counter(); out = S.findWords([row[:] for row in board], sorted(words))
print(f"   found {len(out)} words in {time.perf_counter()-t0:.1f} s")

print("\n== Board-solution line counts (non-blank code lines of the transcribed function/class)")
for name in ["findWords", "solveNQueens", "candy", "getSkyline", "isMatch", "ladderLength", "MedianFinder",
             "searchBST", "isValidBST", "KthLargest", "topKFrequent", "floodFill", "numIslands", "validPath",
             "orangesRotting", "canFinish", "findOrder", "networkDelayTime", "minimumEffortPath", "findCircleNum",
             "findRedundantConnection", "Trie", "subsets", "canJump", "merge", "rob", "coinChange", "lengthOfLIS",
             "longestCommonSubsequence", "minDistance"]:
    lines = [l for l in inspect.getsource(getattr(S, name)).splitlines() if l.strip()]
    print(f"   {name:<26} {len(lines):>3} lines")
