"""Probe — Peirce addendum JD1–JD3: joint determination, fixed in advance (jd_hypotheses.md, jd_methods.md).

Question.  With the criterion fixed before any run — a one-element mechanism whose irreducible cause purview
           holds two other elements, read inside the major complex of an irreducible whole — does the
           criterion read the registered exemplars as the talk claims (JD1), does Simmel's majority give a
           party jointly determined in a system that factors (JD2), and do families not read before confirm
           it (JD3)?
Method.    The paper's reader and state set; distinctions from new_big_phi.phi_structure; Φ_MIP and the
           major complex from org_frontier.probes.lib. Decision rules as in jd_methods.md.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.peirce.probe_peirce_joint_determination [--full]
"""

import itertools
import sys
import time

import pyphi

from org_frontier.thinkers.peirce import forms as F
from org_frontier.thinkers.simmel import forms as S
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict, major_complex
from foundations.proxy_audit.exact_phi import reachable_states


def tied_cause_purviews(net, state, x, tol=1e-9):
    """All cause purviews of the one-element mechanism (x,) whose φ equals the maximum (post hoc)."""
    sub = pyphi.Subsystem(net, state)
    n = len(state)
    scores = []
    for k in range(1, n + 1):
        for pv in itertools.combinations(range(n), k):
            try:
                scores.append((float(sub.find_mip(pyphi.Direction.CAUSE, (x,), pv).phi), pv))
            except Exception:
                continue
    top = max(sc for sc, _ in scores)
    return [pv for sc, pv in scores if top - sc <= tol]


def joint_determination(rules, labels):
    """For each element: the largest cause purview (other elements, φ) of its own first-order
    distinction over the paper's state set, kept only when it holds two or more other elements."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    states = {tuple(1 for _ in range(n))}
    states |= {tuple((s >> i) & 1 for i in range(n)) for s in reachable_states(tpm, n)}
    found = {}
    for st in sorted(states):
        ps = F.distinctions_at(net, st)
        if ps is None:
            continue
        for d in ps.distinctions:
            if float(d.phi) <= 0 or len(d.mechanism) != 1:
                continue
            x = d.mechanism[0]
            others = sorted(set(d.cause.purview) - {x})
            if len(others) < 2:
                continue
            # Post hoc (not in jd_methods.md): the reported cause purview may be one of several tied at the
            # maximal cause φ, with PyPhi choosing by index order. Recompute every candidate purview; the
            # element is tie-robust only if every maximal purview also holds two or more other elements.
            tied = tied_cause_purviews(net, st, x)
            robust = all(len(set(t) - {x}) >= 2 for t in tied)
            key = (len(others), float(d.phi))
            if x not in found or key > found[x][0]:
                found[x] = (key, others, "".join(map(str, st)), robust, len(tied))
    return {labels[x]: {"purview": [labels[j] for j in v[1]], "phi": round(v[0][1], 6), "state": v[2],
                        "tie_robust": v[3], "n_tied_purviews": v[4]}
            for x, v in sorted(found.items())}


def read(name, form):
    labels, rules = form
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core = set(core) if core else set()
    jd = joint_determination(rules, labels)
    phi = round(float(v.max_phi), 6)
    in_whole = phi > 0 and any(x in core and len(core & set(info["purview"])) >= 2 for x, info in jd.items())
    robust = any(info["tie_robust"] for info in jd.values())
    rec = {"form": name, "labels": list(labels), "phi_mip": phi, "core": sorted(core),
           "jd_elements": jd, "jd": bool(jd), "jd_in_whole": bool(in_whole),
           "post_hoc_jd_tie_robust": bool(robust), "seconds": round(time.time() - t0, 2)}
    shown = ", ".join("%s <- %s (φ=%.3f%s)" % (x, "".join(i["purview"]), i["phi"],
                                                "" if i["tie_robust"] else ", tied") for x, i in jd.items()) or "none"
    print("  %-22s Φ_MIP=%.6f  core=%-22s jd=%-5s in_whole=%-5s  %s"
          % (name, phi, tuple(sorted(core)), rec["jd"], rec["jd_in_whole"], shown))
    return rec


def status(n_miss, partial_at=1):
    return "CONFIRMED" if n_miss == 0 else ("PARTIAL" if n_miss <= partial_at else "REFUTED")


def jd1():
    print("JD1 — the registered exemplars under the fixed criterion")
    copies = dict(F.one_input_wirings(3))
    positive = [("control", F.CONTROL), ("giving_genuine", F.GIVING_GENUINE), ("sign_pragmatic", F.SIGN_PRAGMATIC)]
    negative = [("dyad_mutual", S.DYAD_MUTUAL), ("copy_BCA", copies["copy_BCA"]), ("copy_CCA", copies["copy_CCA"]),
                ("giving_degenerate", F.GIVING_DEGENERATE), ("dyadic_degenerate", F.DYADIC_DEGENERATE),
                ("monadic_degenerate", F.MONADIC_DEGENERATE), ("sign_exogenous", F.SIGN_EXOGENOUS)]
    pos = [read(n, f) for n, f in positive]
    neg = [read(n, f) for n, f in negative]
    miss = sum(1 for r in pos if not r["jd_in_whole"]) + sum(1 for r in neg if r["jd"])
    verdict_ = status(miss)
    print("JD1 (criterion reads the exemplars: 3 in a whole, 7 with none): %s  misreads=%d" % (verdict_, miss))
    return {"positive": pos, "negative": neg, "misreads": miss, "verdict": verdict_}


def jd2():
    print("JD2 — Simmel's majority, mutual triad and mediator")
    maj = read("majority_triad", S.MAJORITY_TRIAD)
    mut = read("triad_mutual", S.TRIAD_MUTUAL)
    med = read("mediator", S.MEDIATOR)
    majority_ok = maj["jd"] and maj["phi_mip"] == 0
    others_fail = sum(1 for r in (mut, med) if not r["jd_in_whole"])
    verdict_ = "REFUTED" if not majority_ok else ("CONFIRMED" if others_fail == 0 else "PARTIAL")
    print("JD2 (a party jointly determined in a system that factors: majority jd=%s Φ_MIP=%.6f): %s"
          % (maj["jd"], maj["phi_mip"], verdict_))
    print("  post hoc: majority joint determination tie-robust=%s" % maj["post_hoc_jd_tie_robust"])
    return {"majority_triad": maj, "triad_mutual": mut, "mediator": med, "verdict": verdict_}


def iso_representatives(n):
    """One copy wiring per isomorphism class: relabel k -> p^-1(f(p(k))), keep the smallest tuple."""
    reps = set()
    for f in itertools.product(*[[j for j in range(n) if j != i] for i in range(n)]):
        reps.add(min(tuple(p.index(f[p[k]]) for k in range(n)) for p in itertools.permutations(range(n))))
    labels = tuple("ABCDE"[:n])
    for srcs in sorted(reps):
        yield "copy_" + "".join(labels[j] for j in srcs), (labels, [lambda x, j=j: x[j] for j in srcs])


def jd3(full):
    out = {}
    if full:
        print("JD3(a) — one-input wirings at n = 5, one per isomorphism class")
        recs_a = [read(n, f) for n, f in iso_representatives(5)]
        n_jd = sum(1 for r in recs_a if r["jd"])
        print("  n=5 isomorphism classes=%d  with joint determination=%d" % (len(recs_a), n_jd))
        out["a"] = {"forms": recs_a, "classes": len(recs_a), "with_jd": n_jd}
    k = 30 if full else 8
    print("JD3(b) — two-input sample, seed 1, n = 4, %d forms%s" % (k, "" if full else " (fast prefix)"))
    recs_b = []
    for name, form, spec in F.two_input_sample(k, seed=1, n=4):
        rec = read(name, form)
        rec["spec"] = spec
        recs_b.append(rec)
    in_whole = sum(1 for r in recs_b if r["jd_in_whole"])
    factors = sum(1 for r in recs_b if r["jd"] and r["phi_mip"] == 0)
    print("  forms=%d  joint determination in a whole=%d  joint determination with Φ_MIP=0=%d  no jd=%d"
          % (len(recs_b), in_whole, factors, sum(1 for r in recs_b if not r["jd"])))
    robust_factors = sum(1 for r in recs_b if r["post_hoc_jd_tie_robust"] and r["phi_mip"] == 0)
    robust_whole = sum(1 for r in recs_b if r["post_hoc_jd_tie_robust"] and r["jd_in_whole"])
    print("  post hoc, tie-robust only: in a whole=%d  with Φ_MIP=0=%d" % (robust_whole, robust_factors))
    out["b"] = {"forms": recs_b, "n": len(recs_b), "jd_in_whole": in_whole, "jd_factors": factors}
    if full:
        a_ok = out["a"]["with_jd"] == 0
        cells = (in_whole >= 1) + (factors >= 1)
        verdict_ = "CONFIRMED" if a_ok and cells == 2 else ("PARTIAL" if a_ok and cells == 1 else "REFUTED")
        print("JD3 (confirmation on unread families: n=5 none, both cells non-empty): %s" % verdict_)
        out["verdict"] = verdict_
    return out


def main():
    full = "--full" in sys.argv
    print("Peirce addendum — joint determination, criterion fixed in advance%s" % (" (full)" if full else ""))
    control = F.run_control()
    payload = {"control": control, "JD1": jd1(), "JD2": jd2(), "JD3": jd3(full)}
    F.save("probe_peirce_joint_determination" + ("_full" if full else ""), payload)


if __name__ == "__main__":
    main()
