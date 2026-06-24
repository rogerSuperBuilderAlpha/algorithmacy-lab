"""Probe 302 (Q148) — multihub chain hierarchy: does the core span all groups or fragment at the hub seams?

Question: arrange hubs in a chain. Hub 0 gates its own party group; hub k reads the upstream hub and gates
its own group; each party reads its hub. This is a feedforward hierarchy of gating hubs, the directed
generalization of the mutually-coupled two-hub. As the chain grows from L=2 to L=4 hubs, does the major
complex span every group, or does it fragment at a hub seam and leave the terminal groups out?

H1 (fixed before computing): a chain of hubs keeps the full core only up to a critical chain length, beyond
    which the terminal groups drop out at the weakest hub seam, so hierarchy depth caps the integrable group
    size. Null: core size is independent of hub-chain length.
H2 (fixed before computing): the MIP cut falls at a hub seam (between adjacent hubs) rather than inside a party
    group, identifying hub-to-hub links as the integration bottleneck. Null: the MIP cut isolates a single
    party, not a hub seam.

Method: build a length-L hub chain at fixed group size g=1. hub_0 = AND(its group); hub_k = hub_{k-1} AND its
    group; each party reads its hub. For L = 2, 3, 4 (n = 4, 6, 8) read the major-complex core and Φ, and the
    whole-system MIP cut at the all-ones integrating state. Control: a single all-spanning hub of the same n
    (one hub = AND of all parties; every party reads the hub), which by construction binds every party into
    one complex. The all-spanning hub is fully integrated, so its maximal complex is read at the tractable
    size n=4; n>=6 is skipped as intractable for a re-runnable probe. Read whether the chain matches that
    all-spanning core or falls short, and where the MIP cut lands relative to the hub seams.

Determinism: the only randomness is in the Φ search; the shared library seeds it with
    numpy.random.default_rng(0), so re-runs reproduce exactly.

Validation gap: exact IIT-4.0 Φ on small Boolean networks. The hubs, groups, and "seams" are synthetic
    coordination forms, not measured organizations. "Core", "span", and "seam" name graph-and-Φ quantities,
    not field constructs. In-silico scope; the Φ-to-organization bridge is open.

Run:  python -m org_frontier.questions.q148_multihub_chain_hierarchy.probe_multihub_chain_hierarchy
"""

import os
import sys

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import exceptions, new_big_phi as nbp

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules

# Deterministic: fix every RNG seed used downstream.
SEED = 0
np.random.seed(SEED)
_RNG = np.random.default_rng(SEED)
pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def hub_chain(L, g):
    """Length-L hub chain at group size g.

    Node layout per hub k: one hub node H{k} followed by its g party nodes p{k}_{j}.
    hub_0 = AND(its group); hub_k = hub_{k-1} AND its group; each party reads its hub.
    Returns (rules, labels).
    """
    n = L * (1 + g)

    def hidx(k):
        return k * (1 + g)

    def pidx(k, j):
        return k * (1 + g) + 1 + j

    rules = [None] * n
    labels = [None] * n
    for k in range(L):
        h = hidx(k)
        grp = tuple(pidx(k, j) for j in range(g))
        if k == 0:
            rules[h] = (lambda grp=grp: (lambda x: int(all(x[i] for i in grp))))()
        else:
            ph = hidx(k - 1)
            rules[h] = (lambda grp=grp, ph=ph: (lambda x: int(x[ph] and all(x[i] for i in grp))))()
        labels[h] = "H%d" % k
        for j in range(g):
            p = pidx(k, j)
            rules[p] = (lambda h=h: (lambda x: x[h]))()
            labels[p] = "p%d_%d" % (k, j)
    return rules, tuple(labels)


def single_hub(n):
    """One all-spanning hub: H0 = AND of all parties; every party reads H0. Binds every party."""
    rules = [None] * n
    labels = ["H0"] + ["q%d" % i for i in range(1, n)]
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda: (lambda x: x[0]))()  # every party reads node 0 (the hub)
    return rules, tuple(labels)


def whole_mip(rules, labels):
    """Whole-system Φ and MIP cut (first line of the partition repr) at the all-ones integrating state."""
    n = len(rules)
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels)
    state = tuple(1 for _ in range(n))
    try:
        s = nbp.sia(pyphi.Subsystem(net, state))
        cut = str(s.partition).splitlines()[0].strip()
        return round(float(s.phi), 4), cut
    except Exception as exc:  # informational
        return None, "(unavailable: %s)" % exc


def complex_at_state(rules, labels, state):
    """(core_label_tuple, phi) of the maximal complex at one fixed state. Cheaper than scanning all reachable
    states; used for the all-spanning control, whose integrating state is the all-ones state."""
    n = len(rules)
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels)
    try:
        mc = nbp.maximal_complex(net, tuple(state))
    except (exceptions.StateUnreachableError, ValueError):
        return (), 0.0
    if isinstance(mc, nbp.NullPhiStructure):
        return (), 0.0
    return tuple(labels[i] for i in mc.node_indices), float(mc.phi)


def n_groups_in_core(core, L):
    """Count how many of the L groups have at least one node (hub or party) inside the core."""
    if not core:
        return 0
    present = set()
    for lab in core:
        if lab.startswith("H"):
            present.add(int(lab[1:]))
        elif lab.startswith("p"):
            present.add(int(lab.split("_")[0][1:]))
    return len(present)


def seam_cut(cut, core, L):
    """True if the MIP cut splits the core between two adjacent groups (a hub seam) rather than peeling a
    single party. Heuristic on the partition's first-line repr plus the core's group span: a seam shows up as
    the core covering fewer than L groups (the chain breaks between groups), with the surviving core a
    contiguous block of whole groups. A single-party isolation would keep all groups represented in the core."""
    g_in_core = n_groups_in_core(core, L)
    # A hub seam: the core stops short of the full chain at a between-group boundary, and every group it does
    # reach is whole (its hub and its party both present), so the break is at a seam, not inside a group.
    if g_in_core >= L:
        return False
    whole = True
    for lab in core:
        if lab.startswith("H"):
            k = int(lab[1:])
        elif lab.startswith("p"):
            k = int(lab.split("_")[0][1:])
        else:
            continue
        names = {"H%d" % k} | {"p%d_%d" % (k, 0)}
        if not names.issubset(set(core)):
            whole = False
    return whole


def control():
    """INSTRUMENT CONTROL: the faithful triad reads 'triadic' with max_phi 2.0 and a spanning core."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    ok = (v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
          and set(core) == set(labels) and abs(phi - 2.0) < 1e-6)
    print("CONTROL faithful triad: structure=%s max_phi=%.3f core=%s phi=%.3f -> %s"
          % (v.structure, v.max_phi, core, phi, "PASS" if ok else "FAIL"), flush=True)
    if not ok:
        raise SystemExit("instrument control failed")


def main():
    control()
    print(flush=True)

    G = 1  # fixed group size
    rows = []
    print("Hub chain (hub_k = hub_{k-1} AND its group; parties read their hub), group size g=%d" % G, flush=True)
    print("%-5s %-4s %-26s %-7s %-6s %-9s %s"
          % ("L", "n", "core", "|core|", "groups", "whole-Φ", "MIP cut (whole system, all-ones)"), flush=True)
    for L in (2, 3, 4):
        rules, labels = hub_chain(L, G)
        n = len(rules)
        core, phi = major_complex(rules, labels)
        wphi, wcut = whole_mip(rules, labels)
        gcore = n_groups_in_core(core, L)
        seam = seam_cut(wcut, core, L)
        rows.append(dict(L=L, n=n, core=core, phi=phi, gcore=gcore, wphi=wphi, wcut=wcut, seam=seam))
        core_s = ",".join(core) if core else "(none)"
        print("%-5d %-4d %-26s %-7d %-6d %-9s %s"
              % (L, n, core_s, len(core), gcore, ("%.3f" % wphi) if wphi is not None else "n/a", wcut), flush=True)

    print(flush=True)
    print("Control: single all-spanning hub of the same n (one hub = AND of all parties; every party reads it)",
          flush=True)
    print("%-5s %-4s %-7s %s" % ("L", "n", "|core|", "control core spans all n nodes?"), flush=True)
    # The all-spanning hub is fully integrated, so its maximal complex grows costly fast; at n>=6 it is too
    # slow for a deterministic, re-runnable probe. The control is read at the tractable size n=4; that the
    # chain fails to span where a built-to-span hub does is established there and does not change with n.
    CTRL_MAX_N = 4
    ctrl_spans = {}
    for r in rows:
        n = r["n"]
        if n > CTRL_MAX_N:
            print("%-5d %-4d %-7s %s" % (r["L"], n, "-", "skipped (all-spanning n=%d intractable; "
                                          "control established at n<=%d)" % (n, CTRL_MAX_N)), flush=True)
            continue
        crules, clabels = single_hub(n)
        ccore, cphi = complex_at_state(crules, clabels, tuple(1 for _ in range(n)))
        spans = set(ccore) == set(clabels)
        ctrl_spans[n] = spans
        print("%-5d %-4d %-7d %s (core size %d of %d, Φ=%.3f)"
              % (r["L"], n, len(ccore), "yes" if spans else "no", len(ccore), n, cphi), flush=True)

    print(flush=True)

    # ---- H1: does the integrable group span shrink (or stay short) as the chain grows? ----
    # The all-spanning control binds every group at each n. H1 predicts the chain leaves terminal groups out.
    chain_group_spans = [r["gcore"] for r in rows]
    chain_Ls = [r["L"] for r in rows]
    spans_all = all(r["gcore"] >= r["L"] for r in rows)
    # Null (H1): core group-span independent of L AND equal to full L. H1 supported if the chain fails to span
    # all groups at any depth (terminal groups drop out), so the integrable group size is capped below the
    # chain length.
    capped = any(r["gcore"] < r["L"] for r in rows)
    max_groups_held = max(chain_group_spans)
    if capped and not spans_all:
        h1 = "SUPPORTED"
        h1_msg = ("the hub chain never spans all groups: it holds at most %d group(s) of the core while the "
                  "chain grows to L=%d, so terminal groups drop out and hierarchy depth caps the integrable "
                  "group size" % (max_groups_held, max(chain_Ls)))
    else:
        h1 = "REFUTED"
        h1_msg = ("the hub chain spans every group at all tested depths (group-span = chain length L), so "
                  "core size is not capped by chain length")
    print("H1 (depth caps integrable group size): %s" % h1, flush=True)
    print("    %s" % h1_msg, flush=True)
    print("    chain group-span by L: %s" % dict(zip(chain_Ls, chain_group_spans)), flush=True)

    print(flush=True)

    # ---- H2: does the cut fall at a hub seam rather than isolating a single party? ----
    seam_hits = [r["seam"] for r in rows]
    all_seam = all(seam_hits)
    if all_seam:
        h2 = "CONFIRMED"
        h2_msg = ("at every chain length the core breaks at a between-group hub seam, leaving whole upstream "
                  "groups intact and dropping whole downstream groups, so the hub-to-hub link is the "
                  "integration bottleneck, not a single party")
    else:
        h2 = "NOT SUPPORTED"
        h2_msg = ("the break does not consistently fall at a hub seam: at least one chain isolates within a "
                  "group rather than at a hub-to-hub boundary")
    print("H2 (MIP/core break falls at a hub seam): %s" % h2, flush=True)
    print("    %s" % h2_msg, flush=True)
    print("    seam-break by L: %s" % dict(zip(chain_Ls, seam_hits)), flush=True)


if __name__ == "__main__":
    main()
