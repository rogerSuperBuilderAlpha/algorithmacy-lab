"""Exploratory null-calibration pilot; not a preregistered CRQA experiment.
Run: python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.null_pilot
"""
import json
from pathlib import Path
import numpy as np

SEED=2212026
N=250
T=240
B=199
PERSISTENCE=(0.5,0.9,0.98)
ALPHA=0.05

def series(p, rng):
    x=np.empty(T,dtype=np.int8)
    x[0]=rng.integers(2)
    flips=rng.random(T-1)>p
    for t in range(1,T):
        x[t]=x[t-1]^flips[t-1]
    return x

def corr(a,b):
    x=a.astype(float)-np.mean(a)
    y=b.astype(float)-np.mean(b)
    d=np.linalg.norm(x)*np.linalg.norm(y)
    return float(x@y/d) if d>1e-12 else 0.0

def main():
    rng=np.random.default_rng(SEED)
    rows=[]
    for p in PERSISTENCE:
        counts={"shuffle":0,"circular_shift":0}
        degenerate=0
        for _ in range(N):
            x,y=series(p,rng),series(p,rng)
            degenerate+=int(np.all(x==x[0]) or np.all(y==y[0]))
            observed=abs(corr(x,y))
            for method in counts:
                exceed=0
                for _ in range(B):
                    z=rng.permutation(y) if method=="shuffle" else np.roll(y,int(rng.integers(1,T)))
                    exceed+=int(abs(corr(x,z))>=observed-1e-12)
                counts[method]+=int((1+exceed)/(B+1)<=ALPHA)
        rows.append(dict(persistence=p,independent_pairs=N,timepoints=T,surrogates=B,
                         degenerate_pairs=degenerate,shuffle_rejections=counts["shuffle"],
                         circular_shift_rejections=counts["circular_shift"],
                         shuffle_fpr=counts["shuffle"]/N,circular_shift_fpr=counts["circular_shift"]/N))
    result=dict(status="exploratory",seed=SEED,rows=rows,
                caveats=["Absolute zero-lag Pearson correlation, not CRQA",
                         "Undefined constant-series correlations mapped to zero",
                         "Circular shifts are not generally valid under all dependence regimes",
                         "Surrogate draws are not independent experimental units"])
    output=Path(__file__).with_name("null_pilot_results.json")
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
