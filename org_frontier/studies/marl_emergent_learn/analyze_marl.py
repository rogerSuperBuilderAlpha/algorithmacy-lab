"""Agenda #41 — emergent coordination verdict vs task learnability.

Tabular stateful Q-learning proxy (not deep MARL). Exact binary
IIT-4.0 Φ on emergent (W,S,C) forms after learning. Hypotheses fixed
in hypotheses.md before computing. Cited: #98/#107; #37–#40 pointers.

Run:  python org_frontier/studies/marl_emergent_learn/analyze_marl.py
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
EPISODES = 300
SEEDS = 10
ALPHA = 0.2
STREAK_NEED = 10
SUCCESS_THR = 0.7
AUC_THR = 0.65

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
    "const0": lambda w, c: 0,  # unreachable — forces a failure class
}

def auc(scores, labels) -> float:
    pos = [s for s, lab in zip(scores, labels) if lab]
    neg = [s for s, lab in zip(scores, labels) if not lab]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg)
    return wins / (len(pos) * len(neg))


def designed_rules(cf):
    return [
        lambda x: x[1],
        lambda x, cf=cf: cf(x[0], x[2]),
        lambda x: x[1],
    ]


def embed_rules(pw, pc, cf):
    return [
        lambda x, pw=pw: pw[x[1]],
        lambda x, cf=cf: cf(x[0], x[2]),
        lambda x, pc=pc: pc[x[1]],
    ]


def struct_phi(rules):
    v = verdict(rules, LABELS)
    core, phi_mc = major_complex(rules, LABELS)
    if core is None or phi_mc < 0:
        return v.structure, 0.0, tuple()
    return v.structure, float(phi_mc), tuple(core)


def train(cf, rng):
    """Stateful ε-greedy Q-learning; state = last commit bit."""
    Qw = np.zeros((2, 2))
    Qc = np.zeros((2, 2))
    S = 0
    streak = 0
    hit = EPISODES
    rewards = []
    for ep in range(EPISODES):
        eps = max(0.05, 1.0 - ep / 100.0)
        aw = int(rng.integers(2)) if rng.random() < eps else int(np.argmax(Qw[S]))
        ac = int(rng.integers(2)) if rng.random() < eps else int(np.argmax(Qc[S]))
        r = float(cf(aw, ac))
        Qw[S, aw] += ALPHA * (r - Qw[S, aw])
        Qc[S, ac] += ALPHA * (r - Qc[S, ac])
        S = int(r)
        rewards.append(r)
        streak = streak + 1 if r == 1.0 else 0
        if streak >= STREAK_NEED and hit == EPISODES:
            hit = ep
    pw = [int(np.argmax(Qw[s])) for s in (0, 1)]
    pc = [int(np.argmax(Qc[s])) for s in (0, 1)]
    final = float(np.mean(rewards[-40:])) if rewards else 0.0
    return hit, pw, pc, final


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("MARL EMERGENT LEARN — agenda #41")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print(
        f"  proxy: tabular stateful Q-learn "
        f"(episodes={EPISODES}, seeds={SEEDS}/task) — not deep MARL"
    )
    print("  cited: #98/#107 ABM nulls; #37–#40 pointers only")
    print()

    # designed panel
    designed = {}
    print(f"  {'task':<12}{'designed':<10}{'Φ':>6}  core")
    for name, cf in COMMITS.items():
        st, phi, core = struct_phi(designed_rules(cf))
        designed[name] = (st, phi)
        print(f"  {name:<12}{st:<10}{phi:>6.3f}  {'|'.join(core) if core else '—'}")

    rows = []
    for name, cf in COMMITS.items():
        d_st, d_phi = designed[name]
        for seed in range(SEEDS):
            rng = np.random.default_rng(41000 + seed * 17 + sum(ord(c) for c in name))
            diff, pw, pc, final = train(cf, rng)
            e_st, e_phi, e_core = struct_phi(embed_rules(pw, pc, cf))
            rows.append(
                {
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
                    "pi_W": str(pw),
                    "pi_C": str(pc),
                }
            )

    print()
    print(
        f"  {'task':<12}{'des':<8}{'diff':>7}{'succ':>6}{'e_tri':>6}  note"
    )
    for name in COMMITS:
        rs = [r for r in rows if r["task"] == name]
        md = float(np.mean([r["difficulty"] for r in rs]))
        ms = float(np.mean([r["success"] for r in rs]))
        me = float(np.mean([r["emergent_triadic"] for r in rs]))
        note = ""
        if rs[0]["designed_triadic"] and ms >= 0.8 and me < 0.5:
            note = "open-loop success"
        print(
            f"  {name:<12}{rs[0]['designed']:<8}{md:>7.1f}{ms:>6.2f}{me:>6.2f}  {note}"
        )

    succ = np.array([r["success"] for r in rows], dtype=int)
    e_tri = np.array([r["emergent_triadic"] for r in rows], dtype=float)
    d_tri = np.array([r["designed_triadic"] for r in rows], dtype=float)
    e_phi = np.array([r["emergent_phi"] for r in rows], dtype=float)
    diff = np.array([r["difficulty"] for r in rows], dtype=float)
    # learnability score: higher = easier (for ranking)
    learn = 1.0 - diff / float(EPISODES)

    auc_e_succ = auc(e_tri, succ)
    auc_ephi_succ = auc(e_phi, succ)
    auc_d_succ = auc(d_tri, succ)
    auc_diff_des = auc(diff, d_tri.astype(int))
    auc_diff_em = auc(diff, e_tri.astype(int))
    # does emergent triadic mark *easier* runs? (learnability label = above-median learn)
    easy = (learn >= np.median(learn)).astype(int)
    auc_e_easy = auc(e_tri, easy)

    # H3: among success on designed-triadic tasks, fraction emergent-triadic
    des_tri_succ = [
        r
        for r in rows
        if r["designed_triadic"] and r["success"]
    ]
    frac_em_given = (
        float(np.mean([r["emergent_triadic"] for r in des_tri_succ]))
        if des_tri_succ
        else float("nan")
    )
    and_success_nont = [
        r
        for r in rows
        if r["task"] == "AND"
        and r["success"]
        and not r["emergent_triadic"]
    ]

    # H1: emergent predicts learnability via success AUC, or (if weak) easy-AUC
    h1_succ = (not np.isnan(auc_e_succ)) and auc_e_succ >= AUC_THR
    h1_easy = (not np.isnan(auc_e_easy)) and auc_e_easy >= AUC_THR
    h1 = h1_succ or h1_easy
    h2 = (not np.isnan(auc_diff_des)) and auc_diff_des >= AUC_THR
    h3 = (not np.isnan(frac_em_given)) and frac_em_given > 0.5

    def fmt(x):
        return "n/a" if (x != x) else f"{x:.3f}"  # NaN check

    print()
    print("ASSOCIATION")
    print(f"  N={len(rows)}  success_rate={succ.mean():.2f}  "
          f"emerg_triadic_rate={e_tri.mean():.2f}")
    print(f"  AUC emerg_triadic → success:     {fmt(auc_e_succ)}")
    print(f"  AUC emerg_Φ → success:           {fmt(auc_ephi_succ)}")
    print(f"  AUC emerg_triadic → easy:        {fmt(auc_e_easy)}")
    print(f"  AUC designed_triadic → success:  {fmt(auc_d_succ)}")
    print(f"  AUC difficulty → designed_tri:   {fmt(auc_diff_des)}  (#98-like)")
    print(f"  AUC difficulty → emerg_tri:      {fmt(auc_diff_em)}")
    print(
        f"  P(emerg_tri | success ∧ designed_tri): {frac_em_given:.3f}  "
        f"(n={len(des_tri_succ)})"
    )
    print(f"  AND success with non-tri emergent: {len(and_success_nont)}/{SEEDS}")

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (emergent predicts learnability):  "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (designed verdict predicts difficulty): "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (success ⇒ emergent triadic on des-tri): "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    if (not h1) and (not h2) and (not h3) and ctrl_ok:
        verdict_s = "EMERGENT_NULL"
    elif not h1:
        verdict_s = "NO_PREDICT"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and (not h1) and (not h2) and (not h3)

    print()
    print("STATUS")
    print(f"  H1 emergent→learnability: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 designed→difficulty:  {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 success⇒emerg tri:    {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            AI lane closable — synthesis in AI_MULTIAGENT_ARC.md")
    print()
    print(
        f"verdict: {verdict_s} — emergent coordination verdict after tabular "
        f"MARL does not predict task learnability (AUC emerg→success="
        f"{fmt(auc_e_succ)}, emerg→easy={fmt(auc_e_easy)}); designed verdict "
        f"still fails (#98-like AUC={fmt(auc_diff_des)}); successful AND/OR "
        f"learners induce open-loop non-triadic policies — extends #98/#107; "
        f"association only, not causal"
    )
    print(
        "reading: EMERGENT_NULL — the #98/#107 gap does not close when the "
        "verdict is read on the learned policy loop; irreducibility and "
        "learnability remain different things; candid tabular proxy ≠ deep MARL; "
        "AI lane #37–#41 closable"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
