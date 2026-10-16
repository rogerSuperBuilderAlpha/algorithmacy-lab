"""Decisive isomorphism check for Hassan's candidate aff(6,9,5) vs aff(11,9,5): every one of the 6 node
permutations and all 48 (perm x per-node value flip) maps, applied explicitly, printed one by one."""
import itertools
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import TABLES, stats

a, b = ("aff", 6, 9, 5), ("aff", 11, 9, 5)
ta, tb = TABLES[a], TABLES[b]
L = "XYH"


def show(t):
    return "; ".join("%s'=%s" % (L[j], "".join(map(str, t[j]))) for j in range(3))


def apply(t, perm, mask):
    # relabel: new node perm[j] <- old node j, with old node j's values flipped if mask bit j set
    out = [[0] * 8 for _ in range(3)]
    for s in range(8):
        bits = [(s >> j) & 1 for j in range(3)]
        nb = [0] * 3
        for j in range(3):
            nb[perm[j]] = bits[j] ^ ((mask >> j) & 1)
        ns = sum(nb[k] << k for k in range(3))
        for j in range(3):
            out[perm[j]][ns] = t[j][s] ^ ((mask >> j) & 1)
    return tuple(tuple(r) for r in out)


print("a =", a, show(ta)); print("b =", b, show(tb))
hits6 = [p for p in itertools.permutations(range(3)) if apply(ta, p, 0) == tb]
hits48 = [(p, m) for p in itertools.permutations(range(3)) for m in range(8) if apply(ta, p, m) == tb]
for p in itertools.permutations(range(3)):
    print("perm %s (Y<->H swap=%s): a mapped = %s ; equals b: %s" % (p, p == (0, 2, 1), show(apply(ta, p, 0)), apply(ta, p, 0) == tb))
print("node-permutation isomorphisms (6):", hits6)
print("perm x value-flip isomorphisms (48):", hits48)
print("cross-check with pair_search.permute_tables canon:", min(ps.permute_tables(ta, p) for p in ps.PERMS) == min(ps.permute_tables(tb, p) for p in ps.PERMS))
sa, sb = stats(a), stats(b)
print("const nodes:", sa[0], sb[0], "; marginals equal:", sa[1] == sb[1], [str(x) for x in sa[1]],
      "; self-recurrence equal (0..20):", sa[2] == sb[2], "; cross equal (0..20):", sa[3] == sb[3])
