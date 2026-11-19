"""Exhaustive post-hoc screen of the 7,488 recorded eligible candidate pairs.

Uses the original search's all_candidates list, independently computes stationary
within-channel match profiles at lags 0..20, and checks the 48-element node
permutation/value-flip symmetry group. Does NOT recompute PyPhi.
Run: python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.screen_all_candidates
"""
import itertools
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/"identifiability"/"results"/"pair_search.json"
FLIP=.08
PERMS=list(itertools.permutations(range(3)))

def tables(fid):
    family,*codes=fid
    out=[]
    for j,c in enumerate(codes):
        row=[]
        for s in range(8):
            if family=="aff":
                v=((s&(c>>1)).bit_count()&1)^(c&1)
            elif family=="nsi":
                others=[k for k in range(3) if k!=j]
                ix=((s>>others[0])&1)+2*((s>>others[1])&1)
                v=(c>>ix)&1
            else:
                raise ValueError(family)
            row.append(v)
        out.append(row)
    return np.asarray(out,dtype=np.int8)

def self_profiles(tab):
    states=(np.arange(8)[:,None]>>np.arange(3))&1
    transition=np.prod(np.where(tab.T[:,None,:]==states[None,:,:],1-FLIP,FLIP),axis=2)
    pi=np.full(8,1/8)
    for _ in range(400):
        pi=pi@transition
    assert np.max(np.abs(pi@transition-pi))<1e-11
    m=np.eye(8)
    result=[]
    for lag in range(21):
        joint=pi[:,None]*m
        for j in range(3):
            result.append(float(joint[states[:,j,None]==states[None,:,j]].sum()))
        m=m@transition
    return np.asarray(result)

def equivalent(a,b):
    for perm in PERMS:
        for mask in range(8):
            equal=True
            for s in range(8):
                old=sum(((((s>>perm[k])&1)^((mask>>k)&1)))<<k for k in range(3))
                for j in range(3):
                    if (int(a[j,old])^((mask>>j)&1))!=int(b[perm[j],s]):
                        equal=False
                        break
                if not equal:
                    break
            if equal:
                return True
    return False

def main():
    pairs=json.loads(SOURCE.read_text())["all_candidates"]
    cache={}
    for a,b in pairs:
        for fid in (a,b):
            key=tuple(fid)
            if key not in cache:
                t=tables(fid)
                cache[key]=(t,self_profiles(t))
    matched=[]
    noniso=[]
    for a,b in pairs:
        ta,fa=cache[tuple(a)]
        tb,fb=cache[tuple(b)]
        error=float(np.max(np.abs(fa-fb)))
        if error<1e-10:
            matched.append((a,b,error))
            if not equivalent(ta,tb):
                noniso.append((a,b,error))
    output=dict(status="exploratory",source="pair_search.json/all_candidates",
                pairs_total=len(pairs),unique_forms=len(cache),
                matched_self_profiles=len(matched),
                matched_self_profiles_nonisomorphic_48=len(noniso),
                tolerance=1e-10,lag_range=[0,20],flip=FLIP,
                examples=[dict(a=a,b=b,max_error=err) for a,b,err in noniso[:20]],
                caveats=["Original candidate search's eligible-target filter is inherited, not recomputed with PyPhi",
                         "Cross-channel matching is inherited from the search, not independently rechecked for every pair",
                         "Counts are pairs, not independent discoveries or symmetry-unique classes",
                         "Equal population recurrence profiles do not imply equal finite-sample distributions"])
    (ROOT/"screen_all_candidates_results.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))

if __name__=="__main__":
    main()
