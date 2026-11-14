import sys
print(sys.version)
g=sys.getsizeof
print("recursionlimit",sys.getrecursionlimit())
for v in [0,1,2**30-1,2**30,2**60-1,2**60,2**90,2**120,-2**30,-(2**30)+1]:
    print("int",v if abs(v)<10**6 else f"2^{v.bit_length()}", g(v))
print("float",g(1.5),"True",g(True),"None",g(None),"bool",g(False))
# small-int cache: identity test
def mk(n): return int(str(n))
lo=[n for n in range(-10,300) if mk(n) is mk(n)]
print("shared ints range",min(lo),max(lo))
print("str empty",g(""),"'a'",g("a"),"'ab'",g("ab"),"10",g("a"*10),"100",g("a"*100))
print("latin1 'é'",g("é"),"'éé'",g("éé"),"10 é",g("é"*10))
print("ucs2 '€'",g("€"),"10",g("€"*10),"ucs2 empty-diff", g("€"*10)-g("€"*9))
print("ucs4 '😀'",g("😀"),"10",g("😀"*10),g("😀"*10)-g("😀"*9))
# one-char sharing
def mkc(c): return "".join([c,""]) if False else chr(ord(c))
for n,c in [("ascii a","a"),("0x7f","\x7f"),("0x80","\x80"),("é 0xe9","é"),("ÿ 0xff","ÿ"),("0x100 Ā","Ā"),("€","€"),("emoji","😀")]:
    x=[chr(ord(c)) for _ in range(2)]
    s=("xx"+c)[2:]; t=("yy"+c)[2:]
    print("1-char shared?",n,s is t, "chr:",x[0] is x[1])
# per-char ascii
print("per ascii char", g("a"*1001)-g("a"*1000))
