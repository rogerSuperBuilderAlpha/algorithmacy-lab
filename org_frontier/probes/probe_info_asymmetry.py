"""Probe 77 (#34) — observability asymmetry and the triad.

Question: the triad has the platform observing both parties while each party sees only the platform.
Does that observability asymmetry have a distinct structural signature? Hypothesis: the triad requires
the asymmetry — the system reads both, the parties read only the system; giving the parties direct
sight of each other (symmetric observability) collapses it. Method: over a grid of observability
choices (does S read W; does S read C; is there a direct W↔C channel), classify each.

Nodes: 0=W, 1=S, 2=C. Determination S' = (inputs S reads); parties track S, plus any direct channel.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_info_asymmetry
"""

from .lib import verdict


def build(s_reads_w, s_reads_c, direct_wc):
    def s_rule(x):
        if s_reads_w and s_reads_c:
            return x[0] & x[2]
        if s_reads_w:
            return x[0]
        if s_reads_c:
            return x[2]
        return x[1]
    # parties track S; with a direct channel they also read each other
    w_rule = (lambda x: x[1] | x[2]) if direct_wc else (lambda x: x[1])
    c_rule = (lambda x: x[1] | x[0]) if direct_wc else (lambda x: x[1])
    return [w_rule, s_rule, c_rule]


def main():
    print("PROBE 77 (#34) — observability asymmetry")
    print("=" * 76)
    print(f"  {'S reads W':<10}{'S reads C':<10}{'W↔C direct':<12}{'verdict'}")
    for sw in (1, 0):
        for sc in (1, 0):
            for d in (0, 1):
                v = verdict(build(sw, sc, d), ("W", "S", "C"))
                print(f"  {sw:<10}{sc:<10}{d:<12}{v.structure}  Φ={v.max_phi:.2f}")
    print("=" * 76)
    print("  Reading: the triad sits at S-reads-both / no-direct-channel (platform omniscient, parties")
    print("  partial). Opening a direct W↔C channel — symmetric observability — collapses it, and a")
    print("  platform that reads only one party is dyadic. The asymmetry is the structural condition.")
    print("=" * 76)


if __name__ == "__main__":
    main()
