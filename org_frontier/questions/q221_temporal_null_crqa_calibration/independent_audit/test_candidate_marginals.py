"""Marginal distinguishability of the first eligible q221 candidate.
Run: pytest independent_audit/test_candidate_marginals.py
"""
import numpy as np
from .test_candidate_profiles import A,B,transition,profiles

def test_first_candidate_marginals_are_different():
    _,pa=profiles(A)
    _,pb=profiles(B)
    bits=np.array([[(s>>j)&1 for j in range(3)] for s in range(8)])
    ma=pa@bits
    mb=pb@bits
    assert abs(ma[0]-0.08)<1e-12
    assert abs(mb[0]-0.5)<1e-12
    assert abs(ma[0]-mb[0])>0.4
