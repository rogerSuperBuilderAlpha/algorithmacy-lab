# Board solutions for classes 1-15, transcribed verbatim from
# ADS_In_Class_Solutions.md (line numbers of each "Solution" block given).
# Only changes: #136 and #260 both use the name singleNumber in the key, so they
# are renamed singleNumber_136 / singleNumber_260 here (bodies unchanged); the
# key's board code for #933 and #102 uses deque with no import line, so the
# import is added once at the top (see probe_misc.py for the no-import run).
from collections import deque


class ListNode:  # LeetCode's definition (fetched python3 snippet, #206/#19)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:  # LeetCode's definition (fetched python3 snippet, #104/#102)
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Class 1A, #1480, key lines 77-83
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums


# Class 1B, #217, key lines 164-176
def containsDuplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


# Class 2A, #283, key lines 256-266
def moveZeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


# Class 2B, #88, key lines 332-354
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


# Class 3A, #14, key lines 420-432
def longestCommonPrefix(strs):
    first = strs[0]
    for i in range(len(first)):
        for s in strs:
            if i == len(s) or s[i] != first[i]:
                return first[:i]
    return first


# Class 3B, #303, key lines 514-526
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


# Class 4A, #242, key lines 590-610
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True


# Class 4B, #1, key lines 685-697
def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i


# Class 5A, #125, key lines 774-798
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# Class 5B, #977, key lines 874-898
def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for k in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[k] = nums[left] * nums[left]
            left += 1
        else:
            result[k] = nums[right] * nums[right]
            right -= 1
    return result


# Class 6A, #643, key lines 972-990
def findMaxAverage(nums, k):
    window = 0
    for i in range(k):
        window += nums[i]
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        if window > best:
            best = window
    return best / k


# Class 6B, #121, key lines 1065-1081
def maxProfit(prices):
    left = 0
    best = 0
    for right in range(1, len(prices)):
        if prices[right] < prices[left]:
            left = right
        else:
            best = max(best, prices[right] - prices[left])
    return best


# Class 7A, #20, key lines 1153-1171
def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


# Class 7B, #844, key lines 1247-1267
def backspaceCompare(s, t):
    def build(text):
        stack = []
        for ch in text:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return stack
    return build(s) == build(t)


# Class 8A, #933, key lines 1344-1358
class RecentCounter:
    def __init__(self):
        self.window = deque()

    def ping(self, t):
        self.window.append(t)
        while self.window[0] < t - 3000:
            self.window.popleft()
        return len(self.window)


# Class 8B, #232, key lines 1424-1454
class MyQueue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, x):
        self.inbox.append(x)

    def pop(self):
        self.peek()
        return self.outbox.pop()

    def peek(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]

    def empty(self):
        return not self.inbox and not self.outbox


# Class 9A, #496, key lines 1523-1537
def nextGreaterElement(nums1, nums2):
    greater = {}
    stack = []
    for x in nums2:
        while stack and stack[-1] < x:
            greater[stack.pop()] = x
        stack.append(x)
    return [greater.get(x, -1) for x in nums1]


# Class 9B, #739, key lines 1616-1632
def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


# Class 10A, #206, key lines 1712-1728
def reverseList(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


# Class 10B, #19, key lines 1791-1811
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


# Class 11A, #509, key lines 1875-1887
def fib(n):
    memo = {0: 0, 1: 1}
    def go(k):
        if k not in memo:
            memo[k] = go(k - 1) + go(k - 2)
        return memo[k]
    return go(n)


# Class 11B, #50, key lines 1965-1981
def myPow(x, n):
    if n < 0:
        return 1 / myPow(x, -n)
    if n == 0:
        return 1.0
    half = myPow(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x


# Class 12A, #136, key lines 2055-2063 (renamed from singleNumber)
def singleNumber_136(nums):
    result = 0
    for x in nums:
        result ^= x
    return result


# Class 12B, #260, key lines 2141-2159 (renamed from singleNumber)
def singleNumber_260(nums):
    xor_all = 0
    for x in nums:
        xor_all ^= x
    low = xor_all & -xor_all
    a = 0
    for x in nums:
        if x & low:
            a ^= x
    return [a, xor_all ^ a]


# Class 13A, #1331, key lines 2236-2244
def arrayRankTransform(arr):
    rank = {}
    for x in sorted(set(arr)):
        rank[x] = len(rank) + 1
    return [rank[x] for x in arr]


# Class 13B, #912, key lines 2321-2357
def sortArray(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = sortArray(nums[:mid])
    right = sortArray(nums[mid:])
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Class 14A, #704, key lines 2439-2461
def search(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# Class 14B, #34, key lines 2536-2564
def searchRange(nums, target):
    def first_at_least(x):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
    start = first_at_least(target)
    if start == len(nums) or nums[start] != target:
        return [-1, -1]
    return [start, first_at_least(target + 1) - 1]


# Class 15A, #104, key lines 2640-2650
def maxDepth(root):
    if root is None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return 1 + max(left, right)


# Class 15B, #102, key lines 2725-2755
def levelOrder(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
