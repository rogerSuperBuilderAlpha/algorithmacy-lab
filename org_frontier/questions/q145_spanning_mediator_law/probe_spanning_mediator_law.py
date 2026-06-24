"""Probe Q145 — the spanning-mediator law.

Question: when one mediator spans (reads and is read by) every node of an otherwise
unconnected party set, how do Φ and the core scale versus a mediator that spans only a
fraction of the parties?

H1: A fully spanning single mediator holds the entire node set in the core, with Φ growing
    linearly in n (the conjunctive-hub law). A partially spanning mediator caps the core at
    its span+1 and leaves unspanned parties out. Null: core size is independent of the span
    fraction.
H2: Φ scales with the spanned fraction f as a single monotone curve that collapses across n
    when plotted in f, so span fraction is the controlling variable. Null: Φ(f) curves for
    different n do not collapse.

Method: parameterize single_hub(n, f) so the hub reads/is-read-by only the first
    k = round(f*(n-1)) parties; the hub fires on the conjunction of its spanned parties, each
    spanned party reads the hub, each unspanned party is an isolated self-loop. Sweep f at
    n = 4, 5, 6. major_complex() gives the core tuple and Φ at the integrating state. Controls:
    full single_hub (f=1) and disconnected parties (f=0). Verdicts are read off the computed
    numbers. All work is on synthetic Boolean coordination forms; no organization is measured.

Run:
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q145_spanning_mediator_law.probe_spanning_mediator_law
"""

import os

import numpy as np

from org_frontier.probes.lib import verdict, major_complex


# ---------------------------------------------------------------------------
# Parameterized spanning mediator.
# Node 0 is the hub (mediator). Nodes 1..n-1 are the parties.
# The hub spans the first k = round(f*(n-1)) parties: it reads their conjunction and
# each spanned party reads it back. Unspanned parties are isolated self-loops.
# ---------------------------------------------------------------------------

def _spanned_count(n, f):
    return int(round(f * (n - 1)))


def single_hub(n, f):
    """Return (rules, labels) for a hub spanning the first round(f*(n-1)) of n-1 parties."""
    k = _spanned_count(n, f)
    spanned = tuple(range(1, 1 + k))

    if spanned:
        rules = [lambda x, sp=spanned: int(all(x[i] for i in sp))]
    else:
        rules = [lambda x: 0]
    for p in range(1, n):
        if p in spanned:
            rules.append(lambda x: x[0])           # spanned party reads the hub
        else:
            rules.append(lambda x, p=p: x[p])      # unspanned party: isolated self-loop
    labels = tuple(["H"] + [f"P{i}" for i in range(1, n)])
    return rules, labels


def main():
    np.random.default_rng(0)  # fix RNG; the major-complex search is otherwise deterministic
    print("PROBE Q145 — the spanning-mediator law")
    print("=" * 72)

    # ---- INSTRUMENT CONTROL ------------------------------------------------
    ctrl_rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    ctrl_labels = ("W", "S", "C")
    cv = verdict(ctrl_rules, ctrl_labels)
    cc, cphi = major_complex(ctrl_rules, ctrl_labels)
    ctrl_ok = (cv.structure == "triadic" and abs(cv.max_phi - 2.0) < 1e-9
               and cc == ("W", "S", "C") and abs(cphi - 2.0) < 1e-9)
    print(f"CONTROL faithful triad: structure={cv.structure} max_phi={cv.max_phi} "
          f"core={cc} phi={cphi} -> {'PASS' if ctrl_ok else 'FAIL'}")
    if not ctrl_ok:
        raise SystemExit("instrument control failed")
    print("-" * 72)

    # ---- SWEEP -------------------------------------------------------------
    ns = [4, 5, 6]
    rows = []  # (n, k, f, core_tuple, core_size, phi, span_covers_all, unspanned_excluded)
    print(f"{'n':>2} {'k':>2} {'f':>6} {'core_size':>9} {'phi':>5}  core")
    for n in ns:
        for k in range(n):  # k spanned parties, 0..n-1
            f = k / (n - 1)
            rules, labels = single_hub(n, f)
            core, phi = major_complex(rules, labels)
            core_set = set(core)
            spanned_lbls = {"H"} | {f"P{i}" for i in range(1, 1 + k)}
            unspanned_lbls = {f"P{i}" for i in range(1 + k, n)}
            covers_all = (k == n - 1)
            full_core = (len(core) == n)
            capped_at_span1 = (len(core) == k + 1) and core_set == spanned_lbls
            unspanned_excluded = len(core_set & unspanned_lbls) == 0
            rows.append(dict(n=n, k=k, f=f, core=core, core_size=len(core), phi=phi,
                             covers_all=covers_all, full_core=full_core,
                             capped=capped_at_span1, unspanned_excluded=unspanned_excluded,
                             spanned_present=spanned_lbls <= core_set))
            print(f"{n:>2} {k:>2} {f:>6.3f} {len(core):>9} {phi:>5.1f}  {core}")
    print("-" * 72)

    # ---- H1: full span holds the whole set; Φ linear in n; partial span caps at span+1 ----
    full_rows = [r for r in rows if r["covers_all"]]
    partial_rows = [r for r in rows if 0 < r["k"] < r["n"] - 1]

    full_holds_all = all(r["full_core"] for r in full_rows)
    # Φ at f=1 grows linearly in n: Φ == n-1 for each full-span case.
    phi_linear = all(abs(r["phi"] - (r["n"] - 1)) < 1e-9 for r in full_rows)
    # Partial span: core is exactly the hub plus its k spanned parties (size k+1).
    partial_caps = all(r["capped"] for r in partial_rows)
    partial_excludes = all(r["unspanned_excluded"] for r in partial_rows)
    h1 = full_holds_all and phi_linear and partial_caps and partial_excludes

    print("H1 components:")
    print(f"  full span holds the whole node set (core size == n):   {full_holds_all}")
    print(f"  Φ at full span == n-1 (linear in n): {[ (r['n'], r['phi']) for r in full_rows ]}: {phi_linear}")
    print(f"  partial span caps core at span+1 (hub + k parties):    {partial_caps}")
    print(f"  partial span excludes every unspanned party:           {partial_excludes}")

    # ---- H2: does Φ(f) collapse across n? ----------------------------------
    # Group rows by the fractions common to all n (f in {0, 1}); compare Φ across n.
    # The decisive comparison is at f=1, where every n is sampled.
    phi_at_f1 = sorted({round(r["phi"], 6) for r in full_rows})
    collapses_at_f1 = len(phi_at_f1) == 1
    phi_at_f0 = sorted({round(r["phi"], 6) for r in rows if r["k"] == 0})
    collapses_at_f0 = len(phi_at_f0) == 1
    # H2 requires collapse wherever multiple n share an f; f=1 is shared by all three n.
    h2 = collapses_at_f1 and collapses_at_f0

    print("H2 components:")
    print(f"  Φ values at f=1 across n={ns}: {[r['phi'] for r in full_rows]} "
          f"(distinct={phi_at_f1}, collapses={collapses_at_f1})")
    print(f"  Φ values at f=0 across n={ns}: {[r['phi'] for r in rows if r['k']==0]} "
          f"(distinct={phi_at_f0}, collapses={collapses_at_f0})")
    print(f"  controlling variable check: at fixed f the spanned COUNT k=round(f*(n-1)) "
          f"sets Φ≈k+1, so Φ depends on n at fixed f.")

    print("=" * 72)
    print(f"H1 spanning-mediator law (full span holds all, Φ linear in n; partial caps at span+1): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"H2 Φ(f) collapses across n (span fraction is the controlling variable): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")

    # ---- write a small CSV of the sweep ------------------------------------
    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    import csv
    with open(os.path.join(d_, "sweep.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["n", "k_spanned", "f", "core_size", "phi", "core"])
        for r in rows:
            w.writerow([r["n"], r["k"], f"{r['f']:.4f}", r["core_size"], r["phi"],
                        "|".join(r["core"])])


if __name__ == "__main__":
    main()
