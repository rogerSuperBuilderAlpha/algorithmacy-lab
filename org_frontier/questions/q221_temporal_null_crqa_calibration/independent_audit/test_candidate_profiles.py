"""Independent first-candidate profile regression; no PyPhi dependency."""
import numpy as np

A=((0,0,0,0,0,0,0,0),(1,1,1,1,0,0,0,0),(1,1,0,0,1,1,0,0))
B=((0,1,1,0,0,1,1,0),(1,1,1,1,0,0,0,0),(1,1,0,0,1,1,0,0))
P=0.08

def transition(tables):
    m=np.empty((8,8))
    for s in range(8):
        f=[tables[j][s] for j in range(3)]
        for z in range(8):
            m[s,z]=np.prod([1-P if ((z>>j)&1)==f[j] else P for j in range(3)])
    return m

def profiles(tables,maxlag=20):
    m=transition(tables)
    pi=np.full(8,1/8)
    for _ in range(500):
        pi=pi@m
    assert np.max(np.abs(pi@m-pi))<1e-12
    bits=np.array([[(s>>j)&1 for j in range(3)] for s in range(8)])
    out=[]
    for lag in range(maxlag+1):
        joint=pi[:,None]*np.linalg.matrix_power(m,lag)
        for i in range(3):
            for j in range(3):
                if i!=j:
                    out.append(float(joint[bits[:,i,None]==bits[None,:,j]].sum()))
    return np.array(out),pi

def test_first_candidate_profiles():
    a,pa=profiles(A)
    b,pb=profiles(B)
    assert not np.allclose(transition(A),transition(B))
    assert np.max(np.abs(a-b))<1e-12
    assert np.allclose(pa,[.23,.02,.23,.02,.23,.02,.23,.02],atol=1e-12)
    assert np.allclose(pb,np.full(8,1/8),atol=1e-12)
