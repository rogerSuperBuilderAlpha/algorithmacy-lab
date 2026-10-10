"""Probe 457 — weighted and noisy quorums: does the extremes-only quorum law survive?

Question: a k-of-n threshold mediator binds the full party set only at k = 1 and k = all (probe 117;
coordination-logic atlas, study D). Does that law hold across every weighted threshold rule at three and
four parties, and when the mediator's commit is noisy?

Hypotheses (fixed in hypotheses.md, commit a3716ad8, before this script existed):
  H1  extreme classes (AND or OR of the relevant set R, |R| >= 2) have major complex {S} + R;
      H1b the core's phi equals |R|.
  H2  no irrelevant party is in a major complex; H2b every class with an irrelevant party reads dyadic.
  H3  no mixed class has two or more parties in its major complex.
  H4  in mixed classes with exactly one party in the core, that party has the unique largest swing count.
  H5  under commit noise eps < 0.5, extreme classes keep core {S} + R and the core's phi is non-increasing.
  H6  no mixed class gains a core with two or more parties at any eps.

Method: node 0 = S, nodes 1..n = parties; every party copies S (the threshold_hub wiring of probe 117);
S commits f(x) = 1 iff sum(w_i x_i) >= theta. Weights 0..5 and quotas 1..sum(w) are enumerated, constant
functions dropped, truth tables reduced to one class per party permutation; the run is repeated with
weights 0..6 as a saturation check. Each class is read with org_frontier.probes.lib.verdict (whole
system) and lib.major_complex (core). The noise arm flips the commit with probability eps, builds a
stochastic state-by-node TPM, and reads it with classifier.classify and a TPM-input copy of
lib.major_complex. Control gate C1a/C1b/C2/C3 as pre-registered.

Run (from the repo root, Python 3.10+ venv):
  python -m org_frontier.probes.weighted_quorum.probe_weighted_quorum          # full run
  python -m org_frontier.probes.weighted_quorum.probe_weighted_quorum --ci     # deterministic arm only

--ci skips the noise arm (C2, C3, H5, H6) and the CSV writes; every line it prints is identical to the
corresponding line of the full run.

Scope: exact IIT 4.0 Phi on Boolean models of four and five nodes; evidence about the models only.
"""

import argparse
import csv
import itertools
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import exceptions, new_big_phi

from org_frontier.classifier.classifier import PHI_EPS, classify
from org_frontier.classifier.validate import factoring_control, irreducible_control
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_threshold_scaling import threshold_hub
from foundations.proxy_audit.exact_phi import reachable_states

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
EPS_GRID = (0.0, 0.05, 0.10, 0.20, 0.30, 0.40, 0.45, 0.50)
W_MAX, W_MAX_SAT = 5, 6
TOL_PHI_R = 1e-6   # H1b tolerance
TOL_MONO = 1e-9    # H5 / C2 tolerance

# Rules stated in open PR #808 (probe_voting_stress.py), mapped to party weights (W, C1, C2) and quota,
# with the reading that PR states for them: (structure, Phi, parties in core).
PR808 = [
    ("unanimity (AND)", (1, 1, 1), 3, ("triadic", 3.0, ("W", "C1", "C2"))),
    ("any (OR)", (1, 1, 1), 1, ("triadic", 3.0, ("W", "C1", "C2"))),
    ("majority (2of3)", (1, 1, 1), 2, ("dyadic", 0.0, ())),
    ("weighted 2-1-1, t=2", (2, 1, 1), 2, ("dyadic", 0.0, ("W",))),
    ("weighted 2-1-1, t=3", (2, 1, 1), 3, ("dyadic", 0.0, ("W",))),
    ("weighted 3-1-1, t=3", (3, 1, 1), 3, ("dyadic", 0.0, ("W",))),
    ("weighted 3-1-1, t=4", (3, 1, 1), 4, ("dyadic", 0.0, ("W",))),
    ("2-of-3 excluding W", (0, 1, 1), 2, ("dyadic", 0.0, ("C1", "C2"))),
]


# ------------------------------------------------------------------------------------------------
# Boolean functions
# ------------------------------------------------------------------------------------------------

def table_of(weights, theta):
    n = len(weights)
    return tuple(int(sum(w * ((x >> i) & 1) for i, w in enumerate(weights)) >= theta)
                 for x in range(2 ** n))


def permute_table(table, perm, n):
    """g(x) = f(y) where party perm[i] of y takes the value of party i of x."""
    out = []
    for x in range(2 ** n):
        y = 0
        for i in range(n):
            if (x >> i) & 1:
                y |= 1 << perm[i]
        out.append(table[y])
    return tuple(out)


def enumerate_classes(n, w_max):
    """Map canonical truth table -> representative (weights, theta) that produces it exactly."""
    perms = list(itertools.permutations(range(n)))
    classes = {}
    for weights in itertools.product(range(w_max + 1), repeat=n):
        total = sum(weights)
        for theta in range(1, total + 1):
            t = table_of(weights, theta)
            if len(set(t)) == 1:
                continue  # constant function
            best = None
            for p in perms:
                pt = permute_table(t, p, n)
                if best is None or pt < best[0]:
                    pw = [0] * n
                    for i in range(n):
                        pw[i] = weights[p[i]]
                    best = (pt, tuple(pw))
            canon, pw = best
            assert table_of(pw, theta) == canon
            key = (sum(pw), pw, theta)
            if canon not in classes or key < classes[canon][0]:
                classes[canon] = (key, pw, theta)
    return {c: (v[1], v[2]) for c, v in classes.items()}


def swing_counts(table, n):
    beta = []
    for i in range(n):
        b = 0
        for x in range(2 ** n):
            if not (x >> i) & 1 and table[x] != table[x | (1 << i)]:
                b += 1
        beta.append(b)
    return tuple(beta)


def class_type(table, n, rel):
    if len(rel) == 1:
        return "dictator"
    and_t = tuple(int(all((x >> i) & 1 for i in rel)) for x in range(2 ** n))
    or_t = tuple(int(any((x >> i) & 1 for i in rel)) for x in range(2 ** n))
    if table == and_t:
        return "AND"
    if table == or_t:
        return "OR"
    return "mixed"


# ------------------------------------------------------------------------------------------------
# Forms and readings
# ------------------------------------------------------------------------------------------------

def labels_for(n):
    return ("S",) + tuple(f"P{i + 1}" for i in range(n))


def rules_for(table, n):
    """Node 0 = S commits the table over parties 1..n; every party copies S."""
    def s_rule(x, table=table, n=n):
        idx = sum(x[i + 1] << i for i in range(n))
        return table[idx]
    return [s_rule] + [(lambda x: x[0]) for _ in range(n)]


def noisy_tpm(table, n, eps):
    nn = n + 1
    tpm = np.zeros((2 ** nn, nn))
    for s in range(2 ** nn):
        idx = sum(((s >> (i + 1)) & 1) << i for i in range(n))
        f = table[idx]
        tpm[s, 0] = (1 - eps) * f + eps * (1 - f)
        for j in range(1, nn):
            tpm[s, j] = float(s & 1)
    return tpm


def cm_numeric(tpm):
    nn = tpm.shape[1]
    cm = np.zeros((nn, nn), dtype=int)
    for j in range(nn):
        for i in range(nn):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** nn)):
                cm[i, j] = 1
    return cm


def tpm_major_complex(tpm, cm, labels):
    """Copy of lib.major_complex that takes a (possibly stochastic) state-by-node TPM."""
    nn = tpm.shape[1]
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0)
    for s in reachable_states(tpm, nn):
        state = tuple((s >> i) & 1 for i in range(nn))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except (exceptions.StateUnreachableError, ValueError):
            continue
        if isinstance(mc, new_big_phi.NullPhiStructure):
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(labels[i] for i in mc.node_indices), float(mc.phi))
    return best


def parties_in(core):
    return tuple(c for c in (core or ()) if c != "S")


def fmt_core(core):
    return "{" + ",".join(core) + "}" if core else "none"


def fmt_phi(core, phi, prec=6):
    """lib.major_complex returns phi = -1.0 as a sentinel when no complex exists; print it as '-'."""
    return f"{phi:.{prec}f}" if core else "-"


# ------------------------------------------------------------------------------------------------
# Control gate
# ------------------------------------------------------------------------------------------------

def gate_c1():
    print("Control gate")
    ok = True
    for name, rules, expect in [("C1a factoring control (C decoupled)", factoring_control(), "dyadic"),
                                ("C1a irreducible control (full coupling)", irreducible_control(), "triadic")]:
        v = verdict(rules, ("W", "S", "C"))
        good = v.structure == expect
        ok &= good
        print(f"  {name}: {v.structure} Φ={v.max_phi:.6f}  {'PASS' if good else 'FAIL'}")
    labels = ("S", "P1", "P2", "P3")
    for name, k, expect in [("AND (3-of-3)", 3, "triadic"), ("OR (1-of-3)", 1, "triadic"),
                            ("2-of-3", 2, "dyadic")]:
        rules = threshold_hub(4, k)
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        if expect == "triadic":
            good = (v.structure == "triadic" and abs(v.max_phi - 3.0) < 1e-6
                    and core is not None and set(core) == set(labels))
        else:
            good = v.structure == "dyadic" and core is None
        ok &= good
        print(f"  C1b {name}: {v.structure} Φ={v.max_phi:.6f} core={fmt_core(core)}  "
              f"{'PASS' if good else 'FAIL'}")
    return ok


# ------------------------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------------------------

def status(ok, testable=True):
    if not testable:
        return "NOT_TESTABLE"
    return "SUPPORTED" if ok else "REFUTED"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ci", action="store_true", help="deterministic arm only (no noise arm, no CSV)")
    args = ap.parse_args(argv)

    print("PROBE 457 — weighted and noisy quorums")
    print("=" * 96)
    if not gate_c1():
        print("Control gate C1 failed: no verdict.")
        return 1
    print("  C1 passed.")

    # ---- enumeration with saturation check
    print("\nEnumeration")
    rows = []
    complete_ns = []
    for n in (3, 4):
        base = enumerate_classes(n, W_MAX)
        sat = enumerate_classes(n, W_MAX_SAT)
        new = set(sat) - set(base)
        complete = not new
        print(f"  n={n}: {len(base)} classes with weights 0..{W_MAX}; {len(sat)} with weights "
              f"0..{W_MAX_SAT}; {'saturated' if complete else 'SCOPE_INCOMPLETE'}")
        if complete:
            complete_ns.append(n)
        for cid, (table, (w, theta)) in enumerate(sorted(base.items(), key=lambda kv: (kv[1][0], kv[1][1]))):
            beta = swing_counts(table, n)
            rel = tuple(i for i in range(n) if beta[i] > 0)
            rows.append(dict(n=n, cid=f"n{n}-{cid + 1:02d}", table=table, w=w, theta=theta, beta=beta,
                             rel=rel, ctype=class_type(table, n, rel)))

    # ---- deterministic readings
    for r in rows:
        n = r["n"]
        labels = labels_for(n)
        rules = rules_for(r["table"], n)
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        r.update(structure=v.structure, Phi=v.max_phi, core=core, phi=phi,
                 rel_labels=tuple(labels[i + 1] for i in r["rel"]))

    print("\nPer-class table (deterministic commit)")
    hdr = (f"  {'class':<7}{'weights':<14}{'θ':<4}{'type':<9}{'R':<14}{'β':<14}{'whole':<9}"
           f"{'Φ':<10}{'core':<18}{'φ_core'}")
    print(hdr)
    for r in rows:
        print(f"  {r['cid']:<7}{str(r['w']):<14}{r['theta']:<4}{r['ctype']:<9}"
              f"{fmt_core(r['rel_labels']):<14}{str(r['beta']):<14}{r['structure']:<9}"
              f"{r['Phi']:<10.6f}{fmt_core(r['core']):<18}{fmt_phi(r['core'], r['phi'])}")

    scored = [r for r in rows if r["n"] in complete_ns]
    testable = bool(scored)

    # ---- H1 / H1b
    ext = [r for r in scored if r["ctype"] in ("AND", "OR") and len(r["rel"]) >= 2]
    h1_bad = [r for r in ext if r["core"] is None or set(r["core"]) != {"S", *r["rel_labels"]}]
    h1b_bad = [r for r in ext if abs(r["phi"] - len(r["rel"])) > TOL_PHI_R]
    # ---- H2 / H2b
    h2_bad = [r for r in scored if set(parties_in(r["core"])) - set(r["rel_labels"])]
    with_irrel = [r for r in scored if len(r["rel"]) < r["n"]]
    h2b_bad = [r for r in with_irrel if r["structure"] != "dyadic"]
    # ---- H3 / H4
    mixed = [r for r in scored if r["ctype"] == "mixed"]
    h3_bad = [r for r in mixed if len(parties_in(r["core"])) >= 2]
    one = [r for r in mixed if len(parties_in(r["core"])) == 1]
    tied, scorable, h4_bad = [], [], []
    for r in one:
        mx = max(r["beta"])
        if sum(1 for b in r["beta"] if b == mx) > 1:
            tied.append(r)
            continue
        scorable.append(r)
        top = labels_for(r["n"])[1 + r["beta"].index(mx)]
        if parties_in(r["core"])[0] != top:
            h4_bad.append(r)

    print("\nHypotheses (deterministic arm)")
    print(f"  scored n: {complete_ns}; classes scored: {len(scored)}; extreme |R|>=2: {len(ext)}; "
          f"mixed: {len(mixed)}; with an irrelevant party: {len(with_irrel)}")
    print(f"  H1 (extreme classes bind {{S}}+R):              {status(not h1_bad, testable and bool(ext))}"
          f"  violations {len(h1_bad)}/{len(ext)}")
    print(f"  H1b (core φ = |R| on extreme classes):         {status(not h1b_bad, testable and bool(ext))}"
          f"  violations {len(h1b_bad)}/{len(ext)}")
    print(f"  H2 (irrelevant parties stay out of the core):  {status(not h2_bad, testable)}"
          f"  violations {len(h2_bad)}/{len(scored)}")
    print(f"  H2b (irrelevant party -> whole-system dyadic): {status(not h2b_bad, testable and bool(with_irrel))}"
          f"  violations {len(h2b_bad)}/{len(with_irrel)}")
    print(f"  H3 (mixed classes bind at most one party):     {status(not h3_bad, testable and bool(mixed))}"
          f"  violations {len(h3_bad)}/{len(mixed)}")
    print(f"  H4 (single core party has the unique max β):   "
          f"{status(not h4_bad, testable and len(scorable) >= 3)}"
          f"  scorable {len(scorable)}, tied {len(tied)}, violations {len(h4_bad)}")
    for tag, bad in (("H1", h1_bad), ("H1b", h1b_bad), ("H2", h2_bad), ("H2b", h2b_bad), ("H3", h3_bad),
                     ("H4", h4_bad)):
        for r in bad:
            print(f"    {tag} violation: {r['cid']} w={r['w']} θ={r['theta']} type={r['ctype']} "
                  f"R={fmt_core(r['rel_labels'])} β={r['beta']} core={fmt_core(r['core'])} "
                  f"φ={r['phi']:.6f} whole={r['structure']} Φ={r['Phi']:.6f}")

    # ---- PR #808 rules inside the enumeration
    print("\nRules stated in open PR #808, located in the enumeration (n=3)")
    by_table = {r["table"]: r for r in rows if r["n"] == 3}
    for name, w, theta, (s_struct, s_phi, s_core) in PR808:
        t = table_of(w, theta)
        canon = min(permute_table(t, p, 3) for p in itertools.permutations(range(3)))
        r = by_table[canon]
        # the probe's own reading of #808's labelling (W, C1, C2) = parties 1..3 of the unpermuted rule
        rules = rules_for(t, 3)
        lab = ("S", "W", "C1", "C2")
        v = verdict(rules, lab)
        core, phi = major_complex(rules, lab)
        mine = (v.structure, round(v.max_phi, 3), parties_in(core))
        stated = (s_struct, round(s_phi, 3), s_core)
        agree = mine == stated
        print(f"  {name:<22} -> {r['cid']} ({r['ctype']})  probe: {v.structure} Φ={v.max_phi:.3f} "
              f"parties in core {list(parties_in(core))}  | #808 states: {s_struct} Φ={s_phi:.3f} "
              f"{list(s_core)}  {'agree' if agree else 'DISAGREE'}")

    if args.ci:
        print("\n--ci: noise arm (C2, C3, H5, H6) and CSV output skipped.")
        return 0

    # ---- noise arm
    print("\nNoise arm (commit flipped with probability ε)")
    noise_rows = []
    c2_ok, c3_ok = True, True
    for r in rows:
        n = r["n"]
        labels = labels_for(n)
        for eps in EPS_GRID:
            tpm = noisy_tpm(r["table"], n, eps)
            cm = cm_numeric(tpm)
            v = classify(tpm, cm, labels=labels)
            core, phi = tpm_major_complex(tpm, cm, labels)
            noise_rows.append(dict(cid=r["cid"], n=n, eps=eps, structure=v.structure, Phi=v.max_phi,
                                   core=core, phi=phi))
            if eps == 0.0:
                same = (core == r["core"] and abs(phi - r["phi"]) <= TOL_MONO
                        and v.structure == r["structure"])
                c2_ok &= same
            if eps == 0.5:
                c3_ok &= (v.structure == "dyadic" and len(parties_in(core)) < 2)
    print(f"  C2 (ε=0 reproduces the deterministic readings): {'PASS' if c2_ok else 'FAIL'}")
    print(f"  C3 (ε=0.5 reads dyadic, no core with >=2 parties): {'PASS' if c3_ok else 'FAIL'}")

    nmap = {}
    for x in noise_rows:
        nmap.setdefault(x["cid"], []).append(x)
    print("\nPer-class noise table: core φ by ε (core membership marked * where it differs from ε=0)")
    print(f"  {'class':<7}{'type':<9}" + "".join(f"{e:<10.2f}" for e in EPS_GRID))
    for r in rows:
        seq = nmap[r["cid"]]
        cells = []
        for x in seq:
            mark = "*" if x["core"] != seq[0]["core"] else ""
            cells.append(f"{fmt_phi(x['core'], x['phi'], 4)}{mark}".ljust(10))
        print(f"  {r['cid']:<7}{r['ctype']:<9}" + "".join(cells))

    noise_ok = c2_ok and c3_ok
    ext_n = [r for r in ext]
    h5_bad = []
    for r in ext_n:
        seq = [x for x in nmap[r["cid"]] if x["eps"] < 0.5]
        target = {"S", *r["rel_labels"]}
        for a, b in zip(seq, seq[1:]):
            if b["phi"] > a["phi"] + TOL_MONO:
                h5_bad.append((r, b["eps"], "phi rises"))
        for x in seq:
            if x["core"] is None or set(x["core"]) != target:
                h5_bad.append((r, x["eps"], "membership"))
    h6_bad = [(r, x["eps"]) for r in mixed for x in nmap[r["cid"]]
              if x["eps"] > 0 and len(parties_in(x["core"])) >= 2]

    def nstat(ok, extra=True):
        if not noise_ok:
            return "NOT_TESTABLE (instrument)"
        return status(ok, testable and extra)

    print("\nHypotheses (noise arm)")
    print(f"  H5 (noise keeps extreme membership, φ non-increasing): {nstat(not h5_bad, bool(ext_n))}"
          f"  violations {len(h5_bad)}")
    print(f"  H6 (noise does not rescue a mixed quorum):             {nstat(not h6_bad, bool(mixed))}"
          f"  violations {len(h6_bad)}")
    for r, eps, why in h5_bad:
        x = [y for y in nmap[r["cid"]] if y["eps"] == eps][0]
        print(f"    H5 violation: {r['cid']} ({r['ctype']}) ε={eps:.2f} {why}: core={fmt_core(x['core'])} "
              f"φ={x['phi']:.6f}")
    for r, eps in h6_bad:
        x = [y for y in nmap[r["cid"]] if y["eps"] == eps][0]
        print(f"    H6 violation: {r['cid']} ε={eps:.2f} core={fmt_core(x['core'])} φ={x['phi']:.6f}")

    # ---- CSV
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "classes.csv"), "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["class", "n", "weights", "quota", "type", "relevant", "swing_counts", "truth_table",
                     "whole_structure", "whole_phi", "core", "core_phi"])
        for r in rows:
            wr.writerow([r["cid"], r["n"], " ".join(map(str, r["w"])), r["theta"], r["ctype"],
                         " ".join(r["rel_labels"]), " ".join(map(str, r["beta"])),
                         "".join(map(str, r["table"])), r["structure"], f"{r['Phi']:.6f}",
                         " ".join(r["core"] or ()), fmt_phi(r["core"], r["phi"])])
    with open(os.path.join(RESULTS, "noise.csv"), "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["class", "n", "eps", "whole_structure", "whole_phi", "core", "core_phi"])
        for x in noise_rows:
            wr.writerow([x["cid"], x["n"], f"{x['eps']:.2f}", x["structure"], f"{x['Phi']:.6f}",
                         " ".join(x["core"] or ()), fmt_phi(x["core"], x["phi"])])
    print("\nWrote results/classes.csv and results/noise.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
