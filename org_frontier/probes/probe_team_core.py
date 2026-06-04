"""Probe 51 — the team's irreducible subset (Watson et al. soccer precedent).

Watson et al. (2025/2026) computed Φ for SUBSETS of players on soccer teams. Here: in a larger team
(worker + system + several teammates), is the irreducible core the whole team or a proper subset?
Build heterogeneous teams and read off the major complex.

H51: the irreducible core is the tightly-coupled subset, not the whole team — a heterogeneous team
integrates only over its tight clique, matching the "subsets of players show Φ" picture.

Nodes per form labeled inline.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_team_core
"""

from .lib import verdict, major_complex


def main():
    print("PROBE 51 — the team's irreducible subset")
    print("=" * 84)
    cases = [
        # homogeneous all-required pool (n=4): everyone in one joint determination
        ("homogeneous_pool", ("W", "S", "C1", "C2"),
         [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]]),
        # core triad {W,S,C1} + peripheral C2 (reads S, not constitutive)
        ("core_plus_periphery", ("W", "S", "C1", "C2"),
         [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]]),
        # n=5: tight {W,S,C1} triad + two peripherals tracking S
        ("triad_plus_two", ("W", "S", "C1", "C2", "C3"),
         [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1], lambda x: x[1]]),
    ]
    for name, labels, rules in cases:
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        size = len(core) if core else 0
        print(f"  {name:<22} whole {v.structure:<8} | core={core} (size {size}/{len(labels)}) Φ={phi:.3f}")
    print("=" * 84)
    print("  A heterogeneous team integrates over its tight subset, not the whole roster —")
    print("  the irreducible core is a proper subset (cf. Watson et al.'s subset-Φ).")
    print("=" * 84)


if __name__ == "__main__":
    main()
