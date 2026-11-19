"""O13 pre-registered analysis (HYPOTHESES.md in org_frontier/recurrence/log_estimation).
Run: PYTHONPATH=../stub:/workspace/algorithmacy-lab PYPHI_WELCOME_OFF=true ../venv/bin/python analyze.py
"""
import glob, json, sys, itertools, collections
import numpy as np, pandas as pd, pyphi
from pyphi import new_big_phi
from org_frontier.recurrence.crqa import peak
pyphi.config.PROGRESS_BARS = False; pyphi.config.PARALLEL = False
rng = np.random.default_rng(2026)
import os; K = int(os.environ.get("K",500)); NSURR = int(os.environ.get("NS",200)); NREP = int(os.environ.get("NR",100)); LAB = ("W", "M", "C")
BOTS = {"k8s-ci-robot", "kubernetes-prow[bot]", "bors", "rust-bors[bot]", "rustbot"}
def isbot(a): return a in BOTS or "bot" in a.lower()

# ---------- Φ machinery ----------
_cache = {}
def phi_max(tpm, labels=LAB):
    n = tpm.shape[1]; net = pyphi.Network(tpm, node_labels=labels[:n]); best = (0.0, "")
    for i in range(2 ** n):
        st = tuple((i >> k) & 1 for k in range(n))
        r = new_big_phi.maximal_complex(net, st)
        if r.phi > best[0] + 1e-9:
            best = (float(r.phi), "".join(sorted(labels[j] for j in r.node_indices)))
    return best
def idx(s): return int(sum(int(b) << i for i, b in enumerate(s)))
def counts(X):
    n = X.shape[1]; c1 = np.zeros((2 ** n, n)); c = np.zeros(2 ** n)
    for t in range(len(X) - 1):
        i = idx(X[t]); c[i] += 1; c1[i] += X[t + 1]
    return c1, c
def post_mean(X, a=1.0):
    c1, c = counts(X); return (c1 + a) / (c[:, None] + 2 * a)
from multiprocessing import Pool
POOL=None
def pmap(tpms):
    return POOL.map(phi_max, tpms, chunksize=4)
def posterior(X, a=1.0, k=K):
    c1, c = counts(X)
    out = pmap([rng.beta(c1 + a, c[:, None] - c1 + a) for _ in range(k)])
    return np.array([o[0] for o in out]), [o[1] for o in out]
def multi_MC(core): return len(core) >= 2 and "M" in core and "C" in core
def circ(X):
    Y = X.copy()
    for j in range(X.shape[1]): Y[:, j] = np.roll(X[:, j], rng.integers(24, len(X) - 24))
    return Y

# ---------- instrument check ----------
def simulate(rules, T, eps, n=3):
    x = rng.integers(0, 2, n); out = []
    for _ in range(T):
        nx = np.array([r(x) for r in rules]); flip = rng.random(n) < eps
        x = np.where(flip, 1 - nx, nx); out.append(x.copy())
    return np.array(out)
V11 = [lambda x: x[2], lambda x: x[0], lambda x: x[1]]      # 3-node Prow projection: W=M(merged codebase), M=C, C=W
V9 = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]] # v9: W=S, S=W&C, C=S (S in the M slot)
def truth(rules):
    tpm = np.array([[r(np.array([(s >> k) & 1 for k in range(3)])) for r in rules] for s in range(8)], float)
    return phi_max(tpm)

def build(repo, ev, freq):
    d = ev[ev.repo == repo]
    W = d[((d.type == "PullRequestEvent") & d.action.isin(["opened", "synchronize", "reopened"]) & ~d.bot)]
    M = d[(d.type == "PullRequestEvent") & (d.action == "closed") & (d.merged == True)]
    body = d.body.fillna("").str.strip().str.lower()
    C = d[((d.type == "PullRequestReviewEvent") & (d.review == "approved") & ~d.bot) |
          ((d.type == "IssueCommentEvent") & ~d.bot & (body.str.startswith("/lgtm") | body.str.startswith("/approve") | body.str.contains("@bors r+", regex=False)))]
    idx_ = pd.date_range("2024-04-01", "2024-06-30", freq=freq, inclusive="left", tz="UTC")
    f = lambda s: idx_.isin(s.t.dt.floor(freq)).astype(int)
    botshare = (M.actor.map(isbot)).mean() if len(M) else np.nan
    return np.c_[f(W), f(M), f(C)], dict(nW=len(W), nM=len(M), nC=len(C), bot_merge_share=round(float(botshare), 3))

def main():
    R = {}
    print("== Instrument controls")
    dec = phi_max(np.array([[(s >> k) & 1 for k in range(3)] for s in range(8)], float))
    cyc = truth(V11); R["controls"] = dict(decoupled=dec, coupled_cycle=cyc)
    print("  decoupled", dec, "multi-node:", len(dec[1]) >= 2, "| coupled cycle", cyc)
    assert len(dec[1]) < 2 and cyc[0] > 0 and sorted(cyc[1]) == sorted("WMC")
    ev = pd.concat([pd.read_json(f, lines=True) for f in glob.glob("ev/*.jsonl") if open(f).read(1)])
    ev["t"] = pd.to_datetime(ev.t, utc=True); ev["bot"] = ev.actor.map(isbot)
    X, info = build("kubernetes/kubernetes", ev, "1h"); T = len(X); marg = X.mean(0)
    print("== Instrument check (blind recovery), T", T, "marginals", marg.round(3))
    R["instrument"] = {}
    for name, rules in [("v11_prow", V11), ("v9_human_merge", V9)]:
        tphi, tcore = truth(rules); res = pmap([post_mean(simulate(rules, T, 0.05)) for _ in range(NREP)]); hits = sum(r[1] == tcore for r in res)
        R["instrument"][name] = dict(true_core=tcore, true_phi=tphi, recovery=hits / NREP, passed=hits / NREP >= 0.8)
        print(" ", name, R["instrument"][name])
    if not all(v["passed"] for v in R["instrument"].values()):
        print("INSTRUMENT CHECK FAILED; real-data verdicts not read"); R["halt"] = "instrument"
    repos = sorted(ev.repo.unique()); R["repos"] = {}
    for repo in repos:
        for freq in ["1h", "15min", "4h"]:
            X, info = build(repo, ev, freq); c1, c = counts(X); key = f"{repo}@{freq}"
            r = dict(info, T=len(X), marginals=X.mean(0).round(3).tolist(), state_visits=c.astype(int).tolist(),
                     states_ge30=int((c >= 30).sum()))
            r["marginals_ok"] = bool(((X.mean(0) >= .05) & (X.mean(0) <= .95)).all())
            r["H1"] = r["states_ge30"] >= 6
            if freq == "1h" or r["H1"]:
                v, cores = posterior(X); obs = phi_max(post_mean(X))
                nul = np.array([o[0] for o in pmap([post_mean(circ(X)) for _ in range(NSURR if freq == "1h" else 50)])])
                pm = float(np.mean([multi_MC(k) for k in cores]))
                r.update(phi_median=float(np.median(v)), phi_90=[float(np.quantile(v, .05)), float(np.quantile(v, .95))],
                         P_multi_MC=pm, core_freq=dict(collections.Counter(cores).most_common()),
                         obs_postmean=obs, null_median=float(np.median(nul)), null_95=float(np.quantile(nul, .95)),
                         exceeds_null=obs[0] > np.quantile(nul, .95))
                r["verdict"] = ("inconclusive (H1 failed)" if not r["H1"] else
                                "triadic" if pm >= .8 and r["exceeds_null"] else "dyadic" if pm <= .2 else "undetermined")
                if freq == "1h":
                    # H3 collapse M: (W,C) only
                    v2, _ = posterior(X[:, [0, 2]], k=200)
                    r["H3"] = dict(phi_median_collapsed=float(np.median(v2)),
                                   rel_change=float((np.median(v2) - np.median(v)) / max(np.median(v), 1e-9)))
                    vs, _ = posterior(X, a=0.5, k=200); r["sens_a05_median"] = float(np.median(vs))
                    lag, prom = peak(X[:, 2], X[:, 1], max_lag=24)
                    r["H5"] = dict(peak_lag=lag, prominence=prom, pass_=lag > 0 and prom > 0.05)
                    pc = post_mean(X); r["C_to_M_effect"] = float(np.mean(pc[[4, 5, 6, 7], 1]) - np.mean(pc[[0, 1, 2, 3], 1]))
            R["repos"][key] = r
            print(key, json.dumps({k: r.get(k) for k in ["bot_merge_share", "nW", "nM", "nC", "marginals", "state_visits", "H1", "phi_median", "phi_90", "P_multi_MC", "core_freq", "obs_postmean", "null_95", "verdict", "H3", "H5", "sens_a05_median"]}, default=str))
    json.dump(R, open("results.json", "w"), indent=1, default=str)
if __name__ == '__main__':
    POOL = Pool(8)
    main()
