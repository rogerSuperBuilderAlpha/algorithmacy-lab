"""Paper 3 rebuild — the catalog of the W–S–C model family (from scratch, PyPhi-only).

Paper 2 picked a handful of coordination forms and classified each. Paper 3 enumerates the
complete family of three-node wirings instead, computes exact Φ for every one, and reads off
how the scores are distributed. Most wirings are not recognizable coordination forms. The
enumeration is a coverage check, not a census of coordination. It does two things: it shows
what the model yields across its whole domain, and it shows the hand-modeled organizations in
`typology.py` fall on populated bands of the family rather than being cherry-picked.

The grammar. Node order 0=W (worker), 1=S (system/mediator), 2=C (counterpart), 3=D (fourth
party). A triad wiring is any way each node's next value depends on the other two. There are
16 Boolean functions of two inputs, so the complete triad family is 16^3 = 4096 wirings:
    W' = f_W(S, C),   S' = f_S(W, C),   C' = f_C(W, S).
All are enumerated, with no curation, and deduplicated by identical transition matrix. A
higher-order family adds 48 four-node forms: the mediator S aggregates three parties (W, C, D)
with one of six symmetric functions, and each party reads the mediator only, or the mediator
or the other two.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/rebuild/catalog.py [--smoke]
Output: rebuild/results/catalog.csv (written incrementally; safe to interrupt).
"""

import csv
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import numpy as np

from phi_core import tpm_from_rules, cm_from_rules, phi_over_states


# ----- the 16 Boolean functions of two inputs -----------------------------------------
# tt is a 4-bit truth table; value at inputs (a, b) is bit ((a<<1)|b) of tt. These 16
# functions are the complete space of pairwise dependence.

def _bin(tt):
    return lambda a, b, tt=tt: (tt >> ((a << 1) | b)) & 1

BIN = {tt: _bin(tt) for tt in range(16)}

# Labels in terms of a node's two inputs A, B (for S: A=W, B=C). Value of tt at (a,b) is
# bit ((a<<1)|b).
BIN_LABEL = {
    0: "FALSE", 1: "NOR", 2: "~A&B", 3: "~A", 4: "A&~B", 5: "~B", 6: "XOR", 7: "NAND",
    8: "AND", 9: "XNOR", 10: "B", 11: "~A|B", 12: "A", 13: "A|~B", 14: "OR", 15: "TRUE",
}
DEPENDS_BOTH = {1, 2, 4, 6, 7, 8, 9, 11, 13, 14}  # functions that read both inputs
PARITY = {6, 9}                                    # XOR / XNOR


# ----- structural features from the inferred connectivity (cm[i,j]=1 iff j reads i) -----

def triad_features(cm, fS):
    s_reads_w = cm[0, 1]; s_reads_c = cm[2, 1]
    w_reads_s = cm[1, 0]; w_reads_c = cm[2, 0]
    c_reads_s = cm[1, 2]; c_reads_w = cm[0, 2]
    mediator_depends_both = bool(s_reads_w and s_reads_c)
    strict_mediation = bool(
        mediator_depends_both
        and w_reads_s and not w_reads_c
        and c_reads_s and not c_reads_w
    )
    back_channel = bool(w_reads_c or c_reads_w)
    return {
        "edges": int(cm.sum()),
        "mediator_depends_both": int(mediator_depends_both),
        "strict_mediation": int(strict_mediation),
        "back_channel": int(back_channel),
        "mediator_fn": BIN_LABEL[fS] if mediator_depends_both else "(none)",
    }


# ----- enumeration --------------------------------------------------------------------

def enumerate_triads():
    """Yield (kind, label, rules, n, fS, parity_present) for all 16^3 triad wirings."""
    for fW in range(16):
        for fS in range(16):
            for fC in range(16):
                rules = [
                    lambda x, f=fW: BIN[f](x[1], x[2]),  # W' = f(S, C)
                    lambda x, f=fS: BIN[f](x[0], x[2]),  # S' = f(W, C)
                    lambda x, f=fC: BIN[f](x[0], x[1]),  # C' = f(W, S)
                ]
                parity = int(bool({fW, fS, fC} & PARITY))
                label = f"W={BIN_LABEL[fW]},S={BIN_LABEL[fS]},C={BIN_LABEL[fC]}"
                yield ("triad", label, rules, 3, fS, parity)


TERN = {
    "AND3": lambda a, b, c: a & b & c,
    "OR3": lambda a, b, c: a | b | c,
    "XOR3": lambda a, b, c: a ^ b ^ c,
    "MAJ3": lambda a, b, c: 1 if (a + b + c) >= 2 else 0,
    "NAND3": lambda a, b, c: 0 if (a & b & c) else 1,
    "NOR3": lambda a, b, c: 0 if (a | b | c) else 1,
}


def enumerate_higher_order():
    """Yield 4-node forms: S (node 1) mediates parties W(0), C(2), D(3); each party reads the
    mediator only, or the mediator or the other two parties. 6 mediators x 2^3 = 48."""
    for mname, mfn in TERN.items():
        for bits in range(8):
            w_back, c_back, d_back = (bits >> 0) & 1, (bits >> 1) & 1, (bits >> 2) & 1

            def party(read_others, idx_self):
                others = [p for p in (0, 2, 3) if p != idx_self]
                if read_others:
                    return lambda x, o=others: x[1] | x[o[0]] | x[o[1]]
                return lambda x: x[1]

            rules = [
                party(w_back, 0),
                lambda x, f=mfn: f(x[0], x[2], x[3]),     # S' = mediator(W, C, D)
                party(c_back, 2),
                party(d_back, 3),
            ]
            parity = int(mname == "XOR3")
            label = f"HO:S={mname},back=({w_back}{c_back}{d_back})"
            yield ("higher_order", label, rules, 4, mname, parity)


# ----- driver -------------------------------------------------------------------------

FIELDS = ["id", "kind", "n", "label", "max_phi", "mean_phi", "n_reachable",
          "edges", "mediator_depends_both", "strict_mediation", "back_channel",
          "parity_present", "mediator_fn"]


def run(smoke=False):
    out_dir = os.path.join(_HERE, "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "catalog_smoke.csv" if smoke else "catalog.csv")

    sources = list(enumerate_triads()) + list(enumerate_higher_order())
    if smoke:
        sources = sources[:40] + sources[-12:]

    seen_tpm = set()
    n_written = 0
    with open(out_path, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for (kind, label, rules, n, mtag, parity) in sources:
            tpm = tpm_from_rules(rules, n)
            key = tpm.tobytes()
            if key in seen_tpm:
                continue
            seen_tpm.add(key)
            cm = cm_from_rules(rules, n)
            rows = phi_over_states(tpm, cm, n)
            phis = [p for _, p in rows]
            max_phi = float(np.max(phis)) if phis else 0.0
            mean_phi = float(np.mean(phis)) if phis else 0.0

            if n == 3:
                feat = triad_features(cm, mtag if isinstance(mtag, int) else 8)
            else:
                s_in = int(cm[0, 1] + cm[2, 1] + cm[3, 1])
                parties = [0, 2, 3]
                strict = all(
                    cm[1, p] and sum(cm[q, p] for q in parties if q != p) == 0
                    for p in parties
                )
                back = any(sum(cm[q, p] for q in parties if q != p) > 0 for p in parties)
                feat = {"edges": int(cm.sum()), "mediator_depends_both": int(s_in >= 2),
                        "strict_mediation": int(bool(strict)), "back_channel": int(bool(back)),
                        "mediator_fn": str(mtag)}

            writer.writerow({
                "id": n_written, "kind": kind, "n": n, "label": label,
                "max_phi": round(max_phi, 6), "mean_phi": round(mean_phi, 6),
                "n_reachable": len(rows), "parity_present": parity, **feat,
            })
            fh.flush()
            n_written += 1
            if n_written % 250 == 0:
                print(f"  [{n_written} distinct forms] last: {label} maxΦ={max_phi:.4f}",
                      flush=True)

    print(f"\nDONE. {n_written} distinct forms -> {out_path}")
    return out_path


if __name__ == "__main__":
    smoke = "--smoke" in sys.argv
    print("=" * 78)
    print("PAPER 3 rebuild — enumerating the W–S–C model-family catalog (exact IIT-4.0 Φ)")
    print("  16^3 = 4096 triad wirings + 48 higher-order forms" if not smoke else "  [SMOKE]")
    print("=" * 78)
    run(smoke=smoke)
