"""Four identical parties: tie-dependence of IIT 4.0 verdicts. Nodes P1..P4, S; P_i' = S; S' = h(P1..P4).

Run from the repo root: python org_frontier/studies/four_party_ties/run.py [--quick] [--write] [--jobs N]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import itertools
import json
import os
import random
import sys
import warnings
from importlib.metadata import version
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
warnings.filterwarnings("ignore")

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402
from pyphi.models.subsystem import SystemStateSpecification  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import (  # noqa: E402
    PHI_EPS, classify_rules, cm_from_rules, tpm_from_rules,
)

N = 4
FULL = (1 << N) - 1
LABELS = ("P1", "P2", "P3", "P4", "S")


def bit(m, x):
    return (m >> x) & 1


def from_profile(p):
    return sum(int(p[bin(x).count("1")]) << x for x in range(16))


AND4 = from_profile("00001")
QUICK = [("symmetric", AND4), ("symmetric", from_profile("00111"))]


def pivotal(m):
    out = []
    for a in (0, FULL):
        base = bit(m, a)
        out.append(all(bit(m, a ^ (1 << i)) != base for i in range(N)))
    return out


def profile(m):
    prof = {}
    for x in range(16):
        if prof.setdefault(bin(x).count("1"), bit(m, x)) != bit(m, x):
            return None
    return "".join(str(prof[k]) for k in range(N + 1))


def sample():
    cases = [("symmetric", from_profile(f"{k:05b}")) for k in range(1, 31)]
    rng, seen = random.Random(0), set()
    while len(seen) < 128:
        a = rng.choice((0, FULL))
        v = rng.randint(0, 1)
        m = rng.getrandbits(16)
        m = (m & ~(1 << a)) | (v << a)
        for i in range(N):
            j = a ^ (1 << i)
            m = (m & ~(1 << j)) | ((1 - v) << j)
        if sum(pivotal(m)) == 1:
            seen.add(m)
    cases += [("one_sided", m) for m in sorted(seen)]
    rng = random.Random(1)
    cases += [("uniform", rng.getrandbits(16)) for _ in range(64)]
    return cases


def rules_of(m):
    return [lambda x: x[4]] * N + [lambda x: bit(m, x[0] | (x[1] << 1) | (x[2] << 2) | (x[3] << 3))]


def read(case):
    group, m = case
    rules = rules_of(m)
    v = classify_rules(rules, labels=LABELS)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm)
    lo = hi = 0.0
    tied = 0
    for s in reachable_states(tpm, N + 1):
        sub = pyphi.Subsystem(net, tuple((s >> i) & 1 for i in range(N + 1)))
        si = new_big_phi.system_intrinsic_information(sub)
        causes, effects = si.cause.ties or [si.cause], si.effect.ties or [si.effect]
        tied += (len(causes) * len(effects)) > 1
        phis = [float(new_big_phi.sia(sub, system_state=SystemStateSpecification(cause=c, effect=e)).phi)
                for c, e in itertools.product(causes, effects)]
        lo, hi = max(lo, min(phis)), max(hi, max(phis))
    piv = pivotal(m)
    return dict(group=group, m=m, profile=profile(m), phi=float(v.max_phi), phi_tie_min=lo,
                phi_tie_max=hi, tied_states=tied, pivotal_at_0=piv[0], pivotal_at_1=piv[1],
                rule_R=any(piv), tie_dependent=(lo > PHI_EPS) != (hi > PHI_EPS))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--jobs", type=int, default=os.cpu_count())
    args = ap.parse_args()
    cases = QUICK if args.quick else sample()
    with Pool(args.jobs) as pool:
        rows = pool.map(read, cases, chunksize=1)
    and4 = next(r for r in rows if r["m"] == AND4)
    if abs(and4["phi"] - 4.0) > 1e-6:
        raise SystemExit("control failed")
    print("C1 control (AND4 4.0): PASS")
    for r in rows:
        if r["group"] == "symmetric":
            print(f"profile={r['profile']} phi={r['phi']:.6f} tie_min={r['phi_tie_min']:.6f} "
                  f"tie_max={r['phi_tie_max']:.6f} rule={'Y' if r['rule_R'] else 'N'}")
    if args.quick:
        return
    groups = {}
    for g in ("symmetric", "one_sided", "uniform"):
        gr = [r for r in rows if r["group"] == g]
        groups[g] = dict(n=len(gr), triadic_default=sum(r["phi"] > PHI_EPS for r in gr),
                         triadic_some_tie=sum(r["phi_tie_max"] > PHI_EPS for r in gr),
                         triadic_every_tie=sum(r["phi_tie_min"] > PHI_EPS for r in gr),
                         rule_R=sum(r["rule_R"] for r in gr),
                         tie_dependent=sum(r["tie_dependent"] for r in gr))
        print(f"{g}: {groups[g]}")
    r_bad = [(r["group"], r["m"]) for r in rows if (r["phi_tie_max"] > PHI_EPS) != r["rule_R"]]
    share = groups["one_sided"]["tie_dependent"] / groups["one_sided"]["n"]
    vals = sorted({round(r["phi"], 6) for r in rows if r["phi"] > PHI_EPS})
    print(f"rule R mismatches: {len(r_bad)} {r_bad}")
    print(f"one-sided tie-dependent share: {share:.4f} (three parties: {24 / 56:.4f})")
    print(f"distinct default triadic phi: {vals}")
    scores = {"H1": not r_bad, "H2": groups["symmetric"]["tie_dependent"] == 0, "H3": share > 24 / 56}
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            groups=groups, rule_R_mismatches=r_bad, one_sided_tie_share=share,
            distinct_default_triadic_phi=vals, rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
