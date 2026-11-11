"""Exploratory finite-sample test of the first eligible q221 candidate pair."""
import json
import numpy as np
from pathlib import Path
A=np.array([[0]*8,[1,1,1,1,0,0,0,0],[1,1,0,0,1,1,0,0]],dtype=np.int8)
B=np.array([[0,1,1,0,0,1,1,0],[1,1,1,1,0,0,0,0],[1,1,0,0,1,1,0,0]],dtype=np.int8)
N,T,W,P,L,F=300,600,20,.08,10,.05
def simulate(rules,seed):
    rng=np.random.default_rng(seed)
    state=rng.integers(0,2,3)
    out=np.empty((T,3),dtype=np.int8)
    for t in range(T+W):
        idx=int(state[0]+2*state[1]+4*state[2])
        state=rules[:,idx].copy()^(rng.random(3)<P)
        if t>=W: out[t-W]=state
    return out
def measure(values,truth):
    from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
    result=ob.coupling(np.arange(T),values,L,"timestamp",30)
    prom=result["prom"]
    centrality=ob.centrality(prom,F)
    score,_,noev=ob.bottleneck_scores(centrality,truth)
    return float(prom[np.triu_indices(3,1)].max()),float(centrality.max()),float(score),bool(noev)
def main():
    output={}
    for name,rules,truth in [("A",A,{1,2}),("B",B,{2})]:
        data=np.array([measure(simulate(rules,i),truth) for i in range(N)])
        output[name]=dict(max_prominence_mean=float(data[:,0].mean()),max_centrality_mean=float(data[:,1].mean()),
            any_prominence_above_floor=float(np.mean(data[:,0]>F)),
            no_evidence=float(data[:,3].mean()),bn_score=float(data[:,2].mean()),
            chance=len(truth)/3)
    output["design"]=dict(exploratory=True,seeds_per_system=N,steps=T,warmup=W,flip=P,max_lag=L,prom_floor=F)
    dest=Path(__file__).with_name("candidate_finite_sample_results.json")
    dest.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))
if __name__=="__main__":main()
