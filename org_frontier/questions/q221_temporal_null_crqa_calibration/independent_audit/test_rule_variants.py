"""Regression test: distinguish the two previously conflated XOR variants.

Pure NumPy; no PyPhi. Run with pytest independent_audit/test_rule_variants.py.
"""
import numpy as np

P = 0.08
STATES = np.array([[(s >> j) & 1 for j in range(3)] for s in range(8)], dtype=int)

def transition(variant):
    out = np.zeros((8, 8), dtype=float)
    for s, (x, y, h) in enumerate(STATES):
        z = h if variant == "A_self" else (x ^ y if variant == "B_xor" else h ^ x ^ y)
        target = np.array([x, y, z])
        out[s] = np.prod(np.where(STATES == target, 1-P, P), axis=1)
    return out

def stationary(matrix):
    pi = np.full(8, 1/8)
    for _ in range(2000):
        pi = pi @ matrix
    assert np.max(np.abs(pi @ matrix - pi)) < 1e-12
    return pi

def h_self_match(matrix, pi):
    return sum(pi[s]*matrix[s,t] for s in range(8) for t in range(8)
               if STATES[s,2] == STATES[t,2])

def test_variants_are_distinct():
    a, b, c = [transition(v) for v in ("A_self","B_xor","B_xor_memory")]
    assert not np.allclose(a,b)
    assert not np.allclose(b,c)
    for m in (a,b,c):
        assert np.allclose(m.sum(axis=1),1)

def test_stationary_self_recurrence():
    a,b,c = [transition(v) for v in ("A_self","B_xor","B_xor_memory")]
    pa,pb,pc = [stationary(m) for m in (a,b,c)]
    assert np.allclose(pa,np.full(8,1/8))
    assert np.allclose(pc,np.full(8,1/8))
    assert not np.allclose(pb,np.full(8,1/8))
    assert abs(h_self_match(a,pa)-0.92)<1e-12
    assert abs(h_self_match(c,pc)-0.5)<1e-12
    assert abs(h_self_match(b,pb)-0.74893568)<1e-10
