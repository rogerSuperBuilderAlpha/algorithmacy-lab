"""Probe 20 — AI-mediated communication (AI inside the worker's message production).

Discriminant neighbor: AI-MC places an AI inside the worker's own message production — it reshapes
what the worker sends, but the worker and counterpart still coordinate directly; no third party
commits a determination over both. The dissertation treats AI-MC as dyadic. Test the structure.

H20: AI-MC forms (an assist node A on the worker's side; W and C coordinate directly through A) are
NOT triadic in the algorithmacy sense — the AI is part of the worker, not a mediating third party.
Honest either way: if the W→A→C loop is irreducible, that is a real tension to report.

Nodes: 0=W, 1=A (AI assist), 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_aimc
"""

from .lib import verdict, major_complex

LABELS = ("W", "A", "C")

FORMS = {
    # AI rewrites the worker's message; C receives the AI-shaped signal; W responds to C.
    "aimc_rewrite":  [lambda x: x[2], lambda x: x[0], lambda x: x[1]],
    # AI blends worker intent and context, still on the worker's side.
    "aimc_blend":    [lambda x: x[2], lambda x: x[0] | x[2], lambda x: x[1]],
    # contrast: an external system that commits a joint determination over W and C (algorithmacy)
    "algo_external": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
}


def main():
    print("PROBE 20 — AI-MC (AI in the worker's production) vs algorithmacy")
    print("=" * 78)
    for k, r in FORMS.items():
        v = verdict(r, LABELS)
        core, phi = major_complex(r, LABELS)
        print(f"  {k:<16} {v.structure:<8} Φ={v.max_phi:.3f}  core={core}")
    print("=" * 78)
    print("  (W,A,C loop irreducible? -> a structural tension worth noting if triadic)")


if __name__ == "__main__":
    main()
