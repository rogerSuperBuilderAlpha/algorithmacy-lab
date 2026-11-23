"""Post-hoc check (not pre-registered): maximal complex at every whole-Phi state, k = 4 median, r = 0.05, 0.1, 0.2.

Run from the repo root: python org_frontier/studies/alphabet_ladder_hub/allpeaks.py [--write]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
for p in (ROOT / "third_party", ROOT):
    sys.path.insert(0, str(p))

from org_frontier.studies.ternary_majority_noise.run import LABELS, RULES, build  # noqa: E402
from pyphi_iit4_mv import maximal_complex  # noqa: E402

res = json.loads((Path(__file__).with_name("results") / "results.json").read_text())
out = {}
for r in (0.05, 0.1, 0.2):
    row = next(x for x in res["rows"] if x["rule"] == "median" and x["r"] == r)
    net, _ = build(RULES["median"], 4, r)
    out[str(r)] = {}
    for s in row["peak_states"]:
        mc = maximal_complex(net, tuple(int(c) for c in s))
        core = [LABELS[i] for i in mc.node_indices]
        out[str(r)][s] = dict(core=core, phi=float(mc.phi), ratio=float(mc.phi) / row["whole_phi"])
        print(f"r={r} state {s} core={{{','.join(core)}}} core_phi={mc.phi:.6f} ratio={out[str(r)][s]['ratio']:.6f}",
              flush=True)
    best = max(out[str(r)].values(), key=lambda c: c["phi"])
    print(f"r={r} best core ratio={best['ratio']:.6f}", flush=True)
if "--write" in sys.argv:
    (Path(__file__).with_name("results") / "allpeaks_median_k4.json").write_text(json.dumps(out, indent=1) + "\n")
