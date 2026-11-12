"""tracemalloc bytes per object (requested size) vs sys.getsizeof, N objects built in a list; list slot (8 B) subtracted."""
import tracemalloc, sys
N=100000
def per(name, mk):
    tracemalloc.start()
    b=tracemalloc.get_traced_memory()[0]
    L=[mk(i) for i in range(N)]
    a=tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    print(f"{name:22} tracemalloc/obj={(a-b)/N-8.0:7.1f}  getsizeof(one)={sys.getsizeof(L[-1])}")
per("int > 256", lambda i: i+1000)
per("int 2^31+", lambda i: i+2**31)
per("float", lambda i: i+0.5)
per("str len10 ascii", lambda i: ("%010d"%i))
per("str len1 (new>255?)", lambda i: chr(0x4e00+i%20000))
per("tuple pair", lambda i: (i,i)) 
per("tuple triple (no ints)", lambda i: (None,None,None))
per("pair of two shared", lambda i: (None,None))
per("empty list", lambda i: [])
per("list of 3", lambda i: [None,None,None])
per("dict 1 str key", lambda i: {"a":None})
per("empty dict", lambda i: {})
per("set 1 elt", lambda i: {None})
