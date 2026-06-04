"""Probe 66 (#33) — does a larger counterpart coalition always win vs the principal?

Question: Probe 37 found a 2-counterpart coalition relocates the core to {C1,C2}, ejecting an active
principal. Does this hold as the coalition grows? Hypothesis: a larger coalition still becomes the
core, displacing the principal. Method: build coalition-of-k counterparts (each reads S or the other
counterparts) with an active gating+monitoring principal, for k=2 (n=5) and k=3 (n=6), and read the
major complex.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_coalition_size
"""

from .lib import verdict, major_complex


def coalition_form(k):
    # nodes: 0=W, 1=S, 2..k+1 = C1..Ck (coalition), k+2 = P
    n = k + 3
    cidx = list(range(2, 2 + k))
    pidx = k + 2

    def s_rule(x):
        r = x[0] & x[pidx]            # worker and principal gate
        for c in cidx:
            r &= x[c]                 # all coalition counterparts required
        return r

    rules = [None] * n
    rules[0] = lambda x: x[1]                  # W tracks S
    rules[1] = s_rule                          # S = W & all C & P
    rules[pidx] = lambda x: x[1]               # P monitors S
    for c in cidx:                             # each counterpart reads S OR any other counterpart
        others = [o for o in cidx if o != c]
        rules[c] = (lambda x, c=c, others=tuple(others): x[1] | (any(x[o] for o in others) if others else 0)) \
            if others else (lambda x, c=c: x[1])
        rules[c] = (lambda x, others=tuple(others): int(bool(x[1]) or any(x[o] for o in others)))
    labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, k + 1)] + ["P"])
    return rules, labels


def main():
    print("PROBE 66 (#33) — coalition size vs the principal")
    print("=" * 80)
    for k in (2, 3):
        rules, labels = coalition_form(k)
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        p_in = core is not None and "P" in core
        coalition = {f"C{i}" for i in range(1, k + 1)}
        core_is_coalition = core is not None and set(core) == coalition
        print(f"  k={k} (n={k+3})  whole {v.structure:<8}  core={core} Φ={phi:.3f}  "
              f"P in core: {p_in}  core==coalition: {core_is_coalition}")
    print("=" * 80)
    print("  Reading: if the core is the counterpart coalition at every size, solidarity dominates")
    print("  principal control regardless of coalition size.")
    print("=" * 80)


if __name__ == "__main__":
    main()
