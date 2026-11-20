# Correctness tests for the 30 board solutions of classes 1-15.
# For each problem: LeetCode examples (from fetched/digest.txt), edge cases,
# random inputs compared with a brute-force reference, and one timed run at
# LeetCode's maximum constraint. Run: python3.13 -I test_correctness.py
import sys, os, random, time, math, copy
from collections import Counter, deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import board as B
from board import ListNode, TreeNode

random.seed(20261112)
RESULTS = []


def check(name, cases, fn, ref, eq=lambda a, b: a == b):
    """cases: list of argument tuples. fn/ref receive deep copies."""
    bad = []
    for args in cases:
        got = fn(*copy.deepcopy(args))
        exp = ref(*copy.deepcopy(args))
        if not eq(got, exp):
            bad.append((args, got, exp))
    return bad


def report(pid, examples_bad, edge_bad, rand_bad, n_rand, timing):
    status = 'PASS' if not (examples_bad or edge_bad or rand_bad) else 'FAIL'
    RESULTS.append((pid, status))
    print(f'#{pid}: {status} | examples bad={len(examples_bad)} edge bad={len(edge_bad)} '
          f'random {n_rand} bad={len(rand_bad)} | {timing}')
    for lst in (examples_bad, edge_bad, rand_bad):
        for args, got, exp in lst[:3]:
            print('    FAIL args=', str(args)[:200], 'got=', str(got)[:120], 'exp=', str(exp)[:120])


def timed(f, *args):
    t = time.perf_counter(); f(*args); return f'max-size run {time.perf_counter() - t:.3f}s'


# ---------- helpers for in-place problems ----------
def inplace(f):
    def g(*args):
        f(*args); return args[0]
    return g


def to_ll(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def from_ll(head):
    out = []
    while head:
        out.append(head.val); head = head.next
    return out


def build_tree(vals):  # LeetCode level-order list with None
    if not vals or vals[0] is None:
        return None
    it = iter(vals)
    root = TreeNode(next(it)); q = deque([root])
    while q:
        node = q.popleft()
        try:
            v = next(it)
            if v is not None:
                node.left = TreeNode(v); q.append(node.left)
            v = next(it)
            if v is not None:
                node.right = TreeNode(v); q.append(node.right)
        except StopIteration:
            break
    return root


def random_tree(n, lo=-100, hi=100):
    if n == 0:
        return None
    nodes = [TreeNode(random.randint(lo, hi)) for _ in range(n)]
    for i in range(1, n):  # attach each node to a random earlier node with a free slot
        while True:
            p = nodes[random.randrange(i)]
            side = random.choice(('left', 'right'))
            if getattr(p, side) is None:
                setattr(p, side, nodes[i]); break
    return nodes[0]


def ri(lo, hi): return random.randint(lo, hi)


# 1480 running sum
ex = [([1, 2, 3, 4],), ([1, 1, 1, 1, 1],), ([3, 1, 2, 10, 1],)]
edge = [([5],), ([-10**6] * 1000,), ([10**6] * 1000,), ([0],)]
rnd = [([ri(-10**6, 10**6) for _ in range(ri(1, 30))],) for _ in range(2000)]
ref = lambda nums: [sum(nums[:i + 1]) for i in range(len(nums))]
report(1480, check(0, ex, B.runningSum, ref), check(0, edge, B.runningSum, ref),
       check(0, rnd, B.runningSum, ref), len(rnd), timed(B.runningSum, [ri(-10**6, 10**6) for _ in range(1000)]))

# 217 contains duplicate
ex = [([1, 2, 3, 1],), ([1, 2, 3, 4],), ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],)]
edge = [([7],), ([-10**9, 10**9],), ([-10**9, -10**9],), (list(range(10**5)),)]
rnd = [([ri(-20, 20) for _ in range(ri(1, 15))],) for _ in range(2000)]
ref = lambda nums: any(nums[i] == nums[j] for i in range(len(nums)) for j in range(i + 1, len(nums)))
report(217, check(0, ex, B.containsDuplicate, ref), check(0, edge[:3], B.containsDuplicate, ref),
       check(0, rnd, B.containsDuplicate, ref), len(rnd), timed(B.containsDuplicate, random.sample(range(-10**9, 10**9), 10**5)))

# 283 move zeroes
f = inplace(B.moveZeroes)
ex = [([0, 1, 0, 3, 12],), ([0],)]
edge = [([1],), ([0, 0, 0],), ([1, 2, 3],), ([-2**31, 0, 2**31 - 1],)]
rnd = [([random.choice([0, 0, ri(-2**31, 2**31 - 1)]) for _ in range(ri(1, 20))],) for _ in range(2000)]
ref = lambda nums: [x for x in nums if x != 0] + [0] * nums.count(0)
report(283, check(0, ex, f, ref), check(0, edge, f, ref), check(0, rnd, f, ref), len(rnd),
       timed(B.moveZeroes, [random.choice([0, ri(1, 99)]) for _ in range(10**4)]))

# 88 merge sorted array
f = inplace(B.merge)
def mk88(m, n, lo=-10**9, hi=10**9):
    a = sorted(ri(lo, hi) for _ in range(m)); b = sorted(ri(lo, hi) for _ in range(n))
    return (a + [0] * n, m, b, n)
ex = [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), ([1], 1, [], 0), ([0], 0, [1], 1)]
edge = [([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3), ([2, 2, 0, 0], 2, [2, 2], 2), mk88(0, 200), mk88(200, 0), mk88(100, 100)]
rnd = [mk88(ri(0, 10), ri(0, 10), -5, 5) for _ in range(2000)]
rnd = [c for c in rnd if c[1] + c[3] >= 1]
ref = lambda a, m, b, n: sorted(a[:m] + b)
report(88, check(0, ex, f, ref), check(0, edge, f, ref), check(0, rnd, f, ref), len(rnd), timed(B.merge, *mk88(100, 100)))

# 14 longest common prefix
ex = [(["flower", "flow", "flight"],), (["dog", "racecar", "car"],)]
edge = [([""],), (["a"],), (["", "abc"],), (["abc", ""],), (["ab", "a"],), (["a" * 200] * 200,), (["abc", "abc"],)]
alpha = 'ab'
rnd = [([''.join(random.choice(alpha) for _ in range(ri(0, 6))) for _ in range(ri(1, 6))],) for _ in range(3000)]
def ref14(strs):
    best = ''
    for L in range(min(len(s) for s in strs) + 1):
        p = strs[0][:L]
        if all(s.startswith(p) for s in strs):
            best = p
    return best
report(14, check(0, ex, B.longestCommonPrefix, ref14), check(0, edge, B.longestCommonPrefix, ref14),
       check(0, rnd, B.longestCommonPrefix, ref14), len(rnd), timed(B.longestCommonPrefix, ['a' * 200 for _ in range(200)]))

# 303 range sum query
def run303(nums, queries):
    obj = B.NumArray(nums); return [obj.sumRange(l, r) for l, r in queries]
def ref303(nums, queries):
    return [sum(nums[l:r + 1]) for l, r in queries]
def mk303(n, q, lo=-10**5, hi=10**5):
    nums = [ri(lo, hi) for _ in range(n)]
    qs = []
    for _ in range(q):
        l = ri(0, n - 1); r = ri(l, n - 1); qs.append((l, r))
    return (nums, qs)
ex = [([-2, 0, 3, -5, 2, -1], [(0, 2), (2, 5), (0, 5)])]
edge = [([7], [(0, 0)]), ([10**5] * 10**4, [(0, 9999), (9999, 9999)]), ([-10**5] * 10, [(0, 9)])]
rnd = [mk303(ri(1, 15), 10) for _ in range(1000)]
nums_big, qs_big = mk303(10**4, 10**4)
report(303, check(0, ex, run303, ref303), check(0, edge, run303, ref303), check(0, rnd, run303, ref303), len(rnd),
       timed(run303, nums_big, qs_big))

# 242 valid anagram
ex = [("anagram", "nagaram"), ("rat", "car")]
edge = [("a", "a"), ("a", "b"), ("ab", "a"), ("a", "ab"), ("aab", "abb"), ("z" * 50000, "z" * 50000)]
rnd = []
for _ in range(3000):
    s = ''.join(random.choice('abc') for _ in range(ri(1, 6)))
    t = ''.join(random.sample(s, len(s))) if random.random() < 0.5 else ''.join(random.choice('abc') for _ in range(ri(1, 6)))
    rnd.append((s, t))
ref = lambda s, t: sorted(s) == sorted(t)
big = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(50000))
report(242, check(0, ex, B.isAnagram, ref), check(0, edge, B.isAnagram, ref), check(0, rnd, B.isAnagram, ref), len(rnd),
       timed(B.isAnagram, big, ''.join(sorted(big))))

# 1 two sum: answer valid if indexes differ and sum matches (any order accepted)
def eq1(got, exp_args):
    nums, target = exp_args
    return got is not None and len(got) == 2 and got[0] != got[1] and nums[got[0]] + nums[got[1]] == target
def check1(cases):
    bad = []
    for nums, target in cases:
        got = B.twoSum(list(nums), target)
        if not eq1(got, (nums, target)):
            bad.append(((nums, target), got, 'valid pair'))
    return bad
def mk1(n, lo=-10**9, hi=10**9):
    while True:  # exactly one valid pair
        nums = [ri(lo, hi) for _ in range(n)]
        i, j = random.sample(range(n), 2); target = nums[i] + nums[j]
        cnt = sum(1 for a in range(n) for b in range(a + 1, n) if nums[a] + nums[b] == target)
        if cnt == 1 and -10**9 <= target <= 10**9:
            return (nums, target)
ex = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]
edge = [([0, 0], 0), ([-10**9, 10**9], 0), ([-3, 4, 3, 90], 0), ([5, 1, 5], 10)]
rnd = [mk1(ri(2, 10), -20, 20) for _ in range(2000)]
bigN = random.sample(range(10**6, 10**9), 10**4); big_t = bigN[-1] + bigN[-2]
report(1, check1(ex), check1(edge), check1(rnd), len(rnd), timed(B.twoSum, bigN, big_t))

# 125 valid palindrome
import string
printable = string.printable[:95]  # printable ASCII incl. space
ex = [("A man, a plan, a canal: Panama",), ("race a car",), (" ",)]
edge = [("a",), ("0P",), ("ab_a",), (".,",), ("a.",), ("Aa",), ("1b1",), ("a" * 200000,)]
rnd = [(''.join(random.choice('aAb1 ,.:') for _ in range(ri(1, 10))),) for _ in range(5000)]
rnd += [(''.join(random.choice(printable) for _ in range(ri(1, 8))),) for _ in range(3000)]
def ref125(s):
    c = [ch.lower() for ch in s if ch.isalnum()]; return c == c[::-1]
report(125, check(0, ex, B.isPalindrome, ref125), check(0, edge, B.isPalindrome, ref125),
       check(0, rnd, B.isPalindrome, ref125), len(rnd), timed(B.isPalindrome, 'a' * 200000))

# 977 squares
ex = [([-4, -1, 0, 3, 10],), ([-7, -3, 2, 3, 11],)]
edge = [([0],), ([-10**4],), ([-10**4, 10**4],), ([-5, -3, -1],), ([1, 2, 3],), ([-2, -2, 2, 2],)]
rnd = [(sorted(ri(-10, 10) for _ in range(ri(1, 12))),) for _ in range(3000)]
ref = lambda nums: sorted(x * x for x in nums)
report(977, check(0, ex, B.sortedSquares, ref), check(0, edge, B.sortedSquares, ref),
       check(0, rnd, B.sortedSquares, ref), len(rnd), timed(B.sortedSquares, sorted(ri(-10**4, 10**4) for _ in range(10**4))))

# 643 max average
ex = [([1, 12, -5, -6, 50, 3], 4), ([5], 1)]
edge = [([-10**4] * 5, 5), ([10**4] * 5, 1), ([-1, -2, -3], 2), ([3, -1, 4], 3)]
rnd = []
for _ in range(3000):
    n = ri(1, 12); rnd.append(([ri(-10**4, 10**4) for _ in range(n)], ri(1, n)))
ref = lambda nums, k: max(sum(nums[i:i + k]) for i in range(len(nums) - k + 1)) / k
close = lambda a, b: abs(a - b) < 1e-5
report(643, check(0, ex, B.findMaxAverage, ref, close), check(0, edge, B.findMaxAverage, ref, close),
       check(0, rnd, B.findMaxAverage, ref, close), len(rnd),
       timed(B.findMaxAverage, [ri(-10**4, 10**4) for _ in range(10**5)], 50000))

# 121 stock
ex = [([7, 1, 5, 3, 6, 4],), ([7, 6, 4, 3, 1],)]
edge = [([5],), ([1, 10**4],), ([10**4, 0],), ([2, 2, 2],), ([0, 10**4, 0, 10**4],)]
rnd = [([ri(0, 20) for _ in range(ri(1, 12))],) for _ in range(3000)]
ref = lambda p: max([0] + [p[j] - p[i] for i in range(len(p)) for j in range(i + 1, len(p))])
report(121, check(0, ex, B.maxProfit, ref), check(0, edge, B.maxProfit, ref), check(0, rnd, B.maxProfit, ref), len(rnd),
       timed(B.maxProfit, [ri(0, 10**4) for _ in range(10**5)]))

# 20 valid parentheses
ex = [("()",), ("()[]{}",), ("(]",), ("([])",), ("([)]",)]
edge = [("(",), (")",), ("]",), ("((",), ("(" * 10**4,), ("()" * 5000,), ("{[]}",)]
rnd = [(''.join(random.choice('()[]{}') for _ in range(ri(1, 10))),) for _ in range(5000)]
def ref20(s):
    prev = None
    while prev != s:
        prev = s; s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return s == ''
report(20, check(0, ex, B.isValid, ref20), check(0, edge, B.isValid, ref20), check(0, rnd, B.isValid, ref20), len(rnd),
       timed(B.isValid, '(' * 5000 + ')' * 5000))

# 844 backspace
ex = [("ab#c", "ad#c"), ("ab##", "c#d#"), ("a#c", "b")]
edge = [("#", "#"), ("a##", "#"), ("#a", "a"), ("a", "a#"), ("z" * 200, "z" * 200)]
rnd = [(''.join(random.choice('ab#') for _ in range(ri(1, 8))), ''.join(random.choice('ab#') for _ in range(ri(1, 8)))) for _ in range(5000)]
def typed(x):
    out = ''
    for c in x:
        out = out[:-1] if c == '#' else out + c
    return out
ref = lambda s, t: typed(s) == typed(t)
report(844, check(0, ex, B.backspaceCompare, ref), check(0, edge, B.backspaceCompare, ref),
       check(0, rnd, B.backspaceCompare, ref), len(rnd), timed(B.backspaceCompare, 'a' * 200, 'a' * 200))

# 933 recent counter
def run933(ts):
    rc = B.RecentCounter(); return [rc.ping(t) for t in ts]
def ref933(ts):
    return [sum(1 for u in ts[:i + 1] if t - 3000 <= u <= t) for i, t in enumerate(ts)]
def mk933(k, gap):
    t = 0; out = []
    for _ in range(k):
        t += ri(1, gap); out.append(t)
    return (out,)
ex = [([1, 100, 3001, 3002],)]
edge = [([1],), ([10**9],), ([1, 3001, 3002, 6002],), ([10**9 - 5000, 10**9 - 2000, 10**9],)]
rnd = [mk933(ri(1, 40), random.choice([10, 300, 2000, 4000])) for _ in range(2000)]
report(933, check(0, ex, run933, ref933), check(0, edge, run933, ref933), check(0, rnd, run933, ref933), len(rnd),
       timed(run933, list(range(1, 10**4 + 1))))

# 232 queue with stacks, random op sequences vs deque
def run232(ops):
    q = B.MyQueue(); out = []
    for op, x in ops:
        if op == 'push': out.append(q.push(x))
        elif op == 'pop': out.append(q.pop())
        elif op == 'peek': out.append(q.peek())
        else: out.append(q.empty())
    return out
def ref232(ops):
    d = deque(); out = []
    for op, x in ops:
        if op == 'push': d.append(x); out.append(None)
        elif op == 'pop': out.append(d.popleft())
        elif op == 'peek': out.append(d[0])
        else: out.append(len(d) == 0)
    return out
def mk232(k):
    ops = []; size = 0
    for _ in range(k):
        choices = ['push', 'empty'] + (['pop', 'peek'] if size else [])
        op = random.choice(choices)
        if op == 'push': size += 1
        if op == 'pop': size -= 1
        ops.append((op, ri(1, 9)))
    return (ops,)
ex = [([('push', 1), ('push', 2), ('peek', 0), ('pop', 0), ('empty', 0)],)]
edge = [([('empty', 0)],), ([('push', 9), ('pop', 0), ('empty', 0)],)]
rnd = [mk232(ri(1, 100)) for _ in range(2000)]
report(232, check(0, ex, run232, ref232), check(0, edge, run232, ref232), check(0, rnd, run232, ref232), len(rnd),
       timed(run232, mk232(100)[0]))

# 496 next greater element I
def ref496(nums1, nums2):
    out = []
    for x in nums1:
        j = nums2.index(x); nxt = -1
        for y in nums2[j + 1:]:
            if y > x: nxt = y; break
        out.append(nxt)
    return out
def mk496(n2):
    nums2 = random.sample(range(0, 10**4 + 1), n2); nums1 = random.sample(nums2, ri(1, n2)); return (nums1, nums2)
ex = [([4, 1, 2], [1, 3, 4, 2]), ([2, 4], [1, 2, 3, 4])]
edge = [([5], [5]), ([0], [0, 10**4]), (list(range(1000, 0, -1)), list(range(1000, 0, -1))), (list(range(1000)), list(range(1000)))]
rnd = [mk496(ri(1, 12)) for _ in range(3000)]
report(496, check(0, ex, B.nextGreaterElement, ref496), check(0, edge, B.nextGreaterElement, ref496),
       check(0, rnd, B.nextGreaterElement, ref496), len(rnd), timed(B.nextGreaterElement, *mk496(1000)))

# 739 daily temperatures
def ref739(T):
    out = []
    for i, t in enumerate(T):
        w = 0
        for j in range(i + 1, len(T)):
            if T[j] > t: w = j - i; break
        out.append(w)
    return out
ex = [([73, 74, 75, 71, 69, 72, 76, 73],), ([30, 40, 50, 60],), ([30, 60, 90],)]
edge = [([30],), ([100] * 50,), (list(range(100, 29, -1)),), ([30, 100],)]
rnd = [([ri(30, 40) for _ in range(ri(1, 15))],) for _ in range(3000)]
report(739, check(0, ex, B.dailyTemperatures, ref739), check(0, edge, B.dailyTemperatures, ref739),
       check(0, rnd, B.dailyTemperatures, ref739), len(rnd), timed(B.dailyTemperatures, [ri(30, 100) for _ in range(10**5)]))

# 206 reverse linked list
run206 = lambda vals: from_ll(B.reverseList(to_ll(vals)))
ref = lambda vals: vals[::-1]
ex = [([1, 2, 3, 4, 5],), ([1, 2],), ([],)]
edge = [([7],), ([-5000, 5000],), (list(range(5000)),)]
rnd = [([ri(-5000, 5000) for _ in range(ri(0, 15))],) for _ in range(2000)]
big = to_ll(list(range(5000)))
report(206, check(0, ex, run206, ref), check(0, edge, run206, ref), check(0, rnd, run206, ref), len(rnd), timed(B.reverseList, big))

# 19 remove nth from end
run19 = lambda vals, n: from_ll(B.removeNthFromEnd(to_ll(vals), n))
def ref19(vals, n):
    v = list(vals); del v[len(v) - n]; return v
ex = [([1, 2, 3, 4, 5], 2), ([1], 1), ([1, 2], 1)]
edge = [([1, 2], 2), (list(range(30)), 30), (list(range(30)), 1), ([0, 100, 0], 2)]
rnd = []
for _ in range(3000):
    L = ri(1, 30); rnd.append(([ri(0, 100) for _ in range(L)], ri(1, L)))
report(19, check(0, ex, run19, ref19), check(0, edge, run19, ref19), check(0, rnd, run19, ref19), len(rnd),
       timed(run19, list(range(30)), 15))

# 509 fibonacci
def ref509(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
ex = [(2,), (3,), (4,)]
edge = [(0,), (1,), (30,)]
rnd = [(n,) for n in range(31)]
report(509, check(0, ex, B.fib, ref509), check(0, edge, B.fib, ref509), check(0, rnd, B.fib, ref509), len(rnd), timed(B.fib, 30))

# 50 pow(x, n): compare with Python's float ** within LeetCode-style tolerance
def close50(a, b):
    return abs(a - b) <= 1e-5 or (b != 0 and abs(a - b) / abs(b) < 1e-9)
def ref50(x, n):
    return x ** n
def mk50():
    while True:  # respect constraints: -100<x<100, |x^n|<=1e4, x!=0 or n>0
        x = round(random.uniform(-99.99, 99.99), 5); n = ri(-2**31, 2**31 - 1) if random.random() < 0.3 else ri(-40, 40)
        if x == 0 and n <= 0: continue
        try:
            v = x ** n
        except (OverflowError, ZeroDivisionError):
            continue
        if abs(v) <= 1e4: return (x, n)
ex = [(2.0, 10), (2.1, 3), (2.0, -2)]
edge = [(1.0, 2**31 - 1), (1.0, -2**31), (-1.0, -2**31), (-1.0, 2**31 - 1), (2.0, -2**31), (0.0, 5), (0.00001, 2**31 - 1),
        (99.99999, 2), (-99.99999, 2), (1.0000001, 92000000), (1.0000001, -92000000), (0.5, 13)]  # 1.0000001**92e6 ~ 9.9e3, inside |x^n|<=1e4
rnd = [mk50() for _ in range(5000)]
report(50, check(0, ex, B.myPow, ref50, close50), check(0, edge, B.myPow, ref50, close50),
       check(0, rnd, B.myPow, ref50, close50), len(rnd), timed(B.myPow, 1.0, -2**31))

# 136 single number
def mk136(pairs, lo=-3 * 10**4, hi=3 * 10**4):
    vals = random.sample(range(lo, hi + 1), pairs + 1); nums = vals[:-1] * 2 + [vals[-1]]; random.shuffle(nums); return (nums,)
ref = lambda nums: [k for k, c in Counter(nums).items() if c == 1][0]
ex = [([2, 2, 1],), ([4, 1, 2, 1, 2],), ([1],)]
edge = [([-3 * 10**4],), ([3 * 10**4, -3 * 10**4, 3 * 10**4],), ([0, 5, 5],)]
rnd = [mk136(ri(0, 8)) for _ in range(3000)]
report(136, check(0, ex, B.singleNumber_136, ref), check(0, edge, B.singleNumber_136, ref),
       check(0, rnd, B.singleNumber_136, ref), len(rnd), timed(B.singleNumber_136, mk136(14999)[0]))

# 260 single number III (any order)
def mk260(pairs, lo=-2**31, hi=2**31 - 1):
    vals = random.sample(range(lo, hi + 1), pairs + 2) if hi - lo > 100 else random.sample(range(lo, hi + 1), pairs + 2)
    nums = vals[:pairs] * 2 + vals[pairs:]; random.shuffle(nums); return (nums,)
ref = lambda nums: sorted(k for k, c in Counter(nums).items() if c == 1)
eq = lambda got, exp: sorted(got) == exp
ex = [([1, 2, 1, 3, 2, 5],), ([-1, 0],), ([0, 1],)]
edge = [([-2**31, 0],), ([-2**31, 2**31 - 1],), ([2**31 - 1, -1],), ([-1, -2, 5, 5],), ([-2**31, -2**31 + 1, 7, 7],)]
rnd = [mk260(ri(0, 8)) for _ in range(3000)] + [mk260(ri(0, 6), -8, 8) for _ in range(3000)]
report(260, check(0, ex, B.singleNumber_260, ref, eq), check(0, edge, B.singleNumber_260, ref, eq),
       check(0, rnd, B.singleNumber_260, ref, eq), len(rnd), timed(B.singleNumber_260, mk260(14999)[0]))

# 1331 rank transform
def ref1331(arr):
    return [1 + len({y for y in arr if y < x}) for x in arr]
ex = [([40, 10, 20, 30],), ([100, 100, 100],), ([37, 12, 28, 9, 100, 56, 80, 5, 12],)]
edge = [([],), ([5],), ([-10**9, 10**9, -10**9],)]
rnd = [([ri(-5, 5) for _ in range(ri(0, 12))],) for _ in range(3000)]
report(1331, check(0, ex, B.arrayRankTransform, ref1331), check(0, edge, B.arrayRankTransform, ref1331),
       check(0, rnd, B.arrayRankTransform, ref1331), len(rnd), timed(B.arrayRankTransform, [ri(-10**9, 10**9) for _ in range(10**5)]))

# 912 sort an array
ex = [([5, 2, 3, 1],), ([5, 1, 1, 2, 0, 0],)]
edge = [([1],), ([-5 * 10**4, 5 * 10**4],), ([2] * 1000,), (list(range(1000, 0, -1)),)]
rnd = [([ri(-10, 10) for _ in range(ri(1, 30))],) for _ in range(3000)]
report(912, check(0, ex, B.sortArray, sorted), check(0, edge, B.sortArray, sorted), check(0, rnd, B.sortArray, sorted), len(rnd),
       timed(B.sortArray, [ri(-5 * 10**4, 5 * 10**4) for _ in range(5 * 10**4)]))

# 704 binary search
ref = lambda nums, t: nums.index(t) if t in nums else -1
ex = [([-1, 0, 3, 5, 9, 12], 9), ([-1, 0, 3, 5, 9, 12], 2)]
edge = [([5], 5), ([5], -5), ([-9999, 9999], -9999), ([-9999, 9999], 9999), ([1, 3], 2), ([1, 3], 4), ([1, 3], 0)]
rnd = []
for _ in range(3000):
    nums = sorted(random.sample(range(-20, 21), ri(1, 15))); rnd.append((nums, ri(-22, 22)))
bigs = sorted(random.sample(range(-9999, 10000), 10**4))
report(704, check(0, ex, B.search, ref), check(0, edge, B.search, ref), check(0, rnd, B.search, ref), len(rnd),
       timed(B.search, bigs, bigs[-1]))

# 34 first and last position
def ref34(nums, t):
    idx = [i for i, v in enumerate(nums) if v == t]; return [idx[0], idx[-1]] if idx else [-1, -1]
ex = [([5, 7, 7, 8, 8, 10], 8), ([5, 7, 7, 8, 8, 10], 6), ([], 0)]
edge = [([1], 1), ([1], 2), ([2, 2], 2), ([10**9] * 5, 10**9), ([-10**9, -10**9], -10**9), ([1, 2, 3], 3), ([1, 2, 3], 1), ([1, 2, 3], 4)]
rnd = [(sorted(ri(-5, 5) for _ in range(ri(0, 15))), ri(-6, 6)) for _ in range(3000)]
bigs = sorted(ri(-10**9, 10**9) for _ in range(10**5))
report(34, check(0, ex, B.searchRange, ref34), check(0, edge, B.searchRange, ref34), check(0, rnd, B.searchRange, ref34), len(rnd),
       timed(B.searchRange, bigs, bigs[500]))

# 104 max depth (random trees under default recursion limit; deep chains tested in probe_misc.py)
def ref104(root):
    if root is None: return 0
    d = 0; q = deque([root])
    while q:
        d += 1
        for _ in range(len(q)):
            nd = q.popleft()
            if nd.left: q.append(nd.left)
            if nd.right: q.append(nd.right)
    return d
run104 = lambda vals: B.maxDepth(build_tree(vals))
r104 = lambda vals: ref104(build_tree(vals))
ex = [([3, 9, 20, None, None, 15, 7],), ([1, None, 2],), ([],)]
edge = [([0],), ([1, 2, None, 3, None, 4],), ([-100, 100, -100],)]
rnd_trees = [random_tree(ri(0, 40)) for _ in range(2000)]
rnd_bad = [((t,), B.maxDepth(t), ref104(t)) for t in rnd_trees if B.maxDepth(t) != ref104(t)]
report(104, check(0, ex, run104, r104), check(0, edge, run104, r104), rnd_bad, len(rnd_trees),
       timed(B.maxDepth, random_tree(10**4)))

# 102 level order
def ref102(root):
    out = []
    def dfs(nd, d):
        if nd is None: return
        if d == len(out): out.append([])
        out[d].append(nd.val); dfs(nd.left, d + 1); dfs(nd.right, d + 1)
    dfs(root, 0); return out
run102 = lambda vals: B.levelOrder(build_tree(vals))
r102 = lambda vals: ref102(build_tree(vals))
ex = [([3, 9, 20, None, None, 15, 7],), ([1],), ([],)]
edge = [([0],), ([1, 2, None, 3, None, 4],), ([-1000, 1000, -1000],)]
rnd_trees = [random_tree(ri(0, 40), -1000, 1000) for _ in range(2000)]
rnd_bad = [((t,), B.levelOrder(t), ref102(t)) for t in rnd_trees if B.levelOrder(t) != ref102(t)]
report(102, check(0, ex, run102, r102), check(0, edge, run102, r102), rnd_bad, len(rnd_trees),
       timed(B.levelOrder, random_tree(2000, -1000, 1000)))

print('\nSUMMARY:', sum(1 for _, s in RESULTS if s == 'PASS'), 'PASS of', len(RESULTS))
print('python', sys.version.split()[0])
