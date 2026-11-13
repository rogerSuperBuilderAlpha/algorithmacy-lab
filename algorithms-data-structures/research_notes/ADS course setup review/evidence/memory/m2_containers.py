import sys
g=sys.getsizeof
print("list [] ",g([]),"[0]",g([0]),"[0]*2",g([0]*2),"[0]*10",g([0]*10),"per slot",g([0]*11)-g([0]*10))
for n in (1000,100000):
    a=[]
    for i in range(n): a.append(i)
    c=[i for i in range(n)]
    m=[0]*n
    l=list(range(n))
    print(n,"append",g(a),"slots",(g(a)-56)//8,"spare%",round(100*((g(a)-56)//8-n)/n,2),
          "| comp",g(c),"slots",(g(c)-56)//8,"| [0]*n",g(m),"| list(range)",g(l))
print("tuple ()",g(()),"(1,)",g((1,)),"pair",g((1,2)),"triple",g((1,2,3)),"10",g(tuple(range(10))))
print("dict {}",g({}),"1 entry",g({1:1}),"5",g({i:i for i in range(5)}),"6",g({i:i for i in range(6)}),"dict()",g(dict()))
for n in (1000,100000):
    d={i:i for i in range(n)}
    d2={}
    for i in range(n): d2[i]=i
    s=set(range(n)); s2=set()
    for i in range(n): s2.add(i)
    print(n,"dict comp",g(d),round(g(d)/n,1),"B/entry | dict built",g(d2),round(g(d2)/n,1),"| set(range)",g(s),round(g(s)/n,1),"| set add",g(s2),round(g(s2)/n,1))
print("set()",g(set()),"{1}",g({1}))
from collections import deque
print("deque()",g(deque()))
for n in (1000,100000):
    q=deque(range(n)); q2=deque()
    for i in range(n): q2.append(i)
    print(n,"deque(range)",g(q),round(g(q)/n,2),"| append",g(q2),round(g(q2)/n,2),"| fixed overhead",g(q)-8*n)
