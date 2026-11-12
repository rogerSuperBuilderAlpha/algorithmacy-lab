import sys
g=sys.getsizeof
# list spare room after append at many n
sp=[]
for n in list(range(1,2001))+[5000,10000,50000,100000,200000,500000,1000000]:
    a=[]
    for i in range(n): a.append(i)
    slots=(g(a)-56)//8
    sp.append((n,100*(slots-n)/n))
big=[(n,s) for n,s in sp if n>=1000]
print("append spare%: n=1000",dict(sp)[1000],"n=100000",round(dict(sp)[100000],3),"n=10000",round(dict(sp)[10000],3),"n=1e6",round(dict(sp)[1000000],3))
print("max spare% over n in 100..2000:",max(s for n,s in sp if 100<=n<=2000),"mean over 1000..2000:",round(sum(s for n,s in sp if 1000<=n<=2000)/1001,2))
print("spare% for n in 1000,1100(exp),1101..:",[ (n,round(s,2)) for n,s in sp if n in (1100,1101,1200,1239,1240,1241)])
print("dict {'a':1}",g({'a':1}),"{'a':1,'b':2}",g({'a':1,'b':2}),"dict str keys 6",g({str(i):i for i in range(6)}))
for n in (1000,100000):
    d={str(i):i for i in range(n)}; print("dict str keys",n,g(d),round(g(d)/n,1))
class C: pass
c=C(); c.a=1
print("empty-instance",g(C()),"instance dict",g(c.__dict__))
print("range iter",g(iter(range(10))),"range obj",g(range(10)),"list iter",g(iter([1])))
print("ints 2^30-1",g(2**30-1),"2^30",g(2**30),"2^60-1",g(2**60-1),"2^60",g(2**60),"neg -2^30",g(-2**30))
print("generator",g((i for i in range(3))),"frozenset",g(frozenset()),"bytes b''",g(b''),"bytearray",g(bytearray()))
print("str ascii 100k chars",g("a"*100000))
print("float list slot: [1.5]*3",g([1.5]*3))
