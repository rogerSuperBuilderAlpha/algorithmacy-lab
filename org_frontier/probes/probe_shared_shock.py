"""Probe 61 (#9) — a shared exogenous shock.

Question: does noise that is correlated across the parties, modeled as a shared exogenous shock both
read, change the verdict rather than just the magnitude (as independent noise did in Probe 27)?
Hypothesis: a common shock that couples the parties outside the determination acts like a back-channel
and can change the structure. Method: add a shock node N (a slowly-flipping common source) that the
worker and counterpart both read alongside the system, and compare with the no-shock triad.

Nodes: 0=W, 1=S, 2=C, 3=N (shared shock).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_shared_shock
"""

from .lib import verdict, major_complex

LABELS = ("W", "S", "C", "N")

FORMS = {
    # baseline triad + idle shock (N self-loop, unread): control
    "no_shock":      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
    # shared shock: W and C each read S AND the common shock N
    "shared_shock":  [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[3]],
    # shock also feeds the determination (S reads N too)
    "shock_in_commit": [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[3]],
}


def main():
    print("PROBE 61 (#9) — a shared exogenous shock")
    print("=" * 80)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<18} whole {v.structure:<8} Φ={v.max_phi:.3f}   core={core} Φ={phi:.3f}")
    print("=" * 80)
    print("  Reading: a common shock the parties both read, outside the determination, is the")
    print("  correlated-noise analogue; whether it joins the core or just perturbs the triad says")
    print("  whether structured noise changes the verdict or only the magnitude.")
    print("=" * 80)


if __name__ == "__main__":
    main()
