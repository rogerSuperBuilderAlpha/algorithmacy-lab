"""Hassan's committed candidate_finite_sample.py (unmodified: its simulate/measure functions are imported and used
as-is), applied to the lead NO-constant-node pair P/Q from adjudicate.py. Only the rule tables, truth sets and output
path differ. P: X'=~H, Y'=X^Y, H'=X^H (q161 B={X,H}); Q: X'=~H, Y'=~(X^Y^H), H'=X^H (q161 B={H})."""
import json
from pathlib import Path
import numpy as np
from org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit import candidate_finite_sample as cf

RULES = {"P": [lambda x, y, h: 1 - h, lambda x, y, h: x ^ y, lambda x, y, h: x ^ h],
         "Q": [lambda x, y, h: 1 - h, lambda x, y, h: 1 - (x ^ y ^ h), lambda x, y, h: x ^ h]}
TRUTH = {"P": {0, 2}, "Q": {2}}


def table(rules):  # little-endian s = X + 2Y + 4H, same convention as cf.simulate
    return np.array([[r(s & 1, (s >> 1) & 1, (s >> 2) & 1) for s in range(8)] for r in rules], dtype=np.int8)


out = {}
for name in ("P", "Q"):
    tb = table(RULES[name])
    data = np.array([cf.measure(cf.simulate(tb, i), TRUTH[name]) for i in range(cf.N)])
    other = TRUTH["Q" if name == "P" else "P"]
    data_o = np.array([cf.measure(cf.simulate(tb, i), other)[2] for i in range(cf.N)])
    out[name] = dict(truth_tables=tb.tolist(), max_prominence_mean=float(data[:, 0].mean()),
                     max_centrality_mean=float(data[:, 1].mean()), any_prominence_above_floor=float(np.mean(data[:, 0] > cf.F)),
                     no_evidence=float(data[:, 3].mean()), bn_score=float(data[:, 2].mean()),
                     bn_score_se=float(data[:, 2].std(ddof=1) / np.sqrt(cf.N)),
                     bn_score_vs_other_target=float(data_o.mean()), chance=len(TRUTH[name]) / 3)
out["design"] = dict(exploratory=True, script="independent_audit/candidate_finite_sample.py (simulate, measure)",
                     seeds_per_system=cf.N, seeds="0..N-1, same for P and Q", steps=cf.T, warmup=cf.W, flip=cf.P,
                     max_lag=cf.L, prom_floor=cf.F)
dest = Path(__file__).parent / "results" / "pinned_env_runs" / "lead_pair_finite_sample.json"
dest.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
