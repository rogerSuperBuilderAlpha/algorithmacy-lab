"""Two-triad shared-member merger census (agenda #16; extends q210–q212).

Varies which role is shared (worker / mediator / counterpart) × bridge
(none / AND / OR). Exact IIT-4.0 Φ. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/two_triad_shared_member/analyze_shared_member.py
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

BRIDGES = ("none", "AND", "OR")


def bridge_fn(name, a_idx, b_idx):
    """Shared-node update from two side signals at indices a_idx, b_idx."""
    if name == "none":
        return lambda x, a=a_idx: x[a]
    if name == "AND":
        return lambda x, a=a_idx, b=b_idx: x[a] & x[b]
    if name == "OR":
        return lambda x, a=a_idx, b=b_idx: x[a] | x[b]
    raise KeyError(name)


def form_shared_counterpart(bridge):
    # (W1, S1, W2, S2, C) — q210
    labels = ("W1", "S1", "W2", "S2", "C")
    exclusive = (("W1", "S1"), ("W2", "S2"))
    rules = [
        lambda x: x[1],                          # W1' = S1
        lambda x: x[0] & x[4],                   # S1' = W1 ∧ C
        lambda x: x[3],                          # W2' = S2
        lambda x: x[2] & x[4],                   # S2' = W2 ∧ C
        bridge_fn(bridge, 1, 3),                 # C'  = bridge(S1, S2)
    ]
    return labels, rules, exclusive


def form_shared_mediator(bridge):
    # (W1, C1, W2, C2, S)
    labels = ("W1", "C1", "W2", "C2", "S")
    exclusive = (("W1", "C1"), ("W2", "C2"))
    own1 = lambda x: x[0] & x[1]                 # W1 ∧ C1
    own2 = lambda x: x[2] & x[3]                 # W2 ∧ C2
    if bridge == "none":
        s_rule = lambda x: own1(x)
    elif bridge == "AND":
        s_rule = lambda x: own1(x) & own2(x)
    else:  # OR
        s_rule = lambda x: own1(x) | own2(x)
    rules = [
        lambda x: x[4],                          # W1' = S
        lambda x: x[4],                          # C1' = S
        lambda x: x[4],                          # W2' = S
        lambda x: x[4],                          # C2' = S
        s_rule,                                  # S'  = bridge(own1, own2)
    ]
    return labels, rules, exclusive


def form_shared_worker(bridge):
    # (S1, C1, S2, C2, W)
    labels = ("S1", "C1", "S2", "C2", "W")
    exclusive = (("S1", "C1"), ("S2", "C2"))
    rules = [
        lambda x: x[4] & x[1],                   # S1' = W ∧ C1
        lambda x: x[0],                          # C1' = S1
        lambda x: x[4] & x[3],                   # S2' = W ∧ C2
        lambda x: x[2],                          # C2' = S2
        bridge_fn(bridge, 0, 2),                 # W'  = bridge(S1, S2)
    ]
    return labels, rules, exclusive


ARCHITECTURES = {
    "shared_counterpart": form_shared_counterpart,
    "shared_mediator": form_shared_mediator,
    "shared_worker": form_shared_worker,
}


def spans_both(core, exclusive):
    c = set(core)
    left, right = exclusive
    return bool(c & set(left)) and bool(c & set(right))


def run_cell(arch_name, bridge):
    labels, rules, exclusive = ARCHITECTURES[arch_name](bridge)
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core is not None else ()
    span = spans_both(core_t, exclusive) if core_t else False
    return {
        "architecture": arch_name,
        "bridge": bridge,
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": core_t,
        "core_phi": float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan"),
        "spans_both": span,
        "n_core": len(core_t),
    }


def fmt_core(core):
    return "(" + ",".join(core) + ")" if core else "()"


def main():
    print("TWO-TRIAD SHARED-MEMBER MERGER — agenda #16 (extends q210–q212)")
    print("=" * 80)
    print("  cited: q210 shared-C never merges; q211 direct S↔S merges;")
    print("         q212 only mediator placement merges; residual/cascade closed")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  H1a single triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")

    rows = []
    for arch in ("shared_counterpart", "shared_mediator", "shared_worker"):
        print()
        print(f"ARCHITECTURE {arch}")
        print("-" * 80)
        for bridge in BRIDGES:
            r = run_cell(arch, bridge)
            rows.append(r)
            print(
                f"  bridge={bridge:<4}  {r['structure']:<8} "
                f"wholeΦ_MIP={r['whole_phi_mip']:.4f}  "
                f"core={fmt_core(r['core']):<20} coreΦ={r['core_phi']:.3f}  "
                f"spans_both={r['spans_both']}"
            )

    # index
    def cell(arch, bridge):
        return next(r for r in rows
                    if r["architecture"] == arch and r["bridge"] == bridge)

    sc_none = cell("shared_counterpart", "none")
    sc_and = cell("shared_counterpart", "AND")
    sm_and = cell("shared_mediator", "AND")
    sw_and = cell("shared_worker", "AND")

    h1b = (
        sc_none["structure"] == "dyadic"
        and abs(sc_none["whole_phi_mip"]) < PHI_EPS
        and abs(sc_none["core_phi"] - 2.0) < 1e-3
        and not sc_none["spans_both"]
    )
    print()
    print("H1b shared-C/none q210 replicate: "
          f"whole={sc_none['structure']} Φ_MIP={sc_none['whole_phi_mip']:.4f} "
          f"coreΦ={sc_none['core_phi']:.3f} spans={sc_none['spans_both']}  "
          f"{'PASS' if h1b else 'FAIL'}")
    h1 = ctrl and h1b

    h2 = not sc_and["spans_both"]
    h3 = sm_and["spans_both"]
    h4 = sm_and["core_phi"] > 2.0 + PHI_EPS
    h5 = not sw_and["spans_both"]
    and_cells = [cell(a, "AND") for a in ARCHITECTURES]
    any_merge = any(c["spans_both"] for c in and_cells)
    any_leaf_no = (not sc_and["spans_both"]) or (not sw_and["spans_both"])
    h6 = any_merge and any_leaf_no

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  shared-C/AND   spans={sc_and['spans_both']}  core={fmt_core(sc_and['core'])}  "
          f"coreΦ={sc_and['core_phi']:.3f}")
    print(f"  shared-S/AND   spans={sm_and['spans_both']}  core={fmt_core(sm_and['core'])}  "
          f"coreΦ={sm_and['core_phi']:.3f}")
    print(f"  shared-W/AND   spans={sw_and['spans_both']}  core={fmt_core(sw_and['core'])}  "
          f"coreΦ={sw_and['core_phi']:.3f}")
    print(f"  H1 (control + q210 none replicate): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (shared-C/AND does not merge):   {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (shared-S/AND merges):           {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (shared-S/AND core Φ > 2.0):     {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (shared-W/AND does not merge):   {'SUPPORTED' if h5 else 'REFUTED'}")
    print(f"  H6 (role decides merger under AND): {'SUPPORTED' if h6 else 'REFUTED'}")

    if h3 and h6 and h2:
        reading = "WIN — shared mediator merges; shared leaves do not"
    elif h6:
        reading = "PARTIAL — role matters, but mediator/leaf pattern differs from H3–H5"
    else:
        reading = "NULL — shared role does not sort merger as predicted"

    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  q210 cite: shared counterpart never merges (this census H2)")
    print(f"  q211 cite: direct S↔S merges without shared member")
    print(f"  q212 cite: only mediator channel location merges")
    print(f"  shared-S/AND spans_both={sm_and['spans_both']} coreΦ={sm_and['core_phi']:.3f}")
    print(f"  shared-C/AND spans_both={sc_and['spans_both']} coreΦ={sc_and['core_phi']:.3f}")
    print(f"  shared-W/AND spans_both={sw_and['spans_both']} coreΦ={sw_and['core_phi']:.3f}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}  "
          f"H6={('SUPPORTED' if h6 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = ["architecture", "bridge", "structure", "whole_phi_mip",
                  "core", "core_phi", "spans_both", "n_core"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "architecture": r["architecture"],
                "bridge": r["bridge"],
                "structure": r["structure"],
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core": "|".join(r["core"]),
                "core_phi": f"{r['core_phi']:.6f}",
                "spans_both": str(r["spans_both"]),
                "n_core": r["n_core"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "h6": "SUPPORTED" if h6 else "REFUTED",
            "sm_and_spans": str(sm_and["spans_both"]),
            "sm_and_core_phi": f"{sm_and['core_phi']:.6f}",
            "sc_and_spans": str(sc_and["spans_both"]),
            "sw_and_spans": str(sw_and["spans_both"]),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
