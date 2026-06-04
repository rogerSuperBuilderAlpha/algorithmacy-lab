"""Probe 74 (#30) — is there a regime where the platform+owner core is generic?

Question: Probe 37 / the principal sweep found the core can contract to {S,P}, the platform and its
owner, at the extreme. How often does that happen across the principal's coupling? Hypothesis: as the
principal reads more parties and gates the commit, {S,P} becomes the core ever more often. Method:
sweep whether S gates P and which parties P reads, over the worker–system–counterpart–principal form,
and rate how often the major complex is exactly {S,P} (both human parties ejected).

Nodes: 0=W, 1=S, 2=C, 3=P.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_principal_regime
"""

import itertools

from .lib import major_complex

LABELS = ("W", "S", "C", "P")
READS = [0, 1, 2]  # P may read W, S, C


def build(s_gates_p, p_reads):
    def s_rule(x):
        base = x[0] & x[2]
        return (base & x[3]) if s_gates_p else base

    def p_rule(x, R=tuple(p_reads)):
        if not R:
            return x[3]
        out = 1
        for i in R:
            out &= x[i]
        return out

    return [lambda x: x[1], s_rule, lambda x: x[1], p_rule]


def main():
    sp = total = 0
    examples = []
    for s_gates_p in (0, 1):
        for k in range(len(READS) + 1):
            for combo in itertools.combinations(READS, k):
                core, _ = major_complex(build(s_gates_p, combo), LABELS)
                total += 1
                if core is not None and set(core) == {"S", "P"}:
                    sp += 1
                    examples.append((s_gates_p, "".join("WSC"[i] for i in combo) or "static"))
    print("PROBE 74 (#30) — frequency of the {S,P} platform-and-owner core")
    print("=" * 72)
    print(f"  principal-coupling forms swept: {total}")
    print(f"  core == {{S,P}} (both parties ejected): {sp} ({100*sp/total:.0f}%)")
    if examples:
        print(f"  occurs when S gates P and P reads broadly, e.g. {examples[:4]}")
    print("=" * 72)
    print("  Reading: the platform-and-owner core is not generic but a high-coupling regime — it")
    print("  appears when the principal both gates the commit and reads the parties widely.")
    print("=" * 72)


if __name__ == "__main__":
    main()
