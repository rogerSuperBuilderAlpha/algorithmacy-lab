"""Screen the 20 verified candidate pairs for matching stationary marginals.
Read-only, NumPy only. Run from repository root:
python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.screen_verified_marginals
"""
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
DATA=HERE.parent/"identifiability"/"results"/"pair_search.json"
P=.08

def stationary_marginals(tables):
    t=np.asarray(tables,dtype=int)
    states=((np.arange(8)[:,None]>>np.arange(3))&1)
    target=t.T
    matrix=np.prod(np.where(states[None,:,:]==target[:,None,:],1-P,P),axis=2)
    pi=np.full(8,1/8)
    for _ in range(2000):
        pi=pi@matrix
    if not np.allclose(pi@matrix,pi,atol=1e-12):
        raise AssertionError("stationary distribution not converged")
    return pi@states

def main():
    raw=json.loads(DATA.read_text())
    rows=[]
    for i,pair in enumerate(raw["verified"]):
        a=stationary_marginals(pair["a_tables"])
        b=stationary_marginals(pair["b_tables"])
        rows.append({"index":i,"a_id":pair["a_id"],"b_id":pair["b_id"],
            "marginals_a":a.tolist(),"marginals_b":b.tolist(),
            "max_difference":float(np.max(np.abs(a-b))),
            "match":bool(np.allclose(a,b,atol=1e-10,rtol=0))})
    result={"scope":"20 selected verified candidate pairs only","matches":sum(r["match"] for r in rows),
        "total":len(rows),"rows":rows,"status":"exploratory"}
    print(json.dumps(result,indent=2))
    (HERE/"screen_verified_marginals_results.json").write_text(json.dumps(result,indent=2)+"\n")
if __name__=="__main__":main()
