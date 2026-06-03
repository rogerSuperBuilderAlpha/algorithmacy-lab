"""Probe 29 — the variance puzzle (equifinality).

The dissertation's motivating observation: equivalently-positioned workers get divergent outcomes
through identical systems. Operationalize: hold the SYSTEM's determination fixed (S' = W ∧ C, C' = S)
and vary the WORKER's policy (how W responds). Measure two things per policy:
  - the structural verdict + Φ (a property of the form),
  - a coordination-success rate = mean over initial states of the fraction of the attractor in which
    the system commits a match (S = 1).

H29: among worker policies that keep the worker live to the determination the form stays triadic
(Φ ≈ constant), yet the success rate varies widely — same triadic form, divergent outcomes. The
structure demands algorithmacy; who succeeds depends on the worker's competence within it.

Nodes: 0=W, 1=S, 2=C.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_variance
"""

from .lib import verdict

LABELS = ("W", "S", "C")

# Same system (S'=W∧C, C'=S); different worker policies.
POLICIES = {
    "reactive (W'=S)":      lambda x: x[1],
    "persistent (W'=S∨W)":  lambda x: x[1] | x[0],
    "eager (W'=1)":         lambda x: 1,
    "withdrawn (W'=0)":     lambda x: 0,
    "contrarian (W'=¬S)":   lambda x: 1 - x[1],
}


def success_rate(rules, n=3):
    """Mean over initial states of the attractor fraction with S (bit 1) = 1."""
    def succ(s):
        b = tuple((s >> i) & 1 for i in range(n))
        return sum(int(rules[j](b)) << j for j in range(n))
    rates = []
    for s0 in range(2 ** n):
        seen, s = [], s0
        while s not in seen:
            seen.append(s); s = succ(s)
        cycle = seen[seen.index(s):]
        rates.append(sum((cs >> 1) & 1 for cs in cycle) / len(cycle))
    return sum(rates) / len(rates)


def main():
    print("PROBE 29 — the variance puzzle (same system, different worker policy)")
    print("=" * 78)
    print(f"  {'worker policy':<22}{'verdict':<9}{'Φ':<7}{'success rate'}")
    phis, succs = [], []
    for name, wpol in POLICIES.items():
        rules = [wpol, lambda x: x[0] & x[2], lambda x: x[1]]
        v = verdict(rules, LABELS)
        sr = success_rate(rules)
        phis.append(v.max_phi); succs.append(sr)
        print(f"  {name:<22}{v.structure:<9}{v.max_phi:<7.3f}{sr:.2f}")
    print("=" * 78)
    print(f"  Φ range across policies: {min(phis):.2f}–{max(phis):.2f} ; "
          f"success range: {min(succs):.2f}–{max(succs):.2f}")
    print("  -> identical system, divergent outcomes = the variance puzzle, structurally.")
    print("=" * 78)


if __name__ == "__main__":
    main()
