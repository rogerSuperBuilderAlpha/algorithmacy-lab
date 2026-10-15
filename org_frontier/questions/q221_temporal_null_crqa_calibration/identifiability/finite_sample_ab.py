"""Finite-sample check of the A/B counterexample with q220's ACTUAL pipeline code (read-only imports):
crqa.trajectory -> stage2.observe.coupling(timestamp, full series) -> centrality -> bottleneck_scores.

Settings copied from q220 stage 2: STEPS 600, WARMUP 20, FLIP 0.08, MAX_LAG 10, PROM_FLOOR 0.05, MIN_PAIRS 30.
Seeds: trajectory seed 41_000 + r (r = 0..399) — disjoint from every q220 seed range and from the q221 pilot
(40_000..40_999 reserved for the pilot proper). Same seed list for both systems (common random numbers for
the start state and flip draws; the rule differs only in H).
"""
import sys
import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.questions.q220_observation_process_robustness.stage2 import observe as ob

STEPS, WARMUP, FLIP = 600, 20, 0.08
MAX_LAG, PROM_FLOOR, MIN_PAIRS = 10, 0.05, 30
R = int(sys.argv[1]) if len(sys.argv) > 1 else 400
SEED0 = 41_000

SYSTEMS = {
    "A_self": [lambda x: x[0], lambda x: x[1], lambda x: x[2]],
    "B_xor":  [lambda x: x[0], lambda x: x[1], lambda x: x[0] ^ x[1]],
}
# exact-Φ bottleneck sets are filled in from results/check_ab.txt by the note; scoring here uses the
# argmax set only (pick distribution), so no Φ is needed in this script.


def run(rules):
    out = {k: [] for k in ("maxprom", "maxcc", "any", "lag0", "Hauto1", "pick", "noev", "nties")}
    full_t = np.arange(STEPS)
    for r in range(R):
        raw = trajectory(rules, STEPS, np.random.default_rng(SEED0 + r), flip=FLIP, warmup=WARMUP)
        res = ob.coupling(full_t, raw, MAX_LAG, "timestamp", MIN_PAIRS)
        iu = np.triu_indices(3, 1)
        p = res["prom"][iu]
        cc = ob.centrality(res["prom"], PROM_FLOOR)
        top = cc.max()
        M = np.flatnonzero(cc >= top - 1e-12)
        out["maxprom"].append(p.max())
        out["maxcc"].append(top)
        out["any"].append(float((p > PROM_FLOOR).any()))
        out["lag0"].append(np.mean([(raw[:, a] == raw[:, b]).mean() for a, b in zip(*iu)]))
        out["Hauto1"].append((raw[1:, 2] == raw[:-1, 2]).mean())
        out["noev"].append(float(top <= 0))
        out["nties"].append(M.size)
        out["pick"].append(tuple(int(i) for i in M))
    return out


def se(v):
    v = np.asarray(v, float)
    return v.std(ddof=1) / np.sqrt(v.size)


res = {k: run(v) for k, v in SYSTEMS.items()}
print("R = %d trajectories per system, seeds %d..%d" % (R, SEED0, SEED0 + R - 1))
print("%-32s %18s %18s" % ("statistic", "A_self", "B_xor"))
for k, lab in [("maxprom", "mean max pairwise prominence"), ("maxcc", "mean max centrality"),
               ("any", "any pair above 0.05"), ("lag0", "lag-0 cross match (pair mean)"),
               ("Hauto1", "H lag-1 self-match")]:
    a, b = res["A_self"][k], res["B_xor"][k]
    print("%-32s %10.4f ±%.4f %10.4f ±%.4f" % (lab, np.mean(a), se(a), np.mean(b), se(b)))
for name in SYSTEMS:
    picks = res[name]["pick"]
    ev = [p for p, ne in zip(picks, res[name]["noev"]) if not ne]
    share = {n: sum((n in p) / len(p) for p in ev) / max(len(ev), 1) for n in range(3)}
    print("%s: no-evidence %.3f; among evidence runs, tie-aware argmax share X/Y/H = %.3f/%.3f/%.3f; "
          "mean argmax-set size %.3f" % (name, np.mean(res[name]["noev"]), share[0], share[1], share[2],
                                          np.mean(res[name]["nties"])))
# per-pair prominence means (which pair carries the max)
for name, rules in SYSTEMS.items():
    pp = []
    for r in range(min(R, 400)):
        raw = trajectory(rules, STEPS, np.random.default_rng(SEED0 + r), flip=FLIP, warmup=WARMUP)
        pp.append(ob.coupling(np.arange(STEPS), raw, MAX_LAG, "timestamp", MIN_PAIRS)["prom"][np.triu_indices(3, 1)])
    pp = np.array(pp)
    print("%s mean prominence per pair (XY, XH, YH): %s" % (name, np.round(pp.mean(0), 4).tolist()))
