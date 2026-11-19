"""Exhaustive search over all 4096 three-node affine-GF(2) forms in the q220 family (flip 0.08):
group forms by their exact population cross match profiles (all ordered pairs, lags -20..20), then by
cross + auto profiles, and compute the lab's exact-Φ bottleneck targets inside every group with > 1 member
(stage 2, `--phi`). Output: results/affine_groups.json (stage 1), results/affine_phi.json (stage 2).
"""
import json
import os
import sys
from collections import defaultdict

import numpy as np

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability import exact_profiles as ep

OUT = os.path.join(os.path.dirname(__file__), "results")
L = ("X", "Y", "H")


def key(arr):
    return tuple(np.round(np.asarray(arr), 9).tolist())


def stage1():
    groups_cross, groups_full = defaultdict(list), defaultdict(list)
    for combo, rules in ep.affine_systems():
        prof = ep.all_profiles(rules)
        cross = np.concatenate([prof[(i, j)] for i in range(3) for j in range(3) if i < j])
        auto = np.concatenate([prof[(i, i)] for i in range(3)])
        groups_cross[key(cross)].append(combo)
        groups_full[key(np.concatenate([cross, auto]))].append(combo)
    gc = [g for g in groups_cross.values() if len(g) > 1]
    gf = [g for g in groups_full.values() if len(g) > 1]
    flat = [g for k, g in groups_cross.items() if max(abs(v - 0.5) for v in k) < 1e-9]
    res = {"n_systems": 4096, "n_cross_classes": len(groups_cross), "n_cross_classes_multi": len(gc),
           "n_full_classes": len(groups_full), "n_full_classes_multi": len(gf),
           "flat_cross_class_size": len(flat[0]) if flat else 0,
           "cross_groups": [[list(map(list, c)) for c in g] for g in gc],
           "full_groups": [[list(map(list, c)) for c in g] for g in gf]}
    json.dump(res, open(os.path.join(OUT, "affine_groups.json"), "w"))
    print({k: v for k, v in res.items() if not k.endswith("groups")})


def rules_of(combo):
    return [ep.affine_rule(m, c) for (m, c) in combo]


def stage2(limit=None):
    from org_frontier.questions.q161_noise_robust_verdict.probe_noise_robust_verdict import bottleneck_set, core_indices
    g = json.load(open(os.path.join(OUT, "affine_groups.json")))
    cache = {}
    need = {tuple(map(tuple, c)) for grp in g["cross_groups"] for c in grp}
    need = sorted(need)[:limit] if limit else sorted(need)
    print("computing exact-Φ targets for", len(need), "systems", flush=True)
    for i, combo in enumerate(need):
        rules = rules_of(combo)
        ci, phi = core_indices(rules, L)
        bset, base, drops = bottleneck_set(rules, L)
        cache[str(combo)] = {"core": list(ci) if ci else None, "phi": phi, "B": sorted(bset), "base": base,
                             "drops": [float(d) for d in drops]}
        if i % 100 == 0:
            print(i, combo, cache[str(combo)], flush=True)
            json.dump(cache, open(os.path.join(OUT, "affine_phi.json"), "w"))
    json.dump(cache, open(os.path.join(OUT, "affine_phi.json"), "w"))


if __name__ == "__main__":
    if "--phi" in sys.argv:
        stage2()
    else:
        stage1()
