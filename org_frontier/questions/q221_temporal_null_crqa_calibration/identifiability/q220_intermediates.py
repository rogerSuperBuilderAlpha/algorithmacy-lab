"""Raw and intermediate saves of the repo's q220 pipeline on the lead pair P/Q (mandate: 'q220 pipeline raw /
intermediate saves + regression test'). Same settings as adjudicate.py part (c): T=600, flip 0.08, warmup 20,
max lag 10, timestamp alignment, MIN_PAIRS 30, centrality floor 0.05; seeds 43000..43004 (the first 5 of the
adjudication range). Saves per seed: SHA-256 of the raw trajectory, the 3x3 prominence matrix, centralities,
scores against own / other target. Output: results/q220_intermediates.json."""
import hashlib
import json
import os

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import pair_search as ps
from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact import TABLES

OUT = os.path.join(os.path.dirname(__file__), "results", "q220_intermediates.json")
PAIR = {"P": (("aff", 9, 6, 10), {0, 2}), "Q": (("aff", 9, 15, 10), {2})}
SEEDS = range(43_000, 43_005)


def run_one(fid, B, other, seed):
    raw = trajectory(ps.table_form(TABLES[fid]), 600, np.random.default_rng(seed), flip=0.08, warmup=20)
    c = ob.coupling(np.arange(600), raw, 10, "timestamp", 30)
    cc = ob.centrality(c["prom"], 0.05)
    s_own, _, noev = ob.bottleneck_scores(cc, B)
    s_oth, _, _ = ob.bottleneck_scores(cc, other)
    return {"seed": seed, "traj_sha256": hashlib.sha256(np.ascontiguousarray(raw, dtype=np.int8).tobytes()).hexdigest(),
            "prom": np.round(np.asarray(c["prom"], float), 12).tolist(),
            "centrality": np.round(np.asarray(cc, float), 12).tolist(),
            "score_own": float(s_own), "score_other": float(s_oth), "no_evidence": bool(noev)}


def compute():
    out = {}
    for nm, (fid, B) in PAIR.items():
        other = PAIR["Q" if nm == "P" else "P"][1]
        out[nm] = {"form": list(fid), "target": sorted(B), "runs": [run_one(fid, B, other, s) for s in SEEDS]}
    return out


if __name__ == "__main__":
    res = compute()
    json.dump(res, open(OUT, "w"), indent=1, sort_keys=True)
    for nm, r in res.items():
        print(nm, [(x["seed"], round(x["score_own"], 3), round(x["score_other"], 3)) for x in r["runs"]])
