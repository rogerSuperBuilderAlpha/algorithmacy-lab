"""Exact truth-table symmetry regression for the matched-profile affine pair."""
import itertools
import numpy as np

A=np.array([[0,1,1,0,0,1,1,0],[1,1,1,1,0,0,0,0],[1,1,0,0,1,1,0,0]],dtype=int)
B=np.array([[1,0,1,0,0,1,0,1],[1,1,1,1,0,0,0,0],[1,1,0,0,1,1,0,0]],dtype=int)

def transform(tab,perm,mask):
    """New node perm[j] is old node j; mask flips values in old labels."""
    out=np.zeros((3,8),dtype=int)
    for state in range(8):
        newbits=[(state>>j)&1 for j in range(3)]
        oldbits=[newbits[perm[j]] ^ ((mask>>j)&1) for j in range(3)]
        oldstate=sum(bit<<j for j,bit in enumerate(oldbits))
        for j in range(3):
            out[perm[j],state]=tab[j,oldstate]^((mask>>j)&1)
    return out

def test_matched_profile_pair_is_equivalent_under_48_group():
    matches=[(perm,mask) for perm in itertools.permutations(range(3))
             for mask in range(8) if np.array_equal(transform(A,perm,mask),B)]
    assert matches==[((0,2,1),6),((0,2,1),7)]
