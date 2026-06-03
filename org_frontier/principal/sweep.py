"""Principal-coupling sweep: precisely when does P join the irreducible core?

Finding #8 used four hand-built forms. This makes it a population result by sweeping the principal's
coupling systematically over the W–S–C triad (W' = S, C' = S):

  - S_reads_P in {0, 1}: whether the determination reads P (S' = W ∧ C, or W ∧ C ∧ P).
  - R subset of {W, S, C}: what P reads, with P' = AND over R (R empty -> P static, P' = P).

8 read-sets x 2 gating = 16 forms. For each, compute the major complex (max Φ over reachable
states) and record whether P is in it. The hypothesis from the named forms: P joins the core iff
S reads P (upstream) AND P reads the core (downstream, i.e. R contains S).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.principal.sweep
"""

import csv
import itertools
import os

import pyphi

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from .run import major_complex
from . import forms as pf

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
_RESULTS = os.path.join(os.path.dirname(__file__), "results")

# Indices: 0=W, 1=S, 2=C, 3=P
READABLE = [0, 1, 2]  # P may read any of W, S, C
NAME = {0: "W", 1: "S", 2: "C"}


def build(s_reads_p, read_set):
    """Triad W'=S, C'=S; S' = W&C (& P if s_reads_p); P' = AND over read_set (static if empty)."""
    def s_rule(x, g=s_reads_p):
        base = x[0] & x[2]
        return base & x[3] if g else base

    def p_rule(x, R=tuple(read_set)):
        if not R:
            return x[3]                      # static self-loop
        out = 1
        for i in R:
            out &= x[i]
        return out

    return [lambda x: x[1], s_rule, lambda x: x[1], p_rule]


def main():
    os.makedirs(_RESULTS, exist_ok=True)
    rows = []
    print("PRINCIPAL-COUPLING SWEEP — when does P join the irreducible core?")
    print("=" * 96)
    print(f"  {'S_reads_P':<10}{'P_reads':<12}{'major complex':<20}{'core Φ':<8}{'P in core'}")
    print("-" * 96)
    for s_reads_p in (0, 1):
        for k in range(len(READABLE) + 1):
            for combo in itertools.combinations(READABLE, k):
                rules = build(s_reads_p, combo)
                core, phi = major_complex(rules)
                p_in = core is not None and "P" in core
                reads = "".join(NAME[i] for i in combo) or "(static)"
                rows.append({"s_reads_p": s_reads_p, "p_reads": reads,
                             "major_complex": "".join(core) if core else "",
                             "core_phi": f"{phi:.4f}", "p_in_core": p_in})
                print(f"  {s_reads_p:<10}{reads:<12}{str(core):<20}{phi:<8.3f}{p_in}")
    path = os.path.join(_RESULTS, "sweep.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"\nWrote {path}")

    in_core = [r for r in rows if r["p_in_core"]]
    gated = [r for r in rows if r["s_reads_p"] == 1]
    gated_active = [r for r in gated if r["p_reads"] != "(static)"]
    contracted = [r for r in in_core if "W" not in r["major_complex"] or "C" not in r["major_complex"]]
    print("=" * 96)
    print(f"  P joins the core in {len(in_core)}/{len(rows)} forms.")
    print(f"  every P-in-core form has S_reads_P=1 (gating): {all(r['s_reads_p']==1 for r in in_core)}")
    print(f"  every P-in-core form has P reading >=1 party (not static): "
          f"{all(r['p_reads']!='(static)' for r in in_core)}")
    print(f"  of the gated forms, P joins iff P is not static: "
          f"{sorted(r['p_in_core'] for r in gated_active)==[True]*len(gated_active)}")
    print("  -> P joins the core iff coupling is BIDIRECTIONAL: S reads P (gating) AND P reads")
    print("     at least one party. The party P reads need not be S. Pure ownership, gating-only,")
    print("     and response-only all leave P outside.")
    print(f"  WRINKLE: in {len(contracted)} P-in-core forms the core CONTRACTS (a worker/counterpart")
    print("     drops out) — a heavily-coupled principal can hollow the core toward {S,P}.")
    print("=" * 96)


if __name__ == "__main__":
    main()
