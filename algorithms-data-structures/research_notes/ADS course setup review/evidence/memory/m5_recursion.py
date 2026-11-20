"""Memory per active Python call in CPython 3.13.
Method: run a recursion to depth D in a fresh process; read peak RSS (ru_maxrss, bytes on macOS)
before and after at two depths; per-call = delta RSS / delta depth. Also tracemalloc at the same depths
(tracemalloc only sees PyMem/PyObject allocations, so frame data-stack chunks may be invisible).
Also report code.co_framesize (words) which is the interpreter's own frame size."""
import sys, resource, tracemalloc, subprocess, json
def f1(n):
    if n == 0: return 0
    return 1 + f1(n-1)
def f3(n, a, b):
    if n == 0: return 0
    x = a + 1; y = b + 1
    return x + f3(n-1, x, y) - y
def f0(n):  # linked-list style recursion, two locals
    if n == 0: return 0
    left = n; right = n+1
    return f0(n-1) + left - right + 1
if len(sys.argv) > 1:
    name, depth, mode = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    fn = {"f1": f1, "f3": (lambda n: f3(n,0,0)), "f0": f0}[name]
    sys.setrecursionlimit(depth + 100)
    fn(10)  # warm
    if mode == "tm":
        tracemalloc.start(); b = tracemalloc.get_traced_memory()[0]; tracemalloc.reset_peak()
        fn(depth); pk = tracemalloc.get_traced_memory()[1] - b
        print(json.dumps({"tm_peak": pk}))
    else:
        r0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        fn(depth)
        r1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print(json.dumps({"rss_delta": r1 - r0}))
else:
    print("default recursion limit", sys.getrecursionlimit())
    for n, fn in (("f1", f1), ("f3", f3), ("f0", f0)):
        print(n, "(co_framesize not exposed in 3.13) nlocals", fn.__code__.co_nlocals, "stacksize", fn.__code__.co_stacksize)
    for name in ("f1", "f3", "f0"):
        for mode in ("rss", "tm"):
            res = {}
            for d in ((20000, 100000, 200000) if mode=='rss' else (5000, 20000, 40000)):
                out = subprocess.run([sys.executable, "-I", __file__, name, str(d), mode], capture_output=True, text=True, timeout=300)
                res[d] = list(json.loads(out.stdout.strip().splitlines()[-1]).values())[0] if out.returncode == 0 else out.stderr[-200:]
            print(name, mode, res)
            ks = sorted(res)
            if all(isinstance(res[k], int) for k in ks):
                print("   per call (400k-100k):", round((res[ks[2]] - res[ks[1]]) / (ks[2] - ks[1]), 1), "B;  (100k-20k):", round((res[ks[1]] - res[ks[0]]) / (ks[1] - ks[0]), 1), "B")
