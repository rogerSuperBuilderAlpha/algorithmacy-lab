"""Paper 3 — the catalog of the W–S–C model family.

Instead of hand-picking a handful of organizations, we enumerate the COMPLETE space of
three-node Boolean transition systems in our Worker–System–Counterpart modeling vocabulary —
the *model family* — and compute exact IIT-4.0 Φ for every one, then add a higher-order
(four-node) family. NOTE on interpretation: most of these wirings are NOT recognizable
coordination forms; they are simply every Boolean way three nodes can depend on one another.
The enumeration is a coverage / null check, not a census of real coordination. Its value is
twofold: it lets us characterize what the model does across its whole domain (which structural
features move Φ; how the score is distributed), and it shows that the hand-modeled
organizations in typology_phi.py are not cherry-picked but fall on populated, structurally
meaningful bands of the full model family. Claims here are about the model family, not about
"the space of coordination."

THE GRAMMAR.
  - Node order 0=W (worker), 1=S (system/mediator), 2=C (counterpart), 3=D (4th party).
  - A wiring in the model family = how each node's NEXT value depends on the others NOW.
  - Triad (n=3): every node is some Boolean function of the OTHER TWO. There are exactly 16
    Boolean functions of two inputs, so the complete space is 16^3 = 4096 wirings:
        W' = f_W(S, C),   S' = f_S(W, C),   C' = f_C(W, S).
    We enumerate all of them (dedup by identical transition matrix) — no curation.
  - Higher-order (n=4): a determination binding more than three parties. The mediator S
    aggregates the three parties (W, C, D) with one of a curated set of symmetric functions
    (AND/OR/XOR/MAJ/NAND/NOR); each party either reads the mediator only ("M") or the
    mediator OR the other two parties ("M|rest"). 6 mediators x 2^3 party-modes = 48 forms.

WHAT WE RECORD per form: exact max/mean system Φ over reachable states (max is the form's
placement, matching typology_phi.py), and structural features computed from the inferred
connectivity — so the analysis can ask what drives the score:
  edges, mediator_depends_both, strict_mediation, back_channel, parity_present, mediator_fn.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/catalog.py [--smoke]
Output: results/catalog.csv (written incrementally; safe to interrupt).
"""

import csv
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_P2 = os.path.abspath(os.path.join(_HERE, "..", "paper2_construct"))
if _P2 not in sys.path:
    sys.path.insert(0, _P2)

import numpy as np

from phi_instrument import tpm_from_rules, cm_from_rules, system_phi_over_states

# ---------------------------------------------------------------------------------------
# Boolean function basis (2-input), labelled.  tt = 4-bit truth table; value at (a,b) is
# bit ((a<<1)|b) of tt.  These 16 functions ARE the complete space of pairwise dependence.
# ---------------------------------------------------------------------------------------

def _bin(tt):
    return lambda a, b, tt=tt: (tt >> ((a << 1) | b)) & 1

BIN = {tt: _bin(tt) for tt in range(16)}

BIN_LABEL = {
    0: "FALSE", 1: "NOR", 2: "W&~C", 3: "~C", 4: "~W&C", 5: "~W", 6: "XOR", 7: "NAND",
    8: "AND", 9: "XNOR", 10: "copyA", 11: "A|~B", 12: "copyB", 13: "~A|B", 14: "OR", 15: "TRUE",
}
# Functions that genuinely depend on BOTH inputs (a real two-party determination):
DEPENDS_BOTH = {1, 2, 4, 6, 7, 8, 9, 11, 13, 14}
PARITY = {6, 9}  # XOR / XNOR couplings


# ---------------------------------------------------------------------------------------
# Feature extraction from the inferred connectivity matrix (cm[i,j]=1 iff j depends on i).
# ---------------------------------------------------------------------------------------

def triad_features(cm, fS):
    w_reads_s = cm[1, 0]; w_reads_c = cm[2, 0]
    s_reads_w = cm[0, 1]; s_reads_c = cm[2, 1]
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


# ---------------------------------------------------------------------------------------
# Enumeration
# ---------------------------------------------------------------------------------------

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


# 3-input symmetric mediator functions over (a, b, c):
TERN = {
    "AND3": lambda a, b, c: a & b & c,
    "OR3": lambda a, b, c: a | b | c,
    "XOR3": lambda a, b, c: a ^ b ^ c,
    "MAJ3": lambda a, b, c: 1 if (a + b + c) >= 2 else 0,
    "NAND3": lambda a, b, c: 0 if (a & b & c) else 1,
    "NOR3": lambda a, b, c: 0 if (a | b | c) else 1,
}


def enumerate_higher_order():
    """Yield 4-node forms: S=node1 mediates parties W(0), C(2), D(3); each party reads the
    mediator only ('M') or mediator-OR-the-other-two ('M|rest'). 6 mediators x 8 = 48."""
    for mname, mfn in TERN.items():
        for bits in range(8):  # 3 party modes: bit set => that party also reads the others
            w_back, c_back, d_back = (bits >> 0) & 1, (bits >> 1) & 1, (bits >> 2) & 1

            def party(read_others, idx_self):
                # a party at position `idx_self` reads S (node1); if read_others, also the
                # other two parties (positions in {0,2,3} minus self).
                others = [p for p in (0, 2, 3) if p != idx_self]
                if read_others:
                    return lambda x, o=others: x[1] | x[o[0]] | x[o[1]]
                return lambda x: x[1]

            rules = [
                party(w_back, 0),                                    # W'
                lambda x, f=mfn: f(x[0], x[2], x[3]),                # S' = mediator(W,C,D)
                party(c_back, 2),                                    # C'
                party(d_back, 3),                                    # D'
            ]
            parity = int(mname == "XOR3")
            label = f"HO:S={mname},back=({w_back}{c_back}{d_back})"
            yield ("higher_order", label, rules, 4, mname, parity)


# ---------------------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------------------

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
        for idx, (kind, label, rules, n, mtag, parity) in enumerate(sources):
            tpm = tpm_from_rules(rules, n)
            key = tpm.tobytes()
            if key in seen_tpm:
                continue
            seen_tpm.add(key)
            cm = cm_from_rules(rules, n)
            results = system_phi_over_states(tpm, cm, n)
            phis = [p for _, p in results]
            max_phi = float(np.max(phis)) if phis else 0.0
            mean_phi = float(np.mean(phis)) if phis else 0.0

            if n == 3:
                feat = triad_features(cm, mtag if isinstance(mtag, int) else 8)
            else:  # higher order: derive comparable features from cm
                s_in = int(cm[0, 1] + cm[2, 1] + cm[3, 1])  # how many parties S reads
                parties = [0, 2, 3]
                strict = all(
                    cm[1, p] and sum(cm[q, p] for q in parties if q != p) == 0
                    for p in parties
                )
                back = any(sum(cm[q, p] for q in parties if q != p) > 0 for p in parties)
                feat = {
                    "edges": int(cm.sum()),
                    "mediator_depends_both": int(s_in >= 2),
                    "strict_mediation": int(bool(strict)),
                    "back_channel": int(bool(back)),
                    "mediator_fn": str(mtag),
                }

            row = {
                "id": n_written, "kind": kind, "n": n, "label": label,
                "max_phi": round(max_phi, 6), "mean_phi": round(mean_phi, 6),
                "n_reachable": len(results), "parity_present": parity, **feat,
            }
            writer.writerow(row)
            fh.flush()
            n_written += 1
            if n_written % 100 == 0:
                print(f"  [{n_written} distinct forms] last: {label}  maxΦ={max_phi:.4f}",
                      flush=True)

    print(f"\nDONE. {n_written} distinct coordination forms -> {out_path}")
    return out_path


if __name__ == "__main__":
    smoke = "--smoke" in sys.argv
    print("=" * 78)
    print("PAPER 3 — enumerating the coordination-form catalog (exact IIT-4.0 Φ)")
    print("  16^3 = 4096 triad wirings + 48 higher-order forms" if not smoke else "  [SMOKE]")
    print("=" * 78)
    run(smoke=smoke)
