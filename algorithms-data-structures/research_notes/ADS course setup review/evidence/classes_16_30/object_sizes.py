"""Per-object costs in CPython 3.13: sys.getsizeof vs tracemalloc (bytes per object over 10,000 objects)."""
import sys, tracemalloc, gc
from lc_types import TreeNode
def per_obj(make, n=10_000):
    gc.collect(); tracemalloc.start(); b = tracemalloc.get_traced_memory()[0]
    keep = [make(i) for i in range(n)]
    a = tracemalloc.get_traced_memory()[0]; tracemalloc.stop()
    return (a - b - (56 + 8 * n * 1.125)) / n  # subtract the holding list (approx, growth room)
print(sys.version.split()[0])
print("int > 256      getsizeof", sys.getsizeof(10**6), " tracemalloc/obj %.1f" % per_obj(lambda i: i + 10**6))
print("TreeNode(1)    getsizeof", sys.getsizeof(TreeNode(1)), " tracemalloc/obj %.1f" % per_obj(lambda i: TreeNode(1)))
print("TreeNode(big)  tracemalloc/obj incl. int %.1f" % per_obj(lambda i: TreeNode(i + 10**6)))
print("2-tuple        getsizeof", sys.getsizeof((10**6, 2)), " tracemalloc/obj %.1f" % per_obj(lambda i: (i, 2)))
print("3-tuple        getsizeof", sys.getsizeof((1, 2, 3)), " tracemalloc/obj %.1f" % per_obj(lambda i: (i, 2, 3)))
print("[a,b] list     getsizeof", sys.getsizeof([1, 2]), " tracemalloc/obj %.1f" % per_obj(lambda i: [i, 2]))
print("[a,b,c] list   getsizeof", sys.getsizeof([1, 2, 3]), " tracemalloc/obj %.1f" % per_obj(lambda i: [i, 2, 3]))
print("8-char str     getsizeof", sys.getsizeof("abcdefgh"), " tracemalloc/obj %.1f" % per_obj(lambda i: "abcdefg" + chr(97 + i % 26)))
print("float          getsizeof", sys.getsizeof(1.5), " tracemalloc/obj %.1f" % per_obj(lambda i: i + 0.5))
