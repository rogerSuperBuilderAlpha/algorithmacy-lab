"""Probe 454 (H1–H5) — the chicken-and-egg feed: does an engagement feed remove the first cause?

Question: when a celebrity's post spreads, is the arrangement a one-way chain with a first cause (dyadic,
Φ = 0) or a loop with no first cause (triadic, Φ > 0)? Which ingredient decides: an engagement-reactive
feed, an audience that sees itself, or a celebrity who reacts to engagement?
Hypotheses (hypotheses.md, fixed before this ran): H1 feedforward forms Φ = 0 (known IIT property);
H2 an unmoved celebrity factors the whole, loop core excludes them; H3 a reacting celebrity closes the loop
(triadic, full core); H4 recurrence, not the algorithm, removes the first cause; H5 Φ > 0 ⇔ strongly
connected causal graph (⇒ always, ⇐ ≥ 90%) and FEED-ENG-REACT triadic in ≥ 8/10 feed encodings.
Method: eleven 3–4 node forms (methods.md), whole-system verdict, major complex, an exploratory tie table,
causal-graph strong connectivity, and four ten-function encoding sweeps.
Instrument control: classifier factoring/irreducible controls and the canonical triad at Φ = 2.000.

Stylized models; not a model of any real platform, account, or audience.

Run (from the repo root, venv active):
    python -m org_frontier.questions.q218_chicken_egg_feed.probe_chicken_egg_feed
Add --plot to write results/chicken_egg.png. Deterministic.
"""

import csv
import itertools
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from org_frontier.classifier.validate import factoring_control, irreducible_control
from foundations.proxy_audit.exact_phi import reachable_states

EPS = 1e-9
HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")

GATES = [
    ("a∧b", lambda a, b: a & b), ("a∨b", lambda a, b: a | b),
    ("¬(a∧b)", lambda a, b: 1 - (a & b)), ("¬(a∨b)", lambda a, b: 1 - (a | b)),
    ("a⊕b", lambda a, b: a ^ b), ("¬(a⊕b)", lambda a, b: 1 - (a ^ b)),
    ("a∧¬b", lambda a, b: a & (1 - b)), ("¬a∧b", lambda a, b: (1 - a) & b),
    ("a∨¬b", lambda a, b: a | (1 - b)), ("¬a∨b", lambda a, b: (1 - a) | b),
]
AND = GATES[0][1]
OR = GATES[1][1]
PAB = ("P", "A", "B")
PFAB = ("P", "F", "A", "B")


# ------------------------------------------------------------------ forms
# 3-node order P=0, A=1, B=2 ; 4-node order P=0, F=1, A=2, B=3
def wom(react, g=OR):
    p = (lambda x: g(x[1], x[2])) if react else (lambda x: x[0])
    return [p, lambda x: x[0] | x[2], lambda x: x[0] | x[1]], PAB


def feed(eng, react, counts, g_feed=AND, g_fan=OR):
    if react:
        p = (lambda x: x[1]) if eng else (lambda x: x[2] | x[3])
    else:
        p = lambda x: x[0]
    f = (lambda x: g_feed(x[0], x[2] | x[3])) if eng else (lambda x: x[0])
    if counts:
        a, b = (lambda x: g_fan(x[1], x[3])), (lambda x: g_fan(x[1], x[2]))
    else:
        a, b = (lambda x: x[1]), (lambda x: x[1])
    return [p, f, a, b], PFAB


FORMS = [
    ("BROADCAST", "no feed", lambda: ([lambda x: x[0], lambda x: x[0], lambda x: x[0]], PAB)),
    ("CONTAGION", "no feed", lambda: wom(False)),
    ("WOM-REACT", "no feed", lambda: wom(True)),
    ("FEED-CHRONO", "chronological feed", lambda: feed(False, False, False)),
    ("FEED-CHRONO-REACT", "chronological feed", lambda: feed(False, True, False)),
    ("FEED-ENG", "engagement feed", lambda: feed(True, False, False)),
    ("FEED-ENG-REACT", "engagement feed", lambda: feed(True, True, False)),
    ("FEED-ENG-COUNTS", "engagement feed", lambda: feed(True, False, True)),
    ("FEED-ENG-REACT-COUNTS", "engagement feed", lambda: feed(True, True, True)),
    ("CHAIN", "control", lambda: ([lambda x: x[0], lambda x: x[0], lambda x: x[1], lambda x: x[2]], PFAB)),
    ("RING", "control", lambda: ([lambda x: x[3], lambda x: x[0], lambda x: x[1], lambda x: x[2]], PFAB)),
]

SWEEPS = [
    ("S1", "FEED-ENG-REACT feed rule", lambda g: feed(True, True, False, g_feed=g)),
    ("S2", "FEED-ENG feed rule", lambda g: feed(True, False, False, g_feed=g)),
    ("S3", "FEED-ENG-REACT-COUNTS fan rule", lambda g: feed(True, True, True, g_fan=g)),
    ("S4", "WOM-REACT celebrity rule", lambda g: wom(True, g)),
]


# ------------------------------------------------------------------ measures
def strongly_connected(rules):
    cm = cm_from_rules(rules)
    nn = len(rules)

    def reach(i):
        seen, stack = {i}, [i]
        while stack:
            u = stack.pop()
            for v in range(nn):
                if cm[u, v] and v not in seen:
                    seen.add(v)
                    stack.append(v)
        return seen
    return all(len(reach(i)) == nn for i in range(nn))


def subset_phis(rules, labels):
    nn = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = {}
    for s in reachable_states(tpm, nn):
        st = tuple((s >> i) & 1 for i in range(nn))
        for k in range(2, nn + 1):
            for sub in itertools.combinations(range(nn), k):
                try:
                    phi = float(new_big_phi.sia(pyphi.Subsystem(net, st, nodes=sub)).phi)
                except Exception:
                    continue
                key = "{" + ",".join(labels[i] for i in sub) + "}"
                best[key] = max(best.get(key, 0.0), phi)
    return best


def fmt(core):
    return "{" + ",".join(core) + "}" if core else "none"


def controls():
    fac = classify_rules(factoring_control())
    irr = classify_rules(irreducible_control())
    tri = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("W", "S", "C"))
    ok = fac.structure == "dyadic" and irr.structure == "triadic" and \
        tri.structure == "triadic" and abs(tri.max_phi - 2.0) < 1e-6
    print(f"  controls: factoring={fac.structure} irreducible={irr.structure} "
          f"canonical triad Φ={tri.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed"
    print("  Instrument validated.")


def main():
    print("PROBE 454 (H1–H5) — the chicken-and-egg feed: one-way chain or loop with no first cause?")
    print("  (stylized models; not a model of any real platform or audience)")
    print("=" * 104)
    controls()
    os.makedirs(RESULTS, exist_ok=True)

    print(f"\n  {'form':<23}{'SC':<5}{'whole':<9}{'Φ':>7}  {'core':<14}{'Φcore':>7}  top-Φ subsets (exploratory)")
    res, rows = {}, []
    for fid, kind, build in FORMS:
        rules, labels = build()
        v = verdict(rules, labels)
        core, cphi = major_complex(rules, labels)
        cphi = max(cphi, 0.0)
        if core is None or cphi <= EPS:
            core, cphi = None, 0.0
        sc = strongly_connected(rules)
        best = subset_phis(rules, labels)
        top = max(best.values()) if best else 0.0
        tied = sorted((k for k, x in best.items() if abs(x - top) < 1e-6 and top > EPS), key=len)
        res[fid] = dict(structure=v.structure, phi=v.max_phi, core=core, cphi=cphi, sc=sc,
                        top=top, tied=tied)
        print(f"  {fid:<23}{'yes' if sc else 'no':<5}{v.structure:<9}{v.max_phi:>7.3f}  {fmt(core):<14}"
              f"{cphi:>7.3f}  top={top:.3f} {' '.join(tied) if tied else '-'}")
        rows.append(dict(form=fid, kind=kind, strongly_connected=sc, structure=v.structure,
                         max_phi=round(v.max_phi, 6), core=fmt(core), core_phi=round(cphi, 6),
                         top_subset_phi=round(top, 6), tied_subsets=" ".join(tied)))
    with open(os.path.join(RESULTS, "forms.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("\n  Encoding sweeps (T triadic, d dyadic; SC = strongly connected causal graph)")
    print(f"  {'sweep':<6}{'rule swept':<34}" + "".join(f"{n:<8}" for n, _ in GATES) + " triadic")
    pairs = [(r["sc"], r["structure"] == "triadic") for r in res.values()]
    sweep_counts, srows = {}, []
    for sid, desc, build in SWEEPS:
        marks = []
        for name, g in GATES:
            rules, labels = build(g)
            v = verdict(rules, labels)
            sc = strongly_connected(rules)
            t = v.structure == "triadic"
            marks.append((t, sc))
            pairs.append((sc, t))
            srows.append(dict(sweep=sid, rule=desc, gate=name, strongly_connected=sc,
                              structure=v.structure, max_phi=round(v.max_phi, 6)))
        sweep_counts[sid] = sum(t for t, _ in marks)
        print(f"  {sid:<6}{desc:<34}" + "".join(f"{('T' if t else 'd') + ('' if sc else '*'):<8}"
                                             for t, sc in marks) + f" {sweep_counts[sid]}/10")
    print("  (* = causal graph not strongly connected for that encoding)")
    with open(os.path.join(RESULTS, "sweeps.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(srows[0].keys()))
        w.writeheader()
        w.writerows(srows)

    n_all = len(pairs)
    tri_not_sc = sum(1 for sc, t in pairs if t and not sc)
    sc_total = sum(1 for sc, _ in pairs if sc)
    sc_tri = sum(1 for sc, t in pairs if sc and t)
    print(f"\n  Connectivity table over {n_all} forms: triadic&SC={sc_tri}  dyadic&SC={sc_total - sc_tri}  "
          f"triadic&notSC={tri_not_sc}  dyadic&notSC={n_all - sc_total - tri_not_sc}")

    # ---- exploratory, added after the first run (not pre-registered)
    print("\n  Exploratory, added after the first run (not pre-registered): why FEED-ENG-REACT factors")
    expl = [
        ("E1 one fan", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("P", "F", "A")),
        ("E2 fans differ: B needs feed AND A", [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]),
                                                lambda x: x[1], lambda x: x[1] & x[2]], PFAB),
        ("E3 feed needs both fans", [lambda x: x[1], lambda x: x[0] & x[2] & x[3],
                                     lambda x: x[1], lambda x: x[1]], PFAB),
    ]
    for name, rules, labels in expl:
        v = verdict(rules, labels)
        core, cphi = major_complex(rules, labels)
        print(f"  {name:<38}{v.structure:<9}Φ={v.max_phi:.3f}  core={fmt(core if cphi > EPS else None)} "
              f"Φcore={max(cphi, 0.0):.3f}")

    # ---- decisions
    def tri(f):
        return res[f]["structure"] == "triadic"

    def core(f):
        return set(res[f]["core"] or ())

    def grade(k, full, part):
        return "CONFIRMED" if k >= full else ("PARTIAL" if k >= part else "REFUTED")

    print("\n" + "=" * 104)
    h1 = all(not tri(f) and res[f]["top"] <= EPS for f in ("BROADCAST", "FEED-CHRONO", "CHAIN"))
    print(f"  H1: feedforward forms dyadic with no multi-node complex: {h1} -> "
          f"{'CONFIRMED' if h1 else 'REFUTED'}")
    h2 = [not tri("CONTAGION"), core("CONTAGION") == {"A", "B"},
          not tri("FEED-ENG"), core("FEED-ENG") == {"F", "A", "B"},
          not tri("FEED-ENG-COUNTS"), core("FEED-ENG-COUNTS") == {"F", "A", "B"}]
    print(f"  H2: checks {h2} -> {grade(sum(h2), 6, 4)}")
    h3 = [tri("FEED-ENG-REACT"), core("FEED-ENG-REACT") == set(PFAB),
          tri("FEED-ENG-REACT-COUNTS"), core("FEED-ENG-REACT-COUNTS") == set(PFAB)]
    print(f"  H3: checks {h3} -> {grade(sum(h3), 4, 2)}")
    h4 = [tri("FEED-CHRONO-REACT"), tri("WOM-REACT"), tri("RING")]
    print(f"  H4: checks [FEED-CHRONO-REACT, WOM-REACT, RING triadic] = {h4} -> {grade(sum(h4), 3, 2)}")
    c1 = tri_not_sc == 0
    conv = sc_tri / sc_total if sc_total else 0.0
    c2 = conv >= 0.9
    c3 = sweep_counts["S1"] >= 8
    print(f"  H5: Φ>0 ⇒ SC without exception: {c1} ({tri_not_sc} exceptions); SC ⇒ Φ>0: {sc_tri}/{sc_total} "
          f"= {conv:.2f} (≥0.90: {c2}); S1 triadic {sweep_counts['S1']}/10 (≥8: {c3}) -> "
          f"{grade(sum([c1, c2, c3]), 3, 2)}")
    print(f"  sweeps: S1 {sweep_counts['S1']}/10, S2 {sweep_counts['S2']}/10, S3 {sweep_counts['S3']}/10, "
          f"S4 {sweep_counts['S4']}/10 triadic")
    print("=" * 104)

    if "--plot" in sys.argv:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(14, 5), gridspec_kw={"width_ratios": [3, 2]})
        ids = [f[0] for f in FORMS]
        cols = ["#54A24B" if res[i]["sc"] else "#B0B0B0" for i in ids]
        xs = list(range(len(ids)))
        axes[0].bar([x - 0.2 for x in xs], [res[i]["phi"] for i in ids], 0.4, color=cols,
                    edgecolor="black", label="whole-system Φ")
        axes[0].bar([x + 0.2 for x in xs], [res[i]["top"] for i in ids], 0.4, color=cols, alpha=0.45,
                    hatch="//", edgecolor="black", label="best sub-loop Φ")
        axes[0].set_xticks(xs)
        axes[0].set_xticklabels(ids, rotation=55, ha="right", fontsize=8)
        axes[0].set_ylabel("exact IIT-4.0 Φ")
        axes[0].set_title("Green: no first cause (strongly connected); grey: has a first cause", fontsize=9)
        axes[0].legend(fontsize=8)
        sids = [s[0] + " " + s[1] for s in SWEEPS]
        axes[1].barh(sids, [sweep_counts[s[0]] for s in SWEEPS], color="#4C78A8")
        axes[1].set_xlim(0, 10)
        axes[1].set_xlabel("encodings reading triadic (of 10)")
        axes[1].set_title("Encoding sweeps", fontsize=9)
        axes[1].tick_params(axis="y", labelsize=8)
        fig.suptitle("Chicken-and-egg feed: stylized models, not any real platform", fontsize=10)
        fig.tight_layout()
        fig.savefig(os.path.join(RESULTS, "chicken_egg.png"), dpi=150)
        print("  wrote results/chicken_egg.png")


if __name__ == "__main__":
    main()
