"""Probe Q82 (H1-H4) — the learned surrogate vs the single proxies that failed in Q72.

On the 256-form n=3 outreach family, computes four single proxies (mediator in-degree, total edges,
ΦID Φ_R, whole-minus-sum Φ_WMS), the learned surrogate of Q81, and compares their separation of the
exact verdict. Includes the modal-in-degree subset, where the structural proxy is constant — the regime
of the Q72 read_recipient/one_shot collision.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q82_surrogate_vs_proxy.probe_surrogate_vs_proxy
"""

import csv
import os

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score

from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.proxy_bridge.bridge import proxy_for_form
from org_frontier.questions.q81_learned_surrogate import forms as F

SEED = 0


def best_threshold_accuracy(values, y):
    """Accuracy of the best single cut on `values` (higher predicts triadic)."""
    vals = sorted(set(values))
    best = 0.0
    for thr in vals:
        pred = (np.asarray(values) >= thr).astype(int)
        best = max(best, accuracy_score(y, pred))
        best = max(best, accuracy_score(y, 1 - pred))   # allow the reversed cut
    return best


def main():
    print("PROBE Q82 (H1-H4) — learned surrogate vs single cheap proxies (n=3 outreach family)")
    print("=" * 82)
    rng = np.random.default_rng(SEED)
    X, y, indeg, edges, phi_r, phi_wms = [], [], [], [], [], []
    for _key, rules, labels in F.n3_family():
        y.append(F.exact_label(rules, labels))
        X.append(F.intensive_features(F.trajectory(rules, rng)))
        cm = cm_from_rules(rules)
        indeg.append(int(cm[:, 1].sum()))               # inputs to the mediator (node 1)
        edges.append(int(cm.sum()))
        _s, _pd, _pn, pr, pw = proxy_for_form(rules, 0.08, rng, traj_len=4000)
        phi_r.append(pr)
        phi_wms.append(pw)
    X = np.array(X)
    y = np.array(y)

    proxies = {
        "mediator_in_degree": indeg,
        "total_edges": edges,
        "phi_r": phi_r,
        "phi_wms": phi_wms,
    }
    print(f"  {len(y)} forms ({int(y.sum())} triadic, {len(y) - int(y.sum())} dyadic)")
    proxy_aucs = {}
    proxy_accs = {}
    for name, v in proxies.items():
        auc = roc_auc_score(y, v)
        auc = max(auc, 1 - auc)                          # proxy may predict either direction
        acc = best_threshold_accuracy(v, y)
        proxy_aucs[name] = auc
        proxy_accs[name] = acc
        print(f"    {name:<20} rank-AUC={auc:.3f}  best-threshold acc={acc:.3f}")

    # Learned surrogate: 5-fold CV.
    clf = RandomForestClassifier(n_estimators=400, random_state=0, n_jobs=-1)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    proba = cross_val_predict(clf, X, y, cv=cv, method="predict_proba")[:, 1]
    pred = (proba >= 0.5).astype(int)
    surr_auc = roc_auc_score(y, proba)
    surr_acc = accuracy_score(y, pred)
    print(f"    {'learned_surrogate':<20} CV ROC-AUC={surr_auc:.3f}  CV acc={surr_acc:.3f}")

    # Modal-in-degree subset: where the structural proxy is constant.
    modal = max(set(indeg), key=indeg.count)
    mask = np.array(indeg) == modal
    sub_acc = accuracy_score(y[mask], pred[mask])
    sub_tri = int(y[mask].sum())
    print(f"  modal mediator in-degree = {modal}: {int(mask.sum())} forms "
          f"({sub_tri} triadic, {int(mask.sum()) - sub_tri} dyadic), surrogate OOF acc={sub_acc:.3f}")

    best_proxy_auc = max(proxy_aucs.values())
    best_proxy_acc = max(proxy_accs.values())
    h1 = all(a < 0.85 for a in proxy_aucs.values())
    h2 = surr_auc >= 0.95 and surr_auc > best_proxy_auc
    h3 = surr_acc > best_proxy_acc
    h4 = sub_acc >= 0.90
    print("=" * 82)
    print(f"  H1 every single proxy rank-AUC < 0.85:                 {h1} (max {best_proxy_auc:.3f})")
    print(f"  H2 surrogate AUC >= 0.95 and beats every proxy:        {h2} ({surr_auc:.3f})")
    print(f"  H3 surrogate acc > best single-proxy threshold acc:    {h3} ({surr_acc:.3f} vs {best_proxy_acc:.3f})")
    print(f"  H4 surrogate OOF acc on modal-in-degree subset >= 0.90: {h4} ({sub_acc:.3f})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "surrogate_vs_proxy.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["proxy", "rank_auc", "best_threshold_acc"])
        for name in proxies:
            w.writerow([name, f"{proxy_aucs[name]:.4f}", f"{proxy_accs[name]:.4f}"])
        w.writerow(["learned_surrogate_cv", f"{surr_auc:.4f}", f"{surr_acc:.4f}"])
        w.writerow([f"surrogate_oof_indeg{modal}_subset", "", f"{sub_acc:.4f}"])


if __name__ == "__main__":
    main()
