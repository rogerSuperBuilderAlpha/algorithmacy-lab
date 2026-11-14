import tracemalloc,sys
from collections import deque
def meas(name,build,n):
    tracemalloc.start()
    base=tracemalloc.get_traced_memory()[0]
    tracemalloc.reset_peak()
    obj=build(n)
    cur,peak=tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin=cur-base; pk=peak-base
    print(f"{name:14} n={n:7} final={fin:9} B ({fin/n:6.1f}/el) peak={pk:9} ({pk/n:6.1f}/el) peak/final={pk/fin:.2f} getsizeof={sys.getsizeof(obj)} ({sys.getsizeof(obj)/n:.1f}/el)")
    return obj
def d_build(n):
    d={}
    for i in range(n): d[i]=None   # same value, no int per value
    return d
def s_build(n):
    s=set()
    for i in range(n): s.add(i)
    return s
def dq_build(n):
    q=deque()
    for i in range(n): q.append(None)
    return q
def l_build(n):
    a=[]
    for i in range(n): a.append(None)
    return a
# keys ints: keys are created inside build, so final includes the int objects (28-32 B each)
# also measure with preallocated keys to isolate container
for n in (1000,100000):
    keys=list(range(n))
    def dk(n): 
        d={}
        for k in keys: d[k]=None
        return d
    def sk(n):
        s=set()
        for k in keys: s.add(k)
        return s
    meas("dict(keys pre)",dk,n); meas("set(keys pre)",sk,n)
    meas("dict(keys new)",d_build,n); meas("set(keys new)",s_build,n)
    meas("deque append",dq_build,n); meas("list append",l_build,n)
