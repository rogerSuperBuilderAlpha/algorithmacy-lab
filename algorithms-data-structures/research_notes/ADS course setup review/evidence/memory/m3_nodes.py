import sys,tracemalloc
g=sys.getsizeof
class LN:
    def __init__(s,val=0,next=None): s.val=val;s.next=next
class TN:
    def __init__(s,val=0,left=None,right=None): s.val=val;s.left=left;s.right=right
class LNs:
    __slots__=("val","next")
    def __init__(s,val=0,next=None): s.val=val;s.next=next
class TNs:
    __slots__=("val","left","right")
    def __init__(s,val=0,left=None,right=None): s.val=val;s.left=left;s.right=right
for cls in (LN,LNs,TN,TNs):
    o=cls(1000)
    d=g(o.__dict__) if hasattr(o,"__dict__") else 0
    print(cls.__name__,"getsizeof obj",g(o),"__dict__",d, "(+int 1000: 28 if not cached)")
# tracemalloc: allocate N nodes with distinct int vals > 256
N=100000
for cls in (LN,LNs,TN,TNs):
    vals=list(range(1000,1000+N))
    tracemalloc.start()
    b=tracemalloc.get_traced_memory()[0]
    nodes=[cls(v) for v in vals]
    a=tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    lst=8*N
    print(cls.__name__,"tracemalloc per node incl. list slot",round((a-b)/N,1),"-> excl list slot",round((a-b)/N-8,1),"(val int already allocated, shared)")
# linked chain: node + its own int
for cls in (LN,LNs,TN,TNs):
    tracemalloc.start()
    b=tracemalloc.get_traced_memory()[0]
    head=None
    for i in range(N): head=cls(100000+i, head) if cls in (LN,LNs) else cls(100000+i,head,None)
    a=tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    print(cls.__name__,"chain, per node incl own int object",round((a-b)/N,1))
    del head
