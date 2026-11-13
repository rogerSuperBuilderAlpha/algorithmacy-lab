
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
