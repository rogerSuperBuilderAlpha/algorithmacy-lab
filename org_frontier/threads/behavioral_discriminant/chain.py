"""The twenty-step deep dive on Q10: can cross-recurrence tell a committing mediator from a conveying one.

Q10 from the mediation_boundary thread's QUESTIONS.md. The structural dives used exact Φ; this one asks
whether the behavioral instrument, cross-recurrence on a run of the form, can recover the commit/convey
distinction without the model. It cannot do it sharply, and the reason is the finding: a large class of
conveying mediators is behaviorally identical to committing ones. Each step's question is drawn from the
previous step's result; the narrative is in DEEP_DIVE.md, and every number reproduces here.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/threads/behavioral_discriminant/chain.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from org_frontier.recurrence.crqa import trajectory, peak, coupling_centrality, crqa, md_recurrence
from org_frontier.classifier.classifier import classify_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states

L = ("W", "S", "C")


def rand_strict(rng):
    """A random strict-mediated triad: W and C read S, S reads W and C with a random 2-input gate."""
    tt = [rng.randint(0, 1) for _ in range(4)]
    return [lambda x: x[1], (lambda x, tt=tt: tt[x[0] + 2 * x[2]]), lambda x: x[1]]


def auc(scores, labels):
    pos = [s for s, l in zip(scores, labels) if l]
    neg = [s for s, l in zip(scores, labels) if not l]
    if not pos or not neg:
        return float("nan")
    return sum((a > b) + 0.5 * (a == b) for a in pos for b in neg) / (len(pos) * len(neg))


def measures(rules, seed, steps=800, flip=0.06):
    tr = trajectory(rules, steps, random.Random(seed), flip=flip)
    lag, prom = peak(tr[:, 0], tr[:, 2], max_lag=8)
    cen = coupling_centrality(tr)
    return {"lag": abs(lag), "prom": prom, "Scen": cen[1],
            "wcdet": crqa(tr[:, 0], tr[:, 2])["det"], "mddet": md_recurrence(tr)["det"]}


def sample(n, seed):
    rng = random.Random(seed)
    rows = []
    for k in range(n):
        r = rand_strict(rng)
        v = classify_rules(r, L)
        net, tpm = network(r, L)
        _, core, _ = complex_over_states(net, tpm, 3)
        m = measures(r, 9000 + k)
        m["tri"] = v.structure == "triadic"
        m["phi"] = v.max_phi
        m["Sin"] = core is not None and 1 in core
        rows.append(m)
    return rows


def run():
    print("STEP 1 — behavioral signature, clear cases (committing co-recur synchronously, conveying relay):")
    clear = {"COMMIT S=W&C": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
             "CONVEY relay": [lambda x: x[0], lambda x: x[0], lambda x: x[1]]}
    for name, r in clear.items():
        m = measures(r, 7, steps=600, flip=0.08)
        print(f"  {name:<14} W-C lag={m['lag']}  prominence={m['prom']:.2f}  S-centrality={m['Scen']:.2f}")

    rows = sample(220, 5)
    tri = [r["tri"] for r in rows]
    print(f"\nSTEP 2-3,9-10 — population AUC for predicting committing (Φ>0), {sum(tri)}/{len(tri)} committing:")
    for key, name in [("prom", "W-C directed-coupling prominence"), ("Scen", "S coupling-centrality"),
                      ("lag", "W-C synchrony (-|lag|)"), ("wcdet", "W-C determinism"),
                      ("mddet", "whole-system md-recurrence")]:
        sign = -1 if key == "lag" else 1
        print(f"  {name:<34} AUC={auc([sign * r[key] for r in rows], tri):.2f}")

    print("\nSTEP 4 — the ceiling is structural, not noise (longer + cleaner trajectories hold AUC):")
    for steps, flip in [(600, 0.08), (1500, 0.04)]:
        rr = [dict(measures(rand_strict(random.Random(s)), 100 + s, steps, flip),
                   tri=None) for s in range(120)]
        rng = random.Random(11)
        rr = []
        for k in range(150):
            r = rand_strict(rng)
            rr.append((classify_rules(r, L).structure == "triadic",
                       measures(r, 5000 + k, steps, flip)["prom"]))
        print(f"  steps={steps} flip={flip}: prominence AUC={auc([p for _, p in rr], [t for t, _ in rr]):.2f}")

    print("\nSTEP 5 — detectability tracks the Φ margin (dive 2): prominence vs Φ among committing forms:")
    t = [r for r in rows if r["tri"]]
    print(f"  corr(Φ, W-C prominence) among committing = {np.corrcoef([r['phi'] for r in t], [r['prom'] for r in t])[0, 1]:+.2f}")

    print("\nSTEP 8,11 — mediator centrality vs the major complex, and the false-positive class:")
    print(f"  AUC of S-centrality for S-in-core = {auc([r['Scen'] for r in rows], [r['Sin'] for r in rows]):.2f}")
    fp = [r for r in rows if not r["tri"] and r["prom"] > 0.15]
    tp = [r for r in rows if r["tri"] and r["prom"] > 0.15]
    print(f"  false-positive conveying forms (n={len(fp)}): mean DET {np.mean([r['wcdet'] for r in fp]):.2f}, prominence {np.mean([r['prom'] for r in fp]):.2f}")
    print(f"  true committing forms      (n={len(tp)}): mean DET {np.mean([r['wcdet'] for r in tp]):.2f}, prominence {np.mean([r['prom'] for r in tp]):.2f}")

    print("\nSTEP 12 — no precision/recall tradeoff (the classes overlap in behavior):")
    for th in (0.15, 0.30):
        flagged = [r for r in rows if r["prom"] > th]
        if flagged:
            prec = sum(r["tri"] for r in flagged) / len(flagged)
            rec = sum(r["tri"] for r in flagged) / sum(tri)
            print(f"  threshold {th}: precision={prec:.2f} recall={rec:.2f}")


if __name__ == "__main__":
    run()
