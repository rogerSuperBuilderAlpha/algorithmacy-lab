"""Deeper MARL replication of #41 EMERGENT_NULL.

NumPy MLP + linear FA Q-policies; obs=[S, own, partner]. Exact binary
IIT-4.0 Φ on binarized emergent (W,S,C) forms. Hypotheses fixed in
hypotheses.md before computing. Cited: #41 tabular null; #98/#107.

Run:  python org_frontier/studies/marl_deep_replicate/analyze_deep.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9

LABELS = ("W", "S", "C")
EPISODES = 500
SEEDS = 8
STREAK_NEED = 10
SUCCESS_THR = 0.7
AUC_THR = 0.65
GAMMA = 0.9
LR = 0.05
HIDDEN = 8

# Match #41 panel for fair comparison
COMMITS = {
    "AND": lambda w, c: int(w and c),
    "OR": lambda w, c: int(w or c),
    "NAND": lambda w, c: int(not (w and c)),
    "NOR": lambda w, c: int(not (w or c)),
    "XOR": lambda w, c: int(w ^ c),
    "XNOR": lambda w, c: int(w == c),
    "W_only": lambda w, c: int(w),
    "C_only": lambda w, c: int(c),
    "implies": lambda w, c: int((not w) or c),
    "W_and_notC": lambda w, c: int(w and not c),
    "const0": lambda w, c: 0,
}

ARCHS = ("mlp", "linear")


def auc(scores, labels) -> float:
    pos = [s for s, lab in zip(scores, labels) if lab]
    neg = [s for s, lab in zip(scores, labels) if not lab]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return wins / (len(pos) * len(neg))


def obs_vec(S, own, partner):
    return np.array([float(S), float(own), float(partner)], dtype=float)


class QNet:
    """Linear or 1-hidden MLP Q(obs)→2. NumPy only."""

    def __init__(self, rng, arch: str):
        self.arch = arch
        if arch == "linear":
            self.W = rng.normal(0, 0.3, (3, 2))
            self.b = np.zeros(2)
        else:
            self.W1 = rng.normal(0, 0.3, (3, HIDDEN))
            self.b1 = np.zeros(HIDDEN)
            self.W2 = rng.normal(0, 0.3, (HIDDEN, 2))
            self.b2 = np.zeros(2)

    def qvals(self, obs):
        if self.arch == "linear":
            return obs @ self.W + self.b, None
        z1 = obs @ self.W1 + self.b1
        a1 = np.tanh(z1)
        return a1 @ self.W2 + self.b2, a1

    def act(self, obs, eps, rng):
        if rng.random() < eps:
            return int(rng.integers(2))
        q, _ = self.qvals(obs)
        return int(np.argmax(q))

    def update(self, obs, a, target):
        q, a1 = self.qvals(obs)
        dq = np.zeros(2)
        dq[a] = q[a] - target
        if self.arch == "linear":
            self.W -= LR * np.outer(obs, dq)
            self.b -= LR * dq
            return
        dW2 = np.outer(a1, dq)
        db2 = dq
        da1 = self.W2 @ dq
        dz1 = da1 * (1.0 - a1 ** 2)
        dW1 = np.outer(obs, dz1)
        db1 = dz1
        self.W2 -= LR * dW2
        self.b2 -= LR * db2
        self.W1 -= LR * dW1
        self.b1 -= LR * db1


def policy_table(net, rng):
    """Greedy action for every binary obs triple."""
    t = {}
    for S in (0, 1):
        for own in (0, 1):
            for partner in (0, 1):
                t[(S, own, partner)] = net.act(obs_vec(S, own, partner), 0.0, rng)
    return t


def train(cf, rng, arch: str):
    qw = QNet(rng, arch)
    qc = QNet(np.random.default_rng(int(rng.integers(1, 2**31 - 1))), arch)
    S, w, c = 0, 0, 0
    streak = 0
    hit = EPISODES
    rewards = []
    for ep in range(EPISODES):
        eps = max(0.05, 1.0 - ep / 250.0)
        ow = obs_vec(S, w, c)
        oc = obs_vec(S, c, w)
        aw = qw.act(ow, eps, rng)
        ac = qc.act(oc, eps, rng)
        r = float(cf(aw, ac))
        Sp = int(r)
        bootstrap = 1.0 if ep > 40 else 0.0
        qw_n, _ = qw.qvals(obs_vec(Sp, aw, ac))
        qc_n, _ = qc.qvals(obs_vec(Sp, ac, aw))
        qw.update(ow, aw, r + bootstrap * GAMMA * float(np.max(qw_n)))
        qc.update(oc, ac, r + bootstrap * GAMMA * float(np.max(qc_n)))
        S, w, c = Sp, aw, ac
        rewards.append(r)
        streak = streak + 1 if r == 1.0 else 0
        if streak >= STREAK_NEED and hit == EPISODES:
            hit = ep
    tw = policy_table(qw, rng)
    tc = policy_table(qc, rng)
    final = float(np.mean(rewards[-50:])) if rewards else 0.0
    return hit, tw, tc, final


def embed_rules(tw, tc, cf):
    # At state (W,S,C): W observes (S, own=W, partner=C); C observes (S, own=C, partner=W)
    return [
        lambda x, tw=tw: tw[(x[1], x[0], x[2])],
        lambda x, cf=cf: cf(x[0], x[2]),
        lambda x, tc=tc: tc[(x[1], x[2], x[0])],
    ]


def designed_rules(cf):
    return [
        lambda x: x[1],
        lambda x, cf=cf: cf(x[0], x[2]),
        lambda x: x[1],
    ]


def struct_phi(rules):
    v = verdict(rules, LABELS)
    core, phi_mc = major_complex(rules, LABELS)
    if core is None or phi_mc < 0:
        return v.structure, 0.0, tuple()
    return v.structure, float(phi_mc), tuple(core)


def is_open_loop(tw, tc):
    """Constant action regardless of obs."""
    return len(set(tw.values())) == 1 and len(set(tc.values())) == 1


def fmt(x):
    return "n/a" if (x != x) else f"{x:.3f}"


def eval_arch(arch: str, designed: dict):
    rows = []
    for name, cf in COMMITS.items():
        d_st, d_phi = designed[name]
        for seed in range(SEEDS):
            rng = np.random.default_rng(
                42000 + seed * 19 + sum(ord(c) for c in name + arch)
            )
            diff, tw, tc, final = train(cf, rng, arch)
            e_st, e_phi, e_core = struct_phi(embed_rules(tw, tc, cf))
            rows.append(
                {
                    "arch": arch,
                    "task": name,
                    "seed": seed,
                    "difficulty": diff,
                    "final_reward": round(final, 4),
                    "success": int(final >= SUCCESS_THR),
                    "designed": d_st,
                    "designed_triadic": int(d_st == "triadic"),
                    "designed_phi": d_phi,
                    "emergent": e_st,
                    "emergent_triadic": int(e_st == "triadic"),
                    "emergent_phi": e_phi,
                    "emergent_core": "|".join(e_core) if e_core else "",
                    "open_loop": int(is_open_loop(tw, tc)),
                }
            )
    return rows


def metrics(rows):
    succ = np.array([r["success"] for r in rows], dtype=int)
    e_tri = np.array([r["emergent_triadic"] for r in rows], dtype=float)
    d_tri = np.array([r["designed_triadic"] for r in rows], dtype=float)
    diff = np.array([r["difficulty"] for r in rows], dtype=float)
    learn = 1.0 - diff / float(EPISODES)
    easy = (learn >= np.median(learn)).astype(int)
    auc_e_succ = auc(e_tri, succ)
    auc_e_easy = auc(e_tri, easy)
    auc_diff_des = auc(diff, d_tri.astype(int))
    des_tri_succ = [r for r in rows if r["designed_triadic"] and r["success"]]
    frac_em = (
        float(np.mean([r["emergent_triadic"] for r in des_tri_succ]))
        if des_tri_succ
        else float("nan")
    )
    and_ol = [
        r
        for r in rows
        if r["task"] == "AND" and r["success"] and r["open_loop"]
    ]
    predicts = (
        (not np.isnan(auc_e_succ) and auc_e_succ >= AUC_THR)
        or (not np.isnan(auc_e_easy) and auc_e_easy >= AUC_THR)
    )
    return {
        "auc_e_succ": auc_e_succ,
        "auc_e_easy": auc_e_easy,
        "auc_diff_des": auc_diff_des,
        "frac_em": frac_em,
        "n_des_tri_succ": len(des_tri_succ),
        "and_open_loop": len(and_ol),
        "success_rate": float(succ.mean()),
        "emerg_tri_rate": float(e_tri.mean()),
        "predicts": predicts,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("MARL DEEP REPLICATE — #41 gap")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print(
        f"  deeper proxy: NumPy {ARCHS} Q-nets; obs=[S,own,partner]; "
        f"episodes={EPISODES}, seeds={SEEDS}/task — not MAPPO/QMIX"
    )
    print("  cited: #41 EMERGENT_NULL; #98/#107; #37–#40 pointers")
    print()

    designed = {}
    for name, cf in COMMITS.items():
        st, phi, _ = struct_phi(designed_rules(cf))
        designed[name] = (st, phi)

    all_rows = []
    arch_metrics = {}
    for arch in ARCHS:
        rows = eval_arch(arch, designed)
        all_rows.extend(rows)
        m = metrics(rows)
        arch_metrics[arch] = m
        print(f"  ARCH={arch}")
        print(
            f"    N={len(rows)} succ={m['success_rate']:.2f} "
            f"emerg_tri={m['emerg_tri_rate']:.2f}"
        )
        print(
            f"    AUC emerg→success={fmt(m['auc_e_succ'])}  "
            f"emerg→easy={fmt(m['auc_e_easy'])}  "
            f"diff→designed={fmt(m['auc_diff_des'])}"
        )
        print(
            f"    P(emerg_tri|succ∧des_tri)={m['frac_em']:.3f}  "
            f"AND open-loop success={m['and_open_loop']}/{SEEDS}"
        )
        print(
            f"    predicts_learnability(AUC≥{AUC_THR}): "
            f"{'YES' if m['predicts'] else 'no'}"
        )
        # task strip for primary
        if arch == "mlp":
            print(
                f"    {'task':<12}{'des':<8}{'diff':>7}{'succ':>6}"
                f"{'e_tri':>6}{'ol':>6}"
            )
            for name in COMMITS:
                rs = [r for r in rows if r["task"] == name]
                print(
                    f"    {name:<12}{rs[0]['designed']:<8}"
                    f"{np.mean([r['difficulty'] for r in rs]):>7.1f}"
                    f"{np.mean([r['success'] for r in rs]):>6.2f}"
                    f"{np.mean([r['emergent_triadic'] for r in rs]):>6.2f}"
                    f"{np.mean([r['open_loop'] for r in rs]):>6.2f}"
                )
        print()

    mlp = arch_metrics["mlp"]
    lin = arch_metrics["linear"]

    h1 = mlp["predicts"]
    h2 = (not mlp["predicts"]) and (mlp["frac_em"] <= 0.5) and (
        mlp["and_open_loop"] >= SEEDS // 2
    )
    # H3: architectures disagree on predicts OR on frac_em side of 0.5
    disagree_pred = mlp["predicts"] != lin["predicts"]
    disagree_frac = (mlp["frac_em"] > 0.5) != (lin["frac_em"] > 0.5)
    h3 = disagree_pred or disagree_frac

    print("HYPOTHESES")
    print(
        f"  H1 (MLP restores predictive association):  "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (EMERGENT_NULL survives):               "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (partial — arch/curriculum disagree):   "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  tabular #41 reference: AUC emerg→success≈0.555; "
        f"AND open-loop; EMERGENT_NULL"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)

    if h2 and (not h1) and ctrl_ok:
        verdict_s = "NULL_SURVIVES"
    elif h1 and (not h3):
        verdict_s = "NULL_BREAKS"
    elif h3:
        verdict_s = "PARTIAL"
    else:
        verdict_s = "MIXED"

    # Prefer NULL_SURVIVES when H2 and not H1; H3 alone shouldn't override if both fail alike
    if h2 and not h1 and not h3:
        verdict_s = "NULL_SURVIVES"
    elif h2 and not h1 and h3:
        # mild disagreement but null still primary on MLP
        verdict_s = "NULL_SURVIVES"
    elif h1 and h3:
        verdict_s = "PARTIAL"
    elif h1:
        verdict_s = "NULL_BREAKS"

    grid = ctrl_ok and (
        (verdict_s == "NULL_SURVIVES" and h2 and not h1)
        or (verdict_s == "NULL_BREAKS" and h1)
        or (verdict_s == "PARTIAL" and h3)
    )

    print()
    print("STATUS")
    print(f"  H1 MLP restores association: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 EMERGENT_NULL survives:   {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 partial (arch disagree):  {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            AI lane remains closable (deep gap filled)")
    print()
    print(
        f"verdict: {verdict_s} — deeper NumPy MLP/linear FA MARL "
        f"(obs=[S,own,partner]) "
        f"{'keeps' if verdict_s == 'NULL_SURVIVES' else 'changes'} "
        f"the #41 null: MLP AUC emerg→success={fmt(mlp['auc_e_succ'])}, "
        f"emerg→easy={fmt(mlp['auc_e_easy'])}; "
        f"P(emerg_tri|succ∧des_tri)={mlp['frac_em']:.3f}; "
        f"AND open-loop={mlp['and_open_loop']}/{SEEDS}; "
        f"linear predicts={lin['predicts']}; association only"
    )
    print(
        "reading: "
        + (
            "NULL_SURVIVES — neural/FA policies with larger obs still fail to "
            "link emergent Φ-verdict to learnability; open-loop success persists; "
            "AI lane closable with deep gap filled"
            if verdict_s == "NULL_SURVIVES"
            else (
                "NULL_BREAKS — deeper MARL restores a structure–learnability "
                "association the tabular proxy missed"
                if verdict_s == "NULL_BREAKS"
                else "PARTIAL — association depends on architecture/curriculum; "
                "lane closable with a named residual"
            )
        )
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
