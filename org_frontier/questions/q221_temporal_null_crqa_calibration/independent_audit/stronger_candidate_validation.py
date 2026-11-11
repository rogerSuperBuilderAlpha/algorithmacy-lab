"""Exploratory full-profile candidate validation, NumPy only.

Candidate A aff(9,6,10), B aff(9,15,10). Exact stationary profiles,
finite-sample q220-style prominence/centrality and held-out nearest centroid.
Not a PyPhi calculation and not a confirmatory study.
"""
import json
from pathlib import Path
import numpy as np

P=.08; T=600; W=20; N=240; L=10; FLOOR=.05
IDS={"A":(9,6,10),"B":(9,15,10)}
S=((np.arange(8)[:,None]>>np.arange(3))&1).astype(int)

def rules(codes):
    return np.array([[((int(s)&(c>>1)).bit_count()&1)^(c&1)
                      for s in range(8)] for c in codes],dtype=np.int8)

def tpm(t):
    return np.prod(np.where(t.T[:,None,:]==S[None,:,:],1-P,P),axis=2)

def stationary(m):
    p=np.full(8,.125)
    for _ in range(1000):p=p@m
    assert np.max(abs(p@m-p))<1e-12
    return p

def profiles(m,p):
    q=np.eye(8);out=np.empty((21,3,3))
    for lag in range(21):
        joint=p[:,None]*q
        for a in range(3):
            for b in range(3):
                out[lag,a,b]=joint[S[:,a,None]==S[None,:,b]].sum()
        q=q@m
    return out

def simulate(t,seed):
    rng=np.random.default_rng(seed)
    state=rng.integers(0,2,3)
    out=np.empty((T,3),dtype=np.int8)
    for i in range(T+W):
        idx=int(state@np.array([1,2,4]))
        state=t[:,idx]^(rng.random(3)<P)
        if i>=W:out[i-W]=state
    return out

def features(x):
    pr=[]
    for a in range(3):
        for b in range(a+1,3):
            rates=np.array([np.mean(x[max(0,-k):min(T,T-k),a] ==
                                    x[max(0,k):min(T,T+k),b])
                            for k in range(-L,L+1)])
            pr.append(float(rates.max()-np.median(rates)))
    pr=np.array(pr)
    cc=np.array([sum(pr[i] for i in ix if pr[i]>FLOOR)
                 for ix in [(0,1),(0,2),(1,2)]])
    return np.r_[pr,cc,
                 [float(np.mean(x[:,j])) for j in range(3)],
                 [float(np.mean(x[:-1,j]==x[1:,j])) for j in range(3)]]

def classify(a,b,columns):
    train=np.r_[a[:160],b[:160]][:,columns]
    test=np.r_[a[160:],b[160:]][:,columns]
    sd=train.std(axis=0);sd[sd<1e-10]=1
    mu=train.mean(axis=0)
    train=(train-mu)/sd;test=(test-mu)/sd
    c0=train[:160].mean(axis=0);c1=train[160:].mean(axis=0)
    pred=(np.sum((test-c1)**2,axis=1)<np.sum((test-c0)**2,axis=1))
    truth=np.r_[np.zeros(N-160,dtype=bool),np.ones(N-160,dtype=bool)]
    return dict(correct=int(np.sum(pred==truth)),total=len(truth),
                accuracy=float(np.mean(pred==truth)))

def main():
    m={k:tpm(rules(v)) for k,v in IDS.items()}
    pi={k:stationary(v) for k,v in m.items()}
    pr={k:profiles(m[k],pi[k]) for k in IDS}
    f={k:np.array([features(simulate(rules(v),i)) for i in range(N)])
       for k,v in IDS.items()}
    result=dict(status="exploratory",ids=IDS,
        design=dict(steps=T,warmup=W,flip=P,n_per_system=N,
                    train_per_system=160,test_per_system=80,lag=L),
        stationary={k:pi[k].tolist() for k in IDS},
        max_population_profile_difference=float(np.max(abs(pr["A"]-pr["B"]))),
        mean_features={k:f[k].mean(axis=0).tolist() for k in IDS},
        heldout=dict(cross=classify(f["A"],f["B"],slice(0,6)),
                     marginal_self=classify(f["A"],f["B"],slice(6,12)),
                     combined=classify(f["A"],f["B"],slice(0,12))),
        caveats=["Post-hoc candidate selection","No independent PyPhi run",
                 "Held-out trajectories, not held-out forms",
                 "No proof of equal finite-sample feature laws"])
    Path(__file__).with_name("stronger_candidate_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
