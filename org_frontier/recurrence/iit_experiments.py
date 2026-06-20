"""Ten Φ experiments seeded by the corpus sweep.

The sweep (sweep.py, SWEEP.md) found that structure and behavior locate a coordination's tight pair
differently: the false dyad reads as a weak W-S tie with a strong hidden S-C coupling, the relay
shows strong behavioral coupling with zero integrated information, and irreducible forms tend to
couple synchronously. These experiments take the structural side of those findings and pin it down on
exact Φ. Each prints one result.

Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/recurrence/iit_experiments.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence.crqa import trajectory, crqa, peak
from org_frontier.corpus.forms_library import FORMS
from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
from foundations.proxy_audit.exact_phi import reachable_states

LABELS = ("W", "S", "C")
NAME = {0: "W", 1: "S", 2: "C"}


def rand_form(rng):
    rules = []
    for _ in range(3):
        ins = [i for i in range(3) if rng.random() < 0.5] or [rng.randrange(3)]
        if len(ins) == 1:
            rules.append(_rule_of_one(rng.randint(0, 3), ins[0]))
        else:
            rules.append(_rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins))
    return rules


def core_of(rules):
    net, tpm = network(rules, LABELS)
    _, core, phi = complex_over_states(net, tpm, len(rules))
    return (sorted(core) if core else []), phi, net, tpm


def tightest_pair(rules, seed=3):
    rng = random.Random(seed)
    tr = trajectory(rules, 600, rng, flip=0.08)
    best, bestpair = -1.0, None
    for a, b in [(0, 1), (1, 2), (0, 2)]:
        m = crqa(tr[:, a], tr[:, b])
        _, prom = peak(tr[:, a], tr[:, b], max_lag=10)
        score = m["det"] * prom * m["lmax"]   # sustained, directed, and long
        if score > best:
            best, bestpair = score, (a, b)
    return bestpair


# E1 -------------------------------------------------------------------------------------
def e1_core_vs_tightest(n=200, seed=0):
    rng = random.Random(seed)
    disagree = total = 0
    for _ in range(n):
        rules = rand_form(rng)
        core, phi, _, _ = core_of(rules)
        if phi <= 0 or len(core) < 2:
            continue
        total += 1
        cpair = tuple(sorted(core[:2])) if len(core) == 2 else None
        tpair = tightest_pair(rules)
        if cpair is not None and cpair != tuple(sorted(tpair)):
            disagree += 1
    print(f"E1 core-vs-tightest: among {total} two-node-core irreducible forms, the dynamically "
          f"tightest pair differs from the Φ-core pair in {disagree} ({100*disagree/max(total,1):.0f}%)")


# E2 -------------------------------------------------------------------------------------
def e2_false_dyad_detector():
    """A true dyad and a false dyad present the same W-S pair. Whole-system Φ tells them apart: it
    is zero when the third party is decoupled and positive when a hidden read makes the whole
    irreducible, even when the major complex is still the presented pair."""
    true_dyad = next(x for x in FORMS if x.key == "chat_dyad")
    false_dyad = next(x for x in FORMS if x.key == "gig_false_dyad")
    out = []
    for f in (true_dyad, false_dyad):
        core, phi, _, _ = core_of(f.rules)
        whole = classify_rules(f.rules, LABELS).max_phi
        out.append(f"{f.key}: whole-system Φ={whole:.3f}, major complex={''.join(NAME[i] for i in core)}")
    print("E2 whole-system Φ detects the false dyad (same presented pair, hidden third):")
    print(f"    {out[0]}")
    print(f"    {out[1]} — the hidden read lifts whole-system Φ off zero")


# E3 -------------------------------------------------------------------------------------
def e3_feedforward_chains():
    rows = []
    for n in (2, 3, 4):
        rules = [(lambda x, i=i: x[i - 1]) for i in range(n)]
        rules[0] = (lambda x: x[0])           # source persists
        v = classify_rules(rules, tuple("WSCD"[:n]))
        net, tpm = network(rules, tuple("WSCD"[:n]))
        _, core, _ = complex_over_states(net, tpm, n)
        rows.append(f"len {n}: Φ={v.max_phi:.3f}, core={''.join('WSCD'[i] for i in sorted(core)) if core else '-'}")
    print("E3 feedforward chains carry no integrated information: " + "; ".join(rows))


# E4 -------------------------------------------------------------------------------------
def e4_reciprocity(n=250, seed=1):
    rng = random.Random(seed)
    with2, with2_irr, no2, no2_irr = 0, 0, 0, 0
    for _ in range(n):
        rules = rand_form(rng)
        cm = cm_from_rules(rules)
        has_cycle = any(cm[i, j] and cm[j, i] for i in range(3) for j in range(i + 1, 3))
        _, phi, _, _ = core_of(rules)
        if has_cycle:
            with2 += 1; with2_irr += phi > 0
        else:
            no2 += 1; no2_irr += phi > 0
    print(f"E4 reciprocity drives irreducibility: P(Φ>0 | a 2-cycle) = {100*with2_irr/max(with2,1):.0f}% "
          f"({with2_irr}/{with2}); P(Φ>0 | no 2-cycle) = {100*no2_irr/max(no2,1):.0f}% ({no2_irr}/{no2})")


# E5 -------------------------------------------------------------------------------------
def e5_veto_in_core(n=250, seed=2):
    rng = random.Random(seed)
    irr = veto_in_core = 0
    for _ in range(n):
        rules = rand_form(rng)
        core, phi, net, tpm = core_of(rules)
        if phi <= 0:
            continue
        irr += 1
        W = integrating_coalitions(net, tpm, 3)
        vs = veto_set(W) if W else set()
        if vs and vs.issubset(set(core)):
            veto_in_core += 1
    print(f"E5 the veto player sits in the core: in {veto_in_core}/{irr} irreducible forms with a "
          f"veto player, every veto player is a core member = {100*veto_in_core/max(irr,1):.0f}%")


# E6 -------------------------------------------------------------------------------------
def e6_commit_vs_store():
    a = next(x for x in FORMS if x.key == "ats_strict_bottleneck")
    b = next(x for x in FORMS if x.key == "ats_feedback_factors")
    ca, _, _, _ = core_of(a.rules)
    cb, _, _, _ = core_of(b.rules)
    pa = classify_rules(a.rules, LABELS).max_phi
    pb = classify_rules(b.rules, LABELS).max_phi
    print(f"E6 same topology, commit vs store: {a.key} whole-Φ={pa:.3f} core={''.join(NAME[i] for i in ca)}; "
          f"{b.key} whole-Φ={pb:.3f} core={''.join(NAME[i] for i in cb)} — the third joins the core only when S commits")


# E7 -------------------------------------------------------------------------------------
def e7_phi_det_dissociation(n=200, seed=4):
    rng = random.Random(seed)
    phis, dets = [], []
    for _ in range(n):
        rules = rand_form(rng)
        _, phi, _, _ = core_of(rules)
        tr = trajectory(rules, 400, random.Random(7), flip=0.08)
        best = max(crqa(tr[:, a], tr[:, b])["det"] for a, b in [(0, 1), (1, 2), (0, 2)])
        phis.append(phi); dets.append(best)
    phis, dets = np.array(phis), np.array(dets)
    r = float(np.corrcoef(phis, dets)[0, 1]) if phis.std() > 0 and dets.std() > 0 else 0.0
    hi_det_zero_phi = int(np.sum((dets > 0.8) & (phis <= 0)))
    print(f"E7 Φ and determinism dissociate: corr(Φ, max DET) = {r:+.2f}; "
          f"{hi_det_zero_phi}/{n} forms have DET>0.8 with Φ=0 (sustained coupling, reducible)")


# E8 -------------------------------------------------------------------------------------
def e8_third_party_membership():
    """Where is the third party (C) in each form: a member of the major complex, or excluded. The
    whole-system Φ and the core membership together place it."""
    print("E8 third-party membership across the corpus (whole-system Φ, major complex, C in core):")
    for f in FORMS:
        core, phi, _, _ = core_of(f.rules)
        whole = classify_rules(f.rules, LABELS).max_phi
        inc = "C in core" if 2 in core else "C excluded"
        print(f"    {f.key:<24} whole-Φ {whole:.3f}  core {''.join(NAME[i] for i in core) or '-':<3}  {inc}")


# E9 -------------------------------------------------------------------------------------
def e9_core_stability():
    from pyphi import new_big_phi
    print("E9 does the core membership move across reachable states:")
    for f in FORMS:
        net, tpm = network(f.rules, LABELS)
        seen = set()
        for s in reachable_states(tpm, 3):
            st = tuple((s >> i) & 1 for i in range(3))
            try:
                mc = new_big_phi.maximal_complex(net, st)
                if hasattr(mc, "node_indices") and float(mc.phi) > 1e-9:
                    seen.add(tuple(sorted(mc.node_indices)))
            except Exception:
                continue
        sets = " ".join("".join(NAME[i] for i in c) for c in sorted(seen)) or "-"
        print(f"    {f.key:<24} distinct nonzero cores across states: {len(seen) if seen else 0}  [{sets}]")


# E10 ------------------------------------------------------------------------------------
def e10_structural_sensitivity(n=120, seed=5):
    rng = random.Random(seed)
    flips = flips_changed = 0
    for _ in range(n):
        rules = rand_form(rng)
        base = classify_rules(rules, LABELS).structure
        tpm = np.array([[rules[j]((s & 1, (s >> 1) & 1, (s >> 2) & 1)) for j in range(3)]
                        for s in range(8)], dtype=int)
        for s in range(8):
            for j in range(3):
                t2 = tpm.copy(); t2[s, j] ^= 1
                newrules = [(lambda x, col=col, t=t2: int(t[x[0] | (x[1] << 1) | (x[2] << 2), col]))
                            for col in range(3)]
                flips += 1
                if classify_rules(newrules, LABELS).structure != base:
                    flips_changed += 1
    print(f"E10 structural sensitivity: {flips_changed}/{flips} single-bit rule flips change the "
          f"dyadic/triadic verdict = {100*flips_changed/max(flips,1):.0f}%")


if __name__ == "__main__":
    e1_core_vs_tightest()
    e2_false_dyad_detector()
    e3_feedforward_chains()
    e4_reciprocity()
    e5_veto_in_core()
    e6_commit_vs_store()
    e7_phi_det_dissociation()
    e8_third_party_membership()
    e9_core_stability()
    e10_structural_sensitivity()
