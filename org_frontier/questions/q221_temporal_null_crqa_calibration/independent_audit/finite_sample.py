"""Exploratory finite-sample A/B comparison, not an IIT counterexample.
Run: python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.finite_sample
"""
import json
from pathlib import Path
import numpy as np

P=0.08
T=600
REPS=400
LAG=10
FLOOR=0.05

def trajectory(model,seed):
    rng=np.random.default_rng(seed)
    s=rng.integers(0,2,size=3,dtype=np.int8)
    out=np.zeros((T,3),dtype=np.int8)
    for t in range(T+20):
        x,y,h=map(int,s)
        nxt=np.array([x,y,h if model=="A" else h^x^y],dtype=np.int8)
        s=nxt^(rng.random(3)<P).astype(np.int8)
        if t>=20:
            out[t-20]=s
    return out

def features(a):
    from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
    result=ob.coupling(np.arange(T),a,LAG,"timestamp",30)
    prom=result["prom"]
    centrality=ob.centrality(prom,FLOOR)
    cross_lag0=[float(np.mean(a[:,i]==a[:,j])) for i in range(3) for j in range(i+1,3)]
    return [float(np.max(prom)),float(np.max(centrality)),
            float(np.mean(cross_lag0)),float(np.mean(a[:-1,2]==a[1:,2]))]

def main():
    results={}
    for model in ("A","B"):
        v=np.array([features(trajectory(model,seed)) for seed in range(REPS)])
        results[model]=dict(mean_max_pair_prominence=float(v[:,0].mean()),
            mean_max_centrality=float(v[:,1].mean()),
            mean_lag0_cross_match=float(v[:,2].mean()),
            mean_H_self_lag1_match=float(v[:,3].mean()),
            fraction_any_prominence_over_floor=float(np.mean(v[:,0]>FLOOR)),
            fraction_no_evidence=float(np.mean(v[:,1]<=0)),
            prominence_quantiles=np.quantile(v[:,0],[.05,.5,.95]).tolist())
    results["design"]=dict(status="exploratory",reps_per_model=REPS,steps=T,
        warmup=20,flip=P,max_lag=LAG,prom_floor=FLOOR,
        exact_phi_computed_here=False,original_pair_iit_bottleneck_eligible=False)
    Path(__file__).with_name("finite_sample_results.json").write_text(json.dumps(results,indent=2)+"\n")
    print(json.dumps(results,indent=2))

if __name__=="__main__":
    main()
