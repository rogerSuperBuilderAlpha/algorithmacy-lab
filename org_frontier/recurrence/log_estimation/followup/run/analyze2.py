"""O13 follow-up, per ../../../algorithmacy-lab/org_frontier/recurrence/log_estimation/followup/HYPOTHESES.md.
Run: PYTHONPATH=/workspace/algorithmacy-work/stub:/workspace/algorithmacy-lab PYPHI_WELCOME_OFF=true \
     /workspace/algorithmacy-work/venv/bin/python -u analyze2.py [instrument|real]"""
import glob, json, sys, os, itertools, collections
import numpy as np, pandas as pd, pyphi
from pyphi import new_big_phi
from multiprocessing import Pool
pyphi.config.PROGRESS_BARS = False; pyphi.config.PARALLEL = False
LAB = ("W", "M", "C", "K"); NB = int(os.environ.get("NB", 200)); NS = int(os.environ.get("NS", 100))
NR = int(os.environ.get("NR", 100)); KB = int(os.environ.get("KB", 200))
rng = np.random.default_rng(20261030)
BOTS = {"k8s-ci-robot", "kubernetes-prow[bot]", "bors", "rust-bors[bot]", "rustbot"}
def isbot(a): return a in BOTS or "bot" in str(a).lower()

def phi_max(tpm):
    n = tpm.shape[1]; net = pyphi.Network(tpm, node_labels=LAB[:n]); best = (0.0, "")
    for i in range(2 ** n):
        st = tuple((i >> k) & 1 for k in range(n)); r = new_big_phi.maximal_complex(net, st)
        if r.phi > best[0] + 1e-9: best = (float(r.phi), "".join(sorted(LAB[j] for j in r.node_indices)))
    return best
def core_noK(core): return "".join(c for c in core if c != "K")
def multi_MC(core): c = core_noK(core); return len(c) >= 2 and "M" in c and "C" in c

# ---- transitions from segments (bootstrap joins never create fake transitions)
def pairs(segs, lag=1):
    P, Q = [], []
    for s in segs:
        if len(s) > lag:
            P.append(np.hstack([s[lag - l: len(s) - l] for l in range(1, lag + 1)])); Q.append(s[lag:])
    return np.vstack(P), np.vstack(Q)
def bic_select(Xp, y, cand):
    N = len(y); best = None
    for r in range(len(cand) + 1):
        for S in itertools.combinations(cand, r):
            key = Xp[:, list(S)] @ (1 << np.arange(len(S))) if S else np.zeros(N, int)
            ll = 0.0
            for k in np.unique(key):
                m = key == k; n1 = y[m].sum(); n = m.sum(); p = n1 / n
                if 0 < p < 1: ll += n1 * np.log(p) + (n - n1) * np.log(1 - p)
            b = -2 * ll + (2 ** len(S)) * np.log(N)
            if best is None or b < best[0]: best = (b, S)
    return best
def rule_tpm(segs, n):
    P, Q = pairs(segs); tpm = np.zeros((2 ** n, n)); parents = []
    for i in range(n):
        _, S = bic_select(P, Q[:, i], tuple(range(n))); parents.append(S)
        key = P[:, list(S)] @ (1 << np.arange(len(S))) if S else np.zeros(len(P), int)
        for s in range(2 ** n):
            st = np.array([(s >> k) & 1 for k in range(n)]); ks = int(st[list(S)] @ (1 << np.arange(len(S)))) if S else 0
            m = key == ks; tpm[s, i] = (Q[m, i].sum() + 1) / (m.sum() + 2)
    return tpm, parents
def order2(segs, n):
    P1, Q1 = pairs(segs, 1); P2, Q2 = pairs(segs, 2); out = []
    for i in range(n):
        b1 = bic_select(P2[:, :n], Q2[:, i], tuple(range(n)))[0]   # same sample, lag-1 vars only
        b2 = bic_select(P2, Q2[:, i], tuple(range(2 * n)))
        out.append(dict(node=LAB[i], bic1=round(b1, 1), bic2=round(b2[0], 1), order2_preferred=b2[0] < b1, parents2=[f"{LAB[j % n]}{'t-1' if j < n else 't-2'}" for j in b2[1]]))
    return out
def table_post(segs, n, a=1.0):
    P, Q = pairs(segs); c = np.zeros(2 ** n); c1 = np.zeros((2 ** n, n))
    key = P @ (1 << np.arange(n))
    for s in range(2 ** n): m = key == s; c[s] = m.sum(); c1[s] = Q[m].sum(0)
    return c1, c
def blocks(X, L=24):
    nb = len(X) // L; starts = rng.integers(0, len(X) - L, nb); return [X[s:s + L] for s in starts]
def circ(X):
    Y = X.copy()
    for j in range(3): Y[:, j] = np.roll(X[:, j], rng.integers(24, len(X) - 24))
    return Y
def boot_one(args):
    X, seed = args; global rng; rng = np.random.default_rng(seed)
    t, par = rule_tpm(blocks(X), X.shape[1]); ph = phi_max(t); return ph, [list(p) for p in par]
def surr_one(args):
    X, seed = args; global rng; rng = np.random.default_rng(seed); return phi_max(rule_tpm([circ(X)], X.shape[1])[0])
def tdraw(args):
    c1, c, seed = args; r = np.random.default_rng(seed); return phi_max(r.beta(c1 + 1, c[:, None] - c1 + 1))

# ---- instrument
V11 = [lambda x: x[1], lambda x: x[2], lambda x: x[0]]           # W'=M, M'=C, C'=W
V9 = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]     # W'=S, S'=W&C, C'=S
def simulate(rules, T, eps, seed):
    r = np.random.default_rng(seed); x = r.integers(0, 2, 3); out = []
    for t in range(T):
        nx = np.array([f(x) for f in rules]); fl = r.random(3) < eps; x = np.where(fl, 1 - nx, nx)
        out.append(np.r_[x, int(t % 24 < 12)])
    return np.array(out)
def inst_one(args):
    name, seed = args; X = simulate({'v11':V11,'v9':V9}[name], 2160, 0.05, seed); return phi_max(rule_tpm([X], 4)[0])

# ---- real data
def load():
    ev = pd.concat([pd.read_json(f, lines=True) for f in glob.glob("../ev2/*.jsonl") if os.path.getsize(f)])
    ev["t"] = pd.to_datetime(ev.t, utc=True); ev["bot"] = ev.actor.map(isbot); return ev
def build(repo, ev):
    d = ev[ev.repo == repo].copy(); H = pd.date_range("2024-04-01", "2024-06-30", freq="1h", inclusive="left", tz="UTC")
    d["h"] = d.t.dt.floor("1h"); body = d.body.fillna("").str.strip().str.lower()
    op = d[(d.type == "PullRequestEvent") & (d.action == "opened")].groupby("num").h.min()
    cl = d[(d.type == "PullRequestEvent") & (d.action == "closed")].groupby("num").h.min()
    mg = d[(d.type == "PullRequestEvent") & (d.action == "closed") & (d.merged == True)]
    appr = d[((d.type == "PullRequestReviewEvent") & (d.review == "approved") & ~d.bot) |
             ((d.type == "IssueCommentEvent") & ~d.bot & d.is_pr.astype(bool) & (body.str.startswith("/lgtm") | body.str.startswith("/approve") | body.str.contains("@bors r+", regex=False)))]
    ap = appr.groupby("num").h.min()
    pr = pd.DataFrame({"op": op}).join(ap.rename("ap")).join(cl.rename("cl"))
    hi = pd.Series(np.arange(len(H)), index=H)
    def cnt(start, end):
        a = np.zeros(len(H) + 1)
        for s, e in zip(start, end):
            if pd.isna(s): continue
            i = hi[s]; j = len(H) if pd.isna(e) else hi[e]
            if j > i: a[i] += 1; a[j] -= 1
        return np.cumsum(a)[:len(H)]
    await_ = cnt(pr.op, pr[["ap", "cl"]].min(axis=1)); apnm = cnt(pr.ap.where(pr.ap.notna() & (pr.ap >= pr.op)), pr.cl)
    def above_q(x, q=.5): s = pd.Series(x); return (s > s.rolling(168, min_periods=24).quantile(q).shift(1)).astype(int).values
    thr = {}
    def enc(x, name):
        b = above_q(x); m = b[168:].mean(); thr[name] = "median"
        if m < .05: b = above_q(x, .4); thr[name] = f"40th pct (median gave {m:.3f})"
        elif m > .95: b = above_q(x, .6); thr[name] = f"60th pct (median gave {m:.3f})"
        return b
    W = enc(await_, "W"); C = enc(apnm, "C"); M = H.isin(mg.h).astype(int)
    act = pd.Series(0, index=H); act[:] = H.isin(pd.concat([mg.h, appr.h])).astype(int)
    how = H.dayofweek * 24 + H.hour; rate = act.groupby(how).mean(); busy = set(rate[rate >= rate.median()].index)
    K = np.array([h in busy for h in how], int)
    X = np.c_[W, M, C, K][168:]
    info = dict(n_prs=len(pr), n_merged=int(mg.num.nunique()), bot_merge_share=round(float(mg.actor.map(isbot).mean()), 3),
                marginals=X.mean(0).round(3).tolist(), thresholds=thr)
    return X, info

def run_repo(repo, ev, pool, seedbase):
    X, info = build(repo, ev); r = dict(info); n = 4
    c1, c = table_post([X], n); r["state_visits"] = c.astype(int).tolist(); r["states_ge20"] = int((c >= 20).sum())
    r["H1"] = r["states_ge20"] >= 12; r["marginals_ok"] = bool(((X.mean(0) >= .05) & (X.mean(0) <= .95)).all())
    tpm, par = rule_tpm([X], n); r["parents"] = {LAB[i]: [LAB[j] for j in p] for i, p in enumerate(par)}
    r["phi_rule"] = phi_max(tpm); r["phi_rule_denoised"] = phi_max((tpm > 0.5).astype(float))
    bs = pool.map(boot_one, [(X, seedbase + i) for i in range(NB)])
    v = np.array([b[0][0] for b in bs]); cores = [b[0][1] for b in bs]
    r["boot_phi_median"] = float(np.median(v)); r["boot_phi_90"] = [float(np.quantile(v, .05)), float(np.quantile(v, .95))]
    r["P_multi_MC"] = float(np.mean([multi_MC(k) for k in cores])); r["boot_core_freq"] = dict(collections.Counter(cores).most_common(6))
    r["P_C_in_parents_M"] = float(np.mean([2 in b[1][1] for b in bs]))
    nul = np.array([s[0] for s in pool.map(surr_one, [(X, seedbase + 10000 + i) for i in range(NS)])])
    r["null_median"] = float(np.median(nul)); r["null_95"] = float(np.quantile(nul, .95)); r["exceeds_null"] = r["phi_rule"][0] > r["null_95"]
    tb = pool.map(tdraw, [(c1, c, seedbase + 20000 + i) for i in range(KB)])
    tv = np.array([t[0] for t in tb]); r["table_phi_median"] = float(np.median(tv)); r["table_phi_90"] = [float(np.quantile(tv, .05)), float(np.quantile(tv, .95))]
    r["table_P_multi_MC"] = float(np.mean([multi_MC(t[1]) for t in tb])); r["table_core_freq"] = dict(collections.Counter(t[1] for t in tb).most_common(5))
    o2 = order2([X], n); r["order2"] = o2; r["H5"] = sum(not o["order2_preferred"] for o in o2[:3]) >= 2
    # sensitivity: drop the clock party
    t3, p3 = rule_tpm([X[:, :3]], 3); r["noK_phi_rule"] = phi_max(t3); r["noK_parents"] = {LAB[i]: [LAB[j] for j in p] for i, p in enumerate(p3)}
    r["H2_conditions"] = r["P_multi_MC"] >= .8 and r["exceeds_null"]
    r["verdict"] = ("no verdict (H1 failed)" if not r["H1"] else "triadic" if r["H2_conditions"] else "dyadic" if r["P_multi_MC"] <= .2 else "undetermined")
    return r

if __name__ == "__main__":
    mode = sys.argv[1]; pool = Pool(8); out = {}
    if mode == "instrument":
        dec = phi_max(np.array([[(s >> k) & 1 for k in range(3)] for s in range(8)], float))
        cyc = phi_max(np.array([[f(np.array([(s >> k) & 1 for k in range(3)])) for f in V11] for s in range(8)], float))
        out["controls"] = dict(decoupled=dec, cycle=cyc, pass_=len(dec[1]) < 2 and cyc[0] > 0 and len(cyc[1]) == 3); print(out["controls"])
        for name, rules in [("v11", V11), ("v9", V9)]:
            truth = phi_max(np.array([[f(np.array([(s >> k) & 1 for k in range(3)])) for f in rules] for s in range(8)], float))
            res = pool.map(inst_one, [(name, 1000 * (name == "v9") + i) for i in range(NR)])
            rec = float(np.mean([core_noK(c) == truth[1] for _, c in res]))
            out[name] = dict(true=truth, recovery=rec, pass_=rec >= .8, cores=dict(collections.Counter(c for _, c in res).most_common(5)))
            print(name, out[name])
        json.dump(out, open("instrument.json", "w"), indent=1, default=str)
    else:
        out = json.load(open("results2.json")) if os.path.exists("results2.json") else {"repos": {}}
        ev = load()
        for i, repo in enumerate(["kubernetes/kubernetes", "rust-lang/rust", "django/django", "facebook/react", "microsoft/vscode"]):
            if repo in out["repos"]: print("skip (checkpointed)", repo); continue
            r = run_repo(repo, ev, pool, 100000 * (i + 1)); out["repos"][repo] = r
            print(repo, json.dumps(r, default=str)); json.dump(out, open("results2.json", "w"), indent=1, default=str)
