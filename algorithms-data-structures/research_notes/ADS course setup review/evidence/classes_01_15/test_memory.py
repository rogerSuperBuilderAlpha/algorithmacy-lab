# Memory measurements for the 30 board solutions of classes 1-15, at the input
# size the key states. For each problem prints: the key's figures, a figure
# recomputed from the course's own size table (syllabus lines 174-216), and the
# tracemalloc measurement on CPython 3.13.
#   input    = traced bytes alive after building the input (exact-size lists)
#   aux_peak = tracemalloc peak during the call minus traced bytes before it
#   retained = traced bytes still alive after the call (result and growth)
# Units: the key writes KB/MB for 1024/1024^2 bytes; this script does the same.
# Run: python3.13 -I test_memory.py
import sys, os, gc, random, tracemalloc
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import board as B
from board import ListNode, TreeNode

random.seed(7)
tracemalloc.start()
KB, MB = 1024, 1024 * 1024


def fmt(b):
    if b is None: return '-'
    if abs(b) >= MB: return f'{b / MB:.2f} MB'
    if abs(b) >= KB: return f'{b / KB:.1f} KB'
    return f'{b} B'


def build(f):
    gc.collect(); before = tracemalloc.get_traced_memory()[0]
    obj = f(); gc.collect()
    return obj, tracemalloc.get_traced_memory()[0] - before


def call(f, *args):
    gc.collect(); tracemalloc.reset_peak(); before = tracemalloc.get_traced_memory()[0]
    res = f(*args)
    cur, peak = tracemalloc.get_traced_memory()
    return res, peak - before, cur - before


def exact(seq):
    seq = list(seq); out = [None] * len(seq)
    for i, v in enumerate(seq): out[i] = v
    return out


def new_ints(n, lo=257, hi=10**9, sort=False):
    vals = random.sample(range(lo, hi), n)  # range items are fresh int objects
    if sort: vals.sort()
    return vals  # random.sample returns an exact-size list


def row(pid, key_in, key_aux, form_in, form_aux, m_in, m_aux, m_ret, note=''):
    print(f'#{pid}: INPUT key {key_in} | formula {fmt(form_in)} | measured {fmt(m_in)}   '
          f'AUX key {key_aux} | formula {fmt(form_aux)} | measured peak {fmt(m_aux)}, retained {fmt(m_ret)}  {note}')


# ---- 1480: n = 100,000 distinct ints above 256 ----
nums, m_in = build(lambda: new_ints(100_000, 257, 10**6))
_, peak, ret = call(B.runningSum, nums)
big = sum(1 for v in nums if v >= 2**30)
row(1480, '3.4 MB', '150 B', 56 + 36 * 100_000, 150, m_in, peak, ret,
    f'| sums >= 2**30 (32-byte ints) after the call: {big}; growth {fmt(ret)} is real, not churn')
nums2, _ = build(lambda: new_ints(100_000, 257, 257 + 100_000))  # smallest possible distinct ints above 256
_, peak2, ret2 = call(B.runningSum, nums2)
print(f'      #1480 smallest distinct values 257..100256: final sum {nums2[-1]:,} (2**30 = {2**30:,}); '
      f'sums >= 2**30: {sum(1 for v in nums2 if v >= 2**30)}; aux peak {fmt(peak2)}, retained growth {fmt(ret2)}')
lc, _ = build(lambda: exact(random.randint(-10**6, 10**6) for _ in range(1000)))  # LeetCode limits
_, peak3, ret3 = call(B.runningSum, lc)
print(f'      #1480 at LeetCode limits (n=1000, |v|<=1e6): aux peak {fmt(peak3)}, retained growth {fmt(ret3)}')
del nums, nums2, lc

# ---- 217: n = 100,000 distinct ints above 256 ----
nums, m_in = build(lambda: new_ints(100_000))
_, peak, ret = call(B.containsDuplicate, nums)
s = set(nums)
row(217, '3.4 MB', '4.0 MB (peak ~6 MB)', 56 + 36 * 100_000, 42 * 100_000, m_in, peak, ret,
    f'| getsizeof(set of 1e5)={sys.getsizeof(s)} -> table slots={(sys.getsizeof(s) - 200) // 16} of 16 B')
del nums, s

# ---- 283: n = 100,000, half zeros ----
def mk283():
    a = [0] * 100_000; vals = new_ints(50_000)
    for i, v in zip(random.sample(range(100_000), 50_000), vals): a[i] = v
    return a
nums, m_in = build(mk283)
_, peak, ret = call(B.moveZeroes, nums)
row(283, '2.1 MB', '150 B', 56 + 8 * 100_000 + 28 * 50_000, 150, m_in, peak, ret)
del nums

# ---- 88: m = n = 50,000 ----
def mk88():
    a = new_ints(50_000, sort=True) + [0] * 50_000
    return (exact(a), 50_000, new_ints(50_000, sort=True), 50_000)
args, m_in = build(mk88)
_, peak, ret = call(B.merge, *args)
form_in = (56 + 8 * 100_000 + 28 * 50_000) + (56 + 8 * 50_000 + 28 * 50_000)
row(88, '5.1 MB (formula counts 28 B for all 100,000 nums1 slots)', '150 B', form_in, 150, m_in, peak, ret,
    '| key formula 56+8n+28n (n=1e5) + 56+8n/2+28n/2 = ' + fmt(56 + 36 * 100_000 + 56 + 18 * 100_000))
del args

# ---- 14: 200 strings of 200 chars, all identical (distinct objects) ----
def mk14(last=None):
    base = 'q' * 100
    out = [base + 'q' * 100 for _ in range(200)]  # 200 distinct str objects
    if last: out[-1] = 'q' * 199 + last
    return out
strs, m_in = build(mk14)
res, peak, ret = call(B.longestCommonPrefix, strs)
row(14, '49 KB', '341 B', 200 * 241 + 56 + 8 * 200, 0, m_in, peak, ret,
    f'| identical case returns the input object itself: {res is strs[0]}')
strs2, _ = build(lambda: mk14('z'))
res2, peak2, ret2 = call(B.longestCommonPrefix, strs2)
print(f'      #14 variant (last string differs at char 200): aux peak {fmt(peak2)}, retained {fmt(ret2)} (slice of {len(res2)} chars, getsizeof {sys.getsizeof(res2)})')
del strs, strs2, res, res2

# ---- 303: n = 10,000 ----
nums, m_in = build(lambda: exact(random.randint(257, 10**5) for _ in range(10_000)))
obj, peak, ret = call(B.NumArray, nums)
row(303, '352 KB', '352 KB', 56 + 36 * 10_000, 56 + 8 * 10_001 + 28 * 10_001, m_in, peak, ret,
    f'| prefix list getsizeof {sys.getsizeof(obj.prefix)} vs exact {56 + 8 * 10_001}; course formula with 12% append room: {fmt(56 + int(8 * 1.12 * 10_001) + 28 * 10_001)}')
del nums, obj

# ---- 242: n = 50,000 each ----
letters = 'abcdefghijklmnopqrstuvwxyz'
def mk242():
    s = ''.join(random.choice(letters) for _ in range(50_000)); t = ''.join(random.sample(s, len(s))); return (s, t)
args, m_in = build(mk242)
_, peak, ret = call(B.isAnagram, *args)
d = {}
for ch in args[0]: d[ch] = d.get(ch, 0) + 1
row(242, '98 KB', '2.0 KB', 2 * (41 + 50_000), 1200 + 26 * 28, m_in, peak, ret, f'| getsizeof(26-key str dict)={sys.getsizeof(d)}')
del args, d

# ---- 1: n = 10,000, answer at the end ----
def mk1():
    nums = new_ints(10_000, 10**6, 10**9 // 2); return (nums, nums[0] + nums[-1])
args, m_in = build(mk1)
res, peak, ret = call(B.twoSum, *args)
dd = {v: i for i, v in enumerate(args[0][:-1])}
row(1, '352 KB', '781 KB', 56 + 36 * 10_000 + 28, 52 * 10_000 + 28 * 10_000, m_in, peak, ret,
    f'| answer {res}; getsizeof(dict 9,999 int keys)={sys.getsizeof(dd)} = {sys.getsizeof(dd) / 9999:.1f} B/entry; '
    f'dict + new index ints = {fmt(sys.getsizeof(dd) + 28 * (9999 - 257))}')
del args, dd

# ---- 125: n = 200,000 letters, palindrome ----
def mk125():
    h = ''.join(random.choice(letters + letters.upper()) for _ in range(100_000)); return h + h[::-1].swapcase()
s125, m_in = build(mk125)
res, peak, ret = call(B.isPalindrome, s125)
row(125, '195 KB', '150 B', 41 + 200_000, 150, m_in, peak, ret, f'| result {res}')
del s125

# ---- 977: n = 10,000 sorted, |values| in the thousands ----
nums, m_in = build(lambda: sorted(random.sample([v for v in range(-10_000, 10_001) if abs(v) > 16], 10_000)))
_, peak, ret = call(B.sortedSquares, nums)
row(977, '352 KB', '352 KB', 56 + 36 * 10_000, 56 + 36 * 10_000, m_in, peak, ret)
del nums

# ---- 643: n = 100,000 ints above 256 ----
nums, m_in = build(lambda: exact(random.randint(257, 10_000) for _ in range(100_000)))
_, peak, ret = call(B.findMaxAverage, nums, 1000)
row(643, '3.4 MB', '150 B', 56 + 36 * 100_000, 150, m_in, peak, ret)
del nums

# ---- 121: n = 100,000 prices above 256 ----
nums, m_in = build(lambda: exact(random.randint(257, 10_000) for _ in range(100_000)))
_, peak, ret = call(B.maxProfit, nums)
row(121, '3.4 MB', '150 B', 56 + 36 * 100_000, 150, m_in, peak, ret)
del nums

# ---- 20: n = 10,000 '(' ----
s20, m_in = build(lambda: ''.join(['('] * 10_000))
_, peak, ret = call(B.isValid, s20)
row(20, '9.8 KB', '88 KB', 41 + 10_000, int(8 * 10_000 * 1.12) + 56 + 184, m_in, peak, ret)
del s20

# ---- 844: n = m = 200, no '#' ----
args, m_in = build(lambda: (''.join(random.choice(letters) for _ in range(200)), ''.join(random.choice(letters) for _ in range(200))))
_, peak, ret = call(B.backspaceCompare, *args)
row(844, '482 B', '3.6 KB', 2 * 241, 2 * (56 + int(8 * 200 * 1.12)), m_in, peak, ret)
del args

# ---- 933: 10,000 pings, one per ms ----
ts, m_in = build(lambda: exact(range(1, 10_001)))
def run933(ts):
    rc = B.RecentCounter()
    for t in ts: rc.ping(t)
    return rc
rc, peak, ret = call(run933, ts)
row(933, '273 KB (28n ints)', '25 KB', 28 * (10_000 - 256), int(3001 * 8.3) + 600, m_in, peak, ret,
    f'| final deque len {len(rc.window)}, getsizeof {sys.getsizeof(rc.window)}; measured input includes 56+8n list of pointers')
del ts, rc

# ---- 232: 100,000 pushes, counted with all items in the inbox ----
items, m_in = build(lambda: new_ints(100_000))
def push_all(items):
    q = B.MyQueue()
    for x in items: q.push(x)
    return q
q, peak, ret = call(push_all, items)
row(232, '2.7 MB (28n ints)', '879 KB', 28 * 100_000, 56 + int(8 * 1.12 * 100_000), m_in, peak, ret,
    f'| inbox getsizeof {sys.getsizeof(q.inbox)}')
_, peak_pop, ret_pop = call(q.pop)
print(f'      #232 first pop() pours inbox into outbox: extra peak during that pop {fmt(peak_pop)} on top of the {fmt(ret)} inbox')
del items, q

# ---- 496: n = m = 1,000, nums2 random permutation, nums1 = nums2 ----
def mk496():
    nums2 = random.sample(range(257, 10_001), 1000); nums1 = exact(nums2); return (nums1, nums2)
args, m_in = build(mk496)
res, peak, ret = call(B.nextGreaterElement, *args)
g = {}
st = []; mx = 0
for x in args[1]:
    while st and st[-1] < x: g[st.pop()] = x
    st.append(x); mx = max(mx, len(st))
row(496, '43 KB', '55 KB', 2 * (56 + 8000) + 28 * 1000, 40 * 1000 + 8000 + 8000, m_in, peak, ret,
    f'| dict entries {len(g)}, max stack {mx}, getsizeof(dict) {sys.getsizeof(g)}, answer getsizeof {sys.getsizeof(res)}')
del args, res, g, st

# ---- 739: n = 100,000 equal temperatures ----
temps, m_in = build(lambda: [70] * 100_000)
_, peak, ret = call(B.dailyTemperatures, temps)
row(739, '781 KB', '4.3 MB', 56 + 8 * 100_000, (56 + 8 * 100_000) + 9 * 100_000 + 28 * 100_000, m_in, peak, ret)
del temps

# ---- 206: n = 5,000 nodes ----
def mk_ll(vals):
    head = None
    for v in reversed(vals): head = ListNode(v, head)
    return head
head, m_in = build(lambda: mk_ll(random.choices(range(-5000, 5001), k=5000)))
head_small, m_in_small = build(lambda: mk_ll([7] * 5000))
_, peak, ret = call(B.reverseList, head)
row(206, '488 KB', '150 B', 100 * 5000, 150, m_in, peak, ret,
    f'| per node with LeetCode-range ints {m_in / 5000:.1f} B, per node with a cached small int {m_in_small / 5000:.1f} B; getsizeof(ListNode())={sys.getsizeof(ListNode())}')
del head, head_small

# ---- 19: L = 30 nodes (LeetCode values 0..100, cached) ----
head, m_in = build(lambda: mk_ll(random.choices(range(0, 101), k=30)))
_, peak, ret = call(B.removeNthFromEnd, head, 15)
row(19, '2.9 KB', '250 B', 100 * 30, 100 + 150, m_in, peak, ret, '| values 0..100 per LeetCode are cached ints')
del head

# ---- 509: n = 30 ----
_, peak, ret = call(B.fib, 30)
row(509, '28 B', '6.4 KB (incl. 4.5 KB frames)', 28, 1200 + 17 * 28 + 30 * 150, 28, peak, ret,
    '| tracemalloc does not see frames; formula counts only F(14)..F(30) as new ints (F(13)=233 is cached)')

# ---- 50: n = 2**31 ----
def pow_probe():
    return B.myPow(1.0000000001, 2**31)
_, peak, ret = call(pow_probe)
ints_alive = sum(1 for k in range(32) if (2**31 >> k) > 256)
row(50, '52 B', '5.4 KB (32 frames + 32 floats)', 24 + 32, 33 * 150 + ints_alive * 28 + 2 * 24, 56, peak, ret,
    f'| n values >256 held by frames on the way down: {ints_alive}; at most ~2 floats alive at once')

# ---- 136: n = 30,000 (14,999 pairs + 1), each pair the same int object ----
def mk136():
    vals = random.sample(range(257, 30_001), 15_000); a = vals[:-1] * 2 + [vals[-1]]; random.shuffle(a); return exact(a)
nums, m_in = build(mk136)
_, peak, ret = call(B.singleNumber_136, nums)
row(136, '645 KB', '100 B', 56 + 8 * 29_999 + 28 * 15_000, 100, m_in, peak, ret)
del nums

# ---- 260: n = 30,000 (14,999 pairs + 2) ----
def mk260():
    vals = random.sample(range(257, 2**31 - 1), 15_001); a = vals[:-2] * 2 + vals[-2:]; random.shuffle(a); return exact(a)
nums, m_in = build(mk260)
_, peak, ret = call(B.singleNumber_260, nums)
row(260, '645 KB', '250 B', 56 + 8 * 30_000 + 28 * 15_001, 250, m_in, peak, ret)
del nums

# ---- 1331: n = 100,000 distinct ints above 256 ----
arr, m_in = build(lambda: new_ints(100_000))
res, peak, ret = call(B.arrayRankTransform, arr)
rk = {v: i + 1 for i, v in enumerate(sorted(arr))}
row(1331, '3.4 MB', '9.3 MB', 56 + 36 * 100_000, 9 * 100_000 + 52 * 100_000 + 28 * 100_000 + 9 * 100_000, m_in, peak, ret,
    f'| getsizeof(dict 1e5)={sys.getsizeof(rk)}, answer getsizeof={sys.getsizeof(res)}')
del arr, res, rk

# ---- 912: n = 50,000 random ----
nums, m_in = build(lambda: new_ints(50_000))
res, peak, ret = call(B.sortArray, nums)
row(912, '1.7 MB', '830 KB', 56 + 36 * 50_000, 8 * 50_000 + int(8 * 50_000 * 1.12), m_in, peak, ret,
    f'| result getsizeof {sys.getsizeof(res)}')
del nums, res

# ---- 704: n = 10,000 sorted distinct ----
nums, m_in = build(lambda: new_ints(10_000, sort=True))
_, peak, ret = call(B.search, nums, nums[1234])
row(704, '352 KB', '100 B', 56 + 36 * 10_000, 100, m_in, peak, ret)
del nums

# ---- 34: n = 100,000 sorted, block of 1,000 equal targets ----
def mk34():
    vals = new_ints(99_000, 257, 10**8)
    tgt = 10**8 + 7
    vals += [tgt + 0 * i for i in range(1000)]  # 1,000 equal values (distinct objects not guaranteed)
    vals.sort(); return exact(vals)
nums, m_in = build(mk34)
res, peak, ret = call(B.searchRange, nums, 10**8 + 7)
row(34, '3.4 MB', '250 B', 56 + 36 * 100_000, 250, m_in, peak, ret, f'| result {res}')
del nums

# ---- 104 and 102: n = 10,000 nodes, complete tree ----
def complete_tree(n, val):
    nodes = [TreeNode(val(i)) for i in range(n)]
    for i in range(n):
        if 2 * i + 1 < n: nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n: nodes[i].right = nodes[2 * i + 2]
    return nodes[0]
root, m_in = build(lambda: complete_tree(10_000, lambda i: random.randint(-100, 100)))
root_big, m_in_big = build(lambda: complete_tree(10_000, lambda i: 1000 + i))
d, peak, ret = call(B.maxDepth, root)
row(104, '977 KB', '2.1 KB (14 frames)', 100 * 10_000, 15 * 150, m_in, peak, ret,
    f'| depth {d}; per node: LeetCode values (-100..100) {m_in / 10_000:.1f} B, new int values {m_in_big / 10_000:.1f} B; '
    f'getsizeof(TreeNode())={sys.getsizeof(TreeNode())}; frames invisible to tracemalloc')
res, peak, ret = call(B.levelOrder, root_big)
row(102, '977 KB', '120 KB', 100 * 10_000, 8 * 10_000 + 14 * 56 + int(5000 * 8.3) + 600, m_in_big, peak, ret,
    f'| levels {len(res)}, last level {len(res[-1])}, widest level {max(len(l) for l in res)}; result alone getsizeof sum '
    f'{sys.getsizeof(res) + sum(sys.getsizeof(l) for l in res)}')
print('python', sys.version.split()[0])
